# -*- coding: utf-8 -*-
import json
import os
import re

NARRATOR_VOICE = 'ja-JP-Neural2-B'
FEMALE_VOICE = 'ja-JP-Neural2-B'
MALE_VOICE = 'ja-JP-Neural2-C'

def main():
    # 91 questions strictly following JLPT official Guidebook structure
    # Section 1: 言語知識（文字・語彙） (35 questions)
    # Section 2: 言語知識（文法）・読解 (32 questions)
    # Section 3: 聴解 (24 questions)
    
    questions = []
    
    # -------------------------------------------------------------
    # SECTION 1: 文字・語彙 (Q1〜Q35)
    # -------------------------------------------------------------
    
    # --- 問題1: 漢字読み (Q1〜Q12) ---
    s1_m1 = [
        {
            "qNum": 1,
            "title": "あの山は とても 高いです。",
            "titleRuby": "あの<ruby>山<rt>やま</rt></ruby>は とても <ruby>高<rt>たか</rt></ruby>いです。",
            "target": "山",
            "options": ["かわ", "やま", "うみ", "もり"],
            "correctIndex": 1,
            "explanation": "「山」の正しい読み方は「やま」です。\n1の「かわ」は「川」、3の「うみ」は「海」、4の「もり」は「森」です。"
        },
        {
            "qNum": 2,
            "title": "毎朝、７時に 起きます。",
            "titleRuby": "<ruby>毎朝<rt>まいあさ</rt></ruby>、７時に <ruby>起<rt>お</rt></ruby>きます。",
            "target": "毎朝",
            "options": ["まいあさ", "まいばん", "まいひ", "まいねん"],
            "correctIndex": 0,
            "explanation": "「毎朝」の正しい読み方は「まいあさ」です。\n「まいばん」は「毎晩」、「まいひ」ではなく「まいにち（毎日）」、「まいねん」は「毎年（まいとし）」です。"
        },
        {
            "qNum": 3,
            "title": "駅の 前で 友だちに 会いました。",
            "titleRuby": "<ruby>駅<rt>えき</rt></ruby>の <ruby>前<rt>まえ</rt></ruby>で <ruby>友<rt>とも</rt></ruby>だちに <ruby>会<rt>あ</rt></ruby>いました。",
            "target": "駅",
            "options": ["はし", "いえ", "えき", "みせ"],
            "correctIndex": 2,
            "explanation": "「駅」の正しい読み方は「えき」です。\n1「はし（橋）」、2「いえ（家）」、4「みせ（店）」です。"
        },
        {
            "qNum": 4,
            "title": "この 川の 水は つめたいです。",
            "titleRuby": "この <ruby>川<rt>かわ</rt></ruby>の <ruby>水<rt>みず</rt></ruby>は つめたいです。",
            "target": "水",
            "options": ["みず", "ゆき", "あめ", "き"],
            "correctIndex": 0,
            "explanation": "「水」の正しい読み方は「みず」です。\n2「ゆき（雪）」、3「あめ（雨）」、4「き（木）」です。"
        },
        {
            "qNum": 5,
            "title": "机の 上に 本が あります。",
            "titleRuby": "机の <ruby>上<rt>うえ</rt></ruby>に <ruby>本<rt>ほん</rt></ruby>が あります。",
            "target": "上",
            "options": ["した", "なか", "まえ", "うえ"],
            "correctIndex": 3,
            "explanation": "「上」の正しい読み方は「うえ」です。\n1「した（下）」、2「なか（中）」、3「まえ（前）」です。"
        },
        {
            "qNum": 6,
            "title": "新しい 車を 買いました。",
            "titleRuby": "<ruby>新<rt>あたら</rt></ruby>しい <ruby>車<rt>くるま</rt></ruby>を <ruby>買<rt>か</rt></ruby>いました。",
            "target": "車",
            "options": ["じてんしゃ", "でんしゃ", "くるま", "ひこうき"],
            "correctIndex": 2,
            "explanation": "「車」の正しい読み方は「くるま」です。\n1「自転車」、2「電車」、4「飛行機」です。"
        },
        {
            "qNum": 7,
            "title": "私の 父は ５０さいです。",
            "titleRuby": "<ruby>私<rt>わたし</rt></ruby>の <ruby>父<rt>ちち</rt></ruby>は ５０さいです。",
            "target": "父",
            "options": ["はは", "ちち", "あに", "あね"],
            "correctIndex": 1,
            "explanation": "「父」の正しい読み方は「ちち」です。\n1「はは（母）」、3「あに（兄）」、4「あね（姉）」です。"
        },
        {
            "qNum": 8,
            "title": "きょうは 雨が ふっています。",
            "titleRuby": "きょうは <ruby>雨<rt>あめ</rt></ruby>が ふっています。",
            "target": "雨",
            "options": ["ゆき", "かぜ", "くも", "あめ"],
            "correctIndex": 3,
            "explanation": "「雨」の正しい読み方は「あめ」です。\n1「ゆき（雪）」、2「かぜ（風）」、3「くも（雲）」です。"
        },
        {
            "qNum": 9,
            "title": "教室に 学生が １０人 います。",
            "titleRuby": "<ruby>教室<rt>きょうしつ</rt></ruby>に <ruby>学生<rt>がくせい</rt></ruby>が １０<ruby>人<rt>にん</rt></ruby> います。",
            "target": "学生",
            "options": ["がくせい", "せんせい", "いしゃ", "かいしゃいん"],
            "correctIndex": 0,
            "explanation": "「学生」の正しい読み方は「がくせい」です。\n2「せんせい（先生）」、3「いしゃ（医者）」、4「かいしゃいん（会社員）」です。"
        },
        {
            "qNum": 10,
            "title": "つぎの かどを 右へ まがります。",
            "titleRuby": "つぎの かどを <ruby>右<rt>みぎ</rt></ruby>へ まがります。",
            "target": "右",
            "options": ["ひだり", "みぎ", "きた", "みなみ"],
            "correctIndex": 1,
            "explanation": "「右」の正しい読み方は「みぎ」です。\n1「ひだり（左）」、3「きた（北）」、4「みなみ（南）」です。"
        },
        {
            "qNum": 11,
            "title": "田中さんの 話を 聞きました。",
            "titleRuby": "<ruby>田中<rt>たなか</rt></ruby>さんの <ruby>話<rt>はなし</rt></ruby>を <ruby>聞<rt>き</rt></ruby>きました。",
            "target": "話",
            "options": ["うた", "こえ", "はなし", "おと"],
            "correctIndex": 2,
            "explanation": "「話」の正しい読み方は「はなし」です。\n1「うた（歌）」、2「こえ（声）」、4「おと（音）」です。"
        },
        {
            "qNum": 12,
            "title": "この りんごは 大きいです。",
            "titleRuby": "この りんごは <ruby>大<rt>おお</rt></ruby>きいです。",
            "target": "大",
            "options": ["ちい", "おお", "なが", "たか"],
            "correctIndex": 1,
            "explanation": "「大きい」の「大」の正しい読み方は「おお」です（おおきい）。\n1「ちい（小さい）」、3「なが（長い）」、4「たか（高い）」です。"
        }
    ]

    for item in s1_m1:
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec1",
            "subsectionId": "s1_m1",
            "category": "漢字読み",
            "qNum": item["qNum"],
            "title": item["title"],
            "titleRuby": item["titleRuby"],
            "targetWord": item["target"],
            "questionText": f"<u>{item['target']}</u>の ことばは どう よみますか。",
            "options": item["options"],
            "correctIndex": item["correctIndex"],
            "weight": 1.0,
            "explanation": item["explanation"]
        })

    # --- 問題2: 表記 (Q13〜Q20) ---
    s1_m2 = [
        {
            "qNum": 13,
            "title": "ノートに なまえを かいて ください。",
            "titleRuby": "ノートに <u>なまえ</u>を かいて ください。",
            "target": "なまえ",
            "options": ["本名", "名前", "名字", "名目"],
            "correctIndex": 1,
            "explanation": "「なまえ」は漢字で「名前」と書きます。「名」は名まえ、「前」はまえを表します。"
        },
        {
            "qNum": 14,
            "title": "あそこに おんなのひとが います。",
            "titleRuby": "あそこに <u>おんなのひと</u>が います。",
            "target": "おんなのひと",
            "options": ["女の人", "男の人", "大人", "子供"],
            "correctIndex": 0,
            "explanation": "「おんなのひと」は漢字で「女の人」と書きます。2「男の人」はおとこのひと、3「大人」はおとなです。"
        },
        {
            "qNum": 15,
            "title": "あしたは やすみです。",
            "titleRuby": "あしたは <u>やすみ</u>です。",
            "target": "やすみ",
            "options": ["休み", "体み", "本み", "木み"],
            "correctIndex": 0,
            "explanation": "「やすみ」は漢字で「休み」と書きます。「人」が「木」のそばで休む形です。「体（からだ）」と形が似ているので注意しましょう。"
        },
        {
            "qNum": 16,
            "title": "毎朝 あさ ６時に おきます。",
            "titleRuby": "<ruby>毎朝<rt>まいあさ</rt></ruby> <u>あさ</u> ６時に おきます。",
            "target": "あさ",
            "options": ["朝", "夜", "昼", "夕"],
            "correctIndex": 0,
            "explanation": "「あさ」は漢字で「朝」と書きます。2「夜」はよる、3「昼」はひる、4「夕」はゆう・ゆうがたです。"
        },
        {
            "qNum": 17,
            "title": "ほんを ３さつ よみました。",
            "titleRuby": "<u>ほん</u>を ３さつ よみました。",
            "target": "ほん",
            "options": ["木", "体", "本", "休"],
            "correctIndex": 2,
            "explanation": "「ほん」は漢字で「本」と書きます。1「木」はき、2「体」はからだ、4「休」はやす（み）です。"
        },
        {
            "qNum": 18,
            "title": "あの しろい シャツが すきです。",
            "titleRuby": "あの <u>しろい</u> シャツが すきです。",
            "target": "しろい",
            "options": ["赤い", "青い", "黒い", "白い"],
            "correctIndex": 3,
            "explanation": "「しろい」は漢字で「白い」と書きます。1「赤い」はあかい、2「青い」はあおい、3「黒い」はくろいです。"
        },
        {
            "qNum": 19,
            "title": "たいようは ひがしから のぼります。",
            "titleRuby": "たいようは <u>ひがし</u>から のぼります。",
            "target": "ひがし",
            "options": ["東", "西", "南", "北"],
            "correctIndex": 0,
            "explanation": "「ひがし」は漢字で「東」と書きます。2「西」はにし、3「南」はみなみ、4「北」はきたです。"
        },
        {
            "qNum": 20,
            "title": "げんきな おとこのこが はしっています。",
            "titleRuby": "げんきな <u>おとこのこ</u>が <ruby>走<rt>はし</rt></ruby>っています。",
            "target": "おとこのこ",
            "options": ["女の子", "男の子", "小人", "子犬"],
            "correctIndex": 1,
            "explanation": "「おとこのこ」は漢字で「男の子」と書きます。1「女の子」はおんなのこです。"
        }
    ]

    for item in s1_m2:
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec1",
            "subsectionId": "s1_m2",
            "category": "表記",
            "qNum": item["qNum"],
            "title": item["title"],
            "titleRuby": item["titleRuby"],
            "targetWord": item["target"],
            "questionText": f"<u>{item['target']}</u>の ことばは どう かきますか。",
            "options": item["options"],
            "correctIndex": item["correctIndex"],
            "weight": 1.0,
            "explanation": item["explanation"]
        })

    # --- 問題3: 文脈規定 (Q21〜Q30) ---
    s1_m3 = [
        {
            "qNum": 21,
            "title": "ごはんを 食べたあと、スプーンを （　）。",
            "titleRuby": "ごはんを <ruby>食<rt>た</rt></ruby>べたあと、スプーンを （　）。",
            "options": ["あらいました", "みせました", "こまりました", "あけました"],
            "correctIndex": 0,
            "explanation": "食べた後のスプーンは「洗います（あらいました）」。\n2「見せました」、3「困りました」、4「開けました」は文脈に合いません。"
        },
        {
            "qNum": 22,
            "title": "風が ふいて、きょうは すこし （　）です。",
            "titleRuby": "<ruby>風<rt>かぜ</rt></ruby>が ふいて、きょうは すこし （　）です。",
            "options": ["すずしい", "ほしい", "にぎやか", "じょうず"],
            "correctIndex": 0,
            "explanation": "風が吹いて気温が心地よく下がる様子は「すずしい（涼しい）」と言います。\n2「ほしい（欲しい）」、3「にぎやか（賑やか）」、4「じょうず（上手）」は文脈に合いません。"
        },
        {
            "qNum": 23,
            "title": "（　）に 手紙を 入れて きました。",
            "titleRuby": "（　）に <ruby>手紙<rt>てがみ</rt></ruby>を <ruby>入<rt>い</rt></ruby>れて きました。",
            "options": ["ポスト", "ノート", "プール", "カメラ"],
            "correctIndex": 0,
            "explanation": "手紙を投函する箱は「ポスト」です。\n2「ノート」、3「プール」、4「カメラ」に手紙を入れて投函することはありません。"
        },
        {
            "qNum": 24,
            "title": "切符を （　）に 入れて おきます。",
            "titleRuby": "<ruby>切符<rt>きっぷ</rt></ruby>を （　）に <ruby>入<rt>い</rt></ruby>れて おきます。",
            "options": ["ポケット", "テーブル", "ストーブ", "スリッパ"],
            "correctIndex": 0,
            "explanation": "切符を服の「ポケット」に入れて保管します。\n2「テーブル」、3「ストーブ（暖房器具）」、4「スリッパ（室内履き）」は不適切です。"
        },
        {
            "qNum": 25,
            "title": "朝 起きてから、まず （　）を あびます。",
            "titleRuby": "<ruby>朝<rt>あさ</rt></ruby> <ruby>起<rt>お</rt></ruby>きてから、まず （　）を あびます。",
            "options": ["シャワー", "スカート", "ネクタイ", "ズボン"],
            "correctIndex": 0,
            "explanation": "「シャワーを あびる」でシャワーを浴びるという決まったコロケーションです。\n2「スカート」、3「ネクタイ」、4「ズボン」はいずれも衣服で「あびる」とは言いません。"
        },
        {
            "qNum": 26,
            "title": "エレベーターが 動かないので、（　）で ３階へ 行きます。",
            "titleRuby": "エレベーターが <ruby>動<rt>うご</rt></ruby>かないので、（　）で ３<ruby>階<rt>かい</rt></ruby>へ <ruby>行<rt>い</rt></ruby>きます。",
            "options": ["かいだん", "ぎんこう", "はし", "にわ"],
            "correctIndex": 0,
            "explanation": "エレベーターが動かないときに使って上階へ行くのは「かいだん（階段）」です。\n2「ぎんこう（銀行）」、3「はし（橋）」、4「にわ（庭）」は建物の上階への昇降手段ではありません。"
        },
        {
            "qNum": 27,
            "title": "あした テストが ありますから、家で （　）します。",
            "titleRuby": "あした テストが ありますから、<ruby>家<rt>いえ</rt></ruby>で （　）します。",
            "options": ["べんきょう", "けっこん", "さんぽ", "りょこう"],
            "correctIndex": 0,
            "explanation": "テストがある前日には「べんきょう（勉強）」をします。\n2「けっこん（結婚）」、3「さんぽ（散歩）」、4「りょこう（旅行）」は文脈に合いません。"
        },
        {
            "qNum": 28,
            "title": "寒いですね。（　） お茶を 飲みましょう。",
            "titleRuby": "<ruby>寒<rt>さむ</rt></ruby>いですね。（　） お<ruby>茶<rt>ちゃ</rt></ruby>を <ruby>飲<rt>の</rt></ruby>みましょう。",
            "options": ["あたたかい", "おもい", "くらい", "ひろい"],
            "correctIndex": 0,
            "explanation": "寒いときには「あたたかい（温かい）」お茶を飲むのが適切です。\n2「おもい（重い）」、3「くらい（暗い）」、4「ひろい（広い）」は飲み物の温度には使いません。"
        },
        {
            "qNum": 29,
            "title": "荷物が 重いですから、タクシーを （　）。",
            "titleRuby": "<ruby>荷物<rt>にもつ</rt></ruby>が <ruby>重<rt>おも</rt></ruby>いですから、タクシーを （　）。",
            "options": ["よびました", "ならびました", "とまりました", "わたりました"],
            "correctIndex": 0,
            "explanation": "タクシーを呼ぶときは「タクシーを よびます（呼びました）」と言います。\n2「ならびました（並ぶ）」、3「とまりました（止まる）」、4「わたりました（渡る）」は他動詞として「タクシーを」に続きません。"
        },
        {
            "qNum": 30,
            "title": "来週の 土曜日は わたしの （　）ですから、パーティーを します。",
            "titleRuby": "<ruby>来週<rt>らいしゅう</rt></ruby>の <ruby>土曜日<rt>どようび</rt></ruby>は わたしの （　）ですから、パーティーを します。",
            "options": ["たんじょうび", "しゅうまつ", "きょうだい", "りょうしん"],
            "correctIndex": 0,
            "explanation": "パーティーを開くお祝いの日は「たんじょうび（誕生日）」が最も適切です。\n2「しゅうまつ（週末）」、3「きょうだい（兄弟）」、4「りょうしん（両親）」は文脈に合いません。"
        }
    ]

    for item in s1_m3:
        # Balance correctIndex across options
        shift = (item["qNum"] % 4)
        orig_opts = item["options"]
        new_opts = orig_opts[shift:] + orig_opts[:shift]
        correct_idx = (item["correctIndex"] - shift) % 4
        
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec1",
            "subsectionId": "s1_m3",
            "category": "文脈規定",
            "qNum": item["qNum"],
            "title": item["title"],
            "titleRuby": item["titleRuby"],
            "questionText": "（　）に なにを いれますか。いちばん いい ものを ひとつ えらんで ください。",
            "options": new_opts,
            "correctIndex": correct_idx,
            "weight": 1.0,
            "explanation": item["explanation"]
        })

    # --- 問題4: 言い換え類義 (Q31〜Q35) ---
    s1_m4 = [
        {
            "qNum": 31,
            "title": "きのうの よる、雨が ふりました。",
            "titleRuby": "<u>きのうの よる</u>、<ruby>雨<rt>あめ</rt></ruby>が ふりました。",
            "options": [
                "おととい、雨が ふりました。",
                "ゆうべ、雨が ふりました。",
                "きょうの あさ、雨が ふりました。",
                "あしたの よる、雨が ふります。"
            ],
            "correctIndex": 1,
            "explanation": "「きのうの よる（昨日の夜）」は「ゆうべ（昨夜）」と言い換えることができます。"
        },
        {
            "qNum": 32,
            "title": "この 川で 泳ぐのは きけんです。",
            "titleRuby": "この <ruby>川<rt>かわ</rt></ruby>で <ruby>泳<rt>およ</rt></ruby>ぐのは <u>きけん</u>です。",
            "options": [
                "この 川で 泳ぐのは あぶないです。",
                "この 川で 泳ぐのは たのしいです。",
                "この 川で 泳ぐのは しずかです。",
                "この 川で 泳ぐのは ひろいです。"
            ],
            "correctIndex": 0,
            "explanation": "「きけん（危険）」は「あぶない（危ない）」と同じ意味です。"
        },
        {
            "qNum": 33,
            "title": "バスが すぐに 来ました。",
            "titleRuby": "バスが <u>すぐに</u> <ruby>来<rt>き</rt></ruby>ました。",
            "options": [
                "バスが ゆっくり 来ました。",
                "バスが 遅れて 来ました。",
                "バスが あまり 待たないで 来ました。",
                "バスが まだ 来ません。"
            ],
            "correctIndex": 2,
            "explanation": "「すぐに 来ました」は待つ時間がほとんどなかったという意味なので、「あまり 待たないで 来ました」とほぼ同じ意味になります。"
        },
        {
            "qNum": 34,
            "title": "私の 姉は びょういんの 先生です。",
            "titleRuby": "<ruby>私<rt>わたし</rt></ruby>の <ruby>姉<rt>あね</rt></ruby>は <u>びょういんの 先生</u>です。",
            "options": [
                "私の 姉は がくせいです。",
                "私の 姉は かしゅです。",
                "私の 姉は ぎんこういんです。",
                "私の 姉は いしゃです。"
            ],
            "correctIndex": 3,
            "explanation": "「びょういんの 先生（病院の先生）」は「いしゃ（医者・お医者さん）」のことです。"
        },
        {
            "qNum": 35,
            "title": "駅の 前の デパートで 買い物を しました。",
            "titleRuby": "<ruby>駅<rt>えき</rt></ruby>の <ruby>前<rt>まえ</rt></ruby>の <u>デパート</u>で <ruby>買<rt>か</rt></ruby>い<ruby>物<rt>もの</rt></ruby>を しました。",
            "options": [
                "駅の 前の 大きい 店で 買い物を しました。",
                "駅の 前の ちいさい 本屋で 買い物を しました。",
                "駅の 前の こうえんで 買い物を しました。",
                "駅の 前の びょういんで 買い物を しました。"
            ],
            "correctIndex": 0,
            "explanation": "「デパート（百貨店）」は衣類や食品など何でもそろう「大きい 店」のことです。"
        }
    ]

    for item in s1_m4:
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec1",
            "subsectionId": "s1_m4",
            "category": "言い換え類義",
            "qNum": item["qNum"],
            "title": item["title"],
            "titleRuby": item["titleRuby"],
            "questionText": "＿＿の ぶんと だいたい おなじ いみの ぶんが あります。いちばん いい ものを ひとつ えらんで ください。",
            "options": item["options"],
            "correctIndex": item["correctIndex"],
            "weight": 1.0,
            "explanation": item["explanation"]
        })

    # -------------------------------------------------------------
    # SECTION 2: 文法・読解 (Q36〜Q67)
    # -------------------------------------------------------------

    # --- 文法 問題1: 文法形式の判断 (Q36〜Q51) ---
    s2_m1 = [
        {
            "qNum": 36,
            "title": "わたしは 毎朝 ７時（　） 起きます。",
            "titleRuby": "わたしは <ruby>毎朝<rt>まいあさ</rt></ruby> ７<ruby>時<rt>じ</rt></ruby>（　） <ruby>起<rt>お</rt></ruby>きます。",
            "options": ["に", "で", "を", "へ"],
            "correctIndex": 0,
            "explanation": "特定の時間を表すときは助詞「に」を使います（７時に）。「で」は場所や手段、「を」は対象、「へ」は方向です。"
        },
        {
            "qNum": 37,
            "title": "えんぴつ（　） 名前を 書いて ください。",
            "titleRuby": "えんぴつ（　） <ruby>名前<rt>なまえ</rt></ruby>を <ruby>書<rt>か</rt></ruby>いて ください。",
            "options": ["で", "に", "を", "から"],
            "correctIndex": 0,
            "explanation": "筆記具や手段・道具を表すときは助詞「で」を使います（えんぴつで 書く）。"
        },
        {
            "qNum": 38,
            "title": "机の 上（　） 辞書が あります。",
            "titleRuby": "机の <ruby>上<rt>うえ</rt></ruby>（　） <ruby>辞書<rt>じしょ</rt></ruby>が あります。",
            "options": ["に", "を", "で", "へ"],
            "correctIndex": 0,
            "explanation": "物や人の存在場所（〜に あります／います）を表すときは助詞「に」を使います。"
        },
        {
            "qNum": 39,
            "title": "きのう、一人で デパート（　） 行きました。",
            "titleRuby": "きのう、<ruby>一人<rt>ひとり</rt></ruby>で デパート（　） <ruby>行<rt>い</rt></ruby>きました。",
            "options": ["へ", "が", "を", "から"],
            "correctIndex": 0,
            "explanation": "移動の目的地・方向を表すときは助詞「へ（または に）」を使います（デパートへ 行きました）。"
        },
        {
            "qNum": 40,
            "title": "朝ごはんは パン（　） たまごを 食べました。",
            "titleRuby": "<ruby>朝<rt>あさ</rt></ruby>ごはんは パン（　） たまごを <ruby>食<rt>た</rt></ruby>べました。",
            "options": ["と", "や", "も", "か"],
            "correctIndex": 0,
            "explanation": "名詞を並べて列挙するときは助詞「と」を使います（パンと たまご）。"
        },
        {
            "qNum": 41,
            "title": "友だちと 映画を （　） 行きました。",
            "titleRuby": "<ruby>友<rt>とも</rt></ruby>だちと <ruby>映画<rt>えいが</rt></ruby>を （　） <ruby>行<rt>い</rt></ruby>きました。",
            "options": ["見て", "見に", "見る", "見た"],
            "correctIndex": 1,
            "explanation": "移動の目的を表すときは「動詞のます形語幹 ＋ に行く」を使います（見ます → 見に行く）。"
        },
        {
            "qNum": 42,
            "title": "ここで 写真を （　）。",
            "titleRuby": "ここで <ruby>写真<rt>しゃしん</rt></ruby>を （　）。",
            "options": ["とっても いいです", "とっては いけません", "とりたいです", "とりました"],
            "correctIndex": 1,
            "explanation": "美術館や撮影禁止場所での禁止を表す表現は「〜てはいけません（とっては いけません）」です。"
        },
        {
            "qNum": 43,
            "title": "図書館では 静かに （　） ください。",
            "titleRuby": "<ruby>図書館<rt>としょかん</rt></ruby>では <ruby>静<rt>しず</rt></ruby>かに （　） ください。",
            "options": ["する", "して", "した", "しない"],
            "correctIndex": 1,
            "explanation": "相手にお願い・指示をするときは「動詞のて形 ＋ ください」を使います（します → して ください）。"
        },
        {
            "qNum": 44,
            "title": "すみません、この ペンを （　）。",
            "titleRuby": "すみません、この ペンを （　）。",
            "options": ["つかいますか", "つかって ください", "つかっても いいですか", "つかっては いけませんか"],
            "correctIndex": 2,
            "explanation": "相手に許可を求めるときは「〜てもいいですか（つかっても いいですか）」を使います。"
        },
        {
            "qNum": 45,
            "title": "来年、日本へ （　） です。",
            "titleRuby": "<ruby>来年<rt>らいねん</rt></ruby>、<ruby>日本<rt>にほん</rt></ruby>へ （　） です。",
            "options": ["行く", "行って", "行きたい", "行った"],
            "correctIndex": 2,
            "explanation": "自分の希望を表すときは「動詞ます形語幹 ＋ たいです」を使います（行きます → 行きたいです）。"
        },
        {
            "qNum": 46,
            "title": "わたしは すしを （　） ことが あります。",
            "titleRuby": "わたしは すしを （　） ことが あります。",
            "options": ["食べる", "食べた", "食べて", "食べない"],
            "correctIndex": 1,
            "explanation": "過去の経験を表すときは「動詞のた形 ＋ ことが あります」を使います（食べた ことが あります）。"
        },
        {
            "qNum": 47,
            "title": "寝る （　）、歯を みがきます。",
            "titleRuby": "<ruby>寝<rt>ね</rt></ruby>る （　）、<ruby>歯<rt>は</rt></ruby>を みがきます。",
            "options": ["まえに", "あとで", "とき", "ながら"],
            "correctIndex": 0,
            "explanation": "ある行動をする前を表す構文は「動詞辞書形 ＋ まえに」です（寝る まえに）。"
        },
        {
            "qNum": 48,
            "title": "ごはんを （　） あとで、薬を 飲みます。",
            "titleRuby": "ごはんを （　） あとで、<ruby>薬<rt>くすり</rt></ruby>を <ruby>飲<rt>の</rt></ruby>みます。",
            "options": ["食べる", "食べて", "食べた", "食べない"],
            "correctIndex": 2,
            "explanation": "ある行動が完了したあとを表す構文は「動詞た形 ＋ あとで」です（食べた あとで）。"
        },
        {
            "qNum": 49,
            "title": "いま、外で 雨が （　）。",
            "titleRuby": "いま、<ruby>外<rt>そと</rt></ruby>で <ruby>雨<rt>あめ</rt></ruby>が （　）。",
            "options": ["ふります", "ふって います", "ふりました", "ふるでしょう"],
            "correctIndex": 1,
            "explanation": "現在進行中の動作・出来事を表すときは「動詞て形 ＋ います」を使います（雨が ふって います）。"
        },
        {
            "qNum": 50,
            "title": "きのうは 忙しかった（　）、どこへも 行きませんでした。",
            "titleRuby": "きのうは <ruby>忙<rt>いそが</rt></ruby>しかった（　）、どこへも <ruby>行<rt>い</rt></ruby>きませんでした。",
            "options": ["から", "でも", "のに", "より"],
            "correctIndex": 0,
            "explanation": "理由・原因を表すときは文末に接続助詞「から」を使います（忙しかったから）。"
        },
        {
            "qNum": 51,
            "title": "りんごを みっつ （　）。",
            "titleRuby": "りんごを みっつ （　）。",
            "options": ["あります", "います", "ください", "どうぞ"],
            "correctIndex": 2,
            "explanation": "お店で注文したり物を求めるときは「〜を （数量） ください」と言います。"
        }
    ]

    for item in s2_m1:
        # Shift options to balance correct answers
        shift = (item["qNum"] % 4)
        orig_opts = item["options"]
        new_opts = orig_opts[shift:] + orig_opts[:shift]
        correct_idx = (item["correctIndex"] - shift) % 4
        
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec2",
            "subsectionId": "s2_m1",
            "category": "文法形式の判断",
            "qNum": item["qNum"],
            "title": item["title"],
            "titleRuby": item["titleRuby"],
            "questionText": "（　）に なにを いれますか。いちばん いい ものを ひとつ えらんで ください。",
            "options": new_opts,
            "correctIndex": correct_idx,
            "weight": 1.5,
            "explanation": item["explanation"]
        })

    # --- 文法 問題2: 文の組み立て ★ (Q52〜Q56) ---
    s2_m2 = [
        {
            "qNum": 52,
            "title": "わたしは ＿ ＿ ★ ＿ を 食べました。",
            "titleRuby": "わたしは ＿ ＿ ★ ＿ を <ruby>食<rt>た</rt></ruby>べました。",
            "options": ["レストランで", "おいしい", "きのう", "ラーメン"],
            "order": [2, 0, 1, 3], # 3 きのう, 1 レストランで, 2 おいしい, 4 ラーメン -> ★ is position index 2 (1-based: 3rd slot) -> option 2 ("おいしい")
            "correctIndex": 1,
            "explanation": "正しい語順は「わたしは 【きのう(3)】 【レストランで(1)】 ★【おいしい(2)】 【ラーメン(4)】 を 食べました」となります。★に入るのは 2「おいしい」です。"
        },
        {
            "qNum": 53,
            "title": "日曜日、＿ ＿ ★ ＿ に 会いました。",
            "titleRuby": "<ruby>日曜日<rt>にちようび</rt></ruby>、＿ ＿ ★ ＿ に <ruby>会<rt>あ</rt></ruby>いました。",
            "options": ["高校の", "友だち", "図書館で", "ときの"],
            "order": [2, 0, 3, 1], # 3 図書館で, 1 高校の, 4 ときの, 2 友だち -> ★ is position 3 (index 2) -> option 4 ("ときの")
            "correctIndex": 3,
            "explanation": "正しい語順は「日曜日、【図書館で(3)】 【高校の(1)】 ★【ときの(4)】 【友だち(2)】 に 会いました」となります。★に入るのは 4「ときの」です。"
        },
        {
            "qNum": 54,
            "title": "部屋が 寒いですから、＿ ＿ ★ ＿ ください。",
            "titleRuby": "<ruby>部屋<rt>へや</rt></ruby>が <ruby>寒<rt>さむ</rt></ruby>いですから、＿ ＿ ★ ＿ ください。",
            "options": ["を", "まど", "しめて", "どうぞ"],
            "order": [3, 1, 0, 2], # 4 どうぞ, 2 まど, 1 を, 3 しめて -> ★ is position 3 (index 2) -> option 1 ("を")
            "correctIndex": 0,
            "explanation": "正しい語順は「部屋が 寒いですから、【どうぞ(4)】 【まど(2)】 ★【を(1)】 【しめて(3)】 ください」となります。★に入るのは 1「を」です。"
        },
        {
            "qNum": 55,
            "title": "あしたは ＿ ＿ ★ ＿ 行きます。",
            "titleRuby": "あしたは ＿ ＿ ★ ＿ <ruby>行<rt>い</rt></ruby>きます。",
            "options": ["と", "で", "電車", "友だち"],
            "order": [3, 0, 2, 1], # 4 友だち, 1 と, 3 電車, 2 で -> ★ is position 3 (index 2) -> option 3 ("電車")
            "correctIndex": 2,
            "explanation": "正しい語順は「あしたは 【友だち(4)】 【と(1)】 ★【電車(3)】 【で(2)】 行きます」となります。★に入るのは 3「電車」です。"
        },
        {
            "qNum": 56,
            "title": "まいにち 練習して、日本語が ＿ ＿ ★ ＿ なりました。",
            "titleRuby": "まいにち <ruby>練習<rt>れんしゅう</rt></ruby>して、<ruby>日本語<rt>にほんご</rt></ruby>が ＿ ＿ ★ ＿ なりました。",
            "options": ["話せる", "上手に", "少し", "ように"],
            "order": [2, 1, 0, 3], # 3 少し, 2 上手に, 1 話せる, 4 ように -> ★ is position 3 (index 2) -> option 1 ("話せる")
            "correctIndex": 0,
            "explanation": "正しい語順は「まいにち 練習して、日本語が 【少し(3)】 【上手に(2)】 ★【話せる(1)】 【ように(4)】 なりました」となります。★に入るのは 1「話せる」です。"
        }
    ]

    for item in s2_m2:
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec2",
            "subsectionId": "s2_m2",
            "category": "文の組み立て",
            "qNum": item["qNum"],
            "title": item["title"],
            "titleRuby": item["titleRuby"],
            "questionText": "★に 入る ものは どれですか。いちばん いい ものを ひとつ えらんで ください。",
            "options": item["options"],
            "correctIndex": item["correctIndex"],
            "weight": 2.0,
            "explanation": item["explanation"]
        })

    # --- 文法 問題3: 文章の文法 (Q57〜Q61) ---
    passage_s2_m3 = """（キムさんの 作文）
私の 日本の 生活

私は 先月、韓国から 日本へ 来ました。いま 東京の アパートに 住んで います。
大学の 近くに 住んで いますから、まいにち 歩いて 大学へ [57] 。
大学の 授業は [58] むずかしいですが、とても おもしろいです。
先生や クラスメイトは みんな [59] 。
先週の 日曜日に、友だちと いっしょに 浅草へ 行きました。
浅草で おみやげを [60] 、おいしい うどんを 食べたり しました。
これから もっと いろいろな 所へ [61] 。"""

    passage_ruby_s2_m3 = """（キムさんの <ruby>作文<rt>さくぶん</rt></ruby>）<br>
<ruby>私<rt>わたし</rt></ruby>の <ruby>日本<rt>にほん</rt></ruby>の <ruby>生活<rt>せいかつ</rt></ruby><br><br>
<ruby>私<rt>わたし</rt></ruby>は <ruby>先月<rt>せんげつ</rt></ruby>、<ruby>韓国<rt>かんこく</rt></ruby>から <ruby>日本<rt>にほん</rt></ruby>へ <ruby>来<rt>き</rt></ruby>ました。いま <ruby>東京<rt>とうきょう</rt></ruby>の アパートに <ruby>住<rt>す</rt></ruby>んで います。<br>
<ruby>大学<rt>だいがく</rt></ruby>の <ruby>近<rt>ちか</rt></ruby>くに <ruby>住<rt>す</rt></ruby>んで いますから、まいにち <ruby>歩<rt>ある</rt></ruby>いて <ruby>大学<rt>だいがく</rt></ruby>へ <b>[57]</b> 。<br>
<ruby>大学<rt>だいがく</rt></ruby>の <ruby>授業<rt>じゅぎょう</rt></ruby>は <b>[58]</b> むずかしいですが、とても おもしろいです。<br>
<ruby>先生<rt>せんせい</rt></ruby>や クラスメイトは みんな <b>[59]</b> 。<br>
<ruby>先週<rt>せんしゅう</rt></ruby>の <ruby>日曜日<rt>にちようび</rt></ruby>に、<ruby>友<rt>とも</rt></ruby>だちと いっしょに <ruby>浅草<rt>あさくさ</rt></ruby>へ <ruby>行<rt>い</rt></ruby>きました。<br>
<ruby>浅草<rt>あさくさ</rt></ruby>で おみやげを <b>[60]</b> 、おいしい うどんを <ruby>食<rt>た</rt></ruby>べたり しました。<br>
これから もっと いろいろな <ruby>所<rt>ところ</rt></ruby>へ <b>[61]</b> 。"""

    s2_m3_items = [
        {
            "qNum": 57,
            "target": "[57]",
            "options": ["行きます", "行きました", "行きません", "行きたかったです"],
            "correctIndex": 0,
            "explanation": "「まいにち（毎日）」の習慣を表す文なので、現在形の「行きます」が正解です。"
        },
        {
            "qNum": 58,
            "target": "[58]",
            "options": ["あまり", "少し", "ぜんぜん", "いつも"],
            "correctIndex": 1,
            "explanation": "後半に「〜ですが、とても おもしろいです」と肯定的な逆接が続くため、程度の軽い「少し（すこし）」が最も自然です。「あまり」「ぜんぜん」は否定文（〜ない）とともに使います。"
        },
        {
            "qNum": 59,
            "target": "[59]",
            "options": ["親切です", "親切でした", "親切ではありません", "親切でしたか"],
            "correctIndex": 0,
            "explanation": "現在の普段の様子を述べているため、現在の肯定形「親切です」が正解です。"
        },
        {
            "qNum": 60,
            "target": "[60]",
            "options": ["買って", "買った", "買ったり", "買います"],
            "correctIndex": 2,
            "explanation": "後ろに「食べたり しました」と続いているため、「〜たり 〜たり する」の並列構文です。「買ったり」が正解です。"
        },
        {
            "qNum": 61,
            "target": "[61]",
            "options": ["行きたいです", "行きました", "行きません", "行くことです"],
            "correctIndex": 0,
            "explanation": "文頭に「これから（今後・未来）」があるため、将来の希望を表す「行きたいです」が正解です。"
        }
    ]

    for item in s2_m3_items:
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec2",
            "subsectionId": "s2_m3",
            "category": "文章の文法",
            "qNum": item["qNum"],
            "title": f"空欄 {item['target']} に 入る ものは どれですか。",
            "titleRuby": f"<ruby>空欄<rt>くうらん</rt></ruby> {item['target']} に <ruby>入<rt>はい</rt></ruby>る ものは どれですか。",
            "passage": passage_s2_m3,
            "passageRuby": passage_ruby_s2_m3,
            "questionText": f"{item['target']}に なにを いれますか。ぶんしょうの いみを かんがえて、いちばん いい ものを ひとつ えらんで ください。",
            "options": item["options"],
            "correctIndex": item["correctIndex"],
            "weight": 2.0,
            "explanation": item["explanation"]
        })

    # --- 読解 問題4: 内容理解（短文） (Q62〜Q64) ---
    p62 = """田中さんへ
きのう 借りた 本を 返したいです。きょうの 午後２時に 図書館の 前で 待って います。もし 来られない ときは、電話を して ください。
スミス"""
    p62_ruby = """<ruby>田中<rt>たなか</rt></ruby>さんへ<br>
きのう <ruby>借<rt>か</rt></ruby>りた <ruby>本<rt>ほん</rt></ruby>を <ruby>返<rt>かえ</rt></ruby>したいです。<ruby>今日<rt>きょう</rt></ruby>の <ruby>午後<rt>ごご</rt></ruby>２<ruby>時<rt>じ</rt></ruby>に <ruby>図書館<rt>としょかん</rt></ruby>の <ruby>前<rt>まえ</rt></ruby>で <ruby>待<rt>ま</rt></ruby>って います。もし <ruby>来<rt>こ</rt></ruby>られない ときは、<ruby>電話<rt>でんわ</rt></ruby>を して ください。<br>
スミス"""

    questions.append({
        "id": len(questions) + 1,
        "sectionId": "sec2",
        "subsectionId": "s2_m4",
        "category": "内容理解（短文）",
        "qNum": 62,
        "title": "スミスさんは どうして この メモを 書きましたか。",
        "titleRuby": "スミスさんは どうして この メモを <ruby>書<rt>か</rt></ruby>きましたか。",
        "passage": p62,
        "passageRuby": p62_ruby,
        "evidence": "きのう 借りた 本を 返したいです。",
        "questionText": "つぎの ぶんしょうを よんで、しつもんに こたえて ください。こたえは １・２・３・４から いちばん いい ものを ひとつ えらんで ください。",
        "options": [
            "本を 借りたいから",
            "本を 返したいから",
            "図書館へ 一緒に 行きたいから",
            "電話番号を 聞きたいから"
        ],
        "correctIndex": 1,
        "weight": 3.0,
        "explanation": "本文に「きのう 借りた 本を 返したいです」と書かれています。したがって、メモを書いた理由は 2「本を 返したいから」です。"
    })

    p63 = """４月１０日（日曜日）
朝 ９時に 起きて、部屋を そうじしました。昼ごはんは 近くの カフェで サンドイッチを 食べました。午後は 公園を １時間 さんぽして、夜は 家で テレビを 見ました。とても のんびりした 一日でした。"""
    p63_ruby = """４<ruby>月<rt>がつ</rt></ruby>１０<ruby>日<rt>にち</rt></ruby>（<ruby>日曜日<rt>にちようび</rt></ruby>）<br>
<ruby>朝<rt>あさ</rt></ruby> ９<ruby>時<rt>じ</rt></ruby>に <ruby>起<rt>お</rt></ruby>きて、<ruby>部屋<rt>へや</rt></ruby>を そうじしました。<ruby>昼<rt>ひる</rt></ruby>ごはんは <ruby>近<rt>ちか</rt></ruby>くの カフェで サンドイッチを <ruby>食<rt>た</rt></ruby>べました。<ruby>午後<rt>ごご</rt></ruby>は <ruby>公園<rt>こうえん</rt></ruby>を １<ruby>時間<rt>じかん</rt></ruby> さんぽして、<ruby>夜<rt>よる</rt></ruby>は <ruby>家<rt>いえ</rt></ruby>で テレビを <ruby>見<rt>み</rt></ruby>ました。とても のんびりした <ruby>一日<rt>いちにち</rt></ruby>でした。"""

    questions.append({
        "id": len(questions) + 1,
        "sectionId": "sec2",
        "subsectionId": "s2_m4",
        "category": "内容理解（短文）",
        "qNum": 63,
        "title": "山田さんは 午後 何を しましたか。",
        "titleRuby": "<ruby>山田<rt>やまだ</rt></ruby>さんは <ruby>午後<rt>ごご</rt></ruby> <ruby>何<rt>なに</rt></ruby>を しましたか。",
        "passage": p63,
        "passageRuby": p63_ruby,
        "evidence": "午後は 公園を １時間 さんぽして",
        "questionText": "つぎの ぶんしょうを よんで、しつもんに こたえて ください。こたえは １・２・３・４から いちばん いい ものを ひとつ えらんで ください。",
        "options": [
            "部屋の そうじを しました",
            "カフェで サンドイッチを 食べました",
            "公園を さんぽしました",
            "テレビを 見ました"
        ],
        "correctIndex": 2,
        "weight": 3.0,
        "explanation": "本文に「午後は 公園を １時間 さんぽして」とあります。そうじは朝、サンドイッチは昼、テレビは夜です。正解は 3「公園を さんぽしました」です。"
    })

    p64 = """お客様へ
いつも ご利用 いただき ありがとうございます。
来週の 火曜日（１５日）は、店の 工事の ため 休みます。
水曜日（１６日）から いつもどおり 朝１１時に 開きます。
どうぞ よろしく お願いします。
さくら食堂"""
    p64_ruby = """お<ruby>客<rt>きゃく</rt></ruby><ruby>様<rt>さま</rt></ruby>へ<br>
いつも ご<ruby>利用<rt>りよう</rt></ruby> いただき ありがとうございます。<br>
<ruby>来週<rt>らいしゅう</rt></ruby>の <ruby>火曜日<rt>かようび</rt></ruby>（１５<ruby>日<rt>にち</rt></ruby>）は、<ruby>店<rt>みせ</rt></ruby>の <ruby>工事<rt>こうじ</rt></ruby>の ため <ruby>休<rt>やす</rt></ruby>みます。<br>
<ruby>水曜日<rt>すいようび</rt></ruby>（１６<ruby>日<rt>にち</rt></ruby>）から いつもどおり <ruby>朝<rt>あさ</rt></ruby>１１<ruby>時<rt>じ</rt></ruby>に <ruby>開<rt>あ</rt></ruby>きます。<br>
どうぞ よろしく お<ruby>願<rt>ねが</rt></ruby>いします。<br>
さくら<ruby>食堂<rt>しょくどう</rt></ruby>"""

    questions.append({
        "id": len(questions) + 1,
        "sectionId": "sec2",
        "subsectionId": "s2_m4",
        "category": "内容理解（短文）",
        "qNum": 64,
        "title": "さくら食堂が 休みになる 日は いつですか。",
        "titleRuby": "さくら<ruby>食堂<rt>しょくどう</rt></ruby>が <ruby>休<rt>やす</rt></ruby>みになる <ruby>日<rt>ひ</rt></ruby>は いつですか。",
        "passage": p64,
        "passageRuby": p64_ruby,
        "evidence": "来週の 火曜日（１５日）は、店の 工事の ため 休みます。",
        "questionText": "つぎの ぶんしょうを よんで、しつもんに こたえて ください。こたえは １・２・３・４から いちばん いい ものを ひとつ えらんで ください。",
        "options": [
            "今週の 日曜日",
            "来週の 月曜日",
            "来週の 火曜日",
            "来週の 水曜日"
        ],
        "correctIndex": 2,
        "weight": 3.0,
        "explanation": "張り紙に「来週の 火曜日（１５日）は、店の 工事の ため 休みます」と明記されています。正解は 3「来週の 火曜日」です。"
    })

    # --- 読解 問題5: 内容理解（中文） (Q65〜Q66) ---
    p_chu = """私は 半年まえに この 町に 引っ越して きました。私の 部屋の 近くに 小さな 川が あります。川の よこには 長い 道が あって、きれいな 木や 花がたくさん あります。
私は 毎朝、大学へ 行く まえに、この 道を ３０分 さんぽします。朝は 空気が すずしくて、鳥の 声が 聞こえます。犬と いっしょに 歩いて いる 人や、走って いる 人に 会います。みんな「おはようございます」と あいさつを して くれます。
私は この 町に 来た とき、友だちが いなくて さびしかったです。でも、毎朝 この 川の 道を 歩いて、町の人と あいさつを して、この 町が とても 好きに なりました。"""

    p_chu_ruby = """<ruby>私<rt>わたし</rt></ruby>は <ruby>半年<rt>はんとし</rt></ruby>まえに この <ruby>町<rt>まち</rt></ruby>に <ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>して きました。<ruby>私<rt>わたし</rt></ruby>の <ruby>部屋<rt>へや</rt></ruby>の <ruby>近<rt>ちか</rt></ruby>くに <ruby>小<rt>ちい</rt></ruby>さな <ruby>川<rt>かわ</rt></ruby>が あります。<ruby>川<rt>かわ</rt></ruby>の よこには <ruby>長<rt>なが</rt></ruby>い <ruby>道<rt>みち</rt></ruby>が あって、きれいな <ruby>木<rt>き</rt></ruby>や <ruby>花<rt>はな</rt></ruby>がたくさん あります。<br>
<ruby>私<rt>わたし</rt></ruby>は <ruby>毎朝<rt>まいあさ</rt></ruby>、<ruby>大学<rt>だいがく</rt></ruby>へ <ruby>行<rt>い</rt></ruby>く まえに、この <ruby>道<rt>みち</rt></ruby>を ３０<ruby>分<rt>ぷん</rt></ruby> さんぽします。<ruby>朝<rt>あさ</rt></ruby>は <ruby>空気<rt>くうき</rt></ruby>が すずしくて、<ruby>鳥<rt>とり</rt></ruby>の <ruby>声<rt>こえ</rt></ruby>が <ruby>聞<rt>き</rt></ruby>こえます。<ruby>犬<rt>いぬ</rt></ruby>と いっしょに <ruby>歩<rt>ある</rt></ruby>いて いる <ruby>人<rt>ひと</rt></ruby>や、<ruby>走<rt>はし</rt></ruby>って いる <ruby>人<rt>ひと</rt></ruby>に <ruby>会<rt>あ</rt></ruby>います。みんな「おはようございます」と あいさつを して くれます。<br>
<ruby>私<rt>わたし</rt></ruby>は この <ruby>町<rt>まち</rt></ruby>に <ruby>来<rt>き</rt></ruby>た とき、<ruby>友<rt>とも</rt></ruby>だちが いなくて さびしかったです。でも、<ruby>毎朝<rt>まいあさ</rt></ruby> この <ruby>川<rt>かわ</rt></ruby>の <ruby>道<rt>みち</rt></ruby>を <ruby>歩<rt>ある</rt></ruby>いて、<ruby>町<rt>まち</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>と あいさつを して、この <ruby>町<rt>まち</rt></ruby>が とても <ruby>好<rt>す</rt></ruby>きに なりました。"""

    questions.append({
        "id": len(questions) + 1,
        "sectionId": "sec2",
        "subsectionId": "s2_m5",
        "category": "内容理解（中文）",
        "qNum": 65,
        "title": "筆者は 毎朝 川の 道で 何を しますか。",
        "titleRuby": "<ruby>筆者<rt>ひっしゃ</rt></ruby>は <ruby>毎朝<rt>まいあさ</rt></ruby> <ruby>川<rt>かわ</rt></ruby>の <ruby>道<rt>みち</rt></ruby>で <ruby>何<rt>なに</rt></ruby>を しますか。",
        "passage": p_chu,
        "passageRuby": p_chu_ruby,
        "evidence": "私は 毎朝、大学へ 行く まえに、この 道を ３０分 さんぽします。",
        "questionText": "つぎの ぶんしょうを よんで、しつもんに こたえて ください。こたえは １・２・３・４から いちばん いい ものを ひとつ えらんで ください。",
        "options": [
            "犬と あそびます",
            "３０分 さんぽします",
            "走って 大学へ 行きます",
            "友だちを 待ちます"
        ],
        "correctIndex": 1,
        "weight": 3.5,
        "explanation": "第2段落に「私は 毎朝、大学へ 行く まえに、この 道を ３０分 さんぽします」と明確に書かれています。正解は 2「３０分 さんぽします」です。"
    })

    questions.append({
        "id": len(questions) + 1,
        "sectionId": "sec2",
        "subsectionId": "s2_m5",
        "category": "内容理解（中文）",
        "qNum": 66,
        "title": "筆者は どうして この 町が 好きに なりましたか。",
        "titleRuby": "<ruby>筆者<rt>ひっしゃ</rt></ruby>は どうして この <ruby>町<rt>まち</rt></ruby>が <ruby>好<rt>す</rt></ruby>きに なりましたか。",
        "passage": p_chu,
        "passageRuby": p_chu_ruby,
        "evidence": "毎朝 この 川の 道を 歩いて、町の人と あいさつを して、この 町が とても 好きに なりました。",
        "questionText": "つぎの ぶんしょうを よんで、しつもんに こたえて ください。こたえは １・２・３・４から いちばん いい ものを ひとつ えらんで ください。",
        "options": [
            "新しい 犬を もらったから",
            "大学の 友だちが 引っ越して きたから",
            "朝の さんぽで 町の人と あいさつを かわすように なったから",
            "自分の 部屋が 広くて きれいだから"
        ],
        "correctIndex": 2,
        "weight": 3.5,
        "explanation": "第3段落に「毎朝 この 川の 道を 歩いて、町の人と あいさつを して、この 町が とても 好きに なりました」とあります。正解は 3「朝の さんぽで 町の人と あいさつを かわすように なったから」です。"
    })

    # --- 読解 問題6: 情報検索 (Q67) ---
    p_info = """【みどり市民センター】 日本の りょうり 教室
日本の かてい料理を いっしょに 作りませんか。

・日時： １１月２０日（日） 午後１時〜３時
・場所： みどり市民センター ２階 調理室
・作るもの： 肉じゃが、みそ汁
・参加費： １,０００円（材料代を ふくみます）
・定員： １５人（先着順）
・持ち物： エプロン、ハンドタオル
※ 申し込みは １１月１５日までに 電話か メールで お願いします。
電話：03-1234-5678"""

    p_info_ruby = """【みどり<ruby>市民<rt>しみん</rt></ruby>センター】 <ruby>日本<rt>にほん</rt></ruby>の りょうり <ruby>教室<rt>きょうしつ</rt></ruby><br>
<ruby>日本<rt>にほん</rt></ruby>の かてい<ruby>料理<rt>りょうり</rt></ruby>を いっしょに <ruby>作<rt>つく</rt></ruby>りませんか。<br><br>
・<ruby>日時<rt>にちじ</rt></ruby>： １１<ruby>月<rt>がつ</rt></ruby>２０<ruby>日<rt>にち</rt></ruby>（<ruby>日<rt>にち</rt></ruby>） <ruby>午後<rt>ごご</rt></ruby>１<ruby>時<rt>じ</rt></ruby>〜３<ruby>時<rt>じ</rt></ruby><br>
・<ruby>場所<rt>ばしょ</rt></ruby>： みどり<ruby>市民<rt>しみん</rt></ruby>センター ２<ruby>階<rt>かい</rt></ruby> <ruby>調理室<rt>ちょうりしつ</rt></ruby><br>
・<ruby>作<rt>つく</rt></ruby>るもの： <ruby>肉<rt>にく</rt></ruby>じゃが、みそ<ruby>汁<rt>しる</rt></ruby><br>
・<ruby>参加費<rt>さんかひ</rt></ruby>： １,０００<ruby>円<rt>えん</rt></ruby>（<ruby>材料代<rt>ざいりょうだい</rt></ruby>を ふくみます）<br>
・<ruby>定員<rt>ていいん</rt></ruby>： １５<ruby>人<rt>にん</rt></ruby>（<ruby>先着順<rt>せんちゃくじゅん</rt></ruby>）<br>
・<ruby>持<rt>も</rt></ruby>ち<ruby>物<rt>もの</rt></ruby>： <b>エプロン、ハンドタオル</b><br>
※ <ruby>申<rt>もう</rt></ruby>し<ruby>込<rt>こ</rt></ruby>みは １１<ruby>月<rt>がつ</rt></ruby>１５<ruby>日<rt>にち</rt></ruby>までに <ruby>電話<rt>でんわ</rt></ruby>か メールで お<ruby>願<rt>ねが</rt></ruby>いします。<br>
<ruby>電話<rt>でんわ</rt></ruby>：03-1234-5678"""

    questions.append({
        "id": len(questions) + 1,
        "sectionId": "sec2",
        "subsectionId": "s2_m6",
        "category": "情報検索",
        "qNum": 67,
        "title": "リンさんは この 料理教室に 参加したいです。何を持って 行かなければ なりませんか。",
        "titleRuby": "リンさんは この <ruby>料理<rt>りょうり</rt></ruby><ruby>教室<rt>きょうしつ</rt></ruby>に <ruby>参加<rt>さんか</rt></ruby>したいです。<ruby>何<rt>なに</rt></ruby>を<ruby>持<rt>も</rt></ruby>って <ruby>行<rt>い</rt></ruby>かなければ なりませんか。",
        "passage": p_info,
        "passageRuby": p_info_ruby,
        "evidence": "持ち物： エプロン、ハンドタオル",
        "questionText": "つぎの あんないを みて、しつもんに こたえて ください。こたえは １・２・３・４から いちばん いい ものを ひとつ えらんで ください。",
        "options": [
            "肉と 野菜",
            "エプロンと タオル",
            "料理の 本",
            "包丁と まな板"
        ],
        "correctIndex": 1,
        "weight": 4.0,
        "explanation": "案内チラシの「持ち物」の欄に「エプロン、ハンドタオル」と明記されています。材料代は参加費に含まれているため肉や野菜を持っていく必要はありません。正解は 2「エプロンと タオル」です。"
    })

    # -------------------------------------------------------------
    # SECTION 3: 聴解 (Q68〜Q91)
    # -------------------------------------------------------------

    # --- 聴解 問題1: 課題理解 (Q68〜Q74) ---
    s3_m1 = [
        {
            "qNum": 68,
            "title": "男の人は 黒い ペンを 何本 買いますか。",
            "titleRuby": "<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>は <ruby>黒<rt>くろ</rt></ruby>い ペンを <ruby>何本<rt>なんぼん</rt></ruby> <ruby>買<rt>か</rt></ruby>いますか。",
            "script": """女の人：いらっしゃいませ。
男の人：すみません、この 黒い ペンを ２本と、赤い ペンを １本 ください。
女の人：はい、黒が ２本と、赤が １本ですね。
男の人：あ、すみません。黒い ペンは ３本に して ください。
女の人：わかりました。黒が ３本と、赤が １本ですね。ぜんぶで ４本です。
男の人：はい、お願いします。""",
            "scriptRuby": """<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：いらっしゃいませ。<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：すみません、この <ruby>黒<rt>くろ</rt></ruby>い ペンを ２<ruby>本<rt>ほん</rt></ruby>と、<ruby>赤<rt>あか</rt></ruby>い ペンを １<ruby>本<rt>ぽん</rt></ruby> ください。<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：はい、<ruby>黒<rt>くろ</rt></ruby>が ２<ruby>本<rt>ほん</rt></ruby>と、<ruby>赤<rt>あか</rt></ruby>が １<ruby>本<rt>ぽん</rt></ruby>ですね。<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：あ、すみません。<ruby>黒<rt>くろ</rt></ruby>い ペンは ３<ruby>本<rt>ぼん</rt></ruby>に して ください。<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：わかりました。<ruby>黒<rt>くろ</rt></ruby>が ３<ruby>本<rt>ぼん</rt></ruby>と、<ruby>赤<rt>あか</rt></ruby>が １<ruby>本<rt>ぽん</rt></ruby>ですね。ぜんぶで ４<ruby>本<rt>ほん</rt></ruby>です。<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：はい、お<ruby>願<rt>ねが</rt></ruby>いします。""",
            "prompt1": "問題１。１番。男の人と女の人が話しています。男の人は黒いペンを何本買いますか。",
            "prompt2": "男の人は黒いペンを何本買いますか。",
            "options": ["１本", "２本", "３本", "４本"],
            "correctIndex": 2,
            "dialogueTracks": [
                ("いらっしゃいませ。", FEMALE_VOICE, 400),
                ("すみません、この黒いペンを2本と、赤いペンを1本ください。", MALE_VOICE, 400),
                ("はい、黒が2本と、赤が1本ですね。", FEMALE_VOICE, 400),
                ("あ、すみません。黒いペンは3本にしてください。", MALE_VOICE, 400),
                ("わかりました。黒が3本と、赤が1本ですね。ぜんぶで4本です。", FEMALE_VOICE, 400),
                ("はい、お願いします。", MALE_VOICE, 600)
            ],
            "explanation": "男の人は最初「黒いペンを2本」と言いましたが、その後「黒いペンは3本にしてください」と変更しました。したがって黒いペンは 3「３本」買います。"
        },
        {
            "qNum": 69,
            "title": "学生は あした 何を 持って 来なければ なりませんか。",
            "titleRuby": "<ruby>学生<rt>がくせい</rt></ruby>は あした <ruby>何<rt>なに</rt></ruby>を <ruby>持<rt>も</rt></ruby>って <ruby>来<rt>こ</rt></ruby>なければ なりませんか。",
            "script": """先生：みなさん、あしたの 授業について 話します。教科書と ノートは いつもどおり 持って 来て ください。
学生：先生、辞書も 持って 来ますか。
先生：いいえ、辞書は 教室に ありますから、いりません。でも、宿題の 作文を わすれないで 持って 来て くださいね。
学生：はい、わかりました。""",
            "scriptRuby": """<ruby>先生<rt>せんせい</rt></ruby>：みなさん、あしたの <ruby>授業<rt>じゅぎょう</rt></ruby>について <ruby>話<rt>はな</rt></ruby>します。<ruby>教科書<rt>きょうかしょ</rt></ruby>と ノートは いつもどおり <ruby>持<rt>も</rt></ruby>って <ruby>来<rt>き</rt></ruby>て ください。<br>
<ruby>学生<rt>がくせい</rt></ruby>：<ruby>先生<rt>せんせい</rt></ruby>、<ruby>辞書<rt>じしょ</rt></ruby>も <ruby>持<rt>も</rt></ruby>って <ruby>来<rt>き</rt></ruby>ますか。<br>
<ruby>先生<rt>せんせい</rt></ruby>：いいえ、<ruby>辞書<rt>じしょ</rt></ruby>は <ruby>教室<rt>きょうしつ</rt></ruby>に ありますから、いりません。でも、<ruby>宿題<rt>しゅくだい</rt></ruby>の <ruby>作文<rt>さくぶん</rt></ruby>を わすれないで <ruby>持<rt>も</rt></ruby>って <ruby>来<rt>き</rt></ruby>て くださいね。<br>
<ruby>学生<rt>がくせい</rt></ruby>：はい、わかりました。""",
            "prompt1": "２番。先生と学生が話しています。学生はあした何を持ってこなければなりませんか。",
            "prompt2": "学生はあした何を持ってこなければなりませんか。",
            "options": ["辞書", "作文", "写真", "パソコン"],
            "correctIndex": 1,
            "dialogueTracks": [
                ("みなさん、あしたの授業について話します。教科書とノートはいつもどおり持って来てください。", FEMALE_VOICE, 400),
                ("先生、辞書も持って来ますか。", MALE_VOICE, 400),
                ("いいえ、辞書は教室にありますから、いりません。でも、宿題の作文をわすれないで持って来てくださいね。", FEMALE_VOICE, 400),
                ("はい、わかりました。", MALE_VOICE, 600)
            ],
            "explanation": "辞書は「いりません」と言われ、宿題の「作文」を忘れないで持ってくるよう指示されています。正解は 2「作文」です。"
        },
        {
            "qNum": 70,
            "title": "二人は 何時に 会いますか。",
            "titleRuby": "<ruby>二人<rt>ふたり</rt></ruby>は <ruby>何時<rt>なんじ</rt></ruby>に <ruby>会<rt>あ</rt></ruby>いますか。",
            "script": """男の人：もしもし、あしたの 映画だけど、何時に 会おうか。
女の人：映画は １１時からだから、１０時半は どう？
男の人：うーん、１０時半は ちょっと 早いかな。１０時４５分は どう？
女の人：チケットを 買わなきゃ いけないから、やっぱり １０時半に しようよ。
男の人：そうか。じゃあ、１０時半に 駅の 改札で 会おう。""",
            "scriptRuby": """<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：もしもし、あしたの <ruby>映画<rt>えいが</rt></ruby>だけど、<ruby>何時<rt>なんじ</rt></ruby>に <ruby>会<rt>あ</rt></ruby>おうか。<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：<ruby>映画<rt>えいが</rt></ruby>は １１<ruby>時<rt>じ</rt></ruby>からだから、１０<ruby>時<rt>じ</rt></ruby><ruby>半<rt>はん</rt></ruby>は どう？<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：うーん、１０<ruby>時<rt>じ</rt></ruby><ruby>半<rt>はん</rt></ruby>は ちょっと <ruby>早<rt>はや</rt></ruby>いかな。１０<ruby>時<rt>じ</rt></ruby>４５<ruby>分<rt>ふん</rt></ruby>は どう？<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：チケットを <ruby>買<rt>か</rt></ruby>わなきゃ いけないから、やっぱり １０<ruby>時<rt>じ</rt></ruby><ruby>半<rt>はん</rt></ruby>に しようよ。<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：そうか。じゃあ、１０<ruby>時<rt>じ</rt></ruby><ruby>半<rt>はん</rt></ruby>に <ruby>駅<rt>えき</rt></ruby>の <ruby>改札<rt>かいさつ</rt></ruby>で <ruby>会<rt>あ</rt></ruby>おう。""",
            "prompt1": "三番。男の人と女の人が電話で話しています。二人はあした何時に会いますか。",
            "prompt2": "二人はあした何時に会いますか。",
            "options": ["１０時", "１０時半", "１０時４５分", "１１時"],
            "correctIndex": 1,
            "dialogueTracks": [
                ("もしもし、あしたの映画だけど、何時に会おうか。", MALE_VOICE, 400),
                ("映画は11時からだから、10時半はどう？", FEMALE_VOICE, 400),
                ("うーん、10時半はちょっと早いかな。10時45分はどう？", MALE_VOICE, 400),
                ("チケットを買わなきゃいけないから、やっぱり10時半にしようよ。", FEMALE_VOICE, 400),
                ("そうか。じゃあ、10時半に駅の改札で会おう。", MALE_VOICE, 600)
            ],
            "explanation": "男の人が10時45分を提案しましたが、チケットを買うため「やっぱり10時半にしよう」となり、最終的に10時半に決定しました。正解は 2「１０時半」です。"
        },
        {
            "qNum": 71,
            "title": "病院は どこに ありますか。",
            "titleRuby": "<ruby>病院<rt>びょういん</rt></ruby>は どこに ありますか。",
            "script": """女の人：すみません、この 近くに 病院は ありますか。
男の人：ええ、ありますよ。この 道を まっすぐ 行って、２つめの かどを 右に まがって ください。
女の人：２つめの かどを 右ですね。
男の人：はい。そうすると、左側に 銀行が あります。その となりが 病院ですよ。
女の人：銀行の となりですね。ありがとうございました。""",
            "scriptRuby": """<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：すみません、この <ruby>近<rt>ちか</rt></ruby>くに <ruby>病院<rt>びょういん</rt></ruby>は ありますか。<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：ええ、ありますよ。この <ruby>道<rt>みち</rt></ruby>を まっすぐ <ruby>行<rt>い</rt></ruby>って、２つめの かどを <ruby>右<rt>みぎ</rt></ruby>に まがって ください。<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：２つめの かどを <ruby>右<rt>みぎ</rt></ruby>ですね。<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：はい。そうすると、<ruby>左側<rt>ひだりがわ</rt></ruby>に <ruby>銀行<rt>ぎんこう</rt></ruby>が あります。その となりが <ruby>病院<rt>びょういん</rt></ruby>ですよ。<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：<ruby>銀行<rt>ぎんこう</rt></ruby>の となりですね。ありがとうございました。""",
            "prompt1": "四番。女の人と男の人が話しています。病院はどこにありますか。",
            "prompt2": "病院はどこにありますか。",
            "options": ["１つめのかどの右", "銀行のとなり", "銀行のむかい", "駅のなか"],
            "correctIndex": 1,
            "dialogueTracks": [
                ("すみません、この近くに病院はありますか。", FEMALE_VOICE, 400),
                ("ええ、ありますよ。この道をまっすぐ行って、2つめのかどを右にまがってください。", MALE_VOICE, 400),
                ("2つめのかどを右ですね。", FEMALE_VOICE, 400),
                ("はい。そうすると、左側に銀行があります。そのとなりが病院ですよ。", MALE_VOICE, 400),
                ("銀行のとなりですね。ありがとうございました。", FEMALE_VOICE, 600)
            ],
            "explanation": "男の人が「左側に銀行があります。そのとなりが病院ですよ」と説明しています。正解は 2「銀行のとなり」です。"
        },
        {
            "qNum": 72,
            "title": "女の人は このあと まず 何を しますか。",
            "titleRuby": "<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>は このあと まず <ruby>何<rt>なに</rt></ruby>を しますか。",
            "script": """男の人：佐藤さん、午後の 会議の 準備、手伝って くれる？
女の人：はい、何を しましょうか。
男の人：まず、この 会議の 資料を １０部 コピーして ほしいんだ。
女の人：わかりました。そのあと 会議室の 机を ならべましょうか。
男の人：うん、それは コピーが 終わったあとで いっしょに やろう。
女の人：はい、じゃあ すぐ やってきます。""",
            "scriptRuby": """<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：<ruby>佐藤<rt>さとう</rt></ruby>さん、<ruby>午後<rt>ごご</rt></ruby>の <ruby>会議<rt>かいぎ</rt></ruby>の <ruby>準備<rt>じゅんび</rt></ruby>、<ruby>手伝<rt>てつだ</rt></ruby>って くれる？<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：はい、<ruby>何<rt>なに</rt></ruby>を しましょうか。<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：まず、この <ruby>会議<rt>かいぎ</rt></ruby>の <ruby>資料<rt>しりょう</rt></ruby>を １０<ruby>部<rt>ぶ</rt></ruby> コピーして ほしいんだ。<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：わかりました。そのあと <ruby>会議室<rt>かいぎしつ</rt></ruby>の <ruby>机<rt>つくえ</rt></ruby>を ならべましょうか。<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：うん、それは コピーが <ruby>終<rt>お</rt></ruby>わったあとで いっしょに やろう。<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：はい、じゃあ すぐ やってきます。""",
            "prompt1": "五番。男の人と女の人が会社で話しています。女の人はこのあとまず何をしますか。",
            "prompt2": "女の人はこのあとまず何をしますか。",
            "options": ["会議室へ行く", "資料をコピーする", "机をならべる", "お茶を入れる"],
            "correctIndex": 1,
            "dialogueTracks": [
                ("佐藤さん、午後の会議の準備、手伝ってくれる？", MALE_VOICE, 400),
                ("はい、何をしましょうか。", FEMALE_VOICE, 400),
                ("まず、この会議の資料を10部コピーしてほしいんだ。", MALE_VOICE, 400),
                ("わかりました。そのあと会議室の机をならべましょうか。", FEMALE_VOICE, 400),
                ("うん、それはコピーが終わったあとでいっしょにやろう。", MALE_VOICE, 400),
                ("はい、じゃあすぐやってきます。", FEMALE_VOICE, 600)
            ],
            "explanation": "男の人が「まず、この 会議の 資料を １０部 コピーして ほしいんだ」と言い、女の人は「すぐやってきます」と答えています。机を並べるのはコピーの後です。正解は 2「資料をコピーする」です。"
        },
        {
            "qNum": 73,
            "title": "男の人は カバンに 何を 入れますか。",
            "titleRuby": "<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>は カバンに <ruby>何<rt>なに</rt></ruby>を <ruby>入<rt>い</rt></ruby>れますか。",
            "script": """女の人：これから 出かけるの？
男の人：うん、駅前の 図書館へ 行ってくるよ。
女の人：天気予報で 午後から 雨が ふるって 言ってたよ。折りたたみの 傘を 持って 行ったら？
男の人：え、本当？ じゃあ、カバンに 入れて おくよ。上着は いるかな？
女の人：きょうは あたたかいから、上着は いらないと 思うよ。
男の人：わかった。ありがとう。""",
            "scriptRuby": """<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：これから <ruby>出<rt>で</rt></ruby>かけるの？<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：うん、<ruby>駅前<rt>えきまえ</rt></ruby>の <ruby>図書館<rt>としょかん</rt></ruby>へ <ruby>行<rt>い</rt></ruby>ってくるよ。<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：<ruby>天気予報<rt>てんきよほう</rt></ruby>で <ruby>午後<rt>ごご</rt></ruby>から <ruby>雨<rt>あめ</rt></ruby>が ふるって <ruby>言<rt>い</rt></ruby>ってたよ。<ruby>折<rt>お</rt></ruby>りたたみの <ruby>傘<rt>かさ</rt></ruby>を <ruby>持<rt>も</rt></ruby>って <ruby>行<rt>い</rt></ruby>ったら？<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：え、<ruby>本当<rt>ほんとう</rt></ruby>？ じゃあ、カバンに <ruby>入<rt>い</rt></ruby>れて おくよ。<ruby>上着<rt>うわぎ</rt></ruby>は いるかな？<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：きょうは あたたかいから、<ruby>上着<rt>うわぎ</rt></ruby>は いらないと <ruby>思<rt>おも</rt></ruby>うよ。<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：わかった。ありがとう。""",
            "prompt1": "六番。男の人と女の人が話しています。男の人はカバンに何を入れますか。",
            "prompt2": "男の人はカバンに何を入れますか。",
            "options": ["上着", "傘", "帽子", "辞書"],
            "correctIndex": 1,
            "dialogueTracks": [
                ("これから出かけるの？", FEMALE_VOICE, 400),
                ("うん、駅前の図書館へ行ってくるよ。", MALE_VOICE, 400),
                ("天気予報で午後から雨がふるって言ってたよ。折りたたみの傘を持って行ったら？", FEMALE_VOICE, 400),
                ("え、本当？ じゃあ、カバンに入れておくよ。上着はいるかな？", MALE_VOICE, 400),
                ("きょうはあたたかいから、上着はいらないと思うよ。", FEMALE_VOICE, 400),
                ("わかった。ありがとう。", MALE_VOICE, 600)
            ],
            "explanation": "午後から雨が降るため傘を持っていくよう勧められ、男の人は「カバンに入れておくよ」と答えています。上着は「いらない」と言われています。正解は 2「傘」です。"
        },
        {
            "qNum": 74,
            "title": "男の人は これから テーブルの上に 何を 置きますか。",
            "titleRuby": "<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>は これから テーブルの<ruby>上<rt>うえ</rt></ruby>に <ruby>何<rt>なに</rt></ruby>を <ruby>置<rt>お</rt></ruby>きますか。",
            "script": """女の人：もうすぐ ごはんが できるから、テーブルの 上を 準備して くれる？
男の人：うん、何を 置けば いい？
女の人：食器棚から お皿と おはしを 出して、並べて くれる？
男の人：お皿と おはしね。コップも 置く？
女の人：お茶は 私が あとで 入れるから、コップは まだ いいよ。
男の人：わかった。""",
            "scriptRuby": """<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：もうすぐ ごはんが できるから、テーブルの <ruby>上<rt>うえ</rt></ruby>を <ruby>準備<rt>じゅんび</rt></ruby>して くれる？<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：うん、<ruby>何<rt>なに</rt></ruby>を <ruby>置<rt>お</rt></ruby>けば いい？<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：<ruby>食器棚<rt>しょっきだな</rt></ruby>から お<ruby>皿<rt>さら</rt></ruby>と おはしを <ruby>出<rt>だ</rt></ruby>して、<ruby>並<rt>なら</rt></ruby>べて くれる？<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：お<ruby>皿<rt>さら</rt></ruby>と おはしね。コップも <ruby>置<rt>お</rt></ruby>く？<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：お<ruby>茶<rt>ちゃ</rt></ruby>は <ruby>私<rt>わたし</rt></ruby>が あとで <ruby>入<rt>い</rt></ruby>れるから、コップは まだ いいよ。<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：わかった。""",
            "prompt1": "七番。男の人と女の人が家で話しています。男の人はこれからテーブルの上に何を置きますか。",
            "prompt2": "男の人はこれからテーブルの上に何を置きますか。",
            "options": ["コップ", "お皿とおはし", "お茶", "ごはん"],
            "correctIndex": 1,
            "dialogueTracks": [
                ("もうすぐごはんができるから、テーブルの上を準備してくれる？", FEMALE_VOICE, 400),
                ("うん、何を置けばいい？", MALE_VOICE, 400),
                ("食器棚からお皿とおはしを出して、並べてくれる？", FEMALE_VOICE, 400),
                ("お皿とおはしね。コップも置く？", MALE_VOICE, 400),
                ("お茶は私があとで入れるから、コップはまだいいよ。", FEMALE_VOICE, 400),
                ("わかった。", MALE_VOICE, 600)
            ],
            "explanation": "女の人から「お皿とおはしを出して、並べてくれる？」と頼まれ、コップは「まだいいよ」と言われています。正解は 2「お皿とおはし」です。"
        }
    ]

    for item in s3_m1:
        audio_filename = f"n5_m01_q{item['qNum']:02d}.mp3"
        # Assemble audio tracks
        tracks = [
            (item["prompt1"], NARRATOR_VOICE, 800)
        ] + item["dialogueTracks"] + [
            (item["prompt2"], NARRATOR_VOICE, 500)
        ]
        
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec3",
            "subsectionId": "s3_m1",
            "category": "課題理解",
            "qNum": item["qNum"],
            "title": item["title"],
            "titleRuby": item["titleRuby"],
            "script": item["script"],
            "scriptRuby": item["scriptRuby"],
            "audioUrl": f"audio/mock_n5/{audio_filename}",
            "questionText": "まず しつもんを きいて ください。それから はなしを きいて、１から４の なかから、いちばん いい ものを ひとつ えらんで ください。",
            "options": item["options"],
            "correctIndex": item["correctIndex"],
            "weight": 2.5,
            "explanation": item["explanation"],
            "tracks": tracks
        })

    # --- 聴解 問題2: ポイント理解 (Q75〜Q80) ---
    s3_m2 = [
        {
            "qNum": 75,
            "title": "男の人は どうして きのう パーティーに 行きませんでしたか。",
            "titleRuby": "<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>は どうして きのう パーティーに <ruby>行<rt>い</rt></ruby>きませんでしたか。",
            "script": """女の人：田中さん、きのうの パーティー、どうして 来なかったの？
男の人：行きたかったんだけど、朝から 熱が 出ちゃってね。
女の人：え、熱？ 大丈夫だった？
男の人：うん、薬を 飲んで 一日中 寝ていたから、もう すっかり よくなったよ。
女の人：よかった。みんな 心配して いたよ。""",
            "scriptRuby": """<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：<ruby>田中<rt>たなか</rt></ruby>さん、きのうの パーティー、どうして <ruby>来<rt>こ</rt></ruby>なかったの？<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：<ruby>行<rt>い</rt></ruby>きたかったんだけど、<ruby>朝<rt>あさ</rt></ruby>から <ruby>熱<rt>ねつ</rt></ruby>が <ruby>出<rt>で</rt></ruby>ちゃってね。<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：え、<ruby>熱<rt>ねつ</rt></ruby>？ <ruby>大丈夫<rt>だいじょうぶ</rt></ruby>だった？<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：うん、<ruby>薬<rt>くすり</rt></ruby>を <ruby>飲<rt>の</rt></ruby>んで <ruby>一日中<rt>いちにちじゅう</rt></ruby> <ruby>寝<rt>ね</rt></ruby>ていたから、もう すっかり よくなったよ。<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：よかった。みんな <ruby>心配<rt>しんぱい</rt></ruby>して いたよ。""",
            "prompt1": "問題二。一番。男の人と女の人が話しています。男の人はどうしてきのうパーティーに行きませんでしたか。",
            "prompt2": "男の人はどうしてきのうパーティーに行きませんでしたか。",
            "options": ["忙しかったから", "熱が出たから", "忘れていたから", "雨がふったから"],
            "correctIndex": 1,
            "dialogueTracks": [
                ("田中さん、きのうのパーティー、どうして来なかったの？", FEMALE_VOICE, 400),
                ("行きたかったんだけど、朝から熱が出ちゃってね。", MALE_VOICE, 400),
                ("え、熱？ 大丈夫だった？", FEMALE_VOICE, 400),
                ("うん、薬を飲んで一日中寝ていたから、もうすっかりよくなったよ。", MALE_VOICE, 400),
                ("よかった。みんな心配していたよ。", FEMALE_VOICE, 600)
            ],
            "explanation": "男の人は「朝から 熱が 出ちゃってね」と理由を言っています。正解は 2「熱が出たから」です。"
        },
        {
            "qNum": 76,
            "title": "男の人は どうして 電車で 行くのが 好きですか。",
            "titleRuby": "<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>は どうして <ruby>電車<rt>でんしゃ</rt></ruby>で <ruby>行<rt>い</rt></ruby>くのが <ruby>好<rt>す</rt></ruby>きですか。",
            "script": """女の人：山田さんは いつも 電車で 通勤して いるんですね。車は 使わないんですか。
男の人：車も 持って いますが、電車の ほうが 好きなんです。
女の人：どうしてですか。
男の人：電車の中だと、ゆっくり 本が 読めますからね。毎日の 楽しみなんです。
女の人：なるほど、読書の 時間に なるんですね。""",
            "scriptRuby": """<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：<ruby>山田<rt>やまだ</rt></ruby>さんは いつも <ruby>電車<rt>でんしゃ</rt></ruby>で <ruby>通勤<rt>つうきん</rt></ruby>して いるんですね。<ruby>車<rt>くるま</rt></ruby>は <ruby>使<rt>つか</rt></ruby>わないんですか。<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：<ruby>車<rt>くるま</rt></ruby>も <ruby>持<rt>も</rt></ruby>って いますが、<ruby>電車<rt>でんしゃ</rt></ruby>の ほうが <ruby>好<rt>す</rt></ruby>きなんです。<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：どうしてですか。<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：<ruby>電車<rt>でんしゃ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>だと、ゆっくり <ruby>本<rt>ほん</rt></ruby>が <ruby>読<rt>よ</rt></ruby>めますからね。<ruby>毎日<rt>まいにち</rt></ruby>の <ruby>楽<rt>たの</rt></ruby>しみなんです。<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：なるほど、<ruby>読書<rt>どくしょ</rt></ruby>の <ruby>時間<rt>じかん</rt></ruby>に なるんですね。""",
            "prompt1": "二番。女の人と男の人が話しています。男の人はどうして電車で行くのが好きですか。",
            "prompt2": "男の人はどうして電車で行くのが好きですか。",
            "options": ["切符が安いから", "運転が好きだから", "本が読めるから", "友達に会えるから"],
            "correctIndex": 2,
            "dialogueTracks": [
                ("山田さんはいつも電車で通勤しているんですね。車は使わないんですか。", FEMALE_VOICE, 400),
                ("車も持っていますが、電車のほうが好きなんです。", MALE_VOICE, 400),
                ("どうしてですか。", FEMALE_VOICE, 400),
                ("電車の中だと、ゆっくり本が読めますからね。毎日の楽しみなんです。", MALE_VOICE, 400),
                ("なるほど、読書の時間になるんですね。", FEMALE_VOICE, 600)
            ],
            "explanation": "男の人は「電車の中だと、ゆっくり 本が 読めますからね」と理由を説明しています。正解は 3「本が読めるから」です。"
        },
        {
            "qNum": 77,
            "title": "女の人は どうして その 靴を 買いませんでしたか。",
            "titleRuby": "<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>は どうして その <ruby>靴<rt>くつ</rt></ruby>を <ruby>買<rt>か</rt></ruby>いませんでしたか。",
            "script": """男の人：その 靴、デザインが とても いいね。買ったの？
女の人：ううん、買わなかったの。
男の人：え、どうして？ 値段が 高かったの？
女の人：ううん、値段は 安かったんだけど、履いてみたら サイズが ちょっと 小さくて、足が 痛かったの。
男の人：そうか、サイズが 合わなかったんだね。""",
            "scriptRuby": """<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：その <ruby>靴<rt>くつ</rt></ruby>、デザインが とても いいね。<ruby>買<rt>か</rt></ruby>ったの？<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：ううん、<ruby>買<rt>か</rt></ruby>わなかったの。<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：え、どうして？ <ruby>値段<rt>ねだん</rt></ruby>が <ruby>高<rt>たか</rt></ruby>かったの？<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：ううん、<ruby>値段<rt>ねだん</rt></ruby>は <ruby>安<rt>やす</rt></ruby>かったんだけど、<ruby>履<rt>は</rt></ruby>いてみたら サイズが ちょっと <ruby>小<rt>ちい</rt></ruby>さくて、<ruby>足<rt>あし</rt></ruby>が <ruby>痛<rt>いた</rt></ruby>かったの。<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：そうか、サイズが <ruby>合<rt>あ</rt></ruby>わなかったんだね。""",
            "prompt1": "三番。男の人と女の人が話しています。女の人はどうしてその靴を買いませんでしたか。",
            "prompt2": "女の人はどうしてその靴を買いませんでしたか。",
            "options": ["高かったから", "色が嫌いだったから", "サイズが小さかったから", "店になかったから"],
            "correctIndex": 2,
            "dialogueTracks": [
                ("その靴、デザインがとてもいいね。買ったの？", MALE_VOICE, 400),
                ("ううん、買わなかったの。", FEMALE_VOICE, 400),
                ("え、どうして？ 値段が高かったの？", MALE_VOICE, 400),
                ("ううん、値段は安かったんだけど、履いてみたらサイズがちょっと小さくて、足が痛かったの。", FEMALE_VOICE, 400),
                ("そうか、サイズが合わなかったんだね。", MALE_VOICE, 600)
            ],
            "explanation": "値段は安かったが、「サイズが ちょっと 小さくて、足が 痛かった」ため買いませんでした。正解は 3「サイズが小さかったから」です。"
        },
        {
            "qNum": 78,
            "title": "二人は 日曜日に どこへ 行きますか。",
            "titleRuby": "<ruby>二人<rt>ふたり</rt></ruby>は <ruby>日曜日<rt>にちようび</rt></ruby>に どこへ <ruby>行<rt>い</rt></ruby>きますか。",
            "script": """女の人：日曜日、どこかへ 出かけない？
男の人：いいね。山へ ハイキングに 行く？ それとも 海へ 行く？
女の人：最近 ちょっと つかれているから、山を 歩くのは 大変かも。海の 近くで おいしい 魚を 食べたいな。
男の人：じゃあ、海に 行こう！ 電車で 行けば のんびり できるしね。
女の人：賛成！ そうしましょう。""",
            "scriptRuby": """<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：<ruby>日曜日<rt>にちようび</rt></ruby>、どこかへ <ruby>出<rt>で</rt></ruby>かけない？<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：いいね。<ruby>山<rt>やま</rt></ruby>へ ハイキングに <ruby>行<rt>い</rt></ruby>く？ それとも <ruby>海<rt>うみ</rt></ruby>へ <ruby>行<rt>い</rt></ruby>く？<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：<ruby>最近<rt>さいきん</rt></ruby> ちょっと つかれているから、<ruby>山<rt>やま</rt></ruby>を <ruby>歩<rt>ある</rt></ruby>くのは <ruby>大変<rt>たいへん</rt></ruby>かも。<ruby>海<rt>うみ</rt></ruby>の <ruby>近<rt>ちか</rt></ruby>くで おいしい <ruby>魚<rt>さかな</rt></ruby>を <ruby>食<rt>た</rt></ruby>べたいな。<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：じゃあ、<ruby>海<rt>うみ</rt></ruby>に <ruby>行<rt>い</rt></ruby>こう！ <ruby>電車<rt>でんしゃ</rt></ruby>で <ruby>行<rt>い</rt></ruby>けば のんびり できるしね。<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：<ruby>賛成<rt>さんせい</rt></ruby>！ そうしましょう。""",
            "prompt1": "四番。女の人と男の人が話しています。二人は日曜日にどこへ行きますか。",
            "prompt2": "二人は日曜日にどこへ行きますか。",
            "options": ["山", "海", "カフェ", "デパート"],
            "correctIndex": 1,
            "dialogueTracks": [
                ("日曜日、どこかへ出かけない？", FEMALE_VOICE, 400),
                ("いいね。山へハイキングに行く？ それとも海へ行く？", MALE_VOICE, 400),
                ("最近ちょっとつかれているから、山を歩くのは大変かも。海の近くでおいしい魚を食べたいな。", FEMALE_VOICE, 400),
                ("じゃあ、海に行こう！ 電車で行けばのんびりできるしね。", MALE_VOICE, 400),
                ("賛成！ そうしましょう。", FEMALE_VOICE, 600)
            ],
            "explanation": "山は疲れるので避け、「海の近くでおいしい魚を食べたいな」「じゃあ、海に行こう！」と合意しました。正解は 2「海」です。"
        },
        {
            "qNum": 79,
            "title": "男の人は どんな 部屋を さがして いますか。",
            "titleRuby": "<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>は どんな <ruby>部屋<rt>へや</rt></ruby>を さがして いますか。",
            "script": """女の人：新しい アパート、みつかりましたか。
男の人：まだ さがして いるところです。
女の人：どんな 部屋が いいんですか。
男の人：いまの 部屋は 駅から 遠くて 不便なので、駅から 歩いて ５分くらいの 所が いいですね。
女の人：広さは どうですか。
男の人：広くなくても いいですが、夜 静かな 所が いいです。""",
            "scriptRuby": """<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：<ruby>新<rt>あたら</rt></ruby>しい アパート、みつかりましたか。<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：まだ さがして いるところです。<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：どんな <ruby>部屋<rt>へや</rt></ruby>が いいんですか。<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：いまの <ruby>部屋<rt>へや</rt></ruby>は <ruby>駅<rt>えき</rt></ruby>から <ruby>遠<rt>とお</rt></ruby>くて <ruby>不便<rt>ふべん</rt></ruby>なので、<ruby>駅<rt>えき</rt></ruby>から <ruby>歩<rt>ある</rt></ruby>いて ５<ruby>分<rt>ふん</rt></ruby>くらいの <ruby>所<rt>ところ</rt></ruby>が いいですね。<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：<ruby>広<rt>ひろ</rt></ruby>さは どうですか。<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：<ruby>広<rt>ひろ</rt></ruby>くなくても いいですが、<ruby>夜<rt>よる</rt></ruby> <ruby>静<rt>しず</rt></ruby>かな <ruby>所<rt>ところ</rt></ruby>が いいです。""",
            "prompt1": "五番。男の人と女の人が話しています。男の人はどんな部屋をさがしていますか。",
            "prompt2": "男の人はどんな部屋をさがしていますか。",
            "options": ["駅から近くて静かな部屋", "広くて家賃が安い部屋", "新しくて大きい部屋", "２階の部屋"],
            "correctIndex": 0,
            "dialogueTracks": [
                ("新しいアパート、みつかりましたか。", FEMALE_VOICE, 400),
                ("まださがしているところです。", MALE_VOICE, 400),
                ("どんな部屋がいいんですか。", FEMALE_VOICE, 400),
                ("いまの部屋は駅から遠くて不便なので、駅から歩いて5分くらいの所がいいですね。", MALE_VOICE, 400),
                ("広さはどうですか。", FEMALE_VOICE, 400),
                ("広くなくてもいいですが、夜静かな所がいいです。", MALE_VOICE, 600)
            ],
            "explanation": "男の人は「駅から歩いて5分くらい（駅から近い）」で「夜静かな所（静か）」を希望しています。広さは広くなくてもよいと言っています。正解は 1「駅から近くて静かな部屋」です。"
        },
        {
            "qNum": 80,
            "title": "男の人は 何曜日に ギターの 教室へ 行きますか。",
            "titleRuby": "<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>は <ruby>何曜日<rt>なんようび</rt></ruby>に ギターの <ruby>教室<rt>きょうしつ</rt></ruby>へ <ruby>行<rt>い</rt></ruby>きますか。",
            "script": """女の人：ケンさん、ギターを 習い始めたそうですね。
男の人：はい、先月から 教室に 通って います。
女の人：忙しいのに すごいですね。いつ 通って いるんですか。
男の人：平日は 仕事が ありますから、土曜日の 午後に 行って います。日曜日は 家で 休んで います。
女の人：そうですか、土曜日なんですね。""",
            "scriptRuby": """<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：ケンさん、ギターを <ruby>習<rt>なら</rt></ruby>い<ruby>始<rt>はじ</rt></ruby>めたそうですね。<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：はい、<ruby>先月<rt>せんげつ</rt></ruby>から <ruby>教室<rt>きょうしつ</rt></ruby>に <ruby>通<rt>かよ</rt></ruby>って います。<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：<ruby>忙<rt>いそが</rt></ruby>しいのに すごいですね。いつ <ruby>通<rt>かよ</rt></ruby>って いるんですか。<br>
<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：<ruby>平日<rt>へいじつ</rt></ruby>は <ruby>仕事<rt>しごと</rt></ruby>が ありますから、<ruby>土曜日<rt>どようび</rt></ruby>の <ruby>午後<rt>ごご</rt></ruby>に <ruby>行<rt>い</rt></ruby>って います。<ruby>日曜日<rt>にちようび</rt></ruby>は <ruby>家<rt>いえ</rt></ruby>で <ruby>休<rt>やす</rt></ruby>んで います。<br>
<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>：そうですか、<ruby>土曜日<rt>どようび</rt></ruby>なんですね。""",
            "prompt1": "六番。女の人と男の人が話しています。男の人は何曜日にギターの教室へ行きますか。",
            "prompt2": "男の人は何曜日にギターの教室へ行きますか。",
            "options": ["月曜日", "金曜日", "土曜日", "日曜日"],
            "correctIndex": 2,
            "dialogueTracks": [
                ("ケンさん、ギターを習い始めたそうですね。", FEMALE_VOICE, 400),
                ("はい、先月から教室に通っています。", MALE_VOICE, 400),
                ("忙しいのにすごいですね。いつ通っているんですか。", FEMALE_VOICE, 400),
                ("平日は仕事がありますから、土曜日の午後に行っています。日曜日は家で休んでいます。", MALE_VOICE, 400),
                ("そうですか、土曜日なんですね。", FEMALE_VOICE, 600)
            ],
            "explanation": "男の人は「土曜日の 午後に 行って います。日曜日は 家で 休んで います」と言っています。正解は 3「土曜日」です。"
        }
    ]

    for item in s3_m2:
        audio_filename = f"n5_m01_q{item['qNum']:02d}.mp3"
        tracks = [
            (item["prompt1"], NARRATOR_VOICE, 800)
        ] + item["dialogueTracks"] + [
            (item["prompt2"], NARRATOR_VOICE, 500)
        ]
        
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec3",
            "subsectionId": "s3_m2",
            "category": "ポイント理解",
            "qNum": item["qNum"],
            "title": item["title"],
            "titleRuby": item["titleRuby"],
            "script": item["script"],
            "scriptRuby": item["scriptRuby"],
            "audioUrl": f"audio/mock_n5/{audio_filename}",
            "questionText": "まず しつもんを きいて ください。そのあと、もんだいようしを みて ください。よむ じかんが あります。それから はなしを きいて、１から４の なかから、いちばん いい ものを ひとつ えらんで ください。",
            "options": item["options"],
            "correctIndex": item["correctIndex"],
            "weight": 2.5,
            "explanation": item["explanation"],
            "tracks": tracks
        })

    # --- 聴解 問題3: 発話表現 (Q81〜Q85) (3択) ---
    s3_m3 = [
        {
            "qNum": 81,
            "title": "先生の 部屋に 入ります。何と 言いますか。",
            "titleRuby": "<ruby>先生<rt>せんせい</rt></ruby>の <ruby>部屋<rt>へや</rt></ruby>に <ruby>入<rt>はい</rt></ruby>ります。<ruby>何<rt>なん</rt></ruby>と <ruby>言<rt>い</rt></ruby>いますか。",
            "scene": "先生の 部屋に 入ります。何と 言いますか。",
            "options": ["しつれいします。", "さようなら。", "いってきます。"],
            "correctIndex": 0,
            "audioTracks": [
                ("問題三。一番。先生の部屋に入ります。何と言いますか。", NARRATOR_VOICE, 600),
                ("一番。しつれいします。", NARRATOR_VOICE, 500),
                ("二番。さようなら。", NARRATOR_VOICE, 500),
                ("三番。いってきます。", NARRATOR_VOICE, 500)
            ],
            "explanation": "他人の部屋や研究室などに入るときの挨拶は「しつれいします（失礼します）」です。\n2「さようなら」は別れるとき、3「いってきます」は自分の家を出るときに使います。"
        },
        {
            "qNum": 82,
            "title": "友だちに 料理を ごちそうに なりました。帰るとき、何と 言いますか。",
            "titleRuby": "<ruby>友<rt>とも</rt></ruby>だちに <ruby>料理<rt>りょうり</rt></ruby>を ごちそうに なりました。<ruby>帰<rt>かえ</rt></ruby>るとき、<ruby>何<rt>なん</rt></ruby>と <ruby>言<rt>い</rt></ruby>いますか。",
            "scene": "友だちに 料理を ごちそうに なりました。帰るとき、何と 言いますか。",
            "options": ["いただきます。", "ごちそうさまでした。", "おねがいします。"],
            "correctIndex": 1,
            "audioTracks": [
                ("二番。友だちに料理をごちそうになりました。帰るとき、何と言いますか。", NARRATOR_VOICE, 600),
                ("一番。いただきます。", NARRATOR_VOICE, 500),
                ("二番。ごちそうさまでした。", NARRATOR_VOICE, 500),
                ("三番。おねがいします。", NARRATOR_VOICE, 500)
            ],
            "explanation": "食事をごちそうになった相手に対して感謝を伝える挨拶は「ごちそうさまでした」です。\n1「いただきます」は食べる前、3「おねがいします」は何かを頼むときに使います。"
        },
        {
            "qNum": 83,
            "title": "友だちに 傘を 借りたいです。何と 言いますか。",
            "titleRuby": "<ruby>友<rt>とも</rt></ruby>だちに <ruby>傘<rt>かさ</rt></ruby>を <ruby>借<rt>か</rt></ruby>りたいです。<ruby>何<rt>なん</rt></ruby>と <ruby>言<rt>い</rt></ruby>いますか。",
            "scene": "友だちに 傘を 借りたいです。何と 言いますか。",
            "options": ["傘を 貸しましょうか。", "傘を 貸して ください。", "傘を あげます。"],
            "correctIndex": 1,
            "audioTracks": [
                ("三番。友だちに傘を借りたいです。何と言いますか。", NARRATOR_VOICE, 600),
                ("一番。傘を貸しましょうか。", NARRATOR_VOICE, 500),
                ("二番。傘を貸してください。", NARRATOR_VOICE, 500),
                ("三番。傘をあげます。", NARRATOR_VOICE, 500)
            ],
            "explanation": "自分が借りたいときは、相手に「貸してください」と頼みます。\n1「貸しましょうか」は自分が相手に貸す申し出、3「あげます」は物を贈るときです。"
        },
        {
            "qNum": 84,
            "title": "電車の中で、お年寄りに 席を ゆずります。何と 言いますか。",
            "titleRuby": "<ruby>電車<rt>でんしゃ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>で、お<ruby>年寄<rt>としよ</rt></ruby>りに <ruby>席<rt>せき</rt></ruby>を ゆずります。<ruby>何<rt>なん</rt></ruby>と <ruby>言<rt>い</rt></ruby>いますか。",
            "scene": "電車の中で、お年寄りに 席を ゆずります。何と 言いますか。",
            "options": ["どうぞ。", "ごめんなさい。", "いただきます。"],
            "correctIndex": 0,
            "audioTracks": [
                ("四番。電車の中で、お年寄りに席をゆずります。何と言いますか。", NARRATOR_VOICE, 600),
                ("一番。どうぞ。", NARRATOR_VOICE, 500),
                ("二番。ごめんなさい。", NARRATOR_VOICE, 500),
                ("三番。いただきます。", NARRATOR_VOICE, 500)
            ],
            "explanation": "席を譲るときは相手に「どうぞ（お座りください）」と声をかけます。\n2「ごめんなさい」は謝罪、3「いただきます」は食事の挨拶です。"
        },
        {
            "qNum": 85,
            "title": "友だちの 家に 遊びに 来ました。玄関で 何と 言いますか。",
            "titleRuby": "<ruby>友<rt>とも</rt></ruby>だちの <ruby>家<rt>いえ</rt></ruby>に <ruby>遊<rt>あそ</rt></ruby>びに <ruby>来<rt>き</rt></ruby>ました。<ruby>玄関<rt>げんかん</rt></ruby>で <ruby>何<rt>なん</rt></ruby>と <ruby>言<rt>い</rt></ruby>いますか。",
            "scene": "友だちの 家に 遊びに 来ました。玄関で 何と 言いますか。",
            "options": ["ごめんください。", "おかえりなさい。", "いってらっしゃい。"],
            "correctIndex": 0,
            "audioTracks": [
                ("五番。友だちの家に遊びに来ました。玄関で何と言いますか。", NARRATOR_VOICE, 600),
                ("一番。ごめんください。", NARRATOR_VOICE, 500),
                ("二番。おかえりなさい。", NARRATOR_VOICE, 500),
                ("三番。いってらっしゃい。", NARRATOR_VOICE, 500)
            ],
            "explanation": "訪問先で玄関から人を呼ぶときは「ごめんください」と言います。\n2「おかえりなさい」は帰ってきた人を迎える言葉、3「いってらっしゃい」は出かける人を送り出す言葉です。"
        }
    ]

    for item in s3_m3:
        audio_filename = f"n5_m01_q{item['qNum']:02d}.mp3"
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec3",
            "subsectionId": "s3_m3",
            "category": "発話表現",
            "qNum": item["qNum"],
            "title": item["title"],
            "titleRuby": item["titleRuby"],
            "sceneDesc": item["scene"],
            "audioUrl": f"audio/mock_n5/{audio_filename}",
            "questionText": "えを みながら、しつもんを きいて ください。やじるし（➡）の ひとは なんと いいますか。１から３の なかから、いちばん いい ものを ひとつ えらんで ください。",
            "options": item["options"],
            "correctIndex": item["correctIndex"],
            "weight": 2.5,
            "explanation": item["explanation"],
            "tracks": item["audioTracks"]
        })

    # --- 聴解 問題4: 即時応答 (Q86〜Q91) (3択) ---
    s3_m4 = [
        {
            "qNum": 86,
            "title": "あしたの テスト、がんばって くださいね。",
            "titleRuby": "あしたの テスト、がんばって くださいね。",
            "spoken": "あしたの テスト、がんばって くださいね。",
            "options": ["はい、がんばります。", "いいえ、テストです。", "どういたしまして。"],
            "correctIndex": 0,
            "audioTracks": [
                ("問題四。一番。", NARRATOR_VOICE, 400),
                ("あしたのテスト、がんばってくださいね。", FEMALE_VOICE, 600),
                ("一番。はい、がんばります。", MALE_VOICE, 400),
                ("二番。いいえ、テストです。", MALE_VOICE, 400),
                ("三番。どういたしまして。", MALE_VOICE, 500)
            ],
            "explanation": "「がんばってくださいね」と励まされたときは「はい、がんばります」と答えます。\n3「どういたしまして」はお礼を言われたときの返事です。"
        },
        {
            "qNum": 87,
            "title": "いっしょに お昼ごはんを 食べませんか。",
            "titleRuby": "いっしょに お<ruby>昼<rt>ひる</rt></ruby>ごはんを <ruby>食<rt>た</rt></ruby>べませんか。",
            "spoken": "いっしょに お昼ごはんを 食べませんか。",
            "options": ["ええ、食べましょう。", "ごはんを 食べました。", "はい、おいしいです。"],
            "correctIndex": 0,
            "audioTracks": [
                ("二番。", NARRATOR_VOICE, 400),
                ("いっしょにお昼ごはんを食べませんか。", MALE_VOICE, 600),
                ("一番。ええ、食べましょう。", FEMALE_VOICE, 400),
                ("二番。ごはんを食べました。", FEMALE_VOICE, 400),
                ("三番。はい、おいしいです。", FEMALE_VOICE, 500)
            ],
            "explanation": "「〜ませんか」と誘われたときの承諾表現は「ええ、〜ましょう（食べましょう）」です。"
        },
        {
            "qNum": 88,
            "title": "すみません、この 近くに ポストは ありますか。",
            "titleRuby": "すみません、この <ruby>近<rt>ちか</rt></ruby>くに ポストは ありますか。",
            "spoken": "すみません、この 近くに ポストは ありますか。",
            "options": ["あそこに ありますよ。", "はい、手紙です。", "ポストへ 行きません。"],
            "correctIndex": 0,
            "audioTracks": [
                ("三番。", NARRATOR_VOICE, 400),
                ("すみません、この近くにポストはありますか。", FEMALE_VOICE, 600),
                ("一番。あそこにありますよ。", MALE_VOICE, 400),
                ("二番。はい、手紙です。", MALE_VOICE, 400),
                ("三番。ポストへ行きません。", MALE_VOICE, 500)
            ],
            "explanation": "場所を尋ねられたときは、位置を教えて「あそこに ありますよ」と答えるのが自然です。"
        },
        {
            "qNum": 89,
            "title": "その 荷物、重そうですね。持ちましょうか。",
            "titleRuby": "その <ruby>荷物<rt>にもつ</rt></ruby>、<ruby>重<rt>おも</rt></ruby>そうですね。<ruby>持<rt>も</rt></ruby>ちましょうか。",
            "spoken": "その 荷物、重そうですね。持ちましょうか。",
            "options": ["すみません、お願いします。", "重くありませんでした。", "カバンです。"],
            "correctIndex": 0,
            "audioTracks": [
                ("四番。", NARRATOR_VOICE, 400),
                ("その荷物、重そうですね。持ちましょうか。", MALE_VOICE, 600),
                ("一番。すみません、お願いします。", FEMALE_VOICE, 400),
                ("二番。重くありませんでした。", FEMALE_VOICE, 400),
                ("三番。カバンです。", FEMALE_VOICE, 500)
            ],
            "explanation": "相手が手伝いを申し出てくれた（持ちましょうか）とき、感謝しつつお願いする表現は「すみません、お願いします」です。"
        },
        {
            "qNum": 90,
            "title": "昨日は どこへ 行きましたか。",
            "titleRuby": "<ruby>昨日<rt>きのう</rt></ruby>は どこへ <ruby>行<rt>い</rt></ruby>きましたか。",
            "spoken": "昨日は どこへ 行きましたか。",
            "options": ["図書館へ 行きました。", "友だちと 行きます。", "電車で 行きました。"],
            "correctIndex": 0,
            "audioTracks": [
                ("五番。", NARRATOR_VOICE, 400),
                ("昨日はどこへ行きましたか。", FEMALE_VOICE, 600),
                ("一番。図書館へ行きました。", MALE_VOICE, 400),
                ("二番。友だちと行きます。", MALE_VOICE, 400),
                ("三番。電車で行きました。", MALE_VOICE, 500)
            ],
            "explanation": "「どこへ行きましたか」と場所の過去の移動を尋ねられているので、場所＋へ＋行きました（1「図書館へ 行きました」）が正しい返答です。2は未来形、3は交通手段の答えです。"
        },
        {
            "qNum": 91,
            "title": "田中さんは いま どこに いますか。",
            "titleRuby": "<ruby>田中<rt>たなか</rt></ruby>さんは いま どこに いますか。",
            "spoken": "田中さんは いま どこに いますか。",
            "options": ["会議室に いますよ。", "はい、田中さんです。", "３時です。"],
            "correctIndex": 0,
            "audioTracks": [
                ("六番。", NARRATOR_VOICE, 400),
                ("田中さんはいまどこにいますか。", MALE_VOICE, 600),
                ("一番。会議室にいますよ。", FEMALE_VOICE, 400),
                ("二番。はい、田中さんです。", FEMALE_VOICE, 400),
                ("三番。３時です。", FEMALE_VOICE, 500)
            ],
            "explanation": "人物の現在の居場所を尋ねられているので、場所＋にいます（1「会議室に いますよ」）が正しい返答です。"
        }
    ]

    for item in s3_m4:
        audio_filename = f"n5_m01_q{item['qNum']:02d}.mp3"
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec3",
            "subsectionId": "s3_m4",
            "category": "即時応答",
            "qNum": item["qNum"],
            "title": item["title"],
            "titleRuby": item["titleRuby"],
            "spokenText": item["spoken"],
            "audioUrl": f"audio/mock_n5/{audio_filename}",
            "questionText": "えなどが ありません。ぶんを きいて、１から３の なかから、いちばん いい ものを ひとつ えらんで ください。",
            "options": item["options"],
            "correctIndex": item["correctIndex"],
            "weight": 2.5,
            "explanation": item["explanation"],
            "tracks": item["audioTracks"]
        })

    print(f"Total questions assembled: {len(questions)}")
    assert len(questions) == 91, f"Expected 91 questions, got {len(questions)}"

    # Generate Audio for all Section 3 questions
    print("\nSynthesizing Google Cloud Neural2 Audio for Listening Section...")
    from google.cloud import texttospeech
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/yamauchimiku/Documents/GitHub/japanese-learning/secrets/google_tts_key.json'
    tts_client = texttospeech.TextToSpeechClient()

    audio_dir = '/Users/yamauchimiku/Documents/GitHub/japanese-learning/audio/mock_n5'
    public_audio_dir = '/Users/yamauchimiku/Documents/GitHub/japanese-learning/public/audio/mock_n5'
    os.makedirs(audio_dir, exist_ok=True)
    os.makedirs(public_audio_dir, exist_ok=True)

    def text_for_tts(t):
        if not t:
            return ""
        # Convert ruby to reading: <ruby>漢字<rt>よみ</rt></ruby> -> よみ
        t = re.sub(r'<ruby>[^<]*?<rt>(.*?)</rt></ruby>', r'\1', t)
        t = re.sub(r'<.*?>', '', t)
        # Section numbers (never pronounce 一 as はじめ)
        t = t.replace('問題一', '問題１').replace('問題二', '問題２').replace('問題三', '問題３').replace('問題四', '問題４')
        # Question numbers in prompts (ensure いちばん, にばん, etc.)
        t = re.sub(r'一番(?=[。、\s]|$)', '１番', t)
        t = re.sub(r'二番(?=[。、\s]|$)', '２番', t)
        t = re.sub(r'三番(?=[。、\s]|$)', '３番', t)
        t = re.sub(r'四番(?=[。、\s]|$)', '４番', t)
        t = re.sub(r'五番(?=[。、\s]|$)', '５番', t)
        t = re.sub(r'六番(?=[。、\s]|$)', '６番', t)
        t = re.sub(r'七番(?=[。、\s]|$)', '７番', t)
        # Critical polyphonic verbs: カ変動詞「来る」
        t = t.replace('持って来なければ', '持ってこなければ')
        t = t.replace('来なければ', 'こなければ')
        t = t.replace('来なかった', 'こなかった')
        t = t.replace('来ない', 'こない')
        t = t.replace('遊びに来ました', '遊びにきました')
        t = t.replace('持って来て', '持ってきて')
        t = t.replace('持って来ます', '持ってきます')
        # Other TTS pitfalls
        t = t.replace('何時', 'なんじ')
        t = t.replace('何曜', 'なんよう')
        t = t.replace('何本', 'なんぼん')
        t = t.replace('何人', 'なんにん')
        return t

    for q in questions:
        if q["sectionId"] == "sec3" and "tracks" in q:
            fname = os.path.basename(q["audioUrl"])
            fpath = os.path.join(audio_dir, fname)
            pub_fpath = os.path.join(public_audio_dir, fname)
            print(f"Synthesizing {fname} ...")
            comb = bytearray()
            for txt, voice_name, pause_ms in q["tracks"]:
                clean_t = text_for_tts(txt)
                sinput = texttospeech.SynthesisInput(text=clean_t)
                voice = texttospeech.VoiceSelectionParams(language_code='ja-JP', name=voice_name)
                aconf = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3, speaking_rate=0.92)
                resp = tts_client.synthesize_speech(input=sinput, voice=voice, audio_config=aconf)
                comb.extend(resp.audio_content)

                if pause_ms > 0:
                    p_ssml = f'<speak><break time="{pause_ms}ms"/></speak>'
                    p_in = texttospeech.SynthesisInput(ssml=p_ssml)
                    p_resp = tts_client.synthesize_speech(input=p_in, voice=voice, audio_config=aconf)
                    comb.extend(p_resp.audio_content)
            with open(fpath, 'wb') as f:
                f.write(comb)
            with open(pub_fpath, 'wb') as f:
                f.write(comb)
            print(f"  ✓ Saved {fname} ({len(comb)} bytes)")
            del q["tracks"]

    mock_data = {
        "exam_id": "n5_mock_01",
        "title": "JLPT N5 実戦模擬試験 第1回",
        "level": "N5",
        "totalQuestions": 91,
        "totalTimeMinutes": 105,
        "passingTotalScore": 80,
        "maxTotalScore": 180,
        "benchmarks": {
            "sec_lang_reading": 38,
            "sec_listening": 19
        },
        "sections": [
            {
                "id": "sec1",
                "name": "言語知識（文字・語彙）",
                "shortName": "文字・語彙",
                "timeMinutes": 25,
                "questionsCount": 35,
                "subsections": [
                    { "id": "s1_m1", "name": "問題1 漢字読み", "desc": "<span class='jlpt-underline-blank'></span>の ことばは どう よみますか。１・２・３・４から いちばん いい ものを ひとつ えらんで ください。", "count": 12, "range": [1, 12] },
                    { "id": "s1_m2", "name": "問題2 表記", "desc": "<span class='jlpt-underline-blank'></span>の ことばは どう かきますか。１・２・３・４から いちばん いい ものを ひとつ えらんで ください。", "count": 8, "range": [13, 20] },
                    { "id": "s1_m3", "name": "問題3 文脈規定", "desc": "（　）に なにを いれますか。１・２・３・４から いちばん いい ものを ひとつ えらんで ください。", "count": 10, "range": [21, 30] },
                    { "id": "s1_m4", "name": "問題4 言い換え類義", "desc": "<span class='jlpt-underline-blank'></span>の ぶんと だいたい おなじ いみの ぶんが あります。１・２・３・４から いちばん いい ものを ひとつ えらんで ください。", "count": 5, "range": [31, 35] }
                ]
            },
            {
                "id": "sec2",
                "name": "言語知識（文法）・読解",
                "shortName": "文法・読解",
                "timeMinutes": 50,
                "questionsCount": 32,
                "subsections": [
                    { "id": "s2_m1", "name": "問題1 文法形式の判断", "desc": "（　）に なにを いれますか。１・２・３・４から いちばん いい ものを ひとつ えらんで ください。", "count": 16, "range": [36, 51] },
                    { "id": "s2_m2", "name": "問題2 文の組み立て", "desc": "★に 入る ものは どれですか。１・２・３・４から いちばん いい ものを ひとつ えらんで ください。", "count": 5, "range": [52, 56] },
                    { "id": "s2_m3", "name": "問題3 文章の文法", "desc": "[57]から[61]に 何を 入れますか。文章の 意味を 考えて、１・２・３・４から いちばん いい ものを ひとつ えらんで ください。", "count": 5, "range": [57, 61] },
                    { "id": "s2_m4", "name": "問題4 内容理解（短文）", "desc": "つぎの ぶんしょうを よんで、しつもんに こたえて ください。こたえは １・２・３・４から いちばん いい ものを ひとつ えらんで ください。", "count": 3, "range": [62, 64] },
                    { "id": "s2_m5", "name": "問題5 内容理解（中文）", "desc": "つぎの ぶんしょうを よんで、しつもんに こたえて ください。こたえは １・２・３・４から いちばん いい ものを ひとつ えらんで ください。", "count": 2, "range": [65, 66] },
                    { "id": "s2_m6", "name": "問題6 情報検索", "desc": "案内を 見て、しつもんに こたえて ください。こたえは １・２・３・４から いちばん いい ものを ひとつ えらんで ください。", "count": 1, "range": [67, 67] }
                ]
            },
            {
                "id": "sec3",
                "name": "聴解",
                "shortName": "聴解",
                "timeMinutes": 30,
                "questionsCount": 24,
                "subsections": [
                    { "id": "s3_m1", "name": "問題1 課題理解", "desc": "まず しつもんを 聞いて ください。それから 話を 聞いて、１から４の なかから、いちばん いい ものを ひとつ えらんで ください。", "count": 7, "range": [68, 74] },
                    { "id": "s3_m2", "name": "問題2 ポイント理解", "desc": "まず しつもんを 聞いて ください。そのあと、問題用紙を 見て ください。読む 時間が あります。それから 話を 聞いて、１から４の なかから、いちばん いい ものを ひとつ えらんで ください。", "count": 6, "range": [75, 80] },
                    { "id": "s3_m3", "name": "問題3 発話表現", "desc": "絵を 見ながら、しつもんを 聞いて ください。やじるし（➡）の 人は 何と 言いますか。１から３の なかから、いちばん いい ものを ひとつ えらんで ください。", "count": 5, "range": [81, 85] },
                    { "id": "s3_m4", "name": "問題4 即時応答", "desc": "絵などが ありません。文を 聞いて、１から３の なかから、いちばん いい ものを ひとつ えらんで ください。", "count": 6, "range": [86, 91] }
                ]
            }
        ],
        "questions": questions
    }

    db_js = "window.JLPT_N5_MOCK_DATA = " + json.dumps(mock_data, ensure_ascii=False, indent=2) + ";\n"
    
    out_paths = [
        "/Users/yamauchimiku/Documents/GitHub/japanese-learning/database/jlpt_n5_mock_data.js",
        "/Users/yamauchimiku/Documents/GitHub/japanese-learning/public/database/jlpt_n5_mock_data.js"
    ]
    for p in out_paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(db_js)
        print(f"Saved: {p} ({len(db_js)} bytes)")

if __name__ == '__main__':
    main()
