# -*- coding: utf-8 -*-
import json, re, os

BASE_DIR = "/Users/yamauchimiku/.gemini/antigravity/scratch/japanese-flashcards"

# 1. Fix N2 Vocab ID 713 and ID 689
n2_vocab_files = [
    f"{BASE_DIR}/database/jlpt_n2_vocab_quiz_data.js",
    f"{BASE_DIR}/public/database/jlpt_n2_vocab_quiz_data.js"
]
for p in n2_vocab_files:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    prefix = "window.JLPT_N2_VOCAB_QUIZ_DATA = "
    idx = c.find(prefix)
    data = json.loads(c[idx + len(prefix):].rstrip(';\n '))
    for q in data:
        if q['id'] == 713:
            q['question'] = '診察を嫌がって猫が動物病院で【暴れ】てしまい、先生を困らせてしまった。'
            q['question_ruby'] = '<ruby>診察<rt>しんさつ</rt></ruby>を<ruby>嫌<rt>いや</rt></ruby>がって<ruby>猫<rt>ねこ</rt></ruby>が<ruby>動物<rt>どうぶつ</rt></ruby><ruby>病院<rt>びょういん</rt></ruby>で【<ruby>暴<rt>あば</rt></ruby>れ】てしまい、<ruby>先生<rt>せんせい</rt></ruby>を<ruby>困<rt>こま</rt></ruby>らせてしまった。'
            q['meaning_en'] = 'The cat went wild at the animal hospital hating the examination, troubling the vet.'
            q['explanation'] = '「暴れる（あばれる）」は「激しく手足を動かして騒ぐ・暴れる」という意味です。'
            print("Fixed N2 Vocab ID 713")
        elif q['id'] == 689:
            q['question'] = '地震で家具が倒れないよう、耐震器具を【壁】にしっかり取り付けて固定した。'
            q['question_ruby'] = '<ruby>地震<rt>じしん</rt></ruby>で<ruby>家具<rt>かぐ</rt></ruby>が<ruby>倒<rt>たお</rt></ruby>れないよう、<ruby>耐震<rt>たいしん</rt></ruby><ruby>器具<rt>きぐ</rt></ruby>を【<ruby>壁<rt>かべ</rt></ruby>】にしっかり<ruby>取<rt>と</rt></ruby>り<ruby>付<rt>つ</rt></ruby>けて<ruby>固定<rt>こてい</rt></ruby>した。'
            q['meaning_en'] = 'To prevent furniture from falling in an earthquake, earthquake-resistant fixtures were firmly attached to the wall.'
            print("Fixed N2 Vocab ID 689")
    with open(p, 'w', encoding='utf-8') as f:
        f.write(prefix + json.dumps(data, ensure_ascii=False, indent=2) + ';\n')

