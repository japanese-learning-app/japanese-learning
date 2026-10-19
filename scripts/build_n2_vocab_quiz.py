import json
import re
import os
import sys
import random

# Ensure scripts dir in path
sys.path.append('scripts')
import pykakasi
from fix_all_rubies import fix_rubies_in_text

print("=== Building Perfect JLPT N2 Vocab Quiz Dataset (896 Questions) ===")

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

print(f"Dictionary loaded: {len(dict_map)} entries.")

# Load master kanji database (13,000+ kanji with on/kun readings and meanings)
print("Loading master kanji database...")
with open('database/kanji_master.json', 'r', encoding='utf-8') as f:
    kanji_master = json.load(f)
print(f"Master kanji database loaded: {len(kanji_master)} kanji.")

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
    
    # Try reading as kana
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

def get_similar_list(target_term, extra_terms=None):
    clean_target = re.sub(r'[【】（）()]', '', target_term).strip()
    similars = []
    seen = set()

    # Extract kanji in target_term
    target_kanjis = [c for c in clean_target if '\u4e00' <= c <= '\u9fff']
    if not target_kanjis and len(clean_target) >= 2:
        for item in dict_raw:
            r = item.get('r', '')
            w = item.get('w', '')
            if r == clean_target and any('\u4e00' <= c <= '\u9fff' for c in w):
                target_kanjis = [c for c in w if '\u4e00' <= c <= '\u9fff']
                break
    
    # Priority 1: Words USING that kanji ("その漢字を使った単語")
    if target_kanjis:
        for k in target_kanjis:
            count_for_k = 0
            for w, entry in dict_map.items():
                if k in w and w != clean_target and 2 <= len(w) <= 6 and w not in seen:
                    r = entry.get('r', '')
                    m = '; '.join(entry.get('m', [])[:2]) if entry.get('m') else ''
                    similars.append({"term": w, "reading": r, "meaning": m})
                    seen.add(w)
                    count_for_k += 1
                    if count_for_k >= 3 or len(similars) >= 5:
                        break
            if len(similars) >= 5:
                break

    # Priority 2: Extra terms (collocations, choices)
    if len(similars) < 3 and extra_terms:
        for et in extra_terms:
            c_et = re.sub(r'[【】（）()◆・:\s]', '', et).strip()
            if c_et and c_et != clean_target and c_et not in seen and 2 <= len(c_et) <= 8 and not c_et.startswith('選択肢'):
                e_info = lookup_dict_info(c_et)
                if e_info["term"]:
                    similars.append(e_info)
                    seen.add(c_et)
                    if len(similars) >= 4:
                        break

    # Priority 3: Compounds starting or ending with target
    if len(similars) < 3 and len(clean_target) >= 2:
        for w, entry in dict_map.items():
            if len(similars) >= 4:
                break
            if w != clean_target and (w.startswith(clean_target) or w.endswith(clean_target)) and 2 <= len(w) <= 6:
                if w not in seen:
                    m_str = '; '.join(entry.get('m', [])[:2]) if entry.get('m') else ''
                    r_str = entry.get('r', '')
                    similars.append({"term": w, "reading": r_str, "meaning": m_str})
                    seen.add(w)

    return similars

# Ruby generator with target reading spoiler protection
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

# Natural Entity Replacement for Copyright Protection
REWRITE_ENTITIES = [
    ('山田さん', '佐藤さん'),
    ('田中さん', '高橋さん'),
    ('鈴木さん', '中村さん'),
    ('伊藤さん', '小林さん'),
    ('渡辺さん', '加藤さん'),
    ('吉田さん', '佐々木さん'),
    ('彼ら', 'チームの面々'),
    ('A国', 'フランス'),
    ('B国', 'カナダ'),
    ('東京', '横浜'),
    ('大阪', '神戸'),
    ('京都', '奈良'),
    ('北海道', '長野'),
    ('コンビニ', '駅前のカフェ'),
    ('スーパー', 'セレクトショップ'),
    ('アパート', 'マンション'),
    ('学校', '研修所'),
    ('工場', '研究所'),
]

def clean_sentence_text(s):
    if not s:
        return ""
    s = s.strip()
    s = re.sub(r'^[〇\d\.\s\-\–\—\(\)（）]+', '', s)
    s = re.sub(r'https?://\S+', '', s)
    s = re.sub(r'^\s*(もんだい|問題|第\d+週|\d+日目)\s*', '', s)
    s = re.sub(r'^言\s*い換え.*?[〇○]\s*', '', s)
    s = re.sub(r'^\s*言い換え類義問題\s*\d*\s*[\(（]?[例れ]?[\)）]?\s*[〇○]?\s*', '', s)
    s = re.sub(r'[ロ\u30ed]{2,}', '', s)
    s = re.sub(r'→.*$', '', s)
    s = re.sub(r'[\s\-]+[soN\d]+\s*$', '', s)
    s = re.sub(r'sN.*$', '', s)
    s = re.sub(r'\s+ご\s+い\s*$', '', s)
    s = re.sub(r'50無は', '50年前は', s)
    s = re.sub(r'忠学の', '中学の', s)
    s = re.sub(r'磨っていなさい', '座っていなさい', s)
    s = re.sub(r'[（\(][1-4\d]\s*$', '', s)
    s = re.sub(r'[■∞co•・\s]+$', '', s)
    s = re.sub(r'^[■∞co•・\s]+', '', s)
    # Collapse Japanese internal spaces from OCR
    s = re.sub(r'([ぁ-んァ-ヶ一-龥])\s+([ぁ-んァ-ヶ一-龥])', r'\1\2', s)
    s = re.sub(r'([ぁ-んァ-ヶ一-龥])\s+([ぁ-んァ-ヶ一-龥])', r'\1\2', s)
    for p in ['実際の業務において、', '今回の調査によると、', '事前の打ち合わせで、', '日常生活の中で、', '先輩からの助言によると、', '（　　　）に入る適切な表現を選びなさい：']:
        s = s.replace(p, '')
    for pat, repl in REWRITE_ENTITIES:
        s = s.replace(pat, repl)
    return s.strip()

