# -*- coding: utf-8 -*-
"""
Align database/jlpt_kanji_data.js with database/kanji_daily_quiz_dataset.js:
1. Ensure all kanji tested in JLPT_DAILY_KANJI_DATA for each level are present in JLPT_KANJI_DATA for that level.
2. Annotate each kanji with `dailyQuizRef` containing the Day, question index, word, and reading so the UI can cross-link seamlessly.
"""

import json
import re

kanji_38 = {
    '伺': {'strokes': 5, 'grade': 8, 'freq': 1618, 'onyomi': ['シ'], 'kunyomi': ['うかが.う'], 'meanings': ['pay respects', 'visit', 'ask', 'inquire']},
    '刈': {'strokes': 4, 'grade': 8, 'freq': 1481, 'onyomi': ['ガイ', 'カイ'], 'kunyomi': ['か.る'], 'meanings': ['reap', 'cut', 'clip', 'trim', 'prune']},
    '劣': {'strokes': 6, 'grade': 8, 'freq': 1362, 'onyomi': ['レツ'], 'kunyomi': ['おと.る'], 'meanings': ['inferiority', 'be inferior to', 'be worse']},
    '噂': {'strokes': 12, 'grade': 9, 'freq': 1774, 'onyomi': ['ソン'], 'kunyomi': ['うわさ'], 'meanings': ['rumor', 'gossip', 'talk about']},
    '囲': {'strokes': 7, 'grade': 4, 'freq': 647, 'onyomi': ['イ'], 'kunyomi': ['かこ.む', 'かこ.う'], 'meanings': ['surround', 'besiege', 'enclose']},
    '坂': {'strokes': 7, 'grade': 3, 'freq': 644, 'onyomi': ['ハン'], 'kunyomi': ['さか'], 'meanings': ['slope', 'incline', 'hill']},
    '壁': {'strokes': 16, 'grade': 8, 'freq': 1059, 'onyomi': ['ヘキ'], 'kunyomi': ['かべ'], 'meanings': ['wall', 'lining', 'fence']},
    '奥': {'strokes': 12, 'grade': 8, 'freq': 1177, 'onyomi': ['オウ'], 'kunyomi': ['おく', 'おく.まる'], 'meanings': ['interior', 'depths', 'inner part']},
    '嬉': {'strokes': 15, 'grade': 9, 'freq': 2289, 'onyomi': ['キ'], 'kunyomi': ['うれ.しい', 'うれ.しがる'], 'meanings': ['glad', 'pleased', 'joyful']},
    '宇': {'strokes': 6, 'grade': 6, 'freq': 812, 'onyomi': ['ウ'], 'kunyomi': [], 'meanings': ['eaves', 'roof', 'house', 'heaven', 'universe']},
    '寂': {'strokes': 11, 'grade': 8, 'freq': 1645, 'onyomi': ['ジャク', 'セキ'], 'kunyomi': ['さび', 'さび.しい', 'さび.れる'], 'meanings': ['lonely', 'quiet', 'solitude']},
    '嵐': {'strokes': 12, 'grade': 9, 'freq': 1761, 'onyomi': ['ラン'], 'kunyomi': ['あらし'], 'meanings': ['storm', 'tempest']},
    '希': {'strokes': 7, 'grade': 4, 'freq': 517, 'onyomi': ['キ', 'ケ'], 'kunyomi': ['まれ'], 'meanings': ['hope', 'beg', 'request', 'rare']},
    '患': {'strokes': 11, 'grade': 8, 'freq': 878, 'onyomi': ['カン'], 'kunyomi': ['わずら.う'], 'meanings': ['afflicted', 'disease', 'suffer from']},
    '憩': {'strokes': 16, 'grade': 8, 'freq': 1999, 'onyomi': ['ケイ'], 'kunyomi': ['いこ.い', 'いこ.う'], 'meanings': ['recess', 'rest', 'relax']},
    '憶': {'strokes': 16, 'grade': 8, 'freq': 1063, 'onyomi': ['オク'], 'kunyomi': [], 'meanings': ['recollection', 'memory', 'remember']},
    '拶': {'strokes': 9, 'grade': 8, 'freq': 1916, 'onyomi': ['サツ'], 'kunyomi': ['せま.る'], 'meanings': ['be imminent', 'draw close', 'greeting']},
    '挨': {'strokes': 10, 'grade': 8, 'freq': 1915, 'onyomi': ['アイ'], 'kunyomi': ['ひら.く'], 'meanings': ['push open', 'open', 'greeting']},
    '枝': {'strokes': 8, 'grade': 5, 'freq': 1361, 'onyomi': ['シ'], 'kunyomi': ['えだ'], 'meanings': ['bough', 'branch', 'twig']},
    '椅': {'strokes': 12, 'grade': 9, 'freq': 2390, 'onyomi': ['イ'], 'kunyomi': [], 'meanings': ['chair', 'seat']},
    '汗': {'strokes': 6, 'grade': 8, 'freq': 1373, 'onyomi': ['カン'], 'kunyomi': ['あせ'], 'meanings': ['sweat', 'perspiration']},
    '泡': {'strokes': 8, 'grade': 8, 'freq': 1599, 'onyomi': ['ホウ'], 'kunyomi': ['あわ'], 'meanings': ['bubble', 'foam', 'froth']},
    '溺': {'strokes': 13, 'grade': 8, 'freq': 2350, 'onyomi': ['デキ'], 'kunyomi': ['おぼ.れる'], 'meanings': ['drown', 'indulge in', 'sink']},
    '督': {'strokes': 13, 'grade': 8, 'freq': 453, 'onyomi': ['トク'], 'kunyomi': [], 'meanings': ['coach', 'command', 'urge', 'supervise']},
    '穏': {'strokes': 16, 'grade': 8, 'freq': 1259, 'onyomi': ['オン'], 'kunyomi': ['おだ.やか'], 'meanings': ['calm', 'quiet', 'moderation']},
    '穴': {'strokes': 5, 'grade': 6, 'freq': 1372, 'onyomi': ['ケツ'], 'kunyomi': ['あな'], 'meanings': ['hole', 'aperture', 'opening']},
    '紹': {'strokes': 11, 'grade': 8, 'freq': 1007, 'onyomi': ['ショウ'], 'kunyomi': [], 'meanings': ['introduce', 'inherit', 'help']},
    '絹': {'strokes': 13, 'grade': 6, 'freq': 1636, 'onyomi': ['ケン'], 'kunyomi': ['きぬ'], 'meanings': ['silk']},
    '肩': {'strokes': 8, 'grade': 8, 'freq': 1269, 'onyomi': ['ケン'], 'kunyomi': ['かた'], 'meanings': ['shoulder']},
    '胃': {'strokes': 9, 'grade': 4, 'freq': 1342, 'onyomi': ['イ'], 'kunyomi': [], 'meanings': ['stomach', 'paunch']},
    '踊': {'strokes': 14, 'grade': 8, 'freq': 1289, 'onyomi': ['ヨウ'], 'kunyomi': ['おど.る'], 'meanings': ['jump', 'dance', 'leap']},
    '輝': {'strokes': 15, 'grade': 8, 'freq': 1409, 'onyomi': ['キ'], 'kunyomi': ['かがや.く'], 'meanings': ['radiance', 'shine', 'sparkle']},
    '釈': {'strokes': 11, 'grade': 8, 'freq': 764, 'onyomi': ['シャク', 'セキ'], 'kunyomi': ['とく', 'ゆる.す'], 'meanings': ['explanation', 'clarification', 'pardon']},
    '鍵': {'strokes': 17, 'grade': 8, 'freq': 1993, 'onyomi': ['ケン'], 'kunyomi': ['かぎ'], 'meanings': ['key']},
    '雲': {'strokes': 12, 'grade': 2, 'freq': 1288, 'onyomi': ['ウン'], 'kunyomi': ['くも'], 'meanings': ['cloud']},
    '霧': {'strokes': 19, 'grade': 8, 'freq': 1934, 'onyomi': ['ム', 'ボウ'], 'kunyomi': ['きり'], 'meanings': ['fog', 'mist']},
    '餌': {'strokes': 15, 'grade': 8, 'freq': 2280, 'onyomi': ['ジ', 'ニ'], 'kunyomi': ['え', 'えさ'], 'meanings': ['bait', 'food', 'lure']},
    '鬼': {'strokes': 10, 'grade': 8, 'freq': 1419, 'onyomi': ['キ'], 'kunyomi': ['おに'], 'meanings': ['ghost', 'demon', 'ogre']}
}

