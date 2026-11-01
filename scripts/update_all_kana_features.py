# -*- coding: utf-8 -*-
"""
Script to apply user requests:
1. カタカナ外来語・特殊音（24字）も1行3つ (repeat(3, 1fr))
2. いちばん上のタブ順: ひらがな -> JLPT漢字リスト -> 毎日漢字
3. ひらがな・カタカナの書き方アニメーション、自分で描くなぞり練習、筆順コマ送り (新画赤色)
"""

import re
import sys

def update_kanji_engine():
    path = 'js/kanji_engine.js'
    print(f"Updating {path}...")
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update fetchKanjiStrokes with fallback
    old_fetch = """  async function fetchKanjiStrokes(char) {
    if (KANJI_CACHE[char]) return KANJI_CACHE[char];
    try {
      const hex = char.charCodeAt(0).toString(16).padStart(5, '0');
      const url = `https://cdn.jsdelivr.net/gh/KanjiVG/kanjivg@master/kanji/${hex}.svg`;
      const res = await fetch(url);
      if (!res.ok) throw new Error("KanjiVG fetch failed: " + res.status);
      const svgText = await res.text();

      const pathMatches = [...svgText.matchAll(/<path[^>]*\\bd="([^"]+)"/g)];
      const paths = pathMatches.map(m => m[1]);

      const numMatches = [...svgText.matchAll(/<text[^>]*transform="matrix\\([^\\)]+\\s+([\\d\\.]+)\\s+([\\d\\.]+)\\)"[^>]*>(\\d+)<\\/text>/g)];
      const nums = numMatches.map(m => [parseFloat(m[1]), parseFloat(m[2])]);

      const data = { char, size: GRID, strokesCount: paths.length, paths, nums };
      KANJI_CACHE[char] = data;
      return data;
    } catch (e) {
      console.warn("KanjiVG fetch error for " + char, e);
      return null;
    }
  }"""

    new_fetch = """  async function fetchKanjiStrokes(char) {
    if (!char) return null;
    if (KANJI_CACHE[char]) return KANJI_CACHE[char];
    const hex = char.charCodeAt(0).toString(16).padStart(5, '0');
    const urls = [
      `https://cdn.jsdelivr.net/gh/KanjiVG/kanjivg@master/kanji/${hex}.svg`,
      `https://raw.githubusercontent.com/KanjiVG/kanjivg/master/kanji/${hex}.svg`
    ];

    for (const url of urls) {
      try {
        const res = await fetch(url);
        if (!res.ok) continue;
        const svgText = await res.text();

        const pathMatches = [...svgText.matchAll(/<path[^>]*\\bd="([^"]+)"/g)];
        const paths = pathMatches.map(m => m[1]);

        const numMatches = [...svgText.matchAll(/<text[^>]*transform="matrix\\([^\\)]+\\s+([\\d\\.]+)\\s+([\\d\\.]+)\\)"[^>]*>(\\d+)<\\/text>/g)];
        const nums = numMatches.map(m => [parseFloat(m[1]), parseFloat(m[2])]);

        const data = { char, size: GRID, strokesCount: paths.length, paths, nums };
        KANJI_CACHE[char] = data;
        return data;
      } catch (e) {
        // try next fallback url
      }
    }
    console.warn("KanjiVG fetch error for " + char);
    return null;
  }"""

    if old_fetch in content:
        content = content.replace(old_fetch, new_fetch)

    # 2. Update KanjiEngine methods (renderStage, renderStepGrid, toggleTrace, etc.)
    new_methods = """    replayAnimation(char, stageId = 'kanji-modal-stage', slowToggleId = 'kanji-slow-toggle', numToggleId = 'kanji-numbers-toggle') {
      const data = KANJI_CACHE[char];
      if (data) this.renderStage(data, stageId, slowToggleId, numToggleId);
    },

    toggleNumbers(stageId = 'kanji-modal-stage', numToggleId = 'kanji-numbers-toggle') {
      const checked = document.getElementById(numToggleId)?.checked;
      const g = document.getElementById(`${stageId}-numbers-layer`) || document.getElementById('kvg-numbers-layer');
      if (g) g.style.display = checked ? 'block' : 'none';
    },

    toggleTrace(char, stageId = 'kanji-modal-stage', btnId = 'btn-toggle-trace') {
      const stage = document.getElementById(stageId);
      const data = KANJI_CACHE[char];
      const btn = document.getElementById(btnId);
      if (!stage || !data) return;

      const isTracing = stage.classList.contains('tracing-on');
      const isKanaStudio = (stageId === 'kana-trace-stage');
      const tools = document.getElementById(isKanaStudio ? 'kana-trace-draw-tools' : 'kanji-trace-tools');

      if (isTracing) {
        stage.classList.remove('tracing-on');
        if (btn) btn.textContent = "✍ なぞり練習";
        if (tools) tools.style.display = 'none';
        this.renderStage(data, stageId, isKanaStudio ? 'kana-slow-toggle' : 'kanji-slow-toggle', isKanaStudio ? 'kana-numbers-toggle' : 'kanji-numbers-toggle');
      } else {
        stage.classList.add('tracing-on');
        if (btn) btn.textContent = "▶ お手本に戻る";
        if (tools) tools.style.display = 'flex';
        this.startTrace(stage, data);
      }
    },

    startTrace(container, data) {
      container.innerHTML = '';
      const size = data.size || GRID;

      const ghostSvg = svgEl("svg", {
        viewBox: `0 0 ${size} ${size}`,
        style: "position:absolute; inset:0; width:100%; height:100%; pointer-events:none; z-index:1;"
      });
      ghostSvg.appendChild(makeTianGridGuidelines(size));
      const strokeW = getInkWidth(data.strokesCount);
      data.paths.forEach(p => {
        ghostSvg.appendChild(svgEl("path", {
          d: p, fill: "none", stroke: "#CBD5E1",
          "stroke-width": strokeW, "stroke-linecap": "round", "stroke-linejoin": "round"
        }));
      });
      container.appendChild(ghostSvg);

      const canvas = document.createElement('canvas');
      const w = container.clientWidth || 220;
      const h = container.clientHeight || 220;
      canvas.width = w * window.devicePixelRatio;
      canvas.height = h * window.devicePixelRatio;
      canvas.style.width = w + "px";
      canvas.style.height = h + "px";
      canvas.style.position = "absolute";
      canvas.style.inset = "0";
      canvas.style.zIndex = "2";
      canvas.style.touchAction = "none";
      canvas.style.cursor = "crosshair";
      container.appendChild(canvas);

      const ctx = canvas.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';
      ctx.strokeStyle = '#0F172A';
      ctx.lineWidth = 6;

      canvas._history = [];
      let currentStroke = [];
      let drawing = false;

      const getPos = (e) => {
        const rect = canvas.getBoundingClientRect();
        return { x: e.clientX - rect.left, y: e.clientY - rect.top };
      };

      canvas.onpointerdown = (e) => {
        canvas.setPointerCapture(e.pointerId);
        drawing = true;
        currentStroke = [];
        const p = getPos(e);
        currentStroke.push(p);
        ctx.beginPath();
        ctx.moveTo(p.x, p.y);
      };

      canvas.onpointermove = (e) => {
        if (!drawing) return;
        const p = getPos(e);
        currentStroke.push(p);
        ctx.lineTo(p.x, p.y);
        ctx.stroke();
      };

      const stop = () => {
        if (!drawing) return;
        drawing = false;
        if (currentStroke.length > 0) {
          canvas._history.push([...currentStroke]);
        }
      };

      canvas.onpointerup = stop;
      canvas.onpointercancel = stop;

      container._canvas = canvas;
      container._clear = () => {
        canvas._history = [];
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      };
      container._undo = () => {
        if (!canvas._history || canvas._history.length === 0) return;
        canvas._history.pop();
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';
        ctx.strokeStyle = '#0F172A';
        ctx.lineWidth = 6;
        canvas._history.forEach(stroke => {
          if (stroke.length === 0) return;
          ctx.beginPath();
          ctx.moveTo(stroke[0].x, stroke[0].y);
          for (let i = 1; i < stroke.length; i++) {
            ctx.lineTo(stroke[i].x, stroke[i].y);
          }
          ctx.stroke();
        });
      };
    },

    renderStage(data, stageId = 'kanji-modal-stage', slowToggleId = 'kanji-slow-toggle', numToggleId = 'kanji-numbers-toggle') {
      const stage = document.getElementById(stageId);
      if (!stage) return;
      stage.innerHTML = '';
      stage.classList.remove('tracing-on');

      const isSlow = document.getElementById(slowToggleId)?.checked;
      const showNums = document.getElementById(numToggleId)?.checked ?? true;

      const size = data.size || GRID;
      const svg = svgEl("svg", { viewBox: `0 0 ${size} ${size}`, style: "width:100%; height:100%;" });
      svg.appendChild(makeTianGridGuidelines(size));

      const strokeW = getInkWidth(data.strokesCount);
      const pathNodes = [];

      data.paths.forEach((d) => {
        const p = svgEl("path", {
          d: d,
          fill: "none",
          stroke: "#2563EB",
          "stroke-width": strokeW,
          "stroke-linecap": "round",
          "stroke-linejoin": "round"
        });
        svg.appendChild(p);
        pathNodes.push(p);
      });

      const numG = svgEl("g", { id: `${stageId}-numbers-layer`, style: `display:${showNums ? 'block' : 'none'};` });
      if (data.nums) {
        data.nums.forEach(([x, y], i) => {
          const t = svgEl("text", {
            x: x, y: y,
            fill: "#1E40AF",
            "font-size": "9",
            "font-weight": "bold",
            "font-family": "sans-serif",
            opacity: "0.85"
          });
          t.textContent = i + 1;
          numG.appendChild(t);
        });
      }
      svg.appendChild(numG);
      stage.appendChild(svg);

      this.animatePaths(pathNodes, isSlow ? 750 : 380, stageId);
    },

    animatePaths(paths, durationPerStroke, stageId = 'kanji-modal-stage') {
      if (!this.currentAnimTimers) this.currentAnimTimers = {};
      if (this.currentAnimTimers[stageId]) {
        cancelAnimationFrame(this.currentAnimTimers[stageId]);
      }

      const lengths = paths.map(p => {
        const l = p.getTotalLength();
        p.style.strokeDasharray = l;
        p.style.strokeDashoffset = l;
        return l;
      });

      let currentIdx = 0;
      let startTime = null;

      const step = (timestamp) => {
        if (!startTime) startTime = timestamp;
        const elapsed = timestamp - startTime;
        const progress = Math.min(1, elapsed / durationPerStroke);

        const curPath = paths[currentIdx];
        const curLen = lengths[currentIdx];
        curPath.style.strokeDashoffset = curLen * (1 - progress);

        if (progress < 1) {
          this.currentAnimTimers[stageId] = requestAnimationFrame(step);
        } else {
          curPath.style.strokeDashoffset = 0;
          currentIdx++;
          if (currentIdx < paths.length) {
            startTime = null;
            this.currentAnimTimers[stageId] = requestAnimationFrame(step);
          }
        }
      };

      this.currentAnimTimers[stageId] = requestAnimationFrame(step);
    },

    renderStepGrid(data, gridId = 'kanji-modal-step-grid') {
      const grid = document.getElementById(gridId);
      if (!grid) return;
      grid.innerHTML = '';

      const size = data.size || GRID;
      const strokeW = getInkWidth(data.strokesCount);

      data.paths.forEach((_, stepIdx) => {
        const cell = document.createElement('div');
        cell.className = 'kanji-step-cell';

        const numTag = document.createElement('span');
        numTag.className = 'kanji-step-num';
        numTag.textContent = stepIdx + 1;
        cell.appendChild(numTag);

        const svg = svgEl("svg", { viewBox: `0 0 ${size} ${size}`, style: "width:100%; height:100%;" });
        svg.appendChild(makeTianGridGuidelines(size));

        for (let i = 0; i <= stepIdx; i++) {
          const isLatest = (i === stepIdx);
          svg.appendChild(svgEl("path", {
            d: data.paths[i],
            fill: "none",
            stroke: isLatest ? "#DC2626" : "#475569",
            "stroke-width": isLatest ? strokeW * 1.15 : strokeW,
            "stroke-linecap": "round",
            "stroke-linejoin": "round"
          }));
        }

        cell.appendChild(svg);
        grid.appendChild(cell);
      });
    }"""

    p1 = content.find("    replayAnimation(char) {")
    p2 = content.find("  };\n\n  // ============================================================\n  // 2. 毎日漢字スタイル")
    if p1 != -1 and p2 != -1:
        content = content[:p1] + new_methods + "\n" + content[p2:]
        print("KanjiEngine methods updated!")

    # 3. Update openStrokeModal for kana support
    old_modal_start = "      const lvl = kObj.level || (window.KanjiListEngine ? window.KanjiListEngine.currentLevel : 'N5');"
    new_modal_start = """      const isKana = /[\\u3040-\\u309F\\u30A0-\\u30FF]/.test(char);
      const lvl = kObj.level || (window.KanjiListEngine ? window.KanjiListEngine.currentLevel : 'N5');
      const lvlBadge = isKana ? (char >= '\\u30a0' ? 'カタカナ' : 'ひらがな') : `JLPT ${lvl}`;"""
    
    if old_modal_start in content and "const isKana =" not in content:
        content = content.replace(old_modal_start, new_modal_start)
        # Update badge
        content = content.replace("JLPT ${lvl}</span>", "${lvlBadge}</span>")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("js/kanji_engine.js write complete!")


