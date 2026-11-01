# -*- coding: utf-8 -*-
import json

with open('database/jlpt_vocab_all.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Parse JSON
prefix = 'const JLPT_VOCAB = '
suffix = ';'
idx_start = text.find(prefix) + len(prefix)
idx_end = text.rfind(suffix)

raw_json = text[idx_start:idx_end].strip()
data = json.loads(raw_json)

# Update N3 馬 and 馬鹿
for w in data.get('N3', []):
    if w.get('word') == '馬':
        w['meanings'] = ['horse']
        w['examples'] = [
            {'ja': '牧場で 白い 馬を 見ました。', 'en': 'I saw a white horse at the ranch.'},
            {'ja': '公園で 馬に乗る体験を しました。', 'en': 'I experienced riding a horse at the park.'}
        ]
    elif w.get('word') == '馬鹿':
        w['meanings'] = ['fool', 'idiot', 'trivial matter']
        w['examples'] = [
            {'ja': 'そんな 馬鹿な 話は 信じられません。', 'en': 'I cannot believe such a ridiculous story.'},
            {'ja': '馬鹿正直な ところが 彼の 長所です。', 'en': 'His extreme honesty is his strong point.'}
        ]

new_code = f"// Comprehensive JLPT Vocabulary (N5-N1) in Gojuon (AIUEO) Order\nconst JLPT_VOCAB = {json.dumps(data, ensure_ascii=False)};\n"
with open('database/jlpt_vocab_all.js', 'w', encoding='utf-8') as f:
    f.write(new_code)

print("database/jlpt_vocab_all.js cleanly updated!")
