# -*- coding: utf-8 -*-
"""
JLPT N1 Listening Comprehension Builder & Multi-Speaker Neural2 Synthesizer (35 Questions)
- 100% <ruby> coverage on prompt_ruby, choices_ruby, explanation.ja, script_html
- Zero 'あ、', zero role labels spoken aloud, zero sensitive/brand words
- Multi-speaker Neural2 synthesis (ja-JP-Neural2-B for female/narrator, ja-JP-Neural2-C for male)
- All 35 questions linked to 4:3 illustrations in images/listening_n1/n1_q{1..35}.jpg
"""
import os, sys, re, json, shutil, random, collections

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, 'n3_rewrite'))
from n3_lib import R, P, lint_ruby, sensitive_hits, place_choices, balanced_targets, num_reading

def strip_ruby_keep_tags(html):
    return re.sub(r'<ruby>([^<]+)<rt>[^<]*</rt></ruby>', r'\1', html)

def RR(t):
    def rep_out(src, old, new):
        return re.sub(r'(?<![{|])' + re.escape(old), new, src)
    t = rep_out(t, 'この後', 'この{後|あと}')
    t = rep_out(t, 'このあと', 'このあと')
    t = rep_out(t, 'その後', 'その{後|あと}')
    t = rep_out(t, '何を', '{何|なに}を')
    t = rep_out(t, '何について', '{何|なに}について')
    t = rep_out(t, '何なりと', '{何|なん}なりと')
    t = rep_out(t, '何ですか', '{何|なん}ですか')
    t = rep_out(t, '行いますか', '{行|おこな}いますか')
    t = rep_out(t, '1ヶ月', '1ヶ{月|げつ}')
    t = rep_out(t, '3ヶ月', '3ヶ{月|げつ}')
    t = rep_out(t, '0時', '0{時|じ}')
    t = rep_out(t, '2名', '2{名|めい}')
    t = rep_out(t, '3倍', '3{倍|ばい}')
    t = rep_out(t, '15分圏内', '15{分圏内|ふんけんない}')
    t = rep_out(t, '15分以内', '15{分以内|ふんいない}')
    t = rep_out(t, '15分都市', '15{分都市|ふんとし}')
    t = rep_out(t, '20世紀型', '20{世紀型|せいきがた}')
    t = rep_out(t, '第一線', '{第一線|だいいっせん}')
    t = rep_out(t, '第一志望', '{第一志望|だいいちしぼう}')
    t = rep_out(t, '第三者機関', '{第三者機関|だいさんしゃきかん}')
    t = rep_out(t, '一通り', '{一通|ひととお}り')
    t = rep_out(t, '一人ひとり', '{一人|ひとり}ひとり')
    t = rep_out(t, '一歩前進', '{一歩前進|いっぽぜんしん}')
    t = rep_out(t, '一存', '{一存|いちぞん}')
    t = rep_out(t, '一夜漬け', '{一夜漬|いちやづ}け')
    t = rep_out(t, '万一の際', '{万一|まんいち}の{際|さい}')
    t = rep_out(t, '今夜中', '{今夜中|こんやじゅう}')
    t = rep_out(t, '刊行予定日', '{刊行予定日|かんこうよていび}')
    t = rep_out(t, '試験日程', '{試験日程|しけんにってい}')
    t = rep_out(t, '帰国日程', '{帰国日程|きこくにってい}')
    t = rep_out(t, '今日的', '{今日的|こんにちてき}')
    t = rep_out(t, '日中', '{日中|にっちゅう}')
    t = rep_out(t, '平日', '{平日|へいじつ}')
    t = rep_out(t, '本日', '{本日|ほんじつ}')
    t = rep_out(t, '明後日', '{明後日|あさって}')
    t = rep_out(t, '申出', '{申出|もうしで}')
    t = rep_out(t, '申し分', '{申|もう}し{分|ぶん}')
    t = rep_out(t, '申し上げ', '{申|もう}し{上|あ}げ')
    t = rep_out(t, 'お詫び', 'お{詫|わ}び')
    t = rep_out(t, 'お慶び', 'お{慶|よろこ}び')
    t = rep_out(t, 'お持ち帰り', 'お{持|も}ち{帰|かえ}り')
    t = rep_out(t, 'お体', 'お{体|からだ}')
    t = rep_out(t, 'ご自愛', 'ご{自愛|じあい}')
    t = rep_out(t, 'ご意向', 'ご{意向|いこう}')
    t = rep_out(t, 'ご苦労', 'ご{苦労|くろう}')
    t = rep_out(t, 'ご指摘', 'ご{指摘|してき}')
    t = rep_out(t, 'ご検討', 'ご{検討|けんとう}')
    t = rep_out(t, 'ご専門', 'ご{専門|せんもん}')
    t = rep_out(t, 'ご説明', 'ご{説明|せつめい}')
    t = rep_out(t, '手配', '{手配|てはい}')
    t = rep_out(t, '手法', '{手法|しゅほう}')
    t = rep_out(t, '手段', '{手段|しゅだん}')
    t = rep_out(t, '手応え', '{手応|てごた}え')
    t = rep_out(t, '手触り感', '{手触|てざわ}り{感|かん}')
    t = rep_out(t, '手短に', '{手短|てみじか}に')
    t = rep_out(t, '不手際', '{不手際|ふてぎわ}')
    t = rep_out(t, '手直し', '{手直|てなお}し')
    t = rep_out(t, '決め手', '{決|き}め{手|て}')
    t = rep_out(t, '洗い直して', '{洗|あら}い{直|なお}して')
    t = rep_out(t, '見直して', '{見直|みなお}して')
    t = rep_out(t, '見直し', '{見直|みなお}し')
    t = rep_out(t, '直ちに', '{直|ただ}ちに')
    t = rep_out(t, '直接', '{直接|ちょくせつ}')
    t = rep_out(t, '直感', '{直感|ちょっかん}')
    t = rep_out(t, '直売所', '{直売所|ちょくばいじょ}')
    t = rep_out(t, 'した方が', 'した{方|ほう}が')
    t = rep_out(t, '私の方から', '{私|わたし}の{方|ほう}から')
    t = rep_out(t, '社員の方々', '{社員|しゃいん}の{方々|かたがた}')
    t = rep_out(t, '先方', '{先方|せんぽう}')
    t = rep_out(t, '方針', '{方針|ほうしん}')
    t = rep_out(t, '生じる', '{生|しょう}じる')
    t = rep_out(t, '生まれ', '{生|う}まれ')
    t = rep_out(t, '生み出す', '{生|う}み{出|だ}す')
    t = rep_out(t, '生む', '{生|う}む')
    t = rep_out(t, '生きる', '{生|い}きる')
    t = rep_out(t, '生き残り', '{生|い}き{残|のこ}り')
    t = rep_out(t, '再生', '{再生|さいせい}')
    t = rep_out(t, '生態系', '{生態系|せいたいけい}')
    t = rep_out(t, '生態学者', '{生態学者|せいたいがくしゃ}')
    t = rep_out(t, '生物学者', '{生物学者|せいぶつがくしゃ}')
    t = rep_out(t, '生命', '{生命|せいめい}')
    t = rep_out(t, '共生', '{共生|きょうせい}')
    t = rep_out(t, '生涯学習', '{生涯学習|しょうがいがくしゅう}')
    t = rep_out(t, '公開', '{公開|こうかい}')
    t = rep_out(t, '開発', '{開発|かいはつ}')
    t = rep_out(t, '空調', '{空調|くうちょう}')
    t = rep_out(t, '空間', '{空間|くうかん}')
    t = rep_out(t, '空腹', '{空腹|くうふく}')
    t = rep_out(t, '空洞化', '{空洞化|くうどうか}')
    t = rep_out(t, '十分な', '{十分|じゅうぶん}な')
    t = rep_out(t, '数箇所', '{数箇所|すうかしょ}')
    t = rep_out(t, '平身低頭', '{平身低頭|へいしんていとう}')
    t = rep_out(t, '新進気鋭', '{新進気鋭|しんしんきえい}')
    t = rep_out(t, '前例踏襲', '{前例踏襲|ぜんれいとうしゅう}')
    t = rep_out(t, '踏襲', '{踏襲|とうしゅう}')
    t = rep_out(t, '老舗旅館', '{老舗旅館|しにせりょかん}')
    t = rep_out(t, '違わぬ', '{違|たが}わぬ')
    t = rep_out(t, '頓挫', '{頓挫|とんざ}')
    t = rep_out(t, '抗えなかった', '{抗|あらが}えなかった')
    t = rep_out(t, '払拭', '{払拭|ふっしょく}')
    t = rep_out(t, '座視', '{座視|ざし}')
    t = rep_out(t, '感無量', '{感無量|かんむりょう}')
    t = rep_out(t, '熾烈', '{熾烈|しれつ}')
    t = rep_out(t, '唯一無二', '{唯一無二|ゆいいつむに}')
    t = rep_out(t, '薄利多売', '{薄利多売|はくりたばい}')
    t = rep_out(t, '夏目漱石', '{夏目漱石|なつめそうせき}')
    t = rep_out(t, '百余年前', '{百余年前|ひゃくよねんまえ}')
    t = rep_out(t, '海馬', '{海馬|かいば}')
    t = rep_out(t, '大脳皮質', '{大脳皮質|だいのうひしつ}')
    t = rep_out(t, '選択肢1', '{選択肢|せんたくし}1')
    t = rep_out(t, '選択肢2', '{選択肢|せんたくし}2')
    t = rep_out(t, '選択肢3', '{選択肢|せんたくし}3')
    t = rep_out(t, '選択肢4', '{選択肢|せんたくし}4')
    t = rep_out(t, '案1', '{案|あん}1')
    t = rep_out(t, '案2', '{案|あん}2')
    t = rep_out(t, '案3', '{案|あん}3')
    t = rep_out(t, '案4', '{案|あん}4')
    t = rep_out(t, '質問34', '{質問|しつもん}34')
    t = rep_out(t, '質問35', '{質問|しつもん}35')
    t = rep_out(t, '第1問', '{第|だい}1{問|もん}')
    for i in range(1, 36):
        t = rep_out(t, f'第{i}問', f'{{第|だい}}{i}{{問|もん}}')
    return R(t)