NEW_HTML_TAB_BAR = """    <!-- 固定タブバーエリア（スクロールしても絶対に隠れない・めり込まない！） -->
    <div style="background:#FFFFFF; border-bottom:2px solid #E2ECF2; padding:10px 18px; flex-shrink:0; box-shadow:0 2px 6px rgba(0,0,0,0.03); z-index:10;">
      <div class="kanji-main-tabs">
        <button class="kanji-main-tab-btn active" id="tab-btn-writing-kana" onclick="switchWritingTab('kana')">あ かな学習（ひらがな・カタカナ）</button>
        <button class="kanji-main-tab-btn" id="tab-btn-writing-list" onclick="switchWritingTab('list')">📚 JLPT漢字リスト（書き順・筆順）</button>
        <button class="kanji-main-tab-btn" id="tab-btn-writing-quiz" onclick="switchWritingTab('quiz')">📝 毎日漢字書き取りテスト（毎日漢字スタイル）</button>
        <button class="kanji-main-tab-btn" id="tab-btn-writing-pdf" onclick="switchWritingTab('pdf')">📄 練習用紙プリント</button>
      </div>
    </div>"""

NEW_WRITING_TAB_KANA_PANEL = """      <!-- タブ1: かな学習スタジオ（なぞり書き練習 ＆ 書き取りテスト） -->
      <div id="writing-tab-kana" class="writing-tab-panel" style="display:block;">
        <div style="background:white; border:1.5px solid var(--border-soft); border-radius:16px; padding:20px;">
          <!-- 上部ヘッダー: タイトル + 戻るボタン + モード切替 (✍️ なぞり書き / 📝 書き取りテスト) -->
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
            </div>

            <!-- なぞり書き作業エリア: 左側に文字一覧、右側に書き順アニメーション＆コマ送り＆なぞりキャンバス -->
            <div style="display:grid; grid-template-columns: minmax(280px, 1fr) 340px; gap:20px; align-items:start;" id="kana-trace-layout">
              <!-- 左: かなグリッド (スクロール可能) -->
              <div id="kana-grid-picker" style="max-height:540px; overflow-y:auto; padding-right:6px;">
              </div>

              <!-- 右: 書き順アニメーション・筆順コマ送り・なぞり書き練習ステージ (写真完全再現) -->
              <div style="background:#F8FAFC; border:1.5px solid #CBD5E1; border-radius:14px; padding:16px; display:flex; flex-direction:column; gap:12px; position:sticky; top:10px;">
                <!-- ヘッダー情報: 文字バッジ、読み、画数、発音、全画面モーダルボタン -->
                <div style="display:flex; align-items:center; justify-content:space-between; width:100%;">
                  <div style="display:flex; align-items:center; gap:8px;">
                    <span id="kana-selected-char-badge" style="font-size:1.7rem; font-weight:900; color:#1E3A8A; font-family:'Klee One', cursive, sans-serif; line-height:1;">あ</span>
                    <span id="kana-current-romaji" style="font-size:0.92rem; font-weight:700; color:var(--kobe-blue);">[ a ]</span>
                    <span id="kana-current-strokes-badge" style="font-size:0.75rem; font-weight:800; background:#EFF6FF; color:#1D4ED8; padding:2px 7px; border-radius:6px; border:1px solid #BFDBFE;">3画</span>
                  </div>
                  <div style="display:flex; align-items:center; gap:6px;">
                    <button onclick="playCurrentKanaAudio()" style="background:#EFF6FF; border:1px solid #BFDBFE; color:#1D4ED8; padding:4px 10px; border-radius:8px; font-size:0.82rem; font-weight:800; cursor:pointer; display:flex; align-items:center; gap:4px;">
                      🔊 発音
                    </button>
                    <button onclick="openCurrentKanaStrokeModal()" style="background:white; border:1px solid #CBD5E1; color:#475569; padding:4px 8px; border-radius:8px; font-size:0.78rem; font-weight:700; cursor:pointer;" title="全画面で詳しく見る">
                      🔍 詳細
                    </button>
                  </div>
                </div>

                <!-- 拗音・特殊音 (2文字) の切り替えピル (2文字ある場合のみ表示) -->
                <div id="kana-multichar-selector" style="display:none; gap:6px; margin-bottom:2px;"></div>

                <!-- 田字格アニメーション & なぞり書きステージ (220x220) -->
                <div style="display:flex; flex-direction:column; align-items:center; gap:10px;">
                  <div class="kanji-stage-box" id="kana-trace-stage" style="width:220px; height:220px; border:2px solid #94A3B8; border-radius:12px; background:white; position:relative; overflow:hidden; box-shadow:0 2px 8px rgba(0,0,0,0.04);"></div>

                  <!-- コントロールバー: [▶ もういちど] [ゆっくり] [番号] [✍ なぞり練習] -->
                  <div class="kanji-controls-bar" style="width:100%; justify-content:center; gap:6px; flex-wrap:wrap;">
                    <button class="kanji-play-btn" onclick="replayKanaAnimation()">▶ もういちど</button>
                    <label style="display:inline-flex; align-items:center; gap:4px; cursor:pointer; font-size:0.8rem; color:#475569; font-weight:700;">
                      <input type="checkbox" id="kana-slow-toggle" onchange="replayKanaAnimation()"> ゆっくり
                    </label>
                    <label style="display:inline-flex; align-items:center; gap:4px; cursor:pointer; font-size:0.8rem; color:#475569; font-weight:700;">
                      <input type="checkbox" id="kana-numbers-toggle" checked onchange="toggleKanaNumbers()"> 番号
                    </label>
                    <button class="kanji-btn-trace-mode" id="btn-kana-toggle-trace" onclick="toggleKanaTraceMode()">✍ なぞり練習</button>
                  </div>

                  <!-- なぞり練習ツールバー [🗑️ 消去] [↺ 1画戻す] (なぞり時のみ表示) -->
                  <div id="kana-trace-draw-tools" style="display:none; gap:8px; width:100%; justify-content:center;">
                    <button onclick="clearKanaTraceCanvas()" style="background:white; border:1px solid #CBD5E1; color:#475569; padding:5px 12px; border-radius:8px; font-size:0.78rem; font-weight:700; cursor:pointer;">
                      🗑️ 全て消去
                    </button>
                    <button onclick="undoKanaTraceCanvas()" style="background:white; border:1px solid #CBD5E1; color:#475569; padding:5px 12px; border-radius:8px; font-size:0.78rem; font-weight:700; cursor:pointer;">
                      ↺ 1画戻す
                    </button>
                  </div>
                </div>

                <!-- 筆順コマ送り（新しく書く画＝赤色） -->
                <div style="border-top:1px solid #E2E8F0; padding-top:10px; margin-top:2px;">
                  <div style="font-size:0.8rem; font-weight:800; color:#475569; margin-bottom:8px; display:flex; align-items:center; gap:5px;">
                    <span>🖌️</span> <span>筆順コマ送り（新しく書く画＝赤色）:</span>
                  </div>
                  <div class="kanji-step-grid" id="kana-step-grid" style="display:flex; flex-wrap:wrap; gap:6px; max-height:160px; overflow-y:auto; padding:2px; justify-content:center;"></div>
                </div>

                <!-- フォントによる形の違いガイド -->
                <div id="kana-font-notice-box" style="width:100%;"></div>
              </div>
            </div>
          </div>

          <!-- サブモード2: かな書き取りテスト パネル -->
          <div id="kana-panel-quiz" style="display:none;">
            <div id="kana-quiz-container"></div>
          </div>
        </div>
      </div>"""

