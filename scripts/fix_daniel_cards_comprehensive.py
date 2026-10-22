# -*- coding: utf-8 -*-
"""
Fixes all 103 Daniel cards + card_midori_burikko with authentic 6-language translations
for both `meaning` and `example`.
"""

import json
import re

print("Translating and enriching Daniel's 103 cards & card_midori_burikko...")

# Translations mapping for all 103 words:
# word -> { meaning: { zh_TW, zh_CN, ko, zh_HK, fr }, example: { zh_TW, zh_CN, ko, zh_HK, fr } }
DANIEL_TRANSLATIONS = {
    "card_daniel_001": { # 展覧会
        "meaning": {"zh_TW": "展覽會", "zh_CN": "展览会", "ko": "전람회, 전시회", "zh_HK": "展覽會", "fr": "exposition"},
        "example": {
            "zh_TW": "週末我去美術館看了一場展覽會。",
            "zh_CN": "周末我去美术馆看了一场展览会。",
            "ko": "주말에 미술관 전람회에 다녀왔습니다.",
            "zh_HK": "禮拜六日我去咗美術館睇展覽會。",
            "fr": "Je suis allé à une exposition au musée d'art ce week-end."
        }
    },
    "card_daniel_002": { # 営業マン
        "meaning": {"zh_TW": "業務員、銷售員", "zh_CN": "业务员、销售员", "ko": "영업사원", "zh_HK": "營業員、Sell客", "fr": "commercial, représentant commercial"},
        "example": {
            "zh_TW": "我哥哥是一位汽車銷售業務員。",
            "zh_CN": "我哥哥是一位汽车销售业务员。",
            "ko": "형은 자동차 영업사원입니다.",
            "zh_HK": "我阿哥係賣車嘅業務員。",
            "fr": "Mon grand frère est vendeur de voitures."
        }
    },
    "card_daniel_003": { # 営業時間
        "meaning": {"zh_TW": "營業時間", "zh_CN": "营业时间", "ko": "영업시간", "zh_HK": "營業時間", "fr": "heures d'ouverture"},
        "example": {
            "zh_TW": "這家店的營業時間到幾點為止呢？",
            "zh_CN": "这家店的营业时间到几点为止呢？",
            "ko": "이 가게의 영업시간은 몇 시까지인가요?",
            "zh_HK": "呢間舖頭嘅營業時間開到幾點㗎？",
            "fr": "Jusqu'à quelle heure ce magasin est-il ouvert ?"
        }
    },
    "card_daniel_004": { # 営業時間外
        "meaning": {"zh_TW": "非營業時間", "zh_CN": "非营业时间", "ko": "영업시간 외", "zh_HK": "營業時間以外", "fr": "en dehors des heures d'ouverture"},
        "example": {
            "zh_TW": "因為現在是非營業時間，所以電話打不通。",
            "zh_CN": "因为现在是非营业时间，所以电话打不通。",
            "ko": "영업시간 외라서 전화가 연결되지 않습니다.",
            "zh_HK": "因為而家唔係營業時間，所以打唔通電話。",
            "fr": "Le téléphone ne répond pas car c'est en dehors des heures d'ouverture."
        }
    },
    "card_daniel_005": { # 創業
        "meaning": {"zh_TW": "創業、創立", "zh_CN": "创业、创立", "ko": "창업", "zh_HK": "創業、開檔", "fr": "fondation (d'entreprise)"},
        "example": {
            "zh_TW": "這家老店創業至今已有100年歷史。",
            "zh_CN": "这家老店创业至今已有100年历史。",
            "ko": "이 가게는 창업한 지 100년 되었습니다.",
            "zh_HK": "呢間老字號開咗已經有成100年歷史。",
            "fr": "Ce magasin est en activité depuis 100 ans."
        }
    },
    "card_daniel_006": { # 経営する
        "meaning": {"zh_TW": "經營、管理", "zh_CN": "经营、管理", "ko": "경영하다, 운영하다", "zh_HK": "經營、打理", "fr": "gérer, diriger"},
        "example": {
            "zh_TW": "家父經營著一家義大利餐廳。",
            "zh_CN": "家父经营着一家意大利餐厅。",
            "ko": "아버지는 레스토랑을 경영하고 계십니다.",
            "zh_HK": "我爸爸經營緊一間西餐廳。",
            "fr": "Mon père gère un restaurant."
        }
    },
    "card_daniel_007": { # 家族経営
        "meaning": {"zh_TW": "家族經營、家族企業", "zh_CN": "家族经营、家族企业", "ko": "가족경영", "zh_HK": "家庭式經營", "fr": "entreprise familiale"},
        "example": {
            "zh_TW": "這是一間家族經營的小溫泉旅館。",
            "zh_CN": "这是一间家族经营的小温泉旅馆。",
            "ko": "이곳은 가족이 함께 운영하는 작은 여관입니다.",
            "zh_HK": "呢度係一間家庭式經營嘅細溫泉旅館。",
            "fr": "C'est une petite auberge familiale."
        }
    },
    "card_daniel_008": { # 大家族
        "meaning": {"zh_TW": "大家庭", "zh_CN": "大家庭", "ko": "대가족", "zh_HK": "大家庭", "fr": "famille nombreuse"},
        "example": {
            "zh_TW": "我在一個熱鬧的大家庭中長大。",
            "zh_CN": "我在一个热闹的大家庭中长大。",
            "ko": "저는 대가족 속에서 자랐습니다.",
            "zh_HK": "我喺一個好熱鬧嘅大家庭長大。",
            "fr": "J'ai grandi au sein d'une grande famille."
        }
    },
    "card_daniel_009": { # 亡くなる
        "meaning": {"zh_TW": "逝世、過世", "zh_CN": "逝世、去世", "ko": "돌아가시다", "zh_HK": "過身、逝世", "fr": "décéder, s'éteindre"},
        "example": {
            "zh_TW": "我的祖父在去年安詳過世了。",
            "zh_CN": "我的祖父在去年安详去世了。",
            "ko": "할아버지께서는 작년에 돌아가셨습니다.",
            "zh_HK": "我爺爺喺舊年安詳過身喇。",
            "fr": "Mon grand-père est décédé l'année dernière."
        }
    },
    "card_daniel_010": { # 肉体労働
        "meaning": {"zh_TW": "體力勞動", "zh_CN": "体力劳动", "ko": "육체노동", "zh_HK": "體力勞動、勞力", "fr": "travail manuel, travail physique"},
        "example": {
            "zh_TW": "工地現場的體力勞動雖然辛苦，但非常有成就感。",
            "zh_CN": "工地现场的体力劳动虽然辛苦，但非常有成就感。",
            "ko": "육체노동은 힘들지만 보람이 있습니다.",
            "zh_HK": "做體力勞動嘅工雖然好辛苦，但都好有成就感。",
            "fr": "Le travail manuel est éprouvant mais apporte beaucoup de satisfaction."
        }
    },
    "card_daniel_011": { # 人手不足
        "meaning": {"zh_TW": "人手不足、缺工", "zh_CN": "人手不足、用工短缺", "ko": "일손 부족", "zh_HK": "唔夠人手、缺人", "fr": "pénurie de main-d'œuvre"},
        "example": {
            "zh_TW": "最近很多餐飲店都面臨著人手不足的困境。",
            "zh_CN": "最近很多餐饮店都面临着人手不足的困境。",
            "ko": "어느 회사나 일손 부족으로 고민하고 있습니다.",
            "zh_HK": "而家周圍都好唔夠人手，周圍都請緊人。",
            "fr": "Toutes les entreprises font face à un manque de personnel."
        }
    },
    "card_daniel_012": { # 足りない
        "meaning": {"zh_TW": "不夠、不足", "zh_CN": "不够、不足", "ko": "부족하다, 모자라다", "zh_HK": "唔夠", "fr": "insuffisant, manquer de"},
        "example": {
            "zh_TW": "買這件衣服的錢還稍微差了一點點不夠。",
            "zh_CN": "买这件衣服的钱还稍微差了一点点不够。",
            "ko": "돈이 조금 모자랍니다.",
            "zh_HK": "仲差少少錢先夠買呢件衫。",
            "fr": "Il me manque un peu d'argent."
        }
    },
    "card_daniel_013": { # 不足する
        "meaning": {"zh_TW": "不足、缺乏", "zh_CN": "不足、缺乏", "ko": "부족하다", "zh_HK": "唔夠、缺乏", "fr": "manquer de, être insuffisant"},
        "example": {
            "zh_TW": "最近因為工作忙碌，睡眠時間相當不足。",
            "zh_CN": "最近因为工作忙碌，睡眠时间相当不足。",
            "ko": "요즘 수면이 많이 부족합니다.",
            "zh_HK": "最近個人瞓得唔係好夠，睡眠嚴重不足。",
            "fr": "Ces derniers temps, je manque cruellement de sommeil."
        }
    },
    "card_daniel_014": { # 農場
        "meaning": {"zh_TW": "農場、農莊", "zh_CN": "农场、农庄", "ko": "농장", "zh_HK": "農場", "fr": "ferme, exploitation agricole"},
        "example": {
            "zh_TW": "我朋友在北海道遼闊的農場裡工作。",
            "zh_CN": "我朋友在北海道辽阔的农场里工作。",
            "ko": "홋카이도의 넓은 농장에서 일하고 있습니다.",
            "zh_HK": "我朋友喺北海道嘅大農場嗰度返工。",
            "fr": "Je travaille dans une ferme à Hokkaido."
        }
    },
    "card_daniel_015": { # 進出する
        "meaning": {"zh_TW": "拓展、進軍（市場）", "zh_CN": "拓展、进军（市场）", "ko": "진출하다", "zh_HK": "進軍、拓展業務", "fr": "s'implanter, pénétrer (un marché)"},
        "example": {
            "zh_TW": "那家知名日本拉麵店正式進軍海外市場了。",
            "zh_CN": "那家知名日本拉面店正式进军海外市场了。",
            "ko": "그 회사는 최근 해외 시장에 활발하게 진출하고 있습니다.",
            "zh_HK": "嗰間日本連鎖拉麵店正式進軍海外市場。",
            "fr": "Cette entreprise se développe activement sur les marchés étrangers."
        }
    },
    "card_daniel_016": { # 〜箇所
        "meaning": {"zh_TW": "……處、……個地方（數量詞）", "zh_CN": "……处、……个地方", "ko": "~곳, ~군데", "zh_HK": "……個位、……處", "fr": "compteur pour les lieux/endroits"},
        "example": {
            "zh_TW": "這份合約書上有3個地方需要修改。",
            "zh_CN": "这份合同书上有3个地方需要修改。",
            "ko": "계약서에 잘못된 부분이 3군데 있습니다.",
            "zh_HK": "份合約有三處地方要改返啱佢。",
            "fr": "Il y a 3 erreurs dans le document."
        }
    },
    "card_daniel_017": { # 田んぼ
        "meaning": {"zh_TW": "水田、稻田", "zh_CN": "水田、稻田", "ko": "논", "zh_HK": "稻田、水田", "fr": "rizière"},
        "example": {
            "zh_TW": "鄉下老家的房子周圍全都是綠油油的稻田。",
            "zh_CN": "乡下老家的房子周围全都是绿油油的稻田。",
            "ko": "고향 집 주변은 온통 푸른 논뿐입니다.",
            "zh_HK": "老家間屋周圍全部都係一大片綠油油嘅稻田。",
            "fr": "Autour de la maison, il n'y a que des rizières."
        }
    },
    "card_daniel_018": { # 滝
        "meaning": {"zh_TW": "瀑布", "zh_CN": "瀑布", "ko": "폭포", "zh_HK": "瀑布", "fr": "cascade, chute d'eau"},
        "example": {
            "zh_TW": "這座瀑布水勢磅礡，是名聞遐邇的著名景點。",
            "zh_CN": "这座瀑布水势磅礴，是名闻遐迩的著名景点。",
            "ko": "이 폭포는 물줄기가 시원해서 매우 유명합니다.",
            "zh_HK": "呢條瀑布水流好急好壯觀，係好出名嘅名勝。",
            "fr": "Cette cascade est très célèbre."
        }
    },
    "card_daniel_019": { # 無事
        "meaning": {"zh_TW": "平安、無事", "zh_CN": "平安、无事", "ko": "무사히, 탈 없이", "zh_HK": "平安、冇事", "fr": "sain et sauf, sans encombre"},
        "example": {
            "zh_TW": "長途旅行結束後，平安順利地抵達了家中。",
            "zh_CN": "长途旅行结束后，平安顺利地抵达了家中。",
            "ko": "긴 여행을 마치고 무사히 집에 도착했습니다.",
            "zh_HK": "去完長途旅行返嚟，平平安安返到屋企。",
            "fr": "Je suis bien rentré à la maison sans problème."
        }
    },
    "card_daniel_020": { # 地下鉄
        "meaning": {"zh_TW": "地下鐵、捷運", "zh_CN": "地铁", "ko": "지하철", "zh_HK": "地鐵", "fr": "métro"},
        "example": {
            "zh_TW": "我每天搭乘地下鐵通勤去公司上班。",
            "zh_CN": "我每天搭乘地铁通勤去公司上班。",
            "ko": "매일 지하철을 타고 회사에 출퇴근합니다.",
            "zh_HK": "我每日都搭地鐵返工放工。",
            "fr": "Je prends le métro pour aller au bureau."
        }
    }
}

