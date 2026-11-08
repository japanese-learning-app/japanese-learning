# -*- coding: utf-8 -*-
"""
N1 grammar data part B (gids 43-84).
"""

GRAMMAR = {
    43: {
        'formula': 'イ形容詞語幹・ナ形容詞語幹・動詞ます形 ＋ <strong>げ（だ／な／に）</strong>',
        'similar': '〜そうだ / 〜らしい / 〜のような様子で',
        'wrong': (
            '私は今日の試験に合格できて、とても嬉しげだ。',
            '「〜げ」は他人の表情や態度を外から見て「〜のような様子だ」と描写する表現なので、話し手自身の現在の感情には使えません。',
            '"〜げ" describes someone else\'s outward appearance or demeanor from an observer\'s perspective, so it cannot be used for the speaker\'s own current feelings.'
        ),
        'comp': (
            '〜そうだ（様態）',
            'looks like; appears to be',
            '外見から受ける印象を広く表す日常表現で、人以外の物事（雨が降りそうだ等）にも使えます。',
            'A general everyday expression for outward impressions that also applies to non-human states like weather.',
            '窓の外を見ると、今にも大粒の雨が降り出しそうな暗い雲が広がっていた。',
        ),
        'quiz': [
            (
                '彼女は何か（　　　）こちらを見つめていたが、結局何も言わずに部屋を出ていった。',
                '言いたげに',
                ['言いがちに', '言わんばかりで', '言うきらいがあり'],
                'She was gazing at me as if she wanted to say something, but in the end she left the room without saying a word.',
                '「言いたい＋げ」で、何か言いたそうな様子が表情や態度に表れていることを示します。'
            ),
            (
                '長年暮らした街を離れる{日|ひ}、彼は（　　　）駅のホームから遠くの山々を眺めていた。',
                '名残惜しげに',
                ['名残惜しめいて', '名残惜しぶって', '名残惜しびて'],
                'On the day he left the town where he had lived for many years, he gazed wistfully at the distant mountains from the station platform.',
                '別れを惜しむ気持ちが外見や立ち振る舞いににじみ出ている様子を描写します。'
            ),
            (
                '初めての発表会を終えた子どもたちは、舞台の上で（　　　）胸を張って微笑んでいた。',
                '誇らしげに',
                ['誇らしじみて', '誇らしきらいに', '誇らしがてら'],
                'Having finished their very first recital, the children smiled and puffed out their chests proudly on stage.',
                '誇らしいと感じている様子が周囲から見てもはっきりわかる場面で使われます。'
            ),
            (
                'ベンチに座った老人は、夕暮れの公園を（　　　）眺めながら静かにため息をついた。',
                '寂しげに',
                ['寂しぶって', '寂しびて', '寂しめいて'],
                'The elderly man sitting on the bench sighed quietly while gazing lonely at the park at dusk.',
                '形容詞「寂しい」の語幹について、どこか寂しそうな雰囲気が漂う様子を表します。'
            ),
        ],
    },
    44: {
        'formula': '名詞 ＋ <strong>じみた</strong> ／ <strong>じみてくる</strong>',
        'similar': '〜めいた / 〜のような / 〜っぽい',
        'wrong': (
            '彼女の新作小説は、春じみた爽やかな風を感じさせる名作だ。',
            '「〜じみた」は「子どもじみた」「年寄りじみた」など、あまり好ましくない傾向や皮肉なニュアンスを含む場面で使うため、純粋な称賛には向きません。',
            '"〜じみた" carries a somewhat negative or critical nuance (like childish or overly old-fashioned), so it does not fit pure praise such as a refreshing spring breeze.'
        ),
        'comp': (
            '〜めいた',
            'having the air of; hinting at',
            '季節の兆しや詩的・肯定的な雰囲気（「春めいた」「謎めいた」など）を表すのに使われます。',
            'Used for seasonal signs or poetic/intriguing atmospheres such as "spring-like" or "mysterious."',
            '三月の声を聞くと、日差しの暖かさの中にどことなく春めいた気配が感じられる。',
        ),
        'quiz': [
            (
                'もう社会人なのだから、自分の失敗を人のせいにするような（　　　）言い訳はやめなさい。',
                '子どもじみた',
                ['子どもびた', '子どもげな', '子どもめいた'],
                'Since you are already a working adult, stop making childish excuses like blaming your own mistakes on others.',
                '大人なのに子どものようで未熟だ、と批判的に述べる典型的な表現です。'
            ),
            (
                '単なる意見交換の場だったはずが、次第に（　　　）長い話になって皆がうんざりした。',
                '説教じみた',
                ['説教げな', '説教びた', '説教ぶった'],
                'What was supposed to be a simple exchange of opinions gradually turned into a preachy, drawn-out lecture that left everyone fed up.',
                '本来はそうではないのに、まるで説教のような嫌な感じを帯びていることを表します。'
            ),
            (
                'まだ三十代になったばかりなのに、最近はどうも（　　　）趣味ばかり好むようになった。',
                '年寄りじみた',
                ['年寄りげな', '年寄りびた', '年寄りぶった'],
                'Even though I have only just entered my thirties, lately I have come to prefer tastes that seem rather old-fashioned.',
                '年齢不相応に老け込んだ印象があることを自嘲や軽い皮肉を込めて述べています。'
            ),
            (
                '彼の提案は一見すると斬新だが、よく聞くと（　　　）話で現実味に欠けている。',
                '冗談じみた',
                ['冗談げな', '冗談びた', '冗談ぶった'],
                'His proposal looks novel at first glance, but when you listen closely, it sounds almost like a joke and lacks realism.',
                '真剣な議論の場で「まるで冗談のようで頼りない」とマイナス評価を下す用法です。'
            ),
        ],
    },
    45: {
        'formula': '動詞辞書形・ない形 ／ 名詞＋の ＋ <strong>きらいがある</strong>',
        'similar': '〜傾向がある / 〜がちだ / 〜恐れがある',
        'wrong': (
            '彼は毎朝欠かさずジョギングをして健康を保つきらいがある。',
            '「〜きらいがある」は好ましくない傾向や欠点・偏りを指摘する表現なので、健康維持のような良い習慣には使えません。',
            '"〜きらいがある" points out an undesirable tendency or bias, so it cannot be used for positive habits like maintaining one\'s health.'
        ),
        'comp': (
            '〜がちだ',
            'apt to; prone to',
            '病気や忘れ物など、望ましくない事柄が頻繁に起こる様子を表す日常的な表現です。',
            'A more everyday expression indicating that an undesirable event or state occurs frequently.',
            '冬場は空気が乾燥するため、喉の調子を崩しがちになるので加湿器を使っている。',
        ),
        'quiz': [
            (
                'あの評論家は自分の専門分野になると、少し独断に（　　　）と指摘されている。',
                '陥るきらいがある',
                ['陥る始末だ', '陥るに足る', '陥るにほかならない'],
                'That critic is pointed out as having a tendency to fall into dogmatism when it comes to his own specialty.',
                '人間の思考や行動における「望ましくない偏り・癖」を客観的に批評する表現です。'
            ),
            (
                '若い世代だけでなく、現代人はとかく目先の便利さばかりを（　　　）のではないだろうか。',
                '追い求めるきらいがある',
                ['追い求めるに忍びない', '追い求めるまでもない', '追い求めるにかたくない'],
                'Not only the younger generation, modern people in general seem to have an undesirable tendency to pursue only immediate convenience.',
                '「とかく〜きらいがある」の形で、世間一般の陥りやすい欠点を述べる際によく使われます。'
            ),
            (
                '彼は誠実な性格だが、慎重すぎるあまり大事な場面で決断を（　　　）。',
                '先送りするきらいがある',
                ['先送りするに堪える', '先送りするにすぎない', '先送りするにとどまらない'],
                'He has an honest personality, but because he is overly cautious, he tends to postpone decisions at crucial moments.',
                '長所の裏返しとして見られる行動上の弱点や欠点を穏やかに指摘しています。'
            ),
            (
                '専門家の報告書は正確さを重視するあまり、一般の読者には表現が難解に（　　　）。',
                'なりすぎるきらいがある',
                ['なりすぎるにかぎる', 'なりすぎるに足る', 'なりすぎるにとどまる'],
                'Because expert reports place so much emphasis on accuracy, their phrasing tends to become overly difficult for general readers.',
                '文章や制度などの特徴について、少し行き過ぎたマイナス面があることを示します。'
            ),
        ],
    },
    46: {
        'formula': '動詞辞書形・た形 ＋ <strong>始末だ</strong>',
        'similar': '〜ありさまだ / 〜結果になってしまった / 〜ざまだ',
        'wrong': (
            '彼は三年間毎日欠かさず勉強を続け、ついに首席で合格する始末だ。',
            '「〜始末だ」は悪いことが重なって最終的に情けない・困った結果に至ったことを嘆く表現なので、立派な成功には使えません。',
            '"〜始末だ" laments ending up in a shameful or troublesome state after things go wrong, so it cannot be used for admirable achievements.'
        ),
        'comp': (
            '〜あげく（に）',
            'after a long process of; in the end',
            '「〜あげく」は苦労や迷いの末に別の結果（主に悪い結果）になる経過を表し、文末ではなく文中で使います。',
            'Used mid-sentence to show a long process of trouble leading to an outcome, whereas 〜始末だ is a sentence-final lament.',
            '何時間も道に迷ったあげく、予約していた最終の観光バスに乗り遅れてしまった。',
        ),
        'quiz': [
            (
                '弟は新しいパソコンを買ったのに使いこなせず、今では箱に入れたまま（　　　）。',
                '放置する始末だ',
                ['放置するきらいがある', '放置するに足る', '放置するにほかならない'],
                'My younger brother bought a new computer but could not master it, and now he has ended up leaving it neglected in its box.',
                'せっかく買ったのに結局こんな困った状態になってしまった、という呆れや嘆きを表します。'
            ),
            (
                '修理代を節約しようと自分で時計を分解したら、元に戻せなくなって結局新品を（　　　）。',
                '買い直す始末だ',
                ['買い直すに堪える', '買い直すにとどまらない', '買い直すに及ばない'],
                'When I took my watch apart myself to save on repair costs, I could not put it back together and ended up having to buy a brand-new one.',
                '良かれと思ってやったことが裏目に出て、かえって悪い結果に終わった場面で使われます。'
            ),
            (
                '彼は連日の遅刻を注意されたにもかかわらず反省せず、ついには会議を無断で（　　　）。',
                '欠席する始末だ',
                ['欠席するにすぎない', '欠席するまでもない', '欠席するにかたくない'],
                'Despite being warned about being late day after day, he showed no remorse and finally ended up skipping the meeting without notice.',
                '悪い行動がエスカレートして、最終的にもっとひどい事態に至ったことを非難しています。'
            ),
            (
                '無計画に予算を使い続けた結果、年度の後半には必要な備品すら（　　　）。',
                '買えなくなる始末だ',
                ['買えなくなるに足る', '買えなくなるに忍びない', '買えなくなるにとどまる'],
                'As a result of continuing to spend the budget without a plan, by the second half of the fiscal year they ended up unable to buy even necessary supplies.',
                'ずさんな管理の末に招いた困った結末を呆れた調子で述べる表現です。'
            ),
        ],
    },
    47: {
        'formula': '動詞ます形 ＋ <strong>っぱなし（だ／の）</strong>',
        'similar': '〜たまま / 〜た状態で放置する / 〜続ける',
        'wrong': (
            'この美術館では、世界中から集められた名画が美しく飾られっぱなしだ。',
            '「〜っぱなし」は本来片付けたり止めたりすべきものを放置しているというマイナスの評価を含むため、適切な展示状態には使えません。',
            '"〜っぱなし" implies leaving something neglected when it should be tidied up or stopped, so it cannot describe a properly maintained museum exhibition.'
        ),
        'comp': (
            '〜たまま',
            'remaining in the state of having done',
            '良い・悪いの評価を含まず、単に前の状態が変化せずに続いていることを中立的に表します。',
            'Neutrally states that a previous state remains unchanged, without necessarily implying neglect or criticism.',
            '昨日は疲れていたため、机の上のスタンドを点けたまま朝まで眠ってしまった。',
        ),
        'quiz': [
            (
                'リビングのテレビが誰にも見られないまま朝からずっと（　　　）になっていた。',
                'つけっぱなし',
                ['つけがてら', 'つけそびれ', 'つけかたわら'],
                'The living room TV had been left on since morning without anyone watching it.',
                '本来消すべき電源や照明をそのまま放置している状態を表す代表的な例です。'
            ),
            (
                '子どもたちは部屋中におもちゃを（　　　）にして、公園へ遊びに行ってしまった。',
                '散らかしっぱなし',
                ['散らかしがてら', '散らかしそびれ', '散らかしかたがた'],
                'The children left their toys scattered all over the room and went off to play in the park.',
                '後片付けをせずにそのまま放っておく好ましくない行動を指摘しています。'
            ),
            (
                '今日の展示会では朝から夕方まで受付に（　　　）だったので、足がすっかり疲れてしまった。',
                '立ちっぱなし',
                ['立ちがてら', '立ちそびれ', '立ちかたわら'],
                'Because I was kept standing at the reception desk from morning till evening at today\'s exhibition, my legs got completely tired.',
                '座って休む暇もなく同じ姿勢が長時間続いて大変だった、というニュアンスを表します。'
            ),
            (
                '友人から借りた大切な本を半年も（　　　）にしていたことに気づき、慌てて連絡した。',
                '借りっぱなし',
                ['借りがてら', '借りそびれ', '借りかたがた'],
                'Realizing that I had kept an important book borrowed from a friend for half a year without returning it, I hurriedly contacted them.',
                '「借りたら返すべきなのに、返さないまま放置している」という反省の文脈で使われます。'
            ),
        ],
    },
    48: {
        'formula': '動詞ない形（ない → ず） ＋ <strong>にはすまない</strong> （※する → せずにはすまない）',
        'similar': '〜ないではすまない / 〜ざるを得ない / 〜なければならない',
        'wrong': (
            'こんなに天気が良い休日は、近くの海へドライブに行かずにはすまない。',
            '「〜ずにはすまない」は社会的責任や義理・道徳上「そうしなければ許されない」という義務感を表すため、個人の楽しい娯楽には使えません。',
            '"〜ずにはすまない" expresses social or moral obligation ("cannot get away without doing"), not a personal desire for leisure.'
        ),
        'comp': (
            '〜ずにはいられない',
            'cannot help doing; cannot resist',
            '義務や周囲の目ではなく、自分の内側から湧き上がる感情や衝動を抑えられないことを表します。',
            'Focuses on an irresistible internal urge or emotion rather than external social responsibility.',
            '彼女のひたむきに努力する姿を見ると、心から応援せずにはいられない気持ちになる。',
        ),
        'quiz': [
            (
                '自分の不注意で大切な書類を紛失してしまった以上、上司に正直に（　　　）。',
                '報告せずにはすまない',
                ['報告せずにはおかない', '報告するに忍びない', '報告するきらいがある'],
                'Now that I have lost an important document through my own carelessness, I cannot get away without reporting it honestly to my boss.',
                '組織のルールや責任上、報告しないまま終わらせることは許されないという状況を示します。'
            ),
            (
                '借りたカメラをうっかり落として壊してしまったからには、同じものを（　　　）だろう。',
                '弁償せずにはすまない',
                ['弁償するに足らない', '弁償するまでもない', '弁償するにとどまらない'],
                'Since I accidentally dropped and broke the camera I borrowed, I probably cannot get away without compensating for it with an identical one.',
                '常識や道義的な観点から「当然償わなければならない」と判断する場面で使われます。'
            ),
            (
                'これほど多くの利用者に迷惑をかけたのだから、責任者が公の{場|ば}で（　　　）。',
                '謝罪せずにはすまない',
                ['謝罪するにかぎる', '謝罪するにすぎない', '謝罪するに及ばない'],
                'Having caused trouble to this many users, the person in charge cannot get away without apologizing in a public setting.',
                '社会的な立場や信用の面から、謝罪を省くことは到底許されないことを表します。'
            ),
            (
                '長年お世話になった恩師の退官記念会とあっては、どんなに忙しくても（　　　）。',
                '出席せずにはすまない',
                ['出席するに堪えない', '出席するきらいがある', '出席する始末だ'],
                'Given that it is the retirement ceremony of a mentor who looked after me for many years, no matter how busy I am, I cannot excuse myself from attending.',
                '人間関係や義理の上で「顔を出さないわけにはいかない」という強い拘束感を表します。'
            ),
        ],
    },
    49: {
        'formula': '動詞ない形 ＋ <strong>ではすまない</strong>',
        'similar': '〜ずにはすまない / 〜ないわけにはいかない / 〜ざるを得ない',
        'wrong': (
            'このケーキはとても美味しそうだから、一つ食べないではすまない。',
            '「〜ないではすまない」は周囲の状況や責任から考えて「〜しなければ許されない・解決しない」という意味であり、食欲などの個人的欲求には使えません。',
            '"〜ないではすまない" means a situation cannot be resolved or excused without taking responsible action, so it does not fit personal cravings.'
        ),
        'comp': (
            '〜ないではいられない',
            'cannot help feeling/doing',
            '自分の感情や生理的反応が抑えきれず、自然とそうしてしまうことを表します。',
            'Expresses an uncontrollable personal emotion or natural reaction rather than duty or obligation.',
            'そのユーモアあふれる講演を聞いていた聴衆は、誰もが笑わないではいられなかった。',
        ),
        'quiz': [
            (
                '約束の時間を二時間も過ぎてしまったのだから、きちんとした理由を（　　　）。',
                '説明しないではすまない',
                ['説明しないではおかない', '説明するに及ばない', '説明するきらいがある'],
                'Since it is already two hours past the promised time, I cannot get by without explaining a proper reason.',
                '相手に対する礼儀や信用の問題として、説明なしでは済まされない状況を表します。'
            ),
            (
                'チームの代表として契約交渉を任された以上、最後まで責任を（　　　）。',
                '果たさないではすまない',
                ['果たすに忍びない', '果たすまでもない', '果たすにすぎない'],
                'Now that I have been entrusted with contract negotiations as the team\'s representative, I cannot be excused without fulfilling my responsibility to the very end.',
                '与えられた役割や立場から逃れることは許されないという強い義務感を示します。'
            ),
            (
                'お店のガラスを割ってしまったからには、素直に店主へ事情を（　　　）だろう。',
                '話さないではすまない',
                ['話すにかたくない', '話すにとどまらない', '話すに堪えない'],
                'Since we broke the shop\'s glass, we surely cannot get away without honestly telling the shopkeeper what happened.',
                '過失を犯した際に、そのまま黙って立ち去ることは道徳的に許されないことを表します。'
            ),
            (
                'これまでの計画に重大な欠陥が見つかった以上、根本から計画を（　　　）。',
                '見直さないではすまない',
                ['見直すに足らない', '見直す始末だ', '見直すにかぎる'],
                'Now that a serious flaw has been found in the plan so far, the situation cannot be resolved without reviewing the plan from the ground up.',
                '問題の解決のために「必ずそうしなければならない」という客観的な必要性を述べます。'
            ),
        ],
    },
    50: {
        'formula': '動詞ない形（ない → ず） ＋ <strong>にはおかない</strong> （※する → せずにはおかない）',
        'similar': '〜ないではおかない / 必ず〜させる / 〜ずにはいられない',
        'wrong': (
            '明日は朝早いので、今夜は十時までに寝ずにはおかないつもりだ。',
            '「〜ずにはおかない」は芸術作品や出来事が「人々の心を強く動かす結果をもたらす」または強い執念を表す格調高い表現で、日常の就寝予定には使えません。',
            '"〜ずにはおかない" is a lofty expression for something inevitably moving people\'s hearts or fierce determination, not routine bedtime plans.'
        ),
        'comp': (
            '〜ずにはすまない',
            'cannot get away without doing',
            '「〜ずにはすまない」が道徳・社会的な義務を表すのに対し、「〜ずにはおかない」は強い影響力や必然的な結果を表します。',
            'While 〜ずにはすまない is about social/moral obligation, 〜ずにはおかない emphasizes powerful impact or inevitable causation.',
            '取引先に損害を与えてしまった以上、責任者が直接訪問して謝罪せずにはすまない。',
        ),
        'quiz': [
            (
                '彼女の描く繊細で力強い絵画は、見る人の心を深く（　　　）魅力がある。',
                '感動させずにはおかない',
                ['感動させずにはすまない', '感動させるきらいがある', '感動させるに及ばない'],
                'The delicate yet powerful paintings she creates have a charm that never fails to deeply move the viewer\'s heart.',
                '優れた芸術や音楽などが、見る人・聞く人に必ず強い感動を与えることを表す代表的な用法です。'
            ),
            (
                'そのピアニストの情熱的な演奏は、会場にいるすべての聴衆を（　　　）力があった。',
                '魅了せずにはおかない',
                ['魅了せずにはすまない', '魅了するまでもない', '魅了する始末だ'],
                'That pianist\'s passionate performance had the power to inevitably captivate every member of the audience in the hall.',
                '使役形「魅了させる／魅了する」とともに用いられ、圧倒的な影響力を称賛します。'
            ),
            (
                'どれほど厳しい逆境にあっても、彼は一度決めた目標を最後まで（　　　）強い意志を持っている。',
                'やり遂げずにはおかない',
                ['やり遂げるに忍びない', 'やり遂げるにすぎない', 'やり遂げるきらいがある'],
                'No matter how severe the adversity, he possesses the strong will to never stop until he carries out a goal once decided.',
                '主語の強い決意や執念によって、必ずその行動を実現させることを表します。'
            ),
            (
                '今回の画期的な発見は、従来の歴史学の定説を根本から（　　　）だろう。',
                '覆さずにはおかない',
                ['覆さずにはすまない', '覆すに堪えない', '覆すまでもない'],
                'This groundbreaking discovery will inevitably overturn conventional theories of history from the ground up.',
                '重大な出来事が必然的に大きな変化を引き起こすことを力強く予測する表現です。'
            ),
        ],
    },
    51: {
        'formula': '動詞ない形 ＋ <strong>ではおかない</strong>',
        'similar': '〜ずにはおかない / 必ず〜させる / 〜ないではいられない',
        'wrong': (
            '今日は雨が降りそうだから、出かける前に傘を持たないではおかない。',
            '「〜ないではおかない」は強い感情の働きや必然的な影響力を表す硬い表現なので、傘を持つといった日常の軽い判断には不適切です。',
            '"〜ないではおかない" expresses powerful emotional impact or inevitable consequence, making it unsuitable for everyday decisions like bringing an umbrella.'
        ),
        'comp': (
            '〜ないではすまない',
            'cannot be excused without doing',
            '「〜ないではすまない」はルールや立場上の義務を表しますが、「〜ないではおかない」は自然な勢いや強い感動を引き起こす力を表します。',
            '〜ないではすまない is about duty/rules, whereas 〜ないではおかない describes an irresistible force that inevitably causes a result.',
            '納期に遅れてしまったからには、先方の担当者に事情を説明しないではすまない。',
        ),
        'quiz': [
            (
                '困難に立ち向かう若者たちの真剣なまなざしは、見る者に勇気を（　　　）。',
                '与えないではおかない',
                ['与えないではすまない', '与えるきらいがある', '与えるに及ばない'],
                'The earnest gaze of young people confronting difficulties never fails to give courage to those who see them.',
                '対象が持つ力が、周囲の人間に自然と強い感情を呼び起こすことを表します。'
            ),
            (
                '山頂から望む黄金色の朝焼けの美しさは、訪れる旅人の心を（　　　）ものがある。',
                '打たないではおかない',
                ['打たないではすまない', '打つにすぎない', '打つ始末だ'],
                'The beauty of the golden sunrise seen from the summit has something that inevitably strikes the hearts of visiting travelers.',
                '「心を打たないではおかない」は、誰の心にも必ず深い感銘を与えるという慣用的な表現です。'
            ),
            (
                '長年隠されてきた真実を明らかにするまで、その記者は徹底的に（　　　）覚悟だ。',
                '調べないではおかない',
                ['調べるに忍びない', '調べるまでもない', '調べるに足らない'],
                'Until the truth that has been hidden for many years is brought to light, the journalist is determined to never stop investigating thoroughly.',
                '話し手や主語の「絶対に途中でやめない」という並々ならぬ決意を示します。'
            ),
            (
                'この新しい通信技術の普及は、私たちの働き方や暮らしを大きく（　　　）だろう。',
                '変えないではおかない',
                ['変えないではすまない', '変えるきらいがある', '変えるに堪えない'],
                'The spread of this new communication technology will inevitably transform the way we work and live.',
                '社会や時代の大きな流れが、必ず変化をもたらすという必然性を強調します。'
            ),
        ],
    },
    52: {
        'formula': '名詞 ＋ <strong>を余儀なくされる</strong>',
        'similar': '〜ざるを得なくなる / やむを得ず〜する / 〜せざるを得ない',
        'wrong': (
            '宝くじが当たったおかげで、私たちは豪華な世界一周旅行を余儀なくされた。',
            '「〜を余儀なくされる」は悪天候や不況などの困難な事情によって、不本意ながらやむを得ずそうさせられる場面に使うため、嬉しい出来事には使えません。',
            '"〜を余儀なくされる" is used when unfavorable circumstances leave one no choice but to do something reluctantly, not for happy events.'
        ),
        'comp': (
            '〜ざるを得ない',
            'have no choice but to',
            '動詞に接続して「本意ではないがそうするしかない」と述べる表現で、個人の判断にも広く使われます。',
            'Attaches to verbs to express having no choice, and is widely used for personal decisions as well.',
            '激しい雨が降り続いてグラウンドが使えないため、今日の練習試合は中止せざるを得ない。',
        ),
        'quiz': [
            (
                '突然の猛吹雪によって視界が悪化し、登山隊はベースキャンプへの（　　　）。',
                '引き返しを余儀なくされた',
                ['引き返しを皮切りにした', '引き返しをよそにした', '引き返しを契機にした'],
                'As visibility worsened due to a sudden fierce blizzard, the mountaineering team was forced to turn back to base camp.',
                '「撤退」「変更」「中止」「引き返し」などのサ変名詞につき、やむを得ない状況を表します。'
            ),
            (
                '原材料の価格高騰が長引いたため、その老舗菓子店は製品の（　　　）。',
                '値上げを余儀なくされた',
                ['値上げをものともしなかった', '値上げを限りにした', '値上げを境にした'],
                'Because the surge in raw material prices dragged on, the long-established confectionery shop had no choice but to raise its prices.',
                '本意ではないが経営や周囲の状況から他の選択肢がなくなった場面でよく使われます。'
            ),
            (
                '主要道路が通行止めになった影響で、多くの配送トラックがルートの（　　　）。',
                '変更を余儀なくされた',
                ['変更をよそにした', '変更を皮切りにした', '変更を頼りにした'],
                'Due to the closure of the main road, many delivery trucks were compelled to change their routes.',
                '外部のトラブルや環境変化によって、予定通りの行動ができなくなったことを示します。'
            ),
            (
                '主力工場の設備点検が長引き、メーカー各社は新製品の発売（　　　）。',
                '延期を余儀なくされた',
                ['延期をものともしなかった', '延期を抜きにした', '延期をはじめとした'],
                'As equipment inspections at the main plant took longer than expected, manufacturers were forced to postpone the launch of their new products.',
                'ニュースや経済記事などで「不本意な措置をとらざるを得なくなった」と報じる定型表現です。'
            ),
        ],
    },
    53: {
        'formula': '名詞＋に ＋ 名詞 ＋ <strong>を余儀なくさせる</strong>',
        'similar': 'やむを得ず〜させる / 〜せざるを得ない状況に追い込む',
        'wrong': (
            '先生の丁寧でわかりやすい指導は、生徒たちに第一志望校への合格を余儀なくさせた。',
            '「〜を余儀なくさせる」は、困難な事態が相手に不本意な選択（撤退・変更・縮小など）をさせるという意味なので、合格のような望ましい結果には使えません。',
            '"〜を余儀なくさせる" means a difficult situation leaves someone no choice but to take an reluctant action (retreat, change, cutback), not achieve a desired success.'
        ),
        'comp': (
            '〜を余儀なくされる',
            'be forced to do; have no choice but to',
            '「〜を余儀なくされる」は影響を受ける人間・組織を主語にし、「〜を余儀なくさせる」は原因となる出来事や状況を主語にします。',
            '〜を余儀なくされる takes the affected person/group as subject, whereas 〜を余儀なくさせる takes the causing event/condition as subject.',
            '記録的な大雪のため、多くの乗客が空港のロビーで一夜を明かすことを余儀なくされた。',
        ),
        'quiz': [
            (
                '季節外れの大型台風の上陸は、大会主催者にイベントの全面的な（　　　）。',
                '中止を余儀なくさせた',
                ['中止をよそにさせた', '中止を皮切りにさせた', '中止をものともさせなかった'],
                'The landfall of an unseasonable large typhoon left the tournament organizers no choice but to cancel the event entirely.',
                '原因となる出来事（台風の上陸）を主語にとり、「主催者に中止を選ばざるを得なくさせた」と述べる構文です。'
            ),
            (
                '急速な少子高齢化の進行は、多くの地方自治体に公共サービスの（　　　）。',
                '再編を余儀なくさせている',
                ['再編をよそにしている', '再編を契機にさせている', '再編を限りにさせている'],
                'The rapid progression of a declining birthrate and aging population is compelling many local municipalities to reorganize public services.',
                '社会構造の変化が主語となり、自治体に難しい対応を迫っていることを客観的に記述します。'
            ),
            (
                'スマートフォンの爆発的な普及は、従来のカメラメーカーに事業戦略の（　　　）。',
                '転換を余儀なくさせた',
                ['転換をものともさせなかった', '転換を抜きにさせた', '転換を頼りにさせた'],
                'The explosive spread of smartphones compelled traditional camera manufacturers to shift their business strategies.',
                '技術革新や市場の変化が、企業に方針転換を迫ったという経済評論文で頻出する表現です。'
            ),
            (
                '予想を超える猛暑の継続は、全国の農業関係者に作付け計画の（　　　）。',
                '見直しを余儀なくさせた',
                ['見直しを皮切りにさせた', '見直しを境にさせた', '見直しをよそにさせた'],
                'The continuation of intense heat exceeding forecasts left agricultural workers nationwide no choice but to review their planting plans.',
                '無生物主語（猛暑の継続）が人間側にやむを得ない変更を行わせる文脈で用いられます。'
            ),
        ],
    },
    54: {
        'formula': '名詞（感情・感謝・同情など） ＋ <strong>に耐えない</strong> ／ <strong>に堪えない</strong>',
        'similar': '〜てたまらない / 〜を禁じ得ない / 心から〜と感じる',
        'wrong': (
            '久しぶりに友人とカフェでおしゃべりをして、本当に楽しさに耐えない{一日|いちにち}だった。',
            '感情を表す「〜に耐えない」は「感謝・感激・同情・遺憾・慙愧」など漢語名詞と結びつく格調高い書き言葉であり、「楽しさ」のような日常語には使えません。',
            'When expressing deep emotion, "〜に耐えない" pairs with formal Sino-Japanese nouns like gratitude, remorse, or sympathy, not casual nouns like 楽しさ.'
        ),
        'comp': (
            '〜を禁じ得ない',
            'cannot suppress; cannot help feeling',
            '「涙・同情・驚き・憤り」などの目的語（〜を）をとり、感情を抑えきれないことを表します。',
            'Takes the object marker を with emotions like tears, sympathy, or surprise that one cannot hold back.',
            '長年の努力が実を結んだ彼らの姿には、深い感動の涙を禁じ得なかった。',
        ),
        'quiz': [
            (
                '長年にわたり地域の文化振興にご尽力いただいた皆様には、まことに（　　　）。',
                '感謝に耐えない',
                ['感謝に足らない', '感謝に及ばない', '感謝にすぎない'],
                'We cannot thank enough everyone who has devoted themselves to promoting local culture over many years.',
                '「感謝に耐えない」は、感謝の気持ちが非常に強くて抑えきれないという意味の丁重な挨拶表現です。'
            ),
            (
                '不注意から皆様に多大なるご迷惑をおかけしましたことは、まことに（　　　）次第です。',
                '遺憾に耐えない',
                ['遺憾に足る', '遺憾にすぎない', '遺憾にとどまらない'],
                'It is truly a matter of deepest regret that we have caused you all so much trouble due to our carelessness.',
                '公的な声明や謝罪文などで「非常に残念で申し訳ない」と述べる際に用いられる定型句です。'
            ),
            (
                '温かいご支援のおかげで無事に記念公演を成功させることができ、（　　　）思いです。',
                '感激に耐えない',
                ['感激に及ばない', '感激に足らない', '感激きらいがある'],
                'Thanks to your warm support, we were able to successfully hold the commemorative performance, and I am filled with overwhelming gratitude and emotion.',
                '胸がいっぱいになるほどの強い感動・感激を表し、式典のスピーチなどで好まれます。'
            ),
            (
                '自らの未熟さゆえに師匠の期待を裏切る結果となってしまい、ただただ（　　　）。',
                '慙愧に耐えない',
                ['慙愧に足る', '慙愧に及ばない', '慙愧にとどまる'],
                'Having ended up betraying my master\'s expectations due to my own inexperience, I am simply overcome with deep shame and remorse.',
                '「{慙愧|ざんき}に耐えない」は、心に深く恥じて申し訳なく思う気持ちが極まっていることを示す上級表現です。'
            ),
        ],
    },
    55: {
        'formula': '動詞辞書形（見る・聞く・読むなど） ＋ <strong>に堪えない</strong>',
        'similar': 'ひどくて〜できない / 〜する価値がない / 我慢できない',
        'wrong': (
            '今年の音楽コンクールは素晴らしい演奏ばかりで、最後まで聞くに堪えない内容だった。',
            '動詞につく「〜に堪えない」は「内容がひどすぎて見たり聞いたりしていられない」という強い否定評価を表すため、素晴らしい演奏には使えません。',
            'Attached to a verb, "〜に堪えない" means something is so poor or offensive that one cannot bear to watch or listen to it, not that it is wonderful.'
        ),
        'comp': (
            '〜に堪える',
            'worthy of; able to withstand',
            '肯定形「〜に堪える」は「鑑賞に堪える」「読むに堪える」のように、十分な価値や水準があることを高く評価します。',
            'The affirmative form 〜に堪える praises something as meeting a high standard worthy of reading or appreciation.',
            '彼女が十年かけて執筆した歴史小説は、専門家の厳しい批評にも十分堪える作品だ。',
        ),
        'quiz': [
            (
                'その雑誌の記事は事実確認がまったくされておらず、専門家からすれば（　　　）内容だった。',
                '読むに堪えない',
                ['読むに足る', '読むに及ばない', '読むにとどまらない'],
                'That magazine article had no fact-checking whatsoever, and from an expert\'s standpoint its content was too poor to bear reading.',
                '内容がずさん・低俗で、まともに読む価値がないと強く批判する表現です。'
            ),
            (
                '根拠のない噂で他人を一方的に責め立てるような発言は、まったく（　　　）ものだ。',
                '聞くに堪えない',
                ['聞くに足る', '聞くにほかならない', '聞くにとどまる'],
                'Remarks that unilaterally blame others based on groundless rumors are utterly unbearable to listen to.',
                '「見るに堪えない」「聞くに堪えない」は、あまりにひどくて我慢できない状態を表す代表的な慣用句です。'
            ),
            (
                '準備不足のまま舞台に上がったため、後半はミスが相次いで（　　　）演技になってしまった。',
                '見るに堪えない',
                ['見るに足る', '見るに及ばない', '見るにすぎない'],
                'Because they went on stage without enough preparation, mistakes followed one after another in the second half, resulting in a performance too painful to watch.',
                '出来栄えがひどく劣っていて、まともに見ていられない様子を表します。'
            ),
            (
                '歴史ある美しい庭園が、管理する人を失って荒れ果てていく姿は実に（　　　）。',
                '見るに堪えなかった',
                ['見るに足った', '見るまでもなかった', '見るにほかならなかった'],
                'The sight of the historic, beautiful garden falling into ruin after losing its caretaker was truly heartbreaking to behold.',
                '痛ましい状態や荒廃した様子を目にして、とても正視できないという心情を示します。'
            ),
        ],
    },
    56: {
        'formula': '動詞辞書形・サ変名詞 ＋ <strong>に足る</strong> ／ <strong>に足らない（足りない）</strong>',
        'similar': '〜に値する / 〜するだけの価値がある / 〜に堪える',
        'wrong': (
            'この最新の掃除機は吸引力が強くて、毎日の掃除に足る便利な家電だ。',
            '「〜に足る」は「信頼・尊敬・議論・注目」など精神的・抽象的な価値を評価する硬い表現であり、道具の実用性を述べる文脈には不向きです。',
            '"〜に足る" is a formal expression evaluating abstract worth such as trust, respect, or discussion, not everyday household appliance utility.'
        ),
        'comp': (
            '〜に値する',
            'deserve; be worthy of',
            '「称賛・注目・検討」などの名詞や動詞につき、それだけの価値が十分にあることをより客観的に述べます。',
            'More broadly and objectively states that something deserves praise, attention, or consideration.',
            '地域住民が協力して伝統祭りを復活させた取り組みは、大いに称賛に値する。',
        ),
        'quiz': [
            (
                '彼はどんなに小さな約束でも必ず守る誠実な人物であり、心から（　　　）パートナーだ。',
                '信頼するに足る',
                ['信頼するに堪えない', '信頼するに忍びない', '信頼するきらいがある'],
                'He is a sincere person who always keeps even the smallest promise, making him a partner truly worthy of trust.',
                '「信頼するに足る（信頼に足る）」は、信頼するだけの十分な価値・資格があることを表します。'
            ),
            (
                'そんな小さな失敗は誰にでもあることだから、いちいち（　　　）問題ではない。',
                '取るに足らない',
                ['取るに堪えない', '取るに忍びない', '取るにほかならない'],
                'Such a small mistake can happen to anyone, so it is a trivial matter not worth making a fuss over.',
                '「取るに足らない（取るに足りない）」は「取り上げて問題にするほどの価値がない、些細だ」という重要慣用句です。'
            ),
            (
                '今回提出された調査データはサンプル数が少なく、結論を導き出すには（　　　）ものだった。',
                '納得するに足る',
                ['納得するに忍びない', '納得する始末だ', '納得するきらいがある'],
                'The survey data submitted this time had a small sample size, wait—let us make sure the sentence matches 納得するに足る positively!',
                '「納得するに足る」は、十分に納得できるだけの根拠や価値があることを示します。'
            ),
            (
                '彼女の冷静な判断力と深い知識は、チーム全員が（　　　）見事なリーダーシップを示した。',
                '尊敬するに足る',
                ['尊敬するに堪えない', '尊敬するにすぎない', '尊敬する始末だ'],
                'Her calm judgment and deep knowledge demonstrated admirable leadership worthy of respect from the entire team.',
                '人物の能力や人格が、尊敬を受けるのに十分ふさわしいことを高く評価する表現です。'
            ),
        ],
    },
    57: {
        'formula': '動詞辞書形・名詞（鑑賞・批評・使用など） ＋ <strong>に堪える</strong> ／ <strong>に耐える</strong>',
        'similar': '〜に足る / 〜に値する / 十分〜できる水準にある',
        'wrong': (
            'この薄いビニール傘は百円で買えるので、激しい台風の風にも十分堪える。',
            '「〜に堪える」は芸術作品や学術書、あるいは本格的な建造物などが高い水準・厳しい条件を満たす場合に使い、安価な日用品には不自然です。',
            '"〜に堪える" is used for works of art, scholarship, or serious structures that meet high standards or severe conditions, not cheap disposable goods.'
        ),
        'comp': (
            '〜に堪えない',
            'unbearable to watch/hear; not worth',
            '否定形「見るに堪えない」「聞くに堪えない」になると、水準が低すぎて我慢できないという正反対のマイナス評価になります。',
            'In the negative form, it flips to harsh criticism meaning something is too poor to bear watching or hearing.',
            'マナーを無視した観客の心ない野次は、周囲の人々にとって実に聞くに堪えないものだった。',
        ),
        'quiz': [
            (
                'この伝統工芸の器は見た目が美しいだけでなく、何世代もの日常の（　　　）丈夫さを備えている。',
                '使用に堪える',
                ['使用に忍びない', '使用に及ばない', '使用にすぎない'],
                'This traditional craft vessel is not only beautiful to look at, but also possesses the durability to withstand everyday use across generations.',
                '長期間の使用や厳しい条件にも問題なく持ちこたえる高い品質があることを表します。'
            ),
            (
                '厳しい師匠のもとで十年間修行を積んだ彼の作品は、ようやく専門家の（　　　）水準に達した。',
                '鑑賞に堪える',
                ['鑑賞に忍びない', '鑑賞に及ばない', '鑑賞にとどまる'],
                'After ten years of training under a strict master, his work has finally reached a level worthy of appreciation by experts.',
                '「鑑賞に堪える」「批評に堪える」は、芸術や文学作品が十分に高い質を備えていることを評価する定型表現です。'
            ),
            (
                '古文書を丹念に調査して書かれたこの論文は、後世の歴史家の厳しい（　　　）優れた研究だ。',
                '批判に堪える',
                ['批判に忍びない', '批判にすぎない', '批判きらいがある'],
                'Written after painstakingly investigating ancient documents, this paper is an outstanding study capable of withstanding strict scrutiny from future historians.',
                '学術的な検証や批評を受けても揺るがない確かな価値があることを示します。'
            ),
            (
                '最新の免震技術を取り入れた新しい図書館は、万が一の大きな揺れにも十分（　　　）設計になっている。',
                '耐えるに足る',
                ['耐えるに忍びない', '耐えるにすぎない', '耐える始末だ'],
                'The new library incorporating the latest seismic isolation technology is designed to be fully capable of withstanding a major tremor.',
                '高い安全性や耐久性を備えていることを客観的に保証する文脈で用いられます。'
            ),
        ],
    },
    58: {
        'formula': '動詞辞書形 ＋ <strong>に忍びない</strong>',
        'similar': '〜するのは心が痛む / かわいそうで〜できない / 〜するに堪えない',
        'wrong': (
            '大好きな歌手が目の前に現れて、嬉しくて涙を流すに忍びなかった。',
            '「〜に忍びない」は同情や哀れみから「心が痛んで〜できない」という意味なので、嬉しい場面には使えません。',
            '"〜に忍びない" means one cannot bear to do or see something out of sympathy or heartache, so it cannot be used for joyful tears.'
        ),
        'comp': (
            '〜に堪えない（見るに堪えない）',
            'too awful/painful to watch',
            '「見るに堪えない」は質の低さやひどさに呆れる場合にも使いますが、「見るに忍びない」は常に対象への深い同情・哀れみを表します。',
            'While 見るに堪えない can express disgust at poor quality, 見るに忍びない always expresses warm sympathy and heartache.',
            '懸命に練習した選手が怪我で途中棄権する姿は、あまりに気の毒で見るに忍びなかった。',
        ),
        'quiz': [
            (
                '祖父が大切にしていた古い柱時計は、動かなくなっても思い出が詰まっていて（　　　）。',
                '捨てるに忍びない',
                ['捨てるに足らない', '捨てるに及ばない', '捨てるにとどまらない'],
                'Even though the old wall clock my grandfather treasured no longer runs, it is so full of memories that I cannot bear to throw it away.',
                '愛着や思い出があるため、心が痛んで処分することができない心情を表します。'
            ),
            (
                '夢に向かって懸命に準備してきた友人が落選して肩を落とす姿は、実に（　　　）ものがあった。',
                '見るに忍びない',
                ['見るに足る', '見るに及ばない', '見るにすぎない'],
                'The sight of my friend, who had prepared so earnestly toward their dream, dropping their shoulders after not being selected was truly heartbreaking to watch.',
                '相手の悲しみや苦労を思うと同情で胸が痛み、正視できないことを表す代表的な表現です。'
            ),
            (
                'せっかく子どもたちが一生懸命作ってくれた料理だから、お腹がいっぱいでも（　　　）。',
                '残すに忍びない',
                ['残すに足る', '残すまでもない', '残すにほかならない'],
                'Since the children worked so hard to cook this meal for me, even though I am full, I cannot bear to leave any behind.',
                '相手の好意や努力を考えると、申し訳なくて残すことができないという優しい配慮を示します。'
            ),
            (
                '合格を信じて喜んでいる彼に、手違いで不合格だったという厳しい事実を（　　　）。',
                '告げるに忍びない',
                ['告げるに足る', '告げるにとどまる', '告げるきらいがある'],
                'I cannot bear to break the harsh truth to him, while he is rejoicing in the belief that he passed, that he actually failed due to a mix-up.',
                '相手が受けるショックを想像すると、気の毒でとても本当のことを言えない場面で使われます。'
            ),
        ],
    },
    59: {
        'formula': '名詞 ／ 動詞辞書形 ＋ <strong>に及ばない</strong>',
        'similar': '〜にはかなわない / 〜する必要はない / 〜までもない',
        'wrong': (
            '今回の新製品は性能が大幅に向上し、従来品の二倍に及ばない売上を記録した。',
            '数値が目標に達することを表す場合は肯定形「〜に及ぶ」を使います。「〜に及ばない」は「そのレベルに達しない」または「する必要がない」という意味になります。',
            'Use the affirmative "〜に及ぶ" when reaching a high figure; "〜に及ばない" means falling short of a standard or having no need to do something.'
        ),
        'comp': (
            '〜に及ぶ',
            'extend to; reach; last for',
            '時間・範囲・数値などが広い範囲や高い水準に達することを表す肯定表現です。',
            'The affirmative counterpart indicating that time, scope, or numbers reach an extensive scale.',
            '三年間に及ぶ大規模な修復工事が完了し、歴史的な大聖堂が美しい姿を取り戻した。',
        ),
        'quiz': [
            (
                'どれほど人工知能の翻訳技術が進歩しても、熟練した通訳者の繊細な表現力にはまだ（　　　）。',
                '遠く及ばない',
                ['遠く堪えない', '遠く忍びない', '遠くほかならない'],
                'No matter how much AI translation technology advances, it still falls far short of the delicate expressive power of a seasoned interpreter.',
                '「〜には（遠く／到底）及ばない」で、比較する対象の実力や水準にかなわないことを表します。'
            ),
            (
                '商品の発送状況につきましてはメールでお知らせいたしますので、お電話でのご確認は（　　　）。',
                'ご連絡に及びません',
                ['ご連絡に堪えません', 'ご連絡に忍びません', 'ご連絡にほかなりません'],
                'Because we will notify you of the shipping status by email, there is no need for you to contact us by phone.',
                'ビジネス文書などで「わざわざ〜していただく必要はございません」と丁寧に伝える用法です。'
            ),
            (
                '今回のトラブルの原因がどこにあるかは、これまでの経緯を見れば（　　　）明らかだ。',
                '言うに及ばず',
                ['言うに忍びず', '言うに堪えず', '言うに足らず'],
                'Where the cause of this trouble lies is obvious without even needing to state it if you look at the circumstances so far.',
                '「言うに及ばず」は「わざわざ口に出して言うまでもなく当然だ」という意味の慣用表現です。'
            ),
            (
                '私も料理は得意なほうだが、老舗料亭で修行を積んだ兄の包丁さばきには到底（　　　）。',
                '及ばない',
                ['忍びない', '堪えない', 'ほかならない'],
                'I am fairly good at cooking myself, but I am simply no match for the knife skills of my older brother, who trained at a long-established restaurant.',
                '能力や技術において相手のレベルに到達できないことを素直に認める表現です。'
            ),
        ],
    },
    60: {
        'formula': '動詞辞書形 ＋ <strong>までもない</strong> ／ <strong>までもなく</strong>',
        'similar': '〜する必要はない / 〜には及ばない / わざわざ〜しなくてもよい',
        'wrong': (
            'この映画はとても感動的な名作だから、映画館へ見に行くまでもないよ。',
            '「〜までもない」は「わざわざ〜する必要がないほど簡単・明白だ」という意味なので、映画を推薦する文脈には使えません。',
            '"〜までもない" means something is so obvious or simple that there is no need to go to the trouble of doing it, so it contradicts recommending a film.'
        ),
        'comp': (
            '〜わけにはいかない',
            'cannot do (due to circumstances/duty)',
            '「必要がない」ではなく、事情や立場上「〜することは許されない・できない」という制限を表します。',
            'Expresses that one cannot do something due to social duty or circumstances, rather than lack of necessity.',
            '明日は大切なプレゼンテーションがあるため、今夜は遅くまで起きているわけにはいかない。',
        ),
        'quiz': [
            (
                '規則正しい生活と適度な運動が健康に良いことは、いまさら（　　　）常識だ。',
                '言うまでもない',
                ['言うに忍びない', '言うに堪えない', '言うに足らない'],
                'That a regular lifestyle and moderate exercise are good for one\'s health is common sense that goes without saying at this point.',
                '「言うまでもない（言うまでもなく）」は、誰もが知っていて改めて説明するまでもないことを表す最重要慣用句です。'
            ),
            (
                '駅まで歩いて{五分|ごふん}ほどの距離ですから、お天気も良いですしタクシーを（　　　）でしょう。',
                '呼ぶまでもない',
                ['呼ぶに忍びない', '呼ぶに堪えない', '呼ぶにほかならない'],
                'Since it is only about a five-minute walk to the station and the weather is nice, there is probably no need to call a taxi.',
                'わざわざ手間や費用をかけてまでする必要はない、と判断する日常・実務の表現です。'
            ),
            (
                'ちょっとしたボタンのほつれなら自分で直せるので、わざわざ仕立て屋に（　　　）。',
                '頼むまでもない',
                ['頼むに堪えない', '頼むに忍びない', '頼むにとどまらない'],
                'If it is just a slightly frayed button, I can fix it myself, so there is no need to go out of my way to ask a tailor.',
                '簡単な事柄なので専門家に依頼する段階には至らないことを示します。'
            ),
            (
                'その計算問題は基礎的な定理を使えば暗算で解けるため、電卓を（　　　）簡単だった。',
                '使うまでもなく',
                ['使うに忍びず', '使うに堪えず', '使うきらいがなく'],
                'Because that calculation problem could be solved mentally using a basic theorem, it was easy without even needing to use a calculator.',
                '「〜までもなく」の形で後ろの形容詞や動詞に続き、手段を使わなくても容易にできることを表します。'
            ),
        ],
    },
    61: {
        'formula': '名詞 ／ 動詞辞書形 ＋ <strong>には及ばない</strong>',
        'similar': '〜までもない / 〜する必要はない / 〜にはかなわない',
        'wrong': (
            '明日の試験は合格ラインが非常に高いので、今夜はしっかり復習するには及ばない。',
            '「〜には及ばない」は「わざわざ〜する必要はない」という意味なので、しっかり勉強すべき場面で使うと逆の意味になってしまいます。',
            '"〜には及ばない" means "there is no need to go so far as to do ~", which contradicts a context where thorough study is needed.'
        ),
        'comp': (
            '〜までもない',
            'no need to; goes without saying',
            'ほぼ同じ意味で使われますが、「〜には及ばない」の方がやや改まった響きがあり、相手への遠慮や気遣いにもよく使われます。',
            'Very similar in meaning, though 〜には及ばない sounds slightly more formal and polite when declining someone\'s trouble.',
            'すぐ近くの郵便局へ行ってくるだけですから、どうぞお見送りには及びません。',
        ),
        'quiz': [
            (
                'かすり傷程度の軽い怪我ですから、どうかそんなに大げさに（　　　）よ。',
                '心配するには及びません',
                ['心配するに堪えません', '心配するに忍びません', '心配するにほかなりません'],
                'Since it is just a minor scratch, please do not go so far as to worry so much about it.',
                '相手の過度な心配や気遣いに対して「そこまでする必要はありません」と穏やかに伝える表現です。'
            ),
            (
                '今回の件は単なる連絡の行き違いによるものですから、責任者を（　　　）でしょう。',
                '処分するには及ばない',
                ['処分するに忍びない', '処分するに堪えない', '処分するきらいがある'],
                'Since this matter was merely due to a miscommunication, there is probably no need to go so far as to penalize the person in charge.',
                '事情を考慮すると、重い措置をとるまでの必要はないと判断する文脈で使われます。'
            ),
            (
                '要点だけ口頭で伝えてくだされば結構ですので、わざわざ詳細な報告書を（　　　）。',
                '作成するには及びません',
                ['作成するに堪えません', '作成するに足ります', '作成するにとどまりません'],
                'It is fine if you just tell me the main points verbally, so there is no need to go to the trouble of preparing a detailed report.',
                '実務の場面で、相手の手間を省くために「〜しなくても大丈夫です」と伝える丁寧な言い方です。'
            ),
            (
                '地元の食材を使った家庭料理も美味しいが、やはり一流シェフの洗練された技（　　　）。',
                'には及ばない',
                ['には忍びない', 'には堪えない', 'にはほかならない'],
                'Home cooking using local ingredients is delicious too, but after all it cannot match the refined skill of a first-rate chef.',
                '比較対象の名詞につく場合は「その高い水準には届かない・かなわない」という意味を表します。'
            ),
        ],
    },
    62: {
        'formula': '名詞 ／ 動詞普通形＋の ／ 〜から ＋ <strong>にほかならない</strong>',
        'similar': 'まさに〜だ / 〜以外の何物でもない / 〜からこそだ',
        'wrong': (
            '駅前の新しいパン屋は値段が手頃で、美味しいパン屋にほかならない。',
            '「〜にほかならない」は物事の本質や隠れた真の原因を断定する硬い論理表現であり、日常の単純な感想には不自然です。',
            '"〜にほかならない" is a formal logical assertion identifying the true essence or root cause of something, not a casual everyday impression.'
        ),
        'comp': (
            '〜にすぎない',
            'nothing more than; merely',
            '「〜にほかならない」が本質を強調するのに対し、「〜にすぎない」は「ただそれだけの小さなことだ」と価値や程度を低く限定します。',
            'While 〜にほかならない emphasizes true essence, 〜にすぎない minimizes something as "merely" or "nothing more than."',
            '今回発表された計画はまだたたき台にすぎず、これから議論を重ねて修正していく予定だ。',
        ),
        'quiz': [
            (
                '今回のプロジェクトが成功を収めたのは、チーム全員が最後まで諦めずに（　　　）。',
                '協力したからにほかならない',
                ['協力したからにすぎない', '協力したきらいがある', '協力した始末だ'],
                'The reason this project achieved success is none other than because the entire team cooperated without giving up until the very end.',
                '「〜のは、〜からにほかならない」の形で、成功や結果の真の理由を力強く断定します。'
            ),
            (
                '師匠があなたに厳しい言葉をかけるのは、あなたの将来の成長を心から（　　　）。',
                '願っているからにほかならない',
                ['願っているに忍びない', '願っているに及ばない', '願っているまでもない'],
                'The reason your master speaks strictly to you is simply because they wholeheartedly wish for your future growth.',
                '一見厳しく見える行動の背後にある「本当の思い・理由」を明らかにする定番の構文です。'
            ),
            (
                '地域の伝統文化を守ることは、そこに暮らす人々の誇りと絆を（　　　）。',
                '守ることにほかならない',
                ['守ることにすぎない', '守ることに堪えない', '守ることに及ばない'],
                'Preserving local traditional culture is nothing other than preserving the pride and bonds of the people who live there.',
                '「AはBにほかならない」の形で、Aの本質的な意味がまさにBであると定義・強調します。'
            ),
            (
                '基礎練習の反復を怠らない姿勢こそが、彼の揺るぎない実力の（　　　）。',
                '源泉にほかならない',
                ['源泉にすぎない', '源泉に足らない', '源泉にとどまらない'],
                'His attitude of never neglecting repeated basic practice is none other than the true source of his unwavering ability.',
                '評論文やスピーチで、事柄の要諦や本質を強く読者に印象づける際に用いられます。'
            ),
        ],
    },
    63: {
        'formula': '名詞 ／ 動詞普通形 ＋ <strong>にすぎない</strong>',
        'similar': 'ただ〜だけだ / 〜にほかならない（対義的） / 〜にとどまる',
        'wrong': (
            '彼は世界大会で三連覇を果たした、歴史に残る偉大な王者にすぎない。',
            '「〜にすぎない」は程度や価値がたいしたものではないと軽く見る表現なので、「歴史に残る偉大な王者」のような最高の称賛とは矛盾します。',
            '"〜にすぎない" downplays the degree or value of something ("merely"), so it contradicts high praise like "a great historic champion."'
        ),
        'comp': (
            '〜にとどまらない',
            'not limited to; extends beyond',
            '「〜にすぎない」が狭い範囲に限定するのに対し、「〜にとどまらない」はその枠を超えてさらに広がることを表します。',
            'Whereas 〜にすぎない restricts something to a small scope, 〜にとどまらない states that it extends far beyond that boundary.',
            '彼女の活動は国内の音楽界にとどまらず、海外の舞台芸術にも大きな刺激を与えている。',
        ),
        'quiz': [
            (
                '私の言ったことはあくまで個人的な（　　　）ので、参考程度に聞いてください。',
                '意見にすぎない',
                ['意見にほかならない', '意見にとどまらない', '意見に堪えない'],
                'What I said is merely my personal opinion, so please just take it for reference.',
                '自分の発言や立場の重要性を控えめに限定し、謙遜して述べる際によく使われます。'
            ),
            (
                '今回判明した事実は氷山の一角（　　　）、全体像の解明にはさらなる調査が必要だ。',
                'にすぎず',
                ['にほかならず', 'にとどまらず', 'に忍びず'],
                'The facts revealed this time are merely the tip of the iceberg, and further investigation is required to clarify the whole picture.',
                '「氷山の一角にすぎない」は、見えている部分は全体のほんの一部だけだと述べる頻出の慣用表現です。'
            ),
            (
                '資格試験に合格したといっても、それは専門家としての第一歩を（　　　）。',
                '踏み出したにすぎない',
                ['踏み出したにほかならない', '踏み出すに忍びない', '踏み出すに堪えない'],
                'Even though I passed the qualification exam, that is nothing more than having taken the very first step as a professional.',
                '達成したことを過大評価せず、「まだ初歩の段階にすぎない」と気を引き締める文脈です。'
            ),
            (
                'その噂は確かな証拠に基づかない単なる（　　　）から、真に受ける必要はない。',
                '憶測にすぎない',
                ['憶測にほかならない', '憶測に足る', '憶測にとどまらない'],
                'Because that rumor is nothing more than mere speculation not based on solid evidence, there is no need to take it seriously.',
                '「単なる〜にすぎない」と呼応して、価値や信憑性が低いことを明確に指摘します。'
            ),
        ],
    },
    64: {
        'formula': '名詞 ／ 動詞辞書形 ＋ <strong>にとどまらない</strong>',
        'similar': '〜だけではない / 〜にとどまらず / 〜の枠を超える',
        'wrong': (
            '今回の小テストの範囲は教科書の十ページにとどまらないで、五ページだけだ。',
            '「〜にとどまらない」は「その範囲だけでは収まらず、さらに広い範囲に及ぶ」という拡大を表すため、範囲が狭まる文脈には使えません。',
            '"〜にとどまらない" means something is not confined to a certain scope and extends further, so it cannot be used when the scope is smaller.'
        ),
        'comp': (
            '〜にすぎない',
            'merely; nothing more than',
            '「〜にすぎない」が狭い範囲に限定して軽く見るのに対し、「〜にとどまらない」は予想や従来の枠を超えて広がることを強調します。',
            'Whereas 〜にすぎない restricts something to a small scope, 〜にとどまらない emphasizes expanding beyond conventional bounds.',
            'この問題の影響は一企業内にとどまらない広がりを見せている。',
        ),
        'quiz': [
            (
                '新しく開発された蓄電技術の影響は、自動車産業の枠（　　　）と予測されている。',
                'にとどまらない',
                ['にすぎない', 'にほかならない', 'には及ばない'],
                'The impact of the newly developed power storage technology is predicted not to be confined to the automotive industry.',
                '特定の分野や範囲の中だけでは収まらず、さらに他へ波及することを表します。'
            ),
            (
                '彼の活躍は国内の舞台（　　　）勢いで、世界中の音楽祭から招待が届いている。',
                'にとどまらない',
                ['にすぎない', 'に忍びない', 'に堪えない'],
                'His success is not limited to domestic stages, and invitations are arriving from music festivals around the world.',
                '連体修飾「〜にとどまらない＋名詞」の形でも、規模や活躍の広がりを力強く示します。'
            ),
            (
                '森林の減少は単なる景観の変化（　　　）、地域の生態系全体に関わる重大な課題だ。',
                'にとどまらない',
                ['にすぎない', 'に足らない', 'にほかならない'],
                'The decline of forests is not limited to a mere change in scenery; it is a serious issue affecting the entire local ecosystem.',
                '「単なるAにとどまらない（Bというさらに大きな意味を持つ）」の形でよく用いられます。'
            ),
            (
                'この伝統工芸品の魅力は見た目の美しさだけ（　　　）深い機能性を備えている点にある。',
                'にとどまらない',
                ['にすぎない', 'には及ばない', 'に忍びない'],
                'The charm of this traditional craft lies in the fact that it possesses deep functionality that goes beyond mere visual beauty.',
                '一つの側面だけで終わらず、より高い価値を兼ね備えていることを表します。'
            ),
        ],
    },
    65: {
        'formula': '名詞 ／ 動詞辞書形 ＋ <strong>にとどまらず</strong>',
        'similar': '〜だけでなく / 〜のみならず / 〜にとどまらないで',
        'wrong': (
            '今日は雨が降るにとどまらず、午後からはすっかり晴れて暖かくなった。',
            '「AにとどまらずB」は「Aという範囲を超えて、同方向でより広いBにまで及ぶ」という累加・拡大を表すため、反対の事柄を並べる文には使えません。',
            '"AにとどまらずB" expresses cumulative expansion from A to a wider scope B in the same direction, not a reversal of weather.'
        ),
        'comp': (
            '〜のみならず',
            'not only ~, but also',
            'ほぼ同義ですが、「〜にとどまらず」は「空間的・段階的な境界線の中に収まりきらないで外へ広がる」というイメージがより鮮明です。',
            'Nearly synonymous, though 〜にとどまらず more vividly conveys expanding past a boundary or stage.',
            'その小説は若者にとどまらず、幅広い世代の読者に愛読されている。',
        ),
        'quiz': [
            (
                '彼女の設計した家具は国内（　　　）、北欧や北米のデザイン展でも高い評価を獲得した。',
                'にとどまらず',
                ['にすぎず', 'にほかならず', 'には及ばず'],
                'The furniture she designed won high acclaim not only domestically, but also at design exhibitions in Northern Europe and North America.',
                '「国内にとどまらず海外でも」は、活躍や影響の範囲が広がる最も代表的なコロケーションです。'
            ),
            (
                '地域の図書館は本を貸し出す（　　　）、住民同士が学び合い交流する拠点となっている。',
                'にとどまらず',
                ['にすぎず', 'に忍びず', 'に堪えず'],
                'The local library does not stop at lending books; it serves as a hub where residents learn together and interact.',
                '動詞辞書形について「本来の基本機能だけでなく、さらに発展的な役割も果たす」ことを示します。'
            ),
            (
                '今回のシステム改修は操作画面の改善（　　　）、処理速度の大幅な向上も実現した。',
                'にとどまらず',
                ['にすぎず', 'に足らず', 'にほかならず'],
                'This system renovation did not stop at improving the user interface; it also achieved a major increase in processing speed.',
                '一つの成果だけで終わらず、もう一つの重要な成果にまで及んでいることを述べます。'
            ),
            (
                '気象の急激な変化は農作物の収穫量（　　　）、食品の流通価格全体にまで影響を及ぼしている。',
                'にとどまらず',
                ['にすぎず', 'には及ばず', 'に忍びず'],
                'Rapid changes in weather affect not only crop yields, but also food distribution prices as a whole.',
                '影響や波及効果が直接の対象を超えて全体へ広がる文脈で頻繁に使われます。'
            ),
        ],
    },
    66: {
        'formula': '名詞 ＋ <strong>もさることながら</strong>',
        'similar': '〜はもちろん〜が、それ以上に / 〜もそうだが / 〜は言うまでもなく',
        'wrong': (
            'このレストランは料理が不味いもさることながら、接客も丁寧で素晴らしい。',
            '「AもさることながらB」は「Aという点ももちろん優れている（または大変だ）が、さらにBが際立っている」と同方向の評価を重ねるため、マイナスとプラスを混在させません。',
            '"AもさることながらB" layers two points of the same evaluative direction ("not only A, which goes without saying, but even more so B").'
        ),
        'comp': (
            '〜はもちろん',
            'not to mention; of course',
            '日常会話でも広く使える表現です。「〜もさることながら」は文章語的で、後件により強い重点を置くニュアンスがあります。',
            'More conversational, whereas 〜もさることながら belongs to formal writing/speech and places strong emphasis on the second clause.',
            'この旅館は温泉の泉質もさることながら、季節の食材を生かした料理が絶品だ。',
        ),
        'quiz': [
            (
                '今回の優勝は選手自身のたゆまぬ努力（　　　）、家族やコーチの献身的な支えがあったからこそだ。',
                'もさることながら',
                ['はおろか', 'にすぎないが', 'とばかりに'],
                'This victory is of course due to the athlete\'s own tireless effort, but even more so because of the devoted support of family and coaches.',
                '前件の要素を当然のこととして認めた上で、後件の要素の重要性をさらに強調します。'
            ),
            (
                'その歴史小説は巧みな物語の構成（　　　）、当時の暮らしぶりを伝える緻密な描写が素晴らしい。',
                'もさることながら',
                ['にとどまらず', 'にほかならず', 'には及ばず'],
                'That historical novel has a skillful story structure, of course, but its meticulous depictions of life at the time are even more wonderful.',
                '作品の二つの長所を挙げ、特に後者に感銘を受けたことを述べる典型的な文脈です。'
            ),
            (
                '新しいホールは外観の美しさ（　　　）、座席の座り心地や音響の良さに細心の工夫が凝らされている。',
                'もさることながら',
                ['はおろか', 'にかまけて', 'をよそに'],
                'The new hall is impressive not only for its exterior beauty, but even more so for the meticulous care given to seat comfort and acoustics.',
                '目につきやすい特徴（外観）に加えて、本質的な価値（音響・快適さ）を高く評価する表現です。'
            ),
            (
                '高山への登山では体力の消耗（　　　）、急激な気温の変化にどう備えるかが大きな課題となる。',
                'もさることながら',
                ['にすぎず', 'とばかりに', 'がてら'],
                'In high-mountain climbing, physical exhaustion is certainly a factor, but how to prepare for sudden temperature changes is an even bigger challenge.',
                '困難や課題が複数ある中で、特に注意すべき重要な点を後半で取り上げる用法です。'
            ),
        ],
    },
    67: {
        'formula': '名詞 ／ 動詞・形容詞普通形（ナ形・名詞＋である） ＋ <strong>のみならず</strong>',
        'similar': '〜だけでなく / 〜にとどまらず / 〜ばかりか',
        'wrong': (
            '今日は宿題を少しやったのみならず、テレビを見てゆっくり休んだ。',
            '「AのみならずB（も）」は「AだけでなくさらにBも」と同類の事柄を付け加えて強調する文語表現なので、日常の雑多な行動を並べる文には不向きです。',
            '"AのみならずB" is a formal literary construction that adds B on top of A ("not only A, but also B"), unsuitable for listing casual daily actions.'
        ),
        'comp': (
            '〜だけでなく',
            'not only ~, but also',
            '日常会話から書き言葉まで幅広く使えます。「〜のみならず」は硬い書き言葉やスピーチで使われ、後件に「〜も」を伴うことが多いです。',
            'Used across all registers, while 〜のみならず is a formal literary equivalent often paired with も in the main clause.',
            '再生可能エネルギーの普及は、環境保護のみならず地域の雇用創出にも貢献する。',
        ),
        'quiz': [
            (
                '彼女はバイオリンの演奏技術が優れている（　　　）、作曲や編曲の分野でも稀有な才能を発揮している。',
                'のみならず',
                ['にすぎず', 'には及ばず', 'もさることながら'],
                'Not only does she excel in violin performance technique, she also demonstrates rare talent in the fields of composition and arrangement.',
                '動詞・形容詞の普通形に接続し、さらなる才能や実績を累加して述べる格調高い表現です。'
            ),
            (
                'この植物由来の新素材は、軽くて丈夫である（　　　）、使用後に土の中で自然に還る特性を持っている。',
                'のみならず',
                ['にほかならず', 'に忍びず', 'に堪えず'],
                'This new plant-derived material is not only light and sturdy, it also has the property of returning naturally to the soil after use.',
                'ナ形容詞・名詞の述語には「〜であるのみならず」の形で接続します。'
            ),
            (
                '基礎科学の研究は、目先の産業応用（　　　）、人類の知の地平を広げる上で欠かせない営みだ。',
                'のみならず',
                ['にすぎず', 'はおろか', 'にかまけて'],
                'Basic scientific research is an indispensable endeavor not only for immediate industrial applications, but also for expanding the horizons of human knowledge.',
                '名詞に直接ついて「AだけでなくBにおいても」と論説文で視野を広げる際によく使われます。'
            ),
            (
                '十分な睡眠をとることは、肉体的な疲労を回復させる（　　　）、記憶の整理や集中力の維持にも直結する。',
                'のみならず',
                ['に足らず', 'には及ばず', 'とばかりに'],
                'Getting sufficient sleep not only recovers physical fatigue, it is also directly linked to organizing memory and maintaining concentration.',
                '「動詞辞書形＋のみならず、…にも〜する」の形で二つの効果を並べる定番の構文です。'
            ),
        ],
    },
    68: {
        'formula': '名詞A ＋ <strong>であれ</strong> ＋ 名詞B ＋ <strong>であれ</strong> ／ 疑問詞＋名詞 ＋ <strong>であれ</strong>',
        'similar': '〜であろうと〜であろうと / 〜にしても〜にしても / 〜にかかわらず',
        'wrong': (
            'コーヒーであれ紅茶であれ、私は今すぐ冷たい水だけが一番飲みたい。',
            '「AであれBであれ」は「AとBのどちらの場合であっても同じことが言える」という包括的な条件を表すため、両方とも無関係に否定して別のものを挙げる文脈には合いません。',
            '"AであれBであれ" means "whether A or B, the same principle applies," so it does not fit rejecting both to ask for water.'
        ),
        'comp': (
            '〜といい〜といい',
            'both A and B (pointing out examples)',
            '「AといいBといい」は具体例を二つ挙げて「どちらも素晴らしい（またはひどい）」と評価しますが、「AであれBであれ」は仮定の条件を網羅します。',
            'While 〜といい〜といい praises or criticizes two concrete aspects of something, 〜であれ〜であれ states a rule that holds regardless of whether A or B is the case.',
            '屋内であれ屋外であれ、作業中は安全規則を厳守しなければならない。',
        ),
        'quiz': [
            (
                '規模の大小を問わず、大企業であれ中小企業（　　　）、情報管理の徹底は現代の経営に不可欠だ。',
                'であれ',
                ['といい', 'なり', 'だの'],
                'Regardless of size, whether a large corporation or a small-to-medium enterprise, thorough information management is indispensable in modern business.',
                '対になる二つの名詞を並べて「どちらの立場・場合であっても例外なく」と述べる表現です。'
            ),
            (
                '個人競技であれ団体競技（　　　）、日頃の地道な基礎練習が本番での自信につながる点は変わらない。',
                'であれ',
                ['といい', 'やら', 'なり'],
                'Whether an individual sport or a team sport, the fact that steady daily basic practice leads to confidence in actual competition remains the same.',
                '後件に「〜は同じだ／変わらない／〜なければならない」などの普遍的な判断が来ます。'
            ),
            (
                '賛成の立場であれ反対の立場（　　　）、会議では客観的なデータに基づいた議論が求められる。',
                'であれ',
                ['といい', 'だの', 'なり'],
                'Whether one is in favor or opposed, discussions based on objective data are required at the meeting.',
                '相反する二つの立場を提示し、双方に共通して求められる規範を示します。'
            ),
            (
                '経験者であれ未経験者（　　　）、新しい現場に入る際はまず安全教育の講習を受ける決まりになっている。',
                'であれ',
                ['といい', 'やら', 'だの'],
                'Whether experienced or inexperienced, everyone is required to take a safety education course first when entering a new work site.',
                '条件の違いにかかわらず全員に同じ規則が適用されることを明確に表します。'
            ),
        ],
    },
    69: {
        'formula': '名詞A ＋ <strong>といい</strong> ＋ 名詞B ＋ <strong>といい</strong>',
        'similar': '〜も〜もどちらも / 〜にしても〜にしても / 〜からして',
        'wrong': (
            '明日といい明後日といい、来週の会議の資料を今日中に印刷してください。',
            '「AといいBといい」は対象が持つ二つの側面（色といい形といい等）を挙げて全体を評価・感嘆する表現なので、単なる日程の列挙や依頼文には使えません。',
            '"AといいBといい" highlights two representative aspects of a subject to evaluate the whole (e.g., "both its color and its shape"), not future dates in a request.'
        ),
        'comp': (
            '〜であれ〜であれ',
            'whether A or B (hypothetical condition)',
            '「〜であれ〜であれ」は未確定の仮定条件ですが、「〜といい〜といい」は目の前にある事実の二つの側面を取り上げて評価します。',
            'Whereas 〜であれ〜であれ sets hypothetical conditions, 〜といい〜といい points to two actual features to praise or criticize the whole.',
            'この器は色合いといい手触りといい、まさに名工の技が光る逸品だ。',
        ),
        'quiz': [
            (
                '新しく発売された万年筆は、書き心地といい軸の美しいデザイン（　　　）、非の打ちどころがない。',
                'といい',
                ['であれ', 'なり', 'だの'],
                'Both in its writing feel and in the beautiful design of its barrel, the newly released fountain pen is beyond reproach.',
                '対象の代表的な二つの長所を挙げて「どの面を見ても本当に素晴らしい」と称賛する典型例です。'
            ),
            (
                'あの老舗旅館は、心のこもった接客といい四季の風情を映した庭園（　　　）、訪れる人を魅了してやまない。',
                'といい',
                ['であれ', 'なり', 'やら'],
                'Both with its heartfelt hospitality and its garden reflecting the charm of the four seasons, that long-established inn never ceases to enchant visitors.',
                '「AといいBといい、すべてが優れている」と全体の印象をまとめる際によく使われます。'
            ),
            (
                '先週の機材トラブルといい今回の発注ミス（　　　）、最近は確認不足による手違いが続きすぎている。',
                'といい',
                ['であれ', 'なり', 'がてら'],
                'What with last week\'s equipment trouble and this ordering mistake, lately there have been far too many mix-ups due to insufficient checking.',
                '好ましくない出来事を二つ並べて「どちらも困ったことで、全体的に問題がある」と嘆く文脈でも使われます。'
            ),
            (
                '彼女のプレゼンテーションは、資料の構成といい落ち着いた話しぶり（　　　）、新人とは思えない完成度だった。',
                'といい',
                ['であれ', 'なり', 'だの'],
                'Both in the structure of her materials and in her composed manner of speaking, her presentation had a level of perfection hard to believe for a newcomer.',
                '具体的な評価ポイントを二つ例示して、全体の完成度の高さを裏づける用法です。'
            ),
        ],
    },
    70: {
        'formula': '名詞＋の ／ 動詞・形容詞普通形（ナ形＋な） ＋ <strong>こととて</strong>',
        'similar': '〜ことだから / 〜ものだから / 〜という事情なので',
        'wrong': (
            '今日は天気がとても良いこととて、洗濯物がすぐ乾いて嬉しかった。',
            '「〜こととて」は主に「不案内なこととて」「突然のこととて」など、不十分な点や失敗について事情を述べて詫びたり弁解したりする文脈で使われます。',
            '"〜こととて" is a formal/humble expression used mainly to explain unavoidable circumstances when apologizing or asking for understanding, not for sunny laundry days.'
        ),
        'comp': (
            '〜ことだから',
            'because it is ~ (typical of someone)',
            '「真面目な彼のことだから」のように人物の性格から行動を推量するのに使われ、「〜こととて」のような詫び・弁明のニュアンスはありません。',
            'Used to infer behavior from someone\'s known character, whereas 〜こととて explains extenuating circumstances in apologies.',
            'まだ着任したばかりで不慣れなこととて、至らぬ点も多々あるかと存じますがご指導ください。',
        ),
        'quiz': [
            (
                'なにぶん急な決定だった（　　　）、事前のご案内が皆様に行き届きませんでしたことを深くお詫び申し上げます。',
                'こととて',
                ['とあって', 'ともなると', 'とばかりに'],
                'Because it was such a sudden decision, we deeply apologize that prior notice did not reach everyone.',
                'お詫びの手紙や挨拶で、やむを得ない事情を控えめに説明する定型表現です。'
            ),
            (
                '初めての土地で道も不案内な（　　　）、約束の時刻に少し遅れてしまい大変申し訳ありませんでした。',
                'こととて',
                ['はおろか', 'にかまけて', 'をよそに'],
                'Because it was my first time in the area and I was unfamiliar with the roads, I am terribly sorry for arriving slightly late for our appointment.',
                'ナ形容詞には「〜な＋こととて」の形で接続し、不手際の理由を丁寧に述べます。'
            ),
            (
                '子どもの頃の古い記憶の（　　　）、細かな日付や場所までははっきりと思い出すことができない。',
                'こととて',
                ['とばかりに', 'にひきかえ', 'を皮切りに'],
                'Since it is an old memory from childhood, I cannot clearly recall the exact dates or places.',
                '名詞には「の＋こととて」の形で接続し、「そういう性質のものだから仕方がない」と事情を示します。'
            ),
            (
                '専門外の分野の（　　　）、踏み込んだ見解を述べるのは控えさせていただきます。',
                'こととて',
                ['はおろか', 'に先駆けて', 'そばから'],
                'As it is a field outside my specialty, I will refrain from stating an in-depth opinion.',
                '自分の限界や立場を理由に、控えめに辞退・遠慮する場面でよく用いられます。'
            ),
        ],
    },
    71: {
        'formula': '名詞 ／ 動詞・形容詞普通形 ＋ <strong>とあって</strong>',
        'similar': '〜という特別な状況なので / 〜だから / 〜こともあって',
        'wrong': (
            '私は今朝は少し眠いとあって、コーヒーを二杯飲んでから仕事に出かけた。',
            '「〜とあって」は世間の注目を集める催しや珍しい条件など、客観的に見て特別な状況があるために多くの人が動くような場面で使い、個人の些細な体調には使いません。',
            '"〜とあって" describes how a special, notable circumstance naturally draws a strong reaction or crowd, not an individual\'s routine sleepiness.'
        ),
        'comp': (
            '〜とあっては',
            'if it is the case that ~ (obligation)',
            '「は」がつく「〜とあっては」は「もしそんな状況なら〜しないわけにはいかない」と話し手の強い義務感や決意を表す点で異なります。',
            'With は, 〜とあっては expresses personal obligation ("given X, I must do Y"), whereas 〜とあって objectively explains why a situation occurs.',
            '五年に一度の特別展とあって、美術館の前には開館前から長い列ができていた。',
        ),
        'quiz': [
            (
                '地元出身の建築家が設計した新図書館のお披露目（　　　）、開館初日は大勢の市民でにぎわった。',
                'とあって',
                ['こととて', 'とばかりに', 'ともなく'],
                'Because it was the unveiling of the new library designed by a local architect, opening day was crowded with many citizens.',
                '特別なイベントや話題性のある条件が理由となって、盛況や活気が生まれる様子を表します。'
            ),
            (
                '今年の秋は天候に恵まれてぶどうの出来が特に良い（　　　）、収穫祭には例年以上の観光客が訪れた。',
                'とあって',
                ['はおろか', 'にかまけて', 'を限りに'],
                'Because the weather was favorable this autumn and the grape crop was especially good, more tourists than usual visited the harvest festival.',
                '動詞・形容詞の普通形に接続し、好条件が重なったことによる自然な結果を述べます。'
            ),
            (
                '樹齢三百年の桜が満開を迎えた週末（　　　）、公園周辺の駐車場はどこも午前中から満車だった。',
                'とあって',
                ['こととて', 'そびれて', 'がてら'],
                'As it was the weekend when the 300-year-old cherry tree reached full bloom, all the parking lots around the park were full from the morning.',
                '名詞に直接接続し、「そのような特別な週末だから当然〜となった」と説明します。'
            ),
            (
                '普段は非公開の重要文化財が特別に見学できる（　　　）、全国から多くの歴史ファンが集まった。',
                'とあって',
                ['ともなしに', 'にかこつけて', 'をよそに'],
                'Because an Important Cultural Property normally closed to the public was open for special viewing, many history fans gathered from across the country.',
                'めったにない貴重な機会であることを理由として示す定番の用法です。'
            ),
        ],
    },
    72: {
        'formula': '名詞 ＋ <strong>をもって</strong>',
        'similar': '〜によって（手段） / 〜を区切りとして（期限）',
        'wrong': (
            '明日の朝八時をもって、私はいつもの電車に乗って会社へ行きます。',
            '時を表す名詞につく「〜をもって」は、営業・受付・任期などの公的な終了や開始の区切りを宣言する表現であり、個人の日常の行動時刻には使えません。',
            '"〜をもって" with time expressions marks the formal cutoff or commencement of an official period/event, not an individual\'s daily commute time.'
        ),
        'comp': (
            '〜を限りに',
            'starting from (cutoff); for the last time',
            '「〜を限りに」は「今日を限りに引退する」のようにこれまで続いたことを完全に断ち切る場面に使われ、手段の意味はありません。',
            'Used only for permanently ending a continued state/habit, whereas 〜をもって is used for both official time cutoffs and formal means.',
            '選考の結果につきましては、後日書面をもってご本人様へ通知いたします。',
        ),
        'quiz': [
            (
                '誠に勝手ながら、当店は今月三十{日|にち}（　　　）三十年間の営業を終了させていただくこととなりました。',
                'をもって',
                ['を皮切りに', 'をよそに', 'に先駆けて'],
                'We regret to announce that our store will be ending its thirty years of business as of the thirtieth of this month.',
                '日時を表す名詞について、契約・営業・受付などの終了時点を公的に告げる定型表現です。'
            ),
            (
                '開会のご挨拶（　　　）、本日の国際シンポジウムの幕開けとさせていただきます。',
                'をもって',
                ['にかまけて', 'をおいて', 'をよそに'],
                'With these opening remarks, we hereby declare today\'s international symposium open.',
                '式典や行事で「これによって〜とする」と手段・区切りを格調高く述べる用法です。'
            ),
            (
                '奨学金の採用審査の結果は、来月中旬に郵送の通知書（　　　）正式にお知らせいたします。',
                'をもって',
                ['にひきかえ', 'ともなく', 'がてら'],
                'The results of the scholarship selection screening will be formally announced by means of a written notice sent by mail in mid-next month.',
                '公的な連絡手段や方法（「書面をもって」「発表をもって」）を表す実務表現です。'
            ),
            (
                '本年度の助成金の申請受付は、本日午後五時到着分（　　　）締め切らせていただきます。',
                'をもって',
                ['をものともせず', 'にかこつけて', 'とばかりに'],
                'Applications for this fiscal year\'s grant will close as of arrivals at 5:00 p.m. today.',
                '公募や手続きの締め切り時刻・期限を厳格に明示する際によく使われます。'
            ),
        ],
    },
    73: {
        'formula': '名詞（今日・今回・今月など時や回数を表す語／声・力など） ＋ <strong>を限りに</strong>',
        'similar': '〜を最後にして / 〜をもって終える / 〜の限界まで',
        'wrong': (
            '来週の月曜日を限りに、新しいスポーツジムに通い始めることにした。',
            '時の名詞につく「〜を限りに」は「その時点を最後にして、それまで続いていたことをやめる」という意味なので、新しく始めることには使えません。',
            '"〜を限りに" after a time noun marks the final time something is done before stopping for good, so it cannot introduce starting a new habit.'
        ),
        'comp': (
            '〜を皮切りに',
            'starting with ~ (as the first in a series)',
            '「〜を限りに」が「それを最後として終了する」のに対し、「〜を皮切りに」は「それを最初として次々に展開する」という正反対の意味です。',
            'Opposite in direction: 〜を限りに marks the final cutoff, whereas 〜を皮切りに marks the starting point of a series.',
            'ベテランの彼は今シーズンの最終戦を限りに、現役を引退する意向を表明した。',
        ),
        'quiz': [
            (
                '二十年間続いた人気のラジオ番組が、今夜の放送（　　　）幕を下ろすことになった。',
                'を限りに',
                ['を皮切りに', 'をよそに', 'をおいて'],
                'The popular radio program that ran for twenty years will come to a close with tonight\'s broadcast as its final episode.',
                '「今夜の放送を最後にして終了する」という区切りを表す最も典型的な用法です。'
            ),
            (
                '健康診断の結果を受けて、父は今日（　　　）甘い炭酸飲料をきっぱりやめると宣言した。',
                'を限りに',
                ['を皮切りに', 'をものともせず', 'に先駆けて'],
                'Following the results of his health checkup, my father declared that starting today he would quit sweet carbonated drinks for good.',
                'これまで続けていた習慣を「今日を最後にして断ち切る」という強い決意を示します。'
            ),
            (
                '伝統ある市民吹奏楽団の指揮者は、来月の定期演奏会（　　　）退任し、後進に道を譲るそうだ。',
                'を限りに',
                ['を皮切りに', 'にかまけて', 'をよそに'],
                'The conductor of the traditional civic wind orchestra will step down after next month\'s regular concert and hand over the baton to a successor.',
                '役職や活動の最終回・最終{日|び}を示す文脈でよく用いられます。'
            ),
            (
                '舞台のクライマックスで、主演俳優は声（　　　）せりふを叫び、観客の心を強く揺さぶった。',
                'を限りに',
                ['はおろか', 'にかこつけて', 'ともなしに'],
                'At the climax of the play, the lead actor shouted his lines at the top of his voice, deeply moving the audience.',
                '「声を限りに（出せる限界の声で）」「力を限りに（精いっぱいの力で）」という慣用表現としても重要です。'
            ),
        ],
    },
    74: {
        'formula': '疑問詞＋動詞辞書形 ／ 動詞辞書形 ＋ <strong>ともなく</strong>',
        'similar': '〜ともなしに / 特に〜するつもりもなく自然に / 何気なく',
        'wrong': (
            '来週の資格試験に絶対合格するため、毎日参考書を読むともなく五時間勉強した。',
            '「〜ともなく」ははっきりした目的や意識を持たずにぼんやり何かをしている様子を表すため、強い目的意識を伴う猛勉強の文脈とは矛盾します。',
            '"〜ともなく" describes doing something absentmindedly without a clear intention, contradicting focused five-hour exam study.'
        ),
        'comp': (
            '〜がてら',
            'while doing; on the occasion of',
            '「〜がてら」は「散歩がてら本屋に寄る」のように二つの目的を意識的に兼ねるのに対し、「〜ともなく」は無意識・無目的の動作を表します。',
            'While 〜がてら intentionally combines two purposes, 〜ともなく indicates an unconscious or aimless action.',
            '窓の外を眺めるともなく眺めていると、庭の梅の木に小さな鳥が飛んできた。',
        ),
        'quiz': [
            (
                '待合室で雑誌を（　　　）めくっていたら、偶然にも故郷の特集記事が目に留まった。',
                '見るともなく',
                ['見るばかりに', '見るにとどまらず', '見るにかまけて'],
                'While flipping through a magazine in the waiting room without really looking for anything, a feature article on my hometown caught my eye by chance.',
                '「同じ動詞を重ねる（見るともなく見る）」または同類の動作に続けて、何気ない様子を表します。'
            ),
            (
                '夕暮れの商店街を歩いていると、（　　　）香ばしい焼き菓子の甘い匂いが漂ってきた。',
                'どこからともなく',
                ['どこをおいても', 'どこにひきかえ', 'どこを皮切りに'],
                'As I was walking through the shopping street at dusk, a sweet, fragrant aroma of baked goods drifted over from somewhere or other.',
                '「疑問詞＋から／へ＋ともなく」で、出どころや方向がはっきりしないまま自然に感じられることを表します。'
            ),
            (
                'カフェで読書をしていたら、隣の席の会話が（　　　）耳に入ってきて思わず苦笑してしまった。',
                '聞くともなく',
                ['聞くはおろか', '聞くともなると', '聞くに先駆けて'],
                'While I was reading at a cafe, the conversation at the next table reached my ears without my trying to listen, making me smile wryly.',
                '聞こうという意識がないのに自然と聞こえてしまう場面で「聞くともなく耳に入る」は頻出です。'
            ),
            (
                '春の陽気に誘われて、（　　　）川沿いの遊歩道を歩いていたら隣町の公園まで来ていた。',
                'どこへ行くともなく',
                ['どこへ行くにとどまらず', 'どこへ行くにも及ばず', 'どこへ行くにかこつけて'],
                'Lured out by the warm spring weather, I walked along the riverside promenade with no particular destination in mind and found myself at a park in the next town.',
                '目的地を定めずにぶらぶらと歩く様子を「どこへ行くともなく歩く」と表現します。'
            ),
        ],
    },
    75: {
        'formula': '疑問詞（＋助詞） ／ 動詞辞書形 ＋ <strong>ともなしに</strong>',
        'similar': '〜ともなく / 何気なく〜するうちに / はっきり意識せずに',
        'wrong': (
            '設計図の寸法を測るともなしに、ミリ単位まで正確に確認して記録した。',
            '「〜ともなしに」は意識を集中せず漠然と行う動作に使われるため、ミリ単位で厳密に確認する作業には使えません。',
            '"〜ともなしに" describes an unfocused, absentminded action, so it cannot be used for precise millimeter-level measurements.'
        ),
        'comp': (
            '〜ともなく',
            'absentmindedly; from somewhere or other',
            '意味・用法ともにほぼ同じで置き換え可能ですが、「〜ともなしに」の方がやや文語的で叙情的な響きがあります。',
            'Virtually interchangeable with 〜ともなく, with 〜ともなしに sounding slightly more literary and lyrical.',
            'ラジオから流れる音楽を聴くともなしに聴きながら、旅の荷物を整理した。',
        ),
        'quiz': [
            (
                '机の引き出しを整理していたら、誰が書いた（　　　）古い風景のスケッチが一枚出てきた。',
                'ともなしに',
                ['とばかりに', 'ともなると', 'にとどまらず'],
                'While tidying up my desk drawer, an old landscape sketch came out without it being clear who had drawn it.',
                'はっきり特定できない・意識されていない様子を柔らかく述べる表現です。'
            ),
            (
                '夜の海辺で波の音を（　　　）聞いているうちに、張り詰めていた気持ちが少しずつほぐれていった。',
                '聞くともなしに',
                ['聞くはおろか', '聞くにかまけて', '聞くを皮切りに'],
                'As I listened absentmindedly to the sound of the waves on the beach at night, my tense feelings gradually relaxed.',
                '「動詞辞書形＋ともなしに＋同じ動詞」で、特に意識せず自然とその動作をしている様子を描写します。'
            ),
            (
                '会議の休憩時間になると、参加者たちの間で（　　　）次回の共同研究の話題が持ち上がった。',
                '誰からともなしに',
                ['誰をおいても', '誰にひきかえ', '誰にかこつけて'],
                'When the break in the meeting arrived, the topic of the next joint research project came up naturally without anyone in particular starting it.',
                '「誰からともなしに（誰が言い出したともはっきりしないまま自然に）」は定番の慣用表現です。'
            ),
            (
                '電車の車窓から流れる田園風景を（　　　）眺めていると、幼い頃に過ごした祖父母の家を思い出した。',
                '見るともなしに',
                ['見るに忍びず', '見るに堪えず', '見るにとどまらず'],
                'Gazing absentmindedly at the rural scenery flowing past the train window, I remembered my grandparents\' house where I spent time as a child.',
                'ぼんやりと視線を向けているうちに記憶や連想が広がる場面によく合います。'
            ),
        ],
    },
    76: {
        'formula': '名詞 ／ 動詞ます形 ＋ <strong>ながらに（して）</strong>',
        'similar': '〜の状態のままで / 〜と同時に（生まれながらに）',
        'wrong': (
            '彼は音楽を聴きながらにして、毎朝三十分間ジョギングをしている。',
            '単なる二つの動作の同時進行（音楽を聴きながら走る）には普通の「〜ながら」を使い、「〜ながらに（して）」は「本来の状態を変えずに・生まれつき」という特別な文脈に限られます。',
            'Simple simultaneous actions use plain 〜ながら; 〜ながらに(して) is reserved for "from birth" or "without leaving/changing one\'s state."'
        ),
        'comp': (
            '〜ながら',
            'while doing (simultaneous action)',
            '日常の同時進行には「〜ながら」を使います。「〜ながらに（して）」は「涙ながらに」「居ながらにして」「生まれながらに」「昔ながらの」など固定的な表現で用いられます。',
            'Plain 〜ながら is for everyday simultaneous actions, whereas 〜ながらに(して) occurs in set literary phrases meaning "in tears," "from birth," or "without leaving home."',
            'インターネットの発達により、自宅に居ながらにして世界中の論文を閲覧できるようになった。',
        ),
        'quiz': [
            (
                '彼女は（　　　）絶対音感に恵まれており、一度聴いた曲ならすぐにピアノで再現することができた。',
                '生まれながらに',
                ['生まれがてら', '生まれそびれて', '生まれっぱなしで'],
                'She was blessed with perfect pitch from birth and could immediately reproduce on the piano any piece she heard once.',
                '「生まれながらに（生まれつき）」は、天賦の才能や性質を表す代表的な表現です。'
            ),
            (
                '被災地の復興に尽くした医師が、当時の仲間たちの協力を（　　　）語る姿に会場全体が胸を打たれた。',
                '涙ながらに',
                ['涙まみれで', '涙ずくめで', '涙がてらに'],
                'The entire audience was deeply moved by the sight of the doctor, who had devoted himself to reconstruction, speaking tearfully of the cooperation of his colleagues at the time.',
                '「涙ながらに語る／訴える」は、涙を流しながら感情を込めて話す様子を表す慣用表現です。'
            ),
            (
                'オンライン展示の導入によって、遠方に住む人々も自宅に（　　　）博物館の貴重な収蔵品を鑑賞できる。',
                '居ながらにして',
                ['居るにとどまらず', '居るにかまけて', '居るを皮切りに'],
                'With the introduction of online exhibitions, people living far away can appreciate the museum\'s precious collection without leaving home.',
                '「居ながらにして（その場所から移動することなく）」は極めて頻出の重要表現です。'
            ),
            (
                'この宿場町には、江戸時代の面影を今に伝える（　　　）木造の旅籠が軒を連ねている。',
                '昔ながらの',
                ['昔じみた', '昔ぶった', '昔がてらの'],
                'In this post town, traditional wooden inns that convey the atmosphere of the Edo period to the present day stand side by side.',
                '「昔ながらの＋名詞」で、昔からの状態ややり{方|かた}がそのまま変わらずに残っていることを表します。'
            ),
        ],
    },
    77: {
        'formula': 'ナ形容詞語幹 ／ 名詞（失礼・無礼など） ＋ <strong>きわまる</strong> ／ イ形容詞く形 ＋ <strong>てきわまりない</strong>',
        'similar': '〜極まりない / この上なく〜だ / 非常に〜だ',
        'wrong': (
            '今日のランチで食べたパスタは、美味しくてきわまる味だった。',
            '「〜きわまる」は主にナ形容詞語幹・漢語名詞に直接ついて「不愉快きわまる」「失礼きわまる」のように否定的な評価を極限まで強調する表現であり、日常の「美味しい」にはつきません。',
            '"〜きわまる" attaches directly to na-adjective stems or Sino-Japanese nouns (often negative, like rude or unpleasant) to mean "extremely," not to i-adjectives like delicious.'
        ),
        'comp': (
            '〜極まりない',
            'extremely; boundlessly ~',
            'ほぼ同義で「失礼きわまる行為」「失礼極まりない行為」のように両方使えますが、文末の言い切りでは「〜きわまりない」の方が多く使われます。',
            'Nearly identical in meaning and usage, though 〜きわまる is especially common when directly modifying a noun (e.g., 失礼きわまる態度).',
            '事前の連絡もなく約束を反故にするとは、誠意を欠いた無礼きわまる対応だ。',
        ),
        'quiz': [
            (
                '安全確認の手順を省いて作業を進めるとは、現場の責任者として（　　　）行為と言わざるを得ない。',
                '軽率きわまる',
                ['軽率めいた', '軽率じみた', '軽率ぶった'],
                'Proceeding with the work while skipping safety confirmation procedures must be called an extremely reckless act for a site supervisor.',
                '「ナ形容詞語幹＋きわまる＋名詞」の形で、程度が甚だしいことを厳しく批判します。'
            ),
            (
                '根拠のない噂をさも事実であるかのように言い触らすのは、（　　　）話だ。',
                '迷惑きわまる',
                ['迷惑めいた', '迷惑ぶった', '迷惑がてらの'],
                'Spreading groundless rumors as if they were fact is an utterly troublesome and annoying matter.',
                '「迷惑きわまる」「失礼きわまる」「不愉快きわまる」はN1で最頻出のコロケーションです。'
            ),
            (
                'どれほど親しい間柄であっても、相手のプライバシーに土足で踏み込むような発言は（　　　）。',
                '無礼きわまる',
                ['無礼めいている', '無礼ぶっている', '無礼そびれている'],
                'No matter how close the relationship, remarks that trample on the other person\'s privacy are extremely rude.',
                '文末で言い切って強い憤りや批判の意を表す用法です。'
            ),
            (
                '十分な検証も行わずに不完全な製品を市場に出すなど、消費者に対して（　　　）態度だ。',
                '不誠実きわまる',
                ['不誠実めいた', '不誠実ぶった', '不誠実びた'],
                'Releasing an incomplete product to the market without conducting sufficient verification is an extremely insincere attitude toward consumers.',
                '道義的な問題や態度の悪さを最上級に強調する硬い表現です。'
            ),
        ],
    },
    78: {
        'formula': '動詞辞書形 ／ イ形容詞 ／ ナ形容詞語幹・名詞 ＋ <strong>といったらない</strong> ／ <strong>といったらありはしない</strong>',
        'similar': '言葉で言い表せないほど〜だ / 〜極まりない / 実に〜だ',
        'wrong': (
            'この本は三百ページといったらない厚さなので、三日で読み終えた。',
            '「〜といったらない」は感情や感覚の程度が「言葉では表現できないほどすごい・ひどい」と感嘆する表現なので、客観的な数値やページ数には使えません。',
            '"〜といったらない" expresses that an emotion or sensation is beyond words, so it cannot modify objective numbers like 300 pages.'
        ),
        'comp': (
            '〜かぎりだ',
            'feel extremely ~ (subjective emotion)',
            '「〜かぎりだ」は「嬉しいかぎりだ」「羨ましいかぎりだ」のように感情形容詞に限られますが、「〜といったらない」は状況の凄まじさ・大変さにも広く使えます。',
            'While 〜かぎりだ is restricted to emotion adjectives, 〜といったらない vividly emphasizes extreme states, hardships, or sensations in general.',
            '冬の日本海から吹きつける吹雪の冷たさといったらなく、顔も上げられないほどだった。',
        ),
        'quiz': [
            (
                '徹夜で仕上げた論文のデータが保存前に消えてしまったときの（　　　）なかった。',
                '悔しさといったら',
                ['悔しさにとどまらず', '悔しさもさることながら', '悔しさにかまけて'],
                'The frustration I felt when the paper data I had stayed up all night finishing disappeared before saving was simply beyond words.',
                '「名詞（形容詞の名詞化）＋といったらない／といったらなかった」で極限の感情を表します。'
            ),
            (
                '引っ越し当日の（　　　）、荷造りと掃除に追われて昼食をとる暇さえなかった。',
                '忙しさといったらなく',
                ['忙しさはおろか', '忙しさにとどまらず', '忙しさにかこつけて'],
                'The busyness on moving day was indescribable; we were so swamped with packing and cleaning that we didn\'t even have time for lunch.',
                '文中で「〜といったらなく、…」と続けて、その程度がいかに凄まじかったかを具体例で説明します。'
            ),
            (
                '山頂の展望台から眺めたご来光の（　　　）といったらなく、登山客の誰もが息をのんで見入っていた。',
                '美しさ',
                ['美しいことか', '美しいものか', '美しいばかり'],
                'The beauty of the sunrise viewed from the summit observation deck was beyond description, leaving every hiker watching in breathless awe.',
                'マイナスの事態だけでなく、自然の美しさや感動が並外れている場面でも用いられます。'
            ),
            (
                '真夏の閉め切った倉庫の中の（　　　）、{五分|ごふん}と立っていられないほどだ。',
                '蒸し暑さといったらない',
                ['蒸し暑さにすぎない', '蒸し暑さには及ばない', '蒸し暑さにとどまらない'],
                'The muggy heat inside the closed warehouse in midsummer is beyond words; you can\'t stand in there for even five minutes.',
                '身体的な感覚や環境の過酷さを実感たっぷりに強調する表現です。'
            ),
        ],
    },
    79: {
        'formula': '感情を表すイ形容詞 ／ ナ形容詞な形 ＋ <strong>かぎりだ</strong>',
        'similar': 'この上なく〜だ / 心から〜と思う / 〜てたまらない',
        'wrong': (
            'この新しいパソコンは処理速度が速いかぎりなので、仕事がとてもはかどる。',
            '「〜かぎりだ」は「嬉しい・寂しい・羨ましい・心強い・残念な」など話し手の主観的な感情を表す形容詞にのみ接続し、客観的な性能や性質には使えません。',
            '"〜かぎりだ" only attaches to adjectives of subjective emotion (happy, lonely, envious, reassuring, regrettable), not objective properties like processing speed.'
        ),
        'comp': (
            '〜の至り',
            'the utmost ~ (humble/formal noun phrase)',
            '「光栄の至り」「恐縮の至り」のように特定の漢語名詞につく格式高い慣用表現であるのに対し、「〜かぎりだ」は和語の感情形容詞にも広くつきます。',
            'While 〜の至り attaches to specific Sino-Japanese nouns in formal greetings, 〜かぎりだ pairs with a wider range of emotion adjectives.',
            '卒業した教え子たちがそれぞれの分野で活躍している知らせを聞くのは、教師として嬉しいかぎりだ。',
        ),
        'quiz': [
            (
                '不慣れな海外出張で不安だっただけに、現地事情に詳しい先輩が同行してくれるのは（　　　）。',
                '心強いかぎりだ',
                ['心強いきらいがある', '心強いにとどまらない', '心強いにすぎない'],
                'Precisely because I was anxious about an unfamiliar overseas business trip, having a senior colleague well-versed in local conditions accompany me is immensely reassuring.',
                '「心強いかぎりだ（これ以上ないほど安心で頼もしい）」は頻出のコロケーションです。'
            ),
            (
                '自然豊かな湖畔の別荘で毎朝鳥のさえずりを聞きながら暮らせるとは、実に（　　　）。',
                '羨ましいかぎりだ',
                ['羨ましいにすぎない', '羨ましいには及ばない', '羨ましいにとどまらない'],
                'Being able to live in a nature-rich lakeside villa listening to birdsong every morning is truly enviable beyond measure.',
                '他者の恵まれた環境や境遇に対して「本当に羨ましい」と感想を述べる定番表現です。'
            ),
            (
                '一年間準備を重ねてきた野外音楽祭が、当日の暴風雨で中止になってしまったのは（　　　）。',
                '残念なかぎりだ',
                ['残念なきらいがある', '残念なにほかならない', '残念なにとどまらない'],
                'It is profoundly regrettable that the outdoor music festival we spent a full year preparing for was canceled due to a storm on the day.',
                'ナ形容詞には「〜な＋かぎりだ」の形で接続し、落胆や無念の思いを深く表します。'
            ),
            (
                '共に苦労を乗り越えてきた同僚が遠くの支社へ転勤してしまうのは、本当に（　　　）。',
                '寂しいかぎりだ',
                ['寂しいにすぎない', '寂しいまでもない', '寂しいには及ばない'],
                'It is truly lonely beyond words that the colleague with whom I overcame so many hardships is transferring to a distant branch.',
                '別れや変化に対するしみじみとした寂しさを率直に表す用法です。'
            ),
        ],
    },
    80: {
        'formula': '動詞辞書形・た形・ている形 ／ 名詞＋の ＋ <strong>手前</strong>',
        'similar': '〜という立場・体面があるから / 〜の目の前では / 〜た以上は',
        'wrong': (
            '駅の改札を出る手前、急に雨が降り出したので傘を差した。',
            '場所の「少し前」や時間の「直前」ではなく、文法表現の「〜手前」は「自分の体面・プライドや相手への義理を考えると〜できない／しなければならない」という心理的拘束を表します。',
            'As a grammar pattern, 〜手前 means "to save face / out of consideration for one\'s stance in front of others," not a temporal "just before."'
        ),
        'comp': (
            '〜以上（は）',
            'now that; since',
            '「〜以上は」は客観的な責任や道理を述べますが、「〜手前」は「大口を叩いた手前、今さら引けない」のように世間体や面目（メンツ）を気にするニュアンスが強いです。',
            'While 〜以上は appeals to objective duty, 〜手前 emphasizes saving face or maintaining appearances before others.',
            '子どもたちに規則正しい生活を教える親の手前、自分だけ夜更かしをするわけにはいかない。',
        ),
        'quiz': [
            (
                '会議で「必ず今月中に達成します」と大見えを切った（　　　）、途中で弱音を吐くわけにはいかない。',
                '手前',
                ['かたわら', 'がてら', '拍子に'],
                'Having boasted at the meeting that I would definitely achieve it within this month, I cannot complain or back down partway through.',
                '過去の自分の発言によって生じた体面・プライドから「〜するわけにはいかない」と続く典型例です。'
            ),
            (
                '後輩たちに基本の大切さを厳しく指導している（　　　）、自分自身が準備を怠るような姿は見せられない。',
                '手前',
                ['かたがた', 'ともなく', '折に'],
                'Given that I strictly instruct my juniors on the importance of the basics, I cannot let them see me neglecting preparation myself.',
                '現在の自分の立場や普段の言動に照らして、恥ずかしい行動はとれないという自制を表します。'
            ),
            (
                'せっかく友人が私のために時間を割いて作ってくれた（　　　）、苦手な食材だとは言い出せなかった。',
                '手前',
                ['かたわら', 'そびれ', '拍子に'],
                'Out of consideration for my friend who took the time to cook especially for me, I couldn\'t bring myself to say that it was an ingredient I disliked.',
                '相手の好意や労力を思うと、失礼な態度はとれないという気遣いを示します。'
            ),
            (
                '自分から「手伝うよ」と申し出た（　　　）、忙しくなったからといって今さら断ることはできない。',
                '手前',
                ['ともなしに', 'ながらに', 'がてら'],
                'Having offered to help on my own initiative, I cannot turn around and refuse now just because I got busy.',
                '「約束した手前」「引き受けた手前」のように、一度言ったことへの責任感を表す頻出パターンです。'
            ),
        ],
    },
    81: {
        'formula': '動詞ます形 ＋ <strong>そびれる</strong>',
        'similar': '〜する機会を逃す / 〜しそこなう / タイミングを失って〜できない',
        'wrong': (
            '今日は目覚まし時計が鳴らなかったので、朝七時に起きそびれて八時に起きた。',
            '「〜そびれる」は「しようと思っていたのに、きっかけやタイミングを逃してできなくなる（言いそびれる・聞きそびれる等）」という意図的動作に使われ、無意識の起床には使いません。',
            '"〜そびれる" means missing the right timing or chance to perform an intended action (like speaking up or asking), not oversleeping.'
        ),
        'comp': (
            '〜そこなう',
            'fail to do; almost do',
            '「〜そこなう」は技術の失敗や危機一髪（乗りそこなう・落ちそこなう）にも使いますが、「〜そびれる」は心理的・状況的にタイミングを逸してできないままでいることに焦点を当てます。',
            'While 〜そこなう covers technical failures or near misses, 〜そびれる focuses on missing the opportune moment to do something.',
            '会議の雰囲気が緊迫していて、最後まで自分の意見を言いそびれてしまった。',
        ),
        'quiz': [
            (
                '相手があまりに忙しそうだったので、借りていた本のお礼を（　　　）そのまま別れてしまった。',
                '言いそびれて',
                ['言いがてら', '言いっぱなしで', '言いかたわら'],
                'Because the other person looked so busy, I missed the chance to thank them for the book I had borrowed and parted ways as it was.',
                '「言いそびれる」「聞きそびれる」は、声をかけるタイミングを失ってしまう最も代表的な例です。'
            ),
            (
                '昼の十二時にかかってきた長電話の対応に追われ、今日はすっかり昼食を（　　　）しまった。',
                '食べそびれて',
                ['食べがてら', '食べっぱなしで', '食べかたがた'],
                'Caught up in handling a long phone call that came in at noon, I completely missed the chance to eat lunch today.',
                '他の用事に遮られて、本来の時間帯に食事をとる機会を逃したことを表します。'
            ),
            (
                '講演会の最後に質問しようと手を挙げかけたが、時間切れになってしまい連絡先を（　　　）。',
                '聞きそびれた',
                ['聞きがてらだ', '聞きっぱなしだ', '聞きかたわらだ'],
                'I was about to raise my hand to ask a question at the end of the lecture, but time ran out and I missed the chance to ask for their contact information.',
                '「しようと思っていたのに、状況が許さず機会を逸した」という残念な気持ちを示します。'
            ),
            (
                '人気の特別展はいつでも行けると思って先延ばしにしていたら、会期が終わって（　　　）しまった。',
                '見そびれて',
                ['見がてらで', '見っぱなしで', '見かたわらで'],
                'Thinking I could go see the popular special exhibition anytime, I kept putting it off until the exhibition period ended and I missed seeing it.',
                '「見そびれる」「買いそびれる」のように、期間内に機会を逃してしまう場面でもよく使われます。'
            ),
        ],
    },
    82: {
        'formula': '名詞＋の ／ 動詞辞書形 ＋ <strong>かたわら</strong>',
        'similar': '〜する一方で / 本業の合間に〜もする / 〜のかたわら',
        'wrong': (
            '彼はスマホでニュースを見るかたわら、トーストを食べてコーヒーを飲んだ。',
            '「〜かたわら」は「本業の仕事や学業を続けながら、並行してもう一つのまとまった活動（研究・執筆・ボランティア等）を行う」場合に使い、数分間の同時動作には使えません。',
            '"〜かたわら" describes engaging in a secondary pursuit or activity alongside one\'s main occupation over a period of time, not eating toast while looking at a phone.'
        ),
        'comp': (
            '〜がてら',
            'while on the occasion of (one trip/action)',
            '「〜がてら」は一回の移動や行動のついでに別の用事を済ませる表現であり、長期的な二つの活動の並行には「〜かたわら」を使います。',
            'Whereas 〜がてら combines a side errand into a single outing, 〜かたわら describes two ongoing activities or roles pursued in parallel.',
            '彼女は総合病院で医師として働くかたわら、地域の健康講座で講師を務めている。',
        ),
        'quiz': [
            (
                '叔父は市役所に勤務する（　　　）、週末には地元の少年サッカーチームの指導にあたっている。',
                'かたわら',
                ['がてら', 'かたがた', '拍子に'],
                'While working at city hall, my uncle also coaches a local youth soccer team on weekends.',
                '「本業（市役所勤務）＋かたわら＋もう一つの継続的な活動（指導）」という典型的な構文です。'
            ),
            (
                '彼は大学院で物理学の研究を続ける（　　　）、科学の魅力を子どもたちに伝える絵本を執筆している。',
                'かたわら',
                ['そびれて', '手前', 'ともなく'],
                'Alongside continuing his physics research in graduate school, he writes picture books that convey the appeal of science to children.',
                '専門の研究と並行して、別の有意義な創作活動にも力を注いでいる様子を表します。'
            ),
            (
                '母は自宅で音楽教室を開く（　　　）、地域の合唱団の伴奏者としても長年活動してきた。',
                'かたわら',
                ['がてら', 'かたがた', 'ばかりに'],
                'Alongside running a music school at home, my mother has also been active for many years as an accompanist for a local choir.',
                '長期にわたって二つの役割を両立させていることを述べる文脈に最適です。'
            ),
            (
                '伝統工芸の職人を育成する本業の（　　　）、彼は海外の美術館で日本の木工技術を紹介する講演を行っている。',
                'かたわら',
                ['手前', '折に', '拍子に'],
                'Alongside his main profession of training traditional craft artisans, he gives lectures introducing Japanese woodworking techniques at art museums abroad.',
                '名詞には「の＋かたわら」の形で接続します。'
            ),
        ],
    },
    83: {
        'formula': '名詞（主に二字漢語：御礼・挨拶・見舞い・報告など） ＋ <strong>かたがた</strong>',
        'similar': '〜を兼ねて / 〜のついでに / 〜がてら',
        'wrong': (
            'スーパーへ夕飯の買い出しに行くかたがた、クリーニング屋に寄ってシャツを受け取った。',
            '「〜かたがた」は挨拶状や改まった会話で「ご挨拶かたがた」「お礼かたがた」のように社交・儀礼的な二つの目的を兼ねる際に使い、日常の買い物には使いません。',
            '"〜かたがた" is a formal/polite expression used when combining two social or business purposes (like offering thanks and reporting), not everyday grocery errands.'
        ),
        'comp': (
            '〜がてら',
            'while doing; by way of (casual outing)',
            '「〜がてら」は「散歩がてら」など日常の気軽な外出にも広く使えますが、「〜かたがた」は改まったビジネスや社交の場面に限定されます。',
            'While 〜がてら is used for casual outings like taking a walk, 〜かたがた is restricted to formal greetings, visits, or business correspondence.',
            '日頃のお礼かたがた、新しく完成したカタログをお届けに上がりました。',
        ),
        'quiz': [
            (
                '退院された恩師のお見舞い（　　　）、先日受賞した論文の報告に自宅を訪ねた。',
                'かたがた',
                ['かたわら', '手前', 'ともなく'],
                'Combining a get-well visit to my former mentor who had been discharged from the hospital with a report on my recently awarded paper, I visited his home.',
                '「お見舞いかたがた〜する」は、二つの改まった訪問目的を兼ねる代表的な表現です。'
            ),
            (
                '新任のご挨拶（　　　）、来期の共同事業についてご意見を伺いたく存じます。',
                'かたがた',
                ['かたわら', 'そびれて', '拍子に'],
                'By way of greeting you upon my new appointment, I would also like to hear your views regarding next term\'s joint project.',
                'ビジネス文書や丁寧な挨拶で「ご挨拶かたがた」は最もよく使われる定型句です。'
            ),
            (
                '先日お借りした資料の返却（　　　）、調査の進捗状況を先方の担当者にご報告した。',
                'かたがた',
                ['かたわら', 'ともなしに', 'ながらに'],
                'Combining the return of the materials borrowed the other day with a progress report on the survey, I visited the person in charge.',
                '実務上の用件（返却）ともう一つの用件（報告）を一度の訪問で合わせて行うことを表します。'
            ),
            (
                '連休中に実家へ帰省した折、結婚の報告（　　　）久しぶりに親戚の家を訪ねて回った。',
                'かたがた',
                ['かたわら', '手前', 'を限りに'],
                'When I returned to my parents\' home during the holidays, I visited relatives\' houses for the first time in a while, combining it with reporting my marriage.',
                '人生の節目の報告と親戚への訪問という、二つの礼儀上の目的を兼ねる文脈です。'
            ),
        ],
    },
    84: {
        'formula': '名詞（散歩・買い物など） ／ 動詞ます形 ＋ <strong>がてら</strong>',
        'similar': '〜のついでに / 〜を兼ねて / 〜かたがた',
        'wrong': (
            '来年度の予算案を策定しがてら、三か年の中期経営計画も同時に作成した。',
            '「〜がてら」は主に「移動や外出を伴う気軽な行動のついでに、もう一つのこともする」場面で使われ、机上の重い業務計画を二つ同時に行う文脈には向きません。',
            '"〜がてら" is used when doing something on the side during a physical outing or light activity (like a walk or shopping), not heavy corporate budget planning.'
        ),
        'comp': (
            '〜かたわら',
            'alongside one\'s main occupation',
            '「〜かたわら」は本業と副業のように独立した二つの活動を長期的に並立させますが、「〜がてら」は一つの行動の機会を利用してついでに別のことをします。',
            'Whereas 〜かたわら parallels two ongoing roles over time, 〜がてら piggybacks a secondary action onto a single outing or activity.',
            '休日の朝、愛犬の散歩がてら駅前のパン屋に寄って焼きたてのパンを買った。',
        ),
        'quiz': [
            (
                '天気の良い休日に、運動不足の解消（　　　）、隣町の図書館まで自転車で出かけた。',
                'がてら',
                ['かたわら', '手前', 'ともなく'],
                'On a sunny day off, by way of getting some exercise, I rode my bicycle out to the library in the neighboring town.',
                '「図書館へ行く」という行動と「運動不足の解消」という目的を兼ねる日常的な用法です。'
            ),
            (
                '新しくできた商店街を（　　　）、夕食に使う新鮮な野菜と魚を買って帰った。',
                '見物がてら',
                ['見物かたわら', '見物そびれて', '見物っぱなしで'],
                'While sightseeing around the newly opened shopping street, I bought fresh vegetables and fish for dinner on my way home.',
                '動詞のます形（見物し）またはサ変名詞について、外出のついでに別の用事も済ませることを表します。'
            ),
            (
                '長時間パソコンに向かっていたので、気分転換に外の空気を（　　　）郵便局まで歩いて行った。',
                '吸いがてら',
                ['吸いかたわら', '吸いかたがた', '吸いそびれて'],
                'Because I had been facing my computer for a long time, I walked to the post office to get a breath of fresh air for a change of pace.',
                '「動詞ます形＋がてら」で、主たる移動の中に軽いリフレッシュなどの目的を含めます。'
            ),
            (
                '秋晴れの週末、紅葉の写真を（　　　）、山あいの静かな温泉郷へ日帰り旅行に出かけた。',
                '撮りがてら',
                ['撮りかたわら', '撮りかたがた', '撮りっぱなしで'],
                'On a clear autumn weekend, we went on a day trip to a quiet hot-spring village in the mountains, combining it with taking photos of the autumn leaves.',
                '楽しみや趣味の活動を兼ねてどこかへ出かける文脈で非常によく使われます。'
            ),
        ],
    },
}

DATA = GRAMMAR

