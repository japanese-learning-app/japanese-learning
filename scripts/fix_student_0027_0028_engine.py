import re
import os
import shutil

app_path = '/Users/yamauchimiku/Documents/GitHub/japanese-learning/js/app.js'
with open(app_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update version token
old_ver = "const CURRENT_DATA_VERSION = 'v67_permanent_future_word_protection_v69_autoheal';"
new_ver = "const CURRENT_DATA_VERSION = 'v67_permanent_future_word_protection_v70_fix_0027_0028';"
assert old_ver in code, "old_ver not found"
code = code.replace(old_ver, new_ver)

# 2. Update getBilingualMeaning distinction cleaner
old_clean = r"""    // 🛡️ Nuance / Distinction Defense: Ensure "vs" / "【使い分け】" is NEVER displayed in Meaning / Translation (1st place)
    // It strictly belongs in the 2nd place (Related / Conjugations)
    if (nativeMeaning && (/\bvs\b|【使い分け】/i.test(nativeMeaning))) {
      nativeMeaning = (enMeaning && !/\bvs\b/i.test(enMeaning)) ? enMeaning : (cardWord || '');
    }
    if (enMeaning && (/\bvs\b|【使い分け】/i.test(enMeaning))) {
      enMeaning = cardWord || '';
    }"""

new_clean = r"""    // 🛡️ Nuance / Distinction Defense: Ensure "vs" / "【使い分け】" is NEVER displayed in Meaning / Translation (1st place)
    // It strictly belongs in the 2nd place (Related / Conjugations)
    const cleanDistinction = (text) => {
      if (!text || typeof text !== 'string') return text;
      if (/\bvs\b|【使い分け】/i.test(text)) {
        const m = text.match(/\(([^)]+)\)\s*$/);
        if (m && m[1] && !/\bvs\b/i.test(m[1])) {
          return m[1].trim();
        }
        return '';
      }
      return text;
    };
    nativeMeaning = cleanDistinction(nativeMeaning);
    enMeaning = cleanDistinction(enMeaning);
    if (!nativeMeaning) {
      nativeMeaning = enMeaning || cardWord || '';
    }
    if (!enMeaning) {
      enMeaning = cardWord || '';
    }"""

assert old_clean in code, "old_clean not found"
code = code.replace(old_clean, new_clean)

# 3. Update auto-heal block in initData
old_autoheal = """          // Also purge old custom card duplicates for student 0027 and 0028
          if (window.CLASS_0027_IDS && window.CLASS_0027_IDS.length > 0) {
            const beforeLen = items.length;
            items = items.filter(c => !(c.studentId === '0027' && c.id && !c.id.startsWith('class_word_0027_')));
            if (items.length !== beforeLen) modified = true;
          }
          if (window.CLASS_0028_IDS && window.CLASS_0028_IDS.length > 0) {
            const beforeLen = items.length;
            items = items.filter(c => !(c.studentId === '0028' && c.id && !c.id.startsWith('class_word_0028_')));
            if (items.length !== beforeLen) modified = true;
          }"""

new_autoheal = """          // Also purge old custom card duplicates for student 0027 and 0028
          if (window.CLASS_0027_IDS && window.CLASS_0027_IDS.length > 0) {
            const beforeLen = items.length;
            items = items.filter(c => !(c && c.studentId === '0027' && typeof c.id === 'string' && !c.id.startsWith('class_word_0027_')));
            if (items.length !== beforeLen) modified = true;
          }
          if (window.CLASS_0028_IDS && window.CLASS_0028_IDS.length > 0) {
            const beforeLen = items.length;
            items = items.filter(c => !(c && c.studentId === '0028' && typeof c.id === 'string' && !c.id.startsWith('class_word_0028_')));
            if (items.length !== beforeLen) modified = true;
          }"""

assert old_autoheal in code, "old_autoheal not found"
code = code.replace(old_autoheal, new_autoheal)

# 4. Update seedStudents and allStudentIds in initData version migration
old_migration = """    if (savedVersion !== CURRENT_DATA_VERSION) {
      // Reload latest INITIAL_STUDENTS master list when version updates, while preserving edits & newly added ones
      const seedStudents = window.INITIAL_STUDENTS || [];
      const savedStudents = localStorage.getItem('haku_students');
      if (savedStudents) {
        try {
          const parsed = JSON.parse(savedStudents);
          const savedMap = new Map(parsed.map(s => [s.id, s]));
          // Apply teacher's edited names/passcodes onto seed students, or fallback to seed
          students = seedStudents.map(seed => {
            const saved = savedMap.get(seed.id);
            return saved ? { ...seed, ...saved } : seed;
          });
          // Also include any new students added beyond seed
          const seedIds = new Set(seedStudents.map(s => s.id));
          const customExtra = parsed.filter(s => !seedIds.has(s.id) && !s.id.startsWith('student_'));
          students = [...students, ...customExtra];
        } catch (e) {
          students = seedStudents;
        }
      } else {
        students = seedStudents;
      }
      localStorage.setItem('haku_students', JSON.stringify(students));

      // Initialize per-student exact tab card mappings
      const CLASS_FOLDER_ID = 'folder_class_words';
      const CLASS_FOLDER_NAME = '授業で習った言葉';

      const STUDENT_DOC_RANGES = {
        '0012': [1, 289],      // みどりさん (289語 + 1追加語)
        '0011': [290, 498],    // Keyvinさん (209語)
        '0013': [499, 538],    // ななさん (40語)
        '0014': [539, 639],    // Danielさん (101語)
        '0015': [640, 873],    // Stephenさん (234語)
        '0016': [874, 1144],   // ジウンさん (271語)
        '0017': [1145, 1213],  // ハンウさん (69語)
        '0018': [1214, 1232],  // Justinさん (19語)
        '0019': [1233, 1314],  // ミンギさん (82語)
        '0020': [1315, 1397],  // Colinさん (83語)
        '0021': [1398, 1598],  // ともやさん (201語)
        '0022': [1599, 1602]   // 生徒22 (追加語彙)
      };

      const allStudentIds = [...students.map(s => s.id), 'guest'];
      allStudentIds.forEach(stId => {
        const key = `haku_mylist_${stId}`;
        const foldersKey = `haku_mylist_folders_${stId}`;
        const mapKey = `haku_mylist_card_map_${stId}`;

        // Ensure "授業で習った言葉" folder exists
        let stFolders = [];
        try { stFolders = JSON.parse(localStorage.getItem(foldersKey) || '[]'); } catch (e) { stFolders = []; }
        if (!stFolders.find(f => f.id === CLASS_FOLDER_ID)) {
          stFolders.unshift({ id: CLASS_FOLDER_ID, name: CLASS_FOLDER_NAME });
          localStorage.setItem(foldersKey, JSON.stringify(stFolders));
        }
        // Preserve all existing student cards and add all tagged class words (Non-destructive union)
        let stSet = [];
        try { stSet = JSON.parse(localStorage.getItem(key) || '[]'); } catch (e) { stSet = []; }
        let stMap = {};
        try { stMap = JSON.parse(localStorage.getItem(mapKey) || '{}'); } catch (e) { stMap = {}; }

        const finalStudentSet = new Set(stSet);
        const studentCardIds = new Set();

        // 1. Auto-discover all cards tagged for this student from CLASS_VOCAB_DATA
        (window.CLASS_VOCAB_DATA || []).forEach(c => {
          if (c && c.id && (c.studentId === stId || (Array.isArray(c.studentIds) && c.studentIds.includes(stId)))) {
            studentCardIds.add(c.id);
          }
        });

        // 2. Legacy student doc ranges fallback
        const range = STUDENT_DOC_RANGES[stId];
        if (range) {
          const [startNum, endNum] = range;
          for (let num = startNum; num <= endNum; num++) {
            studentCardIds.add(`class_word_${String(num).padStart(4, '0')}`);
          }
        }

        // 3. Fallbacks for curated cards
        if (stId === '0028') {
          finalStudentSet.forEach(id => {
            if (id.startsWith('card_') && !id.startsWith('class_word_0028_')) {
              finalStudentSet.delete(id);
              delete stMap[id];
            }
          });
          const ids0028 = window.CLASS_0028_IDS || [];
          ids0028.forEach(cId => {
            studentCardIds.add(cId);
            finalStudentSet.add(cId);
            stMap[cId] = CLASS_FOLDER_ID;
          });
        }
        if (stId === '0027') {
          finalStudentSet.forEach(id => {
            if (id.startsWith('card_') && !id.startsWith('class_word_0027_')) {
              finalStudentSet.delete(id);
              delete stMap[id];
            }
          });
          const ids0027 = window.CLASS_0027_IDS || [];
          ids0027.forEach(cId => {
            studentCardIds.add(cId);
            finalStudentSet.add(cId);
            stMap[cId] = CLASS_FOLDER_ID;
          });
        }"""

new_migration = """    if (savedVersion !== CURRENT_DATA_VERSION) {
      // Reload latest master list when version updates, while preserving edits & newly added ones
      if (!window.INITIAL_STUDENTS && window.AppAuth && typeof window.AppAuth.getStudents === 'function') {
        window.INITIAL_STUDENTS = window.AppAuth.getStudents();
      }
      const seedStudents = (window.AppAuth && typeof window.AppAuth.getStudents === 'function') 
        ? window.AppAuth.getStudents() 
        : (window.INITIAL_STUDENTS || []);
      const savedStudents = localStorage.getItem('haku_students');
      if (savedStudents) {
        try {
          const parsed = JSON.parse(savedStudents);
          const savedMap = new Map((Array.isArray(parsed) ? parsed : []).map(s => [s.id, s]));
          // Apply teacher's edited names/passcodes onto seed students, or fallback to seed
          students = seedStudents.map(seed => {
            const saved = savedMap.get(seed.id);
            return saved ? { ...seed, ...saved } : seed;
          });
          // Also include any new students added beyond seed
          const seedIds = new Set(seedStudents.map(s => s.id));
          const customExtra = (Array.isArray(parsed) ? parsed : []).filter(s => s && s.id && !seedIds.has(s.id) && !s.id.startsWith('student_'));
          students = [...students, ...customExtra];
        } catch (e) {
          students = seedStudents;
        }
      } else {
        students = seedStudents;
      }
      localStorage.setItem('haku_students', JSON.stringify(students));

      // Initialize per-student exact tab card mappings
      const CLASS_FOLDER_ID = 'folder_class_words';
      const CLASS_FOLDER_NAME = '授業で習った言葉';

      const STUDENT_DOC_RANGES = {
        '0012': [1, 289],      // みどりさん (289語 + 1追加語)
        '0011': [290, 498],    // Keyvinさん (209語)
        '0013': [499, 538],    // ななさん (40語)
        '0014': [539, 639],    // Danielさん (101語)
        '0015': [640, 873],    // Stephenさん (234語)
        '0016': [874, 1144],   // ジウンさん (271語)
        '0017': [1145, 1213],  // ハンウさん (69語)
        '0018': [1214, 1232],  // Justinさん (19語)
        '0019': [1233, 1314],  // ミンギさん (82語)
        '0020': [1315, 1397],  // Colinさん (83語)
        '0021': [1398, 1598],  // ともやさん (201語)
        '0022': [1599, 1602]   // 生徒22 (追加語彙)
      };

      const allStudentIds = Array.from(new Set([
        ...Object.keys(STUDENT_DOC_RANGES),
        ...students.map(s => s.id),
        '0027',
        '0028',
        '0023',
        '0013',
        '0010',
        'guest'
      ]));
      allStudentIds.forEach(stId => {
        const key = `haku_mylist_${stId}`;
        const foldersKey = `haku_mylist_folders_${stId}`;
        const mapKey = `haku_mylist_card_map_${stId}`;

        // Ensure "授業で習った言葉" folder exists
        let stFolders = [];
        try { stFolders = JSON.parse(localStorage.getItem(foldersKey) || '[]'); } catch (e) { stFolders = []; }
        if (!stFolders.find(f => f.id === CLASS_FOLDER_ID)) {
          stFolders.unshift({ id: CLASS_FOLDER_ID, name: CLASS_FOLDER_NAME });
          localStorage.setItem(foldersKey, JSON.stringify(stFolders));
        }
        // Preserve all existing student cards and add all tagged class words (Non-destructive union)
        let stSet = [];
        try { stSet = JSON.parse(localStorage.getItem(key) || '[]'); } catch (e) { stSet = []; }
        let stMap = {};
        try { stMap = JSON.parse(localStorage.getItem(mapKey) || '{}'); } catch (e) { stMap = {}; }
        if (!stMap || typeof stMap !== 'object' || Array.isArray(stMap)) stMap = {};

        const cleanedStudentIds = (Array.isArray(stSet) ? stSet : [])
          .map(x => (x && typeof x === 'object' && typeof x.id === 'string') ? x.id : x)
          .filter(x => typeof x === 'string');
        const finalStudentSet = new Set(cleanedStudentIds);
        const studentCardIds = new Set();

        // 1. Auto-discover all cards tagged for this student from CLASS_VOCAB_DATA
        (window.CLASS_VOCAB_DATA || []).forEach(c => {
          if (c && c.id && (c.studentId === stId || (Array.isArray(c.studentIds) && c.studentIds.includes(stId)))) {
            studentCardIds.add(c.id);
          }
        });

        // 2. Legacy student doc ranges fallback
        const range = STUDENT_DOC_RANGES[stId];
        if (range) {
          const [startNum, endNum] = range;
          for (let num = startNum; num <= endNum; num++) {
            studentCardIds.add(`class_word_${String(num).padStart(4, '0')}`);
          }
        }

        // 3. Fallbacks for curated cards
        if (stId === '0028') {
          finalStudentSet.forEach(id => {
            if (typeof id === 'string' && id.startsWith('card_') && !id.startsWith('class_word_0028_')) {
              finalStudentSet.delete(id);
              delete stMap[id];
            }
          });
          const ids0028 = window.CLASS_0028_IDS || (window.CLASS_VOCAB_DATA || []).filter(c => c && c.studentId === '0028').map(c => c.id);
          ids0028.forEach(cId => {
            studentCardIds.add(cId);
            finalStudentSet.add(cId);
            stMap[cId] = CLASS_FOLDER_ID;
          });
        }
        if (stId === '0027') {
          finalStudentSet.forEach(id => {
            if (typeof id === 'string' && id.startsWith('card_') && !id.startsWith('class_word_0027_')) {
              finalStudentSet.delete(id);
              delete stMap[id];
            }
          });
          const ids0027 = window.CLASS_0027_IDS || (window.CLASS_VOCAB_DATA || []).filter(c => c && c.studentId === '0027').map(c => c.id);
          ids0027.forEach(cId => {
            studentCardIds.add(cId);
            finalStudentSet.add(cId);
            stMap[cId] = CLASS_FOLDER_ID;
          });
        }"""

assert old_migration in code, "old_migration not found"
code = code.replace(old_migration, new_migration)

# 5. Update students restoration after migration block
old_saved_students = """    const savedStudents = localStorage.getItem('haku_students');
    if (savedStudents) {
      try {
        students = JSON.parse(savedStudents);
      } catch (e) {
        students = window.INITIAL_STUDENTS || [];
      }
    } else {
      students = window.INITIAL_STUDENTS || [];
    }

    // Load active student session if stored
    const savedStudentId = localStorage.getItem('haku_current_student_id');
    if (savedStudentId) {
      const found = students.find(s => s.id === savedStudentId);
      if (found) {
        setStudent(found);
      }
    }"""

new_saved_students = """    const activeSeedStudents = (window.AppAuth && typeof window.AppAuth.getStudents === 'function') 
      ? window.AppAuth.getStudents() 
      : (window.INITIAL_STUDENTS || []);
    const savedStudents = localStorage.getItem('haku_students');
    if (savedStudents) {
      try {
        const parsed = JSON.parse(savedStudents);
        const savedMap = new Map((Array.isArray(parsed) ? parsed : []).map(s => [s.id, s]));
        students = activeSeedStudents.map(seed => {
          const saved = savedMap.get(seed.id);
          return saved ? { ...seed, ...saved } : seed;
        });
        const seedIds = new Set(activeSeedStudents.map(s => s.id));
        const customExtra = (Array.isArray(parsed) ? parsed : []).filter(s => s && s.id && !seedIds.has(s.id) && !s.id.startsWith('student_'));
        students = [...students, ...customExtra];
      } catch (e) {
        students = activeSeedStudents;
      }
    } else {
      students = activeSeedStudents;
    }

    // Load active student session if stored
    const savedStudentId = localStorage.getItem('haku_current_student_id');
    if (savedStudentId) {
      const found = students.find(s => s.id === savedStudentId) || (window.AppAuth && window.AppAuth.getStudents().find(s => s.id === savedStudentId));
      if (found) {
        setStudent(found);
      }
    }"""

assert old_saved_students in code, "old_saved_students not found"
code = code.replace(old_saved_students, new_saved_students)

# 6. Update loadMylistForCurrentStudent with explicit 0027 and 0028 blocks
old_curated_student_branches = """    } else if (studentPrefix === '0010' && typeof ELIIE_CURATED_CARDS !== 'undefined') {
      let needsSave = false;
      ELIIE_NEW_CARD_IDS.forEach(cId => {
        if (!mylistSet.has(cId)) {
          mylistSet.add(cId);
          needsSave = true;
        }
        if (!mylistCardFolderMap[cId]) {
          mylistCardFolderMap[cId] = CLASS_FOLDER_ID;
          needsSave = true;
        }
      });
      if (needsSave) {
        localStorage.setItem(key, JSON.stringify(Array.from(mylistSet)));
        localStorage.setItem(mapKey, JSON.stringify(mylistCardFolderMap));
      }
    }"""

new_curated_student_branches = """    } else if (studentPrefix === '0010' && typeof ELIIE_CURATED_CARDS !== 'undefined') {
      let needsSave = false;
      ELIIE_NEW_CARD_IDS.forEach(cId => {
        if (!mylistSet.has(cId)) {
          mylistSet.add(cId);
          needsSave = true;
        }
        if (!mylistCardFolderMap[cId]) {
          mylistCardFolderMap[cId] = CLASS_FOLDER_ID;
          needsSave = true;
        }
      });
      if (needsSave) {
        localStorage.setItem(key, JSON.stringify(Array.from(mylistSet)));
        localStorage.setItem(mapKey, JSON.stringify(mylistCardFolderMap));
      }
    } else if (studentPrefix === '0027') {
      let needsSave = false;
      const ids0027 = window.CLASS_0027_IDS || (window.CLASS_VOCAB_DATA || []).filter(c => c && c.studentId === '0027').map(c => c.id);
      Array.from(mylistSet).forEach(cId => {
        if (typeof cId !== 'string' || (cId.startsWith('card_') && !cId.startsWith('class_word_0027_'))) {
          mylistSet.delete(cId);
          delete mylistCardFolderMap[cId];
          needsSave = true;
        }
      });
      ids0027.forEach(cId => {
        if (!mylistSet.has(cId)) {
          mylistSet.add(cId);
          needsSave = true;
        }
        if (!mylistCardFolderMap[cId]) {
          mylistCardFolderMap[cId] = CLASS_FOLDER_ID;
          needsSave = true;
        }
      });
      if (needsSave) {
        localStorage.setItem(key, JSON.stringify(Array.from(mylistSet)));
        localStorage.setItem(mapKey, JSON.stringify(mylistCardFolderMap));
      }
    } else if (studentPrefix === '0028') {
      let needsSave = false;
      const ids0028 = window.CLASS_0028_IDS || (window.CLASS_VOCAB_DATA || []).filter(c => c && c.studentId === '0028').map(c => c.id);
      Array.from(mylistSet).forEach(cId => {
        if (typeof cId !== 'string' || (cId.startsWith('card_') && !cId.startsWith('class_word_0028_'))) {
          mylistSet.delete(cId);
          delete mylistCardFolderMap[cId];
          needsSave = true;
        }
      });
      ids0028.forEach(cId => {
        if (!mylistSet.has(cId)) {
          mylistSet.add(cId);
          needsSave = true;
        }
        if (!mylistCardFolderMap[cId]) {
          mylistCardFolderMap[cId] = CLASS_FOLDER_ID;
          needsSave = true;
        }
      });
      if (needsSave) {
        localStorage.setItem(key, JSON.stringify(Array.from(mylistSet)));
        localStorage.setItem(mapKey, JSON.stringify(mylistCardFolderMap));
      }
    }"""

assert old_curated_student_branches in code, "old_curated_student_branches not found"
code = code.replace(old_curated_student_branches, new_curated_student_branches)

# 7. Update deduplication scores in loadMylistForCurrentStudent
old_score_func = """        const getScore = (id, c) => {
          if ((typeof MIDORI_NEW_CARD_IDS !== 'undefined' && MIDORI_NEW_CARD_IDS.includes(id)) ||
              (typeof DANIEL_NEW_CARD_IDS !== 'undefined' && DANIEL_NEW_CARD_IDS.includes(id)) ||
              (typeof ELIIE_NEW_CARD_IDS !== 'undefined' && ELIIE_NEW_CARD_IDS.includes(id))) return 1000;
          if (id && id.startsWith('card_')) {
            const exLen = (c && c.example && c.example.ja) ? c.example.ja.length : 0;
            return 600 + exLen;
          }
          if (id && id.startsWith('class_word_')) {
            const exLen = (c && c.example && c.example.ja) ? c.example.ja.length : 0;
            return 500 + exLen;
          }
          if (id && id.startsWith('seed_')) return 400;
          let s = 100;
          if (c && c.example && c.example.ja && !c.example.ja.includes('(')) s += 50;
          return s;
        };"""

new_score_func = """        const getScore = (id, c) => {
          if (id && (id.startsWith('class_word_0027_') || id.startsWith('class_word_0028_'))) return 3000;
          if ((typeof MIDORI_NEW_CARD_IDS !== 'undefined' && MIDORI_NEW_CARD_IDS.includes(id)) ||
              (typeof DANIEL_NEW_CARD_IDS !== 'undefined' && DANIEL_NEW_CARD_IDS.includes(id)) ||
              (typeof ELIIE_NEW_CARD_IDS !== 'undefined' && ELIIE_NEW_CARD_IDS.includes(id))) return 2000;
          if (id && id.startsWith('class_word_')) {
            const exLen = (c && c.example && c.example.ja) ? c.example.ja.length : 0;
            return 1500 + exLen;
          }
          if (id && id.startsWith('card_')) {
            const exLen = (c && c.example && c.example.ja) ? c.example.ja.length : 0;
            return 600 + exLen;
          }
          if (id && id.startsWith('seed_')) return 400;
          let s = 100;
          if (c && c.example && c.example.ja && !c.example.ja.includes('(')) s += 50;
          return s;
        };"""

assert old_score_func in code, "old_score_func not found"
code = code.replace(old_score_func, new_score_func)

# Also update the same deduplication score in syncStudentFromCloud if present
old_cloud_score = """            const getScore = (id, c) => {
              if ((typeof MIDORI_NEW_CARD_IDS !== 'undefined' && MIDORI_NEW_CARD_IDS.includes(id)) ||
                  (typeof DANIEL_NEW_CARD_IDS !== 'undefined' && DANIEL_NEW_CARD_IDS.includes(id)) ||
                  (typeof ELIIE_NEW_CARD_IDS !== 'undefined' && ELIIE_NEW_CARD_IDS.includes(id))) return 1000;
              if (id && id.startsWith('card_')) return 600 + ((c && c.example && c.example.ja) ? c.example.ja.length : 0);
              if (id && id.startsWith('class_word_')) return 500 + ((c && c.example && c.example.ja) ? c.example.ja.length : 0);
              if (id && id.startsWith('seed_')) return 400;
              return 100;
            };"""

new_cloud_score = """            const getScore = (id, c) => {
              if (id && (id.startsWith('class_word_0027_') || id.startsWith('class_word_0028_'))) return 3000;
              if ((typeof MIDORI_NEW_CARD_IDS !== 'undefined' && MIDORI_NEW_CARD_IDS.includes(id)) ||
                  (typeof DANIEL_NEW_CARD_IDS !== 'undefined' && DANIEL_NEW_CARD_IDS.includes(id)) ||
                  (typeof ELIIE_NEW_CARD_IDS !== 'undefined' && ELIIE_NEW_CARD_IDS.includes(id))) return 2000;
              if (id && id.startsWith('class_word_')) return 1500 + ((c && c.example && c.example.ja) ? c.example.ja.length : 0);
              if (id && id.startsWith('card_')) return 600 + ((c && c.example && c.example.ja) ? c.example.ja.length : 0);
              if (id && id.startsWith('seed_')) return 400;
              return 100;
            };"""

if old_cloud_score in code:
    code = code.replace(old_cloud_score, new_cloud_score)

# 8. Check CLASS_VOCAB_DATA FIRST in getCardById
old_get_card_by_id = """  function getCardById(cardId) {
    if (!cardId) return null;
    if (typeof MIDORI_CURATED_CARDS !== 'undefined') {
      const mCurated = MIDORI_CURATED_CARDS.find(c => c.id === cardId || c.word === cardId);
      if (mCurated) return mCurated;
    }
    if (typeof DANIEL_CURATED_CARDS !== 'undefined') {
      const dCurated = DANIEL_CURATED_CARDS.find(c => c.id === cardId || c.word === cardId);
      if (dCurated) return dCurated;
    }
    if (typeof ELIIE_CURATED_CARDS !== 'undefined') {
      const eCurated = ELIIE_CURATED_CARDS.find(c => c.id === cardId || c.word === cardId);
      if (eCurated) return eCurated;
    }
    if (typeof ARUN_CURATED_CARDS !== 'undefined') {
      const aCurated = ARUN_CURATED_CARDS.find(c => c.id === cardId || c.word === cardId);
      if (aCurated) return aCurated;
    }
    // 1. Check current in-memory vocabList"""

new_get_card_by_id = """  function getCardById(cardId) {
    if (!cardId) return null;
    // 0. Check CLASS_VOCAB_DATA first for curated accuracy & official translations
    if (window.CLASS_VOCAB_DATA && Array.isArray(window.CLASS_VOCAB_DATA)) {
      const cCard = window.CLASS_VOCAB_DATA.find(c => c && (c.id === cardId || c.word === cardId));
      if (cCard) return cCard;
    }
    if (typeof MIDORI_CURATED_CARDS !== 'undefined') {
      const mCurated = MIDORI_CURATED_CARDS.find(c => c.id === cardId || c.word === cardId);
      if (mCurated) return mCurated;
    }
    if (typeof DANIEL_CURATED_CARDS !== 'undefined') {
      const dCurated = DANIEL_CURATED_CARDS.find(c => c.id === cardId || c.word === cardId);
      if (dCurated) return dCurated;
    }
    if (typeof ELIIE_CURATED_CARDS !== 'undefined') {
      const eCurated = ELIIE_CURATED_CARDS.find(c => c.id === cardId || c.word === cardId);
      if (eCurated) return eCurated;
    }
    if (typeof ARUN_CURATED_CARDS !== 'undefined') {
      const aCurated = ARUN_CURATED_CARDS.find(c => c.id === cardId || c.word === cardId);
      if (aCurated) return aCurated;
    }
    // 1. Check current in-memory vocabList"""

assert old_get_card_by_id in code, "old_get_card_by_id not found"
code = code.replace(old_get_card_by_id, new_get_card_by_id)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(code)

pub_path = '/Users/yamauchimiku/Documents/GitHub/japanese-learning/public/js/app.js'
shutil.copy2(app_path, pub_path)
print("Updated js/app.js and synced to public/js/app.js successfully!")
