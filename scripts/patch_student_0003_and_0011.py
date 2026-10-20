import urllib.request
import json

API_KEY = "AIzaSyBNsrBL1xRErsuOHgvI7xNs15cai-auoSE"
PROJECT_ID = "japanese-learning-e8a53"

def to_firestore_value(val):
    if isinstance(val, str):
        return {"stringValue": val}
    elif isinstance(val, bool):
        return {"booleanValue": val}
    elif isinstance(val, int) or isinstance(val, float):
        return {"integerValue": str(val)}
    elif isinstance(val, list):
        return {"arrayValue": {"values": [to_firestore_value(x) for x in val]}}
    elif isinstance(val, dict):
        return {"mapValue": {"fields": {k: to_firestore_value(v) for k, v in val.items()}}}
    return {"nullValue": None}

def patch_student(student_id, passcode, cards):
    auth_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
    auth_data = json.dumps({
        "email": f"{student_id}@haku.local",
        "password": f"haku_{passcode}_sec",
        "returnSecureToken": True
    }).encode("utf-8")
    req = urllib.request.Request(auth_url, data=auth_data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        token_data = json.loads(resp.read().decode("utf-8"))
    id_token = token_data["idToken"]

    firestore_cards = [to_firestore_value(c) for c in cards]
    firestore_mylist = [to_firestore_value(c["id"]) for c in cards]
    firestore_word_names = [to_firestore_value(c["word"]) for c in cards]

    patch_url = (
        f"https://firestore.googleapis.com/v1/projects/{PROJECT_ID}/databases/(default)/documents/students/{student_id}"
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
        "Authorization": f"Bearer {id_token}",
        "Content-Type": "application/json"
    }, method="PATCH")
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
    print(f"✅ Student {student_id} successfully patched with {len(cards)} clean cards!")

