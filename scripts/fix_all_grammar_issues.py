# -*- coding: utf-8 -*-
import json

# 1. FIX N1 GRAMMAR
n1_path = '/Users/yamauchimiku/.gemini/antigravity/scratch/japanese-flashcards/database/jlpt_n1_grammar_quiz_data.js'
with open(n1_path, 'r', encoding='utf-8') as f:
    c = f.read()
idx1 = c.find('=') + 1
idx2 = c.rfind(']') + 1
data_n1 = json.loads(c[idx1:idx2])

for q in data_n1:
    qid = q['id']
    if qid == 177: # きらいがある
        q['choices'] = ['陥る始末だ', '陥る傾向だ', '陥る恐れがある', '陥るきらいがある']
        q['choices_ruby'] = ['<ruby>陥<rt>おちい</rt></ruby>る<ruby>始末<rt>しまつ</rt></ruby>だ', '<ruby>陥<rt>おちい</rt></ruby>る<ruby>傾向<rt>けいこう</rt></ruby>だ', '<ruby>陥<rt>おちい</rt></ruby>る<ruby>恐<rt>おそ</rt></ruby>れがある', '<ruby>陥<rt>おちい</rt></ruby>るきらいがある']
        q['answer'] = 3
    elif qid == 249: # にすぎない
        q['choices'] = ['意見にすぎない', '意見に堪えない', '意見にかかわらない', '意見に値しない']
        q['choices_ruby'] = ['<ruby>意見<rt>いけん</rt></ruby>にすぎない', '<ruby>意見<rt>いけん</rt></ruby>に<ruby>堪<rt>た</rt></ruby>えない', '<ruby>意見<rt>いけん</rt></ruby>にかかわらない', '<ruby>意見<rt>いけん</rt></ruby>に<ruby>値<rt>あたい</rt></ruby>しない']
        q['answer'] = 0
    elif qid == 253: # にとどまらない
        q['choices'] = ['にとどまらない', 'に及ばない', 'にとらわれない', 'を限りにしない']
        q['choices_ruby'] = ['にとどまらない', 'に<ruby>及<rt>およ</rt></ruby>ばない', 'にとらわれない', 'を<ruby>限<rt>かぎ</rt></ruby>りにしない']
        q['answer'] = 0
    elif qid == 255: # にとどまらない
        q['choices'] = ['に足らず', 'に限らず', 'にとどまらず', 'に及ばず']
        q['choices_ruby'] = ['に<ruby>足<rt>た</rt></ruby>らず', 'に<ruby>限<rt>かぎ</rt></ruby>らず', 'にとどまらず', 'に<ruby>及<rt>およ</rt></ruby>ばず']
        q['question'] = '森林の減少は単なる景観の変化（　　　）、地域の生態系全体に関わる重大な課題だ。'
        q['question_ruby'] = '<ruby>森林<rt>しんりん</rt></ruby>の<ruby>減少<rt>げんしょう</rt></ruby>は<ruby>単<rt>たん</rt></ruby>なる<ruby>景観<rt>けいかん</rt></ruby>の<ruby>変化<rt>へんか</rt></ruby>（　　　）、<ruby>地域<rt>ちいき</rt></ruby>の<ruby>生態<rt>せいたい</rt></ruby><ruby>系<rt>けい</rt></ruby><ruby>全体<rt>ぜんたい</rt></ruby>に<ruby>関<rt>かか</rt></ruby>わる<ruby>重大<rt>じゅうだい</rt></ruby>な<ruby>課題<rt>かだい</rt></ruby>だ。'
        q['correct_text'] = 'にとどまらず'
        q['correct_text_ruby'] = 'にとどまらず'
        q['answer'] = 2
    elif qid == 312: # といったらない
        q['choices'] = ['蒸し暑さといったらなく', '蒸し暑さには及ばず', '蒸し暑さに限らず', '蒸し暑さにとどまらず']
        q['choices_ruby'] = ['<ruby>蒸<rt>む</rt></ruby>し<ruby>暑<rt>あつ</rt></ruby>さといったらなく', '<ruby>蒸<rt>む</rt></ruby>し<ruby>暑<rt>あつ</rt></ruby>さには<ruby>及<rt>およ</rt></ruby>ばず', '<ruby>蒸<rt>む</rt></ruby>し<ruby>暑<rt>あつ</rt></ruby>さに<ruby>限<rt>かぎ</rt></ruby>らず', '<ruby>蒸<rt>む</rt></ruby>し<ruby>暑<rt>あつ</rt></ruby>さにとどまらず']
        q['correct_text'] = '蒸し暑さといったらなく'
        q['correct_text_ruby'] = '<ruby>蒸<rt>む</rt></ruby>し<ruby>暑<rt>あつ</rt></ruby>さといったらなく'
        q['answer'] = 0
    elif qid == 450: # てはならない
        q['choices'] = ['てはかなわない', 'てはならない', 'てはいられない', 'てはすまない']
        q['choices_ruby'] = ['てはかなわない', 'てはならない', 'てはいられない', 'てはすまない']
        q['answer'] = 1
    elif qid == 452: # てはならない
        q['choices'] = ['てはならない', 'てはいられない', 'てはかなわない', 'てはすまない']
        q['choices_ruby'] = ['てはならない', 'てはいられない', 'てはかなわない', 'てはすまない']
        q['answer'] = 0

