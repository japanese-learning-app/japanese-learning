# -*- coding: utf-8 -*-
"""
Script to apply complete verb form alignment, sensitive term removal,
and 100% accurate furigana and multi-language translations.
"""
import json
import re

# Update map: card_id -> { 'example': { 'ja': ..., 'en': ..., 'zh_TW': ..., 'zh_CN': ..., 'ko': ..., 'zh_HK': ..., 'fr': ... } }
REVISIONS = {}

# -------------------------------------------------------------
# 1. 基本動詞(1)〜(5) 〜ます形の統一・修正
# -------------------------------------------------------------
# card_0374 起きる・起きます
REVISIONS["card_0374"] = {
    "example": {
        "ja": "<ruby>毎朝<rt>まいあさ</rt></ruby>6<ruby>時<rt>じ</rt></ruby>に<ruby>起<rt>お</rt></ruby>きます。",
        "en": "I wake up at 6 o'clock every morning.",
        "zh_TW": "我每天早上六點起床。",
        "zh_CN": "我每天早上六点起床。",
        "ko": "매일 아침 6시에 일어납니다.",
        "zh_HK": "我每日朝早六點起身。",
        "fr": "Je me lève à 6 heures tous les matins."
    }
}
# card_0375 勉強をする・勉強をします
REVISIONS["card_0375"] = {
    "example": {
        "ja": "<ruby>毎日<rt>まいにち</rt></ruby>2<ruby>時間<rt>じかん</rt></ruby><ruby>日本語<rt>にほんご</rt></ruby>の<ruby>勉強<rt>べんきょう</rt></ruby>をします。",
        "en": "I study Japanese for two hours every day.",
        "zh_TW": "我每天學兩個小時日語。",
        "zh_CN": "我每天学两个小时日语。",
        "ko": "매일 2시간 일본어 공부를 합니다.",
        "zh_HK": "我每日讀兩個鐘頭日文。",
        "fr": "J'étudie le japonais pendant deux heures tous les jours."
    }
}
# card_0377 帰る・帰ります
REVISIONS["card_0377"] = {
    "example": {
        "ja": "<ruby>仕事<rt>しごと</rt></ruby>が<ruby>終<rt>お</rt></ruby>わったら、まっすぐ<ruby>家<rt>いえ</rt></ruby>へ<ruby>帰<rt>かえ</rt></ruby>ります。",
        "en": "When work is finished, I go straight home.",
        "zh_TW": "工作結束後，我直接回家。",
        "zh_CN": "工作结束后，我直接回家。",
        "ko": "일이 끝나면 바로 집으로 돌아갑니다.",
        "zh_HK": "做完嘢之後，我直接返屋企。",
        "fr": "Une fois le travail terminé, je rentre directement chez moi."
    }
}
# card_0380 飲む・飲みます
REVISIONS["card_0380"] = {
    "example": {
        "ja": "<ruby>食後<rt>しょくご</rt></ruby>に<ruby>温<rt>あたた</rt></ruby>かいお<ruby>茶<rt>ちゃ</rt></ruby>を<ruby>飲<rt>の</rt></ruby>みます。",
        "en": "I drink hot tea after meals.",
        "zh_TW": "飯後喝熱茶。",
        "zh_CN": "饭后喝热茶。",
        "ko": "식사 후에 따뜻한 차를 마십니다.",
        "zh_HK": "食完飯之後飲熱茶。",
        "fr": "Je bois du thé chaud après le repas."
    }
}
# card_0383 聞く・聞きます
REVISIONS["card_0383"] = {
    "example": {
        "ja": "<ruby>先生<rt>せんせい</rt></ruby>に<ruby>日本語<rt>にほんご</rt></ruby>の<ruby>発音<rt>はつおん</rt></ruby>を<ruby>聞<rt>き</rt></ruby>きます。",
        "en": "I ask the teacher about Japanese pronunciation.",
        "zh_TW": "向老師請教日語發音。",
        "zh_CN": "向老师请教日语发音。",
        "ko": "선생님께 일본어 발음을 묻습니다.",
        "zh_HK": "問老師日文發音。",
        "fr": "Je demande au professeur la prononciation du japonais."
    }
}
# card_0388 買う・買います
REVISIONS["card_0388"] = {
    "example": {
        "ja": "コンビニで<ruby>昼<rt>ひる</rt></ruby>ごはんのお<ruby>弁当<rt>べんとう</rt></ruby>を<ruby>買<rt>か</rt></ruby>います。",
        "en": "I buy a bento lunch at the convenience store.",
        "zh_TW": "在便利店買午餐便當。",
        "zh_CN": "在便利店买午餐便当。",
        "ko": "편의점에서 점심 도시락을 삽니다.",
        "zh_HK": "喺便利店買晏晝便當。",
        "fr": "J'achète un bento pour le déjeuner au kombini."
    }
}
# card_0392 働く・働きます
REVISIONS["card_0392"] = {
    "example": {
        "ja": "<ruby>月曜日<rt>げつようび</rt></ruby>から<ruby>金曜日<rt>きんようび</rt></ruby>まで<ruby>会社<rt>かいしゃ</rt></ruby>で<ruby>働<rt>はたら</rt></ruby>きます。",
        "en": "I work at the company from Monday to Friday.",
        "zh_TW": "週一到週五在公司上班。",
        "zh_CN": "周一到周五在公司上班。",
        "ko": "월요일부터 금요일까지 회사에서 일합니다.",
        "zh_HK": "由禮拜一到禮拜五喺公司返工。",
        "fr": "Je travaille à l'entreprise du lundi au vendredi."
    }
}
# card_0393 驚く・驚きます
REVISIONS["card_0393"] = {
    "example": {
        "ja": "マジックを<ruby>見<rt>み</rt></ruby>てとても<ruby>驚<rt>おどろ</rt></ruby>きます。",
        "en": "I am very surprised when I see magic tricks.",
        "zh_TW": "看了魔術表演非常驚訝。",
        "zh_CN": "看了魔术表演非常惊讶。",
        "ko": "마술을 보고 매우 놀랍니다.",
        "zh_HK": "睇到魔術表演好驚訝。",
        "fr": "Je suis très surpris en voyant des tours de magie."
    }
}
# card_0394 忘れる・忘れます
REVISIONS["card_0394"] = {
    "example": {
        "ja": "<ruby>約束<rt>やくそく</rt></ruby>の<ruby>時間<rt>じかん</rt></ruby>を<ruby>時々<rt>ときどき</rt></ruby><ruby>忘<rt>わす</rt></ruby>れます。",
        "en": "I sometimes forget the appointment time.",
        "zh_TW": "我有時會忘記約定好的時間。",
        "zh_CN": "我有时期会忘记约好的时间。",
        "ko": "약속 시간을 가끔 잊어버립니다.",
        "zh_HK": "我有時會唔記得約好嘅時間。",
        "fr": "J'oublie parfois l'heure du rendez-vous."
    }
}

# 基本動詞(2): ひらがな表記の漢字化および〜ます形統一
# card_0460 出る・出ます
REVISIONS["card_0460"] = {
    "example": {
        "ja": "<ruby>朝<rt>あさ</rt></ruby>7<ruby>時<rt>じ</rt></ruby>に<ruby>家<rt>いえ</rt></ruby>を<ruby>出<rt>で</rt></ruby>ます。",
        "en": "I leave the house at 7 AM.",
        "zh_TW": "早上七點出門。",
        "zh_CN": "早上七点出门。",
        "ko": "아침 7시에 집을 나섭니다.",
        "zh_HK": "朝早七點出門口。",
        "fr": "Je quitte la maison à 7 heures du matin."
    }
}
# card_0461 入る・入ります
REVISIONS["card_0461"] = {
    "example": {
        "ja": "<ruby>部屋<rt>へや</rt></ruby>に<ruby>入<rt>はい</rt></ruby>ります。",
        "en": "I enter the room.",
        "zh_TW": "進入房間。",
        "zh_CN": "进入房间。",
        "ko": "방에 들어갑니다.",
        "zh_HK": "入房。",
        "fr": "J'entre dans la pièce."
    }
}
# card_0462 着く・着きます
REVISIONS["card_0462"] = {
    "example": {
        "ja": "もうすぐ<ruby>東京<rt>とうきょう</rt></ruby><ruby>駅<rt>えき</rt></ruby>に<ruby>着<rt>つ</rt></ruby>きます。",
        "en": "We will arrive at Tokyo Station soon.",
        "zh_TW": "馬上就要到達東京站了。",
        "zh_CN": "马上就要到达东京站了。",
        "ko": "곧 도쿄역에 도착합니다.",
        "zh_HK": "好快就到東京站喇。",
        "fr": "Nous arriverons bientôt à la gare de Tokyo."
    }
}
# card_0463 渡る・渡ります
REVISIONS["card_0463"] = {
    "example": {
        "ja": "<ruby>青信号<rt>あおしんごう</rt></ruby>で<ruby>横断歩道<rt>おうだんほどう</rt></ruby>を<ruby>渡<rt>わた</rt></ruby>ります。",
        "en": "I cross the pedestrian crossing at the green light.",
        "zh_TW": "綠燈時走斑馬線過馬路。",
        "zh_CN": "绿灯时走斑马线过马路。",
        "ko": "파란불에 횡단보도를 건넙니다.",
        "zh_HK": "綠燈嗰陣過斑馬線。",
        "fr": "Je traverse le passage piéton au feu vert."
    }
}
# card_0464 歩く・歩きます
REVISIONS["card_0464"] = {
    "example": {
        "ja": "<ruby>健康<rt>けんこう</rt></ruby>のために<ruby>毎日<rt>まいにち</rt></ruby>30<ruby>分<rt>ぷん</rt></ruby><ruby>歩<rt>ある</rt></ruby>きます。",
        "en": "I walk for 30 minutes every day for my health.",
        "zh_TW": "為了健康，我每天散步30分鐘。",
        "zh_CN": "为了健康，我每天散步30分钟。",
        "ko": "건강을 위해 매일 30분 걷습니다.",
        "zh_HK": "為咗健康，我每日行路30分鐘。",
        "fr": "Je marche 30 minutes tous les jours pour la santé."
    }
}
# card_0465 走る・走ります
REVISIONS["card_0465"] = {
    "example": {
        "ja": "<ruby>公園<rt>こうえん</rt></ruby>のコースを<ruby>走<rt>はし</rt></ruby>ります。",
        "en": "I run along the park course.",
        "zh_TW": "在公園的跑步道上跑步。",
        "zh_CN": "在公园的跑步道上跑步。",
        "ko": "공원의 코스를 달립니다.",
        "zh_HK": "喺公園嘅緩跑徑跑步。",
        "fr": "Je cours sur la piste du parc."
    }
}
# card_0466 起こす・起こします
REVISIONS["card_0466"] = {
    "example": {
        "ja": "<ruby>毎朝<rt>まいあさ</rt></ruby>7<ruby>時<rt>じ</rt></ruby>に<ruby>弟<rt>おとうと</rt></ruby>を<ruby>起<rt>お</rt></ruby>こします。",
        "en": "I wake up my younger brother at 7 every morning.",
        "zh_TW": "我每天早上七點叫弟弟起床。",
        "zh_CN": "我每天早上七点叫弟弟起床。",
        "ko": "매일 아침 7시에 남동생을 깨웁니다.",
        "zh_HK": "我每日朝早七點叫細佬起身。",
        "fr": "Je réveille mon petit frère à 7 heures tous les matins."
    }
}
# card_0467 洗う・洗います
REVISIONS["card_0467"] = {
    "example": {
        "ja": "ご<ruby>飯<rt>はん</rt></ruby>を<ruby>食<rt>た</rt></ruby>べる<ruby>前<rt>まえ</rt></ruby>に、<ruby>手<rt>て</rt></ruby>をしっかり<ruby>洗<rt>あら</rt></ruby>います。",
        "en": "I wash my hands thoroughly before eating.",
        "zh_TW": "吃飯前會好好洗手。",
        "zh_CN": "吃饭前会好好洗手。",
        "ko": "밥을 먹기 전에 손을 깨끗이 씻습니다.",
        "zh_HK": "食飯之前會洗乾淨手。",
        "fr": "Je me lave bien les mains avant de manger."
    }
}
# card_0468 着る・着ます (※修正: 誤データ修正)
REVISIONS["card_0468"] = {
    "example": {
        "ja": "<ruby>寒<rt>さむ</rt></ruby>い<ruby>日<rt>ひ</rt></ruby>は<ruby>暖<rt>あたた</rt></ruby>かいコートを<ruby>着<rt>き</rt></ruby>ます。",
        "en": "I wear a warm coat on cold days.",
        "zh_TW": "寒冷的日子裡我會穿上溫暖的大衣。",
        "zh_CN": "寒冷的日子里我会穿上温暖的大衣。",
        "ko": "추운 날에는 따뜻한 코트를 입습니다.",
        "zh_HK": "凍嗰陣我會著暖笠笠嘅褸。",
        "fr": "Je porte un manteau chaud les jours de froid."
    }
}
# card_0469 脱ぐ・脱ぎます
REVISIONS["card_0469"] = {
    "example": {
        "ja": "<ruby>玄関<rt>げんかん</rt></ruby>で<ruby>靴<rt>くつ</rt></ruby>を<ruby>脱<rt>ぬ</rt></ruby>ぎます。",
        "en": "I take off my shoes at the entrance.",
        "zh_TW": "在玄關脫鞋。",
        "zh_CN": "在玄关脱鞋。",
        "ko": "현관에서 신발을 벗습니다.",
        "zh_HK": "喺玄關除鞋。",
        "fr": "J'enlève mes chaussures à l'entrée."
    }
}
# card_0470 開ける・開けます
REVISIONS["card_0470"] = {
    "example": {
        "ja": "<ruby>部屋<rt>へや</rt></ruby>の<ruby>窓<rt>まど</rt></ruby>を<ruby>開<rt>あ</rt></ruby>けます。",
        "en": "I open the window of the room.",
        "zh_TW": "打開房間的窗戶。",
        "zh_CN": "打开房间的窗户。",
        "ko": "방 창문을 엽니다.",
        "zh_HK": "開房嘅窗。",
        "fr": "J'ouvre la fenêtre de la pièce."
    }
}
# card_0471 閉める・閉めます
REVISIONS["card_0471"] = {
    "example": {
        "ja": "<ruby>出掛<rt>でか</rt></ruby>ける<ruby>前<rt>まえ</rt></ruby>にドアを<ruby>閉<rt>し</rt></ruby>めます。",
        "en": "I close the door before leaving.",
        "zh_TW": "出門前把門關好。",
        "zh_CN": "出门前把门关好。",
        "ko": "외출하기 전에 문을 닫습니다.",
        "zh_HK": "出門口之前閂好門。",
        "fr": "Je ferme la porte avant de sortir."
    }
}
# card_0472 使う・使います
REVISIONS["card_0472"] = {
    "example": {
        "ja": "<ruby>授業<rt>じゅぎょう</rt></ruby>で<ruby>辞書<rt>じしょ</rt></ruby>を<ruby>使<rt>つか</rt></ruby>います。",
        "en": "I use a dictionary in class.",
        "zh_TW": "上課時使用詞典。",
        "zh_CN": "上课时使用词典。",
        "ko": "수업 시간에 사전을 사용합니다.",
        "zh_HK": "上堂嗰陣用字典。",
        "fr": "J'utilise un dictionnaire pendant le cours."
    }
}
# card_0473 作る・作ります
REVISIONS["card_0473"] = {
    "example": {
        "ja": "<ruby>休日<rt>きゅうじつ</rt></ruby>は<ruby>手作<rt>てづく</rt></ruby>りのパスタを<ruby>作<rt>つく</rt></ruby>ります。",
        "en": "I make homemade pasta on days off.",
        "zh_TW": "休息日我會親手做意大利麵。",
        "zh_CN": "休息日我会亲手做意大利面。",
        "ko": "휴일에는 수제 파스타를 만듭니다.",
        "zh_HK": "放假嗰陣我會自己煮意粉。",
        "fr": "Je fais des pâtes maison les jours de repos."
    }
}
# card_0474 切る・切ります
REVISIONS["card_0474"] = {
    "example": {
        "ja": "<ruby>包丁<rt>ほうちょう</rt></ruby>で<ruby>野菜<rt>やさい</rt></ruby>を<ruby>切<rt>き</rt></ruby>ります。",
        "en": "I cut vegetables with a kitchen knife.",
        "zh_TW": "用菜刀切蔬菜。",
        "zh_CN": "用菜刀切蔬菜。",
        "ko": "칼로 야채를 썹니다.",
        "zh_HK": "用菜刀切菜。",
        "fr": "Je coupe des légumes avec un couteau de cuisine."
    }
}
# card_0475 書く・書きます
REVISIONS["card_0475"] = {
    "example": {
        "ja": "<ruby>友達<rt>ともだち</rt></ruby>に<ruby>手紙<rt>てがみ</rt></ruby>を<ruby>書<rt>か</rt></ruby>きます。",
        "en": "I write a letter to a friend.",
        "zh_TW": "給朋友寫信。",
        "zh_CN": "给朋友写信。",
        "ko": "친구에게 편지를 씁니다.",
        "zh_HK": "寫信畀朋友。",
        "fr": "J'écris une lettre à un ami."
    }
}
# card_0476 答える・答えます
REVISIONS["card_0476"] = {
    "example": {
        "ja": "<ruby>先生<rt>せんせい</rt></ruby>の<ruby>質問<rt>しつもん</rt></ruby>に<ruby>日本語<rt>にほんご</rt></ruby>で<ruby>答<rt>こた</rt></ruby>えます。",
        "en": "I answer the teacher's question in Japanese.",
        "zh_TW": "用日語回答老師的問題。",
        "zh_CN": "用日语回答老师的问题。",
        "ko": "선생님의 질문에 일본어로 대답합니다.",
        "zh_HK": "用日文答老師嘅問題。",
        "fr": "Je réponds à la question du professeur en japonais."
    }
}
# card_0477 教える・教えます
REVISIONS["card_0477"] = {
    "example": {
        "ja": "<ruby>駅<rt>えき</rt></ruby>までの<ruby>道<rt>みち</rt></ruby>を<ruby>親切<rt>しんせつ</rt></ruby>に<ruby>教<rt>おし</rt></ruby>えます。",
        "en": "I kindly show the way to the station.",
        "zh_TW": "熱情地告訴去車站的路。",
        "zh_CN": "热情地告诉去车站的路。",
        "ko": "역으로 가는 길을 친절하게 가르쳐 줍니다.",
        "zh_HK": "好熱心咁教去車站嘅路。",
        "fr": "J'indique gentiment le chemin de la gare."
    }
}
# card_0478 聞こえる・聞こえます
REVISIONS["card_0478"] = {
    "example": {
        "ja": "<ruby>隣<rt>となり</rt></ruby>の<ruby>部屋<rt>へや</rt></ruby>から<ruby>楽<rt>たの</rt></ruby>しそうな<ruby>声<rt>こえ</rt></ruby>が<ruby>聞<rt>き</rt></ruby>こえます。",
        "en": "I hear cheerful voices from the next room.",
        "zh_TW": "從隔壁房間傳來歡快的聲音。",
        "zh_CN": "从隔壁房间传来欢快的声音。",
        "ko": "옆방에서 즐거운 목소리가 들립니다.",
        "zh_HK": "隔離房傳嚟好開心嘅聲。",
        "fr": "J'entends des voix joyeuses venant de la pièce voisine."
    }
}
# card_0479 見える・見えます
REVISIONS["card_0479"] = {
    "example": {
        "ja": "ここから<ruby>富士山<rt>ふじさん</rt></ruby>がよく<ruby>見<rt>み</rt></ruby>えます。",
        "en": "Mount Fuji is clearly visible from here.",
        "zh_TW": "從這裡能清楚看到富士山。",
        "zh_CN": "从这里能清楚看到富士山。",
        "ko": "여기서 후지산이 잘 보입니다.",
        "zh_HK": "喺呢度好清楚睇到富士山。",
        "fr": "On voit très bien le mont Fuji d'ici."
    }
}
# card_0480 待つ・待ちます
REVISIONS["card_0480"] = {
    "example": {
        "ja": "<ruby>駅<rt>えき</rt></ruby>のカフェで<ruby>友達<rt>ともだち</rt></ruby>を<ruby>待<rt>ま</rt></ruby>ちます。",
        "en": "I wait for my friend at the station cafe.",
        "zh_TW": "在車站的咖啡館等朋友。",
        "zh_CN": "在车站的咖啡馆等朋友。",
        "ko": "역 카페에서 친구를 기다립니다.",
        "zh_HK": "喺車站間cafe等朋友。",
        "fr": "J'attends mon ami au café de la gare."
    }
}
# card_0482 知る・知ります
REVISIONS["card_0482"] = {
    "example": {
        "ja": "ニュースを<ruby>見<rt>み</rt></ruby>てそのことを<ruby>知<rt>し</rt></ruby>ります。",
        "en": "I learn about it by watching the news.",
        "zh_TW": "看新聞得知了這件事。",
        "zh_CN": "看新闻得知了这件事。",
        "ko": "뉴스를 보고 그 사실을 압니다.",
        "zh_HK": "睇新聞知道咗呢件事。",
        "fr": "J'apprends cette nouvelle en regardant les informations."
    }
}
# card_0483 わかる・わかります
REVISIONS["card_0483"] = {
    "example": {
        "ja": "<ruby>説明<rt>せつめい</rt></ruby>を<ruby>聞<rt>き</rt></ruby>いて、<ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>がよくわかります。",
        "en": "After listening to the explanation, I understand how to use it well.",
        "zh_TW": "聽了說明後，很清楚使用方法了。",
        "zh_CN": "听了说明后，很清楚使用方法了。",
        "ko": "설명을 듣고 사용법을 잘 알겠습니다.",
        "zh_HK": "聽完解釋之後，好明白點樣用。",
        "fr": "Après avoir écouté l'explication, je comprends bien comment l'utiliser."
    }
}

