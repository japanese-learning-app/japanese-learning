# -*- coding: utf-8 -*-
"""
N5 listening + reading audit / repair.

Reads the ORIGINAL data from scripts/n5_rewrite/scratch/orig_{listening,reading}.js (so this script is idempotent)
and writes database/jlpt_n5_listening_data.js and database/jlpt_n5_reading_data.js (CRLF, 2-space JSON indent).

Run:  python3 scripts/n5_rewrite/fix_listening_reading.py
"""
import sys, re, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
from n5_lib import R, P, lint_ruby, sensitive_hits

# 3-choice 問題3/4 are read aloud as "1番、2番、3番": reordering them needs new MP3s.
# Keep False until the MP3s for n5_q22 / n5_q23 are re-synthesised (see AUDIO_RESYNTH_NEEDED.md).
REORDER_3CHOICE = True


def load_js(path):
    s = open(path, encoding='utf-8', newline='').read().replace('\r\n', '\n')
    i = s.index('window.')
    header = s[:i]
    name = re.match(r'window\.(\w+)\s*=', s[i:]).group(1)
    j = s.index('=', i) + 1
    d, e = json.JSONDecoder().raw_decode(s[j:].lstrip())
    return header, name, d


def save_js(path, header, name, d):
    out = header + f'window.{name} = ' + json.dumps(d, ensure_ascii=False, indent=2) + ';\n'
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(out.replace('\n', '\r\n'))


def RR(t):
    """R() with project-wide fixed readings for words the library cannot decide alone."""
    t = t.replace('何と言', '{何|なん}と言').replace('二人', '{二人|ふたり}').replace('一人', '{一人|ひとり}')
    t = re.sub(r'(?<!\{)辛', '{辛|から}', t)
    t = re.sub(r'日本(?!語)', '{日本|にほん}', t)
    t = t.replace('誕生日', '{誕生日|たんじょうび}')
    t = t.replace('行ってくる', '{行|い}ってくる').replace('通っ', '{通|かよ}っ')
    t = t.replace('留学生', '{留学生|りゅうがくせい}').replace('夕方', '{夕方|ゆうがた}').replace('仕方', '{仕方|しかた}').replace('一生懸命', '{一生懸命|いっしょうけんめい}')
    t = re.sub(r'(?<![\d{])1日に', '{1日|いちにち}に', t)
    t = t.replace('一日', '{一日|いちにち}') if '{一日' not in t else t
    return R(t)


# =====================================================================================================
# LISTENING
# =====================================================================================================
# target position (0-based) of the correct answer for 4-choice questions (their options are NOT read aloud)
LIS_TARGET = {1: 1, 2: 3, 3: 0, 4: 2, 5: 3, 6: 0, 7: 1, 8: 3, 9: 2, 10: 0, 11: 3, 12: 2, 13: 1}

# spoken-script changes (-> AUDIO_RESYNTH_NEEDED.md)
SPEECH_FIX = {
    8: [('いつものバスが事故で来なくて、30分もバス停で待ったんです。', 'いつものバスがなかなか来なくて、30分もバス停で待ったんです。'),
        ('そうでしたか。事故なら仕方ありませんね。', 'そうでしたか。それなら仕方ありませんね。')],
    11: [('天気が悪くなりそうだったので、海へ行きました。', '友達が魚を食べたいと言ったので、海へ行きました。')],
}

TITLE_FIX = {1: 'あしたのテストの持ち物'}

