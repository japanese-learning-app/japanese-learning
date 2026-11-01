# -*- coding: utf-8 -*-
"""
Translate the Kana quiz UI (for both Hiragana and Katakana) to English as requested by user.
Also updates the mode selector pills to bilingual/English (Hiragana: Practice/Test, Katakana: Practice/Test).
"""

import re

def update_files():
    with open('app.html', 'r', encoding='utf-8') as f:
        code = f.read()

    # 1. Update the mode pills in HTML header:
    old_header_pills = '''          <!-- 上部モード切替: ひらがな（練習 / テスト） カタカナ（練習 / テスト） -->
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
          </div>'''

    new_header_pills = '''          <!-- 上部モード切替: ひらがな（練習 / テスト） カタカナ（練習 / テスト） -->
          <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px; margin-bottom:16px; border-bottom:1.5px solid #F1F5F9; padding-bottom:12px;">
            <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
              <!-- ひらがな: 練習 / テスト -->
              <div style="display:inline-flex; align-items:center; gap:4px; background:#F8FAFC; border:1.5px solid #CBD5E1; padding:4px 8px; border-radius:10px;">
                <span style="font-weight:800; font-size:0.86rem; color:#1E3A8A; margin-right:4px;">ひらがな (Hiragana):</span>
                <button class="quiz-level-pill active" id="btn-mode-hira-trace" onclick="selectKanaMode('hiragana', 'trace')">練習 (Practice)</button>
                <button class="quiz-level-pill" id="btn-mode-hira-quiz" onclick="selectKanaMode('hiragana', 'quiz')">テスト (Quiz)</button>
              </div>

              <!-- カタカナ: 練習 / テスト -->
              <div style="display:inline-flex; align-items:center; gap:4px; background:#F8FAFC; border:1.5px solid #CBD5E1; padding:4px 8px; border-radius:10px;">
                <span style="font-weight:800; font-size:0.86rem; color:#1E3A8A; margin-right:4px;">カタカナ (Katakana):</span>
                <button class="quiz-level-pill" id="btn-mode-kata-trace" onclick="selectKanaMode('katakana', 'trace')">練習 (Practice)</button>
                <button class="quiz-level-pill" id="btn-mode-kata-quiz" onclick="selectKanaMode('katakana', 'quiz')">テスト (Quiz)</button>
              </div>
            </div>
          </div>'''

    if old_header_pills in code:
        code = code.replace(old_header_pills, new_header_pills)
        print("Updated header mode pills!")

    # 2. Update KanaWritingQuiz methods: retryMissed and render
    # Replace retryMissed alert
    code = code.replace(
        "alert('まちがえた文字はありません！全問正解です🎉');",
        "alert('No missed characters! Perfect score! 🎉');"
    )

    # Find KanaWritingQuiz.render
    m = re.search(r'(render\(\)\s*\{[\s\S]*?initQuizCanvas\(\);[\s\S]*?\},)', code)
    assert m, "KanaWritingQuiz.render block not found!"

    new_render_func = '''render() {
      const container = document.getElementById(this.containerId);
      if (!container) return;

      const isHira = (this.currentType === 'hiragana');
      const typeLabelEn = isHira ? 'Hiragana' : 'Katakana';
      const catLabelsEn = {
        all: 'All',
        seion: 'Basic (46)',
        dakuon: 'Dakuon (25)',
        youon: 'Combos (33)',
        tokushu: 'Special (24)'
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
            <div style="font-size:1.3rem; font-weight:800; color:#1E293B;">Quiz Completed! Great job!</div>
            <div style="font-size:0.9rem; color:#64748B; margin-top:4px;">
              【${typeLabelEn} / ${catLabelsEn[this.currentCategory] || 'All'}】 Total ${total} Questions
            </div>

            <!-- Score Cards -->
            <div style="display:flex; justify-content:center; gap:20px; margin:20px 0; flex-wrap:wrap;">
              <div style="background:white; border:1.5px solid #86EFAC; border-radius:12px; padding:12px 24px; text-align:center; min-width:110px;">
                <div style="font-size:0.78rem; font-weight:800; color:#15803D;">⭕ Correct</div>
                <div style="font-size:1.8rem; font-weight:900; color:#16A34A; margin-top:2px;">${correctCount}</div>
              </div>
              <div style="background:white; border:1.5px solid #FCA5A5; border-radius:12px; padding:12px 24px; text-align:center; min-width:110px;">
                <div style="font-size:0.78rem; font-weight:800; color:#B91C1C;">❌ Incorrect</div>
                <div style="font-size:1.8rem; font-weight:900; color:#DC2626; margin-top:2px;">${wrongCount}</div>
              </div>
              <div style="background:white; border:1.5px solid #93C5FD; border-radius:12px; padding:12px 24px; text-align:center; min-width:110px;">
                <div style="font-size:0.78rem; font-weight:800; color:#1D4ED8;">Accuracy</div>
                <div style="font-size:1.8rem; font-weight:900; color:#2563EB; margin-top:2px;">${pct}%</div>
              </div>
            </div>

            ${missedList.length > 0 ? `
              <!-- Missed characters review -->
              <div style="background:white; border:1.5px solid #FECACA; border-radius:14px; padding:16px; margin:20px auto; max-width:600px; text-align:left;">
                <div style="font-size:0.88rem; font-weight:800; color:#991B1B; margin-bottom:10px; display:flex; align-items:center; justify-content:space-between;">
                  <span>❌ Missed Characters (Tap to practice tracing)</span>
                  <span style="font-size:0.76rem; color:#B91C1C; font-weight:700;">${missedList.length} Characters</span>
                </div>
                <div style="display:flex; flex-wrap:wrap; gap:8px;">
                  ${missedList.map(item => `
                    <div onclick="KanaWritingQuiz.practiceTraceChar('${item.char}', '${item.romaji}')" style="background:#FEF2F2; border:1.5px solid #F87171; border-radius:8px; padding:6px 12px; display:flex; align-items:center; gap:8px; cursor:pointer;" title="Practice tracing">
                      <span style="font-size:1.3rem; font-weight:800; color:#991B1B;">${item.char}</span>
                      <span style="font-size:0.75rem; color:#7F1D1D;">[ ${item.romaji} ]</span>
                      <span style="font-size:0.72rem; color:#DC2626; font-weight:700;">✍ Practice</span>
                    </div>
                  `).join('')}
                </div>
              </div>
            ` : `
              <div style="background:#F0FDF4; border:1.5px solid #86EFAC; border-radius:12px; padding:14px; margin:16px auto; max-width:500px; color:#15803D; font-weight:700;">
                🎉 Outstanding! Perfect score! Keep up the great work!
              </div>
            `}

            <!-- Action buttons -->
            <div style="display:flex; justify-content:center; gap:12px; margin-top:20px; flex-wrap:wrap;">
              ${missedList.length > 0 ? `
                <button onclick="KanaWritingQuiz.retryMissed()" style="background:#DC2626; color:white; border:none; padding:10px 20px; border-radius:10px; font-weight:800; font-size:0.92rem; cursor:pointer; box-shadow:0 2px 6px rgba(220,38,38,0.25);">
                  ❌ Retest Missed Only
                </button>
              ` : ''}
              <button onclick="KanaWritingQuiz.startQuiz()" style="background:var(--kobe-blue); color:white; border:none; padding:10px 20px; border-radius:10px; font-weight:800; font-size:0.92rem; cursor:pointer; box-shadow:0 2px 6px rgba(29,78,216,0.25);">
                ↺ Retake Quiz
              </button>
            </div>
          </div>
        `;
        return;
      }

      if (this.questions.length === 0) {
        container.innerHTML = '<div style="padding:40px; text-align:center; color:#64748B;">No questions available for this category.</div>';
        return;
      }

      const q = this.questions[this.currentIndex];
      const isFirst = (this.currentIndex === 0);
      const isLast = (this.currentIndex === this.questions.length - 1);
      const maxAllCount = isHira ? 104 : 128;

      container.innerHTML = `
        <div style="display:flex; flex-direction:column; gap:14px;">
          <!-- Toolbar: Script / Scope / Order in English -->
          <div style="background:#F8FAFC; border:1.5px solid #E2E8F0; border-radius:14px; padding:12px 16px; display:flex; flex-direction:column; gap:10px;">
            <!-- Line 1: Script & Scope -->
            <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px;">
              <div style="display:flex; align-items:center; gap:6px; flex-wrap:wrap;">
                <span style="font-size:0.78rem; font-weight:800; color:#475569;">Script:</span>
                <div class="quiz-level-pills">
                  <button class="quiz-level-pill ${this.currentType === 'hiragana' ? 'active' : ''}" onclick="KanaWritingQuiz.setType('hiragana')">Hiragana</button>
                  <button class="quiz-level-pill ${this.currentType === 'katakana' ? 'active' : ''}" onclick="KanaWritingQuiz.setType('katakana')">Katakana</button>
                </div>
              </div>
              <div style="display:flex; align-items:center; gap:6px; flex-wrap:wrap;">
                <span style="font-size:0.78rem; font-weight:800; color:#475569;">Scope:</span>
                <div class="quiz-level-pills">
                  <button class="quiz-level-pill ${this.currentCategory === 'all' ? 'active' : ''}" onclick="KanaWritingQuiz.setCategory('all')">All (${this.questions.length > 0 && this.currentCategory === 'all' && this.currentMode !== 'extract' ? this.questions.length : maxAllCount})</button>
                  <button class="quiz-level-pill ${this.currentCategory === 'seion' ? 'active' : ''}" onclick="KanaWritingQuiz.setCategory('seion')">Basic (46)</button>
                  <button class="quiz-level-pill ${this.currentCategory === 'dakuon' ? 'active' : ''}" onclick="KanaWritingQuiz.setCategory('dakuon')">Dakuon (25)</button>
                  <button class="quiz-level-pill ${this.currentCategory === 'youon' ? 'active' : ''}" onclick="KanaWritingQuiz.setCategory('youon')">Combos (33)</button>
                  ${!isHira ? `
                    <button class="quiz-level-pill ${this.currentCategory === 'tokushu' ? 'active' : ''}" onclick="KanaWritingQuiz.setCategory('tokushu')">Special (24)</button>
                  ` : ''}
                </div>
              </div>
            </div>

            <!-- Line 2: Order / Mode in English -->
            <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px; border-top:1px dashed #CBD5E1; padding-top:8px;">
              <div style="display:flex; align-items:center; gap:6px; flex-wrap:wrap;">
                <span style="font-size:0.78rem; font-weight:800; color:#475569;">Order:</span>
                <div class="quiz-level-pills">
                  <button class="quiz-level-pill ${this.currentMode === 'sequential' ? 'active' : ''}" onclick="KanaWritingQuiz.setMode('sequential')">In Order</button>
                  <button class="quiz-level-pill ${this.currentMode === 'shuffle' ? 'active' : ''}" onclick="KanaWritingQuiz.setMode('shuffle')">Shuffle</button>
                  <button class="quiz-level-pill ${this.currentMode === 'extract' && this.extractCount === 10 ? 'active' : ''}" onclick="KanaWritingQuiz.setMode('extract', 10)">Quick 10</button>
                  <button class="quiz-level-pill ${this.currentMode === 'extract' && this.extractCount === 20 ? 'active' : ''}" onclick="KanaWritingQuiz.setMode('extract', 20)">Quick 20</button>
                  <button class="quiz-level-pill ${this.currentMode === 'extract' && this.extractCount === 25 ? 'active' : ''}" onclick="KanaWritingQuiz.setMode('extract', 25)">Quick 25</button>
                </div>
              </div>
              <button onclick="KanaWritingQuiz.startQuiz()" style="background:white; border:1px solid #CBD5E1; color:#475569; padding:4px 10px; border-radius:6px; font-size:0.75rem; font-weight:700; cursor:pointer;" title="Reset quiz to beginning">
                ↺ Reset
              </button>
            </div>
          </div>

          <!-- Main Test Card -->
          <div style="background:white; border:1.5px solid var(--border-soft); border-radius:16px; padding:20px; box-shadow:0 2px 10px rgba(0,0,0,0.03);">
            <!-- Top info bar: Question number & Score -->
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:14px; flex-wrap:wrap; gap:8px;">
              <div style="font-size:0.92rem; font-weight:800; color:#1E3A8A; display:flex; align-items:center; gap:8px;">
                <span style="background:#EFF6FF; color:#1D4ED8; padding:2px 8px; border-radius:6px; font-size:0.8rem; border:1px solid #BFDBFE;">Question ${this.currentIndex + 1} / ${this.questions.length}</span>
                <span>Write in 【${typeLabelEn}】</span>
              </div>
              <div style="display:flex; align-items:center; gap:8px; font-size:0.82rem; font-weight:800;">
                <span style="color:#16A34A; background:#DCFCE7; padding:2px 8px; border-radius:6px;">⭕ ${correctCount}</span>
                <span style="color:#DC2626; background:#FEE2E2; padding:2px 8px; border-radius:6px;">❌ ${wrongCount}</span>
              </div>
            </div>

            <!-- Question Prompt Box: Romaji and Listen Button -->
            <div style="background:#EFF6FF; border:1.5px solid #BFDBFE; border-radius:14px; padding:16px 20px; display:flex; align-items:center; justify-content:space-between; margin-bottom:16px;">
              <div>
                <div style="font-size:0.78rem; font-weight:800; color:#1E40AF; margin-bottom:2px;">Pronunciation / Romaji:</div>
                <div style="font-size:2rem; font-weight:900; color:#1D4ED8; font-family:'Courier New', monospace; letter-spacing:1px;">
                  [ ${q.romaji} ]
                </div>
              </div>
              <button onclick="playGoogleTTS('${q.char}')" title="Listen to pronunciation" style="background:white; border:1.5px solid #93C5FD; color:#1D4ED8; padding:8px 16px; border-radius:10px; font-size:0.95rem; font-weight:800; cursor:pointer; display:inline-flex; align-items:center; gap:6px; box-shadow:0 2px 4px rgba(0,0,0,0.05);" onmouseover="this.style.background='#DBEAFE'" onmouseout="this.style.background='white'">
                🔊 Listen
              </button>
            </div>

            <!-- Show Answer Button -->
            <button class="mainichi-btn-answer" id="kana-quiz-btn-answer" onclick="KanaWritingQuiz.toggleAnswer()" style="margin: 0 auto 14px; display:block;">
              ${this.isAnswerRevealed ? 'Hide Answer ＾' : 'Show Answer'}
            </button>

            <!-- Drawing Canvas (220x220) -->
            <div style="display:flex; justify-content:center; margin-bottom:12px;">
              <div style="width:220px; height:220px; border:2px solid #94A3B8; border-radius:12px; background:white; position:relative; overflow:hidden; box-shadow:0 2px 8px rgba(0,0,0,0.04);">
                <!-- Guidelines -->
                <div style="position:absolute; inset:0; pointer-events:none;">
                  <div style="position:absolute; top:50%; left:0; right:0; height:1px; border-top:1px dashed #BAE6FD;"></div>
                  <div style="position:absolute; left:50%; top:0; bottom:0; width:1px; border-left:1px dashed #BAE6FD;"></div>
                </div>
                <!-- Interactive Drawing Canvas -->
                <canvas id="kana-quiz-canvas" style="position:absolute; inset:0; width:100%; height:100%; touch-action:none; cursor:crosshair; z-index:2;"></canvas>
              </div>
            </div>

            <!-- Canvas tools: Clear & Undo -->
            <div style="display:flex; align-items:center; justify-content:center; gap:10px; margin-bottom:16px;">
              <button class="mainichi-square-btn" title="Clear canvas" onclick="KanaWritingQuiz.clearCanvas()" style="width:40px; height:40px; font-size:1.1rem;">✕</button>
              <button class="mainichi-square-btn" title="Undo stroke" onclick="KanaWritingQuiz.undoCanvas()" style="width:40px; height:40px; font-size:1.1rem;">↺</button>
            </div>

            <!-- Answer Expansion Panel -->
            ${this.isAnswerRevealed ? `
              <div style="background:#F0FDF4; border:2px solid #86EFAC; border-radius:14px; padding:16px 20px; margin-bottom:18px; animation:fadeIn 0.2s ease;">
                <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px; margin-bottom:14px; border-bottom:1px solid #BBF7D0; padding-bottom:10px;">
                  <div style="display:flex; align-items:center; gap:12px;">
                    <span style="font-size:2.8rem; font-weight:900; color:#15803D; font-family:${isHira ? "'Klee One', cursive" : 'inherit'}; line-height:1;">${q.char}</span>
                    <span style="font-size:1.1rem; font-weight:700; color:#166534;">[ ${q.romaji} ]</span>
                    <button onclick="playGoogleTTS('${q.char}')" title="Listen" style="background:white; border:1px solid #86EFAC; border-radius:8px; font-size:0.95rem; cursor:pointer; padding:3px 10px; color:#15803D;">
                      🔊
                    </button>
                  </div>
                  <button onclick="KanaWritingQuiz.practiceTraceChar('${q.char}', '${q.romaji}')" style="background:white; border:1.5px solid #86EFAC; color:#15803D; padding:6px 12px; border-radius:8px; font-weight:800; font-size:0.8rem; cursor:pointer;">
                    ✍ Practice Tracing
                  </button>
                </div>

                <!-- Self-check buttons -->
                <div class="mainichi-self-check-bar" style="margin-top:0;">
                  <button class="btn-check-ok" onclick="KanaWritingQuiz.mark(true)">⭕ Correct</button>
                  <button class="btn-check-ng" onclick="KanaWritingQuiz.mark(false)">❌ Need Review</button>
                </div>
              </div>
            ` : ''}

            <!-- Navigation bar -->
            <div class="mainichi-nav-bar" style="margin-top:10px;">
              <button class="mainichi-nav-btn" onclick="KanaWritingQuiz.prev()" ${isFirst ? 'disabled' : ''}>
                ◀ Previous
              </button>
              <button class="mainichi-nav-btn" onclick="KanaWritingQuiz.next()">
                ${isLast ? 'View Results ▶' : 'Next Question ▶'}
              </button>
            </div>
          </div>
        </div>
      `;

      setTimeout(() => {
        this.initQuizCanvas();
      }, 30);
    },'''

    code = code[:m.start()] + new_render_func + code[m.end():]

    with open('app.html', 'w', encoding='utf-8') as f:
        f.write(code)

    with open('📱_日本語学習アプリ.html', 'w', encoding='utf-8') as f:
        f.write(code)

    print("Updated app.html and 📱_日本語学習アプリ.html successfully!")

if __name__ == '__main__':
    update_files()
