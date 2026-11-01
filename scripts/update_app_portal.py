# -*- coding: utf-8 -*-
"""
Updates app.html and 📱_日本語学習アプリ.html modal-jlpt section to feature ALL 5 JLPT levels.
"""

import shutil

repo_dir = '/Users/yamauchimiku/Documents/GitHub/japanese-learning'
app_file = f'{repo_dir}/app.html'

with open(app_file, 'r', encoding='utf-8') as f:
    html = f.read()

old_modal = '''<div class="app-modal-overlay" id="modal-jlpt" onclick="closeModalOnBg(event, 'jlpt')">
  <div class="app-modal-box">
    <div class="app-modal-header">
      <div class="app-modal-title">JLPT対策（単語・実戦演習・模試）</div>
      <button class="app-modal-close" onclick="closeModal('jlpt')">✕</button>
    </div>
    <div class="app-modal-body">
      <div style="font-size:0.88rem; color:var(--text-sub);">
        N5〜N1の完全対策。8,910語の五十音順単語リストと、4言語多言語解説つきの実戦問題道場を用意しています。
      </div>
      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap:16px; margin-top:10px;">
        <a href="jlpt_practice.html" style="text-decoration:none; background:#F8FBFE; border:1.5px solid var(--kobe-blue-border); border-radius:16px; padding:20px; display:flex; flex-direction:column; gap:8px; transition:transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
          <div style="font-size:1.8rem;">🎯</div>
          <div style="font-weight:800; font-size:1.1rem; color:var(--kobe-blue);">JLPT実戦演習 道場（N2・N3 文法演習）</div>
          <div style="font-size:0.82rem; color:var(--text-sub);">N2（1,507問）・N3（182問）文法穴埋め4択演習道場、文字・語彙、ふりがな切替、続きから再開に対応。</div>
          <div style="margin-top:auto; font-weight:700; font-size:0.85rem; color:var(--kobe-blue);">演習を開始する →</div>
        </a>

        <a href="jlpt_vocab.html" style="text-decoration:none; background:#FAF8FD; border:1.5px solid var(--lavender-purple-border); border-radius:16px; padding:20px; display:flex; flex-direction:column; gap:8px; transition:transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
          <div style="font-size:1.8rem;">📖</div>
          <div style="font-weight:800; font-size:1.1rem; color:var(--lavender-purple);">JLPT単語帳（8,910語）</div>
          <div style="font-size:0.82rem; color:var(--text-sub);">N5〜N1の全出題語彙を五十音順（あいうえお順）に完全収録。例文・保存機能つき。</div>
          <div style="margin-top:auto; font-weight:700; font-size:0.85rem; color:var(--lavender-purple);">単語帳を開く →</div>
        </a>
      </div>
    </div>
  </div>
</div>'''

