# -*- coding: utf-8 -*-
import glob
import re

files = sorted(glob.glob('/Users/yamauchimiku/.gemini/antigravity/scratch/japanese-flashcards/jlpt_n*_grammar_quiz.html'))

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    old_block_pattern = re.compile(
        r'if\s*\(\s*previousAns\s*!==\s*undefined\s*\)\s*\{'
        r'[\s\S]*?qRuby\s*=\s*qRuby\.replace\([^\)]+\);'
        r'\s*\}\s*else\s*\{'
        r'[\s\S]*?qRuby\s*=\s*qRuby\.replace\([^\)]+\);'
        r'\s*\}'
    )

    new_block = '''// 空欄の正規表現（【　　】または（　　　）などに対応）
    const blankPattern = /(?:【\\s*】|[（\\(]\\s*[）\\)])/;

    if (previousAns !== undefined) {
      const isRight = previousAns.isCorrect;
      const fillClass = isRight ? 'blank-box filled-correct' : 'blank-box filled-wrong';
      qRuby = qRuby.replace(blankPattern, `<span class="${fillClass}">${correctRuby}</span>`);
    } else {
      // 出題時は、空欄直前にある漢字1文字のルビを除去（動詞の活用変化やネタバレ・読み矛盾を完全防止）
      // 例: <ruby>来<rt>らい</rt></ruby>（　　　） -> 来<span class="blank-box">（　　　）</span>
      qRuby = qRuby.replace(/<ruby>([^<]+)<rt>[^<]*<\\/rt><\\/ruby>(?=\\s*(?:【\\s*】|[（\\(]\\s*[）\\)]))/g, '$1');
      qRuby = qRuby.replace(blankPattern, `<span class="blank-box">（　　　）</span>`);
    }'''

    if old_block_pattern.search(content):
        content = old_block_pattern.sub(lambda m: new_block, content)
        print(f"Updated blank replacement block in {file_path}")
    else:
        print(f"WARNING: old_block_pattern didn't match in {file_path}")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

