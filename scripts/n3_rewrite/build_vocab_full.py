# -*- coding: utf-8 -*-
"""
Rebuild database/jlpt_n3_vocab_full_data.js (and public/database/) from:
  scripts/n3_rewrite/data_vocab_full_a.py (records 0-459)
  scripts/n3_rewrite/data_vocab_full_b.py (records 460-919)
  scripts/n3_rewrite/data_vocab_full_c.py (records 920-1379)
  scripts/n3_rewrite/data_vocab_full_d.py (records 1380-1840)
"""
import sys, json, re, os, shutil, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from n3_lib import R, P, lint_ruby, sensitive_hits, write_js, _align, _ruby, HAS_KANJI, _tok

REPO = os.path.dirname(os.path.dirname(HERE))
PATH = os.path.join(REPO, 'database', 'jlpt_n3_vocab_full_data.js')
PUB_PATH = os.path.join(REPO, 'public', 'database', 'jlpt_n3_vocab_full_data.js')

TEMPLATES = [
    '今回のプロジェクトにおいて', '将来の発展を見据え', '時代の変化に柔軟に対応', '綿密な事前調査と検証',
    '様々な課題に直面しても', '状況を慎重に見極めながら', '毎日しっかりと練習を続けて', 'その知らせを聞いたとき',
    'この計画を円滑に進めるため', '周りの状況を落ち着いて確認', '言葉の語尾や文脈に合わせて', '優れた経験と専門的な知識',
    '心地よい風が吹き抜ける', '交通の便が良く緑豊かな', '先生や友達と一緒に', '新しい環境に早く慣れるため',
    '業務の効率化と品質向上', 'どのような困難な状況であっても', '社会の急速な変化に対応', '予期せぬトラブルが発生',
    '多くの関係者と協力しながら', '持続可能な社会の実現に向けて', '図書館で日本の文化や', 'について詳しく調べました',
    '日本の生活に慣れるために', '先生の説明をよく聞いて', '新聞やニュースを見ながら', '友達と相談しながら',
]

def load_js(path):
    s = open(path, encoding='utf-8').read()
    dec = json.JSONDecoder()
    res = {}
    for m in re.finditer(r'window\.(\w+)\s*=\s*(?=[\[\{])', s):
        res[m.group(1)], _ = dec.raw_decode(s[m.end():].lstrip())
    return res

def load_parts():
    V = {}
    for fn in ('data_vocab_full_a.py', 'data_vocab_full_b.py', 'data_vocab_full_c.py', 'data_vocab_full_d.py'):
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
    cats, data = cur['JLPT_N3_VOCAB_CATEGORIES'], cur['JLPT_N3_VOCAB_DATA']
    inv_path = os.path.join(HERE, 'vocab_inventory.json')
    inv_by_id = {}
    if os.path.exists(inv_path):
        for ir in json.load(open(inv_path, encoding='utf-8')):
            inv_by_id[ir['id']] = ir
    V = load_parts()
    errs = []
    out = []
    seen_ex = {}
    for r in data:
        rid = r['id']
        suf = rid.replace('n3_v_', '')
        o = V.get(rid) or V.get(suf)
        if not o:
            if '--partial' in sys.argv:
                continue
            errs.append(f'missing entry for {rid}'); continue
        if isinstance(o, (tuple, list)):
            o = {'ex_source': o[0], 'ex_en': o[1]}
        r = dict(r)
        if rid in inv_by_id:
            ir = inv_by_id[rid]
            for f in ('word', 'reading', 'meaning'):
                if ir.get(f):
                    r[f] = ir[f]
            if ir.get('hw') and 'hw' not in o:
                o['hw'] = ir['hw']
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
        if len(ex_p) < 12:
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
        # Check that the headword (or verb/adj stem) appears in ex_p at a clean token boundary
        w_clean = re.sub(r'^[〜～]|[〜～]$', '', r['word'])
        w_no_suru = re.sub(r'する$', '', w_clean)
        toks = list(_tok.tokenize(ex_p))
        surfaces = [t.surface for t in toks]
        bases = [t.base_form for t in toks]
        starts, ends, pos = set(), set(), 0
        for s_tok in surfaces:
            starts.add(pos); pos += len(s_tok); ends.add(pos)
        hw_ok = (w_clean in surfaces or w_clean in bases or w_no_suru in surfaces or w_no_suru in bases)
        if not hw_ok:
            for m_hw in re.finditer(re.escape(w_no_suru), ex_p):
                if m_hw.start() in starts and m_hw.end() in ends:
                    hw_ok = True; break
                if m_hw.start() in starts and r['cat_id'] in (2, 3, 4, 5):
                    hw_ok = True; break
        if not hw_ok and len(w_no_suru) >= 2 and r['cat_id'] in (2, 3, 5):
            stem_w = w_no_suru[:-1]
            if stem_w in ex_p:
                hw_ok = True
        if not hw_ok:
            errs.append(f'{rid} ({r["word"]}): headword not found at token boundary in ex_ja: {ex_p}')
        out.append(r)

    if errs:
        print(f'{len(errs)} ERRORS:')
        for e in errs[:80]:
            print('  -', e)
        if '--force' not in sys.argv:
            sys.exit(1)

    if '--check' in sys.argv or '--partial' in sys.argv:
        print(f'Checked {len(out)} vocab cards cleanly!')
        return

    for c in cats:
        c['count'] = sum(1 for r in out if r['cat_id'] == c['id'])
    write_js(PATH, [f'JLPT N3 Complete Vocabulary Flashcard Dataset ({len(out)} Words)',
                    'Clean readings, authentic non-sensitive examples, and English translations'],
             [('JLPT_N3_VOCAB_CATEGORIES', cats), ('JLPT_N3_VOCAB_DATA', out)])
    shutil.copyfile(PATH, PUB_PATH)
    print('wrote', len(out), [c['count'] for c in cats], '(and synced to public/database/)')

if __name__ == '__main__':
    main()
