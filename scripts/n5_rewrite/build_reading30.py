# -*- coding: utf-8 -*-
"""
Build database/jlpt_n5_reading_data.js (30 passages: 14 short + 10 mid + 6 info)
from data_reading_a.py and data_reading_b.py.
"""
import os, sys, re, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
from n5_lib import R, P, lint_ruby, balanced_targets_by_group, place_choices, sensitive_hits
from data_reading_a import PASSAGES_SHORT
from data_reading_b import PASSAGES_MID_INFO


def RR(t):
    """Project-wide fixed readings for words the library needs disambiguated."""
    def rep_outside(src, old, new):
        return re.sub(r'(?<![{|])' + re.escape(old), new, src)
    t = rep_outside(t, '何と言', '{何|なん}と言')
    t = re.sub(r'(?<![{|])辛', '{辛|から}', t)
    t = re.sub(r'(?<![{|])日本(?!語|人|料理)', '{日本|にほん}', t)
    t = rep_outside(t, '行ってくる', '{行|い}ってくる')
    t = rep_outside(t, '通っ', '{通|かよ}っ')
    t = rep_outside(t, '留学生', '{留学生|りゅうがくせい}')
    t = rep_outside(t, '夕方', '{夕方|ゆうがた}')
    t = rep_outside(t, '仕方', '{仕方|しかた}')
    t = rep_outside(t, '一生懸命', '{一生懸命|いっしょうけんめい}')
    t = rep_outside(t, '一日中', '{一日中|いちにちじゅう}')
    t = re.sub(r'(?<![\d{|])1日に', '{1日|いちにち}に', t)
    t = rep_outside(t, '空き', '{空|あ}き')
    t = rep_outside(t, '空気', '{空気|くうき}')
    t = rep_outside(t, '空港', '{空港|くうこう}')
    t = rep_outside(t, '開く', '{開|あ}く')
    t = rep_outside(t, '開き', '{開|あ}き')
    t = rep_outside(t, '開いて', '{開|あ}いて')
    t = rep_outside(t, '開店', '{開店|かいてん}')
    t = rep_outside(t, 'やり方', 'やり{方|かた}')
    t = rep_outside(t, '飲み方', '飲み{方|かた}')
    t = rep_outside(t, '使い方', '{使|つか}い{方|かた}')
    t = rep_outside(t, '使い分け', '{使|つか}い{分|わ}け')
    t = rep_outside(t, '高校生', '{高校生|こうこうせい}')
    t = rep_outside(t, '中学生', '{中学生|ちゅうがくせい}')
    t = rep_outside(t, '小学生', '{小学生|しょうがくせい}')
    t = rep_outside(t, '大学生', '{大学生|だいがくせい}')
    t = rep_outside(t, '生活', '{生活|せいかつ}')
    t = re.sub(r'（月）', '（{月|げつ}）', t)
    return R(t)


def ev_span(i, s):
    return f'<span id="ev-n5-p{i}" class="evidence-target">{s}</span>'


def build_table_html(tbl, evs):
    cell = 'p-1.5 border'
    h = [
        '<div class="border-2 border-slate-300 rounded-xl p-4 bg-white text-xs leading-relaxed">',
        '<h4 class="text-center font-bold text-sm text-[#1995AD] border-b pb-2 mb-3">' + RR(tbl['heading']) + '</h4>',
        '<table class="w-full text-left border-collapse border border-slate-200 mb-3">',
        '  <tr class="bg-slate-100 font-bold">' + ''.join(f'<th class="{cell}">{RR(th)}</th>' for th in tbl['headers']) + '</tr>',
    ]
    for row in tbl['rows']:
        tds = [f'<td class="{cell} font-bold">{RR(row[0])}</td>'] + [f'<td class="{cell}">{RR(c)}</td>' for c in row[1:]]
        h.append('  <tr>' + ''.join(tds) + '</tr>')
    h.append('</table>')
    h.append(f'<p class="text-slate-600">{RR(tbl.get("foot_prefix", "※ "))}{evs}</p>')
    h.append('</div>')
    return '\n'.join(h)