# 2. Fix N2 Grammar ID 441, 143, 514, 1343
n2_grammar_files = [
    f"{BASE_DIR}/database/jlpt_n2_grammar_quiz_data.js",
    f"{BASE_DIR}/public/database/jlpt_n2_grammar_quiz_data.js"
]
for p in n2_grammar_files:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    prefix = "window.JLPT_N2_GRAMMAR_QUIZ_DATA = "
    idx = c.find(prefix)
    data = json.loads(c[idx + len(prefix):].rstrip(';\n '))
    for q in data:
        qid = q['id']
        if qid == 441: # ことだから
            q['question'] = 'いつも時間を守る田中さんの【　　】、遅刻するなんて何か事情があったに違いない。'
            q['question_ruby'] = 'いつも<ruby>時間<rt>じかん</rt></ruby>を<ruby>守<rt>まも</rt></ruby>る<ruby>田中<rt>たなか</rt></ruby>さんの【　　】、<ruby>遅刻<rt>ちこく</rt></ruby>するなんて<ruby>何<rt>なに</rt></ruby>か<ruby>事情<rt>じじょう</rt></ruby>があったに<ruby>違<rt>ちが</rt></ruby>いない。'
            q['sentence_jp'] = 'いつも時間を守る田中さんのことだから、遅刻するなんて何か事情があったに違いない。'
            q['sentence_jp_ruby'] = 'いつも<ruby>時間<rt>じかん</rt></ruby>を<ruby>守<rt>まも</rt></ruby>る<ruby>田中<rt>たなか</rt></ruby>さんのことだから、<ruby>遅刻<rt>ちこく</rt></ruby>するなんて<ruby>何<rt>なに</rt></ruby>か<ruby>事情<rt>じじょう</rt></ruby>があったに<ruby>違<rt>ちが</rt></ruby>いない。'
            q['sentence_en'] = 'Knowing Tanaka-san, who is always punctual, there must be a good reason for being late.'
            print("Fixed N2 Grammar ID 441")
        elif qid == 143: # どうやら
            q['question'] = '西の空が急に暗くなってきた。【　　】今夜は雨が降りそうだ。'
            q['question_ruby'] = '<ruby>西<rt>にし</rt></ruby>の<ruby>空<rt>そら</rt></ruby>が<ruby>急<rt>きゅう</rt></ruby>に<ruby>暗<rt>くら</rt></ruby>くなってきた。【　　】<ruby>今夜<rt>こんや</rt></ruby>は<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>りそうだ。'
            q['sentence_jp'] = '西の空が急に暗くなってきた。どうやら今夜は雨が降りそうだ。'
            q['sentence_jp_ruby'] = '<ruby>西<rt>にし</rt></ruby>の<ruby>空<rt>そら</rt></ruby>が<ruby>急<rt>きゅう</rt></ruby>に<ruby>暗<rt>くら</rt></ruby>くなってきた。どうやら<ruby>今夜<rt>こんや</rt></ruby>は<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>りそうだ。'
            q['sentence_en'] = 'The western sky suddenly turned dark. It looks like it might rain tonight.'
            print("Fixed N2 Grammar ID 143")
        elif qid == 514: # もかまわず
            q['question'] = '大雨が降っているの【　　】、子供たちは夢中でサッカーを続けている。'
            q['question_ruby'] = '<ruby>大雨<rt>おおあめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>っているの【　　】、<ruby>子供<rt>こども</rt></ruby>たちは<ruby>夢中<rt>むちゅう</rt></ruby>でサッカーを<ruby>続<rt>つづ</rt></ruby>けている。'
            q['sentence_jp'] = '大雨が降っているのもかまわず、子供たちは夢中でサッカーを続けている。'
            q['sentence_jp_ruby'] = '<ruby>大雨<rt>おおあめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>っているのもかまわず、<ruby>子供<rt>こども</rt></ruby>たちは<ruby>夢中<rt>むちゅう</rt></ruby>でサッカーを<ruby>続<rt>つづ</rt></ruby>けている。'
            q['sentence_en'] = 'Regardless of the heavy rain, the children are engrossed in playing soccer.'
            print("Fixed N2 Grammar ID 514")
        elif qid == 1343: # とっくに
            q['question'] = '待ち合わせの時間は【　　】過ぎているのに、彼はまだ姿を見せない。'
            q['question_ruby'] = '<ruby>待<rt>ま</rt></ruby>ち<ruby>合<rt>あ</rt></ruby>わせの<ruby>時間<rt>じかん</rt></ruby>は【　　】<ruby>過<rt>す</rt></ruby>ぎているのに、<ruby>彼<rt>かれ</rt></ruby>はまだ<ruby>姿<rt>すがた</rt></ruby>を<ruby>見<rt>み</rt></ruby>せない。'
            q['sentence_jp'] = '待ち合わせの時間はとっくに過ぎているのに、彼はまだ姿を見せない。'
            q['sentence_jp_ruby'] = '<ruby>待<rt>ま</rt></ruby>ち<ruby>合<rt>あ</rt></ruby>わせの<ruby>時間<rt>じかん</rt></ruby>はとっくに<ruby>過<rt>す</rt></ruby>ぎているのに、<ruby>彼<rt>かれ</rt></ruby>はまだ<ruby>姿<rt>すがた</rt></ruby>を<ruby>見<rt>み</rt></ruby>せない。'
            q['sentence_en'] = 'The meeting time has long passed, but he has not shown up yet.'
            print("Fixed N2 Grammar ID 1343")
    with open(p, 'w', encoding='utf-8') as f:
        f.write(prefix + json.dumps(data, ensure_ascii=False, indent=2) + ';\n')

# 3. Fix dictionary and vocab examples
vocab_files = [
    f"{BASE_DIR}/database/jlpt_vocab_all.js",
    f"{BASE_DIR}/public/database/jlpt_vocab_all.js",
    f"{BASE_DIR}/database/dict_examples_map.js",
    f"{BASE_DIR}/public/database/dict_examples_map.js"
]
for p in vocab_files:
    if not os.path.exists(p): continue
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('人をナイフで刺すのはやめましょう。', '指にトゲが刺さって痛い。')
    c = c.replace('<ruby>人<rt>にん</rt></ruby>をナイフで<ruby>刺<rt>さ</rt></ruby>すのはやめましょう。', '<ruby>指<rt>ゆび</rt></ruby>にトゲが<ruby>刺<rt>さ</rt></ruby>さって<ruby>痛<rt>いた</rt></ruby>い。')
    c = c.replace("Let's refrain from stabbing people with knives.", "A thorn is stuck in my finger and it hurts.")
    c = c.replace('君はもう少しで私の目を鉛筆で突き刺すところだった。', '虫に刺されたところがかゆくてたまらない。')
    c = c.replace('<ruby>君<rt>きみ</rt></ruby>はもう<ruby>少<rt>すこ</rt></ruby>しで<ruby>私<rt>わたし</rt></ruby>の<ruby>目<rt>め</rt></ruby>を<ruby>鉛筆<rt>えんぴつ</rt></ruby>で<ruby>突<rt>つ</rt></ruby>き<ruby>刺<rt>さ</rt></ruby>すところだった。', '<ruby>虫<rt>むし</rt></ruby>に<ruby>刺<rt>さ</rt></ruby>されたところがかゆくてたまらない。')
    c = c.replace("You nearly poked me in the eye with your pencil.", "The insect bite is so itchy I can hardly bear it.")
    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Sanitized {os.path.basename(p)}")

print("All sensitive & unnatural sentences successfully updated!")