# =========================================================================
# 1. Student 0003 (두성, Korean) - All 23 cards strictly in Ideal Format
# =========================================================================
cards_0003 = [
    {
        "id": "c_0003_nanako",
        "word": "七個",
        "reading": "ななこ",
        "meaning": {"ja": "七個", "ko": "일곱 개 (seven items)", "en": "seven items"},
        "example": {
            "ja": "りんごを<ruby>七個<rt>ななこ</rt></ruby><ruby>買<rt>か</rt></ruby>いました。",
            "ko": "사과를 일곱 개 샀어요. (I bought seven apples.)",
            "en": "I bought seven apples."
        },
        "category": "授業で習った言葉"
    },
    {
        "id": "c_0003_shumi",
        "word": "趣味",
        "reading": "しゅみ",
        "meaning": {"ja": "趣味", "ko": "취미 (hobby, pastime)", "en": "hobby, pastime"},
        "example": {
            "ja": "<ruby>私<rt>わたし</rt></ruby>の<ruby>趣味<rt>しゅみ</rt></ruby>は<ruby>映画鑑賞<rt>えいがかんしょう</rt></ruby>です。",
            "ko": "제 취미는 영화 감상이에요. (My hobby is watching movies.)",
            "en": "My hobby is watching movies."
        },
        "category": "授業で習った言葉"
    },
    {
        "id": "c_0003_shukujitsu",
        "word": "祝日",
        "reading": "しゅくじつ",
        "meaning": {"ja": "祝日", "ko": "공휴일, 축일 (national holiday, public holiday)", "en": "national holiday, public holiday"},
        "example": {
            "ja": "<ruby>明日<rt>あした</rt></ruby>は<ruby>祝日<rt>しゅくじつ</rt></ruby>なので、<ruby>会社<rt>かいしゃ</rt></ruby>は<ruby>休<rt>やす</rt></ruby>みです。",
            "ko": "내일은 공휴일이라서 회사는 쉽니다. (Tomorrow is a public holiday, so the company is closed.)",
            "en": "Tomorrow is a public holiday, so the company is closed."
        },
        "category": "授業で習った言葉"
    },
    {
        "id": "c_0003_basho",
        "word": "場所",
        "reading": "ばしょ",
        "meaning": {"ja": "場所", "ko": "장소, 곳 (place, location)", "en": "place, location"},
        "example": {
            "ja": "<ruby>次<rt>つぎ</rt></ruby>の<ruby>会議<rt>かいぎ</rt></ruby>の<ruby>場所<rt>ばしょ</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えてください。",
            "ko": "다음 회의 장소를 알려주세요. (Please tell me the location of the next meeting.)",
            "en": "Please tell me the location of the next meeting."
        },
        "category": "授業で習った言葉"
    },
    {
        "id": "c_0003_ogoru",
        "word": "奢る",
        "reading": "おごる",
        "meaning": {"ja": "奢る", "ko": "(한턱) 쏘다, 사주다 (to treat someone to food/drinks)", "en": "to treat someone to food/drinks"},
        "example": {
            "ja": "<ruby>今日<rt>きょう</rt></ruby>は<ruby>私<rt>わたし</rt></ruby>が<ruby>昼<rt>ひる</rt></ruby>ご飯を<ruby>奢<rt>おご</rt></ruby>ります。",
            "ko": "오늘은 제가 점심을 살게요. (I will treat you to lunch today.)",
            "en": "I will treat you to lunch today."
        },
        "category": "授業で習った言葉"
    },
    {
        "id": "c_0003_aisatsu",
        "word": "挨拶",
        "reading": "あいさつ",
        "meaning": {"ja": "挨拶", "ko": "인사 (greeting, salutation)", "en": "greeting, salutation"},
        "example": {
            "ja": "<ruby>朝<rt>あさ</rt></ruby>は<ruby>気持<rt>きも</rt></ruby>ちよく<ruby>挨拶<rt>あいさつ</rt></ruby>をしましょう。",
            "ko": "아침에는 기분 좋게 인사를 합시다. (Let's greet each other pleasantly in the morning.)",
            "en": "Let's greet each other pleasantly in the morning."
        },
        "category": "授業で習った言葉"
    },
    {
        "id": "c_0003_yuukyuu",
        "word": "有給",
        "reading": "ゆうきゅう",
        "meaning": {"ja": "有給", "ko": "연차, 유급 휴가 (paid leave, paid time off)", "en": "paid leave, paid time off"},
        "example": {
            "ja": "<ruby>来週<rt>らいしゅう</rt></ruby>の<ruby>金曜日<rt>きんようび</rt></ruby>に<ruby>有給<rt>ゆうきゅう</rt></ruby>を<ruby>取<rt>と</rt></ruby>りました。",
            "ko": "다음 주 금요일에 연차를 냈어요. (I took paid leave next Friday.)",
            "en": "I took paid leave next Friday."
        },
        "category": "授業で習った言葉"
    },
    {
        "id": "c_0003_kensa",
        "word": "検査",
        "reading": "けんさ",
        "meaning": {"ja": "検査", "ko": "검사 (inspection, examination, test)", "en": "inspection, examination, test"},
        "example": {
            "ja": "<ruby>病院<rt>びょういん</rt></ruby>で<ruby>健康<rt>けんこう</rt></ruby>の<ruby>検査<rt>けんさ</rt></ruby>を<ruby>受<rt>う</rt></ruby>けました。",
            "ko": "병원에서 건강 검사를 받았어요. (I had a health checkup at the hospital.)",
            "en": "I had a health checkup at the hospital."
        },
        "category": "授業で習った言葉"
    },
    {
        "id": "c_0003_kekka",
        "word": "結果",
        "reading": "けっか",
        "meaning": {"ja": "結果", "ko": "결과 (result, outcome)", "en": "result, outcome"},
        "example": {
            "ja": "<ruby>試験<rt>しけん</rt></ruby>の<ruby>結果<rt>けっか</rt></ruby>が<ruby>出<rt>で</rt></ruby>るのを<ruby>待<rt>ま</rt></ruby>っています。",
            "ko": "시험 결과가 나오기를 기다리고 있어요. (I am waiting for the test results to come out.)",
            "en": "I am waiting for the test results to come out."
        },
        "category": "授業で習った言葉"
    },
    {
        "id": "c_0003_kanzou",
        "word": "肝臓",
        "reading": "かんぞう",
        "meaning": {"ja": "肝臓", "ko": "간, 간장 (liver)", "en": "liver"},
        "example": {
            "ja": "お<ruby>酒<rt>さけ</rt></ruby>を<ruby>飲<rt>の</rt></ruby>みすぎると、<ruby>肝臓<rt>かんぞう</rt></ruby>を<ruby>悪<rt>わる</rt></ruby>くします。",
            "ko": "술을 너무 많이 마시면 간을 상하게 해요. (Drinking too much alcohol damages your liver.)",
            "en": "Drinking too much alcohol damages your liver."
        },
        "category": "授業で習った言葉"
    },
    {
        "id": "c_0003_nagai",
        "word": "長い",
        "reading": "ながい",
        "meaning": {"ja": "長い", "ko": "길다, 오랜 (long)", "en": "long"},
        "example": {
            "ja": "この<ruby>道<rt>みち</rt></ruby>はとても<ruby>長<rt>なが</rt></ruby>いです。",
            "ko": "이 길은 매우 길어요. (This road is very long.)",
            "en": "This road is very long."
        },
        "category": "授業で習った言葉"
    },
    {
        "id": "c_0003_mushisuru",
        "word": "無視する",
        "reading": "むしする",
        "meaning": {"ja": "無視する", "ko": "무시하다 (to ignore, to disregard)", "en": "to ignore, to disregard"},
        "example": {
            "ja": "<ruby>人<rt>ひと</rt></ruby>の<ruby>話<rt>はなし</rt></ruby>を<ruby>無視<rt>むし</rt></ruby>してはいけません。",
            "ko": "다른 사람의 말을 무시하면 안 돼요. (You must not ignore what other people say.)",
            "en": "You must not ignore what other people say."
        },
        "category": "授業で習った言葉"
    },
    {
        "id": "c_0003_toshiue",
        "word": "年上",
        "reading": "としうえ",
        "meaning": {"ja": "年上", "ko": "연상, 손위 (older, senior)", "en": "older, senior"},
        "example": {
            "ja": "<ruby>彼女<rt>かのじょ</rt></ruby>は<ruby>私<rt>わたし</rt></ruby>より2<ruby>歳<rt>さい</rt></ruby><ruby>年上<rt>としうえ</rt></ruby>です。",
            "ko": "그녀는 나보다 두 살 연상이에요. (She is two years older than me.)",
            "en": "She is two years older than me."
        },
        "category": "授業で習った言葉"
    },
    {
        "id": "c_0003_toshiyori",
        "word": "年寄り",
        "reading": "としより",
        "meaning": {"ja": "年寄り", "ko": "노인, 어르신 (elderly person, senior citizen)", "en": "elderly person, senior citizen"},
        "example": {
            "ja": "電車でお<ruby>年寄<rt>としよ</rt></ruby>りに<ruby>席<rt>せき</rt></ruby>を<ruby>譲<rt>ゆず</rt></ruby>りました。",
            "ko": "전철에서 어르신에게 자리를 양보했어요. (I gave up my seat to an elderly person on the train.)",
            "en": "I gave up my seat to an elderly person on the train."
        },
        "category": "授業で習った言葉"
    },
    {
        "id": "c_0003_kanja",
        "word": "患者",
        "reading": "かんじゃ",
        "meaning": {"ja": "患者", "ko": "환자 (patient)", "en": "patient"},
        "example": {
            "ja": "<ruby>医師<rt>いし</rt></ruby>が<ruby>患者<rt>かんじゃ</rt></ruby>を<ruby>丁寧<rt>ていねい</rt></ruby>に<ruby>診察<rt>しんさつ</rt></ruby>した。",
            "ko": "의사가 환자를 정성껏 진찰했어요. (The doctor examined the patient carefully.)",
            "en": "The doctor examined the patient carefully."
        },
        "category": "授業で習った言葉"
    },
    {
        "id": "c_0003_kankouchi",
        "word": "観光地",
        "reading": "かんこうち",
        "meaning": {"ja": "観光地", "ko": "관광지, 명소 (tourist attraction, tourist spot)", "en": "tourist attraction, tourist spot"},
        "example": {
            "ja": "<ruby>京都<rt>きょうと</rt></ruby>には<ruby>有名<rt>ゆうめい</rt></ruby>な<ruby>観光地<rt>かんこうち</rt></ruby>がたくさんあります。",
            "ko": "교토에는 유명한 관광지가 많이 있어요. (Kyoto has many famous tourist spots.)",
            "en": "Kyoto has many famous tourist spots."
        },
        "category": "授業で習った言葉"
    },
    {
        "id": "c_0003_onsen",
        "word": "温泉",
        "reading": "おんせん",
        "meaning": {"ja": "温泉", "ko": "온천 (hot spring, onsen)", "en": "hot spring, onsen"},
        "example": {
            "ja": "<ruby>週末<rt>しゅうまつ</rt></ruby>に<ruby>温泉<rt>おんせん</rt></ruby>に<ruby>行<rt>い</rt></ruby>ってリフレッシュしたいです。",
            "ko": "주말에 온천에 가서 기분 전환을 하고 싶어요. (I want to go to a hot spring this weekend to refresh myself.)",
            "en": "I want to go to a hot spring this weekend to refresh myself."
        },
        "category": "授業で習った言葉"
    },
    {
        "id": "c_0003_onakagasukimashita",
        "word": "お腹がすきました",
        "reading": "おなかがすきました",
        "meaning": {"ja": "お腹がすきました", "ko": "배가 고픕니다 (I am hungry)", "en": "I am hungry"},
        "example": {
            "ja": "お<ruby>腹<rt>なか</rt></ruby>がすいたので、ラーメンを<ruby>食<rt>た</rt></ruby>べに<ruby>行<rt>い</rt></ruby>きましょう。",
            "ko": "배가 고파서 라면을 먹으러 갑시다. (I am hungry, so let's go eat ramen.)",
            "en": "I am hungry, so let's go eat ramen."
        },
        "category": "授業で習った言葉"
    },
    {
        "id": "c_0003_pekopeko",
        "word": "ペコペコ",
        "reading": "ぺこぺこ",
        "meaning": {"ja": "ペコペコ", "ko": "(배가) 꼬르륵거림, 몹시 배고픔 (famished, very hungry)", "en": "famished, very hungry"},
        "example": {
            "ja": "<ruby>朝<rt>あさ</rt></ruby>から<ruby>何<rt>なに</rt></ruby>も<ruby>食<rt>た</rt></ruby>べていなくて、お<ruby>腹<rt>なか</rt></ruby>がペコペコです。",
            "ko": "아침부터 아무것도 안 먹어서 배가 몹시 고파요. (I haven't eaten anything since morning, so I'm famished.)",
            "en": "I haven't eaten anything since morning, so I'm famished."
        },
        "category": "授業で習った言葉"
    },
    {
        "id": "c_0003_onakagaippai",
        "word": "お腹がいっぱい",
        "reading": "おなかがいっぱい",
        "meaning": {"ja": "お腹がいっぱい", "ko": "배가 부름, 배부르다 (full (after eating))", "en": "full (after eating)"},
        "example": {
            "ja": "<ruby>美味<rt>おい</rt></ruby>しい<ruby>料理<rt>りょうり</rt></ruby>をたくさん<ruby>食<rt>た</rt></ruby>べて、お<ruby>腹<rt>なか</rt></ruby>がいっぱいです。",
            "ko": "맛있는 음식을 많이 먹어서 배가 불러요. (I ate a lot of delicious food, so I am full.)",
            "en": "I ate a lot of delicious food, so I am full."
        },
        "category": "授業で習った言葉"
    },
    {
        "id": "c_0003_panpan",
        "word": "パンパン",
        "reading": "ぱんぱん",
        "meaning": {"ja": "パンパン", "ko": "(배 등이) 빵빵함, 터질 듯 가득 참 (stuffed, bursting full)", "en": "stuffed, bursting full"},
        "example": {
            "ja": "バイキングで<ruby>食<rt>た</rt></ruby>べすぎて、お<ruby>腹<rt>なか</rt></ruby>がパンパンです。",
            "ko": "뷔페에서 너무 많이 먹어서 배가 빵빵해요. (I ate too much at the buffet, so my stomach is bursting full.)",
            "en": "I ate too much at the buffet, so my stomach is bursting full."
        },
        "category": "授業で習った言葉"
    },
    {
        "id": "c_0003_katakori",
        "word": "肩凝り",
        "reading": "かたこり",
        "meaning": {"ja": "肩凝り", "ko": "어깨 결림 (stiff shoulders)", "en": "stiff shoulders"},
        "example": {
            "ja": "パソコンの<ruby>使<rt>つか</rt></ruby>いすぎで、<ruby>肩凝<rt>かたこ</rt></ruby>りがひどいです。",
            "ko": "컴퓨터를 너무 많이 써서 어깨 결림이 심해요. (My shoulders are very stiff from using the computer too much.)",
            "en": "My shoulders are very stiff from using the computer too much."
        },
        "category": "授業で習った言葉"
    },
    {
        "id": "c_0003_shouyu",
        "word": "醤油",
        "reading": "しょうゆ",
        "meaning": {"ja": "醤油", "ko": "간장 (soy sauce)", "en": "soy sauce"},
        "example": {
            "ja": "お<ruby>刺身<rt>さしみ</rt></ruby>に<ruby>醤油<rt>しょうゆ</rt></ruby>をつけて<ruby>食<rt>た</rt></ruby>べます。",
            "ko": "생선회에 간장을 찍어서 먹어요. (I dip sashimi in soy sauce and eat it.)",
            "en": "I eat sashimi dipped in soy sauce."
        },
        "category": "授業で習った言葉"
    }
]