# 基本動詞(3): ます形統一
# card_0646 泳ぐ・泳ぎます
REVISIONS["card_0646"] = {
    "example": {
        "ja": "<ruby>夏休<rt>なつやす</rt></ruby>みに<ruby>海<rt>うみ</rt></ruby>でたくさん<ruby>泳<rt>およ</rt></ruby>ぎます。",
        "en": "I swim a lot in the sea during summer vacation.",
        "zh_TW": "暑假在海裡暢快游泳。",
        "zh_CN": "暑假在海里畅快游泳。",
        "ko": "여름방학에 바다에서 많이 수영합니다.",
        "zh_HK": "暑假喺海入面游好多水。",
        "fr": "Je nage beaucoup dans la mer pendant les vacances d'été."
    }
}
# card_0647 疲れる・疲れます
REVISIONS["card_0647"] = {
    "example": {
        "ja": "たくさん<ruby>歩<rt>ある</rt></ruby>くと<ruby>足<rt>あし</rt></ruby>が<ruby>疲<rt>つか</rt></ruby>れます。",
        "en": "My legs get tired when I walk a lot.",
        "zh_TW": "走很多路的話腳會累。",
        "zh_CN": "走很多路的话脚会累。",
        "ko": "많이 걸으면 다리가 피곤해집니다.",
        "zh_HK": "行好多路隻腳會攰。",
        "fr": "Mes jambes se fatiguent quand je marche beaucoup."
    }
}
# card_0649 つける・つけます
REVISIONS["card_0649"] = {
    "example": {
        "ja": "<ruby>部屋<rt>へや</rt></ruby>が<ruby>暗<rt>くら</rt></ruby>いので<ruby>電気<rt>でんき</rt></ruby>をつけます。",
        "en": "The room is dark, so I turn on the light.",
        "zh_TW": "房間很暗，所以開燈。",
        "zh_CN": "房间很暗，所以开灯。",
        "ko": "방이 어두워서 불을 켭니다.",
        "zh_HK": "間房好黑，所以開燈。",
        "fr": "La pièce est sombre, alors j'allume la lumière."
    }
}
# card_0651 急ぐ・急ぎます
REVISIONS["card_0651"] = {
    "example": {
        "ja": "<ruby>電車<rt>でんしゃ</rt></ruby>の<ruby>時間<rt>じかん</rt></ruby>に<ruby>遅<rt>おく</rt></ruby>れそうなので<ruby>急<rt>いそ</rt></ruby>ぎます。",
        "en": "I hurry because I might be late for the train.",
        "zh_TW": "快要趕不上電車了，所以趕快走。",
        "zh_CN": "快要赶不上电车了，所以赶快走。",
        "ko": "기차 시간에 늦을 것 같아 서두릅니다.",
        "zh_HK": "差唔多趕唔切搭火車，所以行快啲。",
        "fr": "Je me dépêche parce que je risque de rater le train."
    }
}
# card_0652 待つ・待ちます
REVISIONS["card_0652"] = {
    "example": {
        "ja": "<ruby>駅<rt>えき</rt></ruby>の<ruby>改札<rt>かいさつ</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>で<ruby>友達<rt>ともだち</rt></ruby>を<ruby>待<rt>ま</rt></ruby>ちます。",
        "en": "I wait for my friend in front of the station ticket gate.",
        "zh_TW": "在車站剪票口前等朋友。",
        "zh_CN": "在车站检票口前等朋友。",
        "ko": "역 개찰구 앞에서 친구를 기다립니다.",
        "zh_HK": "喺車站入閘機前面等朋友。",
        "fr": "J'attends mon ami devant les portillons de la gare."
    }
}
# card_0653 持つ・持ちます
REVISIONS["card_0653"] = {
    "example": {
        "ja": "<ruby>重<rt>おも</rt></ruby>い<ruby>荷物<rt>にもつ</rt></ruby>を<ruby>私<rt>わたし</rt></ruby>が<ruby>持<rt>も</rt></ruby>ちます。",
        "en": "I will carry the heavy luggage.",
        "zh_TW": "沈重的行李由我來拿。",
        "zh_CN": "沉重的行李由我来拿。",
        "ko": "무거운 짐은 제가 들겠습니다.",
        "zh_HK": "重嘅行李等我拎啦。",
        "fr": "Je porte les bagages lourds."
    }
}
# card_0654 取る・取ります
REVISIONS["card_0654"] = {
    "example": {
        "ja": "テーブルの<ruby>上<rt>うえ</rt></ruby>の<ruby>塩<rt>しお</rt></ruby>を<ruby>取<rt>と</rt></ruby>ります。",
        "en": "I take the salt on the table.",
        "zh_TW": "拿桌子上的鹽。",
        "zh_CN": "拿桌子上的盐。",
        "ko": "테이블 위의 소금을 집습니다.",
        "zh_HK": "拎枱上面嘅鹽。",
        "fr": "Je prends le sel sur la table."
    }
}
# card_0655 手伝う・手伝います
REVISIONS["card_0655"] = {
    "example": {
        "ja": "<ruby>料理<rt>りょうり</rt></ruby>の<ruby>準備<rt>じゅんび</rt></ruby>を<ruby>一緒<rt>いっしょ</rt></ruby>に<ruby>手伝<rt>てつだ</rt></ruby>います。",
        "en": "I help with the cooking preparations together.",
        "zh_TW": "一起幫忙準備做飯。",
        "zh_CN": "一起帮忙准备做饭。",
        "ko": "요리 준비를 함께 돕습니다.",
        "zh_HK": "一齊幫手準備煮飯。",
        "fr": "J'aide à préparer le repas ensemble."
    }
}
# card_0656 助ける・助けます
REVISIONS["card_0656"] = {
    "example": {
        "ja": "<ruby>困<rt>こま</rt></ruby>っている<ruby>人<rt>ひと</rt></ruby>を<ruby>親切<rt>しんせつ</rt></ruby>に<ruby>助<rt>たす</rt></ruby>けます。",
        "en": "I kindly help people in trouble.",
        "zh_TW": "熱心幫助有困難的人。",
        "zh_CN": "热心帮助有困难的人。",
        "ko": "곤란한 사람을 친절하게 돕습니다.",
        "zh_HK": "好心幫有需要嘅人。",
        "fr": "J'aide gentiment les personnes en difficulté."
    }
}
# card_0658 呼ぶ・呼びます
REVISIONS["card_0658"] = {
    "example": {
        "ja": "<ruby>電話<rt>でんわ</rt></ruby>でタクシーを1<ruby>台<rt>だい</rt></ruby><ruby>呼<rt>よ</rt></ruby>びます。",
        "en": "I call a taxi by phone.",
        "zh_TW": "打電話叫一輛計程車。",
        "zh_CN": "打电话叫一辆出租车。",
        "ko": "전화로 택시를 한 대 부릅니다.",
        "zh_HK": "打電話叫一架的士。",
        "fr": "J'appelle un taxi par téléphone."
    }
}
# card_0660 教える・教えます
REVISIONS["card_0660"] = {
    "example": {
        "ja": "<ruby>先生<rt>せんせい</rt></ruby>が<ruby>日本語<rt>にほんご</rt></ruby>をやさしく<ruby>教<rt>おし</rt></ruby>えます。",
        "en": "The teacher gently teaches Japanese.",
        "zh_TW": "老師親切地教日語。",
        "zh_CN": "老师亲切地教日语。",
        "ko": "선생님이 일본어를 친절하게 가르쳐 줍니다.",
        "zh_HK": "老師好溫柔咁教日文。",
        "fr": "Le professeur enseigne gentiment le japonais."
    }
}
# card_0661 入る・入ります
REVISIONS["card_0661"] = {
    "example": {
        "ja": "カフェに<ruby>入<rt>はい</rt></ruby>ってアイスコーヒーを<ruby>飲<rt>の</rt></ruby>みます。",
        "en": "I enter the cafe and drink an iced coffee.",
        "zh_TW": "進咖啡館喝冰咖啡。",
        "zh_CN": "进咖啡馆喝冰咖啡。",
        "ko": "카페에 들어가 아이스커피를 마십니다.",
        "zh_HK": "入cafe飲凍咖啡。",
        "fr": "J'entre dans un café et je bois un café glacé."
    }
}
# card_0662 出る・出ます
REVISIONS["card_0662"] = {
    "example": {
        "ja": "<ruby>会議<rt>かいぎ</rt></ruby>が<ruby>終<rt>お</rt></ruby>わって<ruby>部屋<rt>へや</rt></ruby>を<ruby>出<rt>で</rt></ruby>ます。",
        "en": "The meeting ends and I leave the room.",
        "zh_TW": "會議結束，離開房間。",
        "zh_CN": "会议结束，离开房间。",
        "ko": "회의가 끝나고 방을 나옵니다.",
        "zh_HK": "開完會走出會議室。",
        "fr": "La réunion se termine et je sors de la pièce."
    }
}
# card_0663 降る・降ります
REVISIONS["card_0663"] = {
    "example": {
        "ja": "<ruby>午後<rt>ごご</rt></ruby>から<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>ります。",
        "en": "It will rain from the afternoon.",
        "zh_TW": "下午開始下雨。",
        "zh_CN": "下午开始下雨。",
        "ko": "오후부터 비가 내립니다.",
        "zh_HK": "晏晝開始落雨。",
        "fr": "Il pleut à partir de l'après-midi."
    }
}

# 基本動詞(4): ます形統一
# card_0772 浴びる・浴びます
REVISIONS["card_0772"] = {
    "example": {
        "ja": "<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>起<rt>お</rt></ruby>きたらシャワーを<ruby>浴<rt>あ</rt></ruby>びます。",
        "en": "I take a shower every morning after waking up.",
        "zh_TW": "每天早上一醒來就洗澡沖涼。",
        "zh_CN": "每天早上一醒来就洗澡冲凉。",
        "ko": "매일 아침 일어나면 샤워를 합니다.",
        "zh_HK": "每日朝早一起身就沖涼。",
        "fr": "Je prends une douche tous les matins au réveil."
    }
}
# card_0774 入れる・入れます
REVISIONS["card_0774"] = {
    "example": {
        "ja": "カバンに<ruby>財布<rt>さいふ</rt></ruby>と<ruby>鍵<rt>かぎ</rt></ruby>を<ruby>入<rt>い</rt></ruby>れます。",
        "en": "I put my wallet and keys into my bag.",
        "zh_TW": "把錢包和鑰匙放進包裡。",
        "zh_CN": "把钱包和钥匙放进包里。",
        "ko": "가방에 지갑과 열쇠를 넣습니다.",
        "zh_HK": "將銀包同鎖匙擺入個袋度。",
        "fr": "Je mets mon portefeuille et mes clés dans mon sac."
    }
}
# card_0775 出す・出します
REVISIONS["card_0775"] = {
    "example": {
        "ja": "<ruby>先生<rt>せんせい</rt></ruby>に<ruby>宿題<rt>しゅくだい</rt></ruby>のノートを<ruby>出<rt>だ</rt></ruby>します。",
        "en": "I submit my homework notebook to the teacher.",
        "zh_TW": "向老師提交作業本。",
        "zh_CN": "向老师提交作业本。",
        "ko": "선생님께 숙제 공책을 제출합니다.",
        "zh_HK": "交功課簿畀老師。",
        "fr": "Je remets mon cahier de devoirs au professeur."
    }
}
# card_0776 押す・押します
REVISIONS["card_0776"] = {
    "example": {
        "ja": "エレベーターのボタンを<ruby>押<rt>お</rt></ruby>します。",
        "en": "I press the elevator button.",
        "zh_TW": "按下電梯按鈕。",
        "zh_CN": "按下电梯按钮。",
        "ko": "엘리베이터 버튼을 누릅니다.",
        "zh_HK": "撳升降機掣。",
        "fr": "J'appuie sur le bouton de l'ascenseur."
    }
}
# card_0777 置く・置きます
REVISIONS["card_0777"] = {
    "example": {
        "ja": "<ruby>机<rt>つくえ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に<ruby>本<rt>ほん</rt></ruby>を<ruby>置<rt>お</rt></ruby>きます。",
        "en": "I put the book on the desk.",
        "zh_TW": "把書放在桌子上。",
        "zh_CN": "把书放在桌子上。",
        "ko": "책상 위에 책을 놓습니다.",
        "zh_HK": "擺本書喺張枱上面。",
        "fr": "Je pose le livre sur le bureau."
    }
}
# card_0780 止める・止めます
REVISIONS["card_0780"] = {
    "example": {
        "ja": "<ruby>駐車場<rt>ちゅうしゃじょう</rt></ruby>に<ruby>車<rt>くるま</rt></ruby>を<ruby>止<rt>と</rt></ruby>めます。",
        "en": "I park the car in the parking lot.",
        "zh_TW": "把車停在停車場。",
        "zh_CN": "把车停在停车场。",
        "ko": "주차장에 차를 세웁니다.",
        "zh_HK": "將架車泊喺停車場。",
        "fr": "Je gare la voiture sur le parking."
    }
}
# card_0781 座る・座ります
REVISIONS["card_0781"] = {
    "example": {
        "ja": "こちらのソファに<ruby>座<rt>すわ</rt></ruby>ります。",
        "en": "I sit on this sofa.",
        "zh_TW": "坐在這邊的沙發上。",
        "zh_CN": "坐在这边的沙发上。",
        "ko": "이 소파에 앉습니다.",
        "zh_HK": "坐喺呢張梳化度。",
        "fr": "Je m'assois sur ce canapé."
    }
}
# card_0782 立つ・立ちます
REVISIONS["card_0782"] = {
    "example": {
        "ja": "<ruby>電車<rt>でんしゃ</rt></ruby>でお<ruby>年寄<rt>としよ</rt></ruby>りに<ruby>席<rt>せき</rt></ruby>を<ruby>譲<rt>ゆず</rt></ruby>るために<ruby>立<rt>た</rt></ruby>ちます。",
        "en": "I stand up to give my seat to an elderly person on the train.",
        "zh_TW": "在電車上為了讓座給長者而站起來。",
        "zh_CN": "在电车上为了让座给老人而站起来。",
        "ko": "전철에서 어르신께 자리를 양보하기 위해 일어섭니다.",
        "zh_HK": "喺火車上為咗讓座畀長者而企起身。",
        "fr": "Je me lève pour céder ma place à une personne âgée dans le train."
    }
}
# card_0783 住む・住みます
REVISIONS["card_0783"] = {
    "example": {
        "ja": "<ruby>緑<rt>みどり</rt></ruby>が<ruby>多<rt>おお</rt></ruby>い<ruby>静<rt>しず</rt></ruby>かな<ruby>街<rt>まち</rt></ruby>に<ruby>住<rt>す</rt></ruby>みます。",
        "en": "I live in a quiet town with lots of greenery.",
        "zh_TW": "住在綠意盎然的安靜城鎮裡。",
        "zh_CN": "住在绿意盎然的安静城镇里。",
        "ko": "녹음이 많은 조용한 동네에 삽니다.",
        "zh_HK": "住喺好多綠化又好靜嘅市鎮度。",
        "fr": "J'habite dans une ville calme et verdoyante."
    }
}
# card_0784 吸う・吸います
REVISIONS["card_0784"] = {
    "example": {
        "ja": "<ruby>公園<rt>こうえん</rt></ruby>で<ruby>新鮮<rt>しんせん</rt></ruby>な<ruby>空気<rt>くうき</rt></ruby>を<ruby>吸<rt>す</rt></ruby>います。",
        "en": "I breathe fresh air in the park.",
        "zh_TW": "在公園呼吸新鮮空氣。",
        "zh_CN": "在公园呼吸新鲜空气。",
        "ko": "공원에서 신선한 공기를 마십니다.",
        "zh_HK": "喺公園吸新鮮空氣。",
        "fr": "Je respire de l'air frais dans le parc."
    }
}
# card_0786 忘れる・忘れます
REVISIONS["card_0786"] = {
    "example": {
        "ja": "<ruby>傘<rt>かさ</rt></ruby>を<ruby>時々<rt>ときどき</rt></ruby><ruby>電車<rt>でんしゃ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に<ruby>忘<rt>わす</rt></ruby>れます。",
        "en": "I sometimes leave my umbrella on the train.",
        "zh_TW": "我有時會把雨傘忘在電車裡。",
        "zh_CN": "我有时期会把雨伞忘在电车里。",
        "ko": "가끔 우산을 전철 안에 두고 내립니다.",
        "zh_HK": "我有時會唔記得把遮擺咗喺火車入面。",
        "fr": "J'oublie parfois mon parapluie dans le train."
    }
}
# card_0787 失くす・失くします
REVISIONS["card_0787"] = {
    "example": {
        "ja": "うっかり<ruby>鍵<rt>かぎ</rt></ruby>を<ruby>失<rt>な</rt></ruby>くします。",
        "en": "I carelessly lose my keys.",
        "zh_TW": "不小心把鑰匙弄丟了。",
        "zh_CN": "不小心把钥匙弄丢了。",
        "ko": "깜빡하고 열쇠를 잃어버립니다.",
        "zh_HK": "唔小心整唔見咗條鎖匙。",
        "fr": "Je perds mes clés par inadvertance."
    }
}
# card_0789 返す・返します
REVISIONS["card_0789"] = {
    "example": {
        "ja": "<ruby>明日<rt>あした</rt></ruby><ruby>図書館<rt>としょかん</rt></ruby>へ<ruby>本<rt>ほん</rt></ruby>を<ruby>返<rt>かえ</rt></ruby>します。",
        "en": "I will return the book to the library tomorrow.",
        "zh_TW": "明天把書還給圖書館。",
        "zh_CN": "明天把书还给图书馆。",
        "ko": "내일 도서관에 책을 반납합니다.",
        "zh_HK": "聽日去圖書館還書。",
        "fr": "Je rends le livre à la bibliothèque demain."
    }
}
# card_0790 辞める・辞めます
REVISIONS["card_0790"] = {
    "example": {
        "ja": "<ruby>留学<rt>りゅうがく</rt></ruby>のために<ruby>今<rt>いま</rt></ruby>の<ruby>仕事<rt>しごと</rt></ruby>を<ruby>辞<rt>や</rt></ruby>めます。",
        "en": "I quit my current job to study abroad.",
        "zh_TW": "為了去留學而辭掉現在的工作。",
        "zh_CN": "为了去留学而辞掉现在的工作。",
        "ko": "유학을 위해 지금 일을 그만둡니다.",
        "zh_HK": "為咗去留學而辭咗而家份工。",
        "fr": "Je quitte mon travail actuel pour partir étudier à l'étranger."
    }
}

# 基本動詞(5): ます形統一
# card_0792 修理する・修理します
REVISIONS["card_0792"] = {
    "example": {
        "ja": "<ruby>自転車<rt>じてんしゃ</rt></ruby><ruby>屋<rt>や</rt></ruby>さんでブレーキを<ruby>修理<rt>しゅうり</rt></ruby>します。",
        "en": "I have the bicycle brakes repaired at the bike shop.",
        "zh_TW": "在自行車店修理剎車。",
        "zh_CN": "在自行车店修理刹车。",
        "ko": "자전거 가게에서 브레이크를 수리합니다.",
        "zh_HK": "喺單車舖整迫力（剎車）。",
        "fr": "Je fais réparer les freins au magasin de vélos."
    }
}
# card_0794 泊まる・泊まります
REVISIONS["card_0794"] = {
    "example": {
        "ja": "<ruby>京都<rt>きょうと</rt></ruby>の<ruby>温泉<rt>おんせん</rt></ruby><ruby>旅館<rt>りょかん</rt></ruby>に<ruby>泊<rt>と</rt></ruby>まります。",
        "en": "I stay at a hot spring ryokan in Kyoto.",
        "zh_TW": "住在京都的溫泉旅館。",
        "zh_CN": "住在京都的温泉旅馆。",
        "ko": "교토의 온천 여관에 묵습니다.",
        "zh_HK": "住喺京都嘅溫泉旅館。",
        "fr": "Je séjourne dans un ryokan avec onsen à Kyoto."
    }
}
# card_0795 掃除する・掃除します
REVISIONS["card_0795"] = {
    "example": {
        "ja": "<ruby>休日<rt>きゅうじつ</rt></ruby>の<ruby>朝<rt>あさ</rt></ruby>に<ruby>部屋<rt>へや</rt></ruby>をきれいに<ruby>掃除<rt>そうじ</rt></ruby>します。",
        "en": "I clean the room thoroughly on weekend mornings.",
        "zh_TW": "週末早上把房間打掃得乾乾淨淨。",
        "zh_CN": "周末早上把房间打扫得干干净净。",
        "ko": "휴일 아침에 방을 깨끗이 청소합니다.",
        "zh_HK": "放假嘅朝早將間房打掃得乾乾淨淨。",
        "fr": "Je nettoie la chambre de fond en comble le matin du week-end."
    }
}
# card_0796 洗濯する・洗濯します
REVISIONS["card_0796"] = {
    "example": {
        "ja": "<ruby>週末<rt>しゅうまつ</rt></ruby>にまとめて<ruby>服<rt>ふく</rt></ruby>を<ruby>洗濯<rt>せんたく</rt></ruby>します。",
        "en": "I wash all my clothes together on the weekend.",
        "zh_TW": "週末把衣服集中洗好。",
        "zh_CN": "周末把衣服集中洗好。",
        "ko": "주말에 옷을 몰아서 세탁합니다.",
        "zh_HK": "週末一次過洗衫。",
        "fr": "Je lave tous mes vêtements ensemble le week-end."
    }
}
# card_0798 歌う・歌います
REVISIONS["card_0798"] = {
    "example": {
        "ja": "カラオケで<ruby>友達<rt>ともだち</rt></ruby>と<ruby>一緒<rt>いっしょ</rt></ruby>に<ruby>歌<rt>うた</rt></ruby>を<ruby>歌<rt>うた</rt></ruby>います。",
        "en": "I sing songs with my friends at karaoke.",
        "zh_TW": "在KTV和朋友一起唱歌。",
        "zh_CN": "在KTV和朋友一起唱歌。",
        "ko": "노래방에서 친구와 함께 노래를 부릅니다.",
        "zh_HK": "喺卡拉OK同朋友一齊唱歌。",
        "fr": "Je chante des chansons avec mes amis au karaoké."
    }
}
# card_0801 変える・変えます
REVISIONS["card_0801"] = {
    "example": {
        "ja": "<ruby>気分転換<rt>きぶんてんかん</rt></ruby>にカーテンの<ruby>色<rt>いろ</rt></ruby>を<ruby>変<rt>か</rt></ruby>えます。",
        "en": "I change the color of the curtains for a change of pace.",
        "zh_TW": "為了轉換心情而更換窗簾的顏色。",
        "zh_CN": "为了转换心情而更换窗帘的颜色。",
        "ko": "기분 전환을 위해 커튼 색을 바꿉니다.",
        "zh_HK": "為咗轉下心情而換窗簾嘅顏色。",
        "fr": "Je change la couleur des rideaux pour changer d'ambiance."
    }
}
# card_0803 運転する・運転します
REVISIONS["card_0803"] = {
    "example": {
        "ja": "<ruby>休日<rt>きゅうじつ</rt></ruby>に<ruby>安全<rt>あんぜん</rt></ruby>に<ruby>車<rt>くるま</rt></ruby>を<ruby>運転<rt>うんてん</rt></ruby>します。",
        "en": "I drive the car safely on holidays.",
        "zh_TW": "休假日安全地開車。",
        "zh_CN": "休假日安全地开车。",
        "ko": "휴일에 안전하게 운전합니다.",
        "zh_HK": "放假嗰陣好安全咁揸車。",
        "fr": "Je conduis prudemment pendant les vacances."
    }
}
# card_0804 取る・取ります
REVISIONS["card_0804"] = {
    "example": {
        "ja": "<ruby>棚<rt>たな</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>の<ruby>本<rt>ほん</rt></ruby>を<ruby>取<rt>と</rt></ruby>ります。",
        "en": "I take a book from the shelf.",
        "zh_TW": "拿架子上的書。",
        "zh_CN": "拿架子上的书。",
        "ko": "선반 위의 책을 꺼냅니다.",
        "zh_HK": "拎書架上面本書。",
        "fr": "Je prends un livre sur l'étagère."
    }
}
# card_0805 言う・言います
REVISIONS["card_0805"] = {
    "example": {
        "ja": "<ruby>先生<rt>せんせい</rt></ruby>に「ありがとうございます」と<ruby>言<rt>い</rt></ruby>います。",
        "en": "I say 'Thank you very much' to the teacher.",
        "zh_TW": "向老師說「謝謝」。",
        "zh_CN": "向老师说「谢谢」。",
        "ko": "선생님께 '감사합니다'라고 말합니다.",
        "zh_HK": "同老師講「多謝」。",
        "fr": "Je dis « merci beaucoup » au professeur."
    }
}
# card_0806 気を付ける・気を付けます
REVISIONS["card_0806"] = {
    "example": {
        "ja": "<ruby>夜道<rt>よみち</rt></ruby>では<ruby>足元<rt>あしもと</rt></ruby>に<ruby>気<rt>き</rt></ruby>を<ruby>付<rt>つ</rt></ruby>けます。",
        "en": "I watch my step on dark roads at night.",
        "zh_TW": "在夜路上會小心注意腳下。",
        "zh_CN": "在夜路上会小心注意脚下。",
        "ko": "밤길에서는 발밑을 조심합니다.",
        "zh_HK": "行夜路嗰陣會睇清楚腳下。",
        "fr": "Je fais attention où je mets les pieds sur les routes de nuit."
    }
}
# card_0807 留学する・留学します
REVISIONS["card_0807"] = {
    "example": {
        "ja": "<ruby>来年<rt>らいねん</rt></ruby>から<ruby>日本<rt>にほん</rt></ruby>の<ruby>大学<rt>だいがく</rt></ruby>へ<ruby>留学<rt>りゅうがく</rt></ruby>します。",
        "en": "I will study abroad at a Japanese university starting next year.",
        "zh_TW": "明年開始去日本的大學留學。",
        "zh_CN": "明年开始去日本的大学留学。",
        "ko": "내년부터 일본 대학교로 유학을 갑니다.",
        "zh_HK": "出年開始去日本嘅大學留學。",
        "fr": "J'étudierai à l'université japonaise à partir de l'année prochaine."
    }
}
# card_0810 持ってくる・持ってきます
REVISIONS["card_0810"] = {
    "example": {
        "ja": "<ruby>明日<rt>あした</rt></ruby>の<ruby>授業<rt>じゅぎょう</rt></ruby>に<ruby>教科書<rt>きょうかしょ</rt></ruby>を<ruby>持<rt>も</rt></ruby>ってきます。",
        "en": "I will bring the textbook to tomorrow's class.",
        "zh_TW": "明天的課我會帶教科書來。",
        "zh_CN": "明天的课我会带教科书来。",
        "ko": "내일 수업에 교과서를 가져옵니다.",
        "zh_HK": "聽日上堂我會帶教科書嚟。",
        "fr": "J'apporterai le manuel scolaire au cours de demain."
    }
}
# card_0812 連れてくる・連れてきます
REVISIONS["card_0812"] = {
    "example": {
        "ja": "<ruby>休日<rt>きゅうじつ</rt></ruby>にペットの<ruby>犬<rt>いぬ</rt></ruby>を<ruby>公園<rt>こうえん</rt></ruby>へ<ruby>連<rt>つ</rt></ruby>れてきます。",
        "en": "I bring my pet dog to the park on holidays.",
        "zh_TW": "休假日把寵物狗帶到公園來。",
        "zh_CN": "休假日把宠物狗带到公园来。",
        "ko": "휴일에 반려견을 공원으로 데려옵니다.",
        "zh_HK": "放假嗰陣帶隻寵物狗嚟公園。",
        "fr": "J'amène mon chien au parc pendant les vacances."
    }
}

