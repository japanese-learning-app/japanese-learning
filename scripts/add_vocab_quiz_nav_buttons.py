#!/usr/bin/env python3
import os
import re

QUIZ_PATH = '/Users/yamauchimiku/Documents/GitHub/japanese-learning/jlpt_n2_vocab_quiz.html'

with open(QUIZ_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. State variable userAnswersMap at top
old_state = """  let hasAnsweredCurrent = false;

  // LocalStorage Keys"""
new_state = """  let hasAnsweredCurrent = false;
  let userAnswersMap = {};

  // LocalStorage Keys"""
assert old_state in content, "old_state not found"
content = content.replace(old_state, new_state, 1)

# Remove the later duplicate declaration of let userAnswersMap = {};
old_dup_decl = """  // Result & Review Logic
  let userAnswersMap = {};
  let userReviewFilter = 'all';"""
new_dup_decl = """  // Result & Review Logic
  let userReviewFilter = 'all';"""
assert old_dup_decl in content, "old_dup_decl not found"
content = content.replace(old_dup_decl, new_dup_decl, 1)

# 2. Extract renderExplanationContent and update renderQuestion + handleChoice
old_render_and_handle = """  // Render Question
  function renderQuestion() {
    if (activeIndices.length === 0) {
      questionSentence.innerHTML = '該当する問題が見つかりませんでした。条件を変更してください。';
      choicesGrid.innerHTML = '';
      explanationCard.style.display = 'none';
      btnNext.style.display = 'none';
      return;
    }

    hasAnsweredCurrent = false;
    explanationCard.style.display = 'none';
    btnNext.style.display = 'none';

    const q = data[activeIndices[currentIndex]];
    cardCategoryName.textContent = q.category;
    questionSentence.classList.remove('revealed');

    // Update Instruction Banner
    const inst = getQuestionInstruction(q);
    quizInstIcon.textContent = inst.icon;
    quizInstText.textContent = inst.text;

    // Render formatted question with distinct target chips & blank box
    questionSentence.innerHTML = formatQuestionSentence(q, false, false);

    // Save resume index when user is progressing
    if (currentIndex > 0) {
      localStorage.setItem(STORAGE_RESUME_KEY, currentIndex.toString());
    }
    checkResume();

    // Progress
    progressText.textContent = `問題 ${currentIndex + 1} / ${activeIndices.length}`;
    const pct = Math.round(((currentIndex) / activeIndices.length) * 100);
    progressBar.style.width = `${pct}%`;
    const scorePct = answeredCount > 0 ? Math.round((correctCount / answeredCount) * 100) : 0;
    scoreText.textContent = `正解率: ${scorePct}% (${correctCount} / ${answeredCount})`;

    // Render Choices
    choicesGrid.innerHTML = '';

    // 漢字表記問題（ひらがなから正しい漢字を選ぶ問題）は、選択肢にふりがなを振るとネタバレになるため、プレーンな漢字（q.choices）を使用する
    const isKanjiWriting = (q.category && (q.category.includes('表記') || q.category.includes('書き'))) ||
      (!q.category.includes('読み') && /^[ぁ-んー\s]+$/.test(q.target_word || ''));
    const choices = (!isKanjiWriting && q.choices_ruby && q.choices_ruby.length === 4) ? q.choices_ruby : q.choices;

    // 長い選択肢（用法問題、文が含まれる、または10文字以上）の場合は1列4行にする
    const isLongChoice = choices.some(c => {
      const plain = (c || '').replace(/<[^>]+>/g, '').trim();
      return plain.includes('。') || plain.length >= 10;
    }) || (q.category && (q.category.includes('用法') || q.category.includes('適切な文')));

    choicesGrid.classList.toggle('single-column', isLongChoice);

    choices.forEach((cText, idx) => {
      const btn = document.createElement('button');
      btn.className = 'choice-btn';
      btn.dataset.index = idx;
      btn.innerHTML = `<span class="choice-num">${idx + 1}</span><span class="choice-text">${cText}</span>`;
      btn.addEventListener('click', () => handleChoice(idx));
      choicesGrid.appendChild(btn);
    });

    updateMyListUI();
  }

  // Handle Choice Selection
  function handleChoice(selectedIndex) {
    if (hasAnsweredCurrent) return;
    hasAnsweredCurrent = true;
    answeredCount++;

    const q = data[activeIndices[currentIndex]];
    const buttons = choicesGrid.querySelectorAll('.choice-btn');
    const isCorrect = (selectedIndex === q.answer);

    // Reveal target word reading / blank in question sentence
    questionSentence.classList.add('revealed');
    questionSentence.innerHTML = formatQuestionSentence(q, true, isCorrect);

    if (isCorrect) {
      correctCount++;
      buttons[selectedIndex].classList.add('correct');
      resultTag.className = 'result-tag correct';
      resultTag.innerHTML = `✓ 正解！ (${escapeHtml(q.correct_text)})`;
    } else {
      buttons[selectedIndex].classList.add('wrong');
      if (q.answer >= 0 && q.answer < buttons.length) {
        buttons[q.answer].classList.add('correct');
      }
      resultTag.className = 'result-tag wrong';
      resultTag.innerHTML = `✕ 不正解（正解: ${q.answer + 1}. ${escapeHtml(q.correct_text)}）`;
    }

    userAnswersMap[currentIndex] = {
      dataIndex: activeIndices[currentIndex],
      selectedIndex: selectedIndex,
      isCorrect: isCorrect
    };

    buttons.forEach(b => b.disabled = true);

    // 📖 Update Question & Answer Reading Pairs (User Request 2)
    const targetWord = q.target_word || q.correct_text;
    const targetReading = q.target_word_reading || '';
    const answerWord = q.correct_text;
    const answerReading = q.correct_text_reading || '';

    if (readQuestionWord) readQuestionWord.textContent = targetWord;
    if (readQuestionKana) {
      readQuestionKana.textContent = (targetReading && targetReading !== targetWord) ? `（${targetReading}）` : '';
    }
    if (btnSpeakReadQuestion) {
      btnSpeakReadQuestion.onclick = () => speakJapaneseText(targetWord);
    }

    if (readAnswerWord) readAnswerWord.textContent = answerWord;
    if (readAnswerKana) {
      readAnswerKana.textContent = (answerReading && answerReading !== answerWord) ? `（${answerReading}）` : '';
    }
    if (btnSpeakReadAnswer) {
      btnSpeakReadAnswer.onclick = () => speakJapaneseText(answerWord);
    }
    if (readingPairsCard) readingPairsCard.style.display = 'flex';

    // Show Meaning (if available)
    if (q.meaning_en) {
      explanationText.style.display = 'block';
      explanationText.innerHTML = `<strong>【意味】</strong> ${escapeHtml(q.meaning_en)}`;
    } else {
      explanationText.style.display = 'none';
      explanationText.innerHTML = '';
    }

    // 💡 Nuance & English Direct Translation Differences (User Request 3)
    if (nuanceExplanationCard) {
      if (q.nuance_diff || q.english_pitfall) {
        if (nuanceDiffText) nuanceDiffText.innerHTML = escapeHtml(q.nuance_diff || '').replace(/\\n/g, '<br>');
        if (nuanceEngText) nuanceEngText.innerHTML = escapeHtml(q.english_pitfall || '').replace(/\\n/g, '<br>');
        nuanceExplanationCard.style.display = 'block';
      } else {
        nuanceExplanationCard.style.display = 'none';
      }
    }

    // Kanji Breakdown Cards (漢字, 音読み, 訓読み, 意味)
    if (q.kanji_info && Array.isArray(q.kanji_info) && q.kanji_info.length > 0) {
      kanjiCardsGrid.innerHTML = q.kanji_info.map(ki => `
        <div class="kanji-detail-card">
          <div class="kanji-char-box">
            <span>${escapeHtml(ki.kanji)}</span>
            <span class="kanji-char-sub">漢字</span>
          </div>
          <div class="kanji-readings-box">
            <div class="kanji-reading-row">
              <span class="kanji-reading-lbl">音</span>
              <span class="kanji-reading-val">${escapeHtml(ki.onyomi || '-')}</span>
            </div>
            <div class="kanji-reading-row">
              <span class="kanji-reading-lbl kun">訓</span>
              <span class="kanji-reading-val">${escapeHtml(ki.kunyomi || '-')}</span>
            </div>
            ${ki.meaning ? `
            <div class="kanji-reading-row">
              <span class="kanji-reading-lbl mean">意</span>
              <span class="kanji-reading-val meaning">${escapeHtml(ki.meaning)}</span>
            </div>` : ''}
          </div>
        </div>
      `).join('');
      kanjiBreakdownSection.style.display = 'block';
      similarBoxTitle.innerHTML = '<span>💡 この漢字を使った単語・関連語（タップで辞書検索＆保存）</span>';
    } else {
      kanjiBreakdownSection.style.display = 'none';
      kanjiCardsGrid.innerHTML = '';
      similarBoxTitle.innerHTML = '<span>💡 関連する表現・重要語彙（タップで辞書検索＆保存）</span>';
    }
    
    // Generate Similar / Collocation Pills
    similarItems.innerHTML = '';
    const simList = (q.similar && Array.isArray(q.similar) && q.similar.length > 0)
      ? q.similar
      : [{ term: q.target_word || q.correct_text, reading: '', meaning: '' }];

    simList.forEach(item => {
      const pill = document.createElement('span');
      pill.className = 'similar-pill';
      const rPart = (item.reading && item.reading !== item.term)
        ? `<span class="pill-reading">（${escapeHtml(item.reading)}）</span>`
        : '';
      pill.innerHTML = `🔍 ${escapeHtml(item.term)}${rPart}`;
      pill.title = '内蔵辞書で検索＆マイリストに保存';
      pill.addEventListener('click', () => {
        openTagActionModal(item);
      });
      similarItems.appendChild(pill);
    });

    explanationCard.style.display = 'block';
    btnNext.style.display = 'block';

    // Update Live Score
    const scorePct = Math.round((correctCount / answeredCount) * 100);
    scoreText.textContent = `正解率: ${scorePct}% (${correctCount} / ${answeredCount})`;
  }"""

new_render_and_handle = """  // Render Question
  function renderQuestion() {
    if (activeIndices.length === 0) {
      questionSentence.innerHTML = '該当する問題が見つかりませんでした。条件を変更してください。';
      choicesGrid.innerHTML = '';
      explanationCard.style.display = 'none';
      btnNext.style.display = 'none';
      if (prevBtn) prevBtn.disabled = true;
      if (nextBtn) nextBtn.disabled = true;
      return;
    }

    const q = data[activeIndices[currentIndex]];
    cardCategoryName.textContent = q.category;
    questionSentence.classList.remove('revealed');

    // Update Instruction Banner
    const inst = getQuestionInstruction(q);
    quizInstIcon.textContent = inst.icon;
    quizInstText.textContent = inst.text;

    // Render formatted question with distinct target chips & blank box
    questionSentence.innerHTML = formatQuestionSentence(q, false, false);

    // Save resume index when user is progressing
    if (currentIndex > 0) {
      localStorage.setItem(STORAGE_RESUME_KEY, currentIndex.toString());
    }
    checkResume();

    // Progress
    progressText.textContent = `問題 ${currentIndex + 1} / ${activeIndices.length}`;
    const pct = Math.round(((currentIndex) / activeIndices.length) * 100);
    progressBar.style.width = `${pct}%`;
    const scorePct = answeredCount > 0 ? Math.round((correctCount / answeredCount) * 100) : 0;
    scoreText.textContent = `正解率: ${scorePct}% (${correctCount} / ${answeredCount})`;

    // Render Choices
    choicesGrid.innerHTML = '';

    // 漢字表記問題（ひらがなから正しい漢字を選ぶ問題）は、選択肢にふりがなを振るとネタバレになるため、プレーンな漢字（q.choices）を使用する
    const isKanjiWriting = (q.category && (q.category.includes('表記') || q.category.includes('書き'))) ||
      (!q.category.includes('読み') && /^[ぁ-んー\\s]+$/.test(q.target_word || ''));
    const choices = (!isKanjiWriting && q.choices_ruby && q.choices_ruby.length === 4) ? q.choices_ruby : q.choices;

    // 長い選択肢（用法問題、文が含まれる、または10文字以上）の場合は1列4行にする
    const isLongChoice = choices.some(c => {
      const plain = (c || '').replace(/<[^>]+>/g, '').trim();
      return plain.includes('。') || plain.length >= 10;
    }) || (q.category && (q.category.includes('用法') || q.category.includes('適切な文')));

    choicesGrid.classList.toggle('single-column', isLongChoice);

    choices.forEach((cText, idx) => {
      const btn = document.createElement('button');
      btn.className = 'choice-btn';
      btn.dataset.index = idx;
      btn.innerHTML = `<span class="choice-num">${idx + 1}</span><span class="choice-text">${cText}</span>`;
      btn.addEventListener('click', () => handleChoice(idx));
      choicesGrid.appendChild(btn);
    });

    // Check if previously answered
    const previousAns = userAnswersMap[currentIndex];
    if (previousAns) {
      hasAnsweredCurrent = true;
      questionSentence.classList.add('revealed');
      questionSentence.innerHTML = formatQuestionSentence(q, true, previousAns.isCorrect);

      const buttons = choicesGrid.querySelectorAll('.choice-btn');
      buttons.forEach((b, idx) => {
        b.disabled = true;
        if (idx === q.answer) {
          b.classList.add('correct');
        } else if (idx === previousAns.selectedIndex && !previousAns.isCorrect) {
          b.classList.add('wrong');
        }
      });

      renderExplanationContent(q, previousAns.isCorrect);
      explanationCard.style.display = 'block';
      btnNext.style.display = 'block';
    } else {
      hasAnsweredCurrent = false;
      explanationCard.style.display = 'none';
      btnNext.style.display = 'none';
    }

    // Navigation Buttons State (Always Visible: ← 前に戻る / 次へ行く →)
    if (prevBtn) prevBtn.disabled = (currentIndex === 0);
    if (nextBtn) {
      nextBtn.textContent = (currentIndex === activeIndices.length - 1) ? '結果を見る 🏆' : '次へ行く →';
      nextBtn.disabled = false;
    }
    if (btnNext) {
      btnNext.textContent = (currentIndex === activeIndices.length - 1) ? '演習結果を見る [Enter] 🏆' : '次の問題へ進む [Enter] →';
    }
    if (quizNavBar) quizNavBar.style.display = 'flex';

    updateMyListUI();
  }

  // Render Explanation Card & Reading Details
  function renderExplanationContent(q, isCorrect) {
    if (isCorrect) {
      resultTag.className = 'result-tag correct';
      resultTag.innerHTML = `✓ 正解！ (${escapeHtml(q.correct_text)})`;
    } else {
      resultTag.className = 'result-tag wrong';
      resultTag.innerHTML = `✕ 不正解（正解: ${q.answer + 1}. ${escapeHtml(q.correct_text)}）`;
    }

    // 📖 Update Question & Answer Reading Pairs (User Request 2)
    const targetWord = q.target_word || q.correct_text;
    const targetReading = q.target_word_reading || '';
    const answerWord = q.correct_text;
    const answerReading = q.correct_text_reading || '';

    if (readQuestionWord) readQuestionWord.textContent = targetWord;
    if (readQuestionKana) {
      readQuestionKana.textContent = (targetReading && targetReading !== targetWord) ? `（${targetReading}）` : '';
    }
    if (btnSpeakReadQuestion) {
      btnSpeakReadQuestion.onclick = () => speakJapaneseText(targetWord);
    }

    if (readAnswerWord) readAnswerWord.textContent = answerWord;
    if (readAnswerKana) {
      readAnswerKana.textContent = (answerReading && answerReading !== answerWord) ? `（${answerReading}）` : '';
    }
    if (btnSpeakReadAnswer) {
      btnSpeakReadAnswer.onclick = () => speakJapaneseText(answerWord);
    }
    if (readingPairsCard) readingPairsCard.style.display = 'flex';

    // Show Meaning (if available)
    if (q.meaning_en) {
      explanationText.style.display = 'block';
      explanationText.innerHTML = `<strong>【意味】</strong> ${escapeHtml(q.meaning_en)}`;
    } else {
      explanationText.style.display = 'none';
      explanationText.innerHTML = '';
    }

    // 💡 Nuance & English Direct Translation Differences (User Request 3)
    if (nuanceExplanationCard) {
      if (q.nuance_diff || q.english_pitfall) {
        if (nuanceDiffText) nuanceDiffText.innerHTML = escapeHtml(q.nuance_diff || '').replace(/\\n/g, '<br>');
        if (nuanceEngText) nuanceEngText.innerHTML = escapeHtml(q.english_pitfall || '').replace(/\\n/g, '<br>');
        nuanceExplanationCard.style.display = 'block';
      } else {
        nuanceExplanationCard.style.display = 'none';
      }
    }

    // Kanji Breakdown Cards (漢字, 音読み, 訓読み, 意味)
    if (q.kanji_info && Array.isArray(q.kanji_info) && q.kanji_info.length > 0) {
      kanjiCardsGrid.innerHTML = q.kanji_info.map(ki => `
        <div class="kanji-detail-card">
          <div class="kanji-char-box">
            <span>${escapeHtml(ki.kanji)}</span>
            <span class="kanji-char-sub">漢字</span>
          </div>
          <div class="kanji-readings-box">
            <div class="kanji-reading-row">
              <span class="kanji-reading-lbl">音</span>
              <span class="kanji-reading-val">${escapeHtml(ki.onyomi || '-')}</span>
            </div>
            <div class="kanji-reading-row">
              <span class="kanji-reading-lbl kun">訓</span>
              <span class="kanji-reading-val">${escapeHtml(ki.kunyomi || '-')}</span>
            </div>
            ${ki.meaning ? `
            <div class="kanji-reading-row">
              <span class="kanji-reading-lbl mean">意</span>
              <span class="kanji-reading-val meaning">${escapeHtml(ki.meaning)}</span>
            </div>` : ''}
          </div>
        </div>
      `).join('');
      kanjiBreakdownSection.style.display = 'block';
      similarBoxTitle.innerHTML = '<span>💡 この漢字を使った単語・関連語（タップで辞書検索＆保存）</span>';
    } else {
      kanjiBreakdownSection.style.display = 'none';
      kanjiCardsGrid.innerHTML = '';
      similarBoxTitle.innerHTML = '<span>💡 関連する表現・重要語彙（タップで辞書検索＆保存）</span>';
    }
    
    // Generate Similar / Collocation Pills
    similarItems.innerHTML = '';
    const simList = (q.similar && Array.isArray(q.similar) && q.similar.length > 0)
      ? q.similar
      : [{ term: q.target_word || q.correct_text, reading: '', meaning: '' }];

    simList.forEach(item => {
      const pill = document.createElement('span');
      pill.className = 'similar-pill';
      const rPart = (item.reading && item.reading !== item.term)
        ? `<span class="pill-reading">（${escapeHtml(item.reading)}）</span>`
        : '';
      pill.innerHTML = `🔍 ${escapeHtml(item.term)}${rPart}`;
      pill.title = '内蔵辞書で検索＆マイリストに保存';
      pill.addEventListener('click', () => {
        openTagActionModal(item);
      });
      similarItems.appendChild(pill);
    });
  }

  // Handle Choice Selection
  function handleChoice(selectedIndex) {
    if (hasAnsweredCurrent) return;
    hasAnsweredCurrent = true;
    answeredCount++;

    const q = data[activeIndices[currentIndex]];
    const buttons = choicesGrid.querySelectorAll('.choice-btn');
    const isCorrect = (selectedIndex === q.answer);

    // Reveal target word reading / blank in question sentence
    questionSentence.classList.add('revealed');
    questionSentence.innerHTML = formatQuestionSentence(q, true, isCorrect);

    if (isCorrect) {
      correctCount++;
      buttons[selectedIndex].classList.add('correct');
    } else {
      buttons[selectedIndex].classList.add('wrong');
      if (q.answer >= 0 && q.answer < buttons.length) {
        buttons[q.answer].classList.add('correct');
      }
    }

    userAnswersMap[currentIndex] = {
      dataIndex: activeIndices[currentIndex],
      selectedIndex: selectedIndex,
      isCorrect: isCorrect
    };

    buttons.forEach(b => b.disabled = true);

    renderExplanationContent(q, isCorrect);
    explanationCard.style.display = 'block';
    btnNext.style.display = 'block';

    if (nextBtn) {
      nextBtn.textContent = (currentIndex === activeIndices.length - 1) ? '結果を見る 🏆' : '次へ行く →';
    }
    if (btnNext) {
      btnNext.textContent = (currentIndex === activeIndices.length - 1) ? '演習結果を見る [Enter] 🏆' : '次の問題へ進む [Enter] →';
    }

    // Update Live Score
    const scorePct = Math.round((correctCount / answeredCount) * 100);
    scoreText.textContent = `正解率: ${scorePct}% (${correctCount} / ${answeredCount})`;
  }"""

assert old_render_and_handle in content, "old_render_and_handle not matched"
content = content.replace(old_render_and_handle, new_render_and_handle, 1)

# 3. Add event listeners for prevBtn and nextBtn
old_next_listener = """  // Next Button
  btnNext.addEventListener('click', () => {
    if (currentIndex < activeIndices.length - 1) {
      currentIndex++;
      renderQuestion();
      window.scrollTo({ top: 120, behavior: 'smooth' });
    } else {
      showResultView();
    }
  });"""

new_next_listener = """  // Navigation Buttons (Next & Prev)
  btnNext.addEventListener('click', () => {
    if (currentIndex < activeIndices.length - 1) {
      currentIndex++;
      renderQuestion();
      window.scrollTo({ top: 120, behavior: 'smooth' });
    } else {
      showResultView();
    }
  });

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      if (currentIndex < activeIndices.length - 1) {
        currentIndex++;
        renderQuestion();
        window.scrollTo({ top: 120, behavior: 'smooth' });
      } else {
        showResultView();
      }
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      if (currentIndex > 0) {
        currentIndex--;
        renderQuestion();
        window.scrollTo({ top: 120, behavior: 'smooth' });
      }
    });
  }"""
assert old_next_listener in content, "old_next_listener not matched"
content = content.replace(old_next_listener, new_next_listener, 1)

# 4. Hide/Show quizNavBar in showResultView and hideResultView
old_result_view = """  function showResultView() {
    quizCard.style.display = 'none';
    btnNext.style.display = 'none';
    controlBar.style.display = 'none';
    document.querySelector('.progress-section').style.display = 'none';
    resultView.style.display = 'block';"""

new_result_view = """  function showResultView() {
    quizCard.style.display = 'none';
    btnNext.style.display = 'none';
    controlBar.style.display = 'none';
    document.querySelector('.progress-section').style.display = 'none';
    if (quizNavBar) quizNavBar.style.display = 'none';
    resultView.style.display = 'block';"""
assert old_result_view in content, "old_result_view not matched"
content = content.replace(old_result_view, new_result_view, 1)

old_hide_result = """  function hideResultView() {
    resultView.style.display = 'none';
    quizCard.style.display = 'block';
    controlBar.style.display = 'flex';
    document.querySelector('.progress-section').style.display = 'block';
  }"""

new_hide_result = """  function hideResultView() {
    resultView.style.display = 'none';
    quizCard.style.display = 'block';
    controlBar.style.display = 'flex';
    document.querySelector('.progress-section').style.display = 'block';
    if (quizNavBar) quizNavBar.style.display = 'flex';
  }"""
assert old_hide_result in content, "old_hide_result not matched"
content = content.replace(old_hide_result, new_hide_result, 1)

# 5. Keyboard shortcuts for arrow keys
old_shortcuts = """    } else if (e.key === 'Enter' || e.key === ' ') {
      if (hasAnsweredCurrent && btnNext.style.display !== 'none') {
        e.preventDefault();
        btnNext.click();
      }
    } else if (e.key.toLowerCase() === 'f') {"""

new_shortcuts = """    } else if (e.key === 'Enter' || e.key === ' ') {
      if (nextBtn) {
        e.preventDefault();
        nextBtn.click();
      } else if (hasAnsweredCurrent && btnNext.style.display !== 'none') {
        e.preventDefault();
        btnNext.click();
      }
    } else if (e.key === 'ArrowRight') {
      if (nextBtn) nextBtn.click();
    } else if (e.key === 'ArrowLeft') {
      if (prevBtn && !prevBtn.disabled) prevBtn.click();
    } else if (e.key.toLowerCase() === 'f') {"""
assert old_shortcuts in content, "old_shortcuts not matched"
content = content.replace(old_shortcuts, new_shortcuts, 1)

with open(QUIZ_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully applied navigation bar and previous/next buttons to jlpt_n2_vocab_quiz.html!")
