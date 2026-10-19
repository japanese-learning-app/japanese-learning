#!/usr/bin/env python3
"""
Comprehensive Ruby Fixer
Corrects Japanese furigana (ruby) errors caused by naive morphological analysis:
- 今日は (erroneously read as 'こんにちは' instead of 'きょう' + 'は')
- 今日 (erroneously read as 'こんにち' in everyday sentences)
- 今日初 (erroneously read as 'きょうはつ' instead of '今日:きょう' + '初:はじ')
- 彼の / 彼は (erroneously read as 'かの', 'か' instead of 'かれ')
- 入る / 入って (erroneously read as 'いる', 'いっっ' instead of 'はいる', 'はいっ')
- 放っ (erroneously read as 'ほうっっ' with double sokuon)
- 一日 (erroneously read as 'ついたち' in duration/frequency/greeting contexts)
- 月 (erroneously read as 'がつ' in '月は地球...')
- Trapped particles & okurigana inside <ruby> tags
"""

import os
import re
import json

TARGET_FILES = [
    'database/jlpt_n2_grammar_quiz_data.js',
    'database/jlpt_n2_vocab_quiz_data.json',
    'database/jlpt_n2_vocab_quiz_data.js',
    'database/jlpt_n2_vocab_full_data.js',
    'database/kanji_daily_quiz_dataset.js',
    'database/dict_examples_map.js',
    'public/database/dict_examples_map.js',
    'js/data.js',
    'public/js/data.js'
]