# Target kanji matcher
def find_kanji_for_reading(sentence, reading):
    conv = kks.convert(sentence)
    n = len(conv)
    for length in range(1, 5):
        for i in range(n - length + 1):
            sub = conv[i:i+length]
            orig_comb = ''.join(x['orig'] for x in sub)
            hira_comb = ''.join(x['hira'] for x in sub)
            if not any('\u4e00' <= ch <= '\u9fff' for ch in orig_comb):
                continue
            if hira_comb == reading:
                return orig_comb
            h_clean = re.sub(r'[っつ]', '', hira_comb)
            r_clean = re.sub(r'[っつ]', '', reading)
            if h_clean == r_clean:
                return orig_comb
    
    SPECIAL_READINGS = {
        'はっぺん': '破片',
        'きびしい': '厳しい',
        'つづく': '続く',
        'もとづいて': '基づいて',
        'あらためる': '改める',
        'こたえる': '応える',
        'のぞいて': '除いて',
        'よごして': '汚して',
        'くばって': '配って',
        'すすめられて': '勧められて',
        'やぶれて': '破れて',
        'のべた': '述べた',
        'うすめた': '薄めた',
        'ゆか': '床',
        'みがく': '磨く',
        'ね': '根',
        'さつ': '札',
        'すがた': '姿',
        'げき': '劇',
        'もくぞう': '木造',
        'めじるし': '目印',
        'こうほ': '候補',
        'よぼう': '予防',
        'こうきょう': '公共',
        'じょうけい': '情景',
        'そうち': '装置',
        'かてい': '家庭',
        'あしこし': '足腰',
        'きんにく': '筋肉',
        'えいよう': '栄養',
        'あまい': '甘い',
        'つらい': '辛い',
        'かり': '仮',
        'やちん': '家賃',
        'こくばん': '黒板',
        'きせつ': '季節',
        'あせ': '汗',
        'ふで': '筆',
        'おさない': '幼い',
        'せまい': '狭い',
        'はたけ': '畑',
        'こうくう': '航空',
        'うちゅう': '宇宙',
        'おうしゅう': '欧州',
        'きしょう': '気象',
        'ほうりつ': '法律',
        'しょくよく': '食欲',
        'いのち': '命',
        'ちいき': '地域',
        'ぶたい': '舞台',
        'ふたご': '双子',
        'おおはば': '大幅',
        'ぬすまれた': '盗まれた',
        'めん': '綿',
        'かしこい': '賢い',
        'ぶつぞう': '仏像',
        'かんばん': '看板',
    }
    if reading in SPECIAL_READINGS:
        cand = SPECIAL_READINGS[reading]
        if cand in sentence:
            return cand

    kanji_words = re.findall(r'[\u4e00-\u9fff]+[ぁ-ん]*', sentence)
    for kw in kanji_words:
        kw_hira = ''.join(x['hira'] for x in kks.convert(kw))
        if kw_hira == reading or kw_hira.startswith(reading) or reading.startswith(kw_hira):
            return kw
    return None

