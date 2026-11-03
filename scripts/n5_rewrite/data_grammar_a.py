# -*- coding: utf-8 -*-
"""
N5 grammar textbook details + practice questions, gids 1-23 (hand-authored).
Format: see build_grammar.py docstring.

Shorthand: in Japanese detail strings the words ます形 / て形 / ない形 / た形 / 辞書形 / 普通形 are
auto-converted by J() at the bottom of the file into R()-friendly explicit ruby ({形|けい} etc.).
"""

GRAMMAR = {}

# ---------------------------------------------------------------- 1 です／だ
GRAMMAR[1] = dict(
    name="です／だ", reading="です／だ",
    meaning_en="to be (copula): です polite / だ plain",
    similar="ではありません、でした",
    details=dict(
        formula="<strong>名詞</strong>／<strong>ナ形容詞</strong> ＋ <strong>です</strong>（丁寧）<br>"
                "<strong>名詞</strong>／<strong>ナ形容詞</strong> ＋ <strong>だ</strong>（普通形）<br>"
                "<strong>イ形容詞</strong> ＋ <strong>です</strong>（丁寧にするだけ）",
        notes_ja="「AはBです」でAとBをつなぎます。名詞（学生・先生）とナ形容詞（元気・きれい）には「です」を付けます。"
                 "例：<strong>私は学生です。／この町はきれいです。</strong><br>"
                 "イ形容詞（高い・おいしい）は、そのままで文が終わります。「です」は丁寧にするためだけに付けます。"
                 "例：このカレーは<strong>おいしいです</strong>。<br>"
                 "友達や家族と話すときの普通形は「だ」です。例：今日は休みだ。（ナ形容詞：元気だ）"
                 "ただし、イ形容詞の普通形に「だ」は付きません（おいしい）。疑問文は「か」を付けます：学生ですか。",
        notes_en="Link A and B with 'A wa B desu'. です attaches to nouns (学生) and na-adjectives (元気). "
                 "An i-adjective (高い, おいしい) can already end a sentence, so です only adds politeness: おいしいです. "
                 "The plain form used with friends and family is だ (今日は休みだ); i-adjectives never take だ. "
                 "Add か to make a question: 学生ですか。",
        nuance_ja="「です」は丁寧な言い方で、初対面・先生・お客さん・仕事など、ほとんどの場面で安全に使えます。"
                  "「だ」は友達・家族との会話、日記、メモなどで使う普通形です。ぶっきらぼうに聞こえることがあるので、"
                  "話し言葉では「いい天気ね。」「学生。」のように「だ」を言わないことも多いです。"
                  "また、「は」と「です」はいつも「A＝B」とは限りません。レストランで「私はコーヒーです」と言えば、"
                  "『私はコーヒーにします』という意味になります。",
        nuance_en="です is the safe polite choice for first meetings, teachers, customers and work. だ is the plain form for "
                  "friends, family, diaries and notes; it can sound blunt, so in casual speech it is often dropped "
                  "(「いい天気ね。」). Also, 'A は B です' is not always A = B: in a restaurant, 「私はコーヒーです」 means "
                  "'I'll have coffee'.",
        trap_ja="①英語の be 動詞（am / is / are）と違って、「です」は主語が変わっても形が変わりません（私は学生です／あの人は学生です）。<br>"
                "②イ形容詞に「だ」は付けません。×高いだです・×おいしいだ → ○高いです・○おいしい<br>"
                "③「です」と「だ」を重ねません。×学生だです → ○学生です<br>"
                "④動詞に「です」は付けません。×食べますです → ○食べます<br>"
                "⑤「〜と思います」の前では普通形の「だ」を使います。○先生だと思います ×先生ですと思います",
        trap_en="① Unlike English am/is/are, です never changes with the subject. "
                "② Never put だ after an i-adjective: ×高いだです → ○高いです. "
                "③ Don't stack them: ×学生だです. "
                "④ Don't add です after a ます-verb: ×食べますです. "
                "⑤ Before と思います use the plain だ: ○先生だと思います, ×先生ですと思います.",
        contrast=[
            dict(type="wrong", sentence="このカレーはおいしいだです。",
                 reason_ja="イ形容詞の後ろに「だ」は付けません。丁寧にするなら「です」だけです。",
                 reason_en="Never put だ after an i-adjective; polite speech needs only です."),
            dict(type="correct", sentence="このカレーはおいしいです。",
                 reason_ja="イ形容詞 ＋ です。「です」は丁寧にする働きだけをします。",
                 reason_en="i-adjective + です. です only adds politeness."),
            dict(type="correct", sentence="（友達に）{明日|あした}は{休|やす}みだよ。",
                 reason_ja="友達との会話では、名詞の普通形「だ」を使います。",
                 reason_en="With friends, use the plain form だ after a noun."),
        ],
        comparison=[
            dict(form="名詞 ＋ です", form_en="polite copula", badge="丁寧", badge_type="good",
                 nuance_ja="誰にでも使える基本の丁寧形です。自己紹介・職場・先生との会話で使います。",
                 nuance_en="The all-purpose polite form: introductions, work, talking to teachers.",
                 example="{私|わたし}は{会社員|かいしゃいん}です。"),
            dict(form="名詞 ＋ だ", form_en="plain copula", badge="普通形", badge_type="neutral",
                 nuance_ja="友達・家族との会話、日記、文章（である体）で使います。目上の人には使いません。",
                 nuance_en="Casual talk, diaries and plain-style writing. Not for superiors.",
                 example="{今日|きょう}は{日曜日|にちようび}だ。"),
            dict(form="動詞 ＋ ます", form_en="polite verb ending", badge="動詞", badge_type="both",
                 nuance_ja="動詞の丁寧形は「ます」です。「です」は動詞には付きません。",
                 nuance_en="Verbs are made polite with ます. です does not attach to verbs.",
                 example="{毎朝|まいあさ}、{牛乳|ぎゅうにゅう}を{飲|の}みます。"),
        ],
    ),
    quiz=[
        dict(stem="はじめまして。{田中|たなか}（　　　）。どうぞよろしくお願いします。",
             correct="です", distractors=["ます", "だです", "ました"],
             en="Nice to meet you. I'm Tanaka. Please treat me kindly.",
             notes_ja="名前（名詞）の後ろには「です」を付けます。「ます」「ました」は動詞に付く形なので、名詞には付けられません。"
                      "「だです」のように重ねることもできません。",
             notes_en="After a name (noun) you add です. ます / ました attach only to verbs, and だです can't be stacked."),
        dict(stem="A：{新|あたら}しい{部屋|へや}はどうですか。<br>B：{広|ひろ}くて、とても{明|あか}るい（　　　）。",
             correct="です", distractors=["だ", "ます", "でした"],
             en="A: How is your new room? B: It's spacious and very bright.",
             notes_ja="「明るい」はイ形容詞なので、丁寧にするには「です」だけを付けます。「明るいだ」は間違いです。"
                      "「でした」も「明るいでした」とは言いません（過去は「明るかったです」）。",
             notes_en="明るい is an i-adjective; only です is added for politeness. 明るいだ is wrong, and 明るいでした is wrong too "
                      "(the past is 明るかったです)."),
        dict(stem="A：おじいさんは{最近|さいきん}どうですか。<br>B：ありがとうございます。とても{元気|げんき}（　　　）。",
             correct="です", distractors=["ます", "だです", "いです"],
             en="A: How has your grandfather been lately? B: Thank you. He's very well.",
             notes_ja="「元気」はナ形容詞です。丁寧に答えるときは「元気です」。「元気いです」のようにイ形容詞の形にはなりません。"
                      "「ます」は動詞用で、「だです」は重ねて使えません。",
             notes_en="元気 is a na-adjective, so the polite answer is 元気です. It cannot take the i-adjective ending (×元気い), "
                      "ます is for verbs, and だです can't be stacked."),
        dict(stem="A：あの{人|ひと}は{誰|だれ}ですか。<br>B：{林|はやし}さんの{弟|おとうと}さん（　　　）と{思|おも}います。",
             correct="だ", distractors=["です", "ます", "でした"],
             en="A: Who is that person? B: I think he is Mr. Hayashi's younger brother.",
             notes_ja="「〜と思います」の前には普通形を使います。名詞の普通形は「だ」なので、「弟さんだと思います」になります。"
                      "「ですと」「でしたと」「ますと」の形は、ここでは使えません。",
             notes_en="Before と思います you need the plain form, and the plain form of a noun sentence is だ. "
                      "です / でした / ます cannot precede と here."),
    ],
)

