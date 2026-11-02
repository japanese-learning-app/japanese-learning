# -*- coding: utf-8 -*-
"""
Rebuilds ALL 5 JLPT Grammar Textbooks (N1, N2, N3, N4, N5):
- Ensures 100% robust data binding:
  quizSource = window.JLPT_N{lvl}_QUIZ_DATA || window.JLPT_N{lvl}_GRAMMAR_QUIZ_DATA || []
  detailsMap = window.JLPT_N{lvl}_GRAMMAR_DETAILS || {}
- Dynamically creates clean UNITS_DATA for all grammar items (10-15 per unit)
- Renders full 9 core sections matching N2 masterpiece
- Audio TTS with <rt> sanitization
- Bookmarking & Mastered tracking
"""

import json
import re
import os

repo_dir = '/Users/yamauchimiku/Documents/GitHub/japanese-learning'

LEVEL_SPECS = {
    'n1': {'name': 'N1', 'title': 'JLPT N1 文法マスターテキスト', 'max_gid': 127},
    'n2': {'name': 'N2', 'title': 'JLPT N2 文法マスターテキスト', 'max_gid': 195},
    'n3': {'name': 'N3', 'title': 'JLPT N3 文法マスターテキスト', 'max_gid': 182},
    'n4': {'name': 'N4', 'title': 'JLPT N4 文法マスターテキスト', 'max_gid': 62},
    'n5': {'name': 'N5', 'title': 'JLPT N5 文法マスターテキスト', 'max_gid': 46}
}

