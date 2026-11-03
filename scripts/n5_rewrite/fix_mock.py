# -*- coding: utf-8 -*-
"""
Audit + repair of database/jlpt_n5_mock_data.js  (JLPT N5 mock exam #1, 91 questions).

What this script does (idempotent: it always starts from the CURRENT js file):
  1. Applies hand-written content fixes (EDITS) for questions whose Japanese was unnatural, ambiguous
     (more than one answer possible) or broken (e.g. 文の組み立て rebuilt with the ★ in 4 different positions).
  2. Re-generates every learner-visible ruby field with n5_lib.R():
       titleRuby / passageRuby / scriptRuby / NEW optionsRuby
     - 漢字読み: the underlined target gets <u> and NO ruby (previously it had ruby = spoiler and no underline)
     - one <u> per stem, no nested / double underline
  3. Removes option numbers from explanations ("2「ノート」" -> "「ノート」") so options can be re-ordered safely,
     then re-balances the correct-answer position of all text-only 4-choice questions (ids 1-80).
     Questions 81-91 read their options aloud in the MP3 ("一番…二番…"), so they are NOT re-ordered.
  4. Section instructions (desc) are converted to hiragana so no unruby'd kanji is shown in the exam area.
Output: database/jlpt_n5_mock_data.js  (+ identical copy in public/database/)
"""
import os, re, sys, json, random, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from n5_lib import R, P, lint_ruby, KANJI, sensitive_hits

REPO = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(REPO, 'database/jlpt_n5_mock_data.js')
PUB = os.path.join(REPO, 'public/database/jlpt_n5_mock_data.js')

txt = open(SRC, encoding='utf-8').read()
m0 = re.match(r'window\.JLPT_N5_MOCK_DATA\s*=\s*', txt)
DATA, end = json.JSONDecoder().raw_decode(txt, m0.end())
TAIL = txt[end:]
Q = {q['id']: q for q in DATA['questions']}