# Exact target mappings for Doc1 類義語 (Paraphrases, 69 questions)
DOC1_SYNONYM_TARGETS = {
    304: ('飽きて', 0), # いやになって
    305: ('お手入れ', 2), # ケア
    306: ('最寄り', 1), # 近所の
    307: ('気配り', 3), # 思いやり
    308: ('勘違い', 3), # 思い込んで
    309: ('息抜き', 1), # 休むこと
    310: ('日頃', 3), # 普段
    311: ('素人', 0), # 初心者
    312: ('容姿', 1), # 見た目
    313: ('規模', 2), # 大きさ
    314: ('方針', 0), # 進む方向
    315: ('説得', 2), # 納得 させる
    316: ('加減', 0), # 調整 する
    317: ('後押し', 1), # 助けて
    318: ('通用する', 1), # 役に立つ
    319: ('検討', 3), # よく考える
    320: ('克服', 2), # 乗りこえた
    321: ('倒産', 3), # つぶれた
    322: ('依頼', 2), # お願いした
    323: ('出世', 0), # 地位が上がる
    324: ('ずらして', 1), # 変更して
    325: ('たばねる', 2), # まとめる
    326: ('あわてる', 3), # 急いでする
    327: ('つとめて', 0), # 努力して
    328: ('寄せる', 1), # 集める
    329: ('もちいる', 3), # 使う
    330: ('わく', 0), # 出る
    331: ('縮める', 1), # 短くする
    332: ('含める', 0), # 入れる
    333: ('埋まっている', 2), # いっぱいだ
    334: ('問い合わせる', 3), # 確かめる
    335: ('洗い出す', 0), # あきらかにする
    336: ('追い返した', 1), # 帰らせた
    337: ('引き返した', 3), # 来た道をもどった
    338: ('たくましい', 0), # 強そうな
    339: ('くどい', 1), # しつこい
    340: ('思いがけない', 2), # 意外な
    341: ('おとなしい', 3), # しずかな
    342: ('ものたりない', 2), # 満足できない
    343: ('非凡', 3), # すばらしい
    344: ('あいまい', 0), # はっきりしない
    345: ('的確な', 1), # 明確な
    346: ('余計な', 2), # 不必要な
    347: ('物騒な', 1), # 危険な
    348: ('深刻な', 0), # 厳しい
    349: ('円満な', 1), # おだやかな
    350: ('見事な', 0), # りっぱな
    351: ('あわれな', 2), # かわいそうな
    352: ('わずかな', 3), # 小さい
    353: ('のんびり', 2), # ゆっくりしたい
    354: ('よほど', 0), # とても
    355: ('着々と', 2), # 止まらずに
    356: ('おそらく', 1), # たぶん
    357: ('当分', 0), # しばらく
    358: ('あらゆる', 1), # 全ての
    359: ('案外', 2), # 思ったより
    360: ('たまたま', 1), # 偶然
    361: ('要するに', 0), # つまり
    362: ('しばしば', 2), # 何度も
    363: ('ほっと', 0), # 安心
    364: ('ばったり', 1), # 偶然
    365: ('じたばた', 3), # あわてても
    366: ('はらはら', 0), # 心配
    367: ('ざっと', 1), # だいたい
    368: ('プロセス', 2), # 過程
    369: ('ムード', 0), # ふんいき
    370: ('ナイター', 1), # 夜の試合
    371: ('スペース', 2), # 空間
    372: ('フレッシュな', 0), # 新鮮 な
}

DOC1_SPECIAL_OVERRIDE = {
    76: {'q': 'たくさん食べて【おなか】がいっぱいになった。', 'ans': 0, 'tgt': 'お腹'},
    83: {'q': '新しくできたケーキ屋さんは【ひょうばん】が良い。', 'ans': 2, 'tgt': '評判'},
    93: {'q': 'この研修所の【でんとう】は今も守られている。', 'ans': 0, 'tgt': '伝統'},
    103: {'q': '商品の【きんがく】を確認する。', 'ans': 1, 'tgt': '金額'},
}

all_quiz_questions = []

# ==========================================
# 1. PROCESS DOC1 (436 questions)
# ==========================================
print("Processing Doc1 questions (合格するN2)...")
with open('/tmp/doc1_clean_parsed.json', 'r', encoding='utf-8') as f:
    doc1_items = json.load(f)

for idx, it in enumerate(doc1_items):
    q_id = idx + 1
    sec = it.get("section", "語彙")
    orig_s = clean_sentence_text(it.get("sentence", ""))
    choices = it.get("choices", [])
    ans_1b = it.get("answer", 1)
    ans_0b = max(0, min(len(choices)-1, ans_1b - 1))
    corr_choice = choices[ans_0b] if ans_0b < len(choices) else ""
    
    target_word = it.get("target_word", "")
    target_kanji = None
    target_reading = None
    adapted_q = orig_s

    if q_id in DOC1_SPECIAL_OVERRIDE:
        sp = DOC1_SPECIAL_OVERRIDE[q_id]
        adapted_q = sp['q']
        ans_0b = sp['ans']
        corr_choice = choices[ans_0b]
        target_word = sp['tgt']

    elif q_id in DOC1_SYNONYM_TARGETS:
        s_tgt, s_ans = DOC1_SYNONYM_TARGETS[q_id]
        ans_0b = s_ans
        corr_choice = choices[ans_0b]
        target_word = s_tgt
        if s_tgt in orig_s:
            adapted_q = orig_s.replace(s_tgt, f"【{s_tgt}】", 1)
        else:
            adapted_q = f"【{s_tgt}】：{orig_s}"

    elif sec == "漢字読み":
        target_reading = corr_choice
        target_kanji = find_kanji_for_reading(orig_s, corr_choice)
        if target_kanji and target_kanji in orig_s:
            adapted_q = orig_s.replace(target_kanji, f"【{target_kanji}】", 1)
            target_word = target_kanji
        else:
            target_word = corr_choice
            adapted_q = orig_s
    elif sec == "漢字表記":
        target_word = corr_choice
        cand_kana = ''.join(x['hira'] for x in kks.convert(corr_choice))
        if cand_kana and cand_kana in orig_s:
            adapted_q = orig_s.replace(cand_kana, f"【{cand_kana}】", 1)
        else:
            kanas = re.findall(r'[ぁ-ん]{2,}', orig_s)
            matched = False
            for k_w in kanas:
                if k_w in cand_kana or cand_kana in k_w:
                    adapted_q = orig_s.replace(k_w, f"【{k_w}】", 1)
                    matched = True
                    break
            if not matched and kanas:
                adapted_q = orig_s.replace(kanas[0], f"【{kanas[0]}】", 1)

    elif sec in ["語形成", "文脈規定"]:
        target_word = corr_choice
        if '（　　　）' not in adapted_q:
            if re.search(r'[（\(]\s*[）\)]', adapted_q):
                adapted_q = re.sub(r'[（\(]\s*[）\)]', '（　　　）', adapted_q)
            elif target_word and target_word in adapted_q:
                adapted_q = adapted_q.replace(target_word, '（　　　）', 1)
            else:
                adapted_q = adapted_q + '（　　　）'
    elif sec == "類義語":
        target_word = it.get("target_word", corr_choice)
        if '【' not in adapted_q and target_word in adapted_q:
            adapted_q = adapted_q.replace(target_word, f"【{target_word}】", 1)
    elif sec == "語彙用法":
        target_word = it.get("target_word", corr_choice)
        adapted_q = f"次の言葉の使い方が最も適切な文を選びなさい：【{target_word}】"

    q_ruby = to_ruby_protected(adapted_q, target_kanji, target_reading)
    choices_ruby = [to_ruby_protected(c) for c in choices]

    extra_terms = [c for c in choices if c != corr_choice]
    similar_data = get_similar_list(target_word or corr_choice, extra_terms)

    dict_info = lookup_dict_info(target_word or corr_choice)
    meaning_en = dict_info.get("meaning", "")
    kanji_details = get_kanji_details(target_word or corr_choice)
    
    all_quiz_questions.append({
        "id": len(all_quiz_questions) + 1,
        "source": "合格するN2 (徹底演習編)",
        "category": sec,
        "target_word": target_word or corr_choice,
        "question": adapted_q,
        "question_ruby": q_ruby,
        "choices": choices,
        "choices_ruby": choices_ruby,
        "answer": ans_0b,
        "correct_text": corr_choice,
        "meaning_en": meaning_en,
        "explanation": "",
        "kanji_info": kanji_details,
        "similar": similar_data
    })

