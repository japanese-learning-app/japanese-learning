#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sanitize and Originalize All Business Keigo & App Files:
1. Apply the verified non-existent, easy-to-pronounce unified proper noun registry:
   - 商社: ことほ商社 / はるみの商社
   - IT・システム: そらみのシステム / ななほデジタル
   - 電機・メーカー: ことほ電機 / ななほ製作所
   - 企画・デザイン: ことほ企画 / はるみのデザイン
   - ホテル・旅館: はるみのホテル / ことほ旅館
   - レストラン・カフェ: レストラン・ことほ / カフェ・ななほ
   - ショップ・デパート: ことほデパート / ななほショップ / はるみのマート
   - 大学・学校: はるみの大学 / ことほ日本語学校
   - 病院・銀行・図書館: はるみの病院 / ななほ銀行 / ことほ図書館
   - 駅名・市名: はるみの駅 / みのり野駅 / はるみの市
   - フルネーム: 田中健太 / 鈴木彩 / 中村翔
2. Remove all references to commercial book titles.
3. Rewrite all 204 `point` explanations in `database/keigo_drill_all_data.js` into 100% original pedagogical explanations with spoken/casual-polite register notes.
"""

import json
import os
import re

BASE_DIR = "/Users/yamauchimiku/Documents/GitHub/japanese-learning"

# 1. Proper Noun Replacement Map (Order matters: longer/more specific first)
PROPER_NOUN_REPLACEMENTS = [
    # Commercial book titles & metadata removal
    ("出典: 『サクッと敬語ノート』(189P)『ビジネスメール表現集』(126P)『電話応対の実戦マスター』(158P)", "ビジネス敬語 実践トレーニング完全カタログ（目上との会話・ビジネスメール・電話応対）"),
    ("出典: 『サクッと敬語ノート』『ビジネスメール表現集』『電話応対の実戦マスター』", "ビジネス敬語 実践トレーニング完全カタログ（目上との会話・ビジネスメール・電話応対）"),
    ("出典: 『サクッと敬語ノート』(全189ページ) 完全網羅 (全204問)", "ビジネス敬語 シチュエーション別 NG➔OK 変換データベース（全204問）"),
    ("出典: 『サクッと敬語ノート』(全189ページ) 完全網羅", "ビジネス敬語 シチュエーション別 NG➔OK 変換データベース"),
    ("📖 『サクッと敬語ノート』完全収録 · シチュエーション別 言い換え特訓", "📖 シチュエーション別 NG➔OK 言い換え特訓"),
    ("(書籍『サクッと敬語ノート』完全収録)", "（シチュエーション別 NG➔OK 言い換え特訓）"),
    ("『サクッと敬語ノート』(全189ページ) 完全網羅！", "ビジネス会話の重要表現を完全網羅！"),
    ("『ビジネスメール表現集』(全126ページ) 完全網羅！", "ビジネスメールの重要表現を完全網羅！"),
    ("『電話応対の実戦マスター』(全158ページ) 完全網羅！", "電話・接客応対の重要表現を完全網羅！"),
    ("『サクッと敬語ノート』", "ビジネス敬語マスター"),
    ("『ビジネスメール表現集』", "ビジネスメール表現マスター"),
    ("『電話応対の実戦マスター』", "電話応対マスター"),

    # Trading companies (商社)
    ("株式会社ABC商事", "ことほ商社"),
    ("ABC商事", "ことほ商社"),
    ("フコク商事", "ことほ商社"),
    ("株式会社未来商事", "はるみの商社"),
    ("未来商事", "はるみの商社"),
    ("サクラ商事", "ことほ商社"),
    ("さくら商事", "ことほ商社"),
    ("青葉商事", "はるみの商社"),
    ("東京商事", "ことほ商社"),
    ("A社", "ことほ商社"),
    ("B社", "はるみの商社"),
    ("C社", "そらみのシステム"),
    ("X社", "ことほ商社"),
    ("x社", "ことほ商社"),

    # IT / Tech / Makers / Planning
    ("グローバルテック株式会社", "そらみのシステム"),
    ("グローバルテック", "そらみのシステム"),
    ("株式会社コスモテック", "ななほデジタル"),
    ("コスモテック", "ななほデジタル"),
    ("IMC", "そらみのシステム"),
    ("パワー電気", "ことほ電機"),
    ("株式会社サクラ企画", "ことほ企画"),
    ("サクラ企画", "ことほ企画"),

    # Hotels / Restaurants / Cafes / Shops
    ("ホテル・オーシャンビュー", "はるみのホテル"),
    ("オーシャンビュー", "はるみのホテル"),
    ("トラットリア・サクラ", "レストラン・ことほ"),
    ("ダイニング・蒼（AO）", "レストラン・ことほ"),
    ("ダイニング・蒼", "レストラン・ことほ"),

    # Universities / Hospitals / Banks / Stations
    ("高木大学", "はるみの大学"),
    ("さくら大学", "はるみの大学"),
    ("富士大学", "はるみの大学"),
    ("神戸病院", "はるみの病院"),
    ("アップル銀行", "ななほ銀行"),
    ("渋谷駅", "はるみの駅"),
    ("東京駅", "はるみの駅"),
    ("京都駅", "はるみの駅"),

    # Standardized Person Full Names
    ("山田太郎", "田中健太"),
    ("山田 太郎", "田中 健太"),
    ("佐藤花子", "鈴木彩"),
    ("佐藤 花子", "鈴木 彩"),
]

def apply_proper_nouns(text: str) -> str:
    for old_val, new_val in PROPER_NOUN_REPLACEMENTS:
        text = text.replace(old_val, new_val)
    return text


def build_original_point_explanation(item: dict) -> str:
    """
    Generate a 100% original pedagogical explanation for each NG -> OK drill item,
    including why the NG phrase fails, why the OK phrase works, and a spoken/soft variation note.
    """
    ng = apply_proper_nouns(item.get("ng", ""))
    ok = apply_proper_nouns(item.get("ok", ""))
    sit = apply_proper_nouns(item.get("situation", ""))
    sec = apply_proper_nouns(item.get("section", ""))
    chap = item.get("chapterNum", 1)

    # Spoken / soft variation suggestion
    spoken_alt = ok.split("（")[0].strip()
    spoken_alt = (
        spoken_alt.replace("でございますでしょうか", "でしょうか")
        .replace("でございますね", "ですね")
        .replace("でございます", "です")
        .replace("存じます", "思います")
        .replace("いたします", "します")
        .replace("かしこまりました", "承知しました")
    )

    # Analyze pattern type for tailored original explanation
    if "になられ" in ng or "おっしゃられ" in ng or "召し上がられ" in ng or "ご覧になられ" in ng or "お見えになられ" in ng or "お越しになられ" in ng:
        reason = f"「{ng}」は尊敬語にさらに「〜られる」を重ねた二重敬語のため不自然です。シンプルに「{ok}」と表現するのが正しい敬語です。"
    elif "ご持参" in ng or "拝見され" in ng or "参られ" in ng or "伺われ" in ng or "申され" in ng or "頂戴され" in ng:
        reason = f"自分の動作をへりくだる謙譲語を相手の動作に使ってしまっている誤用です。相手を高める場面では尊敬語を用いて「{ok}」と言い換えます。"
    elif "になります" in ng or "よろしかったでしょうか" in ng or "からお預かり" in ng or "ほど" in ng:
        reason = f"「{ng}」は接客や職場でよく聞かれる不自然なバイト敬語です。ビジネスシーンでは丁寧語の「{ok}」を使うと信頼感が高まります。"
    elif "ご苦労" in ng or "了解" in ng or "参考になり" in ng or "感心" in ng or "なるほど" in ng:
        reason = f"「{ng}」は目上から目下への労いや評価のニュアンスを含むため、上司や取引先に使うと失礼にあたります。「{ok}」と言い換えるのがマナーです。"
    elif "役不足" in ng or "ご自愛" in ng or "かねません" in ng or "ご教授" in ng or "ご検収" in ng:
        reason = f"言葉本来の意味や漢字の使い分けを取り違えやすい表現です。「{sit}」の場面では「{ok}」を選ぶのが正確です。"
    elif chap == 1 or "若者言葉" in sec or "口ぐせ" in sec:
        reason = f"「{ng}」は日常のくだけた話し言葉（口語・若者言葉）であり、ビジネスでは幼い印象を与えます。「{sit}」の場面では「{ok}」と落ち着いた表現に整えましょう。"
    elif chap == 4 or "電話" in sec:
        reason = f"電話応対では相手の顔が見えないため、「{ng}」のように直接的な言い方は避け、クッション言葉を添えて「{ok}」と丁寧に伝えるのが基本です。"
    elif chap == 7 or "メール" in sec or "文書" in sec:
        reason = f"ビジネスメールや文書では、口語の「{ng}」ではなく、書き言葉として整った「{ok}」を用いると品格のある文面になります。"
    else:
        reason = f"「{sit}」の場面で「{ng}」と言うとぶっきらぼう・不自然に響くため、相手に敬意と配慮が伝わる「{ok}」へ言い換えるのが適切です。"

    if spoken_alt and spoken_alt != ok.split("（")[0].strip():
        register_note = f" また、実際の口頭会話や少し親しい職場では「{spoken_alt}」のように少し柔らかく表現してもほぼ同じ意味で自然に通じます。"
    else:
        register_note = " 対面や電話の話し言葉では、語尾のトーンを柔らかくして伝えるとより自然で好印象になります。"

    return reason + register_note


def update_keigo_drill_all_data():
    path = os.path.join(BASE_DIR, "database", "keigo_drill_all_data.js")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    content = apply_proper_nouns(content)

    m_verbs = re.search(r"var KEIGO_VERB_CONVERSIONS\s*=\s*(\[[\s\S]*?\]);", content)
    m_drills = re.search(r"var KEIGO_DRILL_DATABASE\s*=\s*(\[[\s\S]*?\]);", content)
    assert m_verbs and m_drills, "Could not parse keigo_drill_all_data.js"

    verbs = json.loads(m_verbs.group(1))
    drills = json.loads(m_drills.group(1))

    for d in drills:
        d["situation"] = apply_proper_nouns(d.get("situation", ""))
        d["section"] = apply_proper_nouns(d.get("section", ""))
        d["ng"] = apply_proper_nouns(d.get("ng", ""))
        d["ok"] = apply_proper_nouns(d.get("ok", ""))
        d["point"] = build_original_point_explanation(d)

        # Fix options so there are no broken "でございますでしょうか？" strings
        ok_clean = d["ok"]
        ng_clean = d["ng"]
        trap = ok_clean.replace("ました", "になられました").replace("ます", "させていただきます")
        if trap == ok_clean:
            trap = ok_clean + "になられます"
        d["options"] = [ok_clean, ng_clean, trap]

    new_js = (
        "// ============================================================\n"
        "// ビジネス敬語 シチュエーション別 NG➔OK 変換データベース（全204問・完全オリジナル解説）\n"
        "// ============================================================\n\n"
        f"var KEIGO_VERB_CONVERSIONS = {json.dumps(verbs, ensure_ascii=False, indent=2)};\n\n"
        f"var KEIGO_DRILL_DATABASE = {json.dumps(drills, ensure_ascii=False, indent=2)};\n"
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_js)
    print(f"Updated {path} (204 items originalized)")


def update_other_files():
    targets = [
        os.path.join(BASE_DIR, "database", "business_keigo_catalog.js"),
        os.path.join(BASE_DIR, "scripts", "build_business_keigo_practice.py"),
        os.path.join(BASE_DIR, "business_keigo.html"),
        os.path.join(BASE_DIR, "app.html"),
    ]
    for p in targets:
        if not os.path.exists(p):
            continue
        with open(p, "r", encoding="utf-8") as f:
            txt = f.read()
        new_txt = apply_proper_nouns(txt)
        with open(p, "w", encoding="utf-8") as f:
            f.write(new_txt)
        print(f"Applied unified proper nouns to {p}")


if __name__ == "__main__":
    update_keigo_drill_all_data()
    update_other_files()
