# -*- coding: utf-8 -*-
import glob, json, os, re

REPO_DIR = "/Users/yamauchimiku/Documents/GitHub/japanese-learning"
grammar_files = sorted(glob.glob(f"{REPO_DIR}/database/jlpt_n*_grammar_quiz_data.js"))
vocab_files = sorted(glob.glob(f"{REPO_DIR}/database/jlpt_n*_vocab_quiz_data.js"))

UNNATURAL_PATTERNS = [
    (r'君は', '「君は」から始まる文'),
    (r'運命のようだ', '直訳調「運命のようだ」'),
    (r'愛されていた', '直訳受動態'),
    (r'殺[しすせ]', '不穏表現'),
    (r'殴[りるれ]', '不穏表現'),
    (r'突き刺', '不自然・不穏表現'),
    (r'ナイフ', '不穏表現'),
    (r'高いお金を', '不自然な表現'),
    (r'なってただろう', '不自然な縮約'),
    (r'行ってただろう', '不自然な縮約'),
    (r'知ってただろう', '不自然な縮約'),
    (r'後でのことだから', '不自然な表現'),
]

flagged = []

for p in grammar_files + vocab_files:
    fname = os.path.basename(p)
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    idx1 = c.find('=') + 1
    idx2 = c.rfind(']') + 1 if ']' in c[idx1:] else len(c)
    data = json.loads(c[idx1:idx2].rstrip(';\n '))
    
    for q in data:
        qid = q['id']
        qst = q.get('question', '')
        s_jp = q.get('sentence_jp', '')
        full = f"{qst} {s_jp}"
        for pat, desc in UNNATURAL_PATTERNS:
            if re.search(pat, full):
                flagged.append((fname, qid, desc, qst))

print(f"Total flagged unnatural/suspicious patterns: {len(flagged)}")
for f in flagged:
    print(f"[{f[0]}] ID {f[1]} ({f[2]}): {f[3]}")
