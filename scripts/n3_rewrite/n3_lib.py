# -*- coding: utf-8 -*-
"""
N3 content rewrite helper library (adapted & extended from n4_lib.py).

* R(text)            : plain Japanese (+ optional {漢字|よみ} overrides) -> <ruby> HTML
* P(html)            : strip ruby/tags -> plain text
* lint_ruby(html)    : list kanji that are NOT covered by <ruby>
* place_choices(...) : put the correct answer at a target index (safe shuffle)
* balanced_targets() : answer positions 0-3, balanced, never 3-in-a-row
* sensitive_hits(t)  : banned (political / war / hostile / brand / 公式 / 準拠) vocabulary scan
* write_js(...)      : dump as `window.NAME = <json>;`
"""
import re, json, random
from janome.tokenizer import Tokenizer

_tok = Tokenizer()
KANJI = re.compile(r'[\u4e00-\u9fff々〆ヶ]')
HAS_KANJI = lambda s: bool(KANJI.search(s))

def kata2hira(s):
    return ''.join(chr(ord(c) - 0x60) if 'ァ' <= c <= 'ヶ' else c for c in s)

def hira2kata(s):
    return ''.join(chr(ord(c) + 0x60) if 'ぁ' <= c <= 'ゖ' else c for c in s)

def _ruby(base, rt):
    return f'<ruby>{base}<rt>{rt}</rt></ruby>'

# ---------------------------------------------------------------- numerals
_ZEN = str.maketrans('０１２３４５６７８９', '0123456789')
_KNUM = {'〇': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}

def parse_num(s):
    s = s.translate(_ZEN)
    if s == '何':
        return None
    if s.isdigit():
        return int(s)
    n, cur = 0, 0
    for c in s:
        if c in _KNUM:
            cur = _KNUM[c]
        elif c == '十':
            n += (cur or 1) * 10; cur = 0
        elif c == '百':
            n += (cur or 1) * 100; cur = 0
        elif c == '千':
            n += (cur or 1) * 1000; cur = 0
    return n + cur

_DIG = ['れい', 'いち', 'に', 'さん', 'よん', 'ご', 'ろく', 'なな', 'はち', 'きゅう']

