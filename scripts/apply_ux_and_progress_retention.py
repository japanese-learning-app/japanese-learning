# -*- coding: utf-8 -*-
"""
Apply Flashcard Progress Retention & Native Teacher UX Enhancements to js/app.js
1. Keep current card index when switching tabs or returning from background/cloud sync
2. Save and restore section progress (never reset to card 1 unexpectedly)
3. Add keyboard navigation for desktop/tablet (Space, Left/Right arrows, 1, 2, R)
4. Smooth progress bar updates
"""

import re
import os

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    app_js_path = os.path.join(root_dir, 'js', 'app.js')

    with open(app_js_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- 1. Add Flashcard Deck Progress Persistence Functions before updateActiveDeck ---
    persistence_helpers = """  // --- Flashcard Deck Progress Persistence (Never reset to card 1 on tab switch) ---
  function getDeckProgressKey() {
    if (isSearchStudyMode) return null;
    if (isMylistStudyMode) return 'progress_mylist_study';
    if (currentDeckFilter === 'jlpt') return `progress_jlpt_${currentJlptDeckLevel || 'N5'}`;
    if (currentSection !== 'all') return `progress_section_${currentSection}`;
    if (currentFolder !== 'all') return `progress_folder_${currentFolder}`;
    return 'progress_all_curriculum';
  }

  function saveCurrentDeckProgress() {
    const key = getDeckProgressKey();
    if (!key || !activeDeck || activeDeck.length === 0) return;
    try {
      const raw = localStorage.getItem('haku_deck_progress_map');
      const map = raw ? JSON.parse(raw) : {};
      const card = activeDeck[currentIndex];
      map[key] = {
        index: currentIndex,
        cardId: card ? card.id : null,
        total: activeDeck.length,
        timestamp: Date.now()
      };
      localStorage.setItem('haku_deck_progress_map', JSON.stringify(map));
    } catch (e) {}
  }

  function getSavedDeckProgress(key) {
    if (!key) return null;
    try {
      const raw = localStorage.getItem('haku_deck_progress_map');
      if (!raw) return null;
      const map = JSON.parse(raw);
      return map[key] || null;
    } catch (e) {
      return null;
    }
  }

  """

    # Replace updateActiveDeck
    old_update_active_deck = """  function updateActiveDeck() {
    if (currentDeckFilter === 'jlpt') {
      const lvl = currentJlptDeckLevel || 'N5';
      const jlptList = (window.JLPT_VOCAB && window.JLPT_VOCAB[lvl]) || [];
      const dictMap = window.DICT_EXAMPLES_MAP || {};
      activeDeck = jlptList.map((entry, idx) => {
        const dictEx = dictMap[entry.word] || (entry.reading && dictMap[entry.reading]);
        const ex = (entry.examples && entry.examples[0]) ? entry.examples[0] : (dictEx || null);
        const fallbackDlg = getNaturalDefaultDialogue(entry.word, entry.reading || entry.k);
        const meaningText = (entry.meanings || []).join(', ') || '—';
        return {
          id: `jlpt_${entry.level || lvl}_${idx}_${entry.word}`,
          word: entry.word,
          reading: entry.reading || entry.k || entry.word,
          category: `JLPT ${entry.level || lvl}`,
          section_title: `JLPT ${entry.level || lvl} 単語`,
          folder_id: `jlpt_${lvl}`,
          meaning: {
            en: meaningText,
            ja: entry.word,
            zh_TW: meaningText,
            zh_CN: meaningText,
            ko: meaningText,
            zh_HK: meaningText,
            fr: meaningText
          },
          example: {
            ja: ex ? ex.ja : fallbackDlg.ja,
            en: ex ? (ex.en || '') : fallbackDlg.en
          },
          related: `【JLPT】${entry.level || lvl} / 【行】${entry.row || '—'}`,
          isJlpt: true
        };
      });
      currentIndex = 0;
      isCardFlipped = false;
      renderCurrentCard();
      return;
    }

    let pool = vocabList.filter(card => {
      // Shared vs Student dedicated
      if (currentDeckFilter === 'mine') {
        if (!currentStudent) return false;
        return card.studentId === currentStudent.id;
      } else {
        return !card.studentId || card.studentId === 'all';
      }
    });

    // Filter by Folder
    if (currentFolder !== 'all') {
      pool = pool.filter(card => card.folder_id === currentFolder);
    }

    // Filter by Section
    if (currentSection !== 'all') {
      pool = pool.filter(card => Number(card.section_num) === Number(currentSection));
    }

    activeDeck = pool;
    currentIndex = 0;
    isCardFlipped = false;
    renderCurrentCard();
  }"""

    new_update_active_deck = persistence_helpers + """function updateActiveDeck(preserveTarget = false, targetCardId = null, targetIndex = null) {
    if (currentDeckFilter === 'jlpt') {
      const lvl = currentJlptDeckLevel || 'N5';
      const jlptList = (window.JLPT_VOCAB && window.JLPT_VOCAB[lvl]) || [];
      const dictMap = window.DICT_EXAMPLES_MAP || {};
      activeDeck = jlptList.map((entry, idx) => {
        const dictEx = dictMap[entry.word] || (entry.reading && dictMap[entry.reading]);
        const ex = (entry.examples && entry.examples[0]) ? entry.examples[0] : (dictEx || null);
        const fallbackDlg = getNaturalDefaultDialogue(entry.word, entry.reading || entry.k);
        const meaningText = (entry.meanings || []).join(', ') || '—';
        return {
          id: `jlpt_${entry.level || lvl}_${idx}_${entry.word}`,
          word: entry.word,
          reading: entry.reading || entry.k || entry.word,
          category: `JLPT ${entry.level || lvl}`,
          section_title: `JLPT ${entry.level || lvl} 単語`,
          folder_id: `jlpt_${lvl}`,
          meaning: {
            en: meaningText,
            ja: entry.word,
            zh_TW: meaningText,
            zh_CN: meaningText,
            ko: meaningText,
            zh_HK: meaningText,
            fr: meaningText
          },
          example: {
            ja: ex ? ex.ja : fallbackDlg.ja,
            en: ex ? (ex.en || '') : fallbackDlg.en
          },
          related: `【JLPT】${entry.level || lvl} / 【行】${entry.row || '—'}`,
          isJlpt: true
        };
      });
      applyDeckIndexPersistence(preserveTarget, targetCardId, targetIndex);
      return;
    }

    let pool = vocabList.filter(card => {
      // Shared vs Student dedicated
      if (currentDeckFilter === 'mine') {
        if (!currentStudent) return false;
        return card.studentId === currentStudent.id;
      } else {
        return !card.studentId || card.studentId === 'all';
      }
    });

    // Filter by Folder
    if (currentFolder !== 'all') {
      pool = pool.filter(card => card.folder_id === currentFolder);
    }

    // Filter by Section
    if (currentSection !== 'all') {
      pool = pool.filter(card => Number(card.section_num) === Number(currentSection));
    }

    activeDeck = pool;
    applyDeckIndexPersistence(preserveTarget, targetCardId, targetIndex);
  }

  function applyDeckIndexPersistence(preserveTarget = false, targetCardId = null, targetIndex = null) {
    if (!activeDeck || activeDeck.length === 0) {
      currentIndex = 0;
      isCardFlipped = false;
      renderCurrentCard();
      return;
    }

    let desiredIndex = 0;
    const progressKey = getDeckProgressKey();
    const saved = getSavedDeckProgress(progressKey);

    if (targetCardId) {
      const foundIdx = activeDeck.findIndex(c => c.id === targetCardId);
      if (foundIdx !== -1) {
        desiredIndex = foundIdx;
      } else if (targetIndex !== null && targetIndex >= 0 && targetIndex < activeDeck.length) {
        desiredIndex = targetIndex;
      }
    } else if (preserveTarget) {
      if (typeof currentIndex === 'number' && currentIndex >= 0 && currentIndex < activeDeck.length) {
        desiredIndex = currentIndex;
      } else if (saved && typeof saved.index === 'number') {
        desiredIndex = Math.min(Math.max(0, saved.index), activeDeck.length - 1);
      }
    } else {
      if (saved) {
        if (saved.cardId) {
          const foundIdx = activeDeck.findIndex(c => c.id === saved.cardId);
          if (foundIdx !== -1) desiredIndex = foundIdx;
          else if (typeof saved.index === 'number') desiredIndex = Math.min(Math.max(0, saved.index), activeDeck.length - 1);
        } else if (typeof saved.index === 'number') {
          desiredIndex = Math.min(Math.max(0, saved.index), activeDeck.length - 1);
        }
      }
    }

    desiredIndex = Math.min(Math.max(0, desiredIndex), activeDeck.length - 1);
    currentIndex = desiredIndex;
    isCardFlipped = false;
    renderCurrentCard();
    saveCurrentDeckProgress();
  }"""

    assert old_update_active_deck in content, "old_update_active_deck not found in app.js"
    content = content.replace(old_update_active_deck, new_update_active_deck, 1)
    print("Replaced updateActiveDeck with persistence support!")

    # --- 2. Update renderCurrentCard to update progress bar and save progress ---
    old_render_progress = """    const card = activeDeck[currentIndex];
    document.getElementById('cardProgressText').textContent = `${currentIndex + 1} / ${activeDeck.length}`;"""

    new_render_progress = """    const card = activeDeck[currentIndex];
    document.getElementById('cardProgressText').textContent = `${currentIndex + 1} / ${activeDeck.length}`;
    const cardProgressBar = document.getElementById('cardProgressBar');
    if (cardProgressBar && activeDeck.length > 0) {
      const pct = Math.round(((currentIndex + 1) / activeDeck.length) * 100);
      cardProgressBar.style.width = `${pct}%`;
    }
    saveCurrentDeckProgress();"""

    assert old_render_progress in content, "old_render_progress not found"
    content = content.replace(old_render_progress, new_render_progress, 1)
    print("Updated renderCurrentCard with progress bar and saveCurrentDeckProgress!")

    # --- 3. Update navStudy click listener to protect study state ---
    old_nav_study = """    document.getElementById('navStudy').addEventListener('click', () => {
      // Clear search query and close dropdown
      const topSearch = document.getElementById('globalTopSearchInput');
      const clearTopBtn = document.getElementById('btnClearTopSearch');
      const dropdown = document.getElementById('searchDropdownContainer');
      if (topSearch) topSearch.value = '';
      if (clearTopBtn) clearTopBtn.classList.add('hidden');
      if (dropdown) dropdown.classList.add('hidden');
      sidebarSearchQuery = '';

      // Return to folder overview
      backToFolderOverview();
      switchView('flashcards');
    });"""

    new_nav_study = """    document.getElementById('navStudy').addEventListener('click', () => {
      // Clear search query and close dropdown
      const topSearch = document.getElementById('globalTopSearchInput');
      const clearTopBtn = document.getElementById('btnClearTopSearch');
      const dropdown = document.getElementById('searchDropdownContainer');
      if (topSearch) topSearch.value = '';
      if (clearTopBtn) clearTopBtn.classList.add('hidden');
      if (dropdown) dropdown.classList.add('hidden');
      sidebarSearchQuery = '';

      // ★ 学習中（studyモード）なら、途中のカード（5枚目等）をリセットせずそのまま再開！
      if (currentNavLevel === 'study' && activeDeck.length > 0) {
        switchView('flashcards');
        renderCurrentCard();
      } else {
        backToFolderOverview();
        switchView('flashcards');
      }
    });"""

    assert old_nav_study in content, "old_nav_study not found"
    content = content.replace(old_nav_study, new_nav_study, 1)
    print("Protected navStudy click listener from resetting study progress!")

    # --- 4. Update drawerBtnHome to protect study state ---
    old_drawer_home = """      drawerBtnHome.addEventListener('click', () => {
        closeMenuDrawer();
        const topSearch = document.getElementById('globalTopSearchInput');
        const clearTopBtn = document.getElementById('btnClearTopSearch');
        const dropdown = document.getElementById('searchDropdownContainer');
        if (topSearch) topSearch.value = '';
        if (clearTopBtn) clearTopBtn.classList.add('hidden');
        if (dropdown) dropdown.classList.add('hidden');
        sidebarSearchQuery = '';

        backToFolderOverview();
        switchView('flashcards');
      });"""

    new_drawer_home = """      drawerBtnHome.addEventListener('click', () => {
        closeMenuDrawer();
        const topSearch = document.getElementById('globalTopSearchInput');
        const clearTopBtn = document.getElementById('btnClearTopSearch');
        const dropdown = document.getElementById('searchDropdownContainer');
        if (topSearch) topSearch.value = '';
        if (clearTopBtn) clearTopBtn.classList.add('hidden');
        if (dropdown) dropdown.classList.add('hidden');
        sidebarSearchQuery = '';

        if (currentNavLevel === 'study' && activeDeck.length > 0) {
          switchView('flashcards');
          renderCurrentCard();
        } else {
          backToFolderOverview();
          switchView('flashcards');
        }
      });"""

    assert old_drawer_home in content, "old_drawer_home not found"
    content = content.replace(old_drawer_home, new_drawer_home, 1)
    print("Protected drawerBtnHome listener from resetting study progress!")

    # --- 5. Update visibilitychange event to protect current card on background tab return ---
    old_visibility = """    document.addEventListener('visibilitychange', () => {
      if (!document.hidden && currentStudent && currentStudent.id !== 'guest') {
        syncStudentFromCloud(currentStudent.id).then(changed => {
          if (changed) {
            loadMylistForCurrentStudent();
            updateActiveDeck();
            if (currentView === 'mylist') renderMylistGrid();
          }
        }).catch(() => {});
      }
    });"""

    new_visibility = """    document.addEventListener('visibilitychange', () => {
      if (!document.hidden && currentStudent && currentStudent.id !== 'guest') {
        const lastCardId = (activeDeck && activeDeck[currentIndex]) ? activeDeck[currentIndex].id : null;
        const lastIndex = currentIndex;
        syncStudentFromCloud(currentStudent.id).then(changed => {
          if (changed) {
            loadMylistForCurrentStudent();
            // ★ 他タブから戻ってきたときに見ていたカード（5枚目等）をそのまま保持！
            updateActiveDeck(true, lastCardId, lastIndex);
            if (currentView === 'mylist') renderMylistGrid();
          }
        }).catch(() => {});
      }
    });"""

    assert old_visibility in content, "old_visibility not found"
    content = content.replace(old_visibility, new_visibility, 1)
    print("Protected visibilitychange event from resetting card index!")

    # --- 6. Add Keyboard Navigation Shortcuts for Desktop & Tablet ---
    keyboard_shortcuts = """
    // --- Keyboard Shortcuts for Desktop / Tablet (Space to Flip, Arrows to Navigate) ---
    window.addEventListener('keydown', (e) => {
      const tag = (e.target && e.target.tagName) ? e.target.tagName.toLowerCase() : '';
      if (tag === 'input' || tag === 'textarea' || (e.target && e.target.isContentEditable)) return;

      const viewFlashcards = document.getElementById('viewFlashcards');
      if (!viewFlashcards || viewFlashcards.classList.contains('hidden')) return;

      const openModals = document.querySelectorAll('.modal:not(.hidden), [id$="Modal"]:not(.hidden)');
      let hasOpenModal = false;
      openModals.forEach(m => {
        if (m.offsetParent !== null && !m.classList.contains('hidden') && m.id !== 'searchDropdownContainer') {
          hasOpenModal = true;
        }
      });
      if (hasOpenModal) return;

      if (e.code === 'Space') {
        e.preventDefault();
        flipCard();
      } else if (e.code === 'ArrowRight' || e.code === 'KeyD') {
        e.preventDefault();
        const btnNext = document.getElementById('btnNext');
        if (btnNext) btnNext.click();
      } else if (e.code === 'ArrowLeft' || e.code === 'KeyA') {
        e.preventDefault();
        const btnPrev = document.getElementById('btnPrev');
        if (btnPrev) btnPrev.click();
      } else if (e.code === 'KeyR' || e.code === 'ArrowUp') {
        e.preventDefault();
        if (activeDeck && activeDeck[currentIndex]) {
          if (isCardFlipped && activeDeck[currentIndex].example) {
            toggleJapaneseSpeech(activeDeck[currentIndex].example.ja);
          } else {
            toggleJapaneseSpeech(activeDeck[currentIndex]);
          }
        }
      } else if (e.code === 'Digit1' || e.code === 'Numpad1') {
        const btnReview = document.getElementById('btnMarkReview');
        if (btnReview) btnReview.click();
      } else if (e.code === 'Digit2' || e.code === 'Numpad2') {
        const btnKnown = document.getElementById('btnMarkKnown');
        if (btnKnown) btnKnown.click();
      }
    });
"""
    # Insert keyboard shortcuts inside setupEventListeners or near the end of event listeners
    # Find btnMarkKnown listener and add after flashcard button listeners
    anchor = "const btnMarkKnown = document.getElementById('btnMarkKnown');"
    pos = content.find(anchor)
    assert pos != -1, "btnMarkKnown anchor not found"
    # Find the end of flashcard buttons section
    anchor_end = "const flashcardEl = document.getElementById('flashcardElement');"
    pos_end = content.find(anchor_end, pos)
    assert pos_end != -1, "flashcardEl anchor not found"

    content = content[:pos_end] + keyboard_shortcuts + "\n    " + content[pos_end:]
    print("Added desktop/tablet keyboard shortcuts (Space, Arrows, R, 1, 2)!")

    # Write back to js/app.js and public/js/app.js
    public_app_js_path = os.path.join(root_dir, 'public', 'js', 'app.js')
    with open(app_js_path, 'w', encoding='utf-8') as f:
        f.write(content)
    with open(public_app_js_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated js/app.js and public/js/app.js!")

if __name__ == '__main__':
    main()