print(f"Doc1 finished: {len(all_quiz_questions)} questions.")

# ==========================================
# 2. PROCESS DOC2 Days 1-6 (360 questions)
# ==========================================
print("Processing Doc2 Days 1-6 boxes (新にほんご500問 N2)...")
with open('/tmp/doc2_boxes_days1_6.json', 'r', encoding='utf-8') as f:
    doc2_boxes = json.load(f)

# Explicit verified overrides for OCR layout and split boxes
DOC2_OVERRIDES = {
    15: {'q': '娘は七歳の誕生日のお【祝い】に貯金箱をもらいました。', 'c': ['おいわい', 'おみあい', 'おゆわい', 'おにあい'], 'a': 0, 'w': '祝い', 'tgt': '祝い', 'r': 'おいわい'},
    30: {'q': '建設中のビルのパネルが歩道に【倒れ】、歩いていた人が死亡した。', 'c': ['たおれ', 'こわれ', 'われ', 'やぶれ'], 'a': 0, 'w': '倒れ', 'tgt': '倒れ', 'r': 'たおれ'},
    33: {'q': 'あの人はめったに【怒らない】。', 'c': ['怒らない', '努らない', '起こらない', '怖こらない'], 'a': 0, 'w': '怒らない', 'tgt': '怒らない'},
    48: {'q': '【あせ】が出てきた。', 'c': ['汁', '汗', '涙', '油'], 'a': 1, 'w': '汗', 'tgt': '汗', 'r': 'あせ'},
    61: {'q': '妹はあめやらガムやら（　　　）何かを口に入れている。', 'c': ['うんと', 'じょじょに', 'ぞくぞくと', 'たえず'], 'a': 3, 'w': 'たえず', 'tgt': 'たえず'},
    63: {'q': 'お母さん、お湯が【沸いた】よ。', 'c': ['沸いた', '浮いた', '乾いた', '蒸いた'], 'a': 0, 'w': '沸いた', 'tgt': '沸いた'},
    73: {'q': '買ったところに（　　　）を言った方がいいんじゃない？', 'c': ['コメント', 'クレーム', '口コミ', 'イメージ'], 'a': 1, 'w': 'クレーム', 'tgt': 'クレーム'},
    76: {'q': 'この椅子、デザインは（　　　）けれど、すわり心地があんまりよくないね。', 'c': ['けっている', 'こっている', 'もっている', 'そっている'], 'a': 1, 'w': 'こっている', 'tgt': 'こっている'},
    87: {'q': '警察は【盗まれた】絵画と犯人を捜している。', 'c': ['ねすまれた', 'ぬすまれた', 'なすまれた', 'にすまれた'], 'a': 1, 'w': 'ぬすまれた', 'tgt': '盗まれた', 'r': 'ぬすまれた'},
    93: {'q': '1分は60【びょう】です。', 'c': ['秒', '億', '表', '兆'], 'a': 0, 'w': '秒', 'tgt': '秒'},
    99: {'q': 'このシャツは【めん】100%です。', 'c': ['面', '綿', '革', '絹'], 'a': 1, 'w': '綿', 'tgt': '綿', 'r': 'めん'},
    100: {'q': '親の言うことに（　　　）、長男は家を出て行ってしまった。', 'c': ['せめて', 'もめて', 'ぶつかって', 'さからって'], 'a': 3, 'w': 'さからって', 'tgt': 'さからって'},
    105: {'q': 'その警官は、人々から頼られる、【勇気】のある男性でした。', 'c': ['ゆうき', 'ようき', 'にんき', 'こんき'], 'a': 0, 'w': 'ゆうき', 'tgt': '勇気', 'r': 'ゆうき'},
    107: {'q': '状況を説明したいのだが、電話では説明（　　　）。', 'c': ['ほかない', 'わけがない', 'しかない', 'しようがない'], 'a': 3, 'w': 'しようがない', 'tgt': 'しようがない'},
    124: {'q': 'この仕事を（　　　）しないと、落ち着いて食事もできない。', 'c': ['なんとも', 'なにかと', 'なにより', 'なんとか'], 'a': 3, 'w': 'なんとか', 'tgt': 'なんとか'},
    126: {'q': 'もう一人、社員を【雇おう】。', 'c': ['やとおう', 'すくおう', 'うらなおう', 'うかがおう'], 'a': 0, 'w': 'やとおう', 'tgt': '雇おう', 'r': 'やとおう'},
    134: {'q': '社員募集。年齢・性別・経験の有無（　　　）採用します。', 'c': ['をとわず', 'をきっかけに', 'をこめて', 'をかぎりに'], 'a': 0, 'w': 'をとわず', 'tgt': 'をとわず'},
    154: {'q': 'どうしたんだろう。家の前に人が（　　　）いるよ。', 'c': ['おおぜい', 'おおいに', 'おおよそ', 'おおくに'], 'a': 0, 'w': 'おおぜい', 'tgt': 'おおぜい'},
    156: {'q': '準備が【整い】次第、運転を再開します。', 'c': ['ととのい', 'いきおい', 'おこない', 'うたがい'], 'a': 0, 'w': 'ととのい', 'tgt': '整い', 'r': 'ととのい'},
    159: {'q': '今日は天気がいいから、布団を【干そう】。', 'c': ['干そう', '放そう', '超そう', '戻そう'], 'a': 0, 'w': '干そう', 'tgt': '干そう'},
    168: {'q': '名前や住所を【とうろく】した。', 'c': ['登録', '依頼', '変更', '申告'], 'a': 0, 'w': '登録', 'tgt': '登録'},
    175: {'q': 'この夏の（　　　）に、ヨーロッパ旅行をしようと思っています。', 'c': ['休養', '休憩', '休息', '休暇'], 'a': 3, 'w': '休暇', 'tgt': '休暇'},
    177: {'q': '老人や【児童】をねらった犯罪が増えている。', 'c': ['じどう', 'にどう', 'ようじ', 'しょうに'], 'a': 0, 'w': 'じどう', 'tgt': '児童', 'r': 'じどう'},
    186: {'q': '【お互い】に頑張って目標を達成しよう。', 'c': ['おたがい', 'おかだい', 'おがない', 'おながい'], 'a': 0, 'w': 'おたがい', 'tgt': 'お互い', 'r': 'おたがい'},
    217: {'q': '時間がないので、詳しい説明は（　　　）。', 'c': ['はぶきます', 'うしないます', 'はずします', 'なやみます'], 'a': 0, 'w': 'はぶきます', 'tgt': 'はぶきます'},
    225: {'q': '申込書は例を参考に記入し、【封筒】に入れて担当者に渡して下さい。', 'c': ['ふうとう', 'ふっとう', 'ふうどう', 'ふとう'], 'a': 0, 'w': 'ふうとう', 'tgt': '封筒', 'r': 'ふうとう'},
    231: {'q': 'A「裏口の【戸】を閉め忘れたから、閉めといて。」 B「了解。」', 'c': ['と', 'こ', 'ど', 'ご'], 'a': 0, 'w': 'と', 'tgt': '戸', 'r': 'と'},
    239: {'q': '明日の行事が行われるかどうかは、天気（　　　）。', 'c': ['に応じる', 'に伴う', '次第だ', '限りだ'], 'a': 2, 'w': '次第だ', 'tgt': '次第だ'},
    240: {'q': '上司を【敬え】。', 'c': ['うやまう', 'きそう', 'あらそう', 'ととのう'], 'a': 0, 'w': 'うやまう', 'tgt': '敬え', 'r': 'うやまう'},
    246: {'q': '【貿易】の専門学校に行きたいと言うと、両親は賛成してくれた。', 'c': ['ぼうえき', 'ぼえき', 'ぼいき', 'ぼういき'], 'a': 0, 'w': 'ぼうえき', 'tgt': '貿易', 'r': 'ぼうえき'},
    247: {'q': '私は（　　　）から、何をするにも時間がかかる。', 'c': ['納得がいかない', '要領が悪い', '手間になる', 'まねをする'], 'a': 1, 'w': '要領が悪い', 'tgt': '要領が悪い'},
    249: {'q': '庭の木を切るのはいいが、切った枝を片付けるのが【めんどう】だ。', 'c': ['面倒', '面到', '面堂', '面道'], 'a': 0, 'w': '面倒', 'tgt': '面倒'},
    270: {'q': '劇場には【抱え】きれないほどの花束や贈り物が届いていた。', 'c': ['かかえ', 'ささえ', 'たたえ', 'ひかえ'], 'a': 0, 'w': 'かかえ', 'tgt': '抱え', 'r': 'かかえ'},
    280: {'q': 'あ、また計算を間違えた。今日はなんだか頭が（　　　）するなあ。', 'c': ['ぼうっと', 'しいんと', 'ちらっと', 'さっさと'], 'a': 0, 'w': 'ぼうっと', 'tgt': 'ぼうっと'},
    306: {'q': '評判を信じて買った商品が期待外れで、【損】をした。', 'c': ['そん', 'いん', 'けん', 'すん'], 'a': 0, 'w': 'そん', 'tgt': '損', 'r': 'そん'},
    315: {'q': 'この塔も、中の【仏像】も、9世紀に完成したものらしい。', 'c': ['ぶつぞう', 'ふつぞう', 'ぶっしょう', 'ほとけ'], 'a': 0, 'w': 'ぶつぞう', 'tgt': '仏像', 'r': 'ぶつぞう'},
    321: {'q': '中央改札口は込み合いますから、その少し横のほうでお名前を書いた【看板】を持って立っています。', 'c': ['かんばん', 'かんぱん', 'まないた', 'なふだ'], 'a': 0, 'w': 'かんばん', 'tgt': '看板', 'r': 'かんばん'},
    342: {'q': '単純な手続きミスで志望校を受験する機会を逃すなんて、【賢い】人のやることだろうか。', 'c': ['かしこい', 'あやうい', 'おさない', 'しつこい'], 'a': 0, 'w': 'かしこい', 'tgt': '賢い', 'r': 'かしこい'}
}

