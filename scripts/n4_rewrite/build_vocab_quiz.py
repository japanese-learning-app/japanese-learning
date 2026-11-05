# -*- coding: utf-8 -*-
"""
Builds database/jlpt_n4_vocab_quiz_data.js (and public/database/) from:
  scripts/n4_rewrite/data_vocab_quiz.py (READ/WRITE/CTX/SYN/USE, 365 questions total).
"""
import os, sys, re, random, shutil, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from n4_lib import R, P, lint_ruby, place_choices, balanced_targets_by_group, sensitive_hits, write_js
import data_vocab_quiz as D

REPO = os.path.dirname(os.path.dirname(HERE))
BL = '（　　　）'
SRC = 'JLPT N4 実戦オリジナル問題'
errs = []

def rd(html):
    s = re.sub(r'<ruby>[^<]*<rt>(.*?)</rt></ruby>', r'\1', html)
    return re.sub(r'<[^>]+>', '', s)

def ruby(t, **kw):
    try:
        return R(t, **kw)
    except Exception as e:
        errs.append((t[:30], str(e)[:140])); return t

items = []
def u(stem):
    return re.sub(r'\[\[(.*?)\]\]', r'<u>\1</u>', stem)

for stem, tgt, rdg, dist, en, ex in D.READ:
    q = u(stem)
    items.append(('漢字読み', dict(
        question=P(q), question_ruby=ruby(q, skip_u=True), target_word=tgt, target_word_reading=rdg,
        correct_text_reading=rdg, meaning_en=en, explanation=ex, ctext=rdg, plain=True), rdg, dist))

for stem, correct, dist, en, ex in D.WRITE:
    q = u(stem); tgt = re.search(r'\[\[(.*?)\]\]', stem).group(1)
    items.append(('漢字表記', dict(
        question=P(q), question_ruby=ruby(q), target_word=tgt, target_word_reading=tgt,
        correct_text_reading=tgt, meaning_en=en, explanation=ex, ctext=correct, plain=True), correct, dist))

for stem, correct, dist, en, ex in D.CTX:
    stem = stem.replace('\\u3000', '\u3000')
    if stem.count(BL) != 1:
        errs.append((stem[:30], f'CTX stem must contain exactly 1 {BL}'))
    items.append(('文脈規定', dict(
        question=P(stem), question_ruby=ruby(stem), target_word='', target_word_reading='',
        correct_text_reading=rd(ruby(correct)), meaning_en=en, explanation=ex, ctext=correct, plain=False), correct, dist))

for stem, tgt, rdg, correct, dist, en, ex in D.SYN:
    q = u(stem)
    items.append(('類義語', dict(
        question=P(q), question_ruby=ruby(q), target_word=tgt, target_word_reading=rdg,
        correct_text_reading=rd(ruby(correct)), meaning_en=en, explanation=ex, ctext=correct, plain=False), correct, dist))

for word, rdg, correct, dist, en, ex in D.USE:
    wsrc = {'開く': '{開|ひら}く', '空く': '{空|あ}く', '生きる': '{生|い}きる'}.get(word, word)
    q = f'【{wsrc}】の 使い{{方|かた}}として いちばん よいものを 1つ 選んでください。'
    items.append(('語彙用法', dict(
        question=P(q), question_ruby=ruby(q), target_word=P(word) if re.search(r'[\u4e00-\u9fff]', P(word)) else '', target_word_reading=rdg,
        correct_text_reading=rdg, meaning_en=en, explanation=ex, ctext=correct, plain=False), correct, dist))

groups = [c for c, *_ in items]
targets = balanced_targets_by_group(groups, seed=20261105)
rng = random.Random(17)
out = []
seen = set()

for n, ((cat, f, correct, dist), tgt) in enumerate(zip(items, targets), 1):
    try:
        ch, ans = place_choices(correct, dist, tgt, rng)
    except Exception as e:
        errs.append((f['question'][:25], str(e))); continue
    if f['question'] in seen:
        errs.append((f['question'], 'duplicate stem'))
    seen.add(f['question'])
    if cat == '漢字読み' and not all(re.fullmatch(r'[ぁ-んー]+', P(c)) for c in ch):
        errs.append((f['question'], f'non-kana reading choice: {ch}'))
    cr = [P(c) if f['plain'] else ruby(c) for c in ch]
    exp_clean = P(f['explanation'])
    for t in (f['question'], exp_clean, ''.join(P(c) for c in ch)):
        h = sensitive_hits(t)
        if h:
            errs.append((t[:25], f'sensitive {h}'))
    out.append({
        'id': n,
        'source': SRC,
        'category': cat,
        'target_word': P(f['target_word']),
        'question': f['question'],
        'question_ruby': f['question_ruby'],
        'choices': [P(c) for c in ch],
        'choices_ruby': cr,
        'answer': ans,
        'correct_text': P(correct),
        'meaning_en': f['meaning_en'],
        'explanation': exp_clean,
        'target_word_reading': f['target_word_reading'],
        'correct_text_reading': f['correct_text_reading'],
        'correct_text_ruby': P(correct) if f['plain'] else ruby(correct),
    })

for q in out:
    assert q['choices'][q['answer']] == q['correct_text'] and len(set(q['choices'])) == 4
    for h in [q['question_ruby']] + q['choices_ruby']:
        l = lint_ruby(h)
        if l and not (q['category'] == '漢字読み' and '<u>' in h) and not (q['category'] == '漢字表記' and h in q['choices']):
            errs.append((q['id'], 'ruby leak ' + ''.join(l) + ' in ' + h))

if len(out) != 365:
    errs.append(('TOTAL_COUNT', f'Expected 365 questions, got {len(out)}'))

if errs:
    print(len(errs), 'ERRORS')
    for e in errs[:80]:
        print(' ', e)
    if '--force' not in sys.argv:
        sys.exit(1)

if '--check' not in sys.argv:
    p_out = os.path.join(REPO, 'database/jlpt_n4_vocab_quiz_data.js')
    p_pub = os.path.join(REPO, 'public/database/jlpt_n4_vocab_quiz_data.js')
    write_js(p_out,
             [f'JLPT N4 Vocabulary Quiz Dataset ({len(out)} Questions)'],
             [('JLPT_N4_VOCAB_QUIZ_DATA', out)])
    shutil.copyfile(p_out, p_pub)

print(len(out), collections.Counter(q['category'] for q in out), sorted(collections.Counter(q['answer'] for q in out).items()))
