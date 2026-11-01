# -*- coding: utf-8 -*-
"""
Generate jlpt_n3_grammar_quiz.html matching the complete masterpiece jlpt_n2_grammar_quiz.html:
- 728 questions
- Pure （　　　）
- No spoiler in badge: shows "文法 #12" only (no grammar name)
- Audio TTS with <rt> removal
- 10/30/50 round-robin selection and full shuffle
- Bookmarking, weakness review, results screen
"""

with open('/Users/yamauchimiku/Documents/GitHub/japanese-learning/jlpt_n2_grammar_quiz.html', 'r', encoding='utf-8') as f:
    n2_quiz_html = f.read()

n3_quiz_html = n2_quiz_html.replace('JLPT N2 文法穴埋めマスター', 'JLPT N3 文法穴埋めマスター')
n3_quiz_html = n3_quiz_html.replace('N2文法', 'N3文法')
n3_quiz_html = n3_quiz_html.replace('N2 文法', 'N3 文法')
n3_quiz_html = n3_quiz_html.replace('jlpt_n2_grammar_quiz_data.js', 'jlpt_n3_grammar_quiz_data.js')
n3_quiz_html = n3_quiz_html.replace('JLPT_N2_GRAMMAR_QUIZ_DATA', 'JLPT_N3_GRAMMAR_QUIZ_DATA')
n3_quiz_html = n3_quiz_html.replace('jlpt_n2_grammar_progress', 'jlpt_n3_grammar_progress')
n3_quiz_html = n3_quiz_html.replace('jlpt_n2_grammar_weakness', 'jlpt_n3_grammar_weakness')
n3_quiz_html = n3_quiz_html.replace('jlpt_n2_grammar_starred', 'jlpt_n3_grammar_starred')
n3_quiz_html = n3_quiz_html.replace('jlpt_n2_grammar_textbook.html', 'jlpt_n3_grammar_textbook.html')
n3_quiz_html = n3_quiz_html.replace('1,507問', '728問')
n3_quiz_html = n3_quiz_html.replace('1507', '728')
n3_quiz_html = n3_quiz_html.replace('195項目', '182項目')

out_path = '/Users/yamauchimiku/Documents/GitHub/japanese-learning/jlpt_n3_grammar_quiz.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(n3_quiz_html)

print(f"Generated {out_path} successfully!")