# ---------------------------------------------------------------- hand-written edits
# title: plain source text ({漢字|よみ} allowed, <u>…</u> marks the underlined target); options: ORIGINAL order + correctIndex
EDITS = {
    2: dict(options=['まいあさ', 'まいばん', 'まいにち', 'まいとし'], correctIndex=0,
            explanation='「毎朝」の読み方は「まいあさ」です。\n「毎晩」は「まいばん」、「毎日」は「まいにち」、「毎年」は「まいとし」と読みます。'),
    12: dict(target='大きい', options=['おおきい', 'おうきい', 'だいきい', 'おおぎい'], correctIndex=0,
             explanation='「大きい」は「おおきい」と読みます。「大」を「おお」と読むことに注意しましょう。（「だい」は「大学（だいがく）」のように、熟語（じゅくご）の中で使います。）'),
    16: dict(title='あしたの <u>あさ</u>、６時に おきます。'),
    20: dict(title='げんきな <u>おとこのこ</u>が 走っています。'),
    21: dict(title='ごはんを 食べたあと、おさらと スプーンを 水で（　）。',
             explanation='水で食器をきれいにする動作なので、「あらいました（洗いました）」が正解です。\n「みせました」「こまりました」「あけました」は、「水で」という手段と合いません。'),
    29: dict(explanation='「タクシーを」に続けて使えるのは「よびました（呼びました）」です。\n「ならびました」「とまりました」「わたりました」は「タクシーを」とは続きません。'),
    33: dict(title='駅に ついたら、バスが <u>すぐに</u> 来ました。',
             options=['駅に ついて、長い 時間 待って バスに のりました。', '駅に ついたとき、バスは もう 行って いました。',
                      '駅に ついて、あまり 待たないで バスに のりました。', '駅に ついても、バスは 来ませんでした。'], correctIndex=2,
             explanation='「すぐに 来ました」は、待つ時間がほとんどなかったという意味です。「あまり 待たないで バスに のりました」とほぼ同じ意味になります。'),
    40: dict(options=['と', 'を', 'が', 'で'], correctIndex=0,
             explanation='名詞を並べるときは「と」を使います（パンと たまご）。「パンを たまごを」のように「を」を2回続けることはできません。'),
    41: dict(options=['見に', '見る', '見た', '見ました'], correctIndex=0,
             explanation='目的を表すときは「動詞のます形（語幹）＋に 行きます」を使います（見ます → 見に 行きました）。'),
    42: dict(title='プールの まわりでは、走っては（　）。', options=['いけません', 'いいです', 'ください', 'ありません'], correctIndex=0,
             explanation='「〜ては いけません」は禁止を表します（走っては いけません）。\n許可を表すのは「〜ても いいです」で、「〜ては いいです」とは言いません。'),
    44: dict(title='ペンを わすれました。となりの 人の ペンを つかいたいです。ききます。「すみません、その ペンを（　）。」',
             options=['つかいます', 'つかって ください', 'つかっても いいですか', 'つかっては いけません'], correctIndex=2,
             explanation='相手に許可を求めるときは「〜ても いいですか」を使います。\n「つかって ください」は相手にお願いする言い方、「つかっては いけません」は禁止する言い方です。'),
    45: dict(title='来年、日本へ（　）です。'),
    46: dict(title='わたしは 一度、日本で すしを（　）ことが あります。',
             explanation='過去の経験を表すときは「動詞のた形＋ことが あります」を使います（食べた ことが あります）。「一度（いちど）」は「食べる」「食べない」とは合いません。'),
    47: dict(options=['ながら', 'まえに', 'あとで', 'より'], correctIndex=1,
             explanation='「動詞の辞書形＋まえに」で「〜する前に」を表します（寝る まえに）。'),
    50: dict(options=['まで', 'より', 'から', 'でも'], correctIndex=2,
             explanation='理由・原因を表すときは「から」を使います（忙しかったから）。「まで」「より」「でも」は、この文の意味と合いません。'),
    51: dict(title='くだものやで、お客さんが 言います。「すみません、りんごを みっつ（　）。」',
             explanation='お店で買いたい物を言うときは「〜を（数）ください」と言います。\n「どうぞ」は、店の人が物を差し出すときの言葉です。'),
    57: dict(options=['行きます', '行きましょう', '行きません', '行きたかったです'], correctIndex=0,
             explanation='「まいにち」の習慣を表す文なので、現在形の「行きます」が正解です。「行きましょう」は人を誘うときの形で、「行きません」は意味が合いません。'),
    58: dict(options=['あまり', 'ぜんぜん', '少し', 'たくさん'], correctIndex=2,
             explanation='「少し むずかしいですが、とても おもしろいです」で、少し大変だがおもしろい、という意味になります。\n「あまり」「ぜんぜん」は「〜ない」の文で使います。「たくさん」は「むずかしい」に続きません。'),
    59: dict(options=['親切です', '親切でした', '親切ではありません', '親切でしたか'], correctIndex=0,
             explanation='次の文に「いろいろ 教えて くれます」とあるので、今の様子をよい意味で言う「親切です」が正解です。'),
    60: dict(options=['食べたり しました', '食べました', '食べて います', '食べる ことです'], correctIndex=0,
             explanation='前に「おみやげを 買ったり」とあるので、「〜たり 〜たり します」の形になります。「食べたり しました」が正解です。'),
    61: dict(options=['行きたいです', '行きました', '行きません', '行く ことです'], correctIndex=0,
             explanation='文のはじめに「これから（今から先）」があるので、将来の希望を表す「行きたいです」が正解です。'),
    82: dict(title='友だちの 家で 夕ごはんを ごちそうに なりました。帰るとき、何と 言いますか。'),
}

PASSAGE_KIM = '''（キムさんの 作文）
私の 日本の 生活

私は 先月、韓国から 日本へ 来ました。いま 東京の アパートに 住んで います。
大学の 近くに 住んで いますから、まいにち 歩いて 大学へ [57] 。
大学の 授業は [58] むずかしいですが、とても おもしろいです。
先生や クラスメイトは みんな とても [59] 。いろいろ 教えて くれます。
先週の 日曜日に、友だちと いっしょに 浅草へ 行きました。
浅草で おみやげを 買ったり、おいしい うどんを [60] 。
これから もっと いろいろな 所へ [61] 。'''

PASSAGES = {
    **{i: PASSAGE_KIM for i in range(57, 62)},
    62: dict(text='田中さんへ\nきのう 借りた 本を 返したいです。きょうの 午後２時に 図書館の 前で 待って います。もし 時間が ない ときは、電話を して ください。\nスミス',
             evidence='きのう 借りた 本を 返したいです。'),
    64: dict(text='お客様へ\nいつも ご利用 いただき ありがとうございます。\n来週の 火曜日（１５日）は、店の 工事の ため 休みます。\n水曜日（１６日）から いつもどおり 午前１１時に {開|あ}きます。\nどうぞ よろしく お願いします。\nさくら食堂',
             evidence='来週の 火曜日（１５日）は、店の 工事の ため 休みます。'),
}