def clean_choice_val(v):
    v = re.sub(r'[ロ\u30ed]{2,}.*$', '', v)
    v = re.sub(r'[\s\-]+[soN\d]+\s*$', '', v)
    v = re.sub(r'[■∞co•・\s]+$', '', v)
    return v.strip()

def extract_doc2_choices(lines):
    choices = {}
    i = 0
    while i < len(lines):
        l = lines[i].strip()
        if re.search(r'第\d+週|もんだい|\d+日目|ロロロ', l):
            i += 1
            continue
        m = re.match(r'^([1-4])\s*([^\d,，ロ\u30ed\s].*)', l)
        if m:
            num = int(m.group(1))
            val = clean_choice_val(m.group(2))
            if num not in choices and val:
                choices[num] = val
        else:
            m_d = re.match(r'^([1-4])$', l)
            if m_d and i + 1 < len(lines):
                num = int(m_d.group(1))
                nl = lines[i+1].strip()
                if not re.match(r'^[1-4]', nl) and not re.search(r'第\d+週|もんだい|\d+日目|ロロロ', nl):
                    val = clean_choice_val(nl)
                    if num not in choices and val:
                        choices[num] = val
                        i += 1
        i += 1
    if len(choices) == 3 and 4 not in choices:
        for l in lines:
            m_b = re.match(r'^[•・\-]\s*(.*)', l.strip())
            if m_b:
                val = clean_choice_val(m_b.group(1))
                if val:
                    choices[4] = val
                    break
    choice_list = [choices.get(n, f'選択肢{n}') for n in [1, 2, 3, 4]]
    return choice_list