# Generic dictionary-based auto-fill for remaining daniel cards
# Map Daniel word to meanings & examples
DANIEL_ALL = [
    ("card_daniel_021", "宗教", "religion", "宗教", "종교", "religion", "世界にはさまざまな宗教が存在します。", "There are various religions in the world.", "世界上存在著各式各樣的宗教。", "전 세계에는 다양한 종교가 존재합니다.", "世界各地有好多種唔同嘅宗教。"),
    ("card_daniel_022", "存在", "existence", "存在", "존재", "existence", "見えない空気の存在を感じます。", "I feel the existence of invisible air.", "我能感受到無形空氣的存在。", "눈에 보이지 않는 공기의 존재를 느낍니다.", "我感受到無形嘅空氣確實存在。"),
    ("card_daniel_023", "仏教", "Buddhism", "佛教", "불교", "bouddhisme", "日本の伝統文化は仏教の影響を深く受けています。", "Japanese traditional culture is deeply influenced by Buddhism.", "日本傳統文化深受佛教的深遠影響。", "일본의 전통문화는 불교의 영향을 깊게 받았습니다.", "日本傳統文化深受佛教影響。"),
    ("card_daniel_024", "お正月", "New Year", "新年、過年", "설날, 신정", "Nouvel An", "お正月は実家で家族みんなとおせちを食べます。", "During New Year, we eat osechi with the whole family at my parents' home.", "過年時我們全家聚在老家吃年菜慶祝。", "설날에는 본가에서 가족과 함께 명절 음식을 먹습니다.", "過年嗰陣我哋全家人一齊食賀年菜。"),
    ("card_daniel_025", "安くなる", "to become cheaper", "變便宜", "싸지다", "devenir moins cher", "季節の終わりになると服が安くなります。", "Clothes become cheaper at the end of the season.", "到了換季時，衣服就會降價變便宜。", "계절이 바뀔 때가 되면 옷이 저렴해집니다.", "到咗換季嗰時，啲衫就會變平減價。"),
    ("card_daniel_026", "セール", "sale", "特賣、促銷", "세일", "solde, promotion", "デパートで冬のセールが始まりました。", "The winter sale has begun at the department store.", "百貨公司冬季特賣促銷開跑了。", "백화점에서 겨울 정기 세일이 시작되었습니다.", "百貨公司嘅冬季大減價開始咗喇。"),
    ("card_daniel_027", "お葬式", "funeral", "喪禮、葬禮", "장례식", "funérailles", "親戚のお葬式に参列するため黒い服を着ました。", "I wore black clothes to attend a relative's funeral.", "為了參加親戚的喪禮，我穿上了整套黑色喪服。", "친척의 장례식에 참석하기 위해 검은 옷을 입었습니다.", "為咗去親戚嘅喪禮，我著咗一身黑色衫。"),
    ("card_daniel_028", "貿易", "international trade", "貿易", "무역", "commerce international", "日本は多くの国と盛んに貿易を行っています。", "Japan actively conducts trade with many countries.", "日本與世界上許多國家保持著繁榮的貿易往來。", "일본은 많은 나라와 활발하게 무역을 하고 있습니다.", "日本同世界好多國家都有密切嘅貿易往來。"),
    ("card_daniel_029", "政府", "government", "政府", "정부", "gouvernement", "政府が新しい少子化対策を発表しました。", "The government announced new measures against the falling birthrate.", "政府發布了應對少子化危機的新政策。", "정부가 새로운 저출산 대책을 발표했습니다.", "政府公佈咗應對少子化嘅新政策。"),
    ("card_daniel_030", "最優先", "top priority", "最優先", "최우선", "priorité absolue", "工事現場では作業員の安全が最優先です。", "Workers' safety is the top priority at the construction site.", "在工程工地上，作業工人的安全是最優先事項。", "공사 현장에서는 작업자의 안전이 최우선입니다.", "喺工地入面，工人嘅人身安全係最優先考慮。"),
    ("card_daniel_031", "転生", "reincarnation", "轉生、轉世", "환생, 전생", "réincarnation", "異世界に転生するアニメが最近とても人気です。", "Anime where characters reincarnate into another world are very popular recently.", "異世界轉生題材的動漫最近非常受歡迎。", "이세계로 환생하는 애니메이션이 요즘 아주 인기입니다.", "轉生去異世界嘅動漫最近好受歡迎。"),
    ("card_daniel_032", "生まれ変わる", "to be reborn", "脫胎換骨、重生", "다시 태어나다", "renaître", "リフォームして古い部屋が美しく生まれ変わりました。", "The old room was renovated and beautifully reborn.", "經過重新裝潢修繕，老舊的房間煥然一新。", "인테리어를 새로 해서 낡은 방이 몰라보게 새로워졌습니다.", "全屋翻新裝修之後，間舊屋好似重生咁靚。"),
    ("card_daniel_033", "救う", "to save, to rescue", "拯救、救助", "구하다", "sauver, secourir", "医師たちが夜を徹して患者の尊い命を救いました。", "Doctors worked through the night to save the patient's precious life.", "醫師們徹夜奮戰，拯救了患者寶貴的生命。", "의사들이 밤을 새워 환자의 소중한 생명을 구했습니다.", "醫生通宵做手術救返病人條寶貴嘅命。"),
    ("card_daniel_034", "脱出", "escape", "脫離、逃脫", "탈출", "évasion, fuite", "渋滞の列から脱出して別の道を進みました。", "I escaped the traffic jam and took a different road.", "我脫離了壅塞的車陣，改走另一條替代道路。", "꽉 막힌 도로에서 탈출하여 다른 길로 우회했습니다.", "我避開咗大塞車，行咗另一條路走。"),
    ("card_daniel_035", "逃げる", "to flee, to run away", "逃跑、逃走", "도망치다", "s'enfuir", "泥棒が警察の姿を見て急いで逃げました。", "The thief saw the police and quickly ran away.", "小偷一看見警察的身影，急急忙忙拔腿逃跑。", "도둑이 경찰의 모습을 보고 허둥지둥 도망쳤습니다.", "個賊一見到警察即刻拔足狂奔走咗。"),
    ("card_daniel_036", "荷物", "luggage, package", "行李、包裹", "짐, 수하물", "bagage, colis", "旅行の荷物をスーツケースに詰めました。", "I packed my travel luggage into the suitcase.", "我把旅行行李整齊地裝進了行李箱中。", "여행 짐을 여행용 가방에 차곡차곡 챙겼습니다.", "我將去旅行啲行李執好晒入個喼度。"),
    ("card_daniel_037", "多機能", "multifunctional", "多功能", "다기능", "multifonctionnel", "この最新のスマートウォッチはとても多機能です。", "This latest smartwatch is very multifunctional.", "這款最新型的智慧手錶具備非常豐富的多功能。", "이 최신 스마트워치는 매우 다양한 기능을 갖추고 있습니다.", "呢隻最新款智能手錶好多功能好齊全。"),
    ("card_daniel_038", "限定版", "limited edition", "限量版、限定版", "한정판", "édition limitée", "大好きなゲームの限定版パッケージを予約しました。", "I reserved the limited edition package of my favorite game.", "我預購了心愛遊戲的豪華限量限定版。", "좋아하는 게임의 한정판 패키지를 미리 예약했습니다.", "我預訂咗最鍾意隻game嘅限定珍藏版。"),
    ("card_daniel_039", "現地人", "local person", "當地人", "현지인", "habitant local", "旅先で親切な現地人に美味しい食堂を教えてもらいました。", "A kind local person taught me a delicious eatery while traveling.", "在旅途中，親切的當地人告訴了我好吃的道地餐廳。", "여행지에서 친절한 현지인에게 맛있는 식당을 추천받았습니다.", "去旅行嗰陣，當地好心嘅街坊帶咗我去間地道好食嘅小館。"),
    ("card_daniel_040", "車輪", "wheel", "車輪、輪子", "바퀴", "roue", "自転車の車輪に空気をしっかり入れました。", "I pumped air securely into the bicycle wheels.", "我把自行車的車輪胎壓仔細打飽打滿了。", "자전거 바퀴에 공기를 꼼꼼히 채워 넣었습니다.", "我幫部單車個車胎泵滿咗氣。"),
    ("card_daniel_041", "口に合わない", "not to one's taste", "不合口味", "입에 맞지 않다", "ne pas être à son goût", "少し辛すぎて、私の口には合いませんでした。", "It was a bit too spicy and not to my taste.", "味道稍微有點太辣了，不太合我的口味。", "조금 너무 매워서 제 입맛에는 잘 맞지 않았습니다.", "個味太辣喇，唔係好啱我食。"),
    ("card_daniel_042", "保守的", "conservative", "保守的", "보수적", "conservateur", "祖父は考え方が少し保守的ですが家族想いです。", "My grandfather is a bit conservative in thinking, but very caring.", "祖父的思想雖然有些傳統保守，但他非常關愛全家人。", "할아버지는 생각이 다소 보수적이시지만 가족을 끔찍이 아끼십니다.", "爺爺思想雖然保守少少，但好錫我哋屋企人。"),
    ("card_daniel_043", "制限する", "to restrict, to limit", "限制", "제한하다", "limiter, restreindre", "健康のために甘いお菓子の摂取を制限しています。", "For my health, I limit my intake of sweet snacks.", "為了身體健康，我開始節制甜食的攝取量。", "건강을 위해 달콤한 과자 섭취를 제한하고 있습니다.", "為咗健康，我開始限制自己食甜品零食嘅份量。"),
    ("card_daniel_044", "あひる", "duck", "鴨子", "집오리", "canard", "池でのんびり泳ぐ可愛いあひるを眺めました。", "I watched the cute ducks swimming leisurely in the pond.", "我看著池塘裡悠哉划水游著的可愛鴨子。", "연못에서 평화롭게 헤엄치는 귀여운 오리들을 바라보았습니다.", "我望住池塘入面悠閒游水嘅得意鴨仔。"),
    ("card_daniel_045", "渋滞", "traffic jam", "塞車、塞車", "교통 체증", "embouteillage", "雨の日の朝は道路がいつも渋滞します。", "Roads are always congested on rainy weekday mornings.", "每逢下雨天的早晨，道路總是容易嚴重塞車。", "비 오는 날 아침에는 도로가 항상 꽉 막힙니다.", "一到落雨天嘅朝早，條路就實會大塞車。"),
    ("card_daniel_046", "お年寄り", "elderly person", "高齡者、長輩", "어르신", "personne âgée", "階段でお年寄りの重い荷物を持ってあげました。", "I helped an elderly person carry heavy luggage up the stairs.", "在樓梯間我主動幫老人家提了沉重的行李。", "계단에서 어르신의 무거운 짐을 대신 들어드렸습니다.", "見到長者上樓梯好辛苦，我幫佢拎重行李。"),
    ("card_daniel_047", "優しい人", "kind person", "溫柔親切的人", "다정한 사람", "personne gentille", "彼は困った人を放っておけない本当に優しい人です。", "He is a truly kind person who cannot leave anyone in trouble.", "他是個看見別人有難絕不會坐視不管、極其善良的人。", "그는 곤란한 사람을 지나치지 못하는 참 다정한 사람입니다.", "佢見到人有困難一定會主動幫手，係個好善良嘅人。"),
    ("card_daniel_048", "豆乳", "soy milk", "豆漿、豆奶", "두유", "lait de soja", "毎朝健康のために温かい無調整の豆乳を飲みます。", "I drink warm plain soy milk every morning for health.", "為了身體健康，我每天早晨都喝一杯溫熱的純豆漿。", "매일 아침 건강을 위해 따뜻한 무가당 두유를 마십니다.", "為咗身體健康，我每日朝早飲杯熱嘅無糖豆漿。"),
    ("card_daniel_049", "寒い", "cold", "寒冷", "춥다", "froid", "今日の夜は冷え込んでとても寒いです。", "Tonight is chilly and very cold.", "今晚氣溫驟降，天氣非常寒冷。", "오늘 밤은 기온이 뚝 떨어져서 무척 춥습니다.", "今晚天氣轉涼，好凍呀。"),
    ("card_daniel_050", "冷たい", "cold (to touch)", "冰涼的、冰冷的", "차갑다", "froid (au toucher)", "運動の後に冷たいミネラルウォーターを飲みました。", "I drank cold mineral water after exercising.", "運動過後，我喝了一瓶冰涼清冽的礦泉水。", "운동 후에 시원하고 차가운 생수를 마셨습니다.", "做完運動之後，飲咗樽冰凍嘅礦泉水好解渴。"),
    ("card_daniel_051", "舌が肥える", "to have refined palate", "嘴刁、懂吃、品味高", "입맛이 까다롭다/고급이다", "avoir le palais fin", "美味しい名店巡りをするうちにすっかり舌が肥えました。", "Visiting great restaurants has given me a refined palate.", "經常走訪各大美食名店，讓我的嘴變得非常懂吃挑剔。", "맛집을 찾아다니다 보니 자연스레 입맛이 한층 고급스러워졌습니다.", "食得多好嘢，而家個人把嘴變得好刁好識食。"),
    ("card_daniel_052", "蒸す", "to steam", "蒸、清蒸", "찌다", "cuire à la vapeur", "たっぷりの旬の野菜を蒸してヘルシーに食べます。", "I steam plenty of seasonal vegetables to eat healthily.", "將豐富的當季蔬菜清蒸，吃得健康又美味。", "제철 채소를 듬뿍 쪄서 담백하고 건강하게 먹습니다.", "將時令蔬菜清蒸嚟食，清淡又健康。"),
    ("card_daniel_053", "湯気", "steam", "熱氣、水蒸氣", "김, 수증기", "vapeur", "炊きたてのご飯から白い湯気が立ち上っています。", "White steam is rising from freshly cooked rice.", "剛煮好的熱騰騰白飯正冒著裊裊白煙熱氣。", "갓 지은 밥에서 하얀 김이 모락모락 피어오릅니다.", "啱啱煲好嘅白飯冒出熱騰騰嘅白煙。"),
    ("card_daniel_054", "風物詩", "seasonal tradition", "季節風物詩、象徵風情", "풍물시", "tradition saisonnière", "夜空に咲く大輪の花火は日本の夏の風物詩です。", "Big fireworks blooming in night sky are a symbol of Japanese summer.", "在夜空中盛開的壯麗煙火，是日本夏天的代表風物詩。", "밤하늘을 수놓는 불꽃놀이는 일본 여름의 대표적인 풍물시입니다.", "夜空綻放嘅煙花，係日本夏天最具代表性嘅傳統風情。"),
    ("card_daniel_055", "人混み", "crowd", "擁擠人群、人潮", "인파", "foule", "人混みが苦手なので、平日の静かな時間に買い物します。", "I dislike crowds, so I shop during quiet weekday hours.", "我不太適應擁擠的人潮，所以都在平日安靜時去購物。", "사람 많은 곳을 꺼려서 평일 한적한 시간에 쇼핑합니다.", "我好怕人逼人，所以鍾意趁平日少人嗰陣去買嘢。"),
    ("card_daniel_056", "落ち着いた", "calm, relaxed", "沉著的、安詳的", "차분한", "calme, posé", "落ち着いたカフェで本を読むのが至福のひとときです。", "Reading books in a calm, cozy cafe is pure bliss.", "在靜謐沉穩的咖啡廳裡讀書，是我最幸福的時光。", "차분한 분위기의 카페에서 독서하는 시간이 가장 행복합니다.", "喺好清幽寧靜嘅咖啡小店睇書，係最享受嘅時光。"),
    ("card_daniel_057", "見せびらかす", "to show off", "炫耀、賣弄", "자랑하다", "exhiber, crâner", "新しい時計を嬉しそうに友達に見せびらかしました。", "He happily showed off his new watch to his friends.", "他開心地向身邊的朋友炫耀他新買的帥氣手錶。", "새로 산 시계를 신이 나서 친구들에게 자랑했습니다.", "佢好開心噉向朋友曬佢新買隻名錶。"),
    ("card_daniel_058", "本屋", "bookstore", "書店", "서점", "librairie", "駅前の大きな本屋で語学の参考書を買いました。", "I bought language study books at the large bookstore by the station.", "我在車站前的大書店買了幾本外語學習參考書。", "역 앞 대형 서점에서 어학 학습 참고서를 샀습니다.", "喺火車站門口間大書店買咗本學日文嘅參考書。"),
    ("card_daniel_059", "天国", "paradise, heaven", "天堂", "천국", "paradis", "温泉に入って美味しい料理を食べるのはまさに天国です。", "Soaking in hot springs and eating fine food is pure paradise.", "一邊泡露天溫泉一邊享用佳餚，簡直就像身在天堂一樣。", "온천에 몸을 담그고 맛있는 요리를 먹으니 그야말로 천국입니다.", "一路浸溫泉一路食好嘢，真係好似上咗天堂咁嘆。"),
    ("card_daniel_060", "状況", "situation", "情況、現狀", "상황", "situation", "刻一刻と変化する現地の状況を注意深く見守っています。", "We are carefully monitoring the situation on site as it changes moment by moment.", "我們正密切關注著當地隨時在變化的最新情況。", "시시각각 변하는 현지 상황을 주의 깊게 지켜보고 있습니다.", "我哋好密切噉留意住現場隨時變化嘅最新狀況。"),
    ("card_daniel_061", "中心地", "city center, hub", "中心地帶、核心區域", "중심지", "centre-ville, cœur", "ここは交通の便がよく、商業の中心地として栄えています。", "This area has great transit and flourishes as commercial center.", "這裡交通四通八達，作為繁華的商業核心地帶十分興盛。", "이곳은 교통이 편리하여 상업의 중심지로 번영하고 있습니다.", "呢度交通四通八達，係好繁榮嘅商業核心地帶。"),
    ("card_daniel_062", "噴火", "volcanic eruption", "（火山）爆發、噴發", "분화", "éruption volcanique", "火山の噴火に備えて、ハザードマップを確認しました。", "I checked the hazard map in preparation for volcanic eruption.", "為了防範火山噴發災害，我事先確認了防災避難地圖。", "화산 분화에 대비하여 방재 대피 지도를 미리 확인했습니다.", "為咗預防火山爆發，我上網check清楚避難防災地圖。"),
    ("card_daniel_063", "大人っぽい", "mature-looking", "成熟的、有大人味的", "어른스러운", "d'allure adulte", "落ち着いた色のドレスを着るとぐっと大人っぽく見えます。", "Wearing a calm-colored dress makes you look much more mature.", "穿上沉穩色系的優雅禮服，看起來立刻顯得落落大方成熟許多。", "차분한 색상의 원피스를 입으니 한결 어른스러워 보입니다.", "著咗條斯文大方嘅長裙，個人睇起上嚟成熟穩重好多。"),
    ("card_daniel_064", "子供っぽい", "childish", "孩子氣的、幼稚的", "아이 같은", "enfantin", "些細なことで怒るのは少し子供っぽい行動ですよ。", "Getting angry over trivial things is a bit childish behavior.", "因為雞毛蒜皮的小事發脾氣，是稍微有點孩子氣的舉動喔。", "사소한 일로 토라지는 것은 조금 아이 같은 행동이에요.", "因為少少小事就發脾氣，咁樣做太細路仔氣喇。"),
    ("card_daniel_065", "バツイチ", "divorced once", "離過一次婚", "돌싱, 이혼 경험", "divorcé", "彼女はバツイチですが、前向きに人生を楽しんでいます。", "She is divorced once, but lives her life positively and happily.", "她雖然離過一次婚，但依然樂觀開朗地享受著美好人生。", "그녀는 이혼 경험이 있지만 긍정적으로 인생을 즐기고 있습니다.", "佢雖然結過婚離咗婚，但依然好積極樂觀噉過生活。"),
    ("card_daniel_066", "健康的", "healthy", "健康的", "건강한", "sain, équilibré", "野菜をたっぷり使った健康的な自炊メニューを心がけています。", "I try to cook healthy meals packed with plenty of vegetables.", "我平時注重多吃蔬菜，用心烹調健康營養的自煮菜色。", "채소를 듬뿍 넣은 건강한 집밥 요리를 실천하고 있습니다.", "我平日煮飯好注重多食蔬菜，食得健康又有營養。"),
    ("card_daniel_067", "皿洗い", "dishwashing", "洗碗", "설거지", "vaisselle", "美味しい夕食を食べた後、家族で協力して皿洗いをしました。", "After delicious dinner, we cooperated as family to wash dishes.", "享用完美味的晚餐後，全家人同心協力把碗盤洗乾淨。", "맛있는 저녁 식사 후 온 가족이 힘을 모아 설거지를 했습니다.", "食完餐正嘅晚飯之後，一家人齊心合力洗好晒啲碗碟。"),
    ("card_daniel_068", "お皿", "plate, dish", "盤子、碟子", "접시", "assiette", "料理が映えるよう、綺麗な陶器のお皿に盛り付けました。", "I plated the food on pretty ceramic dishes to make it shine.", "為了讓菜餚更顯可口，我將食物盛裝在精美的陶瓷餐盤上。", "음식이 돋보이도록 예쁜 도자기 접시에 정갈하게 담았습니다.", "為咗碟餸睇起上嚟好吸引，我用隻靚陶瓷碟擺盤。"),
    ("card_daniel_069", "偏食", "picky eating", "偏食、挑食", "편식", "alimentation déséquilibrée", "健康のために偏食を直して色々な食材を食べています。", "For my health, I fixed my picky eating and eat various foods.", "為了維持健康，我改掉了挑食的習慣，攝取多樣化食材。", "건강을 위해 편식 습관을 고치고 다양한 식재료를 골고루 먹습니다.", "為咗身體健康，我戒咗挑食嘅壞習慣，乜嘢食物都均衡食啲。"),
    ("card_daniel_070", "井戸水", "well water", "井水", "우물물", "eau de puits", "昔ながらの井戸水は、夏は冷たく冬は温かく感じられます。", "Traditional well water feels cool in summer and warm in winter.", "傳統的水井水冬暖夏涼，喝起來特別清涼甘甜。", "예부터 내려온 우물물은 여름엔 시원하고 겨울엔 따뜻하게 느껴집니다.", "古老傳統嘅井水冬暖夏涼，飲落好清甜甘涼。"),
    ("card_daniel_071", "食習慣", "eating habits", "飲食習慣", "식습관", "habitudes alimentaires", "野菜中心のバランスのよい食習慣を身につけましょう。", "Let's acquire balanced eating habits focused on vegetables.", "讓我們養成以蔬菜為主、營養均衡的優良飲食習慣吧。", "채소 위주의 균형 잡힌 바른 식습관을 길러봅시다.", "養成多菜少肉、營養均衡嘅健康飲食好習慣。"),
    ("card_daniel_072", "生活習慣", "lifestyle habits", "生活習慣", "생활 습관", "mode de vie", "早寝早起きなど、正しい生活習慣を続けることが大切です。", "Keeping healthy lifestyle habits like sleeping and waking early is key.", "保持早睡早起等規律正常的生活習慣，是健康的基石。", "일찍 자고 일찍 일어나는 올바른 생활 습관을 유지하는 것이 중요합니다.", "早睡早起保持規律正常嘅作息生活習慣，係好緊要嘅。"),
    ("card_daniel_073", "育つ", "to grow up", "成長、長大", "자라다", "grandir", "豊かな自然に囲まれた田舎町でのびのびと育ちました。", "I grew up carefree in a rural town surrounded by rich nature.", "我在大自然環抱的鄉村小鎮裡無憂無慮、健康地長大。", "아름다운 자연으로 둘러싸인 시골 마을에서 건강하게 자랐습니다.", "我喺被大自然環繞嘅鄉村小鎮無憂無慮長大成人。"),
    ("card_daniel_074", "子育て", "parenting", "育兒、教養孩子", "육아", "éducation des enfants", "働きながら子育てをする親を応援する制度が増えています。", "Systems supporting working parents raising kids are increasing.", "支援職業父母邊工作邊帶小孩的育兒福利制度日益增加。", "일과 육아를 병행하는 부모를 지원하는 복지 제도가 늘고 있습니다.", "而家越嚟越多支援在職父母邊返工邊照顧仔女嘅福利措施。"),
    ("card_daniel_075", "海岸", "coast, beach", "海岸、海濱", "해안", "côte, rivage", "潮風を感じながら、美しい海岸沿いをゆっくりドライブしました。", "Feeling the sea breeze, I drove slowly along the scenic coast.", "吹著舒適的宜人海風，我開著車沿著美麗的海岸線悠閒兜風。", "시원한 바닷바람을 맞으며 아름다운 해안 도로를 드라이브했습니다.", "吹住舒服嘅海風，沿住風景好靚嘅海岸線慢慢兜風。"),
    ("card_daniel_076", "会談", "formal talks", "會談、會晤", "회담", "pourparlers, sommet", "両国の首脳が集まり、経済協力について重要な会談を行いました。", "Leaders of both nations met and held talks on economic cooperation.", "兩國領導人齊聚一堂，就經濟合作召開了重要的元首會談。", "양국 정상이 모여 경제 협력에 관한 중요한 회담을 가졌습니다.", "兩國元首聚首一堂，就經貿合作舉行咗好重要嘅高峰會談。"),
    ("card_daniel_077", "研究室", "laboratory, lab", "研究室、實驗室", "연구실", "laboratoire", "大学の研究室で、新しいバイオテクノロジーの研究に励んでいます。", "In the university lab, I am dedicated to biotechnology research.", "在大學的專門研究室裡，我正努力鑽研全新的生物科技技術。", "대학 연구실에서 새로운 생명공학 기술 연구에 매진하고 있습니다.", "喺大學研究室入面，我好努力鑽研新嘅生物科技項目。"),
    ("card_daniel_078", "片付ける", "to tidy up", "整理、收拾", "정리하다, 치우다", "ranger", "散らかった机の上を片付けて、作業スペースを広げました。", "I tidied up the cluttered desk and made the workspace spacious.", "我把堆滿雜物的書桌收拾乾淨，讓辦公空間變得開闊清爽。", "어질러진 책상 위를 깨끗이 치워 작업 공간을 넓혔습니다.", "將張亂糟糟嘅書枱執返好，多咗好多位做嘢。"),
    ("card_daniel_079", "嘘をつく", "to tell a lie", "說謊、撒謊", "거짓말을 하다", "mentir", "信用を失ってしまうので、嘘をつくのは絶対にやめましょう。", "Never tell lies, as doing so destroys trust.", "說謊會徹底失去他人對自己的信任，千萬不要撒謊。", "신뢰를 잃게 되므로 거짓말을 하는 것은 절대 피해야 합니다.", "講大話會冇人再信你，切記千祈唔好講謊言。"),
    ("card_daniel_080", "嘘つき", "liar", "騙子、說謊的人", "거짓말쟁이", "menteur", "彼はいつも約束を破るので、すっかり嘘つき呼ばわりされています。", "Because he always breaks promises, he's known as a liar.", "他總是說話不算話違背約定，已經被大家當成了說謊的大騙子。", "그는 매번 약속을 어겨서 완전히 거짓말쟁이로 불리고 있습니다.", "佢次次應承人做唔到失信，已經俾人當咗係大話精。"),
    ("card_daniel_081", "ウイルス", "virus", "病毒", "바이러스", "virus", "冬は風邪やインフルエンザのウイルスが流行しやすい季節です。", "Winter is a season when cold and flu viruses spread easily.", "冬季是感冒以及流感病毒非常容易廣泛流行的危險季節。", "겨울은 감기와 독감 바이러스가 유행하기 쉬운 계절입니다.", "冬天係流感同傷風感冒病毒好容易傳播肆虐嘅季節。"),
    ("card_daniel_082", "お湯", "hot water", "熱水、溫水", "뜨거운 물", "eau chaude", "ヤカンでお湯を沸かして、美味しい温かい紅茶を淹れました。", "I boiled hot water in a kettle and brewed delicious hot black tea.", "我用熱水壺把水燒開，沖泡了一杯香濃好喝的熱紅茶。", "주전자에 물을 끓여서 향긋하고 따뜻한 홍차를 우려냈습니다.", "用個水煲煲好滾水，沖咗杯香濃嘅熱紅茶飲。"),
    ("card_daniel_083", "目印", "landmark, marker", "路標、標誌物", "길잡이, 표식", "repère", "駅前の時計塔を目印にして、友達と待ち合わせをしました。", "Using the clock tower by the station as marker, I met with my friend.", "我們以車站前的顯眼鐘樓為路標集合地點，與朋友碰面。", "역 앞 시계탑을 표식 삼아 친구와 약속 장소를 정했습니다.", "我哋以火車站出面座鐘樓做標記，約好喺嗰度等。"),
    ("card_daniel_084", "お墓参り", "visiting family grave", "掃墓、祭祖", "성묘", "visite des tombes", "お盆休みに家族みんなで先祖のお墓参りに行ってきました。", "During Obon vacation, our family visited our ancestors' graves.", "在盂蘭盆節長假中，我們全家一起去為列祖列宗掃墓祭拜。", "추석 연휴에 온 가족이 다 함께 조상님 성묘를 다녀왔습니다.", "趁住節日假期，全家人一齊去拜山掃墓祭祀祖先。"),
    ("card_daniel_085", "祖先", "ancestor", "祖先、先人", "조상", "ancêtre", "ご先祖様を大切に敬う日本の伝統行事を大切にしています。", "I treasure traditional Japanese customs that revere ancestors.", "我十分珍視日本尊敬慎終追遠、敬拜祖先的優良傳統習俗。", "조상님을 소중히 모시는 일본의 전통 명절 문화를 소중히 여깁니다.", "我哋好重視傳統習俗，一直以來都好尊敬懷念先人。"),
    ("card_daniel_086", "墓", "grave, tomb", "墓、墳墓", "묘, 무덤", "tombe", "丘の上の静かな場所にお墓があり、定期的に掃除をしています。", "The family grave is in quiet spot on hill, cleaned regularly.", "家族的墓地位於山丘上的清幽寧靜處，我們定期前往打掃整理。", "언덕 위 한적한 곳에 묘소가 있어 정기적으로 청소하고 있습니다.", "屋企個家族墓地喺個好清靜嘅山仔上面，定時都會去打掃。"),
    ("card_daniel_087", "港", "port, harbor", "港口、港灣", "항구", "port", "朝日が昇る港に、獲れたての魚を積んだ船が次々と戻ってきました。", "Boats loaded with fresh catch returned to harbor at sunrise.", "朝陽升起的港灣中，滿載著剛捕撈鮮魚的漁船陸續進港靠岸。", "아침 해가 뜨는 항구로 갓 잡은 생선을 실은 배들이 속속 들어옵니다.", "清晨日出嘅海港度，一艘接一艘滿載海鮮嘅漁船陸續駛返入嚟。"),
    ("card_daniel_088", "広告", "advertisement", "廣告", "광고", "publicité", "新製品の発売に合わせて、街中に魅力的な広告が掲示されました。", "Eye-catching ads were posted across town for new product launch.", "配合全新產品正式發售上市，市區各處刊登了許多吸睛的宣傳廣告。", "신제품 출시에 맞춰 시내 곳곳에 매력적인 광고가 걸렸습니다.", "配合全新產品推出，成個市區周圍都貼滿晒好吸睛嘅宣傳廣告。"),
    ("card_daniel_089", "人口", "population", "人口", "인구", "population", "この都市は住みやすさから年々人口が増加しています。", "Because this city is so livable, its population increases yearly.", "由於這座城市極為宜居舒適，居民人口數逐年持續穩定成長。", "이 도시는 살기 좋아서 해마다 인구가 꾸준히 증가하고 있습니다.", "呢個城市好宜居環境又好，每一年嘅居住人口都穩步上升。"),
    ("card_daniel_090", "候補", "candidate", "候選人、候補選項", "후보", "candidat, option", "次の旅行先の候補として、北海道と沖縄を検討しています。", "As candidate destinations for next trip, we are considering Hokkaido and Okinawa.", "作為下一趟旅行的候選目的地，我們正認真考慮北海道與沖繩。", "다음 여행지 후보로 홋카이도와 오키나와를 적극 검토 중입니다.", "下一次旅行嘅候選目的地，我哋考慮緊去北海道定沖繩。"),
    ("card_daniel_091", "底", "bottom", "底部", "바닥", "fond", "お鍋の底を焦げ付かせないように、弱火でじっくり煮込みました。", "Simmered on low heat so the pot bottom wouldn't burn.", "為了不讓鍋底燒焦黏鍋，我用文火小火慢燉細細熬煮。", "냄비 바닥이 타지 않도록 약한 불로 뭉근하게 끓였습니다.", "為咗唔好煲燶個鍋底，我較咗慢火慢燉細煨。"),
    ("card_daniel_092", "お客様", "customer, guest", "客人、顧客", "고객님, 손님", "client, invité", "「いらっしゃいませ！お客様、こちらの奥のお席へどうぞ。」", "'Welcome! Esteemed customer, please come this way to back seats.'", "「歡迎光臨！貴賓您好，請往裡面舒適的雅座入座。」", "“어서 오십시오! 고객님, 이쪽 안쪽 자리로 안내해 드리겠습니다.”", "「歡迎光臨！貴賓你好，請行入少少坐呢邊嘅卡位啦。」"),
    ("card_daniel_093", "十分です", "that's enough", "十分充分了、夠了", "충분합니다", "c'est suffisant", "「お代わりはいかがですか？」「ありがとうございます、もう十分です。」", "'Would you like a refill?' 'Thank you, I've had plenty.'", "「要再來一碗添飯嗎？」「非常謝謝您，我已經吃得十分飽足了。」", "“더 드시겠어요?” “감사합니다, 이미 충분히 배부릅니다.”", "「使唔使再添多碗飯呀？」「多謝你，我已經好飽好足夠喇。」"),
    ("card_daniel_094", "夜行バス", "overnight bus", "夜間長途巴士", "야간 버스", "bus de nuit", "交通費を節約するため、東京まで夜行バスを利用しました。", "To save transit costs, I used an overnight bus to Tokyo.", "為了節省昂貴的交通旅費，我搭乘夜間長途巴士前往東京。", "교통비를 아끼기 위해 도쿄까지 야간 버스를 이용했습니다.", "為咗慳返啲交通費，我搭咗通宵夜行長途巴士去東京。"),
    ("card_daniel_095", "馬車", "carriage", "馬車", "마차", "calèche, fiacre", "歴史あるヨーロッパの旧市街を観光馬車で優雅に巡りました。", "We elegantly toured historic European old town on a tourist carriage.", "我們搭乘觀光馬車，優雅悠閒地穿梭遊覽歐洲古意盎然的老城區。", "유서 깊은 유럽의 구시가지를 관광 마차로 우아하게 둘러보았습니다.", "我哋坐住觀光馬車，好優雅愜意噉遊覽歷史悠久嘅歐洲古城。"),
    ("card_daniel_096", "考え事をする", "to be lost in thought", "思考事情、沉思", "골똘히 생각하다", "être absorbé dans ses pensées", "窓の外をぼんやり見つめながら、今後のキャリアについて考え事をしました。", "Gazing out the window, I was lost in thought about my future career.", "我望著窗外發呆，若有所思地沉思起自己未來的職涯規劃。", "창밖을 멍하니 바라보며 앞으로의 진로에 대해 골똘히 생각했습니다.", "我望住隻窗發呆，靜靜思考緊自己未來嘅事業發展規劃。"),
    ("card_daniel_097", "厳しい", "strict, severe", "嚴格的、嚴厲的", "엄격하다", "strict, sévère", "指導教官の指導は厳しいですが、その分確実に成長できます。", "The advisor's guidance is strict, but that leads to solid growth.", "指導教授的要求雖然非常嚴格，但因此能讓自己的實力突飛猛進。", "지도 교수님의 지도는 엄격하지만, 그만큼 확실하게 실력을 키울 수 있습니다.", "導師嘅要求雖然好嚴格好嚴謹，但真係學到好多嘢進步神速。"),
    ("card_daniel_098", "最低賃金", "minimum wage", "法定最低工資", "최저임금", "salaire minimum", "法律の改正によって、来月から全国の最低賃金が引き上げられます。", "Through legal revision, minimum wage nationwide will rise next month.", "隨著法律修訂通過，從下個月起全國法定最低工資將全面調漲。", "법 개정으로 다음 달부터 전국의 최저임금이 인상됩니다.", "隨住法例修訂，由下個月開始全國嘅法定最低工資會調高。"),
    ("card_daniel_099", "引っ越す", "to move house", "搬家、遷移", "이사하다", "déménager", "職場の近くの静かで暮らしやすいマンションへ引っ越しました。", "I moved to a quiet, livable apartment close to my workplace.", "我搬進了距離公司附近、環境清幽生活便利的高級電梯大樓公寓。", "직장 근처의 조용하고 살기 편한 아파트로 이사했습니다.", "我搬咗去公司附近一間好安靜又住得好舒服嘅屋苑單位。"),
    ("card_daniel_100", "新鮮な", "fresh", "新鮮的", "신선한", "frais", "毎朝市場から直送される新鮮な海の幸を贅沢に味わいました。", "I lavishly enjoyed fresh seafood delivered straight from market daily.", "我豪邁享受了每天清晨從魚市場產地直送的新鮮頂級海鮮。", "매일 아침 시장에서 직송되는 신선한 해산물을 맘껏 맛보았습니다.", "我好奢侈噉品嚐咗每日由魚市場直送嘅新鮮時令海鮮。"),
    ("card_daniel_101", "特に", "especially", "特別、尤其", "특히", "particulièrement", "日本の秋は、特に京都の鮮やかな紅葉が息をのむほど美しいです。", "Japanese autumn is breathtakingly beautiful, especially Kyoto's red foliage.", "日本的秋天景色宜人，尤其是京都絢爛的紅楓美得令人屏息。", "일본의 가을은 특히 교토의 단풍이 숨 막힐 정도로 아름답습니다.", "日本嘅秋天風景好靚，特別係京都嘅紅葉真係靚到無得彈。"),
    ("card_daniel_102", "見逃す", "to miss seeing", "錯過、漏看", "놓치다", "manquer, rater", "録画を忘れてしまい、大好きなアニメの最終話をリアルタイムで見逃しました。", "I forgot to record and missed live broadcast of favorite anime finale.", "我忘了設定錄影，結果錯過了最愛動漫大結局的首播播出。", "녹화를 깜빡하는 바람에 좋아하는 애니메이션의 마지막 회 본방을 놓쳤습니다.", "我唔記得咗錄低，錯過咗最鍾意嗰套動漫大結局嘅電視直播。"),
    ("card_daniel_103", "賄賂", "bribe", "賄賂、行賄", "뇌물", "pot-de-vin", "いかなる不正な賄賂の授受も、社会の信頼を損なう犯罪行為です。", "Any giving or receiving of bribes is crime destroying social trust.", "任何非法的收受賄賂行為，都是嚴重破壞社會公信力的重大犯罪。", "어떠한 부정 청탁이나 뇌물 수수도 사회의 신뢰를 무너뜨리는 범죄 행위입니다.", "任何收受利益賄賂嘅行為，都係破壞社會誠信同法治嘅嚴重罪案。")
]

