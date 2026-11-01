# -*- coding: utf-8 -*-
"""
Apply all UI and Kana updates requested by user:
1. Top tab titles: 'ひらがな・カタカナ', 'JLPT漢字リスト', '毎日書き取りテスト'
2. Kana studio header:
   - Remove 'JLPT漢字リストへ →' button
   - Remove bulky title and subtitle
   - Add 'ひらがな (練習/テスト) カタカナ (練習/テスト)'
   - Remove '（清音）', '（きゃ・しゃ...）' from categories
   - Hide Katakana loanwords from Hiragana view
   - Wire Katakana tracing and quiz
3. Kanji List:
   - Remove '← 漢字テストに戻る' button
   - Level pills order: N1, N2, N3, N4, N5
   - Remove 'Day 2' badge from cards
   - Remove '毎日書き取りテストと100%連動中！' banner
4. Daily Kanji Quiz:
   - Level pills order: N1, N2, N3, N4, N5
   - Remove hardcoded '1日10問' and 'まいにち10問'
"""

import re

def update_kanji_engine():
    with open('js/kanji_engine.js', 'r', encoding='utf-8') as f:
        code = f.read()

    # 1. Update KanjiListEngine currentLevel default to N1
    code = re.sub(
        r"window\.KanjiListEngine\s*=\s*\{[\s\S]*?currentLevel:\s*'N5',",
        "window.KanjiListEngine = {\n    currentLevel: 'N1',",
        code, count=1
    )
    code = re.sub(
        r"init\(containerId,\s*level\s*=\s*'N5'\)",
        "init(containerId, level = 'N1')",
        code, count=1
    )

    # 2. Update KanjiListEngine render toolbar: remove "← 漢字テストに戻る", order N1..N5
    old_toolbar = '''      container.innerHTML = `
        <div class="kanji-list-toolbar">
          <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
            <button onclick="switchWritingTab('quiz')" style="background:#EFF6FF; border:1.5px solid #93C5FD; color:#1D4ED8; padding:6px 14px; border-radius:8px; font-weight:800; font-size:0.84rem; cursor:pointer; display:inline-flex; align-items:center; gap:4px; box-shadow:0 1px 3px rgba(0,0,0,0.05);" title="漢字書き取りテストに戻る">
              ← 漢字テストに戻る
            </button>
            <div class="quiz-level-pills">
              <button class="quiz-level-pill ${this.currentLevel === 'N5' ? 'active' : ''}" onclick="KanjiListEngine.setLevel('N5', this)">N5</button>
              <button class="quiz-level-pill ${this.currentLevel === 'N4' ? 'active' : ''}" onclick="KanjiListEngine.setLevel('N4', this)">N4</button>
              <button class="quiz-level-pill ${this.currentLevel === 'N3' ? 'active' : ''}" onclick="KanjiListEngine.setLevel('N3', this)">N3</button>
              <button class="quiz-level-pill ${this.currentLevel === 'N2' ? 'active' : ''}" onclick="KanjiListEngine.setLevel('N2', this)">N2</button>
              <button class="quiz-level-pill ${this.currentLevel === 'N1' ? 'active' : ''}" onclick="KanjiListEngine.setLevel('N1', this)">N1</button>
            </div>
          </div>'''

    new_toolbar = '''      container.innerHTML = `
        <div class="kanji-list-toolbar">
          <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
            <div class="quiz-level-pills">
              <button class="quiz-level-pill ${this.currentLevel === 'N1' ? 'active' : ''}" onclick="KanjiListEngine.setLevel('N1', this)">N1</button>
              <button class="quiz-level-pill ${this.currentLevel === 'N2' ? 'active' : ''}" onclick="KanjiListEngine.setLevel('N2', this)">N2</button>
              <button class="quiz-level-pill ${this.currentLevel === 'N3' ? 'active' : ''}" onclick="KanjiListEngine.setLevel('N3', this)">N3</button>
              <button class="quiz-level-pill ${this.currentLevel === 'N4' ? 'active' : ''}" onclick="KanjiListEngine.setLevel('N4', this)">N4</button>
              <button class="quiz-level-pill ${this.currentLevel === 'N5' ? 'active' : ''}" onclick="KanjiListEngine.setLevel('N5', this)">N5</button>
            </div>
          </div>'''

    if old_toolbar in code:
        code = code.replace(old_toolbar, new_toolbar)

    # 3. Remove "毎日書き取りテストとの連動案内バナー" from KanjiListEngine
    old_banner = '''        <!-- 毎日書き取りテストとの連動案内バナー -->
        <div style="background:#F0F9FF; border:1.5px solid #BAE6FD; border-radius:12px; padding:10px 14px; margin-bottom:14px; font-size:0.83rem; color:#0369A1; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:8px;">
          <div style="display:flex; align-items:center; gap:6px;">
            <span>✍️</span>
            <span><strong>毎日書き取りテストと100%連動中！</strong> 各漢字カードの「📝 Day X」や詳細モーダルから、すぐにテストに挑戦できます。</span>
          </div>
          <button onclick="switchWritingTab('quiz')" style="background:#0284C7; color:white; border:none; padding:5px 12px; border-radius:7px; font-size:0.78rem; font-weight:800; cursor:pointer;">
            📝 書き取りテストへ
          </button>
        </div>'''

    if old_banner in code:
        code = code.replace(old_banner, '')

    # 4. Remove Day badge from kanji card in KanjiListEngine
    old_card_badge = '''                ${k.dailyQuizRef ? `
                  <div style="font-size:0.65rem; font-weight:800; background:#EFF6FF; color:#1D4ED8; border:1px solid #BFDBFE; border-radius:5px; padding:1px 6px; margin-bottom:4px; display:inline-flex; align-items:center; gap:2px;" title="毎日漢字書き取りテスト Day ${k.dailyQuizRef.day} に出題">
                    📝 Day ${k.dailyQuizRef.day}
                  </div>
                ` : ''}'''

    if old_card_badge in code:
        code = code.replace(old_card_badge, '')

    # 5. In MainichiKanjiQuiz, update default level to N1 and remove hardcoded (1日10問)
    code = re.sub(
        r"window\.MainichiKanjiQuiz\s*=\s*\{[\s\S]*?currentLevel:\s*'N5',",
        "window.MainichiKanjiQuiz = {\n    currentLevel: 'N1',",
        code, count=1
    )
    code = re.sub(
        r"init\(containerId,\s*level\s*=\s*'N5',\s*day\s*=\s*1\)",
        "init(containerId, level = 'N1', day = 1)",
        code, count=1
    )

    old_day_title = '<span style="font-size:0.75rem; color:#64748B;">全${days.length}日 (1日10問)</span>'
    new_day_title = '<span style="font-size:0.75rem; color:#64748B;">全${days.length}日 (${lvlData ? lvlData.totalQuestions : questions.length}問)</span>'
    if old_day_title in code:
        code = code.replace(old_day_title, new_day_title)

    old_q_header = '<span style="font-size:0.8rem; color:#64748B;">まいにち10問</span>'
    new_q_header = '<span style="font-size:0.8rem; color:#64748B;">全${questions.length}問</span>'
    if old_q_header in code:
        code = code.replace(old_q_header, new_q_header)

    with open('js/kanji_engine.js', 'w', encoding='utf-8') as f:
        f.write(code)

    print("js/kanji_engine.js updated successfully!")


