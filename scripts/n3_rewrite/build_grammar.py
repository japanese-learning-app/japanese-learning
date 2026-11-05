# -*- coding: utf-8 -*-
"""
Builds:
  database/jlpt_n3_grammar_quiz_data.js     (728 questions = 182 grammar points x 4)
  database/jlpt_n3_grammar_details.js       (182 textbook entries)
  and syncs both to public/database/
from:
  scripts/n3_rewrite/base_grammar_details.json (existing metadata/formula/notes/nuance/trap)
  scripts/n3_rewrite/data_grammar_a.py  (gids 1-60)
  scripts/n3_rewrite/data_grammar_b.py  (gids 61-121)
  scripts/n3_rewrite/data_grammar_c.py  (gids 122-182)
"""
import os, sys, re, json, random, shutil, importlib.util, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from n3_lib import R, P, lint_ruby, place_choices, balanced_targets_by_group, sensitive_hits, write_js

REPO = os.path.dirname(os.path.dirname(HERE))
BLANK = '（　　　）'

BANNED_PHRASES = [
    '山田さんは熱心に仕事に取り組んだ結果',
    '毎日の努力を積み重ねたからこそ',
    '会議の資料を隅々まで確認し',
    '文脈の判断を誤って安易に',
    '文脈に応じて',
    'を適切に使い分けることが大切です',
]

def _prep_ja(t):
    if not t:
        return ''
    def rep_out(src, old, new):
        return re.sub(r'(?<![{|])' + re.escape(old), new, src)
    t = rep_out(t, '普通形', '{普通形|ふつうけい}')
    t = rep_out(t, '辞書形', '{辞書形|じしょけい}')
    t = rep_out(t, 'ます形', 'ます{形|けい}')
    t = rep_out(t, 'マス形', 'マス{形|けい}')
    t = rep_out(t, 'ない形', 'ない{形|けい}')
    t = rep_out(t, 'ナイ形', 'ナイ{形|けい}')
    t = rep_out(t, 'た形', 'た{形|けい}')
    t = rep_out(t, 'タ形', 'タ{形|けい}')
    t = rep_out(t, 'て形', 'て{形|けい}')
    t = rep_out(t, 'テ形', 'テ{形|けい}')
    t = rep_out(t, '意向形', '{意向形|いこうけい}')
    t = rep_out(t, '可能形', '{可能形|かのうけい}')
    t = rep_out(t, '受身形', '{受身形|うけみけい}')
    t = rep_out(t, '使役形', '{使役形|しえきけい}')
    t = rep_out(t, '命令形', '{命令形|めいれいけい}')
    t = rep_out(t, '条件形', '{条件形|じょうけんけい}')
    t = rep_out(t, '丁寧形', '{丁寧形|ていねいけい}')
    t = rep_out(t, 'イ形容詞', 'イ{形容詞|けいようし}')
    t = rep_out(t, 'ナ形容詞', 'ナ{形容詞|けいようし}')
    t = rep_out(t, 'い形容詞', 'い{形容詞|けいようし}')
    t = rep_out(t, 'な形容詞', 'な{形容詞|けいようし}')
    t = rep_out(t, '目上の人', '{目上|めうえ}の{人|ひと}')
    t = rep_out(t, '目上の方', '{目上|めうえ}の{方|かた}')
    t = rep_out(t, '話し手', '{話|はな}し{手|て}')
    t = rep_out(t, '聞き手', '{聞|き}き{手|て}')
    t = rep_out(t, '書き言葉', '{書|か}き{言葉|ことば}')
    t = rep_out(t, '話し言葉', '{話|はな}し{言葉|ことば}')
    t = rep_out(t, '使い分け', '{使|つか}い{分|わ}け')
    t = rep_out(t, '言い換え', '{言|い}い{換|か}え')
    t = rep_out(t, '結びつき', '{結|むす}びつき')
    t = rep_out(t, '後ろ', '{後|うし}ろ')
    t = rep_out(t, '前後', '{前後|ぜんご}')
    t = rep_out(t, '直後', '{直後|ちょくご}')
    t = rep_out(t, '直前', '{直前|ちょくぜん}')
    t = rep_out(t, '場合', '{場合|ばあい}')
    return R(t)

def load_base():
    p = os.path.join(HERE, 'base_grammar_details.json')
    return json.load(open(p, encoding='utf-8'))