# Explanation overrides. {N} = 1-based number of the correct choice. None -> keep (re-numbered automatically).
EXP = {
    1: {},
    2: {'zh': '女士拜託他「只要胡蘿蔔和馬鈴薯就好」，因此選項{N}正確。'},
    3: {'ko': '10시 15분에 역 안의 카페에서 만나기로 했으므로 {N}번이 정답입니다.'},
    6: {'ja': '駅員が「2番線に来る青い電車に乗ってください」と案内しているため、{N}番が正解です。',
        'en': 'The station attendant tells her to take the blue train that comes to Track 2, so Choice {N} is correct.',
        'zh': '站務員指示「請搭乘2號月台進站的藍色電車」，因此選項{N}正確。',
        'ko': '역무원이 "2번 승강장에 들어오는 파란색 전철을 타세요"라고 안내했으므로 {N}번이 정답입니다.'},
    7: {'zh': '女士請他「在鍋子裡裝水，把水燒開」，男士也答應了，因此選項{N}正確。'},
    8: {'ja': '「いつものバスがなかなか来なくて、30分も待った」と言っているため、{N}番が正解です。',
        'en': 'He says his usual bus would not come for a long time and he waited 30 minutes, so Choice {N} is correct.',
        'zh': '男士說「平常搭的公車遲遲不來，等了30分鐘」，因此選項{N}正確。',
        'ko': '\'평소 타던 버스가 좀처럼 오지 않아서 30분이나 기다렸다\'고 했으므로 {N}번이 정답입니다.'},
    10: {'en': 'He says that among the sports he plays himself, tennis is his favorite, so Choice {N} is correct.'},
    11: {'ja': '「友達が魚を食べたいと言ったので、海へ行きました」と言っているため、{N}番（海）が正解です。',
         'en': 'She says she went to the sea because her friend wanted to eat fish, so Choice {N} (the sea) is correct.',
         'zh': '女士說「因為朋友說想吃魚，所以去了海邊」，因此選項{N}（海邊）正確。',
         'ko': '\'친구가 생선을 먹고 싶다고 해서 바다에 갔습니다\'라고 했으므로 {N}번(바다)이 정답입니다.'},
    13: {'zh': '女士提到契機是「想不看字幕就能看動畫」，因此選項{N}正確。'},
    15: {'ja': '食事が終わったときの挨拶は「ごちそうさまでした」です（{N}番が正解）。'},
    16: {'ja': '知らない人に声をかけて質問するときは「すみません」を使います（{N}番が正解）。'},
    17: {'ja': '仕事場で、ほかの人より先に帰るときは「お先に失礼します」と言います（{N}番が正解）。',
         'en': 'When leaving work before the others, say \'Osaki ni shitsurei shimasu\' (Excuse me for leaving before you), so Choice {N} is correct.',
         'zh': '在公司比其他人先下班時，固定說法是「お先に失礼します」（我先走了），因此選項{N}正確。',
         'ko': '직장에서 다른 사람보다 먼저 퇴근할 때는 \'お先に失礼します(먼저 가 보겠습니다)\'라고 합니다 ({N}번 정답).'},
    18: {'ja': '物を相手に渡すときは「どうぞ」と言います（{N}番が正解）。'},
    21: {'zh': '對方請求借筆，爽快答應並遞上的「はい、どうぞ」（好的，請用，選項{N}）正確。'},
    23: {'ja': '「辛いですか」という質問に対して、「いいえ、あまり辛くないです」（{N}番）が質問に合った答えです。'},
}


def renum(text, lang, old, new):
    pat = {'ja': r'(?<!\d)%d番(?!線)', 'en': r'Choice %d(?!\d)', 'zh': r'選項%d(?!\d)', 'ko': r'(?<!\d)%d번'}[lang] % old
    rep = {'ja': f'{new}番', 'en': f'Choice {new}', 'zh': f'選項{new}', 'ko': f'{new}번'}[lang]
    return re.sub(pat, rep, text)


def build_script_html(speech):
    lines = speech.split('\n')
    header, footer = lines[0], lines[-1]
    body = [l for l in lines[1:-1] if l.strip()]
    p = lambda s: s.replace('。。', '。')
    out = ['<div class="space-y-2 text-sm leading-relaxed">\n      ',
           f'<p class="text-xs font-bold text-slate-400 mb-1">{RR(p(header))}</p>']
    for l in body:
        m = re.match(r'^(\d)番、(.*)$', l)
        if m:
            label, text = f'{m.group(1)}番：', m.group(2)
        else:
            label, text = l.split('：', 1)
            label += '：'
        out.append(f'<p><span class="font-bold text-[#1995AD]">{RR(label)}</span>{RR(text)}</p>')
    out.append(f'<p class="text-xs font-bold text-[#B8596E] mt-2">{RR(p(footer))}</p>')
    out.append('\n    </div>')
    return ''.join(out)