# ---------------------------------------------------------------- 2 ではありません／じゃない
GRAMMAR[2] = dict(
    name="ではありません／じゃない", reading="ではありません／じゃない",
    meaning_en="is not (negative of です／だ)",
    similar="じゃありません、くないです",
    details=dict(
        formula="<strong>名詞</strong>／<strong>ナ形容詞</strong> ＋ <strong>ではありません</strong>（丁寧）<br>"
                "＋ <strong>じゃありません／じゃないです</strong>（話し言葉）<br>"
                "＋ <strong>ではない／じゃない</strong>（普通形）<br>"
                "<strong>イ形容詞</strong>は <strong>〜くないです</strong>（×〜いではありません）",
        notes_ja="「です」の否定です。<strong>学生です → 学生ではありません</strong>。話し言葉では「では」が縮んで「じゃ」になります："
                 "学生じゃありません／学生じゃないです。ナ形容詞も同じです：元気ではありません・にぎやかじゃありません。<br>"
                 "イ形容詞は形が変わります：高い → <strong>高くないです</strong>／高くありません。<br>"
                 "過去は「ではありませんでした／じゃなかったです」です：昨日は雨ではありませんでした。<br>"
                 "「あまり〜」「ぜんぜん〜」と一緒によく使います：あまりにぎやかではありません。",
        notes_en="The negative of です. 学生です → 学生ではありません. In speech では contracts to じゃ: 学生じゃありません / じゃないです. "
                 "Na-adjectives work the same way (元気ではありません). I-adjectives change instead: 高い → 高くないです / 高くありません. "
                 "Past: ではありませんでした / じゃなかったです. Often paired with あまり / ぜんぜん.",
        nuance_ja="名詞・ナ形容詞をはっきり否定する言い方です。「ではありません」は文章・案内・スピーチなど改まった場面、"
                  "「じゃありません」「じゃないです」は日常会話、「じゃない」は友達・家族との普通形です。"
                  "「いいえ、先生ではありません。学生です。」のように、否定のあとに正しい情報を続けると自然な会話になります。",
        nuance_en="It firmly denies a noun or na-adjective. ではありません suits writing, announcements and speeches; "
                  "じゃありません / じゃないです is everyday polite speech; じゃない is plain talk with friends and family. "
                  "It sounds natural when followed by the correct information: 「いいえ、先生ではありません。学生です。」",
        trap_ja="①イ形容詞には使いません。×高いではありません → ○高くないです／高くありません<br>"
                "②「はい／いいえ」の答え方：「学生ではありませんか。」に対して、日本語の「はい」は『あなたの言ったことは正しい』という意味です。"
                "学生でないなら「はい、学生ではありません」、学生なら「いいえ、学生です」と答えます。英語の yes / no と逆になることがあります。<br>"
                "③×学生ないです・×学生ではないません は間違いです。<br>"
                "④過去は「ではありませんでした」です。×ではありませんした",
        trap_en="① Don't use it with i-adjectives: ×高いではありません → ○高くないです. "
                "② Answering a negative question: はい means 'what you said is right', so 「学生ではありませんか。」 → "
                "「はい、学生ではありません」(I'm not) / 「いいえ、学生です」(I am) — the reverse of English yes/no. "
                "③ ×学生ないです and ×学生ではないません are wrong. ④ Past: ではありませんでした (×ではありませんした).",
        contrast=[
            dict(type="wrong", sentence="この{本|ほん}は{高|たか}いではありません。",
                 reason_ja="「高い」はイ形容詞です。「ではありません」は付けられません。",
                 reason_en="高い is an i-adjective, so ではありません can't follow it."),
            dict(type="correct", sentence="この{本|ほん}は{高|たか}くないです。",
                 reason_ja="イ形容詞は「い」を「くない」に変えて否定します（高くありません、でも同じ意味です）。",
                 reason_en="An i-adjective turns い into くない (高くありません means the same)."),
            dict(type="correct", sentence="あの{人|ひと}は{先生|せんせい}じゃありません。{学生|がくせい}です。",
                 reason_ja="名詞の否定は「じゃありません」。あとに正しい情報を続けると自然です。",
                 reason_en="A noun is negated with じゃありません; adding the correct information sounds natural."),
        ],
        comparison=[
            dict(form="〜ではありません", form_en="formal negative", badge="丁寧・改まった", badge_type="good",
                 nuance_ja="文章・案内・スピーチ・お客さんへの説明など、きちんとした場面で使います。",
                 nuance_en="Writing, announcements, speeches and explanations to customers.",
                 example="ここは{駅|えき}ではありません。"),
            dict(form="〜じゃありません／じゃないです", form_en="spoken polite negative", badge="会話", badge_type="both",
                 nuance_ja="日常会話の丁寧な否定です。「ではありません」より柔らかく聞こえます。",
                 nuance_en="Everyday polite negative; sounds softer than ではありません.",
                 example="{私|わたし}は{先生|せんせい}じゃありません。"),
            dict(form="〜くないです", form_en="negative of i-adjectives", badge="イ形容詞", badge_type="neutral",
                 nuance_ja="イ形容詞（高い・おいしい）の否定は、「ではありません」ではなく「くない」です。",
                 nuance_en="i-adjectives (高い, おいしい) are negated with くない, not ではありません.",
                 example="この{部屋|へや}は{広|ひろ}くないです。"),
        ],
    ),
    quiz=[
        dict(stem="A：あの{人|ひと}は{田中|たなか}さんですか。<br>B：いいえ、{田中|たなか}さん（　　　）。{鈴木|すずき}さんです。",
             correct="じゃありません", distractors=["ではません", "ありません", "じゃないます"],
             en="A: Is that person Mr. Tanaka? B: No, he isn't Mr. Tanaka. He's Mr. Suzuki.",
             notes_ja="名詞「田中さん」の否定は「じゃありません」（改まった言い方は「ではありません」）です。"
                      "「ではません」「じゃないます」という形はなく、「ありません」だけでは「じゃ／では」が足りません。",
             notes_en="The negative of a noun is じゃありません (formal: ではありません). Forms like ではません or じゃないます "
                      "don't exist, and ありません alone lacks the じゃ／では."),
        dict(stem="A：この{町|まち}は、{夜|よる}もにぎやかですか。<br>B：いいえ、あまりにぎやか（　　　）。",
             correct="ではありません", distractors=["です", "ます", "でした"],
             en="A: Is this town lively at night, too? B: No, it isn't very lively.",
             notes_ja="「あまり」は否定の文と一緒に使います。ナ形容詞「にぎやか」の丁寧な否定は「ではありません」です。"
                      "「です」「でした」は肯定、「ます」は動詞用なので、どれも入りません。",
             notes_en="あまり goes with a negative. The polite negative of the na-adjective にぎやか is ではありません. "
                      "です / でした are affirmative and ます is for verbs."),
        dict(stem="A：この{ラーメン|らーめん}は{高|たか}いですか。<br>B：いいえ、{高|たか}（　　　）。{安|やす}いですよ。",
             correct="くないです", distractors=["ではありません", "じゃないです", "いではありません"],
             en="A: Is this ramen expensive? B: No, it's not expensive. It's cheap.",
             notes_ja="イ形容詞「高い」の否定は「高くないです」です。「高いではありません」「高いじゃないです」のように、"
                      "名詞用の「ではありません／じゃない」を付けることはできません。",
             notes_en="The negative of the i-adjective 高い is 高くないです. The noun-style ではありません / じゃない "
                      "cannot be attached to it."),
        dict(stem="（{友達|ともだち}へのメッセージ）ごめん、{明日|あした}は{暇|ひま}（　　　）。{仕事|しごと}があるんだ。",
             correct="じゃない", distractors=["じゃなかった", "じゃません", "じゃいない"],
             en="(A message to a friend) Sorry, I'm not free tomorrow. I have work.",
             notes_ja="友達への文なので普通形の「じゃない」を使います。「明日」の話なので過去の「じゃなかった」は不自然で、"
                      "「じゃません」「じゃいない」という形はありません。",
             notes_en="This is casual, so the plain じゃない is used. じゃなかった is past and clashes with 明日, "
                      "and じゃません / じゃいない are not real forms."),
    ],
)

# ---------------------------------------------------------------- 3 ます／ません
GRAMMAR[3] = dict(
    name="ます／ません", reading="ます／ません",
    meaning_en="polite verb endings (present/future): does / does not",
    similar="辞書形、ませんか",
    details=dict(
        formula="<strong>グループ1</strong>：書く → 書<strong>きます</strong>／書き<strong>ません</strong><br>"
                "<strong>グループ2</strong>：食べる → 食べ<strong>ます</strong>／食べ<strong>ません</strong><br>"
                "<strong>グループ3</strong>：する → し<strong>ます</strong>　来る → {来|き}<strong>ます</strong>",
        notes_ja="動詞の丁寧な言い方です。ます形（語幹）に「ます」を付けます。<br>"
                 "・グループ1（五段）：語尾をい段にします。飲む→飲みます、買う→買います、話す→話します<br>"
                 "・グループ2（一段）：「る」を取ります。見る→見ます、寝る→寝ます<br>"
                 "・グループ3：する→します、来る→{来|き}ます<br>"
                 "否定は「ます」を「ません」にします：飲みません・食べません・しません・{来|き}ません。"
                 "習慣（毎日〜）・未来（明日〜）・これからの動作を表します。疑問文は「ますか」です。",
        notes_en="The polite verb ending. Attach ます to the stem (ます form). Group 1: change the final sound to the い-row "
                 "(飲む→飲みます, 買う→買います). Group 2: drop る (見る→見ます). Group 3: する→します, 来る→来(き)ます. "
                 "Negative: ます→ません. It covers habits (毎日), the future (明日) and imminent actions. Questions use ますか.",
        nuance_ja="「ます」は丁寧さを表すだけで、時間は文脈で決まります。「毎日」「よく」＝習慣、「明日」「来週」＝未来、"
                  "「今から」＝すぐの動作です。いま続けている最中の動作は「ています」を使います（食べています）。"
                  "「ません」は『しない』という事実・習慣の否定で、「あまり飲みません」「ぜんぜん食べません」のように副詞と一緒によく使います。"
                  "友達や家族とは辞書形（食べる）に変わります。",
        nuance_en="ます only adds politeness; time comes from context: 毎日 / よく = habit, 明日 / 来週 = future, 今から = about to. "
                  "An action in progress uses ています (食べています). ません negates facts and habits, often with "
                  "あまり / ぜんぜん. With friends and family you switch to the dictionary form (食べる).",
        trap_ja="①辞書形に「ます」を付けません。×行くます → ○行きます<br>"
                "②「です」を足しません。×食べますです → ○食べます<br>"
                "③グループ2の否定を「食べりません」のようにしません。○食べません<br>"
                "④「今、食べます」は『今から食べる』という意味です。『今食べている』は「食べています」です。<br>"
                "⑤「ます」は英語の will にも現在形にも対応するので、時制を分けて考えなくて大丈夫です。",
        trap_en="① Never add ます to the dictionary form: ×行くます → ○行きます. "
                "② Don't add です: ×食べますです. "
                "③ Group 2 negative is 食べません, not ×食べりません. "
                "④ 「今、食べます」 means 'I'm about to eat'; 'I'm eating now' is 食べています. "
                "⑤ ます covers both English 'will' and the simple present.",
        contrast=[
            dict(type="wrong", sentence="{私|わたし}は{毎日|まいにち}{学校|がっこう}へ{行|い}くます。",
                 reason_ja="「ます」は辞書形ではなく、ます形（語幹）に付けます。「行く」は「行き」になります。",
                 reason_en="ます attaches to the stem, not the dictionary form: 行く → 行き."),
            dict(type="correct", sentence="{私|わたし}は{毎日|まいにち}{学校|がっこう}へ{行|い}きます。",
                 reason_ja="行く → 行き ＋ ます。習慣は「ます」で表します。",
                 reason_en="行く → 行き + ます. A habit is expressed with ます."),
            dict(type="correct", sentence="{日曜日|にちようび}は{会社|かいしゃ}に{行|い}きません。",
                 reason_ja="否定は「ません」。「〜は〜ません」で、その日はしないことを言います。",
                 reason_en="The negative is ません; 「〜は〜ません」 says what you don't do on that day."),
        ],
        comparison=[
            dict(form="動詞 ＋ ます", form_en="polite form", badge="丁寧", badge_type="good",
                 nuance_ja="初対面・先生・職場など、丁寧に話す場面の基本です。",
                 nuance_en="The default for first meetings, teachers and the workplace.",
                 example="{毎朝|まいあさ}、{新聞|しんぶん}を{読|よ}みます。"),
            dict(form="辞書形（食べる）", form_en="plain form", badge="普通形", badge_type="neutral",
                 nuance_ja="友達・家族との会話や、日記・メモで使います。目上の人には使いません。",
                 nuance_en="Casual talk with friends and family, diaries and notes. Not for superiors.",
                 example="{毎朝|まいあさ}、{牛乳|ぎゅうにゅう}を{飲|の}む。"),
            dict(form="〜ません／〜ないです", form_en="polite negatives", badge="否定", badge_type="both",
                 nuance_ja="「食べません」が基本の丁寧な否定です。「食べないです」も使いますが、少し話し言葉的です。",
                 nuance_en="食べません is the standard polite negative; 食べないです is also used but sounds more conversational.",
                 example="{私|わたし}はコーヒーを{飲|の}みません。"),
        ],
    ),
    quiz=[
        dict(stem="A：{毎朝|まいあさ}、{朝|あさ}ごはんを{食|た}べますか。<br>B：はい、{毎朝|まいあさ}{食|た}べ（　　　）。",
             correct="ます", distractors=["ません", "ましょう", "ませんか"],
             en="A: Do you eat breakfast every morning? B: Yes, I eat it every morning.",
             notes_ja="「はい」で答えているので、肯定の「ます」が入ります。「ません」は否定、「ましょう」「ませんか」は誘う言い方で、答えの文には合いません。",
             notes_en="B says はい, so the affirmative ます fits. ません is negative, and ましょう / ませんか are invitations, not answers."),
        dict(stem="{私|わたし}はあまりコーヒーを{飲|の}み（　　　）。{紅茶|こうちゃ}のほうが{好|す}きです。",
             correct="ません", distractors=["ます", "ましょう", "ませんか"],
             en="I don't drink coffee very much. I like tea better.",
             notes_ja="「あまり」は否定の文と一緒に使うので「ません」です。「ます」「ましょう」は肯定、「ませんか」は『私は〜ませんか』という質問になってしまい、"
                      "自分のことを言う文には合いません。",
             notes_en="あまり goes with a negative, so ません. ます / ましょう are affirmative, and ませんか would turn the sentence into a question."),
        dict(stem="A：{明日|あした}、{何|なに}をしますか。<br>B：{友達|ともだち}と{映画|えいが}を{見|み}（　　　）。",
             correct="ます", distractors=["ません", "ませんか", "ました"],
             en="A: What are you doing tomorrow? B: I'm going to watch a movie with a friend.",
             notes_ja="「明日」のことを言うので、未来の予定は「ます」で表します。「ました」は過去、「ませんか」は質問、「ません」は『何をしますか』への答えとして合いません。",
             notes_en="The plan is for 明日, so ます expresses the future. ました is past, ませんか is a question, "
                      "and ません wouldn't answer 『何をしますか』."),
        dict(stem="A：{田中|たなか}さんは{今日|きょう}のパーティーに{来|き}ますか。<br>B：いいえ、{来|き}（　　　）。{仕事|しごと}がありますから。",
             correct="ません", distractors=["ます", "ましょう", "ましたか"],
             en="A: Is Mr. Tanaka coming to today's party? B: No, he isn't coming. He has work.",
             notes_ja="「いいえ」と「仕事がありますから」から、来ないことが分かります。否定の「{来|き}ません」が正解です。"
                      "「ます」「ましょう」は肯定・誘いで、「ましたか」は質問です。",
             notes_en="いいえ and 仕事がありますから show he won't come: 来ません. ます / ましょう are affirmative or an invitation, "
                      "and ましたか is a question."),
    ],
)