new_modal = '''<div class="app-modal-overlay" id="modal-jlpt" onclick="closeModalOnBg(event, 'jlpt')">
  <div class="app-modal-box" style="max-width:860px;">
    <div class="app-modal-header">
      <div class="app-modal-title">🏆 JLPT完全制覇（N1〜N5 文法教科書・演習・単語）</div>
      <button class="app-modal-close" onclick="closeModal('jlpt')">✕</button>
    </div>
    <div class="app-modal-body">
      <div style="font-size:0.88rem; color:var(--text-sub); margin-bottom:12px;">
        全レベル（N1・N2・N3・N4・N5）の「文法マスター教科書（9大セクション）」「4択文法穴埋め演習道場（全3,175問）」「単語フラッシュカード（全8,907語）」「語彙演習道場」を完全網羅しています。
      </div>

      <!-- メイン総合道場ボタン -->
      <a href="jlpt_practice.html" style="text-decoration:none; background:linear-gradient(135deg, #1995AD, #127285); color:white; border-radius:16px; padding:18px 24px; display:flex; align-items:center; justify-content:space-between; box-shadow:0 6px 20px rgba(25,149,173,0.25); margin-bottom:16px; transition:transform 0.2s;" onmouseover="this.style.transform='scale(1.01)'" onmouseout="this.style.transform='none'">
        <div>
          <div style="font-size:1.15rem; font-weight:800; display:flex; align-items:center; gap:8px;">
            <span>🎯</span> JLPT総合演習センター（レベル切替・進捗管理）
          </div>
          <div style="font-size:0.82rem; opacity:0.92; margin-top:4px;">
            N1〜N5の全レベルの教科書・カード・演習道場をワンストップで切り替え可能
          </div>
        </div>
        <div style="font-size:1.3rem; font-weight:800;">→</div>
      </a>

      <!-- 5レベル グリッドカード -->
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(150px, 1fr)); gap:10px; margin-bottom:14px;">
        <!-- N1 -->
        <a href="jlpt_n1_grammar_textbook.html" style="text-decoration:none; background:#FAF5FF; border:1.5px solid #E9D5FF; border-radius:12px; padding:12px; display:flex; flex-direction:column; gap:4px; text-align:center;">
          <span style="font-size:1.2rem;">👑</span>
          <strong style="color:#7E22CE; font-size:0.95rem;">N1 最上級</strong>
          <span style="font-size:0.75rem; color:#6B7280;">文法127 / 語彙3,747</span>
        </a>
        <!-- N2 -->
        <a href="jlpt_n2_grammar_textbook.html" style="text-decoration:none; background:#FFF1F2; border:1.5px solid #FECDD3; border-radius:12px; padding:12px; display:flex; flex-direction:column; gap:4px; text-align:center;">
          <span style="font-size:1.2rem;">🌸</span>
          <strong style="color:#BE123C; font-size:0.95rem;">N2 実戦中上級</strong>
          <span style="font-size:0.75rem; color:#6B7280;">文法195 / 語彙3,412</span>
        </a>
        <!-- N3 -->
        <a href="jlpt_n3_grammar_textbook.html" style="text-decoration:none; background:#F0FDFA; border:1.5px solid #99F6E4; border-radius:12px; padding:12px; display:flex; flex-direction:column; gap:4px; text-align:center;">
          <span style="font-size:1.2rem;">💎</span>
          <strong style="color:#0F766E; font-size:0.95rem;">N3 中級完成</strong>
          <span style="font-size:0.75rem; color:#6B7280;">文法182 / 語彙1,841</span>
        </a>
        <!-- N4 -->
        <a href="jlpt_n4_grammar_textbook.html" style="text-decoration:none; background:#F0F9FF; border:1.5px solid #BAE6FD; border-radius:12px; padding:12px; display:flex; flex-direction:column; gap:4px; text-align:center;">
          <span style="font-size:1.2rem;">🌱</span>
          <strong style="color:#0369A1; font-size:0.95rem;">N4 初級基礎</strong>
          <span style="font-size:0.75rem; color:#6B7280;">文法62 / 語彙668</span>
        </a>
        <!-- N5 -->
        <a href="jlpt_n5_grammar_textbook.html" style="text-decoration:none; background:#F0FDF4; border:1.5px solid #BBF7D0; border-radius:12px; padding:12px; display:flex; flex-direction:column; gap:4px; text-align:center;">
          <span style="font-size:1.2rem;">🐣</span>
          <strong style="color:#15803D; font-size:0.95rem;">N5 入門</strong>
          <span style="font-size:0.75rem; color:#6B7280;">文法46 / 語彙702</span>
        </a>
      </div>

      <div style="display:flex; justify-content:flex-end;">
        <a href="jlpt_vocab.html" style="text-decoration:none; color:var(--text-sub); font-size:0.82rem; font-weight:600;">📖 全8,907語 五十音順単語帳を開く →</a>
      </div>
    </div>
  </div>
</div>'''

if old_modal in html:
    html = html.replace(old_modal, new_modal)
    with open(app_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated app.html successfully!")
    
    # Sync to 📱_日本語学習アプリ.html
    shutil.copy2(app_file, f'{repo_dir}/📱_日本語学習アプリ.html')
    print("Synced to 📱_日本語学習アプリ.html successfully!")
else:
    print("Could not find old_modal exact match, checking line numbers...")
