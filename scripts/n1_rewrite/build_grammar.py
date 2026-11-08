# -*- coding: utf-8 -*-
"""
Builds:
  database/jlpt_n1_grammar_quiz_data.js     (508 questions = 127 grammar points x 4)
  database/jlpt_n1_grammar_details.js       (127 textbook entries)
  and syncs both to public/database/
from:
  scripts/n1_rewrite/grammar_inventory.json (127 catalog items)
  scripts/n1_rewrite/data_grammar_a.py  (gids 1-42)
  scripts/n1_rewrite/data_grammar_b.py  (gids 43-84)
  scripts/n1_rewrite/data_grammar_c.py  (gids 85-127)
"""
import os, sys, re, json, random, shutil, importlib.util, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from n1_lib import R, P, lint_ruby, place_choices, balanced_targets_by_group, sensitive_hits, write_js

REPO = os.path.dirname(os.path.dirname(HERE))
BLANK = '（　　　）'

BANNED_PHRASES = [
    '重要性が高く評価されている',
    '全社員が一丸となって努力した結果',
    '友達との気軽な雑談で',
    '責任ある立場として',
    '日常の会話では無理に難しい表現を使わず',
    '山田さんは熱心に仕事に取り組んだ結果',
    '毎日の努力を積み重ねたからこそ',
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
    t = rep_out(t, '生じる', '{生|しょう}じる')
    t = rep_out(t, '生じ', '{生|しょう}じ')
    t = rep_out(t, '生まれる', '{生|う}まれる')
    t = rep_out(t, '生まれ', '{生|う}まれ')
    t = rep_out(t, '生み出す', '{生|う}み{出|だ}す')
    t = rep_out(t, '生み', '{生|う}み')
    t = rep_out(t, '生む', '{生|う}む')
    t = rep_out(t, '生き残ら', '{生|い}き{残|のこ}ら')
    t = rep_out(t, '生き残り', '{生|い}き{残|のこ}り')
    t = rep_out(t, '生き残る', '{生|い}き{残|のこ}る')
    t = rep_out(t, '生きる', '{生|い}きる')
    t = rep_out(t, '生かす', '{生|い}かす')
    t = rep_out(t, '生かし', '{生|い}かし')
    t = rep_out(t, '日用品', '{日用品|にちようひん}')
    t = rep_out(t, '日常', '{日常|にちじょう}')
    t = rep_out(t, '三十分', '{三十分|さんじゅっぷん}')
    t = rep_out(t, '十分', '{十分|じゅうぶん}')
    t = rep_out(t, 'お腹が空い', 'お{腹|なか}が{空|す}い')
    t = rep_out(t, 'お腹が空く', 'お{腹|なか}が{空|す}く')
    t = rep_out(t, '開く', '{開|ひら}く')
    return R(t)

def load_inv():
    p = os.path.join(HERE, 'grammar_inventory.json')
    return {it['gid']: it for it in json.load(open(p, encoding='utf-8'))}

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
    inv = load_inv()
    G = load_parts()
    errors = []
    quiz, details = [], {}
    gids = sorted(G)
    if strict and gids != list(range(1, 128)):
        errors.append(f'missing gids: {sorted(set(range(1, 128)) - set(gids))}')
    items = []
    for gid in gids:
        g = G[gid]
        if len(g['quiz']) != 4:
            errors.append(f'gid {gid}: need exactly 4 quiz items, got {len(g["quiz"])}')
        for qi in range(len(g['quiz'])):
            items.append((gid, qi))

    targets = balanced_targets_by_group([gid for gid, _ in items], seed=20261106)
    rng = random.Random(37)
    qid = 0
    seen_sent = set()
    full_by_gid = collections.defaultdict(list)

    for (gid, qi), tgt in zip(items, targets):
        cat = inv[gid]
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
        for t in (sp, en, notes_ja, g.get('similar', '')):
            h = sensitive_hits(t)
            if h:
                errors.append(f'gid {gid} q{qi}: sensitive {h} in {t}')
        for html_check in [question_ruby, sentence_ruby] + choices_ruby:
            lr = lint_ruby(html_check)
            if lr:
                errors.append(f'gid {gid} q{qi}: unrubied kanji {lr} in {html_check}')

        raw_m = cat['meaning']
        m_parts = re.split(r'\(|\)', raw_m)
        meaning_ja_default = m_parts[0].strip()
        meaning_en_default = m_parts[1].strip() if len(m_parts) > 1 else raw_m

        gname = g.get('name', cat['term'].replace('〜', '').strip())
        rdg = g.get('reading', cat['reading'])
        meaning_en = g.get('meaning_en', meaning_en_default)

        quiz.append({
            'id': qid,
            'grammar_id': gid,
            'grammar': P(gname),
            'reading': rdg,
            'meaning_en': meaning_en,
            'similar': P(g.get('similar', '類義の上級表現')),
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
        cat = inv[gid]
        g = G[gid]
        raw_m = cat['meaning']
        m_parts = re.split(r'\(|\)', raw_m)
        meaning_ja_default = m_parts[0].strip()
        meaning_en_default = m_parts[1].strip() if len(m_parts) > 1 else raw_m

        gname = g.get('name', cat['term'].replace('〜', '').strip())
        meaning_ja = g.get('meaning_ja', meaning_ja_default)
        meaning_en = g.get('meaning_en', meaning_en_default)

        formula_src = g.get('formula', f'名詞／動詞普通形 ＋ <strong>{gname}</strong>')
        notes_ja_src = g.get('notes_ja', f'「{gname}」は、{meaning_ja}という意味を表すN1の重要文型です。評論文・報道・改まった挨拶などで幅広く用いられます。')
        notes_en_src = g.get('notes_en', f"'{P(gname)}' is an advanced N1 pattern meaning '{meaning_en}', commonly used in formal writing, editorials, and speeches.")
        nuance_ja_src = g.get('nuance_ja', f'「{gname}」は、<strong>『{meaning_ja}』</strong>という本質的ニュアンスを持ち、前後の文脈の論理関係や話し手の強い評価を明確に示します。')
        nuance_en_src = g.get('nuance_en', f"'{P(gname)}' expresses <strong>{meaning_en}</strong>, highlighting logical relationships or strong speaker stance in formal contexts.")
        w_sent, w_ja, w_en = g['wrong']
        trap_ja_src = g.get('trap_ja', f'{w_ja} 接続の形や前後の文脈の釣り合いに注意しましょう。')
        trap_en_src = g.get('trap_en', f'{w_en} Pay close attention to required grammatical connection and register.')

        out = {}
        for k, src_v in (
            ('formula', formula_src),
            ('notes_ja', notes_ja_src),
            ('notes_en', notes_en_src),
            ('nuance_ja', nuance_ja_src),
            ('nuance_en', nuance_en_src),
            ('trap_ja', trap_ja_src),
            ('trap_en', trap_en_src),
        ):
            try:
                out[k] = _prep_ja(src_v) if k.endswith('_ja') or k == 'formula' else src_v
            except Exception as e:
                errors.append(f'gid {gid} details.{k}: {e}')
                out[k] = src_v

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
                    'reason_en': f'Natural N1 usage and collocation for {P(gname)}',
                    'sentence': q_rubies[0] if q_rubies else '',
                },
                {
                    'type': 'correct',
                    'label': f'正解 (Correct with {P(gname)})',
                    'reason_ja': _prep_ja('論説・実務でよく使われる格調高い表現'),
                    'reason_en': f'Authentic advanced example using {P(gname)}',
                    'sentence': q_rubies[1] if len(q_rubies) > 1 else '',
                },
            ]
        except Exception as e:
            errors.append(f'gid {gid} contrast: {e}')

        comp_form, comp_en, comp_nuance_ja, comp_nuance_en, comp_ex_src = g['comp']
        try:
            out['comparison'] = [
                {
                    'form': _prep_ja(f'〜{gname}'),
                    'form_en': meaning_en,
                    'badge': 'N1必須表現',
                    'badge_type': 'both',
                    'nuance_ja': _prep_ja(meaning_ja),
                    'nuance_en': meaning_en,
                    'example': q_rubies[2] if len(q_rubies) > 2 else q_rubies[0],
                },
                {
                    'form': _prep_ja(comp_form),
                    'form_en': comp_en,
                    'badge': '類義・関連表現',
                    'badge_type': 'neutral',
                    'nuance_ja': _prep_ja(comp_nuance_ja),
                    'nuance_en': comp_nuance_en,
                    'example': _prep_ja(comp_ex_src),
                },
            ]
        except Exception as e:
            errors.append(f'gid {gid} comparison: {e}')

        for k in ('formula', 'notes_ja', 'nuance_ja', 'trap_ja'):
            h = sensitive_hits(out.get(k, ''))
            if h:
                errors.append(f'gid {gid} sensitive {h} in {k}')
            lr = lint_ruby(out.get(k, ''))
            if lr:
                errors.append(f'gid {gid} unrubied {lr} in {k}')
        for c_item in out.get('contrast', []):
            for fk in ('reason_ja', 'sentence'):
                h = sensitive_hits(c_item.get(fk, ''))
                if h: errors.append(f'gid {gid} contrast sensitive {h}')
                lr = lint_ruby(c_item.get(fk, ''))
                if lr: errors.append(f'gid {gid} contrast unrubied {lr} in {c_item.get(fk,"")}')
        for c_item in out.get('comparison', []):
            for fk in ('form', 'nuance_ja', 'example'):
                h = sensitive_hits(c_item.get(fk, ''))
                if h: errors.append(f'gid {gid} comp sensitive {h}')
                lr = lint_ruby(c_item.get(fk, ''))
                if lr: errors.append(f'gid {gid} comp unrubied {lr} in {c_item.get(fk,"")}')

        details[str(gid)] = out

    if errors:
        print(f'{len(errors)} ERRORS')
        for e in errors[:80]:
            print('  -', e)
        if strict:
            return False

    if write:
        p_quiz = os.path.join(REPO, 'database/jlpt_n1_grammar_quiz_data.js')
        p_det = os.path.join(REPO, 'database/jlpt_n1_grammar_details.js')
        write_js(p_quiz,
                 [f'JLPT N1 Grammar Practice Questions ({len(quiz)} Questions)',
                  '100% Balanced 25.0% Choices & Full Accurate Furigana (Ruby)'],
                 [('JLPT_N1_GRAMMAR_QUIZ_DATA', quiz)],
                 tail='// Dual alias for backwards compatibility\nwindow.JLPT_N1_QUIZ_DATA = window.JLPT_N1_GRAMMAR_QUIZ_DATA;')
        write_js(p_det,
                 [f'JLPT N1 Complete Masterpiece Grammar Details (All {len(details)} Items)'],
                 [('JLPT_N1_GRAMMAR_DETAILS', details)])
        shutil.copyfile(p_quiz, os.path.join(REPO, 'public/database/jlpt_n1_grammar_quiz_data.js'))
        shutil.copyfile(p_det, os.path.join(REPO, 'public/database/jlpt_n1_grammar_details.js'))
        print(f'wrote {len(quiz)} N1 grammar quiz questions, {len(details)} details (and synced to public/database/)')
    return True

if __name__ == '__main__':
    strict = '--partial' not in sys.argv
    write = '--check' not in sys.argv
    ok = build(strict=strict, write=write)
    sys.exit(0 if ok else 1)
