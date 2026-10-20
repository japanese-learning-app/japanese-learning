/**
 * User Progress & Unified Mylist Manager
 * 総合ポータル、マイページ、フラッシュカード、JLPT演習の
 * 全マイリスト（単語・例文・問題・漢字）を一元管理＆クラウド同期するエンジン。
 */
(function() {
  const firebaseConfig = {
    apiKey: "AIzaSyBNsrBL1xRErsuOHgvI7xNs15cai-auoSE",
    authDomain: "japanese-learning-e8a53.firebaseapp.com",
    projectId: "japanese-learning-e8a53",
    storageBucket: "japanese-learning-e8a53.firebasestorage.app",
    messagingSenderId: "1052063287116",
    appId: "1:1052063287116:web:7ccf89640419c489a3f1e9"
  };

  let fbApp = null;
  let fbDb = null;
  let isFirebaseReady = false;

  function initFirebase() {
    if (typeof window !== 'undefined' && window.firebase && !fbApp) {
      try {
        if (!firebase.apps || !firebase.apps.length) {
          fbApp = firebase.initializeApp(firebaseConfig);
        } else {
          fbApp = firebase.app();
        }
        fbDb = firebase.firestore();
        isFirebaseReady = true;
      } catch(e) {
        console.warn('UserProgress: Firebase init notice:', e);
      }
    }
  }

  class ProgressManager {
    constructor() {
      this.listeners = [];
      this.init();
      
      initFirebase();
      this.syncFromCloud();
      this.setupRealtimeListener();

      // ログイン状態変更の監視
      if (window.AppAuth) {
        window.AppAuth.onAuthStateChanged(() => {
          this.init();
          this.syncFromCloud();
          this.setupRealtimeListener();
          this.notify();
        });
      }

      window.addEventListener('storage', (e) => {
        if (e.key && (e.key.startsWith('haku_mylist_') || e.key.startsWith('jlpt_progress_') || e.key === 'haku_current_student_id')) {
          this.init();
          this.notify();
        }
      });

      // 📱 端末間リアルタイム同期: 別端末で保存された後、この画面に戻ってきた瞬間に最新データを自動PULL
      if (typeof document !== 'undefined') {
        document.addEventListener('visibilitychange', () => {
          if (!document.hidden) {
            this.syncFromCloud();
          }
        });
      }
      if (typeof window !== 'undefined') {
        window.addEventListener('focus', () => {
          this.syncFromCloud();
        });
      }
    }

    getCurrentStudentId() {
      if (window.AppAuth && typeof window.AppAuth.getCurrentStudent === 'function') {
        const s = window.AppAuth.getCurrentStudent();
        if (s && s.id) return s.id;
      }
      return localStorage.getItem('haku_current_student_id') || 'guest';
    }

    getStorageKey() {
      const studentId = this.getCurrentStudentId();
      return `jlpt_progress_${studentId}`;
    }

    init() {
      const key = this.getStorageKey();
      const raw = localStorage.getItem(key);
      if (raw) {
        try {
          this.data = JSON.parse(raw);
        } catch(e) {
          this.data = this.getDefaultData();
        }
      } else {
        this.data = this.getDefaultData();
      }
      if (!Array.isArray(this.data.savedVocab)) this.data.savedVocab = [];
      if (!Array.isArray(this.data.completedLessons)) this.data.completedLessons = [];
      this.notify();
    }

    getDefaultData() {
      return {
        completedLessons: [],
        unlockedStages: [1, 2, 3],
        allUnlocked: true,
        savedVocab: [], // [{ word, reading, meaning, level, addedAt, exampleJa, exampleNative, source }]
        points: 0
      };
    }

    save() {
      const key = this.getStorageKey();
      localStorage.setItem(key, JSON.stringify(this.data));
      this.notify();
      this.syncToCloud();
    }

    // ==========================================
    // 🌐 Firebase Cloud Firestore 同期
    // ==========================================
    async syncFromCloud() {
      if (!isFirebaseReady || !fbDb) initFirebase();
      if (!isFirebaseReady || !fbDb) return;
      const studentId = this.getCurrentStudentId();
      if (!studentId || studentId === 'guest') return;

      try {
        const docRef = fbDb.collection('students').doc(studentId);
        const snap = await docRef.get();
        if (snap.exists) {
          const cloudData = snap.data();
          let modified = false;

          // savedVocab の統合
          if (cloudData && Array.isArray(cloudData.savedVocab)) {
            const localMap = new Map((this.data.savedVocab || []).map(v => [v.word, v]));
            cloudData.savedVocab.forEach(v => {
              if (v && v.word && !localMap.has(v.word)) {
                localMap.set(v.word, v);
                modified = true;
              }
            });
            this.data.savedVocab = Array.from(localMap.values());
          }

          // フラッシュカードの mylist（ID配列）の同期
          if (cloudData && Array.isArray(cloudData.mylist)) {
            const fcKey = `haku_mylist_${studentId}`;
            const localFcMylist = JSON.parse(localStorage.getItem(fcKey) || '[]');
            const mergedFc = Array.from(new Set([...localFcMylist, ...cloudData.mylist]));
            localStorage.setItem(fcKey, JSON.stringify(mergedFc));
          }

          // カスタムカード（単語データ）の同期
          if (cloudData && Array.isArray(cloudData.customCards)) {
            const ccKey = `haku_custom_cards_${studentId}`;
            const localCc = JSON.parse(localStorage.getItem(ccKey) || '[]');
            const localMap = new Map(localCc.map(c => [c.id, c]));
            cloudData.customCards.forEach(c => {
              if (c && c.id && !localMap.has(c.id)) {
                localMap.set(c.id, c);
              }
            });
            localStorage.setItem(ccKey, JSON.stringify(Array.from(localMap.values())));
          }

          if (modified) {
            const key = this.getStorageKey();
            localStorage.setItem(key, JSON.stringify(this.data));
            this.notify();
          }
        }
      } catch(err) {
        console.warn('Cloud sync pull notice:', err.message);
      }
    }

    setupRealtimeListener() {
      if (!isFirebaseReady || !fbDb) initFirebase();
      if (!isFirebaseReady || !fbDb) return;
      const studentId = this.getCurrentStudentId();
      if (!studentId || studentId === 'guest') {
        if (this.unsubscribeRealtime) {
          this.unsubscribeRealtime();
          this.unsubscribeRealtime = null;
        }
        return;
      }

      if (this.currentSubscribedStudentId === studentId && this.unsubscribeRealtime) {
        return; // Already listening
      }

      if (this.unsubscribeRealtime) {
        this.unsubscribeRealtime();
      }

      try {
        const docRef = fbDb.collection('students').doc(studentId);
        this.currentSubscribedStudentId = studentId;
        this.unsubscribeRealtime = docRef.onSnapshot((snap) => {
          if (!snap || !snap.exists) return;
          const cloudData = snap.data();
          let modified = false;

          if (cloudData && Array.isArray(cloudData.savedVocab)) {
            const localMap = new Map((this.data.savedVocab || []).map(v => [v.word, v]));
            cloudData.savedVocab.forEach(v => {
              if (v && v.word && !localMap.has(v.word)) {
                localMap.set(v.word, v);
                modified = true;
              }
            });
            this.data.savedVocab = Array.from(localMap.values());
          }

          if (cloudData && Array.isArray(cloudData.mylist)) {
            const fcKey = `haku_mylist_${studentId}`;
            const localFcMylist = JSON.parse(localStorage.getItem(fcKey) || '[]');
            const mergedFc = Array.from(new Set([...localFcMylist, ...cloudData.mylist]));
            localStorage.setItem(fcKey, JSON.stringify(mergedFc));
          }

          if (cloudData && Array.isArray(cloudData.customCards)) {
            const ccKey = `haku_custom_cards_${studentId}`;
            const localCc = JSON.parse(localStorage.getItem(ccKey) || '[]');
            const localMap = new Map(localCc.map(c => [c.id, c]));
            cloudData.customCards.forEach(c => {
              if (c && c.id && !localMap.has(c.id)) {
                localMap.set(c.id, c);
              }
            });
            localStorage.setItem(ccKey, JSON.stringify(Array.from(localMap.values())));
          }

          if (modified) {
            const key = this.getStorageKey();
            localStorage.setItem(key, JSON.stringify(this.data));
            this.notify();
            console.log(`📡 [Realtime Sync] Other device saved new items! Updated student ${studentId} data.`);
          }
        }, (err) => {
          console.warn('Realtime listener notice:', err.message);
        });
      } catch(err) {
        console.warn('setupRealtimeListener note:', err);
      }
    }

    async syncToCloud() {
      if (!isFirebaseReady || !fbDb) initFirebase();
      if (!isFirebaseReady || !fbDb) return;
      const studentId = this.getCurrentStudentId();
      if (!studentId || studentId === 'guest') return;

      try {
        const docRef = fbDb.collection('students').doc(studentId);
        const fcMylist = JSON.parse(localStorage.getItem(`haku_mylist_${studentId}`) || '[]');
        const customCards = JSON.parse(localStorage.getItem(`haku_custom_cards_${studentId}`) || '[]');

        await docRef.set({
          savedVocab: this.data.savedVocab || [],
          mylist: fcMylist,
          customCards: customCards,
          completedLessons: this.data.completedLessons || [],
          updatedAt: firebase.firestore.FieldValue.serverTimestamp()
        }, { merge: true });
      } catch(err) {
        console.warn('Cloud sync push notice:', err.message);
      }
    }

    onProgressChanged(cb) {
      if (typeof cb === 'function') {
        this.listeners.push(cb);
        cb(this.data);
      }
    }

    notify() {
      this.listeners.forEach(cb => {
        try { cb(this.data); } catch(e) { console.error(e); }
      });
    }

    // ==========================================
    // 🌟 全マイリスト統合取得 (Flashcards + JLPT + Portal)
    // ==========================================
    getUnifiedMylist() {
      const studentId = this.getCurrentStudentId();
      const unifiedMap = new Map(); // wordKey -> item

      // 1. ポータル / 例文 / 辞書から保存された単語 (savedVocab)
      (this.data.savedVocab || []).forEach(item => {
        if (!item || !item.word) return;
        unifiedMap.set(item.word, {
          id: item.id || `vocab_${item.word}`,
          word: item.word,
          reading: item.reading || '',
          meaning: item.meaning || '',
          level: item.level || '表現',
          exampleJa: item.exampleJa || '',
          exampleNative: item.exampleNative || '',
          source: item.source || (item.level && item.level.startsWith('N') ? 'jlpt' : 'portal'),
          addedAt: item.addedAt || ''
        });
      });

      // 2. フラッシュカードのマイリスト (haku_mylist_{studentId})
      const fcKey = `haku_mylist_${studentId}`;
      const fcIds = JSON.parse(localStorage.getItem(fcKey) || '[]');
      const customCards = JSON.parse(localStorage.getItem(`haku_custom_cards_${studentId}`) || '[]');

      // 検索辞書・組み込み語彙のプール
      const allVocabPool = [
        ...(customCards || []),
        ...(window.INITIAL_VOCAB || []),
        ...(window.JLPT_VOCAB_ALL || []),
        ...(window.DICT_DATA || [])
      ];

      const poolMap = new Map();
      allVocabPool.forEach(card => {
        if (card.id && !poolMap.has(card.id)) poolMap.set(card.id, card);
        if (card.word && !poolMap.has(card.word)) poolMap.set(card.word, card);
        if (card.w && !poolMap.has(card.w)) poolMap.set(card.w, card);
      });

      fcIds.forEach(id => {
        const found = poolMap.get(id);
        if (found) {
          const word = found.word || found.w;
          const reading = found.reading || found.r || '';
          
          let meaning = '';
          if (found.meaning) {
            if (typeof found.meaning === 'object') {
              const studentLang = (window.AppAuth && window.AppAuth.getCurrentStudent()?.lang) || 'en';
              meaning = found.meaning[studentLang] || found.meaning.en || found.meaning.ja || JSON.stringify(found.meaning);
            } else {
              meaning = String(found.meaning);
            }
          } else if (Array.isArray(found.m)) {
            meaning = found.m.join(', ');
          }

          let exJa = '';
          let exNat = '';
          if (found.example) {
            if (typeof found.example === 'object') {
              exJa = found.example.ja || '';
              const studentLang = (window.AppAuth && window.AppAuth.getCurrentStudent()?.lang) || 'en';
              exNat = found.example[studentLang] || found.example.native || found.example.en || '';
            } else {
              exJa = String(found.example);
            }
          }

          if (unifiedMap.has(word)) {
            // 既存アイテムをフラッシュカードのリッチデータで強化
            const existing = unifiedMap.get(word);
            if (!existing.exampleJa && exJa) existing.exampleJa = exJa;
            if (!existing.exampleNative && exNat) existing.exampleNative = exNat;
            if (!existing.reading && reading) existing.reading = reading;
            if (!existing.meaning && meaning) existing.meaning = meaning;
            existing.cardId = id;
            existing.isFlashcard = true;
          } else {
            unifiedMap.set(word, {
              id: id,
              cardId: id,
              word: word,
              reading: reading,
              meaning: meaning,
              level: found.level || found.category || 'フラッシュカード',
              exampleJa: exJa,
              exampleNative: exNat,
              source: 'flashcard',
              isFlashcard: true,
              addedAt: found.createdAt || ''
            });
          }
        }
      });

      return Array.from(unifiedMap.values());
    }

    // ==========================================
    // 💾 マイリストの保存・追加・削除
    // ==========================================
    isVocabSaved(word) {
      if (!word) return false;
      const list = this.getUnifiedMylist();
      return list.some(item => item.word === word);
    }

    toggleSaveVocab(vocabItem) {
      const wordKey = vocabItem.word || vocabItem.text || vocabItem.w || '';
      if (!wordKey) return false;

      const isSaved = this.isVocabSaved(wordKey);
      if (isSaved) {
        this.removeSavedVocab(wordKey);
        return false;
      } else {
        this.addSavedVocab(vocabItem);
        return true;
      }
    }

    addSavedVocab(vocabItem) {
      const studentId = this.getCurrentStudentId();
      const wordKey = vocabItem.word || vocabItem.text || vocabItem.w || '';
      if (!wordKey) return;

      let meaningStr = vocabItem.meaning || '';
      if (!meaningStr && Array.isArray(vocabItem.meanings)) {
        meaningStr = vocabItem.meanings.join(', ');
      } else if (!meaningStr && Array.isArray(vocabItem.m)) {
        meaningStr = vocabItem.m.join(', ');
      }

      const newItem = {
        id: vocabItem.id || `saved_${Date.now()}_${Math.random().toString(36).substr(2, 5)}`,
        word: wordKey,
        reading: vocabItem.reading || vocabItem.kana || vocabItem.r || '',
        meaning: meaningStr,
        level: vocabItem.level || 'マイリスト',
        exampleJa: vocabItem.exampleJa || (vocabItem.example && vocabItem.example.ja) || '',
        exampleNative: vocabItem.exampleNative || (vocabItem.example && (vocabItem.example.native || vocabItem.example.en)) || '',
        source: vocabItem.source || 'portal',
        addedAt: new Date().toISOString()
      };

      // 1. ポータルの savedVocab に追加
      this.data.savedVocab = (this.data.savedVocab || []).filter(v => v.word !== wordKey);
      this.data.savedVocab.unshift(newItem);
      this.save();

      // 2. フラッシュカードのマイリストにも連動追加！
      try {
        const fcKey = `haku_mylist_${studentId}`;
        const fcIds = new Set(JSON.parse(localStorage.getItem(fcKey) || '[]'));
        fcIds.add(newItem.id);
        localStorage.setItem(fcKey, JSON.stringify(Array.from(fcIds)));

        // カスタムカードとしても保存し、フラッシュカード側で完全表示可能にする
        const ccKey = `haku_custom_cards_${studentId}`;
        const customCards = JSON.parse(localStorage.getItem(ccKey) || '[]');
        const existingCardIdx = customCards.findIndex(c => c.word === wordKey);
        const cardObj = {
          id: newItem.id,
          word: wordKey,
          reading: newItem.reading,
          meaning: { ja: meaningStr, en: meaningStr },
          example: { ja: newItem.exampleJa, en: newItem.exampleNative },
          studentId: studentId,
          createdAt: newItem.addedAt
        };
        if (existingCardIdx >= 0) {
          customCards[existingCardIdx] = cardObj;
        } else {
          customCards.unshift(cardObj);
        }
        localStorage.setItem(ccKey, JSON.stringify(customCards));
      } catch(err) {
        console.warn('Sync to flashcard storage warning:', err);
      }

      this.syncToCloud();
      this.notify();
      return true;
    }

    removeSavedVocab(wordKey) {
      const studentId = this.getCurrentStudentId();
      // 1. savedVocab から削除
      this.data.savedVocab = (this.data.savedVocab || []).filter(v => v.word !== wordKey);
      this.save();

      // 2. フラッシュカードのマイリストからも削除
      try {
        const ccKey = `haku_custom_cards_${studentId}`;
        const customCards = JSON.parse(localStorage.getItem(ccKey) || '[]');
        const card = customCards.find(c => c.word === wordKey);
        const cardId = card ? card.id : null;

        const fcKey = `haku_mylist_${studentId}`;
        const fcIds = new Set(JSON.parse(localStorage.getItem(fcKey) || '[]'));
        if (cardId) fcIds.delete(cardId);
        fcIds.delete(wordKey);
        fcIds.delete(`vocab_${wordKey}`);
        localStorage.setItem(fcKey, JSON.stringify(Array.from(fcIds)));
      } catch(err) {
        console.warn('Remove from flashcard storage notice:', err);
      }

      this.syncToCloud();
      this.notify();
    }

    clearSavedVocab() {
      this.data.savedVocab = [];
      this.save();
    }

    // --- Saved Vocabulary List for Backward Compatibility ---
    getSavedVocabList() {
      return this.getUnifiedMylist();
    }

    // --- Lessons Completion ---
    isLessonCompleted(lessonId) {
      return (this.data.completedLessons || []).includes(lessonId);
    }

    toggleLessonCompleted(lessonId) {
      const list = this.data.completedLessons || [];
      const idx = list.indexOf(lessonId);
      if (idx >= 0) {
        list.splice(idx, 1);
      } else {
        list.push(lessonId);
      }
      this.data.completedLessons = list;
      this.save();
      return this.isLessonCompleted(lessonId);
    }

    getCompletedLessonsCount() {
      return (this.data.completedLessons || []).length;
    }

    // --- Stages Unlocking ---
    isStageUnlocked(stageNum) {
      if (this.data.allUnlocked) return true;
      return (this.data.unlockedStages || [1]).includes(Number(stageNum));
    }

    toggleStageUnlocked(stageNum) {
      const num = Number(stageNum);
      const list = this.data.unlockedStages || [1];
      const idx = list.indexOf(num);
      if (idx >= 0) {
        if (list.length > 1) list.splice(idx, 1);
      } else {
        list.push(num);
      }
      this.data.unlockedStages = list;
      this.save();
      return this.isStageUnlocked(stageNum);
    }

    setAllUnlocked(bool) {
      this.data.allUnlocked = !!bool;
      this.save();
    }

    isAllUnlocked() {
      return !!this.data.allUnlocked;
    }

    // --- Points ---
    getPoints() {
      return this.data.points || 0;
    }

    addPoints(pt) {
      this.data.points = (this.data.points || 0) + Number(pt);
      this.save();
    }
  }

  window.UserProgress = new ProgressManager();
})();
