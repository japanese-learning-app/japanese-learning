# -*- coding: utf-8 -*-
import json
step2_raw = json.load(open('/Users/yamauchimiku/Documents/GitHub/japanese-learning/scripts/step2_raw.json'))

for q in step2_raw:
    print(f"ID: {q['id']}")
    for i, c in enumerate(q['choices']):
        text = c['reason']
        print(f"  [{i+1}] {text[:50]}...")
    print(f"  NOTE: {q['note'][:50]}...")