for idx, box in enumerate(doc2_boxes):
    sec = box.get("sectionType", "語彙")
    ql = box.get("questionLines", [])
    al = box.get("answerLines", [])
    week = box.get("week", 1)
    day = box.get("day", 1)

    if idx in DOC2_OVERRIDES:
        ov = DOC2_OVERRIDES[idx]
        adapted_q = ov['q']
        choices = ov['c']
        ans_0b = ov['a']
        corr_choice = choices[ans_0b]
        target_word = ov.get('tgt', corr_choice)
        target_kanji = ov.get('tgt') if 'r' in ov else None
        target_reading = ov.get('r')
        eng_trans = ""
    else:
        choices = extract_doc2_choices(ql)
        
        # Determine correct answer from AL
        al_text = ' '.join(l.strip() for l in al if not re.search(r'[a-zA-Z]{4,}', l) and not any(sym in l for sym in ['◆', '・', ':']) and l.strip() not in ['こたえ', 'い', 'OK'])
        m_al = re.search(r'([1-4])\s*([^\d\s][^。？！\?]*[。？！\?])', al_text)
        
        ans_num = 1
        al_full_sent = ""
        if m_al:
            ans_num = int(m_al.group(1))
            al_full_sent = m_al.group(2).strip()
        else:
            for al_l in al:
                m_a = re.match(r'^([1-4])\s*(.*)', al_l.strip())
                if m_a and len(al_l.strip()) > 3:
                    ans_num = int(m_a.group(1))
                    break

        found_in_sent = [c_i for c_i, c in enumerate(choices) if len(c) >= 2 and c in al_text and not c.startswith('選択肢')]
        if len(found_in_sent) == 1:
            ans_0b = found_in_sent[0]
        else:
            ans_0b = max(0, min(3, ans_num - 1))

        corr_choice = choices[ans_0b] if ans_0b < len(choices) else choices[0]

        # Extract sentence before and after choices from QL
        before = []
        after = []
        seen_choice = False
        for l in ql:
            l_s = l.strip()
            if re.search(r'第\d+週|もんだい|\d+日目|ロロロ', l_s):
                continue
            has_sent_punct = bool(re.search(r'[。？！\?]', l_s))
            is_choice_start = (re.match(r'^[1-4](\s|[^\d\w]|$)', l_s) or re.match(r'^[1-4][ぁ-んァ-ヶ一-龥]', l_s)) and not has_sent_punct
            if is_choice_start:
                seen_choice = True
            elif not seen_choice:
                cl = clean_sentence_text(l_s)
                if cl: before.append(cl)
            else:
                cl = clean_sentence_text(l_s)
                if cl and not re.match(r'^[•・\-]', cl): after.append(cl)

        s_before = ' '.join(before).strip()
        s_after = ' '.join(after).strip()

        target_kanji = None
        target_reading = None
        target_word = corr_choice

        if sec == "文字":
            full_s = clean_sentence_text(f"{s_before} {s_after}".strip())
            is_reading = all(not any('\u4e00' <= c <= '\u9fff' for c in c_item) for c_item in choices if not c_item.startswith('選択肢'))
            if is_reading:
                target_reading = corr_choice
                target_kanji = find_kanji_for_reading(full_s, corr_choice)
                if target_kanji and target_kanji in full_s:
                    adapted_q = full_s.replace(target_kanji, f"【{target_kanji}】", 1)
                    target_word = target_kanji
                else:
                    target_word = corr_choice
                    adapted_q = full_s
            else:
                cand_kana = ''.join(x['hira'] for x in kks.convert(corr_choice))
                if cand_kana and cand_kana in full_s:
                    adapted_q = full_s.replace(cand_kana, f"【{cand_kana}】", 1)
                    target_word = corr_choice
                else:
                    kanas = re.findall(r'[ぁ-ん]{2,}', full_s)
                    if kanas:
                        adapted_q = full_s.replace(kanas[0], f"【{kanas[0]}】", 1)
                    else:
                        adapted_q = full_s
                    target_word = corr_choice
        else:
            clean_al = clean_sentence_text(al_full_sent)
            if clean_al and corr_choice and corr_choice in clean_al:
                adapted_q = clean_al.replace(corr_choice, '（　　　）', 1)
            elif s_before and s_after:
                adapted_q = f"{s_before}（　　　）{s_after}"
            elif s_before:
                adapted_q = f"{s_before}（　　　）"
            elif s_after:
                adapted_q = f"（　　　）{s_after}"
            else:
                adapted_q = clean_al or "（　　　）"

        eng_trans = ""
        for al_l in al:
            al_clean = al_l.strip()
            if re.search(r'[a-zA-Z]{4,}', al_clean) and not eng_trans:
                eng_trans = al_clean.split('/')[0].strip()

    q_ruby = to_ruby_protected(adapted_q, target_kanji, target_reading)
    choices_ruby = [to_ruby_protected(c) for c in choices]

    similar_data = get_similar_list(target_word or corr_choice, choices)

    dict_info = lookup_dict_info(target_word or corr_choice)
    meaning_en = eng_trans or dict_info.get("meaning", "")
    kanji_details = get_kanji_details(target_word or corr_choice)

    all_quiz_questions.append({
        "id": len(all_quiz_questions) + 1,
        "source": "新にほんご500問 N2",
        "category": f"{sec}（Week {week} Day {day}）",
        "target_word": target_word or corr_choice,
        "question": adapted_q,
        "question_ruby": q_ruby,
        "choices": choices,
        "choices_ruby": choices_ruby,
        "answer": ans_0b,
        "correct_text": corr_choice,
        "meaning_en": meaning_en,
        "explanation": "",
        "kanji_info": kanji_details,
        "similar": similar_data
    })

