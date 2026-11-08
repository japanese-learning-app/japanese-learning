# -*- coding: utf-8 -*-
"""
N1 grammar data part A (gids 1-42).
"""

DATA = {
    1: {
        'formula': '名詞 ＋ <strong>を皮切りに（して）</strong> ／ <strong>を皮切りとして</strong>',
        'similar': '〜を手始めに / 〜を始まりとして / 〜をきっかけに',
        'wrong': (
            '今朝の散歩を皮切りに、私はいつも通り会社へ出勤した。',
            '「〜を皮切りに」は、ある出来事を最初のきっかけとして、同種の活動や催しが次々と連鎖的に広がる場合に使います。単なる日常の順序には使えません。',
            '"〜を皮切りに" is used when an initial event triggers a series of similar events or activities expanding one after another, not for routine daily sequences.'
        ),
        'comp': (
            '〜を契機に',
            'triggered by; taking ~ as a turning point',
            '「〜を契機に」は一つの出来事を転機として大きな変化が生じることに重点があり、「〜を皮切りに」は同種の出来事が次々と続く連鎖性に重点があります。',
            'While 〜を契機に focuses on a major turning point, 〜を皮切りに emphasizes a chain of similar events following the first one.',
            '海外赴任を契機に、彼は異文化理解に関する研究を本格的に始めた。',
        ),
        'quiz': [
            (
                '東京での公演（　　　）、その劇団は全国十か所の劇場で巡回公演を行った。',
                'を皮切りに',
                ['をよそに', 'を限りに', 'を抜きにして'],
                'Starting with the performance in Tokyo, the theater troupe held a touring performance at ten theaters nationwide.',
                '最初の公演を出発点として、同じような公演が各地で次々と行われることを表します。'
            ),
            (
                '駅前の大型書店の開店（　　　）、周辺には新しい商業施設が次々と建設された。',
                'を皮切りとして',
                ['をものともせず', 'を差し置いて', 'を頼りに'],
                'Starting with the opening of the large bookstore in front of the station, new commercial facilities were built one after another in the surrounding area.',
                '一つの店舗の誕生をきっかけに、同種の開発が連鎖的に広がる様子を示します。'
            ),
            (
                '春の新作発表会（　　　）、今年は各地で伝統工芸の展示イベントが相次いで開催される。',
                'を皮切りに',
                ['を尻目に', 'を押して', 'を問わず'],
                'Starting with the spring new collection presentation, traditional craft exhibition events will be held one after another in various regions this year.',
                '「相次いで」「次々と」など、連続して展開することを表す語句とよく呼応します。'
            ),
            (
                '本店での記念セール（　　　）、来週から全国の支店で一斉に感謝祭が始まる予定だ。',
                'を皮切りにして',
                ['をよそにして', 'を境目にして', 'をめぐって'],
                'Starting with the commemorative sale at the main store, appreciation festivals are scheduled to begin simultaneously at branches nationwide next week.',
                '最初の企画を手始めとして、同様の催しが全国へ展開していく流れを表します。'
            ),
        ],
    },
    2: {
        'formula': '名詞 ＋ <strong>であれ</strong> ／ <strong>であれ</strong> ＋ 名詞 ＋ <strong>であれ</strong>',
        'similar': '〜であろうと / 〜にせよ / 〜にしても',
        'wrong': (
            '雨が降るであれ、明日の野外音楽祭は予定通り開催されます。',
            '「〜であれ」は名詞または「疑問詞＋であれ」の形で接続します。動詞の辞書形に直接つなげることはできません。',
            '"〜であれ" attaches to nouns or question-word phrases; it cannot directly follow a verb in dictionary form.'
        ),
        'comp': (
            '〜とはいえ',
            'although; even though (acknowledging a fact)',
            '「〜とはいえ」は既にある事実を認めた上で逆接を述べますが、「〜であれ」は仮定や例示を挙げて「いかなる場合でも例外なく」と強調します。',
            'While 〜とはいえ concedes an actual fact, 〜であれ presents hypothetical examples or extremes to mean "no matter what/who, without exception."',
            '春になったとはいえ、朝晩はまだ冷え込むので上着が手放せない。',
        ),
        'quiz': [
            (
                'いかなる理由（　　　）、図書館の貴重な資料を無断で持ち出すことは許されない。',
                'であれ',
                ['なりとも', 'ならでは', 'ずくめ'],
                'Whatever the reason may be, taking valuable library materials out without permission is not permitted.',
                '「いかなる＋名詞＋であれ」で「どのような理由であっても例外なく」と強く述べる表現です。'
            ),
            (
                'ベテランであれ新人（　　　）、舞台に立つ以上は最高の演奏を届ける責任がある。',
                'であれ',
                ['ごとき', 'まみれ', 'めいて'],
                'Whether a veteran or a newcomer, as long as one stands on stage, one has a responsibility to deliver the best performance.',
                '対照的な二つの名詞を「AであれBであれ」と並べて「どちらの場合であっても同じだ」と述べる用法です。'
            ),
            (
                'たとえ小さな部品一つ（　　　）、品質検査の手順を省略することは一切認められない。',
                'であれ',
                ['ばかりに', 'に先駆けて', 'にかまけて'],
                'Even if it is just a single small part, skipping quality inspection procedures is not permitted at all.',
                '「たとえ〜であれ」の形で、極端な例を挙げて基準の厳格さを示します。'
            ),
            (
                '誰の作品（　　　）、今回の美術コンクールでは名前を伏せて公平に審査が行われる。',
                'であれ',
                ['ゆえに', 'とあっては', 'にかこつけて'],
                'Regardless of whose work it is, judging in this art competition will be conducted fairly with names concealed.',
                '疑問詞を含む名詞句について「誰のものであっても関係なく」という意味を表します。'
            ),
        ],
    },
    3: {
        'formula': 'ナ形容詞語幹・イ形容詞 ＋ <strong>極まりない</strong> ／ 名詞（失礼・迷惑など） ＋ <strong>極まりない</strong>',
        'similar': '〜極まる / 〜この上ない / 非常に〜だ',
        'wrong': (
            '彼の新居は駅から歩いて{三分|さんぷん}という便利極まりない場所にある。',
            '「〜極まりない」は「失礼・危険・不愉快・退屈」など、主に話し手が否定的に捉える感情や状態を強く批判・強調するときに使われます。',
            '"〜極まりない" is predominantly used with negative adjectives like rude, dangerous, or unpleasant to express strong criticism or exasperation.'
        ),
        'comp': (
            '〜この上ない',
            'supreme; nothing could be more ~',
            '「〜この上ない」は「光栄この上ない」「幸せこの上ない」のように肯定的な感謝や喜びにも広く使われる点が異なります。',
            'Unlike 〜極まりない (mostly negative), 〜この上ない is frequently used in positive contexts such as supreme honor or happiness.',
            '長年の研究が評価され、このような賞をいただけるのは光栄この{上|うえ}ないことです。',
        ),
        'quiz': [
            (
                '確認もせずに不確かな噂を広めるのは、当事者にとって迷惑（　　　）行為だ。',
                '極まりない',
                ['まじき', 'ずくめの', 'ならではの'],
                'Spreading unverified rumors without checking is an extremely troublesome act for the people involved.',
                '「迷惑」「失礼」「不快」などのナ形容詞につき、程度が甚だしいことを強く非難します。'
            ),
            (
                '整備されていない夜間の山道を懐中電灯なしで歩くのは、危険（　　　）ことだ。',
                '極まりない',
                ['ごとき', 'まみれの', 'あっての'],
                'Walking along an unmaintained mountain path at night without a flashlight is an extremely dangerous thing to do.',
                'これ以上ないほど危険であるという強い警告のニュアンスを含みます。'
            ),
            (
                '相手の事情も聞かずに一方的に約束を破棄するとは、無責任（　　　）態度である。',
                '極まりない',
                ['たるもの', 'に先駆けた', 'を踏まえた'],
                'Unilaterally breaking a promise without even hearing the other party\'s circumstances is an utterly irresponsible attitude.',
                '相手の態度や振る舞いに対する強い憤りを表す硬い表現です。'
            ),
            (
                '根拠のない憶測で他人の努力を軽視するような発言は、不愉快（　　　）ものだ。',
                '極まりない',
                ['ともなると', 'といえども', 'とばかりに'],
                'Remarks that belittle others\' efforts based on groundless speculation are boundlessly unpleasant.',
                'マイナスの評価を表す語に添えて、感情の高まりを強調します。'
            ),
        ],
    },
    4: {
        'formula': '感情を表す名詞 ＋ <strong>を禁じ得ない</strong>',
        'similar': '〜ずにはいられない / 〜てやまない / 〜を抑えられない',
        'wrong': (
            'あまりのおいしさに、私はもう一つケーキを食べることを禁じ得なかった。',
            '「〜を禁じ得ない」は「同情・驚き・涙・憤り」など自然に湧き上がる感情や涙を抑えられないという意味であり、具体的な行動には使えません。',
            '"〜を禁じ得ない" is used with nouns of emotion or tears that well up involuntarily, not with deliberate physical actions like eating cake.'
        ),
        'comp': (
            '〜ずにはいられない',
            'cannot help doing ~',
            '「〜ずにはいられない」は動詞について行動や感情の両方に使えますが、「〜を禁じ得ない」は感情名詞をとる格調高い書き言葉です。',
            'While 〜ずにはいられない attaches to verbs for both actions and feelings, 〜を禁じ得ない takes emotion nouns in formal written style.',
            'その職人技の精巧さを目の当たりにして、感嘆の声を上げずにはいられなかった。',
        ),
        'quiz': [
            (
                '長年の苦労が報われて舞台で輝く彼女の姿に、深い感動（　　　）。',
                'を禁じ得ない',
                ['を皮切りにする', 'を契機とする', 'をよそにする'],
                'Seeing her shine on stage after years of hard work paid off, I cannot help feeling deeply moved.',
                '「感動」「涙」「同情」などの名詞を受け、胸にこみ上げる思いを抑えられないことを示します。'
            ),
            (
                '歴史ある美しい町並みが失われていく現状には、惜別の念（　　　）。',
                'を禁じ得ない',
                ['をものともしない', 'を抜きにしない', 'を頼りにする'],
                'Facing the current situation where the historic and beautiful townscape is being lost, one cannot suppress a feeling of regretful parting.',
                '「〜の念を禁じ得ない」は評論文や声明文で頻出する代表的な形です。'
            ),
            (
                '誠実に働いてきた人々が不利益を被るような制度には、強い疑問（　　　）。',
                'を禁じ得ない',
                ['を踏まえている', 'に先駆けている', 'にかまけている'],
                'One cannot help feeling strong doubt toward a system in which people who have worked honestly suffer disadvantages.',
                '納得しがたい事態に対して、疑問や憤りの感情が自然に湧くことを表します。'
            ),
            (
                'どれほど厳しい環境でも笑顔を絶やさない彼の姿勢には、敬意（　　　）。',
                'を禁じ得ない',
                ['にかこつける', 'と相まっている', 'にいたっては'],
                'One cannot help feeling respect for his attitude of never losing his smile no matter how harsh the environment.',
                '相手の立派な振る舞いに対して、自然と敬意が湧き上がる文脈で用いられます。'
            ),
        ],
    },
    5: {
        'formula': '名詞 ＋ <strong>に至っては</strong>',
        'similar': '〜になると / 〜ともなると / 〜に関しては（極端な例）',
        'wrong': (
            '兄は料理が得意で、弟に至っては毎日元気に学校へ通っている。',
            '「〜に至っては」は前の文脈と同種の事柄の中で、最も極端な例を取り上げて述べる表現です。無関係な話題を並べることはできません。',
            '"〜に至っては" singles out the most extreme case within the same topic introduced earlier; it cannot connect unrelated topics.'
        ),
        'comp': (
            '〜ともなると',
            'once it reaches the level/stage of ~',
            '「〜ともなると」はある段階や立場に達したときの一般的な変化を述べますが、「〜に至っては」は極端な一例を取り上げて呆れや驚きを示します。',
            'While 〜ともなると describes what naturally happens at a certain level, 〜に至っては highlights an extreme individual case, often with amazement.',
            '標高三千メートルともなると、夏でも肌寒く感じることが多い。',
        ),
        'quiz': [
            (
                '今年の夏は全国的に猛暑が続き、南部の地域（　　　）連日三十八度を超えている。',
                'に至っては',
                ['を皮切りに', 'に先駆けて', 'を踏まえて'],
                'This summer, intense heat has continued nationwide, and when it comes to the southern region, temperatures have exceeded 38 degrees every single day.',
                '全体の傾向を述べた後で、特に極端な例を取り上げて強調する用法です。'
            ),
            (
                '部員たちは皆練習に熱心だが、主将の彼（　　　）毎朝五時から自主練習を続けている。',
                'に至っては',
                ['を契機に', 'と相まって', 'にかこつけて'],
                'All the club members are enthusiastic about practice, and when it comes to him, the captain, he continues voluntary practice from five every morning.',
                '周囲と比べても群を抜いている極端な事例を提示するときに使われます。'
            ),
            (
                '新しい software の操作は難しく、高齢の父（　　　）電源の入れ{方|かた}さえ分からず困っている。'.replace('software ', '機器'),
                'に至っては',
                ['ならでは', 'ゆえに', 'ずくめで'],
                'Operating the new device is difficult, and in my elderly father\'s case, he is troubled because he does not even know how to turn on the power.',
                '否定的な状況の中で、最も程度が甚だしい例を挙げる典型的な文脈です。'
            ),
            (
                '連休中はどの観光地も混雑していたが、有名な展望台（　　　）入場まで三時間も待たされた。',
                'に至っては',
                ['なくして', 'なしに', 'ごときで'],
                'Every tourist spot was crowded during the holidays, and as for the famous observation deck, people had to wait three hours just to enter.',
                '「どこも混雑していた」という前提から、最も極端だった場所を特筆しています。'
            ),
        ],
    },
    6: {
        'formula': '動詞辞書形（する → するまじき／すまじき） ＋ <strong>まじき</strong> ＋ 名詞',
        'similar': '〜てはならない / 許されない / あってはならない',
        'wrong': (
            '今日は雨が降りまじき天気だから、傘を持って出かけた{方|ほう}がいい。',
            '「〜まじき」は社会的立場や職業倫理に照らして「決して許されない行為・態度」を強く非難する表現であり、天候の予想には使えません。',
            '"〜まじき" condemns an unpardonable act given someone\'s social or professional position; it cannot express weather predictions.'
        ),
        'comp': (
            '〜べからざる',
            'that must not be done; impermissible',
            'どちらも文語的な禁止・非難ですが、「〜まじき」は「教育者にあるまじき行為」のように特定の立場・身分にふさわしくない点を強調します。',
            'Both are literary expressions of prohibition, but 〜まじき specifically emphasizes that an act is beneath or unbefitting a certain role or status.',
            '顧客の個人情報を外部に漏らすなど、社会人にあるまじき失態だ。',
        ),
        'quiz': [
            (
                '依頼人の秘密を漏らすなど、専門職としてある（　　　）行為であり到底許されない。',
                'まじき',
                ['ごとき', 'ばかりの', 'めいた'],
                'Leaking a client\'s secrets is an unpardonable act for a professional and cannot possibly be forgiven.',
                '「〜としてあるまじき行為」は、その職業や立場として絶対にあってはならないことを表す定型表現です。'
            ),
            (
                '安全確認を怠ったまま列車を運行するとは、責任者にある（　　　）重大な過失である。',
                'まじき',
                ['ならではの', 'ずくめの', 'まみれの'],
                'Operating a train while neglecting safety checks is a grave fault unbefitting a person in charge.',
                '立場に伴う責任に反する振る舞いを厳しく批判する文脈で用いられます。'
            ),
            (
                '公の{場|ば}で事実無根の噂を言いふらすのは、指導者として許す（　　　）言動だ。',
                'まじき',
                ['極まりない', 'に先駆けた', 'を踏まえた'],
                'Spreading groundless rumors in public is unforgivable conduct for a leader.',
                '「あるまじき」「許すまじき」のように、限られた動詞の辞書形に接続して名詞を修飾します。'
            ),
            (
                '審判の判定に腹を立てて道具を投げつけるなど、一流選手にある（　　　）振る舞いだ。',
                'まじき',
                ['ともなると', 'とあっては', 'といえども'],
                'Throwing equipment in anger at a referee\'s call is behavior unbecoming of a top-class athlete.',
                '社会的な模範となるべき人物の好ましくない行動を戒める表現です。'
            ),
        ],
    },
    7: {
        'formula': '名詞・動詞普通形 ＋ <strong>ごとき</strong> ＋ 名詞 ／ <strong>ごとく</strong> ＋ 動詞・形容詞',
        'similar': '〜のような / 〜みたいに / 〜などの（軽視・謙遜）',
        'wrong': (
            '先生ごときお{方|かた}に私たちの研究をご指導いただけて、大変光栄に存じます。',
            '人物に「〜ごとき」をつけると「〜のような価値の低い者」という強い軽視や、自分に対する謙遜になるため、目上の人への敬意表現には使えません。',
            'Attached to a person, "〜ごとき" expresses either disdain ("someone of such low standing") or self-deprecation, never respect toward a superior.'
        ),
        'comp': (
            '〜たるもの',
            'one who holds the status of ~',
            '「〜たるもの」は高い立場や資格を持つ者の誇り・義務を述べますが、「人物＋ごとき」は能力や立場が低いこと（謙遜または軽視）を表します。',
            'While 〜たるもの highlights the duty of someone in a high position, person + ごとき indicates low status (either humble self-reference or disdain).',
            '私ごとき未熟者にこのような大役が務まるか不安ですが、精一杯努力いたします。',
        ),
        'quiz': [
            (
                '私（　　　）経験の浅い者が、このような伝統ある賞をいただき恐縮しております。',
                'ごとき',
                ['たるもの', 'ならでは', 'ずくめ'],
                'I am humbled that someone as inexperienced as myself has received such a prestigious award.',
                '自分自身につけて「私のような未熟な人間が」とへりくだる謙遜の用法です。'
            ),
            (
                'ほんの数回練習しただけの素人（　　　）に、熟練の職人の技が真似できるはずがない。',
                'ごとき',
                ['極まりない', 'まじき', 'あっての'],
                'There is no way a mere amateur who has only practiced a few times could imitate the skill of a master craftsman.',
                '相手や対象を「その程度のもの」と軽く見るニュアンスを含みます。'
            ),
            (
                '春の嵐が過ぎ去った翌朝、何事もなかったかの（　　　）澄み渡った青空が広がっていた。',
                'ごとく',
                ['ごとき', 'まみれ', 'なりに'],
                'The morning after the spring storm passed, a clear blue sky spread out as if nothing had happened.',
                '連用形「〜ごとく」は動詞や形容詞を修飾し、「〜のように」という比況を表します。'
            ),
            (
                '光陰矢の（　　　）という言葉の通り、大学に入学してからの四年間はあっという間だった。',
                'ごとし',
                ['まじき', 'ずくめ', 'ぶる'],
                'Just as the saying "time flies like an arrow" goes, the four years since entering university passed in the blink of an eye.',
                'ことわざや慣用表現の中で「〜のようである」と文を結ぶ古典的な形です。'
            ),
        ],
    },
    8: {
        'formula': '名詞 ＋ <strong>ずくめ</strong>（の ＋ 名詞 ／ だ）',
        'similar': '〜ばかり / 〜だらけ / すべて〜で満ちている',
        'wrong': (
            '昨日の登山の帰りは急な雨に降られて、靴も服も泥ずくめになってしまった。',
            '「〜ずくめ」は「黒ずくめ」「いいことずくめ」「ごちそうずくめ」など、色や好ましい事柄・習慣的な名詞に限って使われ、汚れの付着には「まみれ」を使います。',
            '"〜ずくめ" is used with colors (all in black) or favorable/abstract things (full of good things), whereas physical dirt or mud requires "〜まみれ".'
        ),
        'comp': (
            '〜まみれ',
            'covered in; smeared with (dirt, sweat, dust)',
            '「〜まみれ」は泥・汗・ほこりなど好ましくない物質が表面に付着する状態を表し、「〜ずくめ」は全体がそれ一色で統一されている状態を表します。',
            'While 〜まみれ describes unpleasant physical substances sticking to a surface, 〜ずくめ describes something consisting entirely of one color or good fortune.',
            '子どもたちは夕暮れまで校庭でボールを追いかけ、汗まみれになって帰ってきた。',
        ),
        'quiz': [
            (
                '今月は昇進が決まった{上|うえ}に懸賞にも当たり、まさにいいこと（　　　）の毎日だ。',
                'ずくめ',
                ['まみれ', 'まじき', 'ごとき'],
                'This month, on top of my promotion being decided, I also won a prize draw; it is truly nothing but good things every day.',
                '「いいことずくめ」「結構ずくめ」のように、好ましいことが重なる状態によく使われます。'
            ),
            (
                '舞台の袖から、帽子から靴まで全身黒（　　　）の衣装を着た演奏者が現れた。',
                'ずくめ',
                ['まみれ', 'ならでは', '極まりない'],
                'From the wings of the stage appeared a performer dressed entirely in black from hat to shoes.',
                '「黒ずくめ」「白ずくめ」など、服装が同じ色で統一されていることを表す代表的な表現です。'
            ),
            (
                '老舗旅館での夕食は、地元の新鮮な海の幸を使ったごちそう（　　　）で感激した。',
                'ずくめ',
                ['まみれ', 'にかまけて', 'はおろか'],
                'Dinner at the long-established inn was full of sumptuous dishes made with fresh local seafood, which deeply impressed us.',
                '最初から最後まで豪華な料理ばかりが並ぶ贅沢な様子を表します。'
            ),
            (
                '祖父母の家を訪問すると、いつも手厚い歓迎と心のこもったおもてなし（　　　）だ。',
                'ずくめ',
                ['まみれ', 'まじき', 'ぶる'],
                'Whenever I visit my grandparents\' house, it is always nothing but warm welcome and heartfelt hospitality.',
                '好ましい待遇や歓迎が最初から最後まで続くことを表します。'
            ),
        ],
    },
    9: {
        'formula': '名詞（汗・泥・ほこり・油など） ＋ <strong>まみれ</strong>（の ＋ 名詞 ／ になる）',
        'similar': '〜だらけ / 〜に塗れて / 一面に〜がついた',
        'wrong': (
            '休日の遊園地は家族連れや観光客まみれで、どの乗り物も長蛇の列だった。',
            '「〜まみれ」は汗・泥・砂・油など、液体や粉状の好ましくないものが表面全体に付着している状態を表すため、人や物の混雑には使えません。',
            '"〜まみれ" describes liquids, powder, or grime sticking all over a surface, so it cannot be used for crowds of people.'
        ),
        'comp': (
            '〜だらけ',
            'full of; riddled with (mistakes, scratches, mud)',
            '「〜だらけ」は「間違いだらけ」「傷だらけ」など数えられる欠点や散乱した物にも広く使えますが、「〜まみれ」は表面にべったり付着する物に限定されます。',
            'While 〜だらけ works broadly with countable flaws (mistakes, scratches), 〜まみれ is restricted to substances coating or clinging to a surface.',
            '最初に書いた下書きは誤字だらけだったので、最初から丁寧に書き直した。',
        ),
        'quiz': [
            (
                '大雨の{中|なか}で行われたサッカーの試合で、選手たちはユニフォームが泥（　　　）になった。',
                'まみれ',
                ['ずくめ', 'ならでは', 'ごとき'],
                'In the soccer match held in heavy rain, the players\' uniforms became covered in mud.',
                '「泥まみれ」は泥が衣服や体の一面に付着している状態を表す最も典型的な例です。'
            ),
            (
                '長年誰も使っていなかった屋根裏部屋を片付けたら、全身がほこり（　　　）になった。',
                'まみれ',
                ['ずくめ', 'まじき', 'めいて'],
                'When I cleaned up the attic that no one had used for years, my whole body became covered in dust.',
                '細かいほこりや砂が表面全体にまとわりつく様子を表します。'
            ),
            (
                '真夏の体育館で三時間もバドミントンの練習を続け、シャツが汗（　　　）になった。',
                'まみれ',
                ['ずくめ', 'ばかり', 'なりに'],
                'After continuing badminton practice for three hours in the midsummer gymnasium, my shirt was soaked in sweat.',
                '「汗まみれ」も日常から文章まで頻繁に用いられる重要コロケーションです。'
            ),
            (
                '工場の古い機械を分解して修理するうちに、作業着も両手も機械油（　　　）になった。',
                'まみれ',
                ['ずくめ', 'ゆえに', 'ぶる'],
                'While disassembling and repairing the old factory machinery, both my work clothes and hands became smeared with machine oil.',
                '油や泥など、簡単に落ちにくい液体がべっとりとついた状態を示します。'
            ),
        ],
    },
    10: {
        'formula': '名詞・普通形（ナ形容詞・名詞 ＋ である） ＋ <strong>ゆえに</strong> ／ <strong>がゆえに</strong> ／ 名詞 ＋ <strong>ゆえの</strong> ＋ 名詞',
        'similar': '〜ために / 〜だからこそ / 〜という理由で',
        'wrong': (
            '今日は電車が遅れたゆえに、十時からの打ち合わせに少し遅れます。',
            '「〜ゆえに」は非常に硬い文語的表現であり、日常の簡単な業務連絡や遅刻の言い訳に使うと不自然に大げさになります。',
            '"〜ゆえに" is a lofty literary expression of cause and reason, making it unnatural for casual everyday excuses like running late for a meeting.'
        ),
        'comp': (
            '〜からこそ',
            'precisely because ~',
            'どちらも理由を強調しますが、「〜ゆえに」は客観的な因果関係や格調高い論述に用いられ、「名詞＋ゆえの＋名詞」の形で連体修飾もできます。',
            'Both highlight a reason, but 〜ゆえに belongs to formal/literary prose and can directly modify nouns via ゆえの.',
            '若さゆえの失敗もあったが、その経験が今の仕事に大きく{生|い}きている。',
        ),
        'quiz': [
            (
                'まだ実務経験が浅いが（　　　）、先輩{方|がた}の助言を素直に吸収して成長することができた。',
                'ゆえに',
                ['おろか', 'まみれに', 'かまけて'],
                'Precisely because my practical experience was still limited, I was able to honestly absorb the advice of my seniors and grow.',
                '「〜がゆえに」の形で、その原因・理由を特に強調して述べる文語的な表現です。'
            ),
            (
                '新雪の美しさに心を奪われたが（　　　）、多くの写真家が冬の早朝にこの渓谷を訪れる。',
                'ゆえに',
                ['とあっては', 'にかこつけて', 'に先駆けて'],
                'Because their hearts are captivated by the beauty of fresh snow, many photographers visit this valley early on winter mornings.',
                '心情や性質が原因となって次の行動や結果が生じることを格調高く表します。'
            ),
            (
                '期待が大きかった（　　　）、計画が延期になったときの落胆もまた大きかった。',
                'ゆえに',
                ['ずくめに', 'そばから', 'なりとも'],
                'Because expectations were high, the disappointment when the plan was postponed was also great.',
                '前の事柄が直接の原因となって、それに見合う結果が生じたことを示します。'
            ),
            (
                '完成度の高さを追求する職人（　　　）厳しいこだわりが、この楽器の音色を支えている。',
                'ゆえの',
                ['ごときの', 'まじき', 'ばかりの'],
                'The strict dedication that comes precisely from being a craftsman pursuing perfection supports the tone of this musical instrument.',
                '「名詞＋ゆえの＋名詞」で「〜だからこそ生じる」という意味の連体修飾になります。'
            ),
        ],
    },
    11: {
        'formula': '名詞 ＋ <strong>ならでは（の ＋ 名詞 ／ だ）</strong>',
        'similar': '〜特有の / 〜にしかできない / 〜だからこそ可能な',
        'wrong': (
            '新入社員ならではの初歩的な入力ミスがいくつも見つかった。',
            '「〜ならでは」は「他には真似できない素晴らしい特徴・価値」を高く評価するときに使う肯定的な表現であり、単なるミスや欠点には使いません。',
            '"〜ならでは" praises a unique, admirable quality that only X possesses; it is not used for ordinary mistakes or shortcomings.'
        ),
        'comp': (
            '〜特有の',
            'peculiar to; characteristic of',
            '「〜特有の」は良い特徴にも悪い現象にも中立的に使えますが、「〜ならでは」は「〜だからこそ味わえる魅力」という称賛の気持ちを伴います。',
            'While 〜特有の is neutral and applies to both good and bad traits, 〜ならでは carries positive admiration for something uniquely valuable.',
            '雪国ならではの美しい冬景色を求めて、毎年多くの旅人がこの村を訪れる。',
        ),
        'quiz': [
            (
                '地元の漁師町（　　　）の新鮮な魚介類を使った料理が、観光客に大好評だ。',
                'ならでは',
                ['ゆえに', 'ごとき', 'まみれ'],
                'Dishes made with fresh seafood unique to a local fishing town are immensely popular with tourists.',
                'その場所や立場でしか味わえない特別な魅力を肯定的に評価する表現です。'
            ),
            (
                '長年の経験を積んだ熟練の職人（　　　）の繊細な手仕事に、見学者は目を奪われた。',
                'ならでは',
                ['まじき', 'ずくめ', 'ぶる'],
                'Visitors were captivated by the delicate craftsmanship uniquely possible for a master artisan with many years of experience.',
                '「他の誰にも真似できない素晴らしい技」を称賛する典型的な用法です。'
            ),
            (
                '手書きの手紙には、デジタルの文書にはない温かみと送り手（　　　）の味わいがある。',
                'ならでは',
                ['極まりない', 'にかまけた', 'とおぼしき'],
                'Handwritten letters have a warmth not found in digital documents and a charm unique to the sender.',
                'その人や物に備わっている独自の魅力を強調するときに用いられます。'
            ),
            (
                '四季の移ろいを繊細に表現した和菓子は、日本の伝統文化（　　　）の芸術と言える。',
                'ならでは',
                ['にかこつけた', 'をよそにした', 'にいたって'],
                'Japanese sweets that delicately express the changing of the four seasons can be called an art form unique to traditional Japanese culture.',
                '「名詞＋ならではの＋名詞」の形で、文化的価値や独自性を高く評価します。'
            ),
        ],
    },
    12: {
        'formula': '名詞 ＋ <strong>にかかわる</strong>',
        'similar': '〜に影響する / 〜を左右する / 〜に重大な関係がある',
        'wrong': (
            '明日の遠足のおやつに何を持っていくかにかかわる楽しい相談をした。',
            '「〜にかかわる」は「名誉・信用・存続・将来」など、重大で深刻な事態に影響を及ぼす場合に限って使われます。些細な話題には使えません。',
            '"〜にかかわる" is restricted to grave matters such as honor, trust, survival, or one\'s future, not trivial topics like choosing snacks.'
        ),
        'comp': (
            '〜に関する',
            'related to; concerning (general topic)',
            '「〜に関する」は話題や分野を中立的に広く指しますが、「〜にかかわる」は重大な危機や根本的な価値に直結することを強調します。',
            'While 〜に関する neutrally indicates any topic, 〜にかかわる emphasizes a critical impact on something vital like reputation or survival.',
            'この地域の水質保全に関する調査報告書が、来月の学会で発表される予定だ。',
        ),
        'quiz': [
            (
                '製品の安全性の不備は、長年築き上げてきた企業の信用（　　　）重大な問題だ。',
                'にかかわる',
                ['にかまける', 'にかこつける', 'に先駆ける'],
                'Deficiencies in product safety are a serious issue affecting the corporate trust built up over many years.',
                '「信用にかかわる」「名誉にかかわる」のように、失ってはならない大切な価値と結びつきます。'
            ),
            (
                '伝統ある工房の名誉（　　　）仕事だからこそ、一切の妥協を許さずに仕上げなければならない。',
                'にかかわる',
                ['にとどまる', 'にいたる', 'に相まった'],
                'Precisely because this work affects the honor of our historic workshop, we must finish it without allowing any compromise.',
                '組織や個人の誇り・評価を左右する重要な局面で用いられます。'
            ),
            (
                '主力商品の開発計画が成功するかどうかは、会社の今後の存続（　　　）大切な岐路である。',
                'にかかわる',
                ['にひきかえ', 'に即した', 'に準じた'],
                'Whether the development plan for the flagship product succeeds is a vital crossroads affecting the future survival of the company.',
                '将来や存続など、組織の運命を大きく左右する事柄に対して使われます。'
            ),
            (
                '今回の資格試験の合否は、彼の今後の進路（　　　）だけに、周囲も結果を案じている。',
                'にかかわる',
                ['にかまける', 'にまつわる', 'に先立つ'],
                'Since passing or failing this qualification exam affects his future career path, those around him are also anxious about the result.',
                '人生の進路や将来に重大な影響を及ぼすことを示す表現です。'
            ),
        ],
    },
    13: {
        'formula': '名詞・普通形 ＋ <strong>とあっては</strong>',
        'similar': '〜という特別な事情なら / 〜となれば / 〜からには',
        'wrong': (
            '毎日いつもの電車に乗るとあっては、私は今日も駅のホームで並んだ。',
            '「〜とあっては」は「恩師の頼み」「一生に一度の機会」など、特別な事情や状況があるために「〜せざるを得ない」と述べる表現です。日常の習慣には使えません。',
            '"〜とあっては" introduces a special circumstance that compels a certain response ("given that it is X, one cannot help doing Y"), not routine daily habits.'
        ),
        'comp': (
            '〜とあれば',
            'if it is the case that ~; for the sake of ~',
            'どちらも特別な事情を条件としますが、「〜とあっては」は「黙っていられない」「断れない」など、そうせざるを得ない心理的拘束感が強く出ます。',
            'Both state special conditions, but 〜とあっては more strongly conveys feeling compelled or unable to refuse under the circumstances.',
            '子どもの将来のための教育資金とあれば、両親はどんな苦労も惜しまなかった。',
        ),
        'quiz': [
            (
                '学生時代にお世話になった恩師からの頼み（　　　）、どれほど忙しくても断るわけにはいかない。',
                'とあっては',
                ['とばかりに', 'と相まって', 'といえども'],
                'Given that it is a request from my former mentor who helped me in my student days, I cannot possibly refuse no matter how busy I am.',
                '特別な事情があるために「断れない」「協力せざるを得ない」という文脈でよく使われます。'
            ),
            (
                '十年ぶりに開催される故郷の伝統祭り（　　　）、遠方からでも帰省して参加したい。',
                'とあっては',
                ['はおろか', 'にかまけて', 'そばから'],
                'Given that it is my hometown\'s traditional festival being held for the first time in ten years, I want to return home and participate even from afar.',
                'めったにない貴重な機会であることを理由に、強い意欲を示す用法です。'
            ),
            (
                '大切な親友の門出を祝う演奏会（　　　）、万全の準備をして舞台に臨まなければならない。',
                'とあっては',
                ['にかこつけて', 'をよそに', '極まりなく'],
                'Given that it is a concert celebrating my dear friend\'s new departure, I must prepare thoroughly for the stage.',
                '状況の特別さを踏まえて、相応の覚悟や行動が必要であることを表します。'
            ),
            (
                '世界的な建築家が手がけた図書館が公開される（　　　）、建築を学ぶ者として見に行かない手はない。',
                'とあっては',
                ['まじきで', 'ずくめで', 'が早いか'],
                'Given that a library designed by a world-renowned architect is being opened to the public, as an architecture student there is no reason not to go see it.',
                '動詞の普通形に接続し、「そのような特別な状況ならば当然〜する」と述べています。'
            ),
        ],
    },
    14: {
        'formula': '名詞（身分・立場・職業） ＋ <strong>たるもの（は）</strong>',
        'similar': '〜であるからには / 〜という立場にある者は / 〜として',
        'wrong': (
            '美味しい紅茶たるものは、お湯の温度と茶葉の量に気をつけて淹れるべきだ。',
            '「〜たるもの」は社会的責任や専門的資格を持つ「人間・組織」の立場につく表現であり、飲み物や道具などの物品には使えません。',
            '"〜たるもの" attaches only to people or roles carrying social responsibility or professional status, never to inanimate objects like tea.'
        ),
        'comp': (
            '〜ならでは',
            'unique to ~; only possible for ~',
            '「〜ならでは」はその対象特有の魅力を称賛しますが、「〜たるもの」は「その立場にある以上、こうあるべきだ」という義務や心構えを説きます。',
            'While 〜ならでは praises unique charm, 〜たるもの states the moral duty or ideal standard expected of someone in a given role.',
            'プロたるもの、どんな状況でも最善を尽くして観客の期待に応えるべきだ。',
        ),
        'quiz': [
            (
                '教育者（　　　）、常に学ぶ姿勢を忘れず、生徒一人ひとりの声に耳を傾けるべきである。',
                'たるもの',
                ['ごとき', 'まみれ', 'ずくめ'],
                'Those who are educators should never forget an attitude of continuous learning and should listen to the voice of each and every student.',
                '社会的立場を表す名詞につき、その立場にふさわしい心構えや義務を説く表現です。'
            ),
            (
                'オーケストラの指揮者（　　　）、楽曲への深い理解と団員を導く統率力が求められる。',
                'たるもの',
                ['ならでは', 'ばかりに', 'にかまけて'],
                'One who is an orchestra conductor is required to have a deep understanding of the music and the leadership to guide the members.',
                '文末は「〜べきだ」「〜が求められる」「〜ねばならない」などの当為表現と呼応します。'
            ),
            (
                '一国の文化を代表する伝統工芸の継承者（　　　）、技の研鑽を怠ってはならない。',
                'たるもの',
                ['まじき', 'ゆえの', 'なりとも'],
                'As a successor of traditional crafts representing a nation\'s culture, one must never neglect the refinement of one\'s skills.',
                '高い誇りや責任を伴う役職・身分に対して用いられる格調高い言い回しです。'
            ),
            (
                'チームの主将（　　　）、苦しい場面でこそ冷静さを保ち、仲間を鼓舞する存在でありたい。',
                'たるもの',
                ['とおぼしき', 'を皮切りに', 'が早いか'],
                'As team captain, one wants to be a presence that stays calm and inspires teammates especially in tough moments.',
                '理想とされる人物像や行動規範を力強く述べる文脈で使われます。'
            ),
        ],
    },
    15: {
        'formula': '名詞A ＋ <strong>あっての</strong> ＋ 名詞B',
        'similar': '〜があるからこそ成り立つ / 〜のおかげで存在する',
        'wrong': (
            '昨日の大雨あっての土砂崩れで、山の道路が一時通行止めになった。',
            '「AあってのB」は「Aという大切な基盤や支えがあるからこそ、価値あるBが成り立つ」という感謝や重要性の強調に使い、災害や悪結果には使いません。',
            '"AあってのB" expresses appreciation that B can exist only thanks to the vital foundation or support of A; it is not used for bad outcomes.'
        ),
        'comp': (
            '〜なくして（は）',
            'without ~ (impossible without)',
            '「AなくしてBはない」は否定の形で必要不可欠さを述べますが、「AあってのB」は肯定の形でAへの感謝や依存関係を温かく強調します。',
            'While 〜なくして states indispensability via negation ("without A, no B"), 〜あっての positively highlights gratitude toward A as the foundation of B.',
            '地域の皆様の温かいご支援なくして、この音楽祭の成功はあり得ませんでした。',
        ),
        'quiz': [
            (
                'いかに優れた企画も健康（　　　）仕事だから、無理をせず十分な休養をとることが大切だ。',
                'あっての',
                ['ゆえの', 'ごときの', 'まみれの'],
                'No matter how excellent a project is, work is only possible with good health, so it is important not to overdo it and to get sufficient rest.',
                '「健康あっての仕事」「体あっての物種」のように、すべての土台となるものを強調します。'
            ),
            (
                '創業百周年を迎えられたのも、日頃よりご愛顧くださるお客様（　　　）ことと深く感謝申し上げます。',
                'あっての',
                ['ずくめの', 'まじき', 'ばかりの'],
                'We are deeply grateful that being able to celebrate our 100th anniversary is entirely thanks to our loyal customers.',
                '挨拶や謝辞において、支えてくれた相手への感謝を述べる定番の表現です。'
            ),
            (
                '舞台{上|じょう}の俳優が輝けるのは、照明や音響を支える裏{方|かた}のスタッフ（　　　）ものだ。',
                'あっての',
                ['極まりない', 'にかまけた', 'をよそにした'],
                'The fact that actors on stage can shine is only possible thanks to the backstage staff supporting lighting and sound.',
                '表に出ない支え手が存在するからこそ成功が成り立つという文脈で用いられます。'
            ),
            (
                '個人の自由な発想も、基礎的な知識と技術の積み重ね（　　　）独創性である。',
                'あっての',
                ['にかこつけた', 'に先駆けた', 'とばかりの'],
                'Individual free thinking is originality that exists only thanks to the accumulation of basic knowledge and skills.',
                '土台となる要素の不可欠さを端的に示す名詞修飾の表現です。'
            ),
        ],
    },
    16: {
        'formula': '名詞 ／ 動詞辞書形 ＋ <strong>ともなると</strong> ／ <strong>ともなれば</strong>',
        'similar': '〜になると / 〜という段階に達すると / 〜ほどの立場になれば',
        'wrong': (
            '朝起きて顔を洗うともなると、私はいつも冷たい水を使うことにしている。',
            '「〜ともなると」はある高い段階・特別な時期・重要な立場に達したときに生じる変化を述べる表現であり、毎日の単純な習慣には使えません。',
            '"〜ともなると" describes what naturally happens once a notable stage, season, or high status is reached, not ordinary daily routines.'
        ),
        'comp': (
            '〜に至っては',
            'when it comes to ~ (extreme case)',
            '「〜に至っては」は最も極端な個別例を挙げて驚きや呆れを示しますが、「〜ともなると」はその段階に達すれば当然そうなるという一般性を述べます。',
            'While 〜に至っては singles out one extreme case, 〜ともなると states what naturally holds true once a certain level or stage is reached.',
            '連休の最終{日|び}ともなると、高速道路の上り線は朝から激しい渋滞が始まる。',
        ),
        'quiz': [
            (
                '全国大会の決勝戦（　　　）、どのチームの選手も一切の隙を見せない緊迫した試合展開になる。',
                'ともなると',
                ['とばかりに', 'はおろか', 'そばから'],
                'Once it comes to the final match of the national tournament, the game unfolds with tense intensity where players on every team show no opening.',
                '高いレベルの段階に達すると、それ相応の特別な状況になることを表します。'
            ),
            (
                '社会人になって自分で生計を立てる（　　　）、学生時代のように気楽に時間を過ごすわけにはいかない。',
                'ともなると',
                ['が早いか', 'にかまけて', 'を皮切りに'],
                'Once one becomes a working adult and earns one\'s own living, one cannot spend time as carefree as in student days.',
                '動詞の辞書形に接続し、立場や環境が大きく変わる段階を示します。'
            ),
            (
                '十一月も下旬（　　　）、北国の山々では初雪の便りが届き始め、冬の準備が本格化する。',
                'ともなれば',
                ['にかこつけて', 'をよそに', 'なりとも'],
                'Once it reaches late November, news of the first snow begins to arrive from the northern mountains, and winter preparations get into full swing.',
                '季節や時期がある段階に進むと自然に起きる変化を描写する用法です。'
            ),
            (
                '数百人の社員を率いる経営者（　　　）、一つの判断が会社全体の将来を左右する重みを持つ。',
                'ともなると',
                ['ごときでは', 'まみれでは', 'ずくめでは'],
                'Once one is an executive leading hundreds of employees, a single decision carries the weight of determining the future of the entire company.',
                '責任ある立場になれば当然それに伴う重責が生じることを述べています。'
            ),
        ],
    },
    17: {
        'formula': '名詞 ／ 動詞辞書形＋こと ＋ <strong>なくして（は）</strong> ＋ 否定表現',
        'similar': '〜なしには〜ない / 〜がなければ〜ない',
        'wrong': (
            '今日は傘なくして外出したが、幸い最後まで雨は降らなかった。',
            '「〜なくして（は）」は「信頼なくして成功はない」のように抽象的で重要な条件が不可欠であることを述べる硬い表現であり、日用品の携行には「〜なしで」を使います。',
            '"〜なくして" is a formal expression stating that an abstract, vital condition is indispensable ("without X, Y is impossible"), not for going out without an umbrella.'
        ),
        'comp': (
            '〜なしに（は）',
            'without doing ~; without ~',
            '「〜なしに」は「断りなしに」「予告なしに」など具体的な手続きや行動を省く場合にも広く使えますが、「〜なくして」は文末に否定を伴って不可欠な前提条件を強調します。',
            'While 〜なしに broadly covers acting without prior notice or permission, 〜なくして pairs with a negative predicate to stress an indispensable prerequisite.',
            '事前の予約なしに人気の美術館へ行ったため、当日は入館できなかった。',
        ),
        'quiz': [
            (
                '地域住民の理解と協力（　　　）、この伝統的な祭りを次世代へ引き継ぐことはできない。',
                'なくしては',
                ['ずくめでは', 'まみれでは', 'にかまけて'],
                'Without the understanding and cooperation of local residents, this traditional festival cannot be passed down to the next generation.',
                '「〜なくしては…できない」の形で、成功に欠かせない必須条件を強く示します。'
            ),
            (
                '地道な基礎研究の積み重ね（　　　）、画期的な新技術の開発はあり得ない。',
                'なくして',
                ['はおろか', 'をよそに', 'とばかりに'],
                'Without the steady accumulation of basic research, the development of groundbreaking new technology is impossible.',
                '抽象度の高い名詞につき、その存在が絶対条件であることを訴える表現です。'
            ),
            (
                '互いの文化や価値観を尊重する姿勢（　　　）、真の国際交流を深めることは難しい。',
                'なくして',
                ['にかこつけて', 'に先駆けて', 'を皮切りに'],
                'Without an attitude of respecting each other\'s cultures and values, it is difficult to deepen genuine international exchange.',
                '評論文やスピーチで「〜がなければ成り立たない」と主張する際によく使われます。'
            ),
            (
                '過去の失敗の原因を徹底的に分析すること（　　　）、組織の根本的な改善は望めない。',
                'なくしては',
                ['ともなると', 'とあっては', 'が早いか'],
                'Without thoroughly analyzing the causes of past failures, fundamental improvement of the organization cannot be hoped for.',
                '「動詞辞書形＋ことなくして（は）」の形で、不可欠な行動を提示しています。'
            ),
        ],
    },
    18: {
        'formula': '名詞 ／ 動詞辞書形＋こと ＋ <strong>なしに（は）</strong>',
        'similar': '〜ないで / 〜を抜きにして / 〜せずに',
        'wrong': (
            '冷蔵庫に牛乳なしに、今朝は紅茶をストレートで飲むことにした。',
            '「〜なしに」は「〜を伴わずに・〜をしないで」と動詞句を修飾するか、「〜なしには…ない」の形で条件を表すため、「牛乳がないから」という単純な理由には使えません。',
            '"〜なしに" modifies an action ("without doing/having X") or forms a conditional ("without X, cannot Y"); it cannot mean "because there is no milk in the fridge."'
        ),
        'comp': (
            '〜を抜きにして（は）',
            'leaving out ~; without ~',
            '「〜を抜きにして」は特定の人物や要素（お世辞・冗談など）を除外することに重点があり、「〜なしに」は手続きや段階を踏まないまま行動する場面でもよく使われます。',
            'While 〜を抜きにして focuses on omitting a person or element (flattery, jokes), 〜なしに often describes acting without required steps or notice.',
            'お世辞を抜きにして、彼女のヴァイオリンの演奏は聴衆の心を強く揺さぶった。',
        ),
        'quiz': [
            (
                '管理者の事前の許可（　　　）、研究室の精密機器を外部へ持ち出すことは禁じられている。',
                'なしに',
                ['ならでは', 'ゆえに', 'ずくめで'],
                'Taking precision instruments out of the laboratory without the administrator\'s prior permission is prohibited.',
                '「許可なしに」「断りなしに」「予告なしに」のように、必要な手続きを経ないことを表します。'
            ),
            (
                'あの映画の感動的な結末は、涙（　　　）最後まで見届けることはできなかった。',
                'なしには',
                ['まみれには', 'ごときには', 'ばかりには'],
                'I could not watch the moving conclusion of that film to the end without tears.',
                '「涙なしには見られない／語れない」は非常によく使われる慣用的なコロケーションです。'
            ),
            (
                '現場で働く人々の意見を聞くこと（　　　）、実効性のある業務改善案を作ることはできない。',
                'なしに',
                ['にかまけて', 'にかこつけて', 'と相まって'],
                'Without listening to the opinions of the people working on site, an effective work improvement plan cannot be created.',
                '「動詞辞書形＋ことなしに」で「〜という行動をとらずに」という意味を表します。'
            ),
            (
                '何の前触れも（　　　）長年の連載小説が最終回を迎え、読者からは惜しむ声が相次いだ。',
                'なしに',
                ['おろか', 'まじき', 'そばから'],
                'Without any prior warning, the long-running serialized novel reached its final chapter, prompting a stream of regretful voices from readers.',
                '「何の前触れもなしに」「何の相談もなしに」の形で、突然の事態を描写します。'
            ),
        ],
    },
    19: {
        'formula': '名詞 ／ 普通形 ＋ <strong>なりに</strong> ／ 名詞 ＋ <strong>なりの</strong> ＋ 名詞',
        'similar': '〜相応に / 〜の立場でできる範囲で / 〜に合わせて',
        'wrong': (
            '世界的な名演奏家なりに、彼のピアノの演奏は非の打ち所がない完璧なものだった。',
            '「〜なりに」は「まだ十分ではないが、その立場・能力の範囲で精一杯」という控えめな評価や限界を含意するため、完璧な対象を最高度に称賛する文には不向きです。',
            '"〜なりに" implies doing the best within certain limits ("in one\'s own modest way"), so it does not fit praising a flawless world-class master.'
        ),
        'comp': (
            '〜ならでは',
            'uniquely possible for ~ (high praise)',
            '「〜ならでは」は他の誰にも真似できない卓越した魅力を称賛しますが、「〜なりに」は限界がある中でそれ相応に工夫・努力している様子を表します。',
            'While 〜ならでは praises unmatched excellence, 〜なりに acknowledges limitations while appreciating effort commensurate with one\'s level.',
            '子どもたちは子どもなりに、家族のために何ができるかを一生懸命考えていた。',
        ),
        'quiz': [
            (
                'まだ経験は浅いが、私（　　　）精一杯工夫して新しい企画書をまとめてみました。',
                'なりに',
                ['ならでは', 'ずくめで', 'まみれに'],
                'Although my experience is still limited, I tried putting together the new proposal with as much ingenuity as I could in my own way.',
                '能力や経験に限りがあることを認めつつ、自分の力の範囲で最善を尽くす姿勢を表します。'
            ),
            (
                '小さな店舗には小さな店舗（　　　）良さがあり、客との距離が近い丁寧な接客ができる。',
                'なりの',
                ['まじき', 'ごときの', 'ばかりの'],
                'A small shop has merits suited to a small shop, allowing attentive service close to customers.',
                '「名詞＋なりの＋名詞」で、その規模や立場にふさわしい特徴があることを示します。'
            ),
            (
                '収入が限られているなら、限られている（　　　）無駄を省いて豊かに暮らす知恵を身につけたい。',
                'なりに',
                ['とばかりに', 'はおろか', 'そばから'],
                'If one\'s income is limited, one wants to acquire the wisdom to eliminate waste and live richly in accordance with those limits.',
                '動詞や形容詞の普通形に接続し、「その状態に応じたやり{方|かた}で」という意味を表します。'
            ),
            (
                '初心者には初心者（　　　）疑問があるはずだから、専門用語を使わずに分かりやすく説明しよう。',
                'なりの',
                ['極まりない', 'にかまけた', 'をよそにした'],
                'Since beginners surely have questions natural to beginners, let\'s explain clearly without using technical terms.',
                'それぞれの段階や立場に応じた視点があることを肯定的に受け止める表現です。'
            ),
        ],
    },
    20: {
        'formula': '名詞 ＋ <strong>を踏まえて</strong> ／ <strong>を踏まえ</strong> ／ <strong>を踏まえた</strong> ＋ 名詞',
        'similar': '〜を考慮に入れて / 〜を前提として / 〜に基づいて',
        'wrong': (
            '駅の階段を強く踏まえて登ったので、ふくらはぎが筋肉痛になった。',
            '文法表現の「〜を踏まえて」は「事実・状況・反省・意見」などを前提や判断材料として次の行動をとるという意味であり、物理的に足で踏む動作には使えません。',
            'As a grammar pattern, "〜を踏まえて" means basing a decision or action on prior facts, feedback, or reflection—not physically stepping on stairs.'
        ),
        'comp': (
            '〜に基づいて',
            'based on (data, law, principle)',
            '「〜に基づいて」は法律・統計データ・基準などを直接の根拠としますが、「〜を踏まえて」は過去の経験や現状・相手の意見などを十分に考慮して行動する点に特徴があります。',
            'While 〜に基づいて relies directly on laws or data as a basis, 〜を踏まえて emphasizes taking past experience, current conditions, or feedback into consideration.',
            '前回のアンケート結果を踏まえて、来年度の講座内容を見直すことになった。',
        ),
        'quiz': [
            (
                '試作段階での反省点（　　　）、開発チームは製品の耐久性を大幅に改良した。',
                'を踏まえて',
                ['をよそに', 'を皮切りに', 'を限りに'],
                'Taking into account the points for reflection from the prototype stage, the development team significantly improved the durability of the product.',
                '過去の経験や反省点を考慮に入れた上で、次の改善策を講じる典型的な用法です。'
            ),
            (
                '利用者から寄せられた多様な意見（　　　）{上|うえ}で、図書館の開館時間が延長された。',
                'を踏まえた',
                ['をものともしない', 'にかまけた', 'にかこつけた'],
                'After taking into consideration the diverse opinions received from users, the library\'s opening hours were extended.',
                '「〜を踏まえた上で」は、前提条件をしっかり考慮したことを強調する頻出表現です。'
            ),
            (
                '地域の高齢化が進む現状（　　　）、誰にでも使いやすい巡回バスの運行が始まった。',
                'を踏まえ',
                ['を尻目に', 'を抜きにして', 'を差し置いて'],
                'Based on the current situation of aging in the community, operation of an easy-to-use community bus has begun.',
                '書き言葉では「〜を踏まえ、…」と連用形で文をつなぐ形もよく使われます。'
            ),
            (
                'これまでの議論の内容（　　　）、次回までに具体的な実行計画を策定してください。',
                'を踏まえて',
                ['をよそにして', 'を境にして', 'を頼りにして'],
                'Based on the content of our discussions so far, please formulate a concrete action plan by next time.',
                '実務や会議において、それまでの経緯を前提として次の作業を求める表現です。'
            ),
        ],
    },
    21: {
        'formula': '名詞 ＋ <strong>に先駆けて</strong> ／ <strong>に先駆け</strong> ／ <strong>に先駆ける</strong> ＋ 名詞',
        'similar': '〜より一足先に / 〜に先立って / 他に先んじて',
        'wrong': (
            '外出に先駆けて、玄関の鍵をきちんとかけたかもう一度確認した。',
            '「〜に先駆けて」は「他社に先駆けて開発する」「全国公開に先駆けて上映する」のように、他の競争相手や本来の時期よりも一歩早く先進的に行う場合に使います。日常の確認作業には「〜に先立って／〜の前に」を使います。',
            '"〜に先駆けて" means pioneering ahead of competitors or holding a preview ahead of a major release, not routine checks before going out.'
        ),
        'comp': (
            '〜に先立って',
            'prior to; before (preparatory step)',
            '「〜に先立って」は式典や開始の前に必要な準備・挨拶を行うことを表しますが、「〜に先駆けて」は「誰よりも早く・世の中に先んじて」という先進性を強調します。',
            'While 〜に先立って denotes a preparatory step before an event, 〜に先駆けて emphasizes being a pioneer ahead of others or ahead of the general release.',
            '映画の全国公開に先駆けて、来週都内で特別試写会が開催される。',
        ),
        'quiz': [
            (
                'そのメーカーは業界（　　　）、環境負荷を大幅に減らした再生素材の容器を導入した。',
                'に先駆けて',
                ['にかまけて', 'にかこつけて', 'にいたっては'],
                'Taking the lead in the industry, that manufacturer introduced containers made of recycled materials that greatly reduce environmental impact.',
                '「業界に先駆けて」「世界に先駆けて」のように、他より早く革新的な取り組みを行う場面で使われます。'
            ),
            (
                '春の全国発売（　　　）、今週末から一部の店舗で新商品の先行体験会が行われる。',
                'に先駆けて',
                ['と相まって', 'をよそに', 'はおろか'],
                'Ahead of the nationwide spring release, an advance trial event for the new product will be held at select stores starting this weekend.',
                '本格的な公開や発売よりも一足早く特別に実施することを表します。'
            ),
            (
                '他地域（　　　）再生可能エネルギーの普及に取り組んだその自治体は、全国から注目を集めている。',
                'に先駆けて',
                ['にとどまって', 'にひきかえ', 'に即して'],
                'The municipality that worked to promote renewable energy ahead of other regions is attracting attention from across the country.',
                '他の地域や団体よりも先進的に行動を起こしたことを高く評価する文脈です。'
            ),
            (
                '時代の変化（　　　）新しい働き{方|かた}を取り入れた企業に、優秀な人材が集まっている。',
                'に先駆けて',
                ['にかかわって', 'にまつわって', 'に準じて'],
                'Talented personnel are gathering at companies that adopted new ways of working ahead of the changing times.',
                '世の中の動きより一歩先に進む先見性を表す表現です。'
            ),
        ],
    },
    22: {
        'formula': '名詞 ＋ <strong>を契機に（して）</strong> ／ <strong>を契機として</strong>',
        'similar': '〜をきっかけに / 〜を転機として / 〜を機に',
        'wrong': (
            '正午の時報を契機に、私たちは社員食堂へ昼食を食べに行った。',
            '「〜を契機に」は社会や人生・事業における「大きな転換点・発展のきっかけ」を表す硬い表現であり、毎日の昼休みの合図のような日常動作には使えません。',
            '"〜を契機に" denotes a major turning point or catalyst for significant change, not a routine daily signal like the noon chime.'
        ),
        'comp': (
            '〜を皮切りに',
            'starting with ~ (followed by a series of similar events)',
            '「〜を皮切りに」は同種の出来事が次々と連鎖することに焦点を当てますが、「〜を契機に」はある出来事を境に状況が大きく変化・発展することに焦点を当てます。',
            'While 〜を皮切りに focuses on a chain of similar events, 〜を契機に focuses on a decisive turning point that brings about major change.',
            '国際会議の開催を契機として、駅周辺の再開発が一気に進められた。',
        ),
        'quiz': [
            (
                '創業五十周年（　　　）、その企業はブランドの象徴であるロゴマークを一新した。',
                'を契機に',
                ['をよそに', 'を限りに', 'を抜きにして'],
                'Taking the 50th anniversary of its founding as a turning point, the company completely renewed its brand logo.',
                '節目の出来事をきっかけとして、大きな刷新や変化を行うときに使われます。'
            ),
            (
                '海外の展示会への出展（　　　）、伝統的な漆器の工房は海外市場への販路を広げた。',
                'を契機として',
                ['をものともせず', 'を尻目に', 'を差し置いて'],
                'Triggered by exhibiting at an overseas trade fair, the traditional lacquerware workshop expanded its sales channels into overseas markets.',
                '事業や活動が大きく飛躍する転機となった事柄を示します。'
            ),
            (
                '新幹線の開通（　　　）、かつて静かだった温泉街には多くの観光客が訪れるようになった。',
                'を契機に',
                ['を押して', 'を頼りに', 'をめぐって'],
                'With the opening of the bullet train line as a turning point, many tourists began visiting the once-quiet hot spring town.',
                '社会的な出来事によって地域の状況が大きく変わったことを表します。'
            ),
            (
                '恩師との出会い（　　　）、彼女は古典文学の翻訳という新たな研究分野に情熱を注ぎ始めた。',
                'を契機にして',
                ['をよそにして', 'を問わず', 'に先駆けて'],
                'With meeting her mentor as a turning point, she began pouring her passion into the new research field of translating classical literature.',
                '人生の進路や目標が定まる重要なきっかけを表す文脈です。'
            ),
        ],
    },
    23: {
        'formula': '名詞 ＋ <strong>を機に</strong>',
        'similar': '〜をきっかけに / 〜を良い機会として / 〜を契機に',
        'wrong': (
            '信号が青になったのを機に、歩行者たちは一斉に横断歩道を渡り始めた。',
            '「〜を機に」は引っ越し・進学・退職・周年など、生活や仕事の節目となる機会を捉えて新しい習慣や行動を始める場合に使い、信号の変化のような瞬間の合図には使いません。',
            '"〜を機に" is used when seizing a milestone opportunity (moving, graduation, retirement) to start something new, not for momentary signals like a traffic light.'
        ),
        'comp': (
            '〜を契機に',
            'triggered by ~ (formal/large-scale turning point)',
            '「〜を契機に」は歴史的・社会的な大変化にも多く使われる硬い表現ですが、「〜を機に」は個人の生活習慣の見直しなど身近な節目にも自然に使えます。',
            'While 〜を契機に is more formal and often used for large-scale changes, 〜を機に is also natural for personal milestones like starting a new habit.',
            '新しい部署への異動を機に、毎朝一時間早く出社して語学の勉強を始めた。',
        ),
        'quiz': [
            (
                '郊外の一戸建てへの引っ越し（　　　）、家族で念願だった家庭菜園を始めることにした。',
                'を機に',
                ['をよそに', 'を限りに', 'をものともせず'],
                'Taking the move to a house in the suburbs as an opportunity, our family decided to start the home vegetable garden we had long wished for.',
                '生活の節目を良い機会として、新しい取り組みを始める典型的な用法です。'
            ),
            (
                '定年退職（　　　）、父は若い頃から興味を持っていた水彩画の教室に通い始めた。',
                'を機に',
                ['を尻目に', 'を抜きにして', 'を差し置いて'],
                'Taking his retirement as an opportunity, my father started attending a watercolor painting class he had been interested in since his youth.',
                '人生の区切りをきっかけに、新しい趣味や生活をスタートする場面でよく使われます。'
            ),
            (
                '店舗の改装工事（　　　）、注文から会計までをスムーズに行える新しいシステムを導入した。',
                'を機に',
                ['を押して', 'を頼りに', 'にかまけて'],
                'Taking the store renovation work as an opportunity, we introduced a new system that allows smooth ordering and payment.',
                '改装や移転などのタイミングに合わせて改善を実施することを表します。'
            ),
            (
                '子どもが独立したの（　　　）、夫婦{二人|ふたり}で全国の美術館を巡る旅行を楽しんでいる。',
                'を機に',
                ['を皮切りに', 'をよそにして', 'にかこつけて'],
                'Taking their child\'s independence as an opportunity, the couple is enjoying traveling around art museums across the country together.',
                '「動詞普通形＋のを機に」の形で、状況の変化を良い機会として捉える表現です。'
            ),
        ],
    },
    24: {
        'formula': '名詞 ＋ <strong>と相まって</strong> ／ 名詞Aと名詞Bが<strong>相まって</strong>',
        'similar': '〜と結びついて / 〜と重なり合って / 〜に加えてさらに',
        'wrong': (
            '今日は紅茶とミルクと相まって、おいしいミルクティーを作って飲んだ。',
            '「〜と相まって」は複数の要因・性質・条件が互いに作用し合って、より大きな効果や印象を生み出すという抽象的な因果関係に使われ、単に材料を混ぜる動作には使えません。',
            '"〜と相まって" describes multiple factors or qualities interacting to produce a heightened effect or impression, not physically mixing ingredients.'
        ),
        'comp': (
            '〜もさることながら',
            'not only ~, but also ~',
            '「〜もさることながら」は二つの要素を並べて後者を強調しますが、「〜と相まって」は二つの要素が互いに影響し合って相乗効果を生む点を強調します。',
            'While 〜もさることながら adds a second emphasis ("not only A, but also B"), 〜と相まって highlights the synergy created by A and B working together.',
            '繊細な照明の演出が美しい音楽と相まって、舞台は幻想的な雰囲気に包まれた。',
        ),
        'quiz': [
            (
                '素材の良さ（　　　）、熟練した料理人の技がこの一皿の深い味わいを{生|う}み出している。',
                'と相まって',
                ['とばかりに', 'とあっては', 'といえども'],
                'Combined with the quality of the ingredients, the skill of the master chef creates the deep flavor of this dish.',
                '二つの優れた要素が組み合わさり、相乗効果によってさらに高い価値が生まれることを示します。'
            ),
            (
                '歴史ある建築の美しさが周囲の紅葉（　　　）、訪れる人々を魅了する見事な景観を作り出している。',
                'と相まって',
                ['にかまけて', 'にかこつけて', 'をよそに'],
                'The beauty of the historic architecture, combined with the surrounding autumn leaves, creates a magnificent view that captivates visitors.',
                '風景や芸術作品において、複数の要素が調和して印象を高める文脈で頻出します。'
            ),
            (
                '近年の健康志向の高まり（　　　）、発酵食品を使った伝統的な和食が再び注目を集めている。',
                'と相まって',
                ['はおろか', 'に先駆けて', 'そばから'],
                'Combined with the recent rise in health consciousness, traditional Japanese food using fermented ingredients is attracting attention once again.',
                '社会的な追い風や別の要因が重なって、ある傾向がいっそう強まる様子を表します。'
            ),
            (
                '俳優の迫真の演技と巧みな脚本（　　　）、その舞台劇は千秋楽まで満席の盛況となった。',
                'が相まって',
                ['にかかわって', 'にとどまって', 'にいたっては'],
                'With the actors\' compelling performances and the clever script working together, the stage play was a sold-out success until the final day.',
                '「AとBが相まって」の形で、二つの要因が一体となって好結果をもたらすことを表します。'
            ),
        ],
    },
    25: {
        'formula': '名詞 ＋ <strong>にかまけて</strong>',
        'similar': '〜にばかり気を取られて / 〜に追われて（他を疎かにする）',
        'wrong': (
            '彼は資格試験の勉強にかまけて、見事に一発で合格を果たした。',
            '「〜にかまけて」は「一つのことに追われたり夢中になったりして、本来やるべき別の大切なことを疎かにする」という反省や批判の文脈で使うため、成功の称賛には使えません。',
            '"〜にかまけて" means being so preoccupied with one thing that one neglects other important duties, so it cannot be used to praise success.'
        ),
        'comp': (
            '〜にかこつけて',
            'under the pretext of ~',
            '「〜にかこつけて」は別の目的のために口実として利用することを表しますが、「〜にかまけて」は忙しさや趣味に気を取られて他を放置してしまうことを表します。',
            'While 〜にかこつけて means using something as a convenient excuse, 〜にかまけて means getting absorbed in or busy with something and neglecting other duties.',
            '日々の忙しさにかまけて、故郷の両親になかなか連絡できずにいたことを反省した。',
        ),
        'quiz': [
            (
                '仕事の忙しさ（　　　）、自分の健康管理をすっかり疎かにしていたことを反省している。',
                'にかまけて',
                ['に先駆けて', 'にかかわって', 'にいたっては'],
                'I am reflecting on having completely neglected my own health management due to being preoccupied with the busyness of work.',
                '「忙しさにかまけて〜を怠る・疎かにする」は最も代表的なコロケーションです。'
            ),
            (
                '趣味の写真撮影（　　　）、休日に片付けるはずだった部屋の整理を後回しにしてしまった。',
                'にかまけて',
                ['を踏まえて', 'を皮切りに', 'と相まって'],
                'Preoccupied with my hobby of photography, I put off tidying the room that I was supposed to clean on my day off.',
                '楽しいことに夢中になるあまり、やるべき用事を放置してしまった場面で使われます。'
            ),
            (
                '目の前の雑務（　　　）、長期的な研究計画の準備がなかなか進まないのが悩みの種だ。',
                'にかまけて',
                ['ならではで', 'ゆえに', 'ずくめで'],
                'Being tied up with immediate daily chores, the fact that preparations for my long-term research plan are not progressing is a source of worry.',
                '日常の雑事に追われて本来の重要な課題に手が回らない状態を示します。'
            ),
            (
                '部活動の練習（　　　）授業の予習や復習を怠るようでは、本末転倒と言わざるを得ない。',
                'にかまけて',
                ['を契機に', 'をよそに', 'ともなると'],
                'Neglecting class preparation and review because of being absorbed in club practice must be called putting the cart before the horse.',
                '一方に偏って本分を忘れてしまう態度を戒める文脈で用いられます。'
            ),
        ],
    },
    26: {
        'formula': '名詞 ／ 動詞普通形＋の ＋ <strong>にかこつけて</strong>',
        'similar': '〜を口実にして / 〜をいいことにして / 〜を理由に利用して',
        'wrong': (
            '厳しい寒さにかこつけて、今朝は庭の池に薄い氷が張っていた。',
            '「〜にかこつけて」は人が別の事柄をもっともらしい口実（言い訳）として利用し、自分のやりたい行動をとるという意味なので、自然現象には使えません。',
            '"〜にかこつけて" requires a human agent using something as a convenient pretext to do what they really want; it cannot describe natural phenomena.'
        ),
        'comp': (
            '〜にかまけて',
            'being preoccupied with ~ (and neglecting other things)',
            '「〜にかまけて」は一つのことに気を取られて他を忘れることですが、「〜にかこつけて」は「取材にかこつけて観光する」のように意図的に口実として利用することです。',
            'Unlike 〜にかまけて (neglecting duties due to preoccupation), 〜にかこつけて means intentionally using something as an excuse to pursue another desire.',
            '彼は現地調査にかこつけて、有名な温泉地を巡る計画を立てているようだ。',
        ),
        'quiz': [
            (
                '地方への出張（　　　）、仕事の後で現地の有名な美術館や老舗の和菓子店を巡った。',
                'にかこつけて',
                ['に先駆けて', 'にかかわって', 'と相まって'],
                'Using a business trip to the provinces as an excuse, I visited famous local art museums and long-established sweet shops after work.',
                '本来の用件を口実にして、個人的な楽しみや別の目的を果たす典型的な例です。'
            ),
            (
                '運動不足の解消（　　　）、新しい自転車を買って週末ごとに遠くの公園まで出かけている。',
                'にかこつけて',
                ['を皮切りに', 'を踏まえて', 'に至っては'],
                'Under the pretext of relieving lack of exercise, I bought a new bicycle and go out to distant parks every weekend.',
                'もっともらしい理由を表に出して、実はやりたいことを楽しんでいるニュアンスを表します。'
            ),
            (
                '資料の返却（　　　）、憧れの先輩の研究室を訪ねて進路の相談に乗ってもらった。',
                'にかこつけて',
                ['をよそに', 'をものともせず', 'はおろか'],
                'Using returning materials as a pretext, I visited the office of the senior I admire and asked for career advice.',
                '本当の目的に近づくために、別の用件をきっかけとして利用する場面で使われます。'
            ),
            (
                'お祝いの品を届けるの（　　　）、久しぶりに姉の新居を訪れてゆっくりおしゃべりを楽しんだ。',
                'にかこつけて',
                ['ともなると', 'とあっては', 'が早いか'],
                'Using delivering a celebratory gift as an excuse, I visited my sister\'s new home for the first time in a while and enjoyed a leisurely chat.',
                '「動詞普通形＋のにかこつけて」の形で、行動の口実を表す用法です。'
            ),
        ],
    },
    27: {
        'formula': '名詞 ＋ <strong>はおろか</strong>',
        'similar': '〜はもちろん〜も / 〜どころか / 〜は言うまでもなく',
        'wrong': (
            '彼は料理が上手で、簡単な目玉焼きはおろか、本格的なフランス料理まで作れる。',
            '「AはおろかBも…」は「難しいAはもちろんのこと、もっと簡単なBさえできない（または極端な状態だ）」という順序で並べるため、簡単なものを先に置くことはできません。',
            'In "AはおろかBも", A must be the more advanced or expected item and B the simpler/more basic one ("cannot do A, let alone even B"), not the reverse.'
        ),
        'comp': (
            '〜どころか',
            'far from ~; on the contrary',
            '「〜どころか」は予想と正反対の事実を表す場合にも広く使えますが、「〜はおろか」は「Aはもちろん、より程度の低いBでさえ〜ない」という段階的な強調に特化しています。',
            'While 〜どころか broadly expresses the opposite of expectations, 〜はおろか specifically emphasizes a scale: "not to mention A, not even the simpler B."',
            '入社した頃は海外出張はおろか、英語で電話応対をすることさえ緊張していた。',
        ),
        'quiz': [
            (
                '骨折が治ったばかりで、全力で走るの（　　　）、階段を普通に上り下りすることさえまだ難しい。',
                'はおろか',
                ['とあっては', 'ともなると', 'に先駆けて'],
                'Since my bone fracture has only just healed, let alone running at full speed, even going up and down stairs normally is still difficult.',
                '「走るのはもちろん無理で、より簡単な階段の上り下りでさえ難しい」と段階的に強調しています。'
            ),
            (
                '連休の初日は大変忙しく、昼食をとる時間（　　　）、お茶を一口飲む余裕すらなかった。',
                'はおろか',
                ['を皮切りに', 'を踏まえて', 'と相まって'],
                'The first day of the holidays was extremely busy; let alone time to eat lunch, there was not even room to take a sip of tea.',
                '「〜はおろか…さえ／すら〜ない」の形で、余裕のなさを強調する頻出パターンです。'
            ),
            (
                'その珍しい高山植物は、県外（　　　）、地元の人々の{間|あいだ}でもほとんど知られていない。',
                'はおろか',
                ['ならでは', 'ゆえに', 'にかまけて'],
                'That rare alpine plant is scarcely known even among local people, let alone outside the prefecture.',
                '当然知らないであろう「県外」を挙げた上で、「地元でさえ」と驚きを添える用法です。'
            ),
            (
                '初めて楽器に触れた{日|ひ}は、一曲通して弾くこと（　　　）、正しい音を出すことさえできなかった。',
                'はおろか',
                ['にかこつけて', 'をよそに', 'そばから'],
                'On the day I touched the musical instrument for the first time, let alone playing a whole song through, I could not even produce a proper sound.',
                '難易度の高い事柄を先に置き、基本的な動作すらできない状態を際立たせます。'
            ),
        ],
    },
    28: {
        'formula': '名詞 ／ 普通形（ナ形容詞・名詞 ＋ だ → なら） ＋ <strong>ならいざしらず</strong>',
        'similar': '〜ならともかく / 〜ならまだしも / 〜であれば話は別だが',
        'wrong': (
            'プロの料理人ならいざしらず、彼は毎日レストランの厨房で見事な腕を振るっている。',
            '「Aならいざしらず、Bは…」は「Aなら事情が違って許されるかもしれないが、実際はそうではないBなのだから許されない・無理だ」という対比を表すため、後件でそのまま肯定することはできません。',
            '"Aならいざしらず、B..." contrasts a hypothetical exception A with the actual reality B ("A might be excusable, but for B it is out of the question").'
        ),
        'comp': (
            '〜ならまだしも',
            '~ would be understandable/forgivable, but',
            'どちらも「Aならまだ許せるがBはだめだ」と対比しますが、「〜ならいざしらず」の方が文語的で硬く、「Aという例外的な状況ならどうか分からないが」という突き放した語気があります。',
            'Both contrast an acceptable A with an unacceptable B, but 〜ならいざしらず is more literary and emphatic ("I don\'t know about case A, but certainly not B").',
            '緊急時ならいざしらず、普段の業務で安全手順を省くことは決して認められない。',
        ),
        'quiz': [
            (
                '初めて参加する新人（　　　）、経験豊富なベテランがこのような基本の手順を忘れるとは驚きだ。',
                'ならいざしらず',
                ['ともなると', 'とあっては', 'に先駆けて'],
                'It might be one thing for a newcomer participating for the first time, but it is surprising for an experienced veteran to forget such a basic procedure.',
                '「新人ならまだ分かるが、ベテランなのだから納得できない」と対比して批判・驚きを表します。'
            ),
            (
                '数十年前の古い機械（　　　）、最新の設備を使っていながらこれほど時間がかかるのはおかしい。',
                'ならいざしらず',
                ['を皮切りに', 'を踏まえて', 'と相まって'],
                'It might be understandable with an old machine from decades ago, but it is strange that it takes this much time when using the latest equipment.',
                '極端な仮定を前に置いて、現在の状況の不合理さを際立たせる用法です。'
            ),
            (
                '小さな子ども（　　　）、社会人が自分の言動に責任を持てないようでは信頼を得られない。',
                'ならいざしらず',
                ['にかまけて', 'にかこつけて', 'をよそに'],
                'A small child might be another matter, but if a working adult cannot take responsibility for their own words and actions, they cannot gain trust.',
                '「〜ならともかく、実際は大人の社会人なのだから」と当然の自覚を促す表現です。'
            ),
            (
                '交通手段のなかった時代（　　　）、現代において連絡もなしに何日も音信不通になるのは考えものだ。',
                'ならいざしらず',
                ['はおろか', 'ゆえに', 'そばから'],
                'An era without transportation and communication might be one thing, but in modern times becoming unreachable for days without notice is questionable.',
                '過去や特殊な環境と現在とを対比し、現状の振る舞いをたしなめる文脈で用いられます。'
            ),
        ],
    },
    29: {
        'formula': '名詞 ／ 普通形（ナ形容詞・名詞 ＋ だ → なら） ＋ <strong>ならまだしも</strong>',
        'similar': '〜ならまだ許せるが / 〜ならともかく / 〜ならいざしらず',
        'wrong': (
            '天気が良ければまだしも、今日は絶好のピクニック{日|び}よりになった。',
            '「Aならまだしも、Bは…」は「Aの程度ならまだ我慢できるが、実際はさらに悪いBなので困る」という文脈で使うため、良い結果につながる文には使えません。',
            '"Aならまだしも、B..." means "A would at least be tolerable, but reality B is even worse," so it cannot lead into a positive outcome.'
        ),
        'comp': (
            '〜ならいざしらず',
            'may be fine for ~, but definitely not',
            '「〜ならいざしらず」は全く性質の異なる立場（子どもと大人など）の対比によく使われ、「〜ならまだしも」は程度の軽い段階（一度の遅刻と三度の遅刻など）との対比にもよく使われます。',
            'While 〜ならいざしらず often contrasts opposite roles (child vs. adult), 〜ならまだしも frequently contrasts degrees ("once would be tolerable, but three times...").',
            '{一度|いちど}の遅刻ならまだしも、同じ週に三度も遅れてくるのは問題だ。',
        ),
        'quiz': [
            (
                '{五分|ごふん}や{十分|じゅっぷん}の遅れ（　　　）、連絡もなしに一時間以上も待たせるのはあんまりだ。',
                'ならまだしも',
                ['ともなると', 'とあっては', 'を皮切りに'],
                'A delay of five or ten minutes would be understandable, but keeping someone waiting for over an hour without any contact is too much.',
                '軽い程度なら大目に見られるが、実際は度を超えていると不満を述べる典型例です。'
            ),
            (
                '自分一人で困るだけ（　　　）、周囲の仲間にまで迷惑をかけるような行動は慎むべきだ。',
                'ならまだしも',
                ['に先駆けて', 'を踏まえて', 'と相まって'],
                'If only you yourself were troubled it would be one thing, but you should refrain from actions that cause trouble even for the colleagues around you.',
                '影響が小さい場合と大きい場合を対比し、後者を強く戒める表現です。'
            ),
            (
                '事前に相談してくれた（　　　）、すべての契約が済んでから事後報告されても対応できない。',
                'ならまだしも',
                ['にかまけて', 'にかこつけて', 'をよそに'],
                'It would have been one thing if you had consulted me in advance, but I cannot deal with it when you only report after all the contracts are completed.',
                '動詞のタ形＋「ならまだしも」で、本来あるべき段階を経なかったことへの困惑を示します。'
            ),
            (
                '冗談で言ったの（　　　）、本気でそのような無謀な計画を実行に移そうとしているなら止めなければならない。',
                'ならまだしも',
                ['はおろか', 'ゆえに', 'そばから'],
                'If it was said as a joke that is one thing, but if they seriously intend to put such a reckless plan into action, we must stop them.',
                '譲歩できる限界を示した上で、現実の深刻な状況に対して警告する用法です。'
            ),
        ],
    },
    30: {
        'formula': '名詞 ／ 普通形（ナ形容詞・名詞 ＋ だ → たり） ＋ <strong>といえども</strong>',
        'similar': '〜であっても / 〜とはいえ / たとえ〜でも',
        'wrong': (
            '今日は少し肌寒いといえども、私はお気に入りの青いセーターを着て出かけた。',
            '「〜といえども」は「いかに権威・実力がある対象であっても例外ではない」と述べる格調高い文語表現であり、日常の服装選びのような軽い話題には不向きです。',
            '"〜といえども" is a lofty literary concession meaning "even the greatest X is no exception," unsuitable for casual everyday topics like choosing a sweater.'
        ),
        'comp': (
            '〜とはいえ',
            'although; nonetheless',
            '「〜とはいえ」は一般的な事実を認めた上で「しかし実際は〜だ」と続けるのに広く使えますが、「〜といえども」は「いかに〜であっても」という強い譲歩・戒めに多く使われます。',
            'While 〜とはいえ is widely used to concede a fact before stating a qualification, 〜といえども has a more solemn tone ("even if one is a master/champion...").',
            'いかに熟練した登山家といえども、冬の山の天候変化を甘く見てはならない。',
        ),
        'quiz': [
            (
                '世界記録を持つ名選手（　　　）、日々の地道な基礎練習を怠れば実力を維持することはできない。',
                'といえども',
                ['とばかりに', 'とあっては', 'ともなると'],
                'Even a famous athlete who holds a world record cannot maintain their ability if they neglect steady daily basic practice.',
                'どれほど優れた人物であっても例外ではないことを厳粛に述べる用法です。'
            ),
            (
                '最新の予測システムをもってしても、自然界の複雑な変化を百パーセント見通すことは困難だと言わざるを得ないが、専門家（　　　）判断に迷う場面がある。',
                'といえども',
                ['ならでは', 'ずくめ', 'まみれ'],
                'Even with the latest forecasting systems it is difficult to foresee complex changes in nature 100 percent, and even experts have moments when they hesitate in judgment.',
                '高い専門性を持つ立場であっても限界があることを示す典型的な文脈です。'
            ),
            (
                '親しい友人同士（　　　）、互いに踏み込んではならない礼儀や節度を守るべきである。',
                'といえども',
                ['にかまけて', 'にかこつけて', 'を皮切りに'],
                'Even among close friends, one should observe courtesy and moderation that must not be overstepped.',
                '「親しき仲にも礼儀あり」と同様に、甘えを戒める文脈でよく使われます。'
            ),
            (
                'たとえ{一分|いっぷん}の遅れ（　　　）、公共交通機関の運行においては重大な支障となり得る。',
                'といえども',
                ['はおろか', 'に先駆けて', 'そばから'],
                'Even a delay of a single minute can become a serious hindrance in the operation of public transportation.',
                '「たとえ＋最小限の例＋といえども」で、わずかな妥協も許されないことを強調します。'
            ),
        ],
    },
    31: {
        'formula': '名詞 ／ 普通形 ＋ <strong>とはいえ</strong>',
        'similar': '〜とはいっても / 〜けれども / 〜であることは事実だが',
        'wrong': (
            'もし明日雨が降るとはいえ、室内の展示会場なのでイベントは予定通り行います。',
            '「〜とはいえ」は既に成立している事実や一般的な認識を「確かに〜だが」と受け止める表現であり、「もし〜なら」という未確定の仮定条件には使えません。',
            '"〜とはいえ" concedes an established fact ("granted that X is true, still..."), so it cannot be used for hypothetical future conditions with もし.'
        ),
        'comp': (
            '〜といえども',
            'even if; even though (literary/emphatic)',
            '「〜といえども」は「いかに〜であっても」と仮定や極端な立場にも使えますが、「〜とはいえ」は現実の事実を一旦認めた上で「しかし実際は思うようにはいかない」と続けます。',
            'Unlike 〜といえども (which can be hypothetical), 〜とはいえ always acknowledges an actual fact before introducing a practical reservation.',
            '操作に慣れたとはいえ、精密な作業なので油断するとミスをしてしまう。',
        ),
        'quiz': [
            (
                '暦の{上|うえ}では立春を過ぎた（　　　）、北風が冷たくコートが手放せない{日|ひ}が続いている。',
                'とはいえ',
                ['とあっては', 'ともなると', 'とばかりに'],
                'Although we have passed the beginning of spring on the calendar, the north wind is cold and days when we cannot part with our coats continue.',
                '「事実として立春は過ぎたが、実際の体感はまだ寒い」と対比する最も代表的な例です。'
            ),
            (
                'リフォームして外観はきれいになった（　　　）、築五十年の木造住宅なので冬の寒さは厳しい。',
                'とはいえ',
                ['を皮切りに', 'に先駆けて', 'にかまけて'],
                'Although it has been renovated and the exterior looks clean, since it is a fifty-year-old wooden house, the winter cold is harsh.',
                '前件の肯定的な事実を認めつつ、なお残る問題点や限界を後件で述べます。'
            ),
            (
                '基礎的な文法をひと通り学んだ（　　　）、現地の新聞を辞書なしでスラスラ読むのはまだ難しい。',
                'とはいえ',
                ['はおろか', 'にかこつけて', 'そばから'],
                'Although I have learned basic grammar from start to finish, reading local newspapers fluently without a dictionary is still difficult.',
                '「〜とはいっても、まだ十分ではない」と控えめに現状を説明する際によく使われます。'
            ),
            (
                '徒歩圏内（　　　）、駅から緩やかな坂道を{二十五分|にじゅうごふん}も歩くので夏場の通勤はなかなかつらい。',
                'とはいえ',
                ['ならでは', 'ずくめ', 'まみれ'],
                'Although it is within walking distance, since you have to walk twenty-five minutes up a gentle slope from the station, commuting in summer is quite tough.',
                '名詞に直接接続し、言葉の上での条件と実際の苦労とのギャップを表します。'
            ),
        ],
    },
    32: {
        'formula': '数量詞（長さ・重さ・大きさ・深さ・距離） ＋ <strong>からある</strong> ＋ 名詞',
        'similar': '〜以上もある / 優に〜を超える',
        'wrong': (
            '昨日の講演会には三百人からある聴衆が集まり、会場は満席になった。',
            '「〜からある」は重さ・長さ・高さ・大きさなど連続的な規模を表す数量詞につき、人数・個数・金額には「〜からの」を使います。',
            '"〜からある" attaches to continuous physical measurements (weight, length, height, size), whereas headcounts, item counts, and money require "〜からの".'
        ),
        'comp': (
            '〜からの',
            'as many as; upwards of (people, items, money)',
            'どちらも数量の多さを強調しますが、「〜からある」は重さ・長さ・大きさ（三十キロからある荷物）に使い、「〜からの」は人数・金額（三千人からの観客）に使います。',
            'Both emphasize large quantities, but 〜からある is used for weight/length/size, while 〜からの is used for numbers of people, items, or sums of money.',
            '彼は三十キロからある登山用の荷物を背負って、険しい山道を登っていった。',
        ),
        'quiz': [
            (
                '神社の境内には、樹齢五百年を超える高さ三十メートル（　　　）大杉がそびえ立っている。',
                'からある',
                ['からの', 'ばかりの', 'なりの'],
                'In the shrine grounds towers a giant cedar tree over 500 years old and fully thirty meters tall.',
                '高さや長さなど、規模の大きさに驚きを込めて「少なくとも三十メートル以上ある」と述べる表現です。'
            ),
            (
                '引っ越しの作業員は、百キロ（　　　）重たいピアノを{二人|ふたり}がかりで慎重に運び出した。',
                'からある',
                ['からの', 'ずくめの', 'まみれの'],
                'The moving workers carefully carried out the heavy piano weighing well over a hundred kilograms between the two of them.',
                '重量の大きさを強調するときに「数量詞（キロ）＋からある＋名詞」の形が用いられます。'
            ),
            (
                '積雪が二メートル（　　　）豪雪地帯では、毎朝の雪かきだけでも大変な重労働になる。',
                'からある',
                ['からの', 'ごときの', 'まじき'],
                'In heavy snowfall areas where snow accumulation reaches two meters or more, just shoveling snow every morning becomes hard labor.',
                '深さや厚みの規模が並大抵ではないことを示す文脈です。'
            ),
            (
                '全長十メートル（　　　）巨大なクジラの骨格標本が、自然史博物館の中央ホールに展示されている。',
                'からある',
                ['からの', 'ならではの', 'ゆえの'],
                'A gigantic whale skeleton specimen measuring ten meters or more in total length is exhibited in the central hall of the natural history museum.',
                '全長・直径・面積などの計測値に添えて、その巨大さを印象づけます。'
            ),
        ],
    },
    33: {
        'formula': '数量詞（人数・金額・個数・年月） ＋ <strong>からの</strong> ＋ 名詞',
        'similar': '〜以上もの / 〜にも達する多くの',
        'wrong': (
            '庭の隅にあった五十キロからの大きな石を、父が一人で動かした。',
            '「〜からの」は人数・金額・個数・回数など数えられる数量や金額の多さを強調するときに使い、重さや長さには「〜からある」を使います。',
            '"〜からの" is used with countable numbers (people, items, days) or sums of money; physical weight or length requires "〜からある".'
        ),
        'comp': (
            '〜からある',
            'as much as; more than (weight, length, height)',
            '「〜からある」は重さ・長さ・高さなどの物理的な大きさに使い、「〜からの」は人数・金額・期間などの多さ（五千人からの応募者）に使います。',
            'While 〜からある is for physical dimensions (weight, length, height), 〜からの is for large headcounts, sums of money, or durations.',
            '全国から五千人からのランナーが集まり、市民マラソン大会が盛大に{開|ひら}かれた。',
        ),
        'quiz': [
            (
                '週末の野外音楽祭には一万人（　　　）観客が詰めかけ、会場は熱気に包まれた。',
                'からの',
                ['からある', 'ずくめの', 'まみれの'],
                'Upwards of ten thousand spectators flocked to the weekend outdoor music festival, filling the venue with excitement.',
                '人数の多さを強調し、「一万人以上もの」という意味を表す用法です。'
            ),
            (
                '重要文化財の修復工事には、数億円（　　　）費用と五年の歳月が費やされた。',
                'からの',
                ['からある', 'まじき', 'ごときの'],
                'Upwards of several hundred million yen in cost and five years of time were spent on the restoration work of the Important Cultural Property.',
                '金額の大きさを強調する際にも「数量詞＋からの＋名詞」が用いられます。'
            ),
            (
                'その作家の新作小説は発売からわずか一か月で五十万部（　　　）売り上げを記録した。',
                'からの',
                ['からある', 'ばかりの', 'にかまけた'],
                'The author\'s new novel recorded sales of upwards of 500,000 copies in just one month after its release.',
                '部数や個数が非常に多いことを驚きとともに伝える表現です。'
            ),
            (
                '今回の奨学生の募集には、わずか十名の枠に対して三百人（　　　）応募者が集まった。',
                'からの',
                ['からある', 'をよそにした', 'に先駆けた'],
                'For this scholarship recruitment, upwards of three hundred applicants gathered for just ten spots.',
                '予想を上回る多数の人が集まったことを示す典型的な文脈です。'
            ),
        ],
    },
    34: {
        'formula': '動詞辞書形・タ形 ＋ <strong>そばから</strong>',
        'similar': '〜するとすぐに（同じことが繰り返される） / 〜した端から',
        'wrong': (
            '目覚まし時計が鳴るそばから、私は飛び起きて朝の散歩に出かけた。',
            '「〜そばから」は「片付けるそばから散らかす」「覚えるそばから忘れる」のように、ある動作をしてもすぐに打ち消されたり同じことが何度も繰り返されたりする場面に使い、一回きりの素早い行動には使えません。',
            '"〜そばから" describes a repetitive cycle where an action is immediately undone or repeated (e.g., forgetting right after memorizing), not a single quick action.'
        ),
        'comp': (
            '〜が早いか',
            'the instant ~; no sooner had ~ than (single immediate action)',
            '「〜が早いか」は一回きりの瞬発的な行動を表しますが、「〜そばから」は「〜してもすぐまた…」という反復的・習慣的な徒労感を表す点が大きく異なります。',
            'While 〜が早いか depicts a single instantaneous action, 〜そばから expresses a repeated cycle, often with frustration that one\'s effort is immediately undone.',
            '新しい英単語を覚えるそばから忘れてしまうので、単語帳を何度も見返している。',
        ),
        'quiz': [
            (
                '秋が深まり、庭の落ち葉を掃いてきれいにする（　　　）また風が吹いて葉が散ってしまう。',
                'そばから',
                ['が早いか', 'や否や', 'なり'],
                'As autumn deepens, no sooner do I sweep the fallen leaves in the garden clean than the wind blows again and scatters more leaves.',
                'せっかく行った動作がすぐに元に戻ってしまう繰り返しの状況を表します。'
            ),
            (
                '幼い子どもたちは、おもちゃを箱に片付けた（　　　）また次のおもちゃを引っ張り出してくる。',
                'そばから',
                ['が早いか', 'や否や', 'とあっては'],
                'Young children pull out the next toy right after you put the toys away in the box.',
                '「片付けるそばから散らかす」は「〜そばから」の最も代表的な用例です。'
            ),
            (
                '専門用語が多くて難しく、メモを取りながら聞く（　　　）内容を忘れてしまいそうになる。',
                'そばから',
                ['ともなると', 'を皮切りに', 'に先駆けて'],
                'Because there are many technical terms and it is difficult, I feel like I am about to forget the content right as I listen and take notes.',
                '「聞くそばから忘れる」「読むそばから忘れる」のように、記憶の定着しにくさを嘆く文脈でよく使われます。'
            ),
            (
                '焼きたてのパンを店頭に並べる（　　　）次々と売れていき、昼前にはすべて完売した。',
                'そばから',
                ['はおろか', 'にかまけて', 'を踏まえて'],
                'No sooner were the freshly baked breads lined up in the storefront than they sold one after another, selling out completely before noon.',
                '補充してもすぐに売れていくという好ましい連続現象にも使うことができます。'
            ),
        ],
    },
    35: {
        'formula': '動詞辞書形・タ形 ＋ <strong>が早いか</strong>',
        'similar': '〜や否や / 〜と同時に / 〜なり / 〜たとたん',
        'wrong': (
            '春が来るが早いか、毎年この公園では色とりどりの花が少しずつ咲き始める。',
            '「〜が早いか」は前の出来事が起きた瞬間に、待ち構えていたかのように次の瞬間的動作が起きるという一回きりの描写に使われ、毎年の緩やかな変化には使えません。',
            '"〜が早いか" vividly describes a single, immediate, rapid action occurring the very instant the preceding event happens—not gradual annual changes.'
        ),
        'comp': (
            '〜そばから',
            'right after doing ~ (repeatedly undone/repeated)',
            '「〜そばから」は何度も繰り返される習慣的な事態を表しますが、「〜が早いか」は「ベルが鳴るが早いか飛び出した」のように一回の素早い行動を描写します。',
            'Unlike 〜そばから (repeated cycles), 〜が早いか captures a single moment of lightning-fast action right upon a trigger.',
            '終業のチャイムが鳴るが早いか、生徒たちは一斉に校庭へと飛び出していった。',
        ),
        'quiz': [
            (
                '開始の合図が鳴る（　　　）、選手たちは一斉にスタートラインから勢いよく駆け出した。',
                'が早いか',
                ['そばから', 'ともなると', 'とあっては'],
                'No sooner had the starting signal sounded than the athletes dashed out vigorously from the starting line all at once.',
                '合図とほぼ同時に素早い行動が起きる様子を{生|い}き{生|い}きと描写する表現です。'
            ),
            (
                '飼い犬は散歩用のリードを見る（　　　）、しっぽを振って玄関のドアの{前|まえ}へ走っていった。',
                'が早いか',
                ['そばから', 'はおろか', 'にかまけて'],
                'The instant the pet dog saw the walking leash, it wagged its tail and ran to the front door.',
                '視覚的なきっかけの直後に、反射的に次の動作へ移る場面でよく使われます。'
            ),
            (
                '家に帰り着いた（　　　）、息子はカバンを置いてすぐに友達と野球をしに出かけてしまった。',
                'が早いか',
                ['そばから', 'を皮切りに', 'を踏まえて'],
                'No sooner had my son arrived home than he put down his bag and immediately went out to play baseball with his friends.',
                '辞書形だけでなくタ形「〜たが早いか」の形でも接続できます。'
            ),
            (
                '劇場の幕が下りる（　　　）、客席からは出演者を称える割れんばかりの拍手が沸き起こった。',
                'が早いか',
                ['そばから', 'にかこつけて', 'に先駆けて'],
                'The moment the theater curtain came down, thunderous applause praising the performers erupted from the audience.',
                '待ちきれなかったかのように直後に反応が起きる緊迫感や感動を表します。'
            ),
        ],
    },
    36: {
        'formula': '動詞辞書形 ＋ <strong>や否や</strong>',
        'similar': '〜が早いか / 〜と同時に / 〜するかしなかのうちに',
        'wrong': (
            '家に帰ったや否や、すぐに手を洗って夕食の支度を始めた。',
            '「〜や否や」は必ず動詞の辞書形（基本形）に接続します。タ形（帰った）に直接つなげることはできません。',
            '"〜や否や" must attach to the dictionary form of a verb (帰るや否や); it cannot attach to the past/ta-form (帰った).'
        ),
        'comp': (
            '〜なり',
            'immediately upon doing ~ (same subject, unexpected action)',
            '「〜なり」は前件と後件の主語が同じ人物に限られますが、「〜や否や」は「扉が開くや否や客がなだれ込んだ」のように前件と後件の主語が異なっても使えます。',
            'While 〜なり requires the same human subject in both clauses, 〜や否や allows different subjects (e.g., "the moment the door opened, customers rushed in").',
            '列車がホームに到着するや否や、待ち構えていた乗客が次々と乗り込んだ。',
        ),
        'quiz': [
            (
                '開店時刻になって扉が{開|あ}く（　　　）、外で並んでいた買い物客が一斉に店内へ入った。',
                'や否や',
                ['そばから', 'なり', 'ともなると'],
                'The moment opening time arrived and the doors opened, the shoppers waiting in line outside entered the store all at once.',
                '「扉が開く」と「買い物客が入る」のように、主語が異なる二つの出来事の同時性を表せます（主語が異なるため「〜なり」は不可）。'
            ),
            (
                '{空|そら}が急に暗くなり冷たい風が吹く（　　　）、大粒の雨が激しく地面を打ち始めた。',
                'や否や',
                ['そばから', 'なり', 'とあっては'],
                'No sooner had the sky suddenly darkened and a cold wind blown than large raindrops began beating hard against the ground.',
                '自然現象が立て続けに起こる緊迫した場面の描写にもよく用いられます。'
            ),
            (
                '優勝決定の知らせが届く（　　　）、控え室にいた部員たちは互いに肩を抱き合って喜んだ。',
                'や否や',
                ['そばから', 'なり', 'はおろか'],
                'The moment the news of winning the championship arrived, the club members in the waiting room hugged each other\'s shoulders in joy.',
                '知らせが届いたその瞬間に歓喜の反応が起きたことを格調高く表します。'
            ),
            (
                '山頂の雲が切れて朝{日|ひ}が昇る（　　　）、あたり一面の雪原が黄金色に輝き始めた。',
                'や否や',
                ['そばから', 'なり', 'にかまけて'],
                'The instant the clouds at the summit parted and the morning sun rose, the snowfield all around began shining in golden hues.',
                '前の動作が完了するかしないかの瞬間に次の現象が生じることを示します。'
            ),
        ],
    },
    37: {
        'formula': '動詞辞書形 ＋ <strong>なり</strong>',
        'similar': '〜とすぐに（そのまま次の動作をする） / 〜たとたんに',
        'wrong': (
            '朝のチャイムが鳴るなり、生徒たちは自分の席に着いて静かに読書を始めた。',
            '「動詞＋なり」は前件と後件が「同じ主語（主に第三者）」でなければならず、チャイムと生徒のように主語が異なる文には使えません。',
            '"Verb + なり" requires the same human subject for both clauses; it cannot connect two clauses with different subjects like "the chime rang" and "the students sat down."'
        ),
        'comp': (
            '〜や否や',
            'the moment ~; as soon as ~',
            '「〜や否や」は前件・後件の主語が違っても使えますが、「〜なり」は同一主語が「Aした状態のまま続けてすぐBという（やや意外な）行動をとる」場面に限られます。',
            'Unlike 〜や否や (which allows different subjects), 〜なり requires the same subject performing an immediate, often surprising action right after the first.',
            '弟は帰宅するなり、一言も話さずに自分の部屋へ入って眠ってしまった。',
        ),
        'quiz': [
            (
                '長旅でよほど疲れていたのか、兄は帰宅する（　　　）ソファに横になって眠ってしまった。',
                'なり',
                ['そばから', 'ともなると', 'とあっては'],
                'Perhaps exhausted from the long trip, my older brother lay down on the sofa and fell asleep the moment he got home.',
                '同一人物が「帰宅する」とすぐに続けて次の動作（眠る）に移ったことを表します。'
            ),
            (
                '親友は私の顔を見る（　　　）、今日あったうれしい出来事を早口で一気に話し始めた。',
                'なり',
                ['そばから', 'はおろか', 'にかまけて'],
                'The moment my best friend saw my face, she began talking rapidly all at once about the happy event that happened today.',
                '「顔を見るなり〜し始めた」は、挨拶も省いてすぐ次の行動に出る様子を描く定番表現です。'
            ),
            (
                '受話器を取る（　　　）相手が用件を切り出したので、こちらは名乗るタイミングを逃してしまった。',
                'なり',
                ['そばから', 'を皮切りに', 'を踏まえて'],
                'Because the other party brought up their business the instant they picked up the receiver, I missed the timing to give my name.',
                '予想外の素早い行動に少し驚いたニュアンスが含まれることが多い表現です。'
            ),
            (
                '幼い娘は祖父から届いた小包を{開|あ}ける（　　　）、中に入っていた絵本を夢中で読み始めた。',
                'なり',
                ['そばから', 'に先駆けて', 'にかこつけて'],
                'The moment my young daughter opened the parcel from her grandfather, she eagerly began reading the picture book inside.',
                '前の動作の勢いのまま、間を置かずに次の動作へ移る様子を鮮やかに切り取ります。'
            ),
        ],
    },
    38: {
        'formula': '動詞ナイ形語幹（する → せん） ＋ <strong>んばかりだ</strong> ／ <strong>んばかりの</strong> ＋ 名詞 ／ <strong>んばかりに</strong>',
        'similar': '今にも〜しそうな様子で / 〜と言わんばかりに / まるで〜しそうなほど',
        'wrong': (
            '明日は雨が降らんばかりだから、洗濯物は今日のうちに干しておこう。',
            '「〜んばかり」は目の前の様子が「今にも〜しそうなほど極端である」という比喩的な強調表現であり、明日の天気予報のような単なる推量には使えません。',
            '"〜んばかり" is a vivid figurative description of something visibly on the verge of happening right before one\'s eyes, not a simple forecast about tomorrow.'
        ),
        'comp': (
            '〜とばかりに',
            'as if to say ~ (showing attitude through action)',
            '「〜とばかりに」は言葉で「〜だ」と言っているかのような態度を表し、「〜んばかりに」は今にもその動作をしそうなほど程度が激しい様子を表します。',
            'While 〜とばかりに means acting "as if to say X," 〜んばかりに describes a state so intense that action X seems on the verge of happening ("almost bursting").',
            '会場は立ち見が出るほどの盛況で、熱気にあふれんばかりだった。',
        ),
        'quiz': [
            (
                '素晴らしい演奏が終わると、会場中に割れん（　　　）拍手と歓声が鳴り響いた。',
                'ばかりの',
                ['ごときの', 'まじき', 'ずくめの'],
                'When the wonderful performance ended, thunderous applause and cheers echoed throughout the venue as if the hall might split open.',
                '「割れんばかりの拍手」は、会場が割れてしまいそうなほど激しい拍手を表す代表的な慣用表現です。'
            ),
            (
                '十年ぶりに再会した旧友は、涙を流さん（　　　）に私の手を強く握りしめて喜んでくれた。',
                'ばかり',
                ['まみれ', 'ならでは', 'ごとき'],
                'Reunited after ten years, my old friend grasped my hands tightly and rejoiced, looking on the verge of tears.',
                '実際には泣いていなくても、今にも涙を流しそうなほど感激している様子を表します。'
            ),
            (
                '何か言いたげにこちらを見つめる彼の表情は、「早く理由を説明してほしい」と言わん（　　　）だった。',
                'ばかり',
                ['ずくめ', 'まじき', 'なり'],
                'His expression as he gazed at me as if wanting to say something was practically saying, "Please explain the reason quickly."',
                '「〜と言わんばかりだ」は、言葉に出さずとも表情や態度がそれを物語っている様子を示します。'
            ),
            (
                '改札口からあふれん（　　　）の乗客が次々と出てきて、駅前広場はたちまち人で埋まった。',
                'ばかり',
                ['まみれ', 'ゆえ', 'おろか'],
                'Passengers practically overflowing from the ticket gates came out one after another, and the station square quickly filled with people.',
                '「あふれんばかりの＋名詞」で、収まりきらないほど満ちている状態を描写します。'
            ),
        ],
    },
    39: {
        'formula': '（引用句・普通形） ＋ <strong>とばかりに</strong>',
        'similar': '「〜」と言わんばかりに / いかにも「〜だ」という態度で',
        'wrong': (
            '先生は「よく頑張ったね」とばかりに、実際に大きな声で私を褒めてくれた。',
            '「〜とばかりに」は「実際には言葉に出していないが、まるでそう言っているかのような態度や行動で示す」という意味なので、実際に声に出して言った場合には使えません。',
            '"〜とばかりに" means acting as though saying something without actually speaking the words aloud; it cannot be used when the person literally says it.'
        ),
        'comp': (
            '〜んばかりに',
            'as if about to ~ (on the verge of doing)',
            '「〜んばかりに」は動詞の未然形について今にもその動作をしそうな様子を表しますが、「〜とばかりに」は心の中のセリフや主張を態度で示す場面に使います。',
            'While 〜んばかりに attaches to verb stems ("on the verge of doing"), 〜とばかりに follows a quoted phrase or clause ("acting as if to say \'...\'").',
            '「このチャンスを逃すものか」とばかりに、彼は真っ先に手を挙げて発言した。',
        ),
        'quiz': [
            (
                '猫は「おなかが{空|す}いた」と（　　　）、{空|から}になった食器の{前|まえ}に座ってこちらをじっと見上げた。',
                'ばかりに',
                ['あっても', 'いえども', '相まって'],
                'As if to say "I\'m hungry," the cat sat in front of its empty dish and stared up at me.',
                '言葉を話さない動物の仕草を、まるでそう訴えているかのように描写する典型例です。'
            ),
            (
                '彼はこの時を待っていたと（　　　）、質疑応答が始まった瞬間に立ち上がって質問した。',
                'ばかりに',
                ['おろか', 'かまけて', '先駆けて'],
                'As if to say he had been waiting for this very moment, he stood up and asked a question the instant the Q&A session began.',
                '「待っていたとばかりに」「ここぞとばかりに」は非常によく使われる定型表現です。'
            ),
            (
                '長時間の会議が終わると、参加者は「やっと終わった」と（　　　）一斉に深い息をついた。',
                'ばかりに',
                ['かこつけて', '踏まえて', '皮切りに'],
                'When the long meeting ended, the participants all let out a deep breath at once, as if to say "It\'s finally over."',
                '口には出さないものの、全員の態度から本音がはっきりと伝わってくる場面です。'
            ),
            (
                '妹は自分の出番だと（　　　）自信に満ちた笑顔でステージの中央へと歩み出た。',
                'ばかりに',
                ['よそに', 'ものともせず', 'いたっては'],
                'As if to say it was her turn to shine, my younger sister stepped out to the center of the stage with a confident smile.',
                '表情や振る舞いからその人の強い意気込みが感じ取れる様子を表します。'
            ),
        ],
    },
    40: {
        'formula': '名詞 ＋ <strong>めく</strong>（<strong>めいて</strong> ／ <strong>めいた</strong> ＋ 名詞）',
        'similar': '〜らしくなる / 〜のような気配を帯びる / 〜じみる',
        'wrong': (
            '弟は最近背が伸びて、すっかり大人めいて見えるようになった。',
            '「〜めく」は季節の兆し（春めく）や抽象的な雰囲気（謎めく・皮肉めく・冗談めく）に使われる語であり、人間の成長や年齢相応の様子には「〜びる（大人びる）」や「〜らしくなる」を使います。',
            '"〜めく" is used for seasonal signs (spring-like) or abstract atmospheres (mysterious, ironic, joking), not for human age/growth like looking like a high schooler.'
        ),
        'comp': (
            '〜びる',
            'to look/seem (mature, rustic, old-fashioned)',
            '「〜びる」は「大人びる」「田舎びる」「古びる」など極めて限られた語について性質の定着を表しますが、「〜めく」は季節の変化や「冗談めいた話」などの気配を表します。',
            'While 〜びる attaches to only a few stems (大人びる, 古びる), 〜めく expresses seasonal transitions (春めく) or an air/tone (謎めいた, 冗談めいた).',
            '三月中旬になり、日差しの温かさにようやく春めいた気配が感じられるようになった。',
        ),
        'quiz': [
            (
                '梅の花がほころび始め、吹く風にもようやく春（　　　）暖かさが感じられるようになった。',
                'めいた',
                ['びた', 'ぶった', 'じみた'],
                'As the plum blossoms begin to open, a spring-like warmth can finally be felt even in the blowing breeze.',
                '「春めく」「秋めく」は季節の気配が感じられるようになることを表す代表的な表現です。'
            ),
            (
                '彼は何もかも知っているかのように、謎（　　　）微笑みを浮かべて静かにうなずいた。',
                'めいた',
                ['びた', 'ぶった', 'まじき'],
                'As if knowing everything, he wore an enigmatic smile and nodded quietly.',
                '「謎めいた微笑み／言葉」は、どこか神秘的で意味深長な雰囲気を表す頻出表現です。'
            ),
            (
                '厳しい指摘も冗談（　　　）口調で柔らかく伝えてくれたので、場の空気が和らいだ。',
                'めいた',
                ['びた', 'ずくめの', 'まみれの'],
                'Because even the strict feedback was conveyed gently in a joking tone, the atmosphere in the room softened.',
                '「冗談めいた」「皮肉めいた」のように、発言の調子やニュアンスを表す際によく使われます。'
            ),
            (
                '九月に入って朝晩の風が涼しくなり、街路樹の葉も少しずつ秋（　　　）きた。',
                'めいて',
                ['びて', 'ぶって', 'きって'],
                'Entering September, the morning and evening breezes have grown cool, and the leaves of the street trees have gradually begun to take on an autumnal air.',
                '「秋めいてくる」「春めいてくる」の形で、季節の移り変わりを叙情的に描写します。'
            ),
        ],
    },
    41: {
        'formula': '名詞 ／ イ形容詞語幹 ／ ナ形容詞語幹 ＋ <strong>ぶる</strong>（<strong>ぶって</strong> ／ <strong>ぶった</strong> ＋ 名詞）',
        'similar': '〜のふりをする / 〜のように見せかける / 気取る',
        'wrong': (
            '彼女は長年の努力で本当に多くの知識を身につけ、すっかり学者ぶっている。',
            '「〜ぶる」は「本当はそうではないのに、自分を大きく見せるためにそのように振る舞う（気取る）」というマイナスの評価を含むため、本物の実力者を褒める文には使えません。',
            '"〜ぶる" carries critical nuance ("putting on airs; pretending to be something one isn\'t"), so it cannot be used to praise genuine expertise.'
        ),
        'comp': (
            '〜びる',
            'to seem mature / take on a natural air',
            '「〜びる（大人びる）」は自然にその雰囲気が備わっている様子を中立〜肯定的に表しますが、「〜ぶる（大人ぶる・上品ぶる）」は意識的に背伸びして見せかける態度を表します。',
            'While 〜びる (大人びる) describes a natural, genuine air of maturity, 〜ぶる (大人ぶる) criticizes consciously putting on airs or pretending.',
            '何でも知っているかのように専門家ぶった口をきくのはやめた{方|ほう}がいい。',
        ),
        'quiz': [
            (
                '自分が苦労して手伝ったのに、彼は何も言わずにいい人（　　　）こともなく静かに去っていった。',
                'ぶる',
                ['びる', 'めく', 'じみる'],
                'Even though he went to great lengths to help, he quietly left without saying anything or trying to act like a saint.',
                '「いい人ぶる」「善人ぶる」は、自分を良く見せようと意識的に振る舞うことを表します。'
            ),
            (
                '少し専門書を読んだくらいで、周囲の人に学者（　　　）態度をとるのは感心しない。',
                'ぶった',
                ['びた', 'めいた', 'まじき'],
                'Putting on scholarly airs toward people around you just because you have read a few specialized books is not admirable.',
                '実際以上の知識や地位があるかのように見せかける態度をたしなめる文脈です。'
            ),
            (
                '彼女はどんなに高い役職に就いても決して偉（　　　）ところがなく、誰に対しても気さくだ。',
                'ぶる',
                ['びる', 'めく', 'ずくめ'],
                'No matter how high a position she attains, she never puts on airs of importance and is friendly toward everyone.',
                '「偉ぶる」「上品ぶる」のように、イ形容詞・ナ形容詞の語幹にも接続します。'
            ),
            (
                'よく知らない分野の話題で知ったか（　　　）と、後で思わぬ恥をかくことになる。',
                'ぶりをする',
                ['びる', 'めく', 'まみれになる'],
                'If you pretend to know all about a topic in a field you are not familiar with, you will end up embarrassing yourself unexpectedly later.',
                '「知ったかぶり（をする）」は日常会話から文章まで頻出する最重要慣用表現です。'
            ),
        ],
    },
    42: {
        'formula': '名詞（大人・田舎・鄙など） ／ 動詞連用形（古びる） ＋ <strong>びる</strong>（<strong>びた</strong> ＋ 名詞 ／ <strong>びて</strong>）',
        'similar': '〜らしく見える / 〜の趣を帯びる / 自然と〜の風情がある',
        'wrong': (
            '彼は難しい本を片手に持って、わざと大人びた態度で友人に自慢した。',
            'わざと意識して背伸びする動作には「大人ぶる」を使います。「大人びる」は内面や外見が自然と大人らしく落ち着いた様子に見えることを表すため、「わざと」とは共起しません。',
            'Deliberately acting grown-up requires "大人ぶる". "大人びる" describes naturally appearing mature or settled, so it cannot pair with "on purpose (わざと)".'
        ),
        'comp': (
            '〜ぶる',
            'to pretend to be ~; to put on airs',
            '「大人ぶる」は子どもが背伸びして大人のふりをすることですが、「大人びる」は年齢の割に自然と落ち着いて大人っぽく見えるという良い・中立的な評価です。',
            'While 大人ぶる means a child consciously acting like an adult, 大人びる means naturally looking or sounding mature beyond one\'s years.',
            '久しぶりに会った姪は、話し{方|かた}も落ち着いてすっかり大人びた印象になっていた。',
        ),
        'quiz': [
            (
                '小学生の頃から彼女はどこか大人（　　　）雰囲気があり、周囲の友達から頼りにされていた。',
                'びた',
                ['ぶった', 'めいた', 'まみれの'],
                'Even since elementary school she had a somewhat mature air about her and was relied upon by the friends around her.',
                '「大人びた雰囲気／顔つき／口調」は、実年齢よりも落ち着いて見える様子を表す最も代表的な例です。'
            ),
            (
                '山あいの鄙（　　　）温泉宿で、川のせせらぎを聞きながら静かな休日を過ごした。',
                'びた',
                ['ぶった', 'めいた', 'ずくめの'],
                'At a rustic hot spring inn nestled in the mountains, I spent a quiet holiday listening to the murmuring of the stream.',
                '「鄙（ひな）びた」は、都会から離れて素朴で落ち着いた風情があることを表すN1頻出語です。'
            ),
            (
                '商店街の角にある古（　　　）看板の喫茶店は、半世紀にわたり地元の人々に愛されている。',
                'びた',
                ['ぶった', 'めいた', 'まじき'],
                'The coffee shop with the timeworn signboard on the corner of the shopping street has been loved by locals for half a century.',
                '「古びた」は年月を経て古くなっているが、味わい深さがある建物や品物によく使われます。'
            ),
            (
                '都会の喧騒を離れ、どこか田舎（　　　）穏やかな風景の{中|なか}をゆっくりと散策した。',
                'びた',
                ['ぶった', 'めいた', 'ごときの'],
                'Leaving the hustle and bustle of the city behind, I strolled leisurely through a gentle, somewhat rustic landscape.',
                '「大人びた」「古びた」「鄙びた」「田舎びた」の四つが試験で問われる主要な形です。'
            ),
        ],
    },
}

GRAMMAR = DATA

