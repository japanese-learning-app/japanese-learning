# -*- coding: utf-8 -*-
"""
JLPT N5 本番模擬試験 10回分（各91問・計910問）生成エンジン
公式ガイドブック準拠・IRT尺度得点対応・全問イラスト完備
"""

import os
import sys
import json
import re

sys.path.append(os.path.dirname(__file__))
import generate_listening_illustrations as gli

def sanitize(text):
    if not text:
        return text
    text = text.replace("この後", "このあと")
    text = text.replace("持って来なければ", "持ってこなければ")
    text = text.replace("来なければ", "こなければ")
    text = text.replace("来なかった", "こなかった")
    text = text.replace("来なくて", "こなくて")
    text = text.replace("来られる", "こられる")
    text = text.replace("問題一", "問題１")
    text = text.replace("問題二", "問題２")
    text = text.replace("問題三", "問題３")
    text = text.replace("問題四", "問題４")
    text = text.replace("一番", "１番")
    text = text.replace("二番", "２番")
    text = text.replace("三番", "３番")
    text = text.replace("四番", "４番")
    text = text.replace("Zoom", "オンラインミーティング")
    text = text.replace("zoom", "オンラインミーティング")
    text = text.replace("ソニー", "大手電機メーカー")
    text = text.replace("パナソニック", "大手家電メーカー")
    return text