# ---------------------------------------------------------------- 4 ました／ませんでした
GRAMMAR[4] = dict(
    name="ました／ませんでした", reading="ました／ませんでした",
    meaning_en="polite verb past: did / did not",
    similar="ていません、ます／ません",
    details=dict(
        formula="<strong>肯定</strong>：〜ます → 〜<strong>ました</strong>（食べます → 食べ<strong>ました</strong>）<br>"
                "<strong>否定</strong>：〜ません → 〜<strong>ませんでした</strong>（食べません → 食べ<strong>ませんでした</strong>）",
        notes_ja="「ます」の過去形です。「ます」を「ました」、「ません」を「ませんでした」に変えるだけで、動詞のグループは関係ありません。"
                 "書きました・食べました・しました・{来|き}ました。否定は「〜ませんでした」です。<br>"
                 "「昨日」「先週」「さっき」などの過去を表す言葉と一緒によく使います。疑問文は「ましたか」です。<br>"
                 "「もう〜ましたか」には、「はい、もう〜ました」／「いいえ、まだです」と答えます。<br>"
                 "名詞・形容詞の過去は別の形です：学生でした／おいしかったです。",
        notes_en="The past of ます. Just change ます → ました and ません → ませんでした, whatever the verb group: "
                 "書きました, 食べました, しました, 来(き)ました. Common with past-time words (昨日, 先週, さっき). Questions: ましたか. "
                 "「もう〜ましたか」 is answered 「はい、もう〜ました」 / 「いいえ、まだです」. "
                 "Nouns and adjectives have their own past forms: 学生でした / おいしかったです.",
        nuance_ja="終わったこと（完了した動作や事実）を述べます。「食べました」は『食べた』という事実で、今もおなかがいっぱいかどうかは関係ありません。"
                  "「ませんでした」は『その時、しなかった』という終わった話です。「どこへも行きませんでした」「何も食べませんでした」のように、"
                  "「疑問詞＋も」と一緒によく使います。『まだしていない（これからするかもしれない）』と言いたいときは、"
                  "「ませんでした」ではなく「まだ〜ていません」を使います。",
        nuance_en="It states something finished: 食べました = 'I ate'. ませんでした says 'did not do it (then)', often with "
                  "question word + も (どこへも行きませんでした, 何も食べませんでした). To say 'not yet (but maybe later)', "
                  "use まだ〜ていません instead of ませんでした.",
        trap_ja="①×食べませんかった／×食べませんした／×食べないでした → ○食べませんでした<br>"
                "②名詞・形容詞に「ました」は付けません。×おいしいました → ○おいしかったです　×雨ました → ○雨でした<br>"
                "③「もう食べましたか」に「いいえ、食べませんでした」と答えると『食べなかった』という過去の話になります。"
                "まだ食べていないなら「いいえ、まだです」「まだ食べていません」と言います。<br>"
                "④英語の過去形（ate）にも現在完了（have eaten）にも「ました」が使えます。",
        trap_en="① ×食べませんかった / ×食べませんした / ×食べないでした → ○食べませんでした. "
                "② Don't add ました to nouns or adjectives: ×おいしいました → ○おいしかったです; ×雨ました → ○雨でした. "
                "③ To 「もう食べましたか」, 「いいえ、食べませんでした」 means 'I didn't eat'; for 'not yet' say 「いいえ、まだです」. "
                "④ ました translates both the English simple past and the present perfect.",
        contrast=[
            dict(type="wrong", sentence="{昨日|きのう}は{学校|がっこう}へ{行|い}きませんかった。",
                 reason_ja="「ません」の過去は「ませんでした」です。イ形容詞の過去「〜かった」を混ぜないでください。",
                 reason_en="The past of ません is ませんでした. Don't mix in the i-adjective past ending かった."),
            dict(type="correct", sentence="{昨日|きのう}は{学校|がっこう}へ{行|い}きませんでした。",
                 reason_ja="行きません → 行きませんでした。昨日しなかったことを表します。",
                 reason_en="行きません → 行きませんでした: something you didn't do yesterday."),
            dict(type="correct", sentence="{昨日|きのう}のカレーはおいしかったです。",
                 reason_ja="形容詞の過去は「ました」ではなく「〜かったです」です。",
                 reason_en="An adjective's past is 〜かったです, not ました."),
        ],
        comparison=[
            dict(form="〜ました", form_en="polite past", badge="丁寧", badge_type="good",
                 nuance_ja="終わった動作・出来事を丁寧に言います。",
                 nuance_en="States a finished action or event politely.",
                 example="{昨日|きのう}、{友達|ともだち}に{会|あ}いました。"),
            dict(form="〜た（普通形）", form_en="plain past", badge="普通形", badge_type="neutral",
                 nuance_ja="友達・家族との会話や日記で使う過去形です。",
                 nuance_en="The past form for friends, family and diaries.",
                 example="{昨日|きのう}、{友達|ともだち}に{会|あ}った。"),
            dict(form="まだ〜ていません", form_en="not yet", badge="未完了", badge_type="both",
                 nuance_ja="『まだ終わっていない・これからするかもしれない』という意味です。「ませんでした」は終わった過去の話です。",
                 nuance_en="'Haven't done it yet, may do it later'. ませんでした is a closed past fact.",
                 example="まだ{宿題|しゅくだい}をしていません。"),
        ],
    ),
    quiz=[
        dict(stem="{昨日|きのう}は{友達|ともだち}と{買|か}い{物|もの}に{行|い}き（　　　）。とても{楽|たの}しかったです。",
             correct="ました", distractors=["ません", "ます", "ませんでした"],
             en="Yesterday I went shopping with a friend. It was a lot of fun.",
             notes_ja="「楽しかったです」とあるので、実際に行ったことが分かります。過去の肯定は「ました」です。"
                      "「ませんでした」は行かなかった意味になり、「ます」「ません」は過去ではありません。",
             notes_en="楽しかったです shows that the speaker actually went, so the past affirmative ました. "
                      "ませんでした would mean 'didn't go', and ます / ません are not past."),
        dict(stem="A：{昨日|きのう}のパーティーに{行|い}きましたか。<br>B：いいえ、{行|い}き（　　　）。{熱|ねつ}がありましたから。",
             correct="ませんでした", distractors=["ました", "ません", "ましたか"],
             en="A: Did you go to yesterday's party? B: No, I didn't. I had a fever.",
             notes_ja="「いいえ」で、昨日のことなので過去の否定「ませんでした」です。「ました」は肯定、「ません」は現在・未来の否定、「ましたか」は質問の形です。",
             notes_en="いいえ plus yesterday means the past negative ませんでした. ました is affirmative, ません is present/future, "
                      "and ましたか is a question."),
        dict(stem="{先週|せんしゅう}の{土曜日|どようび}は{雨|あめ}でしたから、どこへも{行|い}き（　　　）。",
             correct="ませんでした", distractors=["ました", "ません", "ましょう"],
             en="It rained last Saturday, so I didn't go anywhere.",
             notes_ja="「どこへも」は否定の文と一緒に使います。「先週」のことなので過去の否定「ませんでした」です。「ません」は現在・未来、「ました」は肯定、「ましょう」は誘いです。",
             notes_en="どこへも needs a negative, and 先週 makes it past: ませんでした. ません is present/future, ました is affirmative, ましょう is an invitation."),
        dict(stem="A：{昨日|きのう}の{宿題|しゅくだい}は{難|むずか}しかったですか。<br>B：はい、3{時間|じかん}もかかり（　　　）。",
             correct="ました", distractors=["ます", "ません", "ませんでした"],
             en="A: Was yesterday's homework difficult? B: Yes, it took me as long as three hours.",
             notes_ja="「昨日の」「難しかったですか」「はい」から、過去の肯定「ました」が分かります。「3時間も」は『長くかかった』という意味で、否定の「ません／ませんでした」とは合いません。",
             notes_en="昨日の, 難しかったですか and はい point to the past affirmative ました. 3時間も stresses a long time, which clashes with ません / ませんでした."),
    ],
)

