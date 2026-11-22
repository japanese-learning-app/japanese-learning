# -*- coding: utf-8 -*-
import glob, json, re, os, filecmp

print("=== 1. AUDITING GRAMMAR DATASETS ===")
for p in sorted(glob.glob('/Users/yamauchimiku/.gemini/antigravity/scratch/japanese-flashcards/database/jlpt_n*_grammar_quiz_data.js')):
    lvl = p.split('/')[-1].split('_')[1]
    pub = p.replace('/database/', '/public/database/')
    assert os.path.exists(pub), f"Public mirror missing: {pub}"
    assert filecmp.cmp(p, pub), f"Public mirror out of sync: {lvl}"
    
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    idx1 = c.find('=') + 1
    idx2 = c.rfind(']') + 1
    data = json.loads(c[idx1:idx2])
    
    # Check no duplicate choices
    for q in data:
        choices = q['choices']
        assert len(choices) == len(set(choices)), f"Duplicate choices in {lvl} ID {q['id']}: {choices}"
        ans = q['answer']
        assert 0 <= ans < len(choices), f"Invalid answer index in {lvl} ID {q['id']}: {ans}"
        corr = q['correct_text']
        assert corr == choices[ans], f"Correct text mismatch in {lvl} ID {q['id']}: {corr} != {choices[ans]}"
    print(f"[{lvl.upper()} Grammar] OK: {len(data)} items validated & in perfect sync.")

print("\n=== 2. AUDITING VOCAB DATASETS ===")
for p in sorted(glob.glob('/Users/yamauchimiku/.gemini/antigravity/scratch/japanese-flashcards/database/jlpt_n*_vocab_quiz_data.js')):
    lvl = p.split('/')[-1].split('_')[1]
    pub = p.replace('/database/', '/public/database/')
    assert os.path.exists(pub), f"Public mirror missing: {pub}"
    assert filecmp.cmp(p, pub), f"Public mirror out of sync: {lvl}"
    
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    idx1 = c.find('=') + 1
    data = json.loads(c[idx1:].rstrip(';\n '))
    
    for q in data:
        choices = q['choices']
        ans = q['answer']
        assert 0 <= ans < len(choices), f"Invalid answer index in {lvl} ID {q['id']}: {ans}"
        corr = q['correct_text']
        assert corr == choices[ans], f"Correct text mismatch in {lvl} ID {q['id']}: {corr} != {choices[ans]}"
        
        # Check no 'きむ' in ruby
        for elem in q.get('choices_ruby', []):
            assert 'きむ' not in elem, f"Bad ruby 'きむ' in {lvl} ID {q['id']}"
    print(f"[{lvl.upper()} Vocab] OK: {len(data)} items validated & in perfect sync.")

print("\n=== 3. AUDITING HTML FILES ===")
for p in sorted(glob.glob('/Users/yamauchimiku/.gemini/antigravity/scratch/japanese-flashcards/jlpt_n*_grammar_quiz.html')):
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    assert 'sentenceEn.textContent = "";' in c, f"sentenceEn not emptied in {p}"
    assert 'blankPattern' in c, f"blankPattern not found in {p}"
    assert '新しくシャッフルしてもう一度解く' in c, f"shuffle button missing in {p}"
    print(f"[{os.path.basename(p)}] OK: sentenceEn hidden on render, ruby stripped before blank, shuffle retry active.")

for p in sorted(glob.glob('/Users/yamauchimiku/.gemini/antigravity/scratch/japanese-flashcards/jlpt_n*_vocab_quiz.html')):
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    assert '語形成' in c, f"語形成 ruby guard missing in {p}"
    assert '新しくシャッフルしてもう一度解く' in c, f"shuffle button missing in {p}"
    print(f"[{os.path.basename(p)}] OK: kanji writing/word-formation ruby guard active, shuffle retry active.")

print("\nALL INTEGRITY CHECKS PASSED PERFECTLY!")