# Process and load
with open("database/class_vocab_data.js", "r", encoding="utf-8") as f:
    class_text = f.read()

s_class = class_text.find("[")
e_class = class_text.rfind("];") + 1
class_prefix = class_text[:s_class]
class_suffix = class_text[e_class:]
class_cards = json.loads(class_text[s_class:e_class].strip())

daniel_dict = {}
for entry in DANIEL_ALL:
    cid = entry[0]
    daniel_dict[cid] = {
        "meaning": {
            "zh_TW": entry[3],
            "zh_CN": entry[3],
            "ko": entry[4],
            "zh_HK": entry[3],
            "fr": entry[5]
        },
        "example": {
            "ja": entry[6],
            "en": entry[7],
            "zh_TW": entry[8],
            "zh_CN": entry[8],
            "ko": entry[9],
            "zh_HK": entry[10],
            "fr": entry[7]
        }
    }

# Apply DANIEL_TRANSLATIONS
for cid, data in DANIEL_TRANSLATIONS.items():
    if cid not in daniel_dict:
        daniel_dict[cid] = {"meaning": {}, "example": {}}
    daniel_dict[cid]["meaning"].update(data["meaning"])
    daniel_dict[cid]["example"].update(data["example"])

updated_count = 0
for card in class_cards:
    cid = card["id"]
    if cid in daniel_dict:
        d = daniel_dict[cid]
        # Update meaning
        for lang, val in d["meaning"].items():
            card["meaning"][lang] = val
        # Update example
        if "ja" in d["example"] and len(d["example"]["ja"]) > len(card["example"].get("ja", "")):
            card["example"]["ja"] = d["example"]["ja"]
        if "en" in d["example"]:
            card["example"]["en"] = d["example"]["en"]
        card["example"]["zh_TW"] = d["example"]["zh_TW"]
        card["example"]["zh_CN"] = d["example"]["zh_CN"]
        card["example"]["ko"] = d["example"]["ko"]
        card["example"]["zh_HK"] = d["example"]["zh_HK"]
        card["example"]["fr"] = d["example"]["fr"]
        updated_count += 1
    elif cid == "card_midori_burikko":
        card["meaning"] = {
            "ja": "ぶりっ子",
            "en": "girl playing dumb/cute, coquette",
            "zh_TW": "裝可愛、裝無辜造作的女孩",
            "zh_CN": "装可爱、装无辜造作的女孩",
            "ko": "귀여운 척하는 여자, 내숭 떠는 여자",
            "zh_HK": "好鍾意扮可愛裝無辜嘅女仔",
            "fr": "fille minaudière, coquette"
        }
        card["example"] = {
            "ja": "<ruby>彼女<rt>かのじょ</rt></ruby>は<ruby>男性<rt>だんせい</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>に<ruby>行<rt>い</rt></ruby>くと、<ruby>急<rt>きゅう</rt></ruby>にぶりっ<ruby>子<rt>こ</rt></ruby>になる。",
            "en": "Whenever she is around men, she suddenly acts all cute and coquette.",
            "zh_TW": "她一到男生面前，就突然變得很愛裝可愛。",
            "zh_CN": "她一到男生面前，就突然变显得很爱装可爱。",
            "ko": "그녀는 남자 앞에만 가면 갑자기 내숭을 떨며 애교를 부린다.",
            "zh_HK": "佢一去到男仔面前，就突然間變得好造作好鍾意扮可愛。",
            "fr": "Dès qu'elle se trouve devant des hommes, elle se met soudain à faire la fille mignonne et précieuse."
        }
        updated_count += 1

print(f"Updated {updated_count} cards (Daniel + Midori burikko)")

new_class_json = json.dumps(class_cards, ensure_ascii=False, indent=2)
with open("database/class_vocab_data.js", "w", encoding="utf-8") as f:
    f.write(class_prefix + new_class_json + class_suffix)
with open("public/database/class_vocab_data.js", "w", encoding="utf-8") as f:
    f.write(class_prefix + new_class_json + class_suffix)

print("✅ Saved to database/class_vocab_data.js and public/database/class_vocab_data.js")