# =========================================================================
# 2. Student 0011 (Keyvin, French) - Repair 9 reversed cards and keep all 127
# =========================================================================
def repair_0011():
    auth_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
    auth_data = json.dumps({
        "email": "0011@haku.local",
        "password": "haku_2244_sec",
        "returnSecureToken": True
    }).encode("utf-8")
    req = urllib.request.Request(auth_url, data=auth_data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        token_data = json.loads(resp.read().decode("utf-8"))
    id_token = token_data["idToken"]

    doc_url = f"https://firestore.googleapis.com/v1/projects/{PROJECT_ID}/databases/(default)/documents/students/0011"
    req = urllib.request.Request(doc_url, headers={"Authorization": f"Bearer {id_token}"})
    with urllib.request.urlopen(req) as resp:
        doc = json.loads(resp.read().decode("utf-8"))

    raw_cards = doc.get("fields", {}).get("customCards", {}).get("arrayValue", {}).get("values", [])

    repaired_french_9 = {
        "Prenez soin de vous. / Soigne-toi bien.": {
            "id": "c_0011_odaijini",
            "word": "お大事に",
            "reading": "おだいじに",
            "meaning": {"ja": "お大事に", "fr": "Prenez soin de vous. / Soigne-toi bien. (Take care, Get well soon)", "en": "Take care, Get well soon"},
            "example": {
                "ja": "<ruby>風邪<rt>かぜ</rt></ruby>をひいたそうですね。どうぞお<ruby>大事<rt>だいじ</rt></ruby>に。",
                "fr": "J'ai appris que vous aviez attrapé froid. Prenez bien soin de vous. (I heard you caught a cold. Please take care.)",
                "en": "I heard you caught a cold. Please take care."
            }
        },
        "la rumeur": {
            "id": "c_0011_uwasa",
            "word": "噂",
            "reading": "うわさ",
            "meaning": {"ja": "噂", "fr": "la rumeur, le bruit (rumor)", "en": "rumor"},
            "example": {
                "ja": "その<ruby>噂<rt>うわさ</rt></ruby>は<ruby>本当<rt>ほんとう</rt></ruby>ですか？",
                "fr": "Cette rumeur est-elle vraie ? (Is that rumor true?)",
                "en": "Is that rumor true?"
            }
        },
        "l'éternuement": {
            "id": "c_0011_kushami",
            "word": "くしゃみ",
            "reading": "くしゃみ",
            "meaning": {"ja": "くしゃみ", "fr": "l'éternuement (sneeze)", "en": "sneeze"},
            "example": {
                "ja": "<ruby>寒<rt>さむ</rt></ruby>くてくしゃみが<ruby>出<rt>で</rt></ruby>ました。",
                "fr": "J'ai éternué parce qu'il faisait froid. (I sneezed because it was cold.)",
                "en": "I sneezed because it was cold."
            }
        },
        "l'acouphène": {
            "id": "c_0011_miminari",
            "word": "耳鳴り",
            "reading": "みみなり",
            "meaning": {"ja": "耳鳴り", "fr": "l'acouphène, le bourdonnement d'oreille (tinnitus, ringing in ears)", "en": "tinnitus, ringing in ears"},
            "example": {
                "ja": "<ruby>疲<rt>つか</rt></ruby>れると<ruby>耳鳴<rt>みみな</rt></ruby>りがします。",
                "fr": "Quand je suis fatigué, j'ai des acouphènes. (When I'm tired, I get ringing in my ears.)",
                "en": "When I'm tired, I get ringing in my ears."
            }
        },
        "les jeunes": {
            "id": "c_0011_wakamono",
            "word": "若者",
            "reading": "わかもの",
            "meaning": {"ja": "若者", "fr": "les jeunes, la jeunesse (young people, youth)", "en": "young people, youth"},
            "example": {
                "ja": "<ruby>多<rt>おお</rt></ruby>くの<ruby>若者<rt>わかもの</rt></ruby>がイベントに<ruby>参加<rt>さんか</rt></ruby>しました。",
                "fr": "Beaucoup de jeunes ont participé à l'événement. (Many young people participated in the event.)",
                "en": "Many young people participated in the event."
            }
        },
        "la réduction étudiante / le tarif étudiant": {
            "id": "c_0011_gakuwari",
            "word": "学割",
            "reading": "がくわり",
            "meaning": {"ja": "学割", "fr": "la réduction étudiante / le tarif étudiant (student discount)", "en": "student discount"},
            "example": {
                "ja": "<ruby>学生証<rt>がくせいしょう</rt></ruby>を<ruby>見<rt>み</rt></ruby>せると、<ruby>学割<rt>がくわり</rt></ruby>が<ruby>使<rt>つか</rt></ruby>えます。",
                "fr": "En montrant votre carte d'étudiant, vous pouvez bénéficier d'un tarif étudiant. (By showing your student ID, you can use the student discount.)",
                "en": "By showing your student ID, you can use the student discount."
            }
        },
        "la loi": {
            "id": "c_0011_houritsu",
            "word": "法律",
            "reading": "ほうりつ",
            "meaning": {"ja": "法律", "fr": "la loi, la législation (law)", "en": "law"},
            "example": {
                "ja": "<ruby>国<rt>くに</rt></ruby>の<ruby>法律<rt>ほうりつ</rt></ruby>を<ruby>守<rt>まも</rt></ruby>らなければなりません。",
                "fr": "Il faut respecter la loi du pays. (You must obey the laws of the country.)",
                "en": "You must obey the laws of the country."
            }
        },
        "la farine": {
            "id": "c_0011_komugiko",
            "word": "小麦粉",
            "reading": "こむぎこ",
            "meaning": {"ja": "小麦粉", "fr": "la farine de blé (flour, wheat flour)", "en": "flour, wheat flour"},
            "example": {
                "ja": "<ruby>小麦粉<rt>こむぎこ</rt></ruby>と<ruby>卵<rt>たまご</rt></ruby>を<ruby>混<rt>ま</rt></ruby>ぜて生地を<ruby>作<rt>つく</rt></ruby>ります。",
                "fr": "Mélangez la farine et les œufs pour préparer la pâte. (Mix flour and eggs to make dough.)",
                "en": "Mix flour and eggs to make dough."
            }
        },
        "une soirée takoyaki": {
            "id": "c_0011_takopa",
            "word": "タコパ",
            "reading": "たこパ",
            "meaning": {"ja": "タコパ", "fr": "une soirée takoyaki (takoyaki party)", "en": "takoyaki party"},
            "example": {
                "ja": "<ruby>今週末<rt>こんしゅうまつ</rt></ruby>、<ruby>友達<rt>ともだち</rt></ruby>の<ruby>家<rt>いえ</rt></ruby>でタコパをします。",
                "fr": "Ce week-end, on fait une soirée takoyaki chez un ami. (This weekend, we're having a takoyaki party at a friend's house.)",
                "en": "This weekend, we are having a takoyaki party at a friend's house."
            }
        }
    }

    clean_cards_0011 = []
    seen_words = set()

    # First add the 9 repaired items
    for item in repaired_french_9.values():
        clean_cards_0011.append(item)
        seen_words.add(item["word"])

    # Then parse the rest of existing Japanese cards, skipping the reversed ones and duplicates
    for c in raw_cards:
        mv = c.get("mapValue", {}).get("fields", {})
        w = mv.get("word", {}).get("stringValue", "")
        if w in repaired_french_9 or not w:
            continue
        if w in seen_words:
            continue
        seen_words.add(w)

        r = mv.get("reading", {}).get("stringValue", "")
        m_map = mv.get("meaning", {}).get("mapValue", {}).get("fields", {})
        ex_map = mv.get("example", {}).get("mapValue", {}).get("fields", {})

        m_dict = {k: v.get("stringValue", "") for k, v in m_map.items()}
        ex_dict = {k: v.get("stringValue", "") for k, v in ex_map.items()}

        cid = mv.get("id", {}).get("stringValue", f"c_0011_{len(clean_cards_0011)}")
        cat = mv.get("category", {}).get("stringValue", "授業で習った言葉")

        clean_cards_0011.append({
            "id": cid,
            "word": w,
            "reading": r,
            "meaning": m_dict,
            "example": ex_dict,
            "category": cat
        })

    patch_student("0011", "2244", clean_cards_0011)

if __name__ == "__main__":
    patch_student("0003", "3344", cards_0003)
    repair_0011()
