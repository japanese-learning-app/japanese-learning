# -*- coding: utf-8 -*-
import json, re, os

BASE_DIR = "/Users/yamauchimiku/Documents/GitHub/japanese-learning"

# ==========================================
# 1. FIX N1 GRAMMAR
# ==========================================
p_n1 = f"{BASE_DIR}/database/jlpt_n1_grammar_quiz_data.js"
with open(p_n1, 'r', encoding='utf-8') as f:
    c = f.read()
idx1 = c.find('=') + 1
idx2 = c.rfind(']') + 1
data_n1 = json.loads(c[idx1:idx2])

for q in data_n1:
    qid = q['id']
    if qid == 255: # にとどまらない (remove に限らず)
        q['choices'] = ['に足らず', 'にかかわらず', 'にとどまらず', 'に及ばず']
        q['choices_ruby'] = ['に<ruby>足<rt>た</rt></ruby>らず', 'にかかわらず', 'にとどまらず', 'に<ruby>及<rt>およ</rt></ruby>ばず']
        q['answer'] = 2
        print("Fixed N1 Grammar ID 255")
    elif qid == 312: # といったらない
        q['choices'] = ['蒸し暑さといったらなく', '蒸し暑さに及ばず', '蒸し暑さにもかかわらず', '蒸し暑さにかかわらず']
        q['choices_ruby'] = ['<ruby>蒸<rt>む</rt></ruby>し<ruby>暑<rt>あつ</rt></ruby>さといったらなく', '<ruby>蒸<rt>む</rt></ruby>し<ruby>暑<rt>あつ</rt></ruby>さに<ruby>及<rt>およ</rt></ruby>ばず', '<ruby>蒸<rt>む</rt></ruby>し<ruby>暑<rt>あつ</rt></ruby>さにもかかわらず', '<ruby>蒸<rt>む</rt></ruby>し<ruby>暑<rt>あつ</rt></ruby>さにかかわらず']
        q['answer'] = 0
        print("Fixed N1 Grammar ID 312")
    elif qid == 363: # 拍子に (remove あげく, 末に)
        q['choices'] = ['あまり', '拍子に', 'ついでに', '最中に']
        q['choices_ruby'] = ['あまり', '<ruby>拍子<rt>ひょうし</rt></ruby>に', 'ついでに', '<ruby>最中<rt>さいちゅう</rt></ruby>に']
        q['answer'] = 1
        print("Fixed N1 Grammar ID 363")
    elif qid == 394: # てやまない (remove てならない)
        q['choices'] = ['てやまない', 'てかなわない', 'てはいられない', 'てばかりいる']
        q['choices_ruby'] = ['てやまない', 'てかなわない', 'てはいられない', 'てばかりいる']
        q['answer'] = 0
        print("Fixed N1 Grammar ID 394")

for path in [p_n1, p_n1.replace('/database/', '/public/database/')]:
    with open(path, 'w', encoding='utf-8') as f:
        f.write('window.JLPT_N1_GRAMMAR_QUIZ_DATA = ' + json.dumps(data_n1, ensure_ascii=False, indent=2) + ';\n')

# ==========================================
# 2. FIX N2 GRAMMAR
# ==========================================
p_n2_g = f"{BASE_DIR}/database/jlpt_n2_grammar_quiz_data.js"
with open(p_n2_g, 'r', encoding='utf-8') as f:
    c = f.read()
idx1 = c.find('=') + 1
idx2 = c.rfind(']') + 1
data_n2_g = json.loads(c[idx1:idx2])

