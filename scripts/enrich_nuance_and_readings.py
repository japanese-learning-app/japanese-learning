# -*- coding: utf-8 -*-
"""
Enrich nuance explanations and verified reading pairs for all JLPT N2 questions,
repair answer keys and OCR corruptions, and export JSON and JS datasets.
"""

import json
import re
import pykakasi
from collections import Counter
from scripts.vocab_usage_data import VOCAB_USAGE_EXPLANATIONS
from scripts.grammar_judge_data import GRAMMAR_JUDGE_EXPLANATIONS

kks = pykakasi.kakasi()

def to_hira(text):
    if not text:
        return ''
    clean = re.sub(r'<rt>.*?</rt>', '', text)
    clean = re.sub(r'<[^>]+>', '', clean)
    clean = clean.replace('【', '').replace('】', '').replace('（', '').replace('）', '').replace('(', '').replace(')', '').strip()
    res = kks.convert(clean)
    return ''.join([item['hira'] for item in res])

GOKEISEI_READINGS = {
    144: ("未使用", "みしよう", "未", "み"),
    145: ("旧校舎", "きゅうこうしゃ", "旧", "きゅう"),
    146: ("主成分", "しゅせいぶん", "主", "しゅ"),
    147: ("前町長", "ぜんちょうちょう", "前", "ぜん"),
    148: ("再提出", "さいていしゅつ", "再", "さい"),
    149: ("真新しい", "まあたらしい", "真", "ま"),
    150: ("未経験", "みけいけん", "未", "み"),
    151: ("好都合", "こうつごう", "好", "こう"),
    152: ("準決勝", "じゅんけっしょう", "準", "じゅん"),
    153: ("来学期", "らいがっき", "来", "らい"),
    154: ("最年少", "さいねんしょう", "最", "さい"),
    155: ("総人口", "そうじんこう", "総", "そう"),
    156: ("非公開", "ひこうかい", "非", "ひ"),
    157: ("現段階", "げんだんかい", "現", "げん"),
    158: ("全自動", "ぜんじどう", "全", "ぜん"),
    159: ("半開き", "はんびらき", "半", "はん"),
    160: ("元医師", "もといし", "元", "もと"),
    161: ("薄笑い", "うすわらい", "薄", "うす"),
    162: ("初上陸", "はつじょうりく", "初", "はつ"),
    163: ("低カロリー", "ていかろりー", "低", "てい"),
    164: ("異世界", "いせかい", "異", "い"),
    165: ("勤務先", "きんむさき", "先", "さき"),
    166: ("引用元", "いんようもと", "元", "もと"),
    167: ("組み立て式", "くみたてしき", "式", "しき"),
    168: ("光熱費", "こうねつひ", "費", "ひ"),
    169: ("食器類", "しょっきるい", "類", "るい"),
    170: ("和風", "わふう", "風", "ふう"),
    171: ("地域差", "ちいきさ", "差", "さ"),
    172: ("液体状", "えきたいじょう", "状", "じょう"),
    173: ("電気代", "でんきだい", "代", "だい"),
    174: ("アルファベット順", "あるふぁべっとじゅん", "順", "じゅん"),
    175: ("奨学金", "しょうがくきん", "金", "きん"),
    176: ("変更点", "へんこうてん", "点", "てん"),
    177: ("部屋着", "へやぎ", "着", "ぎ"),
    178: ("日本流", "にほんりゅう", "流", "りゅう"),
    179: ("入場許可証", "にゅうじょうきょかしょう", "証", "しょう"),
    180: ("見積書", "みつもりしょ", "書", "しょ"),
    181: ("地域別", "ちいきべつ", "別", "べつ"),
    182: ("聞き手", "ききて", "手", "て"),
    183: ("参加型", "さんかがた", "型", "がた"),
    184: ("予約制", "よやくせい", "制", "せい"),
    185: ("事実上", "じじつじょう", "上", "じょう"),
    186: ("管理下", "かんりか", "下", "か"),
    187: ("消費量", "しょうひりょう", "量", "りょう"),
    188: ("想定内", "そうていない", "内", "ない"),
    189: ("価値観", "かちかん", "観", "かん"),
    190: ("売り切れ", "うりきれ", "切れ", "ぎれ"),
    191: ("かぜ気味", "かぜぎみ", "気味", "ぎみ"),
    192: ("読書離れ", "どくしょばなれ", "離れ", "ばなれ"),
    193: ("夏休み明け", "なつやすみあけ", "明け", "あけ"),
    194: ("海岸沿い", "かいがんぞい", "沿い", "ぞい"),
    748: ("働きぶり", "はたらきぶり", "ぶり", "ぶり"),
}

