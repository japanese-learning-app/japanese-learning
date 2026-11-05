# -*- coding: utf-8 -*-
"""
JLPT N1 Reading Comprehension Builder & Validator (10 Passages, 21 Questions)
- Applies 100% <ruby> coverage to title_ruby, text_html, question_html, choices_ruby, explanation.ja
- Removes sensitive substrings (核心 -> 本質, 強制 -> 強要, 死への恐怖 -> 有限性への畏怖, 産業革命 -> 産業の近代化)
- Balances answer distribution across 21 questions (5/5/5/6) and syncs Choice numbers in 4 languages
- Syncs to database/jlpt_n1_reading_data.js and public/database/jlpt_n1_reading_data.js
"""
import os, sys, re, json, shutil, random, collections

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, 'n3_rewrite'))
from n3_lib import R, P, lint_ruby, sensitive_hits, place_choices, balanced_targets

def strip_ruby_keep_tags(html):
    s = re.sub(r'<ruby\.([^<]+)<rt>[^<]*</rt></ruby>', r'\1', html)
    s = re.sub(r'<ruby>([^<]+)<rt>[^<]*</rt></ruby>', r'\1', s)
    return s

def RR(t):
    def rep_out(src, old, new):
        return re.sub(r'(?<![{|])' + re.escape(old), new, src)
    t = rep_out(t, '他案', '{他案|たあん}')
    t = rep_out(t, '白黒', '{白黒|しろくろ}')
    t = rep_out(t, '直ちに', '{直|ただ}ちに')
    t = rep_out(t, '生まない', '{生|う}まない')
    t = rep_out(t, '生む', '{生|う}む')
    t = rep_out(t, '生み出された', '{生|う}み{出|だ}された')
    t = rep_out(t, '生まれる', '{生|う}まれる')
    t = rep_out(t, '生まれつき', '{生|う}まれつき')
    t = rep_out(t, '生き方', '{生|い}き{方|かた}')
    t = rep_out(t, '生きている', '{生|い}きている')
    t = rep_out(t, '生きる', '{生|い}きる')
    t = rep_out(t, '生き直す', '{生|い}き{直|なお}す')
    t = rep_out(t, '自らの生を', '{自|みずか}らの{生|せい}を')
    t = rep_out(t, '生の切実さ', '{生|せい}の{切実|せつじつ}さ')
    t = rep_out(t, '生じれば', '{生|しょう}じれば')
    t = rep_out(t, '日々の', '{日々|ひび}の')
    t = rep_out(t, '日用雑器', '{日用雑器|にちようざっき}')
    t = rep_out(t, '今日', '{今日|こんにち}')
    t = rep_out(t, '第六感', '{第六感|だいろっかん}')
    t = rep_out(t, '20世紀', '20{世紀|せいき}')
    t = rep_out(t, '24時間', '24{時間|じかん}')
    t = rep_out(t, '空を眺め', '{空|そら}を{眺|なが}め')
    t = rep_out(t, '空白', '{空白|くうはく}')
    t = rep_out(t, '扉が開かれて', '{扉|とびら}が{開|ひら}かれて')
    t = rep_out(t, '開催される', '{開催|かいさい}される')
    t = rep_out(t, '開示', '{開示|かいじ}')
    t = rep_out(t, '開発', '{開発|かいはつ}')
    t = rep_out(t, '1件につき', '1{件|けん}につき')
    t = rep_out(t, '30万円', '30{万円|まんえん}')
    t = rep_out(t, '60万円', '60{万円|まんえん}')
    t = rep_out(t, '5年以内', '5{年以内|ねんいない}')
    t = rep_out(t, '7年以内', '7{年以内|ねんいない}')
    t = rep_out(t, '40歳未満', '40{歳未満|さいみまん}')
    t = rep_out(t, '2週間以上', '2{週間以上|しゅうかんいじょう}')
    t = rep_out(t, '2025年度', '2025{年度|ねんど}')
    t = rep_out(t, '2025年', '2025{年|ねん}')
    t = rep_out(t, '2026年', '2026{年|ねん}')
    t = rep_out(t, '5月1日(木)', '5{月|がつ}{1日|ついたち}({木|もく})')
    t = rep_out(t, '5月31日(土)', '5{月|がつ}31{日|にち}({土|ど})')
    t = rep_out(t, '8月1日', '8{月|がつ}{1日|ついたち}')
    t = rep_out(t, '3月31日', '3{月|がつ}31{日|にち}')
    t = rep_out(t, '30日以内', '30{日以内|にちいない}')
    t = rep_out(t, '1週間以内', '1{週間以内|しゅうかんいない}')
    t = rep_out(t, '6ヶ月以内', '6ヶ{月以内|げついない}')
    t = rep_out(t, '出発日', '{出発日|しゅっぱつび}')
    t = rep_out(t, '5月に出発', '5{月|がつ}に{出発|しゅっぱつ}')
    t = rep_out(t, '4月以降', '4{月以降|がついこう}')
    t = rep_out(t, '第2段落', '{第|だい}2{段落|だんらく}')
    t = rep_out(t, '第3段落', '{第|だい}3{段落|だんらく}')
    t = rep_out(t, '第4段落', '{第|だい}4{段落|だんらく}')
    t = rep_out(t, '第2・第3段落', '{第|だい}2・{第|だい}3{段落|だんらく}')
    t = rep_out(t, '第2項', '{第|だい}2{項|こう}')
    t = rep_out(t, '第3項', '{第|だい}3{項|こう}')
    t = rep_out(t, '選択肢1', '{選択肢|せんたくし}1')
    t = rep_out(t, '選択肢2', '{選択肢|せんたくし}2')
    t = rep_out(t, '選択肢3', '{選択肢|せんたくし}3')
    t = rep_out(t, '選択肢4', '{選択肢|せんたくし}4')
    t = rep_out(t, '柳宗悦', '{柳宗悦|やなぎむねよし}')
    t = rep_out(t, '民藝', '{民藝|みんげい}')
    t = rep_out(t, '佇まい', '{佇|たたず}まい')
    t = rep_out(t, '風合い', '{風合|ふうあ}い')
    t = rep_out(t, '危うさ', '{危|あや}うさ')
    t = rep_out(t, '推し量り', '{推|お}し{量|はか}り')
    t = rep_out(t, '物差し', '{物差|ものさ}し')
    t = rep_out(t, '見做せ', '{見做|みな}せ')
    t = rep_out(t, '胚胎', '{胚胎|はいたい}')
    t = rep_out(t, '俎上', '{俎上|そじょう}')
    t = rep_out(t, '孕んで', '{孕|はら}んで')
    t = rep_out(t, '孕む', '{孕|はら}む')
    t = rep_out(t, '涵養', '{涵養|かんよう}')
    t = rep_out(t, '棄却', '{棄却|ききゃく}')
    t = rep_out(t, '豊饒', '{豊饒|ほうじょう}')
    t = rep_out(t, '交歓', '{交歓|こうかん}')
    return R(t)