for q in data_n2_g:
    qid = q['id']
    if qid == 74: # だけましだ (Unnatural sentence &君は)
        q['question'] = '雨が降ってきたけれど、屋根のある場所で雨宿りできた【　　】よ。'
        q['question_ruby'] = '<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>ってきたけれど、<ruby>屋根<rt>やね</rt></ruby>のある<ruby>場所<rt>ばしょ</rt></ruby>で<ruby>雨宿<rt>あまやど</rt></ruby>りできた【　　】よ。'
        q['sentence_jp'] = '雨が降ってきたけれど、屋根のある場所で雨宿りできただけましだよ。'
        q['sentence_jp_ruby'] = '<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>ってきたけれど、<ruby>屋根<rt>やね</rt></ruby>のある<ruby>場所<rt>ばしょ</rt></ruby>で<ruby>雨宿<rt>あまやど</rt></ruby>りできただけましだよ。'
        q['sentence_en'] = 'It started to rain, but at least we were able to take shelter under a roof.'
        q['choices'] = ['だけましだ', 'にすぎない', 'わけがない', 'てたまらない']
        q['choices_ruby'] = ['だけましだ', 'にすぎない', 'わけがない', 'てたまらない']
        q['answer'] = 0
        print("Fixed N2 Grammar ID 74")
    elif qid == 113: # でしかない (Double answer with にすぎない)
        q['choices'] = ['どころではない', 'でしかない', 'てばかりはいられない', 'かねない']
        q['choices_ruby'] = ['どころではない', 'でしかない', 'てばかりはいられない', 'かねない']
        q['answer'] = 1
        print("Fixed N2 Grammar ID 113")
    elif qid == 250: # 以上は (Double answer with からには)
        q['choices'] = ['恐らく', 'わりに', '次第で', '以上']
        q['choices_ruby'] = ['<ruby>恐<rt>おそ</rt></ruby>らく', 'わりに', '<ruby>次第<rt>しだい</rt></ruby>で', '<ruby>以上<rt>いじょう</rt></ruby>']
        q['answer'] = 3
        print("Fixed N2 Grammar ID 250")
    elif qid == 274: # 一方で (Double answer with 反面)
        q['choices'] = ['一方で', 'わりに', 'どころか', 'からすると']
        q['choices_ruby'] = ['<ruby>一方<rt>いっぽう</rt></ruby>で', 'わりに', 'どころか', 'からすると']
        q['answer'] = 0
        print("Fixed N2 Grammar ID 274")
    elif qid == 410: # からすると (Double answer with にとって)
        q['choices'] = ['からすると', 'に対して', 'として', 'につれて']
        q['choices_ruby'] = ['からすると', 'に<ruby>対<rt>たい</rt></ruby>して', 'として', 'につれて']
        q['answer'] = 0
        print("Fixed N2 Grammar ID 410")
    elif qid == 593: # もっとも (Double answer with ただし)
        q['choices'] = ['あるいは', '限り', 'もっとも', '一方']
        q['choices_ruby'] = ['あるいは', '<ruby>限<rt>かぎ</rt></ruby>り', 'もっとも', '<ruby>一方<rt>いっぽう</rt></ruby>']
        q['answer'] = 2
        print("Fixed N2 Grammar ID 593")
    elif qid == 788: # にせよ/ にしろ (Double answer with にせよ)
        q['choices'] = ['にしろ', 'としても', 'について', 'ところで']
        q['choices_ruby'] = ['にしろ', 'としても', 'について', 'ところで']
        q['answer'] = 0
        print("Fixed N2 Grammar ID 788")

for path in [p_n2_g, p_n2_g.replace('/database/', '/public/database/')]:
    with open(path, 'w', encoding='utf-8') as f:
        f.write('window.JLPT_N2_GRAMMAR_QUIZ_DATA = ' + json.dumps(data_n2_g, ensure_ascii=False, indent=2) + ';\n')

# ==========================================
# 3. FIX N2 VOCAB
# ==========================================
p_n2_v = f"{BASE_DIR}/database/jlpt_n2_vocab_quiz_data.js"
with open(p_n2_v, 'r', encoding='utf-8') as f:
    c = f.read()
prefix = "window.JLPT_N2_VOCAB_QUIZ_DATA = "
idx = c.find(prefix)
data_n2_v = json.loads(c[idx + len(prefix):].rstrip(';\n '))

for q in data_n2_v:
    qid = q['id']
    if qid == 147: # 前町長 (愛されていた -> 信頼されていた)
        q['question'] = '（　　　）町長は市民のみんなから深く信頼されていた。'
        q['question_ruby'] = '（　　　）<ruby>町長<rt>ちょうちょう</rt></ruby>は<ruby>市民<rt>しみん</rt></ruby>のみんなから<ruby>深<rt>ふか</rt></ruby>く<ruby>信頼<rt>しんらい</rt></ruby>されていた。'
        q['meaning_en'] = 'The former mayor was deeply trusted by all the citizens.'
        print("Fixed N2 Vocab ID 147")
    elif qid == 586: # にかけては (山本君 -> 記憶力)
        q['question'] = '彼は足はあまり速くないが、記憶力の良さ（　　　）クラスで一番だ。'
        q['question_ruby'] = '<ruby>彼<rt>かれ</rt></ruby>は<ruby>足<rt>あし</rt></ruby>はあまり<ruby>速<rt>はや</rt></ruby>くないが、<ruby>記憶<rt>きおく</rt></ruby><ruby>力<rt>りょく</rt></ruby>の<ruby>良<rt>よ</rt></ruby>さ（　　　）クラスで<ruby>一番<rt>いちばん</rt></ruby>だ。'
        print("Fixed N2 Vocab ID 586")
    elif qid == 757: # くらいなら (高いお金 -> 多額の費用)
        q['question'] = 'そんなに多額の費用をかけて修理する（　　　）、新しいものに買い換えたほうがいい。'
        q['question_ruby'] = 'そんなに<ruby>多額<rt>たがく</rt></ruby>の<ruby>費用<rt>ひよう</rt></ruby>をかけて<ruby>修理<rt>しゅうり</rt></ruby>する（　　　）、<ruby>新<rt>あたら</rt></ruby>しいものに<ruby>買<rt>か</rt></ruby>い<ruby>換<rt>か</rt></ruby>えたほうがいい。'
        print("Fixed N2 Vocab ID 757")
    elif qid == 764: # 尊重 (君は -> 周囲の意見)
        q['question'] = '仕事を円滑に進めるためには、周囲の意見をもっと【尊重】し、柔軟に耳を傾けることが大切だ。'
        q['question_ruby'] = '<ruby>仕事<rt>しごと</rt></ruby>を<ruby>円滑<rt>えんかつ</rt></ruby>に<ruby>進<rt>すす</rt></ruby>めるためには、<ruby>周囲<rt>しゅうい</rt></ruby>の<ruby>意見<rt>いけん</rt></ruby>をもっと【<ruby>尊重<rt>そんちょう</rt></ruby>】し、<ruby>柔軟<rt>じゅうなん</rt></ruby>に<ruby>耳<rt>みみ</rt></ruby>を<ruby>傾<rt>かたむ</rt></ruby>けることが<ruby>大切<rt>たいせつ</rt></ruby>だ。'
        q['meaning_en'] = 'To carry out work smoothly, it is important to respect surrounding opinions more and listen flexibly.'
        print("Fixed N2 Vocab ID 764")

