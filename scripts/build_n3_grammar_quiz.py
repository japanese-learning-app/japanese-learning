#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JLPT N3 Grammar Quiz Dataset Builder
Combines Part 1 to Part 4, shuffles choices with deterministic seed, applies precise furigana ruby tags,
validates choices and answers, and exports to database/jlpt_n3_grammar_quiz_data.js.
"""

import sys
import os
import json
import re
import random

# Add scripts directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import pykakasi
from fix_all_rubies import fix_rubies_in_text

from n3_grammar_data_part1 import PART1_DATA
from n3_grammar_data_part2 import PART2_DATA
from n3_grammar_data_part3 import PART3_DATA
from n3_grammar_data_part4 import PART4_DATA

kks = pykakasi.kakasi()

def kanji_ruby(text):
    if not text:
        return ""
    # Split text while keeping （　　　）
    parts = re.split(r'(（\s*）|\(　*\)|（　*）|【.*?】)', text)
    processed_parts = []
    
    for part in parts:
        if not part:
            continue
        if re.match(r'（\s*）|\(　*\)|（　*）|【.*?】', part):
            processed_parts.append(part)
            continue
            
        result = kks.convert(part)
        out = []
        for item in result:
            orig = item['orig']
            hira = item['hira']
            # if no kanji, keep as is
            if not any('\u4e00' <= c <= '\u9fff' for c in orig):
                out.append(orig)
                continue
            
            # Check prefix kana
            prefix_len = 0
            while prefix_len < len(orig) and not ('\u4e00' <= orig[prefix_len] <= '\u9fff'):
                prefix_len += 1
            prefix = orig[:prefix_len]
            
            # Check suffix kana
            suffix_len = 0
            while suffix_len < len(orig) - prefix_len and not ('\u4e00' <= orig[-1 - suffix_len] <= '\u9fff'):
                suffix_len += 1
            suffix = orig[len(orig) - suffix_len:] if suffix_len > 0 else ""
            
            kanji_part = orig[prefix_len:len(orig) - suffix_len] if suffix_len > 0 else orig[prefix_len:]
            
            # Trim prefix and suffix from hira
            hira_middle = hira
            if prefix and hira_middle.startswith(prefix):
                hira_middle = hira_middle[len(prefix):]
            if suffix and hira_middle.endswith(suffix):
                hira_middle = hira_middle[:-len(suffix)]
                
            out.append(f"{prefix}<ruby>{kanji_part}<rt>{hira_middle}</rt></ruby>{suffix}")
            
        processed_parts.append("".join(out))
        
    res = "".join(processed_parts)
    # Apply standard fixes
    res = fix_rubies_in_text(res)
    # Custom fixes for common JLPT verbs & multisyllabic kanji
    res = re.sub(r'<ruby>開<rt>ひら</rt></ruby>き', '<ruby>開<rt>あ</rt></ruby>き', res)
    res = re.sub(r'<ruby>開<rt>ひら</rt></ruby>け', '<ruby>開<rt>あ</rt></ruby>け', res)
    res = re.sub(r'<ruby>開<rt>ひら</rt></ruby>いた', '<ruby>開<rt>あ</rt></ruby>いた', res)
    res = re.sub(r'<ruby>降<rt>お</rt></ruby>り出', '<ruby>降<rt>ふ</rt></ruby>り出', res)
    res = re.sub(r'<ruby>降<rt>お</rt></ruby>る', '<ruby>降<rt>ふ</rt></ruby>る', res)
    res = re.sub(r'<ruby>入<rt>い</rt></ruby>って', '<ruby>入<rt>はい</rt></ruby>って', res)
    res = re.sub(r'<ruby>入<rt>い</rt></ruby>った', '<ruby>入<rt>はい</rt></ruby>った', res)
    res = re.sub(r'<ruby>入<rt>い</rt></ruby>る', '<ruby>入<rt>はい</rt></ruby>る', res)
    res = re.sub(r'<ruby>空<rt>そら</rt></ruby>いた', '<ruby>空<rt>あ</rt></ruby>いた', res)
    res = re.sub(r'<ruby>空<rt>そら</rt></ruby>く', '<ruby>空<rt>あ</rt></ruby>く', res)
    return res

def extract_speech_text(html_text):
    if not html_text:
        return ""
    t = str(html_text)
    t = re.sub(r'<rt>[\s\S]*?<\/rt>', '', t, flags=re.IGNORECASE)
    t = re.sub(r'<[^>]+>', '', t)
    t = re.sub(r'（\s*）|\(　*\)|（　*）', '、', t)
    t = re.sub(r'（する）|\(する\)', '', t)
    t = re.sub(r'[【】]', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

print("=== Merging all 4 parts ===")
all_raw = PART1_DATA + PART2_DATA + PART3_DATA + PART4_DATA
print(f"Total raw questions: {len(all_raw)}")

# Deterministic shuffle of choices for balanced distribution
rng = random.Random(42)

final_data = []

for idx, item in enumerate(all_raw, 1):
    correct_text = item["correct_text"]
    original_choices = list(item["choices"])
    
    # Verify correct_text is in choices
    if correct_text not in original_choices:
        raise ValueError(f"ID {idx}: correct_text '{correct_text}' not in choices {original_choices}")
    
    # Verify no duplicates
    if len(set(original_choices)) != 4:
        raise ValueError(f"ID {idx}: Duplicate choices found in {original_choices}")
    
    # Shuffle choices
    shuffled_choices = list(original_choices)
    rng.shuffle(shuffled_choices)
    answer_idx = shuffled_choices.index(correct_text)
    
    # Format question with （　　　）
    q_text = item["question"]
    # Ensure uniform blank
    q_text = re.sub(r'【\s*】|（\s*）|（　*）|\(\s*\)', '（　　　）', q_text)
    
    # Generate rubies
    q_ruby = kanji_ruby(q_text)
    s_jp_ruby = kanji_ruby(item["sentence_jp"])
    choices_ruby = [kanji_ruby(c) for c in shuffled_choices]
    correct_text_ruby = kanji_ruby(correct_text)
    
    # Validate speech text
    speech = extract_speech_text(s_jp_ruby)
    if '<rt>' in speech or '</rt>' in speech:
        raise ValueError(f"ID {idx}: Speech text leak of ruby: {speech}")
    
    entry = {
        "id": idx,
        "grammar_id": item["grammar_id"],
        "grammar": item["grammar"],
        "reading": item["reading"],
        "meaning_en": item["meaning_en"],
        "similar": item.get("similar", ""),
        "sentence_jp": item["sentence_jp"],
        "sentence_furigana": item["sentence_furigana"],
        "sentence_en": item["sentence_en"],
        "question": q_text,
        "choices": shuffled_choices,
        "answer": answer_idx,
        "correct_text": correct_text,
        "notes": item.get("notes", ""),
        "question_ruby": q_ruby,
        "sentence_jp_ruby": s_jp_ruby,
        "choices_ruby": choices_ruby,
        "correct_text_ruby": correct_text_ruby
    }
    final_data.append(entry)

# Write to database/jlpt_n3_grammar_quiz_data.js
out_path = '/Users/yamauchimiku/Documents/GitHub/japanese-learning/database/jlpt_n3_grammar_quiz_data.js'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write('window.JLPT_N3_QUIZ_DATA = ')
    json.dump(final_data, f, ensure_ascii=False, indent=2)
    f.write(';\n')

print(f"Successfully generated {out_path} with {len(final_data)} questions.")

# Check choice distribution
answers_count = [0, 0, 0, 0]
for d in final_data:
    answers_count[d['answer']] += 1
print(f"Answer distribution across 0-3: {answers_count}")