# -------------------------------------------------------------
# 2. 基本動詞 てform (1)〜(3) 修正
# -------------------------------------------------------------
# card_0770 出て
REVISIONS["card_0770"] = {
    "example": {
        "ja": "<ruby>部屋<rt>へや</rt></ruby>を<ruby>出<rt>で</rt></ruby>て、<ruby>駅<rt>えき</rt></ruby>へ<ruby>向<rt>む</rt></ruby>かってください。",
        "en": "Please leave the room and head to the station.",
        "zh_TW": "請離開房間，前往車站。",
        "zh_CN": "请离开房间，前往车站。",
        "ko": "방을 나와서 역으로 향하세요.",
        "zh_HK": "請出行間房，去車站。",
        "fr": "Veuillez sortir de la pièce et vous diriger vers la gare."
    }
}
# card_0771 （雨が）降って
REVISIONS["card_0771"] = {
    "example": {
        "ja": "<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>って、<ruby>道<rt>みち</rt></ruby>がぬれています。",
        "en": "It rained and the streets are wet.",
        "zh_TW": "下雨了，道路都濕了。",
        "zh_CN": "下雨了，道路都湿了。",
        "ko": "비가 내려서 길이 젖어 있습니다.",
        "zh_HK": "落緊雨，條路濕晒。",
        "fr": "Il pleut et la route est mouillée."
    }
}

# -------------------------------------------------------------
# 3. 基本動詞 ないform (1)〜(5) 修正
# -------------------------------------------------------------
# card_0876 終わらない
REVISIONS["card_0876"] = {
    "example": {
        "ja": "<ruby>今日<rt>きょう</rt></ruby>の<ruby>仕事<rt>しごと</rt></ruby>はなかなか<ruby>終<rt>お</rt></ruby>わらない。",
        "en": "Today's work just won't seem to end.",
        "zh_TW": "今天的工作怎麼也做不完。",
        "zh_CN": "今天的工作怎么也做不完。",
        "ko": "오늘 일은 좀처럼 끝나지 않는다.",
        "zh_HK": "今日嘅工作點都做唔完。",
        "fr": "Le travail d'aujourd'hui ne semble pas vouloir se terminer."
    }
}
# card_0907 知らない (※センシティブ排除:「事件」->「内容」)
REVISIONS["card_0907"] = {
    "example": {
        "ja": "その<ruby>話<rt>はなし</rt></ruby>の<ruby>詳<rt>くわ</rt></ruby>しい<ruby>内容<rt>ないよう</rt></ruby>は、まだ<ruby>何<rt>なに</rt></ruby>も<ruby>知<rt>し</rt></ruby>らない。",
        "en": "I don't know any of the details of that story yet.",
        "zh_TW": "我還完全不知道那件事的詳細內容。",
        "zh_CN": "我还完全不知道那件事的详细内容。",
        "ko": "그 이야기의 자세한 내용은 아직 아무것도 모른다.",
        "zh_HK": "我仲未知嗰件事嘅詳細內容。",
        "fr": "Je ne connais pas encore les détails de cette histoire."
    }
}
# card_0916 待たない
REVISIONS["card_0916"] = {
    "example": {
        "ja": "これ<ruby>以上<rt>いじょう</rt></ruby>は<ruby>待<rt>ま</rt></ruby>たないで、<ruby>先<rt>さき</rt></ruby>に<ruby>行<rt>い</rt></ruby>きましょう。",
        "en": "Let's not wait any longer and go ahead.",
        "zh_TW": "別再等了，我們先行一步吧。",
        "zh_CN": "别再等了，我们先行一步吧。",
        "ko": "더 이상 기다리지 말고 먼저 갑시다.",
        "zh_HK": "唔好再等喇，我哋出發先啦。",
        "fr": "N'attendons pas plus longtemps, partons devant."
    }
}
# card_0931 出さない (※怒られる等のネガティブ表現排除)
REVISIONS["card_0931"] = {
    "example": {
        "ja": "<ruby>用事<rt>ようじ</rt></ruby>がない<ruby>日<rt>ひ</rt></ruby>は、ゴミを<ruby>外<rt>そと</rt></ruby>に<ruby>出<rt>だ</rt></ruby>さない。",
        "en": "On days when it's not collection day, I don't put the garbage out.",
        "zh_TW": "非垃圾收集日不把垃圾拿到外面。",
        "zh_CN": "非垃圾收集日不把垃圾拿到外面。",
        "ko": "수거일이 아닌 날에는 쓰레기를 밖에 내놓지 않는다.",
        "zh_HK": "唔係倒垃圾嘅日子就唔會拎垃圾出去。",
        "fr": "Les jours où ce n'est pas le ramassage, je ne sors pas les poubelles."
    }
}

# -------------------------------------------------------------
# 4. 基本動詞 可能形 (1)〜(5) 修正 (過去形から現在可能形へ統一)
# -------------------------------------------------------------
# card_0977 買える
REVISIONS["card_0977"] = {
    "example": {
        "ja": "ネットで<ruby>限定<rt>げんてい</rt></ruby>のチケットが<ruby>買<rt>か</rt></ruby>える。",
        "en": "You can buy limited tickets online.",
        "zh_TW": "可以在網上買到限定門票。",
        "zh_CN": "可以在网上买到限定门票。",
        "ko": "인터넷에서 한정 티켓을 살 수 있다.",
        "zh_HK": "可以喺網上買到限定門票。",
        "fr": "On peut acheter des billets limités sur Internet."
    }
}
# card_0989 忘れられる
REVISIONS["card_0989"] = {
    "example": {
        "ja": "<ruby>音楽<rt>おんがく</rt></ruby>を<ruby>聴<rt>き</rt></ruby>いて、<ruby>忙<rt>いそが</rt></ruby>しい<ruby>日常<rt>にちじょう</rt></ruby>を<ruby>忘<rt>わす</rt></ruby>れられる。",
        "en": "Listening to music helps you forget the busy daily routine.",
        "zh_TW": "聽著音樂，可以忘掉繁忙的日常生活。",
        "zh_CN": "听着音乐，可以忘掉繁忙的日常生活。",
        "ko": "음악을 들으며 바쁜 일상을 잊을 수 있다.",
        "zh_HK": "聽住音樂，可以忘記忙碌嘅日常生活。",
        "fr": "Écouter de la musique permet d'oublier le quotidien trépidant."
    }
}
# card_0991 降りられる
REVISIONS["card_0991"] = {
    "example": {
        "ja": "<ruby>次<rt>つぎ</rt></ruby>の<ruby>駅<rt>えき</rt></ruby>で<ruby>電車<rt>でんしゃ</rt></ruby>を<ruby>降<rt>お</rt></ruby>りられる。",
        "en": "You can get off the train at the next station.",
        "zh_TW": "可以在下一站下電車。",
        "zh_CN": "可以在下一站下电车。",
        "ko": "다음 역에서 전철에서 내릴 수 있다.",
        "zh_HK": "可以喺下一個站落火車。",
        "fr": "On peut descendre du train à la prochaine gare."
    }
}
# card_1001 洗える
REVISIONS["card_1001"] = {
    "example": {
        "ja": "このスーツは<ruby>自宅<rt>じたく</rt></ruby>の<ruby>洗濯機<rt>せんたくき</rt></ruby>で<ruby>洗<rt>あら</rt></ruby>える。",
        "en": "This suit can be washed in a home washing machine.",
        "zh_TW": "這套西裝可以用家裡的洗衣機洗。",
        "zh_CN": "这套西装可以用家里的洗衣机洗。",
        "ko": "이 양복은 집 세탁기로 세탁할 수 있다.",
        "zh_HK": "呢套西裝可以用屋企部洗衣機洗。",
        "fr": "Ce costume peut être lavé dans la machine à laver de la maison."
    }
}
# card_1012 開けられる
REVISIONS["card_1012"] = {
    "example": {
        "ja": "タオルを<ruby>使<rt>つか</rt></ruby>えば、<ruby>固<rt>かた</rt></ruby>いフタも<ruby>開<rt>あ</rt></ruby>けられる。",
        "en": "If you use a towel, you can open even a tight lid.",
        "zh_TW": "用毛巾的話，即使是緊緊的蓋子也能打開。",
        "zh_CN": "用毛巾的话，即使是紧紧的盖子也能打开。",
        "ko": "수건을 사용하면 꽉 닫힌 뚜껑도 열 수 있다.",
        "zh_HK": "用毛巾嘅話，就算好實嘅蓋都可以開到。",
        "fr": "En utilisant une serviette, on peut ouvrir même un couvercle coincé."
    }
}
# card_1014 答えられる
REVISIONS["card_1014"] = {
    "example": {
        "ja": "<ruby>復習<rt>ふくしゅう</rt></ruby>したので、<ruby>先生<rt>せんせい</rt></ruby>の<ruby>質問<rt>しつもん</rt></ruby>にしっかり<ruby>答<rt>こた</rt></ruby>えられる。",
        "en": "Because I reviewed, I can answer the teacher's questions well.",
        "zh_TW": "因為複習過了，所以能好好回答老師的問題。",
        "zh_CN": "因为复习过了，所以能好好回答老师的问题。",
        "ko": "복습했기 때문에 선생님의 질문에 잘 대답할 수 있다.",
        "zh_HK": "因為溫習過，所以可以好好答老師嘅問題。",
        "fr": "Comme j'ai révisé, je peux bien répondre aux questions du professeur."
    }
}
# card_1018 わかる・わかります
REVISIONS["card_1018"] = {
    "example": {
        "ja": "<ruby>説明<rt>せつめい</rt></ruby>を<ruby>聞<rt>き</rt></ruby>いて、<ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>がよくわかります。",
        "en": "After listening to the explanation, I understand how to use it well.",
        "zh_TW": "聽了說明後，很清楚使用方法了。",
        "zh_CN": "听了说明后，很清楚使用方法了。",
        "ko": "설명을 듣고 사용법을 잘 이해합니다.",
        "zh_HK": "聽完解釋之後，好明白點樣用。",
        "fr": "Après avoir écouté l'explication, je comprends bien l'utilisation."
    }
}
# card_1027 取れる
REVISIONS["card_1027"] = {
    "example": {
        "ja": "<ruby>人気<rt>にんき</rt></ruby>のコンサートのチケットが<ruby>取<rt>と</rt></ruby>れる。",
        "en": "You can get tickets for the popular concert.",
        "zh_TW": "可以買到熱門演唱會的門票。",
        "zh_CN": "可以买到热门演唱会的门票。",
        "ko": "인기 콘서트 티켓을 구할 수 있습니다.",
        "zh_HK": "可以買到熱門演唱會嘅飛。",
        "fr": "On peut obtenir des billets pour le concert populaire."
    }
}
# card_1029 助けられる
REVISIONS["card_1029"] = {
    "example": {
        "ja": "<ruby>救助隊<rt>きゅうじょたい</rt></ruby>のおかげで、<ruby>早<rt>はや</rt></ruby>く<ruby>助<rt>たす</rt></ruby>けられる。",
        "en": "Thanks to the rescue team, they can be rescued quickly.",
        "zh_TW": "多虧了救援隊，能夠迅速獲救。",
        "zh_CN": "多亏了救援队，能够迅速获救。",
        "ko": "구조대 덕분에 빨리 구조될 수 있습니다.",
        "zh_HK": "多得救援隊，可以好快獲救。",
        "fr": "Grâce aux sauveteurs, ils peuvent être secourus rapidement."
    }
}
# card_1043 作れる
REVISIONS["card_1043"] = {
    "example": {
        "ja": "レシピを<ruby>見<rt>み</rt></ruby>れば、おいしいケーキが<ruby>作<rt>つく</rt></ruby>れる。",
        "en": "If you follow the recipe, you can make a delicious cake.",
        "zh_TW": "看著食譜的話，就能做出美味的蛋糕。",
        "zh_CN": "看着食谱的话，就能做出美味的蛋糕。",
        "ko": "레시피를 보면 맛있는 케이크를 만들 수 있습니다.",
        "zh_HK": "跟住食譜嘅話，就可以整到好味嘅蛋糕。",
        "fr": "En suivant la recette, on peut faire un délicieux gâteau."
    }
}
# card_1044 売れる
REVISIONS["card_1044"] = {
    "example": {
        "ja": "フリマアプリを<ruby>使<rt>つか</rt></ruby>えば、<ruby>本<rt>ほん</rt></ruby>がすぐ<ruby>売<rt>う</rt></ruby>れる。",
        "en": "If you use a flea market app, books sell quickly.",
        "zh_TW": "使用跳蚤市場App的話，書很快就能賣出去。",
        "zh_CN": "使用跳蚤市场App的话，书很快就能卖出去。",
        "ko": "중고거래 앱을 사용하면 책이 금방 팔립니다.",
        "zh_HK": "用二手買賣App嘅話，啲書好快賣得出。",
        "fr": "En utilisant une application de vente d'occasion, les livres se vendent vite."
    }
}
# card_1046 座れる
REVISIONS["card_1046"] = {
    "example": {
        "ja": "<ruby>始発<rt>しはつ</rt></ruby><ruby>電車<rt>でんしゃ</rt></ruby>に<ruby>乗<rt>の</rt></ruby>れば、ゆっくり<ruby>座<rt>すわ</rt></ruby>れる。",
        "en": "If you take the first train, you can take a seat comfortably.",
        "zh_TW": "如果坐首班車的話，就能舒舒服服地坐著。",
        "zh_CN": "如果坐首班车的话，就能舒舒服服地坐着。",
        "ko": "첫차를 타면 편안하게 앉을 수 있습니다.",
        "zh_HK": "搭頭班車嘅話，就可以舒舒服服咁坐。",
        "fr": "Si vous prenez le premier train, vous pouvez vous asseoir confortablement."
    }
}
# card_1047 立てる
REVISIONS["card_1047"] = {
    "example": {
        "ja": "<ruby>怪我<rt>けが</rt></ruby>が<ruby>治<rt>なお</rt></ruby>って、<ruby>自分<rt>じぶん</rt></ruby>の<ruby>足<rt>あし</rt></ruby>でしっかり<ruby>立<rt>た</rt></ruby>てる。",
        "en": "The injury healed, and I can stand firmly on my own feet.",
        "zh_TW": "傷好了，能靠自己的雙腳站穩了。",
        "zh_CN": "伤好了，能靠自己的双脚站稳了。",
        "ko": "상처가 나아서 자신의 발로 똑바로 설 수 있습니다.",
        "zh_HK": "好返晒之後，可以用自己對腳企穩喇。",
        "fr": "La blessure a guéri et je peux me tenir fermement sur mes pieds."
    }
}
# card_1049 吸える
REVISIONS["card_1049"] = {
    "example": {
        "ja": "<ruby>山<rt>やま</rt></ruby>の<ruby>頂上<rt>ちょうじょう</rt></ruby>で、<ruby>新鮮<rt>しんせん</rt></ruby>な<ruby>空気<rt>くうき</rt></ruby>がたくさん<ruby>吸<rt>す</rt></ruby>える。",
        "en": "At the top of the mountain, you can breathe plenty of fresh air.",
        "zh_TW": "在山頂上可以呼吸很多新鮮空氣。",
        "zh_CN": "在山顶上可以呼吸很多新鲜空气。",
        "ko": "산 정상에서 신선한 공기를 많이 마실 수 있습니다.",
        "zh_HK": "喺山頂可以吸好多新鮮空氣。",
        "fr": "Au sommet de la montagne, on peut respirer beaucoup d'air frais."
    }
}
# card_1064 集められる
REVISIONS["card_1064"] = {
    "example": {
        "ja": "スタンプラリーで、<ruby>全部<rt>ぜんぶ</rt></ruby>のスタンプを<ruby>集<rt>あつ</rt></ruby>められる。",
        "en": "You can collect all the stamps in the stamp rally.",
        "zh_TW": "在集章活動中可以集齊所有的印章。",
        "zh_CN": "在集章活动中可以集齐所有的印章。",
        "ko": "스탬프 랠리에서 모든 스탬프를 모을 수 있습니다.",
        "zh_HK": "喺蓋印活動入面可以吸齊所有印仔。",
        "fr": "On peut collecter tous les tampons lors du rallye de tampons."
    }
}
# card_1067 変われる
REVISIONS["card_1067"] = {
    "example": {
        "ja": "<ruby>努力<rt>どりょく</rt></ruby>すれば、<ruby>人<rt>ひと</rt></ruby>は<ruby>良<rt>よ</rt></ruby>い<ruby>方向<rt>ほうこう</rt></ruby>に<ruby>変<rt>か</rt></ruby>われる。",
        "en": "With effort, anyone can change for the better.",
        "zh_TW": "只要努力，任何人都能朝著好的方向改變。",
        "zh_CN": "只要努力，任何人都能朝着好的方向改变。",
        "ko": "노력하면 사람은 좋은 방향으로 변할 수 있습니다.",
        "zh_HK": "只要努力，人就可以向好嘅方向改變。",
        "fr": "Avec des efforts, tout le monde peut changer en mieux."
    }
}
# card_1070 言える
REVISIONS["card_1070"] = {
    "example": {
        "ja": "「ありがとう」の<ruby>気持<rt>きも</rt></ruby>ちを、きちんと<ruby>言葉<rt>ことば</rt></ruby>で<ruby>言<rt>い</rt></ruby>える。",
        "en": "I can properly express my feelings of 'thank you' in words.",
        "zh_TW": "可以用語言好好表達「謝謝」的心情。",
        "zh_CN": "可以用语言好好表达「谢谢」的心情。",
        "ko": "'고마워'라는 마음을 제대로 말로 표현할 수 있습니다.",
        "zh_HK": "可以用言語好好講出「多謝」嘅心意。",
        "fr": "Je peux exprimer correctement mes sentiments de remerciement avec des mots."
    }
}

