#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path
from janome.tokenizer import Tokenizer

ROOT = Path("/Users/yamauchimiku/Documents/GitHub/japanese-learning")
tokenizer = Tokenizer()

def kata_to_hira(s: str) -> str:
    return ''.join(chr(ord(c) - 0x60) if 'ァ' <= c <= 'ヶ' else c for c in s)

# Multi-reading / compound / business keigo overrides (applied before or during tokenization)
PRE_OVERRIDES = [
    ("表・裏", "<ruby>表<rt>おもて</rt></ruby>・<ruby>裏<rt>うら</rt></ruby>"),
    ("表・日常", "<ruby>表<rt>おもて</rt></ruby>・<ruby>日常<rt>にちじょう</rt></ruby>"),
    ("裏・敬語", "<ruby>裏<rt>うら</rt></ruby>・<ruby>敬語<rt>けいご</rt></ruby>"),
    ("表：", "<ruby>表<rt>おもて</rt></ruby>："),
    ("裏：", "<ruby>裏<rt>うら</rt></ruby>："),
    ("何て言", "<ruby>何<rt>なん</rt></ruby>て<ruby>言<rt>い</rt></ruby>"),
    ("何と言", "<ruby>何<rt>なん</rt></ruby>と<ruby>言<rt>い</rt></ruby>"),
    ("日本", "<ruby>日本<rt>にほん</rt></ruby>"),
    ("1つ目", "1つ<ruby>目<rt>め</rt></ruby>"),
    ("2つ目", "2つ<ruby>目<rt>め</rt></ruby>"),
    ("3つ目", "3つ<ruby>目<rt>め</rt></ruby>"),
    ("目を通", "<ruby>目<rt>め</rt></ruby>を<ruby>通<rt>とお</rt></ruby>"),
    ("目上", "<ruby>目上<rt>めうえ</rt></ruby>"),
    ("何名様", "<ruby>何名様<rt>なんめいさま</rt></ruby>"),
    ("何名", "<ruby>何名<rt>なんめい</rt></ruby>"),
    ("何時頃", "<ruby>何時頃<rt>なんじごろ</rt></ruby>"),
    ("何時", "<ruby>何時<rt>なんじ</rt></ruby>"),
    ("何日", "<ruby>何日<rt>なんにち</rt></ruby>"),
    ("何分", "<ruby>何分<rt>なんぷん</rt></ruby>"),
    ("何人", "<ruby>何人<rt>なんにん</rt></ruby>"),
    ("何階", "<ruby>何階<rt>なんがい</rt></ruby>"),
    ("何泊", "<ruby>何泊<rt>なんぱく</rt></ruby>"),
    ("何様", "<ruby>何様<rt>なにさま</rt></ruby>"),
    ("何件", "<ruby>何件<rt>なんけん</rt></ruby>"),
    ("1名様", "1<ruby>名様<rt>めいさま</rt></ruby>"),
    ("2名様", "2<ruby>名様<rt>めいさま</rt></ruby>"),
    ("3名様", "3<ruby>名様<rt>めいさま</rt></ruby>"),
    ("4名様", "4<ruby>名様<rt>めいさま</rt></ruby>"),
    ("一泊", "<ruby>一泊<rt>いっぱく</rt></ruby>"),
    ("二泊", "<ruby>二泊<rt>にはく</rt></ruby>"),
    ("一日中", "<ruby>一日中<rt>いちにちじゅう</rt></ruby>"),
    ("一日", "<ruby>一日<rt>いちにち</rt></ruby>"),
    ("後ほど", "<ruby>後<rt>のち</rt></ruby>ほど"),
    ("早急に", "<ruby>早急<rt>さっきゅう</rt></ruby>に"),
    ("早急", "<ruby>早急<rt>さっきゅう</rt></ruby>"),
    ("貼付", "<ruby>貼付<rt>ちょうふ</rt></ruby>"),
    ("送付", "<ruby>送付<rt>そうふ</rt></ruby>"),
    ("進捗", "<ruby>進捗<rt>しんちょく</rt></ruby>"),
    ("御社", "<ruby>御社<rt>おんしゃ</rt></ruby>"),
    ("貴社", "<ruby>貴社<rt>きしゃ</rt></ruby>"),
    ("弊社", "<ruby>弊社<rt>へいしゃ</rt></ruby>"),
    ("当社", "<ruby>当社<rt>とうしゃ</rt></ruby>"),
    ("お体", "お<ruby>体<rt>からだ</rt></ruby>"),
    ("お身体", "お<ruby>身体<rt>からだ</rt></ruby>"),
    ("お手数", "お<ruby>手数<rt>てすう</rt></ruby>"),
    ("ご足労", "ご<ruby>足労<rt>そくろう</rt></ruby>"),
    ("ご査収", "ご<ruby>査収<rt>さしゅう</rt></ruby>"),
    ("ご高覧", "ご<ruby>高覧<rt>こうらん</rt></ruby>"),
    ("ご健勝", "ご<ruby>健勝<rt>けんしょう</rt></ruby>"),
    ("ご清栄", "ご<ruby>清栄<rt>せいえい</rt></ruby>"),
    ("ご清祥", "ご<ruby>清祥<rt>せいしょう</rt></ruby>"),
    ("ご自愛", "ご<ruby>自愛<rt>じあい</rt></ruby>"),
    ("ご笑納", "ご<ruby>笑納<rt>しょうのう</rt></ruby>"),
    ("ご海容", "ご<ruby>海容<rt>かいよう</rt></ruby>"),
    ("ご容赦", "ご<ruby>容赦<rt>ようしゃ</rt></ruby>"),
    ("ご愛顧", "ご<ruby>愛顧<rt>あいこ</rt></ruby>"),
    ("ご芳名", "ご<ruby>芳名<rt>ほうめい</rt></ruby>"),
    ("ご意向", "ご<ruby>意向<rt>いこう</rt></ruby>"),
    ("ご都合", "ご<ruby>都合<rt>つごう</rt></ruby>"),
    ("ご一緒", "ご<ruby>一緒<rt>いっしょ</rt></ruby>"),
    ("ご覧", "ご<ruby>覧<rt>らん</rt></ruby>"),
    ("お礼", "お<ruby>礼<rt>れい</rt></ruby>"),
    ("御礼", "<ruby>御礼<rt>おんれい</rt></ruby>"),
    ("お詫び", "お<ruby>詫<rt>わ</rt></ruby>び"),
    ("お尋ね", "お<ruby>尋<rt>たず</rt></ruby>ね"),
    ("お伺い", "お<ruby>伺<rt>うかが</rt></ruby>い"),
    ("伺い", "<ruby>伺<rt>うかが</rt></ruby>い"),
    ("伺う", "<ruby>伺<rt>うかが</rt></ruby>う"),
    ("伺った", "<ruby>伺<rt>うかが</rt></ruby>った"),
    ("伺って", "<ruby>伺<rt>うかが</rt></ruby>って"),
    ("承り", "<ruby>承<rt>うけたまわ</rt></ruby>り"),
    ("承る", "<ruby>承<rt>うけたまわ</rt></ruby>る"),
    ("承った", "<ruby>承<rt>うけたまわ</rt></ruby>った"),
    ("承って", "<ruby>承<rt>うけたまわ</rt></ruby>って"),
    ("存じ", "<ruby>存<rt>ぞん</rt></ruby>じ"),
    ("存じる", "<ruby>存<rt>ぞん</rt></ruby>じる"),
    ("参り", "<ruby>参<rt>まい</rt></ruby>り"),
    ("参る", "<ruby>参<rt>まい</rt></ruby>る"),
    ("参った", "<ruby>参<rt>まい</rt></ruby>った"),
    ("申し上げ", "<ruby>申<rt>もう</rt></ruby>し<ruby>上<rt>あ</rt></ruby>げ"),
    ("申し出", "<ruby>申<rt>もう</rt></ruby>し<ruby>出<rt>で</rt></ruby>"),
    ("申し込み", "<ruby>申<rt>もう</rt></ruby>し<ruby>込<rt>こ</rt></ruby>み"),
    ("申込", "<ruby>申込<rt>もうしこみ</rt></ruby>"),
    ("申し", "<ruby>申<rt>もう</rt></ruby>し"),
    ("申さ", "<ruby>申<rt>もう</rt></ruby>さ"),
    ("申す", "<ruby>申<rt>もう</rt></ruby>す"),
    ("折り返し", "<ruby>折<rt>お</rt></ruby>り<ruby>返<rt>かえ</rt></ruby>し"),
    ("お取り次ぎ", "お<ruby>取<rt>と</rt></ruby>り<ruby>次<rt>つ</rt></ruby>ぎ"),
    ("取り次ぎ", "<ruby>取<rt>と</rt></ruby>り<ruby>次<rt>つ</rt></ruby>ぎ"),
    ("お預かり", "お<ruby>預<rt>あず</rt></ruby>かり"),
    ("お控え", "お<ruby>控<rt>ひか</rt></ruby>え"),
    ("お差し支え", "お<ruby>差<rt>さ</rt></ruby>し<ruby>支<rt>つか</rt></ruby>え"),
    ("差し支え", "<ruby>差<rt>さ</rt></ruby>し<ruby>支<rt>つか</rt></ruby>え"),
    ("差し上げ", "<ruby>差<rt>さ</rt></ruby>し<ruby>上<rt>あ</rt></ruby>げ"),
    ("召し上が", "<ruby>召<rt>め</rt></ruby>し<ruby>上<rt>あ</rt></ruby>が"),
    ("お召し上がり", "お<ruby>召<rt>め</rt></ruby>し<ruby>上<rt>あ</rt></ruby>がり"),
    ("受け賜", "<ruby>受<rt>う</rt></ruby>け<ruby>賜<rt>たまわ</rt></ruby>"),
    ("お目にかか", "お<ruby>目<rt>め</rt></ruby>にかか"),
    ("お見え", "お<ruby>見<rt>み</rt></ruby>え"),
    ("お越し", "お<ruby>越<rt>こ</rt></ruby>し"),
    ("お帰り", "お<ruby>帰<rt>かえ</rt></ruby>り"),
    ("お席", "お<ruby>席<rt>せき</rt></ruby>"),
    ("お名前", "お<ruby>名前<rt>なまえ</rt></ruby>"),
    ("お電話", "お<ruby>電話<rt>でんわ</rt></ruby>"),
    ("お荷物", "お<ruby>荷物<rt>にもつ</rt></ruby>"),
    ("お会計", "お<ruby>会計<rt>かいけい</rt></ruby>"),
    ("お釣り", "お<ruby>釣<rt>つ</rt></ruby>り"),
    ("お水", "お<ruby>水<rt>みず</rt></ruby>"),
    ("お湯", "お<ruby>湯<rt>ゆ</rt></ruby>"),
    ("お茶", "お<ruby>茶<rt>ちゃ</rt></ruby>"),
    ("お車", "お<ruby>車<rt>くるま</rt></ruby>"),
    ("お気をつけ", "お<ruby>気<rt>き</rt></ruby>をつけ"),
    ("立ち寄", "<ruby>立<rt>た</rt></ruby>ち<ruby>寄<rt>よ</rt></ruby>"),
    ("言い換", "<ruby>言<rt>い</rt></ruby>い<ruby>換<rt>か</rt></ruby>"),
    ("行き違", "<ruby>行<rt>ゆ</rt></ruby>き<ruby>違<rt>ちが</rt></ruby>"),
    ("入れ違", "<ruby>入<rt>い</rt></ruby>れ<ruby>違<rt>ちが</rt></ruby>"),
    ("引き継", "<ruby>引<rt>ひ</rt></ruby>き<ruby>継<rt>つ</rt></ruby>"),
    ("受け取", "<ruby>受<rt>う</rt></ruby>け<ruby>取<rt>と</rt></ruby>"),
    ("持ち帰", "<ruby>持<rt>も</rt></ruby>ち<ruby>帰<rt>かえ</rt></ruby>"),
    ("書き言葉", "<ruby>書<rt>か</rt></ruby>き<ruby>言葉<rt>ことば</rt></ruby>"),
    ("話し言葉", "<ruby>話<rt>はな</rt></ruby>し<ruby>言葉<rt>ことば</rt></ruby>"),
    ("心当たり", "<ruby>心当<rt>こころあ</rt></ruby>たり"),
    ("田中健太", "<ruby>田中<rt>たなか</rt></ruby><ruby>健太<rt>けんた</rt></ruby>"),
    ("鈴木彩", "<ruby>鈴木<rt>すずき</rt></ruby><ruby>彩<rt>あや</rt></ruby>"),
    ("中村翔", "<ruby>中村<rt>なかむら</rt></ruby><ruby>翔<rt>しょう</rt></ruby>"),
    ("高橋", "<ruby>高橋<rt>たかはし</rt></ruby>"),
    ("佐藤", "<ruby>佐藤<rt>さとう</rt></ruby>"),
    ("伊藤", "<ruby>伊藤<rt>いとう</rt></ruby>"),
    ("渡辺", "<ruby>渡辺<rt>わたなべ</rt></ruby>"),
    ("山本", "<ruby>山本<rt>やまもと</rt></ruby>"),
]

