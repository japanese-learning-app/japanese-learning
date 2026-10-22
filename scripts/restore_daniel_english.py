# -*- coding: utf-8 -*-
"""
Restores Daniel's 103 cards to pure English.
Meaning: English definition across all language keys.
Example: Japanese sentence with ruby (ja), and English translation across all language keys.
"""

import subprocess
import json

print("Restoring Daniel's 103 cards to pure English...")

# Extract original 103 Daniel cards from commit 1866978
orig_output = subprocess.check_output(["git", "show", "1866978:database/class_vocab_data.js"], text=True)
s_orig = orig_output.find("[")
e_orig = orig_output.rfind("];") + 1
orig_cards = json.loads(orig_output[s_orig:e_orig].strip())
orig_daniels = {c["id"]: c for c in orig_cards if c["id"].startswith("card_daniel_")}

print(f"Extracted {len(orig_daniels)} original Daniel cards.")

# Load current CLASS_VOCAB_DATA
with open("database/class_vocab_data.js", "r", encoding="utf-8") as f:
    class_text = f.read()

s_class = class_text.find("[")
e_class = class_text.rfind("];") + 1
class_prefix = class_text[:s_class]
class_suffix = class_text[e_class:]
class_cards = json.loads(class_text[s_class:e_class].strip())

restored_count = 0
for card in class_cards:
    cid = card["id"]
    if cid in orig_daniels:
        orig = orig_daniels[cid]
        en_meaning = orig["meaning"]["en"]
        ja_example = orig["example"]["ja"]
        en_example = orig["example"]["en"]

        card["word"] = orig["word"]
        card["reading"] = orig["reading"]
        card["category"] = orig.get("category", "授業で習った言葉")
        card["related"] = orig.get("related", f"{orig['reading']}（授業の重要表現）")

        # Set meaning purely in English
        card["meaning"] = {
            "ja": orig["word"],
            "en": en_meaning,
            "zh_TW": en_meaning,
            "zh_CN": en_meaning,
            "ko": en_meaning,
            "zh_HK": en_meaning,
            "fr": en_meaning
        }

        # Set example purely in English
        card["example"] = {
            "ja": ja_example,
            "en": en_example,
            "zh_TW": en_example,
            "zh_CN": en_example,
            "ko": en_example,
            "zh_HK": en_example,
            "fr": en_example
        }
        restored_count += 1

print(f"Restored {restored_count} Daniel cards to pure English.")

new_class_json = json.dumps(class_cards, ensure_ascii=False, indent=2)

with open("database/class_vocab_data.js", "w", encoding="utf-8") as f:
    f.write(class_prefix + new_class_json + class_suffix)

with open("public/database/class_vocab_data.js", "w", encoding="utf-8") as f:
    f.write(class_prefix + new_class_json + class_suffix)

print("✅ Saved to database/class_vocab_data.js and public/database/class_vocab_data.js")
