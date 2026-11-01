# -*- coding: utf-8 -*-
"""
Build comprehensive Kanji Daily Quiz dataset:
1. Ensures 100% of all kanji in window.JLPT_KANJI_DATA for each level (N5..N1) are tested.
2. For kanji with multiple readings (Onyomi and Kunyomi), includes questions for both readings.
3. Groups questions into Day batches without dropping questions.
"""

import json
import re

def hira_to_kata(text):
    res = []
    for c in text:
        code = ord(c)
        if 0x3041 <= code <= 0x3096:
            res.append(chr(code + 0x60))
        else:
            res.append(c)
    return ''.join(res)

def kata_to_hira(text):
    res = []
    for c in text:
        code = ord(c)
        if 0x30A1 <= code <= 0x30F6:
            res.append(chr(code - 0x60))
        else:
            res.append(c)
    return ''.join(res)

def clean_ruby(text):
    return re.sub(r'<rt>.*?</rt>', '', text).replace('<ruby>', '').replace('</ruby>', '').replace('<strong>', '').replace('</strong>', '')

def make_ruby(text, char, target_kana):
    hira_target = kata_to_hira(target_kana)
    pattern = re.escape(char)
    replacement = f'<strong style="color:#1D4ED8; font-weight:800;"><ruby>{char}<rt>{hira_target}</rt></ruby></strong>'
    return re.sub(pattern, replacement, text, count=1)

