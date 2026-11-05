# -*- coding: utf-8 -*-
"""
N3 grammar data part C: gids 122-182.
"""

GRAMMAR = {
    122: {
        'reading': 'たとたん',
        'wrong': (
            '{朝|あさ}{起|お}きたとたん、いつも{歯|は}を{磨|みが}きます。',
            '「〜たとたん」は直後に起きた意外な変化や偶発的な出来事に使うため、毎日の習慣的・意図的な行動には使えません。',
            'Because 〜たとたん describes an unexpected or sudden change right after an action, it cannot be used for habitual or intentional daily actions.',
        ),
        'comp_ex': [
            'ベルが{鳴|な}ると{同時|どうじ}に、{生徒|せいと}たちは{一斉|いっせい}に{教室|きょうしつ}を{出|で}た。',
            '{朝|あさ}{起|お}きるとすぐに、{窓|まど}を{開|あ}けて{新鮮|しんせん}な{空気|くうき}を{吸|す}う。',
        ],
        'quiz': [
            ('玄関のドアを{開|あ}けた（　　　）、香ばしいカレーのいい匂いが漂ってきた。', 'とたん', ['たび', 'とおり', 'きり'], 'As soon as I opened the front door, the appetizing aroma of savory curry wafted in.', '動詞た形＋とたんにで前件の動作の直後に予想外の後件が瞬間的に発生することを表します。'),
            ('{疲|つか}れていたので、ベッドに{横|よこ}になった（　　　）にぐっすり{眠|ねむ}ってしまった。', 'とたん', ['ついで', 'ばかり', '最中'], 'Because I was tired, the moment I lay down on the bed, I fell fast asleep.', '「横になったとたんに」で、動作の直後に瞬間的に眠りに落ちたことを表します。'),
            ('{立|た}ち{上|あ}がった（　　　）、めまいがして{思|おも}わず{壁|かべ}に{手|て}をついた。', 'とたん', ['とおり', 'くせに', 'わりに'], 'The moment I stood up, I felt dizzy and reflexively put my hand against the wall.', '立ち上がった直後に予期せぬめまいが起きたことを表します。'),
            ('{外|そと}へ{出|で}た（　　　）に{激|はげ}しい{雨|あめ}が{降|ふ}り{出|だ}し、すっかり{濡|ぬ}れてしまった。', 'とたん', ['うえで', 'かぎり', 'つもり'], 'Just as I stepped outside, heavy rain started pouring down and I got completely soaked.', '外に出た直後に突発的に雨が降り始めた場面です。'),
        ],
    },
    123: {
        'reading': 'たって',
        'wrong': (
            '{先生|せんせい}、お{忙|いそが}しかったって、どうかご{出席|しゅせき}ください。',
            '「〜たって」は非常にカジュアルな口語表現なので、目上の人に対する丁寧な依頼の場面には不適切です。',
            'Because 〜たって is a very casual spoken expression, it is inappropriate when making a polite request to a superior.',
        ),
        'comp_ex': [
            'どんなに{忙|いそが}しくても、{毎日|まいにち}{朝食|ちょうしょく}だけはしっかり{食|た}べるようにしている。',
            'たとえ{彼|かれ}が{反対|はんたい}したとしたって、{私|わたし}の{決心|けっしん}は{変|か}わらない。',
        ],
        'quiz': [
            ('過ぎてしまったことを今さら悔やん（　　　）、時間を元に戻すことはできない。', 'だって', ['だらけ', 'っぽく', 'がちに'], 'Even if you regret what has already passed at this late hour, you cannot turn back time.', '動詞て形（た形）＋ってで『〜ても』のくだけた口語表現です。'),
            ('今から{走|はし}っ（　　　）、{次|つぎ}の{電車|でんしゃ}にはもう{間|ま}に{合|あ}わないよ。', 'たって', ['たり', 'たら', 'とたん'], 'Even if you run starting now, you will no longer make it in time for the next train.', '「走ったって」は「走っても」の口語形で、仮定の逆接を表します。'),
            ('いくら{説明|せつめい}し（　　　）、{彼|かれ}は{自分|じぶん}の{意見|いけん}を{曲|ま}げようとしないだろう。', 'たって', ['たきり', 'たばかり', 'たとおり'], 'No matter how much you explain, he probably will not bend his opinion.', '「いくら〜たって」で「いくら〜ても」のくだけた逆接条件を表します。'),
            ('そんなに{高|たか}い{服|ふく}を{買|か}っ（　　　）、{着|き}て{行|い}く{場所|ばしょ}がないじゃないか。', 'たって', ['た上で', 'た末に', 'たものの'], 'Even if you buy such expensive clothes, you do not have anywhere to wear them to, do you?', '買っても無駄になるという話し手の判断を会話調で表します。'),
        ],
    },
    124: {
        'reading': 'てばかりいる',
        'wrong': (
            '{彼|かれ}は{毎日|まいにち}{真面目|まじめ}に{勉強|べんきょう}してばかりいて、とても{立派|りっぱ}だ。',
            '「〜てばかりいる」は好ましくない行動の繰り返しに対する不満や批判を表すため、褒める文脈には使えません。',
            'Since 〜てばかりいる expresses criticism or dissatisfaction toward repeated undesirable actions, it cannot be used to praise someone.',
        ),
        'comp_ex': [
            '{最近|さいきん}の{会議|かいぎ}は{議論|ぎろん}ばかりで、具体的な{結論|けつろん}がなかなか{出|で}ない。',
            '{弟|おとうと}は{休日|きゅうじつ}になると{昼寝|ひるね}ばかりして、ちっとも{手伝|てつだ}おうとしない。',
        ],
        'quiz': [
            ('部屋でゲームをして（　　　）いないで、たまには外で体を動かしなさい。', 'ばかり', ['ほど', 'きり', 'とおり'], "Don't just spend all your time playing video games in your room; move your body outside once in a while.", '動詞て形＋ばかりいるで同じ好ましくない動作だけを反復・継続していることへの小言を表します。'),
            ('{彼|かれ}は{人|ひと}の{失敗|しっぱい}を{笑|わら}って（　　　）いるが、{自分|じぶん}では{何|なに}もしようとしない。', 'ばかり', ['くらい', 'ついで', 'とたん'], 'He does nothing but laugh at other people\'s mistakes, yet makes no attempt to do anything himself.', '好ましいとは言えない行動を繰り返している様子を批判しています。'),
            ('{甘い物|あまいもの}を{食|た}べて（　　　）いると、{虫歯|むしば}になってしまいますよ。', 'ばかり', ['とおり', '最中', 'かぎり'], 'If you do nothing but eat sweets, you will end up getting cavities.', '偏った行動の反復に対する注意・警告を表します。'),
            ('スマホを{見|み}て（　　　）いないで、{早|はや}く{宿題|しゅくだい}を{終|お}わらせなさい。', 'ばかり', ['ばかりに', 'どころか', 'わりに'], 'Stop doing nothing but looking at your smartphone, and finish your homework quickly.', '「〜てばかりいないで」の形で、同じことばかりする相手をたしなめます。'),
        ],
    },
    125: {
        'reading': 'てごらん',
        'wrong': (
            '{部長|ぶちょう}、こちらの{新|あたら}しい{企画書|きかくしょ}を{一度|いちど}{読|よ}んでごらん。',
            '「〜てごらん」は親や教師など目上の人が子どもや目下の人に優しく促す表現であり、上司には使えません。',
            '〜てごらん is used by parents or teachers to gently encourage children or juniors, so it cannot be used toward a boss.',
        ),
        'comp_ex': [
            'わからない{単語|たんご}があったら、まず{自分|じぶん}で{辞書|じしょ}を{引|ひ}いてみなさい。',
            'この{靴|くつ}、とても{軽|かる}くて{歩|ある}きやすいから、ちょっと{履|は}いてみて。',
        ],
        'quiz': [
            ('とても美味しいケーキだから、遠慮しないで一口食べて（　　　）。', 'ごらん', ['おき', 'しまい', 'みせ'], "It's a very delicious cake, so don't hesitate and try taking a bite.", '動詞て形＋ごらんで目上の人が目下に対して『試しに〜してみてごらん』と優しく促します。'),
            ('ほら、{空|そら}にきれいな{虹|にじ}が{出|で}ているよ。{窓|まど}から{外|そと}を{見|み}て（　　　）。', 'ごらん', ['しまい', 'おき', 'みせ'], 'Look, there is a beautiful rainbow in the sky. Try looking outside from the window.', '親が子どもなどに優しく視線を向けるよう促す表現です。'),
            ('ヒントをあげるから、もう{一度|いちど}{自分|じぶん}の{力|ちから}で{考|かんが}えて（　　　）。', 'ごらん', ['ばかり', 'とおり', 'とたん'], 'I will give you a hint, so try thinking about it once more on your own.', '教師や親が子どもに試行を優しく勧める場面です。'),
            ('{怖|こわ}くないから、このかわいい{子犬|こいぬ}の{頭|あたま}をそっと{撫|な}でて（　　　）。', 'ごらん', ['きり', 'どころ', '最中'], 'It is not scary, so try gently petting this cute puppy on the head.', '「〜てごらん」で安心させながら行動を促します。'),
        ],
    },
    126: {
        'reading': 'てはじめて',
        'wrong': (
            '{日本|にほん}へ{来|き}てはじめて、{今日|きょう}でちょうど{三|さん}か{月|げつ}になります。',
            '「〜てはじめて」は「ある経験をして初めて真実に気づいた」という認識の成立を表すため、単なる時間経過には「〜てから」を使います。',
            '〜てはじめて means realizing a truth only after experiencing something; for simple elapsed time, use 〜てから.',
        ),
        'comp_ex': [
            '{社会人|しゃかいじん}になってからようやく、{時間|じかん}を{守|まも}ることの{大切|たいせつ}さを{実感|じっかん}した。',
            '{自分|じぶん}の{手|て}で{汗|あせ}を{流|なが}して{働|はたら}いてこそ、お{金|かね}の{価値|かち}がわかるというものだ。',
        ],
        'quiz': [
            ('一人暮らしを始めて（　　　）、親の毎日のありがたみが身に染みて分かった。', 'はじめて', ['ばかりに', 'きり', 'とたん'], 'Only after starting to live alone did I truly realize how grateful I should be to my parents every day.', '動詞て形＋はじめてでその経験をして初めて新しい事実や感謝に気づくことを表します。'),
            ('{病気|びょうき}になって（　　　）、{健康|けんこう}がいかに{大切|たいせつ}であるかに{気|き}づかされた。', 'はじめて', ['ついでに', 'とおりに', '最中に'], 'Only after falling ill was I made to realize just how precious health is.', '病気という経験を通して初めて健康の価値を認識したことを表します。'),
            ('{自分|じぶん}が{親|おや}の{立場|たちば}になって（　　　）、{子育|こそだ}ての{大変|たいへん}さを{実感|じっかん}した。', 'はじめて', ['ばかりに', 'どころか', 'くせに'], 'Only after becoming a parent myself did I truly feel how hard raising a child is.', '当事者になって初めて本当の大変さがわかったという文脈です。'),
            ('{実際|じっさい}に{現地|げんち}を{訪|おとず}れて（　　　）、{写真|しゃしん}だけでは{伝|つた}わらない{迫力|はくりょく}に{圧倒|あっとう}された。', 'はじめて', ['とたんに', 'わりに', 'かわりに'], 'Only after actually visiting the site was I overwhelmed by the impact that photos alone could not convey.', '現地へ行くという経験を経て初めて理解できた感動を表します。'),
        ],
    },
    127: {
        'reading': 'ているばあいじゃない',
        'wrong': (
            '{今日|きょう}は{予定|よてい}がなくて{暇|ひま}だから、{勉強|べんきょう}している{場合|ばあい}じゃない。',
            '「〜ている場合じゃない」は緊急事態や切迫した状況で「そんな余裕はない」と戒める表現なので、単に暇なときには使えません。',
            '〜ている場合じゃない warns that one cannot afford to do something due to an urgent situation, so it cannot be used simply because one is free.',
        ),
        'comp_ex': [
            '{締|し}め{切|き}りが{今日|きょう}に{迫|せま}っており、{昼食|ちゅうしょく}を{食|た}べるどころではない。',
            'ライバル{社|しゃ}が{新商品|しんしょうひん}を{発表|はっぴょう}した{今|いま}、このまま{黙|だま}って{見|み}てはいられない。',
        ],
        'quiz': [
            ('試験は明日なんだから、のんびりテレビを見ている（　　　）じゃないよ！', '場合', ['最中', 'はず', 'とおり'], 'The exam is tomorrow, so this is no time to be leisurely watching TV!', '切迫した状況において『今はそんなのんきなことをしている時ではない』と戒めます。'),
            ('{終電|しゅうでん}に{遅|おく}れそうなんだから、ゆっくり{買|か}い{物|もの}をしている（　　　）ではない。', '場合', ['途中', 'つもり', 'かわり'], 'We are about to miss the last train, so this is no time to be shopping at a leisurely pace.', '終電間際という緊急時にのんびりしてはいられないことを表します。'),
            ('{高熱|こうねつ}が{出|で}ているのだから、{無理|むり}をして{働|はたら}いている（　　　）じゃありませんよ。', '場合', ['わけ', 'はず', 'こと'], 'You have a high fever, so this is no time to be pushing yourself to work.', '体調不良の相手に休養を最優先するよう強く忠告する表現です。'),
            ('{発表|はっぴょう}の{時間|じかん}が{迫|せま}っているのに、こんなところで{迷|まよ}っている（　　　）じゃない。', '場合', ['とおり', 'ついで', 'かぎり'], 'The presentation time is approaching, so this is no time to be hesitating in a place like this.', '差し迫った状況で迷っている余裕がないことを表します。'),
        ],
    },
    128: {
        'reading': 'てからでないと',
        'wrong': (
            '{宿題|しゅくだい}を{終|お}わらせてからでないと、すぐにおやつを{食|た}べました。',
            '「〜てからでないと」の後ろには必ず「〜できない」「〜わからない」などの否定表現が続くため、肯定の事実文は続けられません。',
            '〜てからでないと must be followed by a negative predicate such as 〜できない or 〜わからない, not an affirmative past action.',
        ),
        'comp_ex': [
            '{本人|ほんにん}の{同意|どうい}を{得|え}てからでなければ、この{書類|しょるい}は{公開|こうかい}できません。',
            '{実際|じっさい}に{試着|しちゃく}してみてからでないと、サイズが{合|あ}うかどうかは{分|わ}からない。',
        ],
        'quiz': [
            ('上司の正式な承認を得てから（　　　）、このプロジェクトを勝手に進めることはできない。', 'でないと', ['につれて', 'に反して', 'としても'], 'Unless we first obtain formal approval from the supervisor, we cannot advance this project on our own.', '動詞て形＋からでないと（〜できない）で前件を済ませることが後件の絶対前提条件であることを示します。'),
            ('{実物|じつぶつ}を{自分|じぶん}の{目|め}で{確|たし}かめてから（　　　）、{購入|こうにゅう}するかどうかは{決|き}められない。', 'でないと', ['ばかりに', 'とたんに', 'ついでに'], 'Unless I check the actual item with my own eyes first, I cannot decide whether to purchase it.', '購入判断の前提条件として実物確認が不可欠であることを表します。'),
            ('{担当|たんとう}の{医師|いし}に{相談|そうだん}してから（　　　）、この{薬|くすり}の{量|りょう}を{減|へ}らすことはできません。', 'でないと', ['どころか', 'にしろ', 'わりに'], 'Unless you consult the attending physician first, you cannot reduce the dosage of this medicine.', '医師への相談が先決条件であることを示す表現です。'),
            ('{基礎|きそ}の{文法|ぶんぽう}をしっかり{身|み}につけてから（　　　）、{長文|ちょうぶん}を{正確|せいかく}に{読|よ}み{解|と}くのは{難|むずか}しい。', 'でないと', ['といったら', 'とみえて', 'とすれば'], 'Unless you firmly master basic grammar first, it is difficult to read and comprehend long passages accurately.', '基礎習得が応用への必須ステップであることを表します。'),
        ],
    },
    129: {
        'reading': 'てき',
        'wrong': (
            '{彼|かれ}はとても{優|やさ}しい{的|てき}な{人|ひと}で、みんなから{慕|した}われている。',
            '接尾辞「〜的」は主に二字以上の漢語名詞に付いて性質を表し、和語の形容詞や一般的な具体物名詞には付きません。',
            'The suffix 〜的 attaches mainly to Sino-Japanese nouns to form na-adjectives, not to native Japanese adjectives.',
        ),
        'comp_ex': [
            'あのカフェは{昭和|しょうわ}{風|ふう}のレトロな{内装|ないそう}で、{若者|わかもの}に{人気|にんき}がある。',
            '{春|はる}のような{暖|あたた}かい{陽気|ようき}が{続|つづ}き、{公園|こうえん}の{花|はな}が{咲|さ}き{始|はじ}めた。',
        ],
        'quiz': [
            ('彼女の提案はとても現実（　　　）で、すぐに業務に導入できそうだ。', '的', ['風', '気味', '性'], 'Her proposal is very realistic and seems ready to be immediately implemented in operations.', '名詞＋的（てき）でその性質を帯びている状態をつくり、な形容詞として活用させます。'),
            ('{彼|かれ}はいつも{論理|ろんり}（　　　）な{話|はな}し{方|かた}をするので、{説明|せつめい}がとてもわかりやすい。', '的', ['ぽい', 'がち', 'ぶり'], 'Because he always speaks in a logical manner, his explanations are very easy to understand.', '「論理＋的」で「論理の性質を備えた」という意味のな形容詞になります。'),
            ('この{地域|ちいき}では、{伝統|でんとう}（　　　）な{祭|まつ}りが{今|いま}も{毎年|まいとし}{大切|たいせつ}に{受|う}け{継|つ}がれている。', '的', ['風', '流', '気'], 'In this region, traditional festivals are still carefully passed down every year.', '「伝統的」で伝統の性質を持つ様子を表します。'),
            ('{個人|こじん}（　　　）な{意見|いけん}ですが、今回の{計画|けいかく}にはまだ{改善|かいぜん}の{余地|よち}があると{思|おも}います。', '的', ['様', '向', '感'], 'This is my personal opinion, but I think there is still room for improvement in this plan.', '「個人的」で「個人の立場に関する」という意味を表します。'),
        ],
    },
    130: {
        'reading': 'てもはじまらない',
        'wrong': (
            '{会場|かいじょう}に{全員|ぜんいん}が{集|あつ}まっても始まらないから、{司会者|しかいしゃ}を{呼|よ}ぼう。',
            '「〜ても始まらない」は「いくらそうしても何の解決にもならず無駄だ」という慣用表現であり、イベントの開始そのものには使いません。',
            '〜ても始まらない is an idiom meaning "it does no good / accomplishes nothing," not a literal statement about an event starting.',
        ),
        'comp_ex': [
            '{落|お}としてしまったお{皿|さら}を{嘆|なげ}いてもしょうがないから、{早|はや}く{片付|かたづ}けよう。',
            'やる{気|き}のない{相手|あいて}にいくら{熱心|ねっしん}に{説得|せっとく}しても{無駄|むだ}だ。',
        ],
        'quiz': [
            ('過ぎてしまった失敗を今さらクヨクヨ悩んでも（　　　）。次の対策を練ろう。', '始まらない', ['得ない', '済まない', 'かなわない'], "It's no use brooding over past mistakes at this point. Let's work out our next countermeasure.", '動詞て形＋も始まらないで『いくらその行為をしても事態は好転せず、無意味だ』と述べます。'),
            ('{黙|だま}って{考|かんが}え{込|こ}んでいても（　　　）から、まずは{担当者|たんとうしゃ}に{直接|ちょくせつ}{聞|き}いてみよう。', '始まらない', ['たまらない', 'かまわない', 'いられない'], 'Just sitting silently lost in thought will get us nowhere, so let us first ask the person in charge directly.', '悩んでいるだけでは事態が進展しないことを示し、行動を促します。'),
            ('{逃|に}げてしまったバスをいつまでも{待|ま}っていても（　　　）ので、{歩|ある}いて{駅|えき}へ{向|む}かった。', '始まらない', ['きれない', 'すぎない', 'ちがいない'], 'Waiting around for a bus that had already left would get me nowhere, so I walked toward the station.', 'しても無意味であることを悟って別の行動に切り替える文脈です。'),
            ('{結果|けっか}が{出|で}る{前|まえ}から{心配|しんぱい}しても（　　　）よ。やれるだけのことはやったんだから。', '始まらない', ['おわらない', 'かぎらない', 'あたらない'], 'Worrying before the results even come out will do no good. You have done everything you could.', '取り越し苦労をしても仕方がないと励ます表現です。'),
        ],
    },
    131: {
        'reading': 'てもかまわない',
        'wrong': (
            'どうぞこのペンを{自由|じゆう}にお{使|つか}いになってもかまわないでしょうか。',
            '「〜てもかまわない」は主に許可を与える側が使うか、自分が「（自分は）〜てもかまわない」と譲歩する表現で、丁寧な申し出の疑問には使いません。',
            '〜てもかまわない is used to grant permission or state one\'s own concession, not to politely offer something in a question.',
        ),
        'comp_ex': [
            '{鉛筆|えんぴつ}で{書|か}いてもいいですが、{消|き}えないボールペンの{方|ほう}が{望|のぞ}ましいです。',
            'ご{都合|つごう}が{悪|わる}ければ、{来週|らいしゅう}に{変更|へんこう}して{差|さ}し{支|つか}えありません。',
        ],
        'quiz': [
            ('用事が早く片付いた{方|かた}は、定時より前に退室しても（　　　）。', 'かまいません', ['いけません', 'すぎません', 'なりません'], 'Those who have finished their tasks early may leave the room before the scheduled closing time.', '動詞て形＋もかまわないで許可や容認を表し、『差し支えない・問題ない』という意味になります。'),
            ('{私|わたし}は{何時|なんじ}に{帰|かえ}っても（　　　）ので、みなさんのご{予定|よてい}に{合|あ}わせますよ。', 'かまわない', ['たまらない', 'はじまらない', 'いられない'], 'I do not mind what time I go home, so I will adjust to everyone\'s schedule.', '自分にとってはどの選択でも問題ないと譲歩・容認する表現です。'),
            ('この{資料|しりょう}は{返却|へんきゃく}{不要|ふよう}ですので、{直接|ちょくせつ}メモを{書|か}き{込|こ}んでも（　　　）。', 'かまいません', ['すみません', 'ちがいません', 'およびません'], 'This handout does not need to be returned, so it is fine if you write notes directly on it.', '「〜ても問題ない」と許可を与える丁寧な言い方です。'),
            ('{多少|たしょう}{形|かたち}が{不揃|ふぞろ}いでも（　　　）から、{新鮮|しんせん}な{野菜|やさい}を{仕入|しい}れたい。', 'かまわない', ['しかたがない', 'しょうがない', 'たえられない'], 'It does not matter even if the shapes are slightly uneven; I want to stock fresh vegetables.', '条件として許容できる範囲を示す用法です。'),
        ],
    },
    132: {
        'reading': 'てもしょうがない',
        'wrong': (
            '{彼|かれ}はどんなに{練習|れんしゅう}してもしょうがないほど{上手|じょうず}になった。',
            '「〜てもしょうがない」は「〜しても無駄だ・どうにもならない」という諦めを表すため、努力の成果を褒める文には使えません。',
            '〜てもしょうがない expresses resignation that doing something is pointless, so it cannot describe achieving great skill through practice.',
        ),
        'comp_ex': [
            '{壊|こわ}れてしまった時計をいつまでも{眺|なが}めていても{始|はじ}まらない。',
            '{今|いま}さら{彼|かれ}を{責|せ}めても{仕方|しかた}がないから、{全員|ぜんいん}でリカバーしよう。',
        ],
        'quiz': [
            ('悪天候でイベントが中止になったのは残念だが、文句を言っても（　　　）。', 'しょうがない', ['たまらない', 'おられない', '違いない'], "It's disappointing that the event was cancelled due to bad weather, but there's no point complaining.", '動詞て形＋もしょうがないで、文句や後悔をしても無駄であり仕方がないと諦念を述べます。'),
            ('{忘|わす}れてきたものを{今|いま}さら{悔|く}やんでも（　　　）から、{現地|げんち}で{調達|ちょうたつ}しよう。', 'しょうがない', ['かまわない', 'ちがいない', 'たまらない'], 'There is no point regretting what we left behind at this stage, so let us procure it on site.', '後悔しても状況は変わらないため前向きに対処しようという表現です。'),
            ('いくら{急|いそ}いでも{渋滞|じゅうたい}はどうにもならないし、イライラしても（　　　）よ。', 'しょうがない', ['かぎらない', 'すぎない', 'あたらない'], 'No matter how much we hurry, we cannot do anything about the traffic jam, and there is no use getting irritated.', '自分の力では変えられない事態に対して焦っても無駄だと諭します。'),
            ('{相手|あいて}が{留守|るす}なら{待|ま}っていても（　　　）ので、また{明日|あした}{出直|でなお}すことにした。', 'しょうがない', ['はじまらない', 'いられない', 'かなわない'], 'Since the other person is away from home, there is no point waiting around, so I decided to come back tomorrow.', '待っても無意味であると判断したことを表します。'),
        ],
    },
    133: {
        'reading': 'てしょうがない',
        'wrong': (
            '{今日|きょう}は{書類|しょるい}を{三枚|さんまい}{印刷|いんさつ}してしょうがなかった。',
            '「〜てしょうがない」は自然に湧き上がる感情・感覚・欲求が抑えられないほど強いときに使い、意志的な日常動作には使えません。',
            '〜てしょうがない is used for irrepressible emotions, sensations, or urges, not for deliberate everyday actions like printing documents.',
        ),
        'comp_ex': [
            '{試験|しけん}の{合格|ごうかく}{発表|はっぴょう}が{明日|あした}に{迫|せま}り、{緊張|きんちょう}してたまらない。',
            '{故郷|こきょう}で{一人暮|ひとりぐ}らしをしている{祖母|そぼ}の{体調|たいちょう}が{気|き}になってならない。',
        ],
        'quiz': [
            ('大好きなアーティストの初のライブに行けることになり、今から嬉しくて（　　　）。', 'しょうがない', ['ならない', '始まらない', '済まない'], "Since I've gotten to go to my favorite artist's first live concert, I can't help feeling thrilled from now.", '感情・感覚・生理的欲求を表す言葉＋てしょうがないで『感情を抑えられないほど甚だしい』ことを表します。'),
            ('{朝|あさ}から{何|なに}も{食|た}べていないので、お{腹|なか}が{空|す}いて（　　　）。', 'しょうがない', ['かまわない', 'はじまらない', 'ちがいない'], 'Because I have not eaten anything since morning, I am unbearably hungry.', '空腹という生理的感覚が我慢できないほど強いことを表します。'),
            ('{昨日|きのう}のドラマの{続|つづ}きがどうなるのか、{気|き}になって（　　　）。', 'しょうがない', ['すみません', 'いけません', 'すぎません'], 'I cannot stop wondering what will happen next in yesterday\'s drama.', '「気になってしょうがない」で、好奇心や心配が抑えきれない様子を表します。'),
            ('{新|あたら}しい{職場|しょくば}に{慣|な}れるまでは、{毎日|まいにち}{心細|こころぼそ}くて（　　　）だろう。', 'しょうがない', ['かぎらない', 'あたらない', 'およばない'], 'Until you get used to your new workplace, you will probably feel hopelessly uneasy every day.', '心細いという感情が非常に強いことを表します。'),
        ],
    },
    134: {
        'reading': 'てすむ',
        'wrong': (
            '{彼|かれ}は{五年間|ごねんかん}の{研究|けんきゅう}を{重|かさ}ね、ついに{大発見|だいはっけん}をして済んだ。',
            '「〜て済む」は「大きな問題にならず軽い負担や処置だけで解決する」という意味なので、大きな成果を達成した文脈には使えません。',
            '〜て済む means resolving a matter with minor effort without it turning into a bigger problem, not achieving a major breakthrough.',
        ),
        'comp_ex': [
            '{双方|そうほう}が{歩|あゆ}み{寄|よ}ったおかげで、{長引|ながび}いていたトラブルも{話|はな}し{合|あ}いで{解決|かいけつ}した。',
            '{忙|いそが}しい{朝|あさ}は、{朝食|ちょうしょく}をトーストとコーヒーだけで{済|す}ませることが{多|おお}い。',
        ],
        'quiz': [
            ('幸いなことに事故は軽く、車の小さな修理だけで（　　　）。', '済んだ', ['抜いた', 'あげた', '切った'], 'Fortunately the accident was minor, and it was resolved just with a small repair to the car.', '動詞て形・名詞だけで＋済むで大きな大事に至らず、軽い程度で問題が解決した安堵を表します。'),
            ('{電話|でんわ}で{一言|ひとこと}{謝|あやま}れば（　　　）ことを、{黙|だま}っていたせいで{問題|もんだい}が{大|おお}きくなった。', '済む', ['切る', '抜く', '通す'], 'Something that could have been settled with a quick apology over the phone turned into a big problem because I stayed silent.', '「〜ば済む（〜て済む）」で、簡単な対応だけで解決できるはずだったことを表します。'),
            ('{早|はや}めに{病院|びょういん}へ{行|い}ったおかげで、{入院|にゅういん}せずに{薬|くすり}を{飲|の}むだけで（　　　）。', '済んだ', ['果てた', 'きった', 'ぬいた'], 'Thanks to going to the hospital early, I got by just taking medicine without being hospitalized.', '重症化せず軽い治療だけで解決した安堵を表します。'),
            ('この{手続|てつづ}きはネットで{申|もう}し{込|こ}めるので、わざわざ{窓口|まどぐち}へ{行|い}かなくて（　　　）。', '済む', ['おく', 'みる', 'ある'], 'Since you can apply for this procedure online, you can manage without going all the way to the counter.', '「〜なくて済む」で不要な手間を省けることを表します。'),
        ],
    },
    135: {
        'reading': 'てはいけないから',
        'wrong': (
            '{試験|しけん}に{合格|ごうかく}してはいけないから、{毎日|まいにち}{一生懸命|いっしょうけんめい}{勉強|べんきょう}している。',
            '「〜てはいけないから」は「望ましくない事態にならないように」という予防の理由を表すため、望ましい目標には使えません。',
            '〜てはいけないから expresses a precaution to prevent an undesirable outcome, so it cannot be used with a desirable goal like passing an exam.',
        ),
        'comp_ex': [
            '{大切|たいせつ}な{約束|やくそく}の{時間|じかん}に{遅|おく}れないように、{早|はや}めに{家|いえ}を{出|で}た。',
            '{熱中症|ねっちゅうしょう}の{予防|よぼう}のために、こまめに{水分|すいぶん}を{補給|ほきゅう}してください。',
        ],
        'quiz': [
            ('途中で雨に降られては（　　　）から、折りたたみ傘を持って出かけよう。', 'いけない', ['かまわない', 'ならない', 'すぎない'], "Just in case it rains on the way, let's take a folding umbrella when going out.", '動詞て形＋はいけないからで好ましくない事態が起こるのを予防・警戒する理由を表します。'),
            ('{風邪|かぜ}をひいては（　　　）から、{暖|あたた}かいコートを{着|き}て{出|で}かけなさい。', 'いけない', ['しょうがない', 'はじまらない', 'たまらない'], 'Lest you catch a cold, put on a warm coat before going out.', '風邪をひくという悪い事態を避けるための配慮を表します。'),
            ('{道|みち}が{混|こ}んで{遅刻|ちこく}しては（　　　）ので、いつもより{三十分|さんじゅっぷん}{早|はや}く{出発|しゅっぱつ}した。', 'いけない', ['かまわない', 'ちがいない', 'かぎらない'], 'So that I would not be late due to traffic, I departed thirty minutes earlier than usual.', '「〜てはいけないので」で遅刻防止のために早めに行動した理由を示します。'),
            ('{暗証番号|あんしょうばんごう}を{忘|わす}れては（　　　）と{思|おも}い、{手帳|てちょう}にヒントを{控|ひか}えておいた。', 'いけない', ['たまらない', 'すぎない', 'およばない'], 'Thinking that I must not forget my PIN, I jotted down a hint in my notebook.', '忘れる事態を予防するための備えを表します。'),
        ],
    },
    136: {
        'reading': 'とちゅうで',
        'wrong': (
            '{彼|かれ}は{百|ひゃく}メートルを{一瞬|いっしゅん}で{走|はし}り{切|き}った途中で、{靴|くつ}ひもがほどけた。',
            '「途中で」は完了する前のプロセス（道中や進行中）に使うため、「走り切った（完了した）」の後には使えません。',
            '途中で refers to something happening before completion (on the way or mid-process), so it cannot follow a completed action like 走り切った.',
        ),
        'comp_ex': [
            '{会議|かいぎ}の{最中|さいちゅう}に{突然|とつぜん}スマホのアラームが{鳴|な}り、とても{焦|あせ}った。',
            '{仕事|しごと}の{合間|あいま}に{軽|かる}いストレッチをして、{肩|かた}の{凝|こ}りをほぐしている。',
        ],
        'quiz': [
            ('会社へ向かう（　　　）で財布を忘れたことに気づき、慌てて家に戻った。', '途中', ['最中', '最後', '一方'], 'On the way to the company, I realized I had forgotten my wallet and rushed back home.', '動詞辞書形・名詞の＋途中でで移動や動作の進行の途上であることを表します。'),
            ('{映画|えいが}を{見|み}ている（　　　）で{眠|ねむ}ってしまい、{結末|けつまつ}がどうなったのかわからない。', '途中', ['とたん', 'とおり', 'ついで'], 'I fell asleep in the middle of watching the movie, so I do not know how it ended.', '映画がまだ終わっていない進行の半ばで寝てしまったことを表します。'),
            ('{駅|えき}へ{歩|ある}いて{行|い}く（　　　）に、{新|あたら}しくオープンしたパン{屋|や}を見つけた。', '途中', ['かわり', 'かぎり', 'つもり'], 'On my way walking to the station, I found a newly opened bakery.', '目的地へ移動する道中で見つけたことを表します。'),
            ('{長|なが}い{小説|しょうせつ}を{半分|はんぶん}まで{読|よ}んだが、（　　　）でやめてしまった。', '途中', ['最中', '最後', '直後'], 'I read the long novel halfway through, but I stopped in the middle.', '最後まで完了せず中途で中断したことを表します。'),
        ],
    },
    137: {
        'reading': 'といえば',
        'wrong': (
            '{明日|あした}{雨|あめ}が{降|ふ}るといえば、{試合|しあい}は{来週|らいしゅう}に{延期|えんき}されます。',
            '「〜と言えば」は話題の連想・代表例の提示に使う表現であり、単純な未来の仮定条件には「〜なら」「〜たら」を使います。',
            '〜と言えば introduces a natural association or typical example from a topic; for a simple future condition, use 〜なら or 〜たら.',
        ),
        'comp_ex': [
            '{夏|なつ}の{果物|くだもの}というと、まず{冷|つめ}たく{冷|ひ}やしたスイカが{思|おも}い{浮|う}かぶ。',
            'そういえば、{先週|せんしゅう}{貸|か}した{本|ほん}はもう{読|よ}み{終|お}わりましたか。',
        ],
        'quiz': [
            ('日本の春の風物詩（　　　）、やはり満開の桜の花を思い浮かべる。', 'と言えば', ['とすると', 'といっても', 'と見えて'], 'Speaking of a Japanese spring tradition, one naturally thinks of cherry blossoms in full bloom.', '話題に上がった言葉から連想される代表的なイメージを取り上げる表現です。'),
            ('{北海道|ほっかいどう}のグルメ（　　　）、{新鮮|しんせん}な{魚介類|ぎょかいるい}やラーメンが{欠|か}かせない。', 'と言えば', ['とすれば', 'とみえて', 'どころか'], 'Speaking of Hokkaido gourmet food, fresh seafood and ramen are indispensable.', '「北海道のグルメ」という話題から真っ先に連想される代表例を挙げています。'),
            ('「{来月|らいげつ}から{京都|きょうと}へ{転勤|てんきん}するんだ」「{京都|きょうと}（　　　）、{大学時代|だいがくじだい}に{住|す}んでいた{街|まち}だよね」', 'と言えば', ['といっても', 'としたら', 'につけて'], '"I am transferring to Kyoto next month." "Speaking of Kyoto, that is the city where you lived during your university days, right?"', '相手の発言の中の語句を取り上げて関連する話題へ展開する用法です。'),
            ('{温泉|おんせん}（　　　）、{箱根|はこね}や{草津|くさつ}などが{昔|むかし}から{多|おお}くの{人|ひと}に{親|した}しまれている。', 'と言えば', ['とたんに', 'ばかりに', 'に反して'], 'Speaking of hot springs, places like Hakone and Kusatsu have been loved by many people since olden times.', '代表的な名所を連想して提示する表現です。'),
        ],
    },
    138: {
        'reading': 'といい',
        'wrong': (
            '{私|わたし}は{来年|らいねん}の{試験|しけん}に{合格|ごうかく}するために、{毎日|まいにち}{勉強|べんきょう}するといいですね。',
            '「〜といい」は自分の力では直接コントロールできない事態への願望や、相手への控えめな助言に使い、自分の意志的行動には使いません。',
            '〜といい expresses a wish about something beyond one\'s direct control or gentle advice to someone else, not one\'s own intentional resolution.',
        ),
        'comp_ex': [
            '{今度|こんど}の{連休|れんきゅう}は、{家族|かぞく}{全員|ぜんいん}でゆっくり{旅行|りょこう}に{行|い}けたらいいなあ。',
            '{眠|ねむ}れないときは、{寝|ね}る{前|まえ}に{温|あたた}かいミルクを{飲|の}めばいいですよ。',
        ],
        'quiz': [
            ('明日の屋外ピクニックは、天気が晴れてくれる（　　　）ですね。', 'といい', ['はずだ', 'ものだ', 'わけだ'], "It would be nice if the weather turns out sunny for tomorrow's outdoor picnic.", '動詞辞書形＋といいで話し手の個人的な希望や願いを表します。'),
            ('{新|あたら}しい{職場|しょくば}でも、{優|やさ}しい{同僚|どうりょう}に{恵|めぐ}まれる（　　　）なと{願|ねが}っている。', 'といい', ['わけだ', 'はずだ', 'ことだ'], 'I am hoping that I will be blessed with kind colleagues at my new workplace too.', '自分の意志だけでは決められない幸運を願う表現です。'),
            ('{彼|かれ}の{病気|びょうき}が{一日|いちにち}も{早|はや}く{良|よ}くなる（　　　）ですね。', 'といい', ['ものだ', 'わけだ', 'つもりだ'], 'I hope his illness gets better as soon as possible.', '他者の回復を願う温かい希望の表現です。'),
            ('{落|お}とした{定期券|ていきけん}が、{駅|えき}の{窓口|まどぐち}に{届|とど}いている（　　　）のですが。', 'といい', ['はずな', 'わけな', 'ことな'], 'I really hope the commuter pass I dropped has been turned in at the station counter.', 'まだ分からない状況に対して望ましい結果を期待する表現です。'),
        ],
    },
    139: {
        'reading': 'といっても',
        'wrong': (
            '{彼|かれ}は{大金持|おおがねも}ちだといっても、お{金|かね}が{一円|いちえん}もありません。',
            '「AといってもB」は「Aは事実だが、実態はイメージほど大げさではなくB程度だ」と程度を修正する表現なので、Aを完全否定する文は続けられません。',
            'AといってもB softens an exaggerated impression while keeping A partially true, so B cannot completely contradict A.',
        ),
        'comp_ex': [
            '{春|はる}とは{言|い}っても、{朝晩|あさばん}はまだコートが{手放|てばな}せないほど{冷|ひ}え{込|こ}む。',
            '{健康|けんこう}が{大事|だいじ}だとは{分|わ}かっているが、そうは{言|い}っても{運動|うんどう}する{時間|じかん}がない。',
        ],
        'quiz': [
            ('自分で料理を作ると（　　　）、実際は簡単な野菜炒め程度です。', 'いっても', ['すれば', 'したら', '見えて'], "Although I say I cook for myself, in reality it's just simple stir-fried vegetables.", '言葉から受ける大げさな印象を打ち消し、実際はそれほどではないと修正します。'),
            ('{庭|にわ}があると（　　　）、{植木鉢|うえきばち}を{数個|すうこ}{置|お}けるだけの{狭|せま}いスペースだ。', 'いっても', ['すれば', 'みえて', 'したら'], 'Although I say we have a garden, it is just a narrow space where only a few flowerpots can be placed.', '「庭がある」という言葉から相手が抱く広いイメージを控えめに修正します。'),
            ('{英語|えいご}が{話|はな}せると（　　　）、{日常会話|にちじょうかいわ}がなんとかできるレベルにすぎない。', 'いっても', ['いえば', 'いうと', 'みえて'], 'Even though I say I can speak English, it is merely at a level where I can manage daily conversation.', '実際の能力の程度を限定して説明する用法です。'),
            ('{休|やす}みだと（　　　）、{溜|た}まった{家事|かじ}を{片付|かたづ}けるだけで{一日|いちにち}が{終|お}わってしまう。', 'いっても', ['すれば', 'したら', 'きって'], 'Even though you call it a day off, the whole day ends just by clearing up piled-up housework.', '名目上は休みでも実質はゆっくりできない実情を表します。'),
        ],
    },
    140: {
        'reading': 'ということだ',
        'wrong': (
            '{私|わたし}が{今|いま}ここで{直接|ちょくせつ}{見|み}ている{景色|けしき}がとてもきれいだということだ。',
            '「〜ということだ」は他者からの伝聞（「〜そうだ」）または前文の論理的な言い換え（「つまり〜という意味だ」）に使うため、自分の直接知覚には使えません。',
            '〜ということだ expresses secondhand report ("I heard that") or logical restatement ("it means that"), not direct personal perception.',
        ),
        'comp_ex': [
            'この{標識|ひょうしき}は、ここから{先|さき}は{車両|しゃりょう}が{進入|しんにゅう}できないという{意味|いみ}だ。',
            '{天気予報|てんきよほう}によると、{週末|しゅうまつ}は{全国的|ぜんこくてき}に{晴|は}れるそうだ。',
        ],
        'quiz': [
            ('試験に全員合格したということは、みんなの努力が実を結んだという（　　　）。', 'ことだ', ['わけだ', 'ものだ', 'はずだ'], "Passing the exam all together means that everyone's efforts have borne fruit.", '意味の解釈や言い換えを述べる用法と、公的な伝聞を伝える用法の二面があります。'),
            ('{市役所|しやくしょ}からの{知|し}らせによると、{来月|らいげつ}からごみの{収集|しゅうしゅう}{日|び}が{変|か}わるという（　　　）。', 'ことだ', ['ものだ', 'はずだ', 'つもりだ'], 'According to the notice from city hall, the garbage collection days will change starting next month.', '情報源からの正確な伝聞を表す「〜ということだ」です。'),
            ('{返信|へんしん}がまだ{来|こ}ないということは、{彼|かれ}はまだメールを{読|よ}んでいないという（　　　）。', 'ことだ', ['ものだ', 'どころだ', 'ばかりだ'], 'The fact that a reply has not come yet means that he has not read the email yet.', '「AということはBということだ」で事実からの言い換え・結論を表します。'),
            ('{主催者|しゅさいしゃ}の{発表|はっぴょう}では、{今年|ことし}の{来場者|らいじょうしゃ}は{過去|かこ}{最多|さいた}を{記録|きろく}したという（　　　）。', 'ことだ', ['わけだ', 'はずだ', 'きまりだ'], 'According to the organizer\'s announcement, this year\'s attendance recorded an all-time high.', '公的な発表内容を伝える伝聞表現です。'),
        ],
    },
    141: {
        'reading': 'というのは',
        'wrong': (
            '{明日|あした}は{早|はや}く{起|お}きます。というのは、{早|はや}く{寝|ね}ましょう。',
            '文頭の「というのは」は前文の理由や原因を説明する接続表現なので、文末は「〜からだ」などの理由説明で結び、勧誘や命令にはできません。',
            'Sentence-initial というのは explains the reason for the preceding statement and typically ends with 〜からだ, not an invitation or command.',
        ),
        'comp_ex': [
            '「エコ」とは、{地球環境|ちきゅうかんきょう}に{優|やさ}しいライフスタイルのことだ。',
            '{今日|きょう}は{車|くるま}で{来|き}た。なぜなら、{帰|かえ}りに{重|おも}い{荷物|にもつ}を{運|はこ}ぶからだ。',
        ],
        'quiz': [
            ('今回の提案を延期します。（　　　）事前の調査がまだ{不十分|ふじゅうぶん}だからです。', 'というのは', ['それなら', 'そこで', 'すると'], 'We will postpone this proposal. The reason is that the preliminary survey is still insufficient.', '前文の理由・根拠を詳しく補足説明する際に文頭で使われ、末尾に『〜からだ』を伴います。'),
            ('{彼|かれ}は{地理|ちり}にとても{詳|くわ}しい。（　　　）、{以前|いぜん}{旅行会社|りょこうがいしゃ}で{働|はたら}いていたからだ。', 'というのは', ['ところが', 'ところで', 'それとも'], 'He is very knowledgeable about geography. That is because he used to work at a travel agency.', 'なぜ詳しいのかという理由を後から補足説明する接続表現です。'),
            ('「{老舗|しにせ}」（　　　）、{長年|ながねん}{伝統|でんとう}を{守|まも}り{続|つづ}けている{店|みせ}のことだ。', 'というのは', ['というと', 'といえば', 'とすれば'], 'A "shinisè" (long-established shop) means a store that has continued to preserve tradition for many years.', '言葉の意味や定義を説明する「名詞＋というのは〜のことだ」の用法です。'),
            ('{今日|きょう}は{電車|でんしゃ}が{大変|たいへん}{混雑|こんざつ}していた。（　　　）、{駅|えき}の{近く|ちかく}で{大|おお}きな{花火大会|はなびたいかい}があったからだ。', 'というのは', ['したがって', 'すると', 'そこで'], 'The train was extremely crowded today. The reason is that there was a big fireworks display near the station.', '前文の事態の原因を「というのは〜からだ」で説明します。'),
        ],
    },
    142: {
        'reading': 'というと',
        'wrong': (
            '{明日|あした}{晴|は}れると{言|い}うと、{洗濯物|せんたくもの}を{外|そと}に{干|ほ}します。',
            '「〜と言うと」は話題の連想や確認の問い返しに使う表現であり、天候などの仮定条件を表す文には使えません。',
            '〜と言うと is used for mental association or asking for clarification about a topic, not for conditional clauses like weather.',
        ),
        'comp_ex': [
            '{日本|にほん}の{夏|なつ}といえば、{花火大会|はなびたいかい}や{夏祭|なつまつ}りを{思|おも}い{出|だ}す。',
            '「{来週|らいしゅう}の{火曜日|かようび}に{伺|うかが}います」「{火曜日|かようび}というと、{十日|とおか}のことですね」',
        ],
        'quiz': [
            ('京都の秋と（　　　）、鮮やかな紅葉に包まれた古い寺院が思い浮かぶ。', '言うと', ['したら', 'いっても', 'みえて'], 'When you mention autumn in Kyoto, old temples enveloped in vivid autumn foliage come to mind.', '話題に触れた途端に自然と連想される典型的な物事を挙げる表現です。'),
            ('「{今度|こんど}、{金沢|かなざわ}へ{行|い}くんです」「{金沢|かなざわ}と（　　　）、{兼六園|けんろくえん}があるところですね」', '言うと', ['いっても', 'すれば', 'みえて'], '"I am going to Kanazawa next time." "When you say Kanazawa, that is the place where Kenrokuen Garden is, right?"', '相手が出した地名から代表的な特徴を連想して確認する表現です。'),
            ('{昔話|むかしばなし}の{主人公|しゅじんこう}と（　　　）、{誰|だれ}もがまず{桃太郎|ももたろう}を{思|おも}い{出|だ}すだろう。', '言うと', ['いっても', 'したら', 'きって'], 'When you speak of folktale protagonists, everyone probably thinks of Momotaro first.', 'ジャンルから最も典型的な代表例を挙げる用法です。'),
            ('「{明後日|あさって}が{締|し}め{切|き}りです」「{明後日|あさって}と（　　　）、{金曜日|きんようび}までに{提出|ていしゅつ}すればいいんですね」', '言うと', ['いっても', 'みえて', 'きって'], '"The deadline is the day after tomorrow." "By the day after tomorrow, you mean I should submit it by Friday, right?"', '相手の言葉を別の具体的な言葉に置き換えて確認する用法です。'),
        ],
    },
    143: {
        'reading': 'というより',
        'wrong': (
            '{東京|とうきょう}は{大阪|おおさか}というより、{人口|じんこう}がとても{多|おお}い{都市|とし}だ。',
            '「AというよりB」は同一の対象について「Aと表現するよりBと言い換える{方|ほう}が的確だ」と述べる表現なので、別々の2つの都市の単純比較には「〜より」を使います。',
            'AというよりB rephrases a description of the same subject more accurately; to compare two different cities, use simple 〜より.',
        ),
        'comp_ex': [
            'この{映画|えいが}は{怖|こわ}いというよりは、どこか{切|せつ}なくて{心|こころ}に{残|のこ}る{物語|ものがたり}だ。',
            '{彼|かれ}は{休|やす}みの{日|ひ}も{外出|がいしゅつ}せず、むしろ{家|いえ}で{読書|どくしょ}をして{過|す}ごすのが{好|す}きだ。',
        ],
        'quiz': [
            ('彼は私の友人という（　　　）、人生の目標を教えてくれた大切な恩師だ。', 'より', ['ほど', 'きり', 'ばかり'], 'Rather than a friend, he is an important mentor who taught me life goals.', '最初の表現よりも別の表現のほうが的確・妥当であると言い直す表現です。'),
            ('{今日|きょう}は{涼|すず}しいという（　　　）、コートが{欲|ほ}しいくらい{肌寒|はだざむ}い。', 'より', ['ほど', 'だけ', 'まま'], 'Today is chilly enough to want a coat, rather than merely cool.', '「涼しい」という表現では{不十分|ふじゅうぶん}で「肌寒い」の{方|ほう}が適切だと言い換えています。'),
            ('このカフェは{飲食店|いんしょくてん}という（　　　）、まるで{美術館|びじゅつかん}のように{静|しず}かで{落|お}ち{着|つ}く。', 'より', ['くらい', 'とおり', 'ついで'], 'Rather than an eatery, this cafe is as quiet and relaxing as an art museum.', '対象の特徴をよりふさわしい言葉で言い直す表現です。'),
            ('{彼|かれ}が{成功|せいこう}したのは、{運|うん}がよかったという（　　　）、{地道|じみち}な{努力|どりょく}の{結果|けっか}だ。', 'より', ['ばかり', 'どころ', 'かぎり'], 'His success is the result of steady effort rather than good luck.', '原因や本質をより正確に捉え直す文脈です。'),
        ],
    },
    144: {
        'reading': 'ところで',
        'wrong': (
            '{一生懸命|いっしょうけんめい}{練習|れんしゅう}した。ところで、{試合|しあい}に{負|ま}けてしまった。',
            '「ところで」は前の話とは無関係な新しい話題へ切り替える接続詞であり、予想外の結果（逆接）には「ところが」を使います。',
            'ところで switches to a completely new, unrelated topic; to express an unexpected contrary result, use ところが.',
        ),
        'comp_ex': [
            'さて、ここからは{後半|こうはん}のテーマについて{具体的|ぐたいてき}に{話|はな}し{合|あ}いましょう。',
            '{話|はなし}は{変|か}わるが、{先月|せんげつ}{頼|たの}んでおいた{資料|しりょう}の{準備|じゅんび}はどうなったかな。',
        ],
        'quiz': [
            ('本日の議論はここまでです。（　　　）、来週の懇親会にはご出席されますか。', 'ところで', ['だから', 'そこで', 'ところが'], "That is all for today's discussion. By the way, will you be attending next week's social gathering?", '話題をまったく新しい別のテーマへと転換する最も代表的な接続詞です。'),
            ('お{仕事|しごと}は{順調|じゅんちょう}ですか。（　　　）、お{母様|かあさま}のお{加減|かげん}はその後いかがですか。', 'ところで', ['ところが', 'したがって', 'なぜなら'], 'Is your work going well? By the way, how has your mother been feeling since then?', '仕事の話題から母親の体調へと話題を転換する表現です。'),
            ('{新|あたら}しいオフィスにはもう{慣|な}れましたよ。（　　　）、{今度|こんど}の{連休|れんきゅう}はどこかへ{出|で}かけますか。', 'ところで', ['そのため', 'ところが', 'すなわち'], 'I have already gotten used to the new office. By the way, are you going anywhere for the upcoming holidays?', '前の話題が一区切りついたところで別の話題を切り出しています。'),
            ('おいしいコーヒーをごちそうさまでした。（　　　）、{駅|えき}の{近く|ちかく}に{郵便局|ゆうびんきょく}はありますか。', 'ところで', ['だからこそ', 'それゆえ', 'ところが'], 'Thank you for the delicious coffee. By the way, is there a post office near the station?', 'お礼を述べた後に新しい質問へ切り替える自然な会話の流れです。'),
        ],
    },
    145: {
        'reading': 'ところが',
        'wrong': (
            '{今日|きょう}の{会議|かいぎ}はこれで{終|お}わります。ところが、{昼食|ちゅうしょく}は何を{食|た}べに行きますか。',
            '「ところが」は「予想に反して意外な結果になった」という逆接の接続詞なので、単なる話題の転換には「ところで」を使います。',
            'ところが introduces an unexpected result contrary to expectation; to simply change the subject, use ところで.',
        ),
        'comp_ex': [
            '{彼|かれ}は{若|わか}い。しかし、{仕事|しごと}に対する{責任感|せきにんかん}は{誰|だれ}よりも{強|つよ}い。',
            '{簡単|かんたん}な{修理|しゅうり}だと{思|おも}っていたが、{予想|よそう}に{反|はん}して{三日|みっか}もかかった。',
        ],
        'quiz': [
            ('念入りに準備をして面接に臨んだ。（　　　）思わぬ質問に頭が真っ白になってしまった。', 'ところが', ['だから', 'すると', 'ところで'], 'I prepared meticulously for the interview. However, my mind went completely blank at an unexpected question.', '予想していた展開に反して、意外な結果が起こったときの落差を表す逆接接続詞です。'),
            ('{天気予報|てんきよほう}では{一日中|いちにちじゅう}{晴|は}れると{言|い}っていた。（　　　）、{昼過|ひるす}ぎから{急|きゅう}に{大雨|おおあめ}が{降|ふ}り{出|だ}した。', 'ところが', ['ところで', 'したがって', 'つまり'], 'The weather forecast said it would be sunny all day. However, heavy rain suddenly started pouring in the early afternoon.', '予報に反して予想外の雨が降ったという意外性を表します。'),
            ('{薬|くすり}を{飲|の}めばすぐに{熱|ねつ}が{下|さ}がると{思|おも}っていた。（　　　）、{翌朝|よくあさ}になっても{少|すこ}しも{良|よ}くならなかった。', 'ところが', ['そこで', 'だから', 'ところで'], 'I thought my fever would go down right away if I took medicine. However, even the next morning it had not improved at all.', '期待していた結果と逆の事態になった落差を示します。'),
            ('{値段|ねだん}が{安|やす}いので{品質|ひんしつ}は{期待|きたい}していなかった。（　　　）、{使|つか}ってみると{驚|おどろ}くほど{丈夫|じょうぶ}で{便利|べんり}だった。', 'ところが', ['なぜなら', 'ところで', 'すなわち'], 'Since the price was cheap, I did not expect high quality. However, when I tried using it, it was surprisingly durable and convenient.', '良い意味で予想を裏切られた場面にも「ところが」が使われます。'),
        ],
    },
    146: {
        'reading': 'とみえる',
        'wrong': (
            '{鏡|かがみ}を{見|み}たら、{私|わたし}は{今日|きょう}とても{眠|ねむ}いとみえる。',
            '「〜とみえる」は他者や周囲の客観的な様子を観察して「どうやら〜のようだ」と推測する表現であり、自分自身の感覚には使いません。',
            '〜とみえる draws an inference from observing someone else or external signs ("it appears that"), so it is not used for one\'s own internal feelings.',
        ),
        'comp_ex': [
            '{玄関|げんかん}に{傘|かさ}が{置|お}いてあるところを{見|み}ると、{父|ちち}はもう{帰|かえ}ってきたようだ。',
            'あのお店はいつも{長|なが}い{行列|ぎょうれつ}ができているから、かなり{評判|ひょうばん}がいいらしい。',
        ],
        'quiz': [
            ('朝から満面の笑みを浮かべているところを見ると、嬉しい知らせがあったと（　　　）。', 'みえる', ['いえる', 'きこえる', 'おもえる'], 'Seeing that they have a big smile since morning, it seems they received happy news.', '客観的な様子や兆候を観察して『どうやら〜のようだ』と推測・判断します。'),
            ('{隣|となり}の{家|いえ}は{電気|でんき}がすべて{消|き}えているから、{家族|かぞく}で{出|で}かけていると（　　　）。', 'みえる', ['きこえる', 'いえる', 'しれる'], 'Since all the lights in the neighboring house are off, it appears that the family is out.', '電気が消えているという視覚的な根拠から留守だと推測しています。'),
            ('{彼|かれ}はよほどお{腹|なか}が{空|す}いていたと（　　　）、{大盛|おおも}りのカレーをあっという{間|ま}に{平|たい}らげた。', 'みえて', ['いって', 'きいて', 'して'], 'Appearing to have been extremely hungry, he polished off a large serving of curry in no time.', '文中で「〜とみえて」の形をとり、後件の行動から前件の理由を推測します。'),
            ('{道|みち}がすっかり{濡|ぬ}れているから、{夜中|よなか}にかなり{強|つよ}い{雨|あめ}が{降|ふ}ったと（　　　）。', 'みえる', ['いえる', 'おもえる', 'きこえる'], 'Since the road is completely wet, it seems that fairly heavy rain fell during the night.', '地面の状態から夜中の天気を推測する表現です。'),
        ],
    },
    147: {
        'reading': 'とおりに',
        'wrong': (
            '{先生|せんせい}が{優|やさ}しいとおりに、お{礼|れい}の{手紙|てがみ}を{書|か}きました。',
            '「〜とおりに」は名詞や動詞（辞書形・た形）に付いて「それと全く同じやり方で」を表すため、形容詞には接続できません。',
            '〜とおりに attaches to nouns or verbs (dictionary/ta-form) to mean "in the exact same way as," so it cannot follow adjectives.',
        ),
        'comp_ex': [
            '{説明書|せつめいしょ}の{通|とお}りに{部品|ぶひん}を{組|く}み{立|た}てれば、{誰|だれ}でも{簡単|かんたん}に{作|つく}れます。',
            '{事前の|じぜんの}{計画|けいかく}どおりに{工事|こうじ}が{進|すす}み、{予定|よてい}より{早|はや}く{完成|かんせい}した。',
        ],
        'quiz': [
            ('料理本に書かれているレシピの指示（　　　）に作ったら、とても美味しく仕上がった。', '通り', ['途端', '代わり', '最中'], "When I made it just as instructed in the cookbook's recipe, it turned out very delicious.", '名詞・動詞辞書形・た形＋とおりにで指示や計画に寸分違わず同じように行うことを表します。'),
            ('{私|わたし}がこれから{言|い}う（　　　）に、{発音|はつおん}を{繰|く}り{返|かえ}して{練習|れんしゅう}してみてください。', 'とおり', ['ついで', 'ばかり', 'かぎり'], 'Please try practicing by repeating the pronunciation just as I am about to say it.', '動詞辞書形＋とおりにで、手本と同じように行動するよう促します。'),
            ('{天気予報|てんきよほう}が{予想|よそう}した（　　　）、{午後|ごご}から{冷|つめ}たい{北風|きたかぜ}が{吹|ふ}き{始|はじ}めた。', 'とおり', ['とたん', 'どころ', 'くせ'], 'Just as the weather forecast predicted, a cold north wind started blowing in the afternoon.', '予想と実際の結果が一致したことを表します。'),
            ('{地図|ちず}に{描|えが}いてある（　　　）に{歩|ある}いていけば、{迷|まよ}わずに{美術館|びじゅつかん}へ{着|つ}けますよ。', 'とおり', ['わりに', 'うちに', 'うえで'], 'If you walk just as drawn on the map, you can reach the art museum without getting lost.', '示された道順に従って進むことを表します。'),
        ],
    },
    148: {
        'reading': 'とおす',
        'wrong': (
            '{今朝|けさ}は{時間|じかん}があったので、コーヒーを{一杯|いっぱい}{飲|の}み{通|とお}した。',
            '「〜通す」は困難や長い期間を乗り越えて最後まで一貫してやり抜くことに使うため、日常の短時間の動作には「〜切る」や「〜終わる」を使います。',
            '〜通す implies persisting in an action or attitude all the way through despite time or difficulty, not finishing a quick everyday action.',
        ),
        'comp_ex': [
            '{健康|けんこう}のために、{毎朝|まいあさ}{三十分|さんじゅっぷん}のウォーキングを{三年間|さんねんかん}{続|つづ}けている。',
            '{彼|かれ}は{周囲|しゅうい}にどう{言|い}われようと、{自分|じぶん}のポリシーを{最後|さいご}まで{貫|つらぬ}いた。',
        ],
        'quiz': [
            ('どんな困難に直面しても、自分の信念を最後まで曲げずに貫き（　　　）。', '通した', ['直した', '切った', '抜いた'], 'No matter what difficulties I faced, I persisted in sticking to my convictions without wavering until the end.', '動詞ます形＋通すでその態度や行為を最初から最後まで一貫して維持することを表します。'),
            ('{彼|かれ}は{本当|ほんとう}のことを{知|し}っていたのに、{最後|さいご}まで{知|し}らないと{言|い}い（　　　）。', '通した', ['かけた', 'だした', 'すぎた'], 'Even though he knew the truth, he persisted in claiming he did not know until the very end.', '「言い通す」で主張を最後まで変えずに押し通したことを表します。'),
            ('{足|あし}の{痛|いた}みに{耐|た}えながら、{四十二|よんじゅうに}キロのコースを{見事|みごと}に{走|はし}り（　　　）。', '通した', ['始めた', '直した', '忘れた'], 'Enduring the pain in my legs, I splendidly ran all the way through the 42-kilometer course.', '「走り通す」で最初から最後まで休まず走り抜いたことを表します。'),
            ('{彼女|かのじょ}は{忙|いそが}しい{仕事|しごと}のかたわら、{十年間|じゅうねんかん}もボランティア{活動|かつどう}をやり（　　　）。', '通した', ['かけた', '損ねた', '得た'], 'Alongside her busy work, she kept up her volunteer activities all the way through for ten years.', '長期間にわたって途中でやめずに継続したことを表します。'),
        ],
    },
    149: {
        'reading': 'として',
        'wrong': (
            '{私|わたし}は{健康|けんこう}として、{毎朝|まいあさ}{野菜|やさい}ジュースを{飲|の}んでいます。',
            '「〜として」は立場・資格・役割・カテゴリーを示す表現であり、「健康のために」という目的を表すことはできません。',
            '〜として indicates a role, capacity, or category ("as"), so it cannot express purpose ("for the sake of health").',
        ),
        'comp_ex': [
            '{保護者|ほごしゃ}の{立場|たちば}で、{通学路|つうがくろ}の{安全|あんぜん}{対策|たいさく}について{意見|いけん}を{述|の}べた。',
            '{医師|いし}の{資格|しかく}で、{地域|ちいき}の{健康|けんこう}{相談会|そうだんかい}に{参加|さんか}している。',
        ],
        'quiz': [
            ('彼はチームのキャプテン（　　　）、常に仲間を励まし先頭に立って引っ張っている。', 'として', ['に対して', 'にとって', 'について'], 'As team captain, he always encourages teammates and leads by standing at the forefront.', '名詞＋としてで資格・身分・立場・名目を明確に規定して述べる表現です。'),
            ('{京都|きょうと}は{日本|にほん}を{代表|だいひょう}する{観光都市|かんこうとし}（　　　）、{世界中|せかいじゅう}で{広|ひろ}く{知|し}られている。', 'として', ['にとって', 'につれて', 'に反して'], 'Kyoto is widely known around the world as a sightseeing city representing Japan.', '位置づけや性質・カテゴリーを明確に示す「〜として」です。'),
            ('{趣味|しゅみ}（　　　）{始|はじ}めた{写真|しゃしん}だったが、いつの{間|ま}にか{仕事|しごと}になっていた。', 'として', ['ばかりに', 'どころか', 'わりに'], 'Photography was something I started as a hobby, but before I knew it, it had become my job.', 'どのような名目・位置づけで始めたかを表します。'),
            ('{卒業|そつぎょう}の{記念|きねん}（　　　）、クラス{全員|ぜんいん}で{校庭|こうてい}に{桜|さくら}の{木|き}を{植|う}えた。', 'として', ['について', 'にかけて', 'によって'], 'As a commemoration of graduation, the whole class planted a cherry tree in the schoolyard.', '行為の目的や名目（「〜の印として」）を表す用法です。'),
        ],
    },
    150: {
        'reading': 'とすれば',
        'wrong': (
            '{窓|まど}を{開|あ}けるとすれば、{外|そと}では{雪|ゆき}が{静|しず}かに{降|ふ}っていた。',
            '「〜とすれば」は仮定や前提に基づく推論（「もし〜だと仮定するなら」）を表すため、動作の結果偶然気づいた事実の描写には「〜と」や「〜たら」を使います。',
            '〜とすれば expresses logical deduction from an assumption ("assuming that"), not discovering an actual scene upon opening a window.',
        ),
        'comp_ex': [
            'もし{自由|じゆう}な{時間|じかん}が{一か月|いっかげつ}あるとしたら、どの{国|くに}を{旅|たび}してみたいですか。',
            '{時速|じそく}{六十|ろくじゅう}キロで{走|はし}ると{仮定|かてい}すると、{目的地|もくてきち}まで{約|やく}{二時間|にじかん}かかる{計算|けいさん}だ。',
        ],
        'quiz': [
            ('もしこの計画を実行に移す（　　　）、どれくらいの予算と人員が必要になりますか。', 'とすれば', ['とみえて', 'といえば', 'といっても'], 'Assuming that we put this plan into action, roughly how much budget and personnel will be needed?', '普通形＋とすればで『仮にその事態が真実・前提だと仮定した場合』の推論を導きます。'),
            ('{彼|かれ}の{話|はなし}が{事実|じじつ}だ（　　　）、これまでの{調査|ちょうさ}{方針|ほうしん}を{見直|みなお}す{必要|ひつよう}がある。', 'とすれば', ['とみえて', 'といえば', 'どころか'], 'If what he says is true, we need to review our investigation policy up to now.', 'ある事柄を真実だと仮定した上で導き出される判断を表します。'),
            ('{十時|じゅうじ}の{新幹線|しんかんせん}に{乗|の}る（　　　）、{遅|おく}くとも{九時|くじ}には{家|いえ}を{出|で}なければならない。', 'とすれば', ['といっても', 'とたんに', 'ばかりに'], 'Assuming we take the 10 o\'clock bullet train, we must leave home by 9 o\'clock at the latest.', '前提条件を設定して必要な行動を逆算する表現です。'),
            ('{家具|かぐ}を{新|あたら}しく{買|か}い{替|か}える（　　　）、どんなデザインや{色|いろ}がいいと{思|おも}いますか。', 'とすれば', ['とみえて', 'どころか', 'につれて'], 'Assuming we replace the furniture with new pieces, what kind of design and color do you think would be good?', '仮定の状況を置いて相手の意見を求める文脈です。'),
        ],
    },
    151: {
        'reading': 'とても〜ない',
        'wrong': (
            '{今日|きょう}は{時間|じかん}がたくさんあるから、とても{急|いそ}がなくてもいいよ。',
            '「とても〜ない」は「能力や状況から見て到底〜できない」という強い不可能を表すため、「〜しなくてもいい（不要）」の意味では使えません。',
            'とても〜ない means "cannot possibly do" (complete impossibility), not "do not need to do very much."',
        ),
        'comp_ex': [
            '{何度|なんど}{計算|けいさん}し{直|なお}しても、この{複雑|ふくざつ}な{問題|もんだい}はどうしても{解|と}くことができない。',
            'これほど{高価|こうか}な{絵画|かいが}は、{私|わたし}の{貯金|ちょきん}では{到底|とうてい}{買|か}えるものではない。',
        ],
        'quiz': [
            ('こんなに大量の仕事を、今日中に一人で片付けるのは（　　　）無理だ。', 'とても', ['必ずしも', 'ちっとも', 'めったに'], 'Clearing this massive amount of work alone within today is absolutely impossible.', '可能動詞の否定や無理・できない等と呼応し、能力的に到底不可能であることを表します。'),
            ('{辛|から}すぎて、{私|わたし}にはこのカレーを{最後|さいご}まで（　　　）{食|た}べられそうにない。', 'とても', ['めったに', 'かならずしも', 'すこしも'], 'It is so spicy that there is no way I seem able to eat this curry to the end.', '「とても〜そうにない」で到底できそうにないという判断を表します。'),
            ('{彼|かれ}がそんなひどいことを{言|い}ったなんて、{私|わたし}には（　　　）{信|しん}じられない。', 'とても', ['たまに', 'たいして', 'べつに'], 'I cannot possibly believe that he said such a terrible thing.', '心理的に到底受け入れられない・信じられないことを強調します。'),
            ('{吹雪|ふぶき}がますます{強|つよ}まっており、これ以上{山|やま}を{登|のぼ}り{続|つづ}けるのは（　　　）不可能だ。', 'とても', ['ちっとも', 'めったに', 'かならずしも'], 'The snowstorm is getting stronger and stronger, so continuing to climb the mountain any further is utterly impossible.', '「不可能だ」「無理だ」などの否定的な語とも呼応します。'),
        ],
    },
    152: {
        'reading': 'とともに',
        'wrong': (
            '{友達|ともだち}と共に、{昨日|きのう}の{夜|よる}はカフェで{三時間|さんじかん}おしゃべりした。',
            '「〜と共に」は硬い書き言葉・フォーマルな表現なので、日常の軽い雑談には「〜と一緒に」を使うのが自然です。',
            '〜と共に is a formal, literary expression, so in casual everyday conversation like chatting at a cafe, 〜と一緒に is natural.',
        ),
        'comp_ex': [
            '{週末|しゅうまつ}は{家族|かぞく}と{一緒|いっしょ}に、{近所|きんじょ}の{公園|こうえん}でバドミントンをして{遊|あそ}んだ。',
            '{新|あたら}しい{駅|えき}の{開業|かいぎょう}と{同時|どうじ}に、{周辺|しゅうへん}の{商業施設|しょうぎょうしせつ}もオープンした。',
        ],
        'quiz': [
            ('技術の進歩（　　　）、私たちの生活環境は過去数十年で劇的に変化した。', 'と共に', ['に対して', 'に反して', 'にとって'], 'Along with technological progress, our living environment has dramatically changed over the past few decades.', '名詞・動詞辞書形＋と共にで『〜と一緒に』『〜の変化と連動して』『〜であると同時に』を表します。'),
            ('{年|とし}を{重|かさ}ねる（　　　）、{故郷|こきょう}の{自然|しぜん}の{美|うつく}しさがより{深|ふか}く{感|かん}じられるようになった。', 'と共に', ['に反して', 'について', 'にとって'], 'As I grow older, I have come to feel the beauty of my hometown\'s nature more deeply.', '動詞辞書形＋と共にで、一方の変化に伴って他方も変化することを表します。'),
            ('この{計画|けいかく}は{費用|ひよう}を{抑|おさ}える（　　　）、{作業|さぎょう}の{効率|こうりつ}も{高|たか}めることができる。', 'と共に', ['どころか', 'ばかりに', 'くせに'], 'This plan can keep costs down and at the same time improve work efficiency.', '二つの側面が同時に成り立つ（「〜と同時に」）用法です。'),
            ('{太陽|たいよう}が{昇|のぼ}る（　　　）、{街|まち}は少しずつ{活気|かっき}を{取|と}り{戻|もど}していった。', 'と共に', ['わりに', 'かわりに', 'ついでに'], 'As the sun rose, the town gradually regained its liveliness.', '時間の経過・自然の変化と連動して状況が変わる様子を描写します。'),
        ],
    },
    153: {
        'reading': 'とはかぎらない',
        'wrong': (
            '{明日|あした}の{会議|かいぎ}には、{私|わたし}が出席するとは限らない。',
            '「〜とは限らない」は一般的な通念に対して「例外もある（常にそうとは限らない）」と部分否定する表現であり、個人の1回の予定には使いません。',
            '〜とは限らない expresses partial negation of a general assumption ("not always true"), not uncertainty about one\'s own single plan.',
        ),
        'comp_ex': [
            '{高価|こうか}な{道具|どうぐ}を{使|つか}ったからといって、{必|かなら}ずしも{良|よ}い{作品|さくひん}ができるわけではない。',
            '{経験|けいけん}が{長|なが}いからといって、{誰|だれ}でも{教|おし}えるのが{上手|じょうず}だとは{言|い}えない。',
        ],
        'quiz': [
            ('値段が高い商品だからといって、必ずしも品質が優れているとは（　　　）。', '限らない', ['違いない', 'ほかならない', 'すぎない'], 'Just because a product is expensive does not necessarily mean its quality is superior.', '『必ずしも＋〜とは限らない』と呼応して全面的な例外のない断定を和らげて部分否定します。'),
            ('{天気予報|てんきよほう}がいつも{百|ひゃく}パーセント{当|あ}たるとは（　　　）から、{傘|かさ}を{持|も}って{行|い}こう。', '限らない', ['違いない', 'かまわない', 'たまらない'], 'Since weather forecasts are not always 100% accurate, let us bring an umbrella.', '常に当たるとは言えないという部分否定を表します。'),
            ('{有名|ゆうめい}な{観光地|かんこうち}が、{誰|だれ}にとっても{満足|まんぞく}できる{場所|ばしょ}だとは（　　　）。', '限らない', ['すぎない', 'あたらない', 'およばない'], 'A famous sightseeing spot is not necessarily a satisfying place for everyone.', '人によって{感|かん}じ{方|かた}が異なるため一概には言えないことを示します。'),
            ('{若|わか}い{人|ひと}がみんな{最新|さいしん}の{流行|りゅうこう}に{詳|くわ}しいとは（　　　）。', '限らない', ['ちがいない', 'はじまらない', 'いられない'], 'Not all young people are necessarily knowledgeable about the latest trends.', '固定観念に対して例外があることを指摘する表現です。'),
        ],
    },
    154: {
        'reading': 'ついでに',
        'wrong': (
            '{大学|だいがく}に{合格|ごうかく}するために、{毎日|まいにち}{散歩|さんぽ}のついでに{十時間|じゅうじかん}{勉強|べんきょう}した。',
            '「〜ついでに」は主たる行動の機会を利用して軽い副次的な用事を済ませる表現なので、重大で長時間の本命の行動を後ろに置くのは不自然です。',
            '〜ついでに uses a main action as an opportunity to do a minor secondary task, so putting a major ten-hour effort as the side task is unnatural.',
        ),
        'comp_ex': [
            '{夕方|ゆうがた}の{散歩|さんぽ}がてら、{駅前|えきまえ}の{本屋|ほんや}に{立|た}ち{寄|よ}って{雑誌|ざっし}を{買|か}った。',
            '{出張|しゅっちょう}で{大阪|おおさか}へ{行|い}く{機会|きかい}に、{大学時代|だいがくじだい}の{友人|ゆうじん}に{会|あ}うつもりだ。',
        ],
        'quiz': [
            ('郵便局へ手紙を出しに行く（　　　）に、コンビニで切手も買ってきてほしい。', 'ついで', ['とおり', '最中', '途中'], 'While you are going to the post office to mail a letter, please buy stamps at the convenience store too.', '本来の主たる用事を行う機会を利用して、合わせて別の行動も済ませることを表します。'),
            ('{台所|だいどころ}を{片付|かたづ}けた（　　　）に、{冷蔵庫|れいぞうこ}の{中|なか}もきれいに{拭|ふ}いておいた。', 'ついで', ['とたん', 'あまり', 'くせ'], 'While I was tidying up the kitchen, I also wiped the inside of the refrigerator clean.', '動詞た形＋ついでにで、一つの作業の流れで別の掃除も済ませたことを表します。'),
            ('{自分|じぶん}のお{茶|ちゃ}を{入|い}れる（　　　）に、{母|はは}の{分|ぶん}も{一緒|いっしょ}に{入|い}れた。', 'ついで', ['ばかり', 'どころ', 'かぎり'], 'While making tea for myself, I made a cup for my mother at the same time.', '自分の分を用意する機会に相手の分も作ったという自然な用法です。'),
            ('{図書館|としょかん}へ{本|ほん}を{返|かえ}しに{行|い}く（　　　）に、{来週|らいしゅう}のイベントのチラシをもらってきた。', 'ついで', ['とおり', 'わり', 'うち'], 'While going to the library to return books, I picked up a flyer for next week\'s event.', '主目的の移動を利用して別の用事も果たしたことを表します。'),
        ],
    },
    155: {
        'reading': 'ついに',
        'wrong': (
            '{今朝|けさ}は{七時|しちじ}に{起|お}きて、ついに{顔|かお}を{洗|あら}って{朝ご飯|あさごはん}を{食|た}べた。',
            '「ついに」は長い時間や苦労の末に最終的な結果に至ったときに使う副詞なので、毎日の当たり前の朝の日課には使えません。',
            'ついに is used when a final outcome is reached after a long process or effort, not for routine daily habits like washing one\'s face.',
        ),
        'comp_ex': [
            '{何日|なんにち}も{連絡|れんらく}を{待|ま}っていたが、とうとう{最後|さいご}まで{返事|へんじ}は{来|こ}なかった。',
            '{渋滞|じゅうたい}に{巻|ま}き{込|こ}まれたが、{開演|かいえん}の{五分前|ごふんまえ}にようやく{会場|かいじょう}に{到着|とうちゃく}した。',
        ],
        'quiz': [
            ('10年間に及ぶ地道な研究が実を結び、（　　　）新しい特許を取得することができた。', 'ついに', ['決して', 'ちっとも', 'めったに'], 'Steady research spanning 10 years bore fruit, and at last we were able to acquire a new patent.', '長い時間や努力の末に待望の結果に到達したときの達成感を込めて使います。'),
            ('{何度|なんど}も{挑戦|ちょうせん}を{続|つづ}けた{結果|けっか}、（　　　）{念願|ねんがん}のコンテストで{優勝|ゆうしょう}を果たした。', 'ついに', ['まるで', 'わざと', 'まさか'], 'As a result of continuing to challenge ourselves again and again, we finally won first place in the long-awaited contest.', '粘り強い挑戦の末に目標を達成した感動を表します。'),
            ('{長年|ながねん}{使|つか}い{続|つづ}けてきた{洗濯機|せんたくき}が、{昨日|きのう}（　　　）{動|うご}かなくなってしまった。', 'ついに', ['けっして', 'すこしも', 'かならずしも'], 'The washing machine we had kept using for many years finally stopped working yesterday.', '長い年月の末に寿命を迎えたという最終的な結果にも使われます。'),
            ('{半年間|はんとしかん}かけて{準備|じゅんび}してきた{新|あたら}しいお店が、{明日|あした}（　　　）オープンする。', 'ついに', ['めったに', 'たいして', 'ちっとも'], 'The new shop we have spent half a year preparing will finally open tomorrow.', '長い準備期間を経て待望の日を迎える文脈です。'),
        ],
    },
    156: {
        'reading': 'つい',
        'wrong': (
            '{健康|けんこう}のために、{来月|らいげつ}からは{毎朝|まいあさ}つい{走|はし}るつもりです。',
            '「つい」は自分の意志に反して無意識・うっかりやってしまった過去の失敗や衝動に使われるため、未来の計画や決意には使えません。',
            'つい describes doing something unintentionally or on impulse against one\'s better judgment, so it cannot be used for future plans or resolutions.',
        ),
        'comp_ex': [
            '{乗|の}り{換|か}えの{駅|えき}で{本|ほん}に{夢中|むちゅう}になり、うっかり{降|お}り{過|す}ごしてしまった。',
            'あまりにも{景色|けしき}が{美|うつく}しかったので、{思|おも}わず{足|あし}を{止|と}めて{見入|みい}ってしまった。',
        ],
        'quiz': [
            ('ダイエット中だと分かっていたのに、目の前の甘いケーキを（　　　）食べてしまった。', 'つい', ['わざと', 'まるで', '決して'], 'Even though I knew I was on a diet, I carelessly ended up eating the sweet cake in front of me.', '理性ではいけないと分かっていながら、誘惑や油断で無意識にしてしまう様子を表します。'),
            ('{本屋|ほんや}に{立|た}ち{寄|よ}ると、{予定|よてい}になかった{雑誌|ざっし}まで（　　　）{買|か}ってしまう。', 'つい', ['けっして', 'ちっとも', 'かならずしも'], 'Whenever I drop by a bookstore, I unintentionally end up buying magazines I had not planned to get.', '習慣的に無意識のうちにやってしまう行動を「つい〜てしまう」で表します。'),
            ('{話|はなし}が{盛|も}り{上|あ}がってしまい、（　　　）{時間|じかん}が{経|た}つのを{忘|わす}れていた。', 'つい', ['わざと', 'めったに', 'たいして'], 'The conversation got so lively that I inadvertently lost track of time.', '夢中になって気づかないうちに時間が過ぎていた場面です。'),
            ('{秘密|ひみつ}にしておこうと{思|おも}っていたのに、うれしくて（　　　）{友達|ともだち}に{話|はな}してしまった。', 'つい', ['すこしも', 'まるで', 'まさか'], 'Even though I intended to keep it a secret, I was so happy that I accidentally told my friend.', '感情を抑えきれずうっかり口に出してしまったことを表します。'),
        ],
    },
    157: {
        'reading': 'つまり',
        'wrong': (
            '{今日|きょう}は{雨|あめ}が{降|ふ}っている。つまり、{私|わたし}は{昨日|きのう}ラーメンを{食|た}べた。',
            '「つまり」は前文の内容を要約したり結論へ言い換えたりする接続詞なので、論理的なつながりのない文を結ぶことはできません。',
            'つまり summarizes or restates the preceding statement as a logical conclusion, so it cannot connect two logically unrelated sentences.',
        ),
        'comp_ex': [
            '{彼|かれ}が{言|い}いたいことは、{要|よう}するに「もっと{準備|じゅんび}{期間|きかん}が{必要|ひつよう}だ」ということだ。',
            '{日本|にほん}の{首都|しゅと}、すなわち{東京|とうきょう}には{多|おお}くの{文化施設|ぶんかしせつ}が{集|あつ}まっている。',
        ],
        'quiz': [
            ('明日は休日で学校も会社も休みだ。（　　　）一日中自分の好きなことに没頭できる。', 'つまり', ['それなら', 'なぜなら', 'ただし'], 'Tomorrow is a holiday and both schools and companies are off. In other words, I can devote myself to what I love all day long.', '前述の事実を要約し、別の平易な言葉で本質をズバリと言い換える接続詞です。'),
            ('{母|はは}の{兄|あに}、{私|わたし}にとっての（　　　）{伯父|おじ}は、{高校|こうこう}で{数学|すうがく}を{教|おし}えている。', 'つまり', ['ところが', 'ところで', 'ただし'], 'My mother\'s older brother, that is to say my uncle, teaches mathematics at a high school.', '関係をわかりやすく言い換える用法です。'),
            ('{賛成|さんせい}の{人|ひと}が{過半数|かはんすう}を{超|こ}えた。（　　　）、この{提案|ていあん}は{正式|せいしき}に{採用|さいよう}されたということだ。', 'つまり', ['しかし', 'なぜなら', 'ところで'], 'Those in favor exceeded the majority. In short, it means this proposal has been officially adopted.', '事実から導かれる最終的な結論を要約して述べます。'),
            ('{彼|かれ}は{連絡|れんらく}もなしに{三十分|さんじゅっぷん}も{遅|おく}れてきた。（　　　）、{約束|やくそく}を{軽|かる}く{見|み}ているのだ。', 'つまり', ['ところが', 'それとも', 'もっとも'], 'He showed up thirty minutes late without even contacting us. In other words, he takes promises lightly.', '行動の背景にある本質を言い換えて指摘する表現です。'),
        ],
    },
    158: {
        'reading': 'つもりだった',
        'wrong': (
            '{来年|らいねん}はぜひ{海外旅行|かいがいりょこう}に{行|い}くつもりだったが、今からとても{楽|たの}しみだ。',
            '「〜つもりだった」は「当初はその予定・思い込みだったが、実際はそうならなかった（変更・失敗した）」ときに使うため、現在も継続中の予定には「〜つもりだ」を使います。',
            '〜つもりだった indicates a past intention or belief that did not work out or changed; for a plan still in effect, use 〜つもりだ.',
        ),
        'comp_ex': [
            'しっかり{復習|ふくしゅう}した{気|き}でいたが、テストでは{思|おも}ったほど{点数|てんすう}が{取|と}れなかった。',
            '{週末|しゅうまつ}はキャンプに{行|い}く{予定|よてい}だったが、{台風|たいふう}が{近|ちか}づいたため{中止|ちゅうし}した。',
        ],
        'quiz': [
            ('きちんと鍵を閉めた（　　　）だったが、帰宅したら玄関が{開|あ}いたままになっていた。', 'つもり', ['こと', 'はず', 'わけ'], 'I believed I had locked the door properly, but when I came home the entrance was left open.', '自分ではそのようにしたという強い思い込みがあったが、実際は違っていた落差を表します。'),
            ('{冗談|じょうだん}で{言|い}った（　　　）だったが、{相手|あいて}を{本気|ほんき}で{怒|おこ}らせてしまった。', 'つもり', ['はず', 'わけ', 'もの'], 'I meant it as a joke, but I ended up making the other person genuinely angry.', '自分の意図と実際の結果が食い違ってしまったことを表します。'),
            ('{今日|きょう}は{早|はや}く{帰|かえ}る（　　　）だったが、{急|きゅう}な{仕事|しごと}が{入|はい}って{残業|ざんぎょう}になった。', 'つもり', ['こと', 'もの', 'とこ'], 'I had intended to go home early today, but urgent work came up and I had to work overtime.', '動詞辞書形＋つもりだったがで、予定していた計画が実現しなかったことを表します。'),
            ('{名前|なまえ}を{丁寧|ていねい}に{書|か}いた（　　　）だったが、あとで{見直|みなお}したら{漢字|かんじ}が{一文字|ひともじ}{間違|まちが}っていた。', 'つもり', ['わけ', 'こと', 'まま'], 'I thought I had written my name carefully, but when I looked it over later, one kanji character was wrong.', 'た形＋つもりだったがで、自分の認識と事実のずれを表します。'),
        ],
    },
    159: {
        'reading': 'つもりで',
        'wrong': (
            '{私|わたし}は{本当|ほんとう}の{医者|いしゃ}のつもりで、{毎日|まいにち}{病院|びょういん}で{手術|しゅじゅつ}をしています。',
            '「Aのつもりで」は「実際はAではないが、仮にAになった気持ちで」という比喩的な心構えを表すため、実際の職業そのものには「〜として」を使います。',
            'Aのつもりで means adopting the mindset "as if" one were A when in reality one is not; for one\'s actual profession, use 〜として.',
        ),
        'comp_ex': [
            '{絶対|ぜったい}に{優勝|ゆうしょう}するという{気概|きがい}で、{毎日|まいにち}の{厳|きび}しい{練習|れんしゅう}に{取|と}り{組|く}んでいる。',
            '{新入社員|しんにゅうしゃいん}に{戻|もど}った{気持|きも}ちで、{基礎|きそ}からもう{一度|いちど}{学|まな}び{直|なお}したい。',
        ],
        'quiz': [
            ('本番の試験と同じ（　　　）で、毎日の模擬試験に緊張感を持って臨もう。', 'つもり', ['くせ', 'わりに', 'とおり'], "With the mindset as if it were the actual exam, let's approach the daily practice tests with tension.", '実際は異なっていても、あたかもその状態であるかのような強い気持ち・構えで臨むことを表します。'),
            ('{旅行|りょこう}に{行|い}った（　　　）で、その{分|ぶん}のお{金|かね}を{毎月|まいつき}コツコツ{貯金|ちょきん}している。', 'つもり', ['ばかり', 'とたん', 'どころ'], 'Pretending that I went on a trip, I am steadily saving that amount of money every month.', '実際には行っていないが、行ったと仮定した気持ちで行動することを表します。'),
            ('どうぞご{自分|じぶん}の{家|いえ}にいる（　　　）で、リラックスしてお{過|す}ごしください。', 'つもり', ['かわり', 'ついで', 'かぎり'], 'Please relax and make yourself at home as if you were in your own house.', '来客に対してくつろいでもらうための定番の表現です。'),
            ('これが{最後|さいご}のチャンスだという（　　　）で、{全力|ぜんりょく}を{尽|つ}くして{挑戦|ちょうせん}しよう。', 'つもり', ['とおり', 'くせ', 'あまり'], 'With the mindset that this is our last chance, let us do our utmost and take on the challenge.', '強い覚悟や心構えを持って行動することを表します。'),
        ],
    },
    160: {
        'reading': 'うちに',
        'wrong': (
            '{夏休|なつやす}みのうちに、{八月|はちがつ}{十日|とおか}に{家族|かぞく}で{海|うみ}へ{行|い}きました。',
            '「〜うちに」は「状態が変わらないうちに」または「〜しているうちに自然と変化が起きた」という文脈で使い、特定の日付の出来事には「〜に」や「〜のときに」を使います。',
            '〜うちに means "before a state changes" or "naturally while doing," so it is not used to pinpoint a single event on a specific date.',
        ),
        'comp_ex': [
            '{母|はは}が{昼寝|ひるね}をしているあいだに、{洗濯物|せんたくもの}をすべてたたんでおいた。',
            '{暗|くら}くならないうちに、{山道|やまみち}を{抜|ぬ}けてふもとの{駅|えき}まで{降|お}りよう。',
        ],
        'quiz': [
            ('せっかくの温かいスープが冷めない（　　　）に、どうぞ召し上がってください。', 'うち', ['あいだ', '最中', '途端'], 'Please enjoy the warm soup while it is still warm and before it gets cold.', 'ある好ましい状態が変化してしまう前に、チャンスを逃さず行動することを促します。'),
            ('{若|わか}い（　　　）にたくさんの{本|ほん}を{読|よ}み、いろいろな{場所|ばしょ}を{旅|たび}しておきたい。', 'うち', ['まま', 'きり', 'たび'], 'While I am still young, I want to read many books and travel to various places.', '若さが失われる前に経験を重ねておきたいという表現です。'),
            ('{何度も|なんども}{繰|く}り{返|かえ}し{練習|れんしゅう}している（　　　）に、{難|むずか}しい{曲|きょく}もスムーズに{弾|ひ}けるようになった。', 'うち', ['とおり', 'ついで', 'かわり'], 'As I practiced over and over again, I naturally became able to play the difficult piece smoothly.', '継続している間に自然と変化が起きたことを表す「〜ているうちに」です。'),
            ('{忘|わす}れない（　　　）に、{今|いま}{聞|き}いた{大切|たいせつ}な{予定|よてい}を{手帳|てちょう}にメモしておこう。', 'うち', ['最中', '途端', 'かぎり'], 'Before I forget, let me jot down the important schedule I just heard in my planner.', '記憶が薄れてしまう前に行動することを表します。'),
        ],
    },
    161: {
        'reading': 'うえで',
        'wrong': (
            '{朝|あさ}{起|お}きた上で、{顔|かお}を{洗|あら}って{歯|は}を{磨|みが}きました。',
            '「〜た上で」は重要な判断や行動の前に「まず必要な準備・確認・相談をしっかり行った後で」を表すため、単なる日常動作の連続には「〜てから」を使います。',
            '〜た上で is used when taking an important step after completing necessary preparation or consultation, not for routine sequences like waking up and washing one\'s face.',
        ),
        'comp_ex': [
            '{契約書|けいやくしょ}の{内容|ないよう}をよく{読|よ}んでから、{署名|しょめい}と{捺印|なついん}をしてください。',
            '{企画|きかく}の{初期|しょき}の{段階|だんかい}で、{予算|よさん}の{上限|じょうげん}をしっかり{決|き}めておく{必要|ひつよう}がある。',
        ],
        'quiz': [
            ('両親や学校の先生と{十分|じゅうぶん}に相談した（　　　）で、今後の進路を最終決定したい。', '上', ['前', '中', '下'], 'After thoroughly consulting with my parents and school teachers, I want to make the final decision on my future path.', '動詞た形＋上でで、まず前提となる動作を終えた後で次の行動に移る順序を表します。'),
            ('{説明書|せつめいしょ}をよくお{読|よ}みになった（　　　）で、{正|ただ}しくお{使|つか}いください。', '上', ['中', '下', '先'], 'Please use the product correctly after having read the instruction manual carefully.', '利用の前提として説明書を読むことが必要であることを示します。'),
            ('{現地|げんち}の{状況|じょうきょう}を{詳|くわ}しく{調査|ちょうさ}した（　　　）で、{具体的|ぐたいてき}な{計画|けいかく}を{立|た}てよう。', '上', ['前', '最中', '途端'], 'Let us draw up a concrete plan after investigating the local situation in detail.', 'まず調査を行い、その結果を踏まえて計画を立てる手順を表します。'),
            ('お{互|たが}いの{意見|いけん}をしっかり{納得|なっとく}した（　　　）で、{共同|きょうどう}プロジェクトを{始|はじ}めた。', '上', ['内', '中', '間'], 'After fully agreeing on each other\'s opinions, we started the joint project.', '事前の合意を踏まえて次の段階へ進んだことを表します。'),
        ],
    },
    162: {
        'reading': 'うえに',
        'wrong': (
            'このかばんはデザインがとてもおしゃれな上に、{少|すこ}し{重|おも}くて{使|つか}いにくい。',
            '「〜上に」はプラスの評価にさらにプラス、またはマイナスにさらにマイナスを重ねる表現なので、長所と短所を逆接で結ぶ文には「〜が」「〜ものの」を使います。',
            '〜上に adds a positive point to another positive point (or negative to negative), so it cannot contrast a merit with a demerit.',
        ),
        'comp_ex': [
            '{彼|かれ}は{英語|えいご}だけでなく、フランス{語|ご}やスペイン{語|ご}も{流暢|りゅうちょう}に{話|はな}せる。',
            'あの{店|みせ}のパンは{焼|や}きたてでおいしい。その{上|うえ}、{値段|ねだん}も{手頃|てごろ}だ。',
        ],
        'quiz': [
            ('このアパートは家賃が手頃な（　　　）に、駅から徒歩3分と立地も非常に便利だ。', '上', ['中', '下', '先'], 'This apartment has reasonable rent, and on top of that, its location is very convenient with a 3-minute walk from the station.', '普通形＋上にでプラスのことにさらにプラス、またはマイナスにマイナスが重なることを表します。'),
            ('{今日|きょう}は{強|つよ}い{風|かぜ}が{吹|ふ}いている（　　　）に、{冷|つめ}たい{雨|あめ}まで{降|ふ}り{出|だ}して{本当|ほんとう}に{寒|さむ}い。', '上', ['内', '中', '下'], 'Today, in addition to a strong wind blowing, cold rain has also started falling, making it truly cold.', '悪条件にさらに悪条件が重なった場面を表します。'),
            ('{彼女|かのじょ}は{歌|うた}が{上手|じょうず}な（　　　）に、ピアノやギターの{演奏|えんそう}もプロ{並|な}みだ。', '上', ['内', '間', '前'], 'Not only is she good at singing, her piano and guitar playing are also at a professional level.', '優れた才能にさらに別の長所が加わることを表します。'),
            ('このパソコンは{軽|かる}くて{持|も}ち{運|はこ}びやすい（　　　）に、バッテリーも{長持|ながも}ちする。', '上', ['後', '中', '外'], 'In addition to being light and easy to carry around, this laptop also has a long-lasting battery.', '商品の良い特徴を二つ重ねて述べる表現です。'),
        ],
    },
    163: {
        'reading': 'はべつとして',
        'wrong': (
            '{野菜|やさい}は{別|べつ}として、ニンジンもトマトもピーマンも{全部|ぜんぶ}{食|た}べました。',
            '「Aは別としてB」は「Aは例外として一旦横に置き、他のBについては〜だ」と述べる表現なので、Aの中に含まれるもの全体をBで肯定すると矛盾します。',
            'Aは別としてB sets A aside as an exception while making a statement about B, so B cannot simply affirm the entire category of A.',
        ),
        'comp_ex': [
            '{月曜日|げつようび}の{休館日|きゅうかんび}は{除|のぞ}いて、{毎日|まいにち}{午前|ごぜん}{九時|くじ}から{開館|かいかん}しています。',
            '{細|こま}かいデザインはさておき、まずは{全体|ぜんたい}の{予算|よさん}とスケジュールを{決|き}めよう。',
        ],
        'quiz': [
            ('結果がどうなるかは（　　　）として、全力を尽くして挑戦したこと自体に価値がある。', '別', ['特別', '基準', '中心'], 'Setting aside how the result turns out, the very fact that we challenged with all our might has value.', '名詞＋は別としてで『それは一旦考慮の外に置いて、まずはこちらを論じる』という態度を表します。'),
            ('{値段|ねだん}の{高|たか}さは（　　　）として、このコートの{品質|ひんしつ}と{暖|あたた}かさは{確|たし}かに{素晴|すば}らしい。', '別', ['他', '外', '次'], 'Setting aside its high price, the quality and warmth of this coat are certainly wonderful.', '値段という点は一旦考慮から外して品質を高く評価する表現です。'),
            ('{実際|じっさい}に{買|か}うかどうかは（　　　）として、{新|あたら}しいモデルを{見|み}にショールームへ{行|い}ってみよう。', '別', ['逆', '上', '先'], 'Aside from whether we actually buy it or not, let us go to the showroom to see the new model.', '購入の有無はさておき、まず見に行こうという文脈です。'),
            ('{上手|じょうず}か{下手|へた}かは（　　　）として、{私|わたし}は{人前|ひとまえ}で{歌|うた}を{歌|うた}うのが{大好|だいす}きだ。', '別', ['他', '外', '違'], 'Regardless of whether I am good or bad at it, I love singing in front of people.', '巧拙は問題にせず好きだという気持ちを述べています。'),
        ],
    },
    164: {
        'reading': 'は〜でゆうめい',
        'wrong': (
            'この{町|まち}はおいしいリンゴに{有名|ゆうめい}で、{毎年|まいとし}{多|おお}くの{人|ひと}が{訪|おとず}れます。',
            '「〜で有名だ」は知名度の原因・理由・特徴を助詞「で」で示すため、「に有名」とすることはできません（「〜に人気がある」との混同に注意）。',
            'Famous for X takes the particle で (Xで有名だ) to mark the reason for fame, not に (do not confuse with 〜に人気がある).',
        ),
        'comp_ex': [
            'この{地域|ちいき}は、{日本|にほん}でも{有数|ゆうすう}の{豪雪地帯|ごうせつちたい}として{知|し}られている。',
            '{吉野山|よしのやま}は、{春|はる}になると{山|やま}{全体|ぜんたい}がピンク{色|いろ}に{染|そ}まる{桜|さくら}の{名所|めいしょ}だ。',
        ],
        'quiz': [
            ('北海道の富良野は、初夏に咲き誇る美しいラベンダー畑（　　　）全国的に有名だ。', 'で', ['を', 'に', 'と'], 'Furano in Hokkaido is nationally famous for its beautiful lavender fields blooming in early summer.', '『名詞は＋原因・理由（名詞）＋で有名だ』で知名度の理由・特色を示します。'),
            ('{香川県|かがわけん}は、コシの{強|つよ}いさぬきうどんの{産地|さんち}（　　　）{全国的|ぜんこくてき}に{有名|ゆうめい}だ。', 'で', ['を', 'へ', 'より'], 'Kagawa Prefecture is nationally famous as the production area of firm Sanuki udon noodles.', '有名な理由・特徴を表す助詞「で」が入ります。'),
            ('この{温泉街|おんせんがい}は、{歴史|れきし}のある{木造|もくぞう}の{旅館|りょかん}が{並|なら}ぶ{美|うつく}しい{街並|まちな}み（　　　）{有名|ゆうめい}です。', 'で', ['を', 'に', 'から'], 'This hot spring town is famous for its beautiful streetscape lined with historic wooden inns.', '「美しい街並みで有名」で、何によって知られているかを示します。'),
            ('{彼|かれ}の{出身地|しゅっしんち}は、{冬|ふゆ}に{開|ひら}かれる{幻想的|げんそうてき}な{雪祭|ゆきまつ}り（　　　）{有名|ゆうめい}な{都市|とし}だ。', 'で', ['を', 'と', 'へ'], 'His hometown is a city famous for the fantastic snow festival held in winter.', '名物や行事を理由として示す「〜で有名」の用法です。'),
        ],
    },
    165: {
        'reading': 'わけだ',
        'wrong': (
            '{明日|あした}はきっといい{天気|てんき}になるわけだから、ピクニックに{行|い}こう。',
            '「〜わけだ」は既に起きた事実や理由から論理的に導かれる当然の帰結・納得を表すため、不確実な未来の天候予測には使えません。',
            '〜わけだ expresses a logical conclusion or realization about an existing fact, so it cannot be used for an uncertain weather guess.',
        ),
        'comp_ex': [
            'エアコンが{消|き}えていたのか。道理で{部屋|へや}の{中|なか}がこんなに{暑|あつ}いわけだ。',
            '{毎日|まいにち}{欠|か}かさず{練習|れんしゅう}したのだから、{彼|かれ}が{試合|しあい}で{勝|か}ったのは{当然|とうぜん}だ。',
        ],
        'quiz': [
            ('彼は10年間も日本で暮らしているそうだ。道理で日本語がペラペラな（　　　）。', 'わけだ', ['はずだ', 'ことだ', 'ものだ'], 'I heard that he has lived in Japan for 10 years. No wonder he is so fluent in Japanese!', '理由を聞いて納得し、『なるほど、だからそういう結果になるのも当然だ』と合点がいった心境を表します。'),
            ('{五千円|ごせんえん}の{商品|しょうひん}を{二割|にわり}{引|び}きで{買|か}ったから、{四千円|よんせんえん}払った（　　　）。', 'わけだ', ['ものだ', 'ことだ', 'つもりだ'], 'Since I bought a 5,000-yen item at a 20% discount, that means I paid 4,000 yen.', '計算や事実関係から必然的に導かれる結論を「〜わけだ」で表します。'),
            ('{今日|きょう}は{祝日|しゅくじつ}だったのか。どうりで{電車|でんしゃ}の{中|なか}が{空|す}いている（　　　）。', 'わけだ', ['はずだ', 'ことだ', 'どころだ'], 'Oh, today is a national holiday! No wonder the inside of the train is so uncrowded.', '「どうりで〜わけだ」で原因を知って現状に納得したことを表します。'),
            ('{冷房|れいぼう}をつけたまま{寝|ね}てしまったのだから、のどが{痛|いた}くなる（　　　）。', 'わけだ', ['ことだ', 'つもりだ', 'ばかりだ'], 'Since you fell asleep with the air conditioner left on, it is only natural that your throat hurts.', '原因と結果の論理的なつながりを「当然そうなる」と述べる表現です。'),
        ],
    },
    166: {
        'reading': 'わけではない',
        'wrong': (
            '{私|わたし}は{今日|きょう}お{金|かね}が{一円|いちえん}もないわけではないから、{何|なに}も{買|か}えません。',
            '「〜わけではない」は「全面的に〜だというわけではない（少しは例外がある）」という部分否定なので、後ろに完全否定の結論を続けると意味が矛盾します。',
            '〜わけではない softens a blanket statement ("it does not mean that... completely"), so following it with an absolute negative conclusion contradicts the meaning.',
        ),
        'comp_ex': [
            '{高|たか}い{服|ふく}が、いつも{自分|じぶん}に{似合|にあ}うとは{限|かぎ}らない。',
            '{彼|かれ}の{意見|いけん}に{反対|はんたい}したからといって、{彼|かれ}の{努力|どりょく}を{認|みと}めていないというわけではない。',
        ],
        'quiz': [
            ('お酒が嫌いな（　　　）ではないが、健康のために平日は控えるようにしている。', 'わけ', ['もの', 'はず', 'こと'], "It doesn't mean that I dislike alcohol, but for my health I try to refrain on weekdays.", '全体を完全否定するのではなく、『そう単純に解釈してほしくない』と部分的に婉曲否定します。'),
            ('{暇|ひま}な（　　　）ではないけれど、{君|きみ}の{頼|たの}みなら{時間|じかん}を{作|つく}って{手伝|てつだ}うよ。', 'わけ', ['はず', 'こと', 'まま'], 'It is not that I am free, but since it is your request, I will make time to help you.', 'な形容詞＋なわけではないで、誤解を防ぎつつ事情を説明します。'),
            ('{都会|とかい}の{暮|く}らしに{不満|ふまん}がある（　　　）ではないが、{将来|しょうらい}は{自然|しぜん}の{豊|ゆた}かな{場所|ばしょ}に{住|す}みたい。', 'わけ', ['もの', 'とこ', 'きり'], 'It does not mean I am dissatisfied with city life, but in the future I want to live in a place rich in nature.', '一方を全否定するわけではないと前置きして本音を述べる表現です。'),
            ('{練習|れんしゅう}すれば{誰|だれ}でもすぐにプロになれるという（　　　）ではない。', 'わけ', ['はず', 'こと', 'たび'], 'It is not the case that just anyone can immediately become a professional simply by practicing.', '単純な一般化を部分否定する「〜というわけではない」です。'),
        ],
    },
    167: {
        'reading': 'わけがない',
        'wrong': (
            '{宝|たから}くじを{一枚|いちまい}だけ{買|か}ってみたが、もしかすると{当|あ}たるわけがないかな。',
            '「〜わけがない」は100%確信を持って「絶対にあり得ない」と断言する表現なので、「もしかすると〜かな」という不確かな推測とは一緒に使えません。',
            '〜わけがない asserts with 100% conviction that something is impossible, so it cannot be combined with uncertain expressions like もしかすると〜かな.',
        ),
        'comp_ex': [
            '{彼|かれ}は{今日|きょう}から{海外|かいがい}{出張|しゅっちょう}に{行|い}っているから、{今|いま}オフィスにいるはずがない。',
            'こんなに{複雑|ふくざつ}なパズル、{幼稚園|ようちえん}の{子|こ}どもに{解|と}けるっこないよ。',
        ],
        'quiz': [
            ('こんなに簡単で基本的な問題で、トップの彼が間違える（　　　）がない。', 'わけ', ['こと', 'もの', 'はず'], 'With such a simple and basic question, there is no way that he, being at the top, would get it wrong.', '論理的・常識的に考えて『絶対にそんなことはあり得ない』と強く確信を持って否定します。'),
            ('{真面目|まじめ}な{彼女|かのじょ}が、{大切|たいせつ}な{約束|やくそく}を{連絡|れんらく}もなしに{破|やぶ}る（　　　）がない。', 'わけ', ['こと', 'もの', 'とこ'], 'There is no way that someone as serious as her would break an important promise without contacting us.', '相手の性格をよく知っているからこそ絶対にあり得ないと断言しています。'),
            ('{一週間|いっしゅうかん}で{千個|せんこ}もの{単語|たんご}を{完璧|かんぺき}に{覚|おぼ}えられる（　　　）がない。', 'わけ', ['こと', 'まま', 'きり'], 'There is no way anyone could perfectly memorize as many as a thousand words in a single week.', '常識的に考えて不可能であることを強く主張します。'),
            ('こんなに{高価|こうか}な{時計|とけい}が、{千円|せんえん}で{本物|ほんもの}な（　　　）がないだろう。', 'わけ', ['はず', 'こと', 'もの'], 'There is no way such an expensive watch could be genuine for a thousand yen.', '名詞＋なわけがないで、あり得ないことを強く否定します。'),
        ],
    },
    168: {
        'reading': 'わけにはいかない',
        'wrong': (
            '{私|わたし}はピアノを{習|なら}ったことがないので、この{曲|きょく}を{弾|ひ}くわけにはいかない。',
            '「〜わけにはいかない」は「能力的には可能だが、責任・義理・状況のせいでそうするわけにはいかない」と自制する表現であり、単なる能力不足には「〜ことができない」を使います。',
            '〜わけにはいかない means refraining from an action due to moral, social, or situational constraints despite being physically able; for lack of ability, use 〜ことができない.',
        ),
        'comp_ex': [
            '{館内|かんない}ではフラッシュを{使|つか}って{写真|しゃしん}を{撮|と}ってはいけません。',
            '{親|した}しい{友人|ゆうじん}からの{頼|たの}みとあっては、{断|ことわ}らないわけにはいかない。',
        ],
        'quiz': [
            ('大事なプレゼンを明日に控えているので、今日風邪で休む（　　　）にはいかない。', 'わけ', ['はず', 'こと', 'もの'], 'With an important presentation ahead tomorrow, I simply cannot afford to take a day off with a cold today.', '社会的な義理や常識・心理的理由から『そうすることは許されない・できない』と自制します。'),
            ('{大切|たいせつ}な{秘密|ひみつ}だと{約束|やくそく}したから、{誰|だれ}にも{話|はな}す（　　　）にはいかない。', 'わけ', ['はず', 'こと', 'もの'], 'Because I promised it would be an important secret, I cannot possibly tell anyone.', '約束を守るという道義的な理由から行動を自制する表現です。'),
            ('{後輩|こうはい}たちが{頑張|がんば}っているのに、リーダーの{私|わたし}が{先|さき}に{諦|あきら}める（　　　）にはいかない。', 'わけ', ['はず', 'とこ', 'まま'], 'When my juniors are working so hard, as the leader I cannot afford to give up first.', '立場や責任感から「諦めることはできない」と述べています。'),
            ('せっかく{母|はは}が{手作り|てづくり}してくれたお{弁当|べんとう}を、{残|のこ}す（　　　）にはいかない。', 'わけ', ['こと', 'もの', 'はず'], 'I cannot bring myself to leave behind the boxed lunch my mother went to the trouble of making by hand.', '相手の好意に対する心情的な配慮から「残せない」と述べる用法です。'),
        ],
    },
    169: {
        'reading': 'はもちろん',
        'wrong': (
            '{彼|かれ}はひらがなはもちろん{書|か}けないし、{難|むずか}しい{漢字|かんじ}も{書|か}けない。',
            '否定文で「易しいAでさえできない、まして難しいBはできない」と言う場合は「AはおろかBも〜ない」「AどころかBも〜ない」を使い、「はもちろん」は主に肯定的な累加に使います。',
            'はもちろん adds further examples to an obvious positive/affirmative baseline; for "cannot even do A, let alone B," use はおろか or どころか.',
        ),
        'comp_ex': [
            'この{図書館|としょかん}は{市民|しみん}はもとより、{近隣|きんりん}の{町|まち}に{住|す}む{人|ひと}も{自由|じゆう}に{利用|りよう}できる。',
            '{彼|かれ}は{勉強|べんきょう}ができるばかりでなく、スポーツでも{全国大会|ぜんこくたいかい}に{出場|しゅつじょう}している。',
        ],
        'quiz': [
            ('この観光地は国内の旅行客（　　　）、近年は世界中からの訪日客にも大人気だ。', 'はもちろん', ['はともあれ', 'はさておき', 'はおろか'], 'This sightseeing spot is of course popular among domestic tourists, and recently also immensely popular with overseas visitors.', '前件が当然であることは言うまでもなく、さらにそれ以外の後件にも広く及ぶことを表します。'),
            ('{彼女|かのじょ}は{英語|えいご}（　　　）、{中国語|ちゅうごくご}や{韓国語|かんこくご}も{流暢|りゅうちょう}に{話|はな}すことができる。', 'はもちろん', ['はさておき', 'はともかく', 'はおろか'], 'She can fluently speak not only English, of course, but also Chinese and Korean.', '英語ができることは言うまでもなく、さらに他の言語もできると付け加えます。'),
            ('このカフェのケーキは{味|あじ}（　　　）、{見|み}た{目|め}の{美|うつく}しさにもこだわりが{詰|つ}まっている。', 'はもちろん', ['はべつとして', 'はさておき', 'どころか'], 'The cakes at this cafe are packed with attention not only to taste, of course, but also to visual beauty.', '基本となる味が良い上に、見た目も優れていることを強調します。'),
            ('{週末|しゅうまつ}（　　　）、{平日|へいじつ}の{昼間|ひるま}もこのパン{屋|や}には{多|おお}くのお{客|きゃく}さんが{並|なら}んでいる。', 'はもちろん', ['はともかく', 'はおろか', 'に反して'], 'Not to mention on weekends, even on weekday afternoons many customers line up at this bakery.', '週末に混むのは当然として、平日も賑わっていることを表します。'),
        ],
    },
    170: {
        'reading': 'わりに',
        'wrong': (
            '{彼|かれ}は{毎日|まいにち}{十時間|じゅうじかん}も{勉強|べんきょう}した割に、{見事|みごと}に{一|いち}{位|い}で{合格|ごうかく}した。',
            '「〜割に」は「基準から予想される程度とは違って意外にも〜だ」というギャップを表すため、努力通りの順当な結果には使えません。',
            '〜割に expresses an unexpected contrast relative to a standard ("considering X, surprisingly Y"), so it cannot be used when the outcome matches expectations.',
        ),
        'comp_ex': [
            '{初めて|はじめて}{作|つく}ったにしては、このロールケーキは{形|かたち}も{味|あじ}もとてもよくできている。',
            'あの{選手|せんしゅ}は{小柄|こがら}な{体格|たいかく}の{割|わり}に、パワーがあって{飛距離|ひきょり}が{出|で}る。',
        ],
        'quiz': [
            ('このレストランは値段がとてもリーズナブルな（　　　）に、ボリュームも味も大満足だ。', '割', ['最中', '途端', '通り'], 'Considering that the prices at this restaurant are very reasonable, both volume and taste are deeply satisfying.', '基準となる事柄（値段、年齢、練習量など）から予想される水準と実際の差を対比します。'),
            ('{父|ちち}は{年齢|ねんれい}の（　　　）に{体力|たいりょく}があり、{毎週末|まいしゅうまつ}テニスを{楽|たの}しんでいる。', '割', ['上', '中', '内'], 'My father has stamina for his age and enjoys playing tennis every weekend.', '年齢という基準から想像される以上に元気であることを表します。'),
            ('たくさんお{菓子|かし}を{食|た}べている（　　　）に、{彼女|かのじょ}はちっとも{太|ふと}らない。', '割', ['たび', 'きり', 'まま'], 'Considering how many sweets she eats, she does not gain weight at all.', '食べている量と実際の体型のギャップを表します。'),
            ('この{部屋|へや}は{南向|みなみむ}きの（　　　）に、{前|まえ}のビルが{高|たか}くて{昼間|ひるま}でも{少|すこ}し{暗|くら}い。', '割', ['上', '内', '先'], 'Considering that this room faces south, the building in front is tall so it is slightly dark even during the day.', '南向きなら明るいはずだという予想に反する状態を示します。'),
        ],
    },
    171: {
        'reading': 'わざと',
        'wrong': (
            '{遠|とお}いところから{私|わたし}のお{見舞|みま}いのために、わざと{来|き}てくださってありがとうございます。',
            '「わざと」は「意図的に（しばしば悪戯や不自然なことを）計算してやる」という意味なので、相手が手間をかけて来てくれたことへの感謝には「わざわざ」を使います。',
            'わざと means "on purpose / deliberately" (often for mischief or unnatural acts); to thank someone for going out of their way, use わざわざ.',
        ),
        'comp_ex': [
            '{読者|どくしゃ}の{関心|かんしん}を{引|ひ}くために、あえて{意図的|いとてき}に{結論|けつろん}を{最後|さいご}に{置|お}いた。',
            '{規則|きそく}を{知|し}りながら{故意|こい}に{違反|いはん}した{場合|ばあい}は、{厳|きび}しく{注意|ちゅうい}されます。',
        ],
        'quiz': [
            ('弟はいつも母の気を引くために、（　　　）大きな声で歌を歌ったりする。', 'わざと', ['つい', 'めったに', 'ふと'], "My younger brother always intentionally sings in a loud voice to draw mother's attention.", '偶然ではなく明確な意図や目的を持って意識的にその行動を行う様子を表します。'),
            ('{彼|かれ}は{本当|ほんとう}の{答|こた}えを{知|し}っているのに、（　　　）とぼけて{知|し}らないふりをした。', 'わざと', ['つい', 'うっかり', 'ふと'], 'Even though he knew the real answer, he purposely played dumb and pretended not to know.', '意図的に知らないふりをしたことを表します。'),
            ('{小|ちい}さな{子|こ}どもに{自信|じしん}をつけさせるため、ゲームで（　　　）{負|ま}けてあげた。', 'わざと', ['けっして', 'ちっとも', 'めったに'], 'To give the small child confidence, I lost the game on purpose.', 'あえて意図的に負けるという行動をとった場面です。'),
            ('ごめんなさい、{今|いま}のは{足|あし}が{滑|すべ}っただけで、（　　　）ぶつかったわけではありません。', 'わざと', ['まるで', 'ついに', 'まさか'], 'I am sorry, my foot just slipped right now; I did not bump into you on purpose.', '故意ではないと弁明する際にもよく使われます。'),
        ],
    },
    172: {
        'reading': 'わざわざ',
        'wrong': (
            '{道|みち}を{歩|ある}いていたら、{高校時代|こうこうじだい}の{友人|ゆうじん}にわざわざばったり{出|で}{会|あ}った。',
            '「わざわざ」は「特別に手間や時間をかけて意図的に行う」ことを表すため、「ばったり出会う」のような偶然の出来事には使えません。',
            'わざわざ means going to special trouble or effort intentionally, so it cannot modify an accidental encounter like ばったり出会う.',
        ),
        'comp_ex': [
            'せっかく{京都|きょうと}まで{来|き}たのだから、{美味しい|おいしい}{抹茶|まっちゃ}スイーツを{食|た}べて{帰|かえ}ろう。',
            '{休日|きゅうじつ}に{苦労|くろう}して{並|なら}んだかいがあって、{限定|げんてい}のパンを{買|か}うことができた。',
        ],
        'quiz': [
            ('雨の中、遠い所から私のために（　　　）お越しいただき、本当に恐縮です。', 'わざわざ', ['まるで', 'わざと', '決して'], 'I am truly grateful that you went to the trouble of coming specially for me from afar in the rain.', '普通ならしなくてもよい労力や手間をあえてかけて特別に行ってくれた相手への感謝・敬意を表します。'),
            ('{電話|でんわ}でも{済|す}む{用件|ようけん}なのに、{彼|かれ}は（　　　）{直接|ちょくせつ}オフィスまで{説明|せつめい}に{来|き}てくれた。', 'わざわざ', ['うっかり', 'つい', 'ふと'], 'Even though the matter could have been settled by phone, he went to the trouble of coming directly to the office to explain.', '手間を惜しまず足を運んでくれた丁寧さを表します。'),
            ('ネットで{買|か}えるものを、（　　　）{混雑|こんざつ}した{店|みせ}まで{買|か}いに{行|い}く{必要|ひつよう}はないよ。', 'わざわざ', ['ちっとも', 'めったに', 'かならずしも'], 'There is no need to go all the way to a crowded store to buy something you can get online.', '「わざわざ〜する必要はない」で、余計な手間をかけなくてよいと助言します。'),
            ('{誕生|たんじょう}{日|び}のお{祝|いわ}いに、{祖母|そぼ}が（　　　）{手編|てあ}みのセーターを{送|おく}ってくれた。', 'わざわざ', ['わざと', 'まるで', 'まさか'], 'To celebrate my birthday, my grandmother specially sent me a hand-knitted sweater.', '時間と労力をかけてしてくれた行為への感謝を表します。'),
        ],
    },
    173: {
        'reading': 'よりも',
        'wrong': (
            'この{映画|えいが}はあの{映画|えいが}よりも、どちらも{同|おな}じくらいおもしろかったです。',
            '「AよりもB」はAとBに差があることを比較して述べる表現なので、「どちらも同じくらい」という同等の結論とは一緒に使えません。',
            'AよりもB compares two things to show a difference between them, so it cannot end with "both are equally interesting."',
        ),
        'comp_ex': [
            '{今年|ことし}の{夏|なつ}は{去年|きょねん}より{猛暑日|もうしょび}が{多|おお}く、エアコンが{手放|てばな}せない。',
            'バスに{比|くら}べて、{地下鉄|ちかてつ}の{方|ほう}が{渋滞|じゅうたい}の{影響|えいきょう}を{受|う}けず{時間|じかん}が{正確|せいかく}だ。',
        ],
        'quiz': [
            ('言葉で立派な理想を語る（　　　）、まず小さな行動を実践することのほうが大切だ。', 'よりも', ['きりも', 'ほども', 'ばかりも'], 'Rather than talking of splendid ideals in words, putting small actions into practice first is more important.', '二つの物事を比較して、基準となる前者を退けて後者を選択・重視します。'),
            ('{思|おも}っていた（　　　）テストの{問題|もんだい}が{簡単|かんたん}だったので、{時間|じかん}が{余|あま}った。', 'よりも', ['ばかりも', 'だけも', 'きりも'], 'Because the test questions were easier than I had thought, I had time left over.', '事前の予想を基準として実際と比較する表現です。'),
            ('{一人で|ひとりで}{悩|なや}んでいる（　　　）、{信頼|しんらい}できる{友人|ゆうじん}に{相談|そうだん}した{方|ほう}が{気持|きも}ちが{楽|らく}になるよ。', 'よりも', ['ほども', 'ままも', 'たびも'], 'Rather than worrying all by yourself, consulting a trustworthy friend will make you feel lighter.', '二つの行動を比較して後者を勧める用法です。'),
            ('お{金|かね}や{物|もの}（　　　）、{家族|かぞく}と{過|す}ごす{穏|おだ}やかな{時間|じかん}こそが{何|なに}よりの{宝物|たからもの}だ。', 'よりも', ['だけも', 'すらも', 'きりも'], 'More than money or possessions, peaceful time spent with family is the greatest treasure of all.', '比較の基準を強調する「名詞＋よりも」です。'),
        ],
    },
    174: {
        'reading': 'ようがない',
        'wrong': (
            '{今日|きょう}はお{腹|なか}がいっぱいだから、これ以上ケーキを{食|た}べようがない。',
            '「〜ようがない」は「手段・方法そのものが全く存在しないためやりようがない」という意味であり、満腹などの体調・能力の限界には「〜ことができない」「〜られない」を使います。',
            '〜ようがない means "there is no method or means available to do something," not physical fullness or personal inability.',
        ),
        'comp_ex': [
            '{鍵|かぎ}を{内側|うちがわ}に{忘|わす}れてロックされてしまい、{外|そと}からは{開|あ}けるすべがない。',
            'データが{完全|かんぜん}に{消|き}えてしまったため、{元|もと}に{戻|もど}す{方法|ほうほう}がない。',
        ],
        'quiz': [
            ('電話番号もメールアドレスも分からないので、連絡の取り（　　　）がない。', 'よう', ['はず', 'そう', '気'], "Since I don't know either their phone number or email address, there is simply no way to get in touch.", '動詞ます形＋ようがないで、いくらそうしたくても手段や方法が皆無で不可能であることを表します。'),
            ('{相手|あいて}が{何|なに}も{話|はな}してくれないのでは、こちらとしても{助|たす}け（　　　）がない。', 'よう', ['はず', 'わけ', 'もの'], 'If the other person will not tell us anything, there is simply no way for us to help either.', '事情が分からないため助ける手段がないことを表します。'),
            ('{証拠|しょうこ}となる{記録|きろく}が{残|のこ}っていないため、{事実|じじつ}を{確|たし}かめ（　　　）がない。', 'よう', ['そう', 'まま', 'きり'], 'Because no records serving as evidence remain, there is no way to verify the facts.', '確認するための手段が欠けている場面です。'),
            ('これほど{見事|みごと}な{作品|さくひん}を{前|まえ}にすると、ただ{素晴|すば}らしいとしか{言|い}い（　　　）がない。', 'よう', ['はず', 'わけ', 'こと'], 'Faced with such a splendid work, there is no other way to put it than simply wonderful.', '「〜としか言いようがない」で他に表現する方法がないほど素晴らしいことを表します。'),
        ],
    },
    175: {
        'reading': 'ようなきがする',
        'wrong': (
            '{私|わたし}は{毎日|まいにち}{八時|はちじ}に{会社|かいしゃ}へ{行|い}くような気がする。',
            '「〜ような気がする」は確証のない漠然とした直感や記憶を表すため、自分自身の明確な毎日の事実には使えません。',
            '〜ような気がする expresses a vague hunch or uncertain impression, so it cannot be used for one\'s own definite daily routine.',
        ),
        'comp_ex': [
            '{部屋の模様替|へやのもようが}えをしたら、{以前|いぜん}よりスペースが{広|ひろ}くなった{感|かん}じがする。',
            '{今回|こんかい}のトラブルは、{事前の|じぜんの}{連絡不足|れんらくぶそく}が{原因|げんいん}だったと{思|おも}われる。',
        ],
        'quiz': [
            ('どこかで一度お会いしたことがあるような（　　　）がするのですが、違いますでしょうか。', '気', ['声', '心', '目'], 'I have a feeling that I have met you somewhere once before; might I be mistaken?', '明確な確証はないものの、直感や漠然とした感覚としてそう感じられる心理を表します。'),
            ('{今日|きょう}は{朝|あさ}から{空|そら}が{暗|くら}いので、{夕方|ゆうがた}までに{雨|あめ}が{降|ふ}るような（　　　）がする。', '気', ['目', '手', '口'], 'Because the sky has been dark since morning today, I have a feeling it will rain by evening.', 'はっきりした根拠はないが直感的にそう思えることを表します。'),
            ('{鍵|かぎ}を閉め{忘|わす}れたような（　　　）がして、{心配|しんぱい}になって{家|いえ}へ{引|ひ}き{返|かえ}した。', '気', ['心', '頭', '耳'], 'I had a feeling that I had forgotten to lock the door, so I got worried and turned back home.', '記憶が曖昧でなんとなく不安に感じる心理を描写します。'),
            ('{彼|かれ}の{話|はなし}を{聞|き}いていると、どんな{困難|こんなん}も{乗|の}り{越|こ}えられるような（　　　）がしてくる。', '気', ['目', '声', '手'], 'When I listen to him speak, I start to feel as though I can overcome any difficulty.', '主観的な感覚が湧いてくることを表します。'),
        ],
    },
    176: {
        'reading': 'ようにみえる',
        'wrong': (
            '{暗闇|くらやみ}の{中|なか}で{目|め}を{閉|と}じると、{遠|とお}くから{波|なみ}の{音|おと}がするように見える。',
            '「〜ように見える」は視覚的な外見や様子から受ける印象を表すため、聴覚による音の知覚には「〜ように聞こえる」や「〜ようだ」を使います。',
            '〜ように見える describes an impression based on visual appearance, so it cannot be used for auditory perception with one\'s eyes closed.',
        ),
        'comp_ex': [
            '{彼|かれ}はとても{忙|いそが}しそうに見えるが、{頼|たの}まれごとをすると{笑顔|えがお}で{引|ひ}き{受|う}けてくれる。',
            'このガラス{細工|ざいく}は、まるで{本物|ほんもの}の{氷|こおり}でできているようだ。',
        ],
        'quiz': [
            ('彼女はいつも明るく笑っているが、時折どこか寂しそうにしているようにも（　　　）。', '見える', ['思える', '聞える', '言える'], 'She always smiles brightly, but at times she also appears to look somewhat lonely.', '外見や様子から受ける視覚的・印象的な推測を表します。'),
            ('この{写真|しゃしん}の{建物|たてもの}は{遠近法|えんきんほう}の{効果|こうか}で、{実際|じっさい}よりもはるかに{高|たか}いように（　　　）。', '見える', ['聞こえる', '言える', 'できる'], 'Due to the effect of perspective, the building in this photo looks far taller than it actually is.', '視覚的な{見|み}え{方|かた}を表す「〜ように見える」です。'),
            ('{彼|かれ}は{普段|ふだん}はのんびりしているように（　　　）が、{仕事|しごと}はとても{素早|すばや}く{正確|せいかく}だ。', '見える', ['聞こえる', '言える', '当てる'], 'He usually appears laid-back, but his work is very quick and accurate.', '外見の印象と実際の姿の対比によく使われます。'),
            ('{若々|わかわか}しい{服装|ふくそう}をしているので、{彼女|かのじょ}は{実年齢|じつねんれい}より{十歳|じゅっさい}も{若|わか}いように（　　　）。', '見える', ['聞こえる', '言える', '向ける'], 'Because she dresses youthfully, she looks ten years younger than her actual age.', '見た目から受ける印象を表す典型的な用法です。'),
        ],
    },
    177: {
        'reading': 'ように',
        'wrong': (
            '{将来|しょうらい}{自分|じぶん}の{店|みせ}を{持|も}つように、{毎月|まいつき}{十万円|じゅうまんえん}ずつ{貯金|ちょきん}している。',
            '目的の「〜ように」の前には可能動詞・無意志動詞・否定形などの「状態」が来るため、「店を持つ」のような意志動詞の辞書形には「〜ために」を使います（「持てるように」なら可）。',
            'Purpose ように follows potential, non-volitional, or negative forms; for a volitional verb in dictionary form like 店を持つ, use ために (or change to 持てるように).',
        ),
        'comp_ex': [
            '{留学|りゅうがく}の{費用|ひよう}を{貯|た}めるために、{週|しゅう}に{四日|よっか}アルバイトをしている。',
            '{家族|かぞく}みんなが{一年間|いちねんかん}{健康|けんこう}に{過|す}ごせるようにと、{神社|じんじゃ}でお{参|まい}りをした。',
        ],
        'quiz': [
            ('後ろの席の人にもよく聞こえる（　　　）、マイクを使って大きな声で話した。', 'ように', ['とおりに', 'くせに', 'ために'], 'So that people in the back seats could hear well, I spoke in a loud voice using a microphone.', '無意志動詞や可能形＋ようにで、その状態が実現することを目標として対策を講じます。'),
            ('{朝|あさ}{寝坊|ねぼう}しない（　　　）、{目覚|めざ}まし{時計|どけい}を{二|ふた}つセットしてから{寝|ね}た。', 'ように', ['ために', 'とおりに', 'ばかりに'], 'So that I would not oversleep in the morning, I set two alarm clocks before going to bed.', '動詞ない形＋ようにで、望ましくない状態を防ぐ目的を表します。'),
            ('{小|ちい}さな{子|こ}どもにも{意味|いみ}が{分|わ}かる（　　　）、やさしい{言葉|ことば}を{選|えら}んで{説明|せつめい}した。', 'ように', ['ために', 'とたんに', 'ついでに'], 'So that even small children could understand the meaning, I chose easy words to explain.', '「分かる」という無意志動詞に付いて目標とする状態を示します。'),
            ('いつ{来客|らいきゃく}があっても{対応|たいおう}できる（　　　）、{部屋|へや}はいつも{清潔|せいけつ}に{片付|かたづ}けてある。', 'ように', ['ために', 'くせに', 'わりに'], 'So that I can handle guests whenever they come, I always keep the room clean and tidy.', '可能形「対応できる」＋ようにで、望ましい状態の達成を目的として表します。'),
        ],
    },
    178: {
        'reading': 'ようとしない',
        'wrong': (
            '{私|わたし}は{健康|けんこう}のために、{夜遅|よるおそ}くにラーメンを{食|た}べようとしない。',
            '「〜ようとしない」は三人称の人物が当然すべきことや期待される行動を頑なに拒む態度を批判的に描く表現であり、自分の生活習慣の叙述には「〜ないようにしている」を使います。',
            '〜ようとしない critically describes a third party stubbornly refusing to make an effort; for one\'s own healthy habit, use 〜ないようにしている.',
        ),
        'comp_ex': [
            '{何度|なんど}{注意|ちゅうい}されても、{彼|かれ}は{遅刻|ちこく}の{癖|くせ}を{直|なお}そうとしない。',
            '{彼|かれ}は{自分|じぶん}の{意見|いけん}にこだわり、{周囲|しゅうい}のアドバイスに{頑|かたくな}なに{耳|みみ}を{貸|か}さない。',
        ],
        'quiz': [
            ('彼は自分の非を頑なに認め（　　　）とせず、他人のせいばかりにしている。', 'よう', ['気', 'そう', 'まい'], 'He stubbornly makes no attempt to admit his fault and does nothing but blame others.', '意向形＋としない（とせず）で本人がその行動をする意志・意欲を全く示さない様子を非難します。'),
            ('せっかく{家族|かぞく}が{心配|しんぱい}して{声|こえ}をかけているのに、{彼|かれ}は{部屋|へや}から{出|で}てこ（　　　）としない。', 'よう', ['そう', 'まい', 'はず'], 'Even though his family is worriedly calling out to him, he makes no attempt to come out of his room.', '「出てこようとしない」で、出てくる意志を全く見せない様子を表します。'),
            ('{彼|かれ}は{自分|じぶん}の{考|かんが}えが{絶対|ぜったい}に{正|ただ}しいと{信|しん}じ、{他|ほか}の{人|ひと}の{意見|いけん}を{聞|き}こ（　　　）としない。', 'う', ['よう', 'そう', 'まい'], 'Believing that his own idea is absolutely right, he refuses to listen to other people\'s opinions.', '五段動詞「聞く」の意向形「聞こう」＋としないで、聞く姿勢がないことを表します。'),
            ('あの{店|みせ}は{昔|むかし}からのやり{方|かた}ばかり{守|まも}り、{新|あたら}しいサービスを{取|と}り{入|い}れ（　　　）としない。', 'よう', ['そう', 'まい', 'わけ'], 'That shop only sticks to old-fashioned ways and makes no effort to adopt new services.', '変化に対して消極的で意欲がない様子を指摘しています。'),
        ],
    },
    179: {
        'reading': 'ようとする',
        'wrong': (
            '{明日|あした}は{友達|ともだち}と{映画|えいが}を{見|み}に{行|い}こうとするから、{今夜|こんや}のうちに{宿題|しゅくだい}をしよう。',
            '「〜ようとする」は動作の直前（「今まさに〜するところだ」）または試み・努力を表すため、単なる未来の予定の理由には「〜つもりだから」を使います。',
            '〜ようとする means "just about to do" or "try to do," so for stating a planned future intention as a reason, use 〜つもりだから.',
        ),
        'comp_ex': [
            '{舞台|ぶたい}の{幕|まく}がまさに{上|あ}がろうとしたそのとき、{会場|かいじょう}の{照明|しょうめい}が{静|しず}かに{消|き}えた。',
            '{何度|なんど}か{説得|せっとく}を{試|こころ}みたが、{彼|かれ}の{決心|けっしん}を{変|か}えることはできなかった。',
        ],
        'quiz': [
            ('電車がまさに発車し（　　　）としたその瞬間、駆け込み乗車のベルが鳴り響いた。', 'よう', ['まい', 'そう', '気'], 'At the very instant the train was about to depart, the rushed-boarding chime sounded loudly.', '意向形＋とするで動作が今まさに始まろうとしている直前の瞬間や試みを表します。'),
            ('お{風呂|ふろ}に{入|はい}ろ（　　　）としたとき、ちょうど{宅配便|たくはいびん}のチャイムが{鳴|な}った。', 'う', ['よう', 'そう', 'まい'], 'Just as I was about to get into the bath, the delivery doorbell rang.', '五段動詞「入る」の意向形「入ろう」＋としたときで、動作の直前のタイミングを表します。'),
            ('{泣|な}いている{子|こ}どもをなんとか{笑|わら}わせ（　　　）として、いろいろな{変|へん}な{顔|かお}をしてみた。', 'よう', ['そう', 'まい', 'はず'], 'Trying to somehow make the crying child laugh, I tried making various funny faces.', '「〜ようとして」で目的を実現するために試みる様子を表します。'),
            ('{太陽|たいよう}が{西|にし}の{海|うみ}へ{沈|しず}も（　　　）としている{美|うつく}しい{光景|こうけい}を{写真|しゃしん}に{収|おさ}めた。', 'う', ['よう', 'そう', 'まい'], 'I captured in a photo the beautiful sight of the sun just about to sink into the western sea.', '無意志動詞の意向形＋としているで、現象が起きる直前の場面を描写します。'),
        ],
    },
    180: {
        'reading': 'ずにはいられない',
        'wrong': (
            '{今日|きょう}は{書類|しょるい}の{締|し}め{切|き}り{日|び}なので、{残業|ざんぎょう}せずにはいられない。',
            '「〜ずにはいられない」は内面から湧き上がる感情や生理的衝動を抑えきれないときに使い、規則や仕事の義務による行動には「〜ないわけにはいかない」「〜ざるを得ない」を使います。',
            '〜ずにはいられない is for natural emotional or physical urges that cannot be suppressed; for external duty or work deadlines, use 〜ないわけにはいかない.',
        ),
        'comp_ex': [
            'あんなにおもしろいコントを{見|み}せられたら、{誰|だれ}だって{笑|わら}わないではいられないよ。',
            '{焼|や}きたてのパンの{香|かお}りがしてくると、お{店|みせ}に{入|はい}りたい{気持|きも}ちが{抑|おさ}えられない。',
        ],
        'quiz': [
            ('あの大感動の映画のラストシーンを見て、誰もが涙を流さ（　　　）にはいられなかった。', 'ずに', ['ざる', 'ないで', 'なく'], 'Watching the last scene of that deeply moving movie, nobody could help but shed tears.', '動詞ない形＋ずにはいられないで、感情や衝動が内面から自然と湧き上がり抑えきれないことを表します。'),
            ('{一生懸命|いっしょうけんめい}に{頑張|がんば}る{彼|かれ}の{姿|すがた}を{見|み}ていると、{心|こころ}から{応援|おうえん}せ（　　　）にはいられない。', 'ず', ['ない', 'ぬ', 'まい'], 'When I see him working so hard with all his might, I cannot help cheering for him from the bottom of my heart.', '「する」は「せずにはいられない」の形をとります。'),
            ('あまりにも{景色|けしき}がきれいだったので、カメラを{向|む}けて{写真|しゃしん}を{撮|と}ら（　　　）にはいられなかった。', 'ず', ['ない', 'ざる', 'まい'], 'Because the scenery was so breathtaking, I could not help pointing my camera and taking photos.', '感動して思わず行動してしまう衝動を表します。'),
            ('{久|ひさ}しぶりに{故郷|こきょう}の{料理|りょうり}を{食|た}べたら、{家族|かぞく}のことを{思|おも}い{出|だ}さ（　　　）にはいられなかった。', 'ず', ['ない', 'なく', 'まい'], 'When I ate my hometown\'s food for the first time in a long while, I could not help remembering my family.', '自然と湧き上がる懐かしさや記憶を抑えられない様子を表します。'),
        ],
    },
    181: {
        'reading': 'ずに',
        'wrong': (
            'この{図書館|としょかん}の{本|ほん}は、カウンターで{手続|てつづ}きをせずに{持|も}ち{帰|かえ}ってください。',
            '「〜ないでください」という禁止・依頼の文脈では「×〜ずにください」とは言えず、「〜ないでください」を使います（「〜ずに持ち帰る」のように動詞を修飾するときに使います）。',
            'ずに modifies a following verb phrase ("do B without doing A") and cannot directly precede ください; use 〜ないでください for negative requests.',
        ),
        'comp_ex': [
            '{辞書|じしょ}を{使|つか}わないで、まずは{文脈|ぶんみゃく}から{単語|たんご}の{意味|いみ}を{推測|すいそく}してみよう。',
            '{彼|かれ}は{休日|きゅうじつ}も{休|やす}みを{取|と}らず、ボランティア{活動|かつどう}に{参加|さんか}して{汗|あせ}を{流|なが}した。',
        ],
        'quiz': [
            ('昨夜は一度も目を覚まさ（　　　）、朝のアラームが鳴るまでぐっすり熟睡できた。', 'ずに', ['ないで', 'ずとも', 'なくて'], 'Last night I was able to sleep soundly until the morning alarm rang, without waking up even once.', '動詞ない形＋ずに（するは『せずに』）で〜ない状態を維持したまま主動作を行う硬い表現です。'),
            ('{今朝|けさ}は{寝坊|ねぼう}してしまったため、{朝ご飯|あさごはん}を{食|た}べ（　　　）{慌|あわ}てて{家|いえ}を{出|で}た。', 'ずに', ['なくて', 'なしに', 'ぬまま'], 'Because I overslept this morning, I hurriedly left home without eating breakfast.', '「食べないで」のやや硬い表現として「食べずに」が使われています。'),
            ('{予約|よやく}をせ（　　　）{人気|にんき}のレストランへ{行|い}ったら、{一時間|いちじかん}も{待|ま}つことになった。', 'ずに', ['ないで', 'なくて', 'ぬよう'], 'When I went to the popular restaurant without making a reservation, I ended up having to wait for a full hour.', '「する」は「せずに」という不規則な形になる点が重要です。'),
            ('{誰|だれ}にも{相談|そうだん}せ（　　　）、{一人|ひとり}でそんなに{大|おお}きな{決断|けつだん}をしないでほしい。', 'ずに', ['ないで', 'なくて', 'ぬうち'], 'I wish you would not make such a big decision all by yourself without consulting anyone.', '「相談せずに（＝相談しないで）」で付帯状況を表します。'),
        ],
    },
    182: {
        'reading': 'ずつ',
        'wrong': (
            '{参加費|さんかひ}は{全部|ぜんぶ}で{三千円|さんぜんえん}ずつですから、{代表者|だいひょうしゃ}がまとめて{払|はら}ってください。',
            '「〜ずつ」は「一人あたり／一回あたりに均等に割り当てる量」を表すため、「全部で（合計）」という全体の総額には使えません。',
            '〜ずつ indicates an equal amount distributed per person or per occasion ("each / at a time"), so it cannot be used with 全部で (total sum).',
        ),
        'comp_ex': [
            'オリンピックは{四年|よねん}ごとに{開催|かいさい}され、{世界中|せかいじゅう}の{選手|せんしゅ}が{技|わざ}を{競|きそ}う。',
            '{怪我|けが}の{後|あと}、リハビリの{運動量|うんどうりょう}を{少|すこ}しずつ{増|ふ}やしていった。',
        ],
        'quiz': [
            ('毎日少し（　　　）新しい単語を覚えていけば、1年間で大きな語彙力を身につけられる。', 'ずつ', ['きり', 'ばかり', 'とおり'], 'If you memorize new vocabulary little by little every day, you can acquire vast vocabulary in one year.', '数量詞＋ずつで均等な配分や、同じ分量ずつ段階的に事態が進んでいく様子を表します。'),
            ('この{お土産|おみやげ}のお{菓子|かし}は、{一人|ひとり}{二個|にこ}（　　　）{分|わ}けて{食|た}べましょう。', 'ずつ', ['ごと', 'おき', 'きり'], 'Let us divide and eat these souvenir sweets two pieces per person.', '「一人二個ずつ」で均等に配分することを表します。'),
            ('{混雑|こんざつ}を{防|ふせ}ぐため、エレベーターには{十人|じゅうにん}（　　　）{順番|じゅんばん}にお{乗|の}りください。', 'ずつ', ['ごと', 'おき', 'たび'], 'To prevent crowding, please board the elevator in turn, ten people at a time.', '一回あたりの数量を一定にして繰り返す用法です。'),
            ('{一行|いちぎょう}（　　　）{丁寧|ていねい}に{確認|かくにん}しながら、プログラムの{誤|あやま}りを{探|さが}していった。', 'ずつ', ['きり', 'ばかり', 'どころ'], 'Checking carefully one line at a time, I searched for errors in the program.', '「一行ずつ」で段階的に一つずつ進める様子を表します。'),
        ],
    },
}

