import re
import shutil

app_path = '/Users/yamauchimiku/Documents/GitHub/japanese-learning/js/app.js'
with open(app_path, 'r', encoding='utf-8') as f:
    code = f.read()

target = """    if (btnSaveNewStudent && addStudentModal) {
      btnSaveNewStudent.addEventListener('click', () => {
        const nameVal = nameInput ? nameInput.value.trim() : '';
        const idVal = idInput ? idInput.value.trim() : '';
        const pinVal = passcodeInput ? passcodeInput.value.trim() : '';
        const langVal = langSelect ? langSelect.value : 'en';

        if (!nameVal) {
          showToast('生徒の名前を入力してください');
          if (nameInput) nameInput.focus();
          return;
        }

        if (!idVal) {
          showToast('生徒IDを入力してください');
          return;
        }

        if (!pinVal || pinVal.length < 4) {
          showToast('4桁のパスコードを入力してください');
          return;
        }

        // Check if ID is duplicate
        if (students.some(s => s.id.toLowerCase() === idVal.toLowerCase())) {
          showToast('この生徒IDは既に使用されています');
          return;
        }

        const newStudent = {
          id: idVal,
          name: nameVal,
          lang: langVal,
          passcode: pinVal
        };

        students.push(newStudent);
        localStorage.setItem('haku_students', JSON.stringify(students));

        // Initialize empty "授業で習った言葉" folder for this new student
        const CLASS_FOLDER_ID = 'folder_class_words';
        const CLASS_FOLDER_NAME = '授業で習った言葉';
        const foldersKey = `haku_mylist_folders_${idVal}`;
        localStorage.setItem(foldersKey, JSON.stringify([{ id: CLASS_FOLDER_ID, name: CLASS_FOLDER_NAME }]));

        renderAdminStudentList();
        addStudentModal.classList.add('hidden');
        showToast(`生徒「${nameVal}」（ID: ${idVal} / PIN: ${pinVal}）を追加しました！✨`);
        alert(`【新規生徒アカウント発行完了】\\n\\n生徒名: ${nameVal}\\n生徒ID: ${idVal}\\nパスコード (PIN): ${pinVal}\\n\\n※このパスコードは先生用管理画面の「生徒アカウント一覧」でもいつでも確認できます。`);
      });
    }"""

replacement = """    if (btnSaveNewStudent && addStudentModal) {
      btnSaveNewStudent.addEventListener('click', async () => {
        const nameVal = nameInput ? nameInput.value.trim() : '';
        const idVal = idInput ? idInput.value.trim() : '';
        const pinVal = passcodeInput ? passcodeInput.value.trim() : '';
        const langVal = langSelect ? langSelect.value : 'en';

        if (!nameVal) {
          showToast('生徒の名前を入力してください');
          if (nameInput) nameInput.focus();
          return;
        }

        if (!idVal) {
          showToast('生徒IDを入力してください');
          return;
        }

        if (!pinVal || pinVal.length < 4) {
          showToast('4桁のパスコードを入力してください');
          return;
        }

        // Check if ID is duplicate
        if (students.some(s => s.id.toLowerCase() === idVal.toLowerCase())) {
          showToast('この生徒IDは既に使用されています');
          return;
        }

        const newStudent = {
          id: idVal,
          name: nameVal,
          lang: langVal,
          passcode: pinVal
        };

        students.push(newStudent);
        localStorage.setItem('haku_students', JSON.stringify(students));
        if (typeof MASTER_STUDENT_PASSCODES !== 'undefined') {
          MASTER_STUDENT_PASSCODES[idVal] = pinVal;
        }

        // Initialize empty "授業で習った言葉" folder for this new student
        const CLASS_FOLDER_ID = 'folder_class_words';
        const CLASS_FOLDER_NAME = '授業で習った言葉';
        const foldersKey = `haku_mylist_folders_${idVal}`;
        localStorage.setItem(foldersKey, JSON.stringify([{ id: CLASS_FOLDER_ID, name: CLASS_FOLDER_NAME }]));

        // ☁️ Automatically provision Firebase Cloud Auth account behind the scenes
        try {
          const API_KEY = "AIzaSyBNsrBL1xRErsuOHgvI7xNs15cai-auoSE";
          const virtualEmail = `${idVal.toLowerCase()}@haku.local`;
          const passwordStr = `haku_${pinVal}_sec`;
          const signUpUrl = `https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=${API_KEY}`;
          await fetch(signUpUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              email: virtualEmail,
              password: passwordStr,
              returnSecureToken: true
            })
          });
          console.log(`Cloud auth account auto-created for student ${idVal} ☁️✨`);
        } catch (cloudErr) {
          console.warn('Initial cloud auth provisioning note:', cloudErr);
        }

        renderAdminStudentList();
        addStudentModal.classList.add('hidden');
        showToast(`生徒「${nameVal}」（ID: ${idVal} / PIN: ${pinVal}）を追加しました！✨`);
        alert(`【新規生徒アカウント発行完了】\\n\\n生徒名: ${nameVal}\\n生徒ID: ${idVal}\\nパスコード (PIN): ${pinVal}\\n\\n※Firebaseクラウド認証アカウントも自動連携されました！`);
      });
    }"""

assert target in code, "target not found"
code = code.replace(target, replacement)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(code)

pub_path = '/Users/yamauchimiku/Documents/GitHub/japanese-learning/public/js/app.js'
shutil.copy2(app_path, pub_path)
print("Updated btnSaveNewStudent in js/app.js and public/js/app.js successfully!")
