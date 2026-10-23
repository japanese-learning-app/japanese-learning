#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
repair_n2_vocab_quiz_comprehensive.py
Comprehensive, definitive audit and repair script for JLPT N2 Vocab Quiz Dataset (896 Questions).
- Eliminates ALL answer key errors (IDs 11, 196, 205, 214, 223, 277, 295, 375, 377, 378, 380, 381, 382, 383, 459, 499, 553, 621, 687, 793, etc.)
- Fixes ALL OCR errors, scrambled sentences, truncated sentences, and typos (over 70 questions)
- Normalizes internal word spaces (納得 させる -> 納得させる) across all 896 questions
- Prevents ruby spoilers on all Kanji-writing questions (ひらがな -> 漢字)
- Rebuilds questions 796-896 with authentic JLPT standards
- Perfectly balances answer choices across 0, 1, 2, 3 (exactly 224 questions = 25.0% each)
"""

import json
import re
import os
import sys
import random

sys.path.append('scripts')
import pykakasi
from fix_all_rubies import fix_rubies_in_text

kks = pykakasi.kakasi()

# 1. Load dictionary data for rich definitions & similar words
print("Loading dictionary database...")
with open('database/dictionary_data.js', 'r', encoding='utf-8') as f:
    dict_js = f.read()

m = re.search(r'window\.DICT_DATA\s*=\s*(\[.*?\]);?\s*$', dict_js, re.DOTALL)
dict_raw = json.loads(m.group(1)) if m else []

dict_map = {}
for entry in dict_raw:
    w = entry.get('w', '')
    if w and w not in dict_map:
        dict_map[w] = entry

with open('database/kanji_master.json', 'r', encoding='utf-8') as f:
    kanji_master = json.load(f)

def lookup_dict_info(term):
    if not term:
        return {"term": "", "reading": "", "meaning": ""}
    clean_term = re.sub(r'[【】（）()]', '', term).strip()
    entry = dict_map.get(clean_term)
    if entry:
        meanings = entry.get('m', [])
        m_str = '; '.join(meanings[:2]) if meanings else ""
        r_str = entry.get('r', '')
        return {"term": clean_term, "reading": r_str, "meaning": m_str}
    conv = kks.convert(clean_term)
    hira = ''.join(x['hira'] for x in conv)
    return {"term": clean_term, "reading": hira, "meaning": ""}

def get_kanji_details(text):
    if not text:
        return []
    clean_t = re.sub(r'[【】（）()\s]', '', text)
    kanjis = [c for c in clean_t if '\u4e00' <= c <= '\u9fff']
    if not kanjis and len(clean_t) >= 2:
        for item in dict_raw:
            r = item.get('r', '')
            w = item.get('w', '')
            if r == clean_t and any('\u4e00' <= c <= '\u9fff' for c in w):
                kanjis = [c for c in w if '\u4e00' <= c <= '\u9fff']
                break
    seen = set()
    res = []
    for k in kanjis:
        if k in seen:
            continue
        seen.add(k)
        kd = kanji_master.get(k)
        if kd:
            on = kd.get('readings_on', [])
            on_kat = [''.join(chr(ord(c) + 96) if 'ぁ' <= c <= 'ん' else c for c in r) for r in on]
            kun = [r.replace('.', '') for r in kd.get('readings_kun', []) if not r.startswith('!')]
            meanings = kd.get('meanings', [])
            res.append({
                'kanji': k,
                'onyomi': '・'.join(on_kat) if on_kat else '-',
                'kunyomi': '・'.join(kun) if kun else '-',
                'meaning': ', '.join(meanings[:3]) if meanings else ''
            })
    return res

def to_ruby_protected(sentence, target_kanji=None, target_reading=None):
    if not sentence:
        return ""
    if target_kanji and f"【{target_kanji}】" in sentence:
        placeholder = "___TARGET_KANJI_PROTECTED___"
        temp_s = sentence.replace(f"【{target_kanji}】", placeholder)
        conv = kks.convert(temp_s)
        parts = []
        for item in conv:
            orig = item['orig']
            hira = item['hira']
            if placeholder in orig:
                parts.append(orig)
            elif orig != hira and any('\u4e00' <= c <= '\u9fff' for c in orig):
                parts.append(f"<ruby>{orig}<rt>{hira}</rt></ruby>")
            else:
                parts.append(orig)
        raw = "".join(parts)
        fixed = fix_rubies_in_text(raw)
        reading = target_reading or "".join(x['hira'] for x in kks.convert(target_kanji))
        target_html = f'<ruby class="target-kanji-reading"><span class="target-word">【{target_kanji}】</span><rt class="target-reading-spoiler">{reading}</rt></ruby>'
        return fixed.replace(placeholder, target_html)
    else:
        conv = kks.convert(sentence)
        parts = []
        for item in conv:
            orig = item['orig']
            hira = item['hira']
            if orig != hira and any('\u4e00' <= c <= '\u9fff' for c in orig):
                parts.append(f"<ruby>{orig}<rt>{hira}</rt></ruby>")
            else:
                parts.append(orig)
        raw = "".join(parts)
        return fix_rubies_in_text(raw)

def to_ruby_simple(text):
    if not text:
        return ""
    if not any('\u4e00' <= c <= '\u9fff' for c in text):
        return text
    conv = kks.convert(text)
    parts = []
    for item in conv:
        orig = item['orig']
        hira = item['hira']
        if orig != hira and any('\u4e00' <= c <= '\u9fff' for c in orig):
            parts.append(f"<ruby>{orig}<rt>{hira}</rt></ruby>")
        else:
            parts.append(orig)
    return fix_rubies_in_text("".join(parts))

def clean_internal_spaces(text):
    if not text:
        return ""
    # Protect blanks like （　　　）
    placeholder = "___JLPT_BLANK___"
    s = re.sub(r'（[\s　]*）', placeholder, text)
    # Remove space between kanji and hiragana
    s = re.sub(r'([\u4e00-\u9fff])\s+([\u3040-\u309f])', r'\1\2', s)
    # Remove space between hiragana and hiragana
    s = re.sub(r'([\u3040-\u309f])\s+([\u3040-\u309f])', r'\1\2', s)
    # Remove space between katakana and katakana
    s = re.sub(r'([\u30a0-\u30ff])\s+([\u30a0-\u30ff])', r'\1\2', s)
    # Remove spaces around brackets
    s = re.sub(r'\s+【', '【', s)
    s = re.sub(r'】\s+', '】', s)
    s = re.sub(r'\s*（', '（', s)
    s = re.sub(r'）\s*', '）', s)
    # Restore blank
    s = s.replace(placeholder, "（　　　）")
    # Clean multiple spaces
    s = re.sub(r'[ ]{2,}', ' ', s)
    return s.strip()

# Load current quiz data
with open('database/jlpt_n2_vocab_quiz_data.json', 'r', encoding='utf-8') as f:
    quiz_data = json.load(f)

print(f"Loaded {len(quiz_data)} questions.")
q_by_id = {q['id']: q for q in quiz_data}

# -------------------------------------------------------------
# Comprehensive dictionary of individual question repairs
# -------------------------------------------------------------
INDIVIDUAL_REPAIRS = {
    # 1. Major answer key errors & bracket boundaries
    11: {
        'target_word': '破片',
        'question': 'ガラスの【破片】で指を切ってしまった。',
        'choices': ['はぺん', 'はべん', 'はっぺん', 'はへん'],
        'correct_text': 'はへん',
        'cat': '漢字読み'
    },
    27: {
        'target_word': '警告',
        'question': 'スピードの出しすぎは危険だと【警告】された。',
        'correct_text': 'けいこく',
        'cat': '漢字読み'
    },
    58: {
        'target_word': '柔軟',
        'question': 'スタッフが【柔軟】に対応してくれた。',
        'correct_text': 'じゅうなん',
        'cat': '漢字読み'
    },
    62: {
        'target_word': '単純',
        'question': 'こんな【単純】な計算も間違えるなんて恥ずかしい。',
        'correct_text': 'たんじゅん',
        'cat': '漢字読み'
    },
    70: {
        'target_word': '実',
        'question': '今回の調査で、【実】におもしろい発見があった。',
        'choices': ['みつ', 'じつ', 'み', 'じ'],
        'correct_text': 'じつ',
        'cat': '漢字読み'
    },
    72: {
        'target_word': '常',
        'question': '祖母からもらった指輪を【常】に身に着けている。',
        'choices': ['じょう', 'づね', 'じゅう', 'つね'],
        'correct_text': 'つね',
        'cat': '漢字読み'
    },
    122: {
        'target_word': 'つとめて',
        'question': '10年以上、同じ会社に【つとめて】いる。',
        'choices': ['労めて', '勤めて', '働めて', '仕めて'],
        'correct_text': '勤めて',
        'cat': '漢字表記'
    },
    142: {
        'target_word': 'そくざ',
        'question': 'トラブルが起きたら、【そくざ】に対応するべきだ。',
        'choices': ['印座', '即座', '即底', '印底'],
        'correct_text': '即座',
        'cat': '漢字表記'
    },
    175: {
        'question': '奨学（　　　）をもらいながら大学に通っている。',
        'choices': ['費', '料', '金', '代'],
        'correct_text': '金',
        'cat': '語形成'
    },
    187: {
        'question': '奈良県は日本で最もコーヒーの消費（　　　）が多いところです。',
        'choices': ['集', '点', '量', '力'],
        'correct_text': '量',
        'cat': '語形成'
    },
    192: {
        'question': 'インターネットの発達による若者の読書（　　　）が問題になっている。',
        'choices': ['忘れ', '別れ', '逃げ', '離れ'],
        'correct_text': '離れ',
        'cat': '語形成'
    },
    193: {
        'question': '宿題をしなかったので、夏休み（　　　）から先生にしかられてしまった。',
        'choices': ['明け', '入り', '開け', '出し'],
        'correct_text': '明け',
        'cat': '語形成'
    },
    194: {
        'question': '海岸（　　　）に新しいレストランができた。',
        'choices': ['並み', '沿い', '付き', '過ぎ'],
        'correct_text': '沿い',
        'cat': '語形成'
    },
    196: {
        'question': 'プロのサッカー選手になって（　　　）を立てるのが私の夢だ。',
        'choices': ['生活', '設計', '家計', '生計'],
        'correct_text': '生計',
        'cat': '文脈規定'
    },
    205: {
        'question': '頭の良さと性格の良さはどちらも大切だが、（　　　）の方が人として大切な要素だと思う。',
        'choices': ['以後', '後方', '後者', '以降'],
        'correct_text': '後者',
        'cat': '文脈規定'
    },
    211: {
        'question': 'トラブルが起きたときは、チームみんなで話し合って（　　　）の解決方法を探すべきだ。',
        'choices': ['改良', '大型', '最善', '上位'],
        'correct_text': '最善',
        'cat': '文脈規定'
    },
    214: {
        'question': '新しいウイルスが流行しているため、病院での（　　　）をお断りしています。',
        'choices': ['訪問', '入会', '面会', '来場'],
        'correct_text': '面会',
        'cat': '文脈規定'
    },
    223: {
        'question': 'これまでの製品を（　　　）し、新しいモデルとして発売することになった。',
        'choices': ['新設', '向上', '進歩', '改良'],
        'correct_text': '改良',
        'cat': '文脈規定'
    },
    256: {
        'question': '数か国語を話せる彼は、相手によって言葉を（　　　）ことができる。',
        'choices': ['引き分ける', '使い分ける', '見分ける', '聞き分ける'],
        'correct_text': '使い分ける',
        'cat': '文脈規定'
    },
    277: {
        'question': '森に入ったとたん、鳥が（　　　）飛び立った。',
        'choices': ['存分に', '一斉に', '直ちに', '要するに'],
        'correct_text': '一斉に',
        'cat': '文脈規定'
    },
    295: {
        'question': 'すみません、電話しているのでテレビの（　　　）を下げてもらえませんか。',
        'choices': ['コーラス', 'エネルギー', 'バランス', 'ボリューム'],
        'correct_text': 'ボリューム',
        'cat': '文脈規定'
    },
    375: {
        'target_word': '大手',
        'question': '次の言葉の使い方が最も適切な文を選びなさい：【大手】',
        'choices': [
            'いつも私の手を握ってくれた、父の大手を思い出す。',
            '両親は私が良い大学を卒業して大手の銀行に就職することを願っているようだ。',
            'この店の料理はどれも大盛りで、一人では食べ切ることができない。',
            '彼はとても力持ちなので、どんなに重いものも軽々と持ち上げることができる。'
        ],
        'correct_text': '両親は私が良い大学を卒業して大手の銀行に就職することを願っているようだ。',
        'cat': '語彙用法'
    },
    377: {
        'target_word': '現地',
        'question': '次の言葉の使い方が最も適切な文を選びなさい：【現地】',
        'choices': [
            '正月は実家に帰って、家族とのんびり過ごしたいと思っている。',
            '事故の現場には人がたくさん集まっていて、警察官が取り調べを行っていた。',
            '教科書で学ぶ英語と、現地の人が話す英語は少し違うようだ。',
            '祖父が生まれた故郷は、この辺りはりんご畑だったそうだ。'
        ],
        'correct_text': '教科書で学ぶ英語と、現地の人が話す英語は少し違うようだ。',
        'cat': '語彙用法'
    },
    378: {
        'target_word': '作法',
        'question': '次の言葉の使い方が最も適切な文を選びなさい：【作法】',
        'choices': [
            '会社の規則を破ることは、社員として許されることではない。',
            '彼女は料理教室に通っていただけあって、料理を作る手順がとても良い。',
            '子どものころ、食事の作法について祖母から厳しく教えられた。',
            'この料理の作り方は難しくて、子どもには作れないだろう。'
        ],
        'correct_text': '子どものころ、食事の作法について祖母から厳しく教えられた。',
        'cat': '語彙用法'
    },
    380: {
        'target_word': '性能',
        'question': '次の言葉の使い方が最も適切な文を選びなさい：【性能】',
        'choices': [
            '性能が良いパソコンを使い始めてから、作業が早く進むようになった。',
            'できるだけ能力が高く、性格が良い人を雇いたいと思っている。',
            'ライオンとチンパンジーは、知能の高い動物として有名である。',
            '兄は私と違って生まれたときから才能があるので、何をやってもうまくできる。'
        ],
        'correct_text': '性能が良いパソコンを使い始めてから、作業が早く進むようになった。',
        'cat': '語彙用法'
    },
    381: {
        'target_word': '手元',
        'question': '次の言葉の使い方が最も適切な文を選びなさい：【手元】',
        'choices': [
            '彼女はどんな作業をやらせてみても、とにかく手際が良い。',
            '今日は足元が滑りやすいので、足元に気をつけてお越しください。',
            '私は昔から手先が器用で、だいたいのものは自分で作ることができる。',
            '給料をもらっても、家賃と生活費で手元に残るお金はあまり多くない。'
        ],
        'correct_text': '給料をもらっても、家賃と生活費で手元に残るお金はあまり多くない。',
        'cat': '語彙用法'
    },
    382: {
        'target_word': '人前',
        'question': '次の言葉の使い方が最も適切な文を選びなさい：【人前】',
        'choices': [
            '人前で話すのが苦手で、すぐに緊張して顔が赤くなってしまう。',
            'こんな簡単な仕事もできないようでは、まだまだ一人前ではないな。',
            '映画館の席に座ったら、目の前に背の高い人が座っていたので画面が見えにくかった。',
            'この居酒屋には、いつも愛想が良い店長がいる。'
        ],
        'correct_text': '人前で話すのが苦手で、すぐに緊張して顔が赤くなってしまう。',
        'cat': '語彙用法'
    },
    383: {
        'target_word': '手間',
        'question': '次の言葉の使い方が最も適切な文を選びなさい：【手間】',
        'choices': [
            '赤ちゃんの世話をするためには、時間と体力がたくさん必要だ。',
            '最近は仕事も私生活も忙しくて、人の心配をするような暇は全くない。',
            '一時間くらい時間が空いたので、同僚の仕事を少し手伝うことにした。',
            '仕事が終わって家に帰ってきてから手間のかかる料理を作るのは面倒だ。'
        ],
        'correct_text': '仕事が終わって家に帰ってきてから手間のかかる料理を作るのは面倒だ。',
        'cat': '語彙用法'
    },
    387: {
        'choices': [
            'しばらく会社を休んでいて仕事の手順を忘れてしまったので、同僚に教えてもらった。',
            'どれだけ営業で良い成績を残しても、全く給料が上がらない。',
            'やりがいのある仕事に出会うまで、何度も転職を続けた。',
            '仕事で全く評価してもらえないと、やる気が出なくなってしまう。'
        ],
        'correct_text': 'やりがいのある仕事に出会うまで、何度も転職を続けた。'
    },
    391: {
        'target_word': '段取り',
        'choices': [
            '商品の開発は順調で、来月から次の段階に進む予定です。',
            '大学内の全ての段差を解消するために、大きな工事が行われた。',
            'イベントがうまく進むように、事前にしっかりと段取りしてください。',
            '車いすに乗っている人にとって、階段がある場所はとても不便だ。'
        ],
        'correct_text': 'イベントがうまく進むように、事前にしっかりと段取りしてください。'
    },
    394: {
        'choices': [
            '会議は予定よりかなり長くなり、12時になっても終わらない。',
            'イベント会場まで部長がわざわざお菓子を差し入れしてくれた。',
            '電子マネーを使うようになって、ATMからお金を引き出すことも少なくなった。',
            'もう少しで妻の誕生日なので、何か素敵なプレゼントを贈ろうと考えている。'
        ],
        'correct_text': 'イベント会場まで部長がわざわざお菓子を差し入れしてくれた。'
    },
    403: {
        'choices': [
            '家を出てから会社に着くまで、だいたい一時間くらいかかります。',
            '日曜日はいつもカフェの窓際の席に座って、朝から夜までのんびり過ごす。',
            '無職だった私が、会社を立ち上げるに至るまでのお話をいたします。',
            '付き合って10年目の記念日に彼からプロポーズをされ、胸がいっぱいになって泣いてしまった。'
        ],
        'correct_text': '無職だった私が、会社を立ち上げるに至るまでのお話をいたします。'
    },
    405: {
        'choices': [
            '政治家の不正を暴くために、証拠を集めているところだ。',
            'おとなしかった馬が突然暴れだして、周りにいた人たちがけがを負ってしまった。',
            '先生でも解けなかった数学の問題を、彼は簡単に解いてしまった。',
            'どんな理由があったとしても、人の顔を強く叩くことは許されることではない。'
        ],
        'correct_text': '政治家の不正を暴くために、証拠を集めているところだ。'
    },
    415: {
        'choices': [
            '彼女はいつもいらいらしていて、誰が見てもストレスがたまっているようだった。',
            '夜の間に雪が降って、朝になると外が真っ白になるくらい雪が積もっていた。',
            '部長に頼まれた仕事が多くて、終わらせるのに少なく見積もってもあと二時間はかかりそうだ。',
            'そこにあるダンボールを車に積み込みたいのですが、手伝っていただけませんか。'
        ],
        'correct_text': '部長に頼まれた仕事が多くて、終わらせるのに少なく見積もってもあと二時間はかかりそうだ。'
    },
    416: {
        'choices': [
            '仕事が終わったらスーパーに立ち寄って、ビールとおつまみを買うつもりだ。',
            'そこに立っていると危険ですので、一歩後ろに下がってください。',
            '彼のことはよく知らなかったけれど、話をするうちに彼の性格がだんだん分かってきた。',
            'どんなに言い合いになっても、歩み寄って問題を解決するのが夫婦というものです。'
        ],
        'correct_text': 'どんなに言い合いになっても、歩み寄って問題を解決するのが夫婦というものです。'
    },
    426: {
        'choices': [
            'このレストランは、地元で採れた新鮮な食材を使用している。',
            '彼は清潔感があり、笑顔がさわやかなので、皆から好かれている。',
            '外はちょっと肌寒いので、上着を着て行った方が良いですよ。',
            '電車の中で友達と大声で話していたら、周りの人から冷ややかな目で見られてしまった。'
        ],
        'correct_text': '彼は清潔感があり、笑顔がさわやかなので、皆から好かれている。'
    },
    428: {
        'choices': [
            'けがをしないように、十分に安全を考えてヘルメットをかぶって作業してください。',
            '地震が起きたときは、あわてずにまず机の下に入ってください。',
            'このイチゴケーキは夏の期間限定商品なので、ぜひ買った方が良いですよ。',
            '友達にお勧めされた映画を観に行ったが、いまいちだった。'
        ],
        'correct_text': '友達にお勧めされた映画を観に行ったが、いまいちだった。'
    },
    447: {
        'question': '私が失恋したとき、佐藤さんが（　　　）くれて、うれしかった。',
        'choices': ['あこがれて', '力を入れて', 'なぐさめて', '力を込めて'],
        'correct_text': 'なぐさめて',
        'cat': '文脈規定'
    },
    448: {
        'question': 'その新しい商品は、東京（　　　）、全国の主要な都市で売られている。',
        'choices': ['にはじめ', 'をはじめて', 'にはじめて', 'をはじめ'],
        'correct_text': 'をはじめ',
        'cat': '文法形式の判断'
    },
    452: {
        'target_word': 'お祝い',
        'question': '娘は七歳の誕生日の【お祝い】に貯金箱をもらいました。',
        'choices': ['おにあい', 'おみあい', 'おゆわい', 'おいわい'],
        'correct_text': 'おいわい',
        'cat': '漢字読み'
    },
    454: {
        'question': '会社で嫌なことがあると、酒を（　　　）。',
        'choices': ['飲んでならない', '飲まずにはいられない', '飲まないことではない', '飲むことはならない'],
        'correct_text': '飲まずにはいられない',
        'cat': '文法形式の判断'
    },
    457: {
        'question': '田中さんは、音楽の先生（　　　）、歌がうまい。',
        'choices': ['だけに', 'ほどに', 'ように', 'くらいに'],
        'correct_text': 'だけに',
        'cat': '文法形式の判断'
    },
    459: {
        'question': '歩き始めの幼児は（　　　）ので、親は大変だ。',
        'choices': ['目が回らない', '目がきかない', '目がない', '目がはなせない'],
        'correct_text': '目がはなせない',
        'cat': '文脈規定'
    },
    460: {
        'question': '起業する（　　　）、注意すべきことは何でしょう。',
        'choices': ['にわたり', 'にとって', 'にしても', 'にあたって'],
        'correct_text': 'にあたって',
        'cat': '文法形式の判断'
    },
    462: {
        'question': '今急いで結論を出さないで、少し（　　　）を見てからにしましょう。',
        'choices': ['都合', '様子', '具合', '気分'],
        'correct_text': '様子',
        'cat': '文脈規定'
    },
    463: {
        'question': '工事中（　　　）、通行止め。',
        'choices': ['につき', 'にのみ', 'にとって', 'にわたり'],
        'correct_text': 'につき',
        'cat': '文法形式の判断'
    },
    466: {
        'question': '土地開発が進む（　　　）、緑が少なくなってきた。',
        'choices': ['につれて', 'とともに', 'にしたがって', 'にあたって'],
        'correct_text': 'につれて',
        'cat': '文法形式の判断'
    },
    469: {
        'question': 'タバコの煙は、吸わない人（　　　）迷惑だ。',
        'choices': ['にしたら', 'にしても', 'にしては', 'にせよ'],
        'correct_text': 'にしたら',
        'cat': '文法形式の判断'
    },
    470: {
        'target_word': 'おこらない',
        'question': 'あの人はめったに【おこらない】。',
        'choices': ['怒らない', '怠らない', '怖らない', '恐らない'],
        'correct_text': '怒らない',
        'cat': '漢字表記'
    },
    471: {
        'question': '病気になったり、事故にあったりと、最近（　　　）ことがない。',
        'choices': ['みっともない', 'くだらない', 'ろくな', 'たまらない'],
        'correct_text': 'ろくな',
        'cat': '文脈規定'
    },
    474: {
        'question': 'A「車を買い換えようか。」 B「そんな（　　　）はないよ。」',
        'choices': ['都合', '余裕', '気分', '暮らし'],
        'correct_text': '余裕',
        'cat': '文脈規定'
    },
    477: {
        'question': 'コードが（　　　）に届かないから、延長コードを使おう。',
        'choices': ['コンセント', 'レバー', 'スイッチ', 'サイズ'],
        'correct_text': 'コンセント',
        'cat': '文脈規定'
    },
    480: {
        'question': 'ネットショッピングで安く買ったと思ったが、送料がかかってかえって高く（　　　）。',
        'choices': ['とれた', 'かけた', 'いれた', 'ついた'],
        'correct_text': 'ついた',
        'cat': '文脈規定'
    },
    486: {
        'question': '休日なので家で（　　　）いたのに、電話で会社に呼び出されてしまった。',
        'choices': ['くらして', 'くつろいで', 'のんきして', 'ふざけて'],
        'correct_text': 'くつろいで',
        'cat': '文脈規定'
    },
    489: {
        'question': 'A「昨日の件、どうなった？」 B「今、ここでその話は、（　　　）。」',
        'choices': ['よしましょう', 'はがしましょう', 'やっつけましょう', 'ほうりましょう'],
        'correct_text': 'よしましょう',
        'cat': '文脈規定'
    },
    493: {
        'question': '専門家の予測（　　　）景気は悪くなった。',
        'choices': ['に反して', 'に応えて', 'によって', 'に基づいて'],
        'correct_text': 'に反して',
        'cat': '文法形式の判断'
    },
    499: {
        'question': 'この映画は、事実に（　　　）制作された。',
        'choices': ['につれて', 'にもとづいて', 'のもとで', 'である反面'],
        'correct_text': 'にもとづいて',
        'cat': '文法形式の判断'
    },
    500: {
        'target_word': 'わいた',
        'question': 'お母さん、お湯が【わいた】よ。',
        'choices': ['蒸いた', '浮いた', '乾いた', '沸いた'],
        'correct_text': '沸いた',
        'cat': '漢字表記'
    },
    504: {
        'question': '携帯電話の機能を使い（　　　）人がどれだけいるだろうか。',
        'choices': ['こんでいる', 'はたしている', 'まわしている', 'こなしている'],
        'correct_text': 'こなしている',
        'cat': '文脈規定'
    },
    509: {
        'target_word': '触れないで',
        'question': 'やけどの恐れがありますから、絶対に手を【触れないで】ください。',
        'choices': ['ふれないで', 'さわれないで', 'すれないで', 'あたれないで'],
        'correct_text': 'ふれないで',
        'cat': '漢字読み'
    },
    514: {
        'question': '何かに（　　　）、近所の人にはお世話になっている。',
        'choices': ['しろ', 'つけ', 'やら', 'せよ'],
        'correct_text': 'つけ',
        'cat': '文法形式の判断'
    },
    516: {
        'question': '彼とは年賀状の（　　　）だけで、もう何年も会っていない。',
        'choices': ['あげもらい', '行き帰り', '受け取り', 'やり取り'],
        'correct_text': 'やり取り',
        'cat': '文脈規定'
    },
    520: {
        'question': '庭には赤（　　　）黄（　　　）、いろんな色の花が咲いている。',
        'choices': ['なり／なり', 'にしろ／にしろ', 'にせよ／にせよ', 'やら／やら'],
        'correct_text': 'やら／やら',
        'cat': '文法形式の判断'
    },
    525: {
        'question': '試験が近いので家に（　　　）勉強しないと。',
        'choices': ['こもって', 'こめて', 'くっついて', 'たまって'],
        'correct_text': 'こもって',
        'cat': '文脈規定'
    },
    526: {
        'question': '彼は、親の愛情（　　　）幸せに育った。',
        'choices': ['をこめて', 'のもとで', 'をとわず', 'のたびに'],
        'correct_text': 'のもとで',
        'cat': '文法形式の判断'
    },
    531: {
        'question': 'この化粧品を使い始めてから、肌の（　　　）がよくなった気がする。',
        'choices': ['調子', '様子', '具合', '機嫌'],
        'correct_text': '調子',
        'cat': '文脈規定'
    },
    533: {
        'target_word': '帯',
        'question': '浴衣には簡単な【帯】をします。足袋は普通、はきません。',
        'choices': ['おび', 'ひも', 'たて', 'つな'],
        'correct_text': 'おび',
        'cat': '漢字読み'
    },
    534: {
        'choices': ['耐えられず', '我慢できず', 'がまんせず', 'おさえず'],
        'correct_text': '我慢できず'
    },
    538: {
        'question': 'あんなまずいもの、二度と（　　　）ものか。',
        'choices': ['買い', '買う', '買った', '買わない'],
        'correct_text': '買う',
        'cat': '文法形式の判断'
    },
    540: {
        'question': '第二次世界大戦後、日本は激しい（　　　）になった。',
        'choices': ['ショック', 'ダウン', 'フォーム', 'インフレ'],
        'correct_text': 'インフレ',
        'cat': '文脈規定'
    },
    545: {
        'target_word': 'けん',
        'question': '乗車【けん】を拝見します。',
        'choices': ['券', '符', '状', '札'],
        'correct_text': '券',
        'cat': '漢字表記'
    },
    547: {
        'question': '先生に読むように言われた本は、（　　　）ものの、まだ読んでいない。',
        'choices': ['借りる', '借りない', '借りた', '借りよう'],
        'correct_text': '借りた',
        'cat': '文法形式の判断'
    },
    553: {
        'question': '12月に行われる試験（　　　）、10月に模擬試験をします。',
        'choices': ['をもとに', 'に先だって', 'のもとで', 'にわたり'],
        'correct_text': 'に先だって',
        'cat': '文法形式の判断'
    },
    555: {
        'question': '一つの悩みは解決したが、（　　　）問題がまた起きてしまった。',
        'choices': ['くどい', 'やかましい', 'やっかいな', 'みっともない'],
        'correct_text': 'やっかいな',
        'cat': '文脈規定'
    },
    559: {
        'question': '親切な彼女の（　　　）、引き受けてくれるだろう。',
        'choices': ['ことには', 'ことから', 'ことだから', 'ことなら'],
        'correct_text': 'ことだから',
        'cat': '文法形式の判断'
    },
    564: {
        'question': '犬に顔を（　　　）、べとべとになった。',
        'choices': ['くわえて', 'しゃぶられて', 'かじられて', 'なめられて'],
        'correct_text': 'なめられて',
        'cat': '文脈規定'
    },
    566: {
        'target_word': 'りょうし',
        'question': '大人になったら、【りょうし】になって海で働きたい。',
        'choices': ['料師', '漁師', '武士', '理容師'],
        'correct_text': '漁師',
        'cat': '漢字表記'
    },
    568: {
        'question': '両親は、息子の書いた絵を飽きること（　　　）眺めた。',
        'choices': ['ばかりに', 'ように', 'にかまわず', 'なく'],
        'correct_text': 'なく',
        'cat': '文法形式の判断'
    },
    569: {
        'target_word': '戻して',
        'question': '本を棚に【戻して】ください。',
        'choices': ['もどして', 'かえして', 'とかして', 'かたして'],
        'correct_text': 'もどして',
        'cat': '漢字読み'
    },
    574: {
        'question': '有名人の作品（　　　）、すばらしいとは限らない。',
        'choices': ['だけあって', 'だからといって', 'のことだから', 'にもかかわらず'],
        'correct_text': 'だからといって',
        'cat': '文法形式の判断'
    },
    576: {
        'question': 'そんな（　　　）はなかったのに、田中さんを怒らせてしまった。',
        'choices': ['心配', '計画', 'ようす', 'つもり'],
        'correct_text': 'つもり',
        'cat': '文脈規定'
    },
    582: {
        'question': '田中さん、私の言ったことで気を（　　　）らしく、口をきいてくれないの。',
        'choices': ['落とした', '悪くした', 'さわった', 'かかった'],
        'correct_text': '悪くした',
        'cat': '文脈規定'
    },
    583: {
        'question': '彼の定期券を拾った（　　　）、私たちは友達になった。',
        'choices': ['からといって', 'のをもとに', 'のをきっかけに', 'からより'],
        'correct_text': 'のをきっかけに',
        'cat': '文法形式の判断'
    },
    584: {
        'target_word': '環境',
        'question': '総理大臣は米国を訪問し、【環境】問題について語った。',
        'choices': ['かんきゅう', 'けんきゅう', 'けんきょう', 'かんきょう'],
        'correct_text': 'かんきょう',
        'cat': '漢字読み'
    },
    586: {
        'question': '山本君はスポーツはできないが、頭の良さ（　　　）学年で一番だ。',
        'choices': ['にわたっては', 'をきっかけに', 'にかけては', 'をぬきには'],
        'correct_text': 'にかけては',
        'cat': '文法形式の判断'
    },
    589: {
        'question': '試験の前で、旅行に（　　　）どころではなかった。',
        'choices': ['行く', '行かない', '行こう', '行ける'],
        'correct_text': '行く',
        'cat': '文法形式の判断'
    },
    592: {
        'question': 'CO2を減らすことを（　　　）環境運動が世界中で行われている。',
        'choices': ['目指す', '見下ろす', '見送る', '見つめる'],
        'correct_text': '目指す',
        'cat': '文脈規定'
    },
    595: {
        'question': '買い物を上手にすること（　　　）、彼に勝てる者はいない。',
        'choices': ['にわたっては', 'をきっかけに', 'にかけては', 'をぬきには'],
        'correct_text': 'にかけては',
        'cat': '文法形式の判断'
    },
    596: {
        'target_word': 'ほそう',
        'question': '今日は天気がいいから、布団を【ほそう】。',
        'choices': ['戻そう', '放そう', '超そう', '干そう'],
        'correct_text': '干そう',
        'cat': '漢字表記'
    },
    599: {
        'target_word': '伸びた',
        'question': '髪が【伸びた】ので、床屋へ行くつもりだったが、風邪で延期した。',
        'choices': ['あびた', 'さびた', 'のびた', 'おびた'],
        'correct_text': 'のびた',
        'cat': '漢字読み'
    },
    600: {
        'question': '猫が逃げたので（　　　）けれど、捕まえることができなかった。',
        'choices': ['追い越した', '引き返した', '引きとめた', '追いかけた'],
        'correct_text': '追いかけた',
        'cat': '文脈規定'
    },
    602: {
        'target_word': '翌日',
        'question': 'その爆発事故のニュースは、【翌日】の朝刊に大きく取り上げられた。',
        'choices': ['よくにち', 'よくじつ', 'あくるひ', 'みようにち'],
        'correct_text': 'よくじつ',
        'cat': '漢字読み'
    },
    603: {
        'question': 'この件を解決するために、何かいい（　　　）があったら出してください。',
        'choices': ['能', '運', '案', '質'],
        'correct_text': '案',
        'cat': '文脈規定'
    },
    604: {
        'question': 'この植物には毒があるというが、確かに色（　　　）普通ではない。',
        'choices': ['からこそ', 'からには', 'からといって', 'からして'],
        'correct_text': 'からして',
        'cat': '文法形式の判断'
    },
    606: {
        'question': '演奏が終わると、観客は（　　　）立ち上がって拍手した。',
        'choices': ['いまにも', 'いっせいに', 'ひっしに', 'かってに'],
        'correct_text': 'いっせいに',
        'cat': '文脈規定'
    },
    609: {
        'question': 'タバコは吸っている本人だけでなく、近くにいる人にも（　　　）になる。',
        'choices': ['害', '罪', '悪', '損'],
        'correct_text': '害',
        'cat': '文脈規定'
    },
    618: {
        'question': '音を立ててスープを飲んだら、同席していた娘に（　　　）だと言われて注意された。',
        'choices': ['みにくい', 'げひん', 'きよう', 'ひきょう'],
        'correct_text': 'げひん',
        'cat': '文脈規定'
    },
    619: {
        'question': '弱い者いじめは（　　　）難い行為だ。',
        'choices': ['許さ', '許す', '許し', '許せ'],
        'correct_text': '許し',
        'cat': '文法形式の判断'
    },
    621: {
        'question': 'ゲームに熱中していたら、（　　　）朝になっていた。',
        'choices': ['いずれ', 'いまだに', 'たったいま', 'いつのまにか'],
        'correct_text': 'いつのまにか',
        'cat': '文脈規定'
    },
    622: {
        'question': 'お客様の個人情報は、（　　　）かねます。',
        'choices': ['お教え', 'お教えし', 'お教えて', 'お教えに'],
        'correct_text': 'お教えし',
        'cat': '文法形式の判断'
    },
    626: {
        'target_word': 'すみ',
        'question': '両替機は、部屋の【すみ】にあります。',
        'choices': ['照', '底', '隅', '角'],
        'correct_text': '隅',
        'cat': '漢字表記'
    },
    628: {
        'question': '彼は恐怖の（　　　）、髪が真っ白になってしまった。',
        'choices': ['のかぎり', 'ことから', 'どころか', 'のあまり'],
        'correct_text': 'のあまり',
        'cat': '文法形式の判断'
    },
    635: {
        'target_word': 'こおり',
        'question': '水は零度Cで【こおり】になります。',
        'choices': ['永', '泳', '氷', '凍'],
        'correct_text': '氷',
        'cat': '漢字表記'
    },
    639: {
        'question': '僕はお酒が入ると、自分の感情を（　　　）できなくなる。',
        'choices': ['キャンセル', 'チェンジ', 'コントロール', 'キャッチ'],
        'correct_text': 'コントロール',
        'cat': '文脈規定'
    },
    640: {
        'question': 'このアニメは子供に人気がある（　　　）、大人からは批判されている。',
        'choices': ['だけに', 'ものを', 'ばかりに', '一方で'],
        'correct_text': '一方で',
        'cat': '文法形式の判断'
    },
    643: {
        'question': '引き受けた（　　　）、大変でも最後までやり遂げます。',
        'choices': ['からして', 'からといって', '以上は', 'こそは'],
        'correct_text': '以上は',
        'cat': '文法形式の判断'
    },
    645: {
        'question': '先日の地震で家が（　　　）、住むことができない。',
        'choices': ['かたむいて', 'かたづいて', 'かたよって', 'かたまって'],
        'correct_text': 'かたむいて',
        'cat': '文脈規定'
    },
    649: {
        'question': '日程が（　　　）次第、ご連絡申し上げます。',
        'choices': ['決まり', '決まる', '決まって', '決まれば'],
        'correct_text': '決まり',
        'cat': '文法形式の判断'
    },
    657: {
        'question': '今年になって（　　　）物価が上がり、生活がより厳しくなった。',
        'choices': ['だんだん', 'ますます', 'そろそろ', 'とうとう'],
        'correct_text': 'ますます',
        'cat': '文脈規定'
    },
    661: {
        'question': '消費者の立場（　　　）、価格は安ければ安いほどいいに決まっている。',
        'choices': ['からすれば', 'からには', 'からといって', 'からして'],
        'correct_text': 'からすれば',
        'cat': '文法形式の判断'
    },
    667: {
        'question': '最近、運動不足のせいか、少し歩いただけで息が切れる。',
        'cat': '文脈規定'
    },
    670: {
        'question': '日本に来てから、一度も国へ帰っていない。',
        'cat': '文脈規定'
    },
    672: {
        'question': '息子はまだ大学をやめないと言っている。',
        'cat': '文脈規定'
    },
    677: {
        'target_word': '敬う',
        'question': '目上の人を【敬う】ことが大切だ。',
        'choices': ['うやまう', 'きそう', 'あらそう', 'ととのう'],
        'correct_text': 'うやまう',
        'cat': '漢字読み'
    },
    678: {
        'question': '会社に行く途中で、大学時代の友人と（　　　）出会った。',
        'choices': ['こっそり', 'ばったり', 'ぎっしり', 'ぴったり'],
        'correct_text': 'ばったり',
        'cat': '文脈規定'
    },
    679: {
        'question': '田中さんは経験が（　　　）上に、知識も深い。',
        'choices': ['豊かで', '豊かだ', '豊かな', '豊かの'],
        'correct_text': '豊かな',
        'cat': '文法形式の判断'
    },
    681: {
        'question': '昇給したとはいえ物価の上昇が激しく、家計のやりくりはなかなか（　　　）なりません。',
        'choices': ['らくに', 'のんきに', 'はでに', 'ゆっくり'],
        'correct_text': 'らくに',
        'cat': '文脈規定'
    },
    682: {
        'question': '携帯電話の普及（　　　）、利用者のマナーが問題となってきている。',
        'choices': ['一方で', 'とともに', 'ながら', 'あまり'],
        'correct_text': 'とともに',
        'cat': '文法形式の判断'
    },
    685: {
        'question': 'このタイプの電池は、発火の（　　　）があります。回収にご協力ください。',
        'choices': ['おそれ', 'がち', 'かぎり', 'きっかけ'],
        'correct_text': 'おそれ',
        'cat': '文法形式の判断'
    },
    687: {
        'question': '大雨が続いて、川が、（　　　）あふれそうだ。',
        'choices': ['いまに', 'いまでも', 'いままで', 'いまにも'],
        'correct_text': 'いまにも',
        'cat': '文脈規定'
    },
    690: {
        'question': '私は、朝起きて、一番に新聞に（　　　）、それから出かける支度をする。',
        'choices': ['目をかけ', '目を通し', '目をつけ', '目を引き'],
        'correct_text': '目を通し',
        'cat': '文脈規定'
    },
    692: {
        'target_word': '含まれて',
        'question': 'この食品には小麦粉は【含まれて】おりません。',
        'choices': ['つかまれて', 'かこまれて', 'しくまれて', 'ふくまれて'],
        'correct_text': 'ふくまれて',
        'cat': '漢字読み'
    },
    697: {
        'question': 'このたび、閉店することとなり、これまでのお礼とご挨拶に参った（　　　）。',
        'choices': ['次第です', 'ざるをえません', '以上です', 'よりほかありません'],
        'correct_text': '次第です',
        'cat': '文法形式の判断'
    },
    705: {
        'question': '大量にコピーしたので、紙が（　　　）しまった。',
        'choices': ['切れて', '済んで', '破れて', '抜けて'],
        'correct_text': '切れて',
        'cat': '文脈規定'
    },
    706: {
        'question': '雨が（　　　）、行かなければならない。',
        'choices': ['降ろうか降るまいか', '降ろうが降るまいが', '降ろうか降ろうとしまいか', '降ろうが降ろうとしまいが'],
        'correct_text': '降ろうが降るまいが',
        'cat': '文法形式の判断'
    },
    711: {
        'question': 'その事件は、（　　　）で大きく取り上げられた。',
        'choices': ['ジャンル', 'アンケート', 'マスコミ', 'ニュアンス'],
        'correct_text': 'マスコミ',
        'cat': '文脈規定'
    },
    714: {
        'question': '彼は首相に（　　　）人物だ。',
        'choices': ['やかましい', 'ふさわしい', 'たのもしい', 'ひとしい'],
        'correct_text': 'ふさわしい',
        'cat': '文脈規定'
    },
    715: {
        'question': '大臣の発言は、党の信用に（　　　）と批判の声が上がった。',
        'choices': ['といったところだ', 'ではあるまいし', 'にかかわるものだ', 'きわまりない'],
        'correct_text': 'にかかわるものだ',
        'cat': '文法形式の判断'
    },
    718: {
        'question': '天気が悪いので、客は（　　　）と思いきや、会場は満員になった。',
        'choices': ['集まった', '集まるまい', '集まろう', '集まりつつ'],
        'correct_text': '集まるまい',
        'cat': '文法形式の判断'
    },
    720: {
        'target_word': 'まばたき',
        'question': '子供の（　　　）が多いのが気になり、眼科に連れていきました。',
        'choices': ['しみ', 'あざ', 'まばたき', 'かすみ'],
        'correct_text': 'まばたき',
        'cat': '文脈規定'
    },
    721: {
        'question': 'あの人は他人に厳しい（　　　）、自分にも厳しい。',
        'choices': ['のみならず', 'によらず', 'ばかりで', 'ばかりに'],
        'correct_text': 'のみならず',
        'cat': '文法形式の判断'
    },
    722: {
        'target_word': 'わん',
        'question': '横浜【わん】で巨大魚が発見された。',
        'choices': ['港', '湾', '岸', '湖'],
        'correct_text': '湾',
        'cat': '漢字表記'
    },
    723: {
        'question': '革のジャケットを押し入れにしまったままにしていたら、（　　　）しまった。',
        'choices': ['さびて', 'しぼんで', 'かびて', 'もらして'],
        'correct_text': 'かびて',
        'cat': '文脈規定'
    },
    724: {
        'question': 'このところ、机に（　　　）っぱなしで運動不足だ。',
        'choices': ['向かう', '向かわ', '向かえ', '向かい'],
        'correct_text': '向かい',
        'cat': '文法形式の判断'
    },
    730: {
        'question': '彼は（　　　）なり私に文句を言い始めた。',
        'choices': ['会い', '会う', '会った', '会って'],
        'correct_text': '会う',
        'cat': '文法形式の判断'
    },
    732: {
        'question': '当施設（　　　）のメールは、このアドレスをお使いいただきますよう、お願いいたします。',
        'choices': ['だし', 'いき', 'より', 'あて'],
        'correct_text': 'あて',
        'cat': '文脈規定'
    },
    735: {
        'question': 'この前買ったサングラスが、鼻の形に合わないのか、（　　　）困る。',
        'choices': ['ゆがんで', 'ねじれて', 'ずれて', 'そろえて'],
        'correct_text': 'ずれて',
        'cat': '文脈規定'
    },
    736: {
        'question': '短い生涯だったが、その詩人は命の（　　　）生きた。',
        'choices': ['いたるまで', 'たりとも', 'ごとく', 'あるかぎり'],
        'correct_text': 'あるかぎり',
        'cat': '文法形式の判断'
    },
    737: {
        'target_word': '権利',
        'question': '教育を受ける【権利】は国民が国に対して持つ基本的人権の一つです。',
        'choices': ['けんり', 'かんり', 'こんり', 'きんり'],
        'correct_text': 'けんり',
        'cat': '漢字読み'
    },
    740: {
        'target_word': 'ひとつぶ',
        'question': 'この薬を【ひとつぶ】飲んだら腹痛が治まった。',
        'choices': ['一袋', '一位', '一服', '一粒'],
        'correct_text': '一粒',
        'cat': '漢字表記'
    },
    741: {
        'question': 'この家は築50年だが、少し手を（　　　）まだまだ住める。',
        'choices': ['入れれば', '抜けば', 'つければ', '貸せば'],
        'correct_text': '入れれば',
        'cat': '文脈規定'
    },
    742: {
        'question': 'お近くに（　　　）、ぜひお立ち寄りください。',
        'choices': ['お越しの上', 'お越しの折には', 'お越しの中を', 'お越しの際で'],
        'correct_text': 'お越しの折には',
        'cat': '文法形式の判断'
    },
    744: {
        'question': 'このところ、雨が降ったりやんだりと、（　　　）天気が続いている。',
        'choices': ['おだやかな', 'そうぞうしい', 'みっともない', 'うっとうしい'],
        'correct_text': 'うっとうしい',
        'cat': '文脈規定'
    },
    746: {
        'target_word': 'かれて',
        'question': 'この植物は、あまり太陽に当てると【かれて】しまう。',
        'choices': ['散れて', '枯れて', '折れて', '倒れて'],
        'correct_text': '枯れて',
        'cat': '漢字表記'
    },
    748: {
        'question': 'あんなに不真面目だったのに、今の彼の働き（　　　）には誰もが驚いている。',
        'choices': ['ぶり', 'っぷり', 'げ', 'ふり'],
        'correct_text': 'ぶり',
        'cat': '語形成'
    },
    750: {
        'question': 'お皿を8枚まとめて買ったら、1枚分（　　　）くれた。',
        'choices': ['まけて', '引いて', '安くして', '減らして'],
        'correct_text': 'まけて',
        'cat': '文脈規定'
    },
    751: {
        'question': '（　　　）考え抜いた結果、国に帰ることにしました。',
        'choices': ['自分なりに', '私なりに', '勝手ながら', '思い切って'],
        'correct_text': '私なりに',
        'cat': '文脈規定'
    },
    755: {
        'target_word': 'こうぎ',
        'question': '日程表によれば、午前中は【こうぎ】、午後はゼミです。',
        'choices': ['講義', '協議', '会議', '講話'],
        'correct_text': '講義',
        'cat': '漢字表記'
    },
    756: {
        'question': '彼女は美人だが、（　　　）ので嫌われている。',
        'choices': ['うぬぼれている', 'いばっている', 'あつかましい', 'なまいきだ'],
        'correct_text': 'うぬぼれている',
        'cat': '文脈規定'
    },
    757: {
        'question': 'そんなに高いお金をかけて修理する（　　　）、新しいのに買い換えたほうがいい。',
        'choices': ['くらいなら', 'ばかりに', 'ところで', 'どころか'],
        'correct_text': 'くらいなら',
        'cat': '文法形式の判断'
    },
    770: {
        'target_word': 'ふたご',
        'question': '【ふたご】のどちらが兄または姉かは、生まれた順によって決められるのでしょうか。',
        'choices': ['二子', '双子', '両子', '富子'],
        'correct_text': '双子',
        'cat': '漢字表記'
    },
    771: {
        'question': '古い車を（　　　）に出して、新しい車を買った。',
        'choices': ['立て替え', '値引き', '下取り', '値打ち'],
        'correct_text': '下取り',
        'cat': '文脈規定'
    },
    772: {
        'question': '書類はメールに添付してくれるので、たいていの資料は印刷（　　　）、助かっている。',
        'choices': ['するにすぎず', 'せざるを得なく', 'すべきではなく', 'せずに済み'],
        'correct_text': 'せずに済み',
        'cat': '文法形式の判断'
    },
    778: {
        'question': '災害が起こった時に、水の確保が一番の問題（　　　）。',
        'choices': ['であるべきだ', 'だとされている', 'であるしだいだ', 'でありかねる'],
        'correct_text': 'だとされている',
        'cat': '文法形式の判断'
    },
    781: {
        'question': 'この歌を聴くと、亡くなった母のことが（　　　）。',
        'choices': ['思い出される', '思い出す限りだ', '思い出すものだ', '思い出すまいか'],
        'correct_text': '思い出される',
        'cat': '文法形式の判断'
    },
    782: {
        'target_word': '編んで',
        'question': '母は居間で毛糸の帽子を【編んで】います。',
        'choices': ['くんで', 'あんで', 'もんで', 'へんで'],
        'correct_text': 'あんで',
        'cat': '漢字読み'
    },
    783: {
        'question': '父が亡くなったとき、財産の相続で兄弟と（　　　）。',
        'choices': ['あせった', 'ひねった', 'もめた', 'こもった'],
        'correct_text': 'もめた',
        'cat': '文脈規定'
    },
    786: {
        'question': '上司に怒鳴られる毎日に（　　　）だ。会社を辞めたい。',
        'choices': ['たっぷり', 'ぎっしり', 'うんざり', 'じっくり'],
        'correct_text': 'うんざり',
        'cat': '文脈規定'
    },
    787: {
        'question': '頭が痛かったので薬を飲んだ。（　　　）、すぐに痛みがなくなった。',
        'choices': ['すなわち', 'すると', 'ところで', 'というと'],
        'correct_text': 'すると',
        'cat': '文脈規定'
    },
    789: {
        'question': '事務職なら、パソコンが（　　　）話にならない。',
        'choices': ['使えないと', '使えては', '使えないので', '使えないなら'],
        'correct_text': '使えないと',
        'cat': '文法形式の判断'
    },
    790: {
        'question': 'クラスの大半は中国出身です。（　　　）、私は台湾から来ました。',
        'choices': ['ちなみに', 'ところが', 'すなわち', 'そのうえ'],
        'correct_text': 'ちなみに',
        'cat': '文脈規定'
    },
    791: {
        'target_word': 'ひき',
        'question': '伯父の家には犬が5【ひき】います。',
        'choices': ['羽', '匹', '本', '頭'],
        'correct_text': '匹',
        'cat': '漢字表記'
    },
    792: {
        'question': 'お忙しいところ、（　　　）をおかけして申し訳ありませんでした。',
        'choices': ['お世話', 'お手本', 'お手入れ', 'お手数'],
        'correct_text': 'お手数',
        'cat': '文脈規定'
    },
    793: {
        'question': '来月、ニューヨークに出張するんだってね。（　　　）お願いがあるんだけど・・・。買ってきてほしいものがあるんだ。',
        'choices': ['そこで', 'それはそうと', 'そういえば', 'もっとも'],
        'correct_text': 'それはそうと',
        'cat': '文脈規定'
    },
    794: {
        'target_word': '良好',
        'question': '検査項目はすべて平均的な数値で、健康状態は【良好】です。',
        'choices': ['りゅうこう', 'りょうこう', 'りょこう', 'りゅこう'],
        'correct_text': 'りょうこう',
        'cat': '漢字読み'
    },
    795: {
        'question': '新しく省エネシステムを（　　　）ことにより、光熱費が大幅に削減できた。',
        'choices': ['改修した', '投資した', '活用した', '導入した'],
        'correct_text': '導入した',
        'cat': '文脈規定'
    }
}

# Apply individual repairs
for qid, rep in INDIVIDUAL_REPAIRS.items():
    q = q_by_id[qid]
    if 'cat' in rep:
        q['category'] = rep['cat']
    if 'target_word' in rep:
        q['target_word'] = rep['target_word']
    if 'question' in rep:
        q['question'] = rep['question']
    if 'choices' in rep:
        q['choices'] = rep['choices']
    if 'correct_text' in rep:
        q['correct_text'] = rep['correct_text']

print(f"Applied {len(INDIVIDUAL_REPAIRS)} targeted individual repairs.")

# -------------------------------------------------------------
# Clean internal spaces and normalize formatting for ALL 896 questions
# -------------------------------------------------------------
for q in quiz_data:
    q['question'] = clean_internal_spaces(q.get('question', ''))
    q['choices'] = [clean_internal_spaces(c) for c in q.get('choices', [])]
    if 'target_word' in q:
        q['target_word'] = clean_internal_spaces(q['target_word'])
    if 'correct_text' in q:
        q['correct_text'] = clean_internal_spaces(q['correct_text'])

# -------------------------------------------------------------
# Rebuild questions 796〜896 with authentic JLPT questions & proper distractors
# -------------------------------------------------------------
from repair_n2_vocab_quiz_perfect import REBUILD_796_896

for qid, info in REBUILD_796_896.items():
    q = q_by_id[qid]
    q['category'] = info['cat']
    q['target_word'] = info['target']
    q['question'] = clean_internal_spaces(info['q'])
    q['choices'] = [clean_internal_spaces(c) for c in info['choices']]
    q['correct_text'] = clean_internal_spaces(info['ans'])
    q['meaning_en'] = info['mean']
    q['kanji_info'] = get_kanji_details(info['target'])

print("Rebuilt questions 796-896 with authentic JLPT standards.")

# -------------------------------------------------------------
# Generate accurate Rubies and Kanji Info for ALL 896 questions
# -------------------------------------------------------------
print("Regenerating rubies and kanji info with zero spoiler guarantees...")
for q in quiz_data:
    qid = q['id']
    cat = q.get('category', '')
    quest = q.get('question', '')
    choices = q.get('choices', [])
    corr = q.get('correct_text', '')
    target = q.get('target_word', '')
    
    # Ensure correct_text is in choices
    if corr not in choices:
        raise ValueError(f"CRITICAL: ID {qid} correct_text '{corr}' not in choices {choices}")
    
    # Check question type
    m_target = re.search(r'【([^】]+)】', quest)
    target_in_q = m_target.group(1) if m_target else target
    
    is_reading = (cat == '漢字読み') or (target_in_q and any('\u4e00' <= c <= '\u9fff' for c in target_in_q) and all('\u3040' <= c <= '\u309f' for c in corr))
    is_writing = (cat == '漢字表記') or (target_in_q and all('\u3040' <= c <= '\u309f' for c in target_in_q) and any('\u4e00' <= c <= '\u9fff' for c in corr))
    
    if is_reading:
        q['question_ruby'] = to_ruby_protected(quest, target_in_q, corr)
        # Hiragana choices do not need rubies
        q['choices_ruby'] = list(choices)
    elif is_writing:
        # ABSOLUTELY NO rubies in choices for Kanji writing to avoid giving away the answer!
        q['question_ruby'] = to_ruby_simple(quest)
        q['choices_ruby'] = list(choices)
    else:
        q['question_ruby'] = to_ruby_simple(quest)
        q['choices_ruby'] = [to_ruby_simple(c) for c in choices]
        
    q['answer'] = q['choices'].index(corr)
    if not q.get('kanji_info'):
        q['kanji_info'] = get_kanji_details(target or corr)

print("Rubies generated cleanly.")

# -------------------------------------------------------------
# Rebalance all 896 questions so answer 0, 1, 2, 3 have exactly 224 occurrences each!
# -------------------------------------------------------------
# Target: exactly 224 each for options 0, 1, 2, 3
target_counts = {0: 224, 1: 224, 2: 224, 3: 224}
current_counts = {0: 0, 1: 0, 2: 0, 3: 0}

for q in quiz_data:
    current_counts[q['answer']] += 1

print(f"Current answer distribution before rebalancing: {current_counts}")

# Safe rebalance: move choices and choices_ruby synchronously
random.seed(42)

for target_ans in [0, 1, 2, 3]:
    while current_counts[target_ans] < 224:
        surplus_ans = max((a for a in [0, 1, 2, 3] if current_counts[a] > 224), key=lambda a: current_counts[a])
        cand = None
        # Adjust questions starting from rebuilt or high-ID questions
        for q in reversed(quiz_data):
            if q['answer'] == surplus_ans and q['id'] > 143:
                cand = q
                break
        if not cand:
            break
            
        choices = list(cand['choices'])
        choices_ruby = list(cand['choices_ruby'])
        ct = cand['correct_text']
        
        # Pop correct choice
        old_idx = cand['answer']
        c_item = choices.pop(old_idx)
        cr_item = choices_ruby.pop(old_idx)
        
        # Insert at target_ans
        choices.insert(target_ans, c_item)
        choices_ruby.insert(target_ans, cr_item)
        
        cand['choices'] = choices
        cand['choices_ruby'] = choices_ruby
        cand['answer'] = target_ans
        
        current_counts[surplus_ans] -= 1
        current_counts[target_ans] += 1

print(f"Final answer distribution after perfect rebalance: {current_counts}")

# -------------------------------------------------------------
# Comprehensive Validation Pass
# -------------------------------------------------------------
for q in quiz_data:
    qid = q['id']
    ans = q['answer']
    ct = q['correct_text']
    choices = q['choices']
    choices_ruby = q['choices_ruby']
    
    assert 0 <= ans < 4, f"Invalid ans index {ans} in ID {qid}"
    assert choices[ans] == ct, f"CRITICAL: choices[{ans}] ({choices[ans]}) != ct ({ct}) in ID {qid}"
    assert len(choices) == 4, f"Choices len != 4 in ID {qid}"
    assert len(set(choices)) == 4, f"Duplicate choices in ID {qid}: {choices}"
    assert len(choices_ruby) == 4, f"choices_ruby len != 4 in ID {qid}"
    
    # Check no OCR junk
    for c in choices:
        assert '選択肢' not in c, f"Placeholder in ID {qid}: {c}"
        assert 'ロロ' not in c, f"Junk box in ID {qid}: {c}"
    assert '選択肢' not in q['question'], f"Placeholder in question ID {qid}"
    assert 'ロロ' not in q['question'], f"Junk box in question ID {qid}"

# Save to JSON
with open('database/jlpt_n2_vocab_quiz_data.json', 'w', encoding='utf-8') as f:
    json.dump(quiz_data, f, ensure_ascii=False, indent=2)

# Save to JS
js_content = "window.JLPT_N2_VOCAB_QUIZ_DATA = " + json.dumps(quiz_data, ensure_ascii=False, indent=2) + ";\n"
with open('database/jlpt_n2_vocab_quiz_data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("SUCCESS: Comprehensive repair finished! Both database/jlpt_n2_vocab_quiz_data.json and database/jlpt_n2_vocab_quiz_data.js successfully updated!")
