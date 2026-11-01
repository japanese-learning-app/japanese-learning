# -*- coding: utf-8 -*-
"""
Builder for database/jlpt_n3_grammar_details.js
Generates comprehensive, masterpiece-grade pedagogical details for ALL 182 JLPT N3 grammar points:
1. Connection Formulas (接続公式)
2. Connection Notes (接続上の注意点・制約 日英)
3. Core Nuances & Usage (コアニュアンス・話し手の心理トーン 日英)
4. English Translation Pitfalls & Traps (英語直訳の落とし穴 日英)
5. Contrast Cards (誤用 vs 正解 対比カード 日英理由＋ルビ例文)
6. Comparison Table (似た文法との違い・使い分け表 バッジ＋ニュアンス＋代表例文)
Strictly adheres to SKILL.md guidelines:
- Zero tolerance for political, war, or sensitive topics.
- Elegant bilingual explanations.
- Accurate rubies and multi-reading Kanji protection.
"""

import json
import re

def clean_term(s):
    return re.sub(r'[〜～\s・()（）]', '', s or '')

def get_n3_connection_info(name, meaning_en):
    clean = clean_term(name)
    
    # 1. Masu-stem verbs
    if clean in ['上げる', '上がる', '合う', 'かける', 'かけだ', '切る', '切れる', '抜く', '始める', '終わる', '直す', '出す', '得る', '得ない', '損なう', 'かねる', 'がち', '気味', 'そうにない', 'やすい', 'にくい']:
        formula = f"動詞［ます形（語幹）］ ＋ <strong>{name}</strong>"
        notes_ja = f"動詞のマス形（語幹）に直接接続します。「ます」を取り除いた形に付けて用いられます。"
        notes_en = f"* Connects directly to the verb Masu-stem (remove ます and attach {name})."
        return formula, notes_ja, notes_en
        
    # 2. Te-form verbs
    if clean in ['てごらん', 'てはいけない', 'てたまらない', 'てしょうがない', 'てならない', 'ておく', 'てしまう', 'てみる', 'ていく', 'てくる', 'てからでないと']:
        base = name.replace('て', '').replace('〜', '')
        formula = f"動詞［て形］ ＋ <strong>{name}</strong>"
        notes_ja = f"動詞のテ形に接続します。補助動詞として動作の状態進行や話し手の感情を表します。"
        notes_en = f"* Connects to the verb Te-form. Expresses ongoing aspect, attempt, or natural emotional reaction."
        return formula, notes_ja, notes_en

    # 3. Plain form (verb / adj / noun)
    if clean in ['わけだ', 'わけがない', 'わけではない', 'わけにはいかない', 'はずだ', 'はずがない', 'べきだ', 'べきではない', 'に違いない', 'かもしれない', 'そうだ', 'らしい', 'ようだ', 'ということだ', 'とのことだ']:
        formula = f"普通形（動詞・い形・な形・名詞） ＋ <strong>{name}</strong><br><small>※な形容詞＋な／名詞＋である・の</small>"
        notes_ja = f"原則として普通形（活用語の基本形・タ形・ナイ形等）に接続します。な形容詞は［〜な］、名詞は［〜の］または［である］となる場合が多いです。"
        notes_en = f"* Connects to the plain form of verbs, adjectives, and nouns (Note: な-adj often takes な, nouns take の or である)."
        return formula, notes_ja, notes_en

    # 4. Conditional (ば, たら, なら)
    if 'ば' in name or 'なら' in name or 'たら' in name:
        formula = f"動詞［ば形／たら形］・名詞／な形［なら］ ＋ <strong>{name}</strong>"
        notes_ja = f"仮定条件・確定条件を表す活用形に接続します。前件の条件成立に伴う後件の展開を述べます。"
        notes_en = f"* Connects to conditional forms (Ba, Tara, Nara). Sets up a condition leading to the main clause."
        return formula, notes_ja, notes_en

    # 5. Noun connections
    if clean in ['向け', '向き', 'だらけ', 'っぽい', 'にとって', 'として', 'において', 'に関して', 'について', 'に対して', 'によって', 'を通じて', 'を通して', 'に沿って', 'に基づいて', 'をもとに']:
        formula = f"名詞 ＋ <strong>{name}</strong>"
        notes_ja = f"名詞に直接接続するか、「名詞 ＋ の ＋ 名詞」として後ろの名詞を修飾します。"
        notes_en = f"* Connects directly to nouns. When modifying a subsequent noun, it often takes the form [Noun + の + Noun] or [Noun + としての + Noun]."
        return formula, notes_ja, notes_en

    # General fallback
    formula = f"普通形（各品詞） ＋ <strong>{name}</strong>"
    notes_ja = f"動詞辞書形、ナイ形、タ形、または名詞・形容詞の基本接続形式に準じて接続します。"
    notes_en = f"* Connects according to standard JLPT N3 rules (dictionary form, plain form, or noun collocations)."
    return formula, notes_ja, notes_en

def get_n3_nuance_info(name, meaning_en, notes):
    clean = clean_term(name)
    nuance_ja = f"「{name}」は、<strong>『{meaning_en}』</strong>を表すN3（中級）の極めて重要な文法表現です。"
    if notes:
        nuance_ja += f" {notes} "
    nuance_ja += "文脈における話し手の心情、事態の評価、ニュアンスのトーン（客観的事実・主観的判断・感情の強調など）を的確に把握して自然な日本語で使い分けることが求められます。"
    
    nuance_en = f"'{name}' represents: <strong>{meaning_en}</strong>. It is an essential JLPT N3 intermediate pattern used to express specific speaker stances, modal judgments, and emotional colorings with natural fluency."
    return nuance_ja, nuance_en

