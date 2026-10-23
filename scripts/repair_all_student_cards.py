import urllib.request
import json
import re

API_KEY = "AIzaSyBNsrBL1xRErsuOHgvI7xNs15cai-auoSE"
PROJECT_ID = "japanese-learning-e8a53"

def to_firestore_value(val):
    if isinstance(val, str):
        return {"stringValue": val}
    elif isinstance(val, bool):
        return {"booleanValue": val}
    elif isinstance(val, (int, float)):
        return {"integerValue": str(val)}
    elif isinstance(val, list):
        return {"arrayValue": {"values": [to_firestore_value(x) for x in val]}}
    elif isinstance(val, dict):
        return {"mapValue": {"fields": {k: to_firestore_value(v) for k, v in val.items()}}}
    return {"nullValue": None}

def get_auth_token(student_id, passcode):
    auth_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
    auth_data = json.dumps({
        "email": f"{student_id}@haku.local",
        "password": f"haku_{passcode}_sec",
        "returnSecureToken": True
    }).encode("utf-8")
    req = urllib.request.Request(auth_url, data=auth_data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        token_data = json.loads(resp.read().decode("utf-8"))
    return token_data["idToken"]

# =========================================================================
# 1. Student 0003 (두성, Korean) - Perfect 35 Custom Cards
# =========================================================================
student_0003_cards = [
    {
        "id": "card_1791553287804_n5uz22",
        "word": "趣味",
        "reading": "しゅみ",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "趣味",
            "ko": "취미 (hobby, pastime)",
            "en": "hobby, pastime"
        },
        "example": {
            "ja": "<ruby>私<rt>わたし</rt></ruby>の<ruby>趣味<rt>しゅみ</rt></ruby>は<ruby>映画鑑賞<rt>えいがかんしょう</rt></ruby>です。",
            "ko": "제 취미는 영화 감상이에요. (My hobby is watching movies.)",
            "en": "My hobby is watching movies."
        }
    },
    {
        "id": "card_1791553287808_k6tp79",
        "word": "祝日",
        "reading": "しゅくじつ",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "祝日",
            "ko": "공휴일, 축일 (national holiday, public holiday)",
            "en": "national holiday, public holiday"
        },
        "example": {
            "ja": "<ruby>明日<rt>あした</rt></ruby>は<ruby>祝日<rt>しゅくじつ</rt></ruby>なので、<ruby>会社<rt>かいしゃ</rt></ruby>は<ruby>休<rt>やす</rt></ruby>みです。",
            "ko": "내일은 공휴일이라서 회사는 쉽니다. (Tomorrow is a public holiday, so the company is closed.)",
            "en": "Tomorrow is a public holiday, so the company is closed."
        }
    },
    {
        "id": "card_1791553287808_0mmdmr",
        "word": "場所",
        "reading": "ばしょ",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "場所",
            "ko": "장소, 곳 (place, location)",
            "en": "place, location"
        },
        "example": {
            "ja": "<ruby>次<rt>つぎ</rt></ruby>の<ruby>会議<rt>かいぎ</rt></ruby>の<ruby>場所<rt>ばしょ</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えてください。",
            "ko": "다음 회의 장소를 알려주세요. (Please tell me the location of the next meeting.)",
            "en": "Please tell me the location of the next meeting."
        }
    },
    {
        "id": "card_1791553287808_kvgfxp",
        "word": "奢る",
        "reading": "おごる",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "奢る",
            "ko": "(한턱) 쏘다, 사주다 (to treat someone to food/drinks)",
            "en": "to treat someone to food/drinks"
        },
        "example": {
            "ja": "<ruby>今日<rt>きょう</rt></ruby>は<ruby>私<rt>わたし</rt></ruby>が<ruby>昼<rt>ひる</rt></ruby>ご飯を<ruby>奢<rt>おご</rt></ruby>ります。",
            "ko": "오늘은 제가 점심을 살게요. (I will treat you to lunch today.)",
            "en": "I will treat you to lunch today."
        }
    },
    {
        "id": "card_1791553287808_ihzqfm",
        "word": "挨拶",
        "reading": "あいさつ",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "挨拶",
            "ko": "인사 (greeting, salutation)",
            "en": "greeting, salutation"
        },
        "example": {
            "ja": "<ruby>朝<rt>あさ</rt></ruby>は<ruby>気持<rt>きも</rt></ruby>ちよく<ruby>挨拶<rt>あいさつ</rt></ruby>をしましょう。",
            "ko": "아침에는 기분 좋게 인사를 합시다. (Let's greet each other pleasantly in the morning.)",
            "en": "Let's greet each other pleasantly in the morning."
        }
    },
    {
        "id": "card_1791553287808_d0zy79",
        "word": "有給",
        "reading": "ゆうきゅう",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "有給",
            "ko": "연차, 유급 휴가 (paid leave, paid time off)",
            "en": "paid leave, paid time off"
        },
        "example": {
            "ja": "<ruby>来週<rt>らいしゅう</rt></ruby>の<ruby>金曜日<rt>きんようび</rt></ruby>に<ruby>有給<rt>ゆうきゅう</rt></ruby>を<ruby>取<rt>と</rt></ruby>りました。",
            "ko": "다음 주 금요일에 연차를 냈어요. (I took paid leave next Friday.)",
            "en": "I took paid leave next Friday."
        }
    },
    {
        "id": "card_1791553287809_ispxhb",
        "word": "検査",
        "reading": "けんさ",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "検査",
            "ko": "검사 (inspection, examination, test)",
            "en": "inspection, examination, test"
        },
        "example": {
            "ja": "<ruby>病院<rt>びょういん</rt></ruby>で<ruby>健康<rt>けんこう</rt></ruby>の<ruby>検査<rt>けんさ</rt></ruby>を<ruby>受<rt>う</rt></ruby>けました。",
            "ko": "병원에서 건강 검사를 받았어요. (I had a health checkup at the hospital.)",
            "en": "I had a health checkup at the hospital."
        }
    },
    {
        "id": "card_1791553287809_yezsq2",
        "word": "結果",
        "reading": "けっか",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "結果",
            "ko": "결과 (result, outcome)",
            "en": "result, outcome"
        },
        "example": {
            "ja": "<ruby>試験<rt>しけん</rt></ruby>の<ruby>結果<rt>けっか</rt></ruby>が<ruby>出<rt>で</rt></ruby>るのを<ruby>待<rt>ま</rt></ruby>っています。",
            "ko": "시험 결과가 나오기를 기다리고 있어요. (I am waiting for the test results to come out.)",
            "en": "I am waiting for the test results to come out."
        }
    },
    {
        "id": "card_1791553287809_xlx0ba",
        "word": "肝臓",
        "reading": "かんぞう",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "肝臓",
            "ko": "간, 간장 (liver)",
            "en": "liver"
        },
        "example": {
            "ja": "お<ruby>酒<rt>さけ</rt></ruby>を<ruby>飲<rt>の</rt></ruby>みすぎると、<ruby>肝臓<rt>かんぞう</rt></ruby>を<ruby>悪<rt>わる</rt></ruby>くします。",
            "ko": "술을 너무 많이 마시면 간을 상하게 해요. (Drinking too much alcohol damages your liver.)",
            "en": "Drinking too much alcohol damages your liver."
        }
    },
    {
        "id": "card_1791553287809_psc92k",
        "word": "長い",
        "reading": "ながい",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "長い",
            "ko": "길다, 오랜 (long)",
            "en": "long"
        },
        "example": {
            "ja": "この<ruby>道<rt>みち</rt></ruby>はとても<ruby>長<rt>なが</rt></ruby>いです。",
            "ko": "이 길은 매우 길어요. (This road is very long.)",
            "en": "This road is very long."
        }
    },
    {
        "id": "card_1791553287809_4g5xuj",
        "word": "無視する",
        "reading": "むしする",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "無視する",
            "ko": "무시하다 (to ignore, to disregard)",
            "en": "to ignore, to disregard"
        },
        "example": {
            "ja": "<ruby>人<rt>ひと</rt></ruby>の<ruby>話<rt>はなし</rt></ruby>を<ruby>無視<rt>むし</rt></ruby>してはいけません。",
            "ko": "다른 사람의 말을 무시하면 안 돼요. (You must not ignore what other people say.)",
            "en": "You must not ignore what other people say."
        }
    },
    {
        "id": "card_1791553287809_pkxumu",
        "word": "年上",
        "reading": "としうえ",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "年上",
            "ko": "연상, 손위 (older, senior)",
            "en": "older, senior"
        },
        "example": {
            "ja": "<ruby>彼女<rt>かのじょ</rt></ruby>は<ruby>私<rt>わたし</rt></ruby>より2<ruby>歳<rt>さい</rt></ruby><ruby>年上<rt>としうえ</rt></ruby>です。",
            "ko": "그녀는 나보다 두 살 연상이에요. (She is two years older than me.)",
            "en": "She is two years older than me."
        }
    },
    {
        "id": "card_1791553287809_zszwo5",
        "word": "年寄り",
        "reading": "としより",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "年寄り",
            "ko": "노인, 어르신 (elderly person, senior citizen)",
            "en": "elderly person, senior citizen"
        },
        "example": {
            "ja": "電車でお<ruby>年寄<rt>としよ</rt></ruby>りに<ruby>席<rt>せき</rt></ruby>を<ruby>譲<rt>ゆず</rt></ruby>りました。",
            "ko": "전철에서 어르신에게 자리를 양보했어요. (I gave up my seat to an elderly person on the train.)",
            "en": "I gave up my seat to an elderly person on the train."
        }
    },
    {
        "id": "card_1791553287809_y21jvo",
        "word": "患者",
        "reading": "かんじゃ",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "患者",
            "ko": "환자 (patient)",
            "en": "patient"
        },
        "example": {
            "ja": "<ruby>医師<rt>いし</rt></ruby>が<ruby>患者<rt>かんじゃ</rt></ruby>を<ruby>丁寧<rt>ていねい</rt></ruby>に<ruby>診察<rt>しんさつ</rt></ruby>しました。",
            "ko": "의사가 환자를 정성껏 진찰했어요. (The doctor examined the patient carefully.)",
            "en": "The doctor examined the patient carefully."
        }
    },
    {
        "id": "card_1791738031121_5de4uk__관광지",
        "word": "観光地",
        "reading": "かんこうち",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "観光地",
            "ko": "관광지, 명소 (tourist attraction, tourist spot)",
            "en": "tourist attraction, tourist spot"
        },
        "example": {
            "ja": "<ruby>京都<rt>きょうと</rt></ruby>には<ruby>有名<rt>ゆうめい</rt></ruby>な<ruby>観光地<rt>かんこうち</rt></ruby>がたくさんあります。",
            "ko": "교토에는 유명한 관광지가 많이 있어요. (Kyoto has many famous tourist spots.)",
            "en": "Kyoto has many famous tourist spots."
        }
    },
    {
        "id": "card_1791738031139_s20qye__온천",
        "word": "温泉",
        "reading": "おんせん",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "温泉",
            "ko": "온천 (hot spring, onsen)",
            "en": "hot spring, onsen"
        },
        "example": {
            "ja": "<ruby>週末<rt>しゅうまつ</rt></ruby>に<ruby>温泉<rt>おんせん</rt></ruby>に<ruby>行<rt>い</rt></ruby>ってリフレッシュしたいです。",
            "ko": "주말에 온천에 가서 기분 전환을 하고 싶어요. (I want to go to a hot spring this weekend to refresh myself.)",
            "en": "I want to go to a hot spring this weekend to refresh myself."
        }
    },
    {
        "id": "card_0003_onakagasuita",
        "word": "お腹がすきました",
        "reading": "おなかがすきました",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "お腹がすきました",
            "ko": "배가 고픕니다, 배고파요 (I am hungry)",
            "en": "I am hungry"
        },
        "example": {
            "ja": "お<ruby>腹<rt>なか</rt></ruby>がすいたので、ラーメンを<ruby>食<rt>た</rt></ruby>べに<ruby>行<rt>い</rt></ruby>きましょう。",
            "ko": "배가 고파서 라면을 먹으러 갑시다. (I am hungry, so let's go eat ramen.)",
            "en": "I am hungry, so let's go eat ramen."
        }
    },
    {
        "id": "card_0003_pekopeko",
        "word": "ペコペコ",
        "reading": "ぺこぺこ",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "ペコペコ",
            "ko": "(배가) 꼬르륵거림, 몹시 배고픔 (famished, very hungry)",
            "en": "famished, very hungry"
        },
        "example": {
            "ja": "<ruby>朝<rt>あさ</rt></ruby>から<ruby>何<rt>なに</rt></ruby>も<ruby>食<rt>た</rt></ruby>べていないので、お<ruby>腹<rt>なか</rt></ruby>がペコペコです。",
            "ko": "아침부터 아무것도 안 먹어서 배가 몹시 고파요. (I haven't eaten anything since morning, so I am starving.)",
            "en": "I haven't eaten anything since morning, so I am starving."
        }
    },
    {
        "id": "card_0003_onakagaippai",
        "word": "お腹がいっぱい",
        "reading": "おなかがいっぱい",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "お腹がいっぱい",
            "ko": "배가 부름, 배부르다 (full (after eating))",
            "en": "full (after eating)"
        },
        "example": {
            "ja": "<ruby>美味<rt>おい</rt></ruby>しいごちそうをたくさん<ruby>食<rt>た</rt></ruby>べて、お<ruby>腹<rt>なか</rt></ruby>がいっぱいです。",
            "ko": "맛있는 음식을 많이 먹어서 배가 불러요. (I ate lots of delicious food and my stomach is full.)",
            "en": "I ate lots of delicious food and my stomach is full."
        }
    },
    {
        "id": "card_0003_panpan",
        "word": "パンパン",
        "reading": "ぱんぱん",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "パンパン",
            "ko": "(배 등이) 빵빵함, 터질 듯 가득 참 (stuffed, bursting full)",
            "en": "stuffed, bursting full"
        },
        "example": {
            "ja": "バイキングで<ruby>食<rt>た</rt></ruby>べすぎて、お<ruby>腹<rt>なか</rt></ruby>がパンパンです。",
            "ko": "뷔페에서 너무 많이 먹어서 배가 빵빵해요. (I ate too much at the buffet and my stomach is stuffed.)",
            "en": "I ate too much at the buffet and my stomach is stuffed."
        }
    },
    {
        "id": "card_0003_katakori",
        "word": "肩凝り",
        "reading": "かたこり",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "肩凝り",
            "ko": "어깨 결림, 어깨 뭉침 (stiff shoulders)",
            "en": "stiff shoulders"
        },
        "example": {
            "ja": "パソコンの<ruby>使<rt>つか</rt></ruby>いすぎで、ひどい<ruby>肩凝<rt>かたこ</rt></ruby>りに<ruby>悩<rt>なや</rt></ruby>まされています。",
            "ko": "컴퓨터를 너무 많이 써서 심한 어깨 결림으로 고생하고 있어요. (I am suffering from severe stiff shoulders due to overuse of the computer.)",
            "en": "I am suffering from severe stiff shoulders due to overuse of the computer."
        }
    },
    {
        "id": "card_0003_shouyu",
        "word": "醤油",
        "reading": "しょうゆ",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "醤油",
            "ko": "간장 (soy sauce)",
            "en": "soy sauce"
        },
        "example": {
            "ja": "お<ruby>刺身<rt>さしみ</rt></ruby>に<ruby>醤油<rt>しょうゆ</rt></ruby>をちょっとつけて<ruby>食<rt>た</rt></ruby>べます。",
            "ko": "생선회에 간장을 살짝 찍어서 먹어요. (I eat sashimi by lightly dipping it in soy sauce.)",
            "en": "I eat sashimi by lightly dipping it in soy sauce."
        }
    },
    {
        "id": "card_1792513864965_2yi4kn__幼馴染",
        "word": "幼馴染",
        "reading": "おさななじみ",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "幼馴染",
            "ko": "소꿉친구, 어릴 적 친구 (childhood friend)",
            "en": "childhood friend"
        },
        "example": {
            "ja": "<ruby>彼女<rt>かのじょ</rt></ruby>とは<ruby>子供<rt>こども</rt></ruby>のころからの<ruby>幼馴染<rt>おさななじみ</rt></ruby>で、<ruby>今<rt>いま</rt></ruby>でもよく<ruby>連絡<rt>れんらく</rt></ruby>を<ruby>取<rt>と</rt></ruby>り<ruby>合<rt>あ</rt></ruby>っている。",
            "ko": "그녀와는 어릴 때부터의 소꿉친구라서 지금도 자주 연락을 주고받고 있다. (She and I have been childhood friends since we were little, and we still keep in touch often.)",
            "en": "She and I have been childhood friends since we were little, and we still keep in touch often."
        }
    },
    {
        "id": "card_1792513864974_bllc8o__ゴミ捨て場",
        "word": "ゴミ捨て場",
        "reading": "ごみすてば",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "ゴミ捨て場",
            "ko": "쓰레기장, 쓰레기 배출 장소 (garbage disposal area, trash collection point)",
            "en": "garbage disposal area, trash collection point"
        },
        "example": {
            "ja": "<ruby>指定<rt>してい</rt></ruby>された<ruby>曜日<rt>ようび</rt></ruby>の<ruby>朝<rt>あさ</rt></ruby>に、ゴミを<ruby>近所<rt>きんじょ</rt></ruby>のゴミ<ruby>捨<rt>す</rt></ruby>て<ruby>場<rt>ば</rt></ruby>へ<ruby>出<rt>だ</rt></ruby>しに<ruby>行<rt>い</rt></ruby>きます。",
            "ko": "지정된 요일 아침에 쓰레기를 동네 쓰레기장에 버리러 갑니다. (On the designated day of the week in the morning, I go to take the trash to the local garbage disposal area.)",
            "en": "On the designated day of the week in the morning, I go to take the trash to the local garbage disposal area."
        }
    },
    {
        "id": "card_1792513864982_ryguoa__職場",
        "word": "職場",
        "reading": "しょくば",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "職場",
            "ko": "직장, 일터 (workplace)",
            "en": "workplace"
        },
        "example": {
            "ja": "<ruby>新<rt>あたら</rt></ruby>しい<ruby>職場<rt>しょくば</rt></ruby>は<ruby>雰囲気<rt>ふんいき</rt></ruby>がとてもよく、<ruby>働<rt>はたら</rt></ruby>きやすいです。",
            "ko": "새로운 직장은 분위기가 매우 좋고 일하기 편합니다. (The atmosphere at the new workplace is very good, and it is easy to work there.)",
            "en": "The atmosphere at the new workplace is very good, and it is easy to work there."
        }
    },
    {
        "id": "card_1792513864986_r14ph3__バス停",
        "word": "バス停",
        "reading": "ばすてい",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "バス停",
            "ko": "버스 정류장 (bus stop)",
            "en": "bus stop"
        },
        "example": {
            "ja": "<ruby>家<rt>いえ</rt></ruby>の<ruby>近<rt>ちか</rt></ruby>くにバス<ruby>停<rt>てい</rt></ruby>があるので、<ruby>移動<rt>いどう</rt></ruby>するのにとても<ruby>便利<rt>べんり</rt></ruby>です。",
            "ko": "집 근처에 버스 정류장이 있어서 이동하기 매우 편리합니다. (There is a bus stop near my house, so it is very convenient for getting around.)",
            "en": "There is a bus stop near my house, so it is very convenient for getting around."
        }
    },
    {
        "id": "card_1792685592884_w6m1n1__うるさい",
        "word": "うるさい",
        "reading": "うるさい",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "うるさい",
            "ko": "시끄럽다, 성가시다 (noisy, loud, annoying)",
            "en": "noisy, loud, annoying"
        },
        "example": {
            "ja": "<ruby>外<rt>そと</rt></ruby>の<ruby>工事<rt>こうじ</rt></ruby>の<ruby>音<rt>おと</rt></ruby>がうるさくて、<ruby>勉強<rt>べんきょう</rt></ruby>に<ruby>集中<rt>しゅうちゅう</rt></ruby>できない。",
            "ko": "바깥 공사 소리가 시끄러워서 공부에 집중할 수 없다. (The construction noise outside is so loud that I cannot concentrate on studying.)",
            "en": "The construction noise outside is so loud that I cannot concentrate on studying."
        }
    },
    {
        "id": "card_1792685592891_wiq54q__同い年",
        "word": "同い年",
        "reading": "おないどし",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "同い年",
            "ko": "동갑, 동년배 (same age)",
            "en": "same age"
        },
        "example": {
            "ja": "<ruby>彼<rt>かれ</rt></ruby>とは<ruby>同<rt>おな</rt></ruby>い<ruby>年<rt>どし</rt></ruby>なので、<ruby>初<rt>はじ</rt></ruby>めて<ruby>会<rt>あ</rt></ruby>ったときからすぐに<ruby>仲良<rt>なかよ</rt></ruby>くなれた。",
            "ko": "그와는 동갑이라서 처음 만났을 때부터 바로 친해질 수 있었다. (Since he and I are the same age, we became close right from the first time we met.)",
            "en": "Since he and I are the same age, we became close right from the first time we met."
        }
    },
    {
        "id": "card_1792685592896_g6l584__芸能人",
        "word": "芸能人",
        "reading": "げいのうじん",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "芸能人",
            "ko": "연예인 (celebrity, entertainer)",
            "en": "celebrity, entertainer"
        },
        "example": {
            "ja": "<ruby>渋谷<rt>しぶや</rt></ruby>を<ruby>歩<rt>ある</rt></ruby>いていたら、テレビでよく<ruby>見<rt>み</rt></ruby>る<ruby>芸能人<rt>げいのうじん</rt></ruby>を<ruby>見<rt>み</rt></ruby>かけた。",
            "ko": "시부야를 걷고 있었더니 TV에서 자주 보던 연예인을 우연히 보았다. (While walking in Shibuya, I spotted a celebrity I often see on television.)",
            "en": "While walking in Shibuya, I spotted a celebrity I often see on television."
        }
    },
    {
        "id": "card_1792685592900_tl5unu__提携する",
        "word": "提携する",
        "reading": "ていけいする",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "提携する",
            "ko": "제휴하다, 협력하다 (to partner with, to tie up with)",
            "en": "to partner with, to tie up with"
        },
        "example": {
            "ja": "その<ruby>会社<rt>かいしゃ</rt></ruby>は<ruby>海外<rt>かいがい</rt></ruby>の<ruby>企業<rt>きぎょう</rt></ruby>と<ruby>提携<rt>ていけい</rt></ruby>して、<ruby>新<rt>あたら</rt></ruby>しいサービスを<ruby>始<rt>はじ</rt></ruby>めた。",
            "ko": "그 회사는 해외 기업과 제휴하여 새로운 서비스를 시작했다. (That company partnered with an overseas firm to launch a new service.)",
            "en": "That company partnered with an overseas firm to launch a new service."
        }
    },
    {
        "id": "card_1792685592903_t0xnm8__性格",
        "word": "性格",
        "reading": "せいかく",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "性格",
            "ko": "성격 (personality, character)",
            "en": "personality, character"
        },
        "example": {
            "ja": "<ruby>彼女<rt>かのじょ</rt></ruby>は<ruby>明<rt>あか</rt></ruby>るくて<ruby>優<rt>やさ</rt></ruby>しい<ruby>性格<rt>せいかく</rt></ruby>なので、みんなから<ruby>好<rt>す</rt></ruby>かれている。",
            "ko": "그녀는 밝고 상냥한 성격이라서 모든 사람에게 사랑받고 있다. (She has a bright and kind personality, so she is liked by everyone.)",
            "en": "She has a bright and kind personality, so she is liked by everyone."
        }
    },
    {
        "id": "card_1792685592905_li6i2j__柔らかい",
        "word": "柔らかい",
        "reading": "やわらかい",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "柔らかい",
            "ko": "부드럽다 (soft, tender)",
            "en": "soft, tender"
        },
        "example": {
            "ja": "このお<ruby>肉<rt>にく</rt></ruby>はとても<ruby>柔<rt>やわ</rt></ruby>らかくて、<ruby>口<rt>くち</rt></ruby>の<ruby>中<rt>なか</rt></ruby>でとろけるようだ。",
            "ko": "이 고기는 매우 부드러워서 입안에서 살살 녹는 것 같다. (This meat is so tender that it feels like it melts in your mouth.)",
            "en": "This meat is so tender that it feels like it melts in your mouth."
        }
    },
    {
        "id": "card_1792685592908_t8cn8n__今年",
        "word": "今年",
        "reading": "ことし",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "今年",
            "ko": "올해, 금년 (this year)",
            "en": "this year"
        },
        "example": {
            "ja": "<ruby>今年<rt>ことし</rt></ruby>は<ruby>日本語<rt>にほんご</rt></ruby>の<ruby>試験<rt>しけん</rt></ruby>に<ruby>合格<rt>ごうかく</rt></ruby>できるように、<ruby>毎日<rt>まいにち</rt></ruby><ruby>頑張<rt>がんば</rt></ruby>っています。",
            "ko": "올해는 일본어 시험에 합격할 수 있도록 매일 열심히 하고 있습니다. (I am working hard every day so that I can pass the Japanese exam this year.)",
            "en": "I am working hard every day so that I can pass the Japanese exam this year."
        }
    },
    {
        "id": "card_1792685592911_biappe__去年",
        "word": "去年",
        "reading": "きょねん",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "去年",
            "ko": "작년, 지난해 (last year)",
            "en": "last year"
        },
        "example": {
            "ja": "<ruby>去年<rt>きょねん</rt></ruby>の<ruby>夏<rt>なつ</rt></ruby>に<ruby>友達<rt>ともだち</rt></ruby>と<ruby>一緒<rt>いっしょ</rt></ruby>に<ruby>北海道<rt>ほっかいどう</rt></ruby>へ<ruby>旅行<rt>りょこう</rt></ruby>に<ruby>行<rt>い</rt></ruby>きました。",
            "ko": "작년 여름에 친구와 함께 홋카이도로 여행을 갔습니다. (Last summer, I went on a trip to Hokkaido with my friends.)",
            "en": "Last summer, I went on a trip to Hokkaido with my friends."
        }
    },
    {
        "id": "card_1792685592913_f979og__来年",
        "word": "来年",
        "reading": "らいねん",
        "category": "授業で習った言葉",
        "meaning": {
            "ja": "来年",
            "ko": "내년 (next year)",
            "en": "next year"
        },
        "example": {
            "ja": "<ruby>来年<rt>らいねん</rt></ruby>の<ruby>春<rt>はる</rt></ruby>から<ruby>東京<rt>とうきょう</rt></ruby>の<ruby>大学<rt>だいがく</rt></ruby>に<ruby>留学<rt>りゅうがく</rt></ruby>する<ruby>予定<rt>よてい</rt></ruby>です。",
            "ko": "내년 봄부터 도쿄의 대학교에 유학할 예정입니다. (I plan to study abroad at a university in Tokyo starting next spring.)",
            "en": "I plan to study abroad at a university in Tokyo starting next spring."
        }
    }
]