def fix_listening():
    header, name, d = load_js(os.path.join(HERE, 'scratch', 'orig_listening.js'))
    report = []
    for q in d['questions']:
        n = q['q_num']
        old_ans = q['answer']
        # --- spoken script
        if n in SPEECH_FIX:
            for a, b in SPEECH_FIX[n]:
                assert a in q['speech_audio_text'], (n, a)
                q['speech_audio_text'] = q['speech_audio_text'].replace(a, b)
        # --- choices (plain -> reorder -> ruby)
        plain = [P(c) for c in q['choices']]
        correct = plain[old_ans]
        target = LIS_TARGET.get(n)
        if n == 22 and REORDER_3CHOICE:
            target = 2
        if n == 23 and REORDER_3CHOICE:
            target = 1
        if target is not None and target != old_ans:
            ds = [c for i, c in enumerate(plain) if i != old_ans]
            plain = ds[:target] + [correct] + ds[target:]
        new_ans = plain.index(correct)
        if REORDER_3CHOICE and n in (22, 23) and new_ans != old_ans:
            # re-write the spoken option list ("1番、…") so the MP3 can be re-synthesised in the new order
            sp = q['speech_audio_text'].split('\n')
            k = [i for i, l in enumerate(sp) if re.match(r'^\d番、', l)]
            for pos, i in enumerate(k):
                sp[i] = f'{pos + 1}番、{plain[pos]}'
            q['speech_audio_text'] = '\n'.join(sp)
        q['choices'] = [RR(c) for c in plain]
        q['answer'] = new_ans
        # --- explanation
        exp = {}
        for lang in ('ja', 'en', 'zh', 'ko'):
            if lang in EXP.get(n, {}):
                t = EXP[n][lang].replace('{N}', str(new_ans + 1))
            else:
                t = renum(q['explanation'][lang], lang, old_ans + 1, new_ans + 1)
            exp[lang] = RR(t) if lang == 'ja' else t
        q['explanation'] = exp
        # --- title / prompt ruby / script
        if n in TITLE_FIX:
            q['title'] = TITLE_FIX[n]
        # insert prompt_ruby right after prompt (keep key order tidy)
        new_q = {}
        for k, v in q.items():
            new_q[k] = v
            if k == 'prompt':
                new_q['prompt_ruby'] = RR(q['prompt'])
        new_q['script_html'] = build_script_html(q['speech_audio_text'])
        q.clear(); q.update(new_q)
        report.append((n, old_ans + 1, new_ans + 1))
    save_js(os.path.join(REPO, 'database', 'jlpt_n5_listening_data.js'), header, name, d)
    return d, report


# =====================================================================================================
# READING  (all passages rebuilt from plain source with R(); brackets 【】 around evidence removed)
# =====================================================================================================
def ev(i, s):
    return f'<span id="ev-n5-p{i}" class="evidence-target">{s}</span>'


def para(s, br=False):
    return f'<p class="mb-3">{s}</p>'