# -------------------------------------------------------------
# 5. 基本動詞 たform (1)〜(5) 全103件不一致カード修正 (〜た形直接使用)
# -------------------------------------------------------------
# 基本動詞 たform (1)
REVISIONS["card_1078"] = {
    "example": {
        "ja": "<ruby>今朝<rt>けさ</rt></ruby>は<ruby>目覚<rt>めざ</rt></ruby>ましが<ruby>鳴<rt>な</rt></ruby>る<ruby>前<rt>まえ</rt></ruby>に、６<ruby>時<rt>じ</rt></ruby>に<ruby>起<rt>お</rt></ruby>きた。",
        "en": "This morning, I woke up at 6 o'clock before the alarm went off.",
        "zh_TW": "今天早上鬧鐘響之前，六點就起床了。",
        "zh_CN": "今天早上闹钟响之前，六点就起床了。",
        "ko": "오늘 아침은 알람이 울리기 전에 6시에 일어났다.",
        "zh_HK": "今朝鬧鐘響之前，六點就起咗身。",
        "fr": "Ce matin, je me suis réveillé à 6 heures avant que le réveil ne sonne."
    }
}
REVISIONS["card_1079"] = {
    "example": {
        "ja": "<ruby>昨日<rt>きのう</rt></ruby>の<ruby>夜<rt>よる</rt></ruby>は<ruby>図書館<rt>としょかん</rt></ruby>で、<ruby>日本語<rt>にほんご</rt></ruby>の<ruby>勉強<rt>べんきょう</rt></ruby>をした。",
        "en": "Last night, I studied Japanese at the library.",
        "zh_TW": "昨天晚上在圖書館學了日語。",
        "zh_CN": "昨天晚上在图书馆学了日语。",
        "ko": "어젯밤에는 도서관에서 일본어 공부를 했다.",
        "zh_HK": "琴晚喺圖書館讀咗日文。",
        "fr": "Hier soir, j'ai étudié le japonais à la bibliothèque."
    }
}
REVISIONS["card_1080"] = {
    "example": {
        "ja": "<ruby>先週<rt>せんしゅう</rt></ruby>の<ruby>日曜日<rt>にちようび</rt></ruby>、<ruby>友達<rt>ともだち</rt></ruby>と<ruby>京都<rt>きょうと</rt></ruby>へ<ruby>行<rt>い</rt></ruby>った。",
        "en": "Last Sunday, I went to Kyoto with my friend.",
        "zh_TW": "上個星期天和朋友去了京都。",
        "zh_CN": "上个星期天和朋友去了京都。",
        "ko": "지난주 일요일에 친구와 교토에 갔다.",
        "zh_HK": "上個禮拜日同朋友去咗京都。",
        "fr": "Dimanche dernier, je suis allé à Kyoto avec un ami."
    }
}
REVISIONS["card_1081"] = {
    "example": {
        "ja": "<ruby>仕事<rt>しごと</rt></ruby>が<ruby>終<rt>お</rt></ruby>わって、すぐに<ruby>家<rt>いえ</rt></ruby>へ<ruby>帰<rt>かえ</rt></ruby>った。",
        "en": "After work finished, I went home immediately.",
        "zh_TW": "工作結束後，馬上就回家了。",
        "zh_CN": "工作结束后，马上就回家了。",
        "ko": "일이 끝나고 바로 집으로 돌아갔다.",
        "zh_HK": "收工之後即刻返咗屋企。",
        "fr": "Après le travail, je suis rentré tout de suite chez moi."
    }
}
REVISIONS["card_1082"] = {
    "example": {
        "ja": "<ruby>約束<rt>やくそく</rt></ruby>の<ruby>時間<rt>じかん</rt></ruby>どおりに、<ruby>友達<rt>ともだち</rt></ruby>が<ruby>我<rt>わ</rt></ruby>が<ruby>家<rt>や</rt></ruby>に<ruby>来<rt>き</rt></ruby>た。",
        "en": "My friend came to my home right on time.",
        "zh_TW": "朋友準時來到了我家。",
        "zh_CN": "朋友准时来到了我家。",
        "ko": "약속 시간대로 친구가 우리 집에 왔다.",
        "zh_HK": "朋友準時嚟咗我屋企。",
        "fr": "Mon ami est venu chez moi à l'heure convenue."
    }
}
REVISIONS["card_1083"] = {
    "example": {
        "ja": "<ruby>昼<rt>ひる</rt></ruby>ごはんに、おいしいお<ruby>寿司<rt>すし</rt></ruby>をたくさん<ruby>食<rt>た</rt></ruby>べた。",
        "en": "For lunch, I ate a lot of delicious sushi.",
        "zh_TW": "午餐吃了好多美味的壽司。",
        "zh_CN": "午餐吃了好多美味的寿司。",
        "ko": "점심으로 맛있는 초밥을 많이 먹었다.",
        "zh_HK": "晏晝食咗好多好味嘅壽司。",
        "fr": "Pour le déjeuner, j'ai mangé beaucoup de délicieux sushis."
    }
}
REVISIONS["card_1085"] = {
    "example": {
        "ja": "<ruby>昨夜<rt>ゆうべ</rt></ruby>はとても<ruby>疲<rt>つか</rt></ruby>れていたので、９<ruby>時<rt>じ</rt></ruby>に<ruby>寝<rt>ね</rt></ruby>た。",
        "en": "Last night I was very tired, so I went to bed at 9.",
        "zh_TW": "昨晚非常累，所以九點就睡了。",
        "zh_CN": "昨晚非常累，所以九点就睡了。",
        "ko": "어젯밤에는 너무 피곤해서 9시에 잤다.",
        "zh_HK": "琴晚好攰，所以九點就瞓咗。",
        "fr": "Hier soir, j'étais très fatigué, alors je me suis couché à 9 heures."
    }
}
REVISIONS["card_1086"] = {
    "example": {
        "ja": "<ruby>映画館<rt>えいがかん</rt></ruby>で、<ruby>話題<rt>わだい</rt></ruby>の<ruby>新作<rt>しんさく</rt></ruby>アニメを<ruby>見<rt>み</rt></ruby>た。",
        "en": "I watched the much-talked-about new anime at the movie theater.",
        "zh_TW": "在電影院看了話題熱門的最新動畫。",
        "zh_CN": "在电影院看了话题热门的最新动画。",
        "ko": "영화관에서 화제의 신작 애니메이션을 보았다.",
        "zh_HK": "喺戲院睇咗套好hit嘅新動畫。",
        "fr": "J'ai regardé le nouvel anime dont tout le monde parle au cinéma."
    }
}
REVISIONS["card_1087"] = {
    "example": {
        "ja": "<ruby>道<rt>みち</rt></ruby>がわからなかったので、<ruby>交番<rt>こうばん</rt></ruby>で<ruby>聞<rt>き</rt></ruby>いた。",
        "en": "I didn't know the way, so I asked at the police box.",
        "zh_TW": "因為不知道路，所以在派出所問了路。",
        "zh_CN": "因为不知道路，所以在派出所问了路。",
        "ko": "길을 몰라서 파출소에서 물어보았다.",
        "zh_HK": "因為唔識路，所以喺差館問咗路。",
        "fr": "Je ne connaissais pas le chemin, alors j'ai demandé au poste de police."
    }
}
REVISIONS["card_1088"] = {
    "example": {
        "ja": "<ruby>部屋<rt>へや</rt></ruby>でゆっくりクラシック<ruby>音楽<rt>おんがく</rt></ruby>を<ruby>聴<rt>き</rt></ruby>いた。",
        "en": "I listened to classical music relaxing in my room.",
        "zh_TW": "在房間裡悠閒地聽了古典音樂。",
        "zh_CN": "在房间里悠闲地听了古典音乐。",
        "ko": "방에서 느긋하게 클래식 음악을 들었다.",
        "zh_HK": "喺房度舒舒服服聽咗古典音樂。",
        "fr": "J'ai écouté tranquillement de la musique classique dans ma chambre."
    }
}
REVISIONS["card_1090"] = {
    "example": {
        "ja": "<ruby>久<rt>ひさ</rt></ruby>しぶりに<ruby>国<rt>くに</rt></ruby>の<ruby>両親<rt>りょうしん</rt></ruby>と<ruby>電話<rt>でんわ</rt></ruby>で<ruby>楽<rt>たの</rt></ruby>しく<ruby>話<rt>はな</rt></ruby>した。",
        "en": "I had a pleasant chat on the phone with my parents back home after a long time.",
        "zh_TW": "久違地和老家的父母通電話開心地聊了天。",
        "zh_CN": "久违地和老家的父母通电话开心地聊了天。",
        "ko": "오랜만에 고향의 부모님과 전화로 즐겁게 이야기했다.",
        "zh_HK": "好耐冇同屋企人通電話，傾得好開心。",
        "fr": "J'ai parlé agréablement au téléphone avec mes parents restés au pays après une longue période."
    }
}
REVISIONS["card_1091"] = {
    "example": {
        "ja": "<ruby>駅前<rt>えきまえ</rt></ruby>のカフェで、<ruby>高校<rt>こうこう</rt></ruby><ruby>時代<rt>じだい</rt></ruby>の<ruby>親友<rt>しんゆう</rt></ruby>に<ruby>会<rt>あ</rt></ruby>った。",
        "en": "I met my best friend from high school at a cafe in front of the station.",
        "zh_TW": "在車站前的咖啡館見到了高中的摯友。",
        "zh_CN": "在车站前的咖啡馆见到了高中的挚友。",
        "ko": "역 앞 카페에서 고등학교 시절 절친을 만났다.",
        "zh_HK": "喺站前嘅cafe見返中學最好嘅朋友。",
        "fr": "J'ai rencontré mon meilleur ami du lycée dans un café devant la gare."
    }
}
REVISIONS["card_1094"] = {
    "example": {
        "ja": "チャイムが<ruby>鳴<rt>な</rt></ruby>って、<ruby>日本語<rt>にほんご</rt></ruby>のテストが<ruby>始<rt>はじ</rt></ruby>まった。",
        "en": "The chime rang and the Japanese test started.",
        "zh_TW": "鈴聲響起，日語考試開始了。",
        "zh_CN": "铃声响起，日语考试开始了。",
        "ko": "종이 울리고 일본어 시험이 시작되었다.",
        "zh_HK": "鐘聲響起，日文考試開始咗。",
        "fr": "La sonnerie a retenti et le test de japonais a commencé."
    }
}
REVISIONS["card_1095"] = {
    "example": {
        "ja": "<ruby>長<rt>なが</rt></ruby>い<ruby>会議<rt>かいぎ</rt></ruby>がようやく<ruby>終<rt>お</rt></ruby>わった。",
        "en": "The long meeting finally ended.",
        "zh_TW": "漫長的會議終於結束了。",
        "zh_CN": "漫长的会议终于结束了。",
        "ko": "길었던 회의가 마침내 끝났다.",
        "zh_HK": "漫長嘅會議終於完咗。",
        "fr": "La longue réunion s'est enfin terminée."
    }
}
REVISIONS["card_1096"] = {
    "example": {
        "ja": "<ruby>学生<rt>がくせい</rt></ruby>の<ruby>頃<rt>ころ</rt></ruby>、カフェでアルバイトとして<ruby>働<rt>はたら</rt></ruby>いた。",
        "en": "When I was a student, I worked part-time at a cafe.",
        "zh_TW": "學生時代在咖啡館做過兼職工作。",
        "zh_CN": "学生时代在咖啡馆做过兼职工作。",
        "ko": "학생 시절 카페에서 아르바이트로 일했다.",
        "zh_HK": "讀書嗰陣喺cafe做過兼職返工。",
        "fr": "Quand j'étais étudiant, j'ai travaillé à temps partiel dans un café."
    }
}
REVISIONS["card_1097"] = {
    "example": {
        "ja": "<ruby>友達<rt>ともだち</rt></ruby>からのプレゼントに、とても<ruby>驚<rt>おどろ</rt></ruby>いた！",
        "en": "I was very surprised by the present from my friend!",
        "zh_TW": "收到朋友的禮物，感到非常驚喜！",
        "zh_CN": "收到朋友的礼物，感到非常惊喜！",
        "ko": "친구의 선물에 매우 놀랐다!",
        "zh_HK": "收到朋友嘅禮物，非常之驚喜！",
        "fr": "J'ai été très surpris par le cadeau de mon ami !"
    }
}
REVISIONS["card_1098"] = {
    "example": {
        "ja": "<ruby>電車<rt>でんしゃ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に<ruby>傘<rt>かさ</rt></ruby>を<ruby>忘<rt>わす</rt></ruby>れた。",
        "en": "I forgot my umbrella on the train.",
        "zh_TW": "把雨傘忘在電車裡了。",
        "zh_CN": "把雨伞忘在电车里了。",
        "ko": "전철 안에 우산을 두고 내렸다.",
        "zh_HK": "擺低咗把遮喺火車度唔記得拎。",
        "fr": "J'ai oublié mon parapluie dans le train."
    }
}
REVISIONS["card_1099"] = {
    "example": {
        "ja": "<ruby>今日<rt>きょう</rt></ruby>のレッスンで、<ruby>新<rt>あたら</rt></ruby>しい<ruby>漢字<rt>かんじ</rt></ruby>を10<ruby>個<rt>こ</rt></ruby><ruby>覚<rt>おぼ</rt></ruby>えた。",
        "en": "In today's lesson, I memorized 10 new kanji.",
        "zh_TW": "在今天的課堂上，記住了10個新的漢字。",
        "zh_CN": "在今天的课堂上，记住了10个新的汉字。",
        "ko": "오늘 수업에서 새로운 한자를 10개 외웠다.",
        "zh_HK": "喺今日堂上，記咗10個新漢字。",
        "fr": "Pendant le cours d'aujourd'hui, j'ai mémorisé 10 nouveaux kanji."
    }
}
REVISIONS["card_1100"] = {
    "example": {
        "ja": "<ruby>初<rt>はじ</rt></ruby>めて<ruby>新幹線<rt>しんかんせん</rt></ruby>に<ruby>乗<rt>の</rt></ruby>った。",
        "en": "I rode the Shinkansen for the first time.",
        "zh_TW": "第一次坐了新幹線。",
        "zh_CN": "第一次坐了新干线。",
        "ko": "처음으로 신칸센을 탔다.",
        "zh_HK": "第一次搭新幹線。",
        "fr": "J'ai pris le Shinkansen pour la première fois."
    }
}
REVISIONS["card_1101"] = {
    "example": {
        "ja": "<ruby>目的<rt>もくてき</rt></ruby>の<ruby>駅<rt>えき</rt></ruby>に<ruby>着<rt>つ</rt></ruby>いたので、<ruby>電車<rt>でんしゃ</rt></ruby>を<ruby>降<rt>お</rt></ruby>りた。",
        "en": "Having arrived at the destination station, I got off the train.",
        "zh_TW": "到了目的車站，便下了電車。",
        "zh_CN": "到了目的车站，便下了电车。",
        "ko": "목적지 역에 도착해서 전철에서 내렸다.",
        "zh_HK": "去到目的地車站，就落咗火車。",
        "fr": "Arrivé à la gare de destination, je suis descendu du train."
    }
}
REVISIONS["card_1102"] = {
    "example": {
        "ja": "<ruby>風邪<rt>かぜ</rt></ruby>をひいたので、<ruby>昨日<rt>きのう</rt></ruby>は<ruby>学校<rt>がっこう</rt></ruby>を<ruby>休<rt>やす</rt></ruby>んだ。",
        "en": "Because I caught a cold, I took the day off school yesterday.",
        "zh_TW": "因為感冒了，昨天向學校請假休息了。",
        "zh_CN": "因为感冒了，昨天向学校请假休息了。",
        "ko": "감기에 걸려서 어제는 학교를 쉬었다.",
        "zh_HK": "因為親咗，琴日請假冇返學。",
        "fr": "Comme j'avais attrapé un rhume, je n'ai pas été à l'école hier."
    }
}
REVISIONS["card_1103"] = {
    "example": {
        "ja": "<ruby>休日<rt>きゅうじつ</rt></ruby>にテーマパークで<ruby>一日中<rt>いちにちじゅう</rt></ruby><ruby>遊<rt>あそ</rt></ruby>んだ。",
        "en": "I played all day at the theme park on my day off.",
        "zh_TW": "休假日去主題樂園玩了一整天。",
        "zh_CN": "休假日去主题乐园玩了一整天。",
        "ko": "휴일에 테마파크에서 하루 종일 놀았다.",
        "zh_HK": "放假嗰陣去主題樂園玩咗成日。",
        "fr": "J'ai passé toute la journée à m'amuser au parc à thème pendant mon jour de congé."
    }
}

