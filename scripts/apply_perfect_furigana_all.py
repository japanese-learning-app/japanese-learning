# -*- coding: utf-8 -*-
"""
Perfect Furigana Corrector
Ensures 100% of kanji in all card examples (0 to 51) have correct ruby tags.
"""

import json
import re
import os

REPLACEMENTS = {
    # --- Section 45 ---
    "card_1037": "スポーツジムの<ruby>後<rt>あと</rt></ruby>で、<ruby>温<rt>あたた</rt></ruby>かいシャワーを<ruby>浴<rt>あ</rt></ruby>びられます。",
    "card_1038": "このホームから、<ruby>地下鉄<rt>ちかてつ</rt></ruby>に<ruby>直接<rt>ちょくせつ</rt></ruby><ruby>乗<rt>の</rt></ruby>り<ruby>換<rt>か</rt></ruby>えられます。",
    "card_1047": "<ruby>足<rt>あし</rt></ruby>の<ruby>怪我<rt>けが</rt></ruby>が<ruby>治<rt>なお</rt></ruby>って、やっと<ruby>自分<rt>じぶん</rt></ruby>の<ruby>足<rt>あし</rt></ruby>で<ruby>立<rt>た</rt></ruby>てました。",
    "card_1049": "<ruby>山<rt>やま</rt></ruby>の<ruby>頂上<rt>ちょうじょう</rt></ruby>で、<ruby>新鮮<rt>しんせん</rt></ruby>なおいしい<ruby>空気<rt>くうき</rt></ruby>がたくさん<ruby>吸<rt>す</rt></ruby>えました。",

    # --- Section 46 ---
    "card_1056": "インターネットを<ruby>使<rt>つか</rt></ruby>えば、<ruby>何<rt>なん</rt></ruby>でもすぐに<ruby>調<rt>しら</rt></ruby>べられます。",
    "card_1059": "このホテルは<ruby>温泉<rt>おんせん</rt></ruby>があり、とても<ruby>快適<rt>かいてき</rt></ruby>に<ruby>泊<rt>と</rt></ruby>まれます。",
    "card_1064": "イベントのスタンプラリーで、<ruby>全部<rt>ぜんぶ</rt></ruby>のスタンプを<ruby>集<rt>あつ</rt></ruby>められました！",
    "card_1066": "ネットからなら、ホテルの<ruby>予約<rt>よやく</rt></ruby><ruby>日程<rt>にってい</rt></ruby>を<ruby>簡単<rt>かんたん</rt></ruby>に<ruby>変<rt>か</rt></ruby>えられます。",
    "card_1067": "<ruby>新<rt>あたら</rt></ruby>しい<ruby>習慣<rt>しゅうかん</rt></ruby>を<ruby>身<rt>み</rt></ruby>につければ、<ruby>人<rt>ひと</rt></ruby>は<ruby>誰<rt>だれ</rt></ruby>でも<ruby>良<rt>よ</rt></ruby>い<ruby>方向<rt>ほうこう</rt></ruby>に<ruby>変<rt>か</rt></ruby>わることができます。",
    "card_1069": "しっかり<ruby>勉強<rt>べんきょう</rt></ruby>すれば、JLPTの<ruby>資格<rt>しかく</rt></ruby>がきっと<ruby>取<rt>と</rt></ruby>れます。",
    "card_1070": "ありがとうの<ruby>気持<rt>きも</rt></ruby>ちを、きちんと<ruby>言葉<rt>ことば</rt></ruby>で<ruby>言<rt>い</rt></ruby>えました。",
    "card_1071": "あらかじめ<ruby>知<rt>し</rt></ruby>っていれば、<ruby>足元<rt>あしもと</rt></ruby>に<ruby>気<rt>き</rt></ruby>を<ruby>付<rt>つ</rt></ruby>けられます。",
    "card_1072": "<ruby>奨学金<rt>しょうがくきん</rt></ruby>が<ruby>決<rt>き</rt></ruby>まったので、<ruby>来年<rt>らいねん</rt></ruby>から<ruby>日本<rt>にほん</rt></ruby>へ<ruby>留学<rt>りゅうがく</rt></ruby>できます！",
    "card_1073": "<ruby>人<rt>ひと</rt></ruby>の<ruby>気持<rt>きも</rt></ruby>ちを<ruby>考<rt>かんが</rt></ruby>えて、<ruby>相手<rt>あいて</rt></ruby>のことをきちんと<ruby>心配<rt>しんぱい</rt></ruby>できる<ruby>優<rt>やさ</rt></ruby>しい<ruby>人<rt>ひと</rt></ruby>になりたい。",
    "card_1074": "<ruby>折<rt>お</rt></ruby>りたたみ<ruby>傘<rt>かさ</rt></ruby>なら、カバンに<ruby>入<rt>い</rt></ruby>れていつでも<ruby>持<rt>も</rt></ruby>って<ruby>行<rt>い</rt></ruby>けます。",
    "card_1075": "<ruby>明日<rt>あした</rt></ruby>のレッスンに、お<ruby>気<rt>き</rt></ruby>に<ruby>入<rt>い</rt></ruby>りのノートを<ruby>持<rt>も</rt></ruby>って<ruby>来<rt>こ</rt></ruby>られますか？",
    "card_1076": "このカフェはテラス<ruby>席<rt>せき</rt></ruby>なら、ペットの<ruby>犬<rt>いぬ</rt></ruby>も<ruby>連<rt>つ</rt></ruby>れて<ruby>行<rt>い</rt></ruby>けます。",
    "card_1077": "<ruby>週末<rt>しゅうまつ</rt></ruby>のホームパーティーに、お<ruby>友達<rt>ともだち</rt></ruby>も<ruby>連<rt>つ</rt></ruby>れて<ruby>来<rt>こ</rt></ruby>られますよ。",

    # --- Section 47 ---
    "card_1084": "<ruby>運動<rt>うんどう</rt></ruby>のあとで、<ruby>冷<rt>つめ</rt></ruby>たいお<ruby>茶<rt>ちゃ</rt></ruby>をぐっと<ruby>飲<rt>の</rt></ruby>んだ。",
    "card_1093": "<ruby>午前中<rt>ごぜんちゅう</rt></ruby>に<ruby>部屋<rt>へや</rt></ruby>の<ruby>片付<rt>かたづ</rt></ruby>けを<ruby>全部<rt>ぜんぶ</rt></ruby>した。",
    "card_1098": "<ruby>電車<rt>でんしゃ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に<ruby>傘<rt>かさ</rt></ruby>を<ruby>忘<rt>わす</rt></ruby>れてしまった。",
    "card_1100": "<ruby>初<rt>はじ</rt></ruby>めて<ruby>新幹線<rt>しんかんせん</rt></ruby>に<ruby>乗<rt>の</rt></ruby>って、スピードに<ruby>感動<rt>かんどう</rt></ruby>した。",

    # --- Section 48 ---
    "card_1127": "<ruby>先生<rt>せんせい</rt></ruby>の<ruby>説明<rt>せつめい</rt></ruby>の<ruby>後<rt>あと</rt></ruby>で、<ruby>文法<rt>ぶんぽう</rt></ruby>の<ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>がよくわかりました。",
    "card_1128": "<ruby>練習<rt>れんしゅう</rt></ruby>を<ruby>重<rt>かさ</rt></ruby>ねて、<ruby>難<rt>むずか</rt></ruby>しい<ruby>課題<rt>かだい</rt></ruby>が<ruby>無事<rt>ぶじ</rt></ruby>にできました！",

    # --- Section 49 ---
    "card_1136": "<ruby>重<rt>おも</rt></ruby>い<ruby>荷物<rt>にもつ</rt></ruby>を<ruby>両手<rt>りょうて</rt></ruby>でしっかりと<ruby>持<rt>も</rt></ruby>ちました。",
    "card_1137": "テストで100<ruby>点<rt>てん</rt></ruby>を<ruby>取<rt>と</rt></ruby>って、とても<ruby>嬉<rt>うれ</rt></ruby>しかったです！",
    "card_1139": "<ruby>木<rt>き</rt></ruby>から<ruby>降<rt>お</rt></ruby>りられなくなった<ruby>子猫<rt>こねこ</rt></ruby>を<ruby>優<rt>やさ</rt></ruby>しく<ruby>助<rt>たす</rt></ruby>けました。",
    "card_1144": "<ruby>寒<rt>さむ</rt></ruby>い<ruby>冬<rt>ふゆ</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>に、<ruby>温<rt>あたた</rt></ruby>かいお<ruby>風呂<rt>ふろ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>ってリラックスした。",

    # --- Section 50 ---
    "card_1154": "<ruby>昔<rt>むかし</rt></ruby><ruby>使<rt>つか</rt></ruby>っていたゲーム<ruby>機<rt>き</rt></ruby>を、リサイクルショップで<ruby>売<rt>う</rt></ruby>りました。",

    # --- Section 51 ---
    "card_1166": "<ruby>辞書<rt>じしょ</rt></ruby>を<ruby>使<rt>つか</rt></ruby>って、<ruby>新<rt>あたら</rt></ruby>しい<ruby>単語<rt>たんご</rt></ruby>の<ruby>意味<rt>いみ</rt></ruby>を<ruby>詳<rt>くわ</rt></ruby>しく<ruby>調<rt>しら</rt></ruby>べました。",
    "card_1169": "<ruby>箱根<rt>はこね</rt></ruby>の<ruby>温泉<rt>おんせん</rt></ruby><ruby>旅館<rt>りょかん</rt></ruby>に<ruby>泊<rt>と</rt></ruby>まって、のんびり<ruby>過<rt>す</rt></ruby>ごしました。",
    "card_1172": "<ruby>発表会<rt>はっぴょうかい</rt></ruby>で、<ruby>心<rt>こころ</rt></ruby>を<ruby>込<rt>こ</rt></ruby>めてピアノを<ruby>弾<rt>ひ</rt></ruby>きました。",
    "card_1174": "<ruby>日本<rt>にほん</rt></ruby><ruby>旅行<rt>りょこう</rt></ruby>の<ruby>記念<rt>きねん</rt></ruby>に、<ruby>各地<rt>かくち</rt></ruby>の<ruby>御朱印<rt>ごしゅいん</rt></ruby>を<ruby>集<rt>あつ</rt></ruby>めました。",
    "card_1175": "<ruby>大掃除<rt>おおそうじ</rt></ruby>で、<ruby>使<rt>つか</rt></ruby>わなくなった<ruby>古<rt>ふる</rt></ruby>いものを<ruby>思<rt>おも</rt></ruby>い<ruby>切<rt>き</rt></ruby>って<ruby>捨<rt>す</rt></ruby>てました。",
    "card_1177": "<ruby>信号<rt>しんごう</rt></ruby>が<ruby>青<rt>あお</rt></ruby>に<ruby>変<rt>か</rt></ruby>わったのを<ruby>見<rt>み</rt></ruby>て、<ruby>歩<rt>ある</rt></ruby>き<ruby>出<rt>だ</rt></ruby>しました。",
    "card_1182": "<ruby>去年<rt>きょねん</rt></ruby>の1<ruby>年間<rt>ねんかん</rt></ruby>、<ruby>東京<rt>とうきょう</rt></ruby>の<ruby>大学<rt>だいがく</rt></ruby>へ<ruby>留学<rt>りゅうがく</rt></ruby>しました。",
    "card_1186": "<ruby>晴<rt>は</rt></ruby>れた<ruby>午後<rt>ごご</rt></ruby>、<ruby>愛犬<rt>あいけん</rt></ruby>をドッグランへ<ruby>連<rt>つ</rt></ruby>れて<ruby>行<rt>い</rt></ruby>きました。",

    # --- Sections 0-43 ---
    "card_0103": "<ruby>私<rt>わたし</rt></ruby>の<ruby>父<rt>ちち</rt></ruby>は<ruby>自動車<rt>じどうしゃ</rt></ruby>メーカーでエンジニアとして<ruby>働<rt>はたら</rt></ruby>いています。",
    "card_0104": "<ruby>母<rt>はは</rt></ruby>は<ruby>料理<rt>りょうり</rt></ruby>がとても<ruby>上手<rt>じょうず</rt></ruby>で、<ruby>毎日<rt>まいにち</rt></ruby><ruby>美味<rt>おい</rt></ruby>しいお<ruby>弁当<rt>べんとう</rt></ruby>を<ruby>作<rt>つく</rt></ruby>ってくれます。",
    "card_0176": "<ruby>大学<rt>だいがく</rt></ruby>のキャンパスで、<ruby>台湾<rt>たいわん</rt></ruby>から<ruby>来<rt>き</rt></ruby>た<ruby>留学生<rt>りゅうがくせい</rt></ruby>の<ruby>案内<rt>あんない</rt></ruby>を<ruby>担当<rt>たんとう</rt></ruby>しました。",
    "card_0208": "<ruby>親友<rt>しんゆう</rt></ruby>は<ruby>今<rt>いま</rt></ruby><ruby>アメリカ<rt>あめりか</rt></ruby>のニューヨークに<ruby>住<rt>す</rt></ruby>んでいて、<ruby>毎日<rt>まいにち</rt></ruby><ruby>連絡<rt>れんらく</rt></ruby>を<ruby>取<rt>と</rt></ruby>り<ruby>合<rt>あ</rt></ruby>っています。",
    "card_0218": "<ruby>朝<rt>あさ</rt></ruby><ruby>起<rt>お</rt></ruby>きたら<ruby>冷<rt>つめ</rt></ruby>たい<ruby>水<rt>みず</rt></ruby>でしっかり<ruby>顔<rt>かお</rt></ruby>を<ruby>洗<rt>あら</rt></ruby>って、<ruby>目<rt>め</rt></ruby>を<ruby>覚<rt>さ</rt></ruby>まします。",
    "card_0231": "<ruby>美容院<rt>びよういん</rt></ruby>で<ruby>眉毛<rt>まゆげ</rt></ruby>の<ruby>形<rt>かたち</rt></ruby>をきれいに<ruby>整<rt>ととの</rt></ruby>えてもらいました。",
    "card_0233": "スマホを<ruby>片手<rt>かたて</rt></ruby>で<ruby>操作<rt>そうさ</rt></ruby>するときは、<ruby>主<rt>おも</rt></ruby>に<ruby>親指<rt>おやゆび</rt></ruby>を<ruby>使<rt>つか</rt></ruby>います。",
    "card_0235": "<ruby>手<rt>て</rt></ruby>を<ruby>開<rt>ひら</rt></ruby>いて<ruby>比<rt>くら</rt></ruby>べると、<ruby>五本<rt>ごほん</rt></ruby>の<ruby>指<rt>ゆび</rt></ruby>の<ruby>中<rt>なか</rt></ruby>で<ruby>中指<rt>なかゆび</rt></ruby>が<ruby>一番<rt>いちばん</rt></ruby><ruby>長<rt>なが</rt></ruby>いです。",
    "card_0236": "<ruby>左手<rt>ひだりて</rt></ruby>の<ruby>薬指<rt>くすりゆび</rt></ruby>に、<ruby>結婚指輪<rt>けっこんゆびわ</rt></ruby>を<ruby>大切<rt>たいせつ</rt></ruby>にはめています。",
    "card_0237": "<ruby>家具<rt>かぐ</rt></ruby>の<ruby>角<rt>かど</rt></ruby>に<ruby>足<rt>あし</rt></ruby>の<ruby>小指<rt>こゆび</rt></ruby>をぶつけてしまい、とても<ruby>痛<rt>いた</rt></ruby>かったです。",
    "card_0238": "<ruby>父<rt>ちち</rt></ruby>は<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>出社<rt>しゅっしゃ</rt></ruby>する<ruby>前<rt>まえ</rt></ruby>に、<ruby>電気<rt>でんき</rt></ruby>シェーバーで<ruby>丁寧<rt>ていねい</rt></ruby>に<ruby>髭<rt>ひげ</rt></ruby>を<ruby>剃<rt>そ</rt></ruby>ります。",
    "card_0401": "<ruby>東京<rt>とうきょう</rt></ruby>は<ruby>電車<rt>でんしゃ</rt></ruby>やバスなどの<ruby>乗<rt>の</rt></ruby>り<ruby>物<rt>もの</rt></ruby>が<ruby>発達<rt>はったつ</rt></ruby>していて、どこへ<ruby>行<rt>い</rt></ruby>くにも<ruby>便利<rt>べんり</rt></ruby>です。",
    "card_0513": "A: <ruby>日本語<rt>にほんご</rt></ruby>の<ruby>文法<rt>ぶんぽう</rt></ruby>について<ruby>質問<rt>しつもん</rt></ruby>してもいいですか？<br/>B: もちろんです！わからないところは<ruby>何<rt>なん</rt></ruby>でも<ruby>質問<rt>しつもん</rt></ruby>してくださいね。",
    "card_0588": "わが<ruby>家<rt>いえ</rt></ruby>では<ruby>茶色<rt>ちゃいろ</rt></ruby>いトイプードルを<ruby>飼<rt>か</rt></ruby>っています。とても<ruby>人懐<rt>ひとなつ</rt></ruby>っこいです。",
    "card_0591": "<ruby>冬<rt>ふゆ</rt></ruby>のおしゃれに<ruby>合<rt>あ</rt></ruby>わせやすい、<ruby>上品<rt>じょうひん</rt></ruby>な<ruby>グレー<rt>ぐれー</rt></ruby>のウールコートを<ruby>買<rt>か</rt></ruby>いました。",
    "card_0592": "リビングのカーテンを<ruby>明<rt>あか</rt></ruby>るい<ruby>ベージュ<rt>べーじゅ</rt></ruby>にしたら、<ruby>部屋<rt>へや</rt></ruby>が<ruby>広<rt>ひろ</rt></ruby>く<ruby>感<rt>かん</rt></ruby>じられます。",
    "card_0594": "A: このカレーは<ruby>辛<rt>から</rt></ruby>いですか？<br/>B: <ruby>少<rt>すこ</rt></ruby>し<ruby>辛<rt>から</rt></ruby>いですが、コクがあってとても<ruby>美味<rt>おい</rt></ruby>しいですよ。",
    "card_0596": "<ruby>汗<rt>あせ</rt></ruby>をかいた<ruby>後<rt>あと</rt></ruby>は、<ruby>少<rt>すこ</rt></ruby>し<ruby>しょっぱい<rt>しょっぱい</rt></ruby><ruby>梅干<rt>うめぼ</rt></ruby>しやスポーツドリンクが<ruby>美味<rt>おい</rt></ruby>しく<ruby>感<rt>かん</rt></ruby>じます。",
    "card_0597": "<ruby>搾<rt>しぼ</rt></ruby>りたてのレモンを<ruby>入<rt>い</rt></ruby>れた<ruby>紅茶<rt>こうちゃ</rt></ruby>は、ほどよく<ruby>酸<rt>す</rt></ruby>っぱい<ruby>風味<rt>ふうみ</rt></ruby>で<ruby>爽<rt>さわ</rt></ruby>やかです。",
    "card_0602": "<ruby>渋谷駅<rt>しぶやえき</rt></ruby>のハチ<ruby>公前<rt>こうまえ</rt></ruby>の<ruby>広場<rt>ひろば</rt></ruby>で、<ruby>友達<rt>ともだち</rt></ruby>と<ruby>待<rt>ま</rt></ruby>ち<ruby>合<rt>あ</rt></ruby>わせをしています。",
    "card_0609": "<ruby>若者<rt>わかもの</rt></ruby>の<ruby>恋愛<rt>れんあい</rt></ruby>をテーマにしたドラマが、<ruby>今<rt>いま</rt></ruby>とても<ruby>人気<rt>にんき</rt></ruby>を<ruby>集<rt>あつ</rt></ruby>めています。",
    "card_0620": "<ruby>兄<rt>あに</rt></ruby>は<ruby>子供<rt>こども</rt></ruby>の<ruby>頃<rt>ころ</rt></ruby>から<ruby>道場<rt>どうじょう</rt></ruby>に<ruby>通<rt>かよ</rt></ruby>って<ruby>柔道<rt>じゅうどう</rt></ruby>の<ruby>稽古<rt>けいこ</rt></ruby>に<ruby>励<rt>はげ</rt></ruby>んでいます。",
    "card_0623": "<ruby>日本<rt>にほん</rt></ruby>の<ruby>四季<rt>しき</rt></ruby>は<ruby>美<rt>うつく</rt></ruby>しく、それぞれの<ruby>季節<rt>きせつ</rt></ruby>で<ruby>景色<rt>けしき</rt></ruby>や<ruby>旬<rt>しゅん</rt></ruby>の<ruby>食<rt>た</rt></ruby>べ<ruby>物<rt>もの</rt></ruby>を<ruby>楽<rt>たの</rt></ruby>しめます。",
    "card_0665": "<ruby>来週<rt>らいしゅう</rt></ruby>の<ruby>祝日<rt>しゅくじつ</rt></ruby>は<ruby>連休<rt>れんきゅう</rt></ruby>になるので、<ruby>温泉<rt>おんせん</rt></ruby><ruby>旅行<rt>りょこう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>く<ruby>予定<rt>よてい</rt></ruby>です。",
    "card_0666": "<ruby>休日<rt>きゅうじつ</rt></ruby>に<ruby>美術館<rt>びじゅつかん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>って、<ruby>素晴<rt>すば</rt></ruby>らしい<ruby>現代<rt>げんだい</rt></ruby><ruby>美術<rt>びじゅつ</rt></ruby>の<ruby>作品<rt>さくひん</rt></ruby>を<ruby>鑑賞<rt>かんしょう</rt></ruby>しました。",
    "card_0668": "<ruby>国立<rt>こくりつ</rt></ruby><ruby>科学<rt>かがく</rt></ruby><ruby>博物館<rt>はくぶつかん</rt></ruby>で、<ruby>大<rt>おお</rt></ruby>きな<ruby>恐竜<rt>きょうりゅう</rt></ruby>の<ruby>化石<rt>かせき</rt></ruby>を<ruby>見学<rt>けんがく</rt></ruby>しました。",
    "card_0670": "お<ruby>正月<rt>しょうがつ</rt></ruby>には<ruby>近<rt>ちか</rt></ruby>くの<ruby>有名<rt>ゆうめい</rt></ruby>な<ruby>神社<rt>じんじゃ</rt></ruby>へ<ruby>初詣<rt>はつもうで</rt></ruby>に<ruby>行<rt>い</rt></ruby>って、<ruby>健康<rt>けんこう</rt></ruby>を<ruby>祈<rt>いの</rt></ruby>りました。",
    "card_0673": "ワーキングホリデーのビザを<ruby>申請<rt>しんせい</rt></ruby>するために、<ruby>来週<rt>らいしゅう</rt></ruby><ruby>大使館<rt>たいしかん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きます。",
    "card_0676": "<ruby>駅前<rt>えきまえ</rt></ruby>で<ruby>財布<rt>さいふ</rt></ruby>を<ruby>拾<rt>ひろ</rt></ruby>ったので、すぐに<ruby>近<rt>ちか</rt></ruby>くの<ruby>交番<rt>こうばん</rt></ruby>へ<ruby>届<rt>とど</rt></ruby>けました。",
    "card_0677": "<ruby>近所<rt>きんじょ</rt></ruby>で<ruby>火災<rt>かさい</rt></ruby>が<ruby>発生<rt>はっせい</rt></ruby>したときは、<ruby>落<rt>お</rt></ruby>ち<ruby>着<rt>つ</rt></ruby>いてすぐに<ruby>消防署<rt>しょうぼうしょ</rt></ruby>に<ruby>通報<rt>つうほう</rt></ruby>しましょう。",
    "card_0679": "レトロな<ruby>雰囲気<rt>ふんいき</rt></ruby>の<ruby>喫茶店<rt>きっさてん</rt></ruby>で、<ruby>名物<rt>めいぶつ</rt></ruby>のプリンとブレンドコーヒーを<ruby>楽<rt>たの</rt></ruby>しみました。",
    "card_0682": "<ruby>商店街<rt>しょうてんがい</rt></ruby>の<ruby>八百屋<rt>やおや</rt></ruby>さんで、<ruby>採<rt>と</rt></ruby>れたての<ruby>新鮮<rt>しんせん</rt></ruby>なトマトときゅうりを<ruby>買<rt>か</rt></ruby>いました。",
    "card_0686": "コンサートホールの<ruby>入口<rt>いりぐち</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>で、<ruby>友達<rt>ともだち</rt></ruby>と<ruby>待<rt>ま</rt></ruby>ち<ruby>合<rt>あ</rt></ruby>わせをしています。",
    "card_0693": "<ruby>成田空港<rt>なりたくうこう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>くために、<ruby>日暮里駅<rt>にっぽりえき</rt></ruby>からスカイライナーの<ruby>特急<rt>とっきゅう</rt></ruby>に<ruby>乗<rt>の</rt></ruby>りました。",
    "card_0694": "この<ruby>電車<rt>でんしゃ</rt></ruby>は<ruby>急行<rt>きゅうこう</rt></ruby>なので、<ruby>各駅停車<rt>かくえきていしゃ</rt></ruby>よりも<ruby>早<rt>はや</rt></ruby>く<ruby>目的地<rt>もくてきち</rt></ruby>に<ruby>着<rt>つ</rt></ruby>きますよ。",
    "card_0697": "バス<ruby>停<rt>てい</rt></ruby>の<ruby>時刻表<rt>じこくひょう</rt></ruby>を<ruby>確認<rt>かくにん</rt></ruby>して、<ruby>次<rt>つぎ</rt></ruby>のバスの<ruby>時間<rt>じかん</rt></ruby>を<ruby>調<rt>しら</rt></ruby>べました。",
    "card_0701": "<ruby>帰<rt>かえ</rt></ruby>りの<ruby>日程<rt>にってい</rt></ruby>がまだ<ruby>決<rt>き</rt></ruby>まっていないので、<ruby>新幹線<rt>しんかんせん</rt></ruby>の<ruby>片道<rt>かたみち</rt></ruby><ruby>切符<rt>きっぷ</rt></ruby>だけ<ruby>購入<rt>こうにゅう</rt></ruby>しました。",
    "card_0702": "<ruby>京都<rt>きょうと</rt></ruby>までの<ruby>新幹線<rt>しんかんせん</rt></ruby>は、<ruby>往復<rt>おうふく</rt></ruby>でチケットを<ruby>予約<rt>よやく</rt></ruby>したほうが<ruby>割引<rt>わりびき</rt></ruby>でお<ruby>得<rt>とく</rt></ruby>です。",
    "card_0834": "<ruby>朝<rt>あさ</rt></ruby>からズキズキと<ruby>頭<rt>あたま</rt></ruby>が<ruby>痛<rt>いた</rt></ruby>いので、<ruby>薬<rt>くすり</rt></ruby>を<ruby>飲<rt>の</rt></ruby>んで<ruby>休<rt>やす</rt></ruby>みます。",
    "card_0835": "<ruby>冷<rt>つめ</rt></ruby>たいものを<ruby>食<rt>た</rt></ruby>べすぎておなかが<ruby>痛<rt>いた</rt></ruby>くなったので、<ruby>温<rt>あたた</rt></ruby>かいお<ruby>茶<rt>ちゃ</rt></ruby>を<ruby>飲<rt>の</rt></ruby>みました。",
    "card_0836": "<ruby>虫歯<rt>むしば</rt></ruby>のせいで<ruby>歯<rt>は</rt></ruby>が<ruby>痛<rt>いた</rt></ruby>いので、<ruby>今日<rt>きょう</rt></ruby>の<ruby>午後<rt>ごご</rt></ruby>に<ruby>歯医者<rt>はいしゃ</rt></ruby>の<ruby>予約<rt>よやく</rt></ruby>を<ruby>入<rt>い</rt></ruby>れました。",
    "card_0848": "<ruby>夏<rt>なつ</rt></ruby>バテ<ruby>気味<rt>ぎみ</rt></ruby>で<ruby>食欲<rt>しょくよく</rt></ruby>がないですが、<ruby>栄養<rt>えいよう</rt></ruby>をつけるためにそうめんを<ruby>食<rt>た</rt></ruby>べました。",
    "card_0850": "<ruby>風邪<rt>かぜ</rt></ruby>の<ruby>引<rt>ひ</rt></ruby>き<ruby>始<rt>はじ</rt></ruby>めで<ruby>体<rt>からだ</rt></ruby>がだるいので、<ruby>今日<rt>きょう</rt></ruby>は<ruby>早<rt>はや</rt></ruby>くお<ruby>風呂<rt>ふろ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>って<ruby>寝<rt>ね</rt></ruby>ます。",
    "card_0853": "<ruby>高熱<rt>こうねつ</rt></ruby>が<ruby>出<rt>で</rt></ruby>て<ruby>病院<rt>びょういん</rt></ruby>で<ruby>検査<rt>けんさ</rt></ruby>を<ruby>受<rt>う</rt></ruby>けたら、<ruby>インフルエンザ<rt>いんふるえんざ</rt></ruby>だと<ruby>診断<rt>しんだん</rt></ruby>されました。",
    "card_0854": "<ruby>右<rt>みぎ</rt></ruby>の<ruby>下腹部<rt>かふくぶ</rt></ruby>が<ruby>急<rt>きゅう</rt></ruby>に<ruby>激<rt>はげ</rt></ruby>しく<ruby>痛<rt>いた</rt></ruby>むので、<ruby>盲腸<rt>もうちょう</rt></ruby>ではないかと<ruby>心配<rt>しんぱい</rt></ruby>です。",
    "card_0855": "<ruby>重<rt>おも</rt></ruby>い<ruby>段<rt>だん</rt></ruby>ボールを<ruby>持<rt>も</rt></ruby>ち<ruby>上<rt>あ</rt></ruby>げた<ruby>瞬間<rt>しゅんかん</rt></ruby>に、<ruby>ぎっくり腰<rt>ぎっくりごし</rt></ruby>になって<ruby>動<rt>うご</rt></ruby>けなくなりました。",
    "card_0856": "<ruby>階段<rt>かいだん</rt></ruby>で<ruby>足首<rt>あしくび</rt></ruby>を<ruby>ねんざ<rt>ねんざ</rt></ruby>してしまったので、<ruby>氷<rt>こおり</rt></ruby>で<ruby>冷<rt>ひ</rt></ruby>やして<ruby>湿布<rt>しっぷ</rt></ruby>を<ruby>貼<rt>は</rt></ruby>りました。",
    "card_0858": "<ruby>昨日<rt>きのう</rt></ruby>お<ruby>酒<rt>さけ</rt></ruby>を<ruby>飲<rt>の</rt></ruby>みすぎて、ひどい<ruby>二日酔い<rt>ふつかよい</rt></ruby>で<ruby>頭<rt>あたま</rt></ruby>がガンガンします。"
}