print(f"Doc2 Days 1-6 finished: {len(all_quiz_questions)} questions total.")

# ==========================================
# 3. PROCESS TOP-QUALITY N2 PRACTICE QUESTIONS (100 Questions)
# ==========================================
target_total = 896
needed_count = target_total - len(all_quiz_questions)
print(f"Generating {needed_count} curated N2 practice questions to reach exactly {target_total}...")

with open('database/jlpt_n2_vocab_full_data.js', 'r', encoding='utf-8') as f:
    v_js = f.read()

m_v = re.search(r'window\.JLPT_N2_VOCAB_DATA\s*=\s*(\[.*?\]);?\s*$', v_js, re.DOTALL)
all_vocab = json.loads(m_v.group(1))

# Filter ONLY authentic genuine sentences (strictly exclude dummy template entries)
genuine_vocab = []
for item in all_vocab:
    ex = item.get('ex_ja', '')
    clean_ex = re.sub(r'<rt>.*?</rt>', '', ex)
    clean_ex = re.sub(r'</?ruby>', '', clean_ex)
    if any(dummy in clean_ex for dummy in ['詳しく教えていただけますか', 'こちらの', 'ご説明いたしますね']):
        continue
    if len(clean_ex) >= 20:
        genuine_vocab.append(item)

print(f"Found {len(genuine_vocab)} genuine rich vocabulary entries.")

# Pools for sensible distractors
katakana_pool = [v['word'] for v in genuine_vocab if re.match(r'^[ァ-ヴー]+$', v['word'])]
nouns_2k = [v['word'] for v in genuine_vocab if len(v['word']) == 2 and all('\u4e00' <= c <= '\u9fff' for c in v['word'])]
verbs = [v['word'] for v in genuine_vocab if v['word'].endswith(('る', 'す', 'く', 'ぐ', 'つ', 'ぬ', 'ぶ', 'む', 'う')) and any('\u4e00' <= c <= '\u9fff' for c in v['word'])]
adjs_i = [v['word'] for v in genuine_vocab if v['word'].endswith('い') and any('\u4e00' <= c <= '\u9fff' for c in v['word'])]
adverbs = [v['word'] for v in genuine_vocab if v.get('category') == '副詞' or v['word'].endswith(('と', 'り'))]

random.seed(42)

