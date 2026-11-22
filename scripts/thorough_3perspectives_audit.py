# -*- coding: utf-8 -*-
"""
Thorough 3-Perspectives Audit:
1. Teacher Perspective (Double answers, grammar accuracy, consistency)
2. Student Perspective (Absurd/giveaway dummies, broken connections, ruby spoilers)
3. Native Perspective (Natural Japanese, weird situations, polyphonic kanji ruby misreadings)
"""
import glob, json, re, os

BASE_DIR = "/Users/yamauchimiku/.gemini/antigravity/scratch/japanese-flashcards"

print("=========================================================")
print("THOROUGH 3-PERSPECTIVES AUDIT (TEACHER, STUDENT, NATIVE)")
print("=========================================================")

# Collect all grammar and vocab quiz databases
grammar_files = sorted(glob.glob(os.path.join(BASE_DIR, "database/jlpt_n*_grammar_quiz_data.js")))
vocab_files = sorted(glob.glob(os.path.join(BASE_DIR, "database/jlpt_n*_vocab_quiz_data.js")))

# Lists of issues found
teacher_issues = []
student_issues = []
native_issues = []

# Known polyphonic kanji misreadings to check
# (regex pattern in ruby, explanation)
SUSPICIOUS_RUBY_PATTERNS = [
    (r'<ruby>方<rt>ほう</rt></ruby>ですか', '「〜方ですか」 should be かた'),
    (r'どなたの<ruby>方<rt>ほう</rt></ruby>', '「どなたの方」 should be かた'),
    (r'先生の<ruby>方<rt>ほう</rt></ruby>', '「先生の方」 should be かた'),
    (r'お客<ruby>様<rt>さま</rt></ruby>の<ruby>方<rt>ほう</rt></ruby>', '「お客様の方」 should be かた'),
    (r'<ruby>行<rt>い</rt></ruby>われ', '「行われ」 should be おこなわれ'),
    (r'<ruby>行<rt>い</rt></ruby>う', '「行う」 should be おこなう'),
    (r'<ruby>金<rt>きむ</rt></ruby>', '「金」 should NOT be きむ'),
    (r'<ruby>全<rt>ちょん</rt></ruby>', '「全」 should NOT be ちょん'),
    (r'<ruby>薄<rt>すすき</rt></ruby>', '「薄」 should NOT be すすき'),
    (r'<ruby>主<rt>あるじ</rt></ruby>成分', '「主成分」 should be しゅ'),
    (r'<ruby>好<rt>よしみ</rt></ruby>都合', '「好都合」 should be こう'),
    (r'<ruby>証<rt>あかし</rt></ruby>', '「証(接尾辞)」 should be しょう'),
    (r'<ruby>角<rt>つの</rt></ruby>を<ruby>曲<rt>ま</rt></ruby>が', '「角を曲がる」 should be かど'),
    (r'一日<rt>ついたち</rt>', '「一日(いちにち中)」 context check'),
    (r'一日<rt>いちにち</rt></ruby>に（', '「一日(ついたち)に」 context check'),
    (r'<ruby>中<rt>じゅう</rt></ruby>ですので', '「会議中ですので」 should be ちゅう'),
    (r'<ruby>中<rt>ちゅう</rt></ruby>に<ruby>降<rt>ふ</rt></ruby>っ', '「一日中に」 should be じゅう'),
    (r'<ruby>人気<rt>にんき</rt></ruby>のない', '「人気のない(道/夜道)」 should be ひとけ'),
]

# Sensitive / weird words that shouldn't appear in clean JLPT questions
WEIRD_SITUATION_PATTERNS = [
    (r'突き刺す', 'Violent / weird context: 突き刺す'),
    (r'ボールペンで', 'Check context of ボールペン'),
    (r'殺す', 'Violence: 殺す'),
    (r'死ね', 'Offensive: 死ね'),
    (r'殴る', 'Violence: 殴る'),
    (r'高いお金を払って', 'Unnatural Japanese: 高いお金を払って'),
]

