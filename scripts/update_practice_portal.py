# -*- coding: utf-8 -*-
"""
Updates jlpt_practice.html:
1. Unlock ALL levels (N1, N2, N3, N4, N5).
2. Wire up the 4 main portal cards to load current level pages:
   - jlpt_{lvl}_grammar_textbook.html
   - jlpt_{lvl}_vocab_cards.html
   - jlpt_{lvl}_vocab_quiz.html
   - jlpt_{lvl}_grammar_quiz.html
3. Update stats, counts, and descriptions for all levels.
"""

import re

repo_dir = '/Users/yamauchimiku/Documents/GitHub/japanese-learning'
path = f'{repo_dir}/jlpt_practice.html'

with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update LEVEL_INFO dictionary
level_info_replacement = '''  const LEVEL_INFO = {
    n1: {
      badge: 'JLPT N1 最上級対策',
      title: 'JLPT N1 最上級道場 — 最高峰の日本語力を目指す',
      desc: '文法127項目・語彙3,747語・演習1,000問以上。高度な学術・論説・ビジネス表現を完全マスター。',
      grammarTextbookUrl: 'jlpt_n1_grammar_textbook.html',
      vocabCardsUrl: 'jlpt_n1_vocab_cards.html',
      vocabQuizUrl: 'jlpt_n1_vocab_quiz.html',
      grammarQuizUrl: 'jlpt_n1_grammar_quiz.html',
      grammarPoints: 127,
      grammarQuestions: 508,
      vocabCount: 3747,
      vocabQuizCount: 500
    },
    n2: {
      badge: 'JLPT N2 実戦・中上級対策',
      title: 'JLPT N2 実戦道場 — 合格を確実にする総合演習',
      desc: '文法195項目・語彙3,412語・演習2,400問以上。ビジネス・日常で自在に使いこなす運用力を養成。',
      grammarTextbookUrl: 'jlpt_n2_grammar_textbook.html',
      vocabCardsUrl: 'jlpt_n2_vocab_cards.html',
      vocabQuizUrl: 'jlpt_n2_vocab_quiz.html',
      grammarQuizUrl: 'jlpt_n2_grammar_quiz.html',
      grammarPoints: 195,
      grammarQuestions: 1507,
      vocabCount: 3412,
      vocabQuizCount: 896
    },
    n3: {
      badge: 'JLPT N3 中級完成対策',
      title: 'JLPT N3 中級完成道場 — 初級から中級への大跳躍',
      desc: '文法182項目・語彙1,841語・演習1,200問以上。日常会話の細やかなニュアンスを完全制覇。',
      grammarTextbookUrl: 'jlpt_n3_grammar_textbook.html',
      vocabCardsUrl: 'jlpt_n3_vocab_cards.html',
      vocabQuizUrl: 'jlpt_n3_vocab_quiz.html',
      grammarQuizUrl: 'jlpt_n3_grammar_quiz.html',
      grammarPoints: 182,
      grammarQuestions: 728,
      vocabCount: 1841,
      vocabQuizCount: 500
    },
    n4: {
      badge: 'JLPT N4 初級基礎対策',
      title: 'JLPT N4 初級基礎道場 — 会話と文法の土台を固める',
      desc: '文法62項目・語彙668語・演習600問以上。動詞の活用と重要表現を徹底攻略。',
      grammarTextbookUrl: 'jlpt_n4_grammar_textbook.html',
      vocabCardsUrl: 'jlpt_n4_vocab_cards.html',
      vocabQuizUrl: 'jlpt_n4_vocab_quiz.html',
      grammarQuizUrl: 'jlpt_n4_grammar_quiz.html',
      grammarPoints: 62,
      grammarQuestions: 248,
      vocabCount: 668,
      vocabQuizCount: 365
    },
    n5: {
      badge: 'JLPT N5 入門対策',
      title: 'JLPT N5 入門道場 — はじめての日本語を楽しく完全マスター',
      desc: '文法46項目・語彙702語・演習550問以上。文字・助詞・基本語尾をステップバイステップで習得。',
      grammarTextbookUrl: 'jlpt_n5_grammar_textbook.html',
      vocabCardsUrl: 'jlpt_n5_vocab_cards.html',
      vocabQuizUrl: 'jlpt_n5_vocab_quiz.html',
      grammarQuizUrl: 'jlpt_n5_grammar_quiz.html',
      grammarPoints: 46,
      grammarQuestions: 184,
      vocabCount: 702,
      vocabQuizCount: 371
    }
  };'''

# Replace LEVEL_INFO
html = re.sub(r'const LEVEL_INFO\s*=\s*\{[\s\S]*?\n  \};', level_info_replacement, html)

# 2. Update switchLevel function to unlock all levels
new_switch_level = '''  function switchLevel(lvl) {
    currentLevel = lvl;
    document.querySelectorAll('.level-tab').forEach(tab => {
      tab.classList.toggle('active', tab.textContent.toLowerCase().includes(lvl.toLowerCase()));
    });
    updateBanner();
    updateCardLinks();
    checkGrammarResumeButton();
  }

  function updateCardLinks() {
    const info = LEVEL_INFO[currentLevel] || LEVEL_INFO.n2;
    const linkTextbook = document.getElementById('link-grammar-textbook');
    const linkVocabCards = document.getElementById('link-vocab-cards');
    const linkVocabQuiz = document.getElementById('link-vocab-quiz');
    const linkGrammarQuiz = document.getElementById('link-grammar-quiz');

    if (linkTextbook) {
      linkTextbook.href = info.grammarTextbookUrl;
      linkTextbook.textContent = `📖 テキストで学ぶ (全${info.grammarPoints}文法) →`;
    }
    if (linkVocabCards) {
      linkVocabCards.href = info.vocabCardsUrl;
      linkVocabCards.textContent = `🎴 カード学習を始める (全${info.vocabCount.toLocaleString()}語) →`;
    }
    if (linkVocabQuiz) {
      linkVocabQuiz.href = info.vocabQuizUrl;
      linkVocabQuiz.textContent = `📝 語彙穴埋め演習を解く (全${info.vocabQuizCount}問) →`;
    }
    if (linkGrammarQuiz) {
      linkGrammarQuiz.href = info.grammarQuizUrl;
      linkGrammarQuiz.textContent = `📝 文法穴埋め演習を解く (全${info.grammarQuestions}問) →`;
    }
  }'''

html = re.sub(r'function switchLevel\(lvl\)\s*\{[\s\S]*?checkGrammarResumeButton\(\);\s*\}', new_switch_level, html)

# 3. Add IDs to the 4 card links if not present
html = html.replace('href="jlpt_n2_grammar_textbook.html" class="card-btn-action"', 'id="link-grammar-textbook" href="jlpt_n2_grammar_textbook.html" class="card-btn-action"')
html = html.replace('href="jlpt_n2_vocab_cards.html" class="card-btn-action"', 'id="link-vocab-cards" href="jlpt_n2_vocab_cards.html" class="card-btn-action"')
html = html.replace('href="jlpt_n2_vocab_quiz.html" class="card-btn-action"', 'id="link-vocab-quiz" href="jlpt_n2_vocab_quiz.html" class="card-btn-action"')
html = html.replace('href="jlpt_n2_grammar_quiz.html" class="card-btn-action teal"', 'id="link-grammar-quiz" href="jlpt_n2_grammar_quiz.html" class="card-btn-action teal"')

# Also call updateCardLinks in DOMContentLoaded
html = html.replace('updateBanner();', 'updateBanner(); updateCardLinks();')

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated jlpt_practice.html with full 5-level support successfully!")