RISKY = [
    ('この後', 'このあと'), ('このあと', 'このあと'), ('その後', 'そのあと'), ('そのあと', 'そのあと'),
    ('1ヶ月', 'いっかげつ'), ('3ヶ月', 'さんかげつ'), ('深夜0時', 'しんやれいじ'), ('2名', 'にめい'),
    ('フェーズ2', 'フェーズツー'), ('一人ひとり', 'ひとりひとり'), ('一日', 'いちにち'),
    ('第一志望', 'だいいちしぼう'), ('第一線', 'だいいっせん'), ('第三者機関', 'だいさんしゃきかん'),
    ('一通り', 'ひととおり'), ('一歩前進', 'いっぽぜんしん'), ('一存', 'いちぞん'), ('一夜漬け', 'いちやづけ'),
    ('万一の際', 'まんいちのさい'), ('今夜中', 'こんやじゅう'), ('明後日', 'あさって'),
    ('刊行予定日', 'かんこうよていび'), ('帰国日程', 'きこくにってい'),
    ('無料Wi-Fi', 'むりょうワイファイ'), ('Wi-Fi', 'ワイファイ'), ('IT企業', 'アイティーきぎょう'), ('ITベンチャー', 'アイティーベンチャー'),
    ('GDP（国内総生産）', 'ジーディーピー、こくないそうせいさん'), ('GDP', 'ジーディーピー'),
    ('20世紀型都市', 'にじゅっせいきがたとし'), ('15分都市', 'じゅうごふんとし'), ('15分以内', 'じゅうごふんいない'),
    ('二酸化炭素', 'にさんかたんそ'), ('夏目漱石', 'なつめそうせき'), ('百余年前', 'ひゃくよねんまえ'),
    ('今日的な', 'こんにちてきな'), ('日中', 'にっちゅう'), ('海馬', 'かいば'), ('大脳皮質', 'だいのうひしつ'),
    ('十分な睡眠', 'じゅうぶんなすいみん'), ('前例踏襲', 'ぜんれいとうしゅう'), ('踏襲', 'とうしゅう'),
    ('老舗旅館', 'しにせりょかん'), ('評判に違わぬ', 'ひょうばんにたがわぬ'), ('頓挫', 'とんざ'),
    ('抗えなかった', 'あらがえなかった'), ('痛み入ります', 'いたみいります'), ('払拭', 'ふっしょく'),
    ('新進気鋭', 'しんしんきえい'), ('発想には目を見張る', 'はっそうには、めをみはる'), ('目を見張る', 'めをみはる'), ('平身低頭', 'へいしんていとう'),
    ('お詫び', 'おわび'), ('数箇所', 'すうかしょ'), ('座視', 'ざし'), ('感無量', 'かんむりょう'),
    ('案1は', 'あんいちは'), ('案2は', 'あんには'), ('案3は', 'あんさんは'), ('案4は', 'あんよんは'),
    ('本町において', 'ほんちょうにおいて'), ('生じる', 'しょうじる'), ('生み出す', 'うみだす'),
    ('質問34', 'しつもんさんじゅうよん'), ('質問35', 'しつもんさんじゅうご'),
    ('何を', 'なにを'), ('何について', 'なにについて'), ('何ですか', 'なんですか'),
    ('した方が', 'したほうが'), ('私の方から', 'わたしのほうから'), ('社員の方々', 'しゃいんのかたがた'),
]

