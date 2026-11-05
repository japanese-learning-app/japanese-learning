# -*- coding: utf-8 -*-
"""
Rebuild database/jlpt_n4_vocab_full_data.js (and public/database/) from:
  scripts/n4_rewrite/data_vocab_full_a.py (records 0-333)
  scripts/n4_rewrite/data_vocab_full_b.py (records 334-667)
"""
import sys, json, re, os, shutil, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from n4_lib import R, P, lint_ruby, sensitive_hits, write_js, _align, _ruby, HAS_KANJI

REPO = os.path.dirname(os.path.dirname(HERE))
PATH = os.path.join(REPO, 'database', 'jlpt_n4_vocab_full_data.js')
PUB_PATH = os.path.join(REPO, 'public', 'database', 'jlpt_n4_vocab_full_data.js')

TEMPLATES = [
    '先生や友達と一緒に', '毎日しっかりと練習を続けて', '図書館で日本の文化や', '新しい言葉を覚えるために',
    '日本の生活に慣れるために', '先生の説明をよく聞いて', '新聞やニュースを見ながら', '友達と相談しながら',
    '将来の夢を叶えるために', '会議の前に', '休みの日に家族と一緒に', '大事な試験に合格できるように',
    '周囲の人と協力して', '問題が起きないように', 'インターネットを使って', '先輩のアドバイスを参考にして',
    '健康を守るために', '相手の気持ちを考えながら', '時間がかかったけれども', '昨日の授業で習った',
    'どんなに難しくても', '約束の時間に遅れないように', 'の場面で', 'をきっかけに', 'に関して'
]

def load_js(path):
    s = open(path, encoding='utf-8').read()
    dec = json.JSONDecoder()
    res = {}
    for m in re.finditer(r'window\.(\w+) = ', s):
        res[m.group(1)], _ = dec.raw_decode(s, m.end())
    return res

def load_parts():
    V = {}
    for fn in ('data_vocab_full_a.py', 'data_vocab_full_b.py'):
        p = os.path.join(HERE, fn)
        if not os.path.exists(p):
            print('  (skip missing)', fn); continue
        spec = importlib.util.spec_from_file_location(fn[:-3], p)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for k, v in m.VOCAB_PART.items():
            assert k not in V, f'duplicate key {k}'
            V[k] = v
    return V

def headword_ruby(word, reading, hw_override=None):
    if hw_override:
        return R(hw_override)
    if not HAS_KANJI(word):
        return word
    al = _align(word, reading)
    if al is not None:
        return ''.join(_ruby(txt, rt) if rt else txt for txt, rt in al)
    return _ruby(word, reading)

def main():
    cur = load_js(PATH)
    cats, data = cur['JLPT_N4_VOCAB_CATEGORIES'], cur['JLPT_N4_VOCAB_DATA']
    V = load_parts()
    errs = []
    out = []
    seen_ex = {}
    for r in data:
        rid = r['id']
        suf = rid.replace('n4_v_', '')
        o = V.get(rid) or V.get(suf)
        if not o:
            errs.append(f'missing entry for {rid}'); continue
        r = dict(r)
        for f in ('word', 'reading', 'meaning'):
            if f in o and o[f]:
                r[f] = o[f]
        if not r['meaning']:
            errs.append(f'{rid} ({r["word"]}): empty meaning')
        try:
            r['ruby'] = headword_ruby(r['word'], r['reading'], o.get('hw'))
            r['ex_ja'] = R(o['ex_source'])
            r['ex_en'] = o['ex_en']
        except Exception as e:
            errs.append(f'{rid} ({r["word"]}): ruby error {e}'); continue
        ex_p = P(r['ex_ja'])
        if len(ex_p) < 10:
            errs.append(f'{rid} ({r["word"]}): sentence too short ({len(ex_p)} chars): {ex_p}')
        for tpl in TEMPLATES:
            if tpl in ex_p:
                errs.append(f'{rid} ({r["word"]}): contains banned template "{tpl}": {ex_p}')
        if ex_p in seen_ex:
            errs.append(f'{rid} ({r["word"]}): duplicate ex_ja with {seen_ex[ex_p]}: {ex_p}')
        seen_ex[ex_p] = rid
        for t in (r['word'], r['meaning'], ex_p, r['ex_en']):
            h = sensitive_hits(t)
            if h:
                errs.append(f'{rid} ({r["word"]}): sensitive {h} in {t}')
        for h_chk in (r['ruby'], r['ex_ja']):
            lr = lint_ruby(h_chk)
            if lr:
                errs.append(f'{rid} ({r["word"]}): unrubied kanji {lr} in {h_chk}')
        out.append(r)

    if errs:
        print(f'{len(errs)} ERRORS:')
        for e in errs[:80]:
            print('  -', e)
        if '--force' not in sys.argv:
            sys.exit(1)

    for c in cats:
        c['count'] = sum(1 for r in out if r['cat_id'] == c['id'])
    write_js(PATH, [f'JLPT N4 Complete Vocabulary Flashcard Dataset ({len(out)} Words)'],
             [('JLPT_N4_VOCAB_CATEGORIES', cats), ('JLPT_N4_VOCAB_DATA', out)])
    shutil.copyfile(PATH, PUB_PATH)
    print('wrote', len(out), [c['count'] for c in cats], '(and synced to public/database/)')

if __name__ == '__main__':
    main()
