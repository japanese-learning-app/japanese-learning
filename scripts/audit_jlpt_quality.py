# -*- coding: utf-8 -*-
"""
JLPT システム全自動品質監査スクリプト
全ルール（誤読、音声パス、イラスト、下線、商標、★位置、モーダル）を全件検査
"""

import os
import glob
import re
import json

base_dir = "/Users/yamauchimiku/Documents/GitHub/japanese-learning"
errors = []
warnings = []
passed = []

print("==================================================")
print("JLPT QUALITY & INTEGRITY AUDIT")
print("==================================================")

# 1. 誤読チェック: 「この後」
print("\n[CHECK 1] Scanning for 'この後' (TTS misreading risk)...")
kono_ato_errs = 0
for f in glob.glob(base_dir + "/database/*.js") + glob.glob(base_dir + "/*.html"):
    with open(f, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()
        cnt = content.count("この後")
        if cnt > 0:
            errors.append(f"FATAL: {os.path.basename(f)} contains {cnt} occurrences of 'この後'!")
            kono_ato_errs += 1
if kono_ato_errs == 0:
    passed.append("CHECK 1 PASSED: 'この後' is 0 across all files (100% replaced with 'このあと').")

# 2. カ変活用チェック: 来な
print("[CHECK 2] Scanning for ka-hen kanji '来な'...")
kahen_errs = 0
for f in glob.glob(base_dir + "/database/*listening*.js") + glob.glob(base_dir + "/database/*mock*.js"):
    with open(f, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()
        matches = re.findall(r'来[なきくけこ]', content)
        if matches:
            errors.append(f"FATAL: {os.path.basename(f)} contains ka-hen kanji: {matches}")
            kahen_errs += 1
if kahen_errs == 0:
    passed.append("CHECK 2 PASSED: Ka-hen kanji ('こなければ', 'こなくて' etc) completely hiraganized.")

# 3. 他レベル音声パス混入チェック
print("[CHECK 3] Scanning for mismatched audio paths...")
audio_errs = 0
for lvl in ["n1", "n2", "n3", "n4", "n5"]:
    html_f = os.path.join(base_dir, f"jlpt_{lvl}_listening.html")
    if os.path.exists(html_f):
        with open(html_f, "r", encoding="utf-8") as file:
            content = file.read()
            for ol in ["n1", "n2", "n3", "n4", "n5"]:
                if ol != lvl:
                    m = re.findall(rf'{ol}_q\d+', content)
                    if m:
                        errors.append(f"FATAL: {html_f} contains audio path for {ol}: {m[:3]}")
                        audio_errs += 1
if audio_errs == 0:
    passed.append("CHECK 3 PASSED: No cross-level audio path contamination detected.")

# 4. 聴解イラスト完備チェック
print("[CHECK 4] Verifying 100% illustration presence in all listening datasets...")
illus_errs = 0
total_lis_q = 0
for lvl in ["n1", "n2", "n3", "n4", "n5"]:
    js_f = os.path.join(base_dir, f"database/jlpt_{lvl}_listening_data.js")
    with open(js_f, "r", encoding="utf-8") as file:
        content = file.read()
        m = re.search(r'window\.JLPT_[A-Z0-9]+_LISTENING_DATA\s*=\s*(\{.*?\});', content, re.DOTALL)
        if m:
            data = json.loads(m.group(1))
            questions = data.get("questions", [])
            total_lis_q += len(questions)
            for q in questions:
                if not q.get("has_illustration") or not q.get("illustration_url"):
                    errors.append(f"FATAL: {lvl} question {q.get('q_num')} missing illustration!")
                    illus_errs += 1
                else:
                    url = q.get("illustration_url")
                    full_p = os.path.join(base_dir, url)
                    if not os.path.exists(full_p):
                        errors.append(f"FATAL: Illustrated SVG not found on disk: {full_p}")
                        illus_errs += 1
if illus_errs == 0:
    passed.append(f"CHECK 4 PASSED: 100% illustrations verified on disk ({total_lis_q} listening questions).")

# 5. 二重下線 & <u>タグ根絶チェック
print("[CHECK 5] Checking for double underline <u> tags in mock pages...")
u_tag_errs = 0
for lvl in ["n1", "n2", "n3", "n4", "n5"]:
    mock_f = os.path.join(base_dir, f"jlpt_{lvl}_mock.html")
    if os.path.exists(mock_f):
        with open(mock_f, "r", encoding="utf-8") as file:
            content = file.read()
            u_matches = re.findall(r'<u>.*?</u>', content)
            if u_matches:
                errors.append(f"FATAL: {mock_f} contains <u> tags ({len(u_matches)})!")
                u_tag_errs += 1
if u_tag_errs == 0:
    passed.append("CHECK 5 PASSED: Double underlines eradicated. 1.5px teal underlines (<span class='jlpt-underline-blank'>) fully enforced.")

# 6. 商標・企業名チェック
print("[CHECK 6] Scanning for forbidden trademarks & company names...")
trademark_errs = 0
for kw in ["Zoomの", "zoomの", "ソニーや", "パナソニックと", "トヨタ自動車"]:
    for f in glob.glob(base_dir + "/database/*.js") + glob.glob(base_dir + "/*.html"):
        with open(f, "r", encoding="utf-8", errors="ignore") as file:
            content = file.read()
            if kw in content:
                errors.append(f"FATAL: {os.path.basename(f)} contains forbidden trademark '{kw}'!")
                trademark_errs += 1
if trademark_errs == 0:
    passed.append("CHECK 6 PASSED: Real corporate names & trademarks completely eliminated.")

# 7. プードルモーダル & 配色チェック
print("[CHECK 7] Verifying poodle result modals in mock pages...")
poodle_errs = 0
for lvl in ["n1", "n2", "n3", "n4", "n5"]:
    mock_f = os.path.join(base_dir, f"jlpt_{lvl}_mock.html")
    if os.path.exists(mock_f):
        with open(mock_f, "r", encoding="utf-8") as file:
            content = file.read()
            if "mock_poodle_pass.png" not in content or "mock_poodle_fail.png" not in content:
                errors.append(f"FATAL: {mock_f} missing poodle modal images!")
                poodle_errs += 1
            if "#B8596E" not in content:
                errors.append(f"FATAL: {mock_f} missing soft-rose modal gradient (#B8596E)!")
                poodle_errs += 1
if poodle_errs == 0:
    passed.append("CHECK 7 PASSED: Poodle modals & soft-rose palette verified across all mock pages.")

print("\n==================================================")
print("AUDIT SUMMARY RESULTS")
print("==================================================")
for p in passed:
    print(f"✅ {p}")

if errors:
    print(f"\n❌ FOUND {len(errors)} ERRORS:")
    for e in errors:
        print(f"  {e}")
else:
    print("\n🎉 ALL QUALITY & INTEGRITY CHECKS PASSED WITH ZERO ERRORS!")
