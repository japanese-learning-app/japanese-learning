#!/usr/bin/env python3
import json
import os
import re

REPO_ROOT = '/Users/yamauchimiku/Documents/GitHub/japanese-learning'
TSV_PATH = '/tmp/student_0027_tsv.txt'

def main():
    with open(TSV_PATH, 'r', encoding='utf-8') as f:
        lines = [l.strip() for l in f if l.strip()]

    print(f"Total lines read from TSV: {len(lines)}")
    cards = []
    card_ids = []

    for i, line in enumerate(lines, 1):
        parts = line.split('\t')
        col0 = parts[0].strip()
        col1 = parts[1].strip() if len(parts) > 1 else ''
        col2 = parts[2].strip() if len(parts) > 2 else ''
        col3 = parts[3].strip() if len(parts) > 3 else ''
        col4 = parts[4].strip() if len(parts) > 4 else ''

        # Extract word and reading
        m = re.match(r'^(.*?)[（\(](.*?)[）\)]$', col0)
        if m:
            word = m.group(1).strip()
            reading = m.group(2).strip()
        else:
            word = col0
            reading = col0

        meaning_en = col1
        related = col4
        
        # Nuance / Distinction Guard: Ensure 'vs' difference explanation never leaks into meaning
        if re.search(r'\bvs\b|【使い分け】', meaning_en):
            print(f"Row {i} ({word}): Found 'vs' in meaning col: '{meaning_en}'. Relocating to related!")
            if not related:
                related = meaning_en
            else:
                related = f"{meaning_en}\n{related}"
            meaning_en = word

        card_id = f"class_word_0027_{str(i).zfill(4)}"
        card_ids.append(card_id)

        card_obj = {
            "id": card_id,
            "word": word,
            "reading": reading,
            "category": "授業で習った言葉",
            "studentId": "0027",
            "meaning": {
                "en": meaning_en,
                "ja": word,
                "zh_TW": meaning_en,
                "zh_CN": meaning_en,
                "ko": meaning_en,
                "zh_HK": meaning_en,
                "fr": meaning_en
            },
            "example": {
                "ja": col2,
                "en": col3,
                "zh_TW": col3,
                "zh_CN": col3,
                "ko": col3,
                "zh_HK": col3,
                "fr": col3
            },
            "related": related or f"{reading}（授業の重要表現）"
        }
        cards.append(card_obj)

    print(f"Generated {len(cards)} card objects.")
    print("Sample Card 39 (混ざる):")
    print(json.dumps(cards[38], ensure_ascii=False, indent=2))
    print("Sample Card 40 (混ぜる):")
    print(json.dumps(cards[39], ensure_ascii=False, indent=2))

    # Append to database/class_vocab_data.js and public/database/class_vocab_data.js
    cv_paths = [
        os.path.join(REPO_ROOT, 'database/class_vocab_data.js'),
        os.path.join(REPO_ROOT, 'public/database/class_vocab_data.js')
    ]

    for p in cv_paths:
        with open(p, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already added
        if 'class_word_0027_0001' in content:
            print(f"Removing previous 0027 cards from {p}...")
            content = re.sub(r',\s*// --- Student 0027 Curated Cards.*?window\.CLASS_0027_IDS\s*=\s*\[[^\]]+\];\n?', '', content, flags=re.DOTALL)

        # Build cards JS
        cards_js_lines = []
        for c in cards:
            cards_js_lines.append("  " + json.dumps(c, ensure_ascii=False, indent=2).replace("\n", "\n  ") + ",")
        cards_block = "\n" + "\n".join(cards_js_lines)

        # Insert before closing ]; of window.CLASS_VOCAB_DATA
        pos = content.rfind('];\n\nwindow.CLASS_ARUN_IDS')
        if pos == -1:
            pos = content.rfind('];\nwindow.CLASS_ARUN_IDS')
        if pos == -1:
            pos = content.rfind('];')

        injection = f",\n  // --- Student 0027 Curated Cards ({len(cards)} words) ---{cards_block}\n"
        content = content[:pos] + injection + content[pos:]

        # Also append window.CLASS_0027_IDS
        ids_js = f"\nwindow.CLASS_0027_IDS = {json.dumps(card_ids)};\n"
        content += ids_js

        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {p} successfully!")

    # Check js/app.js and public/js/app.js for student 0027 mapping
    app_paths = [
        os.path.join(REPO_ROOT, 'js/app.js'),
        os.path.join(REPO_ROOT, 'public/js/app.js')
    ]
    for ap in app_paths:
        with open(ap, 'r', encoding='utf-8') as f:
            app_text = f.read()

        target_hook = "if (stId === '0023') {"
        new_hook = """if (stId === '0027') {
          const ids0027 = window.CLASS_0027_IDS || [];
          ids0027.forEach(cId => studentCardIds.add(cId));
        }
        if (stId === '0023') {"""
        if "if (stId === '0027')" not in app_text and target_hook in app_text:
            app_text = app_text.replace(target_hook, new_hook, 1)
            with open(ap, 'w', encoding='utf-8') as f:
                f.write(app_text)
            print(f"Updated studentCardIds hook in {ap}")

if __name__ == '__main__':
    main()
