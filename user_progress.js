/**
 * User Progress & Gamification Manager
 * Manages lesson completion, stage unlocking, and comprehensive vocabulary bookmarks.
 * Synchronized with auth.js (per-user storage) & Firebase Cloud Firestore.
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
        console.log('UserProgress: Firebase Cloud Database connected! ☁️✨');
      } catch(e) {
        console.warn('Firebase init notice:', e);
      }
    }
  }

  class ProgressManager {
    constructor() {
      this.listeners = [];
      this.init();
      
      initFirebase();
      this.syncFromCloud();

      if (window.AppAuth) {
        window.AppAuth.onAuthStateChanged(() => {
          this.init();
          this.syncFromCloud();
        });
      }
    }

    getStorageKey() {
      const user = window.AppAuth ? window.AppAuth.getCurrentUser() : null;
      return user ? `jlpt_progress_${user.id}` : 'jlpt_progress_guest';
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
      this.notify();
    }

    getDefaultData() {
      return {
        completedLessons: [], // ['stage1-lesson1', 'stage1-lesson2', ...]
        unlockedStages: [1, 2, 3], // Default unlocked stages
        allUnlocked: true, // Default to accessible for easy exploration
        savedVocab: [], // [{ word, reading, meaning, level, addedAt }]
        points: 0
      };
    }

    save() {
      const key = this.getStorageKey();
      localStorage.setItem(key, JSON.stringify(this.data));
      this.notify();
      this.syncToCloud();
    }

    async syncFromCloud() {
      if (!isFirebaseReady || !fbDb) initFirebase();
      if (!isFirebaseReady || !fbDb) return;
      const user = window.AppAuth ? window.AppAuth.getCurrentUser() : null;
      const studentId = user ? user.id : (localStorage.getItem('haku_current_student_id') || 'guest');
      if (!studentId || studentId === 'guest') return;
      try {
        const docRef = fbDb.collection('students').doc(studentId);
        const snap = await docRef.get();
        if (snap.exists) {
          const cloudData = snap.data();
          if (cloudData && Array.isArray(cloudData.savedVocab)) {
            const localMap = new Map((this.data.savedVocab || []).map(v => [v.word, v]));
            cloudData.savedVocab.forEach(v => {
              if (v && v.word && !localMap.has(v.word)) {
                localMap.set(v.word, v);
              }
            });
            this.data.savedVocab = Array.from(localMap.values());
            const key = this.getStorageKey();
            localStorage.setItem(key, JSON.stringify(this.data));
            this.notify();
            console.log(`Cloud sync pulled ${this.data.savedVocab.length} items for student ${studentId} ☁️📥`);
          }
        }
      } catch(err) {
        console.warn('Cloud sync pull notice:', err.message);
      }
    }

    async syncToCloud() {
      if (!isFirebaseReady || !fbDb) initFirebase();
      if (!isFirebaseReady || !fbDb) return;
      const user = window.AppAuth ? window.AppAuth.getCurrentUser() : null;
      const studentId = user ? user.id : (localStorage.getItem('haku_current_student_id') || 'guest');
      if (!studentId || studentId === 'guest') return;
      try {
        const docRef = fbDb.collection('students').doc(studentId);
        await docRef.set({
          savedVocab: this.data.savedVocab || [],
          completedLessons: this.data.completedLessons || [],
          updatedAt: firebase.firestore.FieldValue.serverTimestamp()
        }, { merge: true });
        console.log(`Cloud sync pushed ${this.data.savedVocab.length} items for student ${studentId} ☁️📤`);
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

    // --- Saved Vocabulary (Global Vocab Bookmark) ---
    getSavedVocabList() {
      return this.data.savedVocab || [];
    }

    isVocabSaved(word) {
      return (this.data.savedVocab || []).some(v => v.word === word);
    }

    toggleSaveVocab(vocabItem) {
      const list = this.data.savedVocab || [];
      const wordKey = vocabItem.word || vocabItem.text || '';
      const idx = list.findIndex(v => v.word === wordKey);
      if (idx >= 0) {
        list.splice(idx, 1);
      } else {
        let meaningStr = vocabItem.meaning || '';
        if (!meaningStr && Array.isArray(vocabItem.meanings)) {
          meaningStr = vocabItem.meanings.join(', ');
        }
        list.unshift({
          word: wordKey,
          reading: vocabItem.reading || vocabItem.kana || '',
          meaning: meaningStr,
          level: vocabItem.level || '表現',
          addedAt: new Date().toISOString()
        });
      }
      this.data.savedVocab = list;
      this.save();
      return this.isVocabSaved(wordKey);
    }

    removeSavedVocab(word) {
      const list = this.data.savedVocab || [];
      this.data.savedVocab = list.filter(v => v.word !== word);
      this.save();
    }

    clearSavedVocab() {
      this.data.savedVocab = [];
      this.save();
    }

    // --- Points (Placeholder for future gamification rules) ---
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
