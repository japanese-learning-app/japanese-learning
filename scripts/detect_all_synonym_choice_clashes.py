# -*- coding: utf-8 -*-
import glob, json, os

REPO_DIR = "/Users/yamauchimiku/Documents/GitHub/japanese-learning"
grammar_files = sorted(glob.glob(f"{REPO_DIR}/database/jlpt_n*_grammar_quiz_data.js"))

SYNONYM_GROUPS = [
    # 理由・根拠
    {"からには", "以上は", "上は", "以上"},
    {"を契機に", "をきっかけに", "がきっかけで"},
    {"ばかりに", "だけに", "からこそ"},
    
    # 仮定・条件
    {"としたら", "とすれば", "とすると"},
    {"にしたら", "にすれば"},
    {"ものなら", "ことなら"},
    
    # 逆接・譲歩
    {"にしても", "としても"},
    {"にしろ", "にせよ"},
    {"ものの", "反面", "一方で", "一方"},
    {"にもかかわらず", "ながらも", "ものの"},
    {"わりに", "わりには", "にしては"},
    
    # 結果・果て
    {"あげく", "末に", "結果"},
    {"きらいがある", "傾向がある", "恐れがある"},
    
    # 並立・添加
    {"ばかりか", "だけでなく", "のみならず", "にとどまらず", "に限らず"},
    {"はおろか", "どころか"},
    
    # 確信・推量
    {"に違いない", "に相違ない", "はずだ"},
    {"にすぎない", "にほかならない", "でしかない"},
    {"わけがない", "はずがない", "っこない"},
    
    # 感情
    {"てならない", "てたまらない", "てしょうがない", "てしかたがない"},
    
    # 視点・関係
    {"にとって", "から見ると", "から見れば", "からすると", "からすれば"},
    {"に関して", "について", "をめぐって"},
    {"に基づいて", "をもとに", "をもとにして"},
    {"に沿って", "にしたがって", "につれて", "とともに"},
    {"に応じて", "にこたえて"}
]

clash_list = []

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
        
        # Clean choices to match against groups
        # remove prefix like 'の', 'に', etc. if needed, or exact match
        for group in SYNONYM_GROUPS:
            matched_in_group = []
            for ch in choices:
                # check exact or partial
                clean_ch = ch.strip()
                for member in group:
                    if clean_ch == member or clean_ch.endswith(member):
                        matched_in_group.append((ch, member))
                        break
            if len(matched_in_group) >= 2:
                # Check if they are distinct members
                distinct_members = set(m[1] for m in matched_in_group)
                if len(distinct_members) >= 2:
                    clash_list.append((lvl, qid, q.get('grammar',''), [m[0] for m in matched_in_group], qst, choices, ans))

print(f"Total potential synonym clashes found: {len(clash_list)}")
for cl in clash_list:
    print(f"[{cl[0]}] ID {cl[1]} ({cl[2]}): clashed={cl[3]}")
    print(f"      Q: {cl[4]}")
    print(f"      Choices: {cl[5]} (Ans: {cl[6]} -> {cl[5][cl[6]]})")