KANJI_RE = re.compile(r'[\u4e00-\u9fff\u3005]+')
COMPOUND_MID_HIRA_RE = re.compile(r'^([\u4e00-\u9fff\u3005]+)([\u3041-\u3096]+)([\u4e00-\u9fff\u3005]+)$')

def token_to_ruby(surface: str, reading_kata: str) -> str:
    if not KANJI_RE.search(surface):
        return surface
    if not reading_kata or reading_kata == '*':
        return surface
    hira = kata_to_hira(reading_kata)
    if surface == hira:
        return surface

    # Strip matching prefix kana
    s_start = 0
    h_start = 0
    while s_start < len(surface) and h_start < len(hira) and surface[s_start] == hira[h_start]:
        s_start += 1
        h_start += 1

    # Strip matching suffix kana
    s_end = len(surface)
    h_end = len(hira)
    while s_end > s_start and h_end > h_start and surface[s_end - 1] == hira[h_end - 1]:
        s_end -= 1
        h_end -= 1

    prefix = surface[:s_start]
    core_s = surface[s_start:s_end]
    suffix = surface[s_end:]
    core_h = hira[h_start:h_end]

    if not core_s or not core_h:
        return surface

    # Check if core_s is Kanji1 + mid_hira + Kanji2 (e.g., 取り次, 申し込, 受け取)
    m = COMPOUND_MID_HIRA_RE.match(core_s)
    if m:
        k1, mid_h, k2 = m.group(1), m.group(2), m.group(3)
        # Find mid_h inside core_h (at index >= 1 and leaving at least 1 char for k2)
        idx = core_h.find(mid_h, 1)
        if idx != -1 and idx + len(mid_h) < len(core_h):
            r1 = core_h[:idx]
            r2 = core_h[idx + len(mid_h):]
            return f"{prefix}<ruby>{k1}<rt>{r1}</rt></ruby>{mid_h}<ruby>{k2}<rt>{r2}</rt></ruby>{suffix}"

    return f"{prefix}<ruby>{core_s}<rt>{core_h}</rt></ruby>{suffix}"