# ---------------------------------------------------------------- 5 てください
GRAMMAR[5] = dict(
    name="てください", reading="てください",
    meaning_en="please do ~ (request / instruction)",
    similar="ないでください、てもいい、ませんか",
    details=dict(
        formula="動詞 て形 ＋ <strong>ください</strong><br>"
                "名詞 ＋ を ＋ <strong>ください</strong>（〜をください＝〜をくださいと頼む）",
        notes_ja="動詞のて形に「ください」を付けます。て形の作り方：<br>"
                 "・グループ1：う・つ・る→<strong>って</strong>（買って・待って・乗って）／ぬ・ぶ・む→<strong>んで</strong>（飲んで・呼んで）／"
                 "く→<strong>いて</strong>（書いて）／ぐ→<strong>いで</strong>（泳いで）／す→<strong>して</strong>（話して）※行く→行って<br>"
                 "・グループ2：「る」→「て」（食べて・見て）　・グループ3：して・{来|き}て<br>"
                 "例：ここに名前を<strong>書いてください</strong>。／ちょっと<strong>待ってください</strong>。<br>"
                 "名詞のときは「〜をください」（お水をください）で『〜をくれませんか』という意味です。",
        notes_en="Add ください to the て form. Te-form: Group 1 う/つ/る→って, ぬ/ぶ/む→んで, く→いて (行く→行って), ぐ→いで, す→して; "
                 "Group 2 る→て; Group 3 して / 来(き)て. Examples: 書いてください, 待ってください. "
                 "With a noun: 〜をください = 'please give me ~'.",
        nuance_ja="相手に何かをしてもらいたいときの基本の依頼・指示です。先生が学生に、店員がお客さんに、友達に丁寧に頼むときなどに使います。"
                  "「すみません、」「ちょっと」を付けると柔らかくなります。また、「どうぞ座ってください」「たくさん食べてください」のように、"
                  "相手に好意で勧めるときにも使います。ただし、相手に大きな負担をかけるお願いや目上の人へのお願いには、"
                  "「お願いします」「〜ていただけませんか」のような、もっと丁寧な言い方が向いています。",
        nuance_en="The basic way to ask or instruct someone to do something: teachers to students, staff to customers, polite requests "
                  "to friends. Adding すみません or ちょっと softens it. It is also used to offer kindly (どうぞ座ってください, "
                  "たくさん食べてください). For big favours or superiors, more polite forms (お願いします, 〜ていただけませんか) are better.",
        trap_ja="①辞書形や語幹に付けません。×待つください・×待ちください → ○待ってください<br>"
                "②て形の間違いが多いです。×書きてください・×飲みてください・×行いてください → ○書いてください・飲んでください・行ってください<br>"
                "③「〜をください」は名詞にだけ使います。×食べるをください → ○食べてください／ケーキをください<br>"
                "④英語の please のように、どんな場面でも丁寧になるわけではありません。「ください」は指示に近く聞こえることがあるので、"
                "お願いの言葉（すみません・お願いします）を添えると安心です。",
        trap_en="① Not after the dictionary form or stem: ×待つください → ○待ってください. "
                "② Watch te-form mistakes: ×書きて → ○書いて, ×飲みて → ○飲んで, ×行いて → ○行って. "
                "③ 〜をください is for nouns only: ×食べるをください. "
                "④ ください is not a magic 'please'; it can sound like an instruction, so add すみません / お願いします.",
        contrast=[
            dict(type="wrong", sentence="ちょっと{待|ま}つください。",
                 reason_ja="「ください」の前は、辞書形ではなくて形です。「待つ」のて形は「待って」です。",
                 reason_en="ください must follow the te form, not the dictionary form: 待つ → 待って."),
            dict(type="correct", sentence="ちょっと{待|ま}ってください。",
                 reason_ja="待つ → 待って ＋ ください。「ちょっと」が入ると柔らかい依頼になります。",
                 reason_en="待つ → 待って + ください. ちょっと makes it a softer request."),
            dict(type="correct", sentence="すみません、{水|みず}をください。",
                 reason_ja="名詞のときは「〜をください」で、物をくださいと頼む意味になります。",
                 reason_en="After a noun, 〜をください means 'please give me ~'."),
        ],
        comparison=[
            dict(form="〜てください", form_en="request / instruction", badge="依頼", badge_type="good",
                 nuance_ja="相手に何かをしてもらうための依頼・指示です。",
                 nuance_en="Asks the listener to do something.",
                 example="もう{少|すこ}し{大|おお}きい{声|こえ}で{話|はな}してください。"),
            dict(form="〜てもいいですか", form_en="asking permission", badge="許可", badge_type="both",
                 nuance_ja="自分がすることについて、相手に許可を求めます。してもらうのではなく、自分がします。",
                 nuance_en="Asks permission for something YOU will do — you aren't asking the listener to act.",
                 example="この{電話|でんわ}を{使|つか}ってもいいですか。"),
            dict(form="〜て（友達に）", form_en="casual request", badge="普通形", badge_type="neutral",
                 nuance_ja="友達・家族には「ください」を付けないで、て形だけで頼みます。目上の人には使いません。",
                 nuance_en="With friends and family you drop ください and use the te form alone. Not for superiors.",
                 example="ちょっと{待|ま}って。"),
        ],
    ),
    quiz=[
        dict(stem="A：すみません、ここに{名前|なまえ}を（　　　）ください。<br>B：はい、わかりました。",
             correct="{書|か}いて", distractors=["{書|か}きて", "{書|か}って", "{書|か}んで"],
             en="A: Excuse me, please write your name here. B: Yes, certainly.",
             notes_ja="「書く」は「く」で終わるので、て形は「書いて」です。「書って」「書んで」は他のグループ（う・つ・る／ぬ・ぶ・む）の形で、"
                      "「書きて」はて形にならない間違いです。",
             notes_en="書く ends in く, so the te form is 書いて. 書って / 書んで belong to other verb endings, and 書きて is not a te form."),
        dict(stem="A：{田中|たなか}さんは{会議室|かいぎしつ}にいますよ。<br>B：すみません、ちょっと{呼|よ}（　　　）ください。",
             correct="んで", distractors=["いて", "って", "して"],
             en="A: Mr. Tanaka is in the meeting room. B: Sorry, could you call him for me?",
             notes_ja="「呼ぶ」は「ぶ」で終わるので、て形は「呼んで」です。「ぶ・ぬ・む」で終わる動詞は「んで」になります。",
             notes_en="呼ぶ ends in ぶ, so the te form is 呼んで. Verbs ending in ぶ / ぬ / む take んで."),
        dict(stem="A：{先生|せんせい}、{今|いま}、いいですか。<br>B：{今|いま}、{電話|でんわ}をしています。ちょっと{待|ま}（　　　）ください。",
             correct="って", distractors=["んで", "いて", "して"],
             en="A: Teacher, do you have a moment? B: I'm on the phone right now. Please wait a little.",
             notes_ja="「待つ」は「つ」で終わるので、て形は「待って」です。「待んで」「待いて」「待して」はどれもて形のルールに合いません。",
             notes_en="待つ ends in つ, so the te form is 待って. 待んで / 待いて / 待して don't follow the rules."),
        dict(stem="A：いただきます。<br>B：どうぞ、たくさん（　　　）ください。",
             correct="{食|た}べて", distractors=["{食|た}べる", "{食|た}べます", "{食|た}べた"],
             en="A: Thank you for the food. B: Please, eat a lot.",
             notes_ja="「ください」の前は、て形を使います。「食べる」（辞書形）、「食べます」（ます形）、「食べた」（た形）では「ください」に続けられません。",
             notes_en="ください follows the te form. The dictionary form 食べる, the ます form and the past 食べた can't connect to it."),
    ],
)

# ---------------------------------------------------------------- 6 ないでください
GRAMMAR[6] = dict(
    name="ないでください", reading="ないでください",
    meaning_en="please do not do ~",
    similar="てはいけない、てください",
    details=dict(
        formula="動詞 ない形 ＋ <strong>でください</strong>（＝〜<strong>ないでください</strong>）<br>"
                "グループ1：書く→書<strong>かないで</strong>　買う→買<strong>わないで</strong>　グループ2：食べ<strong>ないで</strong>　"
                "グループ3：し<strong>ないで</strong>・{来|こ}<strong>ないで</strong>",
        notes_ja="動詞のない形に「でください」を付けます。ない形の作り方：<br>"
                 "・グループ1：語尾をあ段にして「ない」（書く→書かない、話す→話さない、飲む→飲まない）。"
                 "「う」で終わる動詞は<strong>「わ」</strong>になります（買う→買わない、会う→会わない）。<br>"
                 "・グループ2：「る」を取って「ない」（食べる→食べない、見る→見ない）<br>"
                 "・グループ3：する→しない、来る→{来|こ}ない<br>"
                 "例：ここで写真を<strong>撮らないでください</strong>。／窓を<strong>閉めないでください</strong>。",
        notes_en="Add でください to the ない form. Group 1: change the last sound to the あ-row + ない (書く→書かない); "
                 "verbs ending in う use わ (買う→買わない). Group 2: drop る + ない (食べない). Group 3: しない / 来(こ)ない.",
        nuance_ja="相手に『しないでほしい』と頼む言い方です。「てはいけません」のような強い禁止ではなく、お願いとして伝えるので、"
                  "お客さんや知らない人にも使えます。図書館や美術館の注意書きにもよく使われます（ここで写真を撮らないでください）。"
                  "また、「心配しないでください」「気にしないでください」のように、相手を気づかって言う場合もよくあります。"
                  "友達には「〜ないで」だけで言います。",
        nuance_en="It asks the listener not to do something. Because it is a request, not a strict prohibition like てはいけません, "
                  "it works with customers and strangers, and is common on signs in libraries and museums. "
                  "It is also used caringly (心配しないでください, 気にしないでください). With friends, just 〜ないで.",
        trap_ja="①辞書形に付けません。×食べるないでください → ○食べないでください<br>"
                "②「ないで」を「なくて」にしません。×食べなくてください → ○食べないでください<br>"
                "③ます形に付けません。×食べませんでください → ○食べないでください<br>"
                "④「う」で終わる動詞：×買あないでください・×買いないでください → ○買わないでください<br>"
                "⑤「行かないでください」には『行かないで！』という強い気持ちが入ることがあります。普通の場面では文脈に注意しましょう。",
        trap_en="① Not after the dictionary form: ×食べるないでください. "
                "② Not なくて: ×食べなくてください → ○食べないでください. "
                "③ Not after the ます form: ×食べませんでください. "
                "④ Verbs ending in う: ×買いない → ○買わない. "
                "⑤ 「行かないでください」 can sound like an emotional plea, so mind the context.",
        contrast=[
            dict(type="wrong", sentence="ここで{写真|しゃしん}を{撮|と}らなくてください。",
                 reason_ja="「しないでください」は「ないで」を使います。「なくて」には「ください」を付けられません。",
                 reason_en="For 'please don't', use ないで. なくて can't be followed by ください."),
            dict(type="correct", sentence="ここで{写真|しゃしん}を{撮|と}らないでください。",
                 reason_ja="撮る → 撮らない ＋ でください。お願いとして『しないでほしい』と伝えます。",
                 reason_en="撮る → 撮らない + でください. It asks politely for the action not to be done."),
            dict(type="correct", sentence="{大丈夫|だいじょうぶ}ですから、{心配|しんぱい}しないでください。",
                 reason_ja="相手を気づかうときにも使えます。「心配する」のない形は「心配しない」です。",
                 reason_en="It also works as a caring phrase. The ない form of 心配する is 心配しない."),
        ],
        comparison=[
            dict(form="〜ないでください", form_en="please don't (request)", badge="お願い", badge_type="good",
                 nuance_ja="『しないでほしい』という依頼です。お客さんや知らない人にも使えます。",
                 nuance_en="A request not to do something; works with customers and strangers.",
                 example="ここで{走|はし}らないでください。"),
            dict(form="〜てはいけません", form_en="must not (prohibition)", badge="禁止", badge_type="bad",
                 nuance_ja="ルールや立場に基づく強い禁止です。先生・親・規則の説明で使い、お客さんには強すぎます。",
                 nuance_en="A strong prohibition based on rules or authority (teacher, parent, regulations); too harsh for customers.",
                 example="{教室|きょうしつ}で{走|はし}ってはいけません。"),
            dict(form="〜ないで（友達に）", form_en="casual 'don't'", badge="普通形", badge_type="neutral",
                 nuance_ja="友達・家族には「ください」を付けず、「ないで」だけで言います。",
                 nuance_en="With friends and family, drop ください and say just ないで.",
                 example="{私|わたし}の{部屋|へや}に{入|はい}らないでね。"),
        ],
    ),
    quiz=[
        dict(stem="ここは{図書館|としょかん}です。{大|おお}きい{声|こえ}で{話|はな}（　　　）ください。",
             correct="さないで", distractors=["して", "さなくて", "しないで"],
             en="This is a library. Please don't speak loudly.",
             notes_ja="図書館なので『話さないでほしい』という意味になります。「話す」のない形は「話さない」で、「話さないでください」です。"
                      "「話して」は『話してほしい』になってしまい、「話しないで」はない形の作り方の間違いです。",
             notes_en="In a library the meaning is 'please don't talk': 話す → 話さない → 話さないでください. 話して means 'please talk', "
                      "and 話しないで misforms the ない form."),
        dict(stem="A：このケーキ、{食|た}べてもいいですか。<br>B：すみません、それは{弟|おとうと}のケーキですから、{食|た}べ（　　　）ください。",
             correct="ないで", distractors=["て", "ませんで", "なくて"],
             en="A: May I eat this cake? B: Sorry, it's my little brother's cake, so please don't eat it.",
             notes_ja="弟のケーキなので『食べないでほしい』という意味です。グループ2の動詞は「る」を取って「食べない」→「食べないでください」。"
                      "「食べてください」では逆の意味になり、「ませんで」「なくて」は「ください」に続きません。",
             notes_en="It's the brother's cake, so the meaning is 'please don't eat it': 食べない + でください. 食べてください would mean the opposite, "
                      "and ませんで / なくて can't precede ください."),
        dict(stem="{傘|かさ}がありますから、{新|あたら}しいのを{買|か}（　　　）ください。",
             correct="わないで", distractors=["いないで", "うないで", "らないで"],
             en="You already have an umbrella, so please don't buy a new one.",
             notes_ja="「買う」のように「う」で終わるグループ1の動詞は、ない形で「わ」になります（買わない）。"
                      "「買いない」「買うない」「買らない」はどれも間違った形です。",
             notes_en="Group 1 verbs ending in う use わ in the ない form: 買わない. 買いない / 買うない / 買らない are all wrong."),
        dict(stem="A：{試験|しけん}は{大丈夫|だいじょうぶ}ですか。<br>B：はい。{私|わたし}は{大丈夫|だいじょうぶ}ですから、{心配|しんぱい}（　　　）ください。",
             correct="しないで", distractors=["しなくて", "するないで", "しませんで"],
             en="A: Will the exam be all right? B: Yes. I'm fine, so please don't worry.",
             notes_ja="「心配する」はグループ3の動詞で、ない形は「心配しない」です。「心配しないでください」の形になります。"
                      "「しなくて」「しませんで」は「ください」に続かず、「するない」は作り方の間違いです。",
             notes_en="心配する is a Group 3 verb; its ない form is 心配しない → 心配しないでください. しなくて / しませんで can't precede ください, "
                      "and するない is a wrong formation."),
    ],
)