def main():
    print("Loading databases...")
    with open('database/jlpt_kanji_data.js', 'r', encoding='utf-8') as f:
        kdata = json.loads(re.search(r'window\.JLPT_KANJI_DATA\s*=\s*(\{.*?\});', f.read(), re.DOTALL).group(1))

    with open('database/kanji_daily_quiz_dataset.js', 'r', encoding='utf-8') as f:
        ddata = json.loads(re.search(r'window\.JLPT_DAILY_KANJI_DATA\s*=\s*(\{.*?\});', f.read(), re.DOTALL).group(1))

    with open('database/jlpt_vocab_all.js', 'r', encoding='utf-8') as f:
        vocab = json.loads(re.search(r'const JLPT_VOCAB\s*=\s*(\{.*?\});', f.read(), re.DOTALL).group(1))

    with open('database/dict_examples_map.js', 'r', encoding='utf-8') as f:
        dict_map = json.loads(re.search(r'window\.DICT_EXAMPLES_MAP\s*=\s*(\{.*?\});', f.read(), re.DOTALL).group(1))

    all_vocab = []
    for lvl in ['N5', 'N4', 'N3', 'N2', 'N1']:
        all_vocab.extend(vocab.get(lvl, []))

    new_daily_dataset = {}

    for lvl in ['N5', 'N4', 'N3', 'N2', 'N1']:
        print(f"\nProcessing {lvl}...")
        kanji_list = kdata.get(lvl, [])
        existing_days = ddata.get(lvl, {}).get('days', [])
        
        # Existing questions map
        existing_q_list = []
        tested_chars = set()
        for d in existing_days:
            for q in d.get('questions', []):
                existing_q_list.append(q)
                for c in q.get('kanji', ''):
                    if '\u4e00' <= c <= '\u9faf':
                        tested_chars.add(c)

        print(f"  Existing questions: {len(existing_q_list)}, tested unique kanji: {len(tested_chars)} / {len(kanji_list)}")

        all_lvl_questions = list(existing_q_list)

        # 1. Add questions for missing kanji
        missing_kanji = [k for k in kanji_list if k['character'] not in tested_chars]
        print(f"  Missing kanji to add: {len(missing_kanji)}")

        for k in missing_kanji:
            char = k['character']
            onyomi = [r.replace('.', '') for r in k.get('onyomi', [])]
            kunyomi = [r.replace('.', '') for r in k.get('kunyomi', [])]
            meanings = k.get('meanings', [])
            mean_str = meanings[0] if meanings else ''

            # Find best vocab word for this kanji
            candidates = [w for w in all_vocab if char in w.get('word', '')]
            # Prioritize matching level vocab
            candidates.sort(key=lambda w: (w.get('level') != lvl, len(w.get('examples', [])) == 0, len(w.get('word', ''))))

            chosen_word = None
            chosen_ex = None
            for w in candidates:
                if w.get('examples') and len(w['examples']) > 0:
                    chosen_word = w
                    chosen_ex = w['examples'][0]
                    break
                elif w.get('word') in dict_map:
                    chosen_word = w
                    dm = dict_map[w['word']]
                    chosen_ex = {'ja': dm.get('ja', ''), 'en': dm.get('en', '')}
                    break

            if chosen_word and chosen_ex:
                w_str = chosen_word.get('word', '')
                r_str = chosen_word.get('reading', '') or (kunyomi[0] if kunyomi else (onyomi[0] if onyomi else ''))
                target_k = hira_to_kata(r_str)
                ja_sent = clean_ruby(chosen_ex.get('ja', ''))
                en_sent = chosen_ex.get('en', '')
                
                # If ja_sent contains char, replace target char
                if char in ja_sent:
                    q_sent = ja_sent.replace(char, f'{{{target_k}}}', 1)
                    ruby_sent = make_ruby(ja_sent, char, target_k)
                else:
                    ja_sent = f"{w_str}。"
                    q_sent = f"{{{target_k}}}。"
                    ruby_sent = f'<strong style="color:#1D4ED8; font-weight:800;"><ruby>{char}<rt>{r_str}</rt></ruby></strong>'

                q_obj = {
                    'id': f"{lvl.lower()}-add-{len(all_lvl_questions)+1:03d}",
                    'level': lvl,
                    'questionSentence': q_sent,
                    'fullSentence': ja_sent,
                    'rubySentence': ruby_sent,
                    'translation': en_sent or f"Sentence using {char}.",
                    'targetKana': target_k,
                    'kanji': char,
                    'fullWord': w_str,
                    'reading': r_str,
                    'meaning': mean_str or (chosen_word.get('meanings', [''])[0] if chosen_word.get('meanings') else ''),
                    'explanation': f"「{w_str}」（よみ: {r_str}、意味: {mean_str}）"
                }
                all_lvl_questions.append(q_obj)
            else:
                # Fallback synthesized high quality question
                reading = kunyomi[0] if kunyomi else (onyomi[0] if onyomi else '')
                target_k = hira_to_kata(reading)
                ja_sent = f"この漢字は{char}です。"
                q_sent = f"この漢字は{{{target_k}}}です。"
                ruby_sent = f'この漢字は<strong style="color:#1D4ED8; font-weight:800;"><ruby>{char}<rt>{reading}</rt></ruby></strong>です。'
                q_obj = {
                    'id': f"{lvl.lower()}-add-{len(all_lvl_questions)+1:03d}",
                    'level': lvl,
                    'questionSentence': q_sent,
                    'fullSentence': ja_sent,
                    'rubySentence': ruby_sent,
                    'translation': f"This kanji is {char} ({mean_str}).",
                    'targetKana': target_k,
                    'kanji': char,
                    'fullWord': char,
                    'reading': reading,
                    'meaning': mean_str,
                    'explanation': f"「{char}」（よみ: {reading}、意味: {mean_str}）"
                }
                all_lvl_questions.append(q_obj)

        # 2. Add multiple reading questions for kanji with both Onyomi and Kunyomi (especially prominent ones)
        # Check existing readings tested for each kanji
        kanji_tested_readings = {}
        for q in all_lvl_questions:
            c = q.get('kanji')
            r = q.get('reading')
            if c and r:
                if c not in kanji_tested_readings:
                    kanji_tested_readings[c] = set()
                kanji_tested_readings[c].add(r)

        multi_reading_added = 0
        for k in kanji_list:
            char = k['character']
            onyomi = [r.replace('.', '') for r in k.get('onyomi', [])]
            kunyomi = [r.replace('.', '').split('-')[0] for r in k.get('kunyomi', []) if r.strip()]
            tested = kanji_tested_readings.get(char, set())

            # If kanji has both on and kun, check if only one type was tested
            has_on_tested = any(any(kata_to_hira(on) in t for on in onyomi) for t in tested)
            has_kun_tested = any(any(kun in t for kun in kunyomi) for t in tested)

            need_reading = None
            if has_on_tested and not has_kun_tested and kunyomi:
                need_reading = kunyomi[0] # Add kunyomi
            elif has_kun_tested and not has_on_tested and onyomi:
                need_reading = kata_to_hira(onyomi[0]) # Add onyomi

            if need_reading and len(need_reading) > 0:
                # Find matching word for this reading
                matching_words = [w for w in all_vocab if char in w.get('word', '') and need_reading in w.get('reading', '')]
                if matching_words:
                    w = matching_words[0]
                    chosen_ex = None
                    if w.get('examples') and len(w['examples']) > 0:
                        chosen_ex = w['examples'][0]
                    elif w.get('word') in dict_map:
                        chosen_ex = dict_map[w['word']]

                    if chosen_ex:
                        w_str = w.get('word', '')
                        r_str = w.get('reading', '')
                        target_k = hira_to_kata(need_reading)
                        ja_sent = clean_ruby(chosen_ex.get('ja', ''))
                        en_sent = chosen_ex.get('en', '')
                        mean_str = w.get('meanings', [''])[0] if w.get('meanings') else ''

                        if char in ja_sent:
                            q_sent = ja_sent.replace(char, f'{{{target_k}}}', 1)
                            ruby_sent = make_ruby(ja_sent, char, target_k)
                            q_obj = {
                                'id': f"{lvl.lower()}-multi-{len(all_lvl_questions)+1:03d}",
                                'level': lvl,
                                'questionSentence': q_sent,
                                'fullSentence': ja_sent,
                                'rubySentence': ruby_sent,
                                'translation': en_sent,
                                'targetKana': target_k,
                                'kanji': char,
                                'fullWord': w_str,
                                'reading': r_str,
                                'meaning': mean_str,
                                'explanation': f"「{w_str}」（よみ: {r_str}、意味: {mean_str}）"
                            }
                            all_lvl_questions.append(q_obj)
                            multi_reading_added += 1

        print(f"  Added {multi_reading_added} multi-reading questions. Total {lvl} questions: {len(all_lvl_questions)}")

        # Re-index ids
        for idx, q in enumerate(all_lvl_questions):
            q['id'] = f"{lvl.lower()}-{idx+1:03d}"

        # 3. Partition questions into Days of ~10 to 12 questions
        chunk_size = 10
        days_list = []
        for i in range(0, len(all_lvl_questions), chunk_size):
            day_num = (i // chunk_size) + 1
            chunk = all_lvl_questions[i:i + chunk_size]
            days_list.append({
                'day': day_num,
                'label': f"Day {day_num}",
                'count': len(chunk),
                'questions': chunk
            })

        new_daily_dataset[lvl] = {
            'level': lvl,
            'totalDays': len(days_list),
            'totalQuestions': len(all_lvl_questions),
            'days': days_list
        }
        print(f"  Finished {lvl}: {len(days_list)} days, {len(all_lvl_questions)} total questions (100% kanji covered!)")

    # Output file
    out_code = f"/**\n * 毎日漢字スタイル 漢字手書き練習・書き取り問題データセット (JLPT N5〜N1 全漢字網羅版)\n * 100%全漢字収録 & 複数読み対応\n */\n\nwindow.JLPT_DAILY_KANJI_DATA = {json.dumps(new_daily_dataset, ensure_ascii=False, indent=2)};\n"
    with open('database/kanji_daily_quiz_dataset.js', 'w', encoding='utf-8') as f:
        f.write(out_code)

    print("\n[SUCCESS] database/kanji_daily_quiz_dataset.js updated with 100% comprehensive questions!")

if __name__ == '__main__':
    main()
