# -*- coding: utf-8 -*-
"""
Sanitize violent, terror, political, sensitive, wartime examples from database/jlpt_vocab_all.js
and update database/jlpt_kanji_data.js quiz references.
"""

import json

def sanitize_vocab():
    with open('database/jlpt_vocab_all.js', 'r', encoding='utf-8') as f:
        text = f.read()

    prefix = 'const JLPT_VOCAB = '
    suffix = ';'
    start_idx = text.find(prefix) + len(prefix)
    end_idx = text.rfind(suffix)

    vocab = json.loads(text[start_idx:end_idx].strip())

    for lvl in vocab:
        for w in vocab[lvl]:
            word = w.get('word', '')

            if word == '原爆':
                w['examples'] = [
                    {'ja': '広島の平和記念公園には、世界平和を願うモニュメントがあります。', 'en': 'In Hiroshima Peace Memorial Park, there is a monument praying for world peace.'},
                    {'ja': '平和記念資料館を訪れて、平和の大切さを学びました。', 'en': 'I visited the Peace Memorial Museum and learned the importance of peace.'}
                ]
            elif word == '植民地':
                w['examples'] = [
                    {'ja': 'かつての歴史や世界各国の独立について図書館で調べました。', 'en': 'I researched past history and the independence of various nations at the library.'},
                    {'ja': '世界史の授業で貿易の変遷について学びました。', 'en': 'In world history class, I learned about the transitions of trade.'}
                ]
            elif word == '侵略':
                w['examples'] = [
                    {'ja': '外来種の侵略によって地域の生態系が影響を受けています。', 'en': 'The local ecosystem is affected by the spread of invasive species.'},
                    {'ja': 'コンピュータウイルスによるネットワークへの侵入と侵略を防ぎます。', 'en': 'Prevent intrusion and compromise of the network by computer viruses.'}
                ]
            elif word == 'でたらめ':
                w['examples'] = [
                    {'ja': '根拠のないでたらめな噂を信じてはいけません。', 'en': 'You should not believe groundless, irresponsible rumors.'},
                    {'ja': '試験ででたらめな答えを書くわけにはいきません。', 'en': 'I cannot write random nonsense answers on the exam.'}
                ]
            elif word == '家主':
                w['examples'] = [
                    {'ja': '家主（大家さん）にアパートの契約更新について相談しました。', 'en': 'I consulted the landlord about the renewal of the apartment contract.'},
                    {'ja': '親切な家主のおかげで、安心して快適に暮らせています。', 'en': 'Thanks to the kind landlord, I live comfortably and with peace of mind.'}
                ]
            elif word == '元首':
                w['examples'] = [
                    {'ja': '国際会議で各国の元首が集まり、地球環境問題について話し合いました。', 'en': 'Heads of state from various countries gathered at the international conference to discuss global environmental issues.'},
                    {'ja': '大統領は国家の元首として公式な外交儀礼を行いました。', 'en': 'The president conducted official diplomatic ceremonies as the head of state.'}
                ]
            elif word == '携わる':
                w['examples'] = [
                    {'ja': '彼は長年、最先端の医療機器の開発に携わっています。', 'en': 'He has been involved in the development of cutting-edge medical devices for many years.'},
                    {'ja': '将来は教育や国際交流に携わる仕事をしたいと考えています。', 'en': 'In the future, I want to do work involved in education and international exchange.'}
                ]
            elif word == '暗殺':
                w['examples'] = [
                    {'ja': '歴史映画で、王の暗殺計画を未然に防ぐ騎士の物語を見ました。', 'en': 'I watched a historical film about a knight preventing an assassination plot against the king.'}
                ]

    new_code = f"// Comprehensive JLPT Vocabulary (N5-N1) in Gojuon (AIUEO) Order\nconst JLPT_VOCAB = {json.dumps(vocab, ensure_ascii=False)};\n"
    with open('database/jlpt_vocab_all.js', 'w', encoding='utf-8') as f:
        f.write(new_code)
    print("database/jlpt_vocab_all.js sanitized successfully!")

def sanitize_kanji_data():
    with open('database/jlpt_kanji_data.js', 'r', encoding='utf-8') as f:
        text = f.read().split('=', 1)[1].strip()
        if text.endswith(';'): text = text[:-1]
        data = json.loads(text)

    # In N1, update 爆 dailyQuizRef if it points to 原爆
    for k in data.get('N1', []):
        if k.get('character') == '爆':
            k['dailyQuizRef'] = {
                'level': 'N1',
                'day': 59,
                'qIndex': 4,
                'word': '爆発',
                'reading': 'ばくはつ'
            }
        elif k.get('character') == '植':
            k['dailyQuizRef'] = {
                'level': 'N1',
                'day': 36,
                'qIndex': 1,
                'word': '植える',
                'reading': 'うえる'
            }

    out_code = f"window.JLPT_KANJI_DATA = {json.dumps(data, ensure_ascii=False, indent=2)};\n"
    with open('database/jlpt_kanji_data.js', 'w', encoding='utf-8') as f:
        f.write(out_code)
    print("database/jlpt_kanji_data.js quiz refs sanitized!")

if __name__ == '__main__':
    sanitize_vocab()
    sanitize_kanji_data()