def annotate_segment(seg: str) -> str:
    if not seg or not KANJI_RE.search(seg):
        return seg
    out = []
    for tok in tokenizer.tokenize(seg):
        out.append(token_to_ruby(tok.surface, tok.reading))
    return ''.join(out)

def annotate_text(text: str) -> str:
    if not text or not isinstance(text, str):
        return text
    if '<ruby>' in text:
        return text
    if not KANJI_RE.search(text):
        return text

    # Protect PRE_OVERRIDES using placeholders
    placeholders = []
    work = text
    for pat, rep in PRE_OVERRIDES:
        if pat in work:
            ph = f"__RBPH_{len(placeholders)}__"
            placeholders.append((ph, rep))
            work = work.replace(pat, ph)

    # Split by placeholders and HTML tags if any
    parts = re.split(r'(__RBPH_\d+__|<[^>]+>)', work)
    annotated_parts = []
    for p in parts:
        if not p:
            continue
        if p.startswith('__RBPH_') or p.startswith('<'):
            annotated_parts.append(p)
        else:
            annotated_parts.append(annotate_segment(p))

    res = ''.join(annotated_parts)
    for ph, rep in placeholders:
        res = res.replace(ph, rep)
    while re.search(r"<ruby>([^<]+)<rt>([^<]+)</rt></ruby><ruby>([^<]+)<rt>([^<]+)</rt></ruby>", res):
        res = re.sub(r"<ruby>([^<]+)<rt>([^<]+)</rt></ruby><ruby>([^<]+)<rt>([^<]+)</rt></ruby>", r"<ruby>\1\3<rt>\2\4</rt></ruby>", res)
    return res