added_curated = 0
vocab_cursor = 10

while added_curated < needed_count and vocab_cursor < len(genuine_vocab):
    v = genuine_vocab[vocab_cursor]
    vocab_cursor += 1

    w = v.get('word', '')
    r = v.get('reading', '')
    ex = v.get('ex_ja', '')
    m_en = v.get('meaning_en') or ''

    if not w or not r or not ex or len(w) > 6:
        continue

    # Clean sentence
    clean_ex = re.sub(r'<rt>.*?</rt>', '', ex)
    clean_ex = re.sub(r'</?ruby>', '', clean_ex).strip()
    lines = [l.strip() for l in clean_ex.split('\n') if l.strip()]
    if not lines:
        continue

    target_line = lines[0]
    target_line = re.sub(r'^[AB]:\s*[「\"]?', '', target_line)
    target_line = re.sub(r'[」\"]?$', '', target_line).strip()

    if w not in target_line or len(target_line) < 12:
        continue

    q_mode = added_curated % 3
    target_kanji = None
    target_reading = None
    
    if q_mode == 0:
        # Fill in blank
        adapted_q = target_line.replace(w, '（　　　）', 1)
        target_word = w
        if re.match(r'^[ァ-ヴー]+$', w):
            pool = [x for x in katakana_pool if x != w]
        elif w in nouns_2k:
            pool = [x for x in nouns_2k if x != w]
        elif w in verbs:
            pool = [x for x in verbs if x != w]
        elif w in adjs_i:
            pool = [x for x in adjs_i if x != w]
        elif w in adverbs:
            pool = [x for x in adverbs if x != w]
        else:
            pool = [x['word'] for x in genuine_vocab if x['word'] != w and len(x['word']) == len(w)]
        distractors = random.sample(pool, min(3, len(pool)))
        choices = [w] + distractors
        random.shuffle(choices)
        ans_0b = choices.index(w)
        corr_choice = w
        sec_name = "語彙（実戦演習）"

    elif q_mode == 1 and any('\u4e00' <= ch <= '\u9fff' for ch in w):
        # Kanji reading
        adapted_q = target_line.replace(w, f"【{w}】", 1)
        target_word = w
        target_kanji = w
        target_reading = r
        r_pool = []
        for cand in genuine_vocab:
            cr = cand.get('reading', '')
            if cr and cr != r and abs(len(cr) - len(r)) <= 1:
                r_pool.append(cr)
        distractors = random.sample(r_pool, min(3, len(r_pool)))
        choices = [r] + distractors
        random.shuffle(choices)
        ans_0b = choices.index(r)
        corr_choice = r
        sec_name = "漢字読み（実戦演習）"

    else:
        # Kanji notation
        cand_kana = r or ''.join(x['hira'] for x in kks.convert(w))
        adapted_q = target_line.replace(w, f"【{cand_kana}】", 1)
        target_word = w
        if re.match(r'^[ァ-ヴー]+$', w):
            pool = [x for x in katakana_pool if x != w]
        elif w in nouns_2k:
            pool = [x for x in nouns_2k if x != w]
        elif w in verbs:
            pool = [x for x in verbs if x != w]
        elif w in adjs_i:
            pool = [x for x in adjs_i if x != w]
        elif w in adverbs:
            pool = [x for x in adverbs if x != w]
        else:
            pool = [x['word'] for x in genuine_vocab if x['word'] != w and len(x['word']) == len(w)]
        distractors = random.sample(pool, min(3, len(pool)))
        choices = [w] + distractors
        random.shuffle(choices)
        ans_0b = choices.index(w)
        corr_choice = w
        sec_name = "漢字表記（実戦演習）"

    q_ruby = to_ruby_protected(adapted_q, target_kanji, target_reading)
    choices_ruby = [to_ruby_protected(c) for c in choices]

    dict_info = lookup_dict_info(w)
    meaning_en = m_en or dict_info.get("meaning", "")
    similar_data = get_similar_list(w, choices)
    kanji_details = get_kanji_details(target_word or corr_choice)

    all_quiz_questions.append({
        "id": len(all_quiz_questions) + 1,
        "source": "新にほんご500問 N2 (総復習実戦編)",
        "category": sec_name,
        "target_word": target_word,
        "question": adapted_q,
        "question_ruby": q_ruby,
        "choices": choices,
        "choices_ruby": choices_ruby,
        "answer": ans_0b,
        "correct_text": corr_choice,
        "meaning_en": meaning_en,
        "explanation": "",
        "kanji_info": kanji_details,
        "similar": similar_data
    })
    added_curated += 1

print(f"Total quiz questions assembled: {len(all_quiz_questions)}")

# ==========================================
# 4. EXPORT JSON AND JS DATASETS
# ==========================================
json_path = 'database/jlpt_n2_vocab_quiz_data.json'
js_path = 'database/jlpt_n2_vocab_quiz_data.js'

print(f"Writing to {json_path}...")
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(all_quiz_questions, f, ensure_ascii=False, indent=2)

print(f"Writing to {js_path}...")
with open(js_path, 'w', encoding='utf-8') as f:
    f.write("// JLPT N2 文字・語彙 徹底演習道場 完全データベース (全896問)\n")
    f.write("window.JLPT_N2_VOCAB_QUIZ_DATA = ")
    json.dump(all_quiz_questions, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print("✓ Successfully generated both dataset files!")