def tts_clean(text):
    t = P(strip_ruby_keep_tags(text))
    for a, b in RISKY:
        t = t.replace(a, b)
    return t.replace('。。', '。').strip()

def update_choice_num_in_exp(exp, new_num):
    exp = dict(exp)
    exp['ja'] = re.sub(r'選択肢[1-4]', f'選択肢{new_num}', exp['ja'])
    exp['en'] = re.sub(r'Choice [1-4]', f'Choice {new_num}', exp['en'])
    exp['zh'] = re.sub(r'選項[1-4]', f'選項{new_num}', exp['zh'])
    exp['ko'] = re.sub(r'[1-4]번', f'{new_num}번', exp['ko'])
    return exp

def parse_script_turns(q):
    """Extract clean [(role, text)] turns from script_html without reading speaker labels."""
    qn = q['q_num']
    sec = q['section_id']
    raw = strip_ruby_keep_tags(q['script_html'])
    raw = (raw
        .replace('差別化', '独自化')
        .replace('あ、そうでしたか。', 'なるほど、そうでしたか。')
        .replace('SNSで', 'インターネット上で')
    )
    paras = re.findall(r'<p[^>]*>(.*?)</p>', raw, flags=re.S)
    turns = []
    for p in paras:
        p_txt = p.strip()
        if p_txt.startswith('【場面】'):
            continue
        m_spk = re.match(r'^<span[^>]*>([^<]+)：</span>\s*(.*)$', p_txt, flags=re.S)
        if m_spk:
            spk, line = m_spk.group(1).strip(), P(m_spk.group(2)).strip()
            role = 'f' if ('女' in spk) else ('m' if ('男' in spk or '教授' in spk) else 'f')
            if qn == 2 and '学生' in spk:
                role = 'f'
            # Check if trailing narrator question is attached at end of last speaker line
            for q_end in (
                '男の人はこのあと、まず何を修正しますか。',
                '大学院生はこのあと、何をしなければなりませんか。',
                '女の人はこのあと、まず何をしますか。',
                '男の人はこのあと、どのデータを再検証しますか。',
                '担当者はこのあと、まず何をしますか。',
                '技術者はこのあと、まず何を行いますか。',
                '学生が第一志望の業界を変更した決定的な理由は何ですか。',
                '新製品の発売を延期した最大の理由は何ですか。',
                '今年度の施策で最も注力すべき点は何ですか。',
                'コンペで採用された案が高く評価された要因は何ですか。',
                '共感疲労のメカニズムとして正しいものはどれですか。',
                '国内市場での減益を補うための重点戦略は何ですか。',
                '今回の特別展で従来と異なる最大の試みは何ですか。',
                '二人はどの案を支持していますか。',
                '質問34：男性委員はどの案を支持していますか。',
            ):
                if line.endswith(q_end) and len(line) > len(q_end):
                    main_line = line[:-len(q_end)].strip()
                    turns.append((role, main_line))
                    turns.append(('n', q_end))
                    line = ''
                    break
            if line:
                turns.append((role, line))
        else:
            txt = P(p_txt).strip()
            if txt in ('1、', '2、', '3、'):
                continue
            # Check if it's a monologue in sec3
            if sec == 'sec3':
                # Split intro, monologue body, and final question
                m_mono = re.match(r'^([^。]+話しています。)(.*?)([^。]+ですか。)$', txt)
                if m_mono:
                    intro, body, q_tail = m_mono.groups()
                    spk_role = 'm' if qn in (14, 16, 18) else 'f'
                    turns.append(('n', intro.strip()))
                    turns.append((spk_role, body.strip()))
                    turns.append(('n', q_tail.strip()))
                else:
                    turns.append(('n', txt))
            else:
                turns.append(('n', txt))
    return turns