NEW_KANA_JS_ENGINE = """  // ================= 5. ひらがな・カタカナ なぞり書き＆書き取りテスト エンジン =================
  let currentKanaType = 'hiragana';
  let currentKanaCategory = 'all';
  let currentKanaSubMode = 'trace'; // 'trace' | 'quiz'
  let currentSelectedKana = { char: 'あ', romaji: 'a' };
  let currentActiveKanaSubChar = 'あ';

  const KANA_ALL_DATA = [
    // --- 五十音（清音・46文字） ---
    { h: 'あ', k: 'ア', r: 'a', cat: 'seion' },
    { h: 'い', k: 'イ', r: 'i', cat: 'seion' },
    { h: 'う', k: 'ウ', r: 'u', cat: 'seion' },
    { h: 'え', k: 'エ', r: 'e', cat: 'seion' },
    { h: 'お', k: 'オ', r: 'o', cat: 'seion' },

    { h: 'か', k: 'カ', r: 'ka', cat: 'seion' },
    { h: 'き', k: 'キ', r: 'ki', cat: 'seion' },
    { h: 'く', k: 'ク', r: 'ku', cat: 'seion' },
    { h: 'け', k: 'ケ', r: 'ke', cat: 'seion' },
    { h: 'こ', k: 'コ', r: 'ko', cat: 'seion' },

    { h: 'さ', k: 'サ', r: 'sa', cat: 'seion' },
    { h: 'し', k: 'シ', r: 'shi', cat: 'seion' },
    { h: 'す', k: 'ス', r: 'su', cat: 'seion' },
    { h: 'せ', k: 'セ', r: 'se', cat: 'seion' },
    { h: 'そ', k: 'ソ', r: 'so', cat: 'seion' },

    { h: 'た', k: 'タ', r: 'ta', cat: 'seion' },
    { h: 'ち', k: 'チ', r: 'chi', cat: 'seion' },
    { h: 'つ', k: 'ツ', r: 'tsu', cat: 'seion' },
    { h: 'て', k: 'テ', r: 'te', cat: 'seion' },
    { h: 'と', k: 'ト', r: 'to', cat: 'seion' },

    { h: 'な', k: 'ナ', r: 'na', cat: 'seion' },
    { h: 'に', k: 'ニ', r: 'ni', cat: 'seion' },
    { h: 'ぬ', k: 'ヌ', r: 'nu', cat: 'seion' },
    { h: 'ね', k: 'ネ', r: 'ne', cat: 'seion' },
    { h: 'の', k: 'ノ', r: 'no', cat: 'seion' },

    { h: 'は', k: 'ハ', r: 'ha', cat: 'seion' },
    { h: 'ひ', k: 'ヒ', r: 'hi', cat: 'seion' },
    { h: 'ふ', k: 'フ', r: 'fu', cat: 'seion' },
    { h: 'へ', k: 'ヘ', r: 'he', cat: 'seion' },
    { h: 'ほ', k: 'ホ', r: 'ho', cat: 'seion' },

    { h: 'ま', k: 'マ', r: 'ma', cat: 'seion' },
    { h: 'み', k: 'ミ', r: 'mi', cat: 'seion' },
    { h: 'む', k: 'ム', r: 'mu', cat: 'seion' },
    { h: 'め', k: 'メ', r: 'me', cat: 'seion' },
    { h: 'も', k: 'モ', r: 'mo', cat: 'seion' },

    { h: 'や', k: 'ヤ', r: 'ya', cat: 'seion' },
    { h: '', k: '', r: '', cat: 'blank' },
    { h: 'ゆ', k: 'ユ', r: 'yu', cat: 'seion' },
    { h: '', k: '', r: '', cat: 'blank' },
    { h: 'よ', k: 'ヨ', r: 'yo', cat: 'seion' },

    { h: 'ら', k: 'ラ', r: 'ra', cat: 'seion' },
    { h: 'り', k: 'リ', r: 'ri', cat: 'seion' },
    { h: 'る', k: 'ル', r: 'ru', cat: 'seion' },
    { h: 'れ', k: 'レ', r: 're', cat: 'seion' },
    { h: 'ろ', k: 'ロ', r: 'ro', cat: 'seion' },

    { h: 'わ', k: 'ワ', r: 'wa', cat: 'seion' },
    { h: '', k: '', r: '', cat: 'blank' },
    { h: '', k: '', r: '', cat: 'blank' },
    { h: '', k: '', r: '', cat: 'blank' },
    { h: 'を', k: 'ヲ', r: 'wo', cat: 'seion' },
    { h: 'ん', k: 'ン', r: 'n', cat: 'seion' },

    // --- 濁音・半濁音（25文字） ---
    { h: 'が', k: 'ガ', r: 'ga', cat: 'dakuon' },
    { h: 'ぎ', k: 'ギ', r: 'gi', cat: 'dakuon' },
    { h: 'ぐ', k: 'グ', r: 'gu', cat: 'dakuon' },
    { h: 'げ', k: 'ゲ', r: 'ge', cat: 'dakuon' },
    { h: 'ご', k: 'ゴ', r: 'go', cat: 'dakuon' },

    { h: 'ざ', k: 'ザ', r: 'za', cat: 'dakuon' },
    { h: 'じ', k: 'ジ', r: 'ji', cat: 'dakuon' },
    { h: 'ず', k: 'ズ', r: 'zu', cat: 'dakuon' },
    { h: 'ぜ', k: 'ゼ', r: 'ze', cat: 'dakuon' },
    { h: 'ぞ', k: 'ゾ', r: 'zo', cat: 'dakuon' },

    { h: 'だ', k: 'ダ', r: 'da', cat: 'dakuon' },
    { h: 'ぢ', k: 'ヂ', r: 'ji', cat: 'dakuon' },
    { h: 'づ', k: 'ヅ', r: 'zu', cat: 'dakuon' },
    { h: 'で', k: 'デ', r: 'de', cat: 'dakuon' },
    { h: 'ど', k: 'ド', r: 'do', cat: 'dakuon' },

    { h: 'ば', k: 'バ', r: 'ba', cat: 'dakuon' },
    { h: 'び', k: 'ビ', r: 'bi', cat: 'dakuon' },
    { h: 'ぶ', k: 'ブ', r: 'bu', cat: 'dakuon' },
    { h: 'べ', k: 'ベ', r: 'be', cat: 'dakuon' },
    { h: 'ぼ', k: 'ボ', r: 'bo', cat: 'dakuon' },

    { h: 'ぱ', k: 'パ', r: 'pa', cat: 'dakuon' },
    { h: 'ぴ', k: 'ピ', r: 'pi', cat: 'dakuon' },
    { h: 'ぷ', k: 'プ', r: 'pu', cat: 'dakuon' },
    { h: 'ぺ', k: 'ペ', r: 'pe', cat: 'dakuon' },
    { h: 'ぽ', k: 'ポ', r: 'po', cat: 'dakuon' },

    // --- 拗音（33文字） ---
    { h: 'きゃ', k: 'キャ', r: 'kya', cat: 'youon' },
    { h: 'きゅ', k: 'キュ', r: 'kyu', cat: 'youon' },
    { h: 'きょ', k: 'キョ', r: 'kyo', cat: 'youon' },

    { h: 'しゃ', k: 'シャ', r: 'sha', cat: 'youon' },
    { h: 'しゅ', k: 'シュ', r: 'shu', cat: 'youon' },
    { h: 'しょ', k: 'ショ', r: 'sho', cat: 'youon' },

    { h: 'ちゃ', k: 'チャ', r: 'cha', cat: 'youon' },
    { h: 'ちゅ', k: 'チュ', r: 'chu', cat: 'youon' },
    { h: 'ちょ', k: 'チョ', r: 'cho', cat: 'youon' },

    { h: 'にゃ', k: 'ニャ', r: 'nya', cat: 'youon' },
    { h: 'にゅ', k: 'ニュ', r: 'nyu', cat: 'youon' },
    { h: 'にょ', k: 'ニョ', r: 'nyo', cat: 'youon' },

    { h: 'ひゃ', k: 'ヒャ', r: 'hya', cat: 'youon' },
    { h: 'ひゅ', k: 'ヒュ', r: 'hyu', cat: 'youon' },
    { h: 'ひょ', k: 'ヒョ', r: 'hyo', cat: 'youon' },

    { h: 'みゃ', k: 'ミャ', r: 'mya', cat: 'youon' },
    { h: 'みゅ', k: 'ミュ', r: 'myu', cat: 'youon' },
    { h: 'みょ', k: 'ミョ', r: 'myo', cat: 'youon' },

    { h: 'りゃ', k: 'リャ', r: 'rya', cat: 'youon' },
    { h: 'りゅ', k: 'リュ', r: 'ryu', cat: 'youon' },
    { h: 'りょ', k: 'リョ', r: 'ryo', cat: 'youon' },

    { h: 'ぎゃ', k: 'ギャ', r: 'gya', cat: 'youon' },
    { h: 'ぎゅ', k: 'ギュ', r: 'gyu', cat: 'youon' },
    { h: 'ぎょ', k: 'ギョ', r: 'gyo', cat: 'youon' },

    { h: 'じゃ', k: 'ジャ', r: 'ja', cat: 'youon' },
    { h: 'じゅ', k: 'ジュ', r: 'ju', cat: 'youon' },
    { h: 'じょ', k: 'ジョ', r: 'jo', cat: 'youon' },

    { h: 'びゃ', k: 'ビャ', r: 'bya', cat: 'youon' },
    { h: 'びゅ', k: 'ビュ', r: 'byu', cat: 'youon' },
    { h: 'びょ', k: 'ビョ', r: 'byo', cat: 'youon' },

    { h: 'ぴゃ', k: 'ピャ', r: 'pya', cat: 'youon' },
    { h: 'ぴゅ', k: 'ピュ', r: 'pyu', cat: 'youon' },
    { h: 'ぴょ', k: 'ピョ', r: 'pyo', cat: 'youon' },

    // --- カタカナ外来語・特殊音（24文字） ---
    { h: 'しぇ', k: 'シェ', r: 'she', cat: 'tokushu' },
    { h: 'じぇ', k: 'ジェ', r: 'je', cat: 'tokushu' },
    { h: 'ちぇ', k: 'チェ', r: 'che', cat: 'tokushu' },
    { h: 'てぃ', k: 'ティ', r: 'ti', cat: 'tokushu' },
    { h: 'でぃ', k: 'ディ', r: 'di', cat: 'tokushu' },
    { h: 'でゅ', k: 'デュ', r: 'dyu', cat: 'tokushu' },
    { h: 'とぅ', k: 'トゥ', r: 'tu', cat: 'tokushu' },
    { h: 'どぅ', k: 'ドゥ', r: 'du', cat: 'tokushu' },
    { h: 'ふぁ', k: 'ファ', r: 'fa', cat: 'tokushu' },
    { h: 'ふぃ', k: 'フィ', r: 'fi', cat: 'tokushu' },
    { h: 'ふぇ', k: 'フェ', r: 'fe', cat: 'tokushu' },
    { h: 'ふぉ', k: 'フォ', r: 'fo', cat: 'tokushu' },
    { h: 'うぃ', k: 'ウィ', r: 'wi', cat: 'tokushu' },
    { h: 'うぇ', k: 'ウェ', r: 'we', cat: 'tokushu' },
    { h: 'うぉ', k: 'ウォ', r: 'wo', cat: 'tokushu' },
    { h: 'ヴ', k: 'ヴ', r: 'vu', cat: 'tokushu' },
    { h: 'ゔぁ', k: 'ヴァ', r: 'va', cat: 'tokushu' },
    { h: 'ゔぃ', k: 'ヴィ', r: 'vi', cat: 'tokushu' },
    { h: 'ゔぇ', k: 'ヴェ', r: 've', cat: 'tokushu' },
    { h: 'ゔぉ', k: 'ヴォ', r: 'vo', cat: 'tokushu' },
    { h: 'つぁ', k: 'ツァ', r: 'tsa', cat: 'tokushu' },
    { h: 'つぃ', k: 'ツィ', r: 'tsi', cat: 'tokushu' },
    { h: 'つぇ', k: 'ツェ', r: 'tse', cat: 'tokushu' },
    { h: 'つぉ', k: 'ツォ', r: 'tso', cat: 'tokushu' }
  ];

  function switchKanaSubMode(mode) {
    currentKanaSubMode = mode;
    const btnTrace = document.getElementById('btn-kana-submode-trace');
    const btnQuiz = document.getElementById('btn-kana-submode-quiz');
    if (btnTrace) btnTrace.classList.toggle('active', mode === 'trace');
    if (btnQuiz) btnQuiz.classList.toggle('active', mode === 'quiz');

    const pTrace = document.getElementById('kana-panel-trace');
    const pQuiz = document.getElementById('kana-panel-quiz');
    if (pTrace) pTrace.style.display = (mode === 'trace') ? 'block' : 'none';
    if (pQuiz) pQuiz.style.display = (mode === 'quiz') ? 'block' : 'none';

    if (mode === 'quiz') {
      if (typeof KanaWritingQuiz !== 'undefined') {
        KanaWritingQuiz.init('kana-quiz-container');
      }
    } else {
      updateKanaStrokeView(currentSelectedKana.char, currentSelectedKana.romaji);
    }
  }

  function setKanaCategory(cat, btnEl) {
    currentKanaCategory = cat;
    if (btnEl && btnEl.parentElement) {
      btnEl.parentElement.querySelectorAll('.quiz-level-pill').forEach(b => b.classList.remove('active'));
      btnEl.classList.add('active');
    }
    renderKanaGridPicker();
  }

  function initKanaTab() {
    renderKanaGridPicker();
    const first = KANA_ALL_DATA[0];
    const initialChar = (currentKanaType === 'hiragana') ? first.h : first.k;
    // 音声自動再生は絶対にしない (shouldPlayAudio = false)
    selectKanaForTrace(initialChar, first.r, false);
    if (currentKanaSubMode === 'quiz' && typeof KanaWritingQuiz !== 'undefined') {
      KanaWritingQuiz.init('kana-quiz-container');
    }
  }

  function switchKanaType(type) {
    currentKanaType = type;
    document.getElementById('btn-kana-hira')?.classList.toggle('active', type === 'hiragana');
    document.getElementById('btn-kana-kata')?.classList.toggle('active', type === 'katakana');
    renderKanaGridPicker();
    const first = KANA_ALL_DATA.find(x => x.cat === (currentKanaCategory === 'all' ? 'seion' : currentKanaCategory)) || KANA_ALL_DATA[0];
    const char = (type === 'hiragana') ? first.h : first.k;
    // タイプ切り替え時も自動再生しない
    selectKanaForTrace(char, first.r, false);
    if (typeof KanaWritingQuiz !== 'undefined' && currentKanaSubMode === 'quiz') {
      KanaWritingQuiz.setType(type);
    }
  }

  function renderKanaCell(item) {
    if (!item.h && !item.k) {
      return '<div style="background:transparent; height:48px;"></div>';
    }
    const displayChar = (currentKanaType === 'hiragana') ? item.h : item.k;
    const isSelected = (currentSelectedKana.char === displayChar);
    const escapedChar = displayChar.replace(/'/g, "\\\\'");
    const escapedRomaji = item.r.replace(/'/g, "\\\\'");
    return `
      <div onclick="selectKanaForTrace('${escapedChar}', '${escapedRomaji}', true)" style="background:${isSelected ? '#EFF6FF' : '#FFFFFF'}; border:1.5px solid ${isSelected ? 'var(--kobe-blue)' : '#E2E8F0'}; border-radius:10px; padding:6px 2px; text-align:center; cursor:pointer; transition:all 0.15s; box-shadow:0 1px 3px rgba(0,0,0,0.02);" title="${item.r}">
        <div style="font-size:${displayChar.length > 1 ? '1.05rem' : '1.25rem'}; font-weight:800; font-family:${currentKanaType === 'hiragana' ? "'Klee One', cursive" : 'inherit'}; color:${isSelected ? 'var(--kobe-blue)' : '#1E293B'}; line-height:1.2;">${displayChar}</div>
        <div style="font-size:0.68rem; color:#64748B; margin-top:2px;">${item.r}</div>
      </div>
    `;
  }

  function renderKanaGridPicker() {
    const grid = document.getElementById('kana-grid-picker');
    if (!grid) return;

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
              <span>🌸</span> <span>五十音（清音・46字）</span>
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
              <span>🎋</span> <span>拗音（きゃ・しゃ・ちゃ… 33字）</span>
            </div>
            <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:6px;">
              ${youonList.map(item => renderKanaCell(item)).join('')}
            </div>
          </div>

          <!-- カタカナ外来語・特殊音 (1行3つ) -->
          <div>
            <div style="font-weight:800; font-size:0.86rem; color:#1E3A8A; margin-bottom:8px; display:flex; align-items:center; gap:6px;">
              <span>🌐</span> <span>カタカナ外来語・特殊音（24字）</span>
            </div>
            <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:6px;">
              ${tokushuList.map(item => renderKanaCell(item)).join('')}
            </div>
          </div>
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
    } else if (currentKanaCategory === 'tokushu') {
      // ユーザー指示: 特殊音も1行3つ (repeat(3, 1fr))
      const list = KANA_ALL_DATA.filter(x => x.cat === 'tokushu');
      grid.innerHTML = `<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:6px;">${list.map(item => renderKanaCell(item)).join('')}</div>`;
    }
  }

  // フォントによる形の違いデータベース（手書き推奨 vs 印刷活字）
  const KANA_FONT_VARIATIONS = {
    'さ': {
      char: 'さ',
      handDesc: '下の弧を【離して3画】',
      printDesc: '下が【繋がっている】',
      note: '印刷用フォント（ゴシック体など）では下の線が繋がって見えることがありますが、<strong>手で描く（書く）時はこのお手本のように『離して3画』で書くのが通常</strong>です！'
    },
    'き': {
      char: 'き',
      handDesc: '下の弧を【離して4画】',
      printDesc: '下が【繋がっている】',
      note: '活字フォントでは3画目と下の曲線が繋がっているものがありますが、<strong>自分でノートに書く時は下の曲線を『離して4画』で書く</strong>のが基本です！'
    },
    'り': {
      char: 'り',
      handDesc: '上を【離して2画】',
      printDesc: '上が【繋がっている】',
      note: 'パソコンや本のフォントでは上で繋がって見えることが多いですが、<strong>手で描く時はこのお手本のように『離して2画』で書く</strong>のが一般的です！'
    },
    'そ': {
      char: 'そ',
      handDesc: '一筆でジグザグに書く（1画）',
      printDesc: '上の点と下が離れる（2画）',
      note: '『そ』は1画で続けて書く形と、上の点を離して2画で書く形があります。どちらも正解ですが、<strong>手書きではこの1画で書く形がとてもよく使われます</strong>！'
    },
    'ふ': {
      char: 'ふ',
      handDesc: '4画をそれぞれ離して書く',
      printDesc: '一部が繋がって見える',
      note: 'フォントによっては点や中央の線が繋がって見えることがありますが、<strong>手で書く時は4つの画をそれぞれ離してバランスよく書きます</strong>！'
    }
  };

  function updateKanaVariationNotice(char) {
    const box = document.getElementById('kana-font-notice-box');
    if (!box) return;

    const baseChar = char[0];
    const v = (currentKanaType === 'hiragana') ? KANA_FONT_VARIATIONS[baseChar] : null;
    if (v) {
      box.innerHTML = `
        <div style="background:#FFFBEB; border:1.5px solid #FCD34D; border-radius:12px; padding:10px 12px; width:100%; box-sizing:border-box; margin-top:2px;">
          <div style="display:flex; align-items:center; gap:6px; font-weight:800; font-size:0.84rem; color:#92400E; margin-bottom:8px;">
            <span>💡</span>
            <span>フォントによる形の違い</span>
          </div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-bottom:8px;">
            <!-- 手書き（Klee One: 繋がっていない） -->
            <div style="background:white; border:1.5px solid #10B981; border-radius:8px; padding:6px 4px; text-align:center;">
              <div style="font-size:0.68rem; font-weight:800; color:#059669; white-space:nowrap;">✍️ 書く時（通常）</div>
              <div style="font-family:'Klee One', cursive; font-size:36px; color:#1E293B; line-height:1.2; margin:2px 0;">${v.char}</div>
              <div style="font-size:0.65rem; color:#047857; font-weight:700;">✅ ${v.handDesc}</div>
            </div>
            <!-- 印刷（Noto Sans: 繋がっている） -->
            <div style="background:#F1F5F9; border:1px solid #CBD5E1; border-radius:8px; padding:6px 4px; text-align:center;">
              <div style="font-size:0.68rem; font-weight:700; color:#64748B; white-space:nowrap;">💻 本やPC活字</div>
              <div style="font-family:'Noto Sans JP', sans-serif; font-size:36px; color:#64748B; line-height:1.2; margin:2px 0;">${v.char}</div>
              <div style="font-size:0.65rem; color:#64748B;">${v.printDesc}</div>
            </div>
          </div>
          <div style="font-size:0.75rem; color:#78350F; line-height:1.45; background:#FEF3C7; padding:8px 10px; border-radius:8px; border:1px solid #FDE68A;">
            ${v.note}
          </div>
        </div>
      `;
    } else {
      box.innerHTML = `
        <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:10px; padding:9px 10px; width:100%; box-sizing:border-box; font-size:0.76rem; color:#64748B; line-height:1.4; text-align:center; margin-top:2px;">
          💡 田字格の十字線を意識して、マスの中心にバランスよく書いてみましょう！
        </div>
      `;
    }
  }

  // ================= かな書き順アニメーション ＆ コマ送り表示 ＆ なぞり練習 =================
  async function updateKanaStrokeView(char, romaji) {
    currentSelectedKana = { char, romaji };
    const charBadge = document.getElementById('kana-selected-char-badge');
    const romajiEl = document.getElementById('kana-current-romaji');
    const multiSelector = document.getElementById('kana-multichar-selector');
    const drawTools = document.getElementById('kana-trace-draw-tools');
    const btnTrace = document.getElementById('btn-kana-toggle-trace');

    if (drawTools) drawTools.style.display = 'none';
    if (btnTrace) btnTrace.textContent = '✍ なぞり練習';
    if (romajiEl) romajiEl.textContent = `[ ${romaji} ]`;

    // 2文字（拗音・外来語）の場合
    if (char.length > 1) {
      if (multiSelector) {
        multiSelector.style.display = 'flex';
        multiSelector.innerHTML = [...char].map((sub, idx) => `
          <button class="quiz-level-pill ${idx === 0 ? 'active' : ''}" onclick="selectKanaSubChar('${sub}', this)" style="padding:4px 10px; font-size:0.78rem;">
            ${idx + 1}文字目: ${sub}
          </button>
        `).join('');
      }
      currentActiveKanaSubChar = char[0];
    } else {
      if (multiSelector) multiSelector.style.display = 'none';
      currentActiveKanaSubChar = char;
    }

    if (charBadge) charBadge.textContent = char;
    await loadAndDisplayKanaStrokes(currentActiveKanaSubChar);
    updateKanaVariationNotice(char);
  }

  async function selectKanaSubChar(subChar, btnEl) {
    currentActiveKanaSubChar = subChar;
    if (btnEl && btnEl.parentElement) {
      btnEl.parentElement.querySelectorAll('.quiz-level-pill').forEach(b => b.classList.remove('active'));
      btnEl.classList.add('active');
    }
    await loadAndDisplayKanaStrokes(subChar);
  }

  async function loadAndDisplayKanaStrokes(targetChar) {
    const strokeBadge = document.getElementById('kana-current-strokes-badge');
    if (typeof KanjiEngine === 'undefined') return;

    const data = await KanjiEngine.fetchStrokes(targetChar);
    if (!data) {
      const stage = document.getElementById('kana-trace-stage');
      if (stage) {
        stage.innerHTML = `<div style="display:flex;align-items:center;justify-content:center;height:100%;font-size:4rem;color:#1E3A8A;font-family:'Klee One', cursive, sans-serif;">${targetChar}</div>`;
      }
      if (strokeBadge) strokeBadge.textContent = '1画';
      return;
    }

    if (strokeBadge) strokeBadge.textContent = `${data.strokesCount}画`;
    KanjiEngine.renderStage(data, 'kana-trace-stage', 'kana-slow-toggle', 'kana-numbers-toggle');
    KanjiEngine.renderStepGrid(data, 'kana-step-grid');
  }

  function replayKanaAnimation() {
    if (!currentActiveKanaSubChar || typeof KanjiEngine === 'undefined') return;
    const data = KanjiEngine.fetchStrokes(currentActiveKanaSubChar);
    if (data) {
      KanjiEngine.replayAnimation(currentActiveKanaSubChar, 'kana-trace-stage', 'kana-slow-toggle', 'kana-numbers-toggle');
    }
  }

  function toggleKanaNumbers() {
    if (typeof KanjiEngine !== 'undefined') {
      KanjiEngine.toggleNumbers('kana-trace-stage', 'kana-numbers-toggle');
    }
  }

  function toggleKanaTraceMode() {
    if (!currentActiveKanaSubChar || typeof KanjiEngine === 'undefined') return;
    KanjiEngine.toggleTrace(currentActiveKanaSubChar, 'kana-trace-stage', 'btn-kana-toggle-trace');
  }

  function clearKanaTraceCanvas() {
    const stage = document.getElementById('kana-trace-stage');
    if (stage && typeof stage._clear === 'function') {
      stage._clear();
    }
  }

  function undoKanaTraceCanvas() {
    const stage = document.getElementById('kana-trace-stage');
    if (stage && typeof stage._undo === 'function') {
      stage._undo();
    }
  }

  function openCurrentKanaStrokeModal() {
    if (currentActiveKanaSubChar && typeof KanjiEngine !== 'undefined') {
      KanjiEngine.openStrokeModal(currentActiveKanaSubChar, {
        romaji: currentSelectedKana.romaji,
        isKana: true
      });
    }
  }

  function selectKanaForTrace(char, romaji, shouldPlayAudio = false) {
    updateKanaStrokeView(char, romaji);
    renderKanaGridPicker();
    if (shouldPlayAudio) {
      playCurrentKanaAudio();
    }
  }

  function playCurrentKanaAudio() {
    const soundTarget = currentActiveKanaSubChar || currentSelectedKana.char;
    if (typeof playGoogleTTS === 'function' && soundTarget) {
      playGoogleTTS(soundTarget);
    } else if ('speechSynthesis' in window && soundTarget) {
      window.speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(soundTarget);
      u.lang = 'ja-JP';
      u.rate = 0.85;
      window.speechSynthesis.speak(u);
    }
  }

  // ================= かな書き取りテスト エンジン (MainichiKanjiQuiz スタイル完全踏襲) =================
  window.KanaWritingQuiz = {
    containerId: 'kana-quiz-container',
    currentType: 'hiragana', // 'hiragana' | 'katakana'
    currentCategory: 'all',  // 'all' | 'seion' | 'dakuon' | 'youon' | 'tokushu'
    currentMode: 'sequential', // 'sequential' | 'shuffle' | 'extract'
    extractCount: 10,
    questions: [],
    currentIndex: 0,
    answers: {},
    isAnswerRevealed: false,
    canvasStrokes: [],
    isDrawing: false,
    isCompleted: false,

    init(containerId = 'kana-quiz-container') {
      this.containerId = containerId;
      this.startQuiz();
    },

    startQuiz() {
      let pool = KANA_ALL_DATA.filter(x => x.h && x.k && x.cat !== 'blank');
      if (this.currentCategory !== 'all') {
        pool = pool.filter(x => x.cat === this.currentCategory);
      }

      let list = pool.map(item => ({
        char: (this.currentType === 'hiragana') ? item.h : item.k,
        romaji: item.r,
        category: item.cat,
        h: item.h,
        k: item.k
      }));

      if (this.currentMode === 'sequential') {
        this.questions = list;
      } else if (this.currentMode === 'shuffle') {
        const sh = [...list];
        for (let i = sh.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [sh[i], sh[j]] = [sh[j], sh[i]];
        }
        this.questions = sh;
      } else if (this.currentMode === 'extract') {
        const sh = [...list];
        for (let i = sh.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [sh[i], sh[j]] = [sh[j], sh[i]];
        }
        this.questions = sh.slice(0, Math.min(this.extractCount, sh.length));
      }

      this.currentIndex = 0;
      this.answers = {};
      this.isAnswerRevealed = false;
      this.canvasStrokes = [];
      this.isCompleted = false;

      this.render();
    },

    setType(type) {
      this.currentType = type;
      this.startQuiz();
    },

    setCategory(cat) {
      this.currentCategory = cat;
      this.startQuiz();
    },

    setMode(mode, count = null) {
      this.currentMode = mode;
      if (count) this.extractCount = count;
      this.startQuiz();
    },

    toggleAnswer() {
      this.isAnswerRevealed = !this.isAnswerRevealed;
      this.render();
    },

    hideAnswer() {
      this.isAnswerRevealed = false;
      this.render();
    },

    mark(isCorrect) {
      this.answers[this.currentIndex] = isCorrect;
      if (this.currentIndex < this.questions.length - 1) {
        this.currentIndex++;
        this.isAnswerRevealed = false;
        this.canvasStrokes = [];
        this.render();
      } else {
        this.isCompleted = true;
        this.render();
      }
    },

    prev() {
      if (this.currentIndex > 0) {
        this.currentIndex--;
        this.isAnswerRevealed = false;
        this.canvasStrokes = [];
        this.render();
      }
    },

    next() {
      if (this.currentIndex < this.questions.length - 1) {
        this.currentIndex++;
        this.isAnswerRevealed = false;
        this.canvasStrokes = [];
        this.render();
      } else {
        this.isCompleted = true;
        this.render();
      }
    },

    jumpToQuestion(idx) {
      if (idx >= 0 && idx < this.questions.length) {
        this.currentIndex = idx;
        this.isAnswerRevealed = false;
        this.canvasStrokes = [];
        this.render();
      }
    },

    retryMissed() {
      const missed = this.questions.filter((_, idx) => this.answers[idx] === false);
      if (missed.length === 0) {
        alert('まちがえた文字はありません！全問正解です🎉');
        return;
      }
      this.questions = missed;
      this.currentIndex = 0;
      this.answers = {};
      this.isAnswerRevealed = false;
      this.canvasStrokes = [];
      this.isCompleted = false;
      this.render();
    },

    practiceTraceChar(char, romaji) {
      switchKanaSubMode('trace');
      selectKanaForTrace(char, romaji, false);
      const stage = document.getElementById('kana-trace-layout');
      if (stage) stage.scrollIntoView({ behavior: 'smooth' });
    },

    render() {
      const container = document.getElementById(this.containerId);
      if (!container) return;

      const typeLabel = (this.currentType === 'hiragana') ? 'ひらがな' : 'カタカナ';
      const catLabels = {
        all: 'すべて',
        seion: '五十音（清音）',
        dakuon: '濁音・半濁音',
        youon: '拗音',
        tokushu: '特殊音'
      };

      let correctCount = 0;
      let wrongCount = 0;
      Object.keys(this.answers).forEach(k => {
        if (this.answers[k] === true) correctCount++;
        else if (this.answers[k] === false) wrongCount++;
      });

      if (this.isCompleted) {
        const total = this.questions.length;
        const pct = total > 0 ? Math.round((correctCount / total) * 100) : 0;
        const missedList = this.questions.filter((_, idx) => this.answers[idx] === false);

        container.innerHTML = `
          <div style="background:#F8FAFC; border:1.5px solid #E2E8F0; border-radius:16px; padding:24px; text-align:center;">
            <div style="font-size:2.8rem; margin-bottom:8px;">${pct >= 80 ? '🎉' : '💪'}</div>
            <div style="font-size:1.3rem; font-weight:800; color:#1E293B;">テスト完了！ お疲れさまでした！</div>
            <div style="font-size:0.9rem; color:#64748B; margin-top:4px;">
              【${typeLabel} / ${catLabels[this.currentCategory]}】 全 ${total} 問
            </div>

            <!-- スコア表示 -->
            <div style="display:flex; justify-content:center; gap:20px; margin:20px 0; flex-wrap:wrap;">
              <div style="background:white; border:1.5px solid #86EFAC; border-radius:12px; padding:12px 24px; text-align:center; min-width:110px;">
                <div style="font-size:0.78rem; font-weight:800; color:#15803D;">⭕ 正解数</div>
                <div style="font-size:1.8rem; font-weight:900; color:#16A34A; margin-top:2px;">${correctCount}</div>
              </div>
              <div style="background:white; border:1.5px solid #FCA5A5; border-radius:12px; padding:12px 24px; text-align:center; min-width:110px;">
                <div style="font-size:0.78rem; font-weight:800; color:#B91C1C;">❌ まちがい</div>
                <div style="font-size:1.8rem; font-weight:900; color:#DC2626; margin-top:2px;">${wrongCount}</div>
              </div>
              <div style="background:white; border:1.5px solid #93C5FD; border-radius:12px; padding:12px 24px; text-align:center; min-width:110px;">
                <div style="font-size:0.78rem; font-weight:800; color:#1D4ED8;">正解率</div>
                <div style="font-size:1.8rem; font-weight:900; color:#2563EB; margin-top:2px;">${pct}%</div>
              </div>
            </div>

            ${missedList.length > 0 ? `
              <!-- まちがえた文字の復習リスト -->
              <div style="background:white; border:1.5px solid #FECACA; border-radius:14px; padding:16px; margin:20px auto; max-width:600px; text-align:left;">
                <div style="font-size:0.88rem; font-weight:800; color:#991B1B; margin-bottom:10px; display:flex; align-items:center; justify-content:space-between;">
                  <span>❌ 間違えた文字（タップでなぞり書き練習）</span>
                  <span style="font-size:0.76rem; color:#B91C1C; font-weight:700;">${missedList.length} 文字</span>
                </div>
                <div style="display:flex; flex-wrap:wrap; gap:8px;">
                  ${missedList.map(item => `
                    <div onclick="KanaWritingQuiz.practiceTraceChar('${item.char}', '${item.romaji}')" style="background:#FEF2F2; border:1.5px solid #F87171; border-radius:8px; padding:6px 12px; display:flex; align-items:center; gap:8px; cursor:pointer;" title="なぞり書き練習へ">
                      <span style="font-size:1.3rem; font-weight:800; color:#991B1B;">${item.char}</span>
                      <span style="font-size:0.75rem; color:#7F1D1D;">[ ${item.romaji} ]</span>
                      <span style="font-size:0.72rem; color:#DC2626; font-weight:700;">✍ 練習</span>
                    </div>
                  `).join('')}
                </div>
              </div>
            ` : `
              <div style="background:#F0FDF4; border:1.5px solid #86EFAC; border-radius:12px; padding:14px; margin:16px auto; max-width:500px; color:#15803D; font-weight:700;">
                🎉 すばらしい！ 満点達成です！ 自信を持って次のステップに進みましょう！
              </div>
            `}

            <!-- 操作ボタン -->
            <div style="display:flex; justify-content:center; gap:12px; margin-top:20px; flex-wrap:wrap;">
              ${missedList.length > 0 ? `
                <button onclick="KanaWritingQuiz.retryMissed()" style="background:#DC2626; color:white; border:none; padding:10px 20px; border-radius:10px; font-weight:800; font-size:0.92rem; cursor:pointer; box-shadow:0 2px 6px rgba(220,38,38,0.25);">
                  ❌ まちがえた文字だけ再テスト
                </button>
              ` : ''}
              <button onclick="KanaWritingQuiz.startQuiz()" style="background:var(--kobe-blue); color:white; border:none; padding:10px 20px; border-radius:10px; font-weight:800; font-size:0.92rem; cursor:pointer; box-shadow:0 2px 6px rgba(29,78,216,0.25);">
                ↺ もう一度最初からテスト
              </button>
            </div>
          </div>
        `;
        return;
      }

      if (this.questions.length === 0) {
        container.innerHTML = '<div style="padding:40px; text-align:center; color:#64748B;">出題可能な文字がありません。</div>';
        return;
      }

      const q = this.questions[this.currentIndex];
      const isFirst = (this.currentIndex === 0);
      const isLast = (this.currentIndex === this.questions.length - 1);

      container.innerHTML = `
        <div style="display:flex; flex-direction:column; gap:14px;">
          <!-- テスト設定ツールバー (文字種・出題範囲・出題順序) -->
          <div style="background:#F8FAFC; border:1.5px solid #E2E8F0; border-radius:14px; padding:12px 16px; display:flex; flex-direction:column; gap:10px;">
            <!-- 1行目: 文字種 ＆ 出題範囲 -->
            <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px;">
              <div style="display:flex; align-items:center; gap:6px; flex-wrap:wrap;">
                <span style="font-size:0.78rem; font-weight:800; color:#475569;">文字:</span>
                <div class="quiz-level-pills">
                  <button class="quiz-level-pill ${this.currentType === 'hiragana' ? 'active' : ''}" onclick="KanaWritingQuiz.setType('hiragana')">ひらがな</button>
                  <button class="quiz-level-pill ${this.currentType === 'katakana' ? 'active' : ''}" onclick="KanaWritingQuiz.setType('katakana')">カタカナ</button>
                </div>
              </div>
              <div style="display:flex; align-items:center; gap:6px; flex-wrap:wrap;">
                <span style="font-size:0.78rem; font-weight:800; color:#475569;">範囲:</span>
                <div class="quiz-level-pills">
                  <button class="quiz-level-pill ${this.currentCategory === 'all' ? 'active' : ''}" onclick="KanaWritingQuiz.setCategory('all')">全文字 (${this.questions.length > 0 && this.currentCategory === 'all' && this.currentMode !== 'extract' ? this.questions.length : '128'})</button>
                  <button class="quiz-level-pill ${this.currentCategory === 'seion' ? 'active' : ''}" onclick="KanaWritingQuiz.setCategory('seion')">五十音</button>
                  <button class="quiz-level-pill ${this.currentCategory === 'dakuon' ? 'active' : ''}" onclick="KanaWritingQuiz.setCategory('dakuon')">濁音・半濁音</button>
                  <button class="quiz-level-pill ${this.currentCategory === 'youon' ? 'active' : ''}" onclick="KanaWritingQuiz.setCategory('youon')">拗音</button>
                  <button class="quiz-level-pill ${this.currentCategory === 'tokushu' ? 'active' : ''}" onclick="KanaWritingQuiz.setCategory('tokushu')">カタカナ特殊音</button>
                </div>
              </div>
            </div>

            <!-- 2行目: 出題順序 (あから順番に / シャッフル / 抜粋で: 10問, 20問, 25問) -->
            <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px; border-top:1px dashed #CBD5E1; padding-top:8px;">
              <div style="display:flex; align-items:center; gap:6px; flex-wrap:wrap;">
                <span style="font-size:0.78rem; font-weight:800; color:#475569;">出題形式:</span>
                <div class="quiz-level-pills">
                  <button class="quiz-level-pill ${this.currentMode === 'sequential' ? 'active' : ''}" onclick="KanaWritingQuiz.setMode('sequential')">あから順番に</button>
                  <button class="quiz-level-pill ${this.currentMode === 'shuffle' ? 'active' : ''}" onclick="KanaWritingQuiz.setMode('shuffle')">シャッフル</button>
                  <button class="quiz-level-pill ${this.currentMode === 'extract' && this.extractCount === 10 ? 'active' : ''}" onclick="KanaWritingQuiz.setMode('extract', 10)">抜粋 10問</button>
                  <button class="quiz-level-pill ${this.currentMode === 'extract' && this.extractCount === 20 ? 'active' : ''}" onclick="KanaWritingQuiz.setMode('extract', 20)">抜粋 20問</button>
                  <button class="quiz-level-pill ${this.currentMode === 'extract' && this.extractCount === 25 ? 'active' : ''}" onclick="KanaWritingQuiz.setMode('extract', 25)">抜粋 25問</button>
                </div>
              </div>
              <button onclick="KanaWritingQuiz.startQuiz()" style="background:white; border:1px solid #CBD5E1; color:#475569; padding:4px 10px; border-radius:6px; font-size:0.75rem; font-weight:700; cursor:pointer;">
                ↺ リセット
              </button>
            </div>
          </div>

          <!-- メインテストカード (MainichiKanjiQuiz と同様のデザイン) -->
          <div style="background:white; border:1.5px solid var(--border-soft); border-radius:16px; padding:20px; box-shadow:0 2px 10px rgba(0,0,0,0.03);">
            <!-- 上部インフォバー: 問題数 ＆ スコア -->
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:14px; flex-wrap:wrap; gap:8px;">
              <div style="font-size:0.92rem; font-weight:800; color:#1E3A8A; display:flex; align-items:center; gap:8px;">
                <span style="background:#EFF6FF; color:#1D4ED8; padding:2px 8px; border-radius:6px; font-size:0.8rem; border:1px solid #BFDBFE;">第 ${this.currentIndex + 1} / ${this.questions.length} 問</span>
                <span>【${typeLabel}】を書いてみましょう</span>
              </div>
              <div style="display:flex; align-items:center; gap:8px; font-size:0.82rem; font-weight:800;">
                <span style="color:#16A34A; background:#DCFCE7; padding:2px 8px; border-radius:6px;">⭕ ${correctCount}</span>
                <span style="color:#DC2626; background:#FEE2E2; padding:2px 8px; border-radius:6px;">❌ ${wrongCount}</span>
              </div>
            </div>

            <!-- 問題出題ブロック: ローマ字と発音ボタン -->
            <div style="background:#EFF6FF; border:1.5px solid #BFDBFE; border-radius:14px; padding:16px 20px; display:flex; align-items:center; justify-content:space-between; margin-bottom:16px;">
              <div>
                <div style="font-size:0.78rem; font-weight:800; color:#1E40AF; margin-bottom:2px;">発音・ローマ字:</div>
                <div style="font-size:2rem; font-weight:900; color:#1D4ED8; font-family:'Courier New', monospace; letter-spacing:1px;">
                  [ ${q.romaji} ]
                </div>
              </div>
              <button onclick="playGoogleTTS('${q.char}')" title="発音を聞く" style="background:white; border:1.5px solid #93C5FD; color:#1D4ED8; padding:8px 16px; border-radius:10px; font-size:0.95rem; font-weight:800; cursor:pointer; display:inline-flex; align-items:center; gap:6px; box-shadow:0 2px 4px rgba(0,0,0,0.05);" onmouseover="this.style.background='#DBEAFE'" onmouseout="this.style.background='white'">
                🔊 発音を聞く
              </button>
            </div>

            <!-- 丸っこいグレーの「解答」ボタン -->
            <button class="mainichi-btn-answer" id="kana-quiz-btn-answer" onclick="KanaWritingQuiz.toggleAnswer()" style="margin: 0 auto 14px; display:block;">
              ${this.isAnswerRevealed ? '解答を隠す ＾' : '解答'}
            </button>

            <!-- 手書きキャンバス枠 (田字格 220x220) -->
            <div style="display:flex; justify-content:center; margin-bottom:12px;">
              <div style="width:220px; height:220px; border:2px solid #94A3B8; border-radius:12px; background:white; position:relative; overflow:hidden; box-shadow:0 2px 8px rgba(0,0,0,0.04);">
                <!-- 十字点線 -->
                <div style="position:absolute; inset:0; pointer-events:none;">
                  <div style="position:absolute; top:50%; left:0; right:0; height:1px; border-top:1px dashed #BAE6FD;"></div>
                  <div style="position:absolute; left:50%; top:0; bottom:0; width:1px; border-left:1px dashed #BAE6FD;"></div>
                </div>
                <!-- 手書きCanvas -->
                <canvas id="kana-quiz-canvas" style="position:absolute; inset:0; width:100%; height:100%; touch-action:none; cursor:crosshair; z-index:2;"></canvas>
              </div>
            </div>

            <!-- キャンバス下ツールバー [✕ 消去] [↺ 1画戻す] -->
            <div style="display:flex; align-items:center; justify-content:center; gap:10px; margin-bottom:16px;">
              <button class="mainichi-square-btn" title="全て消去" onclick="KanaWritingQuiz.clearCanvas()" style="width:40px; height:40px; font-size:1.1rem;">✕</button>
              <button class="mainichi-square-btn" title="1画戻す" onclick="KanaWritingQuiz.undoCanvas()" style="width:40px; height:40px; font-size:1.1rem;">↺</button>
            </div>

            <!-- 解答展開パネル (「解答」ボタンで開く) -->
            ${this.isAnswerRevealed ? `
              <div style="background:#F0FDF4; border:2px solid #86EFAC; border-radius:14px; padding:16px 20px; margin-bottom:18px; animation:fadeIn 0.2s ease;">
                <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px; margin-bottom:14px; border-bottom:1px solid #BBF7D0; padding-bottom:10px;">
                  <div style="display:flex; align-items:center; gap:12px;">
                    <span style="font-size:2.8rem; font-weight:900; color:#15803D; font-family:${this.currentType === 'hiragana' ? "'Klee One', cursive" : 'inherit'}; line-height:1;">${q.char}</span>
                    <span style="font-size:1.1rem; font-weight:700; color:#166534;">[ ${q.romaji} ]</span>
                    <button onclick="playGoogleTTS('${q.char}')" title="発音を聞く" style="background:white; border:1px solid #86EFAC; border-radius:8px; font-size:0.95rem; cursor:pointer; padding:3px 10px; color:#15803D;">
                      🔊
                    </button>
                  </div>
                  <button onclick="KanaWritingQuiz.practiceTraceChar('${q.char}', '${q.romaji}')" style="background:white; border:1.5px solid #86EFAC; color:#15803D; padding:6px 12px; border-radius:8px; font-weight:800; font-size:0.8rem; cursor:pointer;">
                    ✍ なぞり練習へ
                  </button>
                </div>

                <!-- 自己採点バー -->
                <div class="mainichi-self-check-bar" style="margin-top:0;">
                  <button class="btn-check-ok" onclick="KanaWritingQuiz.mark(true)">⭕ 正解した！</button>
                  <button class="btn-check-ng" onclick="KanaWritingQuiz.mark(false)">❌ まちがえた（復習に追加）</button>
                </div>
              </div>
            ` : ''}

            <!-- ナビゲーションバー (前へ・次へ) -->
            <div class="mainichi-nav-bar" style="margin-top:10px;">
              <button class="mainichi-nav-btn" onclick="KanaWritingQuiz.prev()" ${isFirst ? 'disabled' : ''}>
                ◀ 前の問題
              </button>
              <button class="mainichi-nav-btn" onclick="KanaWritingQuiz.next()">
                ${isLast ? '結果を見る ▶' : '次の問題 ▶'}
              </button>
            </div>
          </div>
        </div>
      `;

      setTimeout(() => {
        this.initQuizCanvas();
      }, 30);
    },

    initQuizCanvas() {
      const cvs = document.getElementById('kana-quiz-canvas');
      if (!cvs) return;

      const w = 220, h = 220;
      cvs.width = w * window.devicePixelRatio;
      cvs.height = h * window.devicePixelRatio;
      cvs.style.width = w + "px";
      cvs.style.height = h + "px";

      const ctx = cvs.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';
      ctx.strokeStyle = '#0F172A';
      ctx.lineWidth = 6;

      this.redrawQuizCanvas();

      let currentStroke = [];
      const getPos = (e) => {
        const rect = cvs.getBoundingClientRect();
        return { x: e.clientX - rect.left, y: e.clientY - rect.top };
      };

      cvs.onpointerdown = (e) => {
        cvs.setPointerCapture(e.pointerId);
        this.isDrawing = true;
        currentStroke = [];
        const p = getPos(e);
        currentStroke.push(p);
        ctx.beginPath();
        ctx.moveTo(p.x, p.y);
      };

      cvs.onpointermove = (e) => {
        if (!this.isDrawing) return;
        const p = getPos(e);
        currentStroke.push(p);
        ctx.lineTo(p.x, p.y);
        ctx.stroke();
      };

      const stop = () => {
        if (!this.isDrawing) return;
        this.isDrawing = false;
        if (currentStroke.length > 0) {
          this.canvasStrokes.push([...currentStroke]);
        }
      };

      cvs.onpointerup = stop;
      cvs.onpointercancel = stop;
    },

    clearCanvas() {
      this.canvasStrokes = [];
      const cvs = document.getElementById('kana-quiz-canvas');
      if (!cvs) return;
      const ctx = cvs.getContext('2d');
      ctx.clearRect(0, 0, cvs.width, cvs.height);
    },

    undoCanvas() {
      if (this.canvasStrokes.length === 0) return;
      this.canvasStrokes.pop();
      this.redrawQuizCanvas();
    },

    redrawQuizCanvas() {
      const cvs = document.getElementById('kana-quiz-canvas');
      if (!cvs) return;
      const ctx = cvs.getContext('2d');
      ctx.clearRect(0, 0, cvs.width, cvs.height);
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';
      ctx.strokeStyle = '#0F172A';
      ctx.lineWidth = 6;

      this.canvasStrokes.forEach(stroke => {
        if (stroke.length === 0) return;
        ctx.beginPath();
        ctx.moveTo(stroke[0].x, stroke[0].y);
        for (let i = 1; i < stroke.length; i++) {
          ctx.lineTo(stroke[i].x, stroke[i].y);
        }
        ctx.stroke();
      });
    }
  };"""

