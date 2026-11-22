# -*- coding: utf-8 -*-
import glob, json, os

REPO_DIR = "/Users/yamauchimiku/Documents/GitHub/japanese-learning"
grammar_files = sorted(glob.glob(f"{REPO_DIR}/database/jlpt_n*_grammar_quiz_data.js"))

SYNONYM_GROUPS = [
    {"からには", "以上は", "上は", "以上"},
    {"を契機に", "をきっかけに", "がきっかけで"},
    {"としたら", "とすれば", "とすると"},
    {"にしたら", "にすれば"},
    {"ものなら", "ことなら"},
    {"ものの", "反面", "一方で", "一方"},
    {"にもかかわらず", "ながらも"},
    {"わりに", "わりには", "にしては"},
    {"あげく", "末に"},
    {"ばかりか", "だけでなく", "のみならず", "にとどまらず", "に限らず"},
    {"に違いない", "に相違ない"},
    {"にすぎない", "にほかならない", "でしかない"},
    {"てならない", "てたまらない", "てしょうがない"},
    {"にとって", "から見ると", "から見れば", "からすると", "からすれば"},
    {"に関して", "について"},
    {"に基づいて", "をもとに", "をもとにして"},
    {"に沿って", "にしたがって", "につれて", "とともに"},
    {"に応じて", "にこたえて"}
]

for p in grammar_files:
    lvl = os.path.basename(p).split('_')[1].upper()
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    idx1 = c.find('=') + 1
    idx2 = c.rfind(']') + 1
    data = json.loads(c[idx1:idx2])
    
    for q in data:
        qid = q['id']
        qst = q['question']
        choices = q['choices']
        ans = q['answer']
        corr = q['correct_text']
        
        for grp in SYNONYM_GROUPS:
            # check which choices belong to grp
            hits = [ch for ch in choices if any(m == ch or ch.endswith(m) for m in grp)]
            if len(hits) >= 2:
                # print exact details
                print(f"[{lvl}] ID {qid} ({q.get('grammar')}): Ans={ans} ('{corr}')")
                print(f"     Q: {qst}")
                print(f"     Choices: {choices}")
                print(f"     Hits in {grp}: {hits}")
                print("-" * 60)