def build():
    path = os.path.join(REPO, 'database', 'jlpt_n1_listening_data.js')
    s = open(path, encoding='utf-8').read()
    data = json.loads(s[s.find('{'):s.rfind('}') + 1])

    # Make Q34 and Q35 both include the 4-proposal overview + the male/female discussion
    prop_overview = (
        '自治体の検討委員会で旧小学校跡地の利活用について4つの案が提示されています。'
        '案1はITベンチャー向けのサテライトオフィス、案2は地域の農産物直売所と体験型レストラン、'
        '案3は災害時の広域避難拠点と防災備蓄倉庫、案4はシニア生涯学習と子育て世代の交流プラザです。'
        '男女の委員二人が話しています。'
    )
    q34_m = '私は少子高齢化が進む本町において、高齢者の孤立を防ぎつつ若い親たちが安心して子育てできる環境づくりこそが最も急務だと考えます。自治体の財政負担が生じるとしても、多世代の絆を取り戻す福祉的な投資を惜しむべきではありません。'
    q34_f = '福祉の充実も理解できますが、そもそも町の財政を支える税収基盤がなければ持続できません。私はIT企業の誘致によって若い世代を都市部から呼び込み、新たな産業と雇用を生み出すことこそが再生の根本治療だと確信しています。'

    rng = random.Random(20261106)
    V = {'n': 'ja-JP-Neural2-B', 'f': 'ja-JP-Neural2-B', 'm': 'ja-JP-Neural2-C'}
    errors = []

    # Group by 4-choice vs 3-choice to balance answers cleanly
    four_qs = [q for q in data['questions'] if len(q['choices']) == 4]
    three_qs = [q for q in data['questions'] if len(q['choices']) == 3]
    four_targets = balanced_targets(len(four_qs), seed=11)
    three_seq = []
    rng3 = random.Random(22)
    while len(three_seq) < len(three_qs):
        blk = [0, 1, 2]
        rng3.shuffle(blk)
        if len(three_seq) >= 2 and three_seq[-1] == three_seq[-2] == blk[0]:
            blk.append(blk.pop(0))
        three_seq.extend(blk)
    three_targets = three_seq[:len(three_qs)]
    i4, i3 = 0, 0

    for q in data['questions']:
        qn = q['q_num']
        sec = q['section_id']
        q['situation'] = (P(strip_ruby_keep_tags(q['situation']))
            .replace('差別化', '独自化')
            .replace('SNS', 'インターネット')
        )
        if qn == 34:
            q['situation'] = '閉校となった旧小学校の利活用案について委員二人が議論しています。男性委員はどの案を支持していますか。'
        elif qn == 35:
            q['situation'] = '閉校となった旧小学校の利活用案について委員二人が議論しています。女性委員はどの案を支持していますか。'

        q['prompt'] = (P(strip_ruby_keep_tags(q['prompt']))
            .replace('差別化', '独自化')
            .replace('SNS', 'インターネット')
        )
        q['prompt_ruby'] = RR(q['prompt'])
        q['has_illustration'] = True
        q['illustration_url'] = f'images/listening_n1/n1_q{qn}.jpg'
        q['image'] = f'images/listening_n1/n1_q{qn}.jpg'
        q['audio_file'] = f'audio/listening/n1_q{qn}.mp3'

        ch_plains = [
            P(strip_ruby_keep_tags(c)).replace('差別化', '独自化').replace('SNS', 'インターネット')
            for c in q['choices']
        ]
        corr_plain = ch_plains[q['answer']]
        dist_plains = [c for i, c in enumerate(ch_plains) if i != q['answer']]

        if len(ch_plains) == 4:
            tgt = four_targets[i4]; i4 += 1
            new_ch, new_ans = place_choices(corr_plain, dist_plains, tgt, rng)
        else:
            tgt = three_targets[i3]; i3 += 1
            rng.shuffle(dist_plains)
            new_ch = dist_plains[:tgt] + [corr_plain] + dist_plains[tgt:]
            new_ans = tgt

        q['choices'] = [RR(c) for c in new_ch]
        q['choices_ruby'] = q['choices']
        q['answer'] = new_ans

        exp_ja_plain = (P(strip_ruby_keep_tags(q['explanation']['ja']))
            .replace('差別化', '独自化')
            .replace('SNS時代', '情報化時代')
            .replace('SNS', 'インターネット')
        )
        q['explanation']['ja'] = exp_ja_plain
        q['explanation'] = update_choice_num_in_exp(q['explanation'], new_ans + 1)
        q['explanation']['ja'] = RR(q['explanation']['ja'])

        # Build clean turns and script_html
        head_tts = f'だい{num_reading(qn)}もん。'
        segs = []
        dlg_html = f'<p class="text-xs font-bold text-slate-500 mb-2">【{RR("場面")}】{RR(q["situation"])}</p>'

        if sec == 'sec4':
            asker = 'm' if qn % 2 == 0 else 'f'
            replier = 'f' if asker == 'm' else 'm'
            asker_lab = '男の人' if asker == 'm' else '女の人'
            segs.append((V['n'], head_tts, 600))
            segs.append((V[asker], tts_clean(q['prompt']), 1100))
            dlg_html += f'<p><span class="font-bold text-[#1995AD]">{RR(asker_lab)}：</span>{q["prompt_ruby"]}</p>'
            for idx_c, c_plain in enumerate(new_ch):
                num_w = ['いち', 'に', 'さん'][idx_c]
                segs.append((V[replier], f'{num_w}ばん。{tts_clean(c_plain)}', 1400))
                dlg_html += f'<p class="pl-3"><span class="font-bold text-[#1995AD]">{idx_c+1}{RR("番")}：</span>{RR(c_plain)}</p>'
            segs.append((V['n'], '最も適切な返答を選んでください。', 1500))
        elif qn in (34, 35):
            q_tail = '質問34。男性委員はどの案を支持していますか。' if qn == 34 else '質問35。女性委員はどの案を支持していますか。'
            segs.append((V['n'], head_tts + tts_clean(prop_overview), 900))
            segs.append((V['m'], tts_clean(q34_m), 850))
            segs.append((V['f'], tts_clean(q34_f), 900))
            segs.append((V['n'], tts_clean(q_tail), 1600))
            dlg_html += f'<p class="text-xs text-slate-700">{RR(prop_overview)}</p>'
            dlg_html += f'<p><span class="font-bold text-[#1995AD]">{RR("男")}：</span>{RR(q34_m)}</p>'
            dlg_html += f'<p><span class="font-bold text-[#1995AD]">{RR("女")}：</span>{RR(q34_f)}</p>'
            dlg_html += f'<p class="text-xs font-bold text-[#B8596E] mt-2">{RR(q_tail)}</p>'
        else:
            turns = parse_script_turns(q)
            for idx_t, (role, line) in enumerate(turns):
                prefix = head_tts if idx_t == 0 else ''
                pause = 900 if role == 'n' else 800
                if idx_t == len(turns) - 1:
                    pause = 1600
                segs.append((V[role], prefix + tts_clean(line), pause))
                if role == 'n':
                    cls = 'text-xs font-bold text-[#B8596E] mt-2' if idx_t == len(turns) - 1 else 'text-xs text-slate-700'
                    dlg_html += f'<p class="{cls}">{RR(line)}</p>'
                else:
                    lab = '女' if role == 'f' else '男'
                    dlg_html += f'<p><span class="font-bold text-[#1995AD]">{RR(lab)}：</span>{RR(line)}</p>'

        q['script_html'] = f'<div class="space-y-2 text-sm leading-relaxed">{dlg_html}</div>'
        q['speech_audio_text'] = '\n\n'.join(t for _, t, _ in segs)
        q['_segments'] = segs

        if 'あ、' in q['speech_audio_text'] or 'あ、' in P(q['script_html']):
            errors.append(f'Q{qn} still contains あ、')
        for k, h in (('prompt', q['prompt_ruby']), ('choices', ''.join(q['choices_ruby'])), ('exp', q['explanation']['ja']), ('script', q['script_html'])):
            lr = lint_ruby(h)
            if lr:
                errors.append(f'Q{qn} {k} unrubied: {lr}')
        for t_chk in [q['situation'], q['prompt'], q['speech_audio_text'], P(q['explanation']['ja'])] + new_ch:
            sh = sensitive_hits(t_chk)
            if sh:
                errors.append(f'Q{qn} sensitive {sh} in {t_chk[:60]}')

    if errors:
        print(f'{len(errors)} ERRORS:')
        for e in errors:
            print(' ', e)
        sys.exit(1)

    out_qs = [{k: v for k, v in q.items() if not k.startswith('_')} for q in data['questions']]
    data_out = dict(data)
    data_out['questions'] = out_qs
    js_str = '// JLPT N1 Listening Comprehension Data (35 Questions, Multi-Speaker Audio & 4:3 Illustrations)\n'
    js_str += 'window.JLPT_N1_LISTENING_DATA = ' + json.dumps(data_out, ensure_ascii=False, indent=2) + ';\n'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(js_str)
    shutil.copyfile(path, os.path.join(REPO, 'public', 'database', 'jlpt_n1_listening_data.js'))
    print('Wrote JLPT_N1_LISTENING_DATA:', len(out_qs), 'questions, dist =', collections.Counter(q['answer'] for q in out_qs))
    return data['questions']