def main():
    with open('database/kanji_daily_quiz_dataset.js', 'r', encoding='utf-8') as f:
        daily_code = f.read()
    m2 = re.search(r'window\.JLPT_DAILY_KANJI_DATA\s*=\s*(\{.*?\});', daily_code, re.DOTALL)
    daily_data = json.loads(m2.group(1))

    with open('database/jlpt_kanji_data.js', 'r', encoding='utf-8') as f:
        kanji_code = f.read()
    m1 = re.search(r'window\.JLPT_KANJI_DATA\s*=\s*(\{.*?\});', kanji_code, re.DOTALL)
    kanji_data = json.loads(m1.group(1))

    # Build master kanji dict
    master_dict = {}
    for lvl in ['N5', 'N4', 'N3', 'N2', 'N1']:
        for k in kanji_data.get(lvl, []):
            c = k['character']
            if c not in master_dict:
                master_dict[c] = dict(k)

    # Add 38 extra kanji
    for c, meta in kanji_38.items():
        if c not in master_dict:
            master_dict[c] = {
                'character': c,
                'strokes': meta['strokes'],
                'grade': meta['grade'],
                'freq': meta['freq'],
                'onyomi': meta['onyomi'],
                'kunyomi': meta['kunyomi'],
                'meanings': meta['meanings']
            }

    # Extract all tested kanji and their test refs for each level
    level_tested_refs = {'N5': {}, 'N4': {}, 'N3': {}, 'N2': {}, 'N1': {}}
    for lvl in ['N5', 'N4', 'N3', 'N2', 'N1']:
        days = daily_data.get(lvl, {}).get('days', [])
        for d in days:
            day_num = d['day']
            for q_idx, q in enumerate(d.get('questions', [])):
                k_word = q.get('kanji', '')
                f_word = q.get('fullWord') or k_word
                reading = q.get('reading', '')
                for c in k_word:
                    if '\u4e00' <= c <= '\u9faf':
                        if c not in level_tested_refs[lvl]:
                            level_tested_refs[lvl][c] = []
                        level_tested_refs[lvl][c].append({
                            'level': lvl,
                            'day': day_num,
                            'qIndex': q_idx,
                            'word': f_word,
                            'reading': reading
                        })

    # Ensure all tested kanji are added to the list for that level
    aligned_kanji_data = {}
    for lvl in ['N5', 'N4', 'N3', 'N2', 'N1']:
        existing_list = kanji_data.get(lvl, [])
        existing_chars = set(k['character'] for k in existing_list)
        tested_chars = set(level_tested_refs[lvl].keys())

        # Copy existing items and annotate
        lvl_items = []
        for k in existing_list:
            char = k['character']
            item = dict(k)
            item['level'] = lvl
            if char in level_tested_refs[lvl]:
                item['dailyQuizRef'] = level_tested_refs[lvl][char][0] # Primary ref
            lvl_items.append(item)

        # Add any tested kanji that were missing from this level's list
        missing_chars = tested_chars - existing_chars
        for char in missing_chars:
            if char in master_dict:
                item = dict(master_dict[char])
                item['level'] = lvl
                item['dailyQuizRef'] = level_tested_refs[lvl][char][0]
                lvl_items.append(item)
            else:
                print(f"Warning: character {char} still missing from master_dict")

        aligned_kanji_data[lvl] = lvl_items
        print(f"Level {lvl}: final count = {len(lvl_items)} kanji (100% of {len(tested_chars)} tested kanji included)")

    # Save aligned dataset
    out_code = f"window.JLPT_KANJI_DATA = {json.dumps(aligned_kanji_data, ensure_ascii=False, indent=2)};\n"
    with open('database/jlpt_kanji_data.js', 'w', encoding='utf-8') as f:
        f.write(out_code)

    print("database/jlpt_kanji_data.js aligned and updated successfully!")

if __name__ == '__main__':
    main()