# 1. GRAMMAR QUIZ AUDIT
for p in grammar_files:
    lvl = os.path.basename(p).split('_')[1].upper()
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    idx1 = c.find('=') + 1
    idx2 = c.rfind(']') + 1
    data = json.loads(c[idx1:idx2])
    
    for q in data:
        qid = q.get('id')
        gname = q.get('grammar', '')
        qst = q.get('question', '')
        qr = q.get('question_ruby', '')
        choices = q.get('choices', [])
        ans = q.get('answer')
        corr = q.get('correct_text', '')
        
        # Teacher checks
        if corr != choices[ans]:
            teacher_issues.append((lvl, 'Grammar', qid, gname, f"correct_text '{corr}' != choices[{ans}] '{choices[ans]}'"))
        if len(choices) != len(set(choices)):
            teacher_issues.append((lvl, 'Grammar', qid, gname, f"Duplicate choices: {choices}"))
        
        # Student checks (broken connections, obvious absurd dummy)
        # Check if choice starts with 'る' but preceding text doesn't end in dictionary-capable stem
        m_prec = re.search(r'([ぁ-んァ-ヶa-zA-Z0-9ー])\s*(?:【\s*】|[（\(]\s*[）\)])', qst)
        if m_prec:
            prec_char = m_prec.group(1)
            for ch in choices:
                if ch.startswith('る') and prec_char in ['け', 'せ', 'て', 'ね', 'へ', 'め', 'れ', 'え', 'ら', 'か', 'さ', 'た', 'な', 'は', 'ま', 'わ']:
                    student_issues.append((lvl, 'Grammar', qid, gname, f"Suspicious connection '{prec_char}' + '{ch}' in Q: {qst}"))

        # Native checks (suspicious rubies & weird contexts)
        full_text = f"{qst} {qr} {' '.join(choices)} {q.get('sentence_jp','')} {q.get('sentence_jp_ruby','')}"
        for pat, desc in SUSPICIOUS_RUBY_PATTERNS:
            if re.search(pat, full_text):
                native_issues.append((lvl, 'Grammar', qid, gname, f"{desc} in {full_text[:60]}..."))
        for pat, desc in WEIRD_SITUATION_PATTERNS:
            if re.search(pat, full_text):
                native_issues.append((lvl, 'Grammar', qid, gname, f"{desc} in Q: {qst}"))

# 2. VOCAB QUIZ AUDIT
for p in vocab_files:
    lvl = os.path.basename(p).split('_')[1].upper()
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    idx1 = c.find('=') + 1
    data = json.loads(c[idx1:].rstrip(';\n '))
    
    for q in data:
        qid = q.get('id')
        cat = q.get('category', '')
        tw = q.get('target_word', '')
        qst = q.get('question', '')
        qr = q.get('question_ruby', '')
        choices = q.get('choices', [])
        ch_ruby = q.get('choices_ruby', [])
        ans = q.get('answer')
        corr = q.get('correct_text', '')
        
        # Teacher checks
        if ans is None or ans < 0 or ans >= len(choices):
            teacher_issues.append((lvl, 'Vocab', qid, cat, f"Invalid answer index {ans}"))
        elif corr != choices[ans]:
            teacher_issues.append((lvl, 'Vocab', qid, cat, f"correct_text '{corr}' != choices[{ans}] '{choices[ans]}'"))
        if len(choices) != len(set(choices)):
            teacher_issues.append((lvl, 'Vocab', qid, cat, f"Duplicate choices: {choices}"))
        if not q.get('explanation') and cat not in ['漢字読み', '表記']:
            teacher_issues.append((lvl, 'Vocab', qid, cat, f"Empty explanation for non-reading/writing question: TW={tw}"))

        # Student checks
        if any(k in cat for k in ['語形成', '接頭', '接尾', '表記', '書き']):
            for cr in ch_ruby:
                if '<rt>' in cr:
                    student_issues.append((lvl, 'Vocab', qid, cat, f"Ruby spoiler in choices_ruby for {cat}: {cr}"))

        # Native checks
        full_text = f"{qst} {qr} {' '.join(choices)} {' '.join(ch_ruby)} {q.get('correct_text_ruby','')}"
        for pat, desc in SUSPICIOUS_RUBY_PATTERNS:
            if re.search(pat, full_text):
                native_issues.append((lvl, 'Vocab', qid, cat, f"{desc} in {full_text[:60]}..."))
        for pat, desc in WEIRD_SITUATION_PATTERNS:
            if re.search(pat, full_text):
                native_issues.append((lvl, 'Vocab', qid, cat, f"{desc} in Q: {qst}"))

print(f"\n--- TEACHER ISSUES ({len(teacher_issues)}) ---")
for t in teacher_issues[:20]:
    print(f"[{t[0]} {t[1]}] ID {t[2]} ({t[3]}): {t[4]}")

print(f"\n--- STUDENT ISSUES ({len(student_issues)}) ---")
for s in student_issues[:20]:
    print(f"[{s[0]} {s[1]}] ID {s[2]} ({s[3]}): {s[4]}")

print(f"\n--- NATIVE ISSUES ({len(native_issues)}) ---")
for n in native_issues[:20]:
    print(f"[{n[0]} {n[1]}] ID {n[2]} ({n[3]}): {n[4]}")

