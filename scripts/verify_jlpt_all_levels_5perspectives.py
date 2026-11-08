# -*- coding: utf-8 -*-
"""
Final 5-Perspective Comprehensive Verification Script across all JLPT N5, N4, N3, N2, N1
Datasets, Audio Files, Illustrations, Ruby Annotations, Answers, Naturalness, and Coverage.
"""

import os
import sys
import re
import json

BASE_DIR = "/Users/yamauchimiku/Documents/GitHub/japanese-learning"

LEVELS = ["n5", "n4", "n3", "n2", "n1"]
BANNED_TERMS = ["公式", "準拠", "Google", "Neural2", "LINE", "Zoom", "YouTube", "Netflix", "Amazon", "Facebook", "Twitter", "Instagram", "TikTok"]
SENSITIVE_PATTERNS = [
    r"戦争", r"戦時中", r"軍隊", r"兵士", r"植民地", r"原爆", r"テロ", r"虐殺",
    r"領土問題", r"独島", r"竹島", r"尖閣", r"靖国"
]
MECHANICAL_TEMPLATES = [
    "先生や友達と一緒に",
    "毎日しっかりと練習を続けて、上手に",
    "図書館で日本の文化や",
    "ニュースで",
    "将来の夢を叶えるために、今から少しずつ",
    "この言葉は日常会話やニュースなどでよく使われる大切な表現です",
]


def load_js_json(filepath, var_prefix=None):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    if var_prefix:
        m = re.search(re.escape(var_prefix) + r"\s*=\s*(\{|\[)", text)
    else:
        m = re.search(r"=\s*(\{|\[)", text)
    if not m:
        raise ValueError(f"Could not find JSON start in {filepath}")
    start_idx = m.start(1)
    decoder = json.JSONDecoder()
    obj, _ = decoder.raw_decode(text[start_idx:])
    return obj, text


def check_sync(rel_path, errors):
    main_p = os.path.join(BASE_DIR, rel_path)
    pub_p = os.path.join(BASE_DIR, "public", rel_path)
    if not os.path.exists(main_p):
        errors.append(f"Missing main file: {rel_path}")
        return
    if not os.path.exists(pub_p):
        errors.append(f"Missing public mirror file: public/{rel_path}")
        return
    with open(main_p, "rb") as f1, open(pub_p, "rb") as f2:
        if f1.read() != f2.read():
            errors.append(f"Out of sync between {rel_path} and public/{rel_path}")