# ---------------------------------------------------------------- 7 てもいい
GRAMMAR[7] = dict(
    name="てもいい", reading="てもいい",
    meaning_en="may do ~; it's OK to ~ (permission)",
    similar="てはいけない、てください",
    details=dict(
        formula="動詞 て形 ＋ <strong>もいいです</strong>（許可を与える）<br>"
                "動詞 て形 ＋ <strong>もいいですか</strong>（許可を求める）<br>"
                "名詞 ＋ <strong>でもいいです</strong>（〜でも大丈夫）",
        notes_ja="動詞のて形に「もいいです」を付けます。許可を求めるときは「〜てもいいですか」です。<br>"
                 "例：ここに<strong>座ってもいいですか</strong>。―はい、<strong>どうぞ</strong>。／ええ、いいですよ。<br>"
                 "断るときは、「すみません、ちょっと…」と柔らかく言うか、「いいえ、〜てはいけません」と言います。<br>"
                 "「も」を言わずに「〜ていいですか」と言うことも多いです。名詞には「でもいいです」を使います："
                 "鉛筆でもいいです（鉛筆でも大丈夫です）。",
        notes_en="Add もいいです to the te form. To ask permission: 〜てもいいですか. Reply 「はい、どうぞ」 / 「ええ、いいですよ」, "
                 "or refuse softly 「すみません、ちょっと…」 / firmly 「いいえ、〜てはいけません」. The も is often dropped (〜ていいですか). "
                 "With nouns: 〜でもいいです ('~ is fine too').",
        nuance_ja="「〜てもいい」は『〜しても、いい（問題ない）』という意味で、自分がすることについて相手に許可を求めたり、"
                  "相手に許可を与えたりします。「ここで食べてもいいですか」は、してもらうお願いではなく『私がしてもいいか』という質問です。"
                  "答えに注意：「いいです」だけだと、場面によっては『けっこうです（いりません）』の意味に聞こえることがあります"
                  "（コーヒーはどうですか。―いいです）。許可をはっきり伝えるなら、「どうぞ」「いいですよ」を使いましょう。",
        nuance_en="It means 'even if you do ~, it's fine', used to ask permission for your own action or to grant it. "
                  "「ここで食べてもいいですか」 asks 'may I?' — it is not asking the listener to act. Careful with replies: "
                  "a bare 「いいです」 can mean 'no thanks' in some contexts (コーヒーはどうですか。―いいです). "
                  "To clearly grant permission, say どうぞ or いいですよ.",
        trap_ja="①辞書形に付けません。×食べるもいいですか → ○食べてもいいですか<br>"
                "②許可を求めるのに「ください」を使いません。「ここに座ってください」は『座ってほしい（座るように頼む）』になります。"
                "『座っていいか』は「座ってもいいですか」です。<br>"
                "③許可しないとき、「いいえ、いいです」と言わないでください。『いりません』の意味に聞こえます。"
                "「すみません、ちょっと…」「ここでは食べてはいけません」と言います。<br>"
                "④英語の Can I ~? を「できますか」で訳すと意味が変わることがあります。許可は「〜てもいいですか」です。",
        trap_en="① Not after the dictionary form: ×食べるもいいですか. "
                "② Don't use ください to ask permission; 「ここに座ってください」 means 'please sit here'. "
                "③ To refuse, don't say 「いいえ、いいです」 (it can sound like 'no thanks'); say 「すみません、ちょっと…」. "
                "④ English 'Can I ~?' is 〜てもいいですか, not 〜できますか.",
        contrast=[
            dict(type="wrong", sentence="ここで{食|た}べるもいいですか。",
                 reason_ja="「もいいですか」の前は、辞書形ではなくて形です。「食べる」のて形は「食べて」です。",
                 reason_en="Before もいいですか you need the te form, not the dictionary form: 食べる → 食べて."),
            dict(type="correct", sentence="ここで{食|た}べてもいいですか。",
                 reason_ja="食べる → 食べて ＋ もいいですか。『私が食べてもいいか』と許可を求めます。",
                 reason_en="食べる → 食べて + もいいですか. It asks 'may I eat here?'"),
            dict(type="correct", sentence="すみません、ここではちょっと…。",
                 reason_ja="許可しないときは、「いいえ、いいです」ではなく、柔らかい言い方で断ります。",
                 reason_en="To refuse, decline gently like this instead of 「いいえ、いいです」."),
        ],
        comparison=[
            dict(form="〜てもいいですか", form_en="May I ~?", badge="許可を求める", badge_type="good",
                 nuance_ja="自分がすることについて、相手に許可を求めます。",
                 nuance_en="Asks permission for something you want to do.",
                 example="この{辞書|じしょ}を{借|か}りてもいいですか。"),
            dict(form="〜てください", form_en="Please do ~", badge="依頼", badge_type="both",
                 nuance_ja="相手にしてもらうための依頼です。主語が逆になります（してもらう人は相手）。",
                 nuance_en="Asks the listener to act; the actor is reversed (the listener, not you).",
                 example="この{辞書|じしょ}を{貸|か}してください。"),
            dict(form="〜ましょうか", form_en="Shall I ~?", badge="申し出", badge_type="neutral",
                 nuance_ja="相手のために自分がすることを申し出ます。許可を求めるのではなく、手伝いの提案です。",
                 nuance_en="Offers to do something for the listener — an offer, not a request for permission.",
                 example="{窓|まど}を{閉|し}めましょうか。"),
        ],
    ),
    quiz=[
        dict(stem="A：{写真|しゃしん}を（　　　）もいいですか。<br>B：はい、どうぞ。",
             correct="{撮|と}って", distractors=["{撮|と}いて", "{撮|と}んで", "{撮|と}りて"],
             en="A: May I take a picture? B: Yes, go ahead.",
             notes_ja="「撮る」は「る」で終わるグループ1の動詞なので、て形は「撮って」です。「撮いて」「撮んで」「撮りて」はて形のルールに合いません。",
             notes_en="撮る is a Group 1 verb ending in る, so the te form is 撮って. The other forms don't follow the te-form rules."),
        dict(stem="A：ここに{座|すわ}ってもいいですか。<br>B：はい、（　　　）。",
             correct="どうぞ", distractors=["いけません", "ください", "ありません"],
             en="A: May I sit here? B: Yes, please do.",
             notes_ja="許可を求められて「はい」と答えるので、「どうぞ」が自然です。「いけません」は禁止、「ください」「ありません」は答えとして意味が合いません。",
             notes_en="B says はい to a request for permission, so どうぞ fits. いけません is a prohibition, and ください / ありません make no sense as replies."),
        dict(stem="A：{窓|まど}を{開|あ}けて（　　　）いいですか。<br>B：ええ、どうぞ。",
             correct="も", distractors=["が", "を", "に"],
             en="A: May I open the window? B: Sure, go ahead.",
             notes_ja="「〜てもいいですか」で許可を求める形なので、「も」が入ります。「が」「を」「に」は、て形のあとに付けられません。",
             notes_en="The pattern for asking permission is 〜てもいいですか, so も goes here. が / を / に can't follow a te form."),
        dict(stem="A：ここで{食|た}べてもいいですか。<br>B：すみません。ここでは{食|た}べては（　　　）。",
             correct="いけません", distractors=["いいです", "どうぞ", "ください"],
             en="A: May I eat here? B: Sorry. You may not eat here.",
             notes_ja="「すみません」と断っているので、「食べてはいけません」（禁止）が合います。「食べてはいいです」「食べてはどうぞ」「食べてはください」は日本語として成り立ちません。",
             notes_en="B declines with すみません, so the prohibition 食べてはいけません fits. 食べてはいいです / どうぞ / ください are not valid Japanese."),
    ],
)

