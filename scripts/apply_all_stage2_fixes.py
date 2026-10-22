# -*- coding: utf-8 -*-
"""
Applies Stage 2 flashcard fixes to:
- js/data.js & public/js/data.js (24 cards)
- database/class_vocab_data.js & public/database/class_vocab_data.js (210 cards)
"""

import json

print("Applying Stage 2 master flashcard fixes...")

# 1. Load replacements
with open("scripts/initial_replacements_stage2.json", "r", encoding="utf-8") as f:
    initial_reps = json.load(f)

with open("scripts/class_replacements_part1.json", "r", encoding="utf-8") as f:
    class_p1 = json.load(f)

with open("scripts/class_replacements_part2.json", "r", encoding="utf-8") as f:
    class_p2 = json.load(f)

class_reps = {**class_p1, **class_p2}

# ==============================================================================
# Update INITIAL_VOCAB_DATA
# ==============================================================================
with open("js/data.js", "r", encoding="utf-8") as f:
    init_text = f.read()

s_init = init_text.find("window.INITIAL_VOCAB_DATA =") + len("window.INITIAL_VOCAB_DATA =")
e_init = init_text.find("window.SECTIONS_DATA =")
init_prefix = init_text[:s_init]
init_sub = init_text[s_init:e_init]
init_arr_end = init_sub.rfind("];") + 1
init_cards = json.loads(init_sub[:init_arr_end].strip())
init_suffix = init_sub[init_arr_end:] + init_text[e_init:]

applied_init = 0
for card in init_cards:
    cid = card["id"]
    if cid in initial_reps:
        rep = initial_reps[cid]
        if "example" not in card:
            card["example"] = {}
        for k, v in rep.items():
            card["example"][k] = v
        applied_init += 1

print(f"Applied fixes to {applied_init} cards in INITIAL_VOCAB_DATA")
new_init_json = " " + json.dumps(init_cards, ensure_ascii=False, indent=2) + ";\n\n"

with open("js/data.js", "w", encoding="utf-8") as f:
    f.write(init_prefix + new_init_json + init_text[e_init:])
with open("public/js/data.js", "w", encoding="utf-8") as f:
    f.write(init_prefix + new_init_json + init_text[e_init:])
print("✅ Saved js/data.js and public/js/data.js")

# ==============================================================================
# Update CLASS_VOCAB_DATA
# ==============================================================================
with open("database/class_vocab_data.js", "r", encoding="utf-8") as f:
    class_text = f.read()

s_class = class_text.find("[")
e_class = class_text.rfind("];") + 1
class_prefix = class_text[:s_class]
class_suffix = class_text[e_class:]
class_cards = json.loads(class_text[s_class:e_class].strip())

applied_class = 0
for card in class_cards:
    cid = card["id"]
    if cid in class_reps:
        rep = class_reps[cid]
        if "example" not in card:
            card["example"] = {}
        for k, v in rep.items():
            card["example"][k] = v
        applied_class += 1

print(f"Applied fixes to {applied_class} cards in CLASS_VOCAB_DATA")
new_class_json = json.dumps(class_cards, ensure_ascii=False, indent=2)

with open("database/class_vocab_data.js", "w", encoding="utf-8") as f:
    f.write(class_prefix + new_class_json + class_suffix)
with open("public/database/class_vocab_data.js", "w", encoding="utf-8") as f:
    f.write(class_prefix + new_class_json + class_suffix)
print("✅ Saved database/class_vocab_data.js and public/database/class_vocab_data.js")

print("🎉 Stage 2 fixes applied successfully!")