# (text_html source, question, choices[correct first], explanation(ja,en,zh,ko with {N}), target)
READING = [
    dict(
        id='n5_p1', type='短文（内容理解）', section_name='問題4 短文読解', genre='お知らせ・掲示',
        title='日本語クラスの遠足のおしらせ', time_est='2〜3分',
        text=[para('【日本語クラスのみなさんへ】'),
              para('来週の土曜日に、みんなで山へ行きます。朝8時に学校の前に集まってください。'
                   + '@EV@'
                   + '山へ行く{日|ひ}は、昼ごはんと飲み物を持ってきてください。')],
        ev='雨が降ったら、山へは行きません。その{日|ひ}は、午後1時から学校の教室で映画を見ます。',
        vocab=[('遠足（えんそく）', 'excursion / picnic'), ('集まる（あつまる）', 'to gather'), ('持ってくる（もってくる）', 'to bring')],
        question='来週の土曜日、雨が降ったら、どうしますか。',
        correct='午後1時から学校の教室で映画を見ます。',
        wrong=['朝8時に学校の前に集まって、山へ行きます。', '昼ごはんを食べてから山へ行きます。', '来週の日曜日に山へ行きます。'],
        target=2,
        exp=dict(ja='本文に「雨が降ったら、山へは行きません。その{日|ひ}は、午後1時から学校の教室で映画を見ます」とあるので、{N}番が正解です。',
                 en='The notice says that if it rains they will not go to the mountain and will watch a movie in a school classroom from 1:00 p.m. instead, so Choice {N} is correct.',
                 zh='通知中寫道「如果下雨，就不去山上。當天下午1點起在學校教室看電影」，因此選項{N}正確。',
                 ko="안내문에 '비가 오면 산에는 가지 않습니다. 그날은 오후 1시부터 학교 교실에서 영화를 봅니다'라고 적혀 있으므로 {N}번이 정답입니다."),
    ),
    dict(
        id='n5_p2', type='短文（内容理解）', section_name='問題4 短文読解', genre='メモ',
        title='山田さんへのメモ', time_est='2〜3分',
        text=[para('山田さんへ'),
              para('昨日、図書館で本を借りました。山田さんが読みたいと言っていたので、机の上に置きました。<br>'
                   '私は今日、風邪で学校を休みます。' + '@EV@' + 'お願いします。<br>田中より')],
        ev='この本は、明日が返す{日|ひ}です。すみませんが、山田さんが図書館へ返してください。',
        vocab=[('借りる（かりる）', 'to borrow'), ('返す（かえす）', 'to return (something)'), ('風邪（かぜ）', 'a cold / illness')],
        question='山田さんは、何をしなければなりませんか。',
        correct='明日までに、本を図書館へ返すこと。',
        wrong=['田中さんの家へ本を持って行くこと。', '今日、田中さんに電話をかけること。', '図書館で新しい本を借りること。'],
        target=0,
        exp=dict(ja='メモに「この本は、明日が返す{日|ひ}です。すみませんが、山田さんが図書館へ返してください」と書かれているので、{N}番が正解です。',
                 en='The memo says that tomorrow is the return date and asks Yamada to return the book to the library, so Choice {N} is correct.',
                 zh='便條上寫道「這本書明天要還。不好意思，請山田拿去還給圖書館」，因此選項{N}正確。',
                 ko="메모에 '이 책은 내일이 반납하는 날입니다. 미안하지만 야마다 씨가 도서관에 반납해 주세요'라고 적혀 있으므로 {N}번이 정답입니다."),
    ),
    dict(
        id='n5_p3', type='短文（内容理解）', section_name='問題4 短文読解', genre='メール',
        title='誕生日パーティーのメール', time_est='2〜3分',
        text=[para('ケンさん、こんにちは。'),
              para('今度の日曜日は、私の誕生日です。家でパーティーをします。ケンさんも来てください。夕方5時に始まります。'
                   + '@EV@' + 'ケンさんは、おなかをすかせて来てください。<br>マリアより')],
        ev='プレゼントも飲み物も、いりません。ケーキと料理は、私が用意します。',
        vocab=[('誕生日（たんじょうび）', 'birthday'), ('用意する（よういする）', 'to prepare'), ('おなかをすかせる', 'to be hungry (here: to come hungry)')],
        question='ケンさんは、パーティーに行くとき、何を持って行けばいいですか。',
        correct='何も持って行かなくてもいい。',
        wrong=['誕生日プレゼントを持って行く。', 'おいしいケーキを買って持って行く。', '飲み物をたくさん持って行く。'],
        target=3,
        exp=dict(ja='メールに「プレゼントも飲み物も、いりません。ケーキと料理は、私が用意します」と書かれているので、何も持って行かなくてもいいです（{N}番が正解）。',
                 en="The email says Maria needs neither a present nor drinks and will prepare the cake and food herself, so Ken does not need to bring anything (Choice {N}).",
                 zh='郵件中寫道「不需要禮物，也不需要飲料。蛋糕和料理由我來準備」，所以什麼都不用帶（選項{N}正確）。',
                 ko="메일에 '선물도 음료도 필요 없습니다. 케이크와 요리는 제가 준비합니다'라고 적혀 있으므로 아무것도 가져가지 않아도 됩니다 ({N}번 정답)."),
    ),
    dict(
        id='n5_p4', type='中文（内容理解）', section_name='問題5 中文読解', genre='日記',
        title='日本で初めてのお正月', time_est='4〜5分',
        text=[para('1月{2日|ふつか}（水曜日）　晴れ'),
              para('昨日は1月{1日|ついたち}、お正月でした。私は友達の佐藤さんの家へ行きました。佐藤さんのご家族と一緒に「おせち料理」を食べました。きれいで、とてもおいしかったです。'),
              para('昼ごはんの後、みんなで近くの公園へ行きました。人がたくさんいました。'
                   + '@EV@' + 'とても楽しい{一日|いちにち}でした。')],
        ev='公園で、たこあげをしました。私のたこは、いちばん高く上がりました。',
        vocab=[('お正月（おしょうがつ）', 'New Year'), ('おせち料理（おせちりょうり）', 'osechi (traditional New Year dishes)'), ('たこあげ', 'kite flying')],
        question='「私」は公園で何をしましたか。',
        correct='たこあげをした。',
        wrong=['おせち料理をみんなで食べた。', '友達と一緒に映画を見た。', '佐藤さんのご家族と写真をとった。'],
        target=1,
        exp=dict(ja='本文に「公園で、たこあげをしました」と書かれているので、{N}番が正解です。おせち料理を食べたのは佐藤さんの家で、公園ではありません。',
                 en='The diary says the writer flew a kite in the park. The osechi meal was eaten at Sato\'s house, not in the park, so Choice {N} is correct.',
                 zh='日記中寫道「在公園放了風箏」。吃年菜（おせち料理）是在佐藤家，不是在公園，因此選項{N}正確。',
                 ko="일기에 '공원에서 연날리기를 했습니다'라고 적혀 있습니다. 오세치 요리를 먹은 곳은 사토 씨 집이지 공원이 아니므로 {N}번이 정답입니다."),
    ),
    dict(
        id='n5_p5', type='中文（内容理解）', section_name='問題5 中文読解', genre='手紙',
        title='お母さんへの手紙', time_est='4〜5分',
        text=[para('お母さんへ'),
              para('お元気ですか。私は毎日元気に暮らしています。大学の寮の生活にも慣れました。部屋は少し狭いですが、明るくてきれいです。'),
              para('@EV@' + '先週はリンさんの国のカレーを作りました。とてもおいしかったです。来週はテストがありますから、今は一生懸命勉強しています。体に気をつけてくださいね。<br>アンナより')],
        ev='ルームメイトのリンさんはとても親切で、毎晩一緒に晩ごはんを作っています。',
        vocab=[('寮（りょう）', 'dormitory'), ('慣れる（なれる）', 'to get used to'), ('一生懸命（いっしょうけんめい）', "with all one's effort / hard")],
        question='アンナさんは、ルームメイトのリンさんと何をしていますか。',
        correct='毎晩、一緒に晩ごはんを作っている。',
        wrong=['毎日、一緒に大学へ通っている。', '毎週日曜日に、一緒に買い物に行っている。', 'リンさんの国のことばを教えてもらっている。'],
        target=2,
        exp=dict(ja='手紙に「ルームメイトのリンさんはとても親切で、毎晩一緒に晩ごはんを作っています」と書かれているので、{N}番が正解です。',
                 en='The letter says that Lin, the roommate, is very kind and that they make dinner together every evening, so Choice {N} is correct.',
                 zh='信中寫道「室友Lin非常親切，我們每天晚上一起做晚飯」，因此選項{N}正確。',
                 ko="편지에 '룸메이트인 린 씨는 매우 친절해서 매일 밤 함께 저녁을 만들고 있습니다'라고 적혀 있으므로 {N}번이 정답입니다."),
    ),
    dict(
        id='n5_p6', type='情報検索', section_name='問題6 情報検索', genre='案内チラシ',
        title='留学生会館の利用案内', time_est='3〜4分',
        text=None,   # built below (table)
        ev='洗濯機を使うときは、100円玉を1枚入れてください。21時を過ぎたら、使えません。',
        vocab=[('洗濯機（せんたくき）', 'washing machine'), ('自習室（じしゅうしつ）', 'study room'), ('無料（むりょう）', 'free of charge')],
        question='トムさんは、夜9時半に洗濯をしたいです。どうすればいいですか。',
        correct='今夜は使えないので、明日の朝、8時になってから使う。',
        wrong=['100円玉を入れて、今すぐ使う。', '100円玉を入れないで、無料で使う。', '夜10時まで待ってから使う。'],
        target=0,
        exp=dict(ja='案内表に「洗濯機：8:00〜21:00」「21時を過ぎたら、使えません」とあるので、夜9時半には使えません。明日の朝8時になってから使います（{N}番が正解）。',
                 en='The notice says the washing machine can only be used from 8:00 to 21:00 and not after 21:00, so Tom cannot use it at 21:30 and must wait until 8:00 tomorrow morning (Choice {N}).',
                 zh='告示寫道洗衣機的使用時間為8:00〜21:00，「21點以後不能使用」，所以晚上9點半不能用，要等到明天早上8點以後（選項{N}正確）。',
                 ko="안내문에 '세탁기: 8:00~21:00', '21시가 지나면 사용할 수 없습니다'라고 적혀 있으므로 밤 9시 반에는 쓸 수 없고, 내일 아침 8시가 되고 나서 사용합니다 ({N}번 정답)."),
    ),
]


