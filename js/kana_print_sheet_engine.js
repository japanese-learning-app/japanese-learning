/**
 * かな・漢字 練習用紙プリント＆A4横PDFダウンロード エンジン
 * A4用紙サイズ（横向き）完全準拠
 * 見本・なぞる・何もなし・テスト × 50音・濁音・拗音・特殊音・全セット一括
 */

(function() {
  const HIRA_50ON = [
    ["あ", "い", "う", "え", "お"],
    ["か", "き", "く", "け", "こ"],
    ["さ", "し", "す", "せ", "そ"],
    ["た", "ち", "つ", "て", "と"],
    ["な", "に", "ぬ", "ね", "の"],
    ["は", "ひ", "ふ", "へ", "ほ"],
    ["ま", "み", "む", "め", "も"],
    ["や", "", "ゆ", "", "よ"],
    ["ら", "り", "る", "れ", "ろ"],
    ["わ", "", "を", "", "ん"]
  ];

  const KATA_50ON = [
    ["ア", "イ", "ウ", "エ", "オ"],
    ["カ", "キ", "ク", "ケ", "コ"],
    ["サ", "シ", "ス", "セ", "ソ"],
    ["タ", "チ", "ツ", "テ", "ト"],
    ["ナ", "ニ", "ヌ", "ネ", "ノ"],
    ["ハ", "ヒ", "フ", "ヘ", "ホ"],
    ["マ", "ミ", "ム", "メ", "モ"],
    ["ヤ", "", "ユ", "", "ヨ"],
    ["ラ", "リ", "ル", "レ", "ロ"],
    ["ワ", "", "ヲ", "", "ン"]
  ];

  const ROMAJI_50ON = [
    ["a", "i", "u", "e", "o"],
    ["ka", "ki", "ku", "ke", "ko"],
    ["sa", "shi", "su", "se", "so"],
    ["ta", "chi", "tsu", "te", "to"],
    ["na", "ni", "nu", "ne", "no"],
    ["ha", "hi", "fu", "he", "ho"],
    ["ma", "mi", "mu", "me", "mo"],
    ["ya", "", "yu", "", "yo"],
    ["ra", "ri", "ru", "re", "ro"],
    ["wa", "", "wo", "", "n"]
  ];

  const HIRA_DAKUON = [
    ["が", "ぎ", "ぐ", "げ", "ご"],
    ["ざ", "じ", "ず", "ぜ", "ぞ"],
    ["だ", "ぢ", "づ", "で", "ど"],
    ["ば", "び", "ぶ", "べ", "ぼ"],
    ["ぱ", "ぴ", "ぷ", "ぺ", "ぽ"]
  ];

  const KATA_DAKUON = [
    ["ガ", "ギ", "グ", "ゲ", "ゴ"],
    ["ザ", "ジ", "ズ", "ゼ", "ゾ"],
    ["ダ", "ヂ", "ヅ", "デ", "ド"],
    ["バ", "ビ", "ブ", "ベ", "ボ"],
    ["パ", "ピ", "プ", "ペ", "ポ"]
  ];

  const ROMAJI_DAKUON = [
    ["ga", "gi", "gu", "ge", "go"],
    ["za", "ji", "zu", "ze", "zo"],
    ["da", "ji", "zu", "de", "do"],
    ["ba", "bi", "bu", "be", "bo"],
    ["pa", "pi", "pu", "pe", "po"]
  ];

  const HIRA_YOUON = [
    ["きゃ", "きゅ", "きょ"],
    ["しゃ", "しゅ", "しょ"],
    ["ちゃ", "ちゅ", "ちょ"],
    ["にゃ", "にゅ", "にょ"],
    ["ひゃ", "ひゅ", "ひょ"],
    ["みゃ", "みゅ", "みょ"],
    ["りゃ", "りゅ", "りょ"],
    ["ぎゃ", "ぎゅ", "ぎょ"],
    ["じゃ", "じゅ", "じょ"],
    ["びゃ", "びゅ", "びょ"],
    ["ぴゃ", "ぴゅ", "ぴょ"]
  ];

  const KATA_YOUON = [
    ["キャ", "キュ", "キョ"],
    ["シャ", "シュ", "ショ"],
    ["チャ", "チュ", "チョ"],
    ["ニャ", "ニュ", "ニョ"],
    ["ヒャ", "ヒュ", "ヒョ"],
    ["ミャ", "ミュ", "ミョ"],
    ["リャ", "リュ", "リョ"],
    ["ギャ", "ギュ", "ギョ"],
    ["ジャ", "ジュ", "ジョ"],
    ["ビャ", "ビュ", "ビョ"],
    ["ピャ", "ピュ", "ピョ"]
  ];

  const ROMAJI_YOUON = [
    ["kya", "kyu", "kyo"],
    ["sha", "shu", "sho"],
    ["cha", "chu", "cho"],
    ["nya", "nyu", "nyo"],
    ["hya", "hyu", "hyo"],
    ["mya", "myu", "myo"],
    ["rya", "ryu", "ryo"],
    ["gya", "gyu", "gyo"],
    ["ja", "ju", "jo"],
    ["bya", "byu", "byo"],
    ["pya", "pyu", "pyo"]
  ];

  const KATA_TOKUSHU = [
    ["シェ", "ジェ", "チェ", "ティ"],
    ["ディ", "デュ", "トゥ", "ドゥ"],
    ["ファ", "フィ", "フェ", "フォ"],
    ["ウィ", "ウェ", "ウォ", "ヴ"],
    ["ヴァ", "ヴィ", "ヴェ", "ヴォ"],
    ["ツァ", "ツィ", "ツェ", "ツォ"]
  ];

  const ROMAJI_TOKUSHU = [
    ["she", "je", "che", "ti"],
    ["di", "dyu", "tu", "du"],
    ["fa", "fi", "fe", "fo"],
    ["wi", "we", "wo", "vu"],
    ["va", "vi", "ve", "vo"],
    ["tsa", "tsi", "tse", "tso"]
  ];

  function ensureStyles() {
    if (typeof document === "undefined" || !document.head) return;
    if (document.getElementById("kana-print-engine-styles")) return;
    const style = document.createElement("style");
    style.id = "kana-print-engine-styles";
    style.textContent = `
      .a4-sheet-page {
        width: 100%;
        max-width: 880px;
        aspect-ratio: 297 / 210;
        margin: 0 auto 18px auto;
        padding: 16px 20px;
        background: #FFFFFF;
        box-shadow: 0 4px 18px rgba(0,0,0,0.08);
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        justify-content: center;
      }
      .page-break {
        page-break-before: always;
        break-before: page;
      }
      .tianzige-cell {
        aspect-ratio: 1 / 1;
        width: 100%;
        box-sizing: border-box;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
      }
      @media print {
        @page {
          size: A4 landscape;
          margin: 8mm 10mm;
        }
        body {
          background: #FFFFFF !important;
          margin: 0 !important;
          padding: 0 !important;
          -webkit-print-color-adjust: exact !important;
          print-color-adjust: exact !important;
        }
        body * {
          visibility: hidden !important;
        }
        #printable-sheet-wrapper, #printable-sheet-area, #printable-sheet-area * {
          visibility: visible !important;
        }
        #printable-sheet-wrapper {
          position: absolute !important;
          left: 0 !important;
          top: 0 !important;
          width: 100% !important;
          margin: 0 !important;
          padding: 0 !important;
          background: transparent !important;
          box-shadow: none !important;
          overflow: visible !important;
        }
        .a4-sheet-page {
          box-shadow: none !important;
          border: none !important;
          border-radius: 0 !important;
          margin: 0 auto !important;
          padding: 0 !important;
          width: 277mm !important;
          height: 190mm !important;
          max-width: none !important;
          aspect-ratio: auto !important;
        }
        .no-print {
          display: none !important;
        }
      }
    `;
    document.head.appendChild(style);
  }

  window.KanaPrintSheetEngine = {
    containerId: "kana-print-studio-container",
    currentType: "hiragana", // "hiragana" | "katakana"
    currentSet: "50on",     // "50on" | "dakuon" | "youon" | "tokushu" | "all" | "kanji_grid"
    currentStyle: "trace",  // "trace" | "model" | "blank" | "test"

    init(containerId = "kana-print-studio-container") {
      this.containerId = containerId;
      ensureStyles();
      this.render();
    },

    setType(t) {
      this.currentType = t;
      if (t === "hiragana" && this.currentSet === "tokushu") {
        this.currentSet = "50on";
      }
      this.render();
    },

    setSet(s) {
      this.currentSet = s;
      this.render();
    },

    setStyle(st) {
      this.currentStyle = st;
      this.render();
    },

    render() {
      const container = document.getElementById(this.containerId);
      if (!container) return;

      const isHira = (this.currentType === "hiragana");
      const isKanaSet = ["50on", "dakuon", "youon", "tokushu", "all"].includes(this.currentSet);

      container.innerHTML = `
        <div style="display:flex; flex-direction:column; gap:16px;">
          <!-- 上部コントロールバー（画面上のみ表示、印刷時は完全非表示） -->
          <div class="no-print" style="background:#F8FAFC; border:1.5px solid #CBD5E1; border-radius:14px; padding:16px 20px; display:flex; flex-direction:column; gap:12px;">
            <!-- タイトル ＆ アクションボタン -->
            <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px; border-bottom:1.5px solid #E2E8F0; padding-bottom:12px;">
              <div>
                <div style="font-weight:800; font-size:1.15rem; color:#1E3A8A; display:flex; align-items:center; gap:8px;">
                  <span>🖨️</span>
                  <span>練習用紙プリント ＆ A4横PDFスタジオ</span>
                </div>
                <div style="font-size:0.83rem; color:#64748B; margin-top:2px;">
                  A4用紙横サイズ（297mm × 210mm）完全準拠・正方形マス田字格仕様
                </div>
              </div>

              <!-- 右側印刷/ダウンロードボタン -->
              <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
                <!-- 1. PDFダウンロードボタン (ユーザー要望最優先) -->
                <button id="btn-download-pdf" onclick="KanaPrintSheetEngine.downloadPDF()" style="background:#0284C7; color:white; border:none; padding:8px 18px; border-radius:10px; font-weight:800; font-size:0.88rem; cursor:pointer; display:inline-flex; align-items:center; gap:6px; box-shadow:0 2px 6px rgba(2,132,199,0.3); transition:all 0.15s;">
                  📥 A4横 PDFダウンロード
                </button>
                <!-- 2. A4印刷ボタン -->
                <button onclick="KanaPrintSheetEngine.printSheet()" style="background:#1E293B; color:white; border:none; padding:8px 16px; border-radius:10px; font-weight:800; font-size:0.88rem; cursor:pointer; display:inline-flex; align-items:center; gap:6px;">
                  🖨️ A4印刷 / 保存
                </button>
                <!-- 3. HTMLファイル保存 -->
                <button onclick="KanaPrintSheetEngine.downloadStandaloneHTML()" style="background:white; border:1.5px solid #CBD5E1; color:#334155; padding:8px 14px; border-radius:10px; font-weight:700; font-size:0.85rem; cursor:pointer; display:inline-flex; align-items:center; gap:6px;">
                  📄 HTMLファイル保存
                </button>
              </div>
            </div>

            <!-- フィルターセレクター 3段組み -->
            <div style="display:flex; flex-direction:column; gap:10px;">
              <!-- 1. 文字種: ひらがな / カタカナ -->
              ${isKanaSet ? `
              <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
                <span style="font-size:0.8rem; font-weight:800; color:#475569; min-width:65px;">文字種:</span>
                <div class="quiz-level-pills">
                  <button class="quiz-level-pill ${isHira ? "active" : ""}" onclick="KanaPrintSheetEngine.setType('hiragana')">あ ひらがな (Hiragana)</button>
                  <button class="quiz-level-pill ${!isHira ? "active" : ""}" onclick="KanaPrintSheetEngine.setType('katakana')">ア カタカナ (Katakana)</button>
                </div>
              </div>
              ` : ""}

              <!-- 2. 出題セット -->
              <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
                <span style="font-size:0.8rem; font-weight:800; color:#475569; min-width:65px;">文字セット:</span>
                <div class="quiz-level-pills">
                  <button class="quiz-level-pill ${this.currentSet === "50on" ? "active" : ""}" onclick="KanaPrintSheetEngine.setSet('50on')">🌸 五十音 (46字)</button>
                  <button class="quiz-level-pill ${this.currentSet === "dakuon" ? "active" : ""}" onclick="KanaPrintSheetEngine.setSet('dakuon')">🔔 濁音・半濁音 (25字)</button>
                  <button class="quiz-level-pill ${this.currentSet === "youon" ? "active" : ""}" onclick="KanaPrintSheetEngine.setSet('youon')">🎋 拗音 (33字)</button>
                  ${!isHira ? `
                    <button class="quiz-level-pill ${this.currentSet === "tokushu" ? "active" : ""}" onclick="KanaPrintSheetEngine.setSet('tokushu')">🌐 外来語特殊音 (24字)</button>
                  ` : ""}
                  <button class="quiz-level-pill ${this.currentSet === "all" ? "active" : ""}" onclick="KanaPrintSheetEngine.setSet('all')" style="background:${this.currentSet === "all" ? "#1E293B" : "#FFFFFF"}; color:${this.currentSet === "all" ? "#FFFFFF" : "#334155"}; font-weight:800;">
                    📦 全部まとめて一括印刷 (All Sets)
                  </button>
                  <button class="quiz-level-pill ${this.currentSet === "kanji_grid" ? "active" : ""}" onclick="KanaPrintSheetEngine.setSet('kanji_grid')">📝 白紙マス練習用 (たて7段・70マス)</button>
                </div>
              </div>

              <!-- 3. シート種別: 見本 / なぞる / 何もなし / テスト -->
              ${isKanaSet ? `
              <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
                <span style="font-size:0.8rem; font-weight:800; color:#475569; min-width:65px;">シート種別:</span>
                <div class="quiz-level-pills">
                  <button class="quiz-level-pill ${this.currentStyle === "trace" ? "active" : ""}" onclick="KanaPrintSheetEngine.setStyle('trace')">
                    ✍ なぞる（うすい文字＋練習）
                  </button>
                  <button class="quiz-level-pill ${this.currentStyle === "model" ? "active" : ""}" onclick="KanaPrintSheetEngine.setStyle('model')">
                    📖 見本（お手本・濃い文字）
                  </button>
                  <button class="quiz-level-pill ${this.currentStyle === "blank" ? "active" : ""}" onclick="KanaPrintSheetEngine.setStyle('blank')">
                    ⬜ 何もなし（白紙マス自習用・70マス）
                  </button>
                  <button class="quiz-level-pill ${this.currentStyle === "test" ? "active" : ""}" onclick="KanaPrintSheetEngine.setStyle('test')">
                    📝 テスト（ローマ字ヒント・空欄）
                  </button>
                </div>
              </div>
              ` : ""}
            </div>
          </div>

          <!-- プレビュー表示エリア（全画面収容・途切れ完全防止） -->
          <div id="printable-sheet-wrapper" style="width:100%; box-sizing:border-box; background:#F1F5F9; border-radius:12px; padding:16px 8px; display:flex; justify-content:center;">
            <div id="printable-sheet-area" style="width:100%; max-width:880px;">
              ${this.generateSheetPagesHTML()}
            </div>
          </div>
        </div>
      `;
    },

    generateSheetPagesHTML() {
      if (this.currentSet === "all") {
        const pages = ["50on", "dakuon", "youon"];
        if (this.currentType === "katakana") {
          pages.push("tokushu");
        }
        return pages.map((s, idx) => `
          <div class="a4-sheet-page ${idx > 0 ? "page-break" : ""}">
            ${this.renderSingleSheet(s)}
          </div>
        `).join("");
      } else {
        return `
          <div class="a4-sheet-page">
            ${this.renderSingleSheet(this.currentSet)}
          </div>
        `;
      }
    },

    renderSingleSheet(setName) {
      // 1. 何もなし（白紙練習用）または kanji_grid の場合: たて7段×よこ10列 = 70マスの正方形田字格
      if (this.currentStyle === "blank" || setName === "kanji_grid") {
        return this.renderBlank70GridSheet();
      }

      const isHira = (this.currentType === "hiragana");
      const scriptLabel = isHira ? "ひらがな" : "カタカナ";

      let setLabel = "";
      let cols = [];
      let romajiCols = [];

      if (setName === "50on") {
        setLabel = "五十音表";
        cols = isHira ? HIRA_50ON : KATA_50ON;
        romajiCols = ROMAJI_50ON;
      } else if (setName === "dakuon") {
        setLabel = "濁音・半濁音";
        cols = isHira ? HIRA_DAKUON : KATA_DAKUON;
        romajiCols = ROMAJI_DAKUON;
      } else if (setName === "youon") {
        setLabel = "拗音（きゃ・きゅ・きょ…）";
        cols = isHira ? HIRA_YOUON : KATA_YOUON;
        romajiCols = ROMAJI_YOUON;
      } else if (setName === "tokushu") {
        setLabel = "外来語・特殊音";
        cols = KATA_TOKUSHU;
        romajiCols = ROMAJI_TOKUSHU;
      }

      // Build grid cells with aspect-ratio: 1 / 1
      let gridHTML = "";
      if (setName === "50on") {
        // 10 columns Right to Left, 5 rows Top to Bottom (all square)
        gridHTML = `
          <div style="display:grid; grid-template-columns:repeat(10, 1fr); gap:0; border:2px solid #0284C7; background:white; width:100%; box-sizing:border-box;">
            ${Array.from({ length: 5 }).map((_, r) => {
              return Array.from({ length: 10 }).map((_, cIdx) => {
                const colNum = 9 - cIdx; // 9 down to 0 (Right to Left: あ行 is col 0, わ行 is col 9)
                const char = cols[colNum][r] || "";
                const romaji = romajiCols[colNum][r] || "";
                return this.renderCell(char, romaji, isHira);
              }).join("");
            }).join("")}
          </div>
        `;
      } else if (setName === "dakuon") {
        // 5 sounds Right to Left, each paired with a practice square = 10 columns x 5 rows
        gridHTML = `
          <div style="display:grid; grid-template-columns:repeat(10, 1fr); gap:0; border:2px solid #0284C7; background:white; width:100%; box-sizing:border-box;">
            ${Array.from({ length: 5 }).map((_, r) => {
              return [4, 3, 2, 1, 0].map(cNum => {
                const char = cols[cNum][r] || "";
                const romaji = romajiCols[cNum][r] || "";
                const targetCell = this.renderCell(char, romaji, isHira);
                const practiceCell = this.renderCell("", "", isHira, true);
                return practiceCell + targetCell; // Left is practice, Right is model
              }).join("");
            }).join("")}
          </div>
        `;
      } else if (setName === "youon") {
        // 11 sounds x 6 rows (3 vowels + 3 practice rows)
        gridHTML = `
          <div style="display:grid; grid-template-columns:repeat(11, 1fr); gap:0; border:2px solid #0284C7; background:white; width:100%; box-sizing:border-box;">
            ${Array.from({ length: 3 }).map((_, r) => {
              const modelRow = Array.from({ length: 11 }).map((_, cIdx) => {
                const colNum = 10 - cIdx; // 10 down to 0 (ぴゃ -> きゃ)
                const char = cols[colNum][r] || "";
                const romaji = romajiCols[colNum][r] || "";
                return this.renderCell(char, romaji, isHira);
              }).join("");
              const practiceRow = Array.from({ length: 11 }).map(() => {
                return this.renderCell("", "", isHira, true);
              }).join("");
              return modelRow + practiceRow;
            }).join("")}
          </div>
        `;
      } else if (setName === "tokushu") {
        // 6 sounds Right to Left, each paired with a practice square = 12 columns x 4 rows
        gridHTML = `
          <div style="display:grid; grid-template-columns:repeat(12, 1fr); gap:0; border:2px solid #0284C7; background:white; width:100%; box-sizing:border-box;">
            ${Array.from({ length: 4 }).map((_, r) => {
              return [5, 4, 3, 2, 1, 0].map(cNum => {
                const char = cols[cNum][r] || "";
                const romaji = romajiCols[cNum][r] || "";
                const targetCell = this.renderCell(char, romaji, isHira);
                const practiceCell = this.renderCell("", "", isHira, true);
                return practiceCell + targetCell;
              }).join("");
            }).join("")}
          </div>
        `;
      }

      return `
        <div style="width:100%; box-sizing:border-box;">
          <!-- 上部タイトル（不要な写真の飾り・日付・名前・補助線バッジを完全撤廃） -->
          <div style="font-size:1.15rem; font-weight:800; color:#1E293B; margin-bottom:10px; text-align:center; letter-spacing:1px;">
            ${scriptLabel} ${setLabel}
          </div>

          <!-- 正方形マス田字格グリッド本体 -->
          ${gridHTML}
        </div>
      `;
    },

    renderCell(char, romaji, isHira, isBlankPractice = false) {
      if (!char && !isBlankPractice) {
        // 空白マス（や行・わ行の存在しない音マス）
        return `
          <div class="tianzige-cell" style="border:1px solid #38BDF8; background:#F8FAFC;">
            <div style="position:absolute; inset:0; pointer-events:none;">
              <div style="position:absolute; top:50%; left:0; right:0; border-top:1px dashed #BAE6FD;"></div>
              <div style="position:absolute; left:50%; top:0; bottom:0; border-left:1px dashed #BAE6FD;"></div>
            </div>
          </div>
        `;
      }

      let charContent = "";
      if (isBlankPractice || this.currentStyle === "blank") {
        charContent = "";
      } else if (this.currentStyle === "test") {
        charContent = `
          <div style="position:absolute; top:4px; left:6px; font-size:clamp(0.6rem, 1.2vw, 0.75rem); font-weight:800; color:#0284C7; font-family:'Courier New', monospace;">
            [ ${romaji} ]
          </div>
        `;
      } else if (this.currentStyle === "model") {
        const fontSize = char.length > 1 ? "clamp(1.1rem, 2.2vw, 1.8rem)" : "clamp(1.6rem, 3.5vw, 2.7rem)";
        charContent = `
          <div style="font-size:${fontSize}; font-weight:800; color:#0F172A; font-family:${isHira ? "'Klee One', cursive, sans-serif" : "inherit"}; line-height:1; user-select:none;">
            ${char}
          </div>
          ${romaji ? `<div style="position:absolute; bottom:2px; right:4px; font-size:clamp(0.55rem, 0.9vw, 0.65rem); color:#64748B; font-weight:700;">${romaji}</div>` : ""}
        `;
      } else if (this.currentStyle === "trace") {
        const fontSize = char.length > 1 ? "clamp(1.1rem, 2.2vw, 1.8rem)" : "clamp(1.6rem, 3.5vw, 2.7rem)";
        charContent = `
          <div style="font-size:${fontSize}; font-weight:800; color:#CBD5E1; font-family:${isHira ? "'Klee One', cursive, sans-serif" : "inherit"}; line-height:1; user-select:none;">
            ${char}
          </div>
          ${romaji ? `<div style="position:absolute; bottom:2px; right:4px; font-size:clamp(0.55rem, 0.9vw, 0.65rem); color:#94A3B8; font-weight:700;">${romaji}</div>` : ""}
        `;
      }

      return `
        <div class="tianzige-cell" style="border:1px solid #38BDF8; background:white;">
          <!-- 十字補助線 (田字格) -->
          <div style="position:absolute; inset:0; pointer-events:none;">
            <div style="position:absolute; top:50%; left:0; right:0; border-top:1px dashed #BAE6FD;"></div>
            <div style="position:absolute; left:50%; top:0; bottom:0; border-left:1px dashed #BAE6FD;"></div>
          </div>
          ${charContent}
        </div>
      `;
    },

    renderBlank70GridSheet() {
      // ユーザー要望: 何も書いてない練習用は枠たて6か7にしてバランスよく -> たて7段×よこ10列 = 70マス正方形田字格
      return `
        <div style="width:100%; box-sizing:border-box;">
          <div style="font-size:1.15rem; font-weight:800; color:#1E293B; margin-bottom:10px; text-align:center; letter-spacing:1px;">
            練習用紙（マス目・十字補助線入り · 70マス）
          </div>

          <div style="display:grid; grid-template-columns:repeat(10, 1fr); gap:0; border:2px solid #0284C7; background:white; width:100%; box-sizing:border-box;">
            ${Array.from({ length: 7 }).map(() => {
              return Array.from({ length: 10 }).map(() => `
                <div class="tianzige-cell" style="border:1px solid #38BDF8; background:white;">
                  <div style="position:absolute; inset:0; pointer-events:none;">
                    <div style="position:absolute; top:50%; left:0; right:0; border-top:1px dashed #BAE6FD;"></div>
                    <div style="position:absolute; left:50%; top:0; bottom:0; border-left:1px dashed #BAE6FD;"></div>
                  </div>
                </div>
              `).join("");
            }).join("")}
          </div>
        </div>
      `;
    },

    printSheet() {
      const isHira = (this.currentType === "hiragana");
      const sheetHTML = this.generateSheetPagesHTML();
      const fullDoc = `<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>${isHira ? "ひらがな" : "カタカナ"} 練習用紙</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Klee+One:wght@400;600&family=Noto+Sans+JP:wght@400;700;900&display=swap" rel="stylesheet">
  <style>
    @page {
      size: A4 landscape;
      margin: 8mm 10mm;
    }
    * {
      box-sizing: border-box;
    }
    body {
      margin: 0;
      padding: 0;
      font-family: 'Noto Sans JP', sans-serif;
      background: #FFFFFF;
      color: #000000;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }
    .a4-sheet-page {
      width: 277mm;
      height: 190mm;
      box-sizing: border-box;
      margin: 0 auto;
      page-break-after: always;
      break-after: page;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    .tianzige-cell {
      aspect-ratio: 1 / 1;
      width: 100%;
      box-sizing: border-box;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .page-break {
      page-break-before: always;
      break-before: page;
    }
  </style>
</head>
<body>
  ${sheetHTML}
</body>
</html>`;

      let frame = document.getElementById("kana-print-iframe");
      if (!frame) {
        frame = document.createElement("iframe");
        frame.id = "kana-print-iframe";
        frame.style.position = "fixed";
        frame.style.right = "0";
        frame.style.bottom = "0";
        frame.style.width = "0";
        frame.style.height = "0";
        frame.style.border = "none";
        frame.style.visibility = "hidden";
        document.body.appendChild(frame);
      }

      try {
        const doc = frame.contentDocument || frame.contentWindow.document;
        doc.open();
        doc.write(fullDoc);
        doc.close();

        setTimeout(() => {
          try {
            frame.contentWindow.focus();
            frame.contentWindow.print();
          } catch (e) {
            window.print();
          }
        }, 350);
      } catch (e) {
        window.print();
      }
    },

    downloadPDF() {
      const isHira = (this.currentType === "hiragana");
      const filename = `${this.currentType}_${this.currentSet}_${this.currentStyle}_A4.pdf`;

      const runDownload = () => {
        const element = document.getElementById("printable-sheet-area");
        if (!element) return;

        const btn = document.getElementById("btn-download-pdf");
        const origText = btn ? btn.innerHTML : "";
        if (btn) btn.innerHTML = "⏳ PDF生成中...";

        const opt = {
          margin: [8, 10, 8, 10],
          filename: filename,
          image: { type: "jpeg", quality: 0.98 },
          html2canvas: { scale: 2, useCORS: true, letterRendering: true, logging: false },
          jsPDF: { unit: "mm", format: "a4", orientation: "landscape" }
        };

        if (window.html2pdf) {
          window.html2pdf().set(opt).from(element).save().then(() => {
            if (btn) btn.innerHTML = origText;
          }).catch(err => {
            console.error(err);
            if (btn) btn.innerHTML = origText;
            this.printSheet();
          });
        } else {
          if (btn) btn.innerHTML = origText;
          this.printSheet();
        }
      };

      if (window.html2pdf) {
        runDownload();
      } else {
        const s = document.createElement("script");
        s.src = "https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js";
        s.onload = runDownload;
        s.onerror = () => {
          this.printSheet();
        };
        document.head.appendChild(s);
      }
    },

    downloadStandaloneHTML() {
      const isHira = (this.currentType === "hiragana");
      const filename = `${this.currentType}_${this.currentSet}_${this.currentStyle}_worksheet.html`;

      const sheetHTML = this.generateSheetPagesHTML();
      const fullDoc = `<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>${isHira ? "ひらがな" : "カタカナ"} 練習用紙</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Klee+One:wght@400;600&family=Noto+Sans+JP:wght@400;700;900&display=swap" rel="stylesheet">
  <style>
    @page {
      size: A4 landscape;
      margin: 8mm 10mm;
    }
    body {
      margin: 0;
      padding: 10px;
      font-family: 'Noto Sans JP', sans-serif;
      background: #FFFFFF;
      color: #000000;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }
    .a4-sheet-page {
      width: 277mm;
      height: 190mm;
      box-sizing: border-box;
      margin: 0 auto 20px auto;
      page-break-after: always;
      break-after: page;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    .tianzige-cell {
      aspect-ratio: 1 / 1;
      width: 100%;
      box-sizing: border-box;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .page-break {
      page-break-before: always;
      break-before: page;
    }
    @media print {
      body {
        padding: 0;
      }
      .no-print {
        display: none !important;
      }
    }
  </style>
</head>
<body>
  <div class="no-print" style="text-align:center; padding:12px; background:#EFF6FF; border-bottom:1px solid #BFDBFE; margin-bottom:14px;">
    <button onclick="window.print()" style="background:#1D4ED8; color:white; border:none; padding:8px 20px; border-radius:8px; font-weight:800; font-size:1rem; cursor:pointer;">
      🖨️ A4サイズで印刷する / PDFとして保存
    </button>
  </div>
  ${sheetHTML}
</body>
</html>`;

      const blob = new Blob([fullDoc], { type: "text/html;charset=utf-8" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }
  };
})();