def update_html_file(filepath):
    print(f"Updating HTML file: {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update top tab bar in kanji-main-tabs
    tabs_start = '<div class="kanji-main-tabs">'
    tabs_end = '</div>\n    </div>'
    p_ts = content.find(tabs_start)
    if p_ts != -1:
        p_te = content.find('</div>', p_ts)
        if p_te != -1:
            p_te2 = content.find('</div>', p_te + 6)
            # Replace from the beginning of comment <!-- 固定タブバーエリア
            bar_start = content.rfind('<!-- 固定タブバーエリア', 0, p_ts)
            if bar_start != -1:
                content = content[:bar_start] + NEW_HTML_TAB_BAR + content[p_te2 + 6:]
                print(f"[{filepath}] Updated top tab bar order: ひらがな -> JLPT漢字リスト -> 毎日漢字!")

    # 2. Make writing-tab-quiz hidden by default if not already
    content = content.replace('<div id="writing-tab-quiz" class="writing-tab-panel">', '<div id="writing-tab-quiz" class="writing-tab-panel" style="display:none;">')

    # 3. Update writing-tab-kana panel
    start_tag = '<div id="writing-tab-kana"'
    end_tag = '<!-- タブ4: 練習プリントPDF -->'
    start_pos = content.find(start_tag)
    end_pos = content.find(end_tag)

    if start_pos != -1 and end_pos != -1:
        content = content[:start_pos] + NEW_WRITING_TAB_KANA_PANEL + "\n\n      " + content[end_pos:]
        print(f"[{filepath}] Updated writing-tab-kana panel with stroke animation and step-grid!")

    # 4. Update switchWritingTab default tabs array and active tab
    old_switch_order = "['quiz', 'list', 'kana', 'pdf'].forEach(t => {"
    new_switch_order = "['kana', 'list', 'quiz', 'pdf'].forEach(t => {"
    if old_switch_order in content:
        content = content.replace(old_switch_order, new_switch_order)

    # 5. Update openModal('writing') to switchWritingTab('kana')
    content = content.replace("if (name === 'writing' && typeof switchWritingTab === 'function') switchWritingTab('quiz');", "if (name === 'writing' && typeof switchWritingTab === 'function') switchWritingTab('kana');")

    # 6. Update Kana JS engine
    js_start_marker = "// ================= 5. ひらがな・カタカナ なぞり書き＆書き取りテスト エンジン ================="
    js_end_marker = "// ================= ビジネス敬語マスター (フラッシュカード・穴埋め・ロールプレイ) ================="
    
    js_start_pos = content.find(js_start_marker)
    js_end_pos = content.find(js_end_marker)

    if js_start_pos != -1 and js_end_pos != -1:
        content = content[:js_start_pos] + NEW_KANA_JS_ENGINE + "\n\n  " + content[js_end_pos:]
        print(f"[{filepath}] Updated Kana JS engine with stroke animation and step grid!")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[{filepath}] Finished saving.")

if __name__ == '__main__':
    update_kanji_engine()
    update_html_file('app.html')
    update_html_file('📱_日本語学習アプリ.html')
    print("All files updated successfully!")
