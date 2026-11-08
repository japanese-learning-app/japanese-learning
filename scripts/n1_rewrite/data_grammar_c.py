# -*- coding: utf-8 -*-
"""
N1 grammar data part C (gids 85-127).
"""

GRAMMAR = {
    85: {
        'formula': '名詞 ＋ <strong>をよそに（して）</strong>',
        'similar': '〜を顧みず / 〜も構わず / 〜を無視して',
        'wrong': (
            '両親の温かい励ましをよそに、彼は見事に志望校に合格した。',
            '「〜をよそに」は周囲の心配・反対・騒ぎなどを気にかけずに行動する場合に使います。好意的な「励まし」を受け入れて成功した文脈には使えません。',
            '"〜をよそに" is used when someone acts with indifference toward surrounding worry, opposition, or commotion, not when succeeding thanks to warm encouragement.'
        ),
        'comp': (
            '〜を顧みず',
            'disregarding; without looking back at',
            '自分の危険や立場・利益を考えずに、勇気を持って行動するニュアンスが強い表現です。',
            'Emphasizes acting courageously without regard for personal danger, status, or self-interest.',
            '彼は身の危険を顧みず、増水した川へ飛び込んで子どもを救い出した。',
        ),
        'quiz': [
            (
                '周囲の強い反対（　　　）、彼は長年勤めた商社を辞めて陶芸の道へ進んだ。',
                'をよそに',
                ['を皮切りに', 'を境に', 'を限りに'],
                'Indifferent to strong opposition around him, he quit the trading company where he had worked for many years and pursued pottery.',
                '周囲の反対や心配をまったく気にせず独自の行動をとることを表します。'
            ),
            (
                '住民たちの不安（　　　）、大規模な再開発の工事計画は次々と進められていった。',
                'をよそに',
                ['を契機に', 'を頼りに', 'を抜きにして'],
                'Disregarding the residents\' anxiety, the large-scale redevelopment construction plans proceeded one after another.',
                '「不安」「懸念」「騒ぎ」などの名詞につき、それを無視して事態が進む様子を示します。'
            ),
            (
                '世間の激しい騒ぎ（　　　）、その老画家は静かな山奥のアトリエで絵を描き続けた。',
                'をよそに',
                ['を機に', 'を巡って', 'を通して'],
                'Far removed from the intense commotion of the public, the elderly painter kept painting in a quiet studio deep in the mountains.',
                '世間の騒動や噂を自分とは無関係なものとして受け流す態度を表します。'
            ),
            (
                '親の心配（　　　）、息子はリュックひとつで半年間の海外放浪の旅に出かけてしまった。',
                'をよそに',
                ['をはじめ', 'を問わず', 'を通じて'],
                'Indifferent to his parents\' worry, the son set off on a six-month backpacking trip abroad with just a single rucksack.',
                '身近な人の心配を気に留めずに自分のやりたいことを貫く場面でよく使われます。'
            ),
        ],
    },
    86: {
        'formula': '名詞 ＋ <strong>をものともせず（に）</strong>',
        'similar': '〜に屈せず / 〜を乗り越えて / 〜にもめげず',
        'wrong': (
            '彼は毎朝の軽い散歩をものともせずに、健康を維持している。',
            '「〜をものともせず」は大きな困難・悪条件・逆境に立ち向かう場面で使うため、「軽い散歩」のような日常の平易な行動には不自然です。',
            '"〜をものともせず" requires a serious hardship, adversity, or severe condition as its object, not something trivial like a light morning walk.'
        ),
        'comp': (
            '〜を押して',
            'pushing through; braving (illness/busyness)',
            '病気・怪我・多忙・悪天候など、本来なら控えるべき事情を無理に乗り越えて行動することを表します。',
            'Focuses on forcing oneself to act despite illness, injury, or a busy schedule.',
            '高熱を押して舞台に立った俳優の熱演に、会場から大きな拍手が送られた。',
        ),
        'quiz': [
            (
                '吹き荒れる吹雪（　　　）、救助隊員たちは険しい雪山を一歩ずつ登っていった。',
                'をものともせず',
                ['をよそに', 'をきっかけに', 'を差し置いて'],
                'Braving the raging blizzard, the rescue team members climbed the steep snowy mountain step by step.',
                '厳しい自然環境や危機的な状況を少しも恐れずに立ち向かう姿を描写します。'
            ),
            (
                '度重なる実験の失敗（　　　）、研究チームはついに画期的な新素材を開発した。',
                'をものともせずに',
                ['を皮切りに', 'を境にして', 'をよそにして'],
                'Undeterred by repeated experimental failures, the research team finally developed a groundbreaking new material.',
                '逆境や失敗に屈せず努力を続ける肯定的な評価の文脈で用いられます。'
            ),
            (
                '完全アウェーの激しい重圧（　　　）、若き選手たちは堂々たる演技を披露した。',
                'をものともせず',
                ['を抜きにして', 'をめぐって', 'を頼りに'],
                'Defying the intense pressure of a completely away crowd, the young athletes delivered a magnificent performance.',
                '「重圧」「逆風」「悪条件」などの困難を表す名詞と強く結びつきます。'
            ),
            (
                '大きな怪我からの長期離脱（　　　）、彼女は復帰戦で見事な優勝を果たした。',
                'をものともせず',
                ['を限りに', 'を尻目に', 'をはじめとして'],
                'Overcoming a long absence due to a major injury, she achieved a brilliant victory in her comeback match.',
                '苦境を問題にしない強い精神力や行動力を称賛する表現です。'
            ),
        ],
    },
    87: {
        'formula': '名詞 ＋ <strong>を押して</strong> ／ <strong>を押し切って</strong>',
        'similar': '〜を顧みず / 〜にもかかわらず / 〜を乗り越えて',
        'wrong': (
            '絶好の晴天を押して、地域のマラソン大会が盛大に開催された。',
            '「〜を押して」は病気・高齢・多忙・悪天候・反対など、行動を妨げる不利な条件を無理に振り切って行うときに使います。好条件には使えません。',
            '"〜を押して" is used when acting despite unfavorable conditions like illness, busyness, or opposition, so it cannot be used with favorable weather.'
        ),
        'comp': (
            '〜をものともせず',
            'defying; undeterred by',
            '困難を困難とも思わない力強さを強調するのに対し、「〜を押して」は無理をしてでも実行するニュアンスがあります。',
            'While 〜をものともせず stresses fearless strength, 〜を押して emphasizes forcing oneself to act despite strain or opposition.',
            '彼女は足首の痛みを押して最後まで走り抜いたが、試合後に病院へ運ばれた。',
        ),
        'quiz': [
            (
                'ご多忙のところ（　　　）本日の記念式典にご出席いただき、心より感謝申し上げます。',
                'を押して',
                ['をよそに', 'を境に', 'を皮切りに'],
                'We sincerely thank you for taking time out of your busy schedule to attend today\'s commemorative ceremony.',
                '「ご多忙のところを押して」は挨拶状やスピーチで頻出する丁重な慣用表現です。'
            ),
            (
                '医師の静止（　　　）、老舗旅館の女将は退院した翌日から玄関に立って客を迎えた。',
                'を押して',
                ['を契機に', 'を抜きに', 'を通じて'],
                'Despite her doctor\'s advice to rest, the proprietress of the long-established inn stood at the entrance welcoming guests the day after leaving the hospital.',
                '周囲の制止や反対、体調不良などを無理に振り切って行動することを表します。'
            ),
            (
                '80歳という高齢（　　　）、その植物学者は自ら離島の険しい森へ調査に向かった。',
                'を押して',
                ['を限りに', 'をめぐって', 'を頼りに'],
                'Despite his advanced age of eighty, the botanist personally headed into the steep forest of a remote island for research.',
                '体力的なハンディや無理を押して行動を起こす場面で用いられます。'
            ),
            (
                '激しい腰の痛み（　　　）ステージに立ち続けた座長の姿に、劇団員たちは胸を打たれた。',
                'を押して',
                ['を機に', 'を問わず', 'をはじめ'],
                'The troupe members were deeply moved by the sight of their leader continuing to stand on stage despite severe lower back pain.',
                '「病をおして」「痛みを押して」のように身体の不調を我慢して行う連語がよく使われます。'
            ),
        ],
    },
    88: {
        'formula': '名詞 ＋ <strong>をおいて（ほかに）〜ない</strong>',
        'similar': '〜以外にない / 〜を除いてない / 〜ならではの',
        'wrong': (
            'この簡単な入力作業を任せられるのは、ベテランの田中さんをおいてたくさんいる。',
            '「〜をおいて」の後ろには必ず「〜ない」「だれが〜か（反語）」などの否定・限定表現が来て、「唯一それだけだ」と強調します。',
            '"〜をおいて" must be followed by a negative or rhetorical expression indicating uniqueness, never an affirmative like "there are many."'
        ),
        'comp': (
            '〜ならではの',
            'unique to; only possible with',
            'その人や場所だからこそ持つ特別な魅力を肯定的に述べる表現で、文末に否定を伴いません。',
            'Positively highlights a unique charm or quality specific to someone or someplace without requiring a negative predicate.',
            '長年現場で培った職人ならではの勘が、わずかな歪みを見抜いた。',
        ),
        'quiz': [
            (
                'この難航している国際提携の交渉をまとめ上げられる人物は、経験豊富な彼（　　　）いない。',
                'をおいて',
                ['をよそに', 'を境に', 'を皮切りに'],
                'There is no one besides him, with his wealth of experience, who can successfully conclude these stalled international partnership negotiations.',
                '「Aをおいて〜ない」で「A以外には適任者や該当するものが存在しない」と強く限定します。'
            ),
            (
                '繊細な古文書の修復を託せる専門家は、国内では山本先生（　　　）考えられない。',
                'をおいて',
                ['を押して', 'を経て', 'をめぐって'],
                'When it comes to an expert to whom we can entrust the restoration of delicate ancient documents, no one in the country is conceivable besides Professor Yamamoto.',
                '「〜をおいて考えられない」の形で唯一の選択肢であることを強調します。'
            ),
            (
                '長年の夢を実現するチャンスは、条件がすべて整った今（　　　）二度と訪れないだろう。',
                'をおいて',
                ['をものともせず', 'を尻目に', 'を問わず'],
                'The chance to realize this long-held dream will likely never come again if not now, when all conditions are in place.',
                '人物だけでなく「今をおいて」「ここをおいて」のように時や場所にも使えます。'
            ),
            (
                '地域の伝統工芸を次の世代へ継承できる若者は、情熱あふれる彼女（　　　）誰がいようか。',
                'をおいて',
                ['を機に', 'を頼りに', 'を抜きにして'],
                'Who else besides her, brimming with passion, could pass on the region\'s traditional crafts to the next generation?',
                '文末に反語表現「誰がいようか」を伴い、彼女しかいないことを強く訴えています。'
            ),
        ],
    },
    89: {
        'formula': '名詞／疑問詞節 ＋ <strong>はさておき</strong>',
        'similar': '〜はともかく / 〜は別として / 〜は措いて',
        'wrong': (
            '本日の会議では、最も重要な予算案はさておき、それについて今すぐ徹底的に議論しましょう。',
            '「AはさておきB」はAを一旦脇に置いて別の話題Bに移る表現なので、Aそのものを直後に議論する文脈には使えません。',
            '"AはさておきB" sets A aside to focus on B, so you cannot immediately discuss A itself in the main clause.'
        ),
        'comp': (
            '〜はともかく（として）',
            'setting aside; regardless of',
            '「〜はさておき」とほぼ同義ですが、「冗談はさておき」のような決まり文句では「はさておき」が優先されます。',
            'Nearly synonymous, though 〜はさておき is preferred in set phrases like "冗談はさておき" (joking aside) when pivoting to the main topic.',
            'デザインの好みはともかく、この椅子の座り心地と耐久性は抜群だ。',
        ),
        'quiz': [
            (
                '冗談（　　　）、来月の新店舗オープンに向けた具体的な準備状況を報告してください。',
                'はさておき',
                ['をよそに', 'を押して', 'を境に'],
                'Joking aside, please report on the concrete status of preparations for next month\'s new store opening.',
                '「冗談はさておき」は雑談や前置きを切り上げて本題に入る際の代表的な慣用表現です。'
            ),
            (
                ' 최종的な勝敗の結果（　　　）、最後まで諦めずに走り抜いた選手たちに拍手を送りたい。'.replace(' 최종的な', '最終的な'),
                'はさておき',
                ['をおいて', 'を皮切りに', 'をものともせず'],
                'Setting aside the final outcome of victory or defeat, I want to applaud the athletes who ran all the way through without giving up.',
                '結果や細かな事情は一旦別にして、より大切な点を評価するときに使われます。'
            ),
            (
                '実現できるかどうか（　　　）、まずは自由な発想で新しい企画のアイデアを出し合おう。',
                'はさておき',
                ['を契機に', 'を限りに', 'に値する'],
                'Setting aside whether it can be realized or not, let\'s first brainstorm new project ideas freely.',
                '疑問詞節「〜かどうか」を受けて、その問題を後回しにする用法です。'
            ),
            (
                '細かい費用の内訳（　　　）、全体の方針について皆様のご意見を伺いたいと思います。',
                'はさておき',
                ['を経て', 'にあって', 'のみか'],
                'Leaving aside the detailed breakdown of costs for now, I would like to hear everyone\'s opinions on the overall policy.',
                '二次的な事項を後回しにし、優先すべき本題に焦点を当てる表現です。'
            ),
        ],
    },
    90: {
        'formula': '名詞 ＋ <strong>はどうあれ</strong> ／ <strong>はともかく</strong>',
        'similar': '〜はどうであれ / 〜にかかわらず / 〜はともかくとして',
        'wrong': (
            '明日の天気はどうあれ、雨が降ったら屋外イベントは中止になります。',
            '「AはどうあれB」は「Aがどんな状態であってもBは変わらない」という意味なので、Aの条件次第でBが変わる文脈には使えません。',
            '"AはどうあれB" means B holds true regardless of what A is, so it contradicts a clause where B changes depending on A.'
        ),
        'comp': (
            '〜いかんにかかわらず',
            'regardless of',
            'より硬い公的・実務的な表現で、「理由のいかんにかかわらず」のように規則や通知文で好まれます。',
            'More formal and administrative, frequently used in official rules and notices such as "regardless of the reason."',
            '出欠のいかんにかかわらず、今月末までに返信はがきをご投函ください。',
        ),
        'quiz': [
            (
                '経緯（　　　）、お客様にご不便をおかけしたことに対しては誠意をもって謝罪すべきだ。',
                'はどうあれ',
                ['をよそに', 'を押して', 'をおいて'],
                'Whatever the circumstances may have been, we should apologize sincerely for causing inconvenience to the customer.',
                '「理由・経緯・過程はどうあれ」の形で、途中の事情に関係なく結論が変わらないことを示します。'
            ),
            (
                '周囲の評価（　　　）、自分が信じた芸術の道を最後まで追求したことに悔いはない。',
                'はどうあれ',
                ['を境に', 'を皮切りに', 'んがため'],
                'Whatever the evaluation of those around me may be, I have no regrets about pursuing the artistic path I believed in to the very end.',
                '他人の評価や外的な状況に左右されない強い姿勢を表します。'
            ),
            (
                '元の動機（　　　）、結果として地域の清掃活動に多くの若者が集まったのは喜ばしいことだ。',
                'はどうあれ',
                ['をものともせず', 'を経て', 'んとする'],
                'Whatever the original motive may have been, it is wonderful that many young people gathered for the local cleanup activity as a result.',
                '動機やきっかけがどうであれ、現在の結果を肯定的に捉える文脈でよく使われます。'
            ),
            (
                '外観の古さ（　　　）、この木造建築は耐震補強が施されており安全性には全く問題がない。',
                'はどうあれ',
                ['を契機に', 'を限りに', 'に難くない'],
                'Regardless of how old the exterior looks, this wooden building has undergone seismic reinforcement and has no safety issues whatsoever.',
                '表面的な状態がどうであっても本質的な事実は揺るがないことを述べます。'
            ),
        ],
    },
    91: {
        'formula': '動詞た形 ＋ <strong>拍子に</strong>',
        'similar': '〜はずみで / 〜途端に / 〜瞬間に',
        'wrong': (
            '彼は三年間じっくり計画した拍子に、新しいIT企業を立ち上げた。',
            '「〜拍子に」は瞬間的な動作のはずみで偶発的・無意識に何かが起きるときに使うため、計画的・意図的な行動には使えません。',
            '"〜拍子に" describes something happening accidentally from the momentum of a sudden action, so it cannot be used for planned, intentional actions.'
        ),
        'comp': (
            '〜途端に',
            'just as; the moment that',
            '前件の直後に変化が起きる点では似ていますが、「〜拍子に」は物理的な勢いや動作のはずみで不意に結果が生じるニュアンスに特化しています。',
            'While both mark immediate succession, 〜拍子に specifically implies physical momentum or a sudden movement triggering an unintended result.',
            '立ち上がった途端にめまいがして、思わず近くの壁に手をついた。',
        ),
        'quiz': [
            (
                '階段で足を滑らせて転んだ（　　　）、持っていた眼鏡のフレームが曲がってしまった。',
                '拍子に',
                ['折に', '前提で', '極みに'],
                'By the momentum of slipping and falling on the stairs, the frame of the glasses I was holding got bent.',
                '「転んだ拍子に」「立ち上がった拍子に」など、瞬間的な動作のはずみで思わぬ事態が生じることを表します。'
            ),
            (
                '冷たい風に吹かれてくしゃみをした（　　　）、ぎっくり腰になって動けなくなった。',
                '拍子に',
                ['境に', '至りに', 'よそに'],
                'Right at the moment I sneezed from the cold wind, I threw my back out and couldn\'t move.',
                '身体の急な動きが引き金となって偶発的なアクシデントが起きる典型的な例です。'
            ),
            (
                '慌ててカバンから書類を取り出した（　　　）、大切な領収書が床に散らばってしまった。',
                '拍子に',
                ['末に', 'あまり', 'あげく'],
                'In the rush of pulling documents out of my bag, important receipts scattered across the floor.',
                '後件には話し手が意図しなかったマイナスの結果やハプニングが来ることが多いです。'
            ),
            (
                '驚いて後ろを振り返った（　　　）、テーブルの角に肘を強くぶつけてしまった。',
                '拍子に',
                ['うちに', 'ついでに', 'ばかりに'],
                'As I turned around in surprise, I accidentally bumped my elbow hard against the corner of the table.',
                '「ついでに」のような意図的な行動とは異なり、不可抗力のはずみを表します。'
            ),
        ],
    },
    92: {
        'formula': '動詞辞書形・た形／名詞＋の ＋ <strong>折（に／には）</strong>',
        'similar': '〜際に / 〜機会に / 〜ときに',
        'wrong': (
            '毎朝歯を磨く折に、洗面所の鏡をサッと拭くようにしている。',
            '「〜折に」は改まった機会や特別なタイミングを表す雅語的な表現なので、毎朝の歯磨きのような日常の細かな習慣には不釣り合いです。',
            '"〜折に" is an elevated expression used for special occasions or formal opportunities, making it unnatural for mundane daily habits like brushing one\'s teeth.'
        ),
        'comp': (
            '〜際に',
            'on the occasion of; when',
            '「〜際に」はビジネスや実務全般で広く使われますが、「〜折に」はより情緒的・丁重で、手紙や挨拶で好まれます。',
            '〜際に is standard in business and procedures, whereas 〜折に sounds warmer, more literary, and more deferential in letters and greetings.',
            'お申し込みの際には、本人確認書類の写しを添えてご提出ください。',
        ),
        'quiz': [
            (
                '京都へお越しの（　　　）、ぜひ私どもの工房にもお気軽にお立ち寄りください。',
                '折には',
                ['拍子には', '境には', '極みには'],
                'When you have the occasion to visit Kyoto, please feel free to drop by our workshop as well.',
                '手紙や案内状で「お越しの折には」「上京の折には」としてよく使われる丁寧な表現です。'
            ),
            (
                '先月、恩師のお宅を訪問した（　　　）、学生時代の懐かしい写真を見せていただいた。',
                '折に',
                ['拍子に', 'よそに', 'ばかりに'],
                'On the occasion of visiting my former teacher\'s home last month, I was shown nostalgic photos from my student days.',
                '過去の特別な機会を振り返って述べる際にも自然に使われます。'
            ),
            (
                'また何かお困りのことがございました（　　　）、いつでも担当者までご相談ください。',
                '折には',
                ['拍子には', '前提には', '至りには'],
                'Should there ever be an occasion where you have any trouble again, please consult our representative at any time.',
                '目上の相手や顧客に対して礼儀正しく機会を示す表現です。'
            ),
            (
                '海外出張でウィーンを訪れた（　　　）、念願だった歴史ある歌劇場でオペラを鑑賞した。',
                '折に',
                ['拍子に', 'あげく', 'あまりに'],
                'On the occasion of visiting Vienna on an overseas business trip, I watched an opera at the historic opera house I had long wished to see.',
                '「訪れた折に」で「訪問した機会に」という改まった響きになります。'
            ),
        ],
    },
    93: {
        'formula': '名詞 ＋ <strong>を境に（して）</strong> ／ <strong>を境として</strong>',
        'similar': '〜を機に / 〜をきっかけに / 〜を分かれ目として',
        'wrong': (
            'この川を境に、両岸ともまったく同じ気候と植生が続いている。',
            '「〜を境に」は場所や時点を境界として、その前後や両側で状況・性質が大きく異なる（一変する）ことを表すため、「まったく同じ」とは矛盾します。',
            '"〜を境に" marks a boundary across which conditions differ or change dramatically, so it contradicts "completely the same on both sides."'
        ),
        'comp': (
            '〜を契機に（して）',
            'triggered by; taking the opportunity of',
            'ある出来事を積極的な「きっかけ・動機」として発展的な変化が起こる場合に用いられ、空間的な境界には使えません。',
            'Used when an event serves as a catalyst or opportunity for new development; cannot be used for physical or spatial boundaries.',
            '国際博覧会の開催を契機として、駅周辺のインフラ整備が一気に進んだ。',
        ),
        'quiz': [
            (
                '標高二千メートル付近（　　　）、山の植生は広葉樹林から高山植物へと大きく変わる。',
                'を境に',
                ['をよそに', 'を押して', 'をおいて'],
                'Around an altitude of 2,000 meters as a boundary, the mountain vegetation changes dramatically from broadleaf forest to alpine plants.',
                '空間的・地理的な境界線を挟んで様子が一変することを表す代表的な用法です。'
            ),
            (
                '30歳（　　　）体力の衰えを感じ始め、毎週末にジムで泳ぐ習慣をつけた。',
                'を境にして',
                ['をものともせず', 'を抜きにして', 'をよそにして'],
                'Starting around age thirty, I began to feel a decline in physical strength and made a habit of swimming at the gym every weekend.',
                '時間的な節目を境界として、それ以前と以後で状態が変化することを示します。'
            ),
            (
                'あの歴史的な大ヒット作の発表（　　　）、彼の作家としての人生は劇的に好転した。',
                'を境に',
                ['を押して', 'を頼りに', 'を尻目に'],
                'With the release of that historic blockbuster work as a turning point, his life as an author took a dramatic turn for the better.',
                '大きな出来事を転換点として状況がガラリと変わる文脈で使われます。'
            ),
            (
                '立秋（　　　）、朝晩の風に少しずつ秋の涼しさが感じられるようになってきた。',
                'を境に',
                ['をおいて', 'を問わず', 'をめぐって'],
                'With the first day of autumn as a turning point, the coolness of autumn has gradually become noticeable in the morning and evening breeze.',
                '季節の節目や暦の上の区切りを表す名詞ともよく共起します。'
            ),
        ],
    },
    94: {
        'formula': '名詞 ＋ <strong>を経て</strong>',
        'similar': '〜を通して / 〜を通過して / 〜の過程をたどって',
        'wrong': (
            '彼はインターネットの検索を経て、今日の天気予報を3秒で調べた。',
            '「〜を経て」は長い年月・段階的な手続き・経由地などを通過してある結果に至ることを表します。単純な手段・道具（検索で）には「〜によって／〜で」を使います。',
            '"〜を経て" indicates passing through time, stages, processes, or physical waypoints, not using a simple tool or instant method.'
        ),
        'comp': (
            '〜を通じて／〜を通して',
            'through (a medium/intermediary); throughout',
            '仲介者や手段を表す場合（「知人を通じて」「経験を通して」）に使われ、物理的な経由地や段階的な手続きには「〜を経て」が適しています。',
            'Used for intermediaries, mediums, or durations, whereas 〜を経て emphasizes passing through sequential stages, formal procedures, or waypoints.',
            '留学生活での多様な人々との交流を通して、異文化への理解を深めた。',
        ),
        'quiz': [
            (
                '幾度もの厳しい審査と改良（　　　）、新型の医療機器がついに実用化された。',
                'を経て',
                ['をよそに', 'を押して', 'をおいて'],
                'After going through numerous rigorous inspections and improvements, the new medical device was finally put into practical use.',
                '「審査・議論・試行錯誤を経て」のように、必要な過程や段階を通過することを表します。'
            ),
            (
                '十数年の歳月（　　　）、荒廃していた里山の雑木林が豊かな自然を取り戻した。',
                'を経て',
                ['を境に', 'を限りに', 'を尻目に'],
                'After the passage of more than a decade, the neglected rural woodland regained its rich natural environment.',
                '長い時間の経過を表す「歳月・年月・時を経て」は頻出のコロケーションです。'
            ),
            (
                'この国際貨物列車は、複数の国境都市（　　　）終着駅の港町へと到着する。',
                'を経て',
                ['をものともせず', 'を抜きにして', 'を問わず'],
                'This international freight train passes through several border cities before arriving at the port town of its final destination.',
                '場所を表す名詞につき、その地点を経由して目的地へ至ることを示します。'
            ),
            (
                '地域の住民説明会での合意形成（　　　）、新しい図書館の建設工事が着工された。',
                'を経て',
                ['をよそに', 'をおいて', 'を皮切りに'],
                'Following consensus building at local residents\' briefing sessions, construction work on the new library began.',
                '正式な手順やプロセスを踏んだうえで次の段階へ進む文脈で用いられます。'
            ),
        ],
    },
    95: {
        'formula': '名詞 ＋ <strong>を前提として</strong> ／ <strong>を前提に（して）</strong>',
        'similar': '〜を条件として / 〜を基礎として / 〜を踏まえて',
        'wrong': (
            '昨日偶然宝くじに当たったことを前提として、来月新車を買うことにした。',
            '「〜を前提として」は計画や議論の土台となる基本条件を置いたり仮定したりする際に使います。すでに起きた単なる過去のラッキーな出来事の理由付けには不自然です。',
            '"〜を前提として" sets a foundational condition or working assumption for a plan or argument, not a mere causal reason for a past fluke.'
        ),
        'comp': (
            '〜を踏まえて',
            'based on; taking into account',
            'すでに起きた事実・調査結果・反省点などを考慮に入れて判断することを表し、未確定の仮定条件には「〜を前提として」を使います。',
            'Means taking actual facts, survey results, or lessons learned into consideration, whereas 〜を前提として sets a precondition or assumption.',
            '前回のアンケート調査の結果を踏まえて、研修プログラムの内容を見直した。',
        ),
        'quiz': [
            (
                'この雇用契約は、半年後に正社員として登用すること（　　　）結ばれている。',
                'を前提として',
                ['をよそに', 'を押して', 'を皮切りに'],
                'This employment contract is concluded on the premise that the employee will be promoted to a regular full-time position after six months.',
                '契約や計画が成り立つための基本条件を示す典型的な使い方です。'
            ),
            (
                '双方の信頼関係（　　　）成り立つ取引では、情報の透明性が何よりも重要になる。',
                'を前提に',
                ['を境に', 'をおいて', 'を尻目に'],
                'In transactions built on the premise of mutual trust, transparency of information is more important than anything else.',
                '「〜を前提に成り立つ」の形で、物事の基礎・土台となる条件を表します。'
            ),
            (
                '大規模な自然災害が発生した場合（　　　）、自治体の避難計画が策定された。',
                'を前提として',
                ['をものともせず', 'を限りに', 'をよそにして'],
                'The municipality\'s evacuation plan was formulated on the assumption that a large-scale natural disaster occurs.',
                '起こり得る事態をあらかじめ想定して備える文脈でよく用いられます。'
            ),
            (
                'オンラインでの受講（　　　）設計されたカリキュラムのため、自宅からでも無理なく学べる。',
                'を前提として',
                ['を押して', 'を経て', 'をおいて'],
                'Because the curriculum was designed on the premise of online attendance, students can learn comfortably from home.',
                '設計や制度の最初から織り込まれている条件を説明する表現です。'
            ),
        ],
    },
    96: {
        'formula': '名詞 ＋ <strong>をもってすれば</strong> ／ <strong>をもってしても</strong>',
        'similar': '〜を使えば / 〜の力があれば / 〜によれば',
        'wrong': (
            '近くのコンビニで買った傘をもってすれば、少しぐらいの小雨なら濡れずに歩ける。',
            '「〜をもってすれば」は高度な技術・卓越した能力・豊富な経験などに対して使う格調高い表現なので、日用品の「コンビニの傘」には大げさすぎて不自然です。',
            '"〜をもってすれば" is a lofty expression reserved for exceptional skill, advanced technology, or vast experience, not everyday items like a convenience store umbrella.'
        ),
        'comp': (
            '〜をもって',
            'by means of; as of (a time/date)',
            '手段（「書面をもって通知する」）や終了時点（「本日をもって閉店する」）を表す実務表現で、能力の仮定条件には「〜をもってすれば」を使います。',
            'Marks formal means ("notify in writing") or a cutoff time ("close as of today"), whereas 〜をもってすれば expresses hypothetical capability.',
            '誠に勝手ながら、当店は今月末日をもって営業を終了いたします。',
        ),
        'quiz': [
            (
                '彼女の卓越した語学力と交渉術（　　　）、今回の海外提携も必ず成功するだろう。',
                'をもってすれば',
                ['をよそにすれば', 'を押してすれば', 'を境にすれば'],
                'With her outstanding language skills and negotiation ability, this overseas partnership will surely succeed.',
                'すぐれた能力や条件を備えていれば容易に達成できるという高い評価を表します。'
            ),
            (
                '現代の最先端の科学技術（　　　）、深海の生態系の全貌を解明することはまだ難しい。',
                'をもってしても',
                ['を皮切りにしても', 'をよそにしても', 'を限りにしても'],
                'Even with today\'s cutting-edge science and technology, it is still difficult to elucidate the full picture of deep-sea ecosystems.',
                '「〜をもってしても＋否定」で「これほど優れた力を使ってもなお不可能だ」と強調します。'
            ),
            (
                '長年の現場経験（　　　）、このような機械の不具合などすぐに原因を突き止められるはずだ。',
                'をもってすれば',
                ['をおいては', 'をものともせず', 'を尻目には'],
                'With your many years of field experience, you should be able to pinpoint the cause of a machine malfunction like this right away.',
                '相手の豊富な実績や実力を高く認めて期待を込める文脈で使われます。'
            ),
            (
                '名探偵と称される彼の鋭い洞察力（　　　）、この不可解な謎は解けなかった。',
                'をもってしても',
                ['を前提としても', 'を経ても', 'を押しても'],
                'Even with the sharp insight of him who is hailed as a master detective, this baffling mystery could not be solved.',
                '最高水準の能力をもってしても解決できない困難さを際立たせます。'
            ),
        ],
    },
    97: {
        'formula': '動詞ない形（ない→ん／する→せん） ＋ <strong>がため（に）</strong> ／ <strong>がための</strong>＋名詞',
        'similar': '〜ために / 〜を目指して / 〜ようとして',
        'wrong': (
            '明日の朝早く起きんがために、今夜は目覚まし時計を二つセットして寝る。',
            '「〜んがため（に）」は人生の大きな目標・自己表現・強い使命感などを達成しようとする文語的表現です。日常のささいな行動には「〜ために」を使います。',
            '"〜んがため(に)" is a literary expression for striving toward a lofty goal or strong ambition, too grandiose for setting an alarm clock.'
        ),
        'comp': (
            '〜ために',
            'in order to; for the sake of',
            '日常からビジネスまで幅広く使える一般的な目的表現です。「〜んがため」は強い意志と文語的な緊張感を伴います。',
            'The standard purpose expression for all registers, whereas 〜んがため conveys intense determination in a classical, dramatic tone.',
            '健康を維持するために、毎日三十分ほど歩くようにしている。',
        ),
        'quiz': [
            (
                '自らの芸術の理想を実現（　　　）、その彫刻家は私財を投げ打って制作に打ち込んだ。',
                'せんがため',
                ['する拍子に', 'する折に', 'したばかりに'],
                'In order to realize his own artistic ideals, the sculptor invested his private fortune and devoted himself to creation.',
                '「する」は「せんがため（に）」の形になり、強い目的意識を表します。'
            ),
            (
                '頂点を極め（　　　）鍛錬を重ねるアスリートたちの姿は、見る者の胸を熱くさせる。',
                'んがために',
                ['んばかりに', 'んとするに', 'ないことには'],
                'The sight of athletes training tirelessly in order to reach the pinnacle warms the hearts of onlookers.',
                '高い目標を達成するために全力を注ぐ文脈で用いられる硬い書き言葉です。'
            ),
            (
                '厳しい自然の中で生き残ら（　　　）編み出された伝統の知恵が、今もこの村に息づいている。',
                'んがために',
                ['んとして', 'ないでは', 'ようものなら'],
                'Traditional wisdom devised in order to survive in harsh nature still lives on in this village today.',
                '切実な目的や必死の思いを表す場面で高い効果を発揮します。'
            ),
            (
                '真実を明らかに（　　　）の執念が、彼を十年間に及ぶ地道な現地調査へと駆り立てた。',
                'せんがため',
                ['する拍子', 'したあげく', 'するあまり'],
                'His relentless determination to uncover the truth drove him to ten years of steady field research.',
                '「〜んがための＋名詞」の形で後ろの名詞を修飾する用法もよく見られます。'
            ),
        ],
    },
    98: {
        'formula': '動詞ない形（ない→ん／する→せん） ＋ <strong>とする</strong> ／ <strong>としている</strong>',
        'similar': '〜ようとする / 今にも〜そうだ / 〜直前だ',
        'wrong': (
            '来週の土曜日に友達と映画を見んとして、ネットでチケットを予約した。',
            '「〜んとする」は「今まさに〜しようとしている直前の緊迫した局面」や「高い目標に向かおうとする姿勢」を描く文語表現であり、日常の予定には使えません。',
            '"〜んとする" is a literary form describing an imminent moment or grand endeavor, unsuitable for casual weekend plans.'
        ),
        'comp': (
            '〜んばかりだ',
            'as if about to; almost bursting into',
            '実際にはしない（または比喩的な）状態が今にもあふれ出そうな様子を強調します。「〜んとする」は実際にその動作・変化に移ろうとする局面を表します。',
            'Describes a figurative state on the verge of overflowing, whereas 〜んとする indicates actually being about to perform an action or undergo a change.',
            '合格の知らせを聞いた彼女は、今にも泣き出さんばかりの笑顔で両親に抱きついた。',
        ),
        'quiz': [
            (
                '水平線の彼方へ今まさに沈ま（　　　）夕日が、海面を鮮やかな黄金色に染め上げた。',
                'んとする',
                ['んがための', 'ないことには', 'ようものなら'],
                'The setting sun, just about to sink beyond the horizon, dyed the sea surface a vivid golden color.',
                '自然現象などが「今まさに〜しようとしている瞬間」を格調高く描写する用法です。'
            ),
            (
                '長年の課題を克服し、新たな時代を切り{開|ひら}か（　　　）若者たちの意欲が頼もしい。',
                'んとする',
                ['んがため', 'ずにはおかない', 'てやまない'],
                'The ambition of young people striving to overcome longstanding challenges and open up a new era is inspiring.',
                '強い意志を持って何かに挑もうとする姿勢を連体修飾で描く表現です。'
            ),
            (
                '閉館時間を迎え、まさに扉を閉め（　　　）いたその時、駆け込んできた来館者がいた。',
                'んとして',
                ['んがために', 'てはかなわず', 'ないではおれず'],
                'Just as the museum reached closing time and was about to shut its doors, a visitor came rushing in.',
                '「〜ようとしていたちょうどその時」を表す文語的な表現です。'
            ),
            (
                '世界の頂点に挑ま（　　　）気迫が、スタートラインに立つ彼女の表情からひしひしと伝わってきた。',
                'んとする',
                ['んがため', 'ばこその', 'たりともの'],
                'A fierce determination to challenge the top of the world was palpably conveyed by her expression as she stood at the starting line.',
                '名詞「気迫」「姿勢」「意欲」などを修飾して劇的な効果を生みます。'
            ),
        ],
    },
    99: {
        'formula': '動詞て形 ＋ <strong>やまない</strong>',
        'similar': '心から〜している / 切に〜する / 〜てたまらない',
        'wrong': (
            '隣の部屋の住人が毎晩遅くまでギターを弾いてやまない。',
            '「〜てやまない」は話し自身の「強い祈り・願い・感謝・尊敬・期待」などの心情動詞につく表現であり、他人の具体的な物理的動作には使えません。',
            '"〜てやまない" attaches only to verbs of heartfelt emotion (wish, pray, respect, regret), not to concrete physical actions like playing the guitar.'
        ),
        'comp': (
            '〜てたまらない',
            'unbearably; cannot help feeling',
            '身体感覚や日常的な感情（「お腹が空いてたまらない」「嬉しくてたまらない」）に広く使われます。「〜てやまない」は公的な挨拶や論文での誠実な祈念に限られます。',
            'Used broadly for physical sensations and personal feelings, whereas 〜てやまない is restricted to solemn wishes, gratitude, or respect in formal contexts.',
            '久しぶりに故郷の家族に会えると思うと、今から楽しみでたまらない。',
        ),
        'quiz': [
            (
                '皆様の今後のご健勝とご活躍を、心よりお祈り申し上げ（　　　）。',
                'てやみません',
                ['てはかないません', 'てはなりません', 'ずにはいられません'],
                'I wholeheartedly pray for everyone\'s continued good health and success in the future.',
                '式典の挨拶や祝辞の結びとして「祈ってやみません」「願ってやみません」が頻出します。'
            ),
            (
                '被災された地域の{一日|いちにち}も早い復興を、国民の誰もが強く願っ（　　　）。',
                'てやまない',
                ['てたまらない', 'てかなわない', 'てならない'],
                'Every citizen earnestly wishes for the earliest possible recovery of the disaster-stricken areas.',
                '「願う」「祈る」「期待する」「惜しむ」など特定の心情動詞と結びつきます。'
            ),
            (
                '長年にわたり地域医療に献身された先生の功績を、私たちは称え（　　　）。',
                'てやまない',
                ['てはならない', 'ないではおかない', 'ようものなら'],
                'We never cease to praise the achievements of the doctor who devoted himself to community healthcare for many years.',
                '深い敬意や称賛の気持ちがいつまでも消えないことを表します。'
            ),
            (
                '若くして才能を{開|ひら}花させた彼がこの分野を去ってしまうのは、実に惜しん（　　　）ことだ。',
                'でやまない',
                ['ではたまらない', 'ではかなわない', 'ではならない'],
                'It is truly a matter of endless regret that he, having blossomed with talent so young, is leaving this field.',
                '「惜しんでやまない」「悔やんでやまない」のように深い惜別の情にも用いられます。'
            ),
        ],
    },
    100: {
        'formula': '動詞て形 ＋ <strong>からというもの</strong>',
        'similar': '〜て以来（ずっと） / 〜てからは / 〜を境に',
        'wrong': (
            '今朝7時に起きてからというもの、8時に朝食を食べて会社へ向かった。',
            '「〜てからというもの」はある重大な出来事をきっかけに「それ以来ずっと今まで継続的な変化が続いている」ことを表すため、単発の行動の連続には使えません。',
            '"〜てからというもの" emphasizes a lasting change or continuous state ever since a turning point, so it cannot be used for a simple sequence of morning actions.'
        ),
        'comp': (
            '〜てから',
            'after doing; since doing',
            '単なる動作の前後関係（「手を洗ってから食べる」）にも使えますが、「〜てからというもの」は大きな転機以降の持続的な状態変化に限定されます。',
            'Can mark any simple sequence of actions, whereas 〜てからというもの highlights a dramatic, ongoing change in state ever since a milestone event.',
            '資料をもう一度確認してから、部長にメールで提出してください。',
        ),
        'quiz': [
            (
                '昨春に愛犬を飼い始め（　　　）、父は毎朝欠かさず五時に起きて散歩に出かけている。',
                'てからというもの',
                ['た拍子に', 'た折に', 'てやまずに'],
                'Ever since we started keeping a beloved dog last spring, my father has been getting up at five every morning without fail to go for a walk.',
                'ある出来事を契機に生活習慣や態度が大きく変わり、現在まで続いていることを表します。'
            ),
            (
                '一度山登りの魅力に取り憑かれ（　　　）、彼は休日になると必ず全国の山へ出かけている。',
                'てからというもの',
                ['てはかなわず', 'んがために', 'たところで'],
                'Ever since he became captivated by the charm of mountain climbing, he goes out to mountains across the country without fail every holiday.',
                '後件には「ずっと〜ている」「毎日〜だ」などの継続・反復を表す表現が来ます。'
            ),
            (
                '娘が一人暮らしを始め（　　　）、賑やかだった家の中が急に静まり返って寂しくなった。',
                'てからというもの',
                ['んとして', 'てはたまらず', 'ないことには'],
                'Ever since my daughter started living on her own, our once lively house has suddenly become quiet and lonely.',
                '以前の状態と対比して、転機以降の状況が一変したことを強調する表現です。'
            ),
            (
                '先月ぎっくり腰を経験し（　　　）、重い荷物を持ち上げる時は常に姿勢に気をつけている。',
                'てからというもの',
                ['た拍子に', 'てはならずに', 'ようものなら'],
                'Ever since I experienced a strained back last month, I always pay attention to my posture when lifting heavy luggage.',
                '痛い経験などをきっかけに、それ以降の心がけがずっと変わったことを示します。'
            ),
        ],
    },
    101: {
        'formula': '名詞 ＋ <strong>にあって</strong> ／ <strong>にあっても</strong>',
        'similar': '〜という状況の中で / 〜において / 〜の立場にあって',
        'wrong': (
            '私は今、駅前の喫茶店にあってコーヒーを飲みながら読書をしている。',
            '「〜にあって」は特殊な時代・危機的な状況・責任ある立場などの抽象的な環境を表す硬い表現であり、具体的な建物の中にいることには「〜で」を使います。',
            '"〜にあって" refers to an abstract circumstance, era, crisis, or social position, not sitting inside a physical coffee shop.'
        ),
        'comp': (
            '〜において',
            'in; at; regarding',
            '場所・分野・時代などを客観的に示す汎用的な硬い表現です。「〜にあって」は「その特殊な状況・逆境のただ中で」という臨場感や緊迫感を伴います。',
            'A general formal marker for domain, time, or venue, whereas 〜にあって emphasizes being right in the midst of a special, often challenging situation or role.',
            '近代医療において、予防医学の重要性はますます高まっている。',
        ),
        'quiz': [
            (
                '激しい変化が続く現代社会（　　　）、常に自ら学び続ける姿勢が求められている。',
                'にあって',
                ['をよそに', 'を押して', 'をおいて'],
                'In modern society where rapid changes continue, an attitude of constantly learning on one\'s own is required.',
                '「現代社会にあって」「変革期にあって」など、特徴的な時代背景を示す定番の表現です。'
            ),
            (
                'どれほど厳しい逆境（　　　）、希望を失わずに前を向き続けた彼女の強さに感銘を受けた。',
                'にあっても',
                ['を境にしても', 'を皮切りにしても', 'を前提としても'],
                'I was deeply impressed by her strength in continuing to look forward without losing hope, even in the harshest adversity.',
                '「〜にあっても」の形で「そのような困難な状況の中に置かれてもなお」と強調します。'
            ),
            (
                '組織を率いるリーダーの立場（　　　）は、私情を挟まず公正な判断を下さなければならない。',
                'にあって',
                ['をものともせず', 'を尻目に', 'を経て'],
                'When in the position of a leader heading an organization, one must make fair judgments without letting personal feelings interfere.',
                '特定の責任ある立場や役目に身を置いていることを表す用法です。'
            ),
            (
                '通信手段が途絶えた極限状態（　　　）、隊員たちは冷静に互いの安全を確認し合った。',
                'にあって',
                ['をおいて', 'を限りに', 'をよそに'],
                'In an extreme situation where communication means were cut off, the team members calmly confirmed each other\'s safety.',
                '非常事態や特殊な環境のただ中にあることを引き締まった文体で表現します。'
            ),
        ],
    },
    102: {
        'formula': '動詞・形容詞普通形／名詞＋な ＋ <strong>のも無理はない</strong>',
        'similar': '〜のも当然だ / 〜のももっともだ / 〜のは当たり前だ',
        'wrong': (
            '彼は毎日10時間も猛勉強したのだから、試験に落ちたのも無理はない。',
            '「〜のも無理はない」は「前件の理由を考えれば、後件のような感情や結果になるのも当然で納得できる」という意味なので、因果関係が逆の文脈には使えません。',
            '"〜のも無理はない" means a reaction or result is completely understandable given the reason, so it cannot follow a contradictory cause.'
        ),
        'comp': (
            '〜わけだ',
            'no wonder; so that explains why',
            '客観的な論理的帰結（「なるほどだから〜なのだ」）を表します。「〜のも無理はない」は相手の感情や行動に対して同情・理解を示すニュアンスが強いです。',
            'Expresses logical realization ("so that\'s why"), whereas 〜のも無理はない conveys empathy and understanding toward someone\'s feelings or reaction.',
            '暖房が切れていたのか。どうりで部屋の中が寒いわけだ。',
        ),
        'quiz': [
            (
                '徹夜で長時間の作業を続けたのだから、彼が会議中に眠そうにしていた（　　　）。',
                'のも無理はない',
                ['といったらありはしない', 'に難くない', 'に値する'],
                'Since he continued working for long hours all through the night, it is no wonder he looked sleepy during the meeting.',
                '事情を考慮すればその状態になるのも当然だと同情・理解を示す表現です。'
            ),
            (
                '半年かけて準備した企画が直前で白紙になったと聞き、彼女が落胆する（　　　）。',
                'のも無理はない',
                ['てはかなわない', 'てやまない', 'べくもない'],
                'Hearing that the project she spent half a year preparing was scrapped right before implementation, it is only natural that she feels discouraged.',
                '「落胆する」「怒る」「驚く」「心配する」など、人の感情や反応を擁護する文脈でよく使われます。'
            ),
            (
                '二十年ぶりに故郷の駅前に降り立ったのだから、道に迷ってしまう（　　　）。',
                'のも無理はない',
                ['たりともない', 'のみか', 'の至りだ'],
                'Since it was the first time in twenty years that he stood in front of his hometown station, it is no wonder he lost his way.',
                '無理からぬ事情があることを認めて、失敗や戸惑いを優しく肯定します。'
            ),
            (
                '説明書の専門用語があまりに難解なので、初心者が戸惑う（　　　）だろう。',
                'のも無理はない',
                ['てはならない', 'ざるを得ない', 'に値しない'],
                'Because the technical terms in the manual are so arcane, it is quite understandable that beginners feel bewildered.',
                '「〜のももっともだ」と言い換え可能な、納得感を表す文末表現です。'
            ),
        ],
    },
    103: {
        'formula': '名詞／動詞・形容詞普通形（ナ形＋な／である） ＋ <strong>のみか</strong>',
        'similar': '〜だけでなく / 〜ばかりか / 〜にとどまらず',
        'wrong': (
            'この商品はデザインが良いのみか、価格も非常に高くて買いにくい。',
            '「AのみかB（まで・さえ）」はAに加えてさらに同方向（プラスならプラス、マイナスならマイナス）のBが重なる累加表現なので、評価が逆転する逆接には使えません。',
            '"AのみかB" is an additive pattern ("not only A, but furthermore B") where A and B share the same positive or negative orientation, not a contrast.'
        ),
        'comp': (
            '〜ばかりか',
            'not only... but also',
            '意味・用法ともに非常に近いですが、「〜のみか」の方が文語的で硬く、論説文や改まった文章で好まれます。',
            'Very close in meaning and structure, though 〜のみか is more literary and formal than 〜ばかりか.',
            '彼は謝罪しないばかりか、かえってこちらの不注意を責め立てた。',
        ),
        'quiz': [
            (
                'その老舗の和菓子は地元で愛されている（　　　）、海外の美食家からも高く評価されている。',
                'のみか',
                ['の至りか', 'の極みか', 'たりとも'],
                'Not only are the traditional sweets of that long-established shop loved locally, they are also highly praised by gourmets overseas.',
                '「〜のみならず」「〜ばかりか」と同様に、範囲や程度がさらに広がることを示します。'
            ),
            (
                '今回のシステム障害により、業務が停止した（　　　）、顧客データの復旧にも多大な時間を要した。',
                'のみか',
                ['にあって', 'をよそに', 'はさておき'],
                'Due to this system failure, not only were operations halted, but recovering customer data also took an enormous amount of time.',
                'マイナスの事態が一つにとどまらず、さらに重なって起きたことを強調します。'
            ),
            (
                '彼女は三か国語を流暢に話せる（　　　）、古代の文献を直接読み解く専門知識まで備えている。',
                'のみか',
                ['をおいて', 'を押して', '拍子に'],
                'Not only can she speak three languages fluently, she even possesses the specialized knowledge to decipher ancient documents directly.',
                '後件に「〜まで」「〜さえ」「〜も」を伴って驚きのニュアンスを強めることが多いです。'
            ),
            (
                '放置された空き家は景観を損ねる（　　　）、防災上のリスクも高めるとして対策が急がれている。',
                'のみか',
                ['折に', 'を境に', 'はどうあれ'],
                'Because abandoned houses not only mar the landscape but also increase disaster prevention risks, countermeasures are urgently needed.',
                '評論文やニュース解説など硬い書き言葉で用いられる累加表現です。'
            ),
        ],
    },
    104: {
        'formula': '名詞／動詞・形容詞普通形 ＋ <strong>といったらありはしない</strong> ／ <strong>といったらない</strong>',
        'similar': '〜といったらない / この上なく〜だ / 実に〜だ',
        'wrong': (
            '本日の会議の開始時刻は午後二時といったらありはしない。',
            '「〜といったらありはしない」は感情や状態の程度が極端（特にあきれるほどひどい・大変だ）であることを強調する表現であり、客観的な事実や時刻には使えません。',
            '"〜といったらありはしない" emphasizes an extreme degree of emotion or an exasperatingly bad condition, never an objective fact like a meeting time.'
        ),
        'comp': (
            '〜といったらない',
            'beyond description; utterly',
            '肯定的・否定的どちらの極端な程度（「美味しさといったらない」「悔しさといったらない」）にも使えますが、「〜といったらありはしない」は主にマイナスの呆れた状態に使われます。',
            'Can express both positive and negative extremes, whereas 〜といったらありはしない is predominantly used for negative, exasperating situations.',
            '山頂で飲んだ淹れたてのコーヒーの美味しさといったらなかった。',
        ),
        'quiz': [
            (
                '台風が過ぎ去った後の海岸の散らかりよう（　　　）、どこから手を付けていいか途方に暮れた。',
                'といったらありはしない',
                ['のも無理はない', 'に難くない', 'に値する'],
                'The mess on the beach after the typhoon passed was beyond description; we were at a loss as to where to even begin.',
                '「散らかりよう」「汚さ」「ひどさ」など、あきれるほど程度が甚だしいことを強調します。'
            ),
            (
                '繁忙期の経理部門の忙しさ（　　　）、昼食をとる時間さえ惜しんで伝票処理に追われている。',
                'といったらありはしない',
                ['てやまない', 'をおいてほかにない', 'んがためだ'],
                'The busyness of the accounting department during peak season is indescribable; they are pressed with processing slips, grudging even time for lunch.',
                '言葉で言い表せないほど極端な状態であることを感情を込めて述べる表現です。'
            ),
            (
                'せっかく予約した旅館の接客の悪さ（　　　）、二度と泊まりたくないと心底思った。',
                'といったらありはしない',
                ['てはならない', 'ばこそだ', 'のみか'],
                'The poor service at the inn we went to the trouble of booking was utterly appalling; I thought from the bottom of my heart that I never want to stay there again.',
                '話し手の強い不満や呆れの感情を表す文脈でよく用いられます。'
            ),
            (
                '引っ越し直後の部屋の乱雑さ（　　　）、段ボール箱の山で足の踏み場もない状態だ。',
                'といったらありはしない',
                ['に値する', 'てやまない', 'んとする'],
                'The clutter of the room right after moving in is beyond words; with mountains of cardboard boxes, there is nowhere even to step.',
                '名詞化した形容詞（「〜さ」）や「〜よう」につく形が特に自然です。'
            ),
        ],
    },
    105: {
        'formula': '感情・状態を表す名詞 ＋ <strong>の至り（だ）</strong>',
        'similar': '〜の極み / この上なく〜だ / 誠に〜だ',
        'wrong': (
            '昨日は夜遅くまでゲームをしてしまい、睡眠不足の至りだ。',
            '「〜の至り」は「光栄の至り」「赤面の至り」「若気の至り」「恐縮の至り」のように特定の漢語名詞と結びつく慣用性の高い表現であり、日常語の「睡眠不足」などにはつきません。',
            '"〜の至り" is a highly idiomatic, formal expression that pairs with specific Sino-Japanese emotion nouns (like 光栄, 恐縮, 赤面, 若気), not everyday words like lack of sleep.'
        ),
        'comp': (
            '〜の極み',
            'the height of; pinnacle of',
            '「贅沢の極み」「疲労の極み」「痛恨の極み」など、客観的な状態や苦痛の極限にも使われます。「〜の至り」は謙遜・感謝・恥じらいなど主観的な心情の極致によく使われます。',
            'Used for reaching the absolute limit of a state or pain (luxury, exhaustion, regret), whereas 〜の至り centers on subjective humility, gratitude, or embarrassment.',
            '日本庭園を眺めながら懐石料理を味わうとは、まさに贅沢の極みだ。',
        ),
        'quiz': [
            (
                '伝統ある本賞を賜りましたことは、私にとりまして誠に光栄（　　　）でございます。',
                'の至り',
                ['の拍子', 'の折', 'の境'],
                'Receiving this prestigious, time-honored award is truly the utmost honor for me.',
                '「光栄の至り」「感激の至り」「恐縮の至り」は受賞スピーチや礼状の定番表現です。'
            ),
            (
                '学生時代に無謀な冒険をして両親に心配をかけたのは、今思えば若気（　　　）だったと反省している。',
                'の至り',
                ['の前提', 'のよそ', 'の限り'],
                'Looking back now, I reflect that making reckless adventures in my student days and worrying my parents was the height of youthful folly.',
                '「若気の至り（わかげのいたり）」は若い頃の未熟さゆえの過ちを表す代表的な慣用句です。'
            ),
            (
                '専門家である皆様の前でこのような初歩的な誤りを犯してしまい、ただただ赤面（　　　）です。',
                'の至り',
                ['の拍子', 'の折', 'の前提'],
                'Having made such an elementary mistake in front of all of you experts, I am simply utterly ashamed.',
                '「赤面の至り」「汗顔の至り」は自分の失敗を深く恥じ入る硬い表現です。'
            ),
            (
                'ご多忙中にもかかわらず温かいお心遣いをいただき、恐縮（　　　）に存じます。',
                'の至り',
                ['の境', 'の拍子', 'のよそ'],
                'I feel utterly humbled and grateful to receive your warm consideration despite your busy schedule.',
                '手紙やビジネスメールで感謝と謙遜を丁重に伝える際に用いられます。'
            ),
        ],
    },
    106: {
        'formula': '２字漢語などの名詞 ＋ <strong>の極み（だ）</strong>',
        'similar': '〜の至り / 〜の極致 / この上ない〜',
        'wrong': (
            'この新しいカフェのケーキは甘さの極みで、コーヒーによく合う。',
            '「〜の極み」は「贅沢・疲労・痛恨・感激・無礼」など特定の抽象的漢語につく格調高い表現であり、「甘さの極み」のように日常の味覚形容詞の名詞化には通常使いません。',
            '"〜の極み" pairs with elevated abstract nouns (luxury, exhaustion, regret, rudeness), not everyday sensory nouns like "sweetness."'
        ),
        'comp': (
            '〜の至り',
            'the utmost; height of',
            '主に話し手自身の「光栄・恐縮・赤面」などの挨拶表現で使われます。「〜の極み」はプラス・マイナス両方の極限状態（「贅沢の極み」「疲労の極み」）を劇的に描写します。',
            'Mainly used in formal greetings of honor or humility, while 〜の極み dramatically depicts both positive and negative extremes of a condition.',
            '身に余るお褒めの言葉を頂戴し、恐縮の至りでございます。',
        ),
        'quiz': [
            (
                '連日の猛暑と長距離の移動が重なり、調査隊のメンバーは疲労（　　　）に達していた。',
                'の極み',
                ['の至り', 'の拍子', 'の折'],
                'With consecutive days of scorching heat combined with long-distance travel, the research team members had reached the peak of exhaustion.',
                '「疲労の極みに達する」で、疲れがこれ以上ない限界に達していることを表します。'
            ),
            (
                'あと一歩で優勝を逃してしまったことは、チーム全員にとってまさに痛恨（　　　）だった。',
                'の極み',
                ['の拍子', 'の前提', 'の境'],
                'Missing out on the championship by just one step was truly the height of bitter regret for the entire team.',
                '「痛恨の極み」「遺憾の極み」など、非常に強い悔しさや残念さを表す連語です。'
            ),
            (
                '厳選された旬の食材を貸し切りの空間で味わうとは、これ以上ない贅沢（　　　）と言えるだろう。',
                'の極み',
                ['の折', 'の拍子', 'のよそ'],
                'Savoring carefully selected seasonal ingredients in a private space can truly be called the pinnacle of luxury.',
                '「贅沢の極み」は最高度の豊かさや華やかさを表す代表的な慣用表現です。'
            ),
            (
                '恩人の親切を裏切るような彼の振る舞いは、礼儀を欠いた無礼（　　　）だと厳しく批判された。',
                'の極み',
                ['の至り', 'の折', 'の境'],
                'His behavior, which betrayed the kindness of his benefactor, was severely criticized as the height of rudeness lacking all manners.',
                '他者の行動に対する強い非難（「無礼の極み」「傲慢の極み」）にも使われます。'
            ),
        ],
    },
    107: {
        'formula': '最小単位の助数詞（一秒・一円・一人・一歩など）＋ <strong>たりとも〜ない</strong>',
        'similar': '〜すら〜ない / 〜さえ〜ない / 少しも〜ない',
        'wrong': (
            '今日は三時間たりとも勉強しなかったので、明日は頑張ろうと思う。',
            '「〜たりとも〜ない」は「一秒・一円・一滴・一人」など最小の「１」を表す単位について「ほんのわずかでも絶対に〜ない」と強調するため、「三時間」のような大きな数には使えません。',
            '"〜たりとも〜ない" attaches only to minimum single-unit counters (one second, one yen, one drop) to mean "not even a single ~," never larger numbers like three hours.'
        ),
        'comp': (
            '〜すら〜ない',
            'not even',
            '最小単位の数詞に限らず幅広い名詞について極端な例を挙げますが、「〜たりとも」は「１＋助数詞」に特化した格調高い表現です。',
            'Attaches to any noun to give an extreme example, whereas 〜たりとも is an elevated expression restricted to "1 + counter."',
            '忙しすぎて、昼食をとる時間すらなかった。',
        ),
        'quiz': [
            (
                '市民から預かった大切な予算は、たとえ一円（　　　）無駄にすることは許されない。',
                'たりとも',
                ['なりとも', 'ならでは', 'ともなると'],
                'Not even a single yen of the precious budget entrusted to us by the citizens is permitted to be wasted.',
                '「一円たりとも〜ない」で、最小の金額であっても一切無駄にしないという強い決意を表します。'
            ),
            (
                '最終審査の本番が近づき、出場者たちは一秒（　　　）惜しんで最後のリハーサルに打ち込んだ。',
                'たりとも',
                ['ばかりか', 'はおろか', 'にいたっては'],
                'As the final judging approached, the contestants devoted themselves to the final rehearsal, grudging even a single second.',
                '「一秒たりとも惜しむ（無駄にしない）」のように、わずかな時間も無駄にできない緊迫感を示します。'
            ),
            (
                '貴重な水資源を守るため、砂漠の緑化施設では水を一滴（　　　）漏らさない循環設備が導入されている。',
                'たりとも',
                ['ずくめ', 'まみれ', 'ごとき'],
                'To protect precious water resources, the desert greening facility has introduced a circulation system that does not leak even a single drop of water.',
                '「一滴たりとも漏らさない」は最小単位「一滴」を用いた代表的な強調表現です。'
            ),
            (
                '重要文化財が保管されている収蔵庫には、関係者以外は何人（　　　）立ち入ることができない。',
                'たりとも',
                ['ならでは', 'にとどまらず', 'をよそに'],
                'No one whatsoever other than authorized personnel is allowed to enter the repository where important cultural properties are stored.',
                '「何人（なんぴと）たりとも〜ない」は「誰一人として例外なく〜ない」という意味の硬い慣用表現です。'
            ),
        ],
    },
    108: {
        'formula': '名詞 ＋ <strong>をおいてほかに（は）ない</strong>',
        'similar': '〜をおいてない / 〜以外にない / 〜しかない',
        'wrong': (
            '週末に家族で行けるレストランは、駅前のイタリアンをおいてほかに三軒ある。',
            '「〜をおいてほかにない」は「唯一それだけだ」と断定する表現なので、「三軒ある」のような複数の存在を表す述語とは結びつきません。',
            '"〜をおいてほかにない" asserts that something is the sole option, so it cannot pair with predicates indicating multiple alternatives.'
        ),
        'comp': (
            '〜にほかならない',
            'nothing but; none other than',
            '「AはBにほかならない」の形で原因や本質を断定しますが、「Aをおいてほかにない」は「適任者・最適解はAだけだ」と選び出す表現です。',
            'Used as "A is nothing other than B" to define essence or cause, whereas 〜をおいてほかにない singles out A as the only suitable choice.',
            '今回の成功は、チーム全員の地道な努力の結果にほかならない。',
        ),
        'quiz': [
            (
                '百年の歴史を持つ老舗旅館の再建を託せる人物は、現場を知り尽くした彼（　　　）。',
                'をおいてほかにない',
                ['といったらありはしない', 'ないではいられない', 'としたところでだ'],
                'There is no one other than him, who knows the workplace inside and out, to whom we can entrust the rebuilding of the century-old inn.',
                '「彼をおいてほかにない」で、彼以外にふさわしい人物は絶対にいないと強く断定します。'
            ),
            (
                '生態系を守りながら地域経済を活性化させる道は、持続可能な自然観光の推進（　　　）。',
                'をおいてほかにない',
                ['てはかなわない', 'ようものならだ', 'に難くない'],
                'The path to revitalizing the local economy while protecting the ecosystem lies in none other than promoting sustainable eco-tourism.',
                '解決策や方針が唯一それだけであることを格調高く主張する文末表現です。'
            ),
            (
                'これほど緻密な木彫りの装飾を再現できる職人は、現代においては山本名人の右に出る者（　　　）と言われるほど、名人をおいてほかにない。',
                'をおいてほかにない',
                ['てはたまらない', 'ないことにはならない', 'からといってだ'],
                'When it comes to an artisan who can reproduce such intricate wood-carved ornaments, there is truly no one today other than Master Yamamoto.',
                '唯一無二の技術や才能を持つ人物を称える際によく用いられます。'
            ),
            (
                '抜本的な業務改革に踏み切るタイミングは、新システムへの移行が完了した今（　　　）。',
                'をおいてほかにない',
                ['のも無理はない', 'に値しない', 'てやまない'],
                'The timing to embark on fundamental business reform is none other than right now, when the transition to the new system has been completed.',
                '「今をおいてほかにない」は絶好の機会が今しかないことを強調する定型表現です。'
            ),
        ],
    },
    109: {
        'formula': '名詞 ／ 動詞辞書形 ＋ <strong>に値する</strong>',
        'similar': '〜だけの価値がある / 〜に足る / 〜にふさわしい',
        'wrong': (
            'このコンビニのお弁当は五百円に値するので、よく買っています。',
            '「〜に値する」は「称賛・注目・検討・尊敬」など抽象的な高い価値があることを表す表現であり、具体的な金額（五百円）には使えません。',
            '"〜に値する" means "worthy of (praise, attention, consideration)," not a literal monetary price like 500 yen.'
        ),
        'comp': (
            '〜に足る',
            'worthy of; sufficient to',
            '「信頼に足る」「取るに足らない」など限られた慣用表現で使われるさらに硬い文語的表現です。',
            'An even more literary expression mostly seen in fixed phrases like "trustworthy" (信頼に足る) or "trivial" (取るに足らない).',
            '彼はどんな困難な局面でも冷静さを失わない、信頼に足る人物だ。',
        ),
        'quiz': [
            (
                '長年の実験の末に希少疾患の治療法を確立した研究チームの功績は、最高の称賛（　　　）。',
                'に値する',
                ['に難くない', 'にあってだ', 'にとどまる'],
                'The achievement of the research team that established a treatment for a rare disease after years of experiments is worthy of the highest praise.',
                '「称賛に値する」「尊敬に値する」「注目に値する」は頻出のコロケーションです。'
            ),
            (
                '若手社員が提案した資源循環型のパッケージ設計は、実現可能性が高く十分に検討する（　　　）アイデアだ。',
                'に値する',
                ['にいたる', 'にかかわる', 'に先駆ける'],
                'The resource-circulating package design proposed by the young employee has high feasibility and is an idea well worth examining.',
                '動詞辞書形＋「に値する」の形で、その行為をするだけの高い価値があることを示します。'
            ),
            (
                '世界中の天文学者が長年謎としてきた現象を解明した今回の論文は、まさに驚嘆（　　　）発見と言える。',
                'に値する',
                ['にまつわる', 'にひきかえ', 'に即した'],
                'This paper, which elucidated a phenomenon that astronomers around the world had considered a mystery for years, can truly be called a discovery worthy of wonder.',
                '「驚嘆に値する」「特筆に値する」のように評価を表す漢語名詞とよく結びつきます。'
            ),
            (
                '根拠のないうわさ話など一顧だにしない彼の毅然とした態度は、リーダーとして大いに尊敬（　　　）。',
                'に値する',
                ['に相違ない', 'にしのびない', 'にきまっている'],
                'His resolute attitude of not paying the slightest heed to groundless rumors is greatly worthy of respect as a leader.',
                '人物の立派な行動や姿勢を高く評価する文脈で用いられます。'
            ),
        ],
    },
    110: {
        'formula': '名詞（想像・察知・理解など）／ 動詞辞書形 ＋ <strong>に難くない</strong>',
        'similar': '容易に〜できる / 〜は難しくない / 簡単に〜できる',
        'wrong': (
            'この数学の応用問題は定理を使えば解くに難くない。',
            '「〜に難くない」は「想像する・察する・理解する」など心情や状況を推察する動詞・名詞に限定して使われ、「問題を解く」「料理を作る」のような具体動作には使えません。',
            '"〜に難くない" is restricted to verbs/nouns of mental inference or empathy (imagine, surmise, understand), not concrete actions like solving a math problem.'
        ),
        'comp': (
            '〜にしのびない',
            'cannot bear to',
            '形態は似ていますが、「見るにしのびない」のように同情や良心の痛みで我慢できないという意味を表します。',
            'Looks similar in structure, but means being unable to bear doing something out of sympathy or pangs of conscience.',
            '長年愛用した楽器を手放す彼の寂しそうな姿は、見るにしのびなかった。',
        ),
        'quiz': [
            (
                '丹精込めて育てた果樹園が台風で被害を受け、農家の人々がどれほど落胆しているかは想像（　　　）。',
                'に難くない',
                ['に値する', 'にしのびない', 'にいたらない'],
                'It is not hard to imagine how disheartened the farmers must be after the orchard they raised with such care was damaged by the typhoon.',
                '「想像に難くない」は相手の心情や事態を容易に推し量ることができるという最重要慣用表現です。'
            ),
            (
                '慣れない海外赴任先でひとり奮闘していた当時の彼の苦労は、残された業務日誌からも察する（　　　）。',
                'に難くない',
                ['に値しない', 'にきまっている', 'にすぎない'],
                'It is not hard to surmise from the remaining work logs the hardships he faced while struggling alone at an unfamiliar overseas post.',
                '「察するに難くない」「推察するに難くない」の形で書き言葉で多用されます。'
            ),
            (
                '十分な事前説明もないまま計画が変更されれば、住民から反発の声が上がるのは予想する（　　　）ことだ。',
                'に難くない',
                ['にほかならない', 'に先駆ける', 'にかかわる'],
                'If the plan is changed without sufficient prior explanation, it is not hard to foresee that voices of opposition will rise from the residents.',
                '当然予測できる帰結であることを客観的に述べる際にも使われます。'
            ),
            (
                '創業以来の看板製品を手放す経営陣の苦渋の決断は、同業者として理解する（　　　）。',
                'に難くない',
                ['に相違ない', 'にとどまる', 'にまつわる'],
                'As someone in the same industry, it is not difficult to understand the agonizing decision of the management team to let go of their flagship product since the company\'s founding.',
                '他者の立場や苦衷に共感を示す格調高い表現です。'
            ),
        ],
    },
    111: {
        'formula': '動詞・形容詞て形 ＋ <strong>はかなわない</strong>',
        'similar': '〜てはたまらない / 〜たらやりきれない / 我慢できない',
        'wrong': (
            '宝くじで一等が当たってはかなわないので、家族みんなで旅行に行きたい。',
            '「〜てはかなわない」は「そんな状態が続いたら我慢できない・ひどく困る」というマイナスの事態に使うため、嬉しい出来事には使えません。',
            '"〜てはかなわない" expresses exasperation at an unbearable negative situation, so it cannot be used for happy events.'
        ),
        'comp': (
            '〜てはたまらない',
            'unbearably; cannot stand',
            'ほぼ同義で置き換え可能ですが、「〜てはかなわない」は「これではこちらが対処しきれない・参ってしまう」という困惑のニュアンスがより強く出ます。',
            'Nearly interchangeable, though 〜てはかなわない carries a stronger nuance of "I cannot cope with this / it is too much to handle."',
            'こう毎日蒸し暑くてはかなわないから、早めにエアコンの点検を頼もう。',
        ),
        'quiz': [
            (
                '取引先からこう毎日のように仕様変更を要求され（　　　）と、開発現場から悲鳴が上がっている。',
                'てはかなわない',
                ['てやまない', 'てからというもの', 'てはならない'],
                'With the client demanding specification changes almost every single day like this, the development team is crying out that they cannot stand it.',
                '他者の行動や状況によって自分が振り回され、「とても我慢できない」と嘆く表現です。'
            ),
            (
                '梅雨入りしてからというもの、こう来る{日|ひ}も来る{日|ひ}も雨ばかり降っ（　　　）ね。',
                'てはかなわない',
                ['てやまない', 'てはならない', 'てたまらない'],
                'Ever since the rainy season started, we really can\'t stand it raining day after day like this.',
                '天候の不順や暑さ・寒さが続くことへのぼやきとして「こう〜てはかなわない」がよく使われます。'
            ),
            (
                '会議のたびに方針が二転三転し（　　　）から、まずは基本計画を文書で確定させてほしい。',
                'てはかなわない',
                ['てやまない', 'てからというもの', 'てはならない'],
                'We can\'t cope if the policy keeps flip-flopping at every meeting, so please finalize the basic plan in writing first.',
                '「〜てはかなわないから」の形で、改善を求める理由として述べる用法です。'
            ),
            (
                'せっかく植えた野菜の苗をイノシシに次々と荒らされ（　　　）ので、畑の周囲に防護柵を設置した。',
                'てはかなわない',
                ['てやまない', 'てはならない', 'てからというもの'],
                'Since we couldn\'t bear having the vegetable seedlings we planted ravaged one after another by wild boars, we installed a protective fence around the field.',
                '受身形＋「てはかなわない」で、被害が続くことに耐えかねる心情を表します。'
            ),
        ],
    },
    112: {
        'formula': '動詞・形容詞て形 ＋ <strong>はたまらない</strong> ／ <strong>てたまらない</strong>',
        'similar': '〜てしかたがない / 〜てしょうがない / 〜てはかなわない',
        'wrong': (
            '明日は午前九時に出社してたまらない予定です。',
            '「〜てたまらない」は抑えきれない強い感情・感覚、「〜てはたまらない」は困った事態への我慢できなさを表すため、単なる予定には使えません。',
            'Used for irrepressible emotions/sensations or unbearable trouble, never for a neutral schedule.'
        ),
        'comp': (
            '〜てしかたがない',
            'cannot help feeling; extremely',
            'ほぼ同義ですが、「〜てたまらない」の方が感情や肉体的感覚（嬉しい・懐かしい・痛い・痒い）の突き上げるような強さが際立ちます。',
            'Very close in meaning, though 〜てたまらない emphasizes a more intense, surging physical sensation or emotion.',
            '故郷を離れて十年になり、母の手料理が恋しくてしかたがない。',
        ),
        'quiz': [
            (
                '繁忙期にベテラン社員にまで休まれ（　　　）から、シフトの無理がないよう早めに調整しよう。',
                'てはたまらない',
                ['てやまない', 'てからというもの', 'てはならない'],
                'It would be unbearable if even our veteran staff took time off during the busy season, so let\'s adjust the shifts early to avoid overwork.',
                '「〜てはたまらない」は「もしそんなことになったら大変で我慢できない」という危惧・困惑を表します。'
            ),
            (
                '三年ぶりに再会した恩師が私の研究を温かく褒めてくださり、嬉しく（　　　）。',
                'てたまらなかった',
                ['てはならなかった', 'てやまなかった', 'てからというものだった'],
                'My former mentor, whom I met again for the first time in three years, warmly praised my research, and I was unbearably happy.',
                '「〜てたまらない」は感情・感覚形容詞について「非常に〜だ」と強調します。'
            ),
            (
                '大事なプレゼンの最中にプロジェクターが故障し（　　　）と思い、予備の機材も準備しておいた。',
                'てはたまらない',
                ['てやまない', 'てはならない', 'てからというもの'],
                'Thinking it would be unbearable if the projector broke down in the middle of the important presentation, I prepared backup equipment as well.',
                '最悪の事態を想定して予防策をとる文脈で「〜てはたまらないと思い」がよく使われます。'
            ),
            (
                '徹夜で仕上げた設計図のデータが消え（　　　）ので、クラウドと外付けハードディスクの両方に保存した。',
                'てはたまらない',
                ['てやまない', 'てからというもの', 'てはならない'],
                'Because I couldn\'t stand it if the blueprint data I stayed up all night finishing were lost, I saved it to both the cloud and an external hard drive.',
                '取り返しのつかない事態を避けたいという強い気持ちを示します。'
            ),
        ],
    },
    113: {
        'formula': '動詞て形 ＋ <strong>はならない</strong>',
        'similar': '〜てはいけない / 決して〜べきではない / 〜べからず',
        'wrong': (
            '今夜は雨が降りそうだから、洗濯物を外に干してはならないよ。',
            '「〜てはならない」は道徳・法律・社会的使命など重大な規範に基づく禁止を表す書き言葉であり、家庭内のちょっとした注意には重すぎて不自然です。',
            '"〜てはならない" expresses strict prohibition based on moral, legal, or social duty, making it too weighty for casual household reminders.'
        ),
        'comp': (
            '〜てはいけない',
            'must not; may not',
            '日常会話から規則まで幅広く使える一般的な禁止表現です。「〜てはならない」はより客観的・公的な義務や戒めに使われます。',
            'General prohibition usable in everyday speech, whereas 〜てはならない is reserved for objective, public, or ethical imperatives.',
            '展示室の中ではフラッシュを使って写真を撮ってはいけません。',
        ),
        'quiz': [
            (
                '医療従事者たるもの、診察を通じて知り得た患者の個人情報を外部に漏らし（　　　）。',
                'てはならない',
                ['てはかなわない', 'てやまない', 'てたまらない'],
                'Those in the medical profession must never leak patients\' personal information learned through consultations to the outside.',
                '職業倫理や法律上の守秘義務など、絶対的な禁止・戒めを表します。'
            ),
            (
                'どれほど技術が進歩しようとも、自然環境への敬意と謙虚さを忘れ（　　　）と多くの科学者が警鐘を鳴らしている。',
                'てはならない',
                ['てはかなわない', 'てからというもの', 'てたまらない'],
                'Many scientists are sounding the alarm that no matter how much technology advances, we must never forget respect and humility toward the natural environment.',
                '社会全体が守るべき普遍的な規範や教訓を述べる文脈にふさわしい表現です。'
            ),
            (
                '過去の災害の教訓を風化させ（　　　）という思いから、毎年地域で防災訓練が実施されている。',
                'てはならない',
                ['てやまない', 'てはたまらない', 'てからというもの'],
                'Out of the conviction that the lessons of past disasters must never be allowed to fade, disaster prevention drills are held in the community every year.',
                '「〜てはならないという思い／決意」の形で強い使命感を表します。'
            ),
            (
                '公正であるべき審査において、審査員の個人的な好みが採点に影響を及ぼし（　　　）のは当然のことだ。',
                'てはならない',
                ['てやまない', 'てはかなわない', 'てたまらない'],
                'In a judging process that must be fair, it is only natural that the judges\' personal preferences must never influence the scoring.',
                '公正さや規律を守るための厳格なルールを示す際に用いられます。'
            ),
        ],
    },
    114: {
        'formula': '動詞ない形 ＋ <strong>ではいられない</strong>',
        'similar': '〜ずにはいられない / 〜ないわけにはいかない / 思わず〜してしまう',
        'wrong': (
            '毎日健康のために野菜を食べないではいられないようにしている。',
            '「〜ないではいられない」は感情や生理的欲求が自然に湧き上がって抑えられないことを表すため、「〜ようにしている」のような意識的な習慣づけとは矛盾します。',
            '"〜ないではいられない" describes an irresistible, spontaneous urge, so it contradicts conscious habit-forming like "I try to."'
        ),
        'comp': (
            '〜ないわけにはいかない',
            'have no choice but to (out of duty)',
            '社会的義務や周囲の事情から「しなければならない」と理性的に判断する場合に使われます。「〜ないではいられない」は内発的な衝動です。',
            'Expresses rational obligation due to social duty or circumstances, whereas 〜ないではいられない is an internal emotional impulse.',
            '責任者として、今回のトラブルについて説明しないわけにはいかない。',
        ),
        'quiz': [
            (
                '逆境の中でも笑顔を絶やさず懸命に努力する彼女の姿を見ると、応援し（　　　）。',
                'ないではいられない',
                ['ないことにはならない', 'ないものでもない', 'ないとも限らない'],
                'When I see her working so hard without ever losing her smile even in adversity, I cannot help cheering for her.',
                '「応援しないではいられない」で、心が動かされて自然にそうしたくなる気持ちを表します。'
            ),
            (
                '恩師が長年の研究をまとめた遺稿集を読み返すたびに、感謝の念を抱か（　　　）。',
                'ないではいられない',
                ['ないことにはならない', 'ないどころではない', 'ないまでも'],
                'Every time I reread the posthumous collection compiling my mentor\'s years of research, I cannot help feeling a deep sense of gratitude.',
                '内面から自然に湧き上がる感情を抑えられないことを示す表現です。'
            ),
            (
                'あまりにユーモラスな彼の語り口に、厳粛な会場の聴衆も思わず笑わ（　　　）。',
                'ないではいられなかった',
                ['ないことにはならなかった', 'ないはずがなかった', 'ないわけではなかった'],
                'At his utterly humorous way of speaking, even the audience in the solemn hall could not help laughing involuntarily.',
                '生理現象や笑いをこらえきれない場面でもよく使われます。'
            ),
            (
                '自分の作品が本当に世の中に受け入れられるのか、発表の前夜は不安を感じ（　　　）。',
                'ないではいられなかった',
                ['ないことにはならなかった', 'ないものでもなかった', 'ないまでもなかった'],
                'On the eve of the release, I could not help feeling anxious about whether my work would truly be accepted by the world.',
                '頭では考えまいとしても自然に不安や疑問が湧いてしまう心理を描写します。'
            ),
        ],
    },
    115: {
        'formula': '動詞ない形（ナイを除いた形）＋ <strong>ずにはいられない</strong>（※する → せずにはいられない）',
        'similar': '〜ないではいられない / 思わず〜してしまう / 〜を禁じ得ない',
        'wrong': (
            '来週の出張のために、今日中に新幹線の切符を予約せずにはいられない。',
            '「〜ずにはいられない」は感情の衝動でどうしてもそうしてしまう場合に使うため、単なる事務手続きの必要性を述べる文脈には不自然です。',
            '"〜ずにはいられない" is driven by emotional compulsion, making it unnatural for routine administrative tasks like booking a ticket.'
        ),
        'comp': (
            '〜を禁じ得ない',
            'cannot suppress (emotion)',
            '「同情・涙・驚き・憤りを禁じ得ない」のように感情名詞を直接目的語にとる書き言葉です。「〜ずにはいられない」は動詞につきます。',
            'Takes emotion nouns directly as objects in formal writing, whereas 〜ずにはいられない attaches to verbs.',
            '被災地の復興に向けた住民たちの団結力には、感銘を禁じ得ない。',
        ),
        'quiz': [
            (
                ' শত年の時を超えて鮮やかに蘇った壁画の美しさを前にして、訪れた人々は感嘆のため息をもらさ（　　　）。'.replace(' শত年の', '百年の'),
                'ずにはいられなかった',
                ['ないことにはならなかった', 'ざるを得ないことだった', 'べくもなかった'],
                'Standing before the beauty of the mural that vividly came back to life across a hundred years of time, visitors could not help letting out sighs of admiration.',
                '感動のあまり自然にため息が出る様子を「もらさずにはいられない」と表現しています。'
            ),
            (
                '理不尽な扱いを受けている後輩を見たら、性格上、黙って見過ごさずにはおれず一言口を出さ（　　　）。',
                'ずにはいられない',
                ['ないことにはならない', 'べくもない', 'んばかりだ'],
                'Given my personality, when I see a junior colleague being treated unreasonably, I cannot just look the other way in silence and cannot resist speaking up.',
                '自分の性分や正義感から、どうしても行動に出てしまうことを表します。'
            ),
            (
                '故郷の懐かしい風景を描いたその絵画を見ると、幼い頃に祖父母と過ごした夏休みを思い出さ（　　　）。',
                'ずにはいられない',
                ['ないことにはならない', 'べくもない', 'ようものならだ'],
                'Whenever I look at that painting depicting the nostalgic scenery of my hometown, I cannot help remembering the summer vacations I spent with my grandparents as a child.',
                '記憶や感情が自然に呼び起こされる典型的な文脈です。'
            ),
            (
                '細部まで一切の妥協を許さない巨匠の仕事ぶりには、同じ職人として敬意を表さ（　　　）。',
                'ずにはいられない',
                ['ないことにはならない', 'べくもない', 'んがためだ'],
                'As a fellow craftsperson, I cannot help expressing my respect for the master\'s way of working, which allows no compromise down to the finest detail.',
                'サ変動詞「表する」は「表せずにはいられない」または五段化「表さずにはいられない」の形をとります。'
            ),
        ],
    },
    116: {
        'formula': '動詞ない形（ナイを除いた形）＋ <strong>ざるを得ない</strong>（※する → せざるを得ない）',
        'similar': '〜ないわけにはいかない / やむを得ず〜する / 〜ほかない',
        'wrong': (
            '今日は天気がとても良くて気持ちがいいので、公園を散歩せざるを得ない。',
            '「〜ざるを得ない」は「本当はしたくないが、事情があって仕方なく〜する」という消極的・不可避な状況に使うため、楽しい自発的な行動には使えません。',
            '"〜ざるを得ない" implies reluctance under unavoidable circumstances, so it cannot be used for pleasant voluntary activities.'
        ),
        'comp': (
            '〜ほかない',
            'have no other choice but to',
            '「他に方法がないからそれを選ぶ」という手段の限定に焦点があり、「〜ざるを得ない」ほど心理的な抵抗感や不本意さは強くありません。',
            'Focuses on the lack of alternative methods, with less emphasis on psychological reluctance than 〜ざるを得ない.',
            'バスが終了してしまった以上、駅まで歩いて帰るほかない。',
        ),
        'quiz': [
            (
                '主要部品の供給が世界的に滞っているため、来月予定していた新製品の発売時期を延期（　　　）。',
                'せざるを得ない',
                ['せずにはいられない', 'するに難くない', 'するに値する'],
                'Because the supply of key components is stagnating globally, we have no choice but to postpone the release date of the new product scheduled for next month.',
                '「する → せざるを得ない」の接続はN1文法の最頻出ポイントです。'
            ),
            (
                'これだけ明確な実験データが揃っている以上、従来の仮説には誤りがあったと認め（　　　）だろう。',
                'ざるを得ない',
                ['ずにはいられない', 'ないことにはならない', 'べくもない'],
                'Given that such clear experimental data has been assembled, we will have no choice but to admit that there was an error in the conventional hypothesis.',
                '客観的な証拠や論理によって、不本意ながら結論を受け入れる文脈です。'
            ),
            (
                '老朽化による安全上のリスクが指摘されたからには、歴史ある市民会館といえども取り壊しを検討（　　　）。',
                'せざるを得ない',
                ['せずにはいられない', 'するにしのびない', 'するに値する'],
                'Now that safety risks due to aging have been pointed out, we have no choice but to consider demolition, even for the historic civic hall.',
                '惜しい気持ちはあっても、安全上やむを得ず決断する状況を表します。'
            ),
            (
                '台風による暴風警報が発令されたため、主催者は野外音楽祭の中止を決定（　　　）状況に追い込まれた。',
                'せざるを得ない',
                ['せずにはいられない', 'するに難くない', 'するに足る'],
                'Because a storm warning due to the typhoon was issued, the organizers were driven into a situation where they had no choice but to decide to cancel the outdoor music festival.',
                '連体修飾「〜せざるを得ない状況／立場」の形でも頻繁に用いられます。'
            ),
        ],
    },
    117: {
        'formula': '動詞意向形（う・よう）＋ <strong>ものなら</strong>',
        'similar': 'もし万が一〜たら大変だ / 〜たら最後',
        'wrong': (
            '毎日こつこつ練習しようものなら、きっとピアノが上手に弾けるようになるよ。',
            '「〜ようものなら」は「万が一そんなことをしたら、大変な悪い結果になる」という強い警告・危惧を表すため、望ましい結果には使えません。',
            '"〜ようものなら" warns of a dire negative consequence if something happens, so it cannot lead to a positive outcome.'
        ),
        'comp': (
            '〜たら最後',
            'once ~ happens, it is all over',
            'どちらも悪い結果の必然性を表しますが、「〜ようものなら」は「そんなことは滅多にしないが、仮に少しでもしたら大変だ」という仮定性が強いです。',
            'Both lead to bad outcomes, but 〜ようものなら emphasizes a hypothetical warning ("if you were ever to make even a slight slip").',
            'あの頑固な職人は、一度へそを曲げたら最後、誰の言うことも聞かない。',
        ),
        'quiz': [
            (
                '厳しい師匠の稽古中に一瞬でも気を抜こ（　　　）、たちまち鋭い叱責が飛んでくる。',
                'うものなら',
                ['うとしている', 'うにも〜ない', 'うがまいが'],
                'If you were ever to let your guard down even for a moment during the strict master\'s training, a sharp reprimand would immediately fly at you.',
                '五段動詞の意向形（抜こう）＋「ものなら」で、少しの油断も許されない緊張感を表します。'
            ),
            (
                'これほど繊細なガラス工芸品は、運搬中に少しの衝撃でも与え（　　　）、粉々に砕けてしまうだろう。',
                'ようものなら',
                ['ようとするなら', 'ようではないか', 'ようとまいと'],
                'With glass craftwork this delicate, if you were ever to subject it to even a slight shock during transport, it would likely shatter into pieces.',
                '万が一のミスが重大な結果を招くことを警告する表現です。'
            ),
            (
                '年末の繁忙期に基幹システムが止まろ（　　　）、全国の店舗の業務が大混乱に陥ってしまう。',
                'うものなら',
                ['うとしている', 'うがまいが', 'うにも〜ない'],
                'If the core system were ever to stop during the year-end busy season, operations at stores nationwide would fall into utter chaos.',
                '無生物主語（システムが止まる・雨が降る）の万が一の事態にも使えます。'
            ),
            (
                'うちの猫は警戒心が強く、見知らぬ人が急に近づこ（　　　）、すぐに家具の奥へ隠れて出てこない。',
                'うものなら',
                ['うとするなら', 'うではないか', 'うにも〜ない'],
                'Our cat is very wary, and if a stranger were ever to approach suddenly, it would immediately hide deep behind the furniture and not come out.',
                '相手の習性や気質から、特定の行動をとると即座に激しい反応が返ってくることを表します。'
            ),
        ],
    },
    118: {
        'formula': '動詞・形容詞ば形（名詞／ナ形容詞＋であれ）＋ <strong>ばこそ</strong>',
        'similar': '〜からこそ / 〜ゆえに / まさに〜だから',
        'wrong': (
            '今日は雨が降ればこそ、明日の遠足が楽しみだ。',
            '「AばこそB」は「ほかでもないAという特別な理由があるからこそBなのだ」と因果関係を強く強調するため、因果関係のない文には使えません。',
            '"AばこそB" strongly emphasizes that B happens precisely because of reason A, so A and B must have a clear causal link.'
        ),
        'comp': (
            '〜からこそ',
            'precisely because',
            '意味は同じですが、「〜ばこそ」は文語的・格調高い表現で、愛情・信頼・期待など心情的な理由を強調する際によく好まれます。',
            'Same meaning, but 〜ばこそ is more literary and elevated, especially favored when emphasizing heartfelt reasons like love, trust, or expectation.',
            '失敗の悔しさを知っているからこそ、彼は誰よりも努力を続けている。',
        ),
        'quiz': [
            (
                '子どもの将来を真剣に思え（　　　）、時には厳しい言葉で自立を促すことも親の務めだ。',
                'ばこそ',
                ['ばそれまでだ', 'ばきりがない', 'ばいいというものだ'],
                'Precisely because parents seriously care about their children\'s future, it is sometimes their duty to encourage independence with firm words.',
                '「思えばこそ」「愛すればこそ」は、厳しさの裏にある深い愛情を説明する定番の表現です。'
            ),
            (
                '君の実力と誠実さを高く評価していれ（　　　）、この重要な新規プロジェクトのリーダーを任せたのだ。',
                'ばこそ',
                ['ばそれまでだ', 'ようものなら', 'たところで'],
                'It is precisely because I highly value your ability and sincerity that I entrusted you with leading this important new project.',
                '相手への信頼や期待が理由であることを強調して伝える文脈です。'
            ),
            (
                '地域の皆様の温かいご支援があれ（　　　）、当劇団は創立五十周年を迎えることができました。',
                'ばこそ',
                ['ばそれまでだ', 'ようものなら', 'ないことには'],
                'It is precisely because we had the warm support of everyone in the community that our theater troupe was able to celebrate its 50th anniversary.',
                '感謝のスピーチや挨拶で「皆様のご支援があればこそ」は非常に格調高く響きます。'
            ),
            (
                '伝統の味を守り抜きたいと願え（　　　）、店主は手間のかかる昔ながらの製法を今も変えない。',
                'ばこそ',
                ['ようものなら', 'たところで', 'ばきりがない'],
                'Precisely because he wishes to preserve the traditional flavor to the end, the shop owner still does not change the time-consuming, old-fashioned production method.',
                '一見不合理に見えるこだわりの背後にある強い信念を浮き彫りにします。'
            ),
        ],
    },
    119: {
        'formula': '名詞 ＋ <strong>なくしては</strong>（〜ない）',
        'similar': '〜なしには〜ない / 〜がなければ〜ない / 〜抜きには〜ない',
        'wrong': (
            '明日は傘なくしては晴れるでしょう。',
            '「AなくしてはBない」は「Aという不可欠な要素がなければBは成立しない」という構造をとるため、肯定の予測文には使えません。',
            '"AなくしてはBない" means "without essential element A, B cannot be achieved," requiring a negative or rhetorical predicate.'
        ),
        'comp': (
            '〜なしに（は）',
            'without',
            '「断りなしに」「予告なしに」のように付帯状況（〜しないで）にも使えますが、「〜なくしては」は「〜が存在しなければ不可能だ」という必須条件に特化しています。',
            'Can also mean "without doing," whereas 〜なくしては specifically emphasizes an indispensable precondition.',
            '基礎体力の向上なくしては、後半戦を勝ち抜くことはできない。',
        ),
        'quiz': [
            (
                '現場スタッフ一人ひとりの献身的な協力（　　　）、この大規模な国際会議の成功はあり得なかった。',
                'なくしては',
                ['にいたっては', 'にかまけては', 'にとどまらず'],
                'Without the dedicated cooperation of each and every on-site staff member, the success of this large-scale international conference would have been impossible.',
                '「Aなくしては〜あり得ない／不可能だ」で、Aが不可欠な土台であることを強調します。'
            ),
            (
                '基礎科学への地道で長期的な投資（　　　）、次世代を担う革新的な技術は{生|う}まれないだろう。',
                'なくしては',
                ['をおいては', 'をよそには', 'にかこつけては'],
                'Without steady, long-term investment in basic science, innovative technologies to lead the next generation will likely not be born.',
                '論説文で必須条件を提示する際によく使われる格調高い表現です。'
            ),
            (
                '異なる文化的背景を持つ人々との相互理解（　　　）、真に豊かな共生社会を築くことはできない。',
                'なくしては',
                ['にひきかえ', 'に即しては', 'を皮切りに'],
                'Without mutual understanding among people with different cultural backgrounds, we cannot build a truly rich, harmonious society.',
                '抽象的な理念や信頼関係が不可欠であることを訴える文脈に最適です。'
            ),
            (
                '歴史的建造物の保存は、そこに暮らす地域住民の理解と誇り（　　　）到底成り立たない事業である。',
                'なくしては',
                ['はおろか', 'ならでは', 'ともなると'],
                'The preservation of historical buildings is an undertaking that simply cannot stand without the understanding and pride of the local residents living there.',
                '「〜なくして（は）成り立たない」は定番のコロケーションです。'
            ),
        ],
    },
    120: {
        'formula': '動詞・形容詞ない形（ナイを除いた形）＋ <strong>ないことには</strong>（〜ない）',
        'similar': '〜なければ〜ない / まず〜しない限り〜ない',
        'wrong': (
            '新しい靴を履いてみないことには、サイズがぴったりだったので買いました。',
            '「AないことにはBない」は「まずAという前提条件が満たされなければ、Bすることもできない」と後件に否定表現を伴うため、過去の確定事実には使えません。',
            '"AないことにはBない" states a prerequisite ("unless A happens first, B cannot happen") and requires a negative predicate in B.'
        ),
        'comp': (
            '〜ない限り',
            'unless; as long as ~ not',
            '客観的な条件全般に使えますが、「〜ないことには」は「とにかくまずそれをやってみなければ話が始まらない」という実務的・体験的なニュアンスが強いです。',
            'General conditional "unless," whereas 〜ないことには emphasizes "until we at least do A first, we can\'t even take the next step."',
            '実際に現地へ足を運んでみないことには、立地の良し悪しは判断できない。',
        ),
        'quiz': [
            (
                '写真やカタログを見るだけでは分からないから、実物を手に取って確かめ（　　　）購入は決められない。',
                'ないことには',
                ['ないではいられない', 'ないものでもない', 'ないとも限らない'],
                'Since you can\'t tell just by looking at photos or catalogs, I can\'t decide on the purchase unless I hold and check the actual item first.',
                '「まず〜してみないことには、判断できない」という最頻出のパターンです。'
            ),
            (
                '原因となっている初期不良の箇所を特定し（　　　）、具体的な修理の見積もりを出すことはできません。',
                'ないことには',
                ['ないではいられない', 'ないはずがない', 'ないわけでもない'],
                'Unless we first identify the defective part causing the issue, we cannot provide a concrete repair estimate.',
                'ビジネスや技術対応で「前段階が完了しないと次に進めない」ことを丁寧に説明する表現です。'
            ),
            (
                'どれほど優れた企画書であっても、予算の承認が下り（　　　）、プロジェクトを始動させるわけにはいかない。',
                'ないことには',
                ['ないではいられない', 'ないまでも', 'ないどころではない'],
                'No matter how excellent the proposal is, unless the budget approval comes through first, we cannot launch the project.',
                '必須の前提条件がまだ満たされていない状況でよく用いられます。'
            ),
            (
                '朝の渋滞状況は{日|ひ}によって変わるため、実際に家を出て走ってみ（　　　）到着時刻は読めないよ。',
                'ないことには',
                ['ないではいられない', 'ないものでもない', 'ないにはあたらない'],
                'Because morning traffic conditions change from day to day, you can\'t predict the arrival time unless you actually leave the house and drive.',
                '日常会話から実務まで幅広く使われる条件表現です。'
            ),
        ],
    },
    121: {
        'formula': '動詞・形容詞普通形 ／ 名詞 ＋ <strong>としたところで</strong>',
        'similar': '〜たところで / たとえ〜としても / 〜にしたところで',
        'wrong': (
            '今からタクシーに乗ったとしたところで、開演時間に十分間に合ってよかった。',
            '「〜としたところで」は「たとえそう仮定してみたところで、結局役に立たない・無理だ」という消極的な判断が後ろに来るため、肯定的な結果には使えません。',
            '"〜としたところで" introduces a hypothetical assumption followed by a futile or negative conclusion, never a successful past result.'
        ),
        'comp': (
            '〜たところで',
            'even if one were to do',
            '動詞た形に直接ついて「いくら〜しても無駄だ」と述べます。「〜としたところで」は名詞や普通形にもつき、「仮にそうだと仮定しても」と推論の段階を明示します。',
            'Attaches directly to past-form verbs, whereas 〜としたところで can follow nouns or plain forms to explicitly frame a hypothetical assumption.',
            '今さら急いだところで、最終電車にはもう間に合わないだろう。',
        ),
        'quiz': [
            (
                '仮に今から追加の人員を投入した（　　　）、明日の朝までにすべての在庫を点検し終えるのは不可能に近い。',
                'としたところで',
                ['とあっては', 'とばかりに', 'と相まって'],
                'Even if we were to bring in additional personnel starting now, it would be nearly impossible to finish inspecting all the inventory by tomorrow morning.',
                '「仮に〜としたところで、結局無理だ／大差ない」の形で仮定の無力さを示します。'
            ),
            (
                'たとえ最新の分析機器を導入した（　　　）、それを扱う技術者の育成が伴わなければ宝の持ち腐れになる。',
                'としたところで',
                ['とばかりに', 'とあいまって', 'とあっては'],
                'Even assuming we introduced the latest analytical equipment, it would be a waste of a treasure unless accompanied by the training of engineers to operate it.',
                '仮定条件を提示しつつ、それだけでは不十分だと指摘する論説文でよく使われます。'
            ),
            (
                '百歩譲って先方の主張が正しかった（　　　）、事前の連絡なしに契約条件を変更したのは規約違反だ。',
                'としたところで',
                ['とばかりに', 'と相まって', 'とあっては'],
                'Even conceding a hundred steps and assuming the other party\'s claim was correct, changing the contract terms without prior notice is a violation of the rules.',
                '「百歩譲って〜としたところで」は議論で相手の前提を仮に認めた上で反論する定型表現です。'
            ),
            (
                '今から新しい店舗用地を探し始める（　　　）、年内のオープンには到底間に合わないだろう。',
                'としたところで',
                ['とばかりに', 'と相まって', 'とあっては'],
                'Even if we were to start looking for a new store site now, we would never make it in time for an opening within the year.',
                '動詞辞書形＋「としたところで」の形でも「仮に〜するとしても」を表せます。'
            ),
        ],
    },
    122: {
        'formula': '名詞 ＋ <strong>にしたところで</strong>',
        'similar': '〜にしても / 〜にしたって / 〜にしてみれば',
        'wrong': (
            '私にしたところで、昨日の夜はぐっすり眠れて体調が万全だ。',
            '「Aにしたところで」は「例外に見えるAという立場・人物であっても、やはり同じように難しい・困っている」と述べる表現であり、単なる個人の近況報告には使いません。',
            '"Aにしたところで" means "even from the standpoint of A (who might seem an exception), the situation is still difficult," not a simple personal update.'
        ),
        'comp': (
            '〜にしてみれば',
            'from the viewpoint of',
            '他者の立場に身を置いて「その人にとっては〜だろう」と心情を推察することに重点があります。「〜にしたところで」は「その人でさえ例外ではない」という含みがあります。',
            'Focuses on empathetically imagining another\'s perspective, while 〜にしたところで implies "even for that person, it is no different/easy."',
            'ベテランの彼にしたところで、初めての海外支社長の任務には緊張しているはずだ。',
        ),
        'quiz': [
            (
                '業界トップの技術力を誇るあの企業（　　　）、原材料費の急激な高騰には頭を悩ませているに違いない。',
                'にしたところで',
                ['にしてはじめて', 'に即して', 'に先駆けて'],
                'Even for that company, which boasts the top technological capability in the industry, the sharp rise in raw material costs must surely be a headache.',
                '「一見余裕がありそうなAでさえも、実は同様の課題を抱えている」という文脈で使われます。'
            ),
            (
                '反対意見を述べた佐藤さん（　　　）、プロジェクトの成功を願う気持ちは私たちと少しも変わらないはずだ。',
                'にしたところで',
                ['にいたっては', 'にかまけて', 'にひきかえ'],
                'Even from the standpoint of Mr. Sato, who voiced an opposing opinion, his desire for the project\'s success must not differ from ours in the slightest.',
                '対立しているように見える相手の立場にも理解を示す表現です。'
            ),
            (
                '経験豊富な医師（　　　）、すべての症例に対して即座に完璧な答えを出せるわけではない。',
                'にしたところで',
                ['に先駆けて', 'にまつわる', 'に即して'],
                'Even for an experienced physician, it is not the case that they can immediately give a完美 answer to every single clinical case.',
                '専門家や熟練者であっても限界があることを冷静に述べる際によく使われます。'
            ),
            (
                'いつも冷静沈着な部長（　　　）、これほど大きな契約の最終交渉ともなれば内心は穏やかではないだろう。',
                'にしたところで',
                ['にいたっては', 'にかこつけて', 'にひきかえ'],
                'Even for our department manager, who is always calm and collected, when it comes to the final negotiation of such a major contract, he probably isn\'t calm inside.',
                '人物を主語に立てて「〜にしたところで、やはり…だろう」と推量する文型です。'
            ),
        ],
    },
    123: {
        'formula': '人物を表す名詞 ＋ <strong>にしてみれば</strong> ／ <strong>にしてみても</strong>',
        'similar': '〜の立場から見れば / 〜にとっては / 〜からすれば',
        'wrong': (
            '私にしてみれば、この新しいパソコンはとても使いにくいと思います。',
            '「〜にしてみれば」は話し手以外の第三者の立場に身を置いて「あの人から見れば〜だろう」と推察する表現なので、一人称「私」には使えません。',
            '"〜にしてみれば" puts the speaker in a third party\'s shoes to imagine their perspective, so it cannot be used with the first-person "I."'
        ),
        'comp': (
            '〜にとっては',
            'for; to',
            '一人称（「私にとっては」）にも第三者にも使える一般的な評価の基準点です。「〜にしてみれば」は他者の内面や事情を思いやる場面に限られます。',
            'Can be used for both first person and third parties, whereas 〜にしてみれば is restricted to empathetically considering someone else\'s position.',
            '私にとっては懐かしい曲でも、若い世代には新鮮に聞こえるようだ。',
        ),
        'quiz': [
            (
                '良かれと思ってしたアドバイスでも、現場で苦労している担当者（　　　）、実情を知らない外野の口出しに聞こえたのかもしれない。',
                'にしてみれば',
                ['にしてはじめて', 'にいたっては', 'に先駆けて'],
                'Even if the advice was given with good intentions, from the viewpoint of the person in charge struggling on site, it might have sounded like meddling from an outsider who doesn\'t know the reality.',
                '自分の側からは見えにくい「相手の立場からの受け止め{方|かた}」を推察する表現です。'
            ),
            (
                '効率化のためのデジタル化も、長年手書きの台帳に慣れ親しんできた高齢の店主たち（　　　）、大きな負担に感じられるのだろう。',
                'にしてみれば',
                ['に即して', 'にひきかえ', 'にまつわる'],
                'Digitalization for efficiency is probably felt as a heavy burden from the standpoint of elderly shopkeepers who have been accustomed to handwritten ledgers for many years.',
                '相手の背景や事情に寄り添って心情を推し量る文脈で用いられます。'
            ),
            (
                '突然の配置転換を命じられた本人（　　　）、納得がいかない気持ちになるのも無理からぬことだ。',
                'にしてみれば',
                ['にいたっては', 'にかまけて', 'にとどまらず'],
                'From the viewpoint of the person himself who was ordered a sudden reassignment, it is only natural to feel unconvinced.',
                '「本人にしてみれば」「親にしてみれば」「顧客にしてみれば」がよく使われます。'
            ),
            (
                '開発側が小さな仕様変更だと思っていても、毎日そのソフトを使う利用者（　　　）、作業手順が変わる重大な問題なのだ。',
                'にしてみれば',
                ['に先駆けて', 'にかこつけて', 'に即して'],
                'Even if the development side thinks it is a minor specification change, from the perspective of users who use the software every day, it is a serious issue that changes their workflow.',
                '二つの異なる立場（開発側と利用者）を対比させる文で特に効果的です。'
            ),
        ],
    },
    124: {
        'formula': '文の普通形 ＋ <strong>からといって</strong>（〜とは限らない／わけではない）',
        'similar': '〜からといって必ずしも〜ない / たとえ〜でも',
        'wrong': (
            '今日は天気がいいからといって、洗濯物をたくさん干しました。',
            '「AからといってBない」は「Aという理由があるからといって、直ちにBだと考えるのは早計だ」と部分否定・戒めを述べるため、単純な理由を表す肯定文には使えません。',
            '"Aからといって" is followed by a partial negation ("just because A does not mean B"), never a straightforward affirmative action.'
        ),
        'comp': (
            '〜からには',
            'since; now that',
            '「Aである以上は当然Bすべきだ」と順当な帰結を強く主張します。「〜からといって」はその逆で、安易な短絡的結びつきを否定します。',
            'Asserts a natural obligation ("since A, we must B"), whereas 〜からといって rejects jumping to conclusion B just because of A.',
            '引き受けたからには、最後まで責任を持ってやり遂げるつもりだ。',
        ),
        'quiz': [
            (
                '価格が高い（　　　）、必ずしもすべての人にとって使いやすい製品であるとは限らない。',
                'からといって',
                ['からには', 'からして', 'からある'],
                'Just because the price is high does not necessarily mean that it is an easy-to-use product for everyone.',
                '「〜からといって、必ずしも…とは限らない」は最も代表的な呼応パターンです。'
            ),
            (
                '一度の試験で思うような結果が出なかった（　　　）、これまでの努力がすべて無駄になるわけではない。',
                'からといって',
                ['からには', 'からして', 'からの'],
                'Just because you didn\'t get the result you hoped for on a single exam does not mean that all your efforts up to now have been in vain.',
                '失敗して落ち込んでいる人を励まし、短絡的な悲観を否定する文脈です。'
            ),
            (
                '野菜が体にいい（　　　）、そればかり食べてたんぱく質を摂らなければ栄養バランスが崩れてしまう。',
                'からといって',
                ['からには', 'からある', 'からして'],
                'Just because vegetables are good for your health, if you eat only vegetables and don\'t take in protein, your nutritional balance will be thrown off.',
                '「Aだからといって極端な行動をとるのは良くない」と戒める用法です。'
            ),
            (
                '相手が親しい友人だ（　　　）、礼儀や約束をおろそかにしてよい理由にはならない。',
                'からといって',
                ['からには', 'からして', 'からの'],
                'Just because the other person is a close friend is no reason to neglect manners or promises.',
                '「〜からといって、…していいわけではない／理由にはならない」も頻出の形です。'
            ),
        ],
    },
    125: {
        'formula': '名詞（＋の）＋ <strong>いかんだ</strong> ／ <strong>いかんにかかっている</strong>',
        'similar': '〜次第だ / 〜によって決まる / 〜にかかっている',
        'wrong': (
            '昨日のサッカーの試合結果は、選手たちの頑張りいかんだった。',
            '「〜いかんだ」は「これからどうなるかは〜次第で決まる」と未確定の事柄の条件を述べる表現なので、すでに確定した過去の結果には使えません。',
            '"〜いかんだ" states that a future or undetermined outcome depends on X, so it cannot describe an already settled past result.'
        ),
        'comp': (
            '〜次第だ',
            'depends on',
            '日常会話でも広く使える表現です。「〜いかんだ」はより硬い書き言葉・論説調の表現で、「の」を介して名詞につくこともできます。',
            'Widely used in daily conversation as well, whereas 〜いかんだ is a more formal written expression that can also attach via の.',
            '交渉がまとまるかどうかは、先方の誠意ある対応いかんにかかっている。',
        ),
        'quiz': [
            (
                '新しい地域活性化プロジェクトが軌道に乗るかどうかは、住民と行政の連携（　　　）と言える。',
                'いかんだ',
                ['のみか', 'ばかりだ', 'ずくめだ'],
                'Whether the new regional revitalization project gets on track or not can be said to depend on the cooperation between residents and the administration.',
                '「Aいかんだ」で「Aがどうであるかによって結果が決まる」ことを表します。'
            ),
            (
                'どれほど優れた道具も、結局はそれを使う人間の心がけ（　　　）で有益にも無益にもなり得る。',
                'いかん',
                ['まみれ', 'ごとき', 'ずくめ'],
                'No matter how excellent a tool is, depending ultimately on the mindset of the person using it, it can become either beneficial or useless.',
                '「名詞＋いかんで（は）」の形で文中に用いられ、「〜次第で」を表す用法です。'
            ),
            (
                '来期の海外出店計画を拡大するか見直すかは、今四半期の売上実績の（　　　）にかかっている。',
                'いかん',
                ['いたる', 'きわみ', 'おり'],
                'Whether we expand or review next term\'s overseas store opening plan depends on this quarter\'s sales performance.',
                '「名詞＋の＋いかんにかかっている」も非常によく使われる格調高い連語です。'
            ),
            (
                '希少な伝統工芸が百年先まで残るか否かは、若手後継者を育てられるかどうかの取り組み（　　　）。',
                'いかんだ',
                ['まじきだ', 'なりだ', 'ごときだ'],
                'Whether rare traditional crafts survive a hundred years into the future depends on our efforts to train young successors.',
                '将来の成否を左右する決定的な要因を指し示す文末表現です。'
            ),
        ],
    },
    126: {
        'formula': '名詞（＋の）＋ <strong>いかんによって（は）</strong>',
        'similar': '〜次第で（は） / 〜いかんで（は） / 〜に応じて',
        'wrong': (
            '天気が晴れのいかんによっては、明日はハイキングに行きましょう。',
            '「〜いかんによって」の前には「天候・結果・内容・対応」のように幅や変化のある抽象名詞が来ます。「晴れ」のようにすでに一つに決まった語にはつきません。',
            '"〜いかんによって" must follow a noun that has variable states or outcomes (like weather, results, response), not a fixed state like "sunny."'
        ),
        'comp': (
            '〜いかんにかかわらず',
            'regardless of',
            '「〜いかんによって」が「条件次第で結果が変わる」ことを表すのに対し、「〜いかんにかかわらず」は「条件がどうであっても結果は変わらない」と正反対の意味になります。',
            'While 〜いかんによって means the outcome changes depending on X, 〜いかんにかかわらず means the outcome remains the same regardless of X.',
            '天候のいかんにかかわらず、明日の室内音楽祭は予定通り開催いたします。',
        ),
        'quiz': [
            (
                '精密検査の結果（　　　）、来月の海外出張のスケジュールを変更する必要があるかもしれない。',
                'いかんによっては',
                ['いかんにかかわらず', 'をおいてほかに', 'といったらありはせず'],
                'Depending on the results of the detailed medical examination, it may be necessary to change next month\'s overseas business trip schedule.',
                '「〜いかんによっては…かもしれない」で、結果次第では特別な対応が必要になる可能性を示します。'
            ),
            (
                '貸し出し用の機材は、使用状況や破損の程度（　　　）、修理費用をご負担いただく場合がございます。',
                'いかんによって',
                ['いかんにかかわらず', 'を皮切りにして', 'にとどまらず'],
                'For rental equipment, depending on usage conditions and the degree of damage, you may be asked to bear the repair costs.',
                '規約や案内文で条件に応じた対応の違いを明記する際によく使われます。'
            ),
            (
                '交渉相手の出方（　　　）、こちらもあらかじめ用意していた代替案を提示する準備ができている。',
                'いかんによっては',
                ['いかんにかかわらず', 'をものともせずに', 'はおろか'],
                'Depending on how the negotiating partner acts, we are ready to present the alternative plan we prepared in advance.',
                '相手の態度や状況の変化に柔軟に対応する構えを表します。'
            ),
            (
                'アンケートの回答内容の（　　　）、来年度の講座カリキュラムが大幅に刷新される見込みだ。',
                'いかんによって',
                ['いかんにかかわらず', 'をよそにして', 'に先駆けて'],
                'Depending on the content of the survey responses, next year\'s course curriculum is expected to be significantly revamped.',
                '「名詞＋の＋いかんによって」の形で、調査結果や審査内容が判断基準になることを示します。'
            ),
        ],
    },
    127: {
        'formula': '名詞（＋の）＋ <strong>いかんにかかわらず</strong> ／ <strong>いかんによらず</strong>',
        'similar': '〜を問わず / 〜に関係なく / 〜はどうあれ',
        'wrong': (
            'テストの点数のいかんにかかわらず、八十点以上の人だけが上級クラスに進めます。',
            '「〜いかんにかかわらず」は「どんな状態・結果であっても無関係に」という意味なので、点数によって条件を分けている文とは矛盾します。',
            '"〜いかんにかかわらず" means "regardless of," so it contradicts a main clause that filters people based on their score.'
        ),
        'comp': (
            '〜を問わず',
            'regardless of',
            '「年齢・性別・昼夜・屋内外を問わず」など幅広い名詞に使えます。「〜のいかんにかかわらず」は「理由・事情・成否・有無」など抽象度の高い漢語名詞と好んで結びつきます。',
            'Pairs with a wide range of nouns, whereas 〜のいかんにかかわらず prefers formal Sino-Japanese nouns like reason, circumstances, success/failure, or presence/absence.',
            'この市民マラソン大会は、年齢や経験を問わず誰でも参加できます。',
        ),
        'quiz': [
            (
                '応募書類は、採用・不採用の結果の（　　　）、一切返却いたしませんのであらかじめご了承ください。',
                'いかんにかかわらず',
                ['いかんによっては', 'いかんにかかっている', 'いかんだからといって'],
                'Please understand in advance that application documents will not be returned under any circumstances, regardless of the hiring outcome.',
                '募集要項や公的な通知文で「結果・理由・事情のいかんにかかわらず」は最頻出の表現です。'
            ),
            (
                '安全管理規定により、作業現場に入る際は、滞在時間の長短や役職の（　　　）、必ず保護帽を着用しなければならない。',
                'いかんにかかわらず',
                ['いかんによっては', 'をおいてほかに', 'にとどまらず'],
                'According to safety management regulations, when entering the work site, you must wear a protective helmet without fail, regardless of the length of stay or your job title.',
                '例外を一切認めない厳格なルールを述べる文脈で用いられます。'
            ),
            (
                '契約期間満了後の更新の有無の（　　　）、今月末までに所定の確認書をご提出いただく必要があります。',
                'いかんにかかわらず',
                ['いかんによっては', 'を皮切りにして', 'と相まって'],
                'Regardless of whether or not you renew the contract after its expiration, you must submit the prescribed confirmation form by the end of this month.',
                '「有無（うむ）のいかんにかかわらず」は対概念の名詞を伴う代表的なコロケーションです。'
            ),
            (
                'いかなる理由の（　　　）、提出期限を過ぎた論文は審査の対象外となりますので十分ご注意ください。',
                'いかんにかかわらず',
                ['いかんによっては', 'に難くないため', 'に値するから'],
                'Please be fully aware that regardless of the reason, papers submitted past the deadline will not be eligible for review.',
                '「理由のいかんにかかわらず（どんな理由があろうとも）」はN1文法問題で最もよく問われる形の一つです。'
            ),
        ],
    },
}
