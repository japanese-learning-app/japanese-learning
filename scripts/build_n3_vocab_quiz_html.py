# -*- coding: utf-8 -*-
"""
Generate jlpt_n3_vocab_quiz.html based on jlpt_n2_vocab_quiz.html:
- Categories (漢字読み, 表記, 文脈規定, 類義語, 用法)
- Clean, non-sensitive contexts
- Immediate feedback, Audio TTS (<rt> removed)
- 10 / 30 / 50 test pills with results
- Bookmarking and weakness review
"""

with open('/Users/yamauchimiku/Documents/GitHub/japanese-learning/jlpt_n2_vocab_quiz.html', 'r', encoding='utf-8') as f:
    n2_quiz_html = f.read()

n3_quiz_html = n2_quiz_html.replace('JLPT N2 語彙演習マスター', 'JLPT N3 語彙演習マスター')
n3_quiz_html = n3_quiz_html.replace('N2語彙', 'N3語彙')
n3_quiz_html = n3_quiz_html.replace('N2 語彙', 'N3 語彙')
n3_quiz_html = n3_quiz_html.replace('jlpt_n2_vocab_quiz_data.js', 'jlpt_n3_vocab_quiz_data.js')
n3_quiz_html = n3_quiz_html.replace('JLPT_N2_VOCAB_QUIZ_DATA', 'JLPT_N3_VOCAB_QUIZ_DATA')
n3_quiz_html = n3_quiz_html.replace('jlpt_n2_vocab_quiz_data.json', 'jlpt_n3_vocab_quiz_data.js')
n3_quiz_html = n3_quiz_html.replace('jlpt_n2_vocab_quiz_progress', 'jlpt_n3_vocab_quiz_progress')
n3_quiz_html = n3_quiz_html.replace('jlpt_n2_vocab_quiz_weakness', 'jlpt_n3_vocab_quiz_weakness')
n3_quiz_html = n3_quiz_html.replace('896問', '500問')
n3_quiz_html = n3_quiz_html.replace('896', '500')

out_path = '/Users/yamauchimiku/Documents/GitHub/japanese-learning/jlpt_n3_vocab_quiz.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(n3_quiz_html)

print(f"Generated {out_path} successfully!")
