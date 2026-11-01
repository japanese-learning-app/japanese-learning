# -*- coding: utf-8 -*-
"""
Generates the 4 N1 Pages:
1. jlpt_n1_grammar_textbook.html
2. jlpt_n1_grammar_quiz.html
3. jlpt_n1_vocab_cards.html
4. jlpt_n1_vocab_quiz.html
"""

repo_dir = '/Users/yamauchimiku/Documents/GitHub/japanese-learning'

# 1. Grammar Textbook
with open(f'{repo_dir}/jlpt_n2_grammar_textbook.html', 'r', encoding='utf-8') as f:
    textbook_base = f.read()
    
n1_tb = textbook_base.replace('JLPT N2 文法マスターテキスト', 'JLPT N1 文法マスターテキスト')
n1_tb = n1_tb.replace('N2の文法', 'N1の文法')
n1_tb = n1_tb.replace('jlpt_n2_grammar_details.js', 'jlpt_n1_grammar_details.js')
n1_tb = n1_tb.replace('jlpt_n2_grammar_quiz_data.js', 'jlpt_n1_grammar_quiz_data.js')
n1_tb = n1_tb.replace('JLPT_N2_GRAMMAR_DETAILS', 'JLPT_N1_GRAMMAR_DETAILS')
n1_tb = n1_tb.replace('JLPT_N2_GRAMMAR_QUIZ_DATA', 'JLPT_N1_GRAMMAR_QUIZ_DATA')
n1_tb = n1_tb.replace('jlpt_n2_grammar_progress', 'jlpt_n1_grammar_progress')
n1_tb = n1_tb.replace('jlpt_n2_grammar_quiz.html', 'jlpt_n1_grammar_quiz.html')
n1_tb = n1_tb.replace('jlpt_n2_bookmarks', 'jlpt_n1_bookmarks')
n1_tb = n1_tb.replace('jlpt_n2_mastered', 'jlpt_n1_mastered')
n1_tb = n1_tb.replace('jlpt_n2_weakness_pool', 'jlpt_n1_weakness_pool')
n1_tb = n1_tb.replace('195', '127')

with open(f'{repo_dir}/jlpt_n1_grammar_textbook.html', 'w', encoding='utf-8') as f:
    f.write(n1_tb)
print("Generated jlpt_n1_grammar_textbook.html")

# 2. Grammar Quiz
with open(f'{repo_dir}/jlpt_n2_grammar_quiz.html', 'r', encoding='utf-8') as f:
    gquiz_base = f.read()
    
n1_gq = gquiz_base.replace('JLPT N2 文法穴埋めマスター', 'JLPT N1 文法穴埋めマスター')
n1_gq = n1_gq.replace('N2文法', 'N1文法')
n1_gq = n1_gq.replace('N2 文法', 'N1 文法')
n1_gq = n1_gq.replace('jlpt_n2_grammar_quiz_data.js', 'jlpt_n1_grammar_quiz_data.js')
n1_gq = n1_gq.replace('JLPT_N2_GRAMMAR_QUIZ_DATA', 'JLPT_N1_GRAMMAR_QUIZ_DATA')
n1_gq = n1_gq.replace('jlpt_n2_grammar_progress', 'jlpt_n1_grammar_progress')
n1_gq = n1_gq.replace('jlpt_n2_grammar_weakness', 'jlpt_n1_grammar_weakness')
n1_gq = n1_gq.replace('jlpt_n2_grammar_starred', 'jlpt_n1_grammar_starred')
n1_gq = n1_gq.replace('jlpt_n2_grammar_textbook.html', 'jlpt_n1_grammar_textbook.html')
n1_gq = n1_gq.replace('1,507問', '508問')
n1_gq = n1_gq.replace('1507', '508')
n1_gq = n1_gq.replace('195項目', '127項目')

with open(f'{repo_dir}/jlpt_n1_grammar_quiz.html', 'w', encoding='utf-8') as f:
    f.write(n1_gq)
print("Generated jlpt_n1_grammar_quiz.html")

# 3. Vocab Cards
with open(f'{repo_dir}/jlpt_n2_vocab_cards.html', 'r', encoding='utf-8') as f:
    vcards_base = f.read()
    
n1_vc = vcards_base.replace('JLPT N2 単語フラッシュカード', 'JLPT N1 単語フラッシュカード')
n1_vc = n1_vc.replace('N2語彙', 'N1語彙')
n1_vc = n1_vc.replace('N2 語彙', 'N1 語彙')
n1_vc = n1_vc.replace('jlpt_n2_vocab_full_data.js', 'jlpt_n1_vocab_full_data.js')
n1_vc = n1_vc.replace('JLPT_N2_VOCAB_CATEGORIES', 'JLPT_N1_VOCAB_CATEGORIES')
n1_vc = n1_vc.replace('JLPT_N2_VOCAB_DATA', 'JLPT_N1_VOCAB_DATA')
n1_vc = n1_vc.replace('jlpt_n2_vocab_starred', 'jlpt_n1_vocab_starred')
n1_vc = n1_vc.replace('jlpt_n2_vocab_known', 'jlpt_n1_vocab_known')
n1_vc = n1_vc.replace('3,412語', '3,747語')
n1_vc = n1_vc.replace('3412', '3747')

with open(f'{repo_dir}/jlpt_n1_vocab_cards.html', 'w', encoding='utf-8') as f:
    f.write(n1_vc)
print("Generated jlpt_n1_vocab_cards.html")

# 4. Vocab Quiz
with open(f'{repo_dir}/jlpt_n2_vocab_quiz.html', 'r', encoding='utf-8') as f:
    vquiz_base = f.read()
    
n1_vq = vquiz_base.replace('JLPT N2 語彙演習マスター', 'JLPT N1 語彙演習マスター')
n1_vq = n1_vq.replace('N2語彙', 'N1語彙')
n1_vq = n1_vq.replace('N2 語彙', 'N1 語彙')
n1_vq = n1_vq.replace('jlpt_n2_vocab_quiz_data.js', 'jlpt_n1_vocab_quiz_data.js')
n1_vq = n1_vq.replace('JLPT_N2_VOCAB_QUIZ_DATA', 'JLPT_N1_VOCAB_QUIZ_DATA')
n1_vq = n1_vq.replace('jlpt_n2_vocab_quiz_data.json', 'jlpt_n1_vocab_quiz_data.js')
n1_vq = n1_vq.replace('jlpt_n2_vocab_quiz_progress', 'jlpt_n1_vocab_quiz_progress')
n1_vq = n1_vq.replace('jlpt_n2_vocab_quiz_weakness', 'jlpt_n1_vocab_quiz_weakness')
n1_vq = n1_vq.replace('896問', '500問')
n1_vq = n1_vq.replace('896', '500')

with open(f'{repo_dir}/jlpt_n1_vocab_quiz.html', 'w', encoding='utf-8') as f:
    f.write(n1_vq)
print("Generated jlpt_n1_vocab_quiz.html")