SPECIAL_READINGS = {
    "余計な": "よけいな",
    "不必要な": "ふひつような",
    "破片": "はへん",
    "企画": "きかく",
    "証明": "しょうめい",
    "気兼ね": "きがね",
    "気がね": "きがね",
    "素人": "しろうと",
    "日頃": "ひごろ",
    "容姿": "ようし",
    "息抜き": "いきぬき",
    "最寄り": "もより",
    "お手入れ": "おていれ",
    "気配り": "きくばり",
    "勘違い": "かんちがい",
    "手頃": "てごろ",
    "直に": "じかに",
    "一段と": "いちだんと",
    "きっぱり": "きっぱり",
    "ぐったり": "ぐったり",
    "ぐんぐん": "ぐんぐん",
    "いまいち": "いまいち",
    "なかなか": "なかなか",
}

def get_reading(word):
    if not word:
        return ''
    clean = word.replace('【', '').replace('】', '').replace('（', '').replace('）', '').strip()
    if clean in SPECIAL_READINGS:
        return SPECIAL_READINGS[clean]
    return to_hira(clean)

def main():
    json_path = 'database/jlpt_n2_vocab_quiz_data.json'
    js_path = 'database/jlpt_n2_vocab_quiz_data.js'

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"Loaded {len(data)} questions.")

    # 1. Apply explicit corrections
    for q in data:
        qid = q['id']

        # ID 529: 女性向き (むき)
        if qid == 529:
            q['choices'] = ['だらけ', 'むけ', 'ぎみ', 'むき']
            q['answer'] = 3
            q['correct_text'] = 'むき'
            q['target_word'] = 'むき'
            q['meaning_en'] = 'This restaurant is good for women because the portions are small.'

        # ID 532: 色もきれいだし (し)
        if qid == 532:
            q['question'] = 'このバッグは色もきれい（　　　）、形もいい。'
            q['question_ruby'] = 'このバッグは<ruby>色<rt>いろ</rt></ruby>もきれい（　　　）、<ruby>形<rt>かたち</rt></ruby>もいい。'
            q['choices'] = ['し', 'とか', 'やら', 'なら']
            q['choices_ruby'] = ['し', 'とか', 'やら', 'なら']
            q['answer'] = 0
            q['correct_text'] = 'し'
            q['target_word'] = 'し'
            q['meaning_en'] = 'The bag has a nice color as well as a nice shape.'
            q['kanji_info'] = []
            q['similar'] = []

        # ID 562: 知事の発言をめぐって、市役所には抗議の電話が鳴り続けた
        if qid == 562:
            q['question'] = 'テレビ番組での知事の発言（　　　）、市役所には抗議の電話が鳴り続けた。'
            q['question_ruby'] = 'テレビ<ruby>番組<rt>ばんぐみ</rt></ruby>での<ruby>知事<rt>ちじ</rt></ruby>の<ruby>発言<rt>はつげん</rt></ruby>（　　　）、<ruby>市役所<rt>しやくしょ</rt></ruby>には<ruby>抗議<rt>こうぎ</rt></ruby>の<ruby>電話<rt>でんわ</rt></ruby>が<ruby>鳴り<rt>なり</rt></ruby><ruby>続け<rt>つづけ</rt></ruby>た。'
            q['target_word'] = 'をめぐって'

        # ID 652: 父は毎朝、夜が明けるか明けないかのうちに
        if qid == 652:
            q['question'] = '父は毎朝、夜が明けるか明けないか（　　　）、家を出る。'
            q['question_ruby'] = '<ruby>父<rt>ちち</rt></ruby>は<ruby>毎朝<rt>まいあさ</rt></ruby>、<ruby>夜<rt>よる</rt></ruby>が<ruby>明け<rt>あけ</rt></ruby>るか<ruby>明け<rt>あけ</rt></ruby>ないか（　　　）、<ruby>家<rt>いえ</rt></ruby>を<ruby>出る<rt>でる</rt></ruby>。'
            q['target_word'] = 'のうちに'

        # ID 664: この値段からすると、本物の毛皮ではないだろう
        if qid == 664:
            q['question'] = 'この値段（　　　）、本物の毛皮ではないだろう。'
            q['question_ruby'] = 'この<ruby>値段<rt>ねだん</rt></ruby>（　　　）、<ruby>本物<rt>ほんもの</rt></ruby>の<ruby>毛皮<rt>けがわ</rt></ruby>ではないだろう。'
            q['target_word'] = 'からすると'

        # Target word alignment for grammar questions
        if qid == 481:
            q['target_word'] = 'にすぎない'
        elif qid == 499:
            q['target_word'] = 'にもとづいて'
        elif qid == 553:
            q['target_word'] = 'に先だって'
        elif qid == 559:
            q['target_word'] = 'ことだから'
        elif qid == 568:
            q['target_word'] = 'ことなく'
        elif qid == 586:
            q['target_word'] = 'にかけては'
        elif qid == 589:
            q['target_word'] = '行く'
        elif qid == 661:
            q['target_word'] = 'からすれば'

        # 2. Inject Nuance Explanations
        cat = q.get('category', '')

        if cat == '語彙用法' and qid in VOCAB_USAGE_EXPLANATIONS:
            ve = VOCAB_USAGE_EXPLANATIONS[qid]
            q['nuance_diff'] = ve['difference']
            q['english_pitfall'] = ve['english_note']
            q['explanation'] = f"【似た言葉とのニュアンスの違い】\n{ve['difference']}\n\n【英語直訳とのズレ・注意点】\n{ve['english_note']}"

        elif cat == '文法形式の判断' and qid in GRAMMAR_JUDGE_EXPLANATIONS:
            ge = GRAMMAR_JUDGE_EXPLANATIONS[qid]
            q['nuance_diff'] = ge['difference']
            q['english_pitfall'] = ge['english_note']
            q['explanation'] = f"【似た文法とのニュアンスの違い】\n{ge['difference']}\n\n【英語直訳とのズレ・注意点】\n{ge['english_note']}"

        # 3. Reading Pairs for Question & Answer
        if qid in GOKEISEI_READINGS:
            comp, comp_r, pref, pref_r = GOKEISEI_READINGS[qid]
            q['target_word'] = comp
            q['target_word_reading'] = comp_r
            q['correct_text_reading'] = pref_r
        elif cat == '漢字読み':
            q['target_word_reading'] = q['correct_text']
            q['correct_text_reading'] = q['correct_text']
        elif cat == '漢字表記':
            q['target_word_reading'] = q['target_word']
            q['correct_text_reading'] = q['target_word']
        else:
            t = q.get('target_word') or q.get('correct_text') or ''
            c = q.get('correct_text') or ''
            q['target_word_reading'] = get_reading(t)
            q['correct_text_reading'] = get_reading(c)

    # 4. Verification of Balance and Integrity
    ans_counts = Counter(q['answer'] for q in data)
    print("Answer counts distribution across choices 0-3:", ans_counts)
    assert ans_counts[0] == 224 and ans_counts[1] == 224 and ans_counts[2] == 224 and ans_counts[3] == 224, "Answers not perfectly balanced!"

    for q in data:
        assert q['choices'][q['answer']] == q['correct_text'], f"Mismatch in ID {q['id']}"
        assert 'target_word_reading' in q and q['target_word_reading'], f"Missing target reading in ID {q['id']}"
        assert 'correct_text_reading' in q and q['correct_text_reading'], f"Missing correct reading in ID {q['id']}"

    vocab_with_nuance = sum(1 for q in data if q.get('category') == '語彙用法' and q.get('nuance_diff'))
    grammar_with_nuance = sum(1 for q in data if q.get('category') == '文法形式の判断' and q.get('nuance_diff'))
    print(f"Vocab usage questions with nuance: {vocab_with_nuance}/64")
    print(f"Grammar questions with nuance: {grammar_with_nuance}/112")
    assert vocab_with_nuance == 64, "Missing vocab usage nuance!"
    assert grammar_with_nuance == 112, "Missing grammar judge nuance!"

    # 5. Save updated datasets
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Updated {json_path}")

    with open(js_path, 'w', encoding='utf-8') as f:
        f.write("// JLPT N2 Vocab & Grammar Practice Quiz Data (896 Questions)\n")
        f.write("// Complete with verified reading pairs, nuance explanations, and balanced answers.\n")
        f.write("window.JLPT_N2_VOCAB_QUIZ_DATA = ")
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print(f"Updated {js_path}")

if __name__ == '__main__':
    main()
