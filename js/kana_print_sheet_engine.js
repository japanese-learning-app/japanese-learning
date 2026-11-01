/**
 * かな・漢字 練習用紙プリント＆PDFダウンロード エンジン
 * A4用紙サイズ（横向き）完全準拠
 * 見本・なぞる・何もなし・テスト × 50音・濁音・拗音・特殊音・全セット一括 ＆ 漢字練習帳・原稿用紙
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
        width: 277mm;
        min-height: 190mm;
        box-sizing: border-box;
        margin: 0 auto 24px auto;
        padding: 8mm 10mm 6mm 10mm;
        background: #FFFFFF;
        box-shadow: 0 4px 18px rgba(0,0,0,0.12);
        border-radius: 6px;
      }
      .page-break {
        page-break-before: always;
        break-before: page;
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
          border-radius: 0 !important;
          margin: 0 auto !important;
          padding: 0 !important;
          width: 277mm !important;
          min-height: 190mm !important;
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
    currentSet: "50on",     // "50on" | "dakuon" | "youon" | "tokushu" | "all" | "kanji_grid" | "genko"
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
                  <span>かな・漢字 練習用紙プリント ＆ PDF保存スタジオ</span>
                </div>
                <div style="font-size:0.83rem; color:#64748B; margin-top:2px;">
                  幼児・小学生・外国人学習者用 A4用紙サイズ（横向き）十字リーダー入りマス完全対応
                </div>
              </div>

              <!-- 右側印刷/ダウンロードボタン -->
              <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
                <button onclick="KanaPrintSheetEngine.printSheet()" style="background:#1D4ED8; color:white; border:none; padding:8px 18px; border-radius:10px; font-weight:800; font-size:0.88rem; cursor:pointer; display:inline-flex; align-items:center; gap:6px; box-shadow:0 2px 6px rgba(29,78,216,0.25);">
                  🖨️ A4サイズで印刷 / PDF保存
                </button>
                <button onclick="KanaPrintSheetEngine.downloadStandaloneHTML()" style="background:white; border:1.5px solid #CBD5E1; color:#334155; padding:8px 14px; border-radius:10px; font-weight:700; font-size:0.85rem; cursor:pointer; display:inline-flex; align-items:center; gap:6px;">
                  ⬇️ HTMLファイル保存
                </button>
              </div>
            </div>

            <!-- フィルターセレクター 3段組み -->
            <div style="display:flex; flex-direction:column; gap:10px;">
              <!-- 1. 文字種: ひらがな / カタカナ (かなセット選択時のみ) -->
              ${isKanaSet ? `
              <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
                <span style="font-size:0.8rem; font-weight:800; color:#475569; min-width:65px;">文字種:</span>
                <div class="quiz-level-pills">
                  <button class="quiz-level-pill ${isHira ? "active" : ""}" onclick="KanaPrintSheetEngine.setType('hiragana')">あ ひらがな (Hiragana)</button>
                  <button class="quiz-level-pill ${!isHira ? "active" : ""}" onclick="KanaPrintSheetEngine.setType('katakana')">ア カタカナ (Katakana)</button>
                </div>
              </div>
              ` : ""}

              <!-- 2. 出題セット: 五十音 / 濁音・半濁音 / 拗音 / 特殊音 / 全部一括 / 漢字練習帳 / 原稿用紙 -->
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
                  <button class="quiz-level-pill ${this.currentSet === "kanji_grid" ? "active" : ""}" onclick="KanaPrintSheetEngine.setSet('kanji_grid')">📝 漢字練習帳 (84マス)</button>
                  <button class="quiz-level-pill ${this.currentSet === "genko" ? "active" : ""}" onclick="KanaPrintSheetEngine.setSet('genko')">📜 原稿用紙 (400字詰)</button>
                </div>
              </div>

              <!-- 3. シート種別: 見本 / なぞる / 何もなし / テスト (かな練習時) -->
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
                    ⬜ 何もなし（白紙マス自習用）
                  </button>
                  <button class="quiz-level-pill ${this.currentStyle === "test" ? "active" : ""}" onclick="KanaPrintSheetEngine.setStyle('test')">
                    📝 テスト（ローマ字ヒント・空欄）
                  </button>
                </div>
              </div>
              ` : ""}
            </div>
          </div>

          <!-- プレビュー表示エリア ＆ 印刷ターゲット領域 -->
          <div id="printable-sheet-wrapper" style="overflow-x:auto; padding:16px 0; background:#E2E8F0; border-radius:12px; display:flex; justify-content:center;">
            <div id="printable-sheet-area">
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
      if (setName === "kanji_grid") {
        return this.renderKanjiGridSheet();
      }
      if (setName === "genko") {
        return this.renderGenkoSheet();
      }

      const isHira = (this.currentType === "hiragana");
      const scriptLabel = isHira ? "ひらがな" : "カタカナ";

      let setLabel = "";
      let cols = [];
      let romajiCols = [];

      if (setName === "50on") {
        setLabel = "50おん の れんしゅう";
        cols = isHira ? HIRA_50ON : KATA_50ON;
        romajiCols = ROMAJI_50ON;
      } else if (setName === "dakuon") {
        setLabel = "だくおん・はんだくおん の れんしゅう";
        cols = isHira ? HIRA_DAKUON : KATA_DAKUON;
        romajiCols = ROMAJI_DAKUON;
      } else if (setName === "youon") {
        setLabel = "ようおん（きゃ・きゅ・きょ…）の れんしゅう";
        cols = isHira ? HIRA_YOUON : KATA_YOUON;
        romajiCols = ROMAJI_YOUON;
      } else if (setName === "tokushu") {
        setLabel = "がいらいご・とくしゅおん の れんしゅう";
        cols = KATA_TOKUSHU;
        romajiCols = ROMAJI_TOKUSHU;
      }

      // Instruction based on style
      let subTitle = "";
      if (this.currentStyle === "trace") {
        subTitle = `うすい ${scriptLabel}を なぞりましょう。`;
      } else if (this.currentStyle === "model") {
        subTitle = `おてほんの ${scriptLabel}を よくみて、ただしい かきじゅんで かきましょう。`;
      } else if (this.currentStyle === "blank") {
        subTitle = `マスめの なかに、じぶんで ただしく ${scriptLabel}を かきましょう。`;
      } else if (this.currentStyle === "test") {
        subTitle = `ローマじを みて、ただしい ${scriptLabel}を かきましょう。（テスト）`;
      }

      // Build grid cells
      let gridHTML = "";
      if (setName === "50on") {
        // 10 columns Right to Left, 5 rows Top to Bottom
        gridHTML = `
          <div style="display:grid; grid-template-columns:repeat(10, 1fr); gap:0; border:2px solid #0284C7; background:white;">
            ${Array.from({ length: 5 }).map((_, r) => {
              return Array.from({ length: 10 }).map((_, cIdx) => {
                const colNum = 9 - cIdx; // 9, 8, 7, ... 0 (Right to Left: あ行 is col 0, わ行 is col 9)
                const char = cols[colNum][r] || "";
                const romaji = romajiCols[colNum][r] || "";
                return this.renderCell(char, romaji, isHira);
              }).join("");
            }).join("")}
          </div>
        `;
      } else if (setName === "dakuon") {
        // 5 sounds Right to Left, each followed by a blank practice box
        gridHTML = `
          <div style="display:grid; grid-template-columns:repeat(10, 1fr); gap:0; border:2px solid #0284C7; background:white;">
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
        // 11 columns Right to Left, 3 rows
        gridHTML = `
          <div style="display:grid; grid-template-columns:repeat(11, 1fr); gap:0; border:2px solid #0284C7; background:white;">
            ${Array.from({ length: 3 }).map((_, r) => {
              return Array.from({ length: 11 }).map((_, cIdx) => {
                const colNum = 10 - cIdx; // 10 down to 0 (ぴゃ -> きゃ)
                const char = cols[colNum][r] || "";
                const romaji = romajiCols[colNum][r] || "";
                return this.renderCell(char, romaji, isHira, false, "youon");
              }).join("");
            }).join("")}
          </div>
        `;
      } else if (setName === "tokushu") {
        // 6 columns Right to Left, 4 rows
        gridHTML = `
          <div style="display:grid; grid-template-columns:repeat(6, 1fr); gap:0; border:2px solid #0284C7; background:white;">
            ${Array.from({ length: 4 }).map((_, r) => {
              return Array.from({ length: 6 }).map((_, cIdx) => {
                const colNum = 5 - cIdx;
                const char = cols[colNum][r] || "";
                const romaji = romajiCols[colNum][r] || "";
                return this.renderCell(char, romaji, isHira, false, "tokushu");
              }).join("");
            }).join("")}
          </div>
        `;
      }

      return `
        <div style="width:100%; box-sizing:border-box;">
          <!-- 上部ヘッダー (ちびむすドリル完全一致レイアウト) -->
          <div style="display:flex; align-items:flex-end; justify-content:space-between; margin-bottom:10px; border-bottom:1.5px solid #000; padding-bottom:8px;">
            <div>
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-size:0.75rem; background:#E0F2FE; color:#0369A1; font-weight:800; padding:2px 8px; border-radius:4px; border:1px solid #BAE6FD;">十字補助線入りマス</span>
                <span style="font-size:1.25rem; font-weight:900; color:#000; letter-spacing:1px;">■ ${scriptLabel}　${setLabel}</span>
              </div>
              <div style="font-size:0.82rem; color:#334155; margin-top:4px; font-weight:700;">
                ${subTitle}
              </div>
            </div>

            <div style="display:flex; align-items:center; gap:16px;">
              <div style="font-size:0.9rem; font-weight:800; color:#000;">
                _____ がつ _____ にち
              </div>
              <div style="border:1.5px solid #000; padding:4px 10px; display:flex; align-items:center; gap:8px; min-width:180px; height:36px; box-sizing:border-box;">
                <span style="font-size:0.75rem; writing-mode:vertical-rl; font-weight:800; border-right:1px solid #000; padding-right:4px;">なまえ</span>
                <span style="flex:1;"></span>
              </div>
            </div>
          </div>

          <!-- グリッド本体 -->
          ${gridHTML}

          <!-- フッター -->
          <div style="display:flex; align-items:center; justify-content:space-between; margin-top:8px; font-size:0.68rem; color:#64748B;">
            <span>◎ 日本語学習アプリ・ハク先生オリジナル教材（A4横サイズ練習プリント）</span>
            <span>https://nihongo-learning.app</span>
          </div>
        </div>
      `;
    },

    renderCell(char, romaji, isHira, isBlankPractice = false, mode = "default") {
      const minH = (mode === "youon") ? "105px" : (mode === "tokushu" ? "95px" : "86px");

      if (!char && !isBlankPractice) {
        // 存在しない音（yi, ye, wuなど空欄マス）
        return `
          <div style="border:1px solid #38BDF8; background:#F8FAFC; min-height:${minH}; position:relative; box-sizing:border-box;">
            <!-- 十字補助線 -->
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
          <div style="position:absolute; top:4px; left:6px; font-size:0.72rem; font-weight:800; color:#0284C7; font-family:'Courier New', monospace;">
            [ ${romaji} ]
          </div>
        `;
      } else if (this.currentStyle === "model") {
        const fontSize = char.length > 1 ? "2.0rem" : "2.9rem";
        charContent = `
          <div style="font-size:${fontSize}; font-weight:800; color:#0F172A; font-family:${isHira ? "'Klee One', cursive, sans-serif" : "inherit"}; line-height:1; user-select:none;">
            ${char}
          </div>
          ${romaji ? `<div style="position:absolute; bottom:2px; right:4px; font-size:0.65rem; color:#64748B; font-weight:700;">${romaji}</div>` : ""}
        `;
      } else if (this.currentStyle === "trace") {
        const fontSize = char.length > 1 ? "2.0rem" : "2.9rem";
        charContent = `
          <div style="font-size:${fontSize}; font-weight:800; color:#CBD5E1; font-family:${isHira ? "'Klee One', cursive, sans-serif" : "inherit"}; line-height:1; user-select:none;">
            ${char}
          </div>
          ${romaji ? `<div style="position:absolute; bottom:2px; right:4px; font-size:0.65rem; color:#94A3B8; font-weight:700;">${romaji}</div>` : ""}
        `;
      }

      return `
        <div style="border:1px solid #38BDF8; background:white; min-height:${minH}; position:relative; box-sizing:border-box; display:flex; align-items:center; justify-content:center;">
          <!-- 十字補助線 (田字格) -->
          <div style="position:absolute; inset:0; pointer-events:none;">
            <div style="position:absolute; top:50%; left:0; right:0; border-top:1px dashed #BAE6FD;"></div>
            <div style="position:absolute; left:50%; top:0; bottom:0; border-left:1px dashed #BAE6FD;"></div>
          </div>
          ${charContent}
        </div>
      `;
    },

    renderKanjiGridSheet() {
      // 14 columns × 6 rows = 84 田字格マス
      return `
        <div style="width:100%; box-sizing:border-box;">
          <div style="display:flex; align-items:flex-end; justify-content:space-between; margin-bottom:10px; border-bottom:1.5px solid #000; padding-bottom:8px;">
            <div>
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-size:0.75rem; background:#E0F2FE; color:#0369A1; font-weight:800; padding:2px 8px; border-radius:4px; border:1px solid #BAE6FD;">84マス 田字格</span>
                <span style="font-size:1.25rem; font-weight:900; color:#000; letter-spacing:1px;">■ 漢字練習用紙（マス目・十字補助線入り）</span>
              </div>
              <div style="font-size:0.82rem; color:#334155; margin-top:4px; font-weight:700;">
                十字補助線をめやすにして、漢字のへんとつくり、バランスを意識して丁寧に練習しましょう。
              </div>
            </div>
            <div style="display:flex; align-items:center; gap:16px;">
              <div style="font-size:0.9rem; font-weight:800; color:#000;">_____ がつ _____ にち</div>
              <div style="border:1.5px solid #000; padding:4px 10px; display:flex; align-items:center; gap:8px; min-width:180px; height:36px; box-sizing:border-box;">
                <span style="font-size:0.75rem; writing-mode:vertical-rl; font-weight:800; border-right:1px solid #000; padding-right:4px;">なまえ</span>
                <span style="flex:1;"></span>
              </div>
            </div>
          </div>

          <div style="display:grid; grid-template-columns:repeat(14, 1fr); gap:0; border:2px solid #0284C7; background:white;">
            ${Array.from({ length: 6 }).map(() => {
              return Array.from({ length: 14 }).map(() => `
                <div style="border:1px solid #38BDF8; background:white; min-height:86px; position:relative; box-sizing:border-box;">
                  <div style="position:absolute; inset:0; pointer-events:none;">
                    <div style="position:absolute; top:50%; left:0; right:0; border-top:1px dashed #BAE6FD;"></div>
                    <div style="position:absolute; left:50%; top:0; bottom:0; border-left:1px dashed #BAE6FD;"></div>
                  </div>
                </div>
              `).join("");
            }).join("")}
          </div>

          <div style="display:flex; align-items:center; justify-content:space-between; margin-top:8px; font-size:0.68rem; color:#64748B;">
            <span>◎ 日本語学習アプリ・ハク先生オリジナル教材（A4横サイズ 84マス漢字練習帳）</span>
            <span>https://nihongo-learning.app</span>
          </div>
        </div>
      `;
    },

    renderGenkoSheet() {
      // 20 columns × 20 rows = 400字詰 原稿用紙
      return `
        <div style="width:100%; box-sizing:border-box;">
          <div style="display:flex; align-items:flex-end; justify-content:space-between; margin-bottom:10px; border-bottom:1.5px solid #0D7A5F; padding-bottom:8px;">
            <div>
              <span style="font-size:1.2rem; font-weight:900; color:#0D7A5F; letter-spacing:2px;">■ 原稿用紙（400字詰 · 20字×20行）</span>
              <div style="font-size:0.8rem; color:#475569; margin-top:4px;">短作文、日記、長文記述練習用（縦書き）</div>
            </div>
            <div style="display:flex; align-items:center; gap:20px; font-size:0.88rem; color:#334155; font-weight:700;">
              <div>題名: ___________________________</div>
              <div>氏名: ___________________________</div>
            </div>
          </div>

          <!-- 原稿用紙グリッド (上段10行 + 中央魚尾 + 下段10行) -->
          <div style="border:2px solid #0D7A5F; padding:6px; background:#FAFCFB;">
            <!-- 上段10マス -->
            <div style="display:grid; grid-template-columns:repeat(20, 1fr); gap:0; border:1px solid #0D7A5F; background:white;">
              ${Array.from({ length: 10 }).map(() => {
                return Array.from({ length: 20 }).map(() => `
                  <div style="border:0.5px solid #A7D7C5; min-height:24px; box-sizing:border-box; background:white;"></div>
                `).join("");
              }).join("")}
            </div>

            <!-- 中央 魚尾（余白・行番号・区切り） -->
            <div style="display:flex; align-items:center; justify-content:space-between; height:18px; padding:0 12px; font-size:0.7rem; color:#0D7A5F; font-weight:800; border-top:1px solid #0D7A5F; border-bottom:1px solid #0D7A5F; background:#F0FDF4;">
              <span>← 20字詰</span>
              <span>☖ 二〇 × 二〇（四〇〇字） ☗</span>
              <span>20行 →</span>
            </div>

            <!-- 下段10マス -->
            <div style="display:grid; grid-template-columns:repeat(20, 1fr); gap:0; border:1px solid #0D7A5F; background:white;">
              ${Array.from({ length: 10 }).map(() => {
                return Array.from({ length: 20 }).map(() => `
                  <div style="border:0.5px solid #A7D7C5; min-height:24px; box-sizing:border-box; background:white;"></div>
                `).join("");
              }).join("")}
            </div>
          </div>

          <div style="display:flex; align-items:center; justify-content:space-between; margin-top:8px; font-size:0.68rem; color:#64748B;">
            <span>◎ 日本語学習アプリ・ハク先生オリジナル教材（A4横サイズ 400字詰原稿用紙）</span>
            <span>https://nihongo-learning.app</span>
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
  <title>${isHira ? "ひらがな" : "カタカナ"} 練習用紙プリント</title>
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
      min-height: 190mm;
      box-sizing: border-box;
      margin: 0 auto;
      page-break-after: always;
      break-after: page;
      padding: 4mm 0;
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

    downloadStandaloneHTML() {
      const isHira = (this.currentType === "hiragana");
      const filename = `${this.currentType}_${this.currentSet}_${this.currentStyle}_worksheet.html`;

      const sheetHTML = this.generateSheetPagesHTML();
      const fullDoc = `<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>${isHira ? "ひらがな" : "カタカナ"} 練習用紙プリント</title>
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
      min-height: 190mm;
      box-sizing: border-box;
      margin: 0 auto 20px auto;
      page-break-after: always;
      break-after: page;
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