for target in [n1_path, n1_path.replace('/database/', '/public/database/')]:
    with open(target, 'w', encoding='utf-8') as f:
        f.write('window.JLPT_N1_GRAMMAR_QUIZ_DATA = ' + json.dumps(data_n1, ensure_ascii=False, indent=2) + ';\n')
print("Saved N1 grammar fixes.")

# 2. FIX N2 GRAMMAR
n2_path = '/Users/yamauchimiku/.gemini/antigravity/scratch/japanese-flashcards/database/jlpt_n2_grammar_quiz_data.js'
with open(n2_path, 'r', encoding='utf-8') as f:
    c = f.read()
idx1 = c.find('=') + 1
idx2 = c.rfind(']') + 1
data_n2 = json.loads(c[idx1:idx2])

for q in data_n2:
    qid = q['id']
    # Duplicates & double answers
    if qid == 4: # あげく (remove 末に)
        q['choices'] = ['に限らず', '途端に', 'かねる', 'あげく']
        q['choices_ruby'] = ['に<ruby>限<rt>かぎ</rt></ruby>らず', '<ruby>途端<rt>とたん</rt></ruby>に', 'かねる', 'あげく']
        q['answer'] = 3
    elif qid == 5: # あげく (remove 末に)
        q['choices'] = ['あげく', 'だけは', '得る', '反面']
        q['choices_ruby'] = ['あげく', 'だけは', '<ruby>得<rt>え</rt></ruby>る', '<ruby>反面<rt>はんめん</rt></ruby>']
        q['answer'] = 0
    elif qid == 8: # あげく (remove 末に)
        q['choices'] = ['てでも', '次第に', 'うえに', 'あげく']
        q['choices_ruby'] = ['てでも', '<ruby>次第<rt>しだい</rt></ruby>に', 'うえに', 'あげく']
        q['answer'] = 3
    elif qid == 303: # かのように (remove duplicate 末に)
        q['choices'] = ['かのように', 'ようにして', 'そうに', 'くらいに']
        q['choices_ruby'] = ['かのように', 'ようにして', 'そうに', 'くらいに']
        q['answer'] = 0
    elif qid == 588: # ものの (remove duplicate あげく)
        q['choices'] = ['一方', 'わりに', '反面', 'ものの']
        q['choices_ruby'] = ['<ruby>一方<rt>いっぽう</rt></ruby>', 'わりに', '<ruby>反面<rt>はんめん</rt></ruby>', 'ものの']
        q['answer'] = 3
    elif qid == 590: # ものの (remove duplicate に沿って)
        q['choices'] = ['につれて', 'ものの', '反面', 'うえに']
        q['choices_ruby'] = ['につれて', 'ものの', '<ruby>反面<rt>はんめん</rt></ruby>', 'うえに']
        q['answer'] = 1
    elif qid == 874: # にも関わらず (remove duplicate あげく)
        q['choices'] = ['せいか', 'うえで', 'にも関わらず', 'から見ると']
        q['choices_ruby'] = ['せいか', 'うえで', 'にも<ruby>関<rt>かか</rt></ruby>わらず', 'から<ruby>見<rt>み</rt></ruby>ると']
        q['answer'] = 2
    # Mid-sentence sentence-ender dummies
    elif qid == 250: # 以上は
        q['choices'] = ['恐らく', 'からには', '次第で', '以上']
        q['choices_ruby'] = ['<ruby>恐<rt>おそ</rt></ruby>らく', 'からには', '<ruby>次第<rt>しだい</rt></ruby>で', '<ruby>以上<rt>いじょう</rt></ruby>']
        q['answer'] = 3
    elif qid == 274: # 一方で
        q['choices'] = ['一方で', '反面', 'どころか', 'からすると']
        q['choices_ruby'] = ['<ruby>一方<rt>いっぽう</rt></ruby>で', '<ruby>反面<rt>はんめん</rt></ruby>', 'どころか', 'からすると']
        q['answer'] = 0
    elif qid == 383: # から見ると
        q['choices'] = ['だけあって', 'として', 'から見れば', 'にかかわらず']
        q['choices_ruby'] = ['だけあって', 'として', 'から<ruby>見<rt>み</rt></ruby>れば', 'にかかわらず']
        q['answer'] = 2
    elif qid == 410: # からすると
        q['choices'] = ['からすると', 'にとって', 'として', 'につれて']
        q['choices_ruby'] = ['からすると', 'にとって', 'として', 'につれて']
        q['answer'] = 0
    elif qid == 485: # まだしも
        q['choices'] = ['がきっかけで', 'どころか', 'まだしも', 'としても']
        q['choices_ruby'] = ['がきっかけで', 'どころか', 'まだしも', 'としても']
        q['answer'] = 2
    elif qid == 593: # もっとも
        q['choices'] = ['ただし', '限り', 'もっとも', '一方']
        q['choices_ruby'] = ['ただし', '<ruby>限<rt>かぎ</rt></ruby>り', 'もっとも', '<ruby>一方<rt>いっぽう</rt></ruby>']
        q['answer'] = 2
    elif qid == 735: # に応えて
        q['choices'] = ['にこたえて', 'に基づいて', 'かねて', 'に沿って']
        q['choices_ruby'] = ['にこたえて', 'に<ruby>基<rt>もと</rt></ruby>づいて', 'かねて', 'に<ruby>沿<rt>そ</rt></ruby>って']
        q['answer'] = 0
    elif qid == 788: # にせよ
        q['choices'] = ['にしろ', 'としても', 'にせよ', 'ところで']
        q['choices_ruby'] = ['にしろ', 'としても', 'にせよ', 'ところで']
        q['answer'] = 0
    elif qid == 849: # につけ
        q['choices'] = ['につれ', 'につけ', 'とともに', 'にあたり']
        q['choices_ruby'] = ['につれ', 'につけ', 'とともに', 'にあたり']
        q['answer'] = 1
    elif qid == 904: # の上では
        q['choices'] = ['の上では', 'からには', 'において', 'によって']
        q['choices_ruby'] = ['の<ruby>上<rt>うえ</rt></ruby>では', 'からには', 'において', 'によって']
        q['answer'] = 0

