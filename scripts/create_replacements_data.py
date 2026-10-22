# -*- coding: utf-8 -*-
"""
Builder for shared master flashcard replacements (Stage 2).
Covers all remaining duplicate groups, weird proverbs, broken furigana, and short fragments in:
1. INITIAL_VOCAB_DATA (24 cards)
2. CLASS_VOCAB_DATA (210 cards)
"""

import json
import re

print("Building replacement database...")

# Dictionaries of replacements
INITIAL_REPLACEMENTS = {
    "card_0309": { # 毎朝
        "ja": "<ruby>毎朝<rt>まいあさ</rt></ruby>コーヒーを<ruby>淹<rt>い</rt></ruby>れて<ruby>飲<rt>の</rt></ruby>みます。<br/><ruby>目<rt>め</rt></ruby>が<ruby>覚<rt>さ</rt></ruby>めますよ。",
        "en": "I brew and drink coffee every morning. It wakes me up.",
        "zh_TW": "我每天早上都會泡咖啡喝。這樣能提神醒腦呢。",
        "zh_CN": "我每天早上都会泡咖啡喝。这样能提神醒脑呢。",
        "ko": "매일 아침 커피를 내려 마십니다. 잠이 깨거든요.",
        "zh_HK": "我每日朝早都會沖咖啡飲。個人會精神返㗎。",
        "fr": "Je prépare et bois du café tous les matins. Ça me réveille bien."
    },
    "card_0730": { # 入って
        "ja": "どうぞ<ruby>部屋<rt>へや</rt></ruby>に<ruby>入<rt>はい</rt></ruby>って、ソファーに<ruby>座<rt>すわ</rt></ruby>ってください。<br/>お<ruby>茶<rt>ちゃ</rt></ruby>を<ruby>淹<rt>い</rt></ruby>れますね。",
        "en": "Please come in and sit on the sofa. I will brew some tea for you.",
        "zh_TW": "請進房間坐在沙發上吧。我來泡杯茶給您。",
        "zh_CN": "请进房间坐在沙发上吧。我来泡杯茶给您。",
        "ko": "방에 들어와 소파에 앉으세요. 차를 타 드릴게요.",
        "zh_HK": "請入房坐喺梳化度先啦。我沖杯茶俾你飲。",
        "fr": "Entrez dans la pièce et asseyez-vous sur le canapé. Je vais préparer du thé."
    },
    "card_0769": { # 入って (make distinct from 0730)
        "ja": "<ruby>外<rt>そと</rt></ruby>はとても<ruby>寒<rt>さむ</rt></ruby>いので、どうぞ<ruby>暖<rt>あたた</rt></ruby>かい<ruby>部屋<rt>へや</rt></ruby>に<ruby>入<rt>はい</rt></ruby>ってお<ruby>待<rt>ま</rt></ruby>ちください。",
        "en": "It is very cold outside, so please come into the warm room and wait.",
        "zh_TW": "外面非常冷，請進溫暖的房間裡等候吧。",
        "zh_CN": "外面非常冷，请进温暖的房间里等候吧。",
        "ko": "밖이 매우 추우니, 따뜻한 방으로 들어와서 기다리세요.",
        "zh_HK": "出面好凍，請入暖笠笠嘅房入面等啦。",
        "fr": "Il fait très froid dehors, entrez donc dans la pièce chauffée pour attendre."
    },
    "card_0582": { # 味 (was このラーメンはとても美味しいです)
        "ja": "このスープは<ruby>素材<rt>そざい</rt></ruby>の<ruby>味<rt>あじ</rt></ruby>を<ruby>大切<rt>たいせつ</rt></ruby>にしていて、とてもやさしい<ruby>味<rt>あじ</rt></ruby>がします。",
        "en": "This soup cherishes the natural flavors of the ingredients and has a very gentle taste.",
        "zh_TW": "這道湯品注重食材的原味，味道非常溫和順口。",
        "zh_CN": "这道汤品注重食材的原味，味道非常温和顺口。",
        "ko": "이 수프는 식재료 본연의 맛을 살려 아주 부드러운 맛이 납니다.",
        "zh_HK": "呢個湯重視食材嘅原味，味道非常清甜溫和。",
        "fr": "Cette soupe respecte la saveur des ingrédients et a un goût très doux."
    },
    "card_0772": { # 浴びる (was シャワーを浴びる。)
        "ja": "<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>起<rt>お</rt></ruby>きたら、まずシャワーを<ruby>浴<rt>あ</rt></ruby>びて<ruby>気分<rt>きぶん</rt></ruby>をすっきりさせます。",
        "en": "Every morning when I wake up, I first take a shower to refresh myself.",
        "zh_TW": "每天早上起床後，我都會先沖個澡讓自己神清氣爽。",
        "zh_CN": "每天早上起床后，我都会先冲个澡让自己神清气爽。",
        "ko": "매일 아침 일어나면 먼저 샤워를 해서 기분을 상쾌하게 합니다.",
        "zh_HK": "每日朝早起身之後，我都會沖個涼等自己精神醒目。",
        "fr": "Chaque matin au réveil, je prends d'abord une douche pour me rafraîchir."
    },
    "card_0513": { # 質問 (distinct from 0010)
        "ja": "A: <ruby>日本語<rt>にほんご</rt></ruby>の<ruby>文法<rt>ぶんぽう</rt></ruby>について<ruby>質問<rt>しつもん</rt></ruby>してもいいですか？<br/>B: もちろんです！わからないところは何でも質問してくださいね。",
        "en": "A: May I ask a question about Japanese grammar? B: Of course! Feel free to ask anything you don't understand.",
        "zh_TW": "A: 可以請教您關於日語文法的問題嗎？ B: 當然可以！有不懂的地方請儘管提問喔。",
        "zh_CN": "A: 可以请教您关于日语语法的问题吗？ B: 当然可以！有不懂的地方请尽管提问哦。",
        "ko": "A: 일본어 문법에 대해 질문해도 될까요? B: 물론이죠! 모르는 것은 무엇이든 질문하세요.",
        "zh_HK": "A: 請問可唔可以問關於日文文法嘅問題呀？ B: 當然得啦！有唔明嘅隨時問啦。",
        "fr": "A: Puis-je poser une question sur la grammaire japonaise ? B: Bien sûr ! N'hésitez pas à poser toutes vos questions."
    },
    "card_0166": { # 学生 (distinct from 0012)
        "ja": "A: <ruby>妹<rt>いもうと</rt></ruby>さんは<ruby>高校生<rt>こうこうせい</rt></ruby>ですか？<br/>B: はい、この<ruby>春<rt>はる</rt></ruby>から<ruby>高校<rt>こうこう</rt></ruby>の<ruby>学生<rt>がくせい</rt></ruby>になりました。",
        "en": "A: Is your younger sister a high school student? B: Yes, she became a high school student this spring.",
        "zh_TW": "A: 令妹是高中生嗎？ B: 是的，她今年春天剛升上高中成為高中生。",
        "zh_CN": "A: 令妹是高中生吗？ B: 是的，她今年春天刚升上高中成为高中生。",
        "ko": "A: 여동생분은 고등학생인가요? B: 네, 이번 봄부터 고등학교 학생이 되었습니다.",
        "zh_HK": "A: 你妹妹係高中生嚟㗎？ B: 係呀，佢今年春天升咗上高中做學生啦。",
        "fr": "A: Votre petite sœur est-elle lycéenne ? B: Oui, elle est devenue lycéenne ce printemps."
    },
    "card_0183": { # 先生 (distinct from 0013)
        "ja": "A: <ruby>日本語<rt>にほんご</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えてくれた<ruby>先生<rt>せんせい</rt></ruby>にお<ruby>礼<rt>れい</rt></ruby>の<ruby>手紙<rt>てがみ</rt></ruby>を<ruby>書<rt>か</rt></ruby>きました。<br/>B: きっと<ruby>先生<rt>せんせい</rt></ruby>も<ruby>喜<rt>よろこ</rt></ruby>んでくれますね！",
        "en": "A: I wrote a thank-you letter to the teacher who taught me Japanese. B: I'm sure the teacher will be delighted!",
        "zh_TW": "A: 我寫了一封感謝信給教我日語的老師。 B: 老師一定會非常高興的！",
        "zh_CN": "A: 我写了一封感谢信给教我日语的老师。 B: 老师一定会非常高兴的！",
        "ko": "A: 일본어를 가르쳐 주신 선생님께 감사의 편지를 썼어요. B: 분명 선생님도 기뻐하실 거예요!",
        "zh_HK": "A: 我寫咗封感謝信俾教我日文嘅老師呀。 B: 老師睇到一定會好開心！",
        "fr": "A: J'ai écrit une lettre de remerciement au professeur qui m'a enseigné le japonais. B: Je suis sûr que le professeur sera ravi !"
    },
    "card_0497": { # 練習 (distinct from 0018)
        "ja": "スピーチの<ruby>本番<rt>ほんばん</rt></ruby>に<ruby>向<rt>む</rt></ruby>けて、<ruby>毎日<rt>まいにち</rt></ruby><ruby>家<rt>いえ</rt></ruby>で<ruby>大<rt>おお</rt></ruby>きな<ruby>声<rt>こえ</rt></ruby>で<ruby>練習<rt>れんしゅう</rt></ruby>しています。",
        "en": "In preparation for the actual speech, I practice out loud every day at home.",
        "zh_TW": "為了演講正式上場，我每天都在家大聲練習。",
        "zh_CN": "为了演讲正式上场，我每天都在家大声练习。",
        "ko": "스피치 실전을 위해 매일 집에서 큰 소리로 연습하고 있습니다.",
        "zh_HK": "為咗演講嘅正式發表，我每日喺屋企都好大聲噉練習。",
        "fr": "Pour préparer mon discours officiel, je m'entraîne à voix haute chaque jour chez moi."
    },
    "card_0068": { # 大丈夫です (distinct from 0040)
        "ja": "A: <ruby>少<rt>すこ</rt></ruby>し<ruby>熱<rt>ねつ</rt></ruby>があるようですが、<ruby>体調<rt>たいちょう</rt></ruby>は<ruby>大丈夫<rt>だいじょうぶ</rt></ruby>ですか？<br/>B: <ruby>心配<rt>しんぱい</rt></ruby>してくれてありがとう。<ruby>薬<rt>くすり</rt></ruby>を<ruby>飲<rt>の</rt></ruby>んだので<ruby>大丈夫<rt>だいじょうぶ</rt></ruby>です。",
        "en": "A: You seem to have a slight fever, are you alright? B: Thank you for worrying about me. I took some medicine, so I'm okay.",
        "zh_TW": "A: 你看起來有點發燒，身體還好嗎？ B: 謝謝你的關心。我已經吃了藥，所以沒事了。",
        "zh_CN": "A: 你看起来有点发烧，身体还好吗？ B: 谢谢你的关心。我已经吃了药，所以没事了。",
        "ko": "A: 열이 조금 있는 것 같은데, 몸 상태는 괜찮으세요? B: 걱정해 줘서 고마워요. 약을 먹어서 괜찮습니다.",
        "zh_HK": "A: 你好似有啲發燒噉喎，身體頂唔頂得順呀？ B: 多謝你關心。我食咗藥喇，冇事嘅。",
        "fr": "A: Vous semblez avoir un peu de fièvre, ça va ? B: Merci de vous inquiéter. J'ai pris des médicaments, donc tout va bien."
    },
    "card_0486": { # 仕事 (distinct from 0168)
        "ja": "<ruby>新<rt>あたら</rt></ruby>しい<ruby>仕事<rt>しごと</rt></ruby>にも<ruby>少<rt>すこ</rt></ruby>しずつ<ruby>慣<rt>な</rt></ruby>れてきて、<ruby>毎日<rt>まいにち</rt></ruby>とても<ruby>充実<rt>じゅうじつ</rt></ruby>しています。",
        "en": "I'm gradually getting used to my new job, and every day feels very fulfilling.",
        "zh_TW": "我也逐漸習慣了新工作，每天都過得非常充實。",
        "zh_CN": "我也逐渐习惯了新工作，每天都过得非常充实。",
        "ko": "새로운 일에도 조금씩 익숙해져서 매일 매우 충실하게 보내고 있습니다.",
        "zh_HK": "我漸漸適應咗新嘅工作，每日都過得好充實。",
        "fr": "Je m'habitue peu à peu à mon nouveau travail et chaque jour est très épanouissant."
    },
    "card_0351": { # たった今 (distinct from 0350)
        "ja": "A: <ruby>田中<rt>たなか</rt></ruby>さん、もう<ruby>出<rt>で</rt></ruby>かけましたか？<br/>B: はい、たった<ruby>今<rt>いま</rt></ruby>タクシーに<ruby>乗<rt>の</rt></ruby>って<ruby>空港<rt>くうこう</rt></ruby>へ<ruby>向<rt>む</rt></ruby>かいました。",
        "en": "A: Has Mr. Tanaka already left? B: Yes, he just took a taxi and headed for the airport.",
        "zh_TW": "A: 田中先生已經出發了嗎？ B: 是的，他剛剛才搭上計程車前往機場。",
        "zh_CN": "A: 田中先生已经出发了吗？ B: 是的，他刚才搭乘出租车前往机场。",
        "ko": "A: 다나카 씨는 벌써 출발했나요? B: 네, 방금 택시를 타고 공항으로 향했습니다.",
        "zh_HK": "A: 田中生已經出發咗喇？ B: 係呀，佢啱啱搭的士出發去機場喇。",
        "fr": "A: M. Tanaka est-il déjà parti ? B: Oui, il vient tout juste de prendre un taxi pour l'aéroport."
    },
    "card_0419": { # あとで (distinct from 0354)
        "ja": "A: この<ruby>書類<rt>しょるい</rt></ruby>のチェック、お<ruby>願<rt>ねが</rt></ruby>いできますか？<br/>B: <ruby>今<rt>いま</rt></ruby><ruby>手<rt>て</rt></ruby>が<ruby>離<rt>はな</rt></ruby>せないので、30<ruby>分<rt>ぷん</rt></ruby>ほどあとで<ruby>見<rt>み</rt></ruby>てもいいですか？",
        "en": "A: Could you check these documents? B: I have my hands full right now, could I look at them in about 30 minutes?",
        "zh_TW": "A: 可以請您幫忙確認這份文件嗎？ B: 我現在走不開，可以等大約30分鐘後再看嗎？",
        "zh_CN": "A: 可以请您帮忙确认这份文件吗？ B: 我现在抽不开身，可以等大约30分钟后再看吗？",
        "ko": "A: 이 서류 확인을 부탁드려도 될까요? B: 지금 손이 바빠서 그런데, 30분쯤 뒤에 봐도 될까요?",
        "zh_HK": "A: 唔該可唔可以幫手check下呢份文件呀？ B: 我而家做緊嘢走唔開，等半個鐘後先睇得唔得？",
        "fr": "A: Pourriez-vous vérifier ces documents ? B: Je suis occupé pour l'instant, puis-je les regarder dans environ 30 minutes ?"
    },
    "card_0422": { # もうすぐ (distinct from 0355)
        "ja": "もうすぐ<ruby>待<rt>ま</rt></ruby>ちに<ruby>待<rt>ま</rt></ruby>ったゴールデンウィークですね。<ruby>旅行<rt>りょこう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きますか？",
        "en": "The long-awaited Golden Week is coming very soon. Are you going on a trip?",
        "zh_TW": "期待已久的黃金週就快要到了呢。你有要去哪裡旅行嗎？",
        "zh_CN": "期待已久的黄金周马上就要到了呢。你有要去哪里旅行吗？",
        "ko": "이제 곧 기다리고 기다리던 골든위크네요. 여행 가시나요?",
        "zh_HK": "期待已久嘅黃金週就快到喇。你會去旅行嗎？",
        "fr": "La Golden Week tant attendue arrive bientôt. Allez-vous partir en voyage ?"
    },
    "card_0485": { # 勉強 (distinct from 0375)
        "ja": "<ruby>将来<rt>しょうらい</rt></ruby><ruby>日本<rt>にほん</rt></ruby>で<ruby>働<rt>はたら</rt></ruby>くために、<ruby>毎晩<rt>まいばん</rt></ruby><ruby>仕事<rt>しごと</rt></ruby>の<ruby>後<rt>あと</rt></ruby>に<ruby>日本語<rt>にほんご</rt></ruby>の<ruby>勉強<rt>べんきょう</rt></ruby>をしています。",
        "en": "To work in Japan in the future, I study Japanese every night after work.",
        "zh_TW": "為了將來能在日本工作，我每天下班後都會讀日語。",
        "zh_CN": "为了将来能在日本工作，我每天下班后都会学日语。",
        "ko": "앞으로 일본에서 일하기 위해 매일 밤 퇴근 후에 일본어 공부를 하고 있습니다.",
        "zh_HK": "為咗將來可以喺日本做嘢，我每晚收工之後都會溫日文。",
        "fr": "Pour travailler au Japon à l'avenir, j'étudie le japonais chaque soir après le travail."
    },
    "card_0704": { # 勉強をして (distinct from 0375)
        "ja": "<ruby>図書館<rt>としょかん</rt></ruby>で<ruby>集中<rt>しゅうちゅう</rt></ruby>して<ruby>勉強<rt>べんきょう</rt></ruby>をしてから、<ruby>友達<rt>ともだち</rt></ruby>とお<ruby>茶<rt>ちゃ</rt></ruby>を<ruby>飲<rt>の</rt></ruby>みに<ruby>行<rt>い</rt></ruby>きました。",
        "en": "After studying hard at the library, I went to have tea with my friend.",
        "zh_TW": "在圖書館專心讀完書後，我和朋友一起去喝了茶。",
        "zh_CN": "在图书馆专心学习之后，我和朋友一起去喝了茶。",
        "ko": "도서관에서 집중해서 공부를 하고 나서, 친구와 차를 마시러 갔습니다.",
        "zh_HK": "喺圖書館專心讀完書之後，我同朋友去咗飲茶傾計。",
        "fr": "Après avoir étudié intensément à la bibliothèque, je suis allé prendre un thé avec un ami."
    },
    "card_0733": { # 歩いて (distinct from 0410)
        "ja": "<ruby>健康<rt>けんこう</rt></ruby>のために、<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>一駅<rt>ひとえき</rt></ruby><ruby>手前<rt>てまえ</rt></ruby>で<ruby>降<rt>お</rt></ruby>りて<ruby>歩<rt>ある</rt></ruby>いて<ruby>会社<rt>かいしゃ</rt></ruby>へ<ruby>通<rt>かよ</rt></ruby>っています。",
        "en": "For my health, I get off one station early every morning and walk to work.",
        "zh_TW": "為了健康，我每天早上都提早一站下車，走路去上班。",
        "zh_CN": "为了健康，我每天早上都提前一站下车，走路去上班。",
        "ko": "건강을 위해 매일 아침 한 정거장 전에 내려서 걸어서 출근합니다.",
        "zh_HK": "為咗健康，我每日朝早都提早一個站落車，行路去返工。",
        "fr": "Pour ma santé, je descends une station plus tôt chaque matin et vais au travail à pied."
    },
    "card_0605": { # 旅行 (fixed 海の幸 reading & unique sentence)
        "ja": "<ruby>今年<rt>ことし</rt></ruby>の<ruby>夏休<rt>なつやす</rt></ruby>みは、<ruby>友人<rt>ゆうじん</rt></ruby>と<ruby>一緒<rt>いっしょ</rt></ruby>に<ruby>沖縄<rt>おきなわ</rt></ruby>へ3<ruby>泊<rt>はく</rt></ruby>4<ruby>日<rt>よっか</rt></ruby>の<ruby>旅行<rt>りょこう</rt></ruby>に<ruby>行<rt>い</rt></ruby>く<ruby>予定<rt>よてい</rt></ruby>です。",
        "en": "For this summer vacation, I plan to go on a four-day, three-night trip to Okinawa with my friend.",
        "zh_TW": "今年暑假，我打算和朋友一起去沖繩來一趟四天三夜的旅行。",
        "zh_CN": "今年暑假，我打算和朋友一起去冲绳来一趟四天三夜的旅行。",
        "ko": "올해 여름휴가는 친구와 함께 오키나와로 3박 4일 여행을 갈 계획입니다.",
        "zh_HK": "今年暑假，我打算同朋友一齊去沖繩玩四日三夜嘅旅行。",
        "fr": "Pour les vacances d'été de cette année, je prévois de faire un voyage de quatre jours et trois nuits à Okinawa avec un ami."
    },
    "card_0601": { # 約束 (distinct from 0499)
        "ja": "A: <ruby>明日<rt>あした</rt></ruby>の<ruby>午後<rt>ごご</rt></ruby>3<ruby>時<rt>じ</rt></ruby>にカフェで<ruby>会<rt>あ</rt></ruby>う<ruby>約束<rt>やくそく</rt></ruby>、<ruby>覚<rt>おぼ</rt></ruby>えていますか？<br/>B: もちろんです！<ruby>楽<rt>たの</rt></ruby>しみにしていますね。",
        "en": "A: Do you remember our promise to meet at the cafe at 3 PM tomorrow? B: Of course! I'm looking forward to it.",
        "zh_TW": "A: 你還記得明天下午3點在咖啡廳見面的約定嗎？ B: 當然記得！我很期待呢。",
        "zh_CN": "A: 你还记得明天下午3点在咖啡馆见面的约定吗？ B: 当然记得！我很期待呢。",
        "ko": "A: 내일 오후 3시에 카페에서 만나기로 한 약속, 기억하시죠? B: 물론이죠! 기대하고 있을게요.",
        "zh_HK": "A: 你仲記唔記得聽日下晝3點喺cafe見面嘅約定呀？ B: 當然記得啦！好期待呢。",
        "fr": "A: Tu te souviens de notre rendez-vous au café demain à 15 heures ? B: Bien sûr ! J'ai hâte d'y être."
    },
    "card_0804": { # 取る (distinct from 0654)
        "ja": "<ruby>棚<rt>たな</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>にある<ruby>箱<rt>はこ</rt></ruby>を<ruby>取<rt>と</rt></ruby>りたいのですが、<ruby>手<rt>て</rt></ruby>が<ruby>届<rt>とど</rt></ruby>かないので<ruby>取<rt>と</rt></ruby>っていただけますか？",
        "en": "I want to get the box from the top of the shelf, but I can't reach it. Could you take it down for me?",
        "zh_TW": "我想拿架子上的盒子，但手搆不到，可以請您幫我拿一下嗎？",
        "zh_CN": "我想拿架子上的盒子，但手够不到，可以请您帮我拿一下吗？",
        "ko": "선반 위에 있는 상자를 꺼내고 싶은데 손이 닿지 않아서요, 좀 꺼내 주시겠어요?",
        "zh_HK": "我想攞櫃頂上面個盒，但我唔夠高，可唔可以幫我攞落嚟呀？",
        "fr": "Je voudrais attraper la boîte sur l'étagère, mais je ne peux pas l'atteindre. Pourriez-vous me la prendre ?"
    },
    "card_0765": { # 話して (distinct from 0715)
        "ja": "<ruby>日本語<rt>にほんご</rt></ruby>のリスニングがまだ<ruby>苦手<rt>にがて</rt></ruby>なので、もう<ruby>少<rt>すこ</rt></ruby>しゆっくりはっきりと<ruby>話<rt>はな</rt></ruby>していただけますか？",
        "en": "I am still not good at Japanese listening, so could you please speak a little more slowly and clearly?",
        "zh_TW": "我的日語聽力還不太好，可以請您說得稍微慢一點、清楚一點嗎？",
        "zh_CN": "我的日语听力还不太好，可以请您说得稍微慢一点、清楚一点吗？",
        "ko": "일본어 듣기가 아직 서툴러서, 조금만 더 천천히 또박또박 말씀해 주실 수 있나요?",
        "zh_HK": "我聽日文仲係麻麻哋，唔該可唔可以講慢啲同清楚啲呀？",
        "fr": "Je ne suis pas encore très bon en compréhension orale du japonais, pourriez-vous parler un peu plus lentement et clairement s'il vous plaît ?"
    },
    "card_0770": { # 出て (distinct from 0729)
        "ja": "<ruby>家<rt>いえ</rt></ruby>を<ruby>出<rt>で</rt></ruby>る<ruby>前<rt>まえ</rt></ruby>に、エアコンのスイッチを<ruby>切<rt>き</rt></ruby>ったかどうか<ruby>確認<rt>かくにん</rt></ruby>してください。",
        "en": "Before leaving the house, please check whether you turned off the air conditioner.",
        "zh_TW": "出門之前，請確認一下冷氣電源是否已經關閉。",
        "zh_CN": "出门之前，请确认一下空调电源是否已经关闭。",
        "ko": "집을 나서기 전에 에어컨 전원을 껐는지 확인해 주세요.",
        "zh_HK": "出門口之前，請check下有冇熄冷氣機。",
        "fr": "Avant de sortir de la maison, veuillez vérifier si vous avez bien éteint le climatiseur."
    },
    "card_0768": { # 教えて (distinct from 0746)
        "ja": "すみません、この<ruby>漢字<rt>かんじ</rt></ruby>の<ruby>読<rt>よ</rt></ruby>み<ruby>方<rt>かた</rt></ruby>と<ruby>意味<rt>いみ</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えていただけませんか？",
        "en": "Excuse me, could you teach me the reading and meaning of this kanji?",
        "zh_TW": "不好意思，可以請教您這個漢字的讀音和意思嗎？",
        "zh_CN": "不好意思，可以请教您这个汉字的读音和意思吗？",
        "ko": "실례지만, 이 한자의 읽는 법과 의미를 가르쳐 주실 수 있나요?",
        "zh_HK": "唔好意思，可唔可以教我呢個漢字點讀同點解呀？",
        "fr": "Excusez-moi, pourriez-vous m'apprendre la prononciation et le sens de ce kanji ?"
    },
    "card_0760": { # 待って (distinct from 0749)
        "ja": "すぐに<ruby>戻<rt>もど</rt></ruby>ってきますので、こちらのベンチに<ruby>座<rt>すわ</rt></ruby>って<ruby>少<rt>すこ</rt></ruby>し<ruby>待<rt>ま</rt></ruby>っていてください。",
        "en": "I will be back right away, so please sit on this bench and wait for a moment.",
        "zh_TW": "我馬上就會回來，請坐在這張長椅上稍等一下喔。",
        "zh_CN": "我马上就会回来，请坐在这张长椅上稍等一下哦。",
        "ko": "금방 돌아올 테니, 이 벤치에 앉아서 잠시 기다려 주세요.",
        "zh_HK": "我好快返嚟㗎，請坐喺呢邊張長凳度等一陣啦。",
        "fr": "Je reviens tout de suite, alors veuillez vous asseoir sur ce banc et m'attendre un instant."
    }
}

print(f"Defined {len(INITIAL_REPLACEMENTS)} fixes for INITIAL_VOCAB_DATA")
with open("scripts/initial_replacements_stage2.json", "w", encoding="utf-8") as f:
    json.dump(INITIAL_REPLACEMENTS, f, ensure_ascii=False, indent=2)
print("Saved scripts/initial_replacements_stage2.json")
EOF = None
