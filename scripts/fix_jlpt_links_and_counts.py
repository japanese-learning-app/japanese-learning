#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_jlpt_links_and_counts.py

1. Corrects level-specific titles, badges, links, counts, and localStorage keys across all JLPT files.
2. Appends cache-busting timestamp (?v=20261102_1930) to database scripts.
3. Improves ruby rendering line-height and furigana persistence in vocab flashcards.
"""

import os
import re

CACHE_VER = "20261102_1930"

COUNTS = {
    "n1": {
        "level_upper": "N1",
        "grammar_points": 127,
        "grammar_units": 11,
        "grammar_quiz": 508,
        "vocab_count": "3,747",
        "vocab_quiz": 500,
    },
    "n2": {
        "level_upper": "N2",
        "grammar_points": 195,
        "grammar_units": 17,
        "grammar_quiz": "1,507",
        "vocab_count": "3,436",
        "vocab_quiz": 896,
    },
    "n3": {
        "level_upper": "N3",
        "grammar_points": 182,
        "grammar_units": 16,
        "grammar_quiz": 728,
        "vocab_count": "1,841",
        "vocab_quiz": 500,
    },
    "n4": {
        "level_upper": "N4",
        "grammar_points": 62,
        "grammar_units": 7,
        "grammar_quiz": 248,
        "vocab_count": "668",
        "vocab_quiz": 365,
    },
    "n5": {
        "level_upper": "N5",
        "grammar_points": 46,
        "grammar_units": 5,
        "grammar_quiz": 184,
        "vocab_count": "702",
        "vocab_quiz": 371,
    }
}

def fix_vocab_cards():
    for lvl, info in COUNTS.items():
        fname = f"jlpt_{lvl}_vocab_cards.html"
        if not os.path.exists(fname):
            continue
        with open(fname, "r", encoding="utf-8") as f:
            c = f.read()

        u = info["level_upper"]
        v_quiz = info["vocab_quiz"]
        v_count = info["vocab_count"]

        # 1. Update Title & Header Links
        c = re.sub(
            r'href="jlpt_n\d_vocab_quiz\.html"\s+class="px-2\.5 py-1\.5 rounded-xl bg-white/25 hover:bg-white/35[^"]*"\s+title="[^"]*"',
            f'href="jlpt_{lvl}_vocab_quiz.html" class="px-2.5 py-1.5 rounded-xl bg-white/25 hover:bg-white/35 text-white transition flex items-center gap-1 text-xs font-bold border border-white/40 shadow-xs" title="文字・語彙穴埋め演習道場（全{v_quiz}問）へ"',
            c
        )
        c = re.sub(
            r'<span>穴埋め演習\s*\(\d+問\)\s*📝</span>',
            f'<span>穴埋め演習 ({v_quiz}問) 📝</span>',
            c
        )
        # Mid-page banner link
        c = re.sub(
            r'<!-- 穴埋め演習道場[^\n]*-->\s*<div[^>]*>\s*<div[^>]*>\s*<span[^>]*>[^<]*<\/span>\s*<span[^>]*>[^<]*<\/span>\s*<\/div>\s*<a href="jlpt_n\d_vocab_quiz\.html"[^>]*>\s*<span>\d+問道場へ<\/span>',
            f'<!-- 穴埋め演習道場（全{v_quiz}問）誘導バナー -->\n      <div class="mb-4 p-3 rounded-2xl bg-white border border-lightBlue/30 shadow-xs flex items-center justify-between gap-3">\n        <div class="flex items-center gap-2">\n          <span class="px-2 py-0.5 rounded-lg bg-softTeal text-white font-extrabold text-[10px] tracking-wide shrink-0">演習</span>\n          <span class="text-xs font-bold text-darkNavyText">全{v_quiz}問の実戦穴埋め問題に挑戦する</span>\n        </div>\n        <a href="jlpt_{lvl}_vocab_quiz.html" class="px-3 py-1.5 rounded-xl bg-deepNavy hover:bg-slate-800 text-white font-bold text-xs flex items-center gap-1 shrink-0 transition shadow-xs" style="text-decoration:none;">\n          <span>{v_quiz}問道場へ</span>',
            c
        )

        # 2. Footer
        c = re.sub(
            r'JLPT N\d Vocabulary Master Flashcards',
            f'JLPT {u} Vocabulary Master Flashcards',
            c
        )

        # 3. LocalStorage keys
        c = c.replace("localStorage.getItem('jlpt_n2_card_direction')", f"localStorage.getItem('jlpt_{lvl}_card_direction')")
        c = c.replace("localStorage.setItem('jlpt_n2_card_direction'", f"localStorage.setItem('jlpt_{lvl}_card_direction'")

        # 4. Cache busting on database script
        c = re.sub(
            rf'<script src="database/jlpt_{lvl}_vocab_full_data\.js(\?v=[^"]*)?"></script>',
            f'<script src="database/jlpt_{lvl}_vocab_full_data.js?v={CACHE_VER}"></script>',
            c
        )

        # 5. Ensure #backExampleJa has generous line-height for clean ruby display
        if 'id="backExampleJa"' in c:
            c = re.sub(
                r'id="backExampleJa"\s+class="([^"]*)"',
                r'id="backExampleJa" style="line-height: 2.2;" class="\1"',
                c
            )
            # Avoid duplicate style attributes if run repeatedly
            c = re.sub(r'style="line-height: 2\.2;"\s+style="line-height: 2\.2;"', 'style="line-height: 2.2;"', c)

        # 6. Ensure furigana state persistence on load
        if "let isFuriganaOn = true;" in c:
            c = c.replace(
                "let isFuriganaOn = true;",
                "let isFuriganaOn = localStorage.getItem('jlpt_furigana_on') !== '0';"
            )
        if "function toggleFurigana() {" in c or "window.toggleFurigana = function() {" in c:
            c = re.sub(
                r'(window\.toggleFurigana\s*=\s*function\(\)\s*\{\s*isFuriganaOn\s*=\s*!isFuriganaOn;)',
                r"\1\n      localStorage.setItem('jlpt_furigana_on', isFuriganaOn ? '1' : '0');",
                c
            )

        with open(fname, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"Updated {fname}")

def fix_grammar_quizzes():
    for lvl, info in COUNTS.items():
        fname = f"jlpt_{lvl}_grammar_quiz.html"
        if not os.path.exists(fname):
            continue
        with open(fname, "r", encoding="utf-8") as f:
            c = f.read()

        u = info["level_upper"]
        g_quiz = info["grammar_quiz"]
        v_quiz = info["vocab_quiz"]
        v_count = info["vocab_count"]

        # Title
        c = re.sub(
            r'<title>JLPT N\d 文法 マスター[^\n<]*<\/title>',
            f'<title>JLPT {u} 文法穴埋めマスター — 全{g_quiz}問 4択練習道場</title>',
            c
        )

        # Badge
        c = re.sub(
            r'<span class="badge-n\d">N\d レベル<\/span>',
            f'<span class="badge-{lvl}">{u} レベル</span>',
            c
        )

        # Header buttons
        c = re.sub(
            r'<a href="jlpt_n\d_vocab_quiz\.html"\s+class="header-btn"\s+title="[^"]*">\s*📝\s*語彙穴埋め[^\n<]*<\/a>',
            f'<a href="jlpt_{lvl}_vocab_quiz.html" class="header-btn" title="{u}語彙穴埋め演習道場（全{v_quiz}問）へ">\n        📝 語彙穴埋め ({v_quiz}問)\n      </a>',
            c
        )
        c = re.sub(
            r'<a href="jlpt_n\d_vocab_cards\.html"\s+class="header-btn"\s+title="[^"]*">\s*🎴\s*語彙カード\s*<\/a>',
            f'<a href="jlpt_{lvl}_vocab_cards.html" class="header-btn" title="{u}語彙フラッシュカード（全{v_count}語）へ">\n        🎴 語彙カード\n      </a>',
            c
        )

        # Footer
        c = re.sub(
            r'JLPT N\d Grammar Master Study App',
            f'JLPT {u} Grammar Master Study App',
            c
        )

        # Window variable references
        if lvl != "n2":
            c = c.replace("window.JLPT_N2_QUIZ_DATA", f"window.JLPT_{u}_QUIZ_DATA")
            c = c.replace("window.JLPT_N2_VOCAB_DATA", f"window.JLPT_{u}_VOCAB_DATA")
            c = c.replace("database/jlpt_n2_vocab_full_data.js", f"database/jlpt_{lvl}_vocab_full_data.js")

        # Cache buster
        c = re.sub(
            rf'<script src="database/jlpt_{lvl}_grammar_quiz_data\.js(\?v=[^"]*)?"></script>',
            f'<script src="database/jlpt_{lvl}_grammar_quiz_data.js?v={CACHE_VER}"></script>',
            c
        )
        c = re.sub(
            rf'<script src="database/jlpt_{lvl}_vocab_full_data\.js(\?v=[^"]*)?"',
            f'<script src="database/jlpt_{lvl}_vocab_full_data.js?v={CACHE_VER}"',
            c
        )

        with open(fname, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"Updated {fname}")

def fix_vocab_quizzes():
    for lvl, info in COUNTS.items():
        fname = f"jlpt_{lvl}_vocab_quiz.html"
        if not os.path.exists(fname):
            continue
        with open(fname, "r", encoding="utf-8") as f:
            c = f.read()

        u = info["level_upper"]
        v_quiz = info["vocab_quiz"]
        g_quiz = info["grammar_quiz"]

        # Title
        c = re.sub(
            r'<title>JLPT N\d 文字・語彙 穴埋めマスター[^\n<]*<\/title>',
            f'<title>JLPT {u} 文字・語彙 穴埋めマスター — 全{v_quiz}問 4択練習道場</title>',
            c
        )

        # Brand header
        c = re.sub(
            r'<span>JLPT N\d 文字・語彙 穴埋めマスター<\/span>',
            f'<span>JLPT {u} 文字・語彙 穴埋めマスター</span>',
            c
        )
        c = re.sub(
            r'<span class="badge-n\d">全\d+問<\/span>',
            f'<span class="badge-{lvl}">全{v_quiz}問</span>',
            c
        )

        # Header grammar link
        c = re.sub(
            r'<a href="jlpt_n\d_grammar_quiz\.html"\s+class="header-btn"\s+title="[^"]*">',
            f'<a href="jlpt_{lvl}_grammar_quiz.html" class="header-btn" title="{u}文法穴埋め演習道場（全{g_quiz}問）へ">',
            c
        )

        # Script tags cache buster
        c = re.sub(
            rf'<script src="database/jlpt_{lvl}_vocab_quiz_data\.js(\?v=[^"]*)?"><\/script>',
            f'<script src="database/jlpt_{lvl}_vocab_quiz_data.js?v={CACHE_VER}"></script>',
            c
        )

        # Internal JS references
        if lvl != "n2":
            c = c.replace("window.JLPT_N2_VOCAB_DATA", f"window.JLPT_{u}_VOCAB_DATA")
            c = c.replace("database/jlpt_n2_vocab_full_data.js", f"database/jlpt_{lvl}_vocab_full_data.js")

        with open(fname, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"Updated {fname}")

def fix_jlpt_practice():
    fname = "jlpt_practice.html"
    if not os.path.exists(fname):
        return
    with open(fname, "r", encoding="utf-8") as f:
        c = f.read()

    # Update N2 vocab count to 3436
    c = c.replace("vocabCount: 3412", "vocabCount: 3436")
    c = c.replace("語彙3,412語", "語彙3,436語")

    with open(fname, "w", encoding="utf-8") as f:
        f.write(c)
    print(f"Updated {fname}")

if __name__ == "__main__":
    fix_vocab_cards()
    fix_grammar_quizzes()
    fix_vocab_quizzes()
    fix_jlpt_practice()
    print("ALL JLPT LINKS, LABELS, COUNTS, AND CACHE BUSTERS UPDATED SUCCESSFULLY!")
