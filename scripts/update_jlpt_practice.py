#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_jlpt_practice.py
Updates jlpt_practice.html to:
1. Dynamically update ALL counts (grammar, vocab, vocab quiz, grammar quiz) for N1, N2, N3, N4, N5
2. Prevent checkGrammarResumeButton from overriding other levels with hardcoded N2 text
3. Ensure furigana toggle works cleanly
4. Include all script tags for all 5 levels
"""

import re

filepath = '/Users/yamauchimiku/Documents/GitHub/japanese-learning/jlpt_practice.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Scripts tags
old_scripts = '''<script src="auth.js?v=20261021_0110"></script>
<script src="user_progress.js?v=20261021_0110"></script>
<script src="database/jlpt_vocab_all.js"></script>
<script src="database/jlpt_questions_data.js"></script>
<script src="database/jlpt_n2_grammar_quiz_data.js"></script>
<script src="database/jlpt_n3_grammar_quiz_data.js"></script>
<script src="database/jlpt_similar_grammar_dict.js"></script>
<script src="database/jlpt_n2_vocab_full_data.js"></script>
<script src="database/jlpt_explanation_translator.js"></script>
<script src="database/jlpt_option_helper.js"></script>'''

new_scripts = '''<script src="auth.js?v=20261021_0110"></script>
<script src="user_progress.js?v=20261021_0110"></script>
<script src="database/jlpt_vocab_all.js"></script>
<script src="database/jlpt_questions_data.js"></script>
<!-- All 5 Levels Grammar Quiz Data -->
<script src="database/jlpt_n1_grammar_quiz_data.js"></script>
<script src="database/jlpt_n2_grammar_quiz_data.js"></script>
<script src="database/jlpt_n3_grammar_quiz_data.js"></script>
<script src="database/jlpt_n4_grammar_quiz_data.js"></script>
<script src="database/jlpt_n5_grammar_quiz_data.js"></script>
<!-- All 5 Levels Vocab Quiz Data -->
<script src="database/jlpt_n1_vocab_quiz_data.js"></script>
<script src="database/jlpt_n2_vocab_quiz_data.js"></script>
<script src="database/jlpt_n3_vocab_quiz_data.js"></script>
<script src="database/jlpt_n4_vocab_quiz_data.js"></script>
<script src="database/jlpt_n5_vocab_quiz_data.js"></script>
<!-- Full Vocab Datasets -->
<script src="database/jlpt_n1_vocab_full_data.js" defer></script>
<script src="database/jlpt_n2_vocab_full_data.js" defer></script>
<script src="database/jlpt_n3_vocab_full_data.js" defer></script>
<script src="database/jlpt_n4_vocab_full_data.js" defer></script>
<script src="database/jlpt_n5_vocab_full_data.js" defer></script>
<script src="database/jlpt_similar_grammar_dict.js" defer></script>
<script src="database/jlpt_explanation_translator.js" defer></script>
<script src="database/jlpt_option_helper.js" defer></script>'''

content = content.replace(old_scripts, new_scripts)

# 2. Update Hero Counts HTML
old_hero_counts = '''      <div class="hero-counts">
        <div class="hero-count-item pink">
          <div class="hero-count-num" id="vocab-count">3,412 語</div>
          <div class="hero-count-lbl">語彙フラッシュカード</div>
        </div>
        <div class="hero-count-item pink">
          <div class="hero-count-num" style="font-weight:900;">896 問</div>
          <div class="hero-count-lbl">語彙穴埋め</div>
        </div>
        <div class="hero-count-item">
          <div class="hero-count-num" id="grammar-count" style="font-weight:900;">1,507 問</div>
          <div class="hero-count-lbl">文法穴埋め</div>
        </div>
      </div>'''

new_hero_counts = '''      <div class="hero-counts">
        <div class="hero-count-item pink">
          <div class="hero-count-num" id="vocab-count">3,412 語</div>
          <div class="hero-count-lbl">語彙フラッシュカード</div>
        </div>
        <div class="hero-count-item pink">
          <div class="hero-count-num" id="vocab-quiz-count" style="font-weight:900;">896 問</div>
          <div class="hero-count-lbl">語彙穴埋め</div>
        </div>
        <div class="hero-count-item">
          <div class="hero-count-num" id="grammar-count" style="font-weight:900;">1,507 問</div>
          <div class="hero-count-lbl">文法穴埋め</div>
        </div>
      </div>'''

content = content.replace(old_hero_counts, new_hero_counts)

# 3. Update Cards HTML to add IDs
# Card 1: Textbook
old_card_1 = '''      <!-- 文法マスターテキスト (Sakura Pink & Deep Rose: #B8596E, #F2D5DB) -->
      <div class="card-box" style="border: 2px solid #F2D5DB; position: relative; overflow: visible; background: #FFFFFF;">
        <span style="position: absolute; top: -11px; right: 18px; background: linear-gradient(135deg, #B8596E, #CE5A73); color: white; font-size: 11px; font-weight: 800; padding: 2px 10px; border-radius: 12px; letter-spacing: 0.5px; box-shadow: 0 2px 8px rgba(184,89,110,0.3);">全195文法・完全解説</span>
        <div>
          <div class="card-top-row">
            <div class="card-icon-square" style="background:#FAF1F3; color:#B8596E; border-color:#F2D5DB;">📖</div>
            <span class="card-badge-count" style="background:#B8596E; color:white; font-weight:800;">195 項目</span>
          </div>
          <div class="card-title-main" style="color:#B8596E;">文法マスターテキスト</div>
          <div class="card-subtitle-reading">意味別全12章・ミニ演習つき（ぶんぽうマスターテキスト）</div>
          <ul class="card-feature-list">
            <li>全195文法を「意味・機能別」に全12ユニット分類</li>
            <li>接続・コアニュアンス・英語直訳の落とし穴を日英解説</li>
            <li>似た文法の使い分け表 ＆ 厳選N2語彙を散りばめた例文</li>
            <li>各項目に即時判定の理解度ミニ演習 ＆ 読了チェック機能</li>
          </ul>
        </div>
        <div style="margin-top: 14px;">
          <a id="link-grammar-textbook" href="jlpt_n2_grammar_textbook.html" class="card-btn-action" style="text-decoration:none; text-align:center; display:block; background:linear-gradient(135deg, #B8596E, #CE5A73); color:white; font-weight:800; box-shadow: 0 4px 16px rgba(184,89,110,0.3);">
            📖 テキストで学ぶ (全195文法) →
          </a>
        </div>
      </div>'''

new_card_1 = '''      <!-- 文法マスターテキスト (Sakura Pink & Deep Rose: #B8596E, #F2D5DB) -->
      <div class="card-box" style="border: 2px solid #F2D5DB; position: relative; overflow: visible; background: #FFFFFF;">
        <span id="card-textbook-pill" style="position: absolute; top: -11px; right: 18px; background: linear-gradient(135deg, #B8596E, #CE5A73); color: white; font-size: 11px; font-weight: 800; padding: 2px 10px; border-radius: 12px; letter-spacing: 0.5px; box-shadow: 0 2px 8px rgba(184,89,110,0.3);">全195文法・完全解説</span>
        <div>
          <div class="card-top-row">
            <div class="card-icon-square" style="background:#FAF1F3; color:#B8596E; border-color:#F2D5DB;">📖</div>
            <span id="card-textbook-badge" class="card-badge-count" style="background:#B8596E; color:white; font-weight:800;">195 項目</span>
          </div>
          <div class="card-title-main" style="color:#B8596E;">文法マスターテキスト</div>
          <div id="card-textbook-sub" class="card-subtitle-reading">意味別全17章・ミニ演習つき（ぶんぽうマスターテキスト）</div>
          <ul class="card-feature-list">
            <li id="card-textbook-b1">全195文法を「意味・機能別」に全17ユニット分類</li>
            <li>接続・コアニュアンス・英語直訳の落とし穴を日英解説</li>
            <li id="card-textbook-b3">似た文法の使い分け表 ＆ 厳選N2語彙を散りばめた例文</li>
            <li>各項目に即時判定の理解度ミニ演習 ＆ 読了チェック機能</li>
          </ul>
        </div>
        <div style="margin-top: 14px;">
          <a id="link-grammar-textbook" href="jlpt_n2_grammar_textbook.html" class="card-btn-action" style="text-decoration:none; text-align:center; display:block; background:linear-gradient(135deg, #B8596E, #CE5A73); color:white; font-weight:800; box-shadow: 0 4px 16px rgba(184,89,110,0.3);">
            📖 テキストで学ぶ (全195文法) →
          </a>
        </div>
      </div>'''

content = content.replace(old_card_1, new_card_1)

# Card 2: Vocab Cards
old_card_2 = '''      <!-- 語彙フラッシュカード (Coral & Sakura Pink: #ED8C72, #FADADD) -->
      <div class="card-box coral" style="border: 2px solid #FADADD; position: relative; overflow: visible;">
        <span style="position: absolute; top: -11px; right: 18px; background: linear-gradient(135deg, #ED8C72, #E06D50); color: white; font-size: 11px; font-weight: 800; padding: 2px 10px; border-radius: 12px; letter-spacing: 0.5px; box-shadow: 0 2px 8px rgba(237,140,114,0.3);">全25カテゴリ完全網羅</span>
        <div>
          <div class="card-top-row">
            <div class="card-icon-square" style="background:#FFF5F3; color:#ED8C72; border-color:#FADADD;">🎴</div>
            <span class="card-badge-count" style="background:#ED8C72; color:white; font-weight:800;">3,412 語</span>
          </div>
          <div class="card-title-main" style="color:#D45D40;">語彙フラッシュカード</div>
          <div class="card-subtitle-reading">3D両面カード・全25カテゴリ（ごいフラッシュカード）</div>
          <ul class="card-feature-list">
            <li>公式PDF準拠：全25カテゴリ・3,412語完全網羅</li>
            <li>3Dカードフリップで隙間時間にサクサク記憶定着</li>
            <li>漢字の真上にルビ表示（ふりがな ON/OFF 切替）</li>
            <li>全単語に丁寧な会話例文 ＆ ネイティブ音声つき</li>
          </ul>
        </div>
        <div style="margin-top: 14px;">
          <a id="link-vocab-cards" href="jlpt_n2_vocab_cards.html" class="card-btn-action" style="text-decoration:none; text-align:center; display:block; background:linear-gradient(135deg, #ED8C72, #D45D40); color:white; font-weight:800; box-shadow: 0 4px 16px rgba(237,140,114,0.3);">
            🎴 カード学習を始める (全3,412語) →
          </a>
        </div>
      </div>'''

new_card_2 = '''      <!-- 語彙フラッシュカード (Coral & Sakura Pink: #ED8C72, #FADADD) -->
      <div class="card-box coral" style="border: 2px solid #FADADD; position: relative; overflow: visible;">
        <span id="card-vocab-cards-pill" style="position: absolute; top: -11px; right: 18px; background: linear-gradient(135deg, #ED8C72, #E06D50); color: white; font-size: 11px; font-weight: 800; padding: 2px 10px; border-radius: 12px; letter-spacing: 0.5px; box-shadow: 0 2px 8px rgba(237,140,114,0.3);">全3,412語・完全網羅</span>
        <div>
          <div class="card-top-row">
            <div class="card-icon-square" style="background:#FFF5F3; color:#ED8C72; border-color:#FADADD;">🎴</div>
            <span id="card-vocab-cards-badge" class="card-badge-count" style="background:#ED8C72; color:white; font-weight:800;">3,412 語</span>
          </div>
          <div class="card-title-main" style="color:#D45D40;">語彙フラッシュカード</div>
          <div id="card-vocab-cards-sub" class="card-subtitle-reading">3D両面カード・公式全語彙（ごいフラッシュカード）</div>
          <ul class="card-feature-list">
            <li id="card-vocab-cards-b1">全3,412語を完全網羅</li>
            <li>3Dカードフリップで隙間時間にサクサク記憶定着</li>
            <li>漢字の真上にルビ表示（ふりがな ON/OFF 切替）</li>
            <li>全単語に丁寧な会話例文 ＆ ネイティブ音声つき</li>
          </ul>
        </div>
        <div style="margin-top: 14px;">
          <a id="link-vocab-cards" href="jlpt_n2_vocab_cards.html" class="card-btn-action" style="text-decoration:none; text-align:center; display:block; background:linear-gradient(135deg, #ED8C72, #D45D40); color:white; font-weight:800; box-shadow: 0 4px 16px rgba(237,140,114,0.3);">
            🎴 カード学習を始める (全3,412語) →
          </a>
        </div>
      </div>'''

content = content.replace(old_card_2, new_card_2)

# Card 3: Vocab Quiz
old_card_3 = '''      <!-- 語彙穴埋め (Slate Navy & Ice Blue: #4D648D, #D0E1F9) -->
      <div class="card-box navy" style="border: 2px solid #D0E1F9; position: relative; overflow: visible;">
        <span style="position: absolute; top: -11px; right: 18px; background: linear-gradient(135deg, #4D648D, #364866); color: white; font-size: 11px; font-weight: 800; padding: 2px 10px; border-radius: 12px; letter-spacing: 0.5px; box-shadow: 0 2px 8px rgba(77,100,141,0.3);">全2冊・896問完全網羅</span>
        <div>
          <div class="card-top-row">
            <div class="card-icon-square" style="background:#EEF4FC; color:#4D648D; border-color:#D0E1F9;">📝</div>
            <span class="card-badge-count" style="background:#4D648D; color:white; font-weight:800;">896 問</span>
          </div>
          <div class="card-title-main" style="color:#364866;">語彙穴埋め</div>
          <div class="card-subtitle-reading">実戦4択穴埋め演習・全896問（ごいあなうめ）</div>
          <ul class="card-feature-list">
            <li>PDF完全網羅：『新にほんご500問』＆『合格するN2』</li>
            <li>全896問の実戦4択穴埋め問題でテスト対策</li>
            <li>スコア判定 ＆ 間違えた問題だけの集中復習機能</li>
            <li>全問題の解答・解説一覧レビュー機能つき</li>
          </ul>
        </div>
        <div style="margin-top: 14px;">
          <a id="link-vocab-quiz" href="jlpt_n2_vocab_quiz.html" class="card-btn-action" style="text-decoration:none; text-align:center; display:block; background:linear-gradient(135deg, #4D648D, #364866); color:white; font-weight:800; box-shadow: 0 4px 16px rgba(77,100,141,0.3);">
            📝 語彙穴埋め演習を解く (全896問) →
          </a>
        </div>
      </div>'''

new_card_3 = '''      <!-- 語彙穴埋め (Slate Navy & Ice Blue: #4D648D, #D0E1F9) -->
      <div class="card-box navy" style="border: 2px solid #D0E1F9; position: relative; overflow: visible;">
        <span id="card-vocab-quiz-pill" style="position: absolute; top: -11px; right: 18px; background: linear-gradient(135deg, #4D648D, #364866); color: white; font-size: 11px; font-weight: 800; padding: 2px 10px; border-radius: 12px; letter-spacing: 0.5px; box-shadow: 0 2px 8px rgba(77,100,141,0.3);">全896問完全網羅</span>
        <div>
          <div class="card-top-row">
            <div class="card-icon-square" style="background:#EEF4FC; color:#4D648D; border-color:#D0E1F9;">📝</div>
            <span id="card-vocab-quiz-badge" class="card-badge-count" style="background:#4D648D; color:white; font-weight:800;">896 問</span>
          </div>
          <div class="card-title-main" style="color:#364866;">語彙穴埋め</div>
          <div id="card-vocab-quiz-sub" class="card-subtitle-reading">実戦4択穴埋め演習・全896問（ごいあなうめ）</div>
          <ul class="card-feature-list">
            <li>漢字読み・表記・文脈規定・言い換え・用法を網羅</li>
            <li id="card-vocab-quiz-b2">全896問の実戦4択穴埋め問題でテスト対策</li>
            <li>スコア判定 ＆ 間違えた問題だけの集中復習機能</li>
            <li>全問題の解答・解説一覧レビュー機能つき</li>
          </ul>
        </div>
        <div style="margin-top: 14px;">
          <a id="link-vocab-quiz" href="jlpt_n2_vocab_quiz.html" class="card-btn-action" style="text-decoration:none; text-align:center; display:block; background:linear-gradient(135deg, #4D648D, #364866); color:white; font-weight:800; box-shadow: 0 4px 16px rgba(77,100,141,0.3);">
            📝 語彙穴埋め演習を解く (全896問) →
          </a>
        </div>
      </div>'''

content = content.replace(old_card_3, new_card_3)

# Card 4: Grammar Quiz
old_card_4 = '''      <!-- 文法穴埋め (1,507問) -->
      <div class="card-box teal" style="border: 2px solid var(--kobe-blue); position: relative; overflow: visible;">
        <span style="position: absolute; top: -11px; right: 18px; background: linear-gradient(135deg, var(--kobe-blue), var(--navy-dark)); color: white; font-size: 11px; font-weight: 800; padding: 2px 10px; border-radius: 12px; letter-spacing: 0.5px; box-shadow: 0 2px 8px rgba(20,134,173,0.3);">大幅強化・全195文法</span>
        <div>
          <div class="card-top-row">
            <div class="card-icon-square teal">法</div>
            <span class="card-badge-count teal" id="card-grammar-badge" style="background:var(--kobe-blue); color:white; font-weight:800;">1,507 問</span>
          </div>
          <div class="card-title-main teal">文法穴埋め</div>
          <div class="card-subtitle-reading">文法形式・実戦4択穴埋め演習（ぶんぽうあなうめ）</div>
          <ul class="card-feature-list">
            <li>全195文法項目を完全網羅 (全1,507問)</li>
            <li>漢字の真上にルビ（ふりがな ON/OFF）</li>
            <li>英語の対訳 ＆ 似ている文法の解説</li>
            <li>前回の続きから再開機能 ＆ 間違えた問題の復習</li>
          </ul>
        </div>
        <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 14px;">
          <a id="link-grammar-quiz" href="jlpt_n2_grammar_quiz.html" class="card-btn-action teal" style="text-decoration:none; text-align:center; display:block; font-weight: 800;">
            📝 文法穴埋め演習を解く (全1,507問) →
          </a>
          <button id="card-resume-btn" onclick="resumeGrammarQuiz()" style="display:none; padding: 9px 14px; border-radius: 12px; background: linear-gradient(135deg, #E8A4B2, #B8596E); color: white; border: none; font-size: 12.5px; font-weight: 700; cursor: pointer; text-align: center; box-shadow: 0 2px 8px rgba(184,89,110,0.25); transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='none'">
            ▶ 前回の続きからする (<span id="card-resume-num">1</span>問目〜)
          </button>
        </div>
      </div>'''

new_card_4 = '''      <!-- 文法穴埋め (1,507問) -->
      <div class="card-box teal" style="border: 2px solid var(--kobe-blue); position: relative; overflow: visible;">
        <span id="card-grammar-quiz-pill" style="position: absolute; top: -11px; right: 18px; background: linear-gradient(135deg, var(--kobe-blue), var(--navy-dark)); color: white; font-size: 11px; font-weight: 800; padding: 2px 10px; border-radius: 12px; letter-spacing: 0.5px; box-shadow: 0 2px 8px rgba(20,134,173,0.3);">大幅強化・全1,507問</span>
        <div>
          <div class="card-top-row">
            <div class="card-icon-square teal">法</div>
            <span class="card-badge-count teal" id="card-grammar-badge" style="background:var(--kobe-blue); color:white; font-weight:800;">1,507 問</span>
          </div>
          <div class="card-title-main teal">文法穴埋め</div>
          <div class="card-subtitle-reading">文法形式・実戦4択穴埋め演習（ぶんぽうあなうめ）</div>
          <ul class="card-feature-list">
            <li id="card-grammar-quiz-b1">全195文法項目を完全網羅 (全1,507問)</li>
            <li>漢字の真上にルビ（ふりがな ON/OFF）</li>
            <li>英語の対訳 ＆ 似ている文法の解説</li>
            <li>前回の続きから再開機能 ＆ 間違えた問題の復習</li>
          </ul>
        </div>
        <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 14px;">
          <a id="link-grammar-quiz" href="jlpt_n2_grammar_quiz.html" class="card-btn-action teal" style="text-decoration:none; text-align:center; display:block; font-weight: 800;">
            📝 文法穴埋め演習を解く (全1,507問) →
          </a>
          <button id="card-resume-btn" onclick="resumeGrammarQuiz()" style="display:none; padding: 9px 14px; border-radius: 12px; background: linear-gradient(135deg, #E8A4B2, #B8596E); color: white; border: none; font-size: 12.5px; font-weight: 700; cursor: pointer; text-align: center; box-shadow: 0 2px 8px rgba(184,89,110,0.25); transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='none'">
            ▶ 前回の続きからする (<span id="card-resume-num">1</span>問目〜)
          </button>
        </div>
      </div>'''

content = content.replace(old_card_4, new_card_4)

# 4. Replace LEVEL_INFO, switchLevel, updateCardLinks, updateBanner, checkGrammarResumeButton
js_pattern = re.compile(r'const LEVEL_INFO = \{[\s\S]*?function checkGrammarResumeButton\(\) \{[\s\S]*?\n  \}', re.MULTILINE)

new_js = '''const LEVEL_INFO = {
    n1: {
      badge: 'JLPT N1 最上級対策',
      title: 'JLPT N1 最上級道場 — 最高峰の日本語力を目指す',
      desc: '文法127項目・語彙3,747語・演習1,008問。高度な学術・論説・ビジネス表現を完全マスター。',
      grammarTextbookUrl: 'jlpt_n1_grammar_textbook.html',
      vocabCardsUrl: 'jlpt_n1_vocab_cards.html',
      vocabQuizUrl: 'jlpt_n1_vocab_quiz.html',
      grammarQuizUrl: 'jlpt_n1_grammar_quiz.html',
      grammarPoints: 127,
      grammarUnits: 11,
      grammarQuestions: 508,
      vocabCount: 3747,
      vocabQuizCount: 500
    },
    n2: {
      badge: 'JLPT N2 実戦・中上級対策',
      title: 'JLPT N2 実戦道場 — 合格を確実にする総合演習',
      desc: '文法195項目・語彙3,412語・演習2,403問。ビジネス・日常で自在に使いこなす運用力を養成。',
      grammarTextbookUrl: 'jlpt_n2_grammar_textbook.html',
      vocabCardsUrl: 'jlpt_n2_vocab_cards.html',
      vocabQuizUrl: 'jlpt_n2_vocab_quiz.html',
      grammarQuizUrl: 'jlpt_n2_grammar_quiz.html',
      grammarPoints: 195,
      grammarUnits: 17,
      grammarQuestions: 1507,
      vocabCount: 3412,
      vocabQuizCount: 896
    },
    n3: {
      badge: 'JLPT N3 中級完成対策',
      title: 'JLPT N3 中級完成道場 — 初級から中級への大跳躍',
      desc: '文法182項目・語彙1,841語・演習1,228問。日常会話の細やかなニュアンスを完全制覇。',
      grammarTextbookUrl: 'jlpt_n3_grammar_textbook.html',
      vocabCardsUrl: 'jlpt_n3_vocab_cards.html',
      vocabQuizUrl: 'jlpt_n3_vocab_quiz.html',
      grammarQuizUrl: 'jlpt_n3_grammar_quiz.html',
      grammarPoints: 182,
      grammarUnits: 16,
      grammarQuestions: 728,
      vocabCount: 1841,
      vocabQuizCount: 500
    },
    n4: {
      badge: 'JLPT N4 初級基礎対策',
      title: 'JLPT N4 初級基礎道場 — 会話と文法の土台を固める',
      desc: '文法62項目・語彙668語・演習613問。動詞の活用と重要表現を徹底攻略。',
      grammarTextbookUrl: 'jlpt_n4_grammar_textbook.html',
      vocabCardsUrl: 'jlpt_n4_vocab_cards.html',
      vocabQuizUrl: 'jlpt_n4_vocab_quiz.html',
      grammarQuizUrl: 'jlpt_n4_grammar_quiz.html',
      grammarPoints: 62,
      grammarUnits: 7,
      grammarQuestions: 248,
      vocabCount: 668,
      vocabQuizCount: 365
    },
    n5: {
      badge: 'JLPT N5 入門対策',
      title: 'JLPT N5 入門道場 — はじめての日本語を楽しく完全マスター',
      desc: '文法46項目・語彙702語・演習555問。文字・助詞・基本語尾をステップバイステップで習得。',
      grammarTextbookUrl: 'jlpt_n5_grammar_textbook.html',
      vocabCardsUrl: 'jlpt_n5_vocab_cards.html',
      vocabQuizUrl: 'jlpt_n5_vocab_quiz.html',
      grammarQuizUrl: 'jlpt_n5_grammar_quiz.html',
      grammarPoints: 46,
      grammarUnits: 5,
      grammarQuestions: 184,
      vocabCount: 702,
      vocabQuizCount: 371
    }
  };

  function switchLevel(lvl) {
    currentLevel = lvl;
    document.querySelectorAll('.level-tab').forEach(tab => {
      tab.classList.toggle('active', tab.textContent.toLowerCase().includes(lvl.toLowerCase()));
    });
    updateBanner();
    updateCardLinks();
    checkGrammarResumeButton();
  }

  function updateBanner() {
    const info = LEVEL_INFO[currentLevel] || LEVEL_INFO.n2;
    const badgeEl = document.getElementById('banner-badge');
    const titleEl = document.getElementById('banner-title');
    const descEl = document.getElementById('banner-desc');
    if (badgeEl) badgeEl.textContent = currentLevel.toUpperCase();
    if (titleEl) titleEl.textContent = info.title;
    if (descEl) descEl.textContent = info.desc;

    const vcEl = document.getElementById('vocab-count');
    if (vcEl) vcEl.textContent = `${info.vocabCount.toLocaleString()} 語`;
    const vqEl = document.getElementById('vocab-quiz-count');
    if (vqEl) vqEl.textContent = `${info.vocabQuizCount.toLocaleString()} 問`;
    const gcEl = document.getElementById('grammar-count');
    if (gcEl) gcEl.textContent = `${info.grammarQuestions.toLocaleString()} 問`;

    updateMyListBadges();
  }

  function updateCardLinks() {
    const info = LEVEL_INFO[currentLevel] || LEVEL_INFO.n2;
    const lvlU = currentLevel.toUpperCase();

    // 1. 文法マスターテキスト
    const linkTextbook = document.getElementById('link-grammar-textbook');
    if (linkTextbook) {
      linkTextbook.href = info.grammarTextbookUrl;
      linkTextbook.textContent = `📖 テキストで学ぶ (全${info.grammarPoints}文法) →`;
    }
    const tbPill = document.getElementById('card-textbook-pill');
    if (tbPill) tbPill.textContent = `全${info.grammarPoints}文法・完全解説`;
    const tbBadge = document.getElementById('card-textbook-badge');
    if (tbBadge) tbBadge.textContent = `${info.grammarPoints} 項目`;
    const tbSub = document.getElementById('card-textbook-sub');
    if (tbSub) tbSub.textContent = `意味別全${info.grammarUnits}章・ミニ演習つき（ぶんぽうマスターテキスト）`;
    const tbB1 = document.getElementById('card-textbook-b1');
    if (tbB1) tbB1.textContent = `全${info.grammarPoints}文法を「意味・機能別」に全${info.grammarUnits}ユニット分類`;
    const tbB3 = document.getElementById('card-textbook-b3');
    if (tbB3) tbB3.textContent = `似た文法の使い分け表 ＆ 厳選${lvlU}語彙を散りばめた例文`;

    // 2. 語彙フラッシュカード
    const linkVocabCards = document.getElementById('link-vocab-cards');
    if (linkVocabCards) {
      linkVocabCards.href = info.vocabCardsUrl;
      linkVocabCards.textContent = `🎴 カード学習を始める (全${info.vocabCount.toLocaleString()}語) →`;
    }
    const vcPill = document.getElementById('card-vocab-cards-pill');
    if (vcPill) vcPill.textContent = `全${info.vocabCount.toLocaleString()}語・完全網羅`;
    const vcBadge = document.getElementById('card-vocab-cards-badge');
    if (vcBadge) vcBadge.textContent = `${info.vocabCount.toLocaleString()} 語`;
    const vcB1 = document.getElementById('card-vocab-cards-b1');
    if (vcB1) vcB1.textContent = `全${info.vocabCount.toLocaleString()}語を完全網羅`;

    // 3. 語彙穴埋め演習
    const linkVocabQuiz = document.getElementById('link-vocab-quiz');
    if (linkVocabQuiz) {
      linkVocabQuiz.href = info.vocabQuizUrl;
      linkVocabQuiz.textContent = `📝 語彙穴埋め演習を解く (全${info.vocabQuizCount}問) →`;
    }
    const vqPill = document.getElementById('card-vocab-quiz-pill');
    if (vqPill) vqPill.textContent = `全${info.vocabQuizCount}問完全網羅`;
    const vqBadge = document.getElementById('card-vocab-quiz-badge');
    if (vqBadge) vqBadge.textContent = `${info.vocabQuizCount} 問`;
    const vqSub = document.getElementById('card-vocab-quiz-sub');
    if (vqSub) vqSub.textContent = `実戦4択穴埋め演習・全${info.vocabQuizCount}問（ごいあなうめ）`;
    const vqB2 = document.getElementById('card-vocab-quiz-b2');
    if (vqB2) vqB2.textContent = `全${info.vocabQuizCount}問の実戦4択穴埋め問題でテスト対策`;

    // 4. 文法穴埋め演習
    const linkGrammarQuiz = document.getElementById('link-grammar-quiz');
    if (linkGrammarQuiz) {
      linkGrammarQuiz.href = info.grammarQuizUrl;
      linkGrammarQuiz.textContent = `📝 文法穴埋め演習を解く (全${info.grammarQuestions}問) →`;
    }
    const gqPill = document.getElementById('card-grammar-quiz-pill');
    if (gqPill) gqPill.textContent = `大幅強化・全${info.grammarQuestions}問`;
    const gqBadge = document.getElementById('card-grammar-badge');
    if (gqBadge) gqBadge.textContent = `${info.grammarQuestions} 問`;
    const gqB1 = document.getElementById('card-grammar-quiz-b1');
    if (gqB1) gqB1.textContent = `全${info.grammarPoints}文法項目を完全網羅 (全${info.grammarQuestions}問)`;
  }

  function checkGrammarResumeButton() {
    const resumeBtn = document.getElementById('card-resume-btn');
    const resumeNum = document.getElementById('card-resume-num');
    if (!resumeBtn) return;

    try {
      const storageKey = `jlpt_${currentLevel}_grammar_progress`;
      const saved = localStorage.getItem(storageKey);
      if (saved) {
        const prog = JSON.parse(saved);
        if (prog && typeof prog.lastIndex === 'number' && prog.lastIndex > 0) {
          if (resumeNum) resumeNum.textContent = prog.lastIndex + 1;
          resumeBtn.style.display = 'block';
          return;
        }
      }
    } catch(e) {}
    resumeBtn.style.display = 'none';
  }'''

content = js_pattern.sub(new_js, content)

# 5. Update openStartQuizModal and startQuiz
old_modal_start = '''    if (sectionKey === 'grammar') {
      if (titleEl) titleEl.textContent = 'JLPT N2 文法演習 (1,507問)';
      if (allCountText) allCountText.textContent = '全問 (1,507問)';'''

new_modal_start = '''    const info = LEVEL_INFO[currentLevel] || LEVEL_INFO.n2;
    if (sectionKey === 'grammar') {
      if (titleEl) titleEl.textContent = `JLPT ${currentLevel.toUpperCase()} 文法演習 (${info.grammarQuestions}問)`;
      if (allCountText) allCountText.textContent = `全問 (${info.grammarQuestions}問)`;'''

content = content.replace(old_modal_start, new_modal_start)

old_modal_vocab = '''    } else if (sectionKey === 'vocabulary') {
      if (titleEl) titleEl.textContent = 'JLPT N2 文字・語彙演習 (500問)';
      if (allCountText) allCountText.textContent = '全問 (500問)';'''

new_modal_vocab = '''    } else if (sectionKey === 'vocabulary') {
      if (titleEl) titleEl.textContent = `JLPT ${currentLevel.toUpperCase()} 文字・語彙演習 (${info.vocabQuizCount}問)`;
      if (allCountText) allCountText.textContent = `全問 (${info.vocabQuizCount}問)`;'''

content = content.replace(old_modal_vocab, new_modal_vocab)

# Update startQuiz data selection
old_start_quiz_data = '''    } else if (sectionKey === 'grammar') {
      if (window.JLPT_N2_QUIZ_DATA && Array.isArray(window.JLPT_N2_QUIZ_DATA)) {
        let pool = [...window.JLPT_N2_QUIZ_DATA];
        if (quizRandomOrder && startIndex === 0) {
          pool = shuffleArray(pool);
        }
        if (quizLimit > 0 && startIndex === 0) {
          currentQuestions = pool.slice(0, quizLimit);
        } else {
          currentQuestions = pool;
        }
      } else {
        alert('文法データが見つかりません。');
        return;
      }
    } else if (sectionKey === 'vocabulary') {
      const data = (window.JLPT_QUESTIONS_DATA && window.JLPT_QUESTIONS_DATA[currentLevel]) || {};
      let pool = data.vocabulary || [];
      if (quizRandomOrder) pool = shuffleArray(pool);
      if (quizLimit > 0) {
        currentQuestions = pool.slice(0, quizLimit);
      } else {
        currentQuestions = pool;
      }
    }'''

new_start_quiz_data = '''    } else if (sectionKey === 'grammar') {
      const L = currentLevel.toUpperCase();
      const grammarSrc = window[`JLPT_${L}_QUIZ_DATA`] || window[`JLPT_${L}_GRAMMAR_QUIZ_DATA`];
      if (grammarSrc && Array.isArray(grammarSrc) && grammarSrc.length > 0) {
        let pool = [...grammarSrc];
        if (quizRandomOrder && startIndex === 0) {
          pool = shuffleArray(pool);
        }
        if (quizLimit > 0 && startIndex === 0) {
          currentQuestions = pool.slice(0, quizLimit);
        } else {
          currentQuestions = pool;
        }
      } else {
        alert(`${L}の文法演習データが見つかりません。`);
        return;
      }
    } else if (sectionKey === 'vocabulary') {
      const L = currentLevel.toUpperCase();
      const vocabSrc = window[`JLPT_${L}_VOCAB_QUIZ_DATA`];
      let pool = (vocabSrc && Array.isArray(vocabSrc) && vocabSrc.length > 0)
        ? [...vocabSrc]
        : ((window.JLPT_QUESTIONS_DATA && window.JLPT_QUESTIONS_DATA[currentLevel] && window.JLPT_QUESTIONS_DATA[currentLevel].vocabulary) || []);
      if (quizRandomOrder) pool = shuffleArray(pool);
      if (quizLimit > 0) {
        currentQuestions = pool.slice(0, quizLimit);
      } else {
        currentQuestions = pool;
      }
    }'''

content = content.replace(old_start_quiz_data, new_start_quiz_data)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated jlpt_practice.html successfully!')
