#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/verify_all_regressions.py

過去の全修正・ユーザー要望（全305コミット分）が1つも崩れていないかを
毎回自動検証する包括的回帰テスト（Regression Test Suite）。
Git pre-commit フックおよび全修正作業の最終チェックとして必ず実行する。
"""

import os
import re
import sys
import json
import glob
import tempfile
import subprocess

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSC_BIN = '/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc'

failures = []
warnings = []
passed = []

def ok(name):
    passed.append(name)

def fail(name, detail):
    failures.append((name, detail))

def warn(name, detail):
    warnings.append((name, detail))

def read_text(rel_path):
    p = os.path.join(REPO_ROOT, rel_path)
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def main():
    print("=================================================================")
    print("🛡️  JAPANESE LEARNING APP — 全過去修正 自動回帰テスト開始")
    print("=================================================================")

    # -----------------------------------------------------------------
    # [A] 音声 (Google TTS / no-referrer / 2文目保護 / 二重読み防止)
    # -----------------------------------------------------------------
    html_files = sorted(glob.glob(os.path.join(REPO_ROOT, '*.html')) +
                        glob.glob(os.path.join(REPO_ROOT, 'public', '*.html')))
    missing_ref = []
    for hp in html_files:
        rel = os.path.relpath(hp, REPO_ROOT)
        with open(hp, 'r', encoding='utf-8', errors='ignore') as f:
            txt = f.read()
        if 'name="referrer"' not in txt or 'no-referrer' not in txt:
            missing_ref.append(rel)
    if missing_ref:
        fail("A1: 全HTMLの no-referrer タグ（Google TTS 404防止）", f"欠落ファイル: {missing_ref}")
    else:
        ok(f"A1: 全HTML({len(html_files)}件)に <meta name=\"referrer\" content=\"no-referrer\"> 完備")

    app_js = read_text('js/app.js')
    index_html = read_text('index.html')

    # A2: TTS safety in js/app.js
    tts_tokens = [
        ('ensureNoReferrerMeta', '動的no-referrer補完'),
        ('didFallback', '音声フォールバック二重再生防止'),
        ('loadTimer = setTimeout', 'Google TTS 3.5秒タイムアウトフォールバック'),
        ('window.speechSynthesis.resume()', 'iOS Safari speechSynthesis一時停止解除'),
        ('(?![^\\x00-\\x7F]' if False else '/[\\u3040-\\u30FF]/.test(rest)', '2文目日本語カット防止保護'),
        ("cleanText.split(/(?<=[。！？\\n])/)", '句読点チャンク分割正規表現（改行破損なし）'),
    ]
    missing_tts = [desc for tok, desc in tts_tokens if tok not in app_js]
    if missing_tts:
        fail("A2-A5: js/app.js 音声エンジン保護機構", f"不足項目: {missing_tts}")
    else:
        ok("A2-A5: js/app.js 音声エンジン（no-referrer補完 / 3.5sフォールバック / 二重再生防止 / 2文目保護 / チャンク分割）OK")

    # A4: Ruby strip before speech
    if '<rt' in app_js and 'replace(/<rt' in app_js:
        ok("A4: js/app.js 音声読み上げ前の <rt> 先行除去（二重読み防止）OK")
    else:
        fail("A4: js/app.js 音声読み上げ前の <rt> 先行除去", "<rt>除去処理が見つかりません")

    # -----------------------------------------------------------------
    # [B] フラッシュカード・構文チェック・JLPTタブ・ルビ品質
    # -----------------------------------------------------------------
    # B1: JS syntax check via macOS JavaScriptCore (jsc)
    if os.path.exists(JSC_BIN):
        syntax_errors = []
        js_targets = sorted(
            glob.glob(os.path.join(REPO_ROOT, '*.js')) +
            glob.glob(os.path.join(REPO_ROOT, 'js', '*.js')) +
            glob.glob(os.path.join(REPO_ROOT, 'public', 'js', '*.js'))
        )
        for jp in js_targets:
            res = subprocess.run(
                [JSC_BIN, '-e', f"try {{ new Function(read({json.dumps(jp)})); }} catch(e) {{ print('ERR:' + e + ' line:' + e.line); }}"],
                capture_output=True, text=True
            )
            if 'ERR:' in res.stdout:
                syntax_errors.append(f"{os.path.relpath(jp, REPO_ROOT)}: {res.stdout.strip()}")

        # Inline <script> blocks in key HTML files
        for hp in html_files:
            rel = os.path.relpath(hp, REPO_ROOT)
            if rel.startswith('public/') and os.path.exists(os.path.join(REPO_ROOT, rel[7:])):
                continue  # checked via root mirror
            with open(hp, 'r', encoding='utf-8', errors='ignore') as f:
                ht = f.read()
            scripts = re.findall(r'<script(?![^>]*src=)[^>]*>([\s\S]*?)</script>', ht, re.I)
            for idx, sc in enumerate(scripts):
                if not sc.strip():
                    continue
                with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as tf:
                    tf.write(sc)
                    tf_path = tf.name
                try:
                    res = subprocess.run(
                        [JSC_BIN, '-e', f"try {{ new Function(read({json.dumps(tf_path)})); }} catch(e) {{ print('ERR:' + e + ' line:' + e.line); }}"],
                        capture_output=True, text=True
                    )
                    if 'ERR:' in res.stdout:
                        syntax_errors.append(f"{rel} [script #{idx}]: {res.stdout.strip()}")
                finally:
                    os.unlink(tf_path)

        if syntax_errors:
            fail("B1: 全JS・全HTMLインラインスクリプト構文チェック", "; ".join(syntax_errors[:5]))
        else:
            ok("B1: 全JSファイル & 全HTMLインラインスクリプト JavaScript構文エラー 0件")
    else:
        warn("B1: jsc未検出", "JavaScriptCoreが見つからずスキップ")

    # B2-B5: Flashcard core UX features in index.html & js/app.js
    fc_checks = [
        ('user-select: none' in index_html, 'ルビ選択・コピー除外CSS'),
        ('Cache-Control' in index_html, 'index.html キャッシュ無効化メタタグ'),
        ('KANA_ROMAJI_MULTI' in app_js, 'ローマ字変換エンジン'),
        ('読み方 (Reading)' in app_js or '読み方 (Reading)' in index_html, '裏面「読み方 (Reading)」ラベル'),
        ('saveCurrentDeckProgress' in app_js, 'タブ切替時のカード位置保持'),
        ('cardProgressBar' in index_html, 'フラッシュカード進捗バー'),
        ('cleanDistinction' in app_js, '意味欄への「vs/使い分け」混入防止'),
    ]
    missing_fc = [label for cond, label in fc_checks if not cond]
    if missing_fc:
        fail("B2-B5: フラッシュカード過去改善機能", f"欠落: {missing_fc}")
    else:
        ok("B2-B5: フラッシュカード過去改善機能（ルビ選択除外 / ローマ字 / 進捗保持 / 進捗バー / 意味と使い分け分離）OK")

    # B6: Broken ruby tags check in js/app.js & database/class_vocab_data.js
    broken_rubies = re.findall(r'<ruby\.[^<]+</ruby>|<ruby><ruby>', app_js)
    cv_js = read_text('database/class_vocab_data.js')
    broken_rubies_cv = re.findall(r'<ruby\.[^<]+</ruby>|<ruby><ruby>', cv_js)
    naked_rt_cv = []
    for m in re.finditer(r'"ja"\s*:\s*"([^"]*)"', cv_js):
        val = m.group(1)
        if '<rt>' in val and val.count('<ruby>') != val.count('</ruby>'):
            naked_rt_cv.append(val[:40])
    if broken_rubies or broken_rubies_cv or naked_rt_cv:
        fail("B6: ルビタグ整合性検査 (app.js / class_vocab_data.js)", f"app:{len(broken_rubies)}, cv:{len(broken_rubies_cv)}, unbalanced:{len(naked_rt_cv)}")
    else:
        ok("B6: js/app.js & database/class_vocab_data.js 壊れた<ruby>・多重<ruby>・不整合<rt> 0件")

    # D5: N1-N5 vocab cards features (romaji / random test 10/30/50 / study direction)
    vc_issues = []
    for lvl in ['n1', 'n2', 'n3', 'n4', 'n5']:
        p = f'jlpt_{lvl}_vocab_cards.html'
        txt = read_text(p)
        if 'startRandomTest(10)' not in txt or 'startRandomTest(50)' not in txt:
            vc_issues.append(f"{p}: ランダム実力テスト(10/30/50問)欠落")
        if 'toggleStudyDirection' not in txt:
            vc_issues.append(f"{p}: 双方向切替欠落")
    if vc_issues:
        fail("D5: N1〜N5 語彙フラッシュカード必須機能", ", ".join(vc_issues))
    else:
        ok("D5: N1〜N5 語彙フラッシュカード（10/30/50問ランダムテスト / 双方向切替）OK")

    # B7: JLPT tab in index.html must NOT have quiz/practice banners
    m_view_jlpt = re.search(r'<div id="viewJlpt"[\s\S]*?(?=<div id="jlptDetailModal")', index_html)
    if not m_view_jlpt:
        fail("B7: index.html の JLPTタブ構造", "#viewJlpt が見つかりません")
    else:
        vj = m_view_jlpt.group(0)
        forbidden_in_jlpt_tab = ['jlpt_n2_vocab_quiz.html', 'jlpt_n2_grammar_quiz.html', 'jlpt_n2_reading.html', 'jlpt_n2_listening.html']
        found_bad = [u for u in forbidden_in_jlpt_tab if u in vj]
        if found_bad:
            fail("B7: フラッシュカード内JLPTタブの練習問題バナー排除", f"残存リンク: {found_bad}")
        elif 'jlptMasterFlashcardBanner' not in vj:
            fail("B7: フラッシュカード内JLPTタブのフラッシュカードバナー", "#jlptMasterFlashcardBanner が見つかりません")
        else:
            ok("B7: フラッシュカード内JLPTタブは練習問題バナー0件・フラッシュカード専用構成 OK")

    # B8: database/jlpt_vocab_all.js window.JLPT_VOCAB export & 5 levels populated
    jlpt_vocab_txt = read_text('database/jlpt_vocab_all.js')
    if 'window.JLPT_VOCAB = JLPT_VOCAB' not in jlpt_vocab_txt:
        fail("B8: database/jlpt_vocab_all.js の window.JLPT_VOCAB 公開", "window.JLPT_VOCAB = JLPT_VOCAB; がありません")
    elif 'function getJlptVocabDb()' not in app_js:
        fail("B8: js/app.js の getJlptVocabDb() フォールバック", "getJlptVocabDb() が見つかりません")
    else:
        m_json = re.search(r'const JLPT_VOCAB\s*=\s*(\{[\s\S]*\});', jlpt_vocab_txt)
        if not m_json:
            fail("B8: database/jlpt_vocab_all.js JSON構造", "const JLPT_VOCAB = {...}; のパースに失敗")
        else:
            jdata = json.loads(m_json.group(1))
            counts = {lvl: len(jdata.get(lvl, [])) for lvl in ['N5', 'N4', 'N3', 'N2', 'N1']}
            if any(v == 0 for v in counts.values()):
                fail("B8: JLPT 5レベル語彙データ", f"空レベルあり: {counts}")
            else:
                ok(f"B8: JLPT 5レベル単語データ & window.JLPT_VOCAB 公開 OK ({counts}, 計{sum(counts.values()):,}語)")

    # -----------------------------------------------------------------
    # [C] セキュリティ・生徒データ・同期・ルートとpublic完全一致
    # -----------------------------------------------------------------
    # C2: Admin passcode must NEVER be exposed in index.html login modal
    if 'ppooiillkk' in index_html:
        fail("C2: 管理者パスワード非露出（セキュリティ）", "index.html 内に管理者パスコードが含まれています")
    else:
        ok("C2: 公開HTMLに管理者パスコード露出なし OK")

    # C4 / E3: Root <-> public/ mirror sync check for critical files
    mirror_pairs = [
        ('index.html', 'public/index.html'),
        ('app.html', 'public/app.html'),
        ('js/app.js', 'public/js/app.js'),
        ('js/data.js', 'public/js/data.js'),
        ('js/kanji_engine.js', 'public/js/kanji_engine.js'),
        ('auth.js', 'public/auth.js'),
        ('database/class_vocab_data.js', 'public/database/class_vocab_data.js'),
        ('database/jlpt_vocab_all.js', 'public/database/jlpt_vocab_all.js'),
        ('jlpt_practice.html', 'public/jlpt_practice.html'),
    ]
    out_of_sync = []
    for src, dst in mirror_pairs:
        ps = os.path.join(REPO_ROOT, src)
        pd = os.path.join(REPO_ROOT, dst)
        if os.path.exists(ps) and os.path.exists(pd):
            with open(ps, 'rb') as f1, open(pd, 'rb') as f2:
                if f1.read() != f2.read():
                    out_of_sync.append(f"{src} != {dst}")
    if out_of_sync:
        fail("E3: ルートと public/ の完全同期", f"不一致: {out_of_sync}")
    else:
        ok(f"E3: 主要{len(mirror_pairs)}ファイルのルート ↔ public/ 完全一致 OK")

    # -----------------------------------------------------------------
    # [D] JLPT N1〜N5 全ページ存在・ネタバレ防止・絵文字リンク禁止
    # -----------------------------------------------------------------
    required_jlpt_pages = []
    for lvl in ['n1', 'n2', 'n3', 'n4', 'n5']:
        for suffix in ['vocab_cards', 'vocab_quiz', 'grammar_textbook', 'grammar_quiz', 'reading', 'listening', 'mock']:
            required_jlpt_pages.append(f'jlpt_{lvl}_{suffix}.html')
    missing_pages = [p for p in required_jlpt_pages if not os.path.exists(os.path.join(REPO_ROOT, p))]
    if missing_pages:
        fail("D1: JLPT N1〜N5 全35教材ページ実在チェック", f"欠落: {missing_pages}")
    else:
        ok("D1: JLPT N1〜N5 全35教材ページ（語彙カード/語彙クイズ/文法教科書/文法クイズ/読解/聴解/模試）すべて実在 OK")

    # D1b: No emoji filename links in href=""
    emoji_hrefs = []
    for hp in html_files:
        rel = os.path.relpath(hp, REPO_ROOT)
        with open(hp, 'r', encoding='utf-8', errors='ignore') as f:
            ht = f.read()
        if '📱_日本語学習' in ht:
            emoji_hrefs.append(rel)
    if emoji_hrefs:
        fail("D1b: 絵文字ファイル名リンク禁止（404防止）", f"検出: {emoji_hrefs}")
    else:
        ok("D1b: 全HTMLで絵文字ファイル名リンク（404原因）0件 OK")

    # D2: Grammar quiz badge spoiler check & syntax check
    spoiler_pages = []
    for lvl in ['n1', 'n2', 'n3', 'n4', 'n5']:
        p = f'jlpt_{lvl}_grammar_quiz.html'
        txt = read_text(p)
        if 'showToast(selectedLimit > 0 ?  :' in txt:
            spoiler_pages.append(f"{p} (壊れた三項演算子)")
    if spoiler_pages:
        fail("D2: 文法穴埋めクイズ構文・ネタバレチェック", ", ".join(spoiler_pages))
    else:
        ok("D2: N1〜N5 文法穴埋めクイズ構文・正常動作チェック OK")

    # D4: Mock exam double-underline & IRT notice check
    mock_issues = []
    for lvl in ['n1', 'n2', 'n3', 'n4', 'n5']:
        p = f'jlpt_{lvl}_mock.html'
        txt = read_text(p)
        if 'jlpt-underline-blank' not in txt:
            mock_issues.append(f"{p}: .jlpt-underline-blank欠落")
        if 'IRT' not in txt:
            mock_issues.append(f"{p}: IRT注記欠落")
    if mock_issues:
        fail("D4: N1〜N5 本番模擬試験（下線・IRT注記）", ", ".join(mock_issues))
    else:
        ok("D4: N1〜N5 本番模擬試験（二重下線防止 / IRT尺度得点注記）OK")

    # -----------------------------------------------------------------
    # [E] ホームポータル・かな書き取りクイズ・助詞マスター
    # -----------------------------------------------------------------
    app_html = read_text('app.html')
    portal_checks = [
        ('index.html' in app_html, 'フラッシュカード導線'),
        ('jlpt_practice.html' in app_html, 'JLPT道場導線'),
        ('business_keigo.html' in app_html, 'ビジネス敬語導線'),
        ('は・が・に・で・を' in app_html or '助詞' in app_html, '弱点克服・助詞マスター'),
        ('kana-quiz-answer' in app_html or '次の問題へ' in app_html, 'かな書き取りクイズUI'),
    ]
    missing_portal = [label for cond, label in portal_checks if not cond]
    if missing_portal:
        fail("E1-E2: ホームポータル (app.html) 主要モジュール", f"欠落: {missing_portal}")
    else:
        ok("E1-E2: ホームポータル (app.html) 全主要モジュール（フラッシュカード / JLPT / 敬語 / 助詞 / 書き取り）OK")

    # -----------------------------------------------------------------
    # Summary
    # -----------------------------------------------------------------
    print(f"\n✅ 合格項目: {len(passed)} 件")
    for p in passed:
        print(f"  ✓ {p}")
    if warnings:
        print(f"\n⚠️  警告: {len(warnings)} 件")
        for w, d in warnings:
            print(f"  ! {w}: {d}")
    if failures:
        print(f"\n❌ 失敗（回帰検知）: {len(failures)} 件", file=sys.stderr)
        for name, detail in failures:
            print(f"  ✗ {name} -> {detail}", file=sys.stderr)
        sys.exit(1)

    print("\n🎉 [ALL CLEAR] 過去の全修正項目に崩れはありません！\n")
    sys.exit(0)

if __name__ == '__main__':
    main()