def update_choice_num_in_exp(exp, new_num):
    exp = dict(exp)
    exp['ja'] = re.sub(r'選択肢[1-4]', f'選択肢{new_num}', exp['ja'])
    exp['en'] = re.sub(r'Choice [1-4]', f'Choice {new_num}', exp['en'])
    exp['zh'] = re.sub(r'選項[1-4]', f'選項{new_num}', exp['zh'])
    exp['ko'] = re.sub(r'[1-4]번이 정답', f'{new_num}번이 정답', exp['ko'])
    return exp

def main():
    path = os.path.join(REPO, 'database', 'jlpt_n1_reading_data.js')
    s = open(path, encoding='utf-8').read()
    data = json.loads(s[s.find('{'):s.rfind('}') + 1])

    all_qs = []
    for p in data['passages']:
        for q in p['questions']:
            all_qs.append(q)
    targets = balanced_targets(len(all_qs), seed=20261106)
    rng = random.Random(101)
    q_idx = 0
    errors = []

    for p in data['passages']:
        pid = p['id']
        p['title'] = P(strip_ruby_keep_tags(p['title'])).replace('産業革命', '産業の近代化')
        p['title_ruby'] = RR(p['title'])

        raw_html = strip_ruby_keep_tags(p['text_html'])
        raw_html = (raw_html
            .replace('死への恐怖', '有限性への畏怖')
            .replace('産業革命以降', '産業の近代化以降')
            .replace('産業革命', '産業の近代化')
        )
        # Apply RR to text segments outside HTML tags
        segs = re.split(r'(<[^>]+>)', raw_html)
        rubied_segs = []
        for seg in segs:
            if seg.startswith('<'):
                rubied_segs.append(seg)
            else:
                try:
                    rubied_segs.append(RR(seg))
                except Exception as e:
                    errors.append(f'{pid} text_html: {e}')
                    rubied_segs.append(seg)
        p['text_html'] = ''.join(rubied_segs)

        lr = lint_ruby(p['text_html'])
        if lr:
            errors.append(f'{pid} text_html unrubied: {lr}')
        sh = sensitive_hits(p['text_html']) + sensitive_hits(p['title'])
        if sh:
            errors.append(f'{pid} sensitive: {sh}')

        for q in p['questions']:
            tgt = targets[q_idx]; q_idx += 1
            qn = q['q_num']
            q_plain = P(strip_ruby_keep_tags(q['question_html'])).replace('核心的', '本質的')
            q['question_html'] = RR(q_plain)

            ch_plains = [
                P(strip_ruby_keep_tags(c))
                .replace('強制する', '強要する')
                .replace('産業革命期', '近代工業化の初期')
                for c in q['choices']
            ]
            corr_plain = ch_plains[q['answer']]
            dist_plains = [c for i, c in enumerate(ch_plains) if i != q['answer']]
            new_choices, new_ans = place_choices(corr_plain, dist_plains, tgt, rng)
            q['choices'] = new_choices
            q['choices_ruby'] = [RR(c) for c in new_choices]
            q['answer'] = new_ans

            exp_ja_plain = (P(strip_ruby_keep_tags(q['explanation']['ja']))
                .replace('死への恐怖', '有限性への畏怖')
                .replace('産業革命', '産業の近代化')
            )
            q['explanation']['ja'] = exp_ja_plain
            q['explanation'] = update_choice_num_in_exp(q['explanation'], new_ans + 1)
            q['explanation']['ja'] = RR(q['explanation']['ja'])

            for h in [q['question_html'], q['explanation']['ja']] + q['choices_ruby']:
                l = lint_ruby(h)
                if l:
                    errors.append(f'Q{qn} unrubied: {l} in {h}')
            for t_chk in [q_plain, P(q['explanation']['ja'])] + new_choices:
                sh_q = sensitive_hits(t_chk)
                if sh_q:
                    errors.append(f'Q{qn} sensitive {sh_q} in {t_chk}')

    if errors:
        print(f'{len(errors)} ERRORS:')
        for e in errors:
            print(' ', e)
        sys.exit(1)

    ans_dist = collections.Counter(q['answer'] for p in data['passages'] for q in p['questions'])
    out_js = '// JLPT N1 読解実戦模試（全10文章・全21問 完全網羅データ）\nwindow.JLPT_N1_READING_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(out_js)
    pub_path = os.path.join(REPO, 'public', 'database', 'jlpt_n1_reading_data.js')
    shutil.copyfile(path, pub_path)
    print('Wrote JLPT_N1_READING_DATA:', len(data['passages']), 'passages,', sum(len(p['questions']) for p in data['passages']), 'questions, dist =', ans_dist)

if __name__ == '__main__':
    main()
