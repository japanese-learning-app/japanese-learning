# -*- coding: utf-8 -*-
"""Rebuild database/jlpt_n5_vocab_full_data.js from data_vocab_full.VOCAB_FULL (idempotent)."""
import sys, json, re, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from n5_lib import R, lint_ruby, write_js
from data_vocab_full import VOCAB_FULL

REPO = os.path.dirname(os.path.dirname(HERE))
PATH = os.path.join(REPO, 'database', 'jlpt_n5_vocab_full_data.js')

def load(path):
    s = open(path, encoding='utf-8').read()
    dec = json.JSONDecoder()
    res = {}
    for m in re.finditer(r'window\.(\w+) = ', s):
        res[m.group(1)], _ = dec.raw_decode(s, m.end())
    return res

def main():
    cur = load(PATH)
    cats, data = cur['JLPT_N5_VOCAB_CATEGORIES'], cur['JLPT_N5_VOCAB_DATA']
    out = []
    for r in data:
        o = VOCAB_FULL[r['id']]
        r = dict(r)
        for f in ('word', 'reading', 'meaning'):
            if f in o:
                r[f] = o[f]
        r['ruby'] = R(o.get('hw', r['word']))
        r['ex_ja'] = R(o['ex_source'])
        r['ex_en'] = o['ex_en']
        out.append(r)
    for c in cats:
        c['count'] = sum(1 for r in out if r['cat_id'] == c['id'])
    write_js(PATH, [f'JLPT N5 Complete Vocabulary Flashcard Dataset ({len(out)} Words)'],
             [('JLPT_N5_VOCAB_CATEGORIES', cats), ('JLPT_N5_VOCAB_DATA', out)])
    print('wrote', len(out), [c['count'] for c in cats])

if __name__ == '__main__':
    main()
