#!/usr/bin/env python3
import json
import os
import re

REPO_ROOT = '/Users/yamauchimiku/Documents/GitHub/japanese-learning'

CARDS_RAW = [
    ("軽い（かるい）", "light (weight), minor, nimble", "<ruby>この<rt></rt></ruby><ruby>荷物<rt>にもつ</rt></ruby>は<ruby>見<rt>み</rt></ruby>た<ruby>目<rt>め</rt></ruby>よりずっと<ruby>軽<rt>かる</rt></ruby>いです。", "This luggage is much lighter than it looks.", "軽い vs 重い: 「軽い」は重さや負担、程度が小さいこと、「重い」は重量や負担、事態が深刻で大きいこと。"),
    ("重い（おもい）", "heavy (weight), serious, burdensome", "スーツケースが<ruby>重<rt>おも</rt></ruby>いので、タクシーでホテルへ<ruby>向<rt>む</rt></ruby>かいました。", "Since the suitcase was heavy, I headed to the hotel by taxi.", "重い vs 軽い: 「重い病気（深刻な病気）」のように心理的・抽象的な重大さにも使う。"),
    ("続編（ぞくへん）", "sequel (of a movie, novel, anime)", "<ruby>大人気<rt>だいにんき</rt></ruby>アニメの<ruby>続編<rt>ぞくへん</rt></ruby>が、<ruby>来年<rt>らいねん</rt></ruby>の<ruby>春<rt>はる</rt></ruby>に<ruby>公開<rt>こうかい</rt></ruby>されるそうです。", "I heard that the sequel to the popular anime will be released next spring.", "続編 vs 続き: 「続編」は作品として独立した第2作・後編を指す改まった名詞、「続き」は物語や話の直後の部分全般を指す日常語。"),
    ("続き（つづき）", "continuation, the rest (of a story), sequel", "<ruby>時間<rt>じかん</rt></ruby>がなくなったので、この<ruby>話<rt>はな</rt></ruby>の<ruby>続<rt>つづ</rt></ruby>きはまた<ruby>明日<rt>あした</rt></ruby>しましょう。", "We ran out of time, so let's continue this conversation tomorrow.", "続き vs 続編: 「続き」はドラマの次回や中断した会話・作業の再開部分に幅広く使う。"),
    ("完結（かんけつ）", "completion, conclusion (of a series/story)", "１０<ruby>年間<rt>ねんかん</rt></ruby><ruby>連載<rt>れんさい</rt></ruby>が<ruby>続<rt>つづ</rt></ruby>いたマンガが、ついに<ruby>最終回<rt>さいしゅうかい</rt></ruby>で<ruby>完結<rt>かんけつ</rt></ruby>を<ruby>迎<rt>むか</rt></ruby>えた。", "The manga that had been serialized for 10 years finally reached its conclusion with the final chapter.", "完結 vs 終了: 「完結」は物語やシリーズが最後まで完全に描き切って終わること、「終了」は単に期限や作業が終わること。"),
    ("倍速（ばいそく）", "double speed, 1.5x/2x playback speed", "<ruby>時間<rt>じかん</rt></ruby>を<ruby>節約<rt>せつやく</rt></ruby>するために、YouTubeの<ruby>動画<rt>どうが</rt></ruby>を１.５<ruby>倍速<rt>ばいそく</rt></ruby>で<ruby>見<rt>み</rt></ruby>ることが<ruby>多<rt>おお</rt></ruby>い。", "To save time, I often watch YouTube videos at 1.5x speed.", "倍速再生（ばいそくさいせい: double-speed playback）, ２倍速（2x speed）"),
    ("聖地巡礼（せいちじゅんれい）", "anime pilgrimage, visiting real-life anime locations", "<ruby>大好<rt>だいす</rt></ruby>きなアニメの<ruby>舞台<rt>ぶたい</rt></ruby>になった<ruby>街<rt>まち</rt></ruby>を<ruby>訪<rt>おとず</rt></ruby>れて、<ruby>聖地巡礼<rt>せいちじゅんれい</rt></ruby>を<ruby>楽<rt>たの</rt></ruby>しんだ。", "I visited the town that served as the setting for my favorite anime and enjoyed an anime pilgrimage.", "聖地（せいち: anime setting / sacred place）, ロケ地巡り（ろけちめぐり: visiting filming locations）"),
    ("髭（ひげ）", "beard, mustache, whiskers", "<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>仕事<rt>しごと</rt></ruby>に<ruby>行<rt>い</rt></ruby>く<ruby>前<rt>まえ</rt></ruby>に、<ruby>電気<rt>でんき</rt></ruby>カミソリで<ruby>髭<rt>ひげ</rt></ruby>をそります。", "Every morning before going to work, I shave my beard with an electric razor.", "髭を剃る（ひげをそる: to shave）, 髭を生やす（ひげをはやす: to grow a beard）"),
    ("よくなかった（よくなかった）", "was not good, was bad", "<ruby>昨日<rt>きのう</rt></ruby>は<ruby>体調<rt>たいちょう</rt></ruby>があまりよくなかったので、<ruby>早<rt>はや</rt></ruby>めに<ruby>寝<rt>ね</rt></ruby>ました。", "I didn't feel very well yesterday, so I went to bed early.", "「いい／よい」の過去否定形。日常会話では「よくなかった」、改まった場面では「よくありませんでした」。"),
    ("結末（けつまつ）", "ending, conclusion, outcome (of a story)", "そのミステリー<ruby>小説<rt>しょうせつ</rt></ruby>は、だれも<ruby>予想<rt>よそう</rt></ruby>できない<ruby>衝撃的<rt>しょうげきてき</rt></ruby>な<ruby>結末<rt>けつまつ</rt></ruby>だった。", "That mystery novel had a shocking conclusion that no one could have predicted.", "結末 vs 結果: 「結末」は小説・劇・事件の物語的な締めくくりや終わり方、「結果」は原因から導き出された客観的な状態や数値。"),
    ("失望した（しつぼうした）", "was disappointed, felt let down", "<ruby>期待<rt>きたい</rt></ruby>していたレストランの<ruby>料理<rt>りょうり</rt></ruby>がおいしくなくて、とても<ruby>失望<rt>しつぼう</rt></ruby>した。", "The food at the restaurant I had high hopes for wasn't delicious, so I was very disappointed.", "失望 vs がっかり: 「がっかりした」は日常会話での心理的落胆、「失望した」は期待が裏切られたときの深刻で改まった落胆。"),
    ("くっつく（くっつく）", "to stick to, to adhere, to get together (as a couple)", "ガムが<ruby>靴<rt>くつ</rt></ruby>の<ruby>裏<rt>うら</rt></ruby>にくっついてしまって、なかなか取れない。", "Gum got stuck to the bottom of my shoe and won't come off easily.", "くっつく vs くっつける: 「くっつく」は自動詞（自然と付く・恋人同士になる）、「くっつける」は他動詞（物を貼り合わせる）。"),
    ("カップルができる（かっぷるができる）", "a couple is formed, two people start dating", "<ruby>先週<rt>せんしゅう</rt></ruby>の<ruby>合コン<rt>ごうこん</rt></ruby>で、なんと２<ruby>組<rt>くみ</rt></ruby>のカップルができたらしいよ。", "I heard that surprisingly two couples were formed at last week's mixer!", "付き合う（つきあう: to date）, カップル誕生（かっぷるたんじょう）"),
    ("〜派（〜は）", "person who prefers ..., faction, group", "わたしは<ruby>朝<rt>あさ</rt></ruby>ごはんはパンよりごはん<ruby>派<rt>は</rt></ruby>です。", "When it comes to breakfast, I am more of a rice person than a bread person.", "甘党（あまとう: sweet tooth）, 慎重派（しんちょうは: cautious type）, 犬派 vs 猫派"),
    ("広告（こうこく）", "advertisement, ad, commercial", "スマホでゲームをしていると、<ruby>途中<rt>とちゅう</rt></ruby>で<ruby>動画<rt>どうが</rt></ruby>の<ruby>広告<rt>こうこく</rt></ruby>が<ruby>流<rt>なが</rt></ruby>れる。", "When playing a game on my smartphone, video advertisements play midway through.", "広告 vs 宣伝: 「広告」はメディアの広告枠・媒体そのもの、「宣伝」は商品や活動を広くアピールして周知させる行為。"),
    ("確率（かくりつ）", "probability, likelihood, odds", "<ruby>午後<rt>ごご</rt></ruby>から<ruby>降水確率<rt>こうすいかくりつ</rt></ruby>が８０％なので、<ruby>傘<rt>かさ</rt></ruby>を<ruby>持<rt>も</rt></ruby>っていきましょう。", "Since the precipitation probability is 80% from the afternoon, let's take an umbrella.", "降水確率（こうすいかくりつ: chance of rain）, 高確率（こうかくりつ: high probability）"),
    ("完結する（かんけつする）", "to be completed, to conclude (series/novel)", "<ruby>全<rt>ぜん</rt></ruby>３０<ruby>巻<rt>かん</rt></ruby>の<ruby>長編<rt>ちょうへん</rt></ruby><ruby>小説<rt>しょうせつ</rt></ruby>がついに<ruby>完結<rt>かんけつ</rt></ruby>した。", "The 30-volume long novel finally came to an end.", "完結する vs 終わる: サ変動詞。「完結する」は作品・物語が完結することに限定して使う。"),
    ("起こされる（おこされる）", "to be woken up (passive)", "<ruby>今朝<rt>けさ</rt></ruby>は<ruby>早朝<rt>そうちょう</rt></ruby>からカラスの<ruby>大<rt>おお</rt></ruby>きな<ruby>鳴<rt>な</rt></ruby>き<ruby>声<rt>ごえ</rt></ruby>に<ruby>起<rt>お</rt></ruby>こされた。", "This morning I was woken up early by the loud cawing of crows.", "起こす（他動詞）の受身形。目覚まし時計に起こされる、母に起こされる。"),
    ("楽（らく）", "comfortable, easy, painless", "<ruby>新幹線<rt>しんかんせん</rt></ruby>を<ruby>使<rt>つか</rt></ruby>ったら、<ruby>移動<rt>いどう</rt></ruby>がとても<ruby>楽<rt>らく</rt></ruby>でした。", "Using the Shinkansen made traveling very comfortable and easy.", "楽（らく） vs 楽しい（たのしい）: 「楽しい」はワクワクする感情、「楽」は苦労や負担がなくて平穏・心地よい状態。"),
    ("助手（じょしゅ）", "assistant, helper", "<ruby>教授<rt>きょうじゅ</rt></ruby>の<ruby>研究<rt>けんきゅう</rt></ruby>をサポートする<ruby>助手<rt>じょしゅ</rt></ruby>として<ruby>働<rt>はたら</rt></ruby>いています。", "I work as an assistant supporting the professor's research.", "助手席（じょしゅせき: front passenger seat）, アシスタント（日常語）"),
    ("観光地（かんこうち）", "tourist spot, sightseeing destination", "<ruby>京都<rt>きょうと</rt></ruby>は<ruby>世界中<rt>せかいじゅう</rt></ruby>から<ruby>旅行客<rt>りょこうきゃく</rt></ruby>が<ruby>訪<rt>おとず</rt></ruby>れる<ruby>有名<rt>ゆうめい</rt></ruby>な<ruby>観光地<rt>かんこうち</rt></ruby>です。", "Kyoto is a famous tourist destination visited by travelers from all over the world.", "観光（かんこう: sightseeing）, 名所（めいしょ: famous spot）"),
    ("飲食店（いんしょくてん）", "restaurant, eatery, dining establishment", "この<ruby>通<rt>とお</rt></ruby>りには、おいしいラーメン<ruby>屋<rt>や</rt></ruby>やカフェなどの<ruby>飲食店<rt>いんしょくてん</rt></ruby>が<ruby>並<rt>なら</rt></ruby>んでいます。", "Along this street, dining establishments such as delicious ramen shops and cafes line up.", "飲食店 vs レストラン: 「飲食店」は居酒屋・カフェ・ファミレス等を含む公的・業界的な総称。"),
    ("二重価格（にじゅうかかく）", "dual pricing, two-tier pricing", "<ruby>外国人<rt>がいこくじん</rt></ruby><ruby>観光客<rt>かんこうきゃく</rt></ruby>と<ruby>地元<rt>じもと</rt></ruby>の<ruby>住民<rt>じゅうみん</rt></ruby>で<ruby>料金<rt>りょうきん</rt></ruby>を<ruby>分<rt>わ</rt></ruby>ける<ruby>二重価格<rt>にじゅうかかく</rt></ruby>が<ruby>話題<rt>わだい</rt></ruby>になっている。", "Dual pricing, where different fees are charged for foreign tourists and local residents, is becoming a topic of discussion.", "二重価格 vs 割引: 「二重価格」は属性によって異なる定価を設定すること。"),
    ("意見が分かれる（いけんがわかれる）", "opinions are divided, split opinions", "<ruby>新<rt>あたら</rt></ruby>しいプロジェクトの<ruby>方針<rt>ほうしん</rt></ruby>について、チーム<ruby>内<rt>ない</rt></ruby>で<ruby>意見<rt>いけん</rt></ruby>が<ruby>分<rt>わ</rt></ruby>かれた。", "Within the team, opinions were divided regarding the policy for the new project.", "意見が一致する（いけんがいっちする: opinions agree）の対義表現。"),
    ("血液型（けつえきがた）", "blood type", "<ruby>日本<rt>にほん</rt></ruby>では<ruby>初対面<rt>しょたいめん</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>に「<ruby>血液型<rt>けつえきがた</rt></ruby>は<ruby>何型<rt>なにがた</rt></ruby>ですか」と<ruby>聞<rt>き</rt></ruby>かれることがある。", "In Japan, you are sometimes asked 'What is your blood type?' by people you meet for the first time.", "血液型占い（けつえきがたうらない: blood type personality test）"),
    ("几帳面（きちょうめん）", "methodical, meticulous, neat, punctual", "<ruby>彼<rt>かれ</rt></ruby>はとても<ruby>几帳面<rt>きちょうめん</rt></ruby>で、デスクの<ruby>上<rt>うえ</rt></ruby>がいつもきれいに<ruby>片付<rt>かたづ</rt></ruby>いている。", "He is very methodical and neat, and his desk is always neatly organized.", "几帳面 vs 大雑把: 「几帳面」は細かいところまで規則正しくきちんとすること。大雑把の対義語。"),
    ("自己中（じこちゅう）", "selfish, self-centered, egoistic", "<ruby>自分<rt>じぶん</rt></ruby>の<ruby>都合<rt>つごう</rt></ruby>ばかり<ruby>優先<rt>ゆうせん</rt></ruby>するような<ruby>自己中<rt>じこちゅう</rt></ruby>な<ruby>態度<rt>たいど</rt></ruby>はよくないよ。", "A selfish attitude of only prioritizing your own convenience is not good.", "自己中心的（じこちゅうしんてき）の略。わがまま（日常語）。"),
    ("大雑把（おおざっぱ）", "rough, broad, coarse, careless", "<ruby>大雑把<rt>おおざっぱ</rt></ruby>な<ruby>計算<rt>けいさん</rt></ruby>ですが、<ruby>旅行<rt>りょこう</rt></ruby>の<ruby>費用<rt>ひよう</rt></ruby>はひとり５<ruby>万円<rt>まんえん</rt></ruby>くらいです。", "It's a rough calculation, but the travel cost is about 50,000 yen per person.", "大雑把 vs 几帳面: 「大雑把」はおおまかで細部にこだわらないこと。ポジティブには「おおらか」、ネガティブには「雑」を指す。"),
    ("変人（へんじん）", "eccentric person, weirdo, oddball", "<ruby>彼<rt>かれ</rt></ruby>は<ruby>周<rt>まわ</rt></ruby>りから<ruby>変人<rt>へんじん</rt></ruby>と<ruby>呼<rt>よ</rt></ruby>ばれているが、<ruby>実<rt>じつ</rt></ruby>は<ruby>天才的<rt>てんさいてき</rt></ruby>なプログラマーだ。", "He is called an eccentric person by those around him, but he is actually a genius programmer.", "変人 vs 変わり者: 「変わり者」は少し個性的・風変わりな人、「変人」は常識から大きく外れた特異な人。"),
    ("悩む（なやむ）", "to worry, to agonize, to be troubled, to hesitate", "メニューに美味しそうな<ruby>料理<rt>りょうり</rt></ruby>が多すぎて、どれを<ruby>注文<rt>ちゅうもん</rt></ruby>するか<ruby>悩<rt>なや</rt></ruby>んだ。", "There were so many delicious-looking dishes on the menu that I was troubled over which one to order.", "悩む vs 考える: 「考える」は論理的に思考すること、「悩む」はどうすべきか迷って苦しむ内面的な葛藤。"),
    ("偏食（へんしょく）", "unbalanced diet, picky eating habits", "<ruby>子供<rt>こども</rt></ruby>のころは<ruby>偏食<rt>へんしょく</rt></ruby>がひどく、<ruby>野菜<rt>やさい</rt></ruby>をまったく<ruby>食<rt>た</rt></ruby>べなかった。", "When I was a child, I had severe picky eating habits and ate no vegetables at all.", "好き嫌い（すききらい: likes and dislikes / pickiness）の改まった表現。"),
    ("科学（かがく）", "science", "<ruby>現代<rt>げんだい</rt></ruby>の<ruby>科学<rt>かがく</rt></ruby>の<ruby>力<rt>ちから</rt></ruby>によって、さまざまな<ruby>病気<rt>びょうき</rt></ruby>の<ruby>治療<rt>ちりょう</rt></ruby>が<ruby>可能<rt>かのう</rt></ruby>になった。", "Through the power of modern science, treatment of various illnesses has become possible.", "科学 vs 化学: 「科学（かがく）」は自然科学全般、「化学（かがく／ばけがく）」は物質の変化を扱うchemistry。"),
    ("宇宙飛行士（うちゅうひこうし）", "astronaut", "<ruby>子供<rt>こども</rt></ruby>のころの<ruby>夢<rt>ゆめ</rt></ruby>は、<ruby>宇宙飛行士<rt>うちゅうひこうし</rt></ruby>になって<ruby>月<rt>つき</rt></ruby>へ<ruby>行<rt>い</rt></ruby>くことでした。", "My childhood dream was to become an astronaut and go to the moon.", "宇宙ステーション（うちゅうすてーしょん: space station）, 宇宙（うちゅう: outer space）"),
    ("責任（せきにん）", "responsibility, duty, liability", "リーダーとして、プロジェクトを<ruby>成功<rt>せいこう</rt></ruby>させる<ruby>責任<rt>せきにん</rt></ruby>がある。", "As the leader, I have the responsibility to make the project a success.", "責任を持つ（せきにんをもつ: to take responsibility）, 責任感（せきにんかん: sense of responsibility）"),
    ("現実的（げんじつてき）", "realistic, pragmatic, practical", "<ruby>夢<rt>ゆめ</rt></ruby>を<ruby>語<rt>かた</rt></ruby>るだけでなく、<ruby>現実的<rt>げんじつてき</rt></ruby>な<ruby>計画<rt>けいかく</rt></ruby>を<ruby>立<rt>た</rt></ruby>てることが<ruby>大切<rt>たいせつ</rt></ruby>だ。", "It is important not just to talk about dreams, but to make realistic plans.", "現実的 vs 理想的: 「現実的」は実現可能で実際的なこと。「理想的（りそうてき）」の対義語。"),
    ("解剖（かいぼう）", "dissection, autopsy, anatomical analysis", "<ruby>医学生<rt>いがくせい</rt></ruby>たちは<ruby>人体<rt>じんたい</rt></ruby>の<ruby>構造<rt>こうぞう</rt></ruby>を<ruby>学<rt>まな</rt></ruby>ぶために、<ruby>解剖<rt>かいぼう</rt></ruby>の<ruby>実習<rt>じっしゅう</rt></ruby>を<ruby>行<rt>おこな</rt></ruby>う。", "Medical students conduct dissection practice to learn the structure of the human body.", "解剖学（かいぼうがく: anatomy）, 司法解剖（しほうかいぼう: forensic autopsy）"),
    ("物理（ぶつり）", "physics", "<ruby>高校<rt>こうこう</rt></ruby>のとき、<ruby>物理<rt>ぶつり</rt></ruby>の<ruby>実験<rt>じっけん</rt></ruby>がとてもおもしろかった。", "In high school, physics experiments were very interesting.", "物理学（ぶつりがく: physics）, 物理的に（ぶつりてきに: physically）"),
    ("生物（せいぶつ）", "living organism, creature, biology", "<ruby>深海<rt>しんかい</rt></ruby>には、まだ<ruby>見<rt>み</rt></ruby>たこともない<ruby>不思議<rt>ふしぎ</rt></ruby>な<ruby>生物<rt>せいぶつ</rt></ruby>がたくさん<ruby>生息<rt>せいそく</rt></ruby>している。", "In the deep sea, many mysterious living organisms that have never been seen before inhabit.", "生物（せいぶつ: living creature / biology） vs 生物（なまもの: raw food）"),
    ("理系（りけい）", "science track, STEM field/major", "<ruby>数学<rt>すうがく</rt></ruby>やプログラミングが<ruby>得意<rt>とくい</rt></ruby>なので、<ruby>大学<rt>だいがく</rt></ruby>では<ruby>理系<rt>りけい</rt></ruby>の<ruby>学部<rt>がくぶ</rt></ruby>に<ruby>進<rt>すす</rt></ruby>みました。", "Since I was good at math and programming, I proceeded to a STEM faculty at university.", "理系 vs 文系: 「理系」は自然科学・工学系、「文系（ぶんけい）」は人文学・社会科学系。"),
    ("負けず嫌い（まけずぎらい）", "hating to lose, competitive", "<ruby>彼女<rt>かのじょ</rt></ruby>はとても<ruby>負<rt>ま</rt></ruby>けず<ruby>嫌<rt>ぎら</rt></ruby>いで、ゲームでも<ruby>勝<rt>か</rt></ruby>つまでやり<ruby>直<rt>なお</rt></ruby>す。", "She is very competitive and hates to lose, so even in games she replays until she wins.", "競争心が強い（きょうそうしんがつよい: strongly competitive）"),
    ("皮膚科（ひふか）", "dermatology, dermatologist's clinic", "<ruby>肌<rt>はだ</rt></ruby>の<ruby>荒<rt>あ</rt></ruby>れがひどいので、<ruby>近所<rt>きんじょ</rt></ruby>の<ruby>皮膚科<rt>ひふか</rt></ruby>へ<ruby>行<rt>い</rt></ruby>ってお<ruby>薬<rt>くすり</rt></ruby>をもらった。", "Since my skin irritation was severe, I went to a neighborhood dermatology clinic and got medicine.", "内科（ないか: internal medicine）, 外科（げか: surgery）, 眼科（がんか: ophthalmology）"),
    ("一石二鳥（いっせきにちょう）", "killing two birds with one stone", "<ruby>自転車<rt>じてんしゃ</rt></ruby>で<ruby>通勤<rt>つうきん</rt></ruby>すれば、<ruby>運動<rt>うんどう</rt></ruby>にもなるし<ruby>電車代<rt>でんしゃだい</rt></ruby>も<ruby>浮<rt>う</rt></ruby>いて<ruby>一石二鳥<rt>いっせきにちょう</rt></ruby>だ。", "If you commute by bicycle, you get exercise and save train fare, killing two birds with one stone.", "四字熟語。「一挙両得（いっきょりょうとく）」も同義表現。"),
    ("マシ（まし）", "better, preferable, less bad", "<ruby>昨日<rt>きのう</rt></ruby>よりは<ruby>風邪<rt>かぜ</rt></ruby>の<ruby>症状<rt>しょうじょう</rt></ruby>がだいぶマシになりました。", "My cold symptoms have gotten much better compared to yesterday.", "マシ vs より良い: 「マシ」は最善ではないが、より悪い状態と比べれば耐えられる・好ましいというニュアンス。"),
    ("モテモテ（もてもて）", "extremely popular (romantically)", "<ruby>彼<rt>かれ</rt></ruby>はスポーツ万能で<ruby>優<rt>やさ</rt></ruby>しいので、<ruby>学校<rt>がっこう</rt></ruby>でモテモテです。", "He is all-around good at sports and kind, so he is extremely popular at school.", "モテモテ vs モテる: 「モテる」の人気がさらに強調された表現。大勢から好意を寄せられている状態。"),
    ("モテる（もてる）", "to be popular (romantically), to attract interest", "どうすれば<ruby>異性<rt>いせい</rt></ruby>からモテるようになるのか、<ruby>友達<rt>ともだち</rt></ruby>と<ruby>真剣<rt>しんけん</rt></ruby>に<ruby>話<rt>はな</rt></ruby>し<ruby>合<rt>あ</rt></ruby>った。", "I discussed seriously with my friend how to become popular with the opposite sex.", "モテる vs 人気がある: 「人気がある」は一般の好感度、「モテる」は恋愛対象としての好意に特化。"),
    ("合コン（ごうこん）", "group blind date, matchmaking mixer", "<ruby>大学<rt>だいがく</rt></ruby>の<ruby>友達<rt>ともだち</rt></ruby>に<ruby>誘<rt>さそ</rt></ruby>われて、<ruby>初<rt>はじ</rt></ruby>めて<ruby>合コン<rt>ごうこん</rt></ruby>に<ruby>参加<rt>さんか</rt></ruby>した。", "Invited by my university friend, I participated in a group blind date for the first time.", "合同コンパの略。街コン（まちこん: city mixer）"),
    ("法医学（ほういがく）", "forensic medicine", "<ruby>法医学<rt>ほういがく</rt></ruby>のドラマを<ruby>見<rt>み</rt></ruby>てから、<ruby>死因<rt>しいん</rt></ruby>を<ruby>突<rt>つ</rt></ruby>き<ruby>止<rt>と</rt></ruby>める<ruby>仕事<rt>しごと</rt></ruby>に<ruby>興味<rt>きょうみ</rt></ruby>を<ruby>持<rt>も</rt></ruby>った。", "After watching a forensic medicine drama, I became interested in work that pinpoints the cause of death.", "法医学者（ほういがくしゃ: forensic pathologist）, 司法解剖（しほうかいぼう）"),
    ("論文（ろんぶん）", "academic paper, thesis, dissertation", "<ruby>大学院<rt>だいがくいん</rt></ruby>を<ruby>卒業<rt>そつぎょう</rt></ruby>するために、<ruby>徹夜<rt>てつや</rt></ruby>で<ruby>修士<rt>しゅうし</rt></ruby><ruby>論文<rt>ろんぶん</rt></ruby>を<ruby>書<rt>か</rt></ruby>き<ruby>上<rt>あ</rt></ruby>げた。", "In order to graduate from graduate school, I stayed up all night to finish writing my master's thesis.", "卒業論文（そつぎょうろんぶん: graduation thesis）, 論文発表（ろんぶんはっぴょう）"),
    ("実家（じっか）", "one's parents' home, family home", "お<ruby>正月<rt>しょうがつ</rt></ruby>は<ruby>実家<rt>じっか</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>って、<ruby>家族<rt>かぞく</rt></ruby>とゆっくり<ruby>過<rt>す</rt></ruby>ごす<ruby>予定<rt>よてい</rt></ruby>です。", "During New Year's, I plan to return to my parents' home and spend a relaxing time with family.", "実家 vs 我が家: 「実家」は生まれ育った親の家、「我が家（わがや）」は現在自分が暮らしている家庭・住まい。"),
    ("渋滞（じゅうたい）", "traffic jam, congestion", "<ruby>連休<rt>れんきゅう</rt></ruby>の<ruby>初日<rt>しょにち</rt></ruby>で、<ruby>高速道路<rt>こうそくどうろ</rt></ruby>が２０キロも<ruby>渋滞<rt>じゅうたい</rt></ruby>している。", "On the first day of consecutive holidays, the expressway has a 20-kilometer traffic jam.", "交通渋滞（こうつうじゅうたい: traffic congestion）, 混雑（こんざつ: crowding）"),
    ("聴診器（ちょうしんき）", "stethoscope", "お<ruby>医者<rt>いしゃ</rt></ruby>さんが<ruby>聴診器<rt>ちょうしんき</rt></ruby>を<ruby>胸<rt>むね</rt></ruby>に<ruby>当<rt>あ</rt></ruby>てて、<ruby>心臓<rt>しんぞう</rt></ruby>の<ruby>音<rt>おと</rt></ruby>を<ruby>確認<rt>かくにん</rt></ruby>した。", "The doctor placed a stethoscope on my chest and checked my heartbeat sound.", "診察（しんさつ: medical examination）"),
    ("親父ギャグ（おやじぎゃぐ）", "dad joke, corny pun", "<ruby>課長<rt>かちょう</rt></ruby>が<ruby>会議<rt>かいぎ</rt></ruby>で<ruby>親父<rt>おやじ</rt></ruby>ギャグを<ruby>言<rt>い</rt></ruby>って、<ruby>部屋<rt>へや</rt></ruby>がシーンと<ruby>静<rt>しず</rt></ruby>まり<ruby>返<rt>かえ</rt></ruby>った。", "The section manager told a dad joke during the meeting, and the room fell completely silent.", "ダジャレ（pun / wordplay）"),
    ("余命（よめい）", "life expectancy, remaining days/years of life", "<ruby>医師<rt>いし</rt></ruby>から<ruby>余命<rt>よめい</rt></ruby>３か<ruby>月<rt>げつ</rt></ruby>と<ruby>宣告<rt>せんこく</rt></ruby>されたが、<ruby>奇跡的<rt>きせきてき</rt></ruby>に<ruby>回復<rt>かいふく</rt></ruby>した。", "Although declared by the doctor to have a life expectancy of three months, he miraculously recovered.", "余命宣告（よめいせんこく: prognosis announcement）"),
    ("葬式（そうしき）", "funeral, funeral service", "<ruby>祖父<rt>そふ</rt></ruby>の<ruby>葬式<rt>そうしき</rt></ruby>に<ruby>参列<rt>さんれつ</rt></ruby>するため、<ruby>黒<rt>くろ</rt></ruby>いスーツを<ruby>着<rt>き</rt></ruby>て<ruby>出<rt>で</rt></ruby>かけた。", "To attend my grandfather's funeral, I put on a black suit and went out.", "お葬式（おそうしき）, 告別式（こくべつしき: memorial service）"),
    ("世代（せだい）", "generation", "<ruby>親<rt>おや</rt></ruby>の<ruby>世代<rt>せだい</rt></ruby>とわたしたちの<ruby>世代<rt>せだい</rt></ruby>では、<ruby>働<rt>はたら</rt></ruby>き<ruby>方<rt>かた</rt></ruby>に<ruby>対<rt>たい</rt></ruby>する<ruby>考<rt>かんが</rt></ruby>えが<ruby>異<rt>こと</rt></ruby>なる。", "Between our parents' generation and our generation, thoughts toward work styles differ.", "世代交代（せだいこうたい: shift of generations）, Z世代（Z generation）"),
    ("同世代（どうせだい）", "same generation, peer group", "<ruby>同世代<rt>どうせだい</rt></ruby>の<ruby>友達<rt>ともだち</rt></ruby>とは、<ruby>昔<rt>むかし</rt></ruby>のドラマやアニメの<ruby>話<rt>はな</rt></ruby>で盛り上がる。", "With friends of the same generation, we get excited talking about old TV dramas and anime.", "同年代（どうねんだい: same age group）, 同期（どうき: contemporaries）"),
    ("親しむ（したしむ）", "to be familiar with, to grow fond of, to enjoy", "<ruby>幼<rt>おさな</rt></ruby>いころから<ruby>読書<rt>どくしょ</rt></ruby>に<ruby>親<rt>した</rt></ruby>しんできたおかげで、<ruby>語彙力<rt>ごいりょく</rt></ruby>が<ruby>身<rt>み</rt></ruby>についた。", "Thanks to having grown fond of reading books since early childhood, I acquired vocabulary skills.", "親しむ vs 慣れる: 「慣れる」は習慣化・適応すること、「親しむ」は愛着を持って好ましく付き合うこと。"),
    ("親しみやすい（したしみやすい）", "friendly, approachable, easy to relate to", "<ruby>新<rt>あたら</rt></ruby>しい<ruby>先生<rt>せんせい</rt></ruby>はいつも<ruby>笑顔<rt>えがお</rt></ruby>で、とても<ruby>親<rt>した</rt></ruby>しみやすい<ruby>雰囲気<rt>ふんいき</rt></ruby>がある。", "The new teacher is always smiling and has a very approachable atmosphere.", "親しみやすい vs 話しかけやすい: どちらも好印象を与える性格・人柄を表す表現。"),
    ("読者（どくしゃ）", "reader, audience (of a book/article)", "その<ruby>小説家<rt>しょうせつか</rt></ruby>は、<ruby>読者<rt>どくしゃ</rt></ruby>からのファンレターを<ruby>大切<rt>たいせつ</rt></ruby>に<ruby>保管<rt>ほかん</rt></ruby>している。", "That novelist carefully keeps fan letters from readers.", "読者 vs 視聴者: 「読者」は本や記事の読み手、「視聴者」はテレビ・動画の観客・聞き手。"),
    ("視聴者（しちょうしゃ）", "viewer, audience (of TV/broadcast)", "<ruby>番組<rt>ばんぐみ</rt></ruby>の<ruby>最後<rt>さいご</rt></ruby>に、<ruby>視聴者<rt>しちょうしゃ</rt></ruby>へのプレゼントクイズが<ruby>出題<rt>しゅつだい</rt></ruby>された。", "At the end of the program, a giveaway quiz for viewers was presented.", "視聴者 vs 観客: 「観客（かんきゃく）」は現場・劇場の客、「視聴者」は画面・放送越しに見る人。"),
    ("視聴率（しちょうりつ）", "viewer ratings, viewership rating", "<ruby>昨日<rt>きのう</rt></ruby>のサッカー<ruby>決勝戦<rt>けっしょうせん</rt></ruby>は、<ruby>平均<rt>へいきん</rt></ruby><ruby>視聴率<rt>しちょうりつ</rt></ruby>が３０％を<ruby>超<rt>こ</rt></ruby>えた。", "Yesterday's soccer final match exceeded an average viewer rating of 30%.", "高視聴率（こうしちょうりつ: high ratings）"),
    ("一方（で）（いっぽう（で））", "on the other hand, meanwhile, whereas", "スマートフォンは<ruby>生活<rt>せいかつ</rt></ruby>を<ruby>便利<rt>べんり</rt></ruby>にする<ruby>一方<rt>いっぽう</rt></ruby>で、<ruby>睡眠<rt>すいみん</rt></ruby><ruby>不足<rt>ふそく</rt></ruby>の<ruby>原因<rt>げんいん</rt></ruby>にもなる。", "While smartphones make life convenient, on the other hand they also become a cause of lack of sleep.", "一方で vs 他方で: 2つの対比的な側面を述べるときに使う接続表現。"),
    ("登場人物（とうじょうじんぶつ）", "character (in a novel/movie), cast of characters", "このミステリー<ruby>小説<rt>しょうせつ</rt></ruby>は<ruby>登場人物<rt>とうじょうじんぶつ</rt></ruby>が<ruby>多<rt>おお</rt></ruby>いので、メモをしながら<ruby>読<rt>よ</rt></ruby>んでいる。", "Since this mystery novel has many characters, I am reading while taking notes.", "主人公（しゅじんこう: protagonist）, キャラクター"),
    ("一概には言えない（いちがいにはいえない）", "cannot generalize, not necessarily true across the board", "<ruby>高価<rt>こうか</rt></ruby>なものが<ruby>必<rt>かなら</rt></ruby>ずしも<ruby>良<rt>よ</rt></ruby>いとは、<ruby>一概<rt>いちがい</rt></ruby>には<ruby>言<rt>い</rt></ruby>えない。", "One cannot generalize and say that expensive things are necessarily good.", "「一概に〜ない」は個別事情や例外があるため一括りに断定できないことを表す定型表現。")
]

