# -*- coding: utf-8 -*-
"""Builds database/jlpt_n5_vocab_quiz_data.js from data_vocab_quiz.py (READ/WRITE/CTX/SYN/USE)."""
import os, sys, re, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from n5_lib import R, P, lint_ruby, place_choices, balanced_targets_by_group, sensitive_hits, write_js
import data_vocab_quiz as D
REPO = os.path.dirname(os.path.dirname(HERE))
BL = '（　　　）'
SRC = '実戦オリジナル問題'
errs = []

def rd(html):
    s = re.sub(r'<ruby>[^<]*<rt>(.*?)</rt></ruby>', r'\1', html)
    return re.sub(r'<[^>]+>', '', s)

def ruby(t, **kw):
    try:
        return R(t, **kw)
    except Exception as e:
        errs.append((t[:30], str(e)[:140])); return t

items = []   # (category, dict(common fields), correct, distractors)
def u(stem):  # [[x]] -> <u>x</u>
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
    assert stem.count(BL) == 1, stem
    items.append(('文脈規定', dict(
        question=P(stem), question_ruby=ruby(stem), target_word='', target_word_reading='',
        correct_text_reading=rd(ruby(correct)), meaning_en=en, explanation=ex, ctext=correct, plain=False), correct, dist))
for stem, tgt, rdg, correct, dist, en, ex in D.SYN:
    q = u(stem)
    items.append(('類義語', dict(
        question=P(q), question_ruby=ruby(q), target_word=tgt, target_word_reading=rdg,
        correct_text_reading=rd(ruby(correct)), meaning_en=en, explanation=ex, ctext=correct, plain=False), correct, dist))
for word, rdg, correct, dist, en, ex in D.USE:
    wsrc = {'開ける': '{開|あ}ける'}.get(word, word)
    q = f'【{wsrc}】の 使い{{方|かた}}が いちばん 正しい文は どれですか。'
    items.append(('語彙用法', dict(
        question=P(q), question_ruby=ruby(q), target_word=word if re.search(r'[\u4e00-\u9fff]', word) else '', target_word_reading=rdg,
        correct_text_reading=rdg, meaning_en=en, explanation=ex, ctext=correct, plain=False), correct, dist))

# order: interleave categories so the page's sequential view is varied but ids stable by category blocks
groups = [c for c, *_ in items]
targets = balanced_targets_by_group(groups, seed=20261104)
rng = random.Random(11)
out = []
seen = set()
for n, ((cat, f, correct, dist), tgt) in enumerate(zip(items, targets), 1):
    try:
        ch, ans = place_choices(correct, dist, tgt, rng)
    except Exception as e:
        errs.append((f['question'][:20], str(e))); continue
    ch = [P(c) for c in ch] if False else ch
    if f['question'] in seen: errs.append((f['question'], 'duplicate stem'))
    seen.add(f['question'])
    if cat == '漢字読み' and not all(re.fullmatch(r'[ぁ-んー]+', c) for c in ch):
        errs.append((f['question'], 'non-kana reading choice'))
    cr = [c if f['plain'] else ruby(c) for c in ch]
    # note: P() applied at output
    for t in (f['question'], f['explanation'], ''.join(ch)):
        if sensitive_hits(t) or '公式' in t: errs.append((t[:20], 'sensitive/公式'))
    out.append({
        'id': n, 'source': SRC, 'category': cat, 'target_word': f['target_word'],
        'question': f['question'], 'question_ruby': f['question_ruby'],
        'choices': [P(c) for c in ch], 'choices_ruby': cr, 'answer': ans, 'correct_text': P(correct),
        'meaning_en': f['meaning_en'], 'explanation': ruby(f['explanation']) if False else f['explanation'],
        'target_word_reading': f['target_word_reading'], 'correct_text_reading': f['correct_text_reading'],
        'correct_text_ruby': P(correct) if f['plain'] else ruby(correct),
    })
for q in out:
    assert q['choices'][q['answer']] == q['correct_text'] and len(set(q['choices'])) == 4
    for h in [q['question_ruby']] + q['choices_ruby']:
        l = lint_ruby(h)
        if l and not (q['category'] == '漢字読み' and '<u>' in h) and not (q['category'] == '漢字表記' and h in q['choices']):
            errs.append((q['id'], 'ruby leak ' + ''.join(l)))
if errs:
    print(len(errs), 'ERRORS'); [print(' ', e) for e in errs[:60]]
    if '--force' not in sys.argv: sys.exit(1)
if '--check' not in sys.argv:
    write_js(os.path.join(REPO, 'database/jlpt_n5_vocab_quiz_data.js'),
             [f'JLPT N5 Vocabulary Quiz Dataset ({len(out)} Questions)'], [('JLPT_N5_VOCAB_QUIZ_DATA', out)])
import collections
print(len(out), collections.Counter(q['category'] for q in out), sorted(collections.Counter(q['answer'] for q in out).items()))
