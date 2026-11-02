# -*- coding: utf-8 -*-
"""
Integrator for Sections 44 to 51
"""

import json
import re
import os

from data_builder_kanou import SEC_44_CARDS, SEC_45_CARDS, SEC_46_CARDS
from data_builder_ta1_2 import SEC_47_CARDS, SEC_48_CARDS
from data_builder_ta3_4_5 import SEC_49_CARDS, SEC_50_CARDS, SEC_51_CARDS

SECTION_CONFIGS = [
    (44, "基本動詞 可能形 (3)", SEC_44_CARDS),
    (45, "基本動詞 可能形 (4)", SEC_45_CARDS),
    (46, "基本動詞 可能形 (5)", SEC_46_CARDS),
    (47, "基本動詞 たform (1)", SEC_47_CARDS),
    (48, "基本動詞 たform (2)", SEC_48_CARDS),
    (49, "基本動詞 たform (3)", SEC_49_CARDS),
    (50, "基本動詞 たform (4)", SEC_50_CARDS),
    (51, "基本動詞 たform (5)", SEC_51_CARDS),
]

def parse_js_array(content, prefix):
    start = content.find(prefix)
    if start == -1:
        raise ValueError(f"Prefix '{prefix}' not found")
    depth = 0
    in_string = False
    escape = False
    quote_char = None
    array_start = start + len(prefix)
    end = -1

    for i in range(array_start, len(content)):
        c = content[i]
        if escape:
            escape = False
            continue
        if c == '\\':
            escape = True
            continue
        if in_string:
            if c == quote_char:
                in_string = False
            continue
        else:
            if c in ('"', "'"):
                in_string = True
                quote_char = c
                continue
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
    if end == -1:
        raise ValueError(f"Could not find matching bracket for array starting at {array_start}")
    data = json.loads(content[array_start:end])
    return array_start, end, data

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    data_js_path = os.path.join(root_dir, 'js', 'data.js')
    public_data_js_path = os.path.join(root_dir, 'public', 'js', 'data.js')
    sections_catalog_path = os.path.join(root_dir, 'database', 'sections_catalog.json')
    app_js_path = os.path.join(root_dir, 'js', 'app.js')
    index_html_path = os.path.join(root_dir, 'index.html')

    with open(data_js_path, 'r', encoding='utf-8') as f:
        data_js_content = f.read()

    # 1. Parse INITIAL_VOCAB_DATA
    vocab_start, vocab_end, vocab_data = parse_js_array(data_js_content, 'window.INITIAL_VOCAB_DATA = ')
    print(f"Loaded existing vocab data: {len(vocab_data)} cards")

    # Update folder_name for existing folder_4 items (31-43) to '初級 31-51'
    for c in vocab_data:
        if c.get('folder_id') == 'folder_4':
            c['folder_name'] = '初級 31-51'

    # Build new cards
    new_cards = []
    current_id_num = len(vocab_data) + 1  # 1019

    for sec_num, sec_title, card_list in SECTION_CONFIGS:
        print(f"Processing Section {sec_num}: {sec_title} ({len(card_list)} cards)")
        for card_def in card_list:
            card_id = f"card_{current_id_num:04d}"
            card_obj = {
                "id": card_id,
                "section_num": sec_num,
                "section_title": sec_title,
                "folder_id": "folder_4",
                "folder_name": "初級 31-51",
                "word": card_def["word"],
                "reading": card_def["reading"],
                "category": card_def["category"],
                "meaning": card_def["meaning"],
                "example": card_def["example"],
                "related": card_def["related"]
            }
            new_cards.append(card_obj)
            current_id_num += 1

    print(f"Total new cards generated: {len(new_cards)} (expected: 169)")
    all_vocab_data = vocab_data + new_cards
    print(f"Total cards after addition: {len(all_vocab_data)} (expected: 1187)")

    # 2. Parse SECTIONS_DATA
    sec_start, sec_end, sections_data = parse_js_array(data_js_content, 'window.SECTIONS_DATA = ')
    print(f"Loaded existing sections data: {len(sections_data)} sections")

    # Update folder_name for existing folder_4 sections to '初級 31-51'
    for s in sections_data:
        if s.get('folder_id') == 'folder_4':
            s['folder_name'] = '初級 31-51'

    # Add new sections
    for sec_num, sec_title, card_list in SECTION_CONFIGS:
        sections_data.append({
            "num": sec_num,
            "title": sec_title,
            "folder_id": "folder_4",
            "folder_name": "初級 31-51",
            "count": len(card_list)
        })
    print(f"Total sections after addition: {len(sections_data)} (expected: 52, 0 to 51)")

    # Reconstruct data.js content
    # Note: Replace SECTIONS_DATA first if sec_start > vocab_start to preserve indices
    # Actually, let's replace by slicing properly
    assert sec_start > vocab_end, "SECTIONS_DATA expected after INITIAL_VOCAB_DATA"

    vocab_json_str = json.dumps(all_vocab_data, ensure_ascii=False, indent=2)
    sec_json_str = json.dumps(sections_data, ensure_ascii=False, indent=2)

    new_data_js_content = (
        data_js_content[:vocab_start]
        + vocab_json_str
        + data_js_content[vocab_end:sec_start]
        + sec_json_str
        + data_js_content[sec_end:]
    )

    # Write js/data.js
    with open(data_js_path, 'w', encoding='utf-8') as f:
        f.write(new_data_js_content)
    print(f"Wrote updated {data_js_path}")

    # Write public/js/data.js
    with open(public_data_js_path, 'w', encoding='utf-8') as f:
        f.write(new_data_js_content)
    print(f"Wrote updated {public_data_js_path}")

    # 3. Update database/sections_catalog.json
    with open(sections_catalog_path, 'w', encoding='utf-8') as f:
        json.dump(sections_data, f, ensure_ascii=False, indent=2)
    print(f"Wrote updated {sections_catalog_path}")

    # 4. Update js/app.js
    with open(app_js_path, 'r', encoding='utf-8') as f:
        app_js_content = f.read()

    # Update folder_4 configuration
    # Find FOLDER_CONFIGS
    old_folder4_pattern = re.compile(
        r"{\s*id:\s*'folder_4',\s*title:\s*'初級 31-43',\s*desc:\s*'[^\']*',\s*range:\s*\[31,\s*43\],.*?}",
        re.DOTALL
    )
    new_folder4_text = """{
      id: 'folder_4',
      title: '初級 31-51',
      desc: 'て形応用・動詞4/5・病気・ない形・可能形・た形',
      range: [31, 51],
      badge: 'STAGE 4',
      trans: {
        en: 'Beginner 31-51',
        zh_TW: '初級 31-51',
        zh_CN: '初级 31-51',
        ko: '초급 31-51',
        zh_HK: '初級 31-51',
        fr: 'Débutant 31-51'
      }
    }"""
    app_js_content = old_folder4_pattern.sub(new_folder4_text, app_js_content)

    # Update MASTER_SECTIONS_CATALOG
    old_master_end = "{ num: 43, title: '基本動詞 可能形 (2)', folder_id: 'folder_4' }"
    new_master_additions = """{ num: 43, title: '基本動詞 可能形 (2)', folder_id: 'folder_4' },
    { num: 44, title: '基本動詞 可能形 (3)', folder_id: 'folder_4' },
    { num: 45, title: '基本動詞 可能形 (4)', folder_id: 'folder_4' },
    { num: 46, title: '基本動詞 可能形 (5)', folder_id: 'folder_4' },
    { num: 47, title: '基本動詞 たform (1)', folder_id: 'folder_4' },
    { num: 48, title: '基本動詞 たform (2)', folder_id: 'folder_4' },
    { num: 49, title: '基本動詞 たform (3)', folder_id: 'folder_4' },
    { num: 50, title: '基本動詞 たform (4)', folder_id: 'folder_4' },
    { num: 51, title: '基本動詞 たform (5)', folder_id: 'folder_4' }"""
    if old_master_end in app_js_content:
        app_js_content = app_js_content.replace(old_master_end, new_master_additions, 1)
        print("Updated MASTER_SECTIONS_CATALOG in app.js")
    else:
        print("WARNING: old_master_end not found in app.js")

    # Update SECTION_TRANSLATIONS
    old_trans_end = "43: { en: 'Basic Verbs 2 (Potential)', zh_TW: '基本動詞 2（可能形）', zh_CN: '基本动词 2（可能形）', ko: '기본 동사 2 (가능형)', zh_HK: '基本動詞 2（可能形）', fr: 'Verbes de base 2 (forme potentielle)' }"
    new_trans_additions = """43: { en: 'Basic Verbs 2 (Potential)', zh_TW: '基本動詞 2（可能形）', zh_CN: '基本动词 2（可能形）', ko: '기본 동사 2 (가능형)', zh_HK: '基本動詞 2（可能形）', fr: 'Verbes de base 2 (forme potentielle)' },
    44: { en: 'Basic Verbs 3 (Potential)', zh_TW: '基本動詞 3（可能形）', zh_CN: '基本动词 3（可能形）', ko: '기본 동사 3 (가능형)', zh_HK: '基本動詞 3（可能形）', fr: 'Verbes de base 3 (forme potentielle)' },
    45: { en: 'Basic Verbs 4 (Potential)', zh_TW: '基本動詞 4（可能形）', zh_CN: '基本动词 4（可能形）', ko: '기본 동사 4 (가능형)', zh_HK: '基本動詞 4（可能形）', fr: 'Verbes de base 4 (forme potentielle)' },
    46: { en: 'Basic Verbs 5 (Potential)', zh_TW: '基本動詞 5（可能形）', zh_CN: '基本动词 5（可能形）', ko: '기본 동사 5 (가능형)', zh_HK: '基本動詞 5（可能形）', fr: 'Verbes de base 5 (forme potentielle)' },
    47: { en: 'Basic Verbs 1 (Ta-form / Past)', zh_TW: '基本動詞 1（た形／過去式）', zh_CN: '基本动词 1（た形／过去式）', ko: '기본 동사 1 (과거/다형)', zh_HK: '基本動詞 1（た形／過去式）', fr: 'Verbes de base 1 (forme en -ta / passé)' },
    48: { en: 'Basic Verbs 2 (Ta-form / Past)', zh_TW: '基本動詞 2（た形／過去式）', zh_CN: '基本动词 2（た形／过去式）', ko: '기본 동사 2 (과거/다형)', zh_HK: '基本動詞 2（た形／過去式）', fr: 'Verbes de base 2 (forme en -ta / passé)' },
    49: { en: 'Basic Verbs 3 (Ta-form / Past)', zh_TW: '基本動詞 3（た形／過去式）', zh_CN: '基本动词 3（た形／过去式）', ko: '기본 동사 3 (과거/다형)', zh_HK: '基本動詞 3（た形／過去式）', fr: 'Verbes de base 3 (forme en -ta / passé)' },
    50: { en: 'Basic Verbs 4 (Ta-form / Past)', zh_TW: '基本動詞 4（た形／過去式）', zh_CN: '基本动词 4（た形／过去式）', ko: '기본 동사 4 (과거/다형)', zh_HK: '基本動詞 4（た形／過去式）', fr: 'Verbes de base 4 (forme en -ta / passé)' },
    51: { en: 'Basic Verbs 5 (Ta-form / Past)', zh_TW: '基本動詞 5（た形／過去式）', zh_CN: '基本动词 5（た形／过去式）', ko: '기본 동사 5 (과거/다형)', zh_HK: '基本動詞 5（た形／過去式）', fr: 'Verbes de base 5 (forme en -ta / passé)' }"""
    if old_trans_end in app_js_content:
        app_js_content = app_js_content.replace(old_trans_end, new_trans_additions, 1)
        print("Updated SECTION_TRANSLATIONS in app.js")
    else:
        print("WARNING: old_trans_end not found in app.js")

    with open(app_js_path, 'w', encoding='utf-8') as f:
        f.write(app_js_content)
    print(f"Wrote updated {app_js_path}")

    # 5. Update index.html version query
    with open(index_html_path, 'r', encoding='utf-8') as f:
        index_html_content = f.read()

    index_html_content = re.sub(
        r'<script src="js/data\.js\?v=[^"]*"></script>',
        '<script src="js/data.js?v=20261102_2005"></script>',
        index_html_content
    )
    with open(index_html_path, 'w', encoding='utf-8') as f:
        f.write(index_html_content)
    print(f"Wrote updated {index_html_path}")

    print("ALL FILES SUCCESSFULLY UPDATED!")

if __name__ == '__main__':
    main()