# 基本動詞 たform (2)
REVISIONS["card_1104"] = {
    "example": {
        "ja": "<ruby>朝<rt>あさ</rt></ruby>7<ruby>時<rt>じ</rt></ruby>に<ruby>家<rt>いえ</rt></ruby>を<ruby>出<rt>で</rt></ruby>た。",
        "en": "I left the house at 7 AM.",
        "zh_TW": "早上七點出了門。",
        "zh_CN": "早上七点出了门。",
        "ko": "아침 7시에 집을 나왔다.",
        "zh_HK": "朝早七點出咗門口。",
        "fr": "Je suis sorti de chez moi à 7 heures du matin."
    }
}
REVISIONS["card_1105"] = {
    "example": {
        "ja": "<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>ってきたので、<ruby>近<rt>ちか</rt></ruby>くのカフェに<ruby>入<rt>はい</rt></ruby>った。",
        "en": "Because it started to rain, I entered a nearby cafe.",
        "zh_TW": "因為下起雨來，進了附近的咖啡館。",
        "zh_CN": "因为下起雨来，进了附近的咖啡馆。",
        "ko": "비가 내리기 시작해서 근처 카페에 들어갔다.",
        "zh_HK": "因為開始落雨，就入咗附近間cafe。",
        "fr": "Comme il s'est mis à pleuvoir, je suis entré dans un café à proximité."
    }
}
REVISIONS["card_1106"] = {
    "example": {
        "ja": "<ruby>新幹線<rt>しんかんせん</rt></ruby>は<ruby>時間<rt>じかん</rt></ruby>どおりに<ruby>東京<rt>とうきょう</rt></ruby><ruby>駅<rt>えき</rt></ruby>に<ruby>着<rt>つ</rt></ruby>いた。",
        "en": "The Shinkansen arrived at Tokyo Station on schedule.",
        "zh_TW": "新幹線準時到達了東京站。",
        "zh_CN": "新干线准时到达了东京站。",
        "ko": "신칸센은 시간대로 도쿄역에 도착했다.",
        "zh_HK": "新幹線準時去到東京站。",
        "fr": "Le Shinkansen est arrivé à la gare de Tokyo à l'heure prévue."
    }
}
REVISIONS["card_1108"] = {
    "example": {
        "ja": "<ruby>健康<rt>けんこう</rt></ruby>のために、<ruby>昨日<rt>きのう</rt></ruby>は1<ruby>万<rt>まん</rt></ruby><ruby>歩<rt>ぽ</rt></ruby><ruby>歩<rt>ある</rt></ruby>いた。",
        "en": "For my health, I walked 10,000 steps yesterday.",
        "zh_TW": "為了健康，昨天走了一萬步。",
        "zh_CN": "为了健康，昨天走了一万步。",
        "ko": "건강을 위해 어제는 1만 보를 걸었다.",
        "zh_HK": "為咗健康，琴日行咗一萬步。",
        "fr": "Pour ma santé, j'ai marché 10 000 pas hier."
    }
}
REVISIONS["card_1109"] = {
    "example": {
        "ja": "<ruby>遅刻<rt>ちこく</rt></ruby>しそうだったので、<ruby>駅<rt>えき</rt></ruby>まで<ruby>全力<rt>ぜんりょく</rt></ruby>で<ruby>走<rt>はし</rt></ruby>った。",
        "en": "Because I seemed likely to be late, I ran to the station with all my might.",
        "zh_TW": "因為快要遲到了，全力跑向了車站。",
        "zh_CN": "因为快要迟到了，全力跑向了车站。",
        "ko": "지각할 것 같아서 역까지 전력으로 달렸다.",
        "zh_HK": "就嚟遲到，所以博命跑去車站。",
        "fr": "Comme je risquais d'être en retard, j'ai couru de toutes mes forces jusqu'à la gare."
    }
}
REVISIONS["card_1110"] = {
    "example": {
        "ja": "<ruby>朝<rt>あさ</rt></ruby>7<ruby>時<rt>じ</rt></ruby>に、まだ<ruby>眠<rt>ねむ</rt></ruby>っている<ruby>弟<rt>おとうと</rt></ruby>を<ruby>起<rt>お</rt></ruby>こした。",
        "en": "At 7 AM, I woke up my younger brother who was still sleeping.",
        "zh_TW": "早上七點叫醒了還在睡覺的弟弟。",
        "zh_CN": "早上七点叫醒了还在睡觉的弟弟。",
        "ko": "아침 7시에 아직 자고 있는 남동생을 깨웠다.",
        "zh_HK": "朝早七點叫醒咗仲瞓緊嘅細佬。",
        "fr": "À 7 heures du matin, j'ai réveillé mon petit frère qui dormait encore."
    }
}
REVISIONS["card_1111"] = {
    "example": {
        "ja": "<ruby>帰宅<rt>きたく</rt></ruby>してすぐに、<ruby>石鹸<rt>せっけん</rt></ruby>で<ruby>手<rt>て</rt></ruby>をキレイに<ruby>洗<rt>あら</rt></ruby>った。",
        "en": "Right after coming home, I washed my hands cleanly with soap.",
        "zh_TW": "一回到家就馬上用肥皂把手洗得乾乾淨淨。",
        "zh_CN": "一回到家就马上用肥皂把手洗得干干净净。",
        "ko": "귀가하자마자 비누로 손을 깨끗이 씻었다.",
        "zh_HK": "一返到屋企即刻用番梘洗乾淨隻手。",
        "fr": "Dès que je suis rentré chez moi, je me suis bien lavé les mains avec du savon."
    }
}
REVISIONS["card_1112"] = {
    "example": {
        "ja": "<ruby>今日<rt>きょう</rt></ruby>は<ruby>寒<rt>さむ</rt></ruby>かったので、<ruby>厚手<rt>あつで</rt></ruby>のセーターを<ruby>着<rt>き</rt></ruby>た。",
        "en": "Because it was cold today, I wore a thick sweater.",
        "zh_TW": "因為今天很冷，所以穿了厚毛衣。",
        "zh_CN": "因为今天很冷，所以穿了厚毛衣。",
        "ko": "오늘은 추워서 두꺼운 스웨터를 입었다.",
        "zh_HK": "今日好凍，所以著咗件厚毛衣。",
        "fr": "Comme il faisait froid aujourd'hui, j'ai mis un pull épais."
    }
}
REVISIONS["card_1113"] = {
    "example": {
        "ja": "<ruby>玄関<rt>げんかん</rt></ruby>で<ruby>靴<rt>くつ</rt></ruby>を<ruby>脱<rt>ぬ</rt></ruby>いだ。",
        "en": "I took off my shoes at the entrance.",
        "zh_TW": "在玄關脫了鞋。",
        "zh_CN": "在玄关脱了鞋。",
        "ko": "현관에서 신발을 벗었다.",
        "zh_HK": "喺玄關除咗鞋。",
        "fr": "J'ai enlevé mes chaussures à l'entrée."
    }
}
REVISIONS["card_1114"] = {
    "example": {
        "ja": "<ruby>空気<rt>くうき</rt></ruby>を<ruby>入<rt>い</rt></ruby>れ<ruby>換<rt>か</rt></ruby>えるために、<ruby>窓<rt>まど</rt></ruby>を<ruby>開<rt>あ</rt></ruby>けた。",
        "en": "To air out the room, I opened the window.",
        "zh_TW": "為了換氣通風，打開了窗戶。",
        "zh_CN": "为了换气通风，打开了窗户。",
        "ko": "공기를 환기하기 위해 창문을 열었다.",
        "zh_HK": "為咗換氣透氣，開咗隻窗。",
        "fr": "Pour aérer la pièce, j'ai ouvert la fenêtre."
    }
}
REVISIONS["card_1116"] = {
    "example": {
        "ja": "レシピを<ruby>調<rt>しら</rt></ruby>べるために、スマホを<ruby>使<rt>つか</rt></ruby>った。",
        "en": "To look up a recipe, I used my smartphone.",
        "zh_TW": "為了查食譜，用了智慧型手機。",
        "zh_CN": "为了查食谱，用了智能手机。",
        "ko": "레시피를 검색하기 위해 스마트폰을 썼다.",
        "zh_HK": "為咗搵食譜，用咗部智能手機。",
        "fr": "Pour chercher une recette, j'ai utilisé mon smartphone."
    }
}
REVISIONS["card_1117"] = {
    "example": {
        "ja": "<ruby>夕飯<rt>ゆうはん</rt></ruby>に、<ruby>野菜<rt>やさい</rt></ruby>たっぷりのカレーを<ruby>作<rt>つく</rt></ruby>った。",
        "en": "For dinner, I made curry with plenty of vegetables.",
        "zh_TW": "晚飯做了滿滿蔬菜的咖喱。",
        "zh_CN": "晚饭做了满满蔬菜的咖喱。",
        "ko": "저녁으로 야채가 듬뿍 들어간 카레를 만들었다.",
        "zh_HK": "晚餐煮咗好多菜嘅咖喱。",
        "fr": "Pour le dîner, j'ai préparé un curry avec plein de légumes."
    }
}
REVISIONS["card_1118"] = {
    "example": {
        "ja": "<ruby>料理<rt>りょうり</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>に、<ruby>包丁<rt>ほうちょう</rt></ruby>でトマトを<ruby>薄<rt>うす</rt></ruby>く<ruby>切<rt>き</rt></ruby>った。",
        "en": "Before cooking, I sliced the tomatoes thinly with a kitchen knife.",
        "zh_TW": "做菜前用菜刀把番茄切成了薄片。",
        "zh_CN": "做菜前用菜刀把番茄切成了薄片。",
        "ko": "요리하기 전에 칼로 토마토를 얇게 썰었다.",
        "zh_HK": "煮飯之前用菜刀將番茄切薄片。",
        "fr": "Avant de cuisiner, j'ai tranché finement les tomates avec un couteau."
    }
}
REVISIONS["card_1119"] = {
    "example": {
        "ja": "<ruby>旅先<rt>たびさき</rt></ruby>から、<ruby>友達<rt>ともだち</rt></ruby>にポストカードを<ruby>書<rt>か</rt></ruby>いた。",
        "en": "I wrote a postcard to my friend from my trip destination.",
        "zh_TW": "從旅行地給朋友寫了一張明信片。",
        "zh_CN": "从旅行地给朋友写了一张明信片。",
        "ko": "여행지에서 친구에게 엽서를 썼다.",
        "zh_HK": "喺旅行嘅地方寄明信片畀朋友。",
        "fr": "J'ai écrit une carte postale à un ami depuis mon lieu de voyage."
    }
}
REVISIONS["card_1120"] = {
    "example": {
        "ja": "<ruby>先生<rt>せんせい</rt></ruby>からの<ruby>質問<rt>しつもん</rt></ruby>に、ハッキリと<ruby>答<rt>こた</rt></ruby>えた。",
        "en": "I answered the teacher's question clearly.",
        "zh_TW": "清楚地回答了老師的提問。",
        "zh_CN": "清楚地回答了老师的提问。",
        "ko": "선생님의 질문에 또렷하게 대답했다.",
        "zh_HK": "好清楚咁答咗老師嘅問題。",
        "fr": "J'ai répondu clairement à la question du professeur."
    }
}
REVISIONS["card_1121"] = {
    "example": {
        "ja": "<ruby>道<rt>みち</rt></ruby>に<ruby>迷<rt>まよ</rt></ruby>っていた<ruby>観光客<rt>かんこうきゃく</rt></ruby>に、<ruby>駅<rt>えき</rt></ruby>への<ruby>行<rt>い</rt></ruby>き<ruby>方<rt>かた</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えた。",
        "en": "I showed the tourist who was lost the way to the station.",
        "zh_TW": "給迷路的遊客指引了去車站的路。",
        "zh_CN": "给迷路的游客指引了去车站的路。",
        "ko": "길을 잃은 관광객에게 역으로 가는 길을 알려주었다.",
        "zh_HK": "教迷路嘅遊客點樣去車站。",
        "fr": "J'ai indiqué le chemin de la gare aux touristes perdus."
    }
}
REVISIONS["card_1122"] = {
    "example": {
        "ja": "<ruby>遠<rt>とお</rt></ruby>くから、きれいな<ruby>鳥<rt>とり</rt></ruby>の<ruby>鳴<rt>な</rt></ruby>き<ruby>声<rt>ごえ</rt></ruby>が<ruby>聞<rt>き</rt></ruby>こえた。",
        "en": "From far away, I heard the beautiful chirping of birds.",
        "zh_TW": "遠處傳來了悅耳的鳥鳴聲。",
        "zh_CN": "远处传来了悦耳的鸟鸣声。",
        "ko": "멀리서 아름다운 새소리가 들렸다.",
        "zh_HK": "遠處傳嚟好聽嘅雀仔叫聲。",
        "fr": "De loin, j'ai entendu le chant harmonieux des oiseaux."
    }
}
REVISIONS["card_1123"] = {
    "example": {
        "ja": "ホテルの<ruby>窓<rt>まど</rt></ruby>から、きれいな<ruby>富士山<rt>ふじさん</rt></ruby>が<ruby>見<rt>み</rt></ruby>えた。",
        "en": "From the hotel window, I saw the beautiful Mount Fuji.",
        "zh_TW": "從飯店的窗戶看到了美麗的富士山。",
        "zh_CN": "从饭店的窗户看到了美丽的富士山。",
        "ko": "호텔 창문에서 아름다운 후지산이 보였다.",
        "zh_HK": "喺酒店隻窗望出去見到好靚嘅富士山。",
        "fr": "De la fenêtre de l'hôtel, j'ai vu le magnifique mont Fuji."
    }
}
REVISIONS["card_1124"] = {
    "example": {
        "ja": "バスがなかなか<ruby>来<rt>こ</rt></ruby>なかったので、30<ruby>分<rt>ぷん</rt></ruby>も<ruby>待<rt>ま</rt></ruby>った。",
        "en": "Because the bus wouldn't come, I waited for as long as 30 minutes.",
        "zh_TW": "因為公車一直不來，等了足足30分鐘。",
        "zh_CN": "因为公交一直不来，等了足足30分钟。",
        "ko": "버스가 좀처럼 오지 않아서 30분이나 기다렸다.",
        "zh_HK": "架巴士等極都唔嚟，足足等咗30分鐘。",
        "fr": "Comme le bus n'arrivait pas, j'ai attendu 30 minutes entières."
    }
}
REVISIONS["card_1125"] = {
    "example": {
        "ja": "この<ruby>映画<rt>えいが</rt></ruby>はとても<ruby>深<rt>ふか</rt></ruby>いストーリーだと<ruby>思<rt>おも</rt></ruby>った。",
        "en": "I thought this movie had a very deep storyline.",
        "zh_TW": "覺得這部電影的故事非常深刻。",
        "zh_CN": "觉得这部电影的故事非常深刻。",
        "ko": "이 영화는 매우 깊이 있는 스토리라고 생각했다.",
        "zh_HK": "覺得呢套戲嘅故事好有深度。",
        "fr": "J'ai pensé que ce film avait une histoire très profonde."
    }
}
REVISIONS["card_1126"] = {
    "example": {
        "ja": "ニュースを<ruby>見<rt>み</rt></ruby>て、そのことを<ruby>初<rt>はじ</rt></ruby>めて<ruby>知<rt>し</rt></ruby>った。",
        "en": "Watching the news, I learned of that fact for the first time.",
        "zh_TW": "看了新聞，才第一次得知這件事。",
        "zh_CN": "看了新闻，才第一次得知这件事。",
        "ko": "뉴스를 보고 그 사실을 처음 알았다.",
        "zh_HK": "睇咗新聞，先第一次知道呢件事。",
        "fr": "En regardant les nouvelles, j'ai appris ce fait pour la première fois."
    }
}
REVISIONS["card_1127"] = {
    "example": {
        "ja": "<ruby>先生<rt>せんせい</rt></ruby>の<ruby>説明<rt>せつめい</rt></ruby>の<ruby>後<rt>あと</rt></ruby>で、<ruby>文法<rt>ぶんぽう</rt></ruby>の<ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>がよくわかった。",
        "en": "After the teacher's explanation, I understood the grammar usage well.",
        "zh_TW": "聽了老師的解說後，很清楚語法的用法了。",
        "zh_CN": "听了老师的解说后，很清楚语法的用法了。",
        "ko": "선생님의 설명 후에 문법 사용법을 잘 알게 되었다.",
        "zh_HK": "聽完老師嘅解釋之後，好清楚文法點樣用。",
        "fr": "Après les explications du professeur, j'ai bien compris l'usage de la grammaire."
    }
}
REVISIONS["card_1128"] = {
    "example": {
        "ja": "<ruby>練習<rt>れんしゅう</rt></ruby>を<ruby>重<rt>かさ</rt></ruby>ねて、<ruby>難<rt>むずか</rt></ruby>しい<ruby>課題<rt>かだい</rt></ruby>が<ruby>無事<rt>ぶじ</rt></ruby>にできた！",
        "en": "With repeated practice, I successfully accomplished the difficult task!",
        "zh_TW": "經過反復練習，順利完成了難題！",
        "zh_CN": "经过反复练习，顺利完成了难题！",
        "ko": "연습을 거듭하여 어려운 과제를 무사히 해냈다!",
        "zh_HK": "經過反覆練習，順利完成咗個難題！",
        "fr": "À force d'entraînement, j'ai réussi sans problème cette tâche difficile !"
    }
}

# 基本動詞 たform (3)
REVISIONS["card_1129"] = {
    "example": {
        "ja": "<ruby>夏休<rt>なつやす</rt></ruby>みにホテルのプールでたっぷり<ruby>泳<rt>およ</rt></ruby>いだ。",
        "en": "I swam a lot in the hotel pool during the summer vacation.",
        "zh_TW": "暑假在飯店的泳池痛快地游了泳。",
        "zh_CN": "暑假在饭店的泳池痛快地游了泳。",
        "ko": "여름방학에 호텔 수영장에서 실컷 수영했다.",
        "zh_HK": "暑假喺酒店個泳池游咗好多水。",
        "fr": "Pendant les vacances d'été, j'ai bien nagé dans la piscine de l'hôtel."
    }
}
REVISIONS["card_1130"] = {
    "example": {
        "ja": "<ruby>一日中<rt>いちにちじゅう</rt></ruby><ruby>歩<rt>ある</rt></ruby>き<ruby>回<rt>まわ</rt></ruby>ったので、<ruby>足<rt>あし</rt></ruby>がとても<ruby>疲<rt>つか</rt></ruby>れた。",
        "en": "Because I walked around all day, my legs got very tired.",
        "zh_TW": "走了一整天，腳非常累。",
        "zh_CN": "走了一整天，脚非常累。",
        "ko": "하루 종일 걸어 다녀서 다리가 몹시 피곤했다.",
        "zh_HK": "行咗成日，隻腳好攰。",
        "fr": "Comme j'ai marché toute la journée, mes jambes étaient très fatiguées."
    }
}
REVISIONS["card_1131"] = {
    "example": {
        "ja": "<ruby>天気<rt>てんき</rt></ruby>がよかったので、<ruby>午後<rt>ごご</rt></ruby>から<ruby>公園<rt>こうえん</rt></ruby>へ<ruby>出掛<rt>でか</rt></ruby>けた。",
        "en": "Because the weather was nice, I went out to the park in the afternoon.",
        "zh_TW": "天氣很好，所以下午出門去了公園。",
        "zh_CN": "天气很好，所以下午出门去了公园。",
        "ko": "날씨가 좋아서 오후부터 공원으로 나갔다.",
        "zh_HK": "天氣好好，所以晏晝出咗去公園。",
        "fr": "Comme il faisait beau, je suis sorti au parc dans l'après-midi."
    }
}
REVISIONS["card_1132"] = {
    "example": {
        "ja": "<ruby>部屋<rt>へや</rt></ruby>が<ruby>暗<rt>くら</rt></ruby>くなったので、<ruby>電気<rt>でんき</rt></ruby>をつけた。",
        "en": "Because the room became dark, I turned on the light.",
        "zh_TW": "房間變暗了，所以開了燈。",
        "zh_CN": "房间变暗了，所以开了灯。",
        "ko": "방이 어두워져서 불을 켰다.",
        "zh_HK": "間房黑咗，所以開咗燈。",
        "fr": "Comme la pièce s'assombrissait, j'ai allumé la lumière."
    }
}
REVISIONS["card_1133"] = {
    "example": {
        "ja": "<ruby>寝<rt>ね</rt></ruby>る<ruby>前<rt>まえ</rt></ruby>に、テレビの<ruby>電源<rt>でんげん</rt></ruby>をしっかり<ruby>消<rt>け</rt></ruby>した。",
        "en": "Before going to sleep, I made sure to turn off the TV.",
        "zh_TW": "睡前好好關掉了電視電源。",
        "zh_CN": "睡前好好关掉了电视电源。",
        "ko": "자기 전에 TV 전원을 확실하게 껐다.",
        "zh_HK": "瞓覺之前熄好咗電視嘅電源。",
        "fr": "Avant de me coucher, j'ai bien éteint la télévision."
    }
}
REVISIONS["card_1134"] = {
    "example": {
        "ja": "<ruby>電車<rt>でんしゃ</rt></ruby>に<ruby>間<rt>ま</rt></ruby>に<ruby>合<rt>あ</rt></ruby>うように、<ruby>早足<rt>はやあし</rt></ruby>で<ruby>急<rt>いそ</rt></ruby>いだ。",
        "en": "To make it in time for the train, I hurried briskly.",
        "zh_TW": "為了趕上電車，快步趕路。",
        "zh_CN": "为了赶上电车，快步赶路。",
        "ko": "기차 시간에 맞추기 위해 빠른 걸음으로 서둘렀다.",
        "zh_HK": "為咗趕火車，行得好快咁趕路。",
        "fr": "Pour arriver à l'heure pour le train, je me suis dépêché au pas de course."
    }
}
REVISIONS["card_1135"] = {
    "example": {
        "ja": "<ruby>駅<rt>えき</rt></ruby>の<ruby>改札<rt>かいさつ</rt></ruby><ruby>前<rt>まえ</rt></ruby>で、<ruby>友達<rt>ともだち</rt></ruby>が<ruby>来<rt>く</rt></ruby>るのを<ruby>待<rt>ま</rt></ruby>った。",
        "en": "In front of the station ticket gate, I waited for my friend to arrive.",
        "zh_TW": "在車站剪票口前等朋友來。",
        "zh_CN": "在车站检票口前等朋友来。",
        "ko": "역 개찰구 앞에서 친구가 오기를 기다렸다.",
        "zh_HK": "喺車站入閘機前面等朋友嚟。",
        "fr": "Devant les portillons de la gare, j'ai attendu l'arrivée de mon ami."
    }
}
REVISIONS["card_1136"] = {
    "example": {
        "ja": "<ruby>重<rt>おも</rt></ruby>い<ruby>荷物<rt>にもつ</rt></ruby>を<ruby>両手<rt>りょうて</rt></ruby>でしっかりと<ruby>持<rt>も</rt></ruby>った。",
        "en": "I held the heavy luggage firmly with both hands.",
        "zh_TW": "雙手緊緊拿著沈重的行李。",
        "zh_CN": "双手紧紧拿着沉重的行李。",
        "ko": "무거운 짐을 양손으로 단단히 들었다.",
        "zh_HK": "用雙手緊緊拎住好重嘅行李。",
        "fr": "J'ai tenu fermement les bagages lourds à deux mains."
    }
}
REVISIONS["card_1137"] = {
    "example": {
        "ja": "テストで100<ruby>点<rt>てん</rt></ruby>を<ruby>取<rt>と</rt></ruby>った。",
        "en": "I got 100 points on the test.",
        "zh_TW": "考試考了100分。",
        "zh_CN": "考试考了100分。",
        "ko": "시험에서 100점을 받았다.",
        "zh_HK": "考試攞咗100分。",
        "fr": "J'ai obtenu 100 points au test."
    }
}
REVISIONS["card_1138"] = {
    "example": {
        "ja": "<ruby>母<rt>はは</rt></ruby>の<ruby>料理<rt>りょうり</rt></ruby>を<ruby>楽<rt>たの</rt></ruby>しく<ruby>手伝<rt>てつだ</rt></ruby>った。",
        "en": "I enjoyed helping my mother with the cooking.",
        "zh_TW": "開心地幫媽媽做飯。",
        "zh_CN": "开心地帮妈妈做饭。",
        "ko": "어머니의 요리를 즐겁게 도왔다.",
        "zh_HK": "好開心咁幫媽咪煮飯。",
        "fr": "J'ai pris plaisir à aider ma mère à cuisiner."
    }
}
REVISIONS["card_1139"] = {
    "example": {
        "ja": "<ruby>道<rt>みち</rt></ruby>に<ruby>迷<rt>まよ</rt></ruby>っていた<ruby>人<rt>ひと</rt></ruby>を<ruby>優<rt>やさ</rt></ruby>しく<ruby>助<rt>たす</rt></ruby>けた。",
        "en": "I kindly helped a person who was lost.",
        "zh_TW": "熱心幫助了迷路的人。",
        "zh_CN": "热心帮助了迷路的人。",
        "ko": "길을 잃은 사람을 친절하게 도왔다.",
        "zh_HK": "好心幫咗個迷路嘅人。",
        "fr": "J'ai gentiment aidé une personne qui s'était égarée."
    }
}
REVISIONS["card_1140"] = {
    "example": {
        "ja": "<ruby>先生<rt>せんせい</rt></ruby>と<ruby>将来<rt>しょうらい</rt></ruby>の<ruby>夢<rt>ゆめ</rt></ruby>についてじっくり<ruby>話<rt>はな</rt></ruby>した。",
        "en": "I talked thoroughly with my teacher about my future dreams.",
        "zh_TW": "和老師深入聊了未來的夢想。",
        "zh_CN": "和老师深入聊了未来的梦想。",
        "ko": "선생님과 장래 희망에 대해 차분히 이야기했다.",
        "zh_HK": "同老師好好傾咗下將來嘅夢想。",
        "fr": "J'ai discuté en profondeur de mes rêves d'avenir avec mon professeur."
    }
}
REVISIONS["card_1141"] = {
    "example": {
        "ja": "<ruby>大声<rt>おおごえ</rt></ruby>で<ruby>友達<rt>ともだち</rt></ruby>の<ruby>名前<rt>なまえ</rt></ruby>を<ruby>呼<rt>よ</rt></ruby>んだ。",
        "en": "I called my friend's name in a loud voice.",
        "zh_TW": "大聲喊了朋友的名字。",
        "zh_CN": "大声喊了朋友的名字。",
        "ko": "큰 소리로 친구의 이름을 불렀다.",
        "zh_HK": "大聲叫朋友個名。",
        "fr": "J'ai crié le nom de mon ami à haute voix."
    }
}
REVISIONS["card_1142"] = {
    "example": {
        "ja": "<ruby>旅行<rt>りょこう</rt></ruby>のきれいな<ruby>写真<rt>しゃしん</rt></ruby>を、<ruby>友達<rt>ともだち</rt></ruby>にたくさん<ruby>見<rt>み</rt></ruby>せた。",
        "en": "I showed many beautiful travel photos to my friend.",
        "zh_TW": "給朋友看了很多漂亮的旅行照片。",
        "zh_CN": "给朋友看了很多漂亮的旅行照片。",
        "ko": "여행의 예쁜 사진을 친구에게 많이 보여주었다.",
        "zh_HK": "畀朋友睇咗好多好靚嘅旅行相。",
        "fr": "J'ai montré beaucoup de belles photos de voyage à mon ami."
    }
}
REVISIONS["card_1143"] = {
    "example": {
        "ja": "<ruby>同僚<rt>どうりょう</rt></ruby>にパソコンの<ruby>便利<rt>べんり</rt></ruby>なショートカットを<ruby>教<rt>おし</rt></ruby>えた。",
        "en": "I taught my colleague useful computer shortcuts.",
        "zh_TW": "教了同事電腦上實用的快速鍵。",
        "zh_CN": "教了同事电脑上实用的快捷键。",
        "ko": "동료에게 컴퓨터의 유용한 단축키를 알려주었다.",
        "zh_HK": "教咗同事一啲好實用嘅電腦shortcut快捷掣。",
        "fr": "J'ai appris des raccourcis clavier utiles à mon collègue."
    }
}
REVISIONS["card_1144"] = {
    "example": {
        "ja": "<ruby>寒<rt>さむ</rt></ruby>い<ruby>冬<rt>ふゆ</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>に、<ruby>温<rt>あたた</rt></ruby>かいお<ruby>風呂<rt>ふろ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>った。",
        "en": "On a cold winter day, I took a warm bath.",
        "zh_TW": "在寒冷的冬日泡了舒服的熱水澡。",
        "zh_CN": "在寒冷的冬日泡了舒服的热水澡。",
        "ko": "추운 겨울날에 따뜻한 목욕을 했다.",
        "zh_HK": "喺好凍嘅冬天浸咗個好舒服嘅熱水涼。",
        "fr": "Par une froide journée d'hiver, j'ai pris un bon bain chaud."
    }
}
REVISIONS["card_1145"] = {
    "example": {
        "ja": "<ruby>雨<rt>あめ</rt></ruby>あがりの<ruby>空<rt>そら</rt></ruby>に、きれいな<ruby>虹<rt>にじ</rt></ruby>が<ruby>出<rt>で</rt></ruby>た。",
        "en": "A beautiful rainbow appeared in the sky after the rain.",
        "zh_TW": "雨後的空中出現了美麗的彩虹。",
        "zh_CN": "雨后的空中出现了美丽的彩虹。",
        "ko": "비가 갠 하늘에 예쁜 무지개가 떴다.",
        "zh_HK": "落完雨嘅天空出咗條好靚嘅彩虹。",
        "fr": "Un bel arc-en-ciel est apparu dans le ciel après la pluie."
    }
}
REVISIONS["card_1146"] = {
    "example": {
        "ja": "<ruby>夜<rt>よる</rt></ruby>の<ruby>間<rt>あいだ</rt></ruby>に<ruby>雪<rt>ゆき</rt></ruby>がたくさん<ruby>降<rt>ふ</rt></ruby>った。",
        "en": "A lot of snow fell during the night.",
        "zh_TW": "夜裡下了很多雪。",
        "zh_CN": "夜里下了很多雪。",
        "ko": "밤사이에 눈이 많이 내렸다.",
        "zh_HK": "琴晚成晚落咗好大雪。",
        "fr": "Il a beaucoup neigé pendant la nuit."
    }
}