# ---------------------------------------------------------------- 8 てはいけない
GRAMMAR[8] = dict(
    name="てはいけない", reading="てはいけない",
    meaning_en="must not do ~ (prohibition)",
    similar="ないでください、てもいい",
    details=dict(
        formula="動詞 て形 ＋ <strong>はいけません</strong>（丁寧）<br>"
                "動詞 て形 ＋ <strong>はいけない</strong>（普通形）　／　<strong>〜てはだめです</strong>（話し言葉）",
        notes_ja="動詞のて形に「はいけません」を付けます。「〜てもいいです」（許可）の反対の意味です。<br>"
                 "例：教室で<strong>走ってはいけません</strong>。／ここで<strong>泳いではいけません</strong>。<br>"
                 "話し言葉では「〜てはだめです」「〜ちゃだめ」とも言います（食べちゃだめ）。"
                 "友達や子どもには「〜てはいけない」「〜てはだめ」を使います。"
                 "「いけません」の部分は変えられません（×いけません→いけます）。",
        notes_en="Add はいけません to the te form; it is the opposite of 〜てもいいです. Examples: 走ってはいけません, 泳いではいけません. "
                 "Colloquially: 〜てはだめです / 〜ちゃだめ (食べちゃだめ). Plain: 〜てはいけない / 〜てはだめ. "
                 "The いけません part doesn't change.",
        nuance_ja="ルール・安全・マナーに基づく強い禁止です。先生が学生に、親が子どもに、規則やポスターで『してはいけない』と伝えるときに使います。"
                  "立場が上の人が下の人に言う感じが強いので、お客さんや目上の人には使わず、「〜ないでください」を使います。"
                  "「走ってはいけません」と「走らないでください」では、前者のほうが『ルールだからだめ』という強い印象です。",
        nuance_en="A strong prohibition based on rules, safety or manners: a teacher to students, a parent to a child, posters and regulations. "
                  "It carries authority, so with customers or superiors use 〜ないでください. 「走ってはいけません」 sounds like "
                  "'it's against the rules', stronger than 「走らないでください」.",
        trap_ja="①辞書形に付けません。×食べるはいけません → ○食べてはいけません<br>"
                "②お客さんなど、立場が上でない人に使うと失礼です。「ここで写真を撮ってはいけません」より「ここでは写真を撮らないでください」が丁寧です。<br>"
                "③「〜てはいけません」（禁止）と「〜なければいけません」（義務：しなければならない）は別です。"
                "「食べてはいけません」＝食べるな、「食べなければいけません」＝食べる必要がある。英語の must not / must と混ぜないでください。<br>"
                "④「できません」とは言いません。×食べてはできません → ○食べてはいけません",
        trap_en="① Not after the dictionary form: ×食べるはいけません. "
                "② It's rude toward customers or equals; prefer 〜ないでください. "
                "③ 〜てはいけません (prohibition) is different from 〜なければいけません (obligation): 食べてはいけません = don't eat, "
                "食べなければいけません = must eat. "
                "④ Don't use できません here: ×食べてはできません → ○食べてはいけません.",
        contrast=[
            dict(type="wrong", sentence="（お{客|きゃく}さんに）ここで{写真|しゃしん}を{撮|と}ってはいけません。",
                 reason_ja="お客さんに「てはいけません」を使うと、命令のように強く聞こえて失礼です。",
                 reason_en="Saying 〜てはいけません to a customer sounds like a harsh order."),
            dict(type="correct", sentence="（お{客|きゃく}さんに）ここでは{写真|しゃしん}を{撮|と}らないでください。",
                 reason_ja="お客さんには「ないでください」でお願いするのが丁寧です。",
                 reason_en="Asking with ないでください is the polite way with customers."),
            dict(type="correct", sentence="{教室|きょうしつ}で{走|はし}ってはいけません。",
                 reason_ja="先生がルールを伝える場面では「てはいけません」が自然です。",
                 reason_en="When a teacher states a rule, 〜てはいけません is natural."),
        ],
        comparison=[
            dict(form="〜てはいけません", form_en="must not (rule)", badge="禁止", badge_type="bad",
                 nuance_ja="ルールや立場に基づく強い禁止です。",
                 nuance_en="A strong prohibition based on rules or authority.",
                 example="ここでたばこを{吸|す}ってはいけません。"),
            dict(form="〜てはだめです", form_en="not allowed (spoken)", badge="話し言葉", badge_type="neutral",
                 nuance_ja="「いけません」より話し言葉的です。親が子どもに言うときなどによく使います。",
                 nuance_en="More colloquial than いけません; common from parents to children.",
                 example="{夜|よる}は{大|おお}きい{声|こえ}を{出|だ}してはだめですよ。"),
            dict(form="〜なければいけません", form_en="must do (obligation)", badge="義務", badge_type="both",
                 nuance_ja="『しなければならない』という反対の意味です（N4の文法）。「てはいけません」と混ぜないでください。",
                 nuance_en="The opposite sense: 'have to do' (an N4 pattern). Don't confuse it with 〜てはいけません.",
                 example="{毎日|まいにち}{薬|くすり}を{飲|の}まなければいけません。"),
        ],
    ),
    quiz=[
        dict(stem="{美術館|びじゅつかん}の{中|なか}では{写真|しゃしん}を{撮|と}っては（　　　）。",
             correct="いけません", distractors=["いいです", "ありません", "ください"],
             en="You must not take photographs inside the museum.",
             notes_ja="「〜ては」のあとに「いけません」を続けて禁止を表します。「撮ってはいいです」「撮ってはありません」「撮ってはください」は文として成り立ちません。",
             notes_en="〜ては is followed by いけません to express a prohibition. 撮ってはいいです / ありません / ください are not valid."),
        dict(stem="{信号|しんごう}が{赤|あか}いとき、{道|みち}を{渡|わた}（　　　）はいけません。",
             correct="って", distractors=["んで", "いで", "いて"],
             en="When the light is red, you must not cross the road.",
             notes_ja="「渡る」は「る」で終わるグループ1の動詞なので、て形は「渡って」です。「渡んで」「渡いで」「渡いて」はどれもて形のルールに合いません。",
             notes_en="渡る ends in る, so the te form is 渡って. 渡んで / 渡いで / 渡いて don't follow the te-form rules."),
        dict(stem="ここで{走|はし}って（　　　）いけません。{他|ほか}の{人|ひと}に{当|あ}たりますから。",
             correct="は", distractors=["を", "が", "に"],
             en="You must not run here. You might bump into other people.",
             notes_ja="禁止は「〜ては＋いけません」の形です。「走ってを」「走ってが」「走ってに」は、て形のあとに付けられません。",
             notes_en="A prohibition is 〜ては + いけません. を / が / に cannot follow a te form."),
        dict(stem="（{子|こ}どもに）{道|みち}で{遊|あそ}んでは（　　　）よ。{車|くるま}が{来|く}るからね。",
             correct="いけない", distractors=["いい", "ない", "ある"],
             en="(To a child) You mustn't play in the street. Cars come by, you know.",
             notes_ja="車が来るから危ない、という文脈なので、普通形の禁止「いけない」が合います。「遊んではいいよ」は反対の意味、「遊んではない」「遊んではある」は文になりません。",
             notes_en="Cars come by, so the plain prohibition いけない fits. 遊んではいいよ would mean the opposite, and 遊んではない / ある are not valid."),
    ],
)

# ---------------------------------------------------------------- 9 から（理由）
GRAMMAR[9] = dict(
    name="から（理由）", reading="から",
    meaning_en="because; so (giving a reason)",
    similar="ので、だから、ですから",
    details=dict(
        formula="<strong>理由</strong>（文）＋ <strong>から</strong>、<strong>結果・依頼・意見</strong>。<br>"
                "動詞・イ形容詞：<strong>行く／行きます＋から</strong>　　名詞・ナ形容詞：<strong>雨だ／雨です＋から</strong><br>"
                "文の頭：<strong>だから／ですから</strong>、〜（＝それで）",
        notes_ja="理由を言う文の最後に「から」を付けて、そのあとに結果や依頼などを続けます。理由 → 結果の順です。<br>"
                 "・動詞・イ形容詞：<strong>忙しいから</strong>行きません。<br>"
                 "・名詞・ナ形容詞：<strong>雨だから／雨ですから</strong>行きません。（×雨から）<br>"
                 "「から」の前は普通形でも丁寧形でもかまいません（忙しいから／忙しいですから）。<br>"
                 "理由を聞く「どうして〜ですか」には、「〜からです」で答えます。<br>"
                 "「から」のあとには、「暑いから、窓を開けてください。」のように、依頼・誘い・意見も続けられます。",
        notes_en="Put から at the end of the reason clause, then follow with the result, request, etc. Reason → result. "
                 "Verbs and i-adjectives: 忙しいから行きません. Nouns and na-adjectives need だ／です: 雨だから／雨ですから (×雨から). "
                 "The part before から can be plain or polite. 「どうして〜ですか」 is answered with 「〜からです」. "
                 "What follows can be a request or suggestion too: 暑いから、窓を{開|あ}けてください.",
        nuance_ja="「から」は、話し手が『これが理由だ』と自分の判断で理由をはっきり示す言い方です。「ので」より主観的で、"
                  "「暑いから窓を開けてください」「明日は試験だから早く寝よう」のように、あとに依頼・誘い・決意を続けるのに向いています。"
                  "文の頭に置く「だから／ですから」は『だから（そういう理由で）〜』と、前の文を理由にして結果を言う接続の言葉です。"
                  "「から」だけで文を終えると、友達との会話では理由を言い訳のように言う感じになります（だって、忙しいから。）。",
        nuance_en="から presents the reason as the speaker's own judgement ('this is why'). It is more subjective than ので and works well "
                  "before requests, suggestions and decisions. A sentence-initial だから／ですから links the previous sentence as the reason. "
                  "Ending a sentence with から alone (忙しいから。) sounds like an explanation or excuse in casual talk.",
        trap_ja="①名詞に直接付けません。×雨から行きません → ○雨ですから／雨だから行きません<br>"
                "②英語の because は理由の前に来ますが、「から」は理由のあとに来ます。×から雨が降っています、行きません → ○雨が降っていますから、行きません<br>"
                "③「だから」は『それで・そういうわけで』という意味で、文の頭に置いて結果を続けます。『なぜなら』という意味ではありません。"
                "理由を言うときは「〜からです」です。<br>"
                "④「から」は『〜から（出発点）』の意味もあります。文の最後の動詞・形容詞に付いたら、理由です。",
        trap_en="① Not directly after a noun: ×雨から → ○雨ですから. "
                "② English 'because' comes first; から comes after the reason: ○雨が降っていますから、行きません. "
                "③ だから means 'therefore' and introduces the result; it does not mean 'because'. To give a reason, end with 〜からです. "
                "④ から also means 'from'; after a verb or adjective it is 'because'.",
        contrast=[
            dict(type="wrong", sentence="{雨|あめ}から、{行|い}きません。",
                 reason_ja="名詞には、「から」の前に「だ／です」が必要です。",
                 reason_en="A noun needs だ／です before から."),
            dict(type="correct", sentence="{雨|あめ}ですから、{行|い}きません。",
                 reason_ja="名詞 ＋ です ＋ から。理由のあとに結果を続けます。",
                 reason_en="Noun + です + から, then the result."),
            dict(type="correct", sentence="{疲|つか}れましたから、{少|すこ}し{休|やす}みましょう。",
                 reason_ja="「から」のあとに、誘いの表現（ましょう）も続けられます。",
                 reason_en="から can be followed by a suggestion such as ましょう."),
        ],
        comparison=[
            dict(form="〜から", form_en="because (subjective)", badge="理由", badge_type="good",
                 nuance_ja="話し手の理由づけをはっきり言います。あとに依頼・誘いが続けられます。",
                 nuance_en="States the speaker's reason clearly; can precede requests or suggestions.",
                 example="{暑|あつ}いですから、{窓|まど}を{開|あ}けてください。"),
            dict(form="〜ので", form_en="because (softer, N4)", badge="柔らかい", badge_type="neutral",
                 nuance_ja="事実を客観的に説明する感じで、お願いや断りを丁寧に言うときに向いています（N4の文法）。",
                 nuance_en="Sounds objective and soft; good for polite refusals and requests (an N4 pattern).",
                 example="{雨|あめ}なので、{行|い}きません。"),
            dict(form="だから／ですから", form_en="therefore (sentence start)", badge="接続", badge_type="both",
                 nuance_ja="文の頭で、前の文を理由にして結果を言います。",
                 nuance_en="At the start of a sentence, it takes the previous sentence as the reason.",
                 example="{雨|あめ}です。ですから、{行|い}きません。"),
        ],
    ),
    quiz=[
        dict(stem="{暑|あつ}い（　　　）、{窓|まど}を{開|あ}けてください。",
             correct="から", distractors=["まで", "より", "でも"],
             en="It's hot, so please open the window.",
             notes_ja="「暑い」が窓を開けてほしい理由なので、理由を表す「から」が入ります。「まで」（終点）「より」（比較）「でも」は、イ形容詞のあとに付けて理由にはなりません。",
             notes_en="The heat is the reason for the request, so から. まで (limit), より (comparison) and でも can't make a reason after an i-adjective."),
        dict(stem="{今日|きょう}は{寒|さむ}いです。（　　　）、コートを{着|き}ましょう。",
             correct="だから", distractors=["でも", "しかし", "ところで"],
             en="It's cold today. So let's put on our coats.",
             notes_ja="寒いことが理由で、結果が「コートを着ましょう」なので「だから」です。「でも」「しかし」は逆のことを言うときの言葉、「ところで」は話題を変えるときの言葉で、ここでは合いません。",
             notes_en="Cold is the reason and putting on coats is the result: だから. でも / しかし introduce contrast and ところで changes the subject."),
        dict(stem="A：どうして{昨日|きのう}は{来|き}ませんでしたか。<br>B：{風邪|かぜ}を{引|ひ}いた（　　　）です。",
             correct="から", distractors=["のに", "より", "へ"],
             en="A: Why didn't you come yesterday? B: Because I caught a cold.",
             notes_ja="「どうして」にたいする答えは「〜からです」です。「風邪を引いたのにです」「風邪を引いたよりです」「風邪を引いたへです」は文になりません。",
             notes_en="The answer to どうして is 〜からです. The other options make no sense after 風邪を引いた."),
        dict(stem="{明日|あした}は{試験|しけん}がある（　　　）、{今晩|こんばん}は{遊|あそ}びません。",
             correct="から", distractors=["まで", "より", "だけ"],
             en="I have an exam tomorrow, so I won't go out and play tonight.",
             notes_ja="試験があることが、遊ばない理由です。「から」が入ります。「試験があるまで」「〜より」「〜だけ」では、後ろの文と理由・結果のつながりができません。",
             notes_en="The exam is the reason not to play, so から. まで / より / だけ don't create a reason–result link."),
    ],
)