for path in [p_n2_v, p_n2_v.replace('/database/', '/public/database/')]:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(prefix + json.dumps(data_n2_v, ensure_ascii=False, indent=2) + ';\n')

# ==========================================
# 4. FIX N3 GRAMMAR & VOCAB
# ==========================================
p_n3_g = f"{BASE_DIR}/database/jlpt_n3_grammar_quiz_data.js"
with open(p_n3_g, 'r', encoding='utf-8') as f:
    c = f.read()
idx1 = c.find('=') + 1
idx2 = c.rfind(']') + 1
data_n3_g = json.loads(c[idx1:idx2])

for q in data_n3_g:
    qid = q['id']
    if qid == 37: # ばよかった (remove いい)
        q['choices'] = ['よかった', 'に違いない', '助かったのに', 'はずだ']
        q['choices_ruby'] = ['よかった', 'に<ruby>違<rt>ちが</rt></ruby>いない', '<ruby>助<rt>たす</rt></ruby>かったのに', 'はずだ']
        q['answer'] = 0
        print("Fixed N3 Grammar ID 37")
    elif qid == 45: # べきではない
        q['choices'] = ['わけがない', 'べきではない', 'わけではない', 'はずがない']
        q['choices_ruby'] = ['わけがない', 'べきではない', 'わけではない', 'はずがない']
        q['answer'] = 1
        print("Fixed N3 Grammar ID 45")
    elif qid == 46: # べきではない (remove はずがない)
        q['choices'] = ['に違いない', 'わけだ', 'つもりだ', 'べきではない']
        q['choices_ruby'] = ['に<ruby>違<rt>ちが</rt></ruby>いない', 'わけだ', 'つもりだ', 'べきではない']
        q['answer'] = 3
        print("Fixed N3 Grammar ID 46")

for path in [p_n3_g, p_n3_g.replace('/database/', '/public/database/')]:
    with open(path, 'w', encoding='utf-8') as f:
        f.write('window.JLPT_N3_GRAMMAR_QUIZ_DATA = ' + json.dumps(data_n3_g, ensure_ascii=False, indent=2) + ';\n')

p_n3_v = f"{BASE_DIR}/database/jlpt_n3_vocab_quiz_data.js"
with open(p_n3_v, 'r', encoding='utf-8') as f:
    c = f.read()
prefix_n3_v = "window.JLPT_N3_VOCAB_QUIZ_DATA = "
idx = c.find(prefix_n3_v)
data_n3_v = json.loads(c[idx + len(prefix_n3_v):].rstrip(';\n '))

for q in data_n3_v:
    if q['id'] == 116: # ナイフ -> 包丁
        q['question'] = '職人が丁寧に研いだこの包丁は、とても【鋭く】てよく切れる。'
        q['question_ruby'] = '<ruby>職人<rt>しょくにん</rt></ruby>が<ruby>丁寧<rt>ていねい</rt></ruby>に<ruby>研<rt>と</rt></ruby>いだこの<ruby>包丁<rt>ほうちょう</rt></ruby>は、とても【<ruby>鋭<rt>するど</rt></ruby>く】てよく<ruby>切<rt>き</rt></ruby>れる。'
        q['meaning_en'] = 'This kitchen knife, carefully sharpened by a craftsman, is very sharp and cuts well.'
        print("Fixed N3 Vocab ID 116")

for path in [p_n3_v, p_n3_v.replace('/database/', '/public/database/')]:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(prefix_n3_v + json.dumps(data_n3_v, ensure_ascii=False, indent=2) + ';\n')

print("All double answers & unnatural sentences successfully updated!")