def p6_html(ev_src):
    cell = 'p-1.5 border'
    rows = [('キッチン', '7:00 〜 22:00', '0円（無料）'),
            ('{洗濯機|せんたくき}', '8:00 〜 21:00', '1回 100円'),
            ('{自習室|じしゅうしつ}（勉強の{部屋|へや}）', '24時間いつでも', '0円（無料）')]
    h = ['<div class="border-2 border-slate-300 rounded-xl p-4 bg-white text-xs leading-relaxed">',
         '<h4 class="text-center font-bold text-sm text-[#1995AD] border-b pb-2 mb-3">★ ' + R('留学生会館の使い方'.replace('使い方', '{使|つか}いかた').replace('留学生', '{留学生|りゅうがくせい}')) + ' ★</h4>',
         '<table class="w-full text-left border-collapse border border-slate-200 mb-3">',
         f'  <tr class="bg-slate-100 font-bold"><th class="{cell}">{R("{使|つか}うところ")}</th><th class="{cell}">{R("つかえる時間")}</th><th class="{cell}">{R("お金")}</th></tr>']
    for a, b, c in rows:
        h.append(f'  <tr><td class="{cell} font-bold">{R(a)}</td><td class="{cell}">{R(b)}</td><td class="{cell}">{R(c)}</td></tr>')
    h.append('</table>')
    h.append(f'<p class="text-slate-600">{R("※ ")}{ev_src}</p>')
    h.append('</div>')
    return '\n'.join(h)