def fix_rubies_in_text(text: str) -> str:
    c = text

    # 1. 今日 (Today)
    c = re.sub(r'<ruby>今日は<rt>こんにちは</rt></ruby>', '<ruby>今日<rt>きょう</rt></ruby>は', c)
    c = re.sub(r'<ruby>今日初<rt>きょうはつ</rt></ruby>めて', '<ruby>今日<rt>きょう</rt></ruby><ruby>初<rt>はじ</rt></ruby>めて', c)
    c = re.sub(r'<ruby>今日<rt>こんにち</rt></ruby>', '<ruby>今日<rt>きょう</rt></ruby>', c)

    # 2. 彼 (Pronoun 'he' / 'his')
    c = re.sub(r'<ruby>彼の<rt>かの</rt></ruby>', '<ruby>彼<rt>かれ</rt></ruby>の', c)
    c = re.sub(r'<ruby>彼<rt>か</rt></ruby>の', '<ruby>彼<rt>かれ</rt></ruby>の', c)
    c = re.sub(r'<ruby>彼<rt>か</rt></ruby>', '<ruby>彼<rt>かれ</rt></ruby>', c)
    c = re.sub(r'<ruby>彼は<rt>かれは</rt></ruby>', '<ruby>彼<rt>かれ</rt></ruby>は', c)

    # 3. 入る / 入っ / 放っ
    c = re.sub(r'<ruby>入る<rt>いる</rt></ruby>', '<ruby>入<rt>はい</rt></ruby>る', c)
    c = re.sub(r'<ruby>入っ<rt>いっっ</rt></ruby>', '<ruby>入<rt>はい</rt></ruby>っ', c)
    c = re.sub(r'<ruby>入っ<rt>いっ</rt></ruby>', '<ruby>入<rt>はい</rt></ruby>っ', c)
    c = re.sub(r'<ruby>放っ<rt>ほうっっ</rt></ruby>', '<ruby>放<rt>ほう</rt></ruby>っ', c)

    # 4. 一日 (All occurrences in these files are 'いちにち', not 1st of month)
    c = re.sub(r'<ruby>一日<rt>ついたち</rt></ruby><ruby>中<rt>ちゅう</rt></ruby>', '<ruby>一日中<rt>いちにちじゅう</rt></ruby>', c)
    c = re.sub(r'<ruby>一日<rt>ついたち</rt></ruby>', '<ruby>一日<rt>いちにち</rt></ruby>', c)

    # 5. 月 (Moon)
    c = re.sub(r'<ruby>月<rt>がつ</rt></ruby>は地球', '<ruby>月<rt>つき</rt></ruby>は地球', c)
    c = re.sub(r'<ruby>月<rt>げつ</rt></ruby>は地球', '<ruby>月<rt>つき</rt></ruby>は地球', c)

    # 6. Trapped particles
    particle_maps = [
        ('何', 'なに', ['も', 'か', 'を']),
        ('何', 'なん', ['で', 'と']),
        ('上', 'うえ', ['で', 'に', 'の']),
        ('方', 'ほう', ['が', 'を', 'の', 'に']),
        ('時', 'とき', ['に', 'の']),
        ('中', 'なか', ['に', 'の', 'で']),
        ('逆', 'ぎゃく', ['に']),
        ('同時', 'どうじ', ['に']),
        ('非常', 'ひじょう', ['に']),
        ('実際', 'じっさい', ['に']),
        ('一緒', 'いっしょ', ['に']),
        ('誰', 'だれ', ['も', 'か', 'が', 'を']),
        ('僕', 'ぼく', ['は', 'の', 'が']),
        ('気', 'き', ['が', 'を', 'に']),
        ('目', 'め', ['に', 'が', 'を']),
        ('手', 'て', ['を', 'が', 'に']),
        ('足', 'あし', ['が', 'を']),
        ('今', 'いま', ['まで']),
        ('実', 'じつ', ['は']),
        ('後', 'あと', ['で']),
        ('特', 'とく', ['に']),
        ('急', 'きゅう', ['に']),
        ('背', 'せ', ['が']),
        ('声', 'こえ', ['が']),
        ('顔', 'かお', ['が']),
        ('味', 'あじ', ['を']),
        ('他', 'ほか', ['の'])
    ]
    for kanji, reading, suffixes in particle_maps:
        for suf in suffixes:
            pat = f'<ruby>{kanji}{suf}<rt>{reading}{suf}</rt></ruby>'
            rep = f'<ruby>{kanji}<rt>{reading}</rt></ruby>{suf}'
            c = re.sub(pat, rep, c)

    c = re.sub(r'<ruby>子ども<rt>こども</rt></ruby>', '<ruby>子<rt>こ</rt></ruby>ども', c)

    # 7. Okurigana trapped inside ruby
    okuri = [
        ('向', 'む', 'か'),
        ('分', 'わ', 'か'),
        ('行', 'い', 'か'),
        ('上', 'あ', 'が'),
        ('下', 'さ', 'が'),
        ('聞', 'き', 'か'),
        ('出', 'で', 'か'),
        ('確', 'たし', 'か'),
        ('静', 'しず', 'か'),
        ('働', 'はたら', 'か'),
        ('欠', 'か', 'か'),
        ('悪', 'わる', 'か'),
        ('浮', 'う', 'か'),
        ('落', 'お', 'と')
    ]
    for kanji, reading, suf in okuri:
        pat = f'<ruby>{kanji}{suf}<rt>{reading}{suf}</rt></ruby>'
        rep = f'<ruby>{kanji}<rt>{reading}</rt></ruby>{suf}'
        c = re.sub(pat, rep, c)

    return c

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"Base Directory: {base_dir}")

    total_files_updated = 0

    for rel_path in TARGET_FILES:
        abs_path = os.path.join(base_dir, rel_path)
        if not os.path.exists(abs_path):
            print(f"Skipping (not found): {rel_path}")
            continue

        with open(abs_path, 'r', encoding='utf-8') as f:
            content = f.read()

        updated_content = fix_rubies_in_text(content)

        if updated_content != content:
            with open(abs_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"✓ Fixed rubies in: {rel_path}")
            total_files_updated += 1
        else:
            print(f"- Clean, no changes needed: {rel_path}")

    print(f"\nAll tasks complete! {total_files_updated} files updated.")

if __name__ == '__main__':
    main()