PASSAGE_66 = '''私は 半年まえに この 町に 引っ越して きました。私の 部屋の 近くに 小さな 川が あります。川の よこには 長い 道が あって、きれいな 木や 花がたくさん あります。
私は 毎朝、大学へ 行く まえに、この 道を ３０分 さんぽします。朝は 空気が すずしくて、鳥の 声が 聞こえます。犬と いっしょに 歩いて いる 人や、走って いる 人に 会います。みんな「おはようございます」と あいさつを して くれます。
私は この 町に 来た とき、友だちが いなくて さびしかったです。でも、毎朝 この 川の 道を 歩いて、町の 人と あいさつを して、さびしく なくなりました。いま、この 町が とても 好きです。'''
PASSAGES[66] = dict(text=PASSAGE_66, evidence='でも、毎朝 この 川の 道を 歩いて、町の 人と あいさつを して、さびしく なくなりました。')
EDITS[66] = dict(options=['新しい 犬を もらったから', '大学の 友だちが 引っ越して きたから',
                          '町の 人と あいさつを して、さびしく なくなったから', '自分の 部屋が 広くて きれいだから'], correctIndex=2,
                 explanation='第3段落に「町の 人と あいさつを して、さびしく なくなりました。いま、この 町が とても 好きです」とあります。')

# 文の組み立て (rebuilt: unique word order, ★ in different slots)
# frame uses 4 blanks; chunks in correct order; star = index (0-3) of the ★ blank
ORDERING = {
    52: dict(prefix='わたしの', suffix='です。', chunks=['趣味は', '音楽を', '聞く', 'こと'], star=1),
    53: dict(prefix='ごはんを', suffix='ください。', chunks=['食べる', 'まえに', '手を', '洗って'], star=3),
    54: dict(prefix='あの', suffix='田中さんです。', chunks=['青い', 'セーターを', '着ている', '人は'], star=2),
    55: dict(prefix='毎朝', suffix='行きます。', chunks=['ごはんを', '食べて', 'から', '学校へ'], star=0),
    56: dict(prefix='ここで', suffix='いけません。', chunks=['大きい', '声で', '電話を', 'しては'], star=1),
}

# explicit annotations for ambiguous kanji in plain texts that are re-rubied automatically
FIXUPS = [
    ('（日）', '（{日|にち}）'),
    ('（日曜日）', '（日曜日）'),
    ('のんびりした 一日でした', 'のんびりした {一日|いちにち}でした'),
    ('一日中', '{一日中|いちにちじゅう}'),
]

ORDERED_IDS = {64, 68, 70, 80}      # options have a natural order (days, counts, times) -> keep order
SPOKEN_OPTION_IDS = set(range(81, 92))  # options are read aloud in the MP3 -> never re-order

DESC = {  # hiragana-only instructions (no unruby'd kanji in the exam area)
    's2_m2': '★に はいる ものは どれですか。１・２・３・４から いちばん いい ものを ひとつ えらんで ください。',
    's2_m3': '[57]から[61]に なにを いれますか。ぶんしょうの いみを かんがえて、１・２・３・４から いちばん いい ものを ひとつ えらんで ください。',
    's2_m6': 'あんないを みて、しつもんに こたえて ください。こたえは １・２・３・４から いちばん いい ものを ひとつ えらんで ください。',
    's3_m1': 'まず しつもんを きいて ください。それから はなしを きいて、１から４の なかから、いちばん いい ものを ひとつ えらんで ください。',
    's3_m2': 'まず しつもんを きいて ください。そのあと、もんだいようしを みて ください。よむ じかんが あります。それから はなしを きいて、１から４の なかから、いちばん いい ものを ひとつ えらんで ください。',
    's3_m3': 'えを みながら、しつもんを きいて ください。やじるし（➡）の ひとは なんと いいますか。１から３の なかから、いちばん いい ものを ひとつ えらんで ください。',
    's3_m4': 'えなどが ありません。ぶんを きいて、１から３の なかから、いちばん いい ものを ひとつ えらんで ください。',
}

# ---------------------------------------------------------------- helpers
def fix(s):
    for a, b in FIXUPS:
        s = s.replace(a, b)
    s = re.sub(r'(?<![{])一人(?![|])', '{一人|ひとり}', s)
    s = re.sub(r'(?<![{])二人(?![|])', '{二人|ふたり}', s)
    s = s.replace('休みになる 日は', '休みになる {日|ひ}は')
    return s

def strip_nums(expl):
    # "2「ノート」" -> "「ノート」"; "1の「かわ」" -> "「かわ」"
    e = re.sub(r'(?<![0-9０-９])[1-4１-４](?:の|は)?(?=「)', '', expl)
    e = re.sub(r'(正解は|です|ます)\s+(?=「)', r'\1', e)
    return e