for target in [n2_path, n2_path.replace('/database/', '/public/database/')]:
    with open(target, 'w', encoding='utf-8') as f:
        f.write('window.JLPT_N2_GRAMMAR_QUIZ_DATA = ' + json.dumps(data_n2, ensure_ascii=False, indent=2) + ';\n')
print("Saved N2 grammar fixes.")

# 3. FIX N3 GRAMMAR
n3_path = '/Users/yamauchimiku/.gemini/antigravity/scratch/japanese-flashcards/database/jlpt_n3_grammar_quiz_data.js'
with open(n3_path, 'r', encoding='utf-8') as f:
    c = f.read()
idx1 = c.find('=') + 1
idx2 = c.rfind(']') + 1
data_n3 = json.loads(c[idx1:idx2])

for q in data_n3:
    qid = q['id']
    if qid == 38: # ばよかった
        q['choices'] = ['ばいい', 'ば間に合う', 'ば助かった', 'ばよかった']
        q['choices_ruby'] = ['ばいい', 'ば<ruby>間<rt>ま</rt></ruby>に<ruby>合<rt>あ</rt></ruby>う', 'ば<ruby>助<rt>たす</rt></ruby>かった', 'ばよかった']
        q['answer'] = 3
    elif qid == 39: # ばよかった
        q['choices'] = ['ばいい', 'ば十分だ', 'ばよかった', 'ば助かる']
        q['choices_ruby'] = ['ばいい', 'ば<ruby>十分<rt>じゅうぶん</rt></ruby>だ', 'ばよかった', 'ば<ruby>助<rt>たす</rt></ruby>かる']
        q['answer'] = 2
    elif qid == 40: # ばよかった
        q['choices'] = ['ばいいのに', 'ばよかった', 'ば済んだのに', 'ば大丈夫だ']
        q['choices_ruby'] = ['ばいいのに', 'ばよかった', 'ば<ruby>済<rt>す</rt></ruby>んだのに', 'ば<ruby>大丈夫<rt>だいじょうぶ</rt></ruby>だ']
        q['answer'] = 1
    elif qid == 97: # がたい (remove づらい)
        q['choices'] = ['っこない', 'がたい', 'きれない', 'かねない']
        q['choices_ruby'] = ['っこない', 'がたい', 'きれない', 'かねない']
        q['answer'] = 1
    elif qid == 258: # ないことはない
        q['choices'] = ['ないはずだ', 'ないかもしれない', 'ないことはない', 'ない方がいい']
        q['choices_ruby'] = ['ないはずだ', 'ないかもしれない', 'ないことはない', 'ない<ruby>方<rt>ほう</rt></ruby>がいい']
        q['answer'] = 2
    elif qid == 259: # ないことはない
        q['choices'] = ['ないはずだ', 'ないことはない', 'ないままだ', 'ないようだ']
        q['choices_ruby'] = ['ないはずだ', 'ないことはない', 'ないままだ', 'ないようだ']
        q['answer'] = 1
    elif qid == 260: # ないことはない
        q['choices'] = ['ないことはない', 'ない恐れがある', 'ないはずがない', 'ないかもしれない']
        q['choices_ruby'] = ['ないことはない', 'ない<ruby>恐<rt>おそ</rt></ruby>れがある', 'ないはずがない', 'ないかもしれない']
        q['answer'] = 0
    elif qid == 443: # そうもない
        q['question'] = '今日中に終わらせるべき書類が山のように残っていて、とても定時には（　　　）。'
        q['question_ruby'] = '<ruby>今日<rt>きょう</rt></ruby><ruby>中<rt>じゅう</rt></ruby>に<ruby>終<rt>お</rt></ruby>わらせるべき<ruby>書類<rt>しょるい</rt></ruby>が<ruby>山<rt>やま</rt></ruby>のように<ruby>残<rt>のこ</rt></ruby>っていて、とても<ruby>定時<rt>ていじ</rt></ruby>には（　　　）。'
        q['choices'] = ['帰れそうもない', '帰るに違いない', '帰りそうもない', '帰る一方だ']
        q['choices_ruby'] = ['<ruby>帰<rt>かえ</rt></ruby>れそうもない', '<ruby>帰<rt>かえ</rt></ruby>るに<ruby>違<rt>ちが</rt></ruby>いない', '<ruby>帰<rt>かえ</rt></ruby>りそうもない', '<ruby>帰<rt>かえ</rt></ruby>る<ruby>一方<rt>いっぽう</rt></ruby>だ']
        q['correct_text'] = '帰れそうもない'
        q['correct_text_ruby'] = '<ruby>帰<rt>かえ</rt></ruby>れそうもない'
        q['answer'] = 0
    elif qid == 444: # そうもない
        q['question'] = '専門用語ばかりで書かれたこの論文は、予備知識のない私には（　　　）。'
        q['question_ruby'] = '<ruby>専門<rt>せんもん</rt></ruby><ruby>用語<rt>ようご</rt></ruby>ばかりで<ruby>書<rt>か</rt></ruby>かれたこの<ruby>論文<rt>ろんぶん</rt></ruby>は、<ruby>予備<rt>よび</rt></ruby><ruby>知識<rt>ちしき</rt></ruby>のない<ruby>私<rt>わたし</rt></ruby>には（　　　）。'
        q['choices'] = ['理解できそうもない', '理解するに違いない', '理解できるはずだ', '理解する一方だ']
        q['choices_ruby'] = ['<ruby>理解<rt>りかい</rt></ruby>できそうもない', '<ruby>理解<rt>りかい</rt></ruby>するに<ruby>違<rt>ちが</rt></ruby>いない', '<ruby>理解<rt>りかい</rt></ruby>できるはずだ', '<ruby>理解<rt>りかい</rt></ruby>する<ruby>一方<rt>いっぽう</rt></ruby>だ']
        q['correct_text'] = '理解できそうもない'
        q['correct_text_ruby'] = '<ruby>理解<rt>りかい</rt></ruby>できそうもない'
        q['answer'] = 0

for target in [n3_path, n3_path.replace('/database/', '/public/database/')]:
    with open(target, 'w', encoding='utf-8') as f:
        f.write('window.JLPT_N3_GRAMMAR_QUIZ_DATA = ' + json.dumps(data_n3, ensure_ascii=False, indent=2) + ';\n')
print("Saved N3 grammar fixes.")
