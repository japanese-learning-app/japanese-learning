# -*- coding: utf-8 -*-
"""
Update KanaWritingQuiz so clicking 'Show Answer' automatically plays the stroke order animation.
"""

import re

def update():
    with open('app.html', 'r', encoding='utf-8') as f:
        code = f.read()

    # 1. Update toggleAnswer and add playAnswerStrokeAnimation & replayAnswerAnimation
    old_toggle = '''    toggleAnswer() {
      this.isAnswerRevealed = !this.isAnswerRevealed;
      this.render();
    },'''

    new_toggle = '''    async toggleAnswer() {
      this.isAnswerRevealed = !this.isAnswerRevealed;
      this.render();
      if (this.isAnswerRevealed) {
        await this.playAnswerStrokeAnimation();
      }
    },

    async playAnswerStrokeAnimation(targetChar = null) {
      const q = this.questions[this.currentIndex];
      if (!q) return;

      const fullChar = q.char;
      let charToAnimate = targetChar;

      const multiSel = document.getElementById('kana-quiz-multichar-selector');
      if (fullChar.length > 1) {
        if (!charToAnimate) charToAnimate = fullChar[0];
        if (multiSel) {
          multiSel.style.display = 'flex';
          multiSel.innerHTML = [...fullChar].map((sub, idx) => `
            <button class="quiz-level-pill ${sub === charToAnimate ? 'active' : ''}" onclick="KanaWritingQuiz.playAnswerStrokeAnimation('${sub}')" style="padding:3px 10px; font-size:0.75rem;">
              ${idx + 1}: ${sub}
            </button>
          `).join('');
        }
      } else {
        if (!charToAnimate) charToAnimate = fullChar;
        if (multiSel) multiSel.style.display = 'none';
      }

      this.currentAnswerAnimatingChar = charToAnimate;

      if (typeof KanjiEngine === 'undefined') return;
      const data = await KanjiEngine.fetchStrokes(charToAnimate);
      if (!data) return;

      KanjiEngine.renderStage(data, 'kana-quiz-answer-stage');
    },

    replayAnswerAnimation() {
      if (this.currentAnswerAnimatingChar) {
        this.playAnswerStrokeAnimation(this.currentAnswerAnimatingChar);
      }
    },'''

    assert old_toggle in code, "old_toggle not found in app.html"
    code = code.replace(old_toggle, new_toggle)

    # 2. Update Answer Expansion Panel in render()
    old_panel_pattern = r'<!-- Answer Expansion Panel -->[\s\S]*?<!-- Navigation bar -->'
    
    new_panel = '''<!-- Answer Expansion Panel with Automatic Stroke Order Animation -->
            ${this.isAnswerRevealed ? `
              <div style="background:#F0FDF4; border:2px solid #86EFAC; border-radius:16px; padding:18px 20px; margin-bottom:18px; animation:fadeIn 0.2s ease;">
                <!-- Header with Character, Audio & Controls -->
                <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px; margin-bottom:12px; border-bottom:1px solid #BBF7D0; padding-bottom:10px;">
                  <div style="display:flex; align-items:center; gap:10px;">
                    <span style="font-size:1.8rem; font-weight:900; color:#15803D; font-family:${isHira ? "'Klee One', cursive" : 'inherit'}; line-height:1;">${q.char}</span>
                    <span style="font-size:1.05rem; font-weight:700; color:#166534;">[ ${q.romaji} ]</span>
                    <button onclick="playGoogleTTS('${q.char}')" title="Listen" style="background:white; border:1px solid #86EFAC; border-radius:8px; font-size:0.95rem; cursor:pointer; padding:3px 10px; color:#15803D;">
                      🔊
                    </button>
                  </div>
                  <div style="display:flex; align-items:center; gap:8px;">
                    <button onclick="KanaWritingQuiz.replayAnswerAnimation()" style="background:white; border:1.5px solid #86EFAC; color:#15803D; padding:5px 12px; border-radius:8px; font-weight:800; font-size:0.82rem; cursor:pointer; display:inline-flex; align-items:center; gap:4px;" title="Replay stroke order animation">
                      ▶ Replay
                    </button>
                    <button onclick="KanaWritingQuiz.practiceTraceChar('${q.char}', '${q.romaji}')" style="background:white; border:1.5px solid #86EFAC; color:#15803D; padding:5px 12px; border-radius:8px; font-weight:800; font-size:0.82rem; cursor:pointer;" title="Practice tracing">
                      ✍ Practice Tracing
                    </button>
                  </div>
                </div>

                <!-- Multi-character selector for combos -->
                <div id="kana-quiz-multichar-selector" style="display:none; gap:6px; margin-bottom:10px; justify-content:center;"></div>

                <!-- Animated Stroke Order Tianzige Stage (Auto Plays on Click) -->
                <div style="display:flex; flex-direction:column; align-items:center; gap:8px; margin: 12px 0 16px;">
                  <div style="font-size:0.85rem; font-weight:800; color:#15803D; display:flex; align-items:center; gap:6px;">
                    <span>🖌️</span> <span>Stroke Order Animation (書き順)</span>
                  </div>
                  <div class="kanji-stage-box" id="kana-quiz-answer-stage" style="width:200px; height:200px; border:2px solid #86EFAC; border-radius:12px; background:white; position:relative; overflow:hidden; box-shadow:0 3px 10px rgba(0,0,0,0.06);">
                    <!-- Guidelines -->
                    <div style="position:absolute; inset:0; pointer-events:none;">
                      <div style="position:absolute; top:50%; left:0; right:0; height:1px; border-top:1px dashed #BAE6FD;"></div>
                      <div style="position:absolute; left:50%; top:0; bottom:0; width:1px; border-left:1px dashed #BAE6FD;"></div>
                    </div>
                  </div>
                </div>

                <!-- Self-check buttons -->
                <div class="mainichi-self-check-bar" style="margin-top:0;">
                  <button class="btn-check-ok" onclick="KanaWritingQuiz.mark(true)">⭕ Correct</button>
                  <button class="btn-check-ng" onclick="KanaWritingQuiz.mark(false)">❌ Need Review</button>
                </div>
              </div>
            ` : ''}

            <!-- Navigation bar -->'''

    m = re.search(old_panel_pattern, code)
    assert m, "old_panel_pattern not matched in app.html"
    code = code[:m.start()] + new_panel + code[m.end():]

    with open('app.html', 'w', encoding='utf-8') as f:
        f.write(code)

    with open('📱_日本語学習アプリ.html', 'w', encoding='utf-8') as f:
        f.write(code)

    print("Updated stroke order auto-animation in KanaWritingQuiz successfully!")

if __name__ == '__main__':
    update()