def build():
    specs = PASSAGES_SHORT + PASSAGES_MID_INFO
    assert len(specs) == 30, f'expected 30 passages, got {len(specs)}'
    groups = [s['section_name'] for s in specs]
    targets = balanced_targets_by_group(groups, seed=20261105)
    rng = random.Random(20261105)

    passages = []
    for idx, (spec, target) in enumerate(zip(specs, targets), 1):
        pid = f'n5_p{idx}'
        assert spec['id'] == pid, f'id mismatch {spec["id"]} != {pid}'
        ev_id = f'ev-n5-p{idx}'
        evs = ev_span(idx, RR(spec['ev']))

        if 'table' in spec:
            text_html = build_table_html(spec['table'], evs)
        else:
            parts = []
            for t in spec['text']:
                segs = t.split('@EV@')
                out = []
                for k, sg in enumerate(segs):
                    out.append(RR(sg))
                    if k < len(segs) - 1:
                        out.append(evs)
                parts.append(''.join(out))
            text_html = '\n'.join(parts)

        plain_choices, ans_idx = place_choices(spec['correct'], spec['wrong'], target, rng)
        choices_html = [RR(c) for c in plain_choices]

        exp_out = {}
        for lang, txt in spec['exp'].items():
            rep = txt.replace('{N}', str(ans_idx + 1))
            exp_out[lang] = RR(rep) if lang == 'ja' else rep

        q = dict(
            q_num=idx,
            question_html=RR(spec['question']),
            evidence_id=ev_id,
            choices=choices_html,
            answer=ans_idx,
            explanation=exp_out,
        )
        p = dict(
            id=pid,
            type=spec['type'],
            section_name=spec['section_name'],
            genre=spec['genre'],
            title=P(spec['title']),
            title_ruby=RR(spec['title']),
            time_est=spec['time_est'],
            text_html=text_html,
            vocab_notes=[dict(word=w, meaning=m) for w, m in spec['vocab']],
            questions=[q],
        )
        passages.append(p)

    data = dict(
        test_id='jlpt_n5_reading_test_01',
        title='JLPT N5 読解実戦模試 第1回',
        level='N5',
        total_passages=len(passages),
        total_questions=len(passages),
        passages=passages,
    )

    # Self-check
    errs = []
    ans_all = []
    for p in passages:
        q = p['questions'][0]
        fields = {'title_ruby': p['title_ruby'], 'text_html': p['text_html'], 'question': q['question_html'], 'exp.ja': q['explanation']['ja']}
        for i, c in enumerate(q['choices']):
            fields[f'choice{i+1}'] = c
        for k, v in fields.items():
            L = lint_ruby(v)
            if L:
                errs.append(f'{p["id"]} {k} unruby kanji: {L}')
            if '{' in v or '}' in v:
                errs.append(f'{p["id"]} {k} leftover marker in: {v}')
            sh = sensitive_hits(v)
            if sh:
                errs.append(f'{p["id"]} {k} sensitive: {sh}')
        if q['evidence_id'] not in p['text_html']:
            errs.append(f'{p["id"]} evidence_id missing from text_html')
        if len(set(q['choices'])) != 4:
            errs.append(f'{p["id"]} duplicate choices')
        ans_all.append(q['answer'])

    for i in range(2, len(ans_all)):
        if ans_all[i] == ans_all[i - 1] == ans_all[i - 2]:
            errs.append(f'3-in-a-row answer at q{i+1}')

    for sec in ('問題4 短文読解', '問題5 中文読解', '問題6 情報検索'):
        sub = [p['questions'][0]['answer'] for p in passages if p['section_name'] == sec]
        print(f'{sec}: {len(sub)} passages, dist {sorted(collections.Counter(sub).items())}')
    print('overall dist:', sorted(collections.Counter(ans_all).items()))

    if errs:
        for e in errs:
            print('ERR:', e)
        sys.exit(1)

    header = f'// JLPT N5 読解実戦模試（全{len(passages)}題 完全網羅データ）\n'
    out_str = header + 'window.JLPT_N5_READING_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n'
    out_path = os.path.join(REPO, 'database', 'jlpt_n5_reading_data.js')
    with open(out_path, 'w', encoding='utf-8', newline='') as f:
        f.write(out_str.replace('\n', '\r\n'))
    pub_path = os.path.join(REPO, 'public', 'database', 'jlpt_n5_reading_data.js')
    if os.path.exists(os.path.dirname(pub_path)):
        with open(pub_path, 'w', encoding='utf-8', newline='') as f:
            f.write(out_str.replace('\n', '\r\n'))
    print(f'Successfully wrote {len(passages)} passages to {out_path}')


if __name__ == '__main__':
    build()
