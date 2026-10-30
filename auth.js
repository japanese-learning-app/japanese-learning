/**
 * Japanese Learning App - Unified Student Authentication & Session Manager
 * 全ページ共通（総合ポータル, フラッシュカード, JLPT演習, マイページ）で
 * 生徒ID（例: 0001〜0024）およびパスコード、またはハク先生/管理者で
 * シングルサインオン（SSO）ログインを可能にする共通認証エンジン。
 */
(function() {
  // 生徒マスターデータ（js/data.js 未読込時のフォールバック兼用）
  const DEFAULT_STUDENTS = [
    { id: "haku", name: "ハク先生", lang: "ja", passcode: "ppooiillkk" },
    { id: "admin", name: "管理者", lang: "ja", passcode: "ppooiillkk" },
    { id: "0001", name: "Connor", lang: "en", passcode: "1122" },
    { id: "0002", name: "Eason", lang: "zh_HK", passcode: "2233" },
    { id: "0003", name: "두성", lang: "ko", passcode: "3344" },
    { id: "0004", name: "はな", lang: "en", passcode: "4455" },
    { id: "0005", name: "Giselle", lang: "en", passcode: "5566" },
    { id: "0006", name: "れい", lang: "en", passcode: "6677" },
    { id: "0007", name: "ジュンミン", lang: "zh_CN", passcode: "7788" },
    { id: "0008", name: "ヘンリー", lang: "zh_CN", passcode: "8899" },
    { id: "0009", name: "Gabri", lang: "en", passcode: "9900" },
    { id: "0010", name: "Eliie", lang: "zh_TW", passcode: "1133" },
    { id: "0011", name: "Keyvin", lang: "fr", passcode: "2244" },
    { id: "0012", name: "みどり", lang: "zh_TW", passcode: "3355" },
    { id: "0013", name: "なな", lang: "zh_HK", passcode: "4466" },
    { id: "0014", name: "Daniel", lang: "en", passcode: "5577" },
    { id: "0015", name: "Stephen", lang: "en", passcode: "6688" },
    { id: "0016", name: "ジウン", lang: "ko", passcode: "7799" },
    { id: "0017", name: "ハンウ", lang: "ko", passcode: "8800" },
    { id: "0018", name: "Justin", lang: "en", passcode: "1155" },
    { id: "0019", name: "ミンギ", lang: "ko", passcode: "2266" },
    { id: "0020", name: "Colin", lang: "zh_HK", passcode: "3377" },
    { id: "0021", name: "ともや", lang: "zh_TW", passcode: "4488" },
    { id: "0022", name: "生徒22", lang: "ja", passcode: "5599" },
    { id: "0023", name: "Arun", lang: "en", passcode: "6600" },
    { id: "0024", name: "生徒24", lang: "en", passcode: "7788" }
  ];

  const STORAGE_KEY_STUDENT_ID = 'haku_current_student_id';
  const STORAGE_KEY_STUDENTS_LIST = 'haku_students';

  // Firebase Config (Flashcardと同一)
  const firebaseConfig = {
    apiKey: "AIzaSyBNsrBL1xRErsuOHgvI7xNs15cai-auoSE",
    authDomain: "japanese-learning-e8a53.firebaseapp.com",
    projectId: "japanese-learning-e8a53",
    storageBucket: "japanese-learning-e8a53.firebasestorage.app",
    messagingSenderId: "1052063287116",
    appId: "1:1052063287116:web:7ccf89640419c489a3f1e9"
  };

  class UnifiedAuthManager {
    constructor() {
      this.listeners = [];
      this.initFirebase();
      this.refreshCurrentStudent();

      // 他タブでのログイン/ログアウト変更をリアルタイム検知
      window.addEventListener('storage', (e) => {
        if (e.key === STORAGE_KEY_STUDENT_ID) {
          this.refreshCurrentStudent();
          this.notify();
          this.updateAllHeaderUI();
        }
      });

      // DOM構築後に自動UI更新
      if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => this.initAutoHeader());
      } else {
        setTimeout(() => this.initAutoHeader(), 50);
      }
    }

    initFirebase() {
      if (typeof window !== 'undefined' && window.firebase && !this.fbApp) {
        try {
          if (!firebase.apps || !firebase.apps.length) {
            this.fbApp = firebase.initializeApp(firebaseConfig);
          } else {
            this.fbApp = firebase.app();
          }
          this.fbAuth = firebase.auth();
          this.fbDb = firebase.firestore();
        } catch (err) {
          console.warn('UnifiedAuth: Firebase init note:', err);
        }
      }
    }

    getStudents() {
      let saved = null;
      try {
        saved = localStorage.getItem(STORAGE_KEY_STUDENTS_LIST);
      } catch(e) {}
      if (saved) {
        try {
          const parsed = JSON.parse(saved);
          if (Array.isArray(parsed) && parsed.length) return parsed;
        } catch(e) {}
      }
      if (window.INITIAL_STUDENTS && Array.isArray(window.INITIAL_STUDENTS)) {
        return window.INITIAL_STUDENTS;
      }
      return DEFAULT_STUDENTS;
    }

    refreshCurrentStudent() {
      const studentId = localStorage.getItem(STORAGE_KEY_STUDENT_ID);
      if (!studentId || studentId === 'guest') {
        this.currentStudent = null;
        return null;
      }

      const list = this.getStudents();
      const found = list.find(s => s.id.toLowerCase() === studentId.toLowerCase());
      if (found) {
        this.currentStudent = found;
      } else {
        // IDはあるがリストにない場合のフォールバック
        this.currentStudent = { id: studentId, name: `生徒 ${studentId}`, lang: 'en', passcode: '' };
      }
      return this.currentStudent;
    }

    getCurrentStudent() {
      return this.currentStudent;
    }

    // 以前の auth.js の getCurrentUser() との互換性
    getCurrentUser() {
      if (!this.currentStudent) return null;
      return {
        id: this.currentStudent.id,
        name: this.currentStudent.name,
        email: `${this.currentStudent.id}@haku.local`,
        lang: this.currentStudent.lang || 'en',
        isTeacher: (this.currentStudent.id === 'haku' || this.currentStudent.id === 'admin')
      };
    }

    isLoggedIn() {
      return !!this.currentStudent;
    }

    isTeacher() {
      return !!(this.currentStudent && (this.currentStudent.id === 'haku' || this.currentStudent.id === 'admin'));
    }

    onAuthStateChanged(callback) {
      if (typeof callback === 'function') {
        this.listeners.push(callback);
        callback(this.getCurrentUser());
      }
    }

    notify() {
      const u = this.getCurrentUser();
      this.listeners.forEach(cb => {
        try { cb(u); } catch(e) { console.error(e); }
      });
    }

    async ensureCloudAuth(studentId, passcode) {
      this.initFirebase();
      if (!this.fbAuth) return false;
      const email = `${studentId}@haku.local`;
      const pass = `haku_${passcode}_sec`;
      try {
        await this.fbAuth.signInWithEmailAndPassword(email, pass);
        return true;
      } catch (err) {
        if (err.code === 'auth/user-not-found' || err.code === 'auth/invalid-credential') {
          try {
            await this.fbAuth.createUserWithEmailAndPassword(email, pass);
            return true;
          } catch(createErr) {
            console.warn('Cloud create error:', createErr);
          }
        }
        return false;
      }
    }

    async login(studentIdOrName, passcode) {
      const inputId = (studentIdOrName || '').trim();
      const inputPass = (passcode || '').trim();

      if (!inputId) throw new Error('生徒IDまたは名前を入力してください。');
      if (!inputPass) throw new Error('パスコードを入力してください。');

      // 先生・管理者チェック (ppooiillkk または ppooii0099)
      const isTeacherAttempt = (!inputId || inputId.toLowerCase() === 'haku' || inputId === 'ハク' || inputId === 'ハク先生' || inputId.toLowerCase() === 'admin' || inputId === '管理者');
      if (isTeacherAttempt && (inputPass === 'ppooiillkk' || inputPass === 'ppooii0099')) {
        const teacher = { id: 'haku', name: 'ハク先生', lang: 'ja', passcode: inputPass };
        localStorage.setItem(STORAGE_KEY_STUDENT_ID, teacher.id);
        this.currentStudent = teacher;
        this.ensureCloudAuth('haku', inputPass).catch(() => {});
        this.notify();
        this.updateAllHeaderUI();
        return teacher;
      }

      // 通常生徒チェック
      const list = this.getStudents();
      let matched = list.find(s => 
        (s.id.toLowerCase() === inputId.toLowerCase() || s.name.toLowerCase() === inputId.toLowerCase()) &&
        s.passcode === inputPass
      );

      // パスコードが直接一致しない場合、Cloud Authを試行
      if (!matched) {
        const candidate = list.find(s => s.id.toLowerCase() === inputId.toLowerCase() || s.name.toLowerCase() === inputId.toLowerCase());
        const tryId = candidate ? candidate.id : inputId;
        const cloudOk = await this.ensureCloudAuth(tryId, inputPass);
        if (cloudOk) {
          if (candidate) {
            candidate.passcode = inputPass;
            matched = candidate;
          } else {
            matched = { id: tryId, name: `生徒${tryId}`, lang: 'en', passcode: inputPass };
          }
        }
      }

      if (!matched) {
        throw new Error('生徒IDまたはパスコードが正しくありません。');
      }

      localStorage.setItem(STORAGE_KEY_STUDENT_ID, matched.id);
      this.currentStudent = matched;
      this.ensureCloudAuth(matched.id, matched.passcode).catch(() => {});
      this.notify();
      this.updateAllHeaderUI();
      return matched;
    }

    logout() {
      localStorage.removeItem(STORAGE_KEY_STUDENT_ID);
      this.currentStudent = null;
      if (this.fbAuth && this.fbAuth.currentUser) {
        this.fbAuth.signOut().catch(() => {});
      }
      this.notify();
      this.updateAllHeaderUI();
    }

    // ==========================================
    // 🎨 共通ログインモーダル ＆ ヘッダーバッジUI
    // ==========================================
    openLoginModal(defaultId = '') {
      let modal = document.getElementById('unified-auth-modal');
      if (!modal) {
        modal = this.createLoginModalElement();
        document.body.appendChild(modal);
      }
      const idInput = document.getElementById('uauth-id-input');
      const passInput = document.getElementById('uauth-pass-input');
      const errBox = document.getElementById('uauth-err-box');
      if (errBox) errBox.style.display = 'none';
      if (idInput) {
        idInput.value = defaultId || (this.currentStudent ? this.currentStudent.id : '');
        setTimeout(() => (idInput.value ? passInput.focus() : idInput.focus()), 80);
      }
      if (passInput) passInput.value = '';
      modal.style.display = 'flex';
    }

    closeLoginModal() {
      const modal = document.getElementById('unified-auth-modal');
      if (modal) modal.style.display = 'none';
    }

    createLoginModalElement() {
      const wrap = document.createElement('div');
      wrap.id = 'unified-auth-modal';
      wrap.style.cssText = 'position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(15,23,42,0.65); backdrop-filter:blur(4px); z-index:999999; display:none; align-items:center; justify-content:center; padding:16px; font-family:"Inter", "Yu Gothic", sans-serif; box-sizing:border-box;';
      wrap.onclick = (e) => { if (e.target === wrap) this.closeLoginModal(); };

      wrap.innerHTML = `
        <div style="background:white; border-radius:22px; max-width:400px; width:100%; padding:26px 24px; box-shadow:0 20px 45px rgba(0,0,0,0.22); position:relative; box-sizing:border-box;">
          <button onclick="window.AppAuth.closeLoginModal()" style="position:absolute; top:16px; right:16px; background:#F1F5F9; border:none; width:32px; height:32px; border-radius:50%; font-size:16px; color:#64748B; cursor:pointer; display:flex; align-items:center; justify-content:center;">✕</button>
          
          <div style="text-align:center; margin-bottom:20px;">
            <div style="display:inline-flex; align-items:center; justify-content:center; width:52px; height:52px; background:#EEF7FB; border-radius:16px; font-size:26px; margin-bottom:10px;">🌸</div>
            <h3 style="margin:0; font-size:1.25rem; font-weight:800; color:#1E293B;">生徒ログイン</h3>
            <p style="margin:6px 0 0; font-size:0.83rem; color:#64748B;">生徒IDとパスコードでログインすると、フラッシュカード・ポータル・JLPTのマイリストが自動で同期されます。</p>
          </div>

          <div id="uauth-err-box" style="display:none; background:#FEF2F2; border:1px solid #FCA5A5; color:#DC2626; border-radius:10px; padding:10px 14px; font-size:0.82rem; font-weight:700; margin-bottom:16px; line-height:1.4;"></div>

          <form id="uauth-form" onsubmit="event.preventDefault(); window.AppAuth.handleFormSubmit();" style="display:flex; flex-direction:column; gap:14px;">
            <div>
              <label style="display:block; font-size:0.8rem; font-weight:700; color:#334155; margin-bottom:5px;">生徒ID または 名前</label>
              <input type="text" id="uauth-id-input" placeholder="例: 0001, 0003, Connor, 두성..." autocomplete="username" style="width:100%; padding:11px 14px; border:1.5px solid #CBD5E1; border-radius:12px; font-size:0.95rem; font-weight:600; color:#0F172A; box-sizing:border-box; outline:none; transition:border 0.2s;" onfocus="this.style.borderColor='#1486AD'" onblur="this.style.borderColor='#CBD5E1'">
            </div>

            <div>
              <label style="display:block; font-size:0.8rem; font-weight:700; color:#334155; margin-bottom:5px;">4桁パスコード（または管理者キー）</label>
              <div style="position:relative;">
                <input type="password" id="uauth-pass-input" placeholder="4桁の数字 (例: 1122, 3344)" autocomplete="current-password" style="width:100%; padding:11px 42px 11px 14px; border:1.5px solid #CBD5E1; border-radius:12px; font-size:0.95rem; font-weight:600; color:#0F172A; box-sizing:border-box; outline:none; transition:border 0.2s;" onfocus="this.style.borderColor='#1486AD'" onblur="this.style.borderColor='#CBD5E1'">
                <button type="button" onclick="window.AppAuth.togglePassVisibility()" style="position:absolute; right:10px; top:50%; transform:translateY(-50%); background:none; border:none; font-size:16px; cursor:pointer; color:#64748B; padding:4px;">👁️</button>
              </div>
            </div>

            <button type="submit" id="uauth-submit-btn" style="margin-top:6px; background:#1486AD; color:white; border:none; padding:12px; border-radius:12px; font-size:0.95rem; font-weight:800; cursor:pointer; transition:background 0.2s; box-shadow:0 4px 12px rgba(20,134,173,0.25);">
              ログインする
            </button>
          </form>
        </div>
      `;
      return wrap;
    }

    togglePassVisibility() {
      const p = document.getElementById('uauth-pass-input');
      if (p) p.type = (p.type === 'password' ? 'text' : 'password');
    }

    async handleFormSubmit() {
      const id = document.getElementById('uauth-id-input')?.value || '';
      const pass = document.getElementById('uauth-pass-input')?.value || '';
      const errBox = document.getElementById('uauth-err-box');
      const submitBtn = document.getElementById('uauth-submit-btn');

      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = 'ログイン中...';
      }
      if (errBox) errBox.style.display = 'none';

      try {
        const student = await this.login(id, pass);
        this.closeLoginModal();
        if (typeof showToast === 'function') {
          showToast(`ログインしました: ${student.name} さん 🌸`);
        } else {
          alert(`ログインしました: ${student.name} さん 🌸`);
        }
        // ログイン成功時にページ固有の更新関数があれば呼ぶ
        if (window.UserProgress && typeof window.UserProgress.syncFromCloud === 'function') {
          window.UserProgress.syncFromCloud();
        }
        if (typeof renderSavedVocab === 'function') renderSavedVocab();
        if (typeof renderSavedQuizQuestions === 'function') renderSavedQuizQuestions();
        if (typeof updateProfileUI === 'function') updateProfileUI();
        if (typeof renderMyListModal === 'function') renderMyListModal();
        if (typeof renderUnifiedMylistModal === 'function') renderUnifiedMylistModal();
      } catch (err) {
        if (errBox) {
          errBox.textContent = err.message || 'ログインに失敗しました。';
          errBox.style.display = 'block';
        }
      } finally {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.textContent = 'ログインする';
        }
      }
    }

    // ユーザープロファイル確認・ログアウトポップアップ
    openUserMenu() {
      if (!this.currentStudent) {
        this.openLoginModal();
        return;
      }
      const s = this.currentStudent;
      const isTeacher = this.isTeacher();
      const msg = `${isTeacher ? '🌸 ハク先生 / 管理者モード' : `👤 生徒名: ${s.name} (ID: ${s.id})`}\n母国語設定: ${s.lang || 'en'}\n\n別の生徒IDでログインしますか？ログアウトしますか？`;
      
      const action = confirm(`${msg}\n\n[OK] = 別の生徒IDに切り替え\n[キャンセル] = 閉じる`);
      if (action) {
        this.openLoginModal();
      }
    }

    promptLogout() {
      if (confirm('ログアウトしますか？')) {
        this.logout();
        if (typeof showToast === 'function') showToast('ログアウトしました');
        else alert('ログアウトしました');
      }
    }

    // ヘッダーUIを全画面で自動検出＆更新
    updateAllHeaderUI() {
      const s = this.currentStudent;
      const isTeacher = this.isTeacher();

      // 1. フラッシュカード用バッジ (headerStudentBadge)
      const fcBadge = document.getElementById('headerStudentBadge');
      if (fcBadge) {
        fcBadge.textContent = s ? (isTeacher ? 'ハク先生 🌸' : `Student: ${s.name}`) : 'Student: Guest';
      }

      // 2. 総合ポータル用マイページボタン (header-user-name, top-user-chip)
      const portalUserChip = document.getElementById('top-user-chip');
      const portalUserName = document.getElementById('header-user-name');
      if (portalUserName) {
        portalUserName.textContent = s ? (isTeacher ? 'ハク先生 🌸' : `${s.name}`) : 'マイページ';
      }

      // 3. JLPT練習ページ用バッジ (auth-nav-logged-in / auth-nav-logged-out / auth-user-name)
      const jlptLoggedIn = document.getElementById('auth-nav-logged-in');
      const jlptLoggedOut = document.getElementById('auth-nav-logged-out');
      const jlptUserName = document.getElementById('auth-user-name');
      const jlptAvatar = document.getElementById('auth-user-avatar');

      if (jlptLoggedIn && jlptLoggedOut) {
        if (s) {
          jlptLoggedIn.style.display = 'flex';
          jlptLoggedOut.style.display = 'none';
          if (jlptUserName) jlptUserName.textContent = isTeacher ? 'ハク先生 🌸' : `${s.name} さん`;
          if (jlptAvatar) jlptAvatar.textContent = isTeacher ? '🌸' : (s.name || 'ユ').charAt(0);
        } else {
          jlptLoggedIn.style.display = 'none';
          jlptLoggedOut.style.display = 'flex';
        }
      }

      // 4. 動的マウントバッジ (.unified-student-badge)
      document.querySelectorAll('.unified-student-badge').forEach(el => {
        if (s) {
          el.innerHTML = `
            <span style="font-size:14px;">${isTeacher ? '🌸' : '👤'}</span>
            <span style="font-weight:700;">${isTeacher ? 'ハク先生' : s.name}</span>
            <span style="font-size:10px; background:rgba(0,0,0,0.08); padding:2px 6px; border-radius:6px; margin-left:2px;">ID: ${s.id}</span>
          `;
          el.title = 'クリックして生徒切替・ログアウト';
          el.onclick = () => this.openUserMenu();
        } else {
          el.innerHTML = `
            <span style="font-size:14px;">🔑</span>
            <span style="font-weight:700;">ログイン</span>
          `;
          el.title = '生徒ID・パスコードでログイン';
          el.onclick = () => this.openLoginModal();
        }
      });
    }

    initAutoHeader() {
      this.updateAllHeaderUI();

      // 各ページの既存ログインボタンにイベントを上書き/接続
      const oldLoginBtns = document.querySelectorAll('[onclick="openAuthModal()"], [onclick="openAuthModal(\'login\')"]');
      oldLoginBtns.forEach(btn => {
        btn.setAttribute('onclick', 'window.AppAuth.openLoginModal()');
      });
    }
  }

  // グローバル公開 (後方互換性のため AppAuth と StudentAuth の両方で提供)
  const authInstance = new UnifiedAuthManager();
  window.StudentAuth = authInstance;
  window.AppAuth = authInstance;
})();