# ---------------------------------------------------------------- 10 から〜まで
GRAMMAR[10] = dict(
    name="から〜まで", reading="からまで",
    meaning_en="from ~ to ~ (time, place, range)",
    similar="までに、に",
    details=dict(
        formula="<strong>N1</strong> ＋ <strong>から</strong> ＋ <strong>N2</strong> ＋ <strong>まで</strong>（時間・場所・範囲）<br>"
                "例：9時<strong>から</strong>5時<strong>まで</strong>　／　家<strong>から</strong>駅<strong>まで</strong>",
        notes_ja="「から」は始まり（出発点）、「まで」は終わり（終点）を表します。<br>"
                 "・時間：9時から5時まで働きます。　・場所：家から駅まで歩きます。　・範囲：1ページから10ページまで読みます。<br>"
                 "どちらか一つだけでも使えます：9時から始まります。／駅まで行きます。<br>"
                 "「かかります」と一緒に：家から駅まで10分かかります。<br>"
                 "質問：何時から何時までですか。／どこからどこまでですか。／何日から何日までですか。<br>"
                 "「まで」は、その時までずっと続く動作に使います。1回の動作の時刻は「に」です（6時<strong>に</strong>起きます／6時<strong>まで</strong>寝ます）。",
        notes_en="から marks the start, まで marks the end. Time: 9時から5時まで; place: 家から駅まで; range: 1ページから10ページまで. "
                 "Either can be used alone (9時から始まります／駅まで行きます). With かかります: 家から駅まで10分かかります. "
                 "まで is for something that continues up to that point; a single point in time takes に (6時に起きます / 6時まで寝ます).",
        nuance_ja="始まりから終わりまでの『範囲』を示します。時間・距離・数量のどれにも使えて、営業時間、授業の時間、道のり、予定の期間などを言うときに必ず出てくる、"
                  "基本の組み合わせです。「まで」は『そこまで（含めて）ずっと』という気持ちで、動作や状態が途中で途切れず続くことを表します。"
                  "「から」が理由の意味（gid 9）になる文と形が同じなので、前後に「N1から N2まで」の形があれば範囲の意味になります。",
        nuance_en="It shows a range from start to end — hours, distance, quantity. It is how opening hours, class times, routes and "
                  "periods are expressed. まで carries the sense 'all the way up to (and including)', so the action or state continues without a break. "
                  "Unlike から meaning 'because', here the N1から N2まで frame makes it a range.",
        trap_ja="①時刻の「に」と「まで」を混ぜません。×銀行は9時に3時まで開いています → ○9時から3時まで<br>"
                "②「から」を忘れて「まで」だけにすると、始まりが分かりません。「9時まで」は『9時が終わり』という意味です。<br>"
                "③期限（その時刻より前に終える）は「まで」ではなく「までに」です。×5時まで来てください（5時までずっと来る？）→ ○5時までに来てください（N4の文法）<br>"
                "④順番に注意：家から駅まで＝家が出発、駅が到着。駅から家まで＝逆です。<br>"
                "⑤「駅までです」の「まで」は『駅が終点』です。「駅で歩く」は『駅の中で歩く』になり、意味が変わります。",
        trap_en="① Don't mix the point-in-time に with まで: ×9時に3時まで → ○9時から3時まで. "
                "② Using まで alone only gives the end: 「9時まで」 means 'until 9'. "
                "③ A deadline is までに, not まで: ×5時まで来てください → ○5時までに来てください (N4). "
                "④ Mind the order: 家から駅まで = home to station. "
                "⑤ 「駅で歩く」 means 'walk inside the station'; to say 'walk as far as the station', use 駅まで.",
        contrast=[
            dict(type="wrong", sentence="{銀行|ぎんこう}は9{時|じ}に3{時|じ}まで{開|あ}いています。",
                 reason_ja="始まりは「に」ではなく「から」で表します。「9時から3時まで」が範囲の形です。",
                 reason_en="The start is marked by から, not に: 9時から3時まで."),
            dict(type="correct", sentence="{銀行|ぎんこう}は9{時|じ}から3{時|じ}まで{開|あ}いています。",
                 reason_ja="9時（始まり）から3時（終わり）までの範囲を表します。",
                 reason_en="Shows the range from 9 (start) to 3 (end)."),
            dict(type="correct", sentence="{家|いえ}から{駅|えき}まで、{歩|ある}いて10{分|ぷん}かかります。",
                 reason_ja="場所の出発点と終点にも使えます。「かかります」と一緒によく使います。",
                 reason_en="It also marks the start and end of a route, often with かかります."),
        ],
        comparison=[
            dict(form="〜に（時刻）", form_en="at (a point in time)", badge="時点", badge_type="both",
                 nuance_ja="1回の動作が起きる時刻を表します。続く動作の終わりの時刻ではありません。",
                 nuance_en="Marks the moment a single action happens, not the end of a continuing one.",
                 example="{私|わたし}は6{時|じ}に{起|お}きます。"),
            dict(form="〜まで", form_en="until", badge="継続", badge_type="good",
                 nuance_ja="その時刻まで動作・状態がずっと続くことを表します。",
                 nuance_en="The action or state continues until that time.",
                 example="{私|わたし}は{毎朝|まいあさ}、7{時|じ}まで{寝|ね}ています。"),
            dict(form="〜までに", form_en="by (deadline, N4)", badge="期限", badge_type="neutral",
                 nuance_ja="その時刻より前に、動作を一度すませる期限を表します。「まで」とは意味が違います（N4の文法）。",
                 nuance_en="A deadline: the action must happen once before that time. Different from まで (N4 pattern).",
                 example="5{時|じ}までに{来|き}てください。"),
        ],
    ),
    quiz=[
        dict(stem="{図書館|としょかん}は{月曜日|げつようび}から{金曜日|きんようび}（　　　）{開|あ}いています。",
             correct="まで", distractors=["に", "を", "で"],
             en="The library is open from Monday to Friday.",
             notes_ja="「月曜日から」と始まりがあるので、終わりは「金曜日まで」です。「に」「を」「で」は「月曜日から金曜日」の範囲の終わりには使えません。",
             notes_en="The start is 月曜日から, so the end is 金曜日まで. に / を / で can't mark the end of the range."),
        dict(stem="{家|いえ}（　　　）{駅|えき}まで、{歩|ある}いて10{分|ふん}かかります。",
             correct="から", distractors=["まで", "に", "を"],
             en="It takes ten minutes to walk from my house to the station.",
             notes_ja="「駅まで」が終点なので、出発点の「家」には「から」を付けます。「家まで駅まで」「家に駅まで」「家を駅まで」は意味が通りません。",
             notes_en="駅まで is the end point, so the starting point 家 takes から. The other options make no sense."),
        dict(stem="{昨日|きのう}は{夜|よる}8{時|じ}から12{時|じ}（　　　）{勉強|べんきょう}しました。",
             correct="まで", distractors=["に", "を", "で"],
             en="Yesterday I studied from 8 p.m. until 12.",
             notes_ja="「8時から」の始まりに対して、終わりは「12時まで」です。「12時に」は一つの時刻になってしまい、「から」とセットになりません。",
             notes_en="After 8時から, the end is 12時まで. 12時に would be a single point and doesn't pair with から."),
        dict(stem="A：{夏休|なつやす}みは（　　　）{何日|なんにち}までですか。<br>B：7月20日から8月31日までです。",
             correct="{何日|なんにち}から", distractors=["{何日|なんにち}まで", "{何日|なんにち}に", "{何日|なんにち}を"],
             en="A: From what date to what date is the summer vacation? B: From July 20 to August 31.",
             notes_ja="あとに「何日までですか」が続くので、前は始まりを聞く「何日から」です。「何日までですか」を二回重ねたり、「に」「を」を入れたりはできません。",
             notes_en="Since 何日までですか follows, the first part asks the start: 何日から. Repeating まで or using に / を doesn't work."),
    ],
)

# ---------------------------------------------------------------- 11 ましょう
GRAMMAR[11] = dict(
    name="ましょう", reading="ましょう",
    meaning_en="let's ~ (inviting someone to do something together)",
    similar="ませんか、ましょうか",
    details=dict(
        formula="動詞 ます形（語幹）＋ <strong>ましょう</strong><br>"
                "例：食べ<strong>ましょう</strong>　行き<strong>ましょう</strong>　し<strong>ましょう</strong>　{来|き}<strong>ましょう</strong><br>"
                "返事：はい、〜ましょう／ええ、そうしましょう　　断り：すみません、ちょっと…",
        notes_ja="動詞のます形（語幹）に「ましょう」を付けます（食べます→食べましょう、行きます→行きましょう）。"
                 "「一緒に」「みんなで」「そろそろ」「さあ」などと一緒によく使います。<br>"
                 "誘われたときの返事は、「はい、〜ましょう」「いいですね。そうしましょう」。断るときは、「すみません、ちょっと…」と柔らかく言います。<br>"
                 "教室や活動で、先生やリーダーが全員に呼びかけるときにも使います：では、始めましょう。／本を読みましょう。<br>"
                 "名詞や形容詞には付きません。",
        notes_en="Attach ましょう to the ます stem (食べます→食べましょう). Common with 一緒に, みんなで, そろそろ, さあ. "
                 "Accept with 「はい、〜ましょう」 / 「いいですね。そうしましょう」; decline softly: 「すみません、ちょっと…」. "
                 "Teachers and leaders also use it to address everyone (本を読みましょう). It doesn't attach to nouns or adjectives.",
        nuance_ja="話し手が、相手と一緒に何かをしようと呼びかける言い方です。「ましょう」は、話し手の気持ちが決まっていて、"
                  "相手にも同じ行動を求めるので、「ませんか」より積極的で直接的です。そのため、親しい人や同じ立場の人との会話、"
                  "先生が学生へ呼びかける場面に向いています。相手の気持ちを大切にして誘うときは、「ませんか」のほうが柔らかく聞こえます。"
                  "「頑張りましょう」のように、みんなを励ます使い方もあります。",
        nuance_en="The speaker calls on the listener to do something together. Because the speaker has already decided, it is more direct "
                  "than ませんか, so it suits friends, peers and teachers addressing a class. ませんか sounds softer when you want to "
                  "respect the other person's feelings. It can also encourage a group (頑張りましょう).",
        trap_ja="①辞書形に付けません。×行くましょう → ○行きましょう<br>"
                "②自分だけの予定には使いません。×私は明日、一人で買い物に行きましょう → ○行きます。「ましょう」は『相手と一緒に』という意味が必要です。<br>"
                "③目上の人を誘うときは、「ましょう」より「ませんか」のほうが丁寧です。×先生、食べましょう → ○先生、一緒に食べませんか。<br>"
                "④『〜するのはやめよう』という誘いは「行きませんましょう」ではなく、「行くのをやめましょう」と言います。<br>"
                "⑤英語の Let's と同じ形で、否定の Let's not は作れません。",
        trap_en="① Not after the dictionary form: ×行くましょう. "
                "② Not for your own solo plans: ×私は明日、一人で買い物に行きましょう → ○行きます. "
                "③ For a superior, ませんか is more polite than ましょう. "
                "④ 'Let's not' is not ×行きませんましょう; say 行くのをやめましょう. "
                "⑤ It mirrors English 'Let's', but you cannot form 'Let's not' from it.",
        contrast=[
            dict(type="wrong", sentence="{一緒|いっしょ}に{帰|かえ}るましょう。",
                 reason_ja="「ましょう」はます形（語幹）に付けます。「帰る」は「帰り」にして「帰りましょう」です。",
                 reason_en="ましょう attaches to the stem: 帰る → 帰り → 帰りましょう."),
            dict(type="correct", sentence="{一緒|いっしょ}に{帰|かえ}りましょう。",
                 reason_ja="帰る → 帰り ＋ ましょう。『一緒にしよう』と呼びかけます。",
                 reason_en="帰る → 帰り + ましょう: 'let's go home together'."),
            dict(type="correct", sentence="{天気|てんき}がいいですから、{公園|こうえん}へ{行|い}きましょう。",
                 reason_ja="理由（から）のあとに誘いを続けられます。",
                 reason_en="A suggestion can follow a reason with から."),
        ],
        comparison=[
            dict(form="〜ませんか", form_en="Won't you ~?", badge="柔らかい誘い", badge_type="good",
                 nuance_ja="相手の気持ちを聞く形で誘います。目上の人にも使えて、「ましょう」より丁寧で柔らかいです。",
                 nuance_en="Invites by asking the listener's wishes; softer and more polite than ましょう, fine for superiors.",
                 example="{一緒|いっしょ}に{昼|ひる}ごはんを{食|た}べませんか。"),
            dict(form="〜ましょうか", form_en="Shall we / shall I ~?", badge="提案・申し出", badge_type="both",
                 nuance_ja="相手に確認しながら提案したり、自分がすることを申し出たりします（gid 12）。",
                 nuance_en="Checks with the listener while proposing, or offers to do something yourself (see gid 12).",
                 example="そろそろ{帰|かえ}りましょうか。"),
            dict(form="〜よう／〜おう（友達に）", form_en="casual 'let's'", badge="普通形", badge_type="neutral",
                 nuance_ja="友達・家族との会話での「ましょう」にあたる普通形です（食べよう・行こう）。",
                 nuance_en="The plain-form counterpart of ましょう with friends and family (食べよう, 行こう).",
                 example="{一緒|いっしょ}に{行|い}こう。"),
        ],
    ),
    quiz=[
        dict(stem="A：おなかがすきましたね。<br>B：そうですね。{一緒|いっしょ}に{昼|ひる}ごはんを{食|た}べ（　　　）。",
             correct="ましょう", distractors=["ません", "でしょう", "ました"],
             en="A: I'm hungry. B: Me too. Let's have lunch together.",
             notes_ja="お腹がすいたという話から、「一緒に食べよう」と誘う「ましょう」が入ります。「食べません」は否定、「食べでしょう」は形が間違い、「食べました」はもう食べた意味で、文脈に合いません。",
             notes_en="After 'I'm hungry', an invitation ましょう fits. 食べません is negative, 食べでしょう is malformed, and 食べました means already eaten."),
        dict(stem="A：{今度|こんど}の{日曜日|にちようび}、{一緒|いっしょ}に{映画|えいが}を{見|み}ませんか。<br>B：いいですね。（　　　）。",
             correct="{見|み}ましょう", distractors=["{見|み}ません", "{見|み}ました", "{見|み}ないでください"],
             en="A: Why don't we see a movie together this Sunday? B: Sounds good. Let's.",
             notes_ja="「いいですね」と賛成したあとなので、誘いに応える「見ましょう」です。「見ません」「見ないでください」は断る意味、「見ました」は過去で、どれも「いいですね」に合いません。",
             notes_en="After agreeing with いいですね, accept with 見ましょう. 見ません / 見ないでください would refuse, and 見ました is past."),
        dict(stem="{皆|みな}さん、{一緒|いっしょ}に{大|おお}きい{声|こえ}で{読|よ}み（　　　）。",
             correct="ましょう", distractors=["ません", "ました", "ですか"],
             en="Everyone, let's read it aloud together.",
             notes_ja="先生がみんなに呼びかける場面なので、「読みましょう」です。「読みません」「読みました」は呼びかけにならず、「読みですか」は形が間違いです。",
             notes_en="A teacher addressing everyone: 読みましょう. 読みません / 読みました aren't calls to act, and 読みですか is malformed."),
        dict(stem="もう10{時|じ}です。そろそろ{帰|かえ}り（　　　）。",
             correct="ましょう", distractors=["ません", "ました", "ましたか"],
             en="It's already ten o'clock. Let's head home soon.",
             notes_ja="「そろそろ」はこれからの行動に使う言葉なので、「帰りましょう」と提案します。「帰りません」は否定、「帰りました」「帰りましたか」は過去で、「そろそろ」と合いません。",
             notes_en="そろそろ refers to an upcoming action, so the proposal 帰りましょう. 帰りません is negative, and 帰りました / 帰りましたか are past."),
    ],
)

