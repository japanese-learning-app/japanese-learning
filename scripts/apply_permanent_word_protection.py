#!/usr/bin/env python3
import os
import re

APP_PATH = '/Users/yamauchimiku/Documents/GitHub/japanese-learning/js/app.js'
PUBLIC_APP_PATH = '/Users/yamauchimiku/Documents/GitHub/japanese-learning/public/js/app.js'

with open(APP_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Version Bump
old_ver = "const CURRENT_DATA_VERSION = 'v66_restore_arun_all_547_words';"
new_ver = "const CURRENT_DATA_VERSION = 'v67_permanent_future_word_protection';"
assert old_ver in content, "old_ver not found"
content = content.replace(old_ver, new_ver)

# 2. Permanent Custom Archive in initData()
old_custom_load = """    // Load and preserve ALL custom cards across all students (strictly excluding seed/curriculum cards)
    let allCustomCards = [];
    try {
      const fromAll = JSON.parse(localStorage.getItem('haku_all_custom_cards') || '[]');
      if (Array.isArray(fromAll)) {
        fromAll.forEach(c => {
          if (c && c.id && !seedCardMap.has(c.id) && c.section_num === undefined && isCustomCardId(c.id)) {
            allCustomCards.push(c);
          }
        });
      }
    } catch(e) {}"""

new_custom_load = """    // Load and preserve ALL custom cards across all students (strictly excluding seed/curriculum cards)
    let allCustomCards = [];
    try {
      const fromArchive = JSON.parse(localStorage.getItem('haku_permanent_custom_archive') || '[]');
      if (Array.isArray(fromArchive)) {
        fromArchive.forEach(c => {
          if (c && c.id && !seedCardMap.has(c.id) && c.section_num === undefined && isCustomCardId(c.id)) {
            allCustomCards.push(c);
          }
        });
      }
    } catch(e) {}
    try {
      const fromAll = JSON.parse(localStorage.getItem('haku_all_custom_cards') || '[]');
      if (Array.isArray(fromAll)) {
        fromAll.forEach(c => {
          if (c && c.id && !seedCardMap.has(c.id) && c.section_num === undefined && isCustomCardId(c.id)) {
            if (!allCustomCards.find(existing => existing.id === c.id)) {
              allCustomCards.push(c);
            }
          }
        });
      }
    } catch(e) {}"""
assert old_custom_load in content, "old_custom_load not found"
content = content.replace(old_custom_load, new_custom_load)

# Save to permanent custom archive as well in initData()
old_custom_save = "localStorage.setItem('haku_all_custom_cards', JSON.stringify(allCustomCards));"
new_custom_save = """localStorage.setItem('haku_all_custom_cards', JSON.stringify(allCustomCards));
    localStorage.setItem('haku_permanent_custom_archive', JSON.stringify(allCustomCards));"""
assert old_custom_save in content, "old_custom_save not found"
content = content.replace(old_custom_save, new_custom_save, 1)

# 3. Non-destructive union migration in initData() on version update
old_migration_pattern = re.compile(
    r"\s*// Clean previous class_word cards from this student's mylist.*?localStorage\.setItem\(mapKey, JSON\.stringify\(stMap\)\);",
    re.DOTALL
)

new_migration_code = """
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
        if (stId === '0023') {
          const arunIds = window.CLASS_ARUN_IDS || (typeof ARUN_CLASS_WORD_IDS !== 'undefined' ? ARUN_CLASS_WORD_IDS : []);
          arunIds.forEach(cId => studentCardIds.add(cId));
          if (typeof ARUN_NEW_CARD_IDS !== 'undefined') {
            ARUN_NEW_CARD_IDS.forEach(cId => studentCardIds.add(cId));
          }
        }
        if (stId === '0012') {
          studentCardIds.add('card_1791393927923_pd4xbi');
          if (typeof MIDORI_NEW_CARD_IDS !== 'undefined') {
            MIDORI_NEW_CARD_IDS.forEach(id => studentCardIds.add(id));
          }
        }
        if (stId === '0014' && typeof DANIEL_NEW_CARD_IDS !== 'undefined') {
          DANIEL_NEW_CARD_IDS.forEach(id => studentCardIds.add(id));
        }
        if (stId === '0010' && typeof ELIIE_NEW_CARD_IDS !== 'undefined') {
          ELIIE_NEW_CARD_IDS.forEach(id => studentCardIds.add(id));
        }

        // Add discovered cards and assign to class folder
        studentCardIds.forEach(cId => {
          finalStudentSet.add(cId);
          if (!stMap[cId]) {
            stMap[cId] = CLASS_FOLDER_ID;
          }
        });

        localStorage.setItem(key, JSON.stringify(Array.from(finalStudentSet)));
        localStorage.setItem(mapKey, JSON.stringify(stMap));"""

m_mig = old_migration_pattern.search(content)
assert m_mig, "old_migration_pattern not matched"
content = content[:m_mig.start()] + new_migration_code + content[m_mig.end():]

# 4. Auto-discovery in loadMylistFromStorage
old_load_anchor = """    } else if (studentPrefix === '0010' && typeof ELIIE_CURATED_CARDS !== 'undefined') {
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

new_load_anchor = old_load_anchor + """

    // Universal auto-discovery: ensure ANY card tagged with this student ID is included
    let autoDiscoveredAny = false;
    const allKnownClassCards = (window.CLASS_VOCAB_DATA || []).concat(vocabList || []);
    allKnownClassCards.forEach(c => {
      if (c && c.id && (c.studentId === studentPrefix || (Array.isArray(c.studentIds) && c.studentIds.includes(studentPrefix)))) {
        if (!mylistSet.has(c.id)) {
          mylistSet.add(c.id);
          autoDiscoveredAny = true;
        }
        if (!mylistCardFolderMap[c.id]) {
          mylistCardFolderMap[c.id] = CLASS_FOLDER_ID;
          autoDiscoveredAny = true;
        }
      }
    });
    if (autoDiscoveredAny) {
      localStorage.setItem(key, JSON.stringify(Array.from(mylistSet)));
      localStorage.setItem(mapKey, JSON.stringify(mylistCardFolderMap));
    }"""
assert old_load_anchor in content, "old_load_anchor not found"
content = content.replace(old_load_anchor, new_load_anchor, 1)

# 5. Safe additive union merge in syncStudentToCloudDirect
old_direct_sync = """          if (Array.isArray(dataToSync.customCards)) {
            try {
              const snap = await docRef.get();
              const cloudCards = (snap.exists && Array.isArray(snap.data().customCards)) ? snap.data().customCards : [];
              if (snap.exists && snap.data().wordNames) {
                dataToSync.wordNames = { ...snap.data().wordNames, ...(dataToSync.wordNames || {}) };
              }
              const haveIds = new Set(dataToSync.customCards.map(c => c.id));
              cloudCards.forEach(c => {
                if (c && c.id && !isStubCard(c) && !isCorruptedCard(c) && !haveIds.has(c.id)) {
                  dataToSync.customCards.push(c);
                  haveIds.add(c.id);
                }
              });
              dataToSync.customCards = dataToSync.customCards.filter(c => !isCorruptedCard(c));
            } catch (e) {}
          }"""

new_direct_sync = """          try {
            const snap = await docRef.get();
            if (snap.exists) {
              const cloudData = snap.data() || {};
              const cloudRemoved = new Set(Array.isArray(cloudData.removedIds) ? cloudData.removedIds : []);

              // Merge wordNames
              if (cloudData.wordNames) {
                dataToSync.wordNames = { ...cloudData.wordNames, ...(dataToSync.wordNames || {}) };
              }

              // Merge customCards
              const cloudCards = Array.isArray(cloudData.customCards) ? cloudData.customCards : [];
              if (Array.isArray(dataToSync.customCards)) {
                const haveIds = new Set(dataToSync.customCards.map(c => c.id));
                cloudCards.forEach(c => {
                  if (c && c.id && !isStubCard(c) && !isCorruptedCard(c) && !haveIds.has(c.id)) {
                    dataToSync.customCards.push(c);
                    haveIds.add(c.id);
                  }
                });
                dataToSync.customCards = dataToSync.customCards.filter(c => !isCorruptedCard(c));
              } else {
                dataToSync.customCards = cloudCards.filter(c => !isCorruptedCard(c));
              }

              // ★ 超重要: mylist 双方向結合マージ（ローカルの縮小や消滅でクラウドを上書きしない）
              if (Array.isArray(cloudData.mylist) && Array.isArray(dataToSync.mylist)) {
                const mergedMylist = new Set(cloudData.mylist.filter(id => !cloudRemoved.has(id)));
                dataToSync.mylist.forEach(id => {
                  if (!cloudRemoved.has(id)) mergedMylist.add(id);
                });
                dataToSync.mylist = Array.from(mergedMylist);
              }

              // Merge cardFolderMap
              if (cloudData.cardFolderMap && typeof dataToSync.cardFolderMap === 'object') {
                dataToSync.cardFolderMap = { ...cloudData.cardFolderMap, ...dataToSync.cardFolderMap };
              }

              // Merge folders
              if (Array.isArray(cloudData.folders) && Array.isArray(dataToSync.folders)) {
                const folderIds = new Set(dataToSync.folders.map(f => f.id));
                cloudData.folders.forEach(f => {
                  if (f && f.id && !folderIds.has(f.id)) {
                    dataToSync.folders.push(f);
                    folderIds.add(f.id);
                  }
                });
              }
            }
          } catch (e) {
            console.warn('Pre-push cloud direct merge note:', e);
          }"""
assert old_direct_sync in content, "old_direct_sync not found"
content = content.replace(old_direct_sync, new_direct_sync, 1)

# 6. Safe additive union merge in syncStudentToCloud
old_cloud_sync = """        try {
          const snap = await docRef.get();
          if (snap.exists && snap.data().wordNames) {
            mergeWordNames(snap.data().wordNames);
            wordNamesToSync = buildWordNamesFor(Array.from(mylistSet));
          }
          const cloudCards = (snap.exists && Array.isArray(snap.data().customCards)) ? snap.data().customCards : [];
          const haveIds = new Set(customCardsToSync.map(c => c.id));
          cloudCards.forEach(c => {
            if (c && c.id && !isStubCard(c) && !isCorruptedCard(c) && !haveIds.has(c.id) && mylistSet.has(c.id)) {
              customCardsToSync.push(c);
              haveIds.add(c.id);
            }
          });
        } catch (e) {}"""

new_cloud_sync = """        try {
          const snap = await docRef.get();
          if (snap.exists) {
            const cloudData = snap.data() || {};
            if (cloudData.wordNames) {
              mergeWordNames(cloudData.wordNames);
              wordNamesToSync = buildWordNamesFor(Array.from(mylistSet));
            }
            const cloudCards = Array.isArray(cloudData.customCards) ? cloudData.customCards : [];
            const haveIds = new Set(customCardsToSync.map(c => c.id));
            cloudCards.forEach(c => {
              if (c && c.id && !isStubCard(c) && !isCorruptedCard(c) && !haveIds.has(c.id) && mylistSet.has(c.id)) {
                customCardsToSync.push(c);
                haveIds.add(c.id);
              }
            });

            // ★ 超重要: クラウドの mylist を双方向結合マージ（クラウドの既存単語を絶対に消さない）
            const cloudRemoved = new Set(Array.isArray(cloudData.removedIds) ? cloudData.removedIds : []);
            if (Array.isArray(cloudData.mylist) && cloudData.mylist.length > 0) {
              let localAddedFromCloud = false;
              cloudData.mylist.forEach(id => {
                if (!cloudRemoved.has(id) && !mylistSet.has(id)) {
                  mylistSet.add(id);
                  localAddedFromCloud = true;
                }
              });
              if (localAddedFromCloud) {
                const stKey = `haku_mylist_${studentId}`;
                localStorage.setItem(stKey, JSON.stringify(Array.from(mylistSet)));
              }
            }
            if (cloudData.cardFolderMap && typeof cloudData.cardFolderMap === 'object') {
              mylistCardFolderMap = { ...cloudData.cardFolderMap, ...mylistCardFolderMap };
              const mapKey = `haku_mylist_card_map_${studentId}`;
              localStorage.setItem(mapKey, JSON.stringify(mylistCardFolderMap));
            }
          }
        } catch (e) {
          console.warn('Pre-push cloud merge note:', e);
        }"""
assert old_cloud_sync in content, "old_cloud_sync not found"
content = content.replace(old_cloud_sync, new_cloud_sync, 1)

# 7. Permanent archive & student tagging in importTSV
old_import_archive = """          try {
            const stored = JSON.parse(localStorage.getItem('haku_all_custom_cards') || '[]');
            const exIdx = stored.findIndex(c => c.id === newCard.id);
            if (exIdx >= 0) stored[exIdx] = newCard;
            else stored.push(newCard);
            localStorage.setItem('haku_all_custom_cards', JSON.stringify(stored));
          } catch (e) {}"""

new_import_archive = """          try {
            const stored = JSON.parse(localStorage.getItem('haku_all_custom_cards') || '[]');
            const exIdx = stored.findIndex(c => c.id === newCard.id);
            if (exIdx >= 0) stored[exIdx] = newCard;
            else stored.push(newCard);
            localStorage.setItem('haku_all_custom_cards', JSON.stringify(stored));

            // Permanent immutable local archive backup
            const archive = JSON.parse(localStorage.getItem('haku_permanent_custom_archive') || '[]');
            const exAIdx = archive.findIndex(c => c.id === newCard.id);
            if (exAIdx >= 0) archive[exAIdx] = newCard;
            else archive.push(newCard);
            localStorage.setItem('haku_permanent_custom_archive', JSON.stringify(archive));
          } catch (e) {}"""
assert old_import_archive in content, "old_import_archive not found"
content = content.replace(old_import_archive, new_import_archive, 1)

with open(APP_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

with open(PUBLIC_APP_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully applied permanent word protection to js/app.js and public/js/app.js!")