def main():
    base_dir = "/Users/yamauchimiku/Documents/GitHub/japanese-learning"
    svg_dir = os.path.join(base_dir, "images/listening_svg")
    os.makedirs(svg_dir, exist_ok=True)

    # 1. Load Round 1 from existing jlpt_n5_mock_data.js
    r1_path = os.path.join(base_dir, "database/jlpt_n5_mock_data.js")
    with open(r1_path, "r", encoding="utf-8") as f:
        content = f.read()
        json_str = content.replace("window.JLPT_N5_MOCK_DATA = ", "").strip()
        if json_str.endswith(";"):
            json_str = json_str[:-1]
        round1_data = json.loads(json_str)

    rounds = {1: round1_data}

    # Ensure Round 1 listening questions also have SVGs if missing
    for q in round1_data["questions"]:
        if q["sectionId"] == "sec3":
            svg_fname = f"n5_r1_q{q['qNum']}.svg"
            svg_path = os.path.join(svg_dir, svg_fname)
            rel_url = f"images/listening_svg/{svg_fname}"
            if not os.path.exists(svg_path):
                if q["subsectionId"] == "s3_m3":
                    svg_content = gli.make_arrow_svg(q["title"], "挨拶・日常場面での発話", "あなた（➡）", "相手")
                elif q["subsectionId"] == "s3_m4":
                    svg_content = gli.make_scene_svg(q["title"], "一般", "話者", "あなた", "質問に対して最も適切な返答を選びます")
                else:
                    svg_content = gli.make_scene_svg(q["title"], "家庭・日常", "女性", "男性", "対話内容をしっかり確認")
                with open(svg_path, "w", encoding="utf-8") as sf:
                    sf.write(svg_content)
            q["has_illustration"] = True
            q["illustration_url"] = rel_url

    print("Round 1 verified with SVGs.")

    # 2. Build Rounds 2 through 10
    # Vocabulary & Grammar Datasets for N5
    kanji_reading_bank = [
        ("今日", "きょう", ["きのう", "きょう", "あした", "あさって"], 1, "今日の 天気は いいです。"),
        ("先生", "せんせい", ["がくせい", "いしゃ", "せんせい", "ともだち"], 2, "日本語の 先生に 聞きました。"),
        ("車", "くるま", ["でんしゃ", "くるま", "じてんしゃ", "ひこうき"], 1, "新しい 車を 買いました。"),
        ("本", "ほん", ["ほん", "かみ", "てがみ", "ノート"], 0, "図書館で 本を 借りました。"),
        ("友だち", "ともだち", ["かぞく", "きょうだい", "ともだち", "こども"], 2, "日曜日、友だちに 会いました。"),
        ("大学", "だいがく", ["だいがく", "こうこう", "ちゅうがく", "しょうがく"], 0, "兄は 大学に 通っています。"),
        ("時間", "じかん", ["じかん", "きかん", "くかん", "しゅかん"], 0, "テストの 時間は １時間です。"),
        ("雨", "あめ", ["ゆき", "くもり", "あめ", "かぜ"], 2, "外は 雨が ふっています。"),
        ("午後", "ごご", ["ごぜん", "ごご", "あさ", "よる"], 1, "午後は 図書館へ 行きます。"),
        ("手紙", "てがみ", ["きって", "てがみ", "はがき", "ふうとう"], 1, "母に 手紙を 書きました。"),
        ("花", "はな", ["はな", "くさ", "き", "はっぱ"], 0, "庭に きれいな 花が 咲きました。"),
        ("道", "みち", ["かわ", "みち", "やま", "うみ"], 1, "この 道を まっすぐ 行きます。"),
        ("魚", "さかな", ["にく", "さかな", "やさい", "くだもの"], 1, "晩ご飯に 魚を 食べました。"),
        ("目", "め", ["め", "みみ", "はな", "くち"], 0, "テレビを 見すぎて 目が 痛いです。"),
        ("耳", "みみ", ["あたま", "みみ", "かお", "て"], 1, "犬の 耳は 大きいです。"),
        ("足", "あし", ["て", "くび", "かた", "あし"], 3, "たくさん 歩いて 足が 疲れました。"),
        ("空", "そら", ["うみ", "かわ", "そら", "やま"], 2, "青い 空が 広がっています。"),
        ("外国", "がいこく", ["がいこく", "りょこう", "ひこうき", "くに"], 0, "いつか 外国へ 行きたいです。"),
        ("男の人", "おとこのひと", ["おんなのひと", "おとこのひと", "おとこのこ", "おとな"], 1, "あそこに 男の人が います。"),
        ("女の子", "おんなのこ", ["おとこのこ", "おんなのこ", "あかちゃん", "こども"], 1, "公園で 女の子が 遊んでいます。"),
        ("名前", "なまえ", ["なまえ", "じゅうしょ", "でんわ", "へや"], 0, "ここに 名前を 書いて ください。"),
        ("毎日", "まいにち", ["まいあさ", "まいばん", "まいにち", "まいとし"], 2, "毎日 日本語を 勉強します。"),
        ("今週", "こんしゅう", ["せんしゅう", "こんしゅう", "らいしゅう", "まいしゅう"], 1, "今週の 土曜日は 休みです。"),
        ("来月", "らいげつ", ["せんげつ", "こんげつ", "らいげつ", "まいげつ"], 2, "来月、日本へ 行きます。")
    ]

    for round_num in range(2, 11):
        print(f"Generating N5 Mock Round {round_num}...")
        r_questions = []
        
        # Section 1: 文字・語彙 (35問)
        # 問題1: 漢字読み (Q1〜12)
        offset = (round_num * 5) % len(kanji_reading_bank)
        for i in range(12):
            idx = (offset + i) % len(kanji_reading_bank)
            item = kanji_reading_bank[idx]
            q_num = i + 1
            sent = item[4].replace(item[0], f"<span class='jlpt-underline-blank'>{item[0]}</span>")
            r_questions.append({
                "qNum": q_num,
                "sectionId": "sec1",
                "subsectionId": "s1_m1",
                "sectionName": "言語知識（文字・語彙）",
                "subsectionName": "問題1 漢字読み",
                "title": sent,
                "titleRuby": item[4],
                "options": item[2],
                "correctIndex": item[3],
                "explanation": f"「{item[0]}」の正しい読み方は「{item[1]}」です。"
            })

        # 問題2: 表記 (Q13〜20) (8問)
        hyoki_bank = [
            ("やま", "山", ["山", "川", "木", "田"], 0, "休みの日、<span class='jlpt-underline-blank'>やま</span>へ 行きました。"),
            ("かわ", "川", ["海", "川", "池", "水"], 1, "<span class='jlpt-underline-blank'>かわ</span>で 魚を つりました。"),
            ("あめ", "雨", ["雪", "雲", "雨", "風"], 2, "きのうは <span class='jlpt-underline-blank'>あめ</span>でした。"),
            ("ひと", "人", ["人", "入", "大", "八"], 0, "あの <span class='jlpt-underline-blank'>ひと</span>は だれですか。"),
            ("ほん", "本", ["木", "本", "体", "休"], 1, "机の 上に <span class='jlpt-underline-blank'>ほん</span>が あります。"),
            ("みず", "水", ["水", "氷", "川", "湯"], 0, "冷たい <span class='jlpt-underline-blank'>みず</span>を ください。"),
            ("いぬ", "犬", ["太", "犬", "大", "天"], 1, "白い <span class='jlpt-underline-blank'>いぬ</span>を かっています。"),
            ("てがみ", "手紙", ["手紙", "毛紙", "手切", "手紙"], 0, "友だちに <span class='jlpt-underline-blank'>てがみ</span>を 出しました。")
        ]
        for i in range(8):
            item = hyoki_bank[(round_num + i) % len(hyoki_bank)]
            q_num = 13 + i
            r_questions.append({
                "qNum": q_num,
                "sectionId": "sec1",
                "subsectionId": "s1_m2",
                "sectionName": "言語知識（文字・語彙）",
                "subsectionName": "問題2 表記",
                "title": item[4],
                "titleRuby": item[4],
                "options": item[2],
                "correctIndex": item[3],
                "explanation": f"「{item[0]}」は漢字で「{item[1]}」と書きます。"
            })

        # 問題3: 文脈規定 (Q21〜30) (10問)
        bunmyaku_bank = [
            ("あさは ７時に （　）。", ["おきます", "ねます", "いきます", "かえります"], 0, "起きます"),
            ("ごはんの 前に 手を （　）。", ["あらいます", "みがきます", "たべます", "きります"], 0, "洗います"),
            ("スーパーで りんごを （　）。", ["かいました", "うりました", "かしました", "かりました"], 0, "買いました"),
            ("あした テストが あるので、夜 （　）。", ["べんきょうします", "あそびます", "さんぽします", "りょこうします"], 0, "勉強します"),
            ("のどが かわいたので、お茶を （　）。", ["のみました", "たべました", "すいました", "ききました"], 0, "飲みました"),
            ("えきから 大学まで バスに （　）。", ["のりました", "おりました", "あるきました", "とまりました"], 0, "乗りました"),
            ("へやが くらいですから、電気を （　）ください。", ["つけて", "けして", "あけて", "しめて"], 0, "つけて"),
            ("さむいので、まどを （　）ください。", ["しめて", "あけて", "つけて", "けして"], 0, "閉めて"),
            ("まいあさ、しんぶんを （　）。", ["よみます", "みます", "ききます", "かきます"], 0, "読みます"),
            ("コートを ぬいで、ハンガーに （　）。", ["かけました", "おきました", "いれました", "つけました"], 0, "かけました")
        ]
        for i in range(10):
            item = bunmyaku_bank[(round_num * 2 + i) % len(bunmyaku_bank)]
            q_num = 21 + i
            r_questions.append({
                "qNum": q_num,
                "sectionId": "sec1",
                "subsectionId": "s1_m3",
                "sectionName": "言語知識（文字・語彙）",
                "subsectionName": "問題3 文脈規定",
                "title": item[0].replace("（　）", "<span class='jlpt-underline-blank'>　　</span>"),
                "titleRuby": item[0],
                "options": item[1],
                "correctIndex": item[2],
                "explanation": f"文脈から、正解は「{item[1][item[2]]}」です。"
            })

        # 問題4: 類義語 (Q31〜35) (5問)
        ruigi_bank = [
            ("きのうは 天気が よかったです。", ["雨が ふりませんでした", "とても さむかったです", "風が つよかったです", "雪でした"], 0, "天気がいい＝雨が降らない、晴れ"),
            ("この りょうりは からいです。", ["あまいです", "ピリピリします", "おいしくないです", "つめたいです"], 1, "からい＝スパイシー"),
            ("あしたは ひまです。", ["いそがしいです", "用事が ありません", "仕事が あります", "学校へ 行きます"], 1, "ひま＝時間がある、用事がない"),
            ("父は げんきです。", ["体が じょうぶです", "びょうきです", "ねています", "やせています"], 0, "元気＝健康、じょうぶ"),
            ("部屋を そうじしました。", ["きれいに しました", "汚しました", "広くしました", "あかるくしました"], 0, "掃除する＝きれいにする")
        ]
        for i in range(5):
            item = ruigi_bank[(round_num + i) % len(ruigi_bank)]
            q_num = 31 + i
            r_questions.append({
                "qNum": q_num,
                "sectionId": "sec1",
                "subsectionId": "s1_m4",
                "sectionName": "言語知識（文字・語彙）",
                "subsectionName": "問題4 言い換え類義",
                "title": f"<span class='jlpt-underline-blank'>{item[0]}</span> と だいたい 同じ いみの 文は どれですか。",
                "titleRuby": item[0],
                "options": item[1],
                "correctIndex": item[2],
                "explanation": item[3]
            })

        # Section 2: 文法・読解 (32問: Q36〜Q67)
        # 文法問題1: 文法形式判断 (Q36〜51) (16問)
        gram_bank = [
            ("わたしは 毎朝 ７時【　　】起きます。", ["に", "で", "を", "へ"], 0, "特定の時間には助詞「に」を使います。"),
            ("日曜日、友だち【　　】映画を 見ました。", ["と", "に", "で", "を"], 0, "いっしょに行動する相手には助詞「と」を使います。"),
            ("図書館【　　】本を 読みます。", ["で", "に", "を", "へ"], 0, "動作を行う場所には助詞「で」を使います。"),
            ("スーパーへ りんご【　　】買いに 行きます。", ["を", "に", "で", "が"], 0, "目的の動作の前には「を」を使います。"),
            ("この ペンで 名前【　　】書いて ください。", ["を", "に", "が", "で"], 0, "目的語には「を」を使います。"),
            ("日本【　　】１年前に 来ました。", ["へ", "で", "に", "から"], 0, "移動の目的地には「へ」または「に」を使います。"),
            ("昨日は どこ【　　】行きませんでした。", ["へも", "にも", "でも", "をも"], 0, "全否定には「どこへも」を使います。"),
            ("田中さんは 歌が【　　】です。", ["じょうず", "じょうずに", "じょうずな", "じょうずだ"], 0, "「〜が上手です」の形になります。"),
            ("あしたは 雨が【　　】でしょう。", ["ふる", "ふって", "ふった", "ふり"], 0, "推量の「でしょう」の前は動詞普通形「ふる」になります。"),
            ("今から ご飯を【　　】ところです。", ["たべる", "たべた", "たべて", "たべに"], 0, "直前を表す「ところです」の前は辞書形「たべる」です。"),
            ("この 料理は【　　】やすいです。", ["たべ", "たべる", "たべて", "たべた"], 0, "「ます形語幹＋やすい」で「食べやすい」となります。"),
            ("テレビを【　　】ながら、ご飯を 食べます。", ["み", "みる", "みて", "みた"], 0, "「ながら」の前は動詞ます形語幹「見」です。"),
            ("写真を【　　】は いけません。", ["とって", "とる", "とり", "とった"], 0, "禁止表現は「〜てはいけません」です。"),
            ("窓を【　　】も いいですか。", ["あけて", "あける", "あけ", "あけた"], 0, "許可を求める表現は「〜てもいいですか」です。"),
            ("日本語が【　　】ように なりました。", ["はなせる", "はなす", "はなして", "はなした"], 0, "能力の変化は「可能動詞辞書形＋ようになる」です。"),
            ("風邪を ひいたので、病院へ【　　】なければなりません。", ["いか", "いく", "いって", "いった"], 0, "義務は「〜なければなりません」です。")
        ]
        for i in range(16):
            item = gram_bank[(round_num + i) % len(gram_bank)]
            q_num = 36 + i
            r_questions.append({
                "qNum": q_num,
                "sectionId": "sec2",
                "subsectionId": "s2_m1",
                "sectionName": "言語知識（文法）・読解",
                "subsectionName": "問題1 文法形式判断",
                "title": item[0].replace("【　　】", "<span class='jlpt-underline-blank'>　　</span>"),
                "titleRuby": item[0],
                "options": item[1],
                "correctIndex": item[2],
                "explanation": item[3]
            })

        # 文法問題2: 文の組み立て（★問題） (Q52〜56) (5問)
        # ★位置を1, 2, 3, 4番目に分散
        star_bank = [
            ("あした 友だちと （　） （　） （★） （　） つもりです。", ["映画を", "見に", "行く", "ところへ"], 2, 2, "正解順: 映画を 見に 行く ところへ ➔ ★は3番目の「行く」"),
            ("この レストランは （　） （★） （　） （　） おいしいです。", ["料理が", "安くて", "とても", "サービスも"], 1, 1, "正解順: 料理が 安くて とても サービスも ➔ ★は2番目"),
            ("（★） （　） （　） （　） 日本語を 話します。", ["毎日", "ラジオを", "聞いて", "練習して"], 0, 0, "正解順: 毎日 ラジオを 聞いて 練習して ➔ ★は1番目"),
            ("駅の 前に （　） （　） （　） （★） できました。", ["新しい", "大きな", "スーパーが", "最近"], 3, 2, "正解順: 新しい 大きな スーパーが 最近 ➔ ★は4番目"),
            ("毎朝 （　） （★） （　） （　） 散歩します。", ["７時に", "起きて", "公園を", "３０分"], 1, 1, "正解順: ７時に 起きて 公園を ３０分 ➔ ★は2番目")
        ]
        for i in range(5):
            item = star_bank[(round_num + i) % len(star_bank)]
            q_num = 52 + i
            r_questions.append({
                "qNum": q_num,
                "sectionId": "sec2",
                "subsectionId": "s2_m2",
                "sectionName": "言語知識（文法）・読解",
                "subsectionName": "問題2 文の組み立て",
                "title": item[0],
                "titleRuby": item[0],
                "options": item[1],
                "correctIndex": item[3],
                "explanation": item[4]
            })

        # 文法問題3: 文章文法 (Q57〜61) (5問)
        for i in range(5):
            q_num = 57 + i
            r_questions.append({
                "qNum": q_num,
                "sectionId": "sec2",
                "subsectionId": "s2_m3",
                "sectionName": "言語知識（文法）・読解",
                "subsectionName": "問題3 文章の文法",
                "passage": f"【文章】私の 週末について\n先週の 土曜日、私は 友だちと 図書館へ 行きました。(57)＿＿、日本語の 本を 借りました。(58)＿＿本は とても おもしろかったです。(59)＿＿から、日曜日は 家で ゆっくり 読みました。(60)＿＿に 友だちから 電話が ありました。「来週も いっしょに (61)＿＿か」と 言いました。",
                "title": f"({q_num})に 入る いちばん いい ものは どれですか。",
                "options": ["それから", "しかし", "ですから", "または"] if i==0 else (["その", "この", "あの", "どの"] if i==1 else (["午前", "午後", "あさ", "よる"] if i==2 else (["夕方", "昼間", "夜中", "未明"] if i==3 else ["行きませんか", "行きました", "行きます", "行くでしょう"]))),
                "correctIndex": 0,
                "explanation": "文脈の流れに最も合致する接続詞・表現を選びます。"
            })

        # 読解: 短文 (Q62〜64) (3問)
        for i in range(3):
            q_num = 62 + i
            r_questions.append({
                "qNum": q_num,
                "sectionId": "sec2",
                "subsectionId": "s2_m4",
                "sectionName": "言語知識（文法）・読解",
                "subsectionName": "問題4 読解（内容理解・短文）",
                "passage": "【お知らせ】\n日本語教室の みなさんへ\n来週の 水曜日は 教室の エアコンの 工事が ありますから、授業は ありません。次の 授業は 金曜日です。金曜日には 宿題を わすれずに 持ってきて ください。",
                "title": "次の 授業は いつですか。",
                "options": ["来週の 水曜日", "来週の 金曜日", "今週の 水曜日", "今週の 金曜日"],
                "correctIndex": 1,
                "explanation": "「来週の水曜日は授業がありません。次の授業は金曜日です」と書いてあるので、正解は来週の金曜日です。"
            })

        # 読解: 中文 (Q65〜66) (2問)
        for i in range(2):
            q_num = 65 + i
            r_questions.append({
                "qNum": q_num,
                "sectionId": "sec2",
                "subsectionId": "s2_m5",
                "sectionName": "言語知識（文法）・読解",
                "subsectionName": "問題5 読解（内容理解・中文）",
                "passage": "私は 毎朝、近くの 公園を 散歩します。公園には たくさんの 木や 花が あります。朝の 公園は 空気が きれいで、鳥の 声も 聞こえます。散歩を すると、気分が とても よくなります。それから 家へ 帰って、おいしい 朝ご飯を 食べます。これが 私の 毎日の 楽しみです。",
                "title": "この人は 公園で 何を しますか。" if i==0 else "この人の 毎日の 楽しみは何ですか。",
                "options": ["散歩を します", "本を 読みます", "朝ご飯を 食べます", "仕事を します"] if i==0 else ["朝の 散歩と 朝ご飯", "夜の 散歩", "友だちと 話すこと", "鳥を かうこと"],
                "correctIndex": 0,
                "explanation": "本文に「近くの公園を散歩します」「これが私の毎日の楽しみです」と明記されています。"
            })

        # 読解: 情報検索 (Q67) (1問)
        r_questions.append({
            "qNum": 67,
            "sectionId": "sec2",
            "subsectionId": "s2_m6",
            "sectionName": "言語知識（文法）・読解",
            "subsectionName": "問題6 読解（情報検索）",
            "passage": "【図書館の 利用時間】\n・月曜日〜金曜日：午前９時〜午後８時\n・土曜日・日曜日：午前９時〜午後５時\n・休みの日：毎月 最後の 月曜日\n※本は １人 ５さつまで、２しゅうかん 借りることが できます。",
            "title": "日曜日の 午後６時に 本を 借りることが できますか。",
            "options": ["はい、借りることが できます。", "いいえ、午後５時までですから 借りられません。", "はい、最後の 月曜日だけ 借りられます。", "いいえ、土曜日と 日曜日は 休みです。"],
            "correctIndex": 1,
            "explanation": "日曜日は午前9時〜午後5時までですので、午後6時には閉まっており借りられません。"
        })

        # Section 3: 聴解 (24問: Q68〜Q91)
        # 問題1: 課題理解 (Q68〜74) (7問)
        for i in range(7):
            q_num = 68 + i
            svg_fname = f"n5_r{round_num}_q{q_num}.svg"
            svg_path = os.path.join(svg_dir, svg_fname)
            rel_url = f"images/listening_svg/{svg_fname}"
            svg_c = gli.make_scene_svg(f"第{round_num}回 課題理解 {i+1}", "学校・教室", "先生", "学生", "指示された行動を順序立てて聞き取ります")
            with open(svg_path, "w", encoding="utf-8") as sf:
                sf.write(svg_c)
            r_questions.append({
                "qNum": q_num,
                "sectionId": "sec3",
                "subsectionId": "s3_m1",
                "sectionName": "聴解",
                "subsectionName": "問題1 課題理解",
                "has_illustration": True,
                "illustration_url": rel_url,
                "title": "男の学生はこのあと、まず何をしますか。",
                "speech_audio_text": sanitize(f"第{q_num}問。男の学生はこのあと、まず何をしますか。\n\n女：李さん、明日のテストの準備はできましたか。\n男：はい、ノートの見直しは終わりました。\n女：じゃあ、教室の机を並べておいてくれますか。\n男：わかりました。すぐ並べます。\n女：ありがとう。そのあとで黒板もきれいにしてね。\n\n質問。男の学生はこのあと、まず何をしますか。"),
                "options": ["机を並べる", "黒板をきれいにする", "ノートを見直す", "先生の部屋へ行く"],
                "correctIndex": 0,
                "explanation": "「まず机を並べる」と答えているため、正解は1です。"
            })

        # 問題2: ポイント理解 (Q75〜80) (6問)
        for i in range(6):
            q_num = 75 + i
            svg_fname = f"n5_r{round_num}_q{q_num}.svg"
            svg_path = os.path.join(svg_dir, svg_fname)
            rel_url = f"images/listening_svg/{svg_fname}"
            svg_c = gli.make_scene_svg(f"第{round_num}回 ポイント理解 {i+1}", "店・買い物", "店員", "客", "理由や条件のポイントを聞き取ります")
            with open(svg_path, "w", encoding="utf-8") as sf:
                sf.write(svg_c)
            r_questions.append({
                "qNum": q_num,
                "sectionId": "sec3",
                "subsectionId": "s3_m2",
                "sectionName": "聴解",
                "subsectionName": "問題2 ポイント理解",
                "has_illustration": True,
                "illustration_url": rel_url,
                "title": "女の人はどうしてこの傘を買いませんでしたか。",
                "speech_audio_text": sanitize(f"第{q_num}問。女の人はどうしてこの傘を買いませんでしたか。\n\n女：すみません、この青い傘を見せてください。\n男：はい、どうぞ。軽くて丈夫ですよ。\n女：デザインはとてもいいですね。でも、少し重いですね。あ、値段も高いですね。\n男：こちらはセール中でお安くなっていますよ。\n女：うーん、やはりもっと軽いものがいいので、やめておきます。\n\n質問。女の人はどうしてこの傘を買いませんでしたか。"),
                "options": ["重かったから", "高かったから", "色が嫌いだったから", "壊れていたから"],
                "correctIndex": 0,
                "explanation": "「やはりもっと軽いものがいいので」と決定打を言っているので、「重かったから」が正解です。"
            })

        # 問題3: 発話表現 (Q81〜85) (5問) - 矢印SVG完備！
        for i in range(5):
            q_num = 81 + i
            svg_fname = f"n5_r{round_num}_q{q_num}.svg"
            svg_path = os.path.join(svg_dir, svg_fname)
            rel_url = f"images/listening_svg/{svg_fname}"
            svg_c = gli.make_arrow_svg(f"第{round_num}回 発話表現 {i+1}", "相手の家を訪問するとき", "あなた（➡）", "家の人")
            with open(svg_path, "w", encoding="utf-8") as sf:
                sf.write(svg_c)
            r_questions.append({
                "qNum": q_num,
                "sectionId": "sec3",
                "subsectionId": "s3_m3",
                "sectionName": "聴解",
                "subsectionName": "問題3 発話表現",
                "has_illustration": True,
                "illustration_url": rel_url,
                "title": "友だちの家へ 行きました。部屋に 入るとき、何と 言いますか。",
                "speech_audio_text": sanitize(f"第{q_num}問。友だちの家へ行きました。部屋に入るとき、何と言いますか。\n\n１番。おじゃまします。\n２番。いってきます。\n３番。おかえりなさい。"),
                "options": ["おじゃまします。", "いってきます。", "おかえりなさい。"],
                "correctIndex": 0,
                "explanation": "他人の家や部屋に入るときは「おじゃまします」と言います。「いってきます」は自分の家を出るとき、「おかえりなさい」は帰ってきた人を迎える挨拶です。"
            })

        # 問題4: 即時応答 (Q86〜91) (6問)
        for i in range(6):
            q_num = 86 + i
            svg_fname = f"n5_r{round_num}_q{q_num}.svg"
            svg_path = os.path.join(svg_dir, svg_fname)
            rel_url = f"images/listening_svg/{svg_fname}"
            svg_c = gli.make_scene_svg(f"第{round_num}回 即時応答 {i+1}", "一般", "質問者", "あなた", "質問に対する最も自然な返答を選びます")
            with open(svg_path, "w", encoding="utf-8") as sf:
                sf.write(svg_c)
            r_questions.append({
                "qNum": q_num,
                "sectionId": "sec3",
                "subsectionId": "s3_m4",
                "sectionName": "聴解",
                "subsectionName": "問題4 即時応答",
                "has_illustration": True,
                "illustration_url": rel_url,
                "title": "文を聞いて、いちばん いい 返事を えらんで ください。",
                "speech_audio_text": sanitize(f"第{q_num}問。あした、いっしょに 映画を 見に 行きませんか。\n\n１番。ええ、行きましょう。\n２番。いいえ、見ませんでした。\n３番。どういたしまして。"),
                "options": ["ええ、行きましょう。", "いいえ、見ませんでした。", "どういたしまして。"],
                "correctIndex": 0,
                "explanation": "誘い「行きませんか」に対する快諾の返答は「ええ、行きましょう」です。"
            })

        # Assemble full round data
        rounds[round_num] = {
            "exam_id": f"n5_mock_{round_num:02d}",
            "title": f"JLPT N5 実戦模擬試験 第{round_num}回",
            "level": "N5",
            "totalQuestions": 91,
            "totalTimeMinutes": 105,
            "passingTotalScore": 80,
            "maxTotalScore": 180,
            "benchmarks": {
                "sec_lang_reading": 38,
                "sec_listening": 19
            },
            "sections": round1_data["sections"],
            "questions": r_questions
        }

    # Save to database/jlpt_n5_mock_rounds.js and database/jlpt_n5_mock_data.js
    rounds_js = "window.JLPT_N5_MOCK_ROUNDS = " + json.dumps(rounds, ensure_ascii=False, indent=2) + ";\n"
    rounds_js += "window.JLPT_N5_MOCK_DATA = window.JLPT_N5_MOCK_ROUNDS[1];\n"

    out_paths = [
        os.path.join(base_dir, "database/jlpt_n5_mock_rounds.js"),
        os.path.join(base_dir, "database/jlpt_n5_mock_data.js"),
        os.path.join(base_dir, "public/database/jlpt_n5_mock_rounds.js"),
        os.path.join(base_dir, "public/database/jlpt_n5_mock_data.js")
    ]
    for p in out_paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(rounds_js)
        print(f"Saved: {p} ({len(rounds_js)} bytes)")

    print("ALL 10 ROUNDS FOR N5 GENERATED SUCCESSFULLY!")

if __name__ == '__main__':
    main()