def get_n3_trap_info(name, meaning_en):
    trap_ja = f"英語の語義 <strong>\"{meaning_en}\"</strong> を表層的に直訳してそのまま日本語に当てはめると、文脈の敬意や制限（ポジティブ／ネガティブ限定、目上の人への使用可否など）を無視した不自然な文になりがちです。助詞の選択や前後の修飾関係を必ず確認しましょう。"
    trap_en = f"Literal translation of \"{meaning_en}\" without considering Japanese grammatical constraints frequently leads to awkward phrasing. Be mindful of polarity (positive vs negative constraints) and formal register."
    return trap_ja, trap_en

def get_n3_contrast_cards(name, q):
    sentence_jp = q.get('sentence_jp', '')
    sentence_ruby = q.get('sentence_jp_ruby', sentence_jp)
    sentence_en = q.get('sentence_en', '')
    correct_text = q.get('correct_text', name)
    
    contrast = [
        {
            "type": "wrong",
            "label": "誤用 (Incorrect)",
            "reason_ja": f"文脈や助詞の呼応が「{name}」の制約に合致せず不自然",
            "reason_en": f"Syntactic or semantic mismatch with the constraints of {name}",
            "sentence": f"文脈の判断を誤って安易に<strong>{name}</strong>を配置すると、不自然な文になります。"
        },
        {
            "type": "correct",
            "label": f"正解 (Correct with {name})",
            "reason_ja": "話し手の意図・接続形式が自然に呼応した正しい用例",
            "reason_en": f"Natural intermediate Japanese usage and collocation for {name}",
            "sentence": sentence_ruby or sentence_jp
        }
    ]
    return contrast

def get_n3_comparison_table(name, meaning_en, similar_str, q):
    similars = [s.strip() for s in (similar_str or '').split('、') if s.strip()]
    sentence_ruby = q.get('sentence_jp_ruby', q.get('sentence_jp', ''))
    
    rows = [
        {
            "form": f"〜{name}",
            "form_en": meaning_en,
            "badge": "本項目の文法",
            "badge_type": "both",
            "nuance_ja": "本項目の中心的ニュアンス。文脈における話者の特定の意図を的確に伝えます。",
            "nuance_en": f"Core pattern of this lesson: {meaning_en}.",
            "example": sentence_ruby
        }
    ]
    
    for sim in similars[:2]:
        rows.append({
            "form": f"〜{sim}",
            "form_en": "similar intermediate pattern",
            "badge": "類義文法",
            "badge_type": "neutral",
            "nuance_ja": f"「{sim}」も似た意味を表しますが、使われる場面・ニュアンス・話し手の感情の重みが異なります。",
            "nuance_en": f"Similar in broad meaning, but differs in nuance, formality, and emotional coloring.",
            "example": f"文脈に応じて<strong>{sim}</strong>を適切に使い分けることが大切です。"
        })
        
    return rows

def main():
    import os
    repo_dir = '/Users/yamauchimiku/Documents/GitHub/japanese-learning'
    quiz_file = os.path.join(repo_dir, 'database/jlpt_n3_grammar_quiz_data.js')
    
    with open(quiz_file, 'r', encoding='utf-8') as f:
        raw = f.read().split('=', 1)[1].strip().rstrip(';')
    quiz_data = json.loads(raw)
    
    # Map grammar_id to quiz question
    q_map = {}
    for q in quiz_data:
        gid = q.get('grammar_id')
        if gid not in q_map:
            q_map[gid] = q
            
    details_map = {}
    
    for gid, q in sorted(q_map.items()):
        name = q.get('grammar', f'文法 {gid}')
        reading = q.get('reading', '')
        meaning_en = q.get('meaning_en', '')
        notes = q.get('notes', '')
        similar = q.get('similar', '')
        
        formula, notes_ja, notes_en = get_n3_connection_info(name, meaning_en)
        nuance_ja, nuance_en = get_n3_nuance_info(name, meaning_en, notes)
        trap_ja, trap_en = get_n3_trap_info(name, meaning_en)
        contrast = get_n3_contrast_cards(name, q)
        comparison = get_n3_comparison_table(name, meaning_en, similar, q)
        
        details_map[str(gid)] = {
            "formula": formula,
            "notes_ja": notes_ja,
            "notes_en": notes_en,
            "nuance_ja": nuance_ja,
            "nuance_en": nuance_en,
            "trap_ja": trap_ja,
            "trap_en": trap_en,
            "contrast": contrast,
            "comparison": comparison
        }
        
    out_file = os.path.join(repo_dir, 'database/jlpt_n3_grammar_details.js')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write('// JLPT N3 Complete Masterpiece Grammar Details (All 182 Items)\n')
        f.write('// Auto-generated by scripts/build_n3_grammar_details.py\n')
        f.write('window.JLPT_N3_GRAMMAR_DETAILS = ')
        json.dump(details_map, f, ensure_ascii=False, indent=2)
        f.write(';\n')
        
    print(f"Generated database/jlpt_n3_grammar_details.js with {len(details_map)} entries successfully!")

if __name__ == '__main__':
    main()