def num_reading(n, last='std'):
    if n == 0:
        return 'れい'
    parts = []
    th, h, t, u = (n // 1000) % 10, (n // 100) % 10, (n // 10) % 10, n % 10
    if th:
        parts.append(({3: 'さんぜん', 8: 'はっせん'}).get(th, ('' if th == 1 else _DIG[th]) + 'せん'))
    if h:
        parts.append(({3: 'さんびゃく', 6: 'ろっぴゃく', 8: 'はっぴゃく'}).get(h, ('' if h == 1 else _DIG[h]) + 'ひゃく'))
    if t:
        parts.append(('' if t == 1 else _DIG[t]) + 'じゅう')
    if u:
        d = _DIG[u]
        if last == 'yo' and u == 4: d = 'よ'
        if last == 'shichi' and u == 7: d = 'しち'
        if last == 'ku' and u == 9: d = 'く'
        if last == 'geminate':
            d = {1: 'いっ', 6: 'ろっ', 8: 'はっ'}.get(u, d)
        parts.append(d)
    elif last == 'geminate' and t:
        parts[-1] = parts[-1][:-1] + 'っ' if parts[-1].endswith('じゅう') else parts[-1]
    return ''.join(parts)

def _counter(name, n):
    q = n is None
    nq = 'なん'
    if name == '時':
        full = nq + 'じ' if q else num_reading(n, 'yo' if n % 10 == 4 else ('shichi' if n % 10 == 7 else ('ku' if n % 10 == 9 else 'std'))) + 'じ'
        return full, 'じ'
    if name == '時間':
        full = nq + 'じかん' if q else num_reading(n, 'yo' if n % 10 == 4 else ('shichi' if n % 10 == 7 else ('ku' if n % 10 == 9 else 'std'))) + 'じかん'
        return full, 'じかん'
    if name == '分':
        if q: return 'なんぷん', 'ぷん'
        u = n % 10
        p = u in (1, 3, 4, 6, 8, 0)
        c = 'ぷん' if p else 'ふん'
        num = num_reading(n, 'geminate' if u in (1, 6, 8, 0) else 'std')
        if u == 0 and n >= 10:
            num = num_reading(n, 'geminate')
        return num + c, c
    if name == '人':
        if q: return 'なんにん', 'にん'
        if n == 1: raise ValueError('1人/一人 は {一人|ひとり} と明示してください')
        if n == 2: raise ValueError('2人/二人 は {二人|ふたり} と明示してください')
        return num_reading(n, 'yo' if n % 10 == 4 else ('shichi' if n % 10 == 7 else 'std')) + 'にん', 'にん'
    if name == '歳':
        if q: return 'なんさい', 'さい'
        if n == 20: raise ValueError('20歳 は {二十歳|はたち} と明示してください')
        u = n % 10
        return num_reading(n, 'geminate' if u in (1, 8, 0) else 'std') + 'さい', 'さい'
    if name == '月':
        if q: return 'なんがつ', 'がつ'
        return num_reading(n, 'yo' if n % 10 == 4 else ('shichi' if n % 10 == 7 else ('ku' if n % 10 == 9 else 'std'))) + 'がつ', 'がつ'
    if name == '日':
        if q: return 'なんにち', 'にち'
        table = {1: 'ついたち', 2: 'ふつか', 3: 'みっか', 4: 'よっか', 5: 'いつか', 6: 'むいか', 7: 'なのか', 8: 'ようか',
                 9: 'ここのか', 10: 'とおか', 14: 'じゅうよっか', 20: 'はつか', 24: 'にじゅうよっか'}
        if n == 1: raise ValueError('一日/1日 は {一日|いちにち} か {一日|ついたち} と明示してください')
        if n in table:
            return table[n], table[n]
        return num_reading(n) + 'にち', 'にち'
    if name in ('円', '番', '年', '枚', '台', '度', '号', '才', '名', '部', '席', '件', '通', '倍', '割'):
        base = {'円': 'えん', '番': 'ばん', '年': 'ねん', '枚': 'まい', '台': 'だい', '度': 'ど', '号': 'ごう', '才': 'さい',
                '名': 'めい', '部': 'ぶ', '席': 'せき', '件': 'けん', '通': 'つう', '倍': 'ばい', '割': 'わり'}[name]
        if q: return 'なん' + base, base
        mode = 'yo' if n % 10 == 4 and name in ('円', '年') else ('shichi' if n % 10 == 7 and name == '年' else 'std')
        if name == '年' and n % 10 == 9: mode = 'ku'
        if name == '円' and n % 10 == 9: mode = 'std'
        if name == '件' and n % 10 in (1, 6, 8, 0): mode = 'geminate'
        return num_reading(n, mode) + base, base
    if name in ('回', '冊', '個', '階', '週間'):
        base = {'回': 'かい', '冊': 'さつ', '個': 'こ', '階': 'かい', '週間': 'しゅうかん'}[name]
        if q: return 'なん' + ('がい' if name == '階' else base), ('がい' if name == '階' else base)
        u = n % 10
        c = 'がい' if (name == '階' and u == 3) else base
        return num_reading(n, 'geminate' if u in (1, 6, 8, 0) else 'std') + c, c
    if name in ('本', '匹', '杯'):
        base = {'本': 'ほん', '匹': 'ひき', '杯': 'はい'}[name]
        if q: return 'なん' + {'本': 'ぼん', '匹': 'びき', '杯': 'はい'}[name], {'本': 'ぼん', '匹': 'びき', '杯': 'はい'}[name]
        u = n % 10
        cmap = {'本': ('ぽん', 'ぼん', 'ほん'), '匹': ('ぴき', 'びき', 'ひき'), '杯': ('ぱい', 'ばい', 'はい')}[name]
        if u in (1, 6, 8, 0): c = cmap[0]
        elif u == 3: c = cmap[1]
        else: c = cmap[2]
        return num_reading(n, 'geminate' if u in (1, 6, 8, 0) else 'std') + c, c
    if name == 'つ':
        if q: raise ValueError('何つ is not supported; use いくつ')
        tbl = {1: 'ひとつ', 2: 'ふたつ', 3: 'みっつ', 4: 'よっつ', 5: 'いつつ', 6: 'むっつ', 7: 'ななつ', 8: 'やっつ', 9: 'ここのつ', 10: 'とお'}
        if n not in tbl: raise ValueError('つ counter only 1-10')
        return tbl[n], tbl[n]
    raise ValueError('unknown counter ' + name)

_COUNTERS = ['時間', '週間', '時', '分', '日', '人', '歳', '月', '円', '本', '枚', '冊', '個', '回', '階', '番', '台', '匹', '杯', '年', '度', '号', '才', '名', '部', '席', '件', '通', '倍', '割', 'つ']
_NUM_RE = r'(?:[0-9０-９]+|[〇一二三四五六七八九十百]+|何)'
_CNT_RE = re.compile('(' + _NUM_RE + ')(' + '|'.join(_COUNTERS) + ')')

_NOT_COUNTER_FOLLOW = {
    '日': '曜本記常頃付',
    '月': '曜末初',
    '年': '生代間度末',
    '本': '当人語社店格的棚',
    '時': '々計代間期点',
    '分': '別野類析担',
    '人': '気形間類数生',
    '台': '所風湾',
    '番': '組目',
    '回': '転答復収線',
    '度': '々合い',
    '部': '門署長屋分品',
    '名': '前誉称簿',
    '通': 'りりの信勤学',
    '割': '合引',
}

STRICT = {
    '辛': '辛い: {辛|から}い(味覚) か {辛|つら}い(つらい) を明示',
    '開': '開く/開ける: {開|あ}く・{開|あ}ける(ドア・窓・目) か {開|ひら}く(会・店) を明示',
    '空': '空: {空|あ}く / {空|す}く / {空|そら} / {空|から} を明示',
    '方': '方: {方|かた} か {方|ほう} を明示',
    '生': '生: {生|う}まれる/{生|い}きる/{生|な}ま/{生|せい}(学生は一語で自動) を明示',
}

_EXPL = re.compile(r'\{([^{}|]+)\|([^{}|]+)\}')

def _align(surface, reading):
    runs = re.findall(r'[\u4e00-\u9fff々〆ヶ]+|[^\u4e00-\u9fff々〆ヶ]+', surface)
    pat = ''
    for r in runs:
        if HAS_KANJI(r[0]):
            pat += '(.+?)'
        else:
            pat += re.escape(kata2hira(r))
    m = re.fullmatch(pat, kata2hira(reading))
    if not m:
        return None
    out, gi = [], 1
    for r in runs:
        if HAS_KANJI(r[0]):
            out.append((r, m.group(gi))); gi += 1
        else:
            out.append((r, None))
    return out

_FIX_SURFACE = {
    '後': 'あと', '今日': 'きょう', '昨日': 'きのう', '明日': 'あした', '今朝': 'けさ', '今年': 'ことし',
    '去年': 'きょねん', '来年': 'らいねん', '来週': 'らいしゅう', '毎朝': 'まいあさ', '毎晩': 'まいばん',
    '毎日': 'まいにち', '毎週': 'まいしゅう', '毎月': 'まいつき', '毎年': 'まいとし', '大人': 'おとな',
    '上手': 'じょうず', '下手': 'へた', '友達': 'ともだち', '果物': 'くだもの', '眼鏡': 'めがね', '景色': 'けしき',
    '部屋': 'へや', 'お母さん': 'おかあさん', 'お父さん': 'おとうさん', '兄弟': 'きょうだい',
    '一緒': 'いっしょ', '八百屋': 'やおや', '二十歳': 'はたち', '今晩': 'こんばん', '今夜': 'こんや',
    '今月': 'こんげつ', '今週': 'こんしゅう', '先週': 'せんしゅう', '先月': 'せんげつ', '来月': 'らいげつ',
    '一人': 'ひとり', '二人': 'ふたり', '午前': 'ごぜん', '午後': 'ごご',
    '外国': 'がいこく', '日本': 'にほん', '日本語': 'にほんご', '日本人': 'にほんじん', '日本料理': 'にほんりょうり',
    '角': 'かど', '他': 'ほか', '緑色': 'みどりいろ',
    'お土産': 'おみやげ', 'お礼': 'おれい', 'お見舞い': 'おみまい', 'お祝い': 'おいわい',
    'お金持ち': 'おかねもち', '金持ち': 'かねもち', '一生懸命': 'いっしょうけんめい',
    '都合': 'つごう', '返事': 'へんじ', '支度': 'したく', '随分': 'ずいぶん', '田舎': 'いなか',
    '用事': 'ようじ', '花火': 'はなび', '火事': 'かじ', '怪我': 'けが', '泥棒': 'どろぼう',
    '番組': 'ばんぐみ', '具合': 'ぐあい', '留守': 'るす', '着物': 'きもの', '手袋': 'てぶくろ',
    '指輪': 'ゆびわ', '押し入れ': 'おしいれ', 'お嬢さん': 'おじょうさん', 'ご主人': 'ごしゅじん',
    '奥さん': 'おくさん', 'お子さん': 'おこさん', 'お宅': 'おたく', 'お釣り': 'おつり',
    '木綿': 'もめん', '大分': 'だいぶ', '二階建て': 'にかいだて', '運転手': 'うんてんしゅ',
    '米': 'こめ', '毛': 'け', '従兄弟': 'いとこ', '仲良し': 'なかよし', '迷子': 'まいご',
    '一言': 'ひとこと', '一息': 'ひといき', '一旦': 'いったん', '一斉': 'いっせい', '一層': 'いっそう',
    '一種': 'いっしゅ', '一致': 'いっち', '一般': 'いっぱん', '一方': 'いっぽう', '一生': 'いっしょう',
    '一時': 'いちじ', '一部': 'いちぶ', '一番': 'いちばん', '一度': 'いちど', '一流': 'いちりゅう',
    '十分': 'じゅうぶん', '半分': 'はんぶん', '自分': 'じぶん', '気分': 'きぶん', '部分': 'ぶぶん',
    '水分': 'すいぶん', '成分': 'せいぶん', '処分': 'しょぶん', '区分': 'くぶん', '配分': 'はいぶん',
    '大掃除': 'おおそうじ', '大雨': 'おおあめ', '大雪': 'おおゆき', '大風': 'おおかぜ', '大声': 'おおごえ',
    '大人気': 'だいにんき', '大多数': 'だいたすう', '大部分': 'だいぶぶん', '大規模': 'だいきぼ',
    '右腕': 'みぎうで', '左腕': 'ひだりうで', '右手': 'みぎて', '左手': 'ひだりて', '右側': 'みぎがわ', '左側': 'ひだりがわ',
    '間近': 'まぢか', '道幅': 'みちはば', '非常食': 'ひじょうしょく', '運動不足': 'うんどうぶそく', '寝不足': 'ねぶそく',
}

def _ruby_text(seg):
    holders = []
    def _cnt(m):
        num, cnt = m.group(1), m.group(2)
        nxt = seg[m.end():m.end() + 1]
        if cnt in _NOT_COUNTER_FOLLOW and nxt and nxt in _NOT_COUNTER_FOLLOW[cnt] and not (cnt == '年' and nxt == '生'):
            return m.group(0)
        n = parse_num(num)
        is_arabic = num.translate(_ZEN).isdigit()
        if cnt == 'つ' and is_arabic:
            return m.group(0)
        if cnt == '分' and not is_arabic and num != '何':
            raise ValueError(f'{num}分 は {{{num}分|じゅっぷん}} / {{{num}分|じゅうぶん}} など明示してください')
        full, only = _counter(cnt, n)
        if is_arabic and cnt == '日' and only != 'にち':
            html = _ruby(num + cnt, full)
        elif is_arabic:
            html = num + _ruby(cnt, only)
        else:
            html = _ruby(num + cnt, full)
        holders.append(html)
        return f'\uE000{len(holders) - 1}\uE001'
    seg2 = _CNT_RE.sub(_cnt, seg)
    out = []
    parts = re.split('(\uE000\\d+\uE001)', seg2)
    for part in parts:
        if part.startswith('\uE000'):
            out.append(holders[int(part[1:-1])]); continue
        _m = re.match(r'^(\s*)(.*?)(\s*)$', part, re.S)
        lead, core, trail = _m.groups()
        out.append(lead)
        part = core
        toks = list(_tok.tokenize(part)) if part else []
        for i, t in enumerate(toks):
            s = t.surface
            if not HAS_KANJI(s):
                out.append(s); continue
            if s == '日':
                raise ValueError('単独の「日」は {日|ひ} / {日|にち} / {日|び} と明示してください (例: （{日|にち}）)')
            k0 = s[0]
            if k0 in STRICT and (len(s) == 1 or not HAS_KANJI(s[1])) and s not in _FIX_SURFACE:
                if not (k0 == '生' and s in ('生徒', '学生', '先生', '生活', '生産', '生物', '誕生日', '高校生', '大学生', '小学生', '中学生', '留学生', '受験生', '卒業生', '新入生', '人生', '衛生', '発生', '再生', '生涯')):
                    raise ValueError(f'曖昧な漢字「{s}」は明示が必要: {STRICT[k0]}  (text: …{part[max(0,part.find(s)-6):part.find(s)+8]}…)')
            if s in _FIX_SURFACE:
                rd = _FIX_SURFACE[s]
            elif s == '何':
                nxt = toks[i + 1].surface if i + 1 < len(toks) else ''
                if nxt in ('で',):
                    raise ValueError('何で は {何|なん}で / {何|なに}で と明示してください')
                rd = 'なに' if nxt[:1] in ('を', 'が', 'も', 'か', 'に', 'や') else 'なん'
            else:
                rd = kata2hira(t.reading if t.reading and t.reading != '*' else s)
                if s in ('行く', '行き', '行っ', '行け', '行こ') and t.base_form == '行う':
                    rd = rd.replace('おこな', 'い')
                if s.startswith('来') and t.base_form == '来る' and rd.startswith('きた'):
                    rd = 'こ' + rd[2:]
                if s.startswith('怒') and rd.startswith('いか'):
                    rd = 'おこ' + rd[2:]
                if s.startswith('過') and rd.startswith('よぎ'):
                    rd = 'す' + rd[2:]
                if s.startswith('日本') and rd.startswith('にっぽん'):
                    rd = 'にほん' + rd[4:]
                if s in ('重ね', '重ねて', '重ねる', '重ねた') and rd.startswith('おも'):
                    rd = 'かさ' + rd[2:]
            al = _align(s, rd)
            if al is None:
                out.append(_ruby(s, rd))
            else:
                for txt, rt in al:
                    out.append(_ruby(txt, rt) if rt else txt)
        out.append(trail)
    return ''.join(out)

def R(text, skip_u=False):
    if text is None:
        return ''
    result = []
    in_u = False
    def rep_out(src, old, new):
        return re.sub(r'(?<![{|])' + re.escape(old), new, src)
    text = rep_out(text, '一人', '{一人|ひとり}')
    text = rep_out(text, '二人', '{二人|ふたり}')
    text = rep_out(text, '誕生日', '{誕生日|たんじょうび}')
    text = rep_out(text, '運転手', '{運転手|うんてんしゅ}')
    text = rep_out(text, '二階建て', '{二階建て|にかいだて}')
    text = rep_out(text, 'お土産', '{お土産|おみやげ}')
    text = rep_out(text, '一生懸命', '{一生懸命|いっしょうけんめい}')
    text = rep_out(text, '一日中', '{一日中|いちにちじゅう}')
    text = rep_out(text, '世の中', '{世|よ}の{中|なか}')
    text = rep_out(text, '使い方', '{使|つか}い{方|かた}')
    text = rep_out(text, 'やり方', 'やり{方|かた}')
    text = rep_out(text, '考え方', '{考|かんが}え{方|かた}')
    text = rep_out(text, '働き方', '{働|はたら}き{方|かた}')
    text = rep_out(text, '生き方', '{生|い}き{方|かた}')
    text = rep_out(text, '書き方', '{書|か}き{方|かた}')
    text = rep_out(text, '読み方', '{読|よ}み{方|かた}')
    text = rep_out(text, '作り方', '{作|つく}り{方|かた}')
    text = rep_out(text, '話し方', '{話|はな}し{方|かた}')
    text = rep_out(text, '選び方', '{選|えら}び{方|かた}')
    text = rep_out(text, '見方', '{見方|みかた}')
    text = rep_out(text, '味方', '{味方|みかた}')
    text = rep_out(text, '夕方', '{夕方|ゆうがた}')
    text = rep_out(text, '方法', '{方法|ほうほう}')
    text = rep_out(text, '方向', '{方向|ほうこう}')
    text = rep_out(text, '方針', '{方針|ほうしん}')
    text = rep_out(text, '方式', '{方式|ほうしき}')
    text = rep_out(text, '両方', '{両方|りょうほう}')
    text = rep_out(text, '一方', '{一方|いっぽう}')
    text = rep_out(text, 'した方がいい', 'した{方|ほう}がいい')
    text = rep_out(text, 'する方がいい', 'する{方|ほう}がいい')
    text = rep_out(text, 'ない方がいい', 'ない{方|ほう}がいい')
    text = rep_out(text, 'の方が', 'の{方|ほう}が')
    text = rep_out(text, '空き家', '{空|あ}き{家|や}')
    text = rep_out(text, '空き時間', '{空|あ}き{時間|じかん}')
    text = rep_out(text, '空き部屋', '{空|あ}き{部屋|べや}')
    text = rep_out(text, '青空', '{青空|あおぞら}')
    text = rep_out(text, '夜空', '{夜空|よぞら}')
    text = rep_out(text, '空気', '{空気|くうき}')
    text = rep_out(text, '空港', '{空港|くうこう}')
    text = rep_out(text, '空想', '{空想|くうそう}')
    text = rep_out(text, '空間', '{空間|くうかん}')
    text = rep_out(text, '空欄', '{空欄|くうらん}')
    text = re.sub(r'の日(?![本曜記常頃付])', 'の{日|ひ}', text)
    tokens = re.split(r'(<[^>]+>|\{[^{}|]+\|[^{}|]+\})', text)
    for tk in tokens:
        if not tk:
            continue
        if tk.startswith('<'):
            if tk.lower() == '<u>': in_u = True
            elif tk.lower() == '</u>': in_u = False
            result.append(tk)
        elif tk.startswith('{') and _EXPL.fullmatch(tk):
            b, r = _EXPL.fullmatch(tk).groups()
            result.append(b if (skip_u and in_u) else _ruby(b, r))
        else:
            result.append(tk if (skip_u and in_u) else _ruby_text(tk))
    return ''.join(result)

def P(html):
    if html is None:
        return ''
    s = re.sub(r'<rt>.*?</rt>', '', str(html), flags=re.S)
    s = re.sub(r'<[^>]+>', '', s)
    s = _EXPL.sub(lambda m: m.group(1), s)
    return s

def strip_markers(text):
    return P(text)

def lint_ruby(html, allow_in=('u',)):
    s = re.sub(r'<ruby>.*?</ruby>', '', html or '', flags=re.S)
    s = re.sub(r'<[^>]+>', '', s)
    return KANJI.findall(s)

def balanced_targets(n, seed=0):
    rng = random.Random(seed)
    seq = []
    while len(seq) < n:
        blk = [0, 1, 2, 3]
        rng.shuffle(blk)
        while len(seq) >= 2 and seq[-1] == seq[-2] == blk[0]:
            rng.shuffle(blk)
        seq.extend(blk)
    return seq[:n]

def balanced_targets_by_group(groups, seed=0):
    rng = random.Random(seed)
    idx_by_g = {}
    for i, g in enumerate(groups):
        idx_by_g.setdefault(g, []).append(i)
    out = [None] * len(groups)
    for g, idxs in idx_by_g.items():
        t = balanced_targets(len(idxs), seed=rng.randint(0, 10**9))
        for i, v in zip(idxs, t):
            out[i] = v
    for _ in range(50):
        changed = False
        for i in range(2, len(out)):
            if out[i] == out[i - 1] == out[i - 2]:
                for j in range(i + 1, len(out)):
                    if out[j] != out[i] and groups[j] == groups[i] and out[i - 1] != out[j] and (j + 1 >= len(out) or out[j + 1] != out[i]):
                        out[i], out[j] = out[j], out[i]; changed = True; break
        if not changed:
            break
    return out

def place_choices(correct, distractors, target, rng):
    ds = list(dict.fromkeys(d for d in distractors if d != correct))
    if len(ds) != 3:
        raise ValueError(f'need exactly 3 unique distractors != correct: {correct} {distractors}')
    rng.shuffle(ds)
    ch = ds[:target] + [correct] + ds[target:]
    assert ch[target] == correct and len(set(ch)) == 4
    return ch, target

SENSITIVE = [
    '戦争', '戦時', '戦前', '戦後', '兵', '軍', '徴兵', '空襲', '原爆', '特攻', '植民地', '占領', '慰安婦', '強制', '南京',
    '領土', '尖閣', '竹島', '北方領土', '制裁', '紛争', '侵略', '政治', '政党', '選挙', '首相', '大統領', '大臣', '議員', '汚職',
    '賄賂', '犯人', '犯罪', '殺', '自殺', '死ぬ', '死んだ', '暴力', 'いじめ', '差別', '嘘つき', 'ケチ', '嫌われ', '悪口', '信用できない',
    '仲間外れ', '核', 'デモ', '革命', '独裁', '宗教', '天皇', '憲法', '外交', '国会', '首都圏攻撃', 'テロ', '爆弾', '拳銃', '銃', '刀',
    '公式', '準拠', 'Google', 'Neural2', 'Zoom', 'LINE', 'YouTube', 'SNS', 'Instagram', 'Twitter', 'Facebook', 'Amazon', 'Netflix', 'TikTok',
    'タッパー', 'バンドエイド', '宅急便', 'ウォシュレット',
]

def sensitive_hits(text):
    t = P(text)
    return [w for w in SENSITIVE if w in t]

def write_js(path, header_lines, assigns, tail=''):
    out = [f'// {h}' for h in header_lines]
    for name, obj in assigns:
        out.append(f'window.{name} = ' + json.dumps(obj, ensure_ascii=False, indent=2) + ';')
        out.append('')
    if tail:
        out.append(tail)
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + ('\n' if not out[-1].endswith('\n') else ''))