def main():
    print(f"Total words: {len(CARDS_RAW)}")
    cards = []
    card_ids = []
    tsv_lines = []

    for i, item in enumerate(CARDS_RAW, 1):
        col0, meaning_en, ex_ja, ex_en, related = item
        m = re.match(r'^(.*?)[（\(](.*?)[）\)]$', col0)
        if m:
            word = m.group(1).strip()
            reading = m.group(2).strip()
        else:
            word = col0
            reading = col0

        card_id = f"class_word_0028_{str(i).zfill(4)}"
        card_ids.append(card_id)

        card_obj = {
            "id": card_id,
            "word": word,
            "reading": reading,
            "category": "授業で習った言葉",
            "studentId": "0028",
            "meaning": {
                "en": meaning_en,
                "ja": word,
                "zh_TW": meaning_en,
                "zh_CN": meaning_en,
                "ko": meaning_en,
                "zh_HK": meaning_en,
                "fr": meaning_en
            },
            "example": {
                "ja": ex_ja,
                "en": ex_en,
                "zh_TW": ex_en,
                "zh_CN": ex_en,
                "ko": ex_en,
                "zh_HK": ex_en,
                "fr": ex_en
            },
            "related": related or f"{reading}（授業の重要表現）"
        }
        cards.append(card_obj)
        tsv_lines.append(f"{col0}\t{meaning_en}\t{ex_ja}\t{ex_en}\t{related}")

    # 1. Update auth.js and public/auth.js
    auth_paths = [
        os.path.join(REPO_ROOT, 'auth.js'),
        os.path.join(REPO_ROOT, 'public/auth.js')
    ]
    for ap in auth_paths:
        with open(ap, 'r', encoding='utf-8') as f:
            auth_text = f.read()
        if '"0028"' not in auth_text:
            auth_text = auth_text.replace(
                '{ id: "0027", name: "生徒27", lang: "en", passcode: "1122" }',
                '{ id: "0027", name: "生徒27", lang: "en", passcode: "1122" },\n    { id: "0028", name: "生徒28", lang: "en", passcode: "2233" }'
            )
            with open(ap, 'w', encoding='utf-8') as f:
                f.write(auth_text)
            print(f"Updated student 0028 in {ap}")

    # 2. Update js/app.js and public/js/app.js
    app_paths = [
        os.path.join(REPO_ROOT, 'js/app.js'),
        os.path.join(REPO_ROOT, 'public/js/app.js')
    ]
    for ap in app_paths:
        with open(ap, 'r', encoding='utf-8') as f:
            app_text = f.read()
        # MASTER_STUDENT_PASSCODES
        if "'0028': '2233'" not in app_text:
            app_text = app_text.replace(
                "'0027': '1122'",
                "'0027': '1122',\n    '0028': '2233'"
            )
        # studentCardIds hook
        if "if (stId === '0028')" not in app_text:
            app_text = app_text.replace(
                "if (stId === '0027') {",
                """if (stId === '0028') {
          const ids0028 = window.CLASS_0028_IDS || [];
          ids0028.forEach(cId => studentCardIds.add(cId));
        }
        if (stId === '0027') {"""
            )
        with open(ap, 'w', encoding='utf-8') as f:
            f.write(app_text)
        print(f"Updated app hooks in {ap}")

    # 3. Update database/class_vocab_data.js and public/database/class_vocab_data.js
    cv_paths = [
        os.path.join(REPO_ROOT, 'database/class_vocab_data.js'),
        os.path.join(REPO_ROOT, 'public/database/class_vocab_data.js')
    ]
    for cp in cv_paths:
        with open(cp, 'r', encoding='utf-8') as f:
            cv_text = f.read()

        # Remove previous 0028 if any
        if 'class_word_0028_0001' in cv_text:
            cv_text = re.sub(r',\s*// --- Student 0028 Curated Cards.*?window\.CLASS_0028_IDS\s*=\s*\[[^\]]+\];\n?', '', cv_text, flags=re.DOTALL)

        cards_js_lines = []
        for c in cards:
            cards_js_lines.append("  " + json.dumps(c, ensure_ascii=False, indent=2).replace("\n", "\n  ") + ",")
        cards_block = "\n" + "\n".join(cards_js_lines)

        pos = cv_text.rfind('];\n\nwindow.CLASS_ARUN_IDS')
        if pos == -1:
            pos = cv_text.rfind('];\nwindow.CLASS_ARUN_IDS')
        if pos == -1:
            pos = cv_text.rfind('];')

        injection = f",\n  // --- Student 0028 Curated Cards ({len(cards)} words) ---{cards_block}\n"
        cv_text = cv_text[:pos] + injection + cv_text[pos:]

        ids_js = f"\nwindow.CLASS_0028_IDS = {json.dumps(card_ids)};\n"
        cv_text += ids_js

        with open(cp, 'w', encoding='utf-8') as f:
            f.write(cv_text)
        print(f"Updated {cp} successfully!")

    # Save TSV file to /tmp/student_0028_tsv.txt
    with open('/tmp/student_0028_tsv.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(tsv_lines))
    print(f"Saved TSV to /tmp/student_0028_tsv.txt ({len(tsv_lines)} rows)")

if __name__ == '__main__':
    main()