def sentences(line):
    return [s for s in re.split(r'(?<=。)', line) if s != '']

def ruby_passage(text, evidence=None):
    """Sentence-wise ruby so that `evidence` (sentence-wise ruby) is an exact substring of the passage ruby."""
    lines = []
    for line in text.split('\n'):
        line = fix(line)
        line = re.sub(r'\[(\d+)\]', r'<b>[\1]</b>', line)
        lines.append(''.join(R(s) for s in sentences(line)))
    html = '<br>\n'.join(lines)
    ev = None
    if evidence:
        ev = ''.join(R(fix(s)) for s in sentences(evidence))
        assert ev in html, ('evidence not in passage', evidence)
    return html, ev

def plain_passage(text):
    return re.sub(r'\{([^{}|]+)\|[^{}|]+\}', r'\1', text)

def title_source(q):
    """plain stem with <u> for target (kanji-reading: wrap target)."""
    e = EDITS.get(q['id'], {})
    if 'title' in e:
        return e['title']
    if q['category'] == '漢字読み':
        tgt = e.get('target', q['targetWord'])
        t = q['title']
        assert tgt in t, (q['id'], tgt, t)
        return t.replace(tgt, f'<u>{tgt}</u>', 1)
    # 表記 / 言い換え: take the underline from the existing ruby html
    tr = q.get('titleRuby', '')
    s = re.sub(r'<rt>.*?</rt>', '', tr)
    s = re.sub(r'</?ruby>', '', s)
    return s

# ---------------------------------------------------------------- rebuild questions
qs = DATA['questions']
for q in qs:
    i = q['id']
    e = EDITS.get(i, {})
    # ---- options / answer (original order)
    opts = list(e.get('options', q['options']))
    ci = e.get('correctIndex', q['correctIndex'])
    if 'explanation' in e:
        expl = e['explanation']
    else:
        expl = q['explanation']
    q['_opts'], q['_ci'], q['_expl'] = opts, ci, expl

# 文の組み立て
for i, o in ORDERING.items():
    q = Q[i]
    ch = o['chunks']
    blanks = ['＿'] * 4
    blanks[o['star']] = '★'
    q['_title_src'] = f"{o['prefix']} {' '.join(blanks)} {o['suffix']}"
    q['_ordering'] = o

# ---------------------------------------------------------------- answer-position balancing (ids 1-80)
rng = random.Random(20261103)
movable = [q for q in qs if q['id'] <= 80 and q['id'] not in ORDERED_IDS]
fixed_counts = [0, 0, 0, 0]
for q in qs:
    if q['id'] in ORDERED_IDS:
        fixed_counts[q['_ci']] += 1
total4 = 80
goal = [14, 21, 23, 22]            # spoken 3-choice items 81-91 are fixed at [9, 2, 0, 0] -> overall about 23 each
need = [goal[k] - fixed_counts[k] for k in range(4)]
assert sum(need) == len(movable), (need, len(movable))