def fix_reading():
    header, name, d = load_js(os.path.join(HERE, 'scratch', 'orig_reading.js'))
    old = {p['id']: p for p in d['passages']}
    new_passages = []
    for qn, spec in enumerate(READING, 1):
        p0 = old[spec['id']]
        evs = ev(int(spec['id'][-1]), RR(spec['ev']))
        if spec['text'] is None:
            text_html = p6_html(evs)
        else:
            parts = []
            for t in spec['text']:
                # split on the placeholder so each side is annotated separately (tags pass through R)
                segs = t.split('@EV@')
                out = []
                for k, sg in enumerate(segs):
                    # sg may contain <p ...> and <br> tags: R() passes tags through
                    out.append(RR(sg))
                    if k < len(segs) - 1:
                        out.append(evs)
                parts.append(''.join(out))
            text_html = '\n'.join(parts)
        # choices
        ds = spec['wrong']
        plain = ds[:spec['target']] + [spec['correct']] + ds[spec['target']:]
        q0 = p0['questions'][0]
        q = dict(q_num=q0['q_num'], question_html=RR(spec['question']), evidence_id=q0['evidence_id'],
                 choices=[RR(c) for c in plain], answer=spec['target'])
        q['explanation'] = {k: (RR(v.replace('{N}', str(spec['target'] + 1))) if k == 'ja' else v.replace('{N}', str(spec['target'] + 1)))
                            for k, v in spec['exp'].items()}
        p = dict(id=p0['id'], type=spec['type'], section_name=spec['section_name'], genre=spec['genre'],
                 title=spec['title'], title_ruby=RR(spec['title']), time_est=spec['time_est'],
                 text_html=text_html,
                 vocab_notes=[dict(word=w, meaning=m) for w, m in spec['vocab']],
                 questions=[q])
        new_passages.append(p)
    d['passages'] = new_passages
    save_js(os.path.join(REPO, 'database', 'jlpt_n5_reading_data.js'), header, name, d)
    return d