def load_parts():
    G = {}
    for fn in ('data_grammar_a.py', 'data_grammar_b.py', 'data_grammar_c.py'):
        p = os.path.join(HERE, fn)
        if not os.path.exists(p):
            print('  (skip missing)', fn); continue
        spec = importlib.util.spec_from_file_location(fn[:-3], p)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for k, v in m.GRAMMAR.items():
            assert int(k) not in G, f'duplicate gid {k}'
            G[int(k)] = v
    return G

def build(strict=True, write=True):
    base = load_base()
    G = load_parts()
    errors = []
    quiz, details = [], {}
    gids = sorted(G)
    if strict and gids != list(range(1, 183)):
        errors.append(f'missing gids: {sorted(set(range(1, 183)) - set(gids))}')
    items = []
    for gid in gids:
        g = G[gid]
        if len(g['quiz']) != 4:
            errors.append(f'gid {gid}: need exactly 4 quiz items, got {len(g["quiz"])}')
        for qi in range(len(g['quiz'])):
            items.append((gid, qi))

    targets = balanced_targets_by_group([gid for gid, _ in items], seed=20261106)
    rng = random.Random(33)
    qid = 0
    seen_sent = set()
    full_by_gid = collections.defaultdict(list)

    for (gid, qi), tgt in zip(items, targets):
        b = base[str(gid)]
        g = G[gid]
        q = g['quiz'][qi]
        if isinstance(q, (tuple, list)):
            stem, correct, distractors, en, notes_ja = q
        else:
            stem, correct, distractors, en, notes_ja = q['stem'], q['correct'], q['distractors'], q['en'], q.get('notes_ja', '')
        qid += 1
        if stem.count(BLANK) != 1:
            errors.append(f'gid {gid} q{qi}: stem must contain exactly one {BLANK}: {stem}'); continue
        try:
            choices, ans = place_choices(P(correct), [P(d) for d in distractors], tgt, rng)
            # map back to source with ruby hints
            cmap = {P(correct): correct}
            for d in distractors:
                cmap[P(d)] = d
            choices_src = [cmap[c] for c in choices]
        except Exception as e:
            errors.append(f'gid {gid} q{qi}: {e}'); continue

        full_src = stem.replace(BLANK, correct)
        try:
            question_ruby = _prep_ja(stem)
            sentence_ruby = _prep_ja(full_src)
            choices_ruby = [_prep_ja(c) for c in choices_src]
            correct_ruby = _prep_ja(correct)
            notes_ruby = _prep_ja(notes_ja)
        except Exception as e:
            errors.append(f'gid {gid} q{qi}: ruby error {e}'); continue

        sp = P(full_src)
        full_by_gid[gid].append((sp, sentence_ruby))
        if sp in seen_sent:
            errors.append(f'gid {gid} q{qi}: duplicate sentence {sp}')
        seen_sent.add(sp)
        for bad in BANNED_PHRASES:
            if bad in sp:
                errors.append(f'gid {gid} q{qi}: banned phrase {bad} in {sp}')
        for t in (sp, en, notes_ja, g.get('similar', b.get('similar', ''))):
            h = sensitive_hits(t)
            if h:
                errors.append(f'gid {gid} q{qi}: sensitive {h} in {t}')
        for html_check in [question_ruby, sentence_ruby] + choices_ruby:
            lr = lint_ruby(html_check)
            if lr:
                errors.append(f'gid {gid} q{qi}: unrubied kanji {lr} in {html_check}')

        rdg = g.get('reading', b['reading'])
        if re.search(r'[a-zA-Z]', rdg):
            errors.append(f'gid {gid}: reading is still romaji: {rdg}')

        quiz.append({
            'id': qid,
            'grammar_id': gid,
            'grammar': g.get('name', b['grammar']),
            'reading': rdg,
            'meaning_en': g.get('meaning_en', b['meaning_en']),
            'similar': P(g.get('similar', b['similar'])),
            'sentence_jp': sp,
            'sentence_furigana': sp,
            'sentence_en': en,
            'question': P(stem),
            'choices': choices,
            'answer': ans,
            'correct_text': P(correct),
            'notes': notes_ruby,
            'question_ruby': question_ruby,
            'sentence_jp_ruby': sentence_ruby,
            'choices_ruby': choices_ruby,
            'correct_text_ruby': correct_ruby,
        })

    for gid in gids:
        b = base[str(gid)]
        g = G[gid]
        d_base = b['details']
        gname = g.get('name', b['grammar'])
        out = {}
        for k in ('formula', 'notes_ja', 'notes_en', 'nuance_ja', 'nuance_en', 'trap_ja', 'trap_en'):
            v = g.get(k, d_base.get(k, ''))
            v = v.replace('準じて', '従って').replace('準拠', '対応')
            try:
                out[k] = _prep_ja(v) if k.endswith('_ja') or k == 'formula' else v
            except Exception as e:
                errors.append(f'gid {gid} details.{k}: {e}')
                out[k] = v

        w_sent, w_ja, w_en = g['wrong']
        q_rubies = [r for _, r in full_by_gid[gid]]
        try:
            out['contrast'] = [
                {
                    'type': 'wrong',
                    'label': '誤用 (Incorrect)',
                    'reason_ja': _prep_ja(w_ja),
                    'reason_en': w_en,
                    'sentence': _prep_ja(w_sent),
                },
                {
                    'type': 'correct',
                    'label': f'正解 (Correct with {P(gname)})',
                    'reason_ja': _prep_ja('文脈と接続形式が自然に呼応した正しい用例'),
                    'reason_en': f'Natural intermediate usage and collocation for {P(gname)}',
                    'sentence': q_rubies[0] if q_rubies else '',
                },
                {
                    'type': 'correct',
                    'label': f'正解 (Correct with {P(gname)})',
                    'reason_ja': _prep_ja('日常会話・実務でよく使われる自然な表現'),
                    'reason_en': f'Authentic practical example using {P(gname)}',
                    'sentence': q_rubies[1] if len(q_rubies) > 1 else '',
                },
            ]
        except Exception as e:
            errors.append(f'gid {gid} contrast: {e}')

        comp_rows = d_base.get('comparison', [])
        comp_ex = g.get('comp_ex', [])
        out['comparison'] = []
        for idx_c, r in enumerate(comp_rows):
            try:
                if idx_c == 0:
                    ex_html = q_rubies[2] if len(q_rubies) > 2 else q_rubies[0]
                else:
                    ex_src = comp_ex[idx_c - 1] if idx_c - 1 < len(comp_ex) else r['example']
                    ex_html = _prep_ja(ex_src)
                for bad in BANNED_PHRASES:
                    if bad in P(ex_html):
                        errors.append(f'gid {gid} comparison[{idx_c}] has banned template: {P(ex_html)}')
                out['comparison'].append({
                    'form': _prep_ja(r['form']),
                    'form_en': r['form_en'],
                    'badge': r['badge'],
                    'badge_type': r.get('badge_type', 'both'),
                    'nuance_ja': _prep_ja(r['nuance_ja']),
                    'nuance_en': r['nuance_en'],
                    'example': ex_html,
                })
            except Exception as e:
                errors.append(f'gid {gid} comparison[{idx_c}]: {e}')

        for k in ('formula', 'notes_ja', 'nuance_ja', 'trap_ja'):
            h = sensitive_hits(out.get(k, ''))
            if h:
                errors.append(f'gid {gid} sensitive {h} in {k}')
        details[str(gid)] = out

    if errors:
        print(f'{len(errors)} ERRORS')
        for e in errors[:80]:
            print('  -', e)
        if strict:
            return False

    if write:
        p_quiz = os.path.join(REPO, 'database/jlpt_n3_grammar_quiz_data.js')
        p_det = os.path.join(REPO, 'database/jlpt_n3_grammar_details.js')
        write_js(p_quiz,
                 [f'JLPT N3 Grammar Practice Questions ({len(quiz)} Questions)',
                  '100% Balanced 25.0% Choices & Full Accurate Furigana (Ruby)'],
                 [('JLPT_N3_GRAMMAR_QUIZ_DATA', quiz)],
                 tail='// Dual alias for backwards compatibility\nwindow.JLPT_N3_QUIZ_DATA = window.JLPT_N3_GRAMMAR_QUIZ_DATA;')
        write_js(p_det,
                 [f'JLPT N3 Complete Masterpiece Grammar Details (All {len(details)} Items)'],
                 [('JLPT_N3_GRAMMAR_DETAILS', details)])
        shutil.copyfile(p_quiz, os.path.join(REPO, 'public/database/jlpt_n3_grammar_quiz_data.js'))
        shutil.copyfile(p_det, os.path.join(REPO, 'public/database/jlpt_n3_grammar_details.js'))
        print(f'wrote {len(quiz)} N3 grammar quiz questions, {len(details)} details (and synced to public/database/)')
    return True

if __name__ == '__main__':
    strict = '--partial' not in sys.argv
    write = '--check' not in sys.argv
    ok = build(strict=strict, write=write)
    sys.exit(0 if ok else 1)