def main():
    print("=" * 80)
    print("JLPT N5〜N1 全データ・音声・イラスト・ルビ・模擬試験 5視点最終総合検証")
    print("=" * 80)

    errors = []
    stats = {}

    for lv in LEVELS:
        lv_up = lv.upper()
        stats[lv_up] = {}

        # 1. Check file sync between main and public/
        db_files = [
            f"database/jlpt_{lv}_listening_data.js",
            f"database/jlpt_{lv}_reading_data.js",
            f"database/jlpt_{lv}_grammar_details.js",
            f"database/jlpt_{lv}_grammar_quiz_data.js",
            f"database/jlpt_{lv}_vocab_full_data.js",
            f"database/jlpt_{lv}_vocab_quiz_data.js",
            f"database/jlpt_{lv}_mock_rounds.js",
            f"database/jlpt_{lv}_mock_data.js",
        ]
        for dbf in db_files:
            check_sync(dbf, errors)

        html_files = [
            f"jlpt_{lv}_listening.html",
            f"jlpt_{lv}_reading.html",
            f"jlpt_{lv}_mock.html",
        ]
        for hf in html_files:
            check_sync(hf, errors)

        # 2. Listening Practice Data Audit
        l_path = os.path.join(BASE_DIR, f"database/jlpt_{lv}_listening_data.js")
        l_data, l_raw = load_js_json(l_path)
        l_qs = l_data["questions"] if isinstance(l_data, dict) and "questions" in l_data else l_data
        stats[lv_up]["listening_qs"] = len(l_qs)
        for q in l_qs:
            qid = f"{lv_up}_Listening_Q{q.get('id', q.get('qNum'))}"
            audio_url = q.get("audio_file") or q.get("audio_url") or q.get("audioUrl") or ""
            illus_url = q.get("illustration_url") or q.get("illustrationUrl") or ""
            if not audio_url or not os.path.exists(os.path.join(BASE_DIR, audio_url)):
                errors.append(f"{qid}: missing audio {audio_url}")
            elif os.path.getsize(os.path.join(BASE_DIR, audio_url)) < 2000:
                errors.append(f"{qid}: audio file too small {audio_url}")
            if not illus_url or not os.path.exists(os.path.join(BASE_DIR, illus_url)):
                errors.append(f"{qid}: missing illustration {illus_url}")
            script_txt = q.get("dialogue_script") or q.get("script") or q.get("speech_audio_text") or ""
            if re.search(r'(?:^|[\s「（『。！？\n：])あ、', script_txt):
                errors.append(f"{qid}: standalone 'あ、' found in listening script")

        # 3. Reading Practice Data Audit
        r_path = os.path.join(BASE_DIR, f"database/jlpt_{lv}_reading_data.js")
        r_data, r_raw = load_js_json(r_path)
        r_passages = r_data["passages"] if isinstance(r_data, dict) and "passages" in r_data else r_data
        r_q_count = sum(len(p.get("questions", [])) for p in r_passages)
        stats[lv_up]["reading_passages"] = len(r_passages)
        stats[lv_up]["reading_qs"] = r_q_count

        # 4. Grammar Details & Grammar Quiz Audit
        gd_path = os.path.join(BASE_DIR, f"database/jlpt_{lv}_grammar_details.js")
        gd_data, gd_raw = load_js_json(gd_path)
        gd_items = gd_data["items"] if isinstance(gd_data, dict) and "items" in gd_data else (list(gd_data.values()) if isinstance(gd_data, dict) else gd_data)
        stats[lv_up]["grammar_details"] = len(gd_items)

        gq_path = os.path.join(BASE_DIR, f"database/jlpt_{lv}_grammar_quiz_data.js")
        gq_data, gq_raw = load_js_json(gq_path)
        gq_items = gq_data["questions"] if isinstance(gq_data, dict) and "questions" in gq_data else gq_data
        stats[lv_up]["grammar_quiz"] = len(gq_items)

        # 5. Vocab Full Data & Vocab Quiz Audit
        vf_path = os.path.join(BASE_DIR, f"database/jlpt_{lv}_vocab_full_data.js")
        vf_data, vf_raw = load_js_json(vf_path, var_prefix=f"JLPT_{lv_up}_VOCAB_DATA")
        vf_items = vf_data["cards"] if isinstance(vf_data, dict) and "cards" in vf_data else vf_data
        stats[lv_up]["vocab_cards"] = len(vf_items)
        for idx, card in enumerate(vf_items):
            ex = card.get("example_ja") or card.get("example") or ""
            for mt in MECHANICAL_TEMPLATES:
                if mt in ex:
                    errors.append(f"{lv_up}_VocabCard_{idx}: contains mechanical template '{mt}'")

        vq_path = os.path.join(BASE_DIR, f"database/jlpt_{lv}_vocab_quiz_data.js")
        vq_data, vq_raw = load_js_json(vq_path)
        vq_items = vq_data["questions"] if isinstance(vq_data, dict) and "questions" in vq_data else vq_data
        stats[lv_up]["vocab_quiz"] = len(vq_items)

        # 6. Mock Exam 10 Rounds Audit
        mr_path = os.path.join(BASE_DIR, f"database/jlpt_{lv}_mock_rounds.js")
        mr_data, mr_raw = load_js_json(mr_path)
        if len(mr_data) != 10:
            errors.append(f"{lv_up}_Mock: expected 10 rounds, got {len(mr_data)}")
        total_mock_qs = 0
        mock_audio_checked = set()
        for r_key, r_obj in mr_data.items():
            qs = r_obj["questions"]
            total_mock_qs += len(qs)
            if r_obj.get("totalQuestions") != len(qs):
                errors.append(f"{lv_up}_Mock_R{r_key}: totalQuestions={r_obj.get('totalQuestions')} != len(qs)={len(qs)}")
            for q in qs:
                qid = f"{lv_up}_Mock_R{r_key}_Q{q['qNum']}"
                opts = q["options"]
                c_idx = q["correctIndex"]
                if len(set(opts)) != len(opts):
                    errors.append(f"{qid}: duplicate options {opts}")
                if not (0 <= c_idx < len(opts)):
                    errors.append(f"{qid}: invalid correctIndex {c_idx}")
                if q["sectionId"] == "sec3":
                    a_url = q.get("audioUrl", "")
                    i_url = q.get("illustration_url", "")
                    if not a_url or not os.path.exists(os.path.join(BASE_DIR, a_url)):
                        errors.append(f"{qid}: missing mock audio {a_url}")
                    elif os.path.getsize(os.path.join(BASE_DIR, a_url)) < 2000:
                        errors.append(f"{qid}: mock audio too small {a_url}")
                    else:
                        mock_audio_checked.add(a_url)
                    if not i_url or not os.path.exists(os.path.join(BASE_DIR, i_url)):
                        errors.append(f"{qid}: missing mock illustration {i_url}")
                    if re.search(r'(?:^|[\s「（『。！？\n：])あ、', q.get("script", "")):
                        errors.append(f"{qid}: standalone 'あ、' in mock listening script")

        stats[lv_up]["mock_rounds"] = len(mr_data)
        stats[lv_up]["mock_total_qs"] = total_mock_qs
        stats[lv_up]["mock_audio_files"] = len(mock_audio_checked)

        # 7. Check Banned Meta-Terms & Sensitive Patterns across all raw JS for this level
        for dbf in db_files:
            full_p = os.path.join(BASE_DIR, dbf)
            with open(full_p, "r", encoding="utf-8") as f:
                raw_txt = f.read()
            # Strip comment header line 1 before checking
            body_txt = "\n".join(raw_txt.splitlines()[1:])
            for bw in BANNED_TERMS:
                if bw in body_txt:
                    errors.append(f"{dbf}: contains banned term '{bw}'")
            for sp in SENSITIVE_PATTERNS:
                if re.search(sp, body_txt):
                    errors.append(f"{dbf}: matches sensitive pattern '{sp}'")
            if "<ruby>日本<rt>にっぽん</rt></ruby>" in body_txt:
                errors.append(f"{dbf}: contains <ruby>日本<rt>にっぽん</rt></ruby>")
            if "<ruby>怒<rt>いか</rt></ruby>ら" in body_txt or "<ruby>怒<rt>いか</rt></ruby>りま" in body_txt:
                errors.append(f"{dbf}: contains misread 怒(いか) verb")

    check_sync("jlpt_practice.html", errors)

    print("\n--- Summary of Verified Datasets (N5〜N1) ---")
    grand_mock_qs = 0
    grand_vocab_cards = 0
    grand_grammar_quiz = 0
    grand_vocab_quiz = 0
    for lv_up in ["N5", "N4", "N3", "N2", "N1"]:
        st = stats[lv_up]
        grand_mock_qs += st["mock_total_qs"]
        grand_vocab_cards += st["vocab_cards"]
        grand_grammar_quiz += st["grammar_quiz"]
        grand_vocab_quiz += st["vocab_quiz"]
        print(
            f"  [{lv_up}] Listening: {st['listening_qs']} Qs | Reading: {st['reading_passages']} passages ({st['reading_qs']} Qs) | "
            f"Grammar: {st['grammar_details']} items / {st['grammar_quiz']} quiz Qs | "
            f"Vocab: {st['vocab_cards']} cards / {st['vocab_quiz']} quiz Qs | "
            f"Mock Exams: {st['mock_rounds']} rounds ({st['mock_total_qs']} Qs, {st['mock_audio_files']} audio MP3s)"
        )

    print("-" * 80)
    print(f"  Total Mock Exam Questions (50 Rounds): {grand_mock_qs:,} questions")
    print(f"  Total Vocabulary Cards (N5〜N1):        {grand_vocab_cards:,} cards")
    print(f"  Total Grammar Quiz Questions (N5〜N1):  {grand_grammar_quiz:,} questions")
    print(f"  Total Vocab Quiz Questions (N5〜N1):    {grand_vocab_quiz:,} questions")
    print("-" * 80)

    if errors:
        print(f"❌ ERRORS FOUND ({len(errors)}):")
        for e in errors[:40]:
            print("  -", e)
        sys.exit(1)
    else:
        print("✅ [5-PERSPECTIVE AUDIT PASSED] ZERO errors across all N5〜N1 datasets, audio files, illustrations, ruby annotations, and 50 mock exam rounds!")


if __name__ == "__main__":
    main()