# =====================================================================================================
def self_check(lis, rd):
    ok = True
    def bad(msg):
        nonlocal ok; ok = False; print('NG', msg)
    ans = []
    for q in lis['questions']:
        n = q['q_num']
        fields = {'prompt_ruby': q['prompt_ruby'], 'script_html': q['script_html'], 'exp.ja': q['explanation']['ja']}
        for i, c in enumerate(q['choices']):
            fields[f'choice{i+1}'] = c
        for k, v in fields.items():
            L = lint_ruby(v)
            if L: bad(f'listening q{n} {k} unruby kanji {L}')
            if sensitive_hits(v): bad(f'listening q{n} {k} sensitive {sensitive_hits(v)}')
        if len(set(q['choices'])) != len(q['choices']): bad(f'listening q{n} dup choices')
        if '。。' in q['script_html']: bad(f'q{n} 。。 in script_html')
        ans.append(q['answer'] + 1)
    print('listening answers:', ans)
    for q in lis['questions']:
        if q['q_num'] <= 13:
            pass
    print('  4-choice (q1-13):', ans[:13], ' 3-choice (q14-24):', ans[13:])
    for i in range(2, len(ans)):
        if ans[i] == ans[i-1] == ans[i-2]:
            if i + 1 >= 22 and not REORDER_3CHOICE: print(f'WARN 3-in-a-row at q{i+1} (needs MP3 re-synthesis, see AUDIO_RESYNTH_NEEDED.md B)')
            else: bad(f'3-in-a-row at q{i+1}')
    ra = []
    for p in rd['passages']:
        for q in p['questions']:
            fields = {'title_ruby': p['title_ruby'], 'text_html': p['text_html'], 'question': q['question_html'], 'exp.ja': q['explanation']['ja']}
            for i, c in enumerate(q['choices']): fields[f'choice{i+1}'] = c
            for k, v in fields.items():
                L = lint_ruby(v)
                if L: bad(f'reading {p["id"]} {k} unruby kanji {L}')
                if sensitive_hits(v): bad(f'reading {p["id"]} {k} sensitive {sensitive_hits(v)}')
            if q['evidence_id'] not in p['text_html']: bad(f'{p["id"]} evidence id missing')
            if len(set(q['choices'])) != 4: bad(f'{p["id"]} dup choices')
            ra.append(q['answer'] + 1)
    print('reading answers:', ra)
    for i in range(2, len(ra)):
        if ra[i] == ra[i-1] == ra[i-2]: bad('reading 3-in-a-row')
    print('SELF-CHECK', 'OK' if ok else 'FAILED')


if __name__ == '__main__':
    lis, rep = fix_listening()
    rd = fix_reading()
    print('answer moves (q, old, new):', [r for r in rep if r[1] != r[2]])
    self_check(lis, rd)
