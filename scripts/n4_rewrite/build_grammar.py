# -*- coding: utf-8 -*-
"""
Builds
  database/jlpt_n4_grammar_quiz_data.js     (248 questions = 62 grammar points x 4)
  database/jlpt_n4_grammar_details.js       (62 textbook entries)
  and syncs both to public/database/
from the hand-authored part files:
  scripts/n4_rewrite/data_grammar_a.py  (gids 1-31)
  scripts/n4_rewrite/data_grammar_b.py  (gids 32-62)
"""
import os, sys, re, random, shutil, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from n4_lib import R, P, lint_ruby, place_choices, balanced_targets_by_group, sensitive_hits, write_js

REPO = os.path.dirname(os.path.dirname(HERE))
BLANK = '（　　　）'

def load_parts():
    G = {}
    for fn in ('data_grammar_a.py', 'data_grammar_b.py'):
        p = os.path.join(HERE, fn)
        if not os.path.exists(p):
            print('  (skip missing)', fn); continue
        spec = importlib.util.spec_from_file_location(fn[:-3], p)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for k, v in m.GRAMMAR.items():
            assert k not in G, f'duplicate gid {k}'
            G[k] = v
    return G

DJ_FIELDS = ('formula', 'notes_ja', 'nuance_ja', 'trap_ja')

def build(strict=True, write=True):
    G = load_parts()
    errors = []
    quiz, details = [], {}
    gids = sorted(G)
    if strict and gids != list(range(1, 63)):
        errors.append(f'missing gids: {sorted(set(range(1, 63)) - set(gids))}')
    items = []
    for gid in gids:
        g = G[gid]
        if len(g['quiz']) != 4:
            errors.append(f'gid {gid}: need exactly 4 quiz items, got {len(g["quiz"])}')
        for qi, q in enumerate(g['quiz']):
            items.append((gid, qi))
    targets = balanced_targets_by_group([gid for gid, _ in items], seed=20261105)
    rng = random.Random(7)
    qid = 0
    seen_sent = set()
    for (gid, qi), tgt in zip(items, targets):
        g = G[gid]; q = g['quiz'][qi]
        qid += 1
        stem = q['stem']
        if stem.count(BLANK) != 1:
            errors.append(f'gid {gid} q{qi}: stem must contain exactly one {BLANK}: {stem}'); continue
        correct = q['correct']
        try:
            choices, ans = place_choices(correct, q['distractors'], tgt, rng)
        except Exception as e:
            errors.append(f'gid {gid} q{qi}: {e}'); continue
        full = stem.replace(BLANK, correct)
        try:
            question_ruby = R(stem)
            sentence_ruby = R(full)
            choices_ruby = [R(c) for c in choices]
            correct_ruby = R(correct)
            notes_ruby = R(q['notes_ja']) + ' / ' + q['notes_en']
        except Exception as e:
            errors.append(f'gid {gid} q{qi}: ruby error {e}'); continue
        sp = P(full)
        if sp in seen_sent:
            errors.append(f'gid {gid} q{qi}: duplicate sentence {sp}')
        seen_sent.add(sp)
        for t in (sp, q.get('en', ''), q.get('notes_ja', ''), g.get('similar', '')):
            h = sensitive_hits(t)
            if h: errors.append(f'gid {gid} q{qi}: sensitive {h} in {t}')
        for html_check in [question_ruby, sentence_ruby] + choices_ruby:
            lr = lint_ruby(html_check)
            if lr:
                errors.append(f'gid {gid} q{qi}: unrubied kanji {lr} in {html_check}')
        quiz.append({
            'id': qid,
            'grammar_id': gid,
            'grammar': g['name'],
            'reading': g['reading'],
            'meaning_en': g['meaning_en'],
            'similar': g.get('similar', ''),
            'sentence_jp': sp,
            'sentence_furigana': sp,
            'sentence_en': q['en'],
            'question': P(stem),
            'choices': [P(c) for c in choices],
            'answer': ans,
            'correct_text': P(correct),
            'notes': notes_ruby,
            'question_ruby': question_ruby,
            'sentence_jp_ruby': sentence_ruby,
            'choices_ruby': choices_ruby,
            'correct_text_ruby': correct_ruby,
        })
    for gid in gids:
        d = G[gid]['details']
        out = {}
        for k in ('formula', 'notes_ja', 'notes_en', 'nuance_ja', 'nuance_en', 'trap_ja', 'trap_en'):
            v = d[k]
            try:
                out[k] = R(v) if k in DJ_FIELDS else v
            except Exception as e:
                errors.append(f'gid {gid} details.{k}: {e}')
        out['contrast'] = []
        if len(d['contrast']) < 2: errors.append(f'gid {gid}: contrast needs >=2 cards')
        for c in d['contrast']:
            lab = '誤用 (Incorrect)' if c['type'] == 'wrong' else '正解 (Correct)'
            try:
                out['contrast'].append({'type': c['type'], 'label': lab, 'reason_ja': R(c['reason_ja']),
                                        'reason_en': c['reason_en'], 'sentence': R(c['sentence'])})
            except Exception as e:
                errors.append(f'gid {gid} contrast: {e}')
        out['comparison'] = []
        if len(d['comparison']) < 2: errors.append(f'gid {gid}: comparison needs >=2 rows')
        for r in d['comparison']:
            try:
                out['comparison'].append({'form': R(r['form']), 'form_en': r['form_en'], 'badge': r['badge'],
                                          'badge_type': r.get('badge_type', 'both'), 'nuance_ja': R(r['nuance_ja']),
                                          'nuance_en': r['nuance_en'], 'example': R(r['example'])})
            except Exception as e:
                errors.append(f'gid {gid} comparison: {e}')
        for k in ('formula', 'notes_ja', 'nuance_ja', 'trap_ja'):
            h = sensitive_hits(d[k])
            if h: errors.append(f'gid {gid} sensitive {h} in {k}')
        details[str(gid)] = out
    if errors:
        print(f'{len(errors)} ERRORS'); [print('  -', e) for e in errors[:80]]
        if strict: return False
    if write:
        p_quiz = os.path.join(REPO, 'database/jlpt_n4_grammar_quiz_data.js')
        p_det = os.path.join(REPO, 'database/jlpt_n4_grammar_details.js')
        write_js(p_quiz,
                 [f'JLPT N4 Grammar Practice Questions ({len(quiz)} Questions)',
                  'Hand-authored original questions; answers balanced per grammar point; ruby verified'],
                 [('JLPT_N4_GRAMMAR_QUIZ_DATA', quiz)],
                 tail='// Dual alias for backwards compatibility\nwindow.JLPT_N4_QUIZ_DATA = window.JLPT_N4_GRAMMAR_QUIZ_DATA;')
        write_js(p_det,
                 ['JLPT N4 Grammar Textbook Details (hand-authored, ruby verified)'],
                 [('JLPT_N4_GRAMMAR_DETAILS', details)])
        shutil.copyfile(p_quiz, os.path.join(REPO, 'public/database/jlpt_n4_grammar_quiz_data.js'))
        shutil.copyfile(p_det, os.path.join(REPO, 'public/database/jlpt_n4_grammar_details.js'))
        print(f'wrote {len(quiz)} questions, {len(details)} details (and synced to public/database/)')
    return True

if __name__ == '__main__':
    strict = '--partial' not in sys.argv
    write = '--check' not in sys.argv
    ok = build(strict=strict, write=write)
    sys.exit(0 if ok else 1)
