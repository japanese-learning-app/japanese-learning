# -*- coding: utf-8 -*-
"""
N3 grammar data part A (gids 1-60).
"""
import os, json

_HERE = os.path.dirname(os.path.abspath(__file__))
_BASE = json.load(open(os.path.join(_HERE, 'base_grammar_details.json'), encoding='utf-8'))

def _q0(gid):
    q = _BASE[str(gid)]['q0']
    return (q['stem'], q['correct'], q['distractors'], q['en'], q['notes_ja'])

GRAMMAR = {
    1: {
        'reading': 'あげる',
        'wrong': (
            '昨日買った本を半分だけ読み上げたところで眠くなった。',
            '「〜上げる」は最後まで完成・完了させる意味なので、「半分だけ」のような未完了の文脈には使えません。',
            'Since 〜上げる means to finish or complete something all the way to the end, it cannot be used with incomplete expressions like "only halfway."'
        ),
        'comp_ex': [
            '100ページの長い小説を{一日|いちにち}で最後まで読み切った。',
            '夕飯の皿洗いをし終わったら、一緒に映画を見よう。',
        ],
        'quiz': [
            _q0(1),
            ('パン生地を丁寧にこねて、オーブンで香ばしく焼き（　　　）。', '上げた', ['すぎた', 'かけた', '出した'], 'I kneaded the bread dough carefully and baked it up fragrantly in the oven.', '動詞ます形＋上げるで、手をかけて最後まで完成させることを表します。'),
            ('半年かけて調査したデータをまとめ（　　　）、今日やっと上司に提出した。', '上げて', ['かけて', 'すぎて', '出して'], 'I finished compiling the data researched over half a year and finally submitted it to my boss today.', '「まとめ上げる」で、ばらばらの資料や情報を最後までひとつの形に完成させる意味になります。'),
            ('大工さんたちが数か月かけて、立派な木造の家を建て（　　　）。', '上げた', ['かけた', '切れない', 'はじめた'], 'The carpenters spent several months and finished building a splendid wooden house.', '「建て上げる」で、建物を最後まで造り終えて完成させることを表します。'),
        ],
    },
    2: {
        'reading': 'あまりにも',
        'wrong': (
            'このスープはあまりにもちょうどいい温度で飲みやすい。',
            '「あまりにも」は程度が極端に度を越えているときに使うため、「ちょうどいい」のような適度な状態には使えません。',
            'あまりにも expresses an extreme or excessive degree, so it cannot modify moderate expressions like "just the right temperature."'
        ),
        'comp_ex': [
            '山頂からの眺めがあまりに美しくて、しばらく言葉を失った。',
            '今年の夏は非常に暑く、冷房なしではとても過ごせない。',
        ],
        'quiz': [
            _q0(2),
            ('昨日の映画は結末が（　　　）悲しくて、映画館を出ても涙が止まらなかった。', 'あまりにも', ['めったに', 'かならずしも', 'ちっとも'], "Yesterday's movie had such a sad ending that my tears wouldn't stop even after leaving the theater.", '「あまりにも＋形容詞」で、悲しさの程度が常識や予想をはるかに超えていることを強調します。'),
            ('駅からホテルまでの道のりが（　　　）遠かったので、途中でタクシーに乗った。', 'あまりにも', ['べつに', 'まさか', 'たいてい'], 'Because the walk from the station to the hotel was way too far, I took a taxi halfway through.', '距離や程度が極端であることを示し、その結果タクシーに乗ったという理由につながります。'),
            ('彼の言い訳は（　　　）不自然で、誰も本当だとは思わなかった。', 'あまりにも', ['けっして', 'すこしも', 'たまに'], 'His excuse was so unnatural that nobody thought it was true.', '「あまりにも＋な形容詞」で、程度が甚だしいことを表します。'),
        ],
    },
    3: {
        'reading': 'あまり',
        'wrong': (
            'お腹が{空|す}いたあまり、食堂で普通の定食を一人前食べた。',
            '「〜あまり」は感情や状態が極端すぎて通常ではない結果になる時に使います。普通の行動には不自然です。',
            '〜あまり is used when an extreme emotion or state leads to an unusual or unintended result, not an ordinary everyday action.'
        ),
        'comp_ex': [
            '財布を忘れたばかりに、せっかくの特売品を買うことができなかった。',
            'あまりの嬉しさに、彼女は合格通知を握りしめて飛び上がった。',
        ],
        'quiz': [
            _q0(3),
            ('息子が無事に帰ってきた嬉しさの（　　　）、母は玄関で泣き出してしまった。', 'あまり', ['ついでに', 'かわりに', 'わりに'], 'Overcome with joy that her son had returned safely, my mother burst into tears at the entrance.', '「名詞＋のあまり」で、感情が強すぎて思わず涙が出るような結果になったことを表します。'),
            ('締め切りに間に合わせようと急ぐ（　　　）、宛名の漢字を書き間違えてしまった。', 'あまり', ['とおりに', 'くせに', 'どころか'], 'In my excessive haste to meet the deadline, I accidentally wrote the wrong kanji for the addressee.', '「動詞辞書形＋あまり」で、ひとつのことに集中しすぎて良くない結果が起きることを表します。'),
            ('舞台の上で失敗しないかと心配する（　　　）、声が震えてうまく話せなかった。', 'あまり', ['たびに', 'いっぽうで', 'ついでに'], 'Worrying excessively about making a mistake on stage, my voice trembled and I could not speak well.', '極度の心配が原因で、声が震えるという意図しない結果につながったことを示します。'),
        ],
    },
    4: {
        'reading': 'あう',
        'wrong': (
            '私は毎朝鏡を見ながら一人で笑顔を作り合っている。',
            '「〜合う」は複数の人がお互いに同じ動作をする表現なので、一人だけの動作には使えません。',
            '〜合う expresses reciprocal action between two or more people, so it cannot be used for an action performed alone.'
        ),
        'comp_ex': [
            '困ったときはお互いに助け合って生活することが大切だ。',
            '地域の住民が協力して、公園の落ち葉をきれいに掃除した。',
        ],
        'quiz': [
            _q0(4),
            ('狭い道では、歩行者と自転車が道を譲り（　　　）安全に通行しましょう。', 'あって', ['きって', 'すぎて', 'かけて'], 'On narrow roads, pedestrians and cyclists should yield to each other and pass safely.', '「譲り合う」で、双方がお互いに譲るという相互の動作を表します。'),
            ('久しぶりに再会した友人たちは、お互いの近況を遅くまで語り（　　　）。', 'あった', ['きった', 'だした', 'すぎた'], 'The friends who reunited after a long time talked with each other about their recent lives until late.', '「語り合う」で、お互いに話を交わすことを表します。'),
            ('引っ越しの荷物が多かったが、家族みんなで助け（　　　）夕方には片付いた。', 'あったおかげで', ['かけたせいで', 'すぎたために', 'きったくせに'], 'There was a lot of moving luggage, but thanks to the whole family helping each other, it was tidied up by evening.', '「助け合う」で、家族がお互いに協力して支え合う様子を表します。'),
        ],
    },
    5: {
        'reading': 'ば〜ほど',
        'wrong': (
            'この本は読めば読むほど、昨日買ったばかりだ。',
            '「〜ば〜ほど」の後件には、前件の条件に応じて程度が変化する事柄が来なければなりません。',
            'The clause following 〜ば〜ほど must express a state or degree that changes proportionally with the first clause.'
        ),
        'comp_ex': [
            '秋が深まるにつれて、山の木々が赤や黄色に色づいてきた。',
            '技術が進歩するとともに、私たちの暮らしも大きく変化している。',
        ],
        'quiz': [
            _q0(5),
            ('この伝統工芸品は、近くで見れば見る（　　　）職人の細かい技術に感動する。', 'ほど', ['ばかり', 'くらい', 'だけ'], 'The closer you look at this traditional craft, the more moved you are by the artisan’s delicate skill.', '同じ動詞の条件形と辞書形を繰り返して「見れば見るほど」とし、比例して感動が増すことを示します。'),
            ('パソコンの操作は、慣れれば慣れる（　　　）作業のスピードが速くなる。', 'ほど', ['わりに', 'くせに', 'とおり'], 'With computer operations, the more used to them you get, the faster your work speed becomes.', '「慣れれば慣れるほど」で、慣れの度合いと作業速度が比例して上がることを表します。'),
            ('駅に近ければ近い（　　　）、アパートの家賃は高くなるのが一般的だ。', 'ほど', ['きり', 'まま', 'ため'], 'Generally, the closer an apartment is to the station, the higher the rent becomes.', 'い形容詞の条件形「近ければ」＋原形「近い」＋「ほど」で比例関係を表します。'),
        ],
    },
    6: {
        'reading': 'ばいい',
        'wrong': (
            '昨日あんなに食べすぎなければいいのに、今もお腹が痛い。',
            '過去の事実に対する後悔には「〜ばいい」ではなく「〜ばよかった」を使います。',
            'To express regret about a past action, use 〜ばよかった rather than the present/future advice form 〜ばいい.'
        ),
        'comp_ex': [
            'もし当日に都合が悪くなったら、電話で連絡してくれたらいいですよ。',
            '明日の遠足は天気が晴れて、みんなで楽しくお弁当が食べられるといいね。',
        ],
        'quiz': [
            _q0(6),
            ('申込書の書き方が分からなければ、受付の係員に聞けば（　　　）ですよ。', 'いい', ['よかった', 'べき', 'はず'], "If you don't know how to fill out the application form, you can just ask the staff at the reception desk.", '「聞けばいい」で、これからどうすればよいかという簡単な解決策や助言を伝えます。'),
            ('全部を一度に覚えられなくても、毎日少しずつ復習すれば（　　　）から安心してください。', 'いい', ['わけだ', 'ものだ', 'ことだ'], "Even if you can't memorize everything at once, you just need to review little by little every day, so don't worry.", '「復習すればいい」で、気楽なアドバイスや解決策を表します。'),
            ('そんなに緊張しなくても、いつもの練習通りに自分の力を出せば（　　　）よ。', 'いいんだ', ['べきなんだ', 'はずなんだ', 'わけなんだ'], "You don't have to be so nervous; you just need to show your ability as you usually practice.", '相手を励ましながら「そうすれば問題ない」と助言する表現です。'),
        ],
    },
    7: {
        'reading': 'ばかりでなく',
        'wrong': (
            'この部屋は駅から遠いばかりでなく、家賃も安くて便利だ。',
            '「AばかりでなくBも」は同方向の性質（良い点＋良い点、または悪い点＋悪い点）を並べるため、マイナス面とプラス面は並べられません。',
            'AばかりでなくBも pairs two qualities of the same orientation (both positive or both negative), not a drawback with a benefit.'
        ),
        'comp_ex': [
            'このカフェはコーヒーがおいしいだけでなく、手作りのケーキも人気がある。',
            '環境問題は一国のみならず、世界全体で取り組むべき課題である。',
        ],
        'quiz': [
            _q0(7),
            ('この野菜は栄養が豊富な（　　　）、甘みがあって子どもでも食べやすい。', 'ばかりでなく', ['かわりに', 'くせに', 'どころか'], 'This vegetable is not only rich in nutrition, but also sweet and easy for children to eat.', 'な形容詞＋な＋「ばかりでなく」で、栄養面に加えて味も良いことを付け加えます。'),
            ('田中さんは英語が話せる（　　　）、スペイン語の翻訳もこなすことができる。', 'ばかりでなく', ['わりには', 'とたんに', 'ついでに'], 'Tanaka-san cannot only speak English, but can also handle Spanish translation.', '「話せるばかりでなく」で、一つの能力にとどまらずさらに別の能力もあることを表します。'),
            ('昨日の台風で電車が止まった（　　　）、一部の地域では停電も発生した。', 'ばかりでなく', ['おかげで', '反面', 'わりに'], 'Due to yesterday’s typhoon, not only did the trains stop, but power outages also occurred in some areas.', '被害や困った事態が重なった場面でも「AばかりでなくBも」が使われます。'),
        ],
    },
    8: {
        'reading': 'ばかりで',
        'wrong': (
            '妹は毎日熱心に勉強するばかりで、先生からよく褒められている。',
            '「〜ばかりで」は好ましくない行動や偏った状態への不満を表すため、褒められるような良い習慣には使えません。',
            '〜ばかりで carries a negative nuance of doing nothing but an undesirable action, so it does not fit praiseworthy behavior.'
        ),
        'comp_ex': [
            '休みの日に家でゴロゴロしてばかりいては、体力が落ちてしまうよ。',
            '彼はピアノが上手なばかりでなく、自分で作曲もできるそうだ。',
        ],
        'quiz': [
            _q0(8),
            ('うちの弟は休みの日になるとゲームをする（　　　）、ちっとも外へ遊びに行かない。', 'ばかりで', ['とおりで', 'おかげで', 'ついでに'], 'On holidays, my younger brother does nothing but play games and never goes outside to play.', '「ゲームをするばかりで」で、同じ好ましくない行動ばかり繰り返すことへの不満を表します。'),
            ('この会議はいつも同じ問題について議論する（　　　）、具体的な解決策が決まらない。', 'ばかりで', ['とたんに', 'わりに', 'かわりに'], 'This meeting does nothing but discuss the same issues, and no concrete solution is ever decided.', '議論だけに終始して前に進まないマイナスの状況を表します。'),
            ('甘いお菓子を食べる（　　　）野菜を全然食べないと、健康に良くありませんよ。', 'ばかりで', ['どころか', 'につれて', 'とともに'], 'If you only eat sweet snacks and do not eat vegetables at all, it is not good for your health.', '偏った行動を繰り返すことを「〜ばかりで」で批判的に述べています。'),
        ],
    },
    9: {
        'reading': 'ば〜のに',
        'wrong': (
            '明日雨が降らなければ、みんなで海へ行けるのに楽しみだ。',
            '「〜ば〜のに」は事実と反対の仮定をして残念がる表現なので、「楽しみだ」のような前向きな期待には繋がりません。',
            '〜ば〜のに expresses regret or disappointment over a counterfactual situation, so it cannot lead into positive anticipation.'
        ),
        'comp_ex': [
            'もう少し早く家を出たらよかったのに、電車に乗り遅れてしまった。',
            'セールでこんなに安くなるなら、先週買わなければよかった。',
        ],
        'quiz': [
            _q0(9),
            ('あと5分早く駅に着いていれ（　　　）、急行電車に間に合ったのに。', 'ば', ['たら', 'と', 'なら'], 'If only I had arrived at the station five minutes earlier, I would have caught the express train.', '「着いていれば〜間に合ったのに」で、実際は間に合わなかったことへの悔しさを表します。'),
            ('もう少し値段が安けれ（　　　）、このコートをすぐに買うのに。', 'ば', ['と', 'ても', 'ながら'], 'If only the price were a little cheaper, I would buy this coat right away.', '現実には高くて買えない残念な気持ちを「安ければ〜買うのに」で表します。'),
            ('体調が悪いのなら、無理をして出勤しないで家で休めばよかった（　　　）。', 'のに', ['から', 'ので', 'ため'], 'If you were feeling unwell, you should have rested at home instead of forcing yourself to come to work.', '文末の「〜ばよかったのに」で、相手の無理な行動を惜しむ気持ちを表します。'),
        ],
    },
    10: {
        'reading': 'ばよかった',
        'wrong': (
            '来週の試験のために、今日から毎日単語を覚えればよかった。',
            '「〜ばよかった」は過去にしなかったことへの後悔を表すため、これからの未来の行動には使えません。',
            '〜ばよかった expresses regret over a past action not taken, so it cannot be used for future plans.'
        ),
        'comp_ex': [
            '道がこんなに混むと分かっていたら、地下鉄で来たらよかった。',
            '大切なデータは消える前に別の場所にも保存しておくべきだった。',
        ],
        'quiz': [
            _q0(10),
            ('限定品のパンが売り切れていた。もっと早い時間に買いに行け（　　　）。', 'ばよかった', ['ばいい', 'るはずだ', 'るべきだ'], 'The limited-edition bread was sold out. I should have gone to buy it at an earlier hour.', '「買いに行けばよかった」で、早く行かなかった過去の行動を後悔しています。'),
            ('旅行先でこんなに冷え込むなら、厚手のセーターを持ってくれ（　　　）。', 'ばよかった', ['ばいい', 'るわけだ', 'るものだ'], 'If it was going to get this chilly at the travel destination, I should have brought a thick sweater.', '持ってこなかった事実に対して「持ってくればよかった」と悔やむ表現です。'),
            ('あの時すぐにお礼のメールを送っておけ（　　　）と、後から反省した。', 'ばよかった', ['ばいい', 'るばかりだ', 'るに違いない'], 'I reflected afterwards that I should have sent a thank-you email right at that time.', '過去の時点でしておかなかったことを後悔する典型的な表現です。'),
        ],
    },
    11: {
        'reading': 'べきだ',
        'wrong': (
            '今日は天気が良くて暖かいから、午後はきっと晴れるべきだ。',
            '「〜べきだ」は道徳的・社会的な義務や当然の主張を表すため、天気の推量には使えません。',
            '〜べきだ expresses moral obligation or social duty, not weather forecasts or natural probability.'
        ),
        'comp_ex': [
            '明日は朝7時の新幹線に乗るので、今夜は早く寝なければならない。',
            '疲れているときは、無理をしないで早めに休んだほうがいいですよ。',
        ],
        'quiz': [
            _q0(11),
            ('他人に迷惑をかけたのだから、まずは素直に謝る（　　　）だ。', 'べき', ['はず', 'わけ', 'つもり'], 'Since you caused trouble for others, you should first apologize sincerely.', '動詞辞書形＋べきだで、人として当然そうするのが正しいという主張を表します。'),
            ('重要な契約を結ぶ前には、書類の内容を隅々まで確認す（　　　）である。', 'べき', ['らしい', 'そうだ', 'ようだ'], 'Before concluding an important contract, one ought to check the contents of the documents thoroughly.', '「する」に接続するときは「するべき」または「すべき」の両方が使われます。'),
            ('子どもの教育方針については、親だけでなく学校ともよく話し合う（　　　）だ。', 'べき', ['きり', 'まま', 'がち'], 'Regarding educational policies for children, parents ought to discuss thoroughly with the school as well.', '社会的な常識や責任の観点から「話し合うべきだ」と述べています。'),
        ],
    },
    12: {
        'reading': 'べきではない',
        'wrong': (
            'この古いエレベーターは故障中なので、今日は動くべきではない。',
            '機械が動かないという客観的な状況には「〜べきではない（道徳的・常識的禁止）」は使えません。',
            '〜べきではない is for moral or ethical prohibition for people, not for describing mechanical states.'
        ),
        'comp_ex': [
            '美術館の中では、展示されている作品に手を触れてはいけない。',
            '試験の途中で他の受験生の解答を決して見てはならない。',
        ],
        'quiz': [
            _q0(12),
            ('事実かどうか確かめもしないで、根拠のないうわさを広める（　　　）。', 'べきではない', ['はずがない', 'わけがない', 'ことはない'], 'You should not spread groundless rumors without even verifying whether they are true.', '道徳的・社会的なマナーとして「広めるべきではない」と戒めています。'),
            ('相手の話を最後まで聞かずに、自分の意見だけを押し付ける（　　　）。', 'べきではない', ['にすぎない', 'に違いない', 'かもしれない'], 'You ought not to force only your own opinion without listening to the other person to the end.', 'コミュニケーション上の好ましくない態度を諫める表現です。'),
            ('公共の場所で、周りの人に迷惑になるような大声で騒ぐ（　　　）。', 'べきではない', ['どころではない', 'ばかりではない', 'そうもない'], 'In public places, one should not make a loud racket that bothers people around them.', '社会常識として慎むべき行為を「〜べきではない」で示します。'),
        ],
    },
    13: {
        'reading': 'べつに〜ない',
        'wrong': (
            '私はこの映画が別に大好きなので、もう3回も見に行った。',
            '「別に」は必ず後ろに否定表現を伴って「特に〜ない」という意味を表すため、肯定文には使えません。',
            '別に requires a negative predicate to mean "not particularly," so it cannot be used in an affirmative sentence like 大好きだ.'
        ),
        'comp_ex': [
            '週末は特に予定がないので、家でゆっくり読書をするつもりだ。',
            'あの店の料理は値段が高いだけで、たいしておいしくなかった。',
        ],
        'quiz': [
            _q0(13),
            ('「甘いものは嫌いですか？」「いいえ、（　　　）嫌いというわけではありませんよ。」', '別に', ['決して', 'まさか', 'きっと'], '"Do you dislike sweets?" "No, it’s not that I particularly dislike them."', '「別に〜ない」で、相手が思うほど強い理由や感情はないことを柔らかく伝えます。'),
            ('急ぎの用事ではなかったから、今日中に返事が来なくても（　　　）構わない。', '別に', ['まるで', 'めったに', 'とうとう'], "Since it wasn't urgent business, I don't really mind even if a reply doesn't come today.", '「別に構わない」で、取り立てて問題にしない態度を表します。'),
            ('彼は怒っているように見えるかもしれないが、（　　　）機嫌が悪いわけではない。', '別に', ['必ず', 'せめて', 'せっかく'], 'He might look angry, but he is not particularly in a bad mood.', '「別に〜わけではない」で、特別な事情がないことを説明します。'),
        ],
    },
    14: {
        'reading': 'ぶりに',
        'wrong': (
            'このバスは15分ぶりに来るので、次の便まで少し待ちましょう。',
            '規則的な間隔で繰り返されることには「〜おきに」や「〜ごとに」を使い、「〜ぶりに」は使えません。',
            'For regular recurring intervals, use 〜おきに or 〜ごとに; 〜ぶりに is only for something happening after a long gap.'
        ),
        'comp_ex': [
            '長い議論を経て、ようやく新しい計画案が承認された。',
            '日曜日に高校時代の友人と久しぶりに会って、楽しく食事をした。',
        ],
        'quiz': [
            _q0(14),
            ('怪我の治療を終えた選手が、半年（　　　）試合のコートに戻ってきた。', 'ぶりに', ['おきに', 'ごとに', 'うちに'], 'Having finished treatment for his injury, the player returned to the match court for the first time in half a year.', '半年という空白期間を経て再び復帰したことを「半年ぶりに」と表します。'),
            ('先週はずっと雨が続いていたので、こんなに気持ちよく晴れたのは1週間（　　　）だ。', 'ぶり', ['おき', 'ごと', 'きり'], 'Since it rained all last week, this is the first time in a week that it has cleared up so pleasantly.', '名詞述語の形「期間＋ぶりだ」でもよく使われます。'),
            ('祖母の家を5年（　　　）訪ねたら、庭の木が見違えるほど大きく育っていた。', 'ぶりに', ['たびに', 'とおりに', '最中に'], 'When I visited my grandmother’s house for the first time in five years, the garden trees had grown noticeably tall.', '5年間の経過の後に再び訪問したことを示します。'),
        ],
    },
    15: {
        'reading': 'ちゅう・じゅう',
        'wrong': (
            '私は昨日、映画を食べる中にポップコーンをこぼしてしまった。',
            '「〜中」は動作性名詞や期間を表す名詞に直接付く接尾語なので、動詞の辞書形には接続できません。',
            '〜中 is a suffix that attaches directly to action nouns or time/place nouns, not to verb dictionary forms.'
        ),
        'comp_ex': [
            '夏休みの間、子どもたちは毎日のように近所のプールへ泳ぎに行った。',
            '大切な電話をしている最中に、玄関のチャイムが鳴ってしまった。',
        ],
        'quiz': [
            _q0(15),
            ('この図書館の本はすべて貸出（　　　）で、現在は棚に一冊も残っていない。', '中', ['間', '内', '上'], 'All copies of this library book are currently checked out, and not a single volume remains on the shelf now.', '動作を表す名詞＋「中（ちゅう）」で、現在その状態が続いていることを表します。'),
            ('今年の夏休みは、日本（　　　）の名所を列車で旅して回りたい。', '中', ['間', '最中', 'っぱなし'], 'This summer vacation, I want to travel around famous places all over Japan by train.', '場所＋「中（じゅう）」で、その場所の全体・至る所という意味を表します。'),
            ('申込書は今月（　　　）に、郵便または窓口にてご提出ください。', '中', ['間', '頃', '度'], 'Please submit the application form by the end of this month by mail or at the counter.', '期間＋「中（じゅう）に」で、その期間が終わるまでにという期限を表します。'),
        ],
    },
    16: {
        'reading': 'だけでなく',
        'wrong': (
            '今日は雨が降っているだけでなく、傘を持ってこなかったので濡れてしまった。',
            '「〜だけでなく」は同類の事柄を並べて付け加える表現なので、原因と結果をつなぐ接続には使えません。',
            '〜だけでなく adds another item or quality of the same kind, so it cannot be used to connect a cause with its result.'
        ),
        'comp_ex': [
            '彼女は歌が上手なばかりでなく、ダンスの表現力も素晴らしい。',
            'この辞書は学生のみならず、専門の研究者にも広く使われている。',
        ],
        'quiz': [
            _q0(16),
            ('この公園は春に桜がきれいな（　　　）、秋の紅葉もとても見事だ。', 'だけでなく', ['かわりに', 'くせに', 'どころか'], 'This park not only has beautiful cherry blossoms in spring, but its autumn leaves are also magnificent.', 'な形容詞＋な＋「だけでなく」で、春の魅力に加えて秋の魅力もあることを表します。'),
            ('休日は家で読書をする（　　　）、近くの川沿いを走ることもある。', 'だけでなく', ['とたんに', 'ついでに', 'あまり'], 'On holidays, I not only read books at home, but sometimes also run along the nearby river.', '動詞辞書形＋「だけでなく」で、行動の幅が一つにとどまらないことを示します。'),
            ('この図書館は本を借りられる（　　　）、静かな自習室も無料で利用できる。', 'だけでなく', ['わりには', 'おかげで', 'せいで'], 'At this library, you can not only borrow books, but also use the quiet study room for free.', '二つの便利な点を「〜だけでなく〜も」で並べています。'),
        ],
    },
    17: {
        'reading': 'だけど',
        'wrong': (
            '昨日の夜は早く寝た。だけど今朝はとてもすっきり目が覚めた。',
            '「だけど」は逆接（しかし）を表す接続詞なので、順当な結果が続く文脈には使えません。',
            'だけど is a conjunction expressing contrast ("however / but"), so it cannot connect a natural cause-and-effect sequence.'
        ),
        'comp_ex': [
            '何度も電話をかけたけれども、相手は忙しかったのか出なかった。',
            '新しい靴はとても気に入っている。しかし、少しサイズが小さかった。',
        ],
        'quiz': [
            _q0(17),
            ('このケーキは見た目は少し地味だ。（　　　）食べてみると驚くほどおいしい。', 'だけど', ['だから', 'そこで', 'すると'], 'This cake looks a little plain. However, when you try eating it, it is surprisingly delicious.', '前文と対照的な内容を会話調でつなぐ逆接の「だけど」です。'),
            ('日曜日にピクニックへ行く約束をしていた。（　　　）朝から雨が降って中止になった。', 'だけど', ['しかも', 'それに', 'したがって'], 'We had promised to go on a picnic on Sunday. However, it rained from the morning and was canceled.', '予定していたことと反対の残念な結果になったことを「だけど」でつなぎます。'),
            ('パソコンの修理代がかなり高かった。（　　　）仕事に必要だから払うしかなかった。', 'だけど', ['つまり', 'たとえば', 'なぜなら'], 'The computer repair cost was quite high. However, since I needed it for work, I had no choice but to pay.', '「高かったけれど払った」という逆接の関係を口語的に表します。'),
        ],
    },
    18: {
        'reading': 'だけ',
        'wrong': (
            '昨日は疲れていたから、寝たくないだけぐっすり寝た。',
            '範囲や限度を表す「〜だけ」は「〜たいだけ」「できる限り」のような肯定の希望・可能表現と結びつきます。',
            'When expressing "as much as," だけ pairs with affirmative desire or potential verbs like 寝たいだけ or できる限り.'
        ),
        'comp_ex': [
            '腕が痛くなるほどたくさんの荷物を運んで、すっかり疲れてしまった。',
            'ちょっと冗談を言ったくらいで、そんなに本気で怒らないでよ。',
        ],
        'quiz': [
            _q0(18),
            ('ビュッフェでは好きな料理を好きな（　　　）お皿に取って食べられます。', 'だけ', ['ばかり', 'きり', 'しか'], 'At the buffet, you can put as much of your favorite food on your plate as you like and eat it.', '「好きなだけ」で、自分が望む限度いっぱいまでという意味を表します。'),
            ('荷物は持てる（　　　）持って、残りは宅配便で送ることにしよう。', 'だけ', ['ほど', 'くらい', 'まま'], 'Let’s carry as much luggage as we can hold, and send the rest by delivery service.', '可能形「持てる」＋「だけ」で、可能な範囲の最大限を表します。'),
            ('本番の試験では、今まで勉強した力を出し切る（　　　）だ。', 'だけ', ['しか', 'あまり', 'くせ'], 'In the actual exam, all I have to do is put forth all the ability I have studied for up to now.', '文末の「〜だけだ」で、他にすることはなくそれを行えばよいという決意を示します。'),
        ],
    },
    19: {
        'reading': 'だらけ',
        'wrong': (
            '夜の公園を歩くと、美しい星空が星だらけで感動した。',
            '「〜だらけ」は汚れや間違いなど好ましくないものがたくさんある時に使うため、美しい星には使えません。',
            '〜だらけ is used when something is covered or filled with undesirable things, so it does not fit admiring beautiful stars.'
        ),
        'comp_ex': [
            'サッカーの練習で雨のグラウンドを走り回り、ユニフォームが泥まみれになった。',
            '今日は朝から嬉しい知らせが続いて、いいことずくめの{一日|いちにち}だった。',
        ],
        'quiz': [
            _q0(19),
            ('子猫と遊んでいたら、引っかかれて手が傷（　　　）になってしまった。', 'だらけ', ['気味', 'がち', 'っぽい'], 'While playing with the kitten, I got scratched and my hands ended up covered in scratches.', '好ましくないもの（傷）がたくさんついている状態を「傷だらけ」と表します。'),
            ('長い間使っていなかった倉庫の中は、棚も床もほこり（　　　）だった。', 'だらけ', ['ずくめ', 'ばかり', 'きり'], 'Inside the warehouse that had not been used for a long time, both the shelves and the floor were covered in dust.', '名詞「ほこり」＋「だらけ」で、一面がほこりで汚れている様子を表します。'),
            ('雨上がりの土手を自転車で走ったら、ズボンの裾が泥（　　　）になった。', 'だらけ', ['がち', 'おき', 'ぶり'], 'When I rode my bicycle along the riverbank after the rain, the hems of my pants got covered in mud.', '泥がたくさん付着したマイナスの状態を「泥だらけ」と表現します。'),
        ],
    },
    20: {
        'reading': 'どんなに〜ても',
        'wrong': (
            'どんなに急いで走っても、始発電車に余裕で間に合った。',
            '「どんなに〜ても」は逆接の仮定条件なので、「どんなに急いでも間に合わなかった」のように期待に反する結果が続きます。',
            'どんなに〜ても forms a concessive clause ("no matter how much..."), so the main clause must contrast with the effort.'
        ),
        'comp_ex': [
            'いくら説明しても、彼は自分の考えを少しも変えようとしなかった。',
            'たとえ両親に反対されても、留学したいという気持ちは変わらない。',
        ],
        'quiz': [
            _q0(20),
            ('（　　　）仕事が忙しくても、毎晩家族と食事をする時間は大切にしている。', 'どんなに', ['もしも', 'まるで', 'まさか'], 'No matter how busy work gets, I cherish the time to have dinner with my family every evening.', '「どんなに＋形容詞て形＋も」で、忙しさの程度にかかわらず習慣を守ることを表します。'),
            ('このパズルは（　　　）考えても解き方が分からず、とうとう諦めてしまった。', 'どんなに', ['せっかく', 'せめて', 'たいてい'], 'No matter how much I thought about this puzzle, I could not figure out how to solve it and finally gave up.', '「どんなに考えても〜分からない」で、最大限考えても解けないことを強調します。'),
            ('遠くへ引っ越して（　　　）離れていても、私たちはいつまでも親友だ。', 'どんなに', ['決して', 'めったに', 'ちっとも'], 'Even if we move far away and no matter how far apart we are, we will always be best friends.', '距離がどれほど離れていても関係が変わらないことを表します。'),
        ],
    },
    21: {
        'reading': 'どうしても',
        'wrong': (
            '今日は時間があるから、どうしても暇つぶしに散歩へ行くかもしれない。',
            '「どうしても」は強い意志や必然性を表すため、「暇つぶしに〜かもしれない」のような曖昧な文脈には合いません。',
            'どうしても expresses strong determination or inevitability, so it clashes with casual or uncertain expressions like かもしれない.'
        ),
        'comp_ex': [
            '次の試合は決勝進出がかかっているので、なんとしても勝ちたい。',
            '鍵をどこに置いたのか、どうしても思い出せなくて困っている。',
        ],
        'quiz': [
            _q0(21),
            ('今度の週末だけは外せない用事があり、（　　　）出席することができません。', 'どうしても', ['めったに', 'かならずしも', 'たいてい'], 'Just for this coming weekend I have unavoidable business, so I simply cannot attend no matter what.', '否定形と呼応して、どんなに都合をつけようとしても不可能であることを表します。'),
            ('子どもの頃からの夢だった宇宙飛行士に、（　　　）なりたいと思って勉強している。', 'どうしても', ['ちっとも', 'べつに', 'まさか'], 'I am studying because I want to become an astronaut, which has been my dream since childhood, no matter what.', '肯定の希望表現と結びついて「どんなことがあっても実現したい」という強い気持ちを表します。'),
            ('明日の朝一番に提出する書類なので、妥協せず（　　　）今日中に仕上げたい。', 'どうしても', ['たまに', 'すこしも', 'あまり'], 'Since it is a document to be submitted first thing tomorrow morning, I want to finish it today by all means without compromising.', '強い決意をもって「どんなことをしてでも今日中に終えたい」と述べています。'),
        ],
    },
    22: {
        'reading': 'ふりをする',
        'wrong': (
            '彼は本当に風邪をひいて39度の熱があったので、病気のふりをして休んだ。',
            '「ふりをする」は実際はそうではないのに嘘の態度を見せることなので、本当に病気の時には使えません。',
            'ふりをする means pretending to be something one is not, so it cannot be used when the person is genuinely sick.'
        ),
        'comp_ex': [
            '手品師は箱の中が{空|から}っぽに見せかけて、鮮やかな花を取り出した。',
            '彼女は悲しみを隠して、いつものように明るい表情を装っていた。',
        ],
        'quiz': [
            _q0(22),
            ('サプライズパーティーの準備をしていたので、彼の誕生日を忘れた（　　　）をしていた。', 'ふり', ['つもり', 'はず', 'わけ'], 'Because we were preparing a surprise party, we pretended to have forgotten his birthday.', '実際は覚えているのに忘れたように振る舞うことを「忘れたふりをする」と言います。'),
            ('本当は答えを知っていたのに、彼女は知らない（　　　）をして黙っていた。', 'ふり', ['こと', 'もの', 'まま'], 'Even though she actually knew the answer, she pretended not to know and stayed silent.', '動詞ない形「知らない」＋「ふりをする」で、知らない様子を装うことを表します。'),
            ('母が部屋に入ってきたので、漫画を隠して急いで勉強している（　　　）をした。', 'ふり', ['くせ', 'たび', 'せい'], 'Since my mother came into the room, I hid my comic book and quickly pretended to be studying.', '今まさに勉強しているかのように見せかける動作を表します。'),
        ],
    },
    23: {
        'reading': 'ふと',
        'wrong': (
            '半年前から計画を立てて、ふと来週の海外旅行のチケットを予約した。',
            '「ふと」は計画や意図がなく偶然・急に思いついたり気づいたりする様子を表すため、長期計画には使えません。',
            'ふと describes something happening spontaneously or by chance without prior planning, so it cannot modify a long-planned action.'
        ),
        'comp_ex': [
            'あまりにも景色が美しかったので、思わず足を止めて見とれてしまった。',
            '休日の午後に何気なくテレビをつけたら、懐かしい映画が放送されていた。',
        ],
        'quiz': [
            _q0(23),
            ('古いアルバムを整理していたら、（　　　）小学校時代の担任の先生を思い出した。', 'ふと', ['わざと', 'かならず', 'けっして'], 'While organizing old photo albums, I suddenly thought of my homeroom teacher from elementary school.', '意識していなかった記憶が急に心に浮かぶ様子を「ふと思い出す」と表します。'),
            ('仕事の手を止めて（　　　）時計を見ると、もう夜の10時を過ぎていた。', 'ふと', ['せっかく', 'せめて', 'めったに'], 'When I stopped working and casually glanced at the clock, it was already past 10 p.m.', '特別な意図なく視線を向けたときに「ふと見る」を使います。'),
            ('電車の中で（　　　）隣に座っている人を見たら、大学の同級生で驚いた。', 'ふと', ['どうしても', 'かならずしも', 'ちっとも'], 'When I happened to look at the person sitting next to me on the train, I was surprised to see a university classmate.', '偶然何気なく見た様子を表す副詞です。'),
        ],
    },
    24: {
        'reading': 'がち',
        'wrong': (
            '春になって暖かくなると、公園の桜がきれいに咲きがちだ。',
            '「〜がち」は病気や遅刻、忘れ物など好ましくない傾向に使うため、桜がきれいに咲くことには使えません。',
            '〜がち expresses an undesirable tendency (such as illness, lateness, or forgetting), not positive natural events.'
        ),
        'comp_ex': [
            'この薄いグラスは割れやすいので、洗うときは{十分|じゅうぶん}に気をつけてください。',
            '現代人はスマートフォンを見る時間が長く、目が疲れる傾向がある。',
        ],
        'quiz': [
            _q0(24),
            ('冬は空気が乾燥するため、のどを痛めて風邪をひき（　　　）になる。', 'がち', ['だらけ', 'ずくめ', 'っぱなし'], 'Because the air is dry in winter, people tend to hurt their throats and catch colds easily.', '動詞ます形「ひき」＋「がち」で、風邪をひきやすいマイナスの傾向を表します。'),
            ('雪が降る季節は道路が混雑して、バスの到着が遅れ（　　　）だ。', 'がち', ['気味', 'っぽい', 'きり'], 'In the snowy season, the roads get congested and bus arrivals tend to be delayed.', '「遅れがち」で、たびたび遅れる傾向があることを示します。'),
            ('忙しい{日|ひ}が続くと、睡眠時間が不足して体調を崩し（　　　）なので注意したい。', 'がち', ['かけ', 'すぎ', 'おき'], 'When busy days continue, sleep time runs short and one tends to fall out of shape, so I want to be careful.', '好ましくない状態に陥りやすいことを「崩しがち」と表現します。'),
        ],
    },
    25: {
        'reading': 'がたい',
        'wrong': (
            'この瓶のふたは固く閉まっていて、子どもの力では{開|あ}けがたい。',
            '「〜がたい」は「信じがたい」「理解しがたい」など心の働きや発言に関する動詞に付き、物理的な力作業には「〜にくい」を使います。',
            '〜がたい attaches to mental or expressive verbs (believe, understand, forgive, say), whereas 〜にくい is used for physical difficulty.'
        ),
        'comp_ex': [
            'この靴は底が硬くて歩きにくいから、長距離の散歩には向いていない。',
            'お世話になった先輩からの頼みは断りづらくて、つい引き受けてしまった。',
        ],
        'quiz': [
            _q0(25),
            ('あんなに練習したチームが1回戦で負けるとは、誰にとっても想像し（　　　）結果だった。', 'がたい', ['すぎる', 'かける', 'っぱなしの'], 'That a team which practiced so much would lose in the first round was a result hard for anyone to imagine.', '「想像しがたい」で、心理的に到底想像できないほど意外であることを表します。'),
            ('長年の友人を裏切るような彼の態度は、どうしても理解し（　　　）。', 'がたい', ['きれない', 'かねない', 'っこない'], 'His attitude of betraying a longtime friend is simply impossible to understand.', '「理解しがたい」は、納得や理解が心理的に困難であることを示す代表的な表現です。'),
            ('旅先で出会った人々の温かい親切は、何年たっても忘れ（　　　）思い出だ。', 'がたい', ['がちだ', '気味だ', 'だらけの'], 'The warm kindness of the people I met while traveling is an unforgettable memory no matter how many years pass.', '「忘れがたい」で、心に深く残っていて忘れられないことを表します。'),
        ],
    },
    26: {
        'reading': 'ぎみ',
        'wrong': (
            '彼は昨日から入院して高熱を出しているので、少し風邪気味だ。',
            '「〜気味」は「ほんの少しその傾向がある」という軽い状態を表すため、高熱で入院するような重い症状には使えません。',
            '〜気味 indicates a slight touch or mild tendency of a condition, so it cannot describe a severe illness requiring hospitalization.'
        ),
        'comp_ex': [
            '最近は若い世代の間で、静かな田舎暮らしに関心を持つ傾向が見られる。',
            '徹夜明けで少し疲れの感じが残っているが、午後の会議には出られる。',
        ],
        'quiz': [
            _q0(26),
            ('連休中にごちそうを食べすぎて、なんだか少し太り（　　　）だ。', '気味', ['がち', 'だらけ', 'っぱなし'], 'Having eaten too many feasts during the holidays, I feel like I have gained a little weight.', '動詞ます形「太り」＋「気味」で、少し太ってきた兆候があることを表します。'),
            ('今週は残業が続いて疲れ（　　　）だから、週末は家でゆっくり休もう。', '気味', ['っぽい', 'ずくめ', 'きり'], 'Since overtime has continued this week and I am feeling a bit tired, let’s rest at home this weekend.', '「疲れ気味」で、現在少し疲れを感じている状態を表します。'),
            ('初めての舞台で最初は緊張（　　　）だったが、だんだん落ち着いて演奏できた。', '気味', ['がち', 'かけ', 'おき'], 'On my first stage I was feeling slightly nervous at the beginning, but gradually I calmed down and played well.', '名詞「緊張」＋「気味」で、やや緊張している様子を表します。'),
        ],
    },
    27: {
        'reading': 'ごとに',
        'wrong': (
            '私は3年ごとに久しぶりに高校の同窓会へ出席した。',
            '「〜ごとに」は毎回規則的に繰り返すことを表し、「久しぶりに（1回だけ期間が離れた）」とは一緒に使えません。',
            '〜ごとに expresses regular repetition ("every X"), so it cannot be combined with a one-off gap expression like 久しぶりに.'
        ),
        'comp_ex': [
            '祖母は私が遊びに行くたびに、大好きなイチゴのケーキを焼いてくれる。',
            '道路の端に10メートルおきに街灯が設置されていて、夜でも明るい。',
        ],
        'quiz': [
            _q0(27),
            ('この路線バスは、平日の朝は10分（　　　）に発車するのでとても便利だ。', 'ごと', ['ぶり', 'きり', 'まま'], 'This route bus departs every 10 minutes on weekday mornings, so it is very convenient.', '時間を表す名詞＋「ごとに」で、一定の間隔で規則的に繰り返されることを示します。'),
            ('一雨降る（　　　）に春の暖かさが近づいてくるのを感じる。', 'ごと', ['おき', 'ぶり', 'かけ'], 'With every rainfall, I feel the warmth of spring drawing closer.', '動詞辞書形＋「ごとに」で、その事柄が起こるにつれて一歩ずつ変化が進むことを表します。'),
            ('発表会はクラス（　　　）に順番で行われますので、案内があるまでお待ちください。', 'ごと', ['たび', 'おき', 'うち'], 'The presentation will be held in turn by each class, so please wait until you are called.', '集団の名詞＋「ごとに」で、「それぞれの単位に分けて」という意味を表します。'),
        ],
    },
    28: {
        'reading': 'ほど〜ない',
        'wrong': (
            '今日のテストは昨日のテストほど難しかったので、時間が足りなかった。',
            '比較の基準を示す「〜ほど」で程度が低いことを言う場合は、必ず「難しくなかった」のように否定形が続きます。',
            'When 〜ほど marks a standard of comparison ("not as... as"), the predicate must be in the negative form.'
        ),
        'comp_ex': [
            '家族の健康くらい大切なものはないと、病気をして改めて感じた。',
            '明日の試験は範囲が狭いので、前回ほど大変ではないと思う。',
        ],
        'quiz': [
            _q0(28),
            ('新しい掃除機は音が静かで、前のモデル（　　　）重くないので使いやすい。', 'ほど', ['ばかり', 'だけ', 'きり'], 'The new vacuum cleaner is quiet and not as heavy as the previous model, making it easy to use.', '「前のモデルほど重くない」で、比較の対象ほど程度が高くないことを表します。'),
            ('実際に自分でやってみると、見る（　　　）簡単ではないことがよく分かった。', 'ほど', ['わりに', 'くせに', 'とおり'], 'When I actually tried doing it myself, I realized well that it is not as easy as it looks.', '動詞辞書形「見る」＋「ほど〜ない」で、見た目ほど簡単ではないことを表します。'),
            ('一生懸命練習して勝った試合（　　　）嬉しいことはない。', 'ほど', ['ばかり', 'どころ', 'ついで'], 'There is nothing as joyful as a match won after practicing with all one’s might.', '「〜ほど…ことはない」で、最上級の感情や価値を強調する表現です。'),
        ],
    },
    29: {
        'reading': 'ほど',
        'wrong': (
            '今日は少しだけ風が吹いていて、傘が壊れるほど穏やかな天気だ。',
            '「〜ほど」は程度が非常に高いことを例示するため、「傘が壊れるほど」は「穏やかな天気」とは矛盾します。',
            '〜ほど illustrates an extreme degree, so "strong enough to break an umbrella" contradicts "calm weather."'
        ),
        'comp_ex': [
            'おなかが痛くなるくらい大笑いして、日頃のストレスが吹き飛んだ。',
            'テーブルの上からこぼれるばかりにごちそうが並んでいる。',
        ],
        'quiz': [
            _q0(29),
            ('久しぶりに山登りをしたら、翌日は階段を下りられない（　　　）足が痛くなった。', 'ほど', ['わりに', 'くせに', 'かわりに'], 'After mountain climbing for the first time in a while, my legs hurt so much the next day that I could not walk down the stairs.', '痛みの程度の激しさを「階段を下りられないほど」という具体例で示しています。'),
            ('今年の夏は、外に5分立っているだけで汗が噴き出す（　　　）蒸し暑い。', 'ほど', ['ばかり', 'とおり', 'きり'], 'This summer is so humid that sweat pours out just from standing outside for five minutes.', '蒸し暑さの程度がどれほど高いかを「〜ほど」で表します。'),
            ('会場には入り口からあふれる（　　　）大勢の観客が集まっていた。', 'ほど', ['だけ', 'しか', 'まま'], 'So many spectators had gathered at the venue that they were overflowing from the entrance.', '人数の多さを強調する「あふれるほど」の用法です。'),
        ],
    },
    30: {
        'reading': 'いちどに',
        'wrong': (
            'この狭い改札口は、一人ずつ順番に一度に通ってください。',
            '「一度に」は複数を同時にまとめて行う意味なので、「一人ずつ順番に」とは正反対で一緒に使えません。',
            '一度に means doing multiple things all at once, which contradicts "one person at a time in order."'
        ),
        'comp_ex': [
            '春になると、庭のチューリップがいっぺんに色鮮やかな花を咲かせた。',
            '新入社員の研修とオフィスの引っ越しが同時に重なって大忙しだった。',
        ],
        'quiz': [
            _q0(30),
            ('春になって気温が上がり、桜も梅も（　　　）に咲き始めた。', '一度', ['一斉', '一応', '一向'], 'As spring arrived and temperatures rose, both cherry and plum blossoms began to bloom all at once.', '「一度に（いちどに）」で、複数の花が一回で同時に咲く様子を表します。'),
            ('そんなにたくさんの質問を（　　　）にされても、すぐには答えられません。', '一度', ['一体', '一部', '一般'], 'Even if you ask so many questions all at once, I cannot answer them right away.', '複数の質問を同時にまとめてされることを「一度にされる」と表します。'),
            ('重い荷物を（　　　）に運ぼうとせず、何回かに分けて運んだほうが安全だ。', '一度', ['一息', '一旦', '一層'], 'Rather than trying to carry heavy luggage all at once, it is safer to divide it into several trips.', '「何回かに分けて」と対比して、一回でまとめて運ぶことを「一度に」と言います。'),
        ],
    },
    31: {
        'reading': 'いくら〜ても',
        'wrong': (
            'いくら練習しても、彼はついに全国大会で優勝することができた。',
            '「いくら〜ても」は逆接の条件を表すため、「優勝することができた」のような順当な成功結果には繋がりません。',
            'いくら〜ても introduces a concessive condition ("no matter how much..."), so it cannot lead into a direct positive result of that effort.'
        ),
        'comp_ex': [
            'どんなに遠くに離れていても、家族を大切に思う気持ちは変わらない。',
            'たとえ時間がかかったとしても、最後まで自分の力でやり遂げたい。',
        ],
        'quiz': [
            _q0(31),
            ('（　　　）美味しい料理でも、毎日同じメニューばかり続くと飽きてしまう。', 'いくら', ['もしも', 'まさか', 'まるで'], 'No matter how delicious the food is, if the exact same menu continues every day, you get tired of it.', '「いくら＋形容詞ても」で、美味しさの程度がどれほど高くても飽きるという逆接を表します。'),
            ('（　　　）急いでタクシーに乗っても、今からでは開演時間に間に合いそうにない。', 'いくら', ['せっかく', 'せめて', 'たいてい'], 'No matter how much we hurry and take a taxi, it does not look like we will make the curtain time from now.', '「いくら〜ても」で、どれだけ急いでも結果が変わらないことを示します。'),
            ('若い頃と違って、最近は（　　　）寝ても疲れがなかなか取れない。', 'いくら', ['決して', 'めったに', 'ちっとも'], 'Unlike when I was young, lately no matter how much I sleep, I cannot easily get rid of my fatigue.', '睡眠の量がどれだけ多くても疲れが取れないことを「いくら寝ても」で表します。'),
        ],
    },
    32: {
        'reading': 'いっぽうだ',
        'wrong': (
            '毎朝ジョギングを続けたおかげで、最近は体力が良くなる一方だ。',
            '「〜一方だ」は主に状況が悪化したり増減が止まらない傾向に使われ、単に「良くなる」のような好ましい変化にはあまり使いません。',
            '〜一方だ is typically used for continuous progression in one direction, most often worsening conditions or unchecked increases/decreases.'
        ),
        'comp_ex': [
            'スマートフォンの普及により、紙の新聞を読む人は減るばかりだ。',
            '春が近づくにつれて、昼間の気温がどんどん上がってきた。',
        ],
        'quiz': [
            _q0(32),
            ('インターネットの普及によって、世界の情報量は増える（　　　）だ。', '一方', ['最中', 'っぱなし', 'きり'], 'With the spread of the internet, the amount of information in the world only continues to increase.', '動詞辞書形「増える」＋「一方だ」で、増加の傾向が止まらずに進むことを表します。'),
            ('忙しくて掃除をする暇がなく、机の上には書類がたまる（　　　）だ。', '一方', ['気味', 'がち', 'かけ'], 'I am so busy that I have no time to clean, and documents on my desk just keep piling up.', '好ましくない状態がどんどん進んでいく様子を「たまる一方だ」と表します。'),
            ('原材料の価格が上がり続け、工場の経営は苦しくなる（　　　）だ。', '一方', ['とおり', 'かわり', 'どころ'], 'Prices of raw materials keep rising, and the management of the factory is only getting tougher.', '状況が悪化する方向に進み続けていることを示します。'),
        ],
    },
    33: {
        'reading': 'いったい',
        'wrong': (
            '明日の会議は一体午後2時から第1会議室で始まります。',
            '「一体」は疑問詞を伴う疑問文で「いったい何が・なぜ」と強調する副詞なので、事実を述べる平叙文には使えません。',
            '一体 is an adverb that reinforces a question word ("what/who/why on earth"), so it cannot be used in a plain declarative statement.'
        ),
        'comp_ex': [
            'こんな大事な書類をなくすなんて、いったい全体どういうつもりなのか。',
            '誰もいないはずの教室の電気がついているが、いったい誰がつけたのだろう。',
        ],
        'quiz': [
            _q0(33),
            ('私の机の上にきれいな花束が置いてあるが、（　　　）誰がプレゼントしてくれたのだろう。', '一体', ['一応', '一斉', '一旦'], 'There is a pretty bouquet of flowers on my desk, but who on earth could have given it to me as a present?', '疑問詞「誰」の前に「一体」を置いて、驚きや疑問の気持ちを強めています。'),
            ('さっきから同じ場所をぐるぐる回っているけれど、（　　　）どこへ向かっているのですか。', '一体', ['一向', '一層', '一息'], 'We have been going around in circles in the same place for a while now, where on earth are we heading?', '「一体どこへ〜か」で、見当がつかないもどかしさや強い疑問を表します。'),
            ('こんなにたくさんの荷物を抱えて、彼は（　　　）何を始めるつもりなのだろうか。', '一体', ['一度', '一部', '一般'], 'Carrying this much luggage, what on earth is he planning to start?', '疑問詞「何」と結びついて「いったい何を」と強く問いかける表現です。'),
        ],
    },
    34: {
        'reading': 'じゃない',
        'wrong': (
            '社内規定により、来週から新しい制服を着るんじゃない。',
            '確認や柔らかい推測を表す「〜んじゃない？」は会話表現であり、硬い規則の通達には使えません（また文末を下げると禁止の意味になります）。',
            'The conversational confirmation/suggestion 〜んじゃない？ does not fit formal written regulations (and with falling intonation it sounds like blunt prohibition).'
        ),
        'comp_ex': [
            'こんなに毎日練習しているのだから、次の大会では優勝できるのではないか。',
            '{空|そら}に黒い雲が広がってきたから、もうすぐ雨が降るだろう。',
        ],
        'quiz': [
            _q0(34),
            ('そのコート、とてもよく似合っているね。すごく素敵なん（　　　）！', 'じゃない', ['どころか', 'ばかりか', 'っこない'], 'That coat looks great on you. Isn’t it really lovely!', '「素敵なんじゃない！」と感嘆や賛成の気持ちを親しく伝える口語表現です。'),
            ('何度もあくびをしているけれど、昨夜はあまり眠れなかったん（　　　）？', 'じゃない', ['べきだ', 'ものか', 'っぱなし'], 'You have been yawning repeatedly; didn’t you sleep well last night?', '相手の様子を見て「〜なのではないか」と柔らかく推測・確認する表現です。'),
            ('時計を見て！もうすぐ電車の時間だから、急いだほうがいいん（　　　）？', 'じゃない', ['きれない', 'かねない', 'がたい'], 'Look at the clock! It is almost time for the train, so shouldn’t we hurry?', '「〜たほうがいいんじゃない？」で、相手に控えめに提案・忠告します。'),
        ],
    },
    35: {
        'reading': 'かける',
        'wrong': (
            '先月全部読みかけた本を、今日図書館へ返しに行った。',
            '「〜かける」は途中で止まって最後まで終わっていない状態を表すため、「全部」とは一緒に使えません。',
            '〜かける means an action was started but left unfinished halfway, so it contradicts "all the way through" (全部).'
        ),
        'comp_ex': [
            'テーブルの上に飲みかけのコーヒーが置いたままになっている。',
            '駅へ向かう途中で雨が降り出したので、急いでコンビニで傘を買った。',
        ],
        'quiz': [
            _q0(35),
            ('夕食を食べ（　　　）ところで急な電話がかかってきて、席を立った。', 'かけた', ['きった', 'すぎた', '抜いた'], 'Just when I had started eating dinner, an urgent phone call came in and I left my seat.', '「食べかけた」で、食べ始めてまだ終わっていない途中の段階を表します。'),
            ('彼は何か言い（　　　）が、周りの様子を見て急に口をつぐんだ。', 'かけた', ['あげた', 'きった', 'すぎた'], 'He was about to say something, but looking at the situation around him, he suddenly fell silent.', '「言いかけた」で、言葉を口に出そうとして途中でやめた様子を表します。'),
            ('お皿に食べ（　　　）のクッキーが残っているけれど、誰が食べていたの？', 'かけ', ['きり', 'すぎ', 'がち'], 'There is a half-eaten cookie left on the plate; who was eating it?', '「動詞ます形＋かけの＋名詞」で、途中でそのままになっている物を表します。'),
        ],
    },
    36: {
        'reading': 'かなにか',
        'wrong': (
            '私の生年月日は1998年5月3日か何かです。',
            '「〜か何か」ははっきり特定せずに例を挙げる表現なので、自分の正確な生年月日を答える場面には不自然です。',
            '〜か何か gives an approximate example ("or something"), so it is unnatural when stating exact personal facts like one’s own birth date.'
        ),
        'comp_ex': [
            '休日は映画か何かを見て、家でゆっくり過ごすことが多い。',
            '少し時間があるから、駅前の喫茶店でコーヒーでも飲みませんか。',
        ],
        'quiz': [
            _q0(36),
            ('小腹が{空|す}いたので、果物（　　　）軽いものを少し食べたいな。', 'か何か', ['どころか', 'ばかりか', 'とたんに'], 'Since I am a little hungry, I would like to eat a little bit of fruit or something light.', '「果物か何か」で、果物を一例として挙げつつ軽い食べ物を漠然と指しています。'),
            ('来週のパーティーには、手作りのお菓子（　　　）を持っていくつもりだ。', 'か何か', ['のあまり', 'のくせに', 'のわりに'], 'To next week’s party, I plan to bring homemade sweets or something.', '持参する物をはっきり限定せず「お菓子か何か」と柔らかく例示しています。'),
            ('さっき廊下で物音がしたのは、風で窓が揺れた（　　　）だろう。', 'か何か', ['ばかり', 'とおり', 'きり'], 'The noise in the hallway just now was probably the window shaking in the wind or something.', '原因をはっきり断定せず、一例を挙げて推測する用法です。'),
        ],
    },
    37: {
        'reading': 'から〜にかけて',
        'wrong': (
            '今日の午後の会議は、2時00分から3時00分にかけて行われます。',
            '「〜から〜にかけて」は境界がはっきりしないおおよその範囲を表すため、正確な開始・終了時刻には「〜から〜まで」を使います。',
            '〜から〜にかけて indicates an approximate span without sharp boundaries, so exact start and end times require 〜から〜まで.'
        ),
        'comp_ex': [
            'この銀行の窓口は、平日の午前9時から午後3時まで営業しています。',
            '秋から冬にかけて空気が乾燥するので、風邪の予防に気をつけたい。',
        ],
        'quiz': [
            _q0(37),
            ('昨日の夜から今朝に（　　　）、山沿いの地域でたくさんの雪が降った。', 'かけて', ['つれて', 'とって', 'よると'], 'From last night through this morning, a lot of snow fell in the mountainous areas.', '「夜から今朝にかけて」で、連続するおおよその時間帯を表します。'),
            ('この地域では、6月から7月に（　　　）雨の多い季節が続く。', 'かけて', ['対して', '関して', '比べて'], 'In this region, the rainy season continues from around June through July.', '時期のまたがる範囲を「6月から7月にかけて」と示しています。'),
            ('首から肩に（　　　）ひどく凝っているので、温泉でゆっくり温まりたい。', 'かけて', ['そって', 'こめて', 'むけて'], 'Since I have terrible stiffness from my neck across to my shoulders, I want to warm up slowly in a hot spring.', '体の部位など空間的な広がりにも「AからBにかけて」が使われます。'),
        ],
    },
    38: {
        'reading': 'かわりに',
        'wrong': (
            '今日は天気が良い代わりに、公園で楽しくお弁当を食べた。',
            '「代わりに」は「代理・代替・交換条件・対比」を表すため、単なる理由（「天気が良いから」）の意味では使えません。',
            '代わりに expresses substitution, compensation, or contrast, so it cannot be used simply to mean "because the weather is nice."'
        ),
        'comp_ex': [
            '入院中の部長にかわって、課長が本日の会議の司会を務めた。',
            'このアパートは駅から近くて便利なのだが、その反面、家賃が少し高い。',
        ],
        'quiz': [
            _q0(38),
            ('料理を作ってもらった（　　　）、食後の皿洗いは私が担当することにした。', '代わりに', ['くせに', 'あまりに', 'とたんに'], 'In return for having the meal cooked for me, I decided to take charge of washing the dishes after eating.', '「〜してもらう代わりに」で、交換条件や役割分担を表します。'),
            ('バターがなかったので、その（　　　）サラダ油を使ってお菓子を焼いた。', '代わりに', ['おかげで', 'せいで', 'たびに'], 'Since there was no butter, I baked the sweets using salad oil instead.', '「その代わりに」で、別の物で代用したことを表します。'),
            ('この部屋は少し狭い（　　　）、南向きで日当たりがとても良いのが気に入っている。', '代わりに', ['どころか', 'ばかりか', 'につれて'], 'While this room is a bit small, in compensation it faces south and gets great sunlight, which I like.', 'ひとつの短所を補う長所があるという対比を表します。'),
        ],
    },
    39: {
        'reading': 'けっか',
        'wrong': (
            'これからアンケート調査を行う結果、来月にも計画を見直すつもりだ。',
            '「〜結果」はすでに行われたことの後に起きた事実を表すため、「これから行う」という未完了の動作には付きません。',
            '〜結果 describes an outcome following a completed action or investigation, so it connects to the past form (行った結果), not a future action.'
        ),
        'comp_ex': [
            '何か月も悩み抜いた末に、彼は自分の店を{開|ひら}く決心をした。',
            'どの靴にするか散々迷ったあげく、結局一足も買わずに帰ってきた。',
        ],
        'quiz': [
            _q0(39),
            ('病院で詳しい検査を受けた（　　　）、どこにも異常がないことが分かって安心した。', '結果', ['最中', '途端', 'ついで'], 'As a result of undergoing a detailed examination at the hospital, I was relieved to find nothing abnormal anywhere.', '「動詞た形＋結果」で、検査を行った末に判明した事柄を客観的に述べます。'),
            ('生活習慣を見直して毎日歩いた（　　　）、半年で体重が3キロ減った。', '結果', ['あまり', 'くせに', 'かわり'], 'As a result of reviewing my lifestyle habits and walking every day, my weight decreased by three kilograms in half a year.', '継続した行動の成果として現れた事実を「〜た結果」で表します。'),
            ('全社員へのアンケート調査の（　　　）を踏まえて、食堂のメニューが新しくなった。', '結果', ['原因', '理由', '目的'], 'Based on the results of the questionnaire survey of all employees, the cafeteria menu was renewed.', '「名詞＋の結果」で、調査などから得られたまとまりを示します。'),
        ],
    },
    40: {
        'reading': 'けっきょく',
        'wrong': (
            '朝起きたらすぐに出発する予定だったが、結局予定通りすぐに出発した。',
            '「結局」は途中で迷ったり紆余曲折があった末の結末に使われるため、最初から何の変化もなく予定通り進んだ場合には不自然です。',
            '結局 implies reaching a final outcome after twists, turns, or hesitation, so it feels unnatural when everything went straight as planned from the start.'
        ),
        'comp_ex': [
            '長い間修理しながら使っていた時計が、とうとう動かなくなってしまった。',
            '何年も研究を続けてきた新しい薬が、ついに完成の日を迎えた。',
        ],
        'quiz': [
            _q0(40),
            ('傘を持っていくか迷ったが、持っていかなくて（　　　）帰りに雨に降られた。', '結局', ['決して', 'めったに', 'せっかく'], 'I hesitated over whether to bring an umbrella, didn’t bring one, and in the end got caught in the rain on my way home.', '迷った末の最終的な結果を「結局」で導いています。'),
            ('休日にどこへ行くか家族で話し合ったが、意見がまとまらず（　　　）家で過ごした。', '結局', ['かならず', 'ちっとも', 'まるで'], 'The family discussed where to go on the holiday, but could not agree and ended up spending the day at home.', 'いろいろ話し合った末にどうなったかをまとめる副詞です。'),
            ('3軒の本屋を回って探したけれど、（　　　）欲しかった雑誌は見つからなかった。', '結局', ['たいてい', 'べつに', 'まさか'], 'I went around three bookstores looking for it, but in the end the magazine I wanted was not found.', '努力したものの最終的にどうなったかを表す「結局」の用法です。'),
        ],
    },
    41: {
        'reading': 'けっして〜ない',
        'wrong': (
            '来週の試合には、練習の成果を出して決して優勝したい。',
            '「決して」は必ず否定表現（〜ない・〜まい）と呼応して強い否定を表すため、肯定文には使えません。',
            '決して must pair with a negative predicate ("never / by no means"), so it cannot be used in an affirmative sentence.'
        ),
        'comp_ex': [
            '大事な試験の前なので、今日は絶対に風邪をひくわけにはいかない。',
            'どれほど難しい問題であっても、途中で投げ出すことは断じてしない。',
        ],
        'quiz': [
            _q0(41),
            ('どれほど困難な壁にぶつかっても、私は自分の夢を（　　　）諦めない。', '決して', ['たいてい', 'せっかく', 'せめて'], 'No matter how difficult a wall I hit, I will never give up on my dream.', '「決して〜ない」で、強い意志による否定を表します。'),
            ('この山道は夜は暗くて危険ですから、（　　　）一人で歩かないでください。', '決して', ['かならず', 'おそらく', 'たまに'], 'Since this mountain path is dark and dangerous at night, please never walk alone.', '強い禁止・注意の文脈で「決して〜ないでください」と使われます。'),
            ('今回の成功はチーム全員で協力した成果であり、（　　　）私一人の力ではありません。', '決して', ['めったに', 'ほとんど', 'あまり'], 'This success is the result of the whole team cooperating, and is by no means my own power alone.', '事実を強く否定して謙遜や強調を表す「決して〜ではない」の用法です。'),
        ],
    },
    42: {
        'reading': 'きれない',
        'wrong': (
            '今日は時間がたっぷりあるので、この薄い本ならすぐ読み切れない。',
            '「〜切れない」は量や数が多すぎて最後までできないことを表すため、「時間がたっぷりあってすぐ読める」文脈には矛盾します。',
            '〜切れない means being unable to finish something completely because of its large amount or difficulty, contradicting having plenty of time for a thin book.'
        ),
        'comp_ex': [
            'まだ心の整理がつかず、留学に行くかどうか決めきらないままでいる。',
            '夜空には数えきれないほどの美しい星がきらきらと輝いていた。',
        ],
        'quiz': [
            _q0(42),
            ('引っ越しまでに整理しなければならない荷物が多すぎて、{一日|いちにち}では片付け（　　　）。', '切れない', ['すぎない', 'かけない', 'がたい'], 'There is too much luggage to organize before the move, so I cannot finish tidying it all up in one day.', '動詞ます形＋「切れない」で、量が多すぎて最後まで完了できないことを表します。'),
            ('今回の旅行では楽しい思い出がたくさんできて、一言では語り（　　　）。', '切れない', ['かねない', 'っこない', 'っぱなしだ'], 'I made so many fun memories on this trip that I cannot tell them all in a single word.', '「語り切れない」で、内容が豊富すぎてすべてを話し終えることができないという意味になります。'),
            ('お祭りの会場には、広場に入り（　　　）ほどたくさんの見物客が集まった。', '切れない', ['すぎない', 'がたい', 'かけない'], 'So many spectators gathered at the festival venue that they could not all fit into the plaza.', '「入り切れない」で、収容できる限界を超えて全部は入れないことを表します。'),
        ],
    },
    43: {
        'reading': 'きり',
        'wrong': (
            '弟はさっき部屋に入ったきり、5分後にもう一度リビングへ出てきた。',
            '「〜たきり」は「その動作を最後に、その後ずっと変化がない」ことを表すため、すぐに出てきた場合には使えません。',
            '〜たきり indicates that after an action occurred, no subsequent change happened for a long time, so it cannot be used when the state changed five minutes later.'
        ),
        'comp_ex': [
            '休日は午前中に少し買い物に出かけただけで、あとは家でゆっくり過ごした。',
            '朝から激しい雨が降り続いていて、外へ出ようにも出られない状態だ。',
        ],
        'quiz': [
            _q0(43),
            ('父は朝早く「散歩に行く」と言って出かけた（　　　）、昼になっても帰ってこない。', 'きり', ['たび', 'うち', 'ころ'], 'My father went out early in the morning saying "I’m going for a walk," and has not come back even at noon.', '「出かけたきり」で、出かけたのを最後に帰ってこない状態が続いていることを表します。'),
            ('友人から借りた本を本棚に置いた（　　　）、忙しくてまだ1ページも読んでいない。', 'きり', ['ばかり', 'とおり', 'ついで'], 'Ever since placing the book borrowed from my friend on the bookshelf, I have been too busy to read even a single page.', '「置いたきり〜ない」で、置いた後の動作が行われていないことを示します。'),
            ('広い会場に残っているのは、片付けを担当する私たち二人（　　　）だった。', 'きり', ['まま', 'がち', 'おき'], 'All who remained in the spacious venue were just the two of us in charge of cleaning up.', '名詞＋「きり」で、「〜だけ（他にはいない）」という限定を表します。'),
        ],
    },
    44: {
        'reading': 'きる',
        'wrong': (
            'おなかいっぱいになったので、お皿の料理を半分だけ残して食べ切った。',
            '「〜切る」は残さず最後まで完全にやり遂げる意味なので、「半分残して」とは矛盾します。',
            '〜切る means finishing something completely to the very end, which contradicts leaving half of the food on the plate.'
        ),
        'comp_ex': [
            '試合の最後の1秒まで力を尽くして戦った選手たちに大きな拍手が送られた。',
            '予定していた今日の作業をすべて終えて、ほっと一息ついた。',
        ],
        'quiz': [
            _q0(44),
            ('夏休みの宿題を8月の前半のうちにすべてやり（　　　）、後半はゆっくり遊んだ。', '切って', ['かけて', 'すぎて', '出して'], 'I finished doing all of my summer vacation homework in the first half of August, and played leisurely in the second half.', '「やり切る」で、宿題を最後まで完全に終わらせたことを表します。'),
            ('長い登山道を5時間かけて登り（　　　）とき、目の前に素晴らしい景色が広がった。', '切った', ['かけた', 'すぎた', '抜いた'], 'When I finished climbing the long mountain trail over five hours, a wonderful view spread out before my eyes.', '「登り切る」で、頂上まで最後まで登り終えることを表します。'),
            ('貯金箱にためた小銭を全部使い（　　　）、欲しかった腕時計を購入した。', '切って', ['かけて', 'すぎて', 'あって'], 'I used up all the coins saved in my piggy bank and purchased the wristwatch I wanted.', '「使い切る」で、残らず最後まで全部使ってしまうことを示します。'),
        ],
    },
    45: {
        'reading': 'っけ',
        'wrong': (
            '本日お配りした資料の1ページ目に、本日の予定が書いてあったっけ。',
            '「〜っけ」は過去に知っていたはずのことを思い出そうとする親しい会話表現なので、改まったスピーチや案内には使えません。',
            '〜っけ is a casual conversational particle used when trying to recall something one once knew, so it is inappropriate in formal announcements.'
        ),
        'comp_ex': [
            '来週の読書会の会場は、図書館の2階の会議室だったっけ？',
            'すみません、明日の打ち合わせは何時からでしたっけ？',
        ],
        'quiz': [
            _q0(45),
            ('あれ、家の鍵をどこに置いた（　　　）？さっきテーブルの上に置いたはずなのに。', 'っけ', ['ものか', 'わけだ', 'べきだ'], 'Huh, where did I put my house key? I am sure I put it on the table just now.', '自分がした行動や記憶を思い出そうとして自問するときに「〜たっけ」を使います。'),
            ('鈴木さんの新しい電話番号、メモしたはずなんだけど何番だった（　　　）？', 'っけ', ['はず', 'こと', 'まま'], 'I am sure I wrote down Suzuki-san’s new phone number, but what number was it again?', '「何番だったっけ？」と記憶が曖昧なことを確かめる会話表現です。'),
            ('今日が提出期限のレポート、もう先生に出した（　　　）？', 'っけ', ['きり', 'がち', 'ぎみ'], 'Did you already hand in the report due today to the teacher?', '親しい相手に過去の事実を確認する「〜たっけ？」の用法です。'),
        ],
    },
    46: {
        'reading': 'こむ',
        'wrong': (
            '部屋の空気を入れ替えるために、窓を広く{開|あ}け込んだ。',
            '「〜込む」は中へ深く入る・徹底的にその動作を続ける意味なので、「窓を{開|あ}ける」のような外へ広げる動作には付きません。',
            '〜込む means moving deeply inside or doing an action intensively, so it does not attach to verbs like 開ける ("open outward").'
        ),
        'comp_ex': [
            '彼は椅子の背もたれに深く腰をかけて、静かに目を閉じた。',
            '子どもたちは時間を忘れて、ブロック遊びにすっかり熱中している。',
        ],
        'quiz': [
            _q0(46),
            ('野菜と肉を弱火で3時間も煮（　　　）ので、とても柔らかくておいしい。', '込んだ', ['上げた', 'かけた', '出した'], 'Because I simmered the vegetables and meat over low heat for three hours, they are very tender and delicious.', '「煮込む」で、時間をかけて中までしっかり味が染みるように煮ることを表します。'),
            ('彼は難しい顔をして何かを深く考え（　　　）いたので、声をかけられなかった。', '込んで', ['切って', 'すぎて', 'あって'], 'Since he was deeply lost in thought with a serious look on his face, I could not call out to him.', '「考え込む」で、ひとつのことを深く長く考え続ける様子を表します。'),
            ('冷たい風が部屋の中に吹き（　　　）きたので、急いで窓を閉めた。', '込んで', ['上げて', '出して', 'かけて'], 'Since cold wind blew into the room, I hurriedly closed the window.', '外から内部へ勢いよく入る動作を「吹き込む」と表します。'),
        ],
    },
    47: {
        'reading': 'こそ',
        'wrong': (
            '今日は雨が降っているこそ、外へ出かけないで家で映画を見よう。',
            '文と文をつないで理由を強調するときは、動詞や形容詞に直接「こそ」は付けられず「雨が降っているからこそ」のように「からこそ」の形にします。',
            'To emphasize a clause as a reason, こそ attaches to から (〜からこそ), not directly to a verb or adjective.'
        ),
        'comp_ex': [
            '雲ひとつない青空が広がり、今日はまさに絶好のハイキング{日和|びより}だ。',
            '今度の試合には絶対に勝って、応援してくれたみんなに恩返しをしたい。',
        ],
        'quiz': [
            _q0(47),
            ('お忙しいところ丁寧にご案内いただき、こちら（　　　）ありがとうございました。', 'こそ', ['さえ', 'ばかり', 'きり'], 'Thank you very much for kindly guiding me despite being busy; I am the one who should thank you.', 'お礼の返答で「こちらこそ」と言い、感謝すべきなのは自分のほうだと強調します。'),
            ('基礎の練習（　　　）が上達への一番の近道だと、コーチはいつも言っている。', 'こそ', ['しか', 'ほど', 'だけ'], 'The coach always says that basic practice itself is the shortest shortcut to improvement.', '「名詞＋こそ（が）」で、他の何よりもそれが重要であると強く取り立てます。'),
            ('何度も失敗して悔しい思いをしたから（　　　）、合格したときの喜びが大きかった。', 'こそ', ['には', 'とて', 'なり'], 'Precisely because I failed many times and felt frustrated, the joy when I passed was all the greater.', '「〜からこそ」で、その理由があって初めて良い結果につながったことを強調します。'),
        ],
    },
    48: {
        'reading': 'ことから',
        'wrong': (
            '明日雨が降ることから、今日の午後のうちに買い物を済ませておこう。',
            '「〜ことから」はすでに起きた事実や根拠から判断・命名が導かれるときに使うため、まだ起きていない未来の予定には「〜ので／から」を使います。',
            '〜ことから introduces an established fact or observation as the basis for a conclusion or name, not a future plan.'
        ),
        'comp_ex': [
            '建物の老朽化が進んでいるという理由から、来春に取り壊されることになった。',
            '昨日の大雨によって川の増水が続き、近くの橋が一時通行止めになった。',
        ],
        'quiz': [
            _q0(48),
            ('玄関に濡れた傘が置いてある（　　　）、外で雨が降り始めたことが分かった。', 'ことから', ['ことには', 'ことにして', 'ことになって'], 'From the fact that a wet umbrella was placed at the entrance, I could tell that it had started raining outside.', '目にした事実（濡れた傘がある）を根拠として判断したことを「〜ことから」で表します。'),
            ('この島は形がハートに似ている（　　　）、恋人たちの聖地と呼ばれている。', 'ことから', ['ところに', 'ばかりに', 'くせに'], 'Because its shape resembles a heart, this island is called a sanctuary for lovers.', '名前の由来や呼ばれ{方|かた}の根拠を示す「〜ことから」の代表的な用法です。'),
            ('ちょっとした言葉の誤解があった（　　　）、二人はしばらく口をきかなくなった。', 'ことから', ['ところで', 'とたんに', 'ついでに'], 'Triggered by a slight misunderstanding of words, the two stopped speaking to each other for a while.', '小さなきっかけが原因で事態が発展したことを表します。'),
        ],
    },
    49: {
        'reading': 'ことになっている',
        'wrong': (
            '私は毎朝健康のために、起きたらすぐコップ一杯の水を飲むことになっている。',
            '自分が個人的に決めた習慣には「〜ことにしている」を使い、規則や社会的な決まりを表す「〜ことになっている」は使えません。',
            'For a personal habit one has decided on oneself, use 〜ことにしている; 〜ことになっている is for external rules, schedules, or agreements.'
        ),
        'comp_ex': [
            'この学生寮では、門限の夜10時までに必ず部屋へ戻る規則だ。',
            '来週の火曜日に、新しいプロジェクトの説明会が{開|ひら}かれる予定だ。',
        ],
        'quiz': [
            _q0(49),
            ('このマンションでは、犬や猫などのペットは飼ってはいけない（　　　）。', 'ことになっている', ['ことにしている', 'ことにする', 'ことになる'], 'In this apartment building, it is a rule that you must not keep pets such as dogs and cats.', '動詞ない形＋「ことになっている」で、禁止のルールや決まりを表します。'),
            ('ゴミは毎週火曜日と金曜日の朝8時までに、指定の場所へ出す（　　　）。', 'ことになっている', ['ことにしている', 'ことである', 'ことがない'], 'Trash is supposed to be put out at the designated place by 8 a.m. every Tuesday and Friday.', '地域のルールや決まり事を説明する表現です。'),
            ('来月、東京で{開|ひら}かれる全国大会に、私たちの学校から代表が2名出場する（　　　）。', 'ことになっている', ['ことにしている', 'ことだった', 'ことはない'], 'Two representatives from our school are scheduled to participate in the national tournament held in Tokyo next month.', 'すでに決まっている今後の予定を「〜ことになっている」で伝えます。'),
        ],
    },
    50: {
        'reading': 'ことは〜が',
        'wrong': (
            'その新しい映画は見たことは見たが、とても感動して最高だった。',
            '「〜ことは〜が」は「一応その事実は認めるが、{十分|じゅうぶん}ではない」という消極的な制限が後ろに続くため、手放しで褒める文脈には合いません。',
            '〜ことは〜が concedes a fact only to add a reservation or limitation in the second clause, so it cannot be followed by unqualified praise.'
        ),
        'comp_ex': [
            'このパソコンは確かに性能は高いが、持ち歩くには少し重すぎる。',
            'レシピ通りに作ったけれども、母が作ってくれる味にはかなわなかった。',
        ],
        'quiz': [
            _q0(50),
            ('説明書を読んだ（　　　）読んだが、専門用語が多くてよく理解できなかった。', 'ことは', ['だけは', 'ほどは', 'きりは'], 'I did read the instruction manual, to be sure, but there were many technical terms and I could not understand it well.', '同じ動詞「読んだ」を繰り返して、読んだ事実を認めつつ理解はできなかったと続けています。'),
            ('この靴は安い（　　　）安いが、底が薄くて長く歩くと足が疲れそうだ。', 'ことは', ['わりには', 'くせには', 'ものには'], 'These shoes are cheap, it is true, but the soles are thin and my feet will likely get tired if I walk for a long time.', '形容詞「安い」を繰り返して「安いことは安いが」と条件付きの肯定を表します。'),
            ('免許を持っている（　　　）持っているけれど、ここ5年ほど一度も運転していない。', 'ことは', ['ばかりは', 'くらいは', 'っぱなしは'], 'I do have a driver’s license, but I haven’t driven even once for about the last five years.', '「持っていることは持っているけれど」で、実際には活用できていない事情を付け加えます。'),
        ],
    },
    51: {
        'reading': 'ことはない',
        'wrong': (
            '私は今まで一度も飛行機に遅れることはない。',
            '過去の経験を否定するときは「遅れたことはない」とた形を使い、辞書形＋「ことはない」は「〜する必要はない」という意味になります。',
            'With the dictionary form, 〜ことはない means "there is no need to ~"; to say "have never done," use the past form 〜たことはない.'
        ),
        'comp_ex': [
            '駅から歩いて5分ほどの場所ですから、わざわざタクシーに乗る必要はないですよ。',
            '明日は休日で学校も休みだから、朝早く起きなくていい。',
        ],
        'quiz': [
            _q0(51),
            ('まだ時間はたっぷりあるから、そんなに慌てて走る（　　　）はないよ。', 'こと', ['もの', 'はず', 'わけ'], 'Since there is still plenty of time, there is no need to run in such a hurry.', '動詞辞書形「走る」＋「ことはない」で、走る必要がないと落ち着かせる表現です。'),
            ('誰でも最初は失敗するのだから、一度のミスで落ち込む（　　　）はありません。', 'こと', ['べき', 'まま', 'きり'], 'Since everyone makes mistakes at first, there is no need to feel depressed over a single mistake.', '相手を励まして「落ち込む必要はない」と伝える用法です。'),
            ('会議の資料ならすでに人数分印刷してありますから、新しくコピーする（　　　）はないですよ。', 'こと', ['とこ', 'たび', 'せい'], 'As for the meeting materials, copies for everyone have already been printed, so there is no need to make new copies.', 'すでに準備が済んでいるため不要であることを伝えています。'),
        ],
    },
    52: {
        'reading': 'こと',
        'wrong': (
            '先生、明日の宿題は何ページまで提出することですか。',
            '文末の「〜こと」は規則や掲示などで一方的に指示・命令を伝える表現なので、目上の人に質問する文には使えません。',
            'Sentence-final 〜こと issues written rules or instructions, so it cannot be used to ask a question to a teacher.'
        ),
        'comp_ex': [
            '体育館を使用する際は、必ず室内用の運動靴に履き替えなければならない。',
            '図書館の本を借りたら、決められた返却期限をきちんと守るべきだ。',
        ],
        'quiz': [
            _q0(52),
            ('レポートは来週の月曜日の正午までに、担当教員へ直接提出する（　　　）。', 'こと', ['もの', 'わけ', 'はず'], 'Reports are to be submitted directly to the instructor in charge by noon next Monday.', '学校の掲示や案内文で「提出すること」と規則・指示を伝える表現です。'),
            ('実験室に入る際は、安全のために必ず白衣と保護眼鏡を着用する（　　　）。', 'こと', ['きり', 'まま', 'ばかり'], 'When entering the laboratory, be sure to wear a lab coat and protective glasses for safety.', '注意事項の箇条書きなどで使われる命令・指示の「〜こと」です。'),
            ('寮の廊下や共用スペースでは、夜10時以降に大声で話さない（　　　）。', 'こと', ['べき', 'はず', 'わけ'], 'Do not speak loudly after 10 p.m. in the dormitory hallways or common spaces.', '動詞ない形＋「こと」で、「〜してはいけない」という禁止の規則を表します。'),
        ],
    },
    53: {
        'reading': 'くらい・ぐらい',
        'wrong': (
            '彼は料理のプロだから、難しいフランス料理くらいしか作れない。',
            '「〜くらい」で軽い程度を表す場合、「プロだから難しい料理くらい簡単に作れる」とは言えますが、「プロなのにそれしか作れない」は文脈が矛盾します。',
            'Using くらい to trivialize something requires a matching context; saying a professional "can only make difficult French cuisine" is contradictory.'
        ),
        'comp_ex': [
            '昨日は立っていられないほど強い風が吹いて、電車のダイヤが乱れた。',
            'ただの冗談だったのに、彼は泣き出さんばかりに悔しがっていた。',
        ],
        'quiz': [
            _q0(53),
            ('急に予定が変わるなら、電話で一言連絡する（　　　）のことはしてほしかった。', 'くらい', ['あまり', 'どころ', 'とたん'], 'If your plans were going to change suddenly, I wished you had at least called to say a word.', '最低限のマナーとして「せめて連絡するくらいのことは」と不満を述べる表現です。'),
            ('お湯を注ぐだけなのだから、カップ麺（　　　）私にだって作れますよ。', 'くらい', ['ばかり', 'とおり', 'ながら'], 'Since you just pour hot water, even I can make at least cup noodles.', '簡単なことの一例として「カップ麺くらい」と軽く取り上げています。'),
            ('足の裏にマメができて、靴を履くのも痛い（　　　）だった。', 'くらい', ['くせに', 'わりに', 'かわり'], 'I got a blister on the sole of my foot, and it hurt so much that even putting on shoes was painful.', '痛みの程度がどれほどかを「靴を履くのも痛いくらい」と表しています。'),
        ],
    },
    54: {
        'reading': 'くせに',
        'wrong': (
            '田中先生はお忙しいくせに、いつも丁寧に質問に答えてくださいます。',
            '「〜くせに」は相手を見下したり非難する強いマイナス感情を含むため、目上の人への感謝や敬意を表す文には絶対に使えません。',
            '〜くせに carries a strong tone of criticism or contempt, so it must never be used when praising or speaking respectfully of a superior.'
        ),
        'comp_ex': [
            'せっかく早起きして出かけたのに、お目当ての店は休みの{日|ひ}だった。',
            '激しい雨が降っているにもかかわらず、大勢のファンが会場の前に並んでいた。',
        ],
        'quiz': [
            _q0(54),
            ('彼はいつも「すぐやる」と言う（　　　）、締め切りを守ったことが一度もない。', 'くせに', ['おかげで', 'あまりに', 'とたんに'], 'Even though he always says "I’ll do it right away," he has never once kept a deadline.', '言っていることと実際の行動が矛盾していることを「言うくせに」と批判しています。'),
            ('本当は甘いものが大好きな（　　　）、彼はみんなの前では食べないふりをしている。', 'くせに', ['せいで', 'たびに', 'うちに'], 'Even though he actually loves sweets, he pretends not to eat them in front of everyone.', 'な形容詞＋な＋「くせに」で、事実と異なる態度への皮肉や軽い非難を表します。'),
            ('漢字が読めない（　　　）、小学生の弟は難しい大人の本を読みたがる。', 'くせに', ['わりに', 'とおり', 'ついで'], 'Even though he can’t read the kanji, my elementary-school younger brother wants to read difficult adult books.', '親しい身内に対して「読めないのに背伸びをしている」とからかうニュアンスで使っています。'),
        ],
    },
    55: {
        'reading': 'まるで',
        'wrong': (
            'この写真は本物の風景を撮ったので、まるで本物の風景だ。',
            '「まるで〜ようだ」は実際は違うものを別の何かにたとえる比喩表現なので、本物をそのまま本物と言うときには使えません。',
            'まるで is used for similes and metaphors (comparing something to what it is not), so it cannot describe something literally being itself.'
        ),
        'comp_ex': [
            '彼女はあたかも自分一人で仕事をやり遂げたかのように話していた。',
            '満開の桜並木の下を歩いていると、ちょうどピンク色のトンネルをくぐっているかのようだ。',
        ],
        'quiz': [
            _q0(55),
            ('4月なのに朝から雪が降って、（　　　）真冬に逆戻りしたような寒さだ。', 'まるで', ['決して', 'めったに', 'べつに'], 'Even though it is April, it has been snowing since morning, and it is cold as if we had gone back to midwinter.', '実際は春なのに真冬のように寒いことを「まるで〜ようだ」でたとえています。'),
            ('久しぶりに再会した彼女は、（　　　）別人のように大人っぽくなっていた。', 'まるで', ['ちっとも', 'かならず', 'せめて'], 'When I reunited with her after a long time, she had grown mature just like a completely different person.', '「まるで別人のように」で、変化の大きさを比喩的に強調します。'),
            ('彼はテストの結果が悪かったというのに、（　　　）気にしていない様子で笑っている。', 'まるで', ['まさか', 'もしも', 'たいてい'], 'Even though his test results were poor, he is laughing looking as if he doesn’t care at all.', '「まるで＋否定（気にしていない）」で、「全く〜ない」という意味も表します。'),
        ],
    },
    56: {
        'reading': 'まさか',
        'wrong': (
            '毎日一生懸命勉強していたから、まさか合格するとは思っていた。',
            '「まさか」は予想もしなかった意外な事態や強い否定（「〜とは思わなかった」「〜はずがない」）と結びつくため、予想通りの肯定文には使えません。',
            'まさか expresses disbelief at an unexpected turn of events and pairs with negative/doubtful endings, not expected affirmative outcomes.'
        ),
        'comp_ex': [
            'あんなに元気だった彼が、よもや入院することになるとは夢にも思わなかった。',
            'こんな短い期間でこれほど大きな建物を完成させるとは、とても人間の技とは思えない。',
        ],
        'quiz': [
            _q0(56),
            ('軽い気持ちで応募した写真コンテストで、（　　　）自分の作品が1等に選ばれるとは思わなかった。', 'まさか', ['かならず', 'たいてい', 'せっかく'], 'I never thought that my work would by any chance be chosen for first prize in the photo contest I entered casually.', '「まさか〜とは思わなかった」で、全く予想していなかった驚きを表します。'),
            ('今はこんなに晴れているのだから、（　　　）午後から雪が降るなんてことはないだろう。', 'まさか', ['めったに', 'ちっとも', 'べつに'], 'Since it is this sunny right now, there is no way it could possibly snow in the afternoon.', '「まさか〜ないだろう」で、「そんなことは起こらないはずだ」という強い推測を表します。'),
            ('冗談で言っただけなのに、（　　　）彼が本当に信じるとは夢にも思わなかった。', 'まさか', ['せめて', 'まるで', 'とうとう'], 'I only said it as a joke, and I never dreamed that he would actually believe it.', '予想外の反応に対する驚きを強調する用法です。'),
        ],
    },
    57: {
        'reading': 'めったに〜ない',
        'wrong': (
            '私は健康のために、毎朝めったに公園を散歩している。',
            '「めったに」は必ず後ろに否定形（〜ない）を伴って「ほとんど〜ない」という低い頻度を表すため、肯定文には使えません。',
            'めったに must always be followed by a negative verb or adjective to mean "seldom / rarely," and cannot be used affirmatively.'
        ),
        'comp_ex': [
            '普段は自転車で通勤しているので、平日にバスに乗ることはほとんどない。',
            'この珍しい高山植物は、標高の高い岩場でまれにしか見ることができない。',
        ],
        'quiz': [
            _q0(57),
            ('普段は自炊をしているので、平日の夜にレストランで外食することは（　　　）ない。', 'めったに', ['決して', 'まさか', 'きっと'], 'Since I usually cook for myself, I seldom eat out at restaurants on weekday evenings.', '「めったに〜ない」で、回数や頻度が非常に少ないことを表します。'),
            ('これほど保存状態が良い古い絵画は、美術館でも（　　　）見られない貴重なものだ。', 'めったに', ['せっかく', 'せめて', 'たいてい'], 'An old painting in such good condition is something precious that can rarely be seen even in art museums.', '機会が極めて少ないことを「めったに見られない」と表現します。'),
            ('いつも穏やかな父は、私たちが小さな失敗をしても（　　　）怒らない。', 'めったに', ['まるで', 'もしも', 'とうとう'], 'My father, who is always calm, rarely gets angry even when we make small mistakes.', '怒る頻度が極めて低いことを表します。'),
        ],
    },
    58: {
        'reading': 'も〜ば〜も',
        'wrong': (
            'この店は料理もおいしければ、店員の態度も悪くて残念だ。',
            '「〜も〜ば〜も」は良い点同士、または悪い点同士を並べて強調する表現なので、長所と短所を対比するときには使いません。',
            '〜も〜ば〜も lists two parallel qualities (both positive or both negative), so it is not used to contrast a merit with a demerit.'
        ),
        'comp_ex': [
            '彼女はピアノも弾けるし歌も上手なので、音楽の先生に向いている。',
            'この旅館は温泉の質が良いだけでなく、地元の食材を使った料理も素晴らしい。',
        ],
        'quiz': [
            _q0(58),
            ('新しく入った新入社員は、英語も話せれ（　　　）プログラミングの知識も豊富だ。', 'ば', ['と', 'たら', 'なら'], 'The new employee who just joined can both speak English and has abundant knowledge of programming.', '「英語も話せれば〜知識も豊富だ」で、二つの優れた能力を並べて評価しています。'),
            ('お祭りの会場には、地元の子どもたちもいれ（　　　）遠くから来た観光客もたくさんいた。', 'ば', ['ても', 'のに', 'から'], 'At the festival venue, there were both local children and many tourists who came from afar.', '「AもいればBもいる」で、いろいろな人が同時に存在することを表します。'),
            ('この靴はデザインも良けれ（　　　）、軽くて履き心地も抜群だ。', 'ば', ['ど', 'と', 'たら'], 'These shoes not only have a good design, but are also light and extraordinarily comfortable to wear.', 'い形容詞の条件形「良ければ」を使って二つの長所を並列しています。'),
        ],
    },
    59: {
        'reading': 'もしかしたら',
        'wrong': (
            'さっき合格通知の手紙が届いたので、もしかしたら試験に合格したに違いない。',
            '「もしかしたら」は確信が低い推測（「〜かもしれない」）と呼応するため、すでに確定した事実や「〜に違いない」とは合いません。',
            'もしかしたら expresses a tentative possibility ("perhaps / maybe") and pairs with 〜かもしれない, not with certainty (〜に違いない).'
        ),
        'comp_ex': [
            '時間になっても田中さんが来ないけれど、もしかすると電車の遅延に巻き込まれたのかもしれない。',
            '引き出しの奥を探せば、ひょっとしたら昔の写真が見つかるかもしれないよ。',
        ],
        'quiz': [
            _q0(59),
            ('何度インターホンを押しても返事がないから、（　　　）留守なのかもしれない。', 'もしかしたら', ['かならず', 'けっして', 'めったに'], 'Since there is no answer no matter how many times I press the intercom, perhaps they are away from home.', '「もしかしたら〜かもしれない」で、確証はないがあり得る可能性を推測します。'),
            ('カバンの中に財布が見当たらない。（　　　）さっきの店に置き忘れたかもしれない。', 'もしかしたら', ['せっかく', 'せめて', 'ちっとも'], 'I can’t find my wallet in my bag. Perhaps I left it behind at the shop just now.', '不確かな記憶をもとに「ひょっとすると〜かもしれない」と心配する場面です。'),
            ('彼は今日とても嬉しそうにしているから、（　　　）何か良い知らせがあったのだろうか。', 'もしかしたら', ['どうしても', 'べつに', 'たいてい'], 'He looks very happy today, so could it be that he received some good news?', '疑問文「〜のだろうか」とも呼応して推測を表します。'),
        ],
    },
    60: {
        'reading': 'もしも〜たら',
        'wrong': (
            'もしもさっき昼ご飯を食べたら、今はお腹がいっぱいだ。',
            'すでに終わった過去の事実には「もしも〜たら」という仮定は使えません。これから起こりうることや事実に反する想像に使います。',
            'もしも〜たら is for hypothetical future conditions or counterfactual imagination, not for already completed real events.'
        ),
        'comp_ex': [
            '万一会場で迷子になった場合は、正面入り口の案内所へ来てください。',
            '仮に計画が途中で変更になったとしても、すぐに対応できるように準備しておこう。',
        ],
        'quiz': [
            _q0(60),
            ('（　　　）タイムマシンに乗って過去へ戻れたら、子どもの頃の自分に会ってみたい。', 'もしも', ['まるで', 'まさか', 'めったに'], 'If by any chance I could ride a time machine and go back to the past, I would like to meet my childhood self.', '現実にはあり得ない空想の仮定を「もしも〜たら」で導いています。'),
            ('（　　　）当日になって雨が降ったら、運動会は翌週の日曜日に延期されます。', 'もしも', ['せっかく', 'せめて', 'かならず'], 'If it should rain on the day of the event, the sports day will be postponed to the following Sunday.', '起こるかどうかわからない未来の条件を仮定する表現です。'),
            ('（　　　）途中で道が分からなくなったら、遠慮なく私の携帯電話に連絡してください。', 'もしも', ['ちっとも', 'べつに', 'たいてい'], 'If by any chance you lose your way halfway through, please do not hesitate to call my mobile phone.', '万が一の状況を想定してアドバイスする文脈です。'),
        ],
    },
}



