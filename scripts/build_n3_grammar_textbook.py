# -*- coding: utf-8 -*-
"""
Generate the full jlpt_n3_grammar_textbook.html with sidebar categories, search,
4 mini quizzes per grammar point, bookmarking, and dictionary integration.
Strictly adheres to SKILL.md:
- 9 core sections matching N2 textbook
- No number badge in main title
- Clean cyan and sakura pink aesthetic
- extractSpeechText audio sanitization (<rt> removed)
"""

with open('/Users/yamauchimiku/Documents/GitHub/japanese-learning/jlpt_n2_grammar_textbook.html', 'r', encoding='utf-8') as f:
    n2_html = f.read()

# Replace N2 specific references with N3
n3_html = n2_html.replace('JLPT N2 文法マスターテキスト', 'JLPT N3 文法マスターテキスト')
n3_html = n3_html.replace('N2の文法', 'N3の文法')
n3_html = n3_html.replace('jlpt_n2_grammar_details.js', 'jlpt_n3_grammar_details.js')
n3_html = n3_html.replace('jlpt_n2_grammar_quiz_data.js', 'jlpt_n3_grammar_quiz_data.js')
n3_html = n3_html.replace('JLPT_N2_GRAMMAR_DETAILS', 'JLPT_N3_GRAMMAR_DETAILS')
n3_html = n3_html.replace('JLPT_N2_GRAMMAR_QUIZ_DATA', 'JLPT_N3_GRAMMAR_QUIZ_DATA')
n3_html = n3_html.replace('jlpt_n2_grammar_progress', 'jlpt_n3_grammar_progress')
n3_html = n3_html.replace('jlpt_n2_grammar_quiz.html', 'jlpt_n3_grammar_quiz.html')
n3_html = n3_html.replace('jlpt_n2_bookmarks', 'jlpt_n3_bookmarks')
n3_html = n3_html.replace('jlpt_n2_mastered', 'jlpt_n3_mastered')
n3_html = n3_html.replace('jlpt_n2_weakness_pool', 'jlpt_n3_weakness_pool')
n3_html = n3_html.replace('195', '182') # 182 grammar points for N3

# Write to jlpt_n3_grammar_textbook.html
out_path = '/Users/yamauchimiku/Documents/GitHub/japanese-learning/jlpt_n3_grammar_textbook.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(n3_html)

print(f"Generated {out_path} successfully!")