for lvl, spec in LEVEL_SPECS.items():
    L = spec['name']
    l_lower = lvl
    max_gid = spec['max_gid']
    
    # 1. Read grammar quiz data
    qpath = f'{repo_dir}/database/jlpt_{l_lower}_grammar_quiz_data.js'
    with open(qpath, 'r', encoding='utf-8') as f:
        q_raw = f.read()
        
    s_idx = q_raw.find('[')
    e_idx = q_raw.rfind(']')
    q_data = json.loads(q_raw[s_idx:e_idx+1]) if (s_idx >= 0 and e_idx >= 0) else []
    
    unique_grammars = {}
    for q in q_data:
        gid = q.get('grammar_id')
        if gid and gid not in unique_grammars:
            unique_grammars[gid] = {
                'id': gid,
                'name': q.get('grammar', f'文法 #{gid}'),
                'reading': q.get('reading', ''),
                'meaning_en': q.get('meaning_en', '')
            }
            
    actual_max = max(unique_grammars.keys()) if unique_grammars else max_gid
    
    # 2. Build Units Data dynamically
    units = []
    unit_size = 12 if actual_max > 100 else 10
    total_units = (actual_max + unit_size - 1) // unit_size
    
    for u_idx in range(total_units):
        start_gid = u_idx * unit_size + 1
        end_gid = min(actual_max, (u_idx + 1) * unit_size)
        gids = list(range(start_gid, end_gid + 1))
        
        group_name = "基礎編（まずはこれを覚えよう！）" if u_idx < total_units // 2 else "発展・合格必須編（差がつく重要文法）"
        u_name = f"{u_idx + 1}. 第 {u_idx + 1} 章 ({start_gid}〜{end_gid})"
        u_en = f"Chapter {u_idx + 1} (Patterns #{start_gid} - #{end_gid})"
        
        units.append({
            'id': f'unit_{u_idx+1:02d}',
            'group': group_name,
            'name': u_name,
            'name_en': u_en,
            'gids': gids
        })
        
    units_json = json.dumps(units, ensure_ascii=False, indent=6)

    # 3. Build HTML
    page_html = f'''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JLPT {L} 文法マスターテキスト（教科書・解説）</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+JP:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary-blue: #1995AD;
      --primary-blue-dark: #127285;
      --primary-blue-light: #43B0C4;
      --primary-blue-pale: #EDF7F9;
      --primary-blue-border: #A1D6E2;

      --sakura-pink-bg: #FAF1F3;
      --sakura-pink-soft: #FDF7F8;
      --sakura-pink-accent: #E8A4B2;
      --sakura-pink-deep: #B8596E;
      --sakura-pink-hover: #CE5A73;
      --sakura-pink-border: #F2D5DB;

      --point-navy: #4D648D;
      --point-ice: #D0E1F9;

      --text-primary: #1F2D3D;
      --text-secondary: #4D648D;
      --text-muted: #6B7C8E;

      --card-bg: #FFFFFF;
      --card-border: #F2D5DB;
      --card-shadow: 0 8px 24px rgba(25, 149, 173, 0.07);

      --correct-green: #2E7D32;
      --correct-bg: #E8F5E9;
      --correct-border: #81C784;

      --app-font: 'Inter', "Yu Gothic", YuGothic, "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }}
    body {{
      font-family: var(--app-font);
      background-color: var(--sakura-pink-bg);
      color: var(--text-primary);
      line-height: 1.7;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}

    ruby {{ ruby-position: over; ruby-align: center; }}
    ruby rt {{
      font-size: 0.54em;
      color: var(--primary-blue-dark);
      font-weight: 600;
      user-select: none;
      letter-spacing: 0;
      line-height: 1;
      transform: translateY(-2px);
    }}
    body.hide-furigana ruby rt {{ display: none !important; }}

    /* Layout */
    .app-header {{
      background: #FFFFFF;
      border-bottom: 1.5px solid var(--sakura-pink-border);
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 2px 12px rgba(184, 89, 110, 0.04);
    }}
    .header-inner {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 10px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }}
    .header-left {{ display: flex; align-items: center; gap: 12px; }}
    .header-title-box h1 {{
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--sakura-pink-deep);
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .header-title-box p {{ font-size: 0.75rem; color: var(--text-muted); }}

    .header-nav-btn {{
      padding: 7px 12px;
      border-radius: 10px;
      border: 1px solid var(--sakura-pink-border);
      background: var(--sakura-pink-soft);
      color: var(--sakura-pink-deep);
      font-size: 12.5px;
      font-weight: 700;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}
    .header-nav-btn:hover {{ background: #FFFFFF; border-color: var(--sakura-pink-deep); }}

    .main-layout {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 20px;
      display: grid;
      grid-template-columns: 360px 1fr;
      gap: 24px;
      flex: 1;
      width: 100%;
    }}

    @media (max-width: 900px) {{
      .main-layout {{ grid-template-columns: 1fr; padding: 12px; }}
      .sidebar-panel {{ display: none; }}
    }}

    /* Sidebar */
    .sidebar-panel {{
      background: #FFFFFF;
      border: 1.5px solid var(--sakura-pink-border);
      border-radius: 16px;
      display: flex;
      flex-direction: column;
      height: calc(100vh - 120px);
      position: sticky;
      top: 80px;
      overflow: hidden;
      box-shadow: var(--card-shadow);
    }}
    .sidebar-top {{ padding: 16px; border-bottom: 1px solid var(--sakura-pink-border); }}
    .sidebar-search-wrap {{ position: relative; }}
    .sidebar-search-input {{
      width: 100%;
      padding: 9px 14px 9px 36px;
      border-radius: 10px;
      border: 1px solid var(--sakura-pink-border);
      background: var(--sakura-pink-soft);
      font-size: 13px;
      color: var(--text-primary);
      outline: none;
    }}
    .sidebar-search-input:focus {{ border-color: var(--primary-blue); background: #FFFFFF; }}
    .sidebar-search-icon {{ position: absolute; left: 12px; top: 50%; transform: translateY(-50%); color: var(--text-muted); font-size: 14px; }}

    .sidebar-filter-tabs {{ display: flex; gap: 6px; margin-top: 10px; }}
    .sidebar-tab-btn {{
      flex: 1;
      padding: 6px;
      border-radius: 8px;
      border: 1px solid var(--sakura-pink-border);
      background: var(--sakura-pink-soft);
      font-size: 11.5px;
      font-weight: 700;
      color: var(--text-secondary);
      cursor: pointer;
      text-align: center;
    }}
    .sidebar-tab-btn.active {{ background: var(--primary-blue); color: #FFFFFF; border-color: var(--primary-blue); }}

    .sidebar-cats-scroll {{ flex: 1; overflow-y: auto; padding: 12px; }}
    .cat-group-heading {{ font-size: 11px; font-weight: 800; color: var(--sakura-pink-deep); margin: 12px 6px 6px; text-transform: uppercase; }}
    .cat-unit-card {{ border: 1px solid var(--sakura-pink-border); border-radius: 10px; margin-bottom: 8px; overflow: hidden; }}
    .cat-unit-header {{
      padding: 10px 12px;
      background: var(--sakura-pink-soft);
      display: flex;
      align-items: center;
      justify-content: space-between;
      cursor: pointer;
      font-size: 12.5px;
      font-weight: 700;
      color: var(--text-primary);
    }}
    .cat-unit-header:hover {{ background: #FCEEF1; }}
    .cat-unit-count {{ font-size: 11px; background: #FFFFFF; padding: 2px 8px; border-radius: 12px; border: 1px solid var(--sakura-pink-border); color: var(--text-muted); }}
    .cat-grammar-list {{ display: none; padding: 6px 0; background: #FFFFFF; }}
    .cat-unit-card.expanded .cat-grammar-list {{ display: block; }}
    .cat-grammar-item {{
      padding: 8px 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 13px;
      cursor: pointer;
      border-left: 3px solid transparent;
      transition: all 0.15s;
    }}
    .cat-grammar-item:hover {{ background: var(--primary-blue-pale); color: var(--primary-blue-dark); }}
    .cat-grammar-item.active {{ background: var(--primary-blue-pale); border-left-color: var(--primary-blue); color: var(--primary-blue-dark); font-weight: 700; }}
    .cat-grammar-info {{ display: flex; flex-direction: column; gap: 2px; }}
    .cat-grammar-ja {{ font-size: 13.5px; }}
    .cat-grammar-en {{ font-size: 11px; color: var(--text-muted); }}

    /* Main Lesson Card Container */
    .lesson-main-content {{ display: flex; flex-direction: column; gap: 20px; }}
    .lesson-card {{
      background: #FFFFFF;
      border: 1.5px solid var(--sakura-pink-border);
      border-radius: 20px;
      padding: 28px;
      box-shadow: var(--card-shadow);
    }}
    .lesson-header {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 16px;
      padding-bottom: 18px;
      border-bottom: 1.5px solid var(--sakura-pink-border);
      margin-bottom: 24px;
    }}
    .grammar-name {{ font-size: 1.7rem; font-weight: 800; color: var(--text-primary); }}
    .grammar-meaning-en {{ font-size: 0.95rem; color: var(--primary-blue-dark); font-weight: 600; margin-top: 4px; display: block; }}

    /* 9 Core Sections */
    .section-tag {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 12.5px;
      font-weight: 800;
      color: var(--primary-blue-dark);
      background: var(--primary-blue-pale);
      border: 1px solid var(--primary-blue-border);
      padding: 4px 12px;
      border-radius: 8px;
      margin-bottom: 12px;
    }}
    .connection-box {{
      background: #FFFFFF;
      border: 1.5px solid var(--primary-blue-border);
      border-left: 6px solid var(--primary-blue);
      border-radius: 12px;
      padding: 16px 20px;
      font-size: 14.5px;
      line-height: 1.8;
      margin-bottom: 24px;
    }}
    .connection-notes {{ font-size: 12.5px; color: var(--text-muted); margin-top: 8px; border-top: 1px dashed #E2E8F0; padding-top: 8px; }}

    /* Examples */
    .examples-wrap {{ display: flex; flex-direction: column; gap: 12px; margin-bottom: 24px; }}
    .example-card {{
      background: #FFFFFF;
      border: 1.5px solid #E2E8F0;
      border-radius: 14px;
      padding: 14px 18px;
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 12px;
      transition: all 0.2s;
    }}
    .example-card:hover {{ border-color: var(--primary-blue-border); box-shadow: 0 4px 12px rgba(25, 149, 173, 0.06); }}
    .example-ja {{ font-size: 15px; color: var(--text-primary); font-weight: 600; }}
    .example-en {{ font-size: 12.5px; color: var(--text-muted); margin-top: 4px; }}
    .tts-btn {{
      background: var(--sakura-pink-soft);
      border: 1px solid var(--sakura-pink-border);
      border-radius: 8px;
      width: 32px;
      height: 32px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 15px;
      flex-shrink: 0;
      transition: transform 0.15s;
    }}
    .tts-btn:hover {{ transform: scale(1.08); background: #FFFFFF; }}

    /* Nuance Box (Cyan) */
    .nuance-box {{
      background: var(--primary-blue-pale);
      border: 1.5px solid var(--primary-blue-border);
      border-radius: 14px;
      padding: 18px 20px;
      margin-bottom: 24px;
    }}
    .nuance-title {{ font-size: 13.5px; font-weight: 800; color: var(--primary-blue-dark); margin-bottom: 8px; display: flex; align-items: center; gap: 6px; }}
    .nuance-ja {{ font-size: 14px; color: var(--text-primary); line-height: 1.8; }}
    .nuance-en {{ font-size: 12.5px; color: var(--text-secondary); margin-top: 6px; }}

    /* Trap Box (Amber Yellow) */
    .trap-box {{
      background: #FFFBEB;
      border: 1.5px solid #FDE68A;
      border-radius: 14px;
      padding: 18px 20px;
      margin-bottom: 24px;
    }}
    .trap-title {{ font-size: 13.5px; font-weight: 800; color: #B45309; margin-bottom: 8px; display: flex; align-items: center; gap: 6px; }}
    .trap-ja {{ font-size: 14px; color: #78350F; line-height: 1.8; }}
    .trap-en {{ font-size: 12.5px; color: #92400E; margin-top: 6px; }}

    /* Contrast Cards */
    .contrast-cards-wrap {{ display: flex; flex-direction: column; gap: 10px; margin-top: 12px; }}
    .contrast-card {{
      background: #FFFFFF;
      border: 1.5px solid #F1E5E8;
      border-radius: 12px;
      padding: 12px 16px;
    }}
    .contrast-header {{ display: flex; align-items: center; gap: 12px; margin-bottom: 6px; }}
    .contrast-badge {{ font-size: 11.5px; font-weight: 800; padding: 3px 8px; border-radius: 6px; }}
    .contrast-badge.wrong {{ background: #FEE2E2; color: #991B1B; }}
    .contrast-badge.correct {{ background: #DCFCE7; color: #166534; }}
    .contrast-reason {{ font-size: 12px; color: var(--text-muted); }}
    .contrast-sentence {{ font-size: 14px; color: var(--text-primary); }}

    /* Comparison Table */
    .comparison-table-wrap {{
      background: #FFFFFF;
      border: 1.5px solid #E2E8F0;
      border-radius: 14px;
      overflow-x: auto;
      margin-bottom: 24px;
    }}
    .comp-table {{ width: 100%; border-collapse: collapse; font-size: 13.5px; text-align: left; }}
    .comp-table th {{ background: var(--primary-blue-pale); color: var(--primary-blue-dark); padding: 12px 16px; font-weight: 800; border-bottom: 1.5px solid var(--primary-blue-border); }}
    .comp-table td {{ padding: 14px 16px; border-bottom: 1px solid #E2E8F0; vertical-align: top; }}
    .comp-badge {{ display: inline-block; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 6px; margin-bottom: 4px; }}
    .comp-badge.bad {{ background: #FEE2E2; color: #991B1B; }}
    .comp-badge.both {{ background: #FEF3C7; color: #92400E; }}
    .comp-badge.neutral {{ background: #E0E7FF; color: #3730A3; }}

    /* Mini Quizzes (Sakura Pink Box) */
    .mini-quiz-box {{
      background: var(--sakura-pink-soft);
      border: 1.5px solid var(--sakura-pink-border);
      border-radius: 18px;
      padding: 24px;
      margin-bottom: 24px;
    }}
    .quiz-title-head {{ font-size: 1.1rem; font-weight: 800; color: var(--sakura-pink-deep); margin-bottom: 16px; display: flex; align-items: center; justify-content: space-between; }}
    .quiz-card {{
      background: #FFFFFF;
      border: 1.5px solid var(--sakura-pink-border);
      border-radius: 14px;
      padding: 18px;
      margin-bottom: 14px;
    }}
    .quiz-q-num {{ font-size: 12px; font-weight: 800; color: var(--primary-blue-dark); margin-bottom: 6px; }}
    .quiz-question-sentence {{ font-size: 15px; font-weight: 700; color: var(--text-primary); margin-bottom: 14px; }}
    .quiz-choices-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }}
    @media (max-width: 600px) {{ .quiz-choices-grid {{ grid-template-columns: 1fr; }} }}
    .quiz-choice-btn {{
      background: #FFFFFF;
      border: 1.5px solid #E2E8F0;
      border-radius: 10px;
      padding: 10px 14px;
      font-size: 13.5px;
      font-weight: 600;
      color: var(--text-primary);
      text-align: left;
      cursor: pointer;
      transition: all 0.15s;
    }}
    .quiz-choice-btn:hover {{ border-color: var(--primary-blue); background: var(--primary-blue-pale); }}
    .quiz-choice-btn.is-correct {{ background: #DCFCE7 !important; border-color: #86EFAC !important; color: #166534 !important; font-weight: 800; }}
    .quiz-choice-btn.is-wrong {{ background: #FEE2E2 !important; border-color: #FCA5A5 !important; color: #991B1B !important; }}
    .quiz-feedback {{ display: none; margin-top: 12px; padding: 12px; border-radius: 10px; font-size: 13px; }}
    .quiz-feedback.is-correct {{ background: #F0FDF4; border: 1px solid #BBF7D0; color: #166534; }}
    .quiz-feedback.is-wrong {{ background: #FEF2F2; border: 1px solid #FECACA; color: #991B1B; }}

    /* Dojo CTA */
    .dojo-cta-btn-clean {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      width: 100%;
      padding: 14px 20px;
      border-radius: 14px;
      background: linear-gradient(135deg, var(--sakura-pink-deep), var(--sakura-pink-hover));
      color: #FFFFFF;
      font-size: 15px;
      font-weight: 800;
      text-decoration: none;
      box-shadow: 0 4px 16px rgba(184, 89, 110, 0.25);
      transition: transform 0.2s;
    }}
    .dojo-cta-btn-clean:hover {{ transform: translateY(-2px); }}

    /* Sticky Bottom Nav */
    .sticky-bottom-nav {{
      position: sticky;
      bottom: 0;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(10px);
      border-top: 1.5px solid var(--sakura-pink-border);
      padding: 10px 20px;
      z-index: 99;
      display: flex;
      align-items: center;
      justify-content: space-between;
      max-width: 1440px;
      margin: 0 auto;
      width: 100%;
    }}
    .nav-arrow-btn {{
      padding: 8px 16px;
      border-radius: 10px;
      border: 1px solid var(--sakura-pink-border);
      background: #FFFFFF;
      font-size: 13px;
      font-weight: 700;
      color: var(--text-primary);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .nav-arrow-btn:hover:not(:disabled) {{ background: var(--sakura-pink-soft); border-color: var(--sakura-pink-deep); }}
    .nav-arrow-btn:disabled {{ opacity: 0.4; cursor: not-allowed; }}
  </style>
</head>
<body>

  <!-- App Header -->
  <header class="app-header">
    <div class="header-inner">
      <div class="header-left">
        <a href="jlpt_practice.html" class="header-nav-btn">← 総合道場へ</a>
        <div class="header-title-box">
          <h1>📖 JLPT {L} 文法マスターテキスト</h1>
          <p>全{actual_max}項目 完全網羅・理解度ミニ演習付き</p>
        </div>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <button id="furiganaToggle" class="header-nav-btn" onclick="toggleFurigana()">ふりがな: ON</button>
        <a href="jlpt_{l_lower}_grammar_quiz.html" class="header-nav-btn" style="background:var(--primary-blue); color:white; border-color:var(--primary-blue);">📝 演習道場へ →</a>
      </div>
    </div>
  </header>

  <!-- Main Layout -->
  <div class="main-layout">
    <!-- Sidebar -->
    <aside class="sidebar-panel">
      <div class="sidebar-top">
        <div class="sidebar-search-wrap">
          <span class="sidebar-search-icon">🔍</span>
          <input type="text" id="sidebarSearchInput" class="sidebar-search-input" placeholder="{L}文法を検索（名前・意味・読み）..." oninput="handleSearch(this.value)">
        </div>
        <div class="sidebar-filter-tabs">
          <button class="sidebar-tab-btn active" id="tab-all" onclick="setFilter('all')">全{actual_max}項目</button>
          <button class="sidebar-tab-btn" id="tab-star" onclick="setFilter('star')">⭐ 復習</button>
          <button class="sidebar-tab-btn" id="tab-done" onclick="setFilter('done')">✓ 読了</button>
        </div>
      </div>
      <div class="sidebar-cats-scroll" id="sidebarCatsList"></div>
    </aside>

    <!-- Main Lesson Content -->
    <main class="lesson-main-content">
      <div id="lessonCardContainer"></div>
    </main>
  </div>

  <!-- Sticky Bottom Bar -->
  <footer class="sticky-bottom-nav">
    <button class="nav-arrow-btn" id="stickyBtnPrev" onclick="navigateGrammar(-1)">← 前の文法</button>
    <div id="stickyLessonTitle" style="font-weight:800; font-size:14px; color:var(--text-primary);">第 1 課</div>
    <button class="nav-arrow-btn" id="stickyBtnNext" onclick="navigateGrammar(1)">次の文法 →</button>
  </footer>

  <!-- Scripts -->
  <script src="auth.js"></script>
  <script src="user_progress.js"></script>
  <script src="database/dictionary_data.js"></script>
  <script src="database/jlpt_{l_lower}_grammar_details.js"></script>
  <script src="database/jlpt_{l_lower}_grammar_quiz_data.js"></script>

  <script>
    const UNITS_DATA = {units_json};

    // User State
    const userBookmarks = new Set(JSON.parse(localStorage.getItem('jlpt_{l_lower}_bookmarks') || '[]'));
    const userMastered = new Set(JSON.parse(localStorage.getItem('jlpt_{l_lower}_mastered') || '[]'));

    // Audio TTS Helper with <rt> sanitization
    window.speakJapaneseText = function(text) {{
      if (!text) return;
      const clean = text
        .replace(/<rt>[\s\S]*?<\/rt>/gi, '')
        .replace(/<[^>]+>/g, '')
        .replace(/（\s*）|\(　*\)|（　*）/g, '、')
        .replace(/\s+/g, ' ')
        .trim();

      if ('speechSynthesis' in window) {{
        window.speechSynthesis.cancel();
        const u = new SpeechSynthesisUtterance(clean);
        u.lang = 'ja-JP';
        u.rate = 0.95;
        window.speechSynthesis.speak(u);
      }}
    }};

    // Build Grammar Maps (Robust Dual Fallback)
    const grammarMap = new Map();
    const grammarQuestionsMap = new Map();

    const quizSource = window.JLPT_{L}_QUIZ_DATA || window.JLPT_{L}_GRAMMAR_QUIZ_DATA || [];
    quizSource.forEach(q => {{
      const gid = q.grammar_id;
      if (!grammarMap.has(gid)) {{
        grammarMap.set(gid, {{
          id: gid,
          name: q.grammar,
          reading: q.reading || '',
          meaning_en: q.meaning_en || '',
          similar: q.similar || '',
          sample_sentence_ja: q.sentence_jp_ruby || q.sentence_jp,
          sample_sentence_en: q.sentence_en || ''
        }});
      }}
      if (!grammarQuestionsMap.has(gid)) {{
        grammarQuestionsMap.set(gid, []);
      }}
      grammarQuestionsMap.get(gid).push(q);
    }});

    const detailsMap = window.JLPT_{L}_GRAMMAR_DETAILS || {{}};

    let currentGid = 1;
    let currentFilter = 'all';
    let searchQuery = '';

    function toggleFurigana() {{
      document.body.classList.toggle('hide-furigana');
      const isHidden = document.body.classList.contains('hide-furigana');
      document.getElementById('furiganaToggle').textContent = isHidden ? 'ふりがな: OFF' : 'ふりがな: ON';
    }}

    function setFilter(filter) {{
      currentFilter = filter;
      document.querySelectorAll('.sidebar-tab-btn').forEach(b => b.classList.remove('active'));
      const activeBtn = document.getElementById(`tab-${{filter}}`);
      if (activeBtn) activeBtn.classList.add('active');
      renderSidebar();
    }}

    function handleSearch(q) {{
      searchQuery = (q || '').trim();
      renderSidebar();
    }}

    function renderSidebar() {{
      const container = document.getElementById('sidebarCatsList');
      if (!container) return;
      container.innerHTML = '';
      let currentGroup = '';

      UNITS_DATA.forEach(unit => {{
        if (unit.group !== currentGroup) {{
          currentGroup = unit.group;
          const groupHead = document.createElement('div');
          groupHead.className = 'cat-group-heading';
          groupHead.textContent = currentGroup;
          container.appendChild(groupHead);
        }}

        const filteredGids = unit.gids.filter(gid => {{
          const g = grammarMap.get(gid);
          if (!g) return false;
          if (currentFilter === 'star' && !userBookmarks.has(gid)) return false;
          if (currentFilter === 'done' && !userMastered.has(gid)) return false;
          if (searchQuery) {{
            const q = searchQuery.toLowerCase();
            const mName = g.name.toLowerCase().includes(q);
            const mRead = (g.reading || '').toLowerCase().includes(q);
            const mMean = (g.meaning_en || '').toLowerCase().includes(q);
            if (!mName && !mRead && !mMean) return false;
          }}
          return true;
        }});

        if (filteredGids.length === 0 && (currentFilter !== 'all' || searchQuery)) return;

        const isCurrentInUnit = unit.gids.includes(currentGid);
        const card = document.createElement('div');
        card.className = `cat-unit-card ${{isCurrentInUnit ? 'expanded' : ''}}`;

        const head = document.createElement('div');
        head.className = 'cat-unit-header';
        head.innerHTML = `
          <span>${{unit.name}}</span>
          <span class="cat-unit-count">${{filteredGids.length}}</span>
        `;
        head.onclick = () => card.classList.toggle('expanded');

        const list = document.createElement('div');
        list.className = 'cat-grammar-list';

        filteredGids.forEach(gid => {{
          const g = grammarMap.get(gid);
          if (!g) return;
          const item = document.createElement('div');
          item.className = `cat-grammar-item ${{gid === currentGid ? 'active' : ''}}`;
          item.onclick = () => selectGrammar(gid);

          let icons = '';
          if (userMastered.has(gid)) icons += '✓ ';
          if (userBookmarks.has(gid)) icons += '⭐ ';

          item.innerHTML = `
            <div class="cat-grammar-info">
              <span class="cat-grammar-ja">${{g.name}}</span>
              <span class="cat-grammar-en">${{g.meaning_en}}</span>
            </div>
            <div style="font-size:12px; color:var(--sakura-pink-deep); font-weight:800;">${{icons}}</div>
          `;
          list.appendChild(item);
        }});

        card.appendChild(head);
        card.appendChild(list);
        container.appendChild(card);
      }});
    }}

    function selectGrammar(gid) {{
      currentGid = gid;
      renderSidebar();
      renderLessonContent(gid);
      updateStickyNav();
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function navigateGrammar(delta) {{
      const next = currentGid + delta;
      if (next >= 1 && next <= {actual_max}) {{
        selectGrammar(next);
      }}
    }}

    function updateStickyNav() {{
      const title = document.getElementById('stickyLessonTitle');
      const prevBtn = document.getElementById('stickyBtnPrev');
      const nextBtn = document.getElementById('stickyBtnNext');
      const g = grammarMap.get(currentGid);
      if (title && g) title.textContent = `第 ${{currentGid}} 課 : ${{g.name}}`;
      if (prevBtn) prevBtn.disabled = (currentGid <= 1);
      if (nextBtn) nextBtn.disabled = (currentGid >= {actual_max});
    }}

    function toggleBookmark(gid) {{
      if (userBookmarks.has(gid)) userBookmarks.delete(gid);
      else userBookmarks.add(gid);
      localStorage.setItem('jlpt_{l_lower}_bookmarks', JSON.stringify([...userBookmarks]));
      renderLessonContent(gid);
      renderSidebar();
    }}

    function toggleMastered(gid) {{
      if (userMastered.has(gid)) userMastered.delete(gid);
      else userMastered.add(gid);
      localStorage.setItem('jlpt_{l_lower}_mastered', JSON.stringify([...userMastered]));
      renderLessonContent(gid);
      renderSidebar();
    }}

    function renderLessonContent(gid) {{
      const container = document.getElementById('lessonCardContainer');
      if (!container) return;
      const g = grammarMap.get(gid) || {{ id: gid, name: `文法 #${{gid}}`, meaning_en: '' }};
      const d = detailsMap[String(gid)] || {{}};

      const isStarred = userBookmarks.has(gid);
      const isDone = userMastered.has(gid);
      const qList = (grammarQuestionsMap.get(gid) || []).slice(0, 4);

      // Contrast Cards
      let contrastHtml = '';
      if (d.contrast && d.contrast.length) {{
        contrastHtml = `
          <div class="contrast-cards-wrap">
            ${{d.contrast.map(c => `
              <div class="contrast-card">
                <div class="contrast-header">
                  <span class="contrast-badge ${{c.type}}">${{c.label}}</span>
                  <span class="contrast-reason">💡 ${{c.reason_ja || ''}} / ${{c.reason_en || ''}}</span>
                </div>
                <div class="contrast-sentence">${{c.sentence}}</div>
              </div>
            `).join('')}}
          </div>
        `;
      }}

      // Comparison Table
      let compHtml = '';
      if (d.comparison && d.comparison.length) {{
        compHtml = `
          <div class="section-tag" style="margin-top:20px;">🔍 似た文法との違い・使い分け表</div>
          <div class="comparison-table-wrap">
            <table class="comp-table">
              <thead>
                <tr>
                  <th style="width:25%;">文法形式</th>
                  <th style="width:45%;">ニュアンス・使い分け</th>
                  <th style="width:30%;">代表例文</th>
                </tr>
              </thead>
              <tbody>
                ${{d.comparison.map(row => `
                  <tr>
                    <td>
                      <strong>${{row.form}}</strong><br>
                      <small style="color:var(--text-muted);">${{row.form_en || ''}}</small>
                    </td>
                    <td>
                      <span class="comp-badge ${{row.badge_type || 'both'}}">${{row.badge || '使い分け'}}</span><br>
                      ${{row.nuance_ja || ''}}<br>
                      <small style="color:var(--text-secondary);">${{row.nuance_en || ''}}</small>
                    </td>
                    <td style="font-size:13px;">${{row.example || ''}}</td>
                  </tr>
                `).join('')}}
              </tbody>
            </table>
          </div>
        `;
      }}

      // Examples Cards
      let examplesHtml = '';
      if (qList.length) {{
        examplesHtml = qList.map((q, idx) => `
          <div class="example-card">
            <div>
              <div class="example-ja">${{q.sentence_jp_ruby || q.sentence_jp}}</div>
              <div class="example-en">${{q.sentence_en || ''}}</div>
            </div>
            <button class="tts-btn" onclick="speakJapaneseText('${{(q.sentence_jp || '').replace(/'/g, "\\\\'")}}')" title="音声再生">🔊</button>
          </div>
        `).join('');
      }}

      // Mini Quizzes
      let quizHtml = '';
      if (qList.length) {{
        quizHtml = `
          <div class="mini-quiz-box">
            <div class="quiz-title-head">
              <span>✏️ 理解度チェック（その場で解けるミニ特訓 全${{qList.length}}問）</span>
              <span style="font-size:12px; color:var(--text-muted);">即時判定</span>
            </div>
            ${{qList.map((q, qIdx) => `
              <div class="quiz-card" id="qcard-${{qIdx}}">
                <div class="quiz-q-num">第 ${{qIdx + 1}} 問</div>
                <div class="quiz-question-sentence">${{q.question_ruby || q.question}}</div>
                <div class="quiz-choices-grid">
                  ${{q.choices.map((c, cIdx) => `
                    <button class="quiz-choice-btn" onclick="checkMiniQuiz(${{qIdx}}, ${{cIdx}}, ${{q.answer}})">
                      ${{cIdx + 1}}. ${{c}}
                    </button>
                  `).join('')}}
                </div>
                <div class="quiz-feedback" id="qfb-${{qIdx}}">
                  <div id="qfb-status-${{qIdx}}" style="font-weight:800; margin-bottom:4px;"></div>
                  <div style="margin-top:6px; display:flex; align-items:flex-start; justify-content:space-between; gap:10px;">
                    <div><strong>正解の文:</strong> ${{q.sentence_jp_ruby || q.sentence_jp}}</div>
                    <button type="button" class="tts-btn" onclick="speakJapaneseText('${{(q.sentence_jp || '').replace(/'/g, "\\\\'")}}')" title="音声再生">🔊</button>
                  </div>
                  <div style="margin-top:4px; font-size:12px; color:var(--text-muted);">${{q.notes || ''}}</div>
                </div>
              </div>
            `).join('')}}
          </div>
        `;
      }}

      container.innerHTML = `
        <article class="lesson-card">
          <header class="lesson-header">
            <div>
              <h1 class="grammar-name">${{g.name}}</h1>
              <span class="grammar-meaning-en">${{g.meaning_en}}</span>
            </div>
            <div style="display:flex; gap:8px;">
              <button class="header-nav-btn" onclick="toggleBookmark(${{gid}})">
                ${{isStarred ? '⭐ 復習中' : '⭐ 復習'}}
              </button>
              <button class="header-nav-btn" onclick="toggleMastered(${{gid}})" style="${{isDone ? 'background:#DCFCE7; color:#166534; border-color:#86EFAC;' : ''}}">
                ${{isDone ? '✓ 読了済み' : '✓ 読了'}}
              </button>
            </div>
          </header>

          <!-- 1. Connection & Rules -->
          <div class="section-tag">📐 接続と文法規則 (Form & Connection)</div>
          <div class="connection-box">
            ${{d.formula || '動詞／名詞 ＋ <strong>' + g.name + '</strong>'}}
            <div class="connection-notes">
              ${{d.notes_ja || '文脈に合わせて正しく接続します。'}}<br>
              <small>${{d.notes_en || ''}}</small>
            </div>
          </div>

          <!-- 2. Practical Examples -->
          <div class="section-tag">📝 実践例文 (Practical Examples)</div>
          <div class="examples-wrap">
            ${{examplesHtml}}
          </div>

          <!-- 3. Core Nuance -->
          <div class="nuance-box">
            <div class="nuance-title">💡 コアニュアンス (Core Nuance)</div>
            <div class="nuance-ja">${{d.nuance_ja || ''}}</div>
            <div class="nuance-en">${{d.nuance_en || ''}}</div>
          </div>

          <!-- 4. Trap (Common Pitfalls) -->
          <div class="trap-box">
            <div class="trap-title">⚠️ 英語直訳の落とし穴 (Common Pitfalls & Traps)</div>
            <div class="trap-ja">${{d.trap_ja || ''}}</div>
            <div class="trap-en">${{d.trap_en || ''}}</div>
            ${{contrastHtml}}
          </div>

          <!-- 5. Comparison Table -->
          ${{compHtml}}

          <!-- 6. Mini Quiz -->
          ${{quizHtml}}

          <!-- 7. CTA -->
          <a href="jlpt_{l_lower}_grammar_quiz.html" class="dojo-cta-btn-clean">
            🥋 JLPT {L} 文法演習道場でさらに実戦特訓する →
          </a>
        </article>
      `;
    }}

    window.checkMiniQuiz = function(qIdx, choiceIdx, correctIdx) {{
      const card = document.getElementById(`qcard-${{qIdx}}`);
      const fb = document.getElementById(`qfb-${{qIdx}}`);
      const statusEl = document.getElementById(`qfb-status-${{qIdx}}`);
      if (!card || !fb) return;

      const btns = card.querySelectorAll('.quiz-choice-btn');
      btns.forEach((btn, idx) => {{
        btn.disabled = true;
        if (idx === correctIdx) btn.classList.add('is-correct');
        else if (idx === choiceIdx) btn.classList.add('is-wrong');
      }});

      const isCorrect = (choiceIdx === correctIdx);
      fb.style.display = 'block';
      fb.className = `quiz-feedback ${{isCorrect ? 'is-correct' : 'is-wrong'}}`;
      statusEl.textContent = isCorrect ? '🎉 正解！' : `不正解（正解は ${{correctIdx + 1}} 番です）`;
    }};

    window.addEventListener('DOMContentLoaded', () => {{
      renderSidebar();
      selectGrammar(1);
    }});
  </script>
</body>
</html>
'''

    out_file = f'{repo_dir}/jlpt_{l_lower}_grammar_textbook.html'
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(page_html)
    print(f"Rebuilt {out_file} successfully! (actual_max={actual_max}, units={len(units)})")
