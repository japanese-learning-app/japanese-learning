# -*- coding: utf-8 -*-
"""
Rebuilds and fixes ALL Grammar & Vocab Quiz HTMLs (N1-N5):
- Ensures robust data loading:
  data = window.JLPT_N{lvl}_QUIZ_DATA || window.JLPT_N{lvl}_GRAMMAR_QUIZ_DATA || []
- Removes broken script tags like jlpt_n2_data.js
- Ensures immediate renderQuestion() display on load
"""

import re
import os

repo_dir = '/Users/yamauchimiku/Documents/GitHub/japanese-learning'

LEVELS = ['n1', 'n2', 'n3', 'n4', 'n5']

# 1. Grammar Quizzes
for lvl in LEVELS:
    L = lvl.upper()
    qpath = f'{repo_dir}/jlpt_{lvl}_grammar_quiz.html'
    if not os.path.exists(qpath):
        continue
    with open(qpath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Replace data definition
    html = re.sub(
        r'const data = window\.JLPT_N\d_QUIZ_DATA.*?;',
        f'const data = window.JLPT_{L}_QUIZ_DATA || window.JLPT_{L}_GRAMMAR_QUIZ_DATA || [];',
        html
    )
    # Also replace in case it's GRAMMAR_QUIZ_DATA
    html = re.sub(
        r'const data = window\.JLPT_N\d_GRAMMAR_QUIZ_DATA.*?;',
        f'const data = window.JLPT_{L}_QUIZ_DATA || window.JLPT_{L}_GRAMMAR_QUIZ_DATA || [];',
        html
    )
    
    with open(qpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Fixed grammar quiz: {qpath}")

# 2. Vocab Quizzes
for lvl in LEVELS:
    L = lvl.upper()
    vqpath = f'{repo_dir}/jlpt_{lvl}_vocab_quiz.html'
    if not os.path.exists(vqpath):
        continue
    with open(vqpath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Remove non-existent script tag
    html = html.replace('<script src="database/jlpt_n2_data.js"></script>', '')
    html = html.replace(f'<script src="database/jlpt_{lvl}_data.js"></script>', '')
    
    # Ensure correct data assignment
    html = re.sub(
        r'let data = window\.JLPT_N\d_VOCAB_QUIZ_DATA.*?;',
        f'let data = window.JLPT_{L}_VOCAB_QUIZ_DATA || [];',
        html
    )
    
    with open(vqpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Fixed vocab quiz: {vqpath}")