def make_targets():
    for _ in range(20000):
        seq = [k for k in range(4) for _ in range(need[k])]
        rng.shuffle(seq)
        # no run of 3 (consider ordered ids at their fixed positions)
        full = []
        it = iter(seq)
        for q in qs:
            if q['id'] > 80:
                break
            full.append(q['_ci'] if q['id'] in ORDERED_IDS else next(it))
        if any(full[j] == full[j - 1] == full[j - 2] for j in range(2, len(full))):
            continue
        # spread inside each subsection: no choice more than ceil(n/4)+1 times
        ok = True
        by = {}
        for q, t in zip([x for x in qs if x['id'] <= 80], full):
            by.setdefault(q['subsectionId'], []).append(t)
        for sub, lst in by.items():
            n = len(lst)
            if any(lst.count(k) > -(-n // 4) + 1 for k in range(4)):
                ok = False; break
        if ok:
            return full
    raise SystemExit('could not build balanced targets')

targets = make_targets()
tmap = {q['id']: t for q, t in zip([x for x in qs if x['id'] <= 80], targets)}

for q in qs:
    i = q['id']
    opts, ci = q['_opts'], q['_ci']
    if i in ORDERING:
        o = q['_ordering']
        correct = o['chunks'][o['star']]
        others = [c for c in o['chunks'] if c != correct]
        rng.shuffle(others)
        tgt = tmap[i]
        new = others[:tgt] + [correct] + others[tgt:]
        # make sure the display order is not the natural order (avoid giving away the answer pattern)
        q['_new_opts'], q['_new_ci'] = new, tgt
        nat = ''.join(f'【{c}】' if k != o['star'] else f'★【{c}】' for k, c in enumerate(o['chunks']))
        q['_expl_final'] = (f"正しい語順は「{o['prefix']} {nat} {o['suffix']}」となります。\n★に入るのは「{correct}」です。")
        continue
    if i in SPOKEN_OPTION_IDS or i in ORDERED_IDS:
        q['_new_opts'], q['_new_ci'] = opts, ci
    else:
        tgt = tmap[i]
        correct = opts[ci]
        others = [o for k, o in enumerate(opts) if k != ci]
        new = others[:tgt] + [correct] + others[tgt:]
        q['_new_opts'], q['_new_ci'] = new, tgt
    q['_expl_final'] = strip_nums(q['_expl'])

# ---------------------------------------------------------------- generate ruby fields + write back
problems = []
for q in qs:
    i = q['id']
    cat = q['category']
    # title
    src = q.get('_title_src') or title_source(q)
    src = fix(src)
    try:
        if cat == '漢字読み':
            tr = R(src, skip_u=True)
        else:
            tr = R(src)
    except Exception as ex:
        problems.append((i, 'title', str(ex))); continue
    q['titleRuby'] = tr
    q['title'] = P(re.sub(r'</?u>', '', src))
    if cat == '漢字読み':
        q['targetWord'] = EDITS.get(i, {}).get('target', q['targetWord'])
    # options
    q['options'] = q['_new_opts']
    q['correctIndex'] = q['_new_ci']
    if cat in ('表記',) or cat == '漢字読み':
        q.pop('optionsRuby', None)   # 表記: choices are plain kanji on purpose (no spoiler ruby); 読み: kana only
    else:
        try:
            q['optionsRuby'] = [R(fix(o)) for o in q['options']]
        except Exception as ex:
            problems.append((i, 'options', str(ex)))
    q['explanation'] = q['_expl_final']
    # passage
    if i in PASSAGES:
        p = PASSAGES[i]
        text = p if isinstance(p, str) else p['text']
        ev = None if isinstance(p, str) else p.get('evidence')
        try:
            html, evh = ruby_passage(text, ev)
        except Exception as ex:
            problems.append((i, 'passage', str(ex))); continue
        q['passage'] = plain_passage(text)
        q['passageRuby'] = html
        if evh:
            q['evidence'] = evh
        elif 'evidence' in q and not ev:
            pass
    elif q.get('passage'):
        # unchanged passages (63, 65, 67): rebuild ruby sentence-wise for verified readings, keep evidence
        ev_plain = None
        # recover the plain evidence from the existing (ruby) evidence
        if q.get('evidence'):
            ev_plain = P(q['evidence'])
        try:
            html, evh = ruby_passage(q['passage'], ev_plain)
        except Exception as ex:
            problems.append((i, 'passage', str(ex))); continue
        q['passageRuby'] = html
        if evh:
            q['evidence'] = evh
    # script (listening)
    if q.get('script'):
        try:
            q['scriptRuby'] = '<br>\n'.join(R(fix(l)) for l in q['script'].split('\n'))
        except Exception as ex:
            problems.append((i, 'script', str(ex)))
    if i == 82:
        q['sceneDesc'] = P(re.sub(r'</?u>', '', EDITS[82]['title']))
    for k in [k for k in q if k.startswith('_')]:
        q.pop(k)

for sec in DATA['sections']:
    for sub in sec['subsections']:
        if sub['id'] in DESC:
            sub['desc'] = DESC[sub['id']]

if problems:
    print('PROBLEMS:'); [print('  ', p) for p in problems]
    sys.exit(1)

# normalise key order: keep original order, put optionsRuby right after options
for q in qs:
    od = {}
    for k, v in q.items():
        if k == 'optionsRuby':
            continue
        od[k] = v
        if k == 'options' and 'optionsRuby' in q:
            od['optionsRuby'] = q['optionsRuby']
    q.clear(); q.update(od)

body = json.dumps(DATA, ensure_ascii=False, indent=2)
final = 'window.JLPT_N5_MOCK_DATA = ' + body + ';\n'
if '--check' in sys.argv:
    print('check only; not written')
else:
    open(SRC, 'w', encoding='utf-8').write(final)
    shutil.copyfile(SRC, PUB)
    print('written', SRC, 'and', PUB)
print('answer distribution (all 91):', [sum(1 for q in qs if q['correctIndex'] == k) for k in range(4)])