# 基本動詞 たform (4)
REVISIONS["card_1147"] = {
    "example": {
        "ja": "ジョギングの<ruby>後<rt>あと</rt></ruby>で、さっぱりとシャワーを<ruby>浴<rt>あ</rt></ruby>びた。",
        "en": "After jogging, I took a refreshing shower.",
        "zh_TW": "慢跑後沖了個清爽的澡。",
        "zh_CN": "慢跑后冲了个清爽的澡。",
        "ko": "조깅 후에 개운하게 샤워를 했다.",
        "zh_HK": "跑完步之後沖咗個好舒服嘅涼。",
        "fr": "Après le jogging, j'ai pris une douche rafraîchissante."
    }
}
REVISIONS["card_1148"] = {
    "example": {
        "ja": "<ruby>新宿<rt>しんじゅく</rt></ruby><ruby>駅<rt>えき</rt></ruby>でJRから<ruby>地下鉄<rt>ちかてつ</rt></ruby>に<ruby>乗<rt>の</rt></ruby>り<ruby>換<rt>か</rt></ruby>えた。",
        "en": "I transferred from JR to the subway at Shinjuku Station.",
        "zh_TW": "在新宿站從JR換乘了地下鐵。",
        "zh_CN": "在新宿站从JR换乘了地铁。",
        "ko": "신주쿠역에서 JR에서 지하철로 환승했다.",
        "zh_HK": "喺新宿站由JR轉搭地下鐵。",
        "fr": "À la gare de Shinjuku, j'ai changé de la ligne JR au métro."
    }
}
REVISIONS["card_1149"] = {
    "example": {
        "ja": "<ruby>財布<rt>さいふ</rt></ruby>をしっかりとカバンの<ruby>中<rt>なか</rt></ruby>に<ruby>入<rt>い</rt></ruby>れた。",
        "en": "I put my wallet securely into my bag.",
        "zh_TW": "把錢包妥善放進了包包裡。",
        "zh_CN": "把钱包妥善放进了包包里。",
        "ko": "지갑을 가방 안에 단단히 넣었다.",
        "zh_HK": "將銀包妥妥帖帖咁擺咗入個袋入面。",
        "fr": "J'ai bien rangé mon portefeuille dans mon sac."
    }
}
REVISIONS["card_1150"] = {
    "example": {
        "ja": "<ruby>郵便局<rt>ゆうびんきょく</rt></ruby>のポストに、<ruby>友達<rt>ともだち</rt></ruby>への<ruby>手紙<rt>てがみ</rt></ruby>を<ruby>出<rt>だ</rt></ruby>した。",
        "en": "I dropped the letter to my friend into the postbox at the post office.",
        "zh_TW": "在郵局的郵筒裡寄出了給朋友的信。",
        "zh_CN": "在邮局的邮箱里寄出了给朋友的信。",
        "ko": "우체국 우체통에 친구에게 보내는 편지를 넣었다.",
        "zh_HK": "喺郵局個郵筒度寄咗封信畀朋友。",
        "fr": "J'ai posté la lettre pour mon ami dans la boîte aux lettres de la poste."
    }
}
REVISIONS["card_1151"] = {
    "example": {
        "ja": "ピンポンとインターホンのボタンを<ruby>押<rt>お</rt></ruby>した。",
        "en": "I pressed the intercom buzzer button with a chime.",
        "zh_TW": "叮咚一聲按下了對講機的按鈕。",
        "zh_CN": "叮咚一声按下了对讲机的按钮。",
        "ko": "딩동 하고 인터폰 버튼을 눌렀다.",
        "zh_HK": "叮咚一聲撳咗門鐘對講機掣。",
        "fr": "J'ai appuyé sur le bouton de l'interphone."
    }
}
REVISIONS["card_1152"] = {
    "example": {
        "ja": "<ruby>買<rt>か</rt></ruby>ってきたお<ruby>花<rt>はな</rt></ruby>を、テーブルの<ruby>上<rt>うえ</rt></ruby>に<ruby>置<rt>お</rt></ruby>いた。",
        "en": "I placed the flowers I bought on the table.",
        "zh_TW": "把買回來的花擺在桌子上。",
        "zh_CN": "把买回来的花摆在桌子上。",
        "ko": "사 온 꽃을 테이블 위에 놓았다.",
        "zh_HK": "將買返嚟嘅花擺咗喺張枱上面。",
        "fr": "J'ai posé sur la table les fleurs que je venais d'acheter."
    }
}
REVISIONS["card_1153"] = {
    "example": {
        "ja": "<ruby>友達<rt>ともだち</rt></ruby>のために、バースデーカードを<ruby>作<rt>つく</rt></ruby>った。",
        "en": "I made a birthday card for my friend.",
        "zh_TW": "為朋友親手做了生日卡片。",
        "zh_CN": "为朋友亲手做了生日卡片。",
        "ko": "친구를 위해 생일 카드를 만들었다.",
        "zh_HK": "為朋友親手整咗張生日卡。",
        "fr": "J'ai fabriqué une carte d'anniversaire pour mon ami."
    }
}
REVISIONS["card_1154"] = {
    "example": {
        "ja": "<ruby>昔<rt>むかし</rt></ruby><ruby>使<rt>つか</rt></ruby>っていたゲーム<ruby>機<rt>き</rt></ruby>を、リサイクルショップで<ruby>売<rt>う</rt></ruby>った。",
        "en": "I sold the game console I used to play at a secondhand shop.",
        "zh_TW": "在二手店賣掉了以前用過的遊戲機。",
        "zh_CN": "在二手店卖掉了以前用过的游戏机。",
        "ko": "예전에 쓰던 게임기를 중고 매장에서 팔았다.",
        "zh_HK": "喺二手舖賣咗以前玩過嘅遊戲機。",
        "fr": "J'ai vendu mon ancienne console de jeux dans un magasin d'occasion."
    }
}
REVISIONS["card_1155"] = {
    "example": {
        "ja": "<ruby>車<rt>くるま</rt></ruby>をコインパーキングにしっかりと<ruby>止<rt>と</rt></ruby>めた。",
        "en": "I parked the car properly in the coin parking lot.",
        "zh_TW": "把車妥善停在了收費停車場。",
        "zh_CN": "把车妥善停在了收费停车场。",
        "ko": "차를 코인 주차장에 잘 세웠다.",
        "zh_HK": "將架車泊好喺計時停車場。",
        "fr": "J'ai bien garé la voiture dans le parking payant."
    }
}
REVISIONS["card_1156"] = {
    "example": {
        "ja": "<ruby>疲<rt>つか</rt></ruby>れたので、<ruby>公園<rt>こうえん</rt></ruby>のベンチにゆっくり<ruby>座<rt>すわ</rt></ruby>った。",
        "en": "Because I was tired, I sat down comfortably on the park bench.",
        "zh_TW": "因為累了，在公園的長椅上舒舒服服地坐了下來。",
        "zh_CN": "因为累了，在公园的长椅上舒舒服服地坐了下来。",
        "ko": "피곤해서 공원 벤치에 편안히 앉았다.",
        "zh_HK": "因為好攰，喺公園張長凳度坐咗陣。",
        "fr": "Comme j'étais fatigué, je me suis assis tranquillement sur un banc du parc."
    }
}
REVISIONS["card_1157"] = {
    "example": {
        "ja": "お<ruby>年寄<rt>としよ</rt></ruby>りに<ruby>席<rt>せき</rt></ruby>をゆずるため、スッと<ruby>立<rt>た</rt></ruby>った。",
        "en": "I stood up smoothly to give my seat to an elderly person.",
        "zh_TW": "為了給長者讓座，俐落地站了起來。",
        "zh_CN": "为了给老人让座，利落地站了起来。",
        "ko": "어르신께 자리를 양보하기 위해 벌떡 일어섰다.",
        "zh_HK": "為咗讓座畀長者，好快咁企咗起身。",
        "fr": "Je me suis levé aussitôt pour céder ma place à une personne âgée."
    }
}
REVISIONS["card_1158"] = {
    "example": {
        "ja": "<ruby>大学<rt>だいがく</rt></ruby><ruby>時代<rt>じだい</rt></ruby>に、４<ruby>年間<rt>ねんかん</rt></ruby><ruby>京都<rt>きょうと</rt></ruby>に<ruby>住<rt>す</rt></ruby>んだ。",
        "en": "During my university days, I lived in Kyoto for four years.",
        "zh_TW": "大學時代在京都住了四年。",
        "zh_CN": "大学时代在京都住了四年。",
        "ko": "대학 시절에 4년 동안 교토에 살았다.",
        "zh_HK": "讀大學嗰陣喺京都住咗四年。",
        "fr": "Pendant mes années universitaires, j'ai vécu quatre ans à Kyoto."
    }
}
REVISIONS["card_1159"] = {
    "example": {
        "ja": "<ruby>朝<rt>あさ</rt></ruby>の<ruby>新鮮<rt>しんせん</rt></ruby>な<ruby>空気<rt>くうき</rt></ruby>を<ruby>深<rt>ふか</rt></ruby>く<ruby>吸<rt>す</rt></ruby>った。",
        "en": "I deeply inhaled the morning's fresh air.",
        "zh_TW": "深深吸了一口早晨新鮮的空氣。",
        "zh_CN": "深深吸了一口早晨新鲜的空气。",
        "ko": "아침의 신선한 공기를 깊게 들이마셨다.",
        "zh_HK": "深呼吸吸咗一啖朝早嘅新鮮空氣。",
        "fr": "J'ai inspiré profondément l'air frais du matin."
    }
}
REVISIONS["card_1160"] = {
    "example": {
        "ja": "<ruby>動画<rt>どうが</rt></ruby>を<ruby>見<rt>み</rt></ruby>て、<ruby>駅<rt>えき</rt></ruby>までのルートをしっかり<ruby>覚<rt>おぼ</rt></ruby>えた。",
        "en": "I watched the video and memorized the route to the station thoroughly.",
        "zh_TW": "看著影片牢牢記住了去車站的路線。",
        "zh_CN": "看着视频牢牢记住了去车站的路线。",
        "ko": "영상을 보고 역까지 가는 경로를 확실하게 외웠다.",
        "zh_HK": "睇片記熟咗去車站嘅行法。",
        "fr": "J'ai regardé la vidéo et j'ai bien mémorisé l'itinéraire jusqu'à la gare."
    }
}
REVISIONS["card_1161"] = {
    "example": {
        "ja": "<ruby>急<rt>いそ</rt></ruby>いでいたので、スマホを<ruby>家<rt>いえ</rt></ruby>に<ruby>忘<rt>わす</rt></ruby>れた。",
        "en": "Because I was in a rush, I forgot my smartphone at home.",
        "zh_TW": "因為趕時間，把手機忘在家裡了。",
        "zh_CN": "因为赶时间，把手机忘在家里了。",
        "ko": "서두르느라 스마트폰을 집에 두고 왔다.",
        "zh_HK": "因為趕時間，擺低咗部手機喺屋企唔記得拎。",
        "fr": "Comme j'étais pressé, j'ai oublié mon smartphone à la maison."
    }
}
REVISIONS["card_1162"] = {
    "example": {
        "ja": "<ruby>家<rt>いえ</rt></ruby>の<ruby>鍵<rt>かぎ</rt></ruby>を<ruby>失<rt>な</rt></ruby>くした。",
        "en": "I lost my house key.",
        "zh_TW": "把家裡的鑰匙弄丟了。",
        "zh_CN": "把家里的钥匙弄丢了。",
        "ko": "집 열쇠를 잃어버렸다.",
        "zh_HK": "整唔見咗屋企條鎖匙。",
        "fr": "J'ai perdu la clé de ma maison."
    }
}
REVISIONS["card_1163"] = {
    "example": {
        "ja": "コンビニで<ruby>公共<rt>こうきょう</rt></ruby><ruby>料金<rt>りょうきん</rt></ruby>をしっかりと<ruby>払<rt>はら</rt></ruby>った。",
        "en": "I paid the utility bills properly at the convenience store.",
        "zh_TW": "在便利店繳清了公共事業費。",
        "zh_CN": "在便利店缴清了公共事业费。",
        "ko": "편의점에서 공공요금을 확실하게 냈다.",
        "zh_HK": "喺便利店交妥咗水電煤等雜費。",
        "fr": "J'ai bien payé mes factures d'eau et d'électricité au kombini."
    }
}
REVISIONS["card_1164"] = {
    "example": {
        "ja": "<ruby>友達<rt>ともだち</rt></ruby>から<ruby>借<rt>か</rt></ruby>りていた<ruby>本<rt>ほん</rt></ruby>を、お<ruby>礼<rt>れい</rt></ruby>を<ruby>言<rt>い</rt></ruby>って<ruby>返<rt>かえ</rt></ruby>した。",
        "en": "I returned the book I borrowed from my friend with words of thanks.",
        "zh_TW": "向朋友道謝後歸還了借來的書。",
        "zh_CN": "向朋友道谢后归还了借来的书。",
        "ko": "친구에게 빌렸던 책을 고맙다고 인사하며 돌려주었다.",
        "zh_HK": "同朋友講多謝之後還返本書畀佢。",
        "fr": "J'ai rendu le livre que j'avais emprunté à mon ami en le remerciant."
    }
}
REVISIONS["card_1165"] = {
    "example": {
        "ja": "<ruby>長年<rt>ながねん</rt></ruby><ruby>勤<rt>つと</rt></ruby>めた<ruby>会社<rt>かいしゃ</rt></ruby>を<ruby>円満<rt>えんまん</rt></ruby>に<ruby>辞<rt>や</rt></ruby>めた。",
        "en": "I left on good terms from the company where I worked for many years.",
        "zh_TW": "圓滿辭去了工作多年的公司。",
        "zh_CN": "圆满辞去了工作多年的公司。",
        "ko": "오랫동안 근무했던 회사를 원만하게 그만두었다.",
        "zh_HK": "好順利咁辭咗做咗好多年嘅公司。",
        "fr": "J'ai quitté en bons termes l'entreprise où j'avais travaillé de longues années."
    }
}

# 基本動詞 たform (5)
REVISIONS["card_1166"] = {
    "example": {
        "ja": "<ruby>辞書<rt>じしょ</rt></ruby>を<ruby>使<rt>つか</rt></ruby>って、<ruby>新<rt>あたら</rt></ruby>しい<ruby>単語<rt>たんご</rt></ruby>の<ruby>意味<rt>いみ</rt></ruby>を<ruby>詳<rt>くわ</rt></ruby>しく<ruby>調<rt>しら</rt></ruby>べた。",
        "en": "Using a dictionary, I looked up the meaning of the new word in detail.",
        "zh_TW": "用詞典詳細查了新單詞的意思。",
        "zh_CN": "用词典详细查了新单词的意思。",
        "ko": "사전을 사용하여 새로운 단어의 뜻을 자세히 알아보았다.",
        "zh_HK": "用字典好詳細咁查咗新生字嘅意思。",
        "fr": "En utilisant un dictionnaire, j'ai cherché en détail la signification du nouveau mot."
    }
}
REVISIONS["card_1167"] = {
    "example": {
        "ja": "パンクした<ruby>自転車<rt>じてんしゃ</rt></ruby>を、<ruby>自分<rt>じぶん</rt></ruby>の<ruby>手<rt>て</rt></ruby>でキレイに<ruby>修理<rt>しゅうり</rt></ruby>した。",
        "en": "I repaired the flat tire on my bicycle neatly with my own hands.",
        "zh_TW": "親手把漏氣的自行車修得完好如初。",
        "zh_CN": "亲手把漏气的自行车修得完好如初。",
        "ko": "펑크 난 자전거를 직접 손으로 말끔히 수리했다.",
        "zh_HK": "自己親手整返好爆咗胎嘅單車。",
        "fr": "J'ai réparé moi-même le pneu crevé de mon vélo avec succès."
    }
}
REVISIONS["card_1168"] = {
    "example": {
        "ja": "<ruby>集合<rt>しゅうごう</rt></ruby><ruby>場所<rt>ばしょ</rt></ruby>の<ruby>変更<rt>へんこう</rt></ruby>について、グループに<ruby>連絡<rt>れんらく</rt></ruby>した。",
        "en": "I contacted the group about the change of meeting place.",
        "zh_TW": "就集合地點的變更向群組發送了通知。",
        "zh_CN": "就集合地点的变更向群组发送了通知。",
        "ko": "집합 장소 변경에 대해 그룹에 연락했다.",
        "zh_HK": "喺group入面通知大家改咗集合地點。",
        "fr": "J'ai contacté le groupe pour le changement du lieu de rendez-vous."
    }
}
REVISIONS["card_1169"] = {
    "example": {
        "ja": "<ruby>箱根<rt>はこね</rt></ruby>の<ruby>温泉<rt>おんせん</rt></ruby><ruby>旅館<rt>りょかん</rt></ruby>に<ruby>泊<rt>と</rt></ruby>まった。",
        "en": "I stayed at a hot spring ryokan in Hakone.",
        "zh_TW": "入住了箱根的溫泉旅館。",
        "zh_CN": "入住了箱根的温泉旅馆。",
        "ko": "하코네의 온천 여관에 묵었다.",
        "zh_HK": "住咗喺箱根嘅溫泉旅館。",
        "fr": "J'ai logé dans un ryokan avec onsen à Hakone."
    }
}
REVISIONS["card_1170"] = {
    "example": {
        "ja": "<ruby>週末<rt>しゅうまつ</rt></ruby>に<ruby>部屋<rt>へや</rt></ruby>とキッチンをピカピカに<ruby>掃除<rt>そうじ</rt></ruby>した。",
        "en": "Over the weekend, I cleaned my room and kitchen until they sparkled.",
        "zh_TW": "週末把房間和廚房打掃得閃閃發亮。",
        "zh_CN": "周末把房间和厨房打扫得闪闪发亮。",
        "ko": "주말에 방과 부엌을 반짝반짝하게 청소했다.",
        "zh_HK": "週末將間房同廚房打掃得乾淨到發令。",
        "fr": "Ce week-end, j'ai nettoyé ma chambre et ma cuisine pour qu'elles brillent comme un sou neuf."
    }
}
REVISIONS["card_1171"] = {
    "example": {
        "ja": "<ruby>晴<rt>は</rt></ruby>れたので、お<ruby>布団<rt>ふとん</rt></ruby>やシーツをまとめて<ruby>洗濯<rt>せんたく</rt></ruby>した。",
        "en": "Because it cleared up, I washed all my futons and bedsheets together.",
        "zh_TW": "因為天晴了，一口氣把棉被和床單都洗了。",
        "zh_CN": "因为天晴了，一口气把棉被和床单都洗了。",
        "ko": "날이 맑아서 이불과 시트를 한꺼번에 세탁했다.",
        "zh_HK": "見好天，一次過洗晒被同床單。",
        "fr": "Comme il faisait beau, j'ai lavé les futons et les draps en même temps."
    }
}
REVISIONS["card_1172"] = {
    "example": {
        "ja": "<ruby>発表会<rt>はっぴょうかい</rt></ruby>で、<ruby>心<rt>こころ</rt></ruby>を<ruby>込<rt>こ</rt></ruby>めてピアノを<ruby>弾<rt>ひ</rt></ruby>いた。",
        "en": "At the recital, I played the piano with all my heart.",
        "zh_TW": "在發表會上全心全意彈奏了鋼琴。",
        "zh_CN": "在发表会上全心全意弹奏了钢琴。",
        "ko": "발표회에서 온 마음을 다해 피아노를 쳤다.",
        "zh_HK": "喺發表會上好用心咁彈鋼琴。",
        "fr": "Lors du récital, j'ai joué du piano de tout mon cœur."
    }
}
REVISIONS["card_1173"] = {
    "example": {
        "ja": "カラオケで<ruby>友達<rt>ともだち</rt></ruby>と<ruby>一緒<rt>いっしょ</rt></ruby>に、たくさん<ruby>歌<rt>うた</rt></ruby>った。",
        "en": "I sang a lot together with my friends at karaoke.",
        "zh_TW": "在KTV和朋友一起唱了好多歌。",
        "zh_CN": "在KTV和朋友一起唱了好多歌。",
        "ko": "노래방에서 친구들과 함께 실컷 노래를 불렀다.",
        "zh_HK": "喺卡拉OK同朋友一齊唱咗好多歌。",
        "fr": "J'ai beaucoup chanté avec mes amis au karaoké."
    }
}
REVISIONS["card_1174"] = {
    "example": {
        "ja": "<ruby>日本<rt>にほん</rt></ruby><ruby>旅行<rt>りょこう</rt></ruby>の<ruby>記念<rt>きねん</rt></ruby>に、<ruby>各地<rt>かくち</rt></ruby>の<ruby>御朱印<rt>ごしゅいん</rt></ruby>を<ruby>集<rt>あつ</rt></ruby>めた。",
        "en": "As a souvenir of my Japan trip, I collected goshuin stamps from various places.",
        "zh_TW": "作為日本旅行的紀念，收集了各地的御朱印。",
        "zh_CN": "作为日本旅行的纪念，收集了各地的御朱印。",
        "ko": "일본 여행 기념으로 각지의 고슈인을 모았다.",
        "zh_HK": "為咗紀念日本旅行，收集咗唔同地方嘅御朱印。",
        "fr": "En souvenir de mon voyage au Japon, j'ai collectionné les goshuin de divers endroits."
    }
}
REVISIONS["card_1175"] = {
    "example": {
        "ja": "<ruby>大掃除<rt>おおそうじ</rt></ruby>で、<ruby>使<rt>つか</rt></ruby>わなくなった<ruby>古<rt>ふる</rt></ruby>いものを<ruby>思<rt>おも</rt></ruby>い<ruby>切<rt>き</rt></ruby>って<ruby>捨<rt>す</rt></ruby>てた。",
        "en": "During the big cleaning, I made up my mind to throw away old things I no longer used.",
        "zh_TW": "在大掃除中下定決心扔掉了不再使用的舊物。",
        "zh_CN": "在大扫除中下定决心扔掉了不再使用的旧物。",
        "ko": "대청소에서 쓰지 않게 된 오래된 물건을 과감히 버렸다.",
        "zh_HK": "喺大掃除度，決心抌咗啲冇用嘅舊嘢。",
        "fr": "Pendant le grand nettoyage, j'ai résolument jeté les vieux objets dont je ne me servais plus."
    }
}
REVISIONS["card_1176"] = {
    "example": {
        "ja": "<ruby>気分転換<rt>きぶんてんかん</rt></ruby>に、スマホのケースを<ruby>新<rt>あたら</rt></ruby>しいものに<ruby>変<rt>か</rt></ruby>えた。",
        "en": "For a change of mood, I changed my phone case to a new one.",
        "zh_TW": "為了轉換心情，把手機殼換成了新的。",
        "zh_CN": "为了转换心情，把手机壳换成了新的。",
        "ko": "기분 전환으로 스마트폰 케이스를 새것으로 바꿨다.",
        "zh_HK": "為咗轉下心情，換咗個新嘅電話殼。",
        "fr": "Pour changer d'air, j'ai remplacé ma coque de smartphone par une neuve."
    }
}
REVISIONS["card_1178"] = {
    "example": {
        "ja": "<ruby>家族<rt>かぞく</rt></ruby>とドライブに<ruby>行<rt>い</rt></ruby>くため、<ruby>安全<rt>あんぜん</rt></ruby>に<ruby>車<rt>くるま</rt></ruby>を<ruby>運転<rt>うんてん</rt></ruby>した。",
        "en": "To go on a drive with my family, I drove the car safely.",
        "zh_TW": "為了和家人去兜風，安全地開了車。",
        "zh_CN": "为了和家人去兜风，安全地开了车。",
        "ko": "가족과 드라이브를 가기 위해 안전하게 운전했다.",
        "zh_HK": "為咗同屋企人去兜風，好安全咁揸車。",
        "fr": "Pour aller faire une promenade en voiture en famille, j'ai conduit prudemment."
    }
}
REVISIONS["card_1179"] = {
    "example": {
        "ja": "<ruby>教習所<rt>きょうしゅうじょ</rt></ruby>に<ruby>通<rt>かよ</rt></ruby>って、<ruby>無事<rt>ぶじ</rt></ruby>に<ruby>運転<rt>うんてん</rt></ruby><ruby>免許<rt>めんきょ</rt></ruby>を<ruby>取<rt>と</rt></ruby>った！",
        "en": "I attended driving school and successfully obtained my driver's license!",
        "zh_TW": "去駕訓班上課，順利拿到了駕照！",
        "zh_CN": "去驾校上课，顺利拿到了驾照！",
        "ko": "운전면허학원에 다녀서 무사히 운전면허를 땄다!",
        "zh_HK": "去駕駛學院學車，順利考到車牌！",
        "fr": "Je suis allé à l'auto-école et j'ai obtenu mon permis de conduire avec succès !"
    }
}
REVISIONS["card_1180"] = {
    "example": {
        "ja": "<ruby>先生<rt>せんせい</rt></ruby>に「ありがとうございました」と<ruby>笑顔<rt>えがお</rt></ruby>で<ruby>言<rt>い</rt></ruby>った。",
        "en": "I said 'Thank you very much' to the teacher with a smile.",
        "zh_TW": "笑著對老師說了「謝謝」。",
        "zh_CN": "笑着对老师说了「谢谢」。",
        "ko": "선생님께 '감사합니다'라고 웃는 얼굴로 말했다.",
        "zh_HK": "笑笑口咁同老師講咗句「多謝你」。",
        "fr": "J'ai dit « merci beaucoup » au professeur avec un sourire."
    }
}
REVISIONS["card_1181"] = {
    "example": {
        "ja": "<ruby>雪道<rt>ゆきみち</rt></ruby>で<ruby>転<rt>ころ</rt></ruby>ばないよう、<ruby>足元<rt>あしもと</rt></ruby>に<ruby>気<rt>き</rt></ruby>を<ruby>付<rt>つ</rt></ruby>けた。",
        "en": "To avoid slipping on the snowy road, I watched my step carefully.",
        "zh_TW": "為了不在雪路上跌倒，特別小心了腳下。",
        "zh_CN": "为了不在雪路上跌倒，特别小心了脚下。",
        "ko": "눈길에서 넘어지지 않도록 발밑을 조심했다.",
        "zh_HK": "為咗唔喺雪地上跌親，好小心睇住腳下。",
        "fr": "Pour ne pas glisser sur la route enneigée, j'ai fait bien attention où je mettais les pieds."
    }
}
REVISIONS["card_1182"] = {
    "example": {
        "ja": "<ruby>去年<rt>きょねん</rt></ruby>の1<ruby>年間<rt>ねんかん</rt></ruby>、<ruby>東京<rt>とうきょう</rt></ruby>の<ruby>大学<rt>だいがく</rt></ruby>へ<ruby>留学<rt>りゅうがく</rt></ruby>した。",
        "en": "For one year last year, I studied abroad at a university in Tokyo.",
        "zh_TW": "去年的整整一年，在東京的大學留了學。",
        "zh_CN": "去年的整整一年，在东京的大学留了学。",
        "ko": "작년 1년 동안 도쿄의 대학교로 유학을 다녀왔다.",
        "zh_HK": "舊年整整一年，喺東京嘅大學留學。",
        "fr": "Pendant un an l'année dernière, j'ai fait mes études dans une université à Tokyo."
    }
}
REVISIONS["card_1183"] = {
    "example": {
        "ja": "<ruby>友達<rt>ともだち</rt></ruby>からの<ruby>返事<rt>へんじ</rt></ruby>が<ruby>遅<rt>おそ</rt></ruby>かったので、とても<ruby>心配<rt>しんぱい</rt></ruby>した。",
        "en": "Because my friend's reply was late, I was very worried.",
        "zh_TW": "因為朋友回信很慢，所以非常擔心。",
        "zh_CN": "因为朋友回信很慢，所以非常担心。",
        "ko": "친구의 답장이 늦어서 몹시 걱정했다.",
        "zh_HK": "因為朋友遲遲未覆，所以好擔心。",
        "fr": "Comme la réponse de mon ami tardait, je me suis beaucoup inquiété."
    }
}
REVISIONS["card_1184"] = {
    "example": {
        "ja": "ピクニックに、<ruby>手作<rt>てづく</rt></ruby>りのお<ruby>弁当<rt>べんとう</rt></ruby>を<ruby>持<rt>も</rt></ruby>って<ruby>行<rt>い</rt></ruby>った。",
        "en": "I took a homemade bento lunch to the picnic.",
        "zh_TW": "去野餐時帶了親手做的便當。",
        "zh_CN": "去野餐时带了亲手做的便当。",
        "ko": "소풍에 직접 만든 도시락을 가지고 갔다.",
        "zh_HK": "去野餐嗰陣帶咗自己整嘅便當去。",
        "fr": "Pour le pique-nique, j'ai apporté un bento fait maison."
    }
}
REVISIONS["card_1185"] = {
    "example": {
        "ja": "<ruby>旅行<rt>りょこう</rt></ruby>のお<ruby>土産<rt>みやげ</rt></ruby>を、みんなに<ruby>持<rt>も</rt></ruby>ってきた。",
        "en": "I brought souvenirs from the trip for everyone.",
        "zh_TW": "給大家帶來了旅行的特產手信。",
        "zh_CN": "给大家带来了旅行的特产手信。",
        "ko": "여행 선물을 모두에게 가져왔다.",
        "zh_HK": "帶咗旅行買嘅手信返嚟畀大家。",
        "fr": "J'ai apporté des souvenirs de voyage pour tout le monde."
    }
}
REVISIONS["card_1186"] = {
    "example": {
        "ja": "<ruby>晴<rt>は</rt></ruby>れた<ruby>午後<rt>ごご</rt></ruby>、ペットの<ruby>犬<rt>いぬ</rt></ruby>を<ruby>公園<rt>こうえん</rt></ruby>へ<ruby>連<rt>つ</rt></ruby>れて<ruby>行<rt>い</rt></ruby>った。",
        "en": "On a sunny afternoon, I took my pet dog to the park.",
        "zh_TW": "在晴朗的午後，帶了寵物狗去公園。",
        "zh_CN": "在晴朗的午后，带了宠物狗去公园。",
        "ko": "화창한 오후에 반려견을 공원으로 데려갔다.",
        "zh_HK": "喺好天嘅晏晝，帶咗隻狗去公園散步。",
        "fr": "Par un après-midi ensoleillé, j'ai emmené mon chien au parc."
    }
}
REVISIONS["card_1187"] = {
    "example": {
        "ja": "<ruby>今日<rt>きょう</rt></ruby>のパーティーに、<ruby>高校<rt>こうこう</rt></ruby><ruby>時代<rt>じだい</rt></ruby>の<ruby>親友<rt>しんゆう</rt></ruby>を<ruby>連<rt>つ</rt></ruby>れてきた。",
        "en": "I brought my best friend from high school to today's party.",
        "zh_TW": "把高中的摯友帶到了今天的派對上。",
        "zh_CN": "把高中的挚友带到了今天的派对上。",
        "ko": "오늘 파티에 고등학교 시절 절친을 데려왔다.",
        "zh_HK": "今日個party我帶咗中學最好嘅朋友嚟。",
        "fr": "J'ai amené mon meilleur ami du lycée à la fête d'aujourd'hui."
    }
}

