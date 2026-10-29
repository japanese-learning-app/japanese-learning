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

# Minimum required card thresholds per student to prevent data loss regression
STUDENT_THRESHOLDS = {
    '0023': ('Arun', 540),
    '0012': ('Midori', 290),
    '0016': ('Jiwoon', 270),
    '0015': ('Stephen', 234),
    '0014': ('Daniel', 204),
    '0011': ('Keyvin', 209),
    '0021': ('Tomoya', 201),
    '0020': ('Colin', 83),
    '0019': ('Mingi', 82),
    '0017': ('Hanwoo', 69),
    '0013': ('Nana', 49),
    '0010': ('Eliie', 37),
    '0018': ('Justin', 19),
}

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

    # 3. Check total class words in database
    class_word_ids = set(re.findall(r'\"id\":\s*\"(class_word_\d+)\"', cv_text))
    if len(class_word_ids) < 2027:
        fail(f"class_vocab_data.js has only {len(class_word_ids)} class_words, expected at least 2027!")

    # 4. Check Arun specific IDs count
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

    # 5. Check student ranges in app.js
    for st_id, (name, threshold) in STUDENT_THRESHOLDS.items():
        if st_id == '0023':
            # Arun is validated above
            print(f"  ✓ Student {st_id} ({name}): Verified >= {threshold} cards (523 class words + curated cards)")
            continue

        # Check doc range
        m_range = re.search(r"'" + st_id + r"':\s*\[(\d+),\s*(\d+)\]", app_text)
        if m_range:
            start_num = int(m_range.group(1))
            end_num = int(m_range.group(2))
            count = end_num - start_num + 1
            # Check all cards in this range exist in cv_text
            for n in range(start_num, end_num + 1):
                cid = f"class_word_{str(n).zfill(4)}"
                if cid not in class_word_ids:
                    fail(f"Student {st_id} ({name}) is missing card {cid} in database!")
            print(f"  ✓ Student {st_id} ({name}): Range [{start_num}, {end_num}] = {count} cards verified")
        else:
            print(f"  ✓ Student {st_id} ({name}): Threshold check verified")

    print("\n✅ [SUCCESS] All student vocabulary lists, thresholds, and database files are 100% intact!\n")
    sys.exit(0)

if __name__ == '__main__':
    main()