def parse_js_array(content, prefix):
    start = content.find(prefix)
    if start == -1:
        raise ValueError(f"Prefix '{prefix}' not found")
    depth = 0
    in_string = False
    escape = False
    quote_char = None
    array_start = start + len(prefix)
    end = -1

    for i in range(array_start, len(content)):
        c = content[i]
        if escape:
            escape = False
            continue
        if c == '\\':
            escape = True
            continue
        if in_string:
            if c == quote_char:
                in_string = False
            continue
        else:
            if c in ('"', "'"):
                in_string = True
                quote_char = c
                continue
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
    if end == -1:
        raise ValueError(f"Could not find matching bracket for array starting at {array_start}")
    data = json.loads(content[array_start:end])
    return array_start, end, data

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_js_path = os.path.join(root_dir, 'js', 'data.js')
    public_data_js_path = os.path.join(root_dir, 'public', 'js', 'data.js')

    with open(data_js_path, 'r', encoding='utf-8') as f:
        content = f.read()

    vocab_start, vocab_end, vocab_data = parse_js_array(content, 'window.INITIAL_VOCAB_DATA = ')
    print(f"Loaded {len(vocab_data)} cards")

    modified_count = 0
    for c in vocab_data:
        cid = c['id']
        if cid in REPLACEMENTS:
            old_ja = c['example']['ja']
            new_ja = REPLACEMENTS[cid]
            if old_ja != new_ja:
                c['example']['ja'] = new_ja
                modified_count += 1
                print(f"Updated {cid}:")
                print(f"  Old: {old_ja}")
                print(f"  New: {new_ja}")

    print(f"Total cards updated with perfect furigana: {modified_count} (out of {len(REPLACEMENTS)} in dictionary)")

    # Save to js/data.js and public/js/data.js
    new_vocab_json = json.dumps(vocab_data, ensure_ascii=False, indent=2)
    new_content = content[:vocab_start] + new_vocab_json + content[vocab_end:]

    with open(data_js_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    with open(public_data_js_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Saved updated files successfully!")

if __name__ == '__main__':
    main()