print(f"Total revision entries prepared: {len(REVISIONS)}")

# Additional entries
ADDITIONAL_ENTRIES = {'card_0661': {'example': {'en': 'In the afternoon, I enter a quiet cafe.',
                           'fr': "Dans l'après-midi, j'entre dans un café tranquille.",
                           'ja': '<ruby>午後<rt>ごご</rt></ruby>、<ruby>静<rt>しず</rt></ruby>かなカフェに<ruby>入<rt>はい</rt></ruby>ります。',
                           'ko': '오후에 조용한 카페에 들어갑니다.',
                           'zh_CN': '下午走进一家安静的咖啡馆。',
                           'zh_HK': '晏晝入咗一間好靜嘅cafe。',
                           'zh_TW': '下午走進一家安靜的咖啡館。'}},
 'card_0969': {'example': {'en': 'Because my errands finished early, I can go to the concert.',
                           'fr': 'Comme mes courses se sont terminées tôt, je peux aller au concert.',
                           'ja': '<ruby>用事<rt>ようじ</rt></ruby>が<ruby>早<rt>はや</rt></ruby>く<ruby>終<rt>お</rt></ruby>わったので、コンサートに<ruby>行<rt>い</rt></ruby>ける。',
                           'ko': '볼일이 일찍 끝나서 콘서트에 갈 수 있다.',
                           'zh_CN': '因为事情办完得早，所以能去演唱会了。',
                           'zh_HK': '因為啲嘢好快做完，所以可以去演唱會喇。',
                           'zh_TW': '因為事情辦完得早，所以能去演唱會了。'}},
 'card_0992': {'example': {'en': "If it is convenient, you can come to tomorrow's party.",
                           'fr': 'Si cela vous convient, vous pouvez venir à la fête de demain.',
                           'ja': '<ruby>都合<rt>つごう</rt></ruby>がよければ、<ruby>明日<rt>あした</rt></ruby>のパーティーに<ruby>来<rt>こ</rt></ruby>られる。',
                           'ko': '형편이 좋으면 내일 파티에 올 수 있다.',
                           'zh_CN': '方便的话，可以来参加明天的派对。',
                           'zh_HK': '得閒嘅話，聽日個party可以嚟到。',
                           'zh_TW': '方便的話，可以來參加明天的派對。'}},
 'card_0993': {'example': {'en': 'Thanks to my effort, I can make difficult dishes too.',
                           'fr': 'Grâce à mes efforts, je peux même préparer des plats difficiles.',
                           'ja': '<ruby>努力<rt>どりょく</rt></ruby>したおかげで、<ruby>難<rt>むずか</rt></ruby>しい<ruby>料理<rt>りょうり</rt></ruby>もできる。',
                           'ko': '노력한 덕분에 어려운 요리도 할 수 있다.',
                           'zh_CN': '多亏努力，连难做的料理也会做了。',
                           'zh_HK': '多得努力，連咁難嘅菜式都整到。',
                           'zh_TW': '多虧努力，連難做的料理也會做了。'}},
 'card_0995': {'example': {'en': 'Can we enter this restaurant without a reservation?',
                           'fr': 'Peut-on entrer dans ce restaurant sans réservation ?',
                           'ja': '<ruby>予約<rt>よやく</rt></ruby>なしでも、このレストランに<ruby>入<rt>はい</rt></ruby>れますか？',
                           'ko': '예약이 없어도 이 식당에 들어갈 수 있습니까?',
                           'zh_CN': '即使没有预约，也能进这家餐厅吗？',
                           'zh_HK': '冇訂位嘅話，入唔入到呢間餐廳食飯？',
                           'zh_TW': '即使沒有預約，也能進這家餐廳嗎？'}},
 'card_1019': {'example': {'en': "Because I've practiced since childhood, I can swim 1 kilometer.",
                           'fr': "Comme j'ai appris depuis l'enfance, je peux nager 1 kilomètre.",
                           'ja': '<ruby>子<rt>こ</rt></ruby>どもの<ruby>頃<rt>ころ</rt></ruby>から<ruby>習<rt>なら</rt></ruby>っているので、1キロ<ruby>泳<rt>およ</rt></ruby>げる。',
                           'ko': '어릴 때부터 배웠기 때문에 1킬로미터 수영할 수 있다.',
                           'zh_CN': '因为从小就学，所以能游一公里。',
                           'zh_HK': '因為細個就學，所以游到一公里。',
                           'zh_TW': '因為從小就學，所以能遊一公里。'}},
 'card_1021': {'example': {'en': 'Because the rain stopped, I can finally go out.',
                           'fr': 'Comme la pluie a cessé, je peux enfin sortir.',
                           'ja': '<ruby>雨<rt>あめ</rt></ruby>がやんだので、やっと<ruby>外<rt>そと</rt></ruby>へ<ruby>出掛<rt>でか</rt></ruby>けられる。',
                           'ko': '비가 그쳐서 드디어 밖으로 외출할 수 있다.',
                           'zh_CN': '雨停了，终于可以出门了。',
                           'zh_HK': '落完雨，終於可以出街喇。',
                           'zh_TW': '雨停了，終於可以出門了。'}},
 'card_1022': {'example': {'en': 'Because I changed the remote batteries, I can turn on the air conditioner.',
                           'fr': "Comme j'ai changé les piles de la télécommande, je peux allumer la climatisation.",
                           'ja': 'リモコンの<ruby>電池<rt>でんち</rt></ruby>を<ruby>換<rt>か</rt></ruby>えたので、エアコンをつけられる。',
                           'ko': '리모컨 배터리를 갈아서 에어컨을 켤 수 있다.',
                           'zh_CN': '换了遥控器的电池，所以能开空调了。',
                           'zh_HK': '換咗遙控嘅電，所以開到冷氣喇。',
                           'zh_TW': '換了遙控器的電池，所以能開空調了。'}},
 'card_1023': {'example': {'en': 'With an erasable pen, you can erase words immediately even if you make a mistake.',
                           'fr': "Avec un stylo effaçable, on peut effacer tout de suite même en cas d'erreur.",
                           'ja': 'フリクションペンなら、<ruby>間違<rt>まちが</rt></ruby>えてもすぐに<ruby>字<rt>じ</rt></ruby>を<ruby>消<rt>け</rt></ruby>せる。',
                           'ko': '지워지는 펜이라면 틀려도 바로 글씨를 지울 수 있다.',
                           'zh_CN': '如果是可擦笔的话，即使写错也能马上擦掉。',
                           'zh_HK': '用擦得甩嘅原子筆，寫錯字都可以即刻擦得甩。',
                           'zh_TW': '如果是可擦筆的話，即使寫錯也能馬上擦掉。'}},
 'card_1024': {'example': {'en': 'If you call a taxi, you can still hurry in time for the Shinkansen.',
                           'fr': 'En appelant un taxi, on peut encore se dépêcher pour avoir le Shinkansen.',
                           'ja': 'タクシーを<ruby>呼<rt>よ</rt></ruby>べば、まだ<ruby>新幹線<rt>しんかんせん</rt></ruby>の<ruby>時間<rt>じかん</rt></ruby>に<ruby>急<rt>いそ</rt></ruby>げる。',
                           'ko': '택시를 부르면 아직 신칸센 시간에 맞출 수 있다.',
                           'zh_CN': '叫出租车的话，还能赶得上新干线的时间。',
                           'zh_HK': '叫架的士嘅話，仲可以趕得切新幹線班車。',
                           'zh_TW': '叫計程車的話，還能趕得上新幹線的時間。'}},
 'card_1025': {'example': {'en': "If I'm reading a book at a cafe, I can wait for about 30 more minutes.",
                           'fr': 'En lisant un livre au café, je peux attendre encore environ 30 minutes.',
                           'ja': 'カフェで<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みながらなら、あと30<ruby>分<rt>ぷん</rt></ruby>くらい<ruby>待<rt>ま</rt></ruby>てる。',
                           'ko': '카페에서 책을 읽으면서라면 앞으로 30분 정도는 기다릴 수 있다.',
                           'zh_CN': '在咖啡馆看书的话，还能再等大约30分钟。',
                           'zh_HK': '喺cafe睇住書嘅話，仲可以等多30分鐘左右。',
                           'zh_TW': '在咖啡館看書的話，還能再等大約30分鐘。'}},
 'card_1026': {'example': {'en': 'This suitcase is so light that you can hold it with one hand.',
                           'fr': "Cette valise est très légère, on peut la porter d'une seule main.",
                           'ja': 'このスーツケースはとても<ruby>軽<rt>かる</rt></ruby>いので、<ruby>片手<rt>かたて</rt></ruby>でも<ruby>持<rt>も</rt></ruby>てる。',
                           'ko': '이 여행용 가방은 매우 가벼워서 한 손으로도 들 수 있다.',
                           'zh_CN': '这个行李箱非常轻，单手也能拿得动。',
                           'zh_HK': '呢個行李喼好輕，單手都拎得起。',
                           'zh_TW': '這個行李箱非常輕，單手也能拿得動。'}},
 'card_1028': {'example': {'en': 'Because I have no plans in the afternoon, I can help with moving.',
                           'fr': "Comme je n'ai rien de prévu cet après-midi, je peux aider pour le déménagement.",
                           'ja': '<ruby>午後<rt>ごご</rt></ruby>は<ruby>予定<rt>よてい</rt></ruby>がないので、<ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>しを<ruby>手伝<rt>てつだ</rt></ruby>える。',
                           'ko': '오후에는 일정이 없어서 이사를 도울 수 있다.',
                           'zh_CN': '下午没有安排，所以能帮忙搬家。',
                           'zh_HK': '晏晝冇嘢做，所以幫手搬屋。',
                           'zh_TW': '下午沒有安排，所以能幫忙搬家。'}},
 'card_1030': {'example': {'en': 'Thanks to practicing every day, I can speak daily conversation in Japanese.',
                           'fr': 'Grâce à ma pratique quotidienne, je peux tenir une conversation quotidienne en '
                                 'japonais.',
                           'ja': '<ruby>毎日<rt>まいにち</rt></ruby><ruby>練習<rt>れんしゅう</rt></ruby>したおかげで、<ruby>日本語<rt>にほんご</rt></ruby>で<ruby>日常<rt>にちじょう</rt></ruby><ruby>会話<rt>かいわ</rt></ruby>が<ruby>話<rt>はな</rt></ruby>せる。',
                           'ko': '매일 연습한 덕분에 일본어로 일상 대화를 할 수 있다.',
                           'zh_CN': '多亏每天练习，现在能用日语进行日常对话了。',
                           'zh_HK': '多得每日練習，而家用日文講到日常對話喇。',
                           'zh_TW': '多虧每天練習，現在能用日語進行日常對話了。'}},
 'card_1031': {'example': {'en': 'If you use the smartphone app, you can call a taxi right away.',
                           'fr': "Avec l'application sur smartphone, on peut appeler un taxi immédiatement.",
                           'ja': 'スマホのアプリを<ruby>使<rt>つか</rt></ruby>えば、すぐにタクシーを<ruby>呼<rt>よ</rt></ruby>べる。',
                           'ko': '스마트폰 앱을 쓰면 바로 택시를 부를 수 있다.',
                           'zh_CN': '用手机App的话，马上就能叫到出租车。',
                           'zh_HK': '用手機App嘅話，即刻可以叫到架的士。',
                           'zh_TW': '用手機App的話，馬上就能叫到計程車。'}},
 'card_1032': {'example': {'en': "If it's the passport photo page, I can show it right now.",
                           'fr': "Si c'est la page photo du passeport, je peux la montrer tout de suite.",
                           'ja': 'パスポートの<ruby>写真<rt>しゃしん</rt></ruby>ページなら、<ruby>今<rt>いま</rt></ruby>すぐ<ruby>見<rt>み</rt></ruby>せられる。',
                           'ko': '여권의 사진 페이지라면 지금 바로 보여줄 수 있다.',
                           'zh_CN': '如果是护照的照片页，现在就能给你看。',
                           'zh_HK': '如果係護照相嗰一頁，而家即刻可以畀你睇。',
                           'zh_TW': '如果是護照的照片頁，現在就能給你看。'}},
 'card_1033': {'example': {'en': "If it's how to get to the station, I can draw a map and show you.",
                           'fr': "Pour le chemin vers la gare, je peux dessiner un plan pour vous l'expliquer.",
                           'ja': '<ruby>駅<rt>えき</rt></ruby>への<ruby>行<rt>い</rt></ruby>き<ruby>方<rt>かた</rt></ruby>なら、<ruby>地図<rt>ちず</rt></ruby>を<ruby>描<rt>か</rt></ruby>いて<ruby>教<rt>おし</rt></ruby>えられる。',
                           'ko': '역으로 가는 길이라면 지도를 그려서 알려줄 수 있다.',
                           'zh_CN': '去车站的路线，我可以画地图告诉你。',
                           'zh_HK': '去車站嘅行法，我可以畫張地圖教你。',
                           'zh_TW': '去車站的路線，我可以畫地圖告訴你。'}},
 'card_1034': {'example': {'en': 'If you take off your shoes, you can enter this Japanese-style room.',
                           'fr': 'En enlevant vos chaussures, vous pouvez entrer dans cette pièce japonaise.',
                           'ja': '<ruby>靴<rt>くつ</rt></ruby>を<ruby>脱<rt>ぬ</rt></ruby>げば、こちらの<ruby>和室<rt>わしつ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>れる。',
                           'ko': '신발을 벗으면 이 다다미방에 들어갈 수 있다.',
                           'zh_CN': '脱了鞋就能进这间日式房间。',
                           'zh_HK': '除咗鞋嘅話，就可以入呢間和室。',
                           'zh_TW': '脫了鞋就能進這間日式房間。'}},
 'card_1035': {'example': {'en': 'Because the meeting ended, I can finally answer the phone.',
                           'fr': 'Comme la réunion est terminée, je peux enfin répondre au téléphone.',
                           'ja': '<ruby>会議<rt>かいぎ</rt></ruby>が<ruby>終<rt>お</rt></ruby>わったので、やっと<ruby>電話<rt>でんわ</rt></ruby>に<ruby>出<rt>で</rt></ruby>られる。',
                           'ko': '회의가 끝나서 드디어 전화를 받을 수 있다.',
                           'zh_CN': '会议结束了，终于能接电话了。',
                           'zh_HK': '開完會，終於聽得電話喇。',
                           'zh_TW': '會議結束了，終於能接電話了。'}},
 'card_1037': {'example': {'en': 'You can take a warm shower after working out at the gym.',
                           'fr': 'Après la gym, on peut prendre une douche chaude.',
                           'ja': 'スポーツジムの<ruby>後<rt>あと</rt></ruby>で、<ruby>温<rt>あたた</rt></ruby>かいシャワーを<ruby>浴<rt>あ</rt></ruby>びられる。',
                           'ko': '헬스장 이용 후에 따뜻한 샤워를 할 수 있다.',
                           'zh_CN': '在健身房运动后可以洗个温水澡。',
                           'zh_HK': '喺gym做完運動之後可以沖個熱水涼。',
                           'zh_TW': '在健身房運動後可以洗個溫水澡。'}},
 'card_1038': {'example': {'en': 'From this platform, you can transfer directly to the subway.',
                           'fr': 'Depuis ce quai, vous pouvez changer directement pour le métro.',
                           'ja': 'このホームから、<ruby>地下鉄<rt>ちかてつ</rt></ruby>に<ruby>直接<rt>ちょくせつ</rt></ruby><ruby>乗<rt>の</rt></ruby>り<ruby>換<rt>か</rt></ruby>えられる。',
                           'ko': '이 승강장에서 지하철로 바로 환승할 수 있다.',
                           'zh_CN': '从这个站台可以直接换乘地铁。',
                           'zh_HK': '喺呢個月台可以直接轉搭地下鐵。',
                           'zh_TW': '從這個月台可以直接轉乘地下鐵。'}},
 'card_1039': {'example': {'en': 'In this backpack, you can easily fit a laptop too.',
                           'fr': 'Dans ce sac à dos, on peut ranger facilement un ordinateur portable.',
                           'ja': 'このリュックには、ノートパソコンもゆったり<ruby>入<rt>い</rt></ruby>れられる。',
                           'ko': '이 배낭에는 노트북도 넉넉히 넣을 수 있다.',
                           'zh_CN': '这个背包里连笔记本电脑也能轻松装下。',
                           'zh_HK': '呢個背囊好大，連部手提電腦都擺得落。',
                           'zh_TW': '這個背包裡連筆記型電腦也能輕鬆裝下。'}},
 'card_1040': {'example': {'en': 'Because homework finished early, I can submit the report before the deadline.',
                           'fr': 'Comme mes devoirs sont finis tôt, je peux rendre le rapport avant la date limite.',
                           'ja': '<ruby>宿題<rt>しゅくだい</rt></ruby>が<ruby>早<rt>はや</rt></ruby>く<ruby>終<rt>お</rt></ruby>わったので、<ruby>期限<rt>きげん</rt></ruby><ruby>前<rt>まえ</rt></ruby>にレポートを<ruby>出<rt>だ</rt></ruby>せる。',
                           'ko': '숙제가 일찍 끝나서 마감 전에 보고서를 제출할 수 있다.',
                           'zh_CN': '因为作业早早做完了，可以在截止日期前交报告。',
                           'zh_HK': '因為功課好快做完，可以在截止日期前交report報告。',
                           'zh_TW': '因為作業早早做完了，可以在截止日期前交報告。'}},
 'card_1041': {'example': {'en': 'Because I grew taller, I can press the high elevator buttons too.',
                           'fr': "Comme j'ai grandi, je peux appuyer même sur les boutons élevés de l'ascenseur.",
                           'ja': '<ruby>背<rt>せ</rt></ruby>が<ruby>伸<rt>の</rt></ruby>びたので、エレベーターの<ruby>高<rt>たか</rt></ruby>いボタンも<ruby>押<rt>お</rt></ruby>せる。',
                           'ko': '키가 커서 엘리베이터의 높은 버튼도 누를 수 있다.',
                           'zh_CN': '长高了之后，电梯较高的按钮也按得到了。',
                           'zh_HK': '高咗之後，升降機較高嘅掣都撳得到了。',
                           'zh_TW': '長高了之後，電梯較高的按鈕也按得到了。'}},
 'card_1042': {'example': {'en': 'Because the desk is spacious, you can place two monitors on it.',
                           'fr': 'Comme le bureau est grand, on peut y poser deux écrans.',
                           'ja': 'デスクが<ruby>広<rt>ひろ</rt></ruby>いので、モニターを２<ruby>台<rt>だい</rt></ruby><ruby>置<rt>お</rt></ruby>ける。',
                           'ko': '책상이 넓어서 모니터를 2대 놓을 수 있다.',
                           'zh_CN': '书桌很宽敞，可以放两台显示器。',
                           'zh_HK': '張枱好大，可以擺到兩部mon電腦螢幕。',
                           'zh_TW': '書桌很寬敞，可以放兩台螢幕。'}},
 'card_1045': {'example': {'en': 'In front of this apartment building, you can park the car.',
                           'fr': 'Devant cet immeuble, on peut garer la voiture.',
                           'ja': 'このマンションの<ruby>前<rt>まえ</rt></ruby>なら、<ruby>車<rt>くるま</rt></ruby>を<ruby>止<rt>と</rt></ruby>められる。',
                           'ko': '이 아파트 앞이라면 차를 세울 수 있다.',
                           'zh_CN': '在这栋公寓前面的话可以停车。',
                           'zh_HK': '喺呢座大廈前面嘅話可以泊車。',
                           'zh_TW': '在這棟公寓前面的話可以停車。'}},
 'card_1048': {'example': {'en': 'This neighborhood is safe, and you can live here with great peace of mind.',
                           'fr': 'Ce quartier est sûr et on peut y habiter en toute tranquillité.',
                           'ja': 'この<ruby>街<rt>まち</rt></ruby>は<ruby>治安<rt>ちあん</rt></ruby>がよく、とても<ruby>安心<rt>あんしん</rt></ruby>して<ruby>住<rt>す</rt></ruby>める。',
                           'ko': '이 동네는 치안이 좋아서 매우 안심하고 살 수 있다.',
                           'zh_CN': '这个小镇治安良好，能非常安心地居住。',
                           'zh_HK': '呢區治安好，可以好安心咁住。',
                           'zh_TW': '這個小鎮治安良好，能非常安心地居住。'}},
 'card_1050': {'example': {'en': 'Thanks to the flashcards, I can memorize new words quickly.',
                           'fr': 'Grâce aux cartes mémoire, on peut mémoriser rapidement de nouveaux mots.',
                           'ja': 'フラッシュカードのおかげで、<ruby>新<rt>あたら</rt></ruby>しい<ruby>単語<rt>たんご</rt></ruby>がすぐ<ruby>覚<rt>おぼ</rt></ruby>えられる。',
                           'ko': '단어 카드 덕분에 새로운 단어를 금방 외울 수 있다.',
                           'zh_CN': '多亏字卡，能很快记住新单词。',
                           'zh_HK': '多得flashcard，好快就記到新單字。',
                           'zh_TW': '多虧字卡，能很快記住新單詞。'}},
 'card_1051': {'example': {'en': 'Relaxing at the resort, you can completely forget your fatigue.',
                           'fr': 'En se relaxant au centre de villégiature, on peut complètement oublier sa fatigue.',
                           'ja': 'リゾートでゆっくり<ruby>過<rt>す</rt></ruby>ごして、<ruby>疲<rt>つか</rt></ruby>れをすっかり<ruby>忘<rt>わす</rt></ruby>れられる。',
                           'ko': '리조트에서 느긋하게 지내며 피로를 말끔히 잊을 수 있다.',
                           'zh_CN': '在度假胜地悠闲度过，能把疲劳完全忘掉。',
                           'zh_HK': '喺度假勝地好好休息，可以忘記晒所有疲勞。',
                           'zh_TW': '在度假勝地悠閒度過，能把疲勞完全忘掉。'}},
 'card_1052': {'example': {'en': 'If you make a checklist, you can eliminate mistakes.',
                           'fr': 'En créant une liste de vérification, on peut éliminer les erreurs.',
                           'ja': 'チェックリストを<ruby>作<rt>つく</rt></ruby>れば、ミスを<ruby>失<rt>な</rt></ruby>くせる。',
                           'ko': '체크리스트를 만들면 실수를 없앨 수 있다.',
                           'zh_CN': '制作核对清单的话，就能消除失误。',
                           'zh_HK': '整返張checklist，就可以減少出錯。',
                           'zh_TW': '製作核對清單的話，就能消除失誤。'}},
 'card_1053': {'example': {'en': 'Here, you can pay not only with a credit card but also with smartphone payment.',
                           'fr': 'Ici, on peut payer non seulement par carte de crédit, mais aussi par paiement '
                                 'mobile.',
                           'ja': 'ここならクレジットカードだけでなく、スマホ<ruby>決済<rt>けっさい</rt></ruby>でも<ruby>払<rt>はら</rt></ruby>える。',
                           'ko': '여기서는 신용카드뿐만 아니라 스마트폰 결제로도 결제할 수 있다.',
                           'zh_CN': '在这里不仅能用信用卡，还能用移动支付付款。',
                           'zh_HK': '喺呢度除咗可以用信用卡，仲可以用手機支付俾錢。',
                           'zh_TW': '在這裡不僅能用信用卡，還能用行動支付付款。'}},
 'card_1054': {'example': {'en': 'With the library book drop, you can return books anytime 24 hours a day.',
                           'fr': 'Avec la boîte de retour de la bibliothèque, on peut rendre les livres à toute heure '
                                 '24h/24.',
                           'ja': '<ruby>図書館<rt>としょかん</rt></ruby>のポストなら、24<ruby>時間<rt>じかん</rt></ruby>いつでも<ruby>本<rt>ほん</rt></ruby>を<ruby>返<rt>かえ</rt></ruby>せる。',
                           'ko': '도서관 반납함이라면 24시간 언제라도 책을 반납할 수 있다.',
                           'zh_CN': '如果是图书馆的还书箱，24小时随时都能还书。',
                           'zh_HK': '用圖書館個還書箱嘅話，24小時幾時都可以還書。',
                           'zh_TW': '如果是圖書館的還書箱，24小時隨時都能還書。'}},
 'card_1055': {'example': {'en': 'If you have strong willpower, you can stop eating too many sweets too.',
                           'fr': 'Avec une forte volonté, on peut aussi arrêter de manger trop de sucreries.',
                           'ja': '<ruby>強<rt>つよ</rt></ruby>い<ruby>意志<rt>いし</rt></ruby>があれば、<ruby>甘<rt>あま</rt></ruby>いものの<ruby>食<rt>た</rt></ruby>べすぎも<ruby>辞<rt>や</rt></ruby>められる。',
                           'ko': '강한 의지만 있다면 단것을 과식하는 것도 그만둘 수 있다.',
                           'zh_CN': '只要有坚强的意志，连吃太多甜食的习惯也能戒掉。',
                           'zh_HK': '只要有堅定嘅意志，食太甜嘅習慣都可以戒得到。',
                           'zh_TW': '只要有堅強的意志，連吃太多甜食的習慣也能戒掉。'}},
 'card_1056': {'example': {'en': 'Using the Internet, you can look up anything right away.',
                           'fr': "En utilisant Internet, on peut chercher n'importe quoi tout de suite.",
                           'ja': 'インターネットを<ruby>使<rt>つか</rt></ruby>えば、<ruby>何<rt>なん</rt></ruby>でもすぐに<ruby>調<rt>しら</rt></ruby>べられる。',
                           'ko': '인터넷을 이용하면 무엇이든 바로 찾아볼 수 있다.',
                           'zh_CN': '使用网络的话，什么都可以马上查到。',
                           'zh_HK': '用上網嘅話，咩都可以即刻查得到。',
                           'zh_TW': '使用網路的話，什麼都可以馬上查到。'}},
 'card_1057': {'example': {'en': 'If you ask a specialized shop, this computer can be repaired.',
                           'fr': 'Si vous vous adressez à un magasin spécialisé, cet ordinateur peut être réparé.',
                           'ja': '<ruby>専門<rt>せんもん</rt></ruby>の<ruby>店<rt>みせ</rt></ruby>に<ruby>頼<rt>たの</rt></ruby>めば、このパソコンは<ruby>修理<rt>しゅうり</rt></ruby>できる。',
                           'ko': '전문 매장에 맡기면 이 컴퓨터는 수리할 수 있다.',
                           'zh_CN': '委托专门店的话，这台电脑可以修好。',
                           'zh_HK': '攞去專門舖頭整嘅話，呢部電腦可以整得返好。',
                           'zh_TW': '委託專門店的話，這台電腦可以修好。'}},
 'card_1058': {'example': {'en': 'With the app, you can contact your family at any time.',
                           'fr': "Grâce à l'application, on peut contacter sa famille à tout moment.",
                           'ja': 'アプリで、いつでも<ruby>家族<rt>かぞく</rt></ruby>に<ruby>連絡<rt>れんらく</rt></ruby>できる。',
                           'ko': '앱으로 언제든지 가족에게 연락할 수 있다.',
                           'zh_CN': '用应用程序随时都能联系家人。',
                           'zh_HK': '用App隨時都可以聯絡到屋企人。',
                           'zh_TW': '用應用程式隨時都能聯繫家人。'}},
 'card_1059': {'example': {'en': 'This hotel has hot springs, and you can stay very comfortably.',
                           'fr': 'Cet hôtel dispose de sources chaudes, on peut y séjourner très confortablement.',
                           'ja': 'このホテルは<ruby>温泉<rt>おんせん</rt></ruby>があり、とても<ruby>快適<rt>かいてき</rt></ruby>に<ruby>泊<rt>と</rt></ruby>まれる。',
                           'ko': '이 호텔은 온천이 있어서 매우 쾌적하게 묵을 수 있다.',
                           'zh_CN': '这家饭店有温泉，能住得非常舒服。',
                           'zh_HK': '呢間酒店有溫泉，住得好舒服。',
                           'zh_TW': '這家飯店有溫泉，能住得非常舒服。'}},
 'card_1060': {'example': {'en': 'With a robot vacuum cleaner, you can clean even while away from home.',
                           'fr': 'Avec un robot aspirateur, on peut nettoyer même en étant absent.',
                           'ja': 'ロボット<ruby>掃除機<rt>そうじき</rt></ruby>で、<ruby>留守<rt>るす</rt></ruby>の<ruby>間<rt>あいだ</rt></ruby>にも<ruby>掃除<rt>そうじ</rt></ruby>できる。',
                           'ko': '로봇 청소기로 외출 중에도 청소할 수 있다.',
                           'zh_CN': '用扫地机器人，外出不在家时也能打扫。',
                           'zh_HK': '用掃地機械人，出咗去不在家嗰陣都打掃得到。',
                           'zh_TW': '用掃地機器人，外出不在家時也能打掃。'}},
 'card_1061': {'example': {'en': 'This sweater can be washed even in a home washing machine.',
                           'fr': 'Ce pull peut être lavé même dans la machine à laver familiale.',
                           'ja': 'このセーターは<ruby>自宅<rt>じたく</rt></ruby>の<ruby>洗濯機<rt>せんたくき</rt></ruby>でも<ruby>洗濯<rt>せんたく</rt></ruby>できる。',
                           'ko': '이 스웨터는 집 세탁기로도 세탁할 수 있다.',
                           'zh_CN': '这件毛衣在家里的洗衣机里也能清洗。',
                           'zh_HK': '呢件毛衣用屋企部洗衣機都洗得。',
                           'zh_TW': '這件毛衣在家裡的洗衣機裡也能清洗。'}},
 'card_1063': {'example': {'en': 'Because I memorized the lyrics, I can sing Japanese anime songs.',
                           'fr': "Comme j'ai appris les paroles, je peux chanter des chansons d'anime en japonais.",
                           'ja': '<ruby>歌詞<rt>かし</rt></ruby>を<ruby>覚<rt>おぼ</rt></ruby>えたので、<ruby>日本語<rt>にほんご</rt></ruby>のアニメソングが<ruby>歌<rt>うた</rt></ruby>える。',
                           'ko': '가사를 외웠기 때문에 일본 애니메이션 노래를 부를 수 있다.',
                           'zh_CN': '因为记住了歌词，能唱日语动漫歌曲了。',
                           'zh_HK': '背熟咗歌詞，所以唱到日文動漫歌喇。',
                           'zh_TW': '因為記住了歌詞，能唱日語動漫歌曲了。'}},
 'card_1065': {'example': {'en': 'If you tear off the label, you can throw plastic bottles away at the recycling '
                                 'station.',
                           'fr': "Si vous retirez l'étiquette, vous pouvez jeter les bouteilles en plastique au point "
                                 'de recyclage.',
                           'ja': 'ペットボトルはラベルをはがせば、リサイクルステーションに<ruby>捨<rt>す</rt></ruby>てられる。',
                           'ko': '페트병은 라벨을 떼어내면 재활용 수거함에 버릴 수 있다.',
                           'zh_CN': '塑料瓶只要撕掉标签，就能扔到回收站。',
                           'zh_HK': '膠樽撕咗張包裝紙，就可以拎去回收站抌。',
                           'zh_TW': '寶特瓶只要撕掉標籤，就能扔到回收站。'}},
 'card_1066': {'example': {'en': 'Online, you can easily change the hotel reservation dates.',
                           'fr': "En ligne, on peut facilement modifier les dates de réservation d'hôtel.",
                           'ja': 'ネットからなら、ホテルの<ruby>予約<rt>よやく</rt></ruby><ruby>日程<rt>にってい</rt></ruby>を<ruby>簡単<rt>かんたん</rt></ruby>に<ruby>変<rt>か</rt></ruby>えられる。',
                           'ko': '온라인에서는 호텔 예약 일정을 쉽게 변경할 수 있다.',
                           'zh_CN': '在网上可以轻松更改饭店的预约日期。',
                           'zh_HK': '喺網上可以好容易改到酒店嘅訂房日子。',
                           'zh_TW': '在網上可以輕鬆更改飯店的預約日期。'}},
 'card_1068': {'example': {'en': 'Because I got my license, I can drive a rental car.',
                           'fr': "Comme j'ai obtenu mon permis, je peux conduire une voiture de location.",
                           'ja': '<ruby>免許<rt>めんきょ</rt></ruby>を<ruby>取<rt>と</rt></ruby>ったので、レンタカーを<ruby>運転<rt>うんてん</rt></ruby>できる。',
                           'ko': '면허를 땄기 때문에 렌터카를 운전할 수 있다.',
                           'zh_CN': '因为拿到了驾照，所以能开租来的车了。',
                           'zh_HK': '考到車牌之後，就可以揸租返嚟嘅車喇。',
                           'zh_TW': '因為拿到了駕照，所以能開租來的車了。'}},
 'card_1069': {'example': {'en': 'If you study hard, you will surely be able to obtain the JLPT qualification.',
                           'fr': 'En étudiant sérieusement, on peut certainement obtenir le diplôme du JLPT.',
                           'ja': 'しっかり<ruby>勉強<rt>べんきょう</rt></ruby>すれば、JLPTの<ruby>資格<rt>しかく</rt></ruby>がきっと<ruby>取<rt>と</rt></ruby>れる。',
                           'ko': '열심히 공부하면 JLPT 자격을 분명히 취득할 수 있다.',
                           'zh_CN': '好好学习的话，一定能考取JLPT资格证书。',
                           'zh_HK': '畀心機溫書嘅話，一定考到JLPT證書。',
                           'zh_TW': '好好學習的話，一定能考取JLPT資格證書。'}},
 'card_1071': {'example': {'en': 'If you know in advance, you can watch your step.',
                           'fr': "Si on le sait à l'avance, on peut faire attention où l'on met les pieds.",
                           'ja': 'あらかじめ<ruby>知<rt>し</rt></ruby>っていれば、<ruby>足元<rt>あしもと</rt></ruby>に<ruby>気<rt>き</rt></ruby>を<ruby>付<rt>つ</rt></ruby>けられる。',
                           'ko': '미리 알고 있다면 발밑을 조심할 수 있다.',
                           'zh_CN': '如果事先知道的话，就能注意脚下了。',
                           'zh_HK': '如果一早知嘅話，就可以留意腳下安全。',
                           'zh_TW': '如果事先知道的話，就能注意腳下了。'}},
 'card_1072': {'example': {'en': 'Because the scholarship was decided, I can study abroad in Japan from next year!',
                           'fr': "Comme la bourse est confirmée, je peux partir étudier au Japon dès l'année prochaine "
                                 '!',
                           'ja': '<ruby>奨学金<rt>しょうがくきん</rt></ruby>が<ruby>決<rt>き</rt></ruby>まったので、<ruby>来年<rt>らいねん</rt></ruby>から<ruby>日本<rt>にほん</rt></ruby>へ<ruby>留学<rt>りゅうがく</rt></ruby>できる！',
                           'ko': '장학금이 결정되어 내년부터 일본으로 유학 갈 수 있다!',
                           'zh_CN': '奖学金定下来了，明年开始就能去日本留学了！',
                           'zh_HK': '攞到獎學金，出年開始就可以去日本留學喇！',
                           'zh_TW': '獎學金定下來了，明年開始就能去日本留學了！'}},
 'card_1074': {'example': {'en': 'With a folding umbrella, you can put it in your bag and take it anywhere anytime.',
                           'fr': "Avec un parapluie pliable, on peut le mettre dans son sac et l'emmener n'importe "
                                 'quand.',
                           'ja': '<ruby>折<rt>お</rt></ruby>りたたみ<ruby>傘<rt>かさ</rt></ruby>なら、カバンに<ruby>入<rt>い</rt></ruby>れていつでも<ruby>持<rt>も</rt></ruby>って<ruby>行<rt>い</rt></ruby>ける。',
                           'ko': '접이식 우산이라면 가방에 넣어서 언제든 가지고 갈 수 있다.',
                           'zh_CN': '如果是折叠伞的话，放进包里随时都能带去。',
                           'zh_HK': '縮骨遮嘅話，擺入個袋度幾時都可以帶去。',
                           'zh_TW': '如果是折疊傘的話，放進包裡隨時都能帶去。'}},
 'card_1075': {'example': {'en': "You can bring your favorite notebook to tomorrow's lesson.",
                           'fr': 'Vous pouvez apporter votre carnet préféré au cours de demain.',
                           'ja': '<ruby>明日<rt>あした</rt></ruby>のレッスンに、お<ruby>気<rt>き</rt></ruby>に<ruby>入<rt>い</rt></ruby>りのノートを<ruby>持<rt>も</rt></ruby>って<ruby>来<rt>こ</rt></ruby>られる。',
                           'ko': '내일 수업에 마음에 드는 공책을 가져올 수 있다.',
                           'zh_CN': '可以把喜欢的笔记本带到明天的课堂来。',
                           'zh_HK': '聽日上堂可以帶自己鍾意本notebook嚟。',
                           'zh_TW': '可以把喜歡的筆記本帶到明天的課堂來。'}},
 'card_1076': {'example': {'en': 'On the terrace seats, you can take your pet dog too.',
                           'fr': 'En terrasse, vous pouvez aussi emmener votre chien.',
                           'ja': 'テラス<ruby>席<rt>せき</rt></ruby>なら、ペットの<ruby>犬<rt>いぬ</rt></ruby>も<ruby>連<rt>つ</rt></ruby>れて<ruby>行<rt>い</rt></ruby>ける。',
                           'ko': '테라스 좌석이라면 반려견도 데리고 갈 수 있다.',
                           'zh_CN': '露天座位的话，也能带宠物狗去。',
                           'zh_HK': '坐露天位嘅話，都可以帶埋隻狗去。',
                           'zh_TW': '露天座位的話，也能帶寵物狗去。'}},
 'card_1077': {'example': {'en': 'You can bring your friends along to the weekend party too.',
                           'fr': 'Vous pouvez aussi amener vos amis à la fête du week-end.',
                           'ja': '<ruby>週末<rt>しゅうまつ</rt></ruby>のパーティーに、お<ruby>友達<rt>ともだち</rt></ruby>も<ruby>連<rt>つ</rt></ruby>れて<ruby>来<rt>こ</rt></ruby>られる。',
                           'ko': '주말 파티에 친구도 데려올 수 있다.',
                           'zh_CN': '周末的派对上，也可以把朋友一起带过来。',
                           'zh_HK': '週末個party，都可以帶埋朋友一齊嚟。',
                           'zh_TW': '週末的派對上，也可以把朋友一起帶過來。'}}}
REVISIONS.update(ADDITIONAL_ENTRIES)
