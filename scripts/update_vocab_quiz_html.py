# -*- coding: utf-8 -*-
import glob
import re

files = sorted(glob.glob('/Users/yamauchimiku/.gemini/antigravity/scratch/japanese-flashcards/jlpt_n*_vocab_quiz.html'))

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update isKanjiWriting to prevent ruby spoiler on word-formation / affixes
    old_is_kanji = "const isKanjiWriting = (q.category && (q.category.includes('表記') || q.category.includes('書き')))"
    new_is_kanji = "const isKanjiWriting = (q.category && (q.category.includes('表記') || q.category.includes('書き') || q.category.includes('語形成') || q.category.includes('接頭') || q.category.includes('接尾')))"
    if old_is_kanji in content:
        content = content.replace(old_is_kanji, new_is_kanji)
        print(f"Updated isKanjiWriting in {file_path}")

    # 2. Update btnRetryAll button text in HTML
    old_btn_html = re.compile(r'<button class="btn-retry-all" id="btnRetryAll">[\s\S]*?<span>もう一度解く</span>[\s\S]*?</button>')
    new_btn_html = '''<button class="btn-retry-all" id="btnRetryAll" title="問題を新しくシャッフルして別の問題に挑戦します">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"></path><path d="M3 3v5h5"></path></svg>
          <span>🔄 新しくシャッフルしてもう一度解く</span>
        </button>'''
    if old_btn_html.search(content):
        content = old_btn_html.sub(new_btn_html, content)
        print(f"Updated btnRetryAll HTML in {file_path}")

    # 3. Update btnRetryAll click event listener in JS
    old_listener = re.compile(
        r'btnRetryAll\.addEventListener\(\'click\',\s*\(\)\s*=>\s*\{'
        r'[\s\S]*?currentIndex\s*=\s*0;'
        r'[\s\S]*?correctCount\s*=\s*0;'
        r'[\s\S]*?answeredCount\s*=\s*0;'
        r'[\s\S]*?userAnswersMap\s*=\s*\{\};'
        r'[\s\S]*?hideResultView\(\);'
        r'[\s\S]*?renderQuestion\(\);'
        r'[\s\S]*?showToast\([^\)]*\);'
        r'\s*\}\);'
    )

    new_listener = '''btnRetryAll.addEventListener('click', () => {
    // 10問、30問、50問（または全問）で、毎回語彙を新たにシャッフル・厳選して再生成！
    activeIndices = buildBalancedIndices(selectedLimit, categoryFilter ? categoryFilter.value : 'all');
    currentIndex = 0;
    correctCount = 0;
    answeredCount = 0;
    userAnswersMap = {};
    hideResultView();
    renderQuestion();
    showToast(selectedLimit > 0 ? `新しい問題セット（${selectedLimit}問）をシャッフル生成しました！` : '全問題を新しくシャッフルして最初から解き直します！');
  });'''

    if old_listener.search(content):
        content = old_listener.sub(new_listener, content)
        print(f"Updated btnRetryAll JS listener in {file_path}")
    else:
        print(f"WARNING: listener regex didn't match in {file_path}")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

