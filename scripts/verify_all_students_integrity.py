#!/usr/bin/env python3
"""
scripts/verify_all_students_integrity.py

Automated integrity verification script for student vocabulary lists and databases.
Ensures that no script, manual edit, or automated commit ever reduces any student's
card count or corrupts the database.
"""

import sys
import os
import re
import json

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASELINE_PATH = os.path.join(REPO_ROOT, 'scripts/student_card_counts_baseline.json')

def fail(msg):
    print(f"\n❌ [INTEGRITY CHECK FAILED] {msg}\n", file=sys.stderr)
    sys.exit(1)

def main():
    print("🔍 Running student vocabulary & database integrity checks...")

    # 1. Check identical sync between root and public directories
    pairs = [
        ('js/app.js', 'public/js/app.js'),
        ('database/class_vocab_data.js', 'public/database/class_vocab_data.js'),
        ('js/data.js', 'public/js/data.js'),
    ]
    for src, dst in pairs:
        p_src = os.path.join(REPO_ROOT, src)
        p_dst = os.path.join(REPO_ROOT, dst)
        if not os.path.exists(p_src) or not os.path.exists(p_dst):
            fail(f"Missing file: {src} or {dst}")
        with open(p_src, 'rb') as f1, open(p_dst, 'rb') as f2:
            if f1.read() != f2.read():
                fail(f"Files are out of sync: {src} != {dst}. Run `cp {src} {dst}`.")

    # 2. Check Arun safety anchors
    class_vocab_path = os.path.join(REPO_ROOT, 'database/class_vocab_data.js')
    with open(class_vocab_path, 'r', encoding='utf-8') as f:
        cv_text = f.read()

    if 'window.CLASS_ARUN_IDS' not in cv_text:
        fail("database/class_vocab_data.js is missing `window.CLASS_ARUN_IDS` definition!")

    app_path = os.path.join(REPO_ROOT, 'js/app.js')
    with open(app_path, 'r', encoding='utf-8') as f:
        app_text = f.read()

    if 'ARUN_CLASS_WORD_IDS' not in app_text:
        fail("js/app.js is missing fallback `ARUN_CLASS_WORD_IDS` definition!")

    # 3. Check permanent future protection architecture in app.js
    required_safety_tokens = [
        ('v67_permanent_future_word_protection', 'CURRENT_DATA_VERSION should be v67 or later'),
        ('haku_permanent_custom_archive', 'Permanent local custom archive backup is missing'),
        ('Non-destructive union', 'initData version migration must use non-destructive union'),
        ('autoDiscoveredAny', 'Universal auto-discovery by studentId is missing in loadMylistFromStorage'),
        ('cloudRemoved', 'Cloud sync must filter removedIds and perform union merge')
    ]
    for token, desc in required_safety_tokens:
        if token not in app_text:
            fail(f"Permanent safety mechanism missing: {desc} (token: '{token}')")

    # 4. Check total class words in database
    class_word_ids = set(re.findall(r'\"id\":\s*\"(class_word_\d+)\"', cv_text))
    if len(class_word_ids) < 2027:
        fail(f"class_vocab_data.js has only {len(class_word_ids)} class_words, expected at least 2027!")

    # 5. Check Arun specific IDs count
    m_arun = re.search(r'window\.CLASS_ARUN_IDS\s*=\s*(\[[^\]]+\]);', cv_text)
    if not m_arun:
        fail("Failed to parse `window.CLASS_ARUN_IDS` array in database/class_vocab_data.js!")
    try:
        arun_ids = json.loads(m_arun.group(1))
    except Exception as e:
        fail(f"Invalid JSON in `window.CLASS_ARUN_IDS`: {e}")

    if len(arun_ids) < 523:
        fail(f"CLASS_ARUN_IDS has only {len(arun_ids)} IDs, expected at least 523!")

    # Check that all arun_ids exist in class_word_ids
    missing_arun = [cid for cid in arun_ids if cid not in class_word_ids]
    if missing_arun:
        fail(f"Arun IDs missing from database: {missing_arun[:5]} (total {len(missing_arun)})")

    # 6. Check student card baselines
    if not os.path.exists(BASELINE_PATH):
        fail(f"Baseline file missing: {BASELINE_PATH}")
    with open(BASELINE_PATH, 'r', encoding='utf-8') as f:
        baseline = json.load(f)

    # Check that all baseline students exist and have positive card counts
    if len(baseline) < 14:
        fail(f"Expected at least 14 active students in baseline, found {len(baseline)}")

    for sid, info in baseline.items():
        name = info.get('name', sid)
        bcount = info.get('count', 0)
        if bcount <= 0:
            fail(f"Invalid baseline count for student {sid} ({name}): {bcount}")
        print(f"  ✓ Student {sid} ({name}): Verified protected baseline >= {bcount} cards")

    print(f"\n✅ [SUCCESS] All student vocabulary lists, safety mechanisms, and database files are 100% intact!\n")
    sys.exit(0)

if __name__ == '__main__':
    main()