# Student 0003 Mylist: card_0335 (七個) + all 35 custom cards
student_0003_mylist = ["card_0335"] + [c["id"] for c in student_0003_cards]

# =========================================================================
# 2. Student 0023 (Arun, English) - Fix 4 cards with missing ruby tags
# =========================================================================
def fix_arun():
    token = get_auth_token("0023", "6600")
    get_url = f"https://firestore.googleapis.com/v1/projects/{PROJECT_ID}/databases/(default)/documents/students/0023"
    req = urllib.request.Request(get_url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req) as resp:
        doc = json.loads(resp.read().decode("utf-8"))

    raw_cards = doc.get("fields", {}).get("customCards", {}).get("arrayValue", {}).get("values", [])
    seen_ids = set()
    cleaned_cards = []
    
    ruby_fixes = {
        "お小遣い": {
            "ja": "<ruby>毎月<rt>まいつき</rt></ruby>のお<ruby>小遣<rt>こづか</rt></ruby>いの<ruby>中<rt>なか</rt></ruby>から<ruby>少<rt>すこ</rt></ruby>しずつ<ruby>貯金<rt>ちょきん</rt></ruby>して、ずっと<ruby>欲<rt>ほ</rt></ruby>しかったゲームソフトを<ruby>買<rt>か</rt></ruby>った。",
            "en": "I steadily saved up from my monthly allowance and bought the video game software I had wanted for a long time."
        },
        "後悔": {
            "ja": "あの<ruby>時<rt>とき</rt></ruby>もっと<ruby>一生懸命<rt>いっしょうけんめい</rt></ruby><ruby>勉強<rt>べんきょう</rt></ruby>しておけばよかったと、<ruby>今<rt>いま</rt></ruby>になって<ruby>深<rt>ふか</rt></ruby>く<ruby>後悔<rt>こうかい</rt></ruby>している。",
            "en": "I now deeply regret that I did not study much harder back then."
        },
        "口パク": {
            "ja": "<ruby>図書館<rt>としょかん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>で<ruby>声<rt>こえ</rt></ruby>を<ruby>出<rt>だ</rt></ruby>せなかったので、<ruby>友達<rt>ともだち</rt></ruby>に<ruby>向<rt>む</rt></ruby>かって<ruby>口<rt>くち</rt></ruby>パクで「<ruby>帰<rt>かえ</rt></ruby>ろう」と<ruby>伝<rt>つた</rt></ruby>えた。",
            "en": "Because I could not make a sound in the library, I mouthed \"Let's go home\" to my friend."
        },
        "〜の代わりに": {
            "ja": "<ruby>急病<rt>きゅうびょう</rt></ruby>で<ruby>出席<rt>しゅっせき</rt></ruby>できなくなった<ruby>課長<rt>かちょう</rt></ruby>の<ruby>代<rt>か</rt></ruby>わりに、<ruby>私<rt>わたし</rt></ruby>が<ruby>代理<rt>だいり</rt></ruby>でプレゼンを<ruby>行<rt>おこな</rt></ruby>うことになった。",
            "en": "Instead of the section manager who fell ill and could not attend, I was assigned to give the presentation in his place."
        }
    }

    for c in raw_cards:
        f = c.get("mapValue", {}).get("fields", {})
        cid = f.get("id", {}).get("stringValue", "")
        w = f.get("word", {}).get("stringValue", "")
        if cid in seen_ids:
            continue
        seen_ids.add(cid)
        
        card_obj = {
            "id": cid,
            "word": w,
            "reading": f.get("reading", {}).get("stringValue", ""),
            "category": f.get("category", {}).get("stringValue", "授業で習った言葉"),
            "meaning": {
                k: v.get("stringValue", "")
                for k, v in f.get("meaning", {}).get("mapValue", {}).get("fields", {}).items()
            },
            "example": {
                k: v.get("stringValue", "")
                for k, v in f.get("example", {}).get("mapValue", {}).get("fields", {}).items()
            }
        }
        if w in ruby_fixes:
            card_obj["example"]["ja"] = ruby_fixes[w]["ja"]
            card_obj["example"]["en"] = ruby_fixes[w]["en"]
            
        cleaned_cards.append(card_obj)
        
    patch_url = (
        f"https://firestore.googleapis.com/v1/projects/{PROJECT_ID}/databases/(default)/documents/students/0023"
        f"?updateMask.fieldPaths=customCards"
    )
    firestore_cards = [to_firestore_value(c) for c in cleaned_cards]
    patch_payload = json.dumps({
        "fields": {
            "customCards": {"arrayValue": {"values": firestore_cards}}
        }
    }).encode("utf-8")
    req = urllib.request.Request(patch_url, data=patch_payload, headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }, method="PATCH")
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
    print(f"✅ Student 0023 successfully patched with {len(cleaned_cards)} clean cards!")

def patch_student_0003():
    token = get_auth_token("0003", "3344")
    firestore_cards = [to_firestore_value(c) for c in student_0003_cards]
    firestore_mylist = [to_firestore_value(mid) for mid in student_0003_mylist]
    firestore_word_names = [to_firestore_value(c["word"]) for c in student_0003_cards]

    patch_url = (
        f"https://firestore.googleapis.com/v1/projects/{PROJECT_ID}/databases/(default)/documents/students/0003"
        f"?updateMask.fieldPaths=customCards&updateMask.fieldPaths=mylist&updateMask.fieldPaths=wordNames"
    )
    patch_payload = json.dumps({
        "fields": {
            "customCards": {"arrayValue": {"values": firestore_cards}},
            "mylist": {"arrayValue": {"values": firestore_mylist}},
            "wordNames": {"arrayValue": {"values": firestore_word_names}}
        }
    }).encode("utf-8")

    req = urllib.request.Request(patch_url, data=patch_payload, headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }, method="PATCH")
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
    print(f"✅ Student 0003 successfully patched with {len(student_0003_cards)} clean cards and {len(student_0003_mylist)} mylist items!")

if __name__ == "__main__":
    patch_student_0003()
    fix_arun()