def synth_all(qs):
    os.environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS', os.path.join(REPO, 'secrets/google_tts_key.json'))
    from google.cloud import texttospeech
    cl = texttospeech.TextToSpeechClient()
    only = set(int(x) for x in sys.argv[sys.argv.index('--only') + 1:]) if '--only' in sys.argv else set()

    def synth(text, voice, ssml=False):
        inp = texttospeech.SynthesisInput(ssml=text) if ssml else texttospeech.SynthesisInput(text=text)
        r = cl.synthesize_speech(
            input=inp,
            voice=texttospeech.VoiceSelectionParams(language_code='ja-JP', name=voice),
            audio_config=texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3, speaking_rate=0.96)
        )
        return r.audio_content

    total_chars = 0
    for q in qs:
        n = q['q_num']
        if only and n not in only:
            continue
        buf = bytearray()
        for voice, text, pause in q['_segments']:
            buf += synth(text, voice)
            total_chars += len(text)
            if pause:
                buf += synth(f'<speak><break time="{pause}ms"/></speak>', voice, ssml=True)
        for d in (
            os.path.join(REPO, 'audio/listening', f'n1_q{n}.mp3'),
            os.path.join(REPO, 'public/audio/listening', f'n1_q{n}.mp3'),
        ):
            os.makedirs(os.path.dirname(d), exist_ok=True)
            with open(d, 'wb') as f:
                f.write(buf)
        print(f'Synthesized n1_q{n}.mp3 ({len(buf)} bytes)')
    print(f'Total synthesized characters: {total_chars}')

if __name__ == '__main__':
    qs = build()
    if '--audio' in sys.argv:
        synth_all(qs)
