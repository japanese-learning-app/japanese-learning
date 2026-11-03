# -*- coding: utf-8 -*-
"""
N5 content rewrite helper library.

* R(text)            : plain Japanese (+ optional {漢字|よみ} overrides) -> <ruby> HTML
* P(html)            : strip ruby/tags -> plain text
* lint_ruby(html)    : list kanji that are NOT covered by <ruby>
* place_choices(...) : put the correct answer at a target index (safe shuffle)
* balanced_targets() : answer positions 0-3, balanced, never 3-in-a-row
* sensitive_hits(t)  : banned (political / war / hostile) vocabulary scan
* write_js(...)      : dump as `window.NAME = <json>;`

Ruby policy
-----------
* Everything is annotated automatically with Janome, then PATCHED by hand-verified rules
  (counters, 後->あと, 一人/二人, N日, 何+counter, 来る ...).
* Ambiguous kanji MUST be annotated explicitly with {漢字|よみ}; R() raises otherwise:
      辛 開 空 方 生 何(+で)  一日/１日/1日  and Arabic-digit + 日/人 for 1-2 people etc.
  e.g.  {辛|から}い  /  {辛|つら}い  /  窓が{開|あ}く  /  会を{開|ひら}く  /  {方|かた}  /  {方|ほう}
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
    # kanji numeral up to 999
    n, cur = 0, 0
    for c in s:
        if c in _KNUM:
            cur = cur * 10 + _KNUM[c] if False else _KNUM[c]
        elif c == '十':
            n += (cur or 1) * 10; cur = 0
        elif c == '百':
            n += (cur or 1) * 100; cur = 0
    return n + cur

_DIG = ['れい', 'いち', 'に', 'さん', 'よん', 'ご', 'ろく', 'なな', 'はち', 'きゅう']

def num_reading(n, last='std'):
    """n -> hiragana. last: 'std' | 'yo'(4=よ) | 'shichi'(7) | 'ku'(9=く) | 'geminate'(1,6,8,10 sokuon)"""
    if n == 0:
        return 'れい'
    parts = []
    h, t, u = n // 100, (n // 10) % 10, n % 10
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
        parts[-1] = parts[-1].replace('じゅっ', 'じゅっ')
    return ''.join(parts)

# counters: name -> function(n) -> (full reading incl. numeral, counter-only reading)
def _counter(name, n):
    """Return (full, counter_only) hiragana or raise ValueError."""
    q = n is None  # 何
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
        if u == 0 and n >= 10:  # 10, 20 ... じゅっぷん
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
    if name in ('円', '番', '年', '枚', '台', '度', '号', '才'):
        base = {'円': 'えん', '番': 'ばん', '年': 'ねん', '枚': 'まい', '台': 'だい', '度': 'ど', '号': 'ごう', '才': 'さい'}[name]
        if q: return 'なん' + base, base
        mode = 'yo' if n % 10 == 4 and name in ('円', '年') else ('shichi' if n % 10 == 7 and name == '年' else 'std')
        if name == '年' and n % 10 == 9: mode = 'ku'
        if name == '円' and n % 10 == 9: mode = 'std'
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

_COUNTERS = ['時間', '週間', '時', '分', '日', '人', '歳', '月', '円', '本', '枚', '冊', '個', '回', '階', '番', '台', '匹', '杯', '年', '度', '号', '才', 'つ']
_NUM_RE = r'(?:[0-9０-９]+|[〇一二三四五六七八九十百]+|何)'
_CNT_RE = re.compile('(' + _NUM_RE + ')(' + '|'.join(_COUNTERS) + ')')

# 日曜日・日本 など「日」で始まる語の誤爆防止、数詞+年/月/日 の複合名詞の直後文字チェック
_NOT_COUNTER_FOLLOW = {
    '日': '曜本',      # 一日曜 ... (unlikely) / 三日本 ...
    '月': '曜',        # 月曜日
    '年': '生',        # 一年生 -> OK as 年 counter (いちねんせい) but handled by Janome? keep as counter
    '本': '当人語',    # 一本当 / 三本人 (rare)
    '時': '々計代間',  # 時々 時計 時代 時間 (時間 handled above)
    '分': '別野',      # 分別 (rare)
    '人': '気形',      # 二人気 (rare)
    '台': '所',        # 台所 (一台所 rare)
    '番': '組',
}

# ---------------------------------------------------------------- strict ambiguous kanji
STRICT = {
    '辛': '辛い: {辛|から}い(味覚) か {辛|つら}い(つらい) を明示',
    '開': '開く/開ける: {開|あ}く・{開|あ}ける(ドア・窓・目) か {開|ひら}く(会・店) を明示',
    '空': '空: {空|あ}く / {空|す}く / {空|そら} / {空|から} を明示',
    '方': '方: {方|かた} か {方|ほう} を明示',
    '生': '生: {生|う}まれる/{生|な}ま/{生|せい}(学生は一語で自動) を明示',
}

_EXPL = re.compile(r'\{([^{}|]+)\|([^{}|]+)\}')

def _align(surface, reading):
    """Split surface into [(text, rt or None)] with okurigana aligned. None if impossible."""
    runs = re.findall(r'[\u4e00-\u9fff々〆ヶ]+|[^\u4e00-\u9fff々〆ヶ]+', surface)
    pat = ''
    for r in runs:
        if HAS_KANJI(r[0]):
            pat += '(.+?)'
        else:
            pat += re.escape(kata2hira(r))
    m = re.fullmatch(pat, reading)
    if not m:
        return None
    out, gi = [], 1
    for r in runs:
        if HAS_KANJI(r[0]):
            out.append((r, m.group(gi))); gi += 1
        else:
            out.append((r, None))
    return out

_FIX_SURFACE = {  # surface -> hiragana reading (hand verified)
    '後': 'あと', '今日': 'きょう', '昨日': 'きのう', '明日': 'あした', '今朝': 'けさ', '今年': 'ことし',
    '去年': 'きょねん', '来年': 'らいねん', '来週': 'らいしゅう', '毎朝': 'まいあさ', '毎晩': 'まいばん',
    '毎日': 'まいにち', '毎週': 'まいしゅう', '毎月': 'まいつき', '毎年': 'まいとし', '大人': 'おとな',
    '上手': 'じょうず', '下手': 'へた', '友達': 'ともだち', '果物': 'くだもの', '眼鏡': 'めがね', '景色': 'けしき',
    '部屋': 'へや', 'お母さん': 'おかあさん', 'お父さん': 'おとうさん', '兄弟': 'きょうだい',
    '一緒': 'いっしょ', '八百屋': 'やおや', '二十歳': 'はたち', '今晩': 'こんばん', '今夜': 'こんや',
    '今月': 'こんげつ', '今週': 'こんしゅう', '先週': 'せんしゅう', '先月': 'せんげつ', '来月': 'らいげつ',
    '一人': 'ひとり', '二人': 'ふたり', '午前': 'ごぜん', '午後': 'ごご', '何': None,  # 何 handled in context
    '外国': 'がいこく', '日本': 'にほん', '日本語': 'にほんご', '日本人': 'にほんじん', '日本料理': 'にほんりょうり',
    '中': None, '人': None, '日': None,
}
_FIX_SURFACE = {k: v for k, v in _FIX_SURFACE.items() if v}

def _ruby_text(seg):
    """Auto ruby for one tag-free segment (no explicit markers inside)."""
    # 1. numerals + counters first (protect with placeholders)
    holders = []
    def _cnt(m):
        num, cnt = m.group(1), m.group(2)
        # avoid false positives: 日本, 日曜, 月曜, 時々, 時計 ...
        nxt = seg[m.end():m.end() + 1]
        if cnt in _NOT_COUNTER_FOLLOW and nxt and nxt in _NOT_COUNTER_FOLLOW[cnt] and not (cnt == '年' and nxt == '生'):
            return m.group(0)
        # 一日中・一日おき: need explicit
        n = parse_num(num)
        is_arabic = num.translate(_ZEN).isdigit()
        if cnt == 'つ' and is_arabic:
            return m.group(0)            # '２つ' has no kanji -> no ruby
        if cnt == '分' and not is_arabic and num != '何':
            raise ValueError(f'{num}分 は {{{num}分|じゅっぷん}} / {{{num}分|じゅうぶん}} など明示してください')
        full, only = _counter(cnt, n)
        if is_arabic and cnt == '日' and only != 'にち':
            html = _ruby(num + cnt, full)   # 3日 -> みっか etc. (digit is part of the reading)
        elif is_arabic:
            html = num + _ruby(cnt, only)
        else:
            html = _ruby(num + cnt, full)
        holders.append(html)
        return f'\uE000{len(holders) - 1}\uE001'
    # 何 + counter and numerals; skip 'つ' unless kanji numeral
    seg2 = _CNT_RE.sub(_cnt, seg)
    # 2. tokenize remaining
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
                # bare single kanji or kanji+okurigana (辛い, 開ける, 方, 生まれる ...): reading depends on context
                if not (k0 == '生' and s in ('生徒', '学生', '先生')):
                    raise ValueError(f'曖昧な漢字「{s}」は明示が必要: {STRICT[k0]}  (text: …{part[max(0,part.find(s)-6):part.find(s)+8]}…)')
            if s in _FIX_SURFACE:
                rd = _FIX_SURFACE[s]
            elif s == '何':
                nxt = toks[i + 1].surface if i + 1 < len(toks) else ''
                if nxt in ('で',):
                    raise ValueError('何で は {何|なん}で / {何|なに}で と明示してください')
                rd = 'なに' if nxt[:1] in ('を', 'が', 'も', 'か', 'に', 'や') else 'なん'
                # 何も / 何か / 何を / 何が / 何に -> なに;  何です / 何の / 何時 -> なん
            else:
                rd = kata2hira(t.reading if t.reading and t.reading != '*' else s)
                if s[0] == '行' and t.base_form == '行う':      # 行って/行き... are always 行く at N5 (Janome sometimes picks 行う)
                    rd = rd.replace('おこな', 'い')
            al = _align(s, rd)
            if al is None:
                out.append(_ruby(s, rd))
            else:
                for txt, rt in al:
                    out.append(_ruby(txt, rt) if rt else txt)
        out.append(trail)
    return ''.join(out)

def R(text, skip_u=False):
    """Plain text with optional {漢字|よみ} -> ruby HTML. Existing HTML tags (u, strong, br, span) pass through.
    skip_u=True: text inside <u>…</u> gets NO ruby (kanji-reading questions: the underlined target must not be spoiled)."""
    if text is None:
        return ''
    result = []
    in_u = False
    # split on tags and explicit annotations
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
    """Plain text: remove <rt>…</rt>, tags and {x|y} markers (keeps base)."""
    if html is None:
        return ''
    s = re.sub(r'<rt>.*?</rt>', '', str(html), flags=re.S)
    s = re.sub(r'<[^>]+>', '', s)
    s = _EXPL.sub(lambda m: m.group(1), s)
    return s

def strip_markers(text):
    """Source text (with {x|y}) -> plain display text."""
    return P(text)

def lint_ruby(html, allow_in=('u',)):
    """Return list of kanji that sit outside <ruby>…</ruby> (rt content excluded)."""
    s = re.sub(r'<ruby>.*?</ruby>', '', html or '', flags=re.S)
    s = re.sub(r'<[^>]+>', '', s)
    return KANJI.findall(s)

# ---------------------------------------------------------------- quiz helpers
def balanced_targets(n, seed=0):
    """List of n target indices 0-3: each block of 4 is a permutation -> max run 2, each ~25%."""
    rng = random.Random(seed)
    seq = []
    while len(seq) < n:
        blk = [0, 1, 2, 3]
        rng.shuffle(blk)
        # avoid a run of 3 across the block boundary
        while len(seq) >= 2 and seq[-1] == seq[-2] == blk[0]:
            rng.shuffle(blk)
        seq.extend(blk)
    return seq[:n]

def balanced_targets_by_group(groups, seed=0):
    """groups: list of group ids (one per item, in item order). Positions are balanced WITHIN each group
    (blocks of 4 per group) and no 3-in-a-row globally. Returns list of targets in item order."""
    rng = random.Random(seed)
    idx_by_g = {}
    for i, g in enumerate(groups):
        idx_by_g.setdefault(g, []).append(i)
    out = [None] * len(groups)
    for g, idxs in idx_by_g.items():
        t = balanced_targets(len(idxs), seed=rng.randint(0, 10**9))
        for i, v in zip(idxs, t):
            out[i] = v
    # global fix: break runs of 3 by swapping targets between same-group items (keeps balance) or by a swap of positions
    for _ in range(50):
        changed = False
        for i in range(2, len(out)):
            if out[i] == out[i - 1] == out[i - 2]:
                # find j > i with different value to swap within the same group if possible
                for j in range(i + 1, len(out)):
                    if out[j] != out[i] and groups[j] == groups[i] and out[i - 1] != out[j] and (j + 1 >= len(out) or out[j + 1] != out[i]):
                        out[i], out[j] = out[j], out[i]; changed = True; break
        if not changed:
            break
    return out

def place_choices(correct, distractors, target, rng):
    """Return (choices, answer_index) with `correct` at index `target`. distractors must be 3 unique values != correct."""
    ds = list(dict.fromkeys(d for d in distractors if d != correct))
    if len(ds) != 3:
        raise ValueError(f'need exactly 3 unique distractors != correct: {correct} {distractors}')
    rng.shuffle(ds)
    ch = ds[:target] + [correct] + ds[target:]
    assert ch[target] == correct and len(set(ch)) == 4
    return ch, target

# ---------------------------------------------------------------- sensitivity scan
SENSITIVE = [
    '戦争', '戦時', '戦前', '戦後', '兵', '軍', '徴兵', '空襲', '原爆', '特攻', '植民地', '占領', '慰安婦', '強制', '南京',
    '領土', '尖閣', '竹島', '北方領土', '制裁', '紛争', '侵略', '政治', '政党', '選挙', '首相', '大統領', '大臣', '議員', '汚職',
    '賄賂', '犯人', '犯罪', '殺', '死ぬ', '死んだ', '暴力', 'いじめ', '差別', '嘘つき', 'ケチ', '嫌われ', '悪口', '信用できない',
    '仲間外れ', '核', 'デモ', '革命', '独裁', '宗教', '天皇', '憲法', '外交', '国会', '首都圏攻撃', 'テロ', '爆弾', '拳銃', '銃', '刀',
]

def sensitive_hits(text):
    t = P(text)
    return [w for w in SENSITIVE if w in t]

# ---------------------------------------------------------------- output
def write_js(path, header_lines, assigns, tail=''):
    """assigns: list of (name, obj). Writes JSON with 2-space indent, matching the existing file style."""
    out = [f'// {h}' for h in header_lines]
    for name, obj in assigns:
        out.append(f'window.{name} = ' + json.dumps(obj, ensure_ascii=False, indent=2) + ';')
        out.append('')
    if tail:
        out.append(tail)
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + ('\n' if not out[-1].endswith('\n') else ''))

if __name__ == '__main__':
    tests = [
        '{明日|あした}は友達と一緒に来なければなりません。',
        'この後、{三人|さんにん}で何人来ますか。',
        '{二人|ふたり}で10時に会います。',
        '今日は10時15分に駅で会います。３日前に来た。',
        '{辛|から}いカレーを食べた。窓を{開|あ}けて、会議を{開|ひら}く。',
        '毎日、何時に寝ますか。何を食べますか。何ですか。',
        'お母さんは台所で料理をしています。',
    ]
    for t in tests:
        try:
            print(t, '\n  ->', R(t))
        except Exception as e:
            print(t, '\n  ERR', e)