if __name__ == '__main__':
    test_sents = [
        "企画書をお送りいたしましたが、すでにご覧になりましたでしょうか？",
        "何名様でいらっしゃいますか？お席へご案内いたします。",
        "あいにく田中は席を外しております。後ほど折り返しお電話いたします。",
        "お目にかかれるのを楽しみにしております。ご査収のほどよろしくお願い申し上げます。"
    ]
    for s in test_sents:
        print(annotate_text(s))

def build_full_ruby_dict():
    # Collect all strings from all 3 JS files + UI strings
    files = [
        ROOT / "database/business_keigo_catalog.js",
        ROOT / "database/keigo_drill_all_data.js",
        ROOT / "database/business_keigo_practice_data.js",
        ROOT / "business_keigo.html"
    ]
    string_lit_re = re.compile(r'"([^"\\]*(?:\\.[^"\\]*)*)"|\'([^\'\\]*(?:\\.[^\'\\]*)*)\'')
    all_texts = set()
    for fp in files:
        if not fp.exists():
            continue
        content = fp.read_text(encoding="utf-8")
        for m in string_lit_re.finditer(content):
            s = m.group(1) if m.group(1) is not None else m.group(2)
            # unescape \n
            s_unesc = s.replace('\\n', '\n')
            if KANJI_RE.search(s_unesc) and '<' not in s_unesc and len(s_unesc) <= 800:
                all_texts.add(s_unesc)

    sentence_map = {}
    word_map = {}

    # Seed word_map with PRE_OVERRIDES
    for k, v in PRE_OVERRIDES:
        word_map[k] = v

    for txt in sorted(all_texts):
        annotated = annotate_text(txt)
        if annotated != txt:
            sentence_map[txt] = annotated
        # Also extract individual tokens for fallback word replacement
        for tok in tokenizer.tokenize(txt):
            surf = tok.surface
            if KANJI_RE.search(surf) and surf not in word_map:
                rb_tok = token_to_ruby(surf, tok.reading)
                if rb_tok != surf:
                    word_map[surf] = "<ruby>目<rt>め</rt></ruby>" if surf == "目" else rb_tok

    # Sort word_map longest key first so compound words match before single kanji
    word_list = sorted(word_map.items(), key=lambda x: (-len(x[0]), x[0]))

    out_js = (
        "// ============================================================================\n"
        "// ふりがな（ルビ）完全変換辞書 — 全データ＆動的テキスト対応\n"
        "// ============================================================================\n"
        f"window.KEIGO_SENTENCE_RUBY_MAP = {json.dumps(sentence_map, ensure_ascii=False)};\n"
        f"window.KEIGO_WORD_RUBY_LIST = {json.dumps(word_list, ensure_ascii=False)};\n"
    )
    out_path = ROOT / "database/keigo_ruby_dict.js"
    out_path.write_text(out_js, encoding="utf-8")
    print(f"Generated {out_path}: {len(sentence_map)} sentences, {len(word_list)} unique kanji tokens.")

if __name__ == '__main__':
    build_full_ruby_dict()