def update_app_html():
    with open('app.html', 'r', encoding='utf-8') as f:
        code = f.read()

    # 1. Update Top Tabs
    old_tabs = '''      <div class="kanji-main-tabs">
        <button class="kanji-main-tab-btn active" id="tab-btn-writing-kana" onclick="switchWritingTab('kana')">あ かな学習（ひらがな・カタカナ）</button>
        <button class="kanji-main-tab-btn" id="tab-btn-writing-list" onclick="switchWritingTab('list')">📚 JLPT漢字リスト（書き順・筆順）</button>
        <button class="kanji-main-tab-btn" id="tab-btn-writing-quiz" onclick="switchWritingTab('quiz')">📝 毎日漢字書き取りテスト（毎日漢字スタイル）</button>
        <button class="kanji-main-tab-btn" id="tab-btn-writing-pdf" onclick="switchWritingTab('pdf')">📄 練習用紙プリント</button>
      </div>'''

    new_tabs = '''      <div class="kanji-main-tabs">
        <button class="kanji-main-tab-btn active" id="tab-btn-writing-kana" onclick="switchWritingTab('kana')">ひらがな・カタカナ</button>
        <button class="kanji-main-tab-btn" id="tab-btn-writing-list" onclick="switchWritingTab('list')">JLPT漢字リスト</button>
        <button class="kanji-main-tab-btn" id="tab-btn-writing-quiz" onclick="switchWritingTab('quiz')">毎日書き取りテスト</button>
        <button class="kanji-main-tab-btn" id="tab-btn-writing-pdf" onclick="switchWritingTab('pdf')">練習用紙プリント</button>
      </div>'''

    if old_tabs in code:
        code = code.replace(old_tabs, new_tabs)

    # 2. Update Daily Writing Quiz top level bar (N1 on left)
    old_quiz_bar = '''        <div class="quiz-top-level-bar">
          <div class="quiz-level-pills">
            <button class="quiz-level-pill active" onclick="setWritingQuizLevel('N5', this)">N5（10日・100問）</button>
            <button class="quiz-level-pill" onclick="setWritingQuizLevel('N4', this)">N4（18日・180問）</button>
            <button class="quiz-level-pill" onclick="setWritingQuizLevel('N3', this)">N3（30日・300問）</button>
            <button class="quiz-level-pill" onclick="setWritingQuizLevel('N2', this)">N2（30日・300問）</button>
            <button class="quiz-level-pill" onclick="setWritingQuizLevel('N1', this)">N1（30日・300問）</button>
          </div>
          <div style="font-size:0.84rem; color:#64748B;">
            💡 縦のインデックスからDay（1日10問）を選び、白紙に手書きして<strong>「解答」</strong>で自己採点できます。
          </div>
        </div>'''

    new_quiz_bar = '''        <div class="quiz-top-level-bar">
          <div class="quiz-level-pills">
            <button class="quiz-level-pill active" onclick="setWritingQuizLevel('N1', this)">N1</button>
            <button class="quiz-level-pill" onclick="setWritingQuizLevel('N2', this)">N2</button>
            <button class="quiz-level-pill" onclick="setWritingQuizLevel('N3', this)">N3</button>
            <button class="quiz-level-pill" onclick="setWritingQuizLevel('N4', this)">N4</button>
            <button class="quiz-level-pill" onclick="setWritingQuizLevel('N5', this)">N5</button>
          </div>
          <div style="font-size:0.84rem; color:#64748B;">
            💡 縦のインデックスからDayを選び、白紙に手書きして<strong>「解答」</strong>で自己採点できます。
          </div>
        </div>'''

    if old_quiz_bar in code:
        code = code.replace(old_quiz_bar, new_quiz_bar)

    # 3. Update Kana Panel Header & Category Filter
    old_kana_header = '''          <!-- 上部ヘッダー: タイトル + 戻るボタン + モード切替 (✍️ なぞり書き / 📝 書き取りテスト) -->
          <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px; margin-bottom:16px; border-bottom:1.5px solid #F1F5F9; padding-bottom:14px;">
            <div>
              <div style="font-weight:800; color:var(--kobe-blue); font-size:1.15rem; display:flex; align-items:center; gap:6px;">
                <span>あ</span>
                <span>かな学習スタジオ（五十音・濁音・拗音・特殊音）</span>
              </div>
              <div style="font-size:0.83rem; color:var(--text-sub); margin-top:2px;">
                書き順アニメーション・筆順コマ送り・田字格なぞり練習・書き取りテスト全対応！
              </div>
            </div>
            <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
              <button onclick="switchWritingTab('list')" style="background:#EFF6FF; border:1.5px solid #93C5FD; color:#1D4ED8; padding:6px 12px; border-radius:8px; font-weight:800; font-size:0.82rem; cursor:pointer;">
                JLPT漢字リストへ →
              </button>
              <div class="quiz-level-pills">
                <button class="quiz-level-pill active" id="btn-kana-submode-trace" onclick="switchKanaSubMode('trace')">✍️ 書き順・なぞり練習</button>
                <button class="quiz-level-pill" id="btn-kana-submode-quiz" onclick="switchKanaSubMode('quiz')">📝 かな書き取りテスト</button>
              </div>
            </div>
          </div>

          <!-- サブモード1: なぞり書き練習 パネル -->
          <div id="kana-panel-trace">
            <!-- フィルターバー: カテゴリ pills & ひらがな/カタカナ切替 -->
            <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px; margin-bottom:14px;">
              <div class="quiz-level-pills" id="kana-category-pills">
                <button class="quiz-level-pill active" onclick="setKanaCategory('all', this)">すべて</button>
                <button class="quiz-level-pill" onclick="setKanaCategory('seion', this)">五十音（清音）</button>
                <button class="quiz-level-pill" onclick="setKanaCategory('dakuon', this)">濁音・半濁音</button>
                <button class="quiz-level-pill" onclick="setKanaCategory('youon', this)">拗音（きゃ・しゃ…）</button>
                <button class="quiz-level-pill" onclick="setKanaCategory('tokushu', this)">カタカナ特殊音</button>
              </div>
              <div class="quiz-level-pills">
                <button class="quiz-level-pill active" id="btn-kana-hira" onclick="switchKanaType('hiragana')">ひらがな</button>
                <button class="quiz-level-pill" id="btn-kana-kata" onclick="switchKanaType('katakana')">カタカナ</button>
              </div>
            </div>'''

    new_kana_header = '''          <!-- 上部モード切替: ひらがな（練習 / テスト） カタカナ（練習 / テスト） -->
          <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px; margin-bottom:16px; border-bottom:1.5px solid #F1F5F9; padding-bottom:12px;">
            <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
              <!-- ひらがな: 練習 / テスト -->
              <div style="display:inline-flex; align-items:center; gap:4px; background:#F8FAFC; border:1.5px solid #CBD5E1; padding:4px 8px; border-radius:10px;">
                <span style="font-weight:800; font-size:0.86rem; color:#1E3A8A; margin-right:4px;">ひらがな:</span>
                <button class="quiz-level-pill active" id="btn-mode-hira-trace" onclick="selectKanaMode('hiragana', 'trace')">練習</button>
                <button class="quiz-level-pill" id="btn-mode-hira-quiz" onclick="selectKanaMode('hiragana', 'quiz')">テスト</button>
              </div>

              <!-- カタカナ: 練習 / テスト -->
              <div style="display:inline-flex; align-items:center; gap:4px; background:#F8FAFC; border:1.5px solid #CBD5E1; padding:4px 8px; border-radius:10px;">
                <span style="font-weight:800; font-size:0.86rem; color:#1E3A8A; margin-right:4px;">カタカナ:</span>
                <button class="quiz-level-pill" id="btn-mode-kata-trace" onclick="selectKanaMode('katakana', 'trace')">練習</button>
                <button class="quiz-level-pill" id="btn-mode-kata-quiz" onclick="selectKanaMode('katakana', 'quiz')">テスト</button>
              </div>
            </div>
          </div>

          <!-- サブモード1: なぞり書き練習 パネル -->
          <div id="kana-panel-trace">
            <!-- フィルターバー: カテゴリ pills -->
            <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px; margin-bottom:14px;">
              <div class="quiz-level-pills" id="kana-category-pills">
                <button class="quiz-level-pill active" onclick="setKanaCategory('all', this)">すべて</button>
                <button class="quiz-level-pill" onclick="setKanaCategory('seion', this)">五十音</button>
                <button class="quiz-level-pill" onclick="setKanaCategory('dakuon', this)">濁音・半濁音</button>
                <button class="quiz-level-pill" onclick="setKanaCategory('youon', this)">拗音</button>
                <button class="quiz-level-pill" id="pill-kana-tokushu" style="display:none;" onclick="setKanaCategory('tokushu', this)">特殊音</button>
              </div>
            </div>'''

    if old_kana_header in code:
        code = code.replace(old_kana_header, new_kana_header)

    # 4. Update JS for selectKanaMode
    old_js_block = '''  let currentKanaType = 'hiragana';
  let currentKanaCategory = 'all';
  let currentKanaSubMode = 'trace'; // 'trace' | 'quiz'
  let currentSelectedKana = { char: 'あ', romaji: 'a' };
  let currentActiveKanaSubChar = 'あ';'''

    new_js_block = '''  let currentKanaType = 'hiragana';
  let currentKanaCategory = 'all';
  let currentKanaSubMode = 'trace'; // 'trace' | 'quiz'
  let currentSelectedKana = { char: 'あ', romaji: 'a' };
  let currentActiveKanaSubChar = 'あ';

  function selectKanaMode(type, mode) {
    currentKanaType = type;
    currentKanaSubMode = mode;

    document.getElementById('btn-mode-hira-trace')?.classList.toggle('active', type === 'hiragana' && mode === 'trace');
    document.getElementById('btn-mode-hira-quiz')?.classList.toggle('active', type === 'hiragana' && mode === 'quiz');
    document.getElementById('btn-mode-kata-trace')?.classList.toggle('active', type === 'katakana' && mode === 'trace');
    document.getElementById('btn-mode-kata-quiz')?.classList.toggle('active', type === 'katakana' && mode === 'quiz');

    const tracePanel = document.getElementById('kana-panel-trace');
    const quizPanel = document.getElementById('kana-panel-quiz');

    if (mode === 'trace') {
      if (tracePanel) tracePanel.style.display = 'block';
      if (quizPanel) quizPanel.style.display = 'none';
      renderKanaGridPicker();
      const first = KANA_ALL_DATA.find(x => x.cat === (currentKanaCategory === 'all' ? 'seion' : currentKanaCategory)) || KANA_ALL_DATA[0];
      const char = (type === 'hiragana') ? first.h : first.k;
      selectKanaForTrace(char, first.r, false);
    } else {
      if (tracePanel) tracePanel.style.display = 'none';
      if (quizPanel) quizPanel.style.display = 'block';
      if (typeof KanaWritingQuiz !== 'undefined') {
        KanaWritingQuiz.setType(type);
      }
    }
  }'''

    if old_js_block in code:
        code = code.replace(old_js_block, new_js_block)

    # 5. Replace renderKanaGridPicker
    m = re.search(r'(function renderKanaGridPicker\(\) \{[\s\S]*?\n  \})', code)
    if m:
        new_grid_func = '''function renderKanaGridPicker() {
    const grid = document.getElementById('kana-grid-picker');
    if (!grid) return;

    // Show/hide 特殊音 pill based on currentKanaType
    const tokushuPill = document.getElementById('pill-kana-tokushu');
    if (tokushuPill) {
      tokushuPill.style.display = (currentKanaType === 'katakana') ? 'inline-block' : 'none';
    }
    if (currentKanaType === 'hiragana' && currentKanaCategory === 'tokushu') {
      currentKanaCategory = 'all';
    }

    if (currentKanaCategory === 'all') {
      const seionList = KANA_ALL_DATA.filter(x => x.cat === 'seion' || x.cat === 'blank');
      const dakuonList = KANA_ALL_DATA.filter(x => x.cat === 'dakuon');
      const youonList = KANA_ALL_DATA.filter(x => x.cat === 'youon');
      const tokushuList = KANA_ALL_DATA.filter(x => x.cat === 'tokushu');

      grid.innerHTML = `
        <div style="display:flex; flex-direction:column; gap:16px;">
          <!-- 五十音 -->
          <div>
            <div style="font-weight:800; font-size:0.86rem; color:#1E3A8A; margin-bottom:8px; display:flex; align-items:center; gap:6px;">
              <span>🌸</span> <span>五十音（46字）</span>
            </div>
            <div style="display:grid; grid-template-columns:repeat(5, 1fr); gap:6px;">
              ${seionList.map(item => renderKanaCell(item)).join('')}
            </div>
          </div>

          <!-- 濁音・半濁音 -->
          <div>
            <div style="font-weight:800; font-size:0.86rem; color:#1E3A8A; margin-bottom:8px; display:flex; align-items:center; gap:6px;">
              <span>🔔</span> <span>濁音・半濁音（25字）</span>
            </div>
            <div style="display:grid; grid-template-columns:repeat(5, 1fr); gap:6px;">
              ${dakuonList.map(item => renderKanaCell(item)).join('')}
            </div>
          </div>

          <!-- 拗音 -->
          <div>
            <div style="font-weight:800; font-size:0.86rem; color:#1E3A8A; margin-bottom:8px; display:flex; align-items:center; gap:6px;">
              <span>🎋</span> <span>拗音（33字）</span>
            </div>
            <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:6px;">
              ${youonList.map(item => renderKanaCell(item)).join('')}
            </div>
          </div>

          ${currentKanaType === 'katakana' ? `
            <!-- カタカナ外来語・特殊音 (1行3つ) -->
            <div>
              <div style="font-weight:800; font-size:0.86rem; color:#1E3A8A; margin-bottom:8px; display:flex; align-items:center; gap:6px;">
                <span>🌐</span> <span>外来語・特殊音（24字）</span>
              </div>
              <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:6px;">
                ${tokushuList.map(item => renderKanaCell(item)).join('')}
              </div>
            </div>
          ` : ''}
        </div>
      `;
    } else if (currentKanaCategory === 'seion') {
      const list = KANA_ALL_DATA.filter(x => x.cat === 'seion' || x.cat === 'blank');
      grid.innerHTML = `<div style="display:grid; grid-template-columns:repeat(5, 1fr); gap:6px;">${list.map(item => renderKanaCell(item)).join('')}</div>`;
    } else if (currentKanaCategory === 'dakuon') {
      const list = KANA_ALL_DATA.filter(x => x.cat === 'dakuon');
      grid.innerHTML = `<div style="display:grid; grid-template-columns:repeat(5, 1fr); gap:6px;">${list.map(item => renderKanaCell(item)).join('')}</div>`;
    } else if (currentKanaCategory === 'youon') {
      const list = KANA_ALL_DATA.filter(x => x.cat === 'youon');
      grid.innerHTML = `<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:6px;">${list.map(item => renderKanaCell(item)).join('')}</div>`;
    } else if (currentKanaCategory === 'tokushu' && currentKanaType === 'katakana') {
      const list = KANA_ALL_DATA.filter(x => x.cat === 'tokushu');
      grid.innerHTML = `<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:6px;">${list.map(item => renderKanaCell(item)).join('')}</div>`;
    }
  }'''
        code = code[:m.start()] + new_grid_func + code[m.end():]

    # 6. Update KanaWritingQuiz: exclude tokushu when in hiragana
    old_quiz_start = '''    startQuiz() {
      let pool = KANA_ALL_DATA.filter(x => x.h && x.k && x.cat !== 'blank');
      if (this.currentCategory !== 'all') {
        pool = pool.filter(x => x.cat === this.currentCategory);
      }'''

    new_quiz_start = '''    startQuiz() {
      let pool = KANA_ALL_DATA.filter(x => x.h && x.k && x.cat !== 'blank');
      if (this.currentType === 'hiragana') {
        pool = pool.filter(x => x.cat !== 'tokushu');
      }
      if (this.currentCategory !== 'all') {
        pool = pool.filter(x => x.cat === this.currentCategory);
      }'''

    if old_quiz_start in code:
        code = code.replace(old_quiz_start, new_quiz_start)

    # 7. Update default levels
    code = code.replace("let currentWritingQuizLevel = 'N5';", "let currentWritingQuizLevel = 'N1';")
    code = code.replace("let currentKanjiListLevel = 'N5';", "let currentKanjiListLevel = 'N1';")

    with open('app.html', 'w', encoding='utf-8') as f:
        f.write(code)

    with open('📱_日本語学習アプリ.html', 'w', encoding='utf-8') as f:
        f.write(code)

    print("app.html and 📱_日本語学習アプリ.html updated successfully!")

if __name__ == '__main__':
    update_kanji_engine()
    update_app_html()
