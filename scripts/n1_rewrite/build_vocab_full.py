# -*- coding: utf-8 -*-
"""
Rebuild database/jlpt_n1_vocab_full_data.js (and public/database/) from:
  scripts/n1_rewrite/vocab_inventory.json (3,747 records; 1,305 already clean + 2,442 needing rewrite)
  scripts/n1_rewrite/data_vocab_full_a.py (need_rewrite slice A: records 0..610)
  scripts/n1_rewrite/data_vocab_full_b.py (need_rewrite slice B: records 611..1220)
  scripts/n1_rewrite/data_vocab_full_c.py (need_rewrite slice C: records 1221..1830)
  scripts/n1_rewrite/data_vocab_full_d.py (need_rewrite slice D: records 1831..2441)
"""
import sys, json, re, os, shutil, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from n1_lib import R, P, lint_ruby, sensitive_hits, write_js, _align, _ruby, HAS_KANJI, _tok

REPO = os.path.dirname(os.path.dirname(HERE))
PATH = os.path.join(REPO, 'database', 'jlpt_n1_vocab_full_data.js')
PUB_PATH = os.path.join(REPO, 'public', 'database', 'jlpt_n1_vocab_full_data.js')

TEMPLATES = [
    '今回のプロジェクトにおいて', '将来の発展を見据え', '時代の変化に柔軟に対応', '綿密な事前調査と検証',
    '様々な課題に直面しても', '状況を慎重に見極めながら', '毎日しっかりと練習を続けて', 'その知らせを聞いたとき',
    'この計画を円滑に進めるため', '周りの状況を落ち着いて確認', '言葉の語尾や文脈に合わせて', '優れた経験と専門的な知識',
    '心地よい風が吹き抜ける', '交通の便が良く緑豊かな', '先生や友達と一緒に', '新しい環境に早く慣れるため',
    '業務の効率化と品質向上', 'どのような困難な状況であっても', '社会の急速な変化に対応', '予期せぬトラブルが発生',
    '多くの関係者と協力しながら', '持続可能な社会の実現に向けて', '図書館で日本の文化や', 'について詳しく調べました',
    '日本の生活に慣れるために', '先生の説明をよく聞いて', '新聞やニュースを見ながら', '友達と相談しながら',
    '専門家の間で活発な議論が交わされた', 'に関する詳細な研究成果が学会で発表された', '心から楽しんでいる',
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

def has_token(word, ex_p):
    w = re.sub(r'^[〜～]|[〜～]$', '', word)
    w_ns = re.sub(r'する$', '', w)
    toks = list(_tok.tokenize(ex_p))
    for i, t in enumerate(toks):
        if t.surface == w or t.base_form == w or t.surface == w_ns or t.base_form == w_ns:
            return True
        if len(w) >= 2 and t.surface.startswith(w[:-1]) and t.base_form == w:
            return True
        acc = ''
        for j in range(i, len(toks)):
            acc += toks[j].surface
            if acc == w or acc == w_ns:
                return True
            if len(acc) > len(w) + 2:
                break
    return False

def main():
    cur = load_js(PATH)
    cats, data = cur['JLPT_N1_VOCAB_CATEGORIES'], cur['JLPT_N1_VOCAB_DATA']
    inv_path = os.path.join(HERE, 'vocab_inventory.json')
    inv_by_id = {ir['id']: ir for ir in json.load(open(inv_path, encoding='utf-8'))}
    V = load_parts()
    errs = []
    out = []
    seen_ex = {}
    for r in data:
        rid = r['id']
        suf = rid.replace('n1_v_', '')
        ir = inv_by_id[rid]
        o = V.get(rid) or V.get(suf)
        r = dict(r)
        r['word'] = ir['word']
        r['reading'] = ir['reading']
        r['meaning'] = ir['meaning']
        if o:
            if isinstance(o, (tuple, list)):
                o = {'ex_source': o[0], 'ex_en': o[1]}
            for f in ('word', 'reading', 'meaning'):
                if f in o and o[f]:
                    r[f] = o[f]
            try:
                r['ruby'] = headword_ruby(r['word'], r['reading'], o.get('hw'))
                r['ex_ja'] = R(o['ex_source'])
                r['ex_en'] = o['ex_en']
            except Exception as e:
                errs.append(f'{rid} ({r["word"]}): ruby error {e}'); continue
        else:
            if ir['need_rewrite']:
                if '--partial' in sys.argv:
                    continue
                errs.append(f'missing rewrite entry for {rid} ({r["word"]})'); continue
            # Already clean card: keep existing ruby, ex_ja, ex_en
            r['ruby'] = headword_ruby(r['word'], r['reading'])

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
        if not has_token(r['word'], ex_p):
            errs.append(f'{rid} ({r["word"]}): headword not found at token boundary in {ex_p}')
        out.append(r)

    if errs:
        print(f'{len(errs)} ERRORS:')
        for e in errs[:80]:
            print('  -', e)
        if '--force' not in sys.argv:
            sys.exit(1)

    if '--check' not in sys.argv:
        write_js(PATH,
                 [f'JLPT N1 Complete Vocabulary Flashcard Dataset ({len(out)} Words)',
                  '100% Dedicated Context Sentences, Full Ruby, Zero Templates'],
                 [('JLPT_N1_VOCAB_CATEGORIES', cats), ('JLPT_N1_VOCAB_DATA', out)])
        shutil.copyfile(PATH, PUB_PATH)
        print(f'Wrote {len(out)} N1 vocab cards to {PATH} and {PUB_PATH}')

if __name__ == '__main__':
    main()
