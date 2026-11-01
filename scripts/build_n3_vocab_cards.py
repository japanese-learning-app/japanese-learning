# -*- coding: utf-8 -*-
"""
Generate jlpt_n3_vocab_cards.html based on the masterpiece jlpt_n2_vocab_cards.html:
- Flashcards with clean flip animation (Space, Up/Down, Left/Right, 1/2)
- Audio pronunciation (reading prioritized, <rt> removed)
- 10 / 30 / 50 random test pills with result screens
- Category filtering and search
- Bookmarks and weakness review
"""

with open('/Users/yamauchimiku/Documents/GitHub/japanese-learning/jlpt_n2_vocab_cards.html', 'r', encoding='utf-8') as f:
    n2_cards_html = f.read()

n3_cards_html = n2_cards_html.replace('JLPT N2 単語フラッシュカード', 'JLPT N3 単語フラッシュカード')
n3_cards_html = n3_cards_html.replace('N2語彙', 'N3語彙')
n3_cards_html = n3_cards_html.replace('N2 語彙', 'N3 語彙')
n3_cards_html = n3_cards_html.replace('jlpt_n2_vocab_full_data.js', 'jlpt_n3_vocab_full_data.js')
n3_cards_html = n3_cards_html.replace('JLPT_N2_VOCAB_CATEGORIES', 'JLPT_N3_VOCAB_CATEGORIES')
n3_cards_html = n3_cards_html.replace('JLPT_N2_VOCAB_DATA', 'JLPT_N3_VOCAB_DATA')
n3_cards_html = n3_cards_html.replace('jlpt_n2_vocab_starred', 'jlpt_n3_vocab_starred')
n3_cards_html = n3_cards_html.replace('jlpt_n2_vocab_known', 'jlpt_n3_vocab_known')
n3_cards_html = n3_cards_html.replace('3,412語', '1,841語')
n3_cards_html = n3_cards_html.replace('3412', '1841')

out_path = '/Users/yamauchimiku/Documents/GitHub/japanese-learning/jlpt_n3_vocab_cards.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(n3_cards_html)

print(f"Generated {out_path} successfully!")