# ---------------------------------------------------------------- 12 ましょうか
GRAMMAR[12] = dict(
    name="ましょうか", reading="ましょうか",
    meaning_en="shall I ~? / shall we ~? (offer / suggestion)",
    similar="ましょう、ませんか、てもいいですか",
    details=dict(
        formula="動詞 ます形（語幹）＋ <strong>ましょうか</strong><br>"
                "① 申し出：荷物を<strong>持ちましょうか</strong>。（私が〜しましょうか）<br>"
                "② 提案・相談：何を<strong>食べましょうか</strong>。（私たちは〜しましょうか）",
        notes_ja="動詞のます形（語幹）に「ましょうか」を付けます。使い方は2つです。<br>"
                 "① <strong>申し出</strong>（Shall I ~?）：相手のために、自分がすることを申し出ます。<br>"
                 "　重そうですね。持ちましょうか。―ありがとうございます。お願いします。／いいえ、大丈夫です。<br>"
                 "② <strong>提案・相談</strong>（Shall we ~?）：どうするか、相手と相談しながら提案します。疑問詞とよく使います。<br>"
                 "　どこで会いましょうか。―駅の前はどうですか。／そうしましょう。<br>"
                 "断るときは、「いいえ、いいです」より「大丈夫です」「けっこうです。ありがとうございます」が分かりやすいです。",
        notes_en="Attach ましょうか to the ます stem. Two uses: (1) an offer ('Shall I ~?'): 持ちましょうか; "
                 "(2) a suggestion or consultation ('Shall we ~?'), often with question words: どこで会いましょうか. "
                 "To decline an offer, 「大丈夫です」 / 「けっこうです」 is clearer than 「いいえ、いいです」.",
        nuance_ja="「ましょうか」は、相手の意向を聞きながら提案する言い方です。申し出の場合は、相手が『お願いします』か『大丈夫です』かを自由に選べるので、"
                  "親切で押しつけがましくありません。提案の場合も、「ましょう」より相手の意見を尊重する感じがあります。"
                  "困っている人を見かけたときの申し出（手伝いましょうか）は、日常生活で一番よく使われる使い方です。",
        nuance_en="ましょうか proposes something while leaving the choice to the listener. As an offer, the listener can freely say 'yes please' or "
                  "'no thanks', so it is kind and not pushy. As a suggestion, it respects the listener's opinion more than ましょう. "
                  "Offering help to someone in need (手伝いましょうか) is its most common everyday use.",
        trap_ja="①「ましょうか」は自分がすることの申し出です。相手に頼むときには使いません。×（友達に）このかばんを持ちましょうか。（『持ってください』の意味では使えません）<br>"
                "②相手の予定を聞くときに使いません。×あなたは何を食べましょうか → ○あなたは何を食べますか。<br>"
                "③「いいえ、いいです」は断りですが、『いい＝OK』に聞こえて、返事が分かりにくくなります。「大丈夫です」を使いましょう。<br>"
                "④×食べるましょうか。ます形（語幹）に付けます。<br>"
                "⑤英語の Shall I ~? とよく似ていますが、「Would you like me to ~?」くらいの気持ちで使うと自然です。",
        trap_en="① It offers YOUR action; you can't use it to ask someone else: ×(to a friend) このかばんを持ちましょうか meaning 'could you hold this?'. "
                "② Don't use it to ask what the listener will do: ×あなたは何を食べましょうか → ○食べますか. "
                "③ 「いいえ、いいです」 is ambiguous; say 「大丈夫です」. "
                "④ ×食べるましょうか — attach to the stem. "
                "⑤ It resembles 'Shall I ~?' but feels more like 'Would you like me to ~?'.",
        contrast=[
            dict(type="wrong", sentence="（{友達|ともだち}に{頼|たの}む）ちょっと、このかばんを{持|も}ちましょうか。",
                 reason_ja="「ましょうか」は自分がすることを申し出る形です。相手に持ってもらうお願いには使えません。",
                 reason_en="ましょうか offers your own action; it can't ask someone else to hold the bag."),
            dict(type="correct", sentence="ちょっと、このかばんを{持|も}ってください。",
                 reason_ja="相手にしてもらうお願いは「〜てください」です。",
                 reason_en="Asking someone else to do it is 〜てください."),
            dict(type="correct", sentence="{荷物|にもつ}、{持|も}ちましょうか。",
                 reason_ja="自分が持つことを申し出る正しい使い方です。",
                 reason_en="The correct use: offering to carry the luggage yourself."),
        ],
        comparison=[
            dict(form="〜ましょうか", form_en="Shall I / Shall we ~?", badge="申し出・提案", badge_type="good",
                 nuance_ja="相手の意向を聞きながら、自分の行動を申し出たり提案したりします。",
                 nuance_en="Offers or proposes while checking the listener's wishes.",
                 example="{窓|まど}を{閉|し}めましょうか。"),
            dict(form="〜ましょう", form_en="Let's ~", badge="誘い", badge_type="both",
                 nuance_ja="話し手が決めて、一緒にしようと呼びかけます。確認はしません。",
                 nuance_en="The speaker has decided and calls for joint action; no checking.",
                 example="{窓|まど}を{閉|し}めましょう。"),
            dict(form="〜ますか", form_en="Do you ~?", badge="質問", badge_type="neutral",
                 nuance_ja="相手がするかどうか、または予定を聞く普通の質問です。申し出ではありません。",
                 nuance_en="A plain question about whether or what the listener does; not an offer.",
                 example="{窓|まど}を{閉|し}めますか。"),
        ],
    ),
    quiz=[
        dict(stem="A：{荷物|にもつ}が{重|おも}そうですね。{私|わたし}が{持|も}ち（　　　）。<br>B：ありがとうございます。お{願|ねが}いします。",
             correct="ましょうか", distractors=["ませんか", "ますか", "ました"],
             en="A: That luggage looks heavy. Shall I carry it? B: Thank you. Yes, please.",
             notes_ja="相手のために自分が持つことを申し出る「持ちましょうか」です。「持ちませんか」は一緒に持つ誘い、「持ちますか」は質問、「持ちました」は過去で、申し出になりません。",
             notes_en="An offer to carry it for the other person: 持ちましょうか. 持ちませんか is an invitation, 持ちますか a question, 持ちました past."),
        dict(stem="A：{今晩|こんばん}、{何|なに}を{食|た}べ（　　　）。<br>B：そうですね。カレーはどうですか。",
             correct="ましょうか", distractors=["ました", "ません", "ましたか"],
             en="A: What shall we have for dinner tonight? B: Hmm, how about curry?",
             notes_ja="二人で何を食べるか相談する場面なので、「食べましょうか」です。「食べました」「食べましたか」は過去、「食べません」は否定で、これからの相談には合いません。",
             notes_en="Two people deciding what to eat: 食べましょうか. 食べました / 食べましたか are past and 食べません is negative."),
        dict(stem="A：{雨|あめ}ですね。{駅|えき}まで{車|くるま}で{送|おく}り（　　　）。<br>B：えっ、いいんですか。ありがとうございます。",
             correct="ましょうか", distractors=["ません", "ました", "ますか"],
             en="A: It's raining. Shall I drive you to the station? B: Really? Thank you.",
             notes_ja="Aが送ることを申し出ているので、「送りましょうか」が自然です。「送りません」「送りました」は断りや過去になり、「送りますか」は申し出になりません。",
             notes_en="A is offering to give a lift: 送りましょうか. 送りません / 送りました are refusal or past, and 送りますか isn't an offer."),
        dict(stem="A：{手伝|てつだ}いましょうか。<br>B：ありがとうございます。じゃあ、（　　　）。",
             correct="お{願|ねが}いします", distractors=["いただきます", "いってきます", "おやすみなさい"],
             en="A: Shall I help you? B: Thank you. Then, yes please.",
             notes_ja="申し出を受けるときの返事は「お願いします」です。「いただきます」は食事の前、「いってきます」は出かけるとき、「おやすみなさい」は寝る前のあいさつです。",
             notes_en="To accept an offer, say お願いします. いただきます is said before eating, いってきます when leaving home, おやすみなさい before bed."),
    ],
)
