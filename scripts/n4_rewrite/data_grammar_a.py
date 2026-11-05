# -*- coding: utf-8 -*-
"""
N4 grammar textbook details + practice questions, gids 1-31 (hand-authored).
Format: see build_grammar.py docstring.

Shorthand: in Japanese detail strings the words ます形 / て形 / ない形 / た形 / 辞書形 / 普通形 are
auto-converted by _J() at the bottom of the file into R()-friendly explicit ruby ({形|けい} etc.).
"""

GRAMMAR = {}

# ---------------------------------------------------------------- 1 なければならない
GRAMMAR[1] = dict(
    name="なければならない", reading="なければならない",
    meaning_en="must do ~; have to do ~",
    similar="なくてはならない、ないといけない、なくてもいい",
    details=dict(
        formula="<strong>動詞ない形</strong>（い → <strong>ければならない</strong>）<br>"
                "丁寧形：<strong>〜なければなりません</strong><br>"
                "※「する」→ しなければならない ／ 「来る」→ {来|こ}なければならない",
        notes_ja="動詞の「ない形」の最後の「い」を取って、「ければならない（丁寧：ければなりません）」を付けます。"
                 "『〜しないといけない』『義務や必要があって、ぜひそうする』という意味を表します。<br>"
                 "例：{毎日|まいにち}{薬|くすり}を<strong>{飲|の}まなければなりません</strong>。<br>"
                 "会話では「〜なきゃ（いけない）」「〜ないと」のように短く言うことも多いですが、"
                 "きちんとした会話や文章では「〜なければなりません」を使います。",
        notes_en="Drop the final い of a verb's ない-form and add ければならない (polite: ければなりません) to express obligation or necessity ('must / have to'). "
                 "In casual speech it often contracts to 〜なきゃ or 〜ないと, while 〜なければなりません is standard in polite speech and writing.",
        nuance_ja="規則・法律・約束・仕事や学校の義務など、『自分の気持ちに関係なく、やらなければならないこと』によく使います。"
                  "「なくてはならない」とほぼ同じ意味ですが、「なければならない」のほうが少し硬く、書き言葉や公的な場面でもよく使われます。"
                  "否定の「〜なくてもいい（する必要がない）」とセットで覚えましょう。",
        nuance_en="Used for obligations arising from rules, laws, promises, school, or work regardless of personal preference. "
                  "Nearly synonymous with なくてはならない, though なければならない sounds slightly more formal and is very common in writing. "
                  "Learn it as a pair with its opposite 〜なくてもいい ('don't have to').",
        trap_ja="①「ない形」の「い」を残さないこと。×飲まないければならない → ○{飲|の}まなければならない<br>"
                "②「する」「来る」の「ない形」に注意。×すなければならない → ○しなければならない ／ ×来なければならない（き） → ○{来|こ}なければならない<br>"
                "③『〜する必要がない』と言いたいときに「〜なければならないではない」とは言いません。「〜なくてもいいです」を使います。",
        trap_en="① Drop the い of ない: ×飲まないければならない → ○飲まなければならない. "
                "② Watch irregular verbs: する → しなければならない, 来る → 来(こ)なければならない. "
                "③ The negative ('don't have to') is 〜なくてもいい, not ×なければならないではない.",
        contrast=[
            dict(type="wrong", sentence="{明日|あした}は{早|はや}く{起|お}きないければなりません。",
                 reason_ja="「ない形」の「い」を取ってから「ければなりません」を付けます。",
                 reason_en="Drop the final い of the ない-form before adding ければなりません."),
            dict(type="correct", sentence="{明日|あした}は{早|はや}く{起|お}きなければなりません。",
                 reason_ja="「起きない」の「い」を取って「起きなければなりません」にします。",
                 reason_en="起きない minus い + ければなりません."),
            dict(type="correct", sentence="{今日|きょう}中にこの{書類|しょるい}を{出|だ}さなければならない。",
                 reason_ja="普通形は「〜なければならない」です。",
                 reason_en="The plain form is 〜なければならない."),
        ],
        comparison=[
            dict(form="〜なければならない", form_en="must do (standard/formal)", badge="義務・標準", badge_type="good",
                 nuance_ja="規則や義務を表すもっとも標準的な言い方です。話し言葉でも書き言葉でも使えます。",
                 nuance_en="The standard expression for obligation or duty, suitable for both speech and writing.",
                 example="{金曜日|きんようび}までに{本|ほん}を{返|かえ}さなければなりません。"),
            dict(form="〜なくてはならない", form_en="must do (slightly softer)", badge="義務・会話", badge_type="both",
                 nuance_ja="意味はほぼ同じですが、少し会話向きで柔らかい響きがあります。",
                 nuance_en="Almost identical meaning, slightly more conversational in tone.",
                 example="そろそろ{家|いえ}を{出|で}なくてはなりません。"),
            dict(form="〜なくてもいい", form_en="don't have to", badge="不必要", badge_type="neutral",
                 nuance_ja="義務の否定（しなくても問題ない）を表します。",
                 nuance_en="Expresses lack of necessity ('don't have to').",
                 example="{明日|あした}は{来|こ}なくてもいいですよ。"),
        ],
    ),
    quiz=[
        dict(stem="{明日|あした}は{朝|あさ}{早|はや}く{出|で}かけるので、{今夜|こんや}は{早|はや}く（　　　）。",
             correct="{寝|ね}なければなりません",
             distractors=["{寝|ね}ないければなりません", "{寝|ね}るなければなりません", "{寝|ね}なくてもいいです"],
             en="Since I'm leaving early tomorrow morning, I have to go to bed early tonight.",
             notes_ja="「寝る」のない形「寝ない」から「い」を取って「寝なければなりません」にします。「寝ないければ」「寝るなければ」は接続の誤りです。",
             notes_en="Drop い from 寝ない and add ければなりません. 寝ないければ and 寝るなければ are ungrammatical."),
        dict(stem="この{図書館|としょかん}で{借|か}りた{本|ほん}は、2{週間|しゅうかん}{以内|いない}に（　　　）。",
             correct="{返|かえ}さなければなりません",
             distractors=["{返|かえ}しなければなりません", "{返|かえ}すなければなりません", "{返|かえ}さなくてもいいです"],
             en="Books borrowed from this library must be returned within two weeks.",
             notes_ja="五段動詞「返す」のない形は「返さない」なので、「返さなければなりません」になります。「返しない」とは言いません。",
             notes_en="The ない-form of 返す (u-verb) is 返さない, giving 返さなければなりません. ×返しない is wrong."),
        dict(stem="{外国|がいこく}へ{旅行|りょこう}に{行|い}くときは、パスポートを（　　　）。",
             correct="{持|も}って{行|い}かなければならない",
             distractors=["{持|も}って{行|い}きなければならない", "{持|も}って{行|い}くなければならない", "{持|も}って{行|い}かないければならない"],
             en="When traveling abroad, you must take your passport with you.",
             notes_ja="「持って行く」のない形「持って行かない」の「い」を「ければならない」に変えます。",
             notes_en="Replace the final い of 持って行かない with ければならない."),
        dict(stem="{午後|ごご}から{大切|たいせつ}な{会議|かいぎ}があるので、1{時|じ}までに{会社|かいしゃ}へ（　　　）。",
             correct="{戻|もど}らなければなりません",
             distractors=["{戻|もど}りなければなりません", "{戻|もど}るなければなりません", "{戻|もど}らないければなりません"],
             en="There is an important meeting in the afternoon, so I must return to the office by 1 o'clock.",
             notes_ja="「戻る」のない形は「戻らない」です。「い」を取って「戻らなければなりません」にします。",
             notes_en="The ない-form of 戻る is 戻らない; drop い and add ければなりません."),
    ],
)

# ---------------------------------------------------------------- 2 なくてはならない
GRAMMAR[2] = dict(
    name="なくてはならない", reading="なくてはならない",
    meaning_en="must do ~; have to do ~",
    similar="なければならない、なくてはいけない、なくてもいい",
    details=dict(
        formula="<strong>動詞ない形</strong>（い → <strong>くてはならない</strong>）<br>"
                "丁寧形：<strong>〜なくてはなりません</strong> ／ <strong>〜なくてはいけません</strong><br>"
                "会話の短縮形：<strong>〜なくちゃ（いけない）</strong>",
        notes_ja="動詞の「ない形」の最後の「い」を「くてはならない（丁寧：くてはなりません）」に変えます。"
                 "『〜しないと困る・〜する必要がある』という義務や必要を表します。<br>"
                 "例：もう8{時|じ}だから、<strong>{行|い}かなくてはなりません</strong>。<br>"
                 "日常会話では「〜なくてはいけません」や、さらにくだけた「〜なくちゃ」の形もよく使われます。",
        notes_en="Replace the final い of a verb's ない-form with くてはならない (polite: くてはなりません) to express necessity or obligation ('must / have to'). "
                 "In everyday conversation, 〜なくてはいけません and the casual contraction 〜なくちゃ are very common.",
        nuance_ja="「〜なければならない」と意味は同じですが、「〜なくてはならない」は『そうしないと良くない結果になる』という気持ちが少し強く、"
                  "日常の生活習慣や身近な予定について話すときによく使われます。"
                  "短縮形は「なくては → なくちゃ」「なければ → なきゃ」と対応しています。",
        nuance_en="Same core meaning as 〜なければならない, but 〜なくてはならない feels slightly more tied to everyday personal situations ('if I don't do this, it won't do'). "
                  "Note the matching casual contractions: なくては → なくちゃ, なければ → なきゃ.",
        trap_ja="①「ない形」の「い」を残さないこと。×行かないくてはならない → ○{行|い}かなくてはならない<br>"
                "②肯定の「て形」に付けないこと。×行ってはならない（※これは『行ってはいけない＝禁止』の意味になってしまいます！）<br>"
                "③「〜なくてはならない」と「〜てはならない（禁止）」を混同しないように注意しましょう。",
        trap_en="① Drop the い of ない: ×行かないくてはならない → ○行かなくてはならない. "
                "② Never use the affirmative て-form: 行ってはならない means 'must NOT go' (prohibition), the exact opposite! "
                "③ Carefully distinguish 〜なくてはならない (must do) from 〜てはならない (must not do).",
        contrast=[
            dict(type="wrong", sentence="この{薬|くすり}は{食後|しょくご}に{飲|の}んではなりません。",
                 reason_ja="「飲んではなりません（て形＋はならない）」は『飲むな（禁止）』という意味になってしまいます。",
                 reason_en="飲んではなりません (て-form + はならない) means 'must NOT drink' (prohibition)."),
            dict(type="correct", sentence="この{薬|くすり}は{食後|しょくご}に{飲|の}まなくてはなりません。",
                 reason_ja="『飲む必要がある』は「ない形」から作って「飲まなくてはなりません」と言います。",
                 reason_en="To say 'must drink', build from the ない-form: 飲まなくてはなりません."),
            dict(type="correct", sentence="{今日|きょう}は{夕飯|ゆうはん}を{作|つく}らなくてはならない。",
                 reason_ja="「作らない」の「い」を「くてはならない」に変えた正しい形です。",
                 reason_en="Correct form built from 作らない."),
        ],
        comparison=[
            dict(form="〜なくてはならない", form_en="must do", badge="義務", badge_type="good",
                 nuance_ja="『しないといけない』という義務・必要を表します。会話では「〜なくちゃ」になります。",
                 nuance_en="Expresses obligation ('have to do'). Contracts to 〜なくちゃ in casual speech.",
                 example="{宿題|しゅくだい}を{終|お}わらせなくてはなりません。"),
            dict(form="〜てはならない／〜てはいけない", form_en="must NOT do (prohibition)", badge="禁止", badge_type="bad",
                 nuance_ja="肯定の「て形」に付くと『してはいけない（禁止）』という反対の意味になります。",
                 nuance_en="Attached to the affirmative て-form, it means 'must NOT do' (prohibition).",
                 example="ここで{写真|しゃしん}を{撮|と}ってはいけません。"),
            dict(form="〜なければならない", form_en="must do (standard)", badge="義務・書き言葉", badge_type="both",
                 nuance_ja="「なくてはならない」とほぼ同じですが、より硬い文章にも広く使われます。",
                 nuance_en="Nearly identical, used even more widely in formal writing.",
                 example="{規則|きそく}を{守|まも}らなければならない。"),
        ],
    ),
    quiz=[
        dict(stem="もうすぐ{電車|でんしゃ}が{来|く}るから、{急|いそ}いで{切符|きっぷ}を（　　　）。",
             correct="{買|か}わなくてはなりません",
             distractors=["{買|か}ってはなりません", "{買|か}わなくていいです", "{買|か}うなくてはなりません"],
             en="The train is coming soon, so I have to hurry and buy a ticket.",
             notes_ja="「買う」のない形は「買わない」なので、「買わなくてはなりません」が正解です。「買ってはなりません」は『買うな（禁止）』の意味になります。",
             notes_en="From 買わない we get 買わなくてはなりません. 買ってはなりません means 'must not buy'."),
        dict(stem="{明日|あした}の{朝|あさ}までに、このレポートを（　　　）。",
             correct="{書|か}き{終|お}わらなくてはならない",
             distractors=["{書|か}き{終|お}わってはならない", "{書|か}き{終|お}わらないくてはならない", "{書|か}き{終|お}わるなくてはならない"],
             en="I have to finish writing this report by tomorrow morning.",
             notes_ja="「書き終わらない」の「い」を「くてはならない」に変えます。「書き終わってはならない」は禁止になってしまいます。",
             notes_en="Change the final い of 書き終わらない to くてはならない."),
        dict(stem="{引|ひ}っ{越|こ}しの{前|まえ}に、{部屋|へや}の{中|なか}をきれいに（　　　）。",
             correct="{掃除|そうじ}しなくてはなりません",
             distractors=["{掃除|そうじ}してはなりません", "{掃除|そうじ}しないくてはなりません", "{掃除|そうじ}するなくてはなりません"],
             en="Before moving out, I must clean the inside of the room thoroughly.",
             notes_ja="「掃除する」のない形は「掃除しない」なので、「掃除しなくてはなりません」になります。",
             notes_en="The ない-form of 掃除する is 掃除しない, giving 掃除しなくてはなりません."),
        dict(stem="{母|はは}が{入院|にゅういん}しているので、{今日|きょう}は{私|わたし}が{晩|ばん}ご{飯|はん}の{支度|したく}を（　　　）。",
             correct="しなくてはなりません",
             distractors=["してはなりません", "すなくてはなりません", "しないくてはなりません"],
             en="Because my mother is in the hospital, I have to prepare dinner today.",
             notes_ja="「する」のない形「しない」から「しなくてはなりません」を作ります。「してはなりません」は禁止の意味です。",
             notes_en="Build from しない → しなくてはなりません. してはなりません means 'must not do'."),
    ],
)

# ---------------------------------------------------------------- 3 なくてもいい
GRAMMAR[3] = dict(
    name="なくてもいい", reading="なくてもいい",
    meaning_en="don't have to; need not do",
    similar="なければならない、てもいい、なくてもかまわない",
    details=dict(
        formula="<strong>動詞ない形</strong>（い → <strong>くてもいい</strong>）<br>"
                "<strong>イ形容詞</strong>（い → <strong>くなくてもいい</strong>）<br>"
                "<strong>ナ形容詞・名詞</strong> ＋ <strong>でなくてもいい（じゃなくてもいい）</strong>",
        notes_ja="動詞の「ない形」の「い」を取って「くてもいい（です）」を付けると、『〜する必要がない』『〜しなくても大丈夫だ』という意味になります。<br>"
                 "例：{靴|くつ}を<strong>{脱|ぬ}がなくてもいいです</strong>。<br>"
                 "形容詞や名詞にも使えます。例：{高|たか}くなくてもいい／{今日|きょう}でなくてもいいです。<br>"
                 "「いい」の代わりに「かまいません（〜なくてもかまいません）」を使うと、より丁寧な表現になります。",
        notes_en="Drop the final い of the ない-form and add くてもいい(です) to mean 'don't have to / need not'. "
                 "It also works with i-adjectives (高くなくてもいい) and na-adjectives/nouns (暇でなくてもいい / 今日でなくてもいい). "
                 "Replacing いい with かまいません sounds more polite.",
        nuance_ja="「〜なければなりませんか（しなければいけませんか）」という質問に対して、"
                  "「いいえ、〜なくてもいいですよ」と答えるパターンがとてもよく使われます。"
                  "『してはいけない』ではなく、『してもいいし、しなくてもいい（無理にしなくて大丈夫）』という優しい許可のニュアンスです。",
        nuance_en="Frequently used to answer 'Must I ~?' (〜なければなりませんか): 'No, you don't have to' (いいえ、〜なくてもいいですよ). "
                  "It does NOT mean 'must not'; it reassures the listener that doing the action is optional.",
        trap_ja="①「〜てもいい（許可：してもいい）」と「〜なくてもいい（不必要：しなくて大丈夫）」は1文字違いなので、意味を取り違えないこと。<br>"
                "②「ない形」の「い」を残さないこと。×行かないくてもいい → ○{行|い}かなくてもいい<br>"
                "③「いい（良い）」の否定ではないので、「よくない」にしないこと。",
        trap_en="① Distinguish 〜てもいい ('may do') from 〜なくてもいい ('don't have to do'). "
                "② Drop the い of ない: ×行かないくてもいい → ○行かなくてもいい. "
                "③ Keep いい at the end (it means 'it is okay if you don't').",
        contrast=[
            dict(type="wrong", sentence="{明日|あした}は{休|やす}みですから、{会社|かいしゃ}へ{行|い}かないくてもいいです。",
                 reason_ja="「行かない」の「い」を取ってから「くてもいいです」を付けます。",
                 reason_en="Drop the い of 行かない before adding くてもいいです."),
            dict(type="correct", sentence="{明日|あした}は{休|やす}みですから、{会社|かいしゃ}へ{行|い}かなくてもいいです。",
                 reason_ja="「行かない」→「行かなくてもいいです」が正しい形です。",
                 reason_en="Correct form: 行かない → 行かなくてもいいです."),
            dict(type="correct", sentence="{全部|ぜんぶ}{食|た}べなくてもいいですよ。",
                 reason_ja="『無理に全部食べる必要はない』という意味です。",
                 reason_en="Means 'You don't have to eat it all.'"),
        ],
        comparison=[
            dict(form="〜なくてもいい", form_en="don't have to do", badge="不必要", badge_type="good",
                 nuance_ja="『する必要がない』という意味です。「〜なければなりませんか」への否定の返事に使います。",
                 nuance_en="Means 'need not do'. Used as the negative reply to 〜なければなりませんか.",
                 example="{名前|なまえ}は{書|か}かなくてもいいです。"),
            dict(form="〜てもいい", form_en="may do / it's okay to do", badge="許可", badge_type="both",
                 nuance_ja="肯定の「て形」に付き、『〜してもかまわない（許可）』を表します。",
                 nuance_en="Attaches to the affirmative て-form to grant permission ('may do').",
                 example="ここに{座|すわ}ってもいいですよ。"),
            dict(form="〜てはいけない", form_en="must not do", badge="禁止", badge_type="bad",
                 nuance_ja="『してはいけない（禁止）』を表します。英語の don't have to と must not の違いと同じです。",
                 nuance_en="Expresses prohibition ('must not'), just like the difference between 'don't have to' and 'must not'.",
                 example="ここに{車|くるま}を{止|と}めてはいけません。"),
        ],
    ),
    quiz=[
        dict(stem="A：{靴|くつ}を{脱|ぬ}がなければなりませんか。<br>B：いいえ、そのまま{入|はい}ってください。（　　　）よ。",
             correct="{脱|ぬ}がなくてもいいです",
             distractors=["{脱|ぬ}いでもいいです", "{脱|ぬ}がなければなりません", "{脱|ぬ}がないくてもいいです"],
             en="A: Do I have to take off my shoes? B: No, please come in as you are. You don't have to take them off.",
             notes_ja="「そのまま入ってください」と言っているので、『脱ぐ必要はない』という意味の「脱がなくてもいいです」が正解です。",
             notes_en="Since B says 'come in as you are', the meaning is 'you don't need to take them off' (脱がなくてもいいです)."),
        dict(stem="{簡単|かんたん}な{言葉|ことば}で{書|か}いてあるので、{辞書|じしょ}を（　　　）{分|わ}かります。",
             correct="{使|つか}わなくても",
             distractors=["{使|つか}わなければ", "{使|つか}わないくても", "{使|つか}うなくても"],
             en="Because it is written in simple words, you can understand it without having to use a dictionary.",
             notes_ja="「使わなくても分かります」で『辞書を使う必要がなく、そのまま分かる』という意味になります。",
             notes_en="使わなくても分かります means 'you can understand it even without using a dictionary'."),
        dict(stem="{熱|ねつ}が{下|さ}がったから、もうこの{薬|くすり}は（　　　）と{医者|いしゃ}に{言|い}われました。",
             correct="{飲|の}まなくてもいい",
             distractors=["{飲|の}まなければならない", "{飲|の}まないくてもいい", "{飲|の}むなくてもいい"],
             en="Since my fever went down, I was told by the doctor that I don't have to take this medicine anymore.",
             notes_ja="熱が下がったので、薬を『飲む必要がない』＝「飲まなくてもいい」が文脈に合います。",
             notes_en="Since the fever is gone, the doctor said 'you no longer need to take it' (飲まなくてもいい)."),
        dict(stem="{明日|あした}は{時間|じかん}がたくさんあるから、そんなに{早|はや}く（　　　）よ。",
             correct="{起|お}きなくてもいいです",
             distractors=["{起|お}きなければなりません", "{起|お}きないくてもいいです", "{起|お}きてはいけません"],
             en="We have plenty of time tomorrow, so you don't have to wake up that early.",
             notes_ja="「起きる」のない形「起きない」から「い」を取って「起きなくてもいいです」にします。",
             notes_en="Drop い from 起きない and add くてもいいです."),
    ],
)

# ---------------------------------------------------------------- 4 たことがある
GRAMMAR[4] = dict(
    name="たことがある", reading="たことがある",
    meaning_en="have the experience of doing ~; have done ~ before",
    similar="ことがある（時々）、たばかりだ",
    details=dict(
        formula="<strong>動詞た形</strong> ＋ <strong>ことがある／ことがあります</strong><br>"
                "否定（一度もない）：<strong>〜たことがない／〜たことがありません</strong>",
        notes_ja="動詞の「た形」に「ことがある（丁寧：ことがあります）」を付けると、これまでにその経験があること（『〜した経験がある』）を表します。<br>"
                 "例：{私|わたし}は{北海道|ほっかいどう}へ<strong>{行|い}ったことがあります</strong>。<br>"
                 "一度も経験がないときは「〜たことがありません」と言います。「{一度|いちど}も〜たことがありません」「{何回|なんかい}か〜たことがあります」のような言葉とよく一緒に使います。",
        notes_en="Attach ことがある / ことがあります to the た-form of a verb to talk about past life experience ('have done ~ before'). "
                 "The negative is 〜たことがない / ありません ('have never done ~'), often paired with 一度も ('not even once').",
        nuance_ja="過去の『経験』を話す表現なので、「{昨日|きのう}」「{先週|せんしゅう}」のような近い過去の特定の時点を表す言葉とは一緒に使いません。"
                  "昨日の出来事を言うときは、普通の過去形「{昨日|きのう}、{映画|えいが}を{見|み}ました」を使います。",
        nuance_en="Because it expresses general life experience up to now, it is NOT used with specific recent time words like 昨日 ('yesterday') or 先週 ('last week'). "
                  "For a single recent event, use the simple past (昨日、映画を見ました).",
        trap_ja="①「昨日〜たことがある」「今朝〜たことがある」とは言いません。×{昨日|きのう}お{寿司|すし}を{食|た}べたことがあります → ○{昨日|きのう}お{寿司|すし}を{食|た}べました<br>"
                "②辞書形に「ことがある」を付けると『時々〜する（現在の習慣・たまにあること）』という別の意味になります。経験は必ず「た形」を使います。<br>"
                "③否定は「〜なかったことがある」ではなく「〜たことがない」が基本です。",
        trap_en="① Don't pair it with specific recent times like 昨日 or 今朝: ×昨日お寿司を食べたことがあります → ○昨日お寿司を食べました. "
                "② Verb dictionary form + ことがある means 'sometimes happens to do'; experience MUST use the た-form. "
                "③ To say 'have never done', use 〜たことがない (not ×〜なかったことがある).",
        contrast=[
            dict(type="wrong", sentence="{昨日|きのう}、{新|あたら}しいレストランへ{行|い}ったことがあります。",
                 reason_ja="「昨日」のような特定の近い過去の出来事には「〜たことがあります」は使えません。",
                 reason_en="Don't use 〜たことがあります for a specific event yesterday; use the simple past 行きました."),
            dict(type="correct", sentence="{私|わたし}は{富士山|ふじさん}に{登|のぼ}ったことがあります。",
                 reason_ja="これまでの人生の経験を述べるときに「た形＋ことがあります」を使います。",
                 reason_en="Use た-form + ことがあります to state a life experience."),
            dict(type="correct", sentence="{私|わたし}は{一度|いちど}もスキーをしたことがありません。",
                 reason_ja="「一度も〜たことがありません」で『経験がゼロだ』と強調できます。",
                 reason_en="一度も〜たことがありません emphasizes having zero experience."),
        ],
        comparison=[
            dict(form="動詞た形 ＋ ことがある", form_en="have done before (experience)", badge="経験", badge_type="good",
                 nuance_ja="過去に一度でもその経験があることを表します。",
                 nuance_en="States that you have experienced doing something at least once in the past.",
                 example="{馬|うま}に{乗|の}ったことがあります。"),
            dict(form="動詞辞書形 ＋ ことがある", form_en="sometimes do / occasionally happens", badge="時々", badge_type="both",
                 nuance_ja="辞書形に付くと『たま〜にそういうことがある』という現在の頻度を表します。",
                 nuance_en="With the dictionary form, it means 'occasionally happens to do ~'.",
                 example="{朝寝坊|あさねぼう}してバスに{遅|おく}れることがあります。"),
            dict(form="動詞た形（〜ました）", form_en="did ~ (simple past)", badge="過去の事実", badge_type="neutral",
                 nuance_ja="「昨日」「先週」など、いつの出来事かを普通に話すときに使います。",
                 nuance_en="Simple past fact at a specific time such as yesterday or last week.",
                 example="{先週|せんしゅう}、{京都|きょうと}へ{行|い}きました。"),
        ],
    ),
    quiz=[
        dict(stem="A：{日本|にほん}の{着物|きもの}を（　　　）か。<br>B：はい、{去年|きょねん}{京都|きょうと}で{一度|いちど}だけ{着|き}ました。",
             correct="{着|き}たことがあります",
             distractors=["{着|き}ることがあります", "{着|き}たことがいます", "{着|き}てことがあります"],
             en="A: Have you ever worn a Japanese kimono? B: Yes, I wore one just once in Kyoto last year.",
             notes_ja="過去の経験を聞くので「た形＋ことがありますか」を使います。「着ることがあります」は『時々着る』という意味になります。",
             notes_en="Use た-form + ことがありますか to ask about past experience. 着ることがあります means 'sometimes wear'."),
        dict(stem="{私|わたし}は{生|う}まれてから{一度|いちど}も{飛行機|ひこうき}に（　　　）。",
             correct="{乗|の}ったことがありません",
             distractors=["{乗|の}ることはありません", "{乗|の}らなかったことがあります", "{乗|の}ってことがありません"],
             en="I have never been on an airplane since I was born.",
             notes_ja="「一度も〜たことがありません」で『一度も経験がない』ことを表します。",
             notes_en="一度も〜たことがありません expresses having never experienced something."),
        dict(stem="あの{有名|ゆうめい}な{歌手|かしゅ}を、{一度|いちど}{駅|えき}で（　　　）。",
             correct="{見|み}たことがあります",
             distractors=["{見|み}ることがあります", "{見|み}てことがあります", "{見|み}たことがいます"],
             en="I have seen that famous singer once at the station.",
             notes_ja="「一度〜で見た」という過去の経験なので、「見たことがあります」が正解です。",
             notes_en="Seeing the singer once in the past is an experience: 見たことがあります."),
        dict(stem="A：この{果物|くだもの}を{食|た}べたことがありますか。<br>B：いいえ、{名前|なまえ}も（　　　）。",
             correct="{聞|き}いたことがありません",
             distractors=["{聞|き}くことがありません", "{聞|き}いてことがありません", "{聞|き}かなかったことがあります"],
             en="A: Have you ever eaten this fruit? B: No, I have never even heard its name.",
             notes_ja="『名前を聞いた経験もない』という意味なので、「た形＋ことがありません」にします。",
             notes_en="Means 'I haven't even heard the name before': 聞いたことがありません."),
    ],
)

# ---------------------------------------------------------------- 5 ほうがいい
GRAMMAR[5] = dict(
    name="ほうがいい", reading="ほうがいい",
    meaning_en="had better do ~; should do ~",
    similar="たらいい、なければならない",
    details=dict(
        formula="するべき（肯定の助言）：<strong>動詞た形</strong> ＋ <strong>{方|ほう}がいい（です）</strong><br>"
                "しないべき（否定の助言）：<strong>動詞ない形</strong> ＋ <strong>{方|ほう}がいい（です）</strong>",
        notes_ja="相手にアドバイス（助言）や忠告をするときに使います。<br>"
                 "『〜したほうがいい』と言うときは、これからすることでも<strong>「た形」</strong>を使います。<br>"
                 "例：{熱|ねつ}があるなら、{病院|びょういん}へ<strong>{行|い}った{方|ほう}がいいですよ</strong>。<br>"
                 "反対に『〜しないほうがいい』と言うときは、<strong>「ない形」</strong>をそのまま使います。<br>"
                 "例：{夜遅|よるおそ}くに甘い物を<strong>{食|た}べない{方|ほう}がいいです</strong>。",
        notes_en="Used to give advice or a recommendation ('had better / should'). "
                 "For positive advice, use the **た-form** + ほうがいい even though the action is in the future (病院へ行ったほうがいい). "
                 "For negative advice ('had better not'), use the **ない-form** + ほうがいい (食べないほうがいい).",
        nuance_ja="「た形＋ほうがいい」は、具体的な場面で『こうしたほうがいいよ！』とはっきり勧める表現です。"
                  "ただし、目上の人（先生や上司）に「〜たほうがいいですよ」と言うと、少し上から目線（おせっかい）に聞こえることがあります。"
                  "会話では語尾に「〜たほうがいいですよ」「〜たほうがいいんじゃないですか」を付けると柔らかくなります。",
        nuance_en="た-form + ほうがいい gives clear, concrete advice for a specific situation. "
                  "Because it sounds quite direct ('you'd better ~'), avoid using it directly toward superiors. "
                  "Adding よ or んじゃないですか softens it in conversation.",
        trap_ja="①肯定のアドバイスでは、これからすることでも「辞書形」ではなく「た形」が自然です（辞書形は一般的なことわざのような文脈に限られます）。<br>"
                "②否定のアドバイスは「なかったほうがいい」ではなく「ない形＋ほうがいい」です。×行かなかったほうがいい → ○{行|い}かない{方|ほう}がいい<br>"
                "③「{方|ほう}」の読み{方|かた}は「かた」ではなく「<strong>ほう</strong>」です。",
        trap_en="① Positive advice for a specific situation uses the た-form (行ったほうがいい), not the dictionary form. "
                "② Negative advice uses the present ない-form (行かないほうがいい), NOT ×行かなかったほうがいい. "
                "③ Here 方 is read ほう, not かた.",
        contrast=[
            dict(type="wrong", sentence="お{腹|なか}が{痛|いた}いなら、{冷|つめ}たい{水|みず}は{飲|の}まなかった{方|ほう}がいいですよ。",
                 reason_ja="否定のアドバイスは「なかった」ではなく現在の「ない形」を使います。",
                 reason_en="Negative advice uses the present ない-form (飲まない), not 飲まなかった."),
            dict(type="correct", sentence="お{腹|なか}が{痛|いた}いなら、{冷|つめ}たい{水|みず}は{飲|の}まない{方|ほう}がいいですよ。",
                 reason_ja="「ない形＋ほうがいい」で『〜しないほうがいい』という助言になります。",
                 reason_en="ない-form + ほうがいい means 'you had better not ~'."),
            dict(type="correct", sentence="{雨|あめ}が{降|ふ}りそうだから、{傘|かさ}を{持|も}って{行|い}った{方|ほう}がいいよ。",
                 reason_ja="肯定のアドバイスは「た形＋ほうがいい」を使います。",
                 reason_en="Positive advice uses た-form + ほうがいい."),
        ],
        comparison=[
            dict(form="動詞た形 ＋ {方|ほう}がいい", form_en="had better do ~", badge="肯定の助言", badge_type="good",
                 nuance_ja="これからの行動について『そうするべきだ』と強く勧めます。",
                 nuance_en="Recommends taking an action ('you should / had better do ~').",
                 example="{早|はや}めに{予約|よやく}した{方|ほう}がいいですよ。"),
            dict(form="動詞ない形 ＋ {方|ほう}がいい", form_en="had better not do ~", badge="否定の助言", badge_type="bad",
                 nuance_ja="『そうしないほうがいい』と止めるアドバイスです。",
                 nuance_en="Advises against doing something ('you had better not ~').",
                 example="{無理|むり}をしない{方|ほう}がいいです。"),
            dict(form="〜たらどうですか", form_en="why don't you ~?", badge="提案", badge_type="neutral",
                 nuance_ja="「〜たほうがいい」より押しつけがましくなく、軽く提案する言い方です。",
                 nuance_en="A gentler suggestion ('why don't you ~?') than 〜たほうがいい.",
                 example="{先生|せんせい}に{相談|そうだん}したらどうですか。"),
        ],
    ),
    quiz=[
        dict(stem="{顔色|かおいろ}があまりよくないですね。{今日|きょう}は{早|はや}く{帰|かえ}って（　　　）よ。",
             correct="{休|やす}んだ{方|ほう}がいいです",
             distractors=["{休|やす}むの{方|ほう}がいいです", "{休|やす}んで{方|ほう}がいいです", "{休|やす}まない{方|ほう}がいいです"],
             en="You don't look very well. You had better go home early and rest today.",
             notes_ja="肯定のアドバイスなので「た形＋ほうがいい」＝「休んだほうがいいです」にします。動詞と「{方|ほう}」の間に「の」は入りません。",
             notes_en="Positive advice uses た-form + ほうがいい (休んだほうがいいです). Do not insert の."),
        dict(stem="この{道|みち}は{夜|よる}になるととても{暗|くら}いから、{一人|ひとり}で（　　　）よ。",
             correct="{歩|ある}かない{方|ほう}がいいです",
             distractors=["{歩|ある}かなかった{方|ほう}がいいです", "{歩|ある}いた{方|ほう}がいいです", "{歩|ある}くなく{方|ほう}がいいです"],
             en="This street gets very dark at night, so you had better not walk alone.",
             notes_ja="『一人で歩かないほうがいい』という否定の助言なので、「ない形＋ほうがいい」（歩かないほうがいいです）が正解です。",
             notes_en="Negative advice uses the ない-form + ほうがいい: 歩かないほうがいいです."),
        dict(stem="{連休|れんきゅう}はホテルがすぐいっぱいになるから、{今|いま}すぐ（　　　）。",
             correct="{予約|よやく}した{方|ほう}がいい",
             distractors=["{予約|よやく}して{方|ほう}がいい", "{予約|よやく}しない{方|ほう}がいい", "{予約|よやく}するの{方|ほう}がいい"],
             en="Hotels fill up quickly during the holidays, so you should make a reservation right now.",
             notes_ja="これから予約する場合でも、具体的な助言には「た形＋ほうがいい」（予約したほうがいい）を使います。",
             notes_en="Even for a future action, concrete positive advice takes た-form + ほうがいい."),
        dict(stem="のどが{痛|いた}いときは、あまり{辛|から}い{料理|りょうり}は（　　　）と{思|おも}います。",
             correct="{食|た}べない{方|ほう}がいい",
             distractors=["{食|た}べなかった{方|ほう}がいい", "{食|た}べた{方|ほう}がいい", "{食|た}べないの{方|ほう}がいい"],
             en="When you have a sore throat, I think you had better not eat very spicy food.",
             notes_ja="のどが痛いときに{辛|から}い料理は控えるべきなので、否定の助言「食べないほうがいい」が正解です。",
             notes_en="Advising against spicy food when having a sore throat requires ない-form + ほうがいい."),
    ],
)

# ---------------------------------------------------------------- 6 すぎる
GRAMMAR[6] = dict(
    name="すぎる", reading="すぎる",
    meaning_en="too much; excessively ~",
    similar="やすい、にくい、とても",
    details=dict(
        formula="<strong>動詞ます形</strong>（ますを取る） ＋ <strong>すぎる／すぎます</strong><br>"
                "<strong>イ形容詞</strong>（い を取る） ＋ <strong>すぎる／すぎます</strong><br>"
                "<strong>ナ形容詞</strong>（な を取る） ＋ <strong>すぎる／すぎます</strong><br>"
                "※「ない」→ なさすぎる（例：{少|すく}なすぎる／お金がなさすぎる）",
        notes_ja="動詞や形容詞の後ろに付けて、『程度をこえている（〜しすぎる／あまりに〜だ）』という意味を表します。<br>"
                 "例：{昨日|きのう}はケーキを<strong>{食|た}べすぎました</strong>。<br>"
                 "例：このかばんは<strong>{大|おお}きすぎます</strong>。／この{問題|もんだい}は<strong>{簡単|かんたん}すぎます</strong>。<br>"
                 "「〜すぎる」全体は<strong>二類動詞（一段動詞・る動詞）</strong>として活用します（すぎます・すぎて・すぎない・すぎた）。",
        notes_en="Attach すぎる to a verb stem (ます-form minus ます), an i-adjective stem (minus い), or a na-adjective stem (minus な) to mean 'too ~ / do ~ too much'. "
                 "The resulting word conjugates as a regular ichidan (ru) verb: すぎます, すぎて, すぎない, すぎた.",
        nuance_ja="基本的には『度がすぎていて良くない・困る』というマイナスの気持ちで使われます（食べすぎた、高すぎる、難しすぎる）。"
                  "ただし、会話では「おもしろすぎる」「おいしすぎる」のように、プラスのことを強調するためにもよく使われます。",
        nuance_en="Primarily expresses an undesirable excess ('too expensive', 'ate too much'). "
                  "In casual speech, however, it is also widely used for emphatic praise (おいしすぎる 'so delicious!').",
        trap_ja="①イ形容詞の「い」や動詞の「ます」を残さないこと。×高いすぎる → ○{高|たか}すぎる ／ ×食べますすぎる → ○{食|た}べすぎる<br>"
                "②ナ形容詞に「だ」や「な」を残さないこと。×静かなすぎる → ○{静|しず}かすぎる<br>"
                "③「いい」は「よすぎる」になります。×いすぎる → ○よすぎる",
        trap_en="① Drop い from i-adjectives and ます from verbs: ×高いすぎる → ○高すぎる. "
                "② Drop な/だ from na-adjectives: ×静かなすぎる → ○静かすぎる. "
                "③ いい becomes よすぎる.",
        contrast=[
            dict(type="wrong", sentence="このシャツは{高|たか}いすぎて、{買|か}えません。",
                 reason_ja="イ形容詞の「い」を取ってから「すぎる（すぎて）」を付けます。",
                 reason_en="Drop the final い of the i-adjective before すぎる."),
            dict(type="correct", sentence="このシャツは{高|たか}すぎて、{買|か}えません。",
                 reason_ja="「高い」の「い」を取って「高すぎて」にします。",
                 reason_en="高い minus い + すぎて = 高すぎて."),
            dict(type="correct", sentence="{夕飯|ゆうはん}を{食|た}べすぎて、お{腹|なか}がいっぱいです。",
                 reason_ja="動詞のます形（食べ）＋ すぎて。",
                 reason_en="Verb stem (食べ) + すぎて."),
        ],
        comparison=[
            dict(form="〜すぎる", form_en="too ~ / do ~ too much", badge="過度", badge_type="bad",
                 nuance_ja="適当な限度をこえてしまって困る、というニュアンスがあります。",
                 nuance_en="Exceeds a reasonable limit, usually with an undesirable result.",
                 example="テレビを{見|み}すぎて{目|め}が{疲|つか}れました。"),
            dict(form="とても ＋ 形容詞", form_en="very ~", badge="程度が高い", badge_type="good",
                 nuance_ja="単に程度が高いことを表し、『困る』というマイナスの意味はありません。",
                 nuance_en="Simply means 'very ~' without implying excess or a problem.",
                 example="このケーキはとてもおいしいです。"),
            dict(form="あまり〜ない", form_en="not very ~", badge="程度が低い", badge_type="neutral",
                 nuance_ja="否定形と一緒に使って『それほど〜ではない』を表します。",
                 nuance_en="Used with a negative predicate to mean 'not very ~'.",
                 example="このテストはあまり{難|むずか}しくなかったです。"),
        ],
    ),
    quiz=[
        dict(stem="{昨日|きのう}の{晩|ばん}はコーヒーを（　　　）、なかなか{眠|ねむ}れませんでした。",
             correct="{飲|の}みすぎて",
             distractors=["{飲|の}むすぎて", "{飲|の}んですぎて", "{飲|の}みやすくて"],
             en="Last night I drank too much coffee and couldn't fall asleep easily.",
             notes_ja="「飲みます」の「ます」を取って「飲みすぎて」にします。「飲むすぎて」「飲んですぎて」は接続の誤りです。",
             notes_en="Attach すぎて to the verb stem 飲み (from 飲みます)."),
        dict(stem="このズボンは{私|わたし}には（　　　）ので、もう{少|すこ}し{短|みじか}いのがいいです。",
             correct="{長|なが}すぎる",
             distractors=["{長|なが}いすぎる", "{長|なが}くすぎる", "{長|なが}さすぎる"],
             en="These pants are too long for me, so I'd like a slightly shorter pair.",
             notes_ja="イ形容詞「長い」の「い」を取って「長すぎる」にします。「長いすぎる」「長くすぎる」は誤りです。",
             notes_en="Drop い from 長い and add すぎる → 長すぎる."),
        dict(stem="テストの{問題|もんだい}が（　　　）、{最後|さいご}まで{書|か}くことができませんでした。",
             correct="{難|むずか}しすぎて",
             distractors=["{難|むずか}しいすぎて", "{難|むずか}しくすぎて", "{難|むずか}しさすぎて"],
             en="The test questions were too difficult, so I couldn't finish writing to the end.",
             notes_ja="「難しい」の「い」を取って「難しすぎて」にします。",
             notes_en="Drop い from 難しい and add すぎて → 難しすぎて."),
        dict(stem="{夜|よる}の{公園|こうえん}は（　　　）ので、{一人|ひとり}で{歩|ある}くのは{少|すこ}し{怖|こわ}いです。",
             correct="{静|しず}かすぎる",
             distractors=["{静|しず}かなすぎる", "{静|しず}かにすぎる", "{静|しず}かだすぎる"],
             en="The park at night is too quiet, so walking alone is a little scary.",
             notes_ja="ナ形容詞「静か（な）」は「な・だ」を取って、そのまま「静かすぎる」にします。",
             notes_en="For na-adjectives like 静か, attach すぎる directly to the stem: 静かすぎる."),
    ],
)

# ---------------------------------------------------------------- 7 やすい
GRAMMAR[7] = dict(
    name="やすい", reading="やすい",
    meaning_en="easy to do ~; likely to ~",
    similar="にくい、すぎる",
    details=dict(
        formula="<strong>動詞ます形</strong>（ますを取る） ＋ <strong>やすい（です）</strong><br>"
                "※イ形容詞として活用します（やすくない／やすかった／やすくて）",
        notes_ja="動詞の「ます形」から「ます」を取って「やすい」を付けます。意味は2つあります。<br>"
                 "①<strong>『〜するのが簡単だ・使いやすい』</strong><br>"
                 "例：このペンはとても<strong>{書|か}きやすいです</strong>。／この{辞書|じしょ}は<strong>{使|つか}いやすいです</strong>。<br>"
                 "②<strong>『すぐ〜の状態になる・〜する傾向がある』</strong><br>"
                 "例：{冬|ふゆ}はかぜを<strong>ひきやすいです</strong>。／このコップは{薄|うす}くて<strong>{割|わ}れやすいです</strong>。",
        notes_en="Attach やすい to a verb stem (ます-form minus ます). It has two meanings: "
                 "(1) 'easy to do' (このペンは書きやすい 'this pen is easy to write with'), and "
                 "(2) 'tends to / likely to happen' (冬はかぜをひきやすい 'it's easy to catch a cold in winter'). "
                 "It conjugates as an i-adjective (やすくない, やすくて).",
        nuance_ja="対象（ペン・靴・道・説明など）の性質として『それを使う人にとって楽だ・やりやすい』と言いたいときに使います。"
                  "反対語は「〜にくい（やりにくい・簡単には〜しない）」です。"
                  "漢字で「安い（値段が安い）」と書かないように、いつもひらがなで「やすい」と書きます。",
        nuance_en="Describes an inherent quality of an object or situation that makes an action effortless or frequent. "
                  "Its opposite is 〜にくい ('hard to do / unlikely to'). "
                  "Always write 〜やすい in hiragana (never with the kanji 安い 'cheap').",
        trap_ja="①辞書形やて形に付けないこと。×書くやすい・×書いてやすい → ○{書|か}きやすい<br>"
                "②イ形容詞として活用するので、否定は「〜やすくない」、て形は「〜やすくて」です。<br>"
                "③テストの問題などが『簡単だ』と言うときは、単に「この問題は{易|やさ}しい／{簡単|かんたん}だ」と言うほうが自然です。",
        trap_en="① Attach to the ます-stem only: ×書くやすい / ×書いてやすい → ○書きやすい. "
                "② It conjugates like an i-adjective: やすくない, やすくて. "
                "③ Write it in hiragana, not 安い.",
        contrast=[
            dict(type="wrong", sentence="この{靴|くつ}は{軽|かる}くて、とても{歩|ある}くやすいです。",
                 reason_ja="辞書形「歩く」ではなく、ます形の「歩き」に「やすい」を付けます。",
                 reason_en="Attach やすい to the ます-stem 歩き, not the dictionary form 歩く."),
            dict(type="correct", sentence="この{靴|くつ}は{軽|かる}くて、とても{歩|ある}きやすいです。",
                 reason_ja="「歩きます」の「ます」を取って「歩きやすいです」にします。",
                 reason_en="歩きます minus ます + やすいです = 歩きやすいです."),
            dict(type="correct", sentence="{春|はる}は{天気|てんき}が{変|か}わりやすいです。",
                 reason_ja="『すぐ変わる傾向がある』という2つ目の意味です。",
                 reason_en="Second meaning: 'tends to change easily'."),
        ],
        comparison=[
            dict(form="〜やすい", form_en="easy to do / likely to", badge="容易・傾向", badge_type="good",
                 nuance_ja="する方法や道具の性質が良くて『楽にできる』、または『よく起こる』ことを表します。",
                 nuance_en="Easy to do because of the item's design/nature, or prone to happening.",
                 example="{林|はやし}{先生|せんせい}の{説明|せつめい}は{分|わ}かりやすいです。"),
            dict(form="〜にくい", form_en="hard to do / unlikely to", badge="困難", badge_type="bad",
                 nuance_ja="「〜やすい」の反対で、『やりにくい・なかなか〜しない』を表します。",
                 nuance_en="Opposite of 〜やすい: hard to do or resistant to happening.",
                 example="この{漢字|かんじ}は{覚|おぼ}えにくいです。"),
            dict(form="〜すぎる", form_en="do ~ too much", badge="過度", badge_type="neutral",
                 nuance_ja="同じ「ます形接続」ですが、『度がすぎる』という意味になります。",
                 nuance_en="Also attaches to the ます-stem, but means 'do ~ excessively'.",
                 example="{買|か}いすぎないように{気|き}をつけます。"),
        ],
    ),
    quiz=[
        dict(stem="このカメラは{小|ちい}さくて{軽|かる}いので、{旅行|りょこう}に（　　　）です。",
             correct="{持|も}って{行|い}きやすい",
             distractors=["{持|も}って{行|い}くやすい", "{持|も}って{行|い}きにくい", "{持|も}って{行|い}きすぎる"],
             en="Because this camera is small and light, it is easy to take on trips.",
             notes_ja="「小さくて軽い」というプラスの理由があるので、『楽に持って行ける』＝「持って行きやすい」が正解です。",
             notes_en="Because it is small and light, it is 'easy to carry' (持って行きやすい)."),
        dict(stem="{字|じ}が{大|おお}きくて、{絵|え}もたくさんあるので、この{本|ほん}はとても（　　　）です。",
             correct="{読|よ}みやすい",
             distractors=["{読|よ}むやすい", "{読|よ}んでやすい", "{読|よ}みにくい"],
             en="With large print and lots of pictures, this book is very easy to read.",
             notes_ja="「読みます」の「ます」を取って「読みやすい」にします。字が大きくて絵も多いので「読みにくい」は合いません。",
             notes_en="Large letters and pictures make it 'easy to read': 読みやすい."),
        dict(stem="{季節|きせつ}の{変|か}わり{目|め}は、かぜを（　　　）から{気|き}をつけてくださいね。",
             correct="ひきやすい",
             distractors=["ひくやすい", "ひきにくい", "ひいてやすい"],
             en="It's easy to catch a cold at the change of seasons, so please take care.",
             notes_ja="『かぜをひく傾向がある・すぐかぜをひく』という意味で「ひきやすい」を使います。",
             notes_en="Means 'prone to catching a cold': ひきやすい."),
        dict(stem="この{駅|えき}の{周|まわ}りは{店|みせ}も{多|おお}いし、{電車|でんしゃ}も{便利|べんり}だから、とても（　　　）です。",
             correct="{住|す}みやすい",
             distractors=["{住|す}むやすい", "{住|す}みにくい", "{住|す}みすぎる"],
             en="Around this station there are many shops and the trains are convenient, so it is very easy to live in.",
             notes_ja="店が多くて便利なので、『生活しやすい』＝「住みやすい」が文脈に合います。",
             notes_en="Many shops and convenient trains make the area 'easy/comfortable to live in' (住みやすい)."),
    ],
)

# ---------------------------------------------------------------- 8 にくい
GRAMMAR[8] = dict(
    name="にくい", reading="にくい",
    meaning_en="hard / difficult to do ~",
    similar="やすい、すぎる",
    details=dict(
        formula="<strong>動詞ます形</strong>（ますを取る） ＋ <strong>にくい（です）</strong><br>"
                "※イ形容詞として活用します（にくくない／にくかった／にくくて）",
        notes_ja="動詞の「ます形」から「ます」を取って「にくい」を付けます。「〜やすい」の反対の表現です。<br>"
                 "①<strong>『〜するのが難しい・やりづらい』</strong><br>"
                 "例：この{薬|くすり}は{苦|にが}くて<strong>{飲|の}みにくいです</strong>。／このハサミは<strong>{切|き}りにくいです</strong>。<br>"
                 "②<strong>『なかなか〜しない（性質）』</strong><br>"
                 "例：このコップはプラスチックだから<strong>{割|わ}れにくいです</strong>（＝丈夫で良い）。",
        notes_en="Attach にくい to a verb stem (ます-form minus ます). It is the opposite of 〜やすい and has two uses: "
                 "(1) 'hard / awkward to do' (この薬は飲みにくい 'this medicine is hard to swallow'), and "
                 "(2) 'resistant to / doesn't easily ~' (割れにくい 'doesn't break easily'). "
                 "Conjugates as an i-adjective.",
        nuance_ja="①『〜するのが大変で困る（歩きにくい・見にくい・言いにくい）』というマイナスの場面だけでなく、"
                  "②『汚れにくい・壊れにくい・太りにくい』のように、『簡単には悪い状態にならない』というプラスの性質を表すときにもよく使います。",
        nuance_en="Used both for awkwardness/difficulty (歩きにくい 'hard to walk in', 言いにくい 'hard to say') and for positive durability or resistance (壊れにくい 'hard to break', 汚れにくい 'stain-resistant').",
        trap_ja="①辞書形やて形に付けないこと。×飲むにくい・×飲みににくい → ○{飲|の}みにくい<br>"
                "②「憎い（にくい）」という漢字は使いません。必ずひらがなで「にくい」と書きます。<br>"
                "③能力として『できない』ではなく、『やりづらい・簡単には〜しない』という性質を表します。",
        trap_en="① Attach directly to the ます-stem: ×飲むにくい / ×飲みににくい → ○飲みにくい. "
                "② Always write にくい in hiragana. "
                "③ Expresses difficulty/resistance of the action, not total inability.",
        contrast=[
            dict(type="wrong", sentence="この{靴|くつ}は{少|すこ}し{小|ちい}さくて、{歩|ある}くにくいです。",
                 reason_ja="辞書形「歩く」ではなく、ます形「歩き」に「にくい」を付けます。",
                 reason_en="Use the ます-stem 歩き, not the dictionary form 歩く."),
            dict(type="correct", sentence="この{靴|くつ}は{少|すこ}し{小|ちい}さくて、{歩|ある}きにくいです。",
                 reason_ja="「歩きます」の「ます」を取って「歩きにくいです」にします。",
                 reason_en="歩きます minus ます + にくいです = 歩きにくいです."),
            dict(type="correct", sentence="{黒|くろ}い{服|ふく}は{汚|よご}れが{目立|めだ}ちにくいです。",
                 reason_ja="『簡単には目立たない』という性質を表しています。",
                 reason_en="Expresses the property 'doesn't stand out easily'."),
        ],
        comparison=[
            dict(form="〜にくい", form_en="hard to do / resistant to", badge="困難・性質", badge_type="bad",
                 nuance_ja="道具や状況のせいで『やりづらい』、または『なかなか〜しない』ことを表します。",
                 nuance_en="Hard or awkward to do, or does not happen easily.",
                 example="{声|こえ}が{小|ちい}さくて{聞|き}きとりにくいです。"),
            dict(form="〜やすい", form_en="easy to do / likely to", badge="容易・傾向", badge_type="good",
                 nuance_ja="「〜にくい」の正反対で、『楽にできる』『すぐ〜なる』を表します。",
                 nuance_en="Direct opposite of 〜にくい: easy to do or happens easily.",
                 example="このサイトはとても{見|み}やすいです。"),
            dict(form="〜られない（不可能）", form_en="cannot do", badge="不可能", badge_type="neutral",
                 nuance_ja="『まったくできない』ことを表します。「〜にくい」は『できるけれど大変だ』です。",
                 nuance_en="Means 'cannot do at all', whereas 〜にくい means 'can do, but with difficulty'.",
                 example="{辛|から}すぎて{食|た}べられません。"),
        ],
    ),
    quiz=[
        dict(stem="この{魚|さかな}は{小|ちい}さい{骨|ほね}がたくさんあって、とても（　　　）です。",
             correct="{食|た}べにくい",
             distractors=["{食|た}べるにくい", "{食|た}べやすい", "{食|た}べてにくい"],
             en="This fish has lots of small bones and is very hard to eat.",
             notes_ja="細かい骨がたくさんあるので、『食べるのが大変だ』＝「食べにくい」が正解です。",
             notes_en="Lots of small bones make the fish 'hard to eat' (食べにくい)."),
        dict(stem="{雨|あめ}の{日|ひ}は{洗濯物|せんたくもの}がなかなか（　　　）から、{困|こま}ります。",
             correct="{乾|かわ}きにくい",
             distractors=["{乾|かわ}くにくい", "{乾|かわ}きやすい", "{乾|かわ}いてにくい"],
             en="On rainy days, laundry doesn't dry easily, which is troublesome.",
             notes_ja="雨の日は洗濯物が『簡単には乾かない』ので、「乾きにくい」が正解です。「乾くにくい」「乾いてにくい」は接続の誤りです。",
             notes_en="On rainy days laundry 'doesn't dry easily' (乾きにくい)."),
        dict(stem="{田中|たなか}さんの{字|じ}は{小|ちい}さすぎて、とても（　　　）です。",
             correct="{読|よ}みにくい",
             distractors=["{読|よ}むにくい", "{読|よ}みやすい", "{読|よ}んでにくい"],
             en="Mr. Tanaka's handwriting is too small and very hard to read.",
             notes_ja="字が小さすぎるので、『読むのが難しい』＝「読みにくい」が文脈に合います。",
             notes_en="Because the handwriting is too small, it is 'hard to read' (読みにくい)."),
        dict(stem="このガラスは{特別|とくべつ}な{材料|ざいりょう}でできているので、{落|お}としても（　　　）です。",
             correct="{割|わ}れにくい",
             distractors=["{割|わ}れるにくい", "{割|わ}れやすい", "{割|わ}れてにくい"],
             en="Because this glass is made of a special material, it doesn't break easily even if dropped.",
             notes_ja="特別な材料で丈夫なので、『簡単には割れない』という意味の「割れにくい」が正解です。",
             notes_en="Made of a special material, it 'does not break easily' (割れにくい)."),
    ],
)

# ---------------------------------------------------------------- 9 つもりだ
GRAMMAR[9] = dict(
    name="つもりだ", reading="つもりだ",
    meaning_en="plan to; intend to ~",
    similar="予定だ、ようと思う、ことにする",
    details=dict(
        formula="する意志：<strong>動詞辞書形</strong> ＋ <strong>つもりだ／つもりです</strong><br>"
                "しない意志：<strong>動詞ない形</strong> ＋ <strong>つもりだ／つもりです</strong>",
        notes_ja="話し手（自分）の『これから〜しようと思っている』という<strong>意志・計画</strong>を表します。<br>"
                 "例：{来年|らいねん}、{日本|にほん}へ<strong>{行|い}くつもりです</strong>。<br>"
                 "『〜しないでおこう』と決めているときは、「ない形＋つもりです」を使います。<br>"
                 "例：お{菓子|かし}はしばらく<strong>{食|た}べないつもりです</strong>（または「{行|い}くつもりはありません」）。",
        notes_en="Expresses the speaker's personal intention or plan ('I intend to / plan to ~'). "
                 "Attach つもりだ / つもりです to the verb dictionary form for positive intentions (行くつもりです) and to the ない-form for negative intentions (食べないつもりです; or 行くつもりはありません).",
        nuance_ja="「〜ようと思っています」よりも、『もう心の中で決めている』という強い意志があります。"
                  "自分の気持ちを表す表現なので、目上の人に「先生も行くつもりですか」と聞くのは失礼になります（目上の人には「いらっしゃいますか」「ご{予定|よてい}はいかがですか」などを使います）。",
        nuance_en="Stronger and more settled than 〜ようと思っています ('I'm thinking of ~'). "
                  "Because it probes personal intentions, avoid asking superiors directly with 〜つもりですか.",
        trap_ja="①動詞の「ます形」や「て形」には付きません。×行きますつもり・×行ってつもり → ○{行|い}くつもり<br>"
                "②自分の意志では決められないこと（天気が晴れる・試験に受かるなど）には使えません。<br>"
                "③第三者の予定を客観的に言うときは「〜つもりです」ではなく「〜{予定|よてい}です」「〜そうです」などを使います。",
        trap_en="① Attach to the dictionary form or ない-form, never ます or て: ×行ってつもり → ○行くつもり. "
                "② Cannot be used for things outside one's control (e.g., passing an exam or the weather). "
                "③ Mainly used for first-person statements or second-person questions among equals.",
        contrast=[
            dict(type="wrong", sentence="{週末|しゅうまつ}は{部屋|へや}を{掃除|そうじ}してつもりです。",
                 reason_ja="「て形」には付きません。辞書形「掃除する」を使います。",
                 reason_en="Do not attach つもり to the て-form; use the dictionary form 掃除する."),
            dict(type="correct", sentence="{週末|しゅうまつ}は{部屋|へや}を{掃除|そうじ}するつもりです。",
                 reason_ja="辞書形 ＋ つもりです。",
                 reason_en="Dictionary form + つもりです."),
            dict(type="correct", sentence="{今日|きょう}はどこへも{行|い}かないつもりです。",
                 reason_ja="『行かないと決めている』は「ない形＋つもりです」で表します。",
                 reason_en="ない-form + つもりです expresses the intention not to do something."),
        ],
        comparison=[
            dict(form="〜つもりだ", form_en="intend to / plan to (personal will)", badge="個人の意志", badge_type="good",
                 nuance_ja="自分の心の中で『こうしよう』と決めている計画を表します。",
                 nuance_en="A personal intention or plan decided in one's own mind.",
                 example="{大学|だいがく}を{卒業|そつぎょう}したら、{国|くに}へ{帰|かえ}るつもりです。"),
            dict(form="〜{予定|よてい}だ", form_en="scheduled to (objective plan)", badge="スケジュール", badge_type="both",
                 nuance_ja="カレンダーや日程表に決まっている客観的なスケジュールを表します。名詞の「の」にも付きます。",
                 nuance_en="An objective schedule or timetable. Can also follow Noun + の.",
                 example="{飛行機|ひこうき}は3{時|じ}に{着|つ}く{予定|よてい}です。"),
            dict(form="〜ようと{思|おも}っている", form_en="thinking of doing ~", badge="考え中", badge_type="neutral",
                 nuance_ja="「つもり」より少し柔らかく、『そうしようかなと考えている』段階にも使えます。",
                 nuance_en="Slightly softer than つもり; 'I'm thinking of doing ~'.",
                 example="{来月|らいげつ}、{新|あたら}しいパソコンを{買|か}おうと{思|おも}っています。"),
        ],
    ),
    quiz=[
        dict(stem="{夏休|なつやす}みは{家族|かぞく}と{海|うみ}へ（　　　）です。",
             correct="{行|い}くつもり",
             distractors=["{行|い}きつもり", "{行|い}ってつもり", "{行|い}くのつもり"],
             en="I plan to go to the beach with my family during summer vacation.",
             notes_ja="「つもり」の前は動詞の辞書形（またはない形）です。動詞と「つもり」の間に「の」は要りません。",
             notes_en="つもり attaches directly to the dictionary form 行く without の."),
        dict(stem="{体|からだ}にあまりよくないから、これからは{甘い物|あまいもの}をたくさん（　　　）です。",
             correct="{食|た}べないつもり",
             distractors=["{食|た}べなくつもり", "{食|た}べないのつもり", "{食|た}べてつもり"],
             en="Because it's not very good for my health, I intend not to eat a lot of sweets from now on.",
             notes_ja="『〜しないようにしようと思っている』という否定の意志は「ない形＋つもり」で表します。",
             notes_en="Negative intention uses ない-form + つもり (食べないつもり)."),
        dict(stem="{将来|しょうらい}、{自分|じぶん}の{店|みせ}を{出|だ}したいので、{今|いま}はお{金|かね}を（　　　）。",
             correct="{貯|た}めるつもりだ",
             distractors=["{貯|た}めてつもりだ", "{貯|た}めつもりだ", "{貯|た}めるのつもりだ"],
             en="Because I want to open my own shop in the future, I intend to save money now.",
             notes_ja="一段動詞「貯める」の辞書形にそのまま「つもりだ」を付けます。",
             notes_en="Attach つもりだ directly to the dictionary form 貯める."),
        dict(stem="A：{今度|こんど}の{日曜日|にちようび}は{何|なに}をするつもりですか。<br>B：{天気|てんき}がよかったら、{山|やま}に（　　　）です。",
             correct="{登|のぼ}るつもり",
             distractors=["{登|のぼ}りつもり", "{登|のぼ}ってつもり", "{登|のぼ}るのつもり"],
             en="A: What do you plan to do this Sunday? B: If the weather is nice, I plan to climb a mountain.",
             notes_ja="「登る」の辞書形に「つもりです」を付けます。",
             notes_en="Dictionary form 登る + つもりです."),
    ],
)

# ---------------------------------------------------------------- 10 予定だ
GRAMMAR[10] = dict(
    name="予定だ", reading="よていだ",
    meaning_en="scheduled to; plan to ~",
    similar="つもりだ、ことになる",
    details=dict(
        formula="<strong>動詞辞書形</strong> ＋ <strong>{予定|よてい}だ／{予定|よてい}です</strong><br>"
                "<strong>名詞 ＋ の</strong> ＋ <strong>{予定|よてい}だ／{予定|よてい}です</strong>",
        notes_ja="個人・会社・学校・乗り物などの<strong>客観的なスケジュール（日程・計画）</strong>を表します。<br>"
                 "例：{来月|らいげつ}、{大阪|おおさか}へ<strong>{出張|しゅっちょう}する{予定|よてい}です</strong>。<br>"
                 "「予定」は名詞なので、前に「名詞＋の」を付けることもできます。<br>"
                 "例：{会議|かいぎ}は<strong>3{時|じ}からの{予定|よてい}です</strong>。／{明日|あした}は<strong>{休|やす}みの{予定|よてい}です</strong>。",
        notes_en="Expresses a scheduled plan or itinerary ('is scheduled to / plan to'). "
                 "Because 予定 is a noun, it follows either a verb dictionary form (出張する予定です) or Noun + の (3時からの予定です).",
        nuance_ja="「〜つもりだ」が『自分の気持ち・意志』を表すのに対して、「〜予定だ」は『カレンダーや予定表に決まっていること』を客観的に伝えます。"
                  "そのため、自分の予定だけでなく、会議・旅行の日程・電車の到着時刻・他の人のスケジュールにも広く使えます。",
        nuance_en="Whereas 〜つもりだ focuses on personal intention, 〜予定だ states an objective schedule or timetable. "
                  "It can therefore be used for meetings, trips, train arrivals, and other people's schedules as well as your own.",
        trap_ja="①名詞の後ろには必ず「<strong>の</strong>」が必要です。×会議は月曜日予定です → ○{会議|かいぎ}は{月曜日|げつようび}<strong>の</strong>{予定|よてい}です<br>"
                "②動詞の後ろには「の」を付けません。×行くの予定です → ○{行|い}く{予定|よてい}です<br>"
                "③動詞のます形やて形には付きません。×行って予定です → ○{行|い}く{予定|よてい}です",
        trap_en="① Always put の between a noun and 予定: ○月曜日の予定です (×月曜日予定です). "
                "② Do NOT put の after a verb: ○行く予定です (×行くの予定です). "
                "③ Never attach 予定 to the て-form or ます-form.",
        contrast=[
            dict(type="wrong", sentence="{次|つぎ}の{会議|かいぎ}は{来週|らいしゅう}の{水曜日|すいようび}{予定|よてい}です。",
                 reason_ja="名詞「水曜日」と名詞「予定」をつなぐときは「の」が必要です。",
                 reason_en="Join the noun 水曜日 to the noun 予定 with の."),
            dict(type="correct", sentence="{次|つぎ}の{会議|かいぎ}は{来週|らいしゅう}の{水曜日|すいようび}の{予定|よてい}です。",
                 reason_ja="名詞 ＋ の ＋ 予定です。",
                 reason_en="Noun + の + 予定です."),
            dict(type="correct", sentence="{新|あたら}しい{図書館|としょかん}は{来月|らいげつ}オープンする{予定|よてい}です。",
                 reason_ja="動詞辞書形 ＋ 予定です。建物の完成や開店などのスケジュールにも使えます。",
                 reason_en="Verb dictionary form + 予定です; works for impersonal schedules too."),
        ],
        comparison=[
            dict(form="〜{予定|よてい}だ", form_en="scheduled to", badge="客観的日程", badge_type="good",
                 nuance_ja="日程表や計画として決まっていることを表します。名詞＋のにも付きます。",
                 nuance_en="States a decided schedule or itinerary; accepts Noun + の.",
                 example="{午後|ごご}5{時|じ}に{着|つ}く{予定|よてい}です。"),
            dict(form="〜つもりだ", form_en="intend to", badge="個人の意志", badge_type="both",
                 nuance_ja="話し手自身の『〜しよう』という気持ちを表します。電車の到着などには使えません。",
                 nuance_en="Speaker's personal intention; cannot be used for train arrivals or events.",
                 example="{今日|きょう}は{早|はや}く{帰|かえ}るつもりです。"),
            dict(form="〜ことになる", form_en="it has been decided that", badge="決定結果", badge_type="neutral",
                 nuance_ja="周囲や会社などで『〜ということに決まった』という決定の結果を伝えます。",
                 nuance_en="Reports how something came to be decided (often by an organization).",
                 example="{来月|らいげつ}{東京|とうきょう}へ{転勤|てんきん}することになりました。"),
        ],
    ),
    quiz=[
        dict(stem="{社長|しゃちょう}は{明日|あした}の{午後|ごご}、{東京|とうきょう}へ（　　　）です。",
             correct="{出発|しゅっぱつ}する{予定|よてい}",
             distractors=["{出発|しゅっぱつ}する{予定|よてい}の", "{出発|しゅっぱつ}して{予定|よてい}", "{出発|しゅっぱつ}するつもり"],
             en="The company president is scheduled to depart for Tokyo tomorrow afternoon.",
             notes_ja="社長（目上の第三者）のスケジュールを客観的に伝えるので、動詞辞書形＋「予定」（出発する予定です）が適切です。",
             notes_en="To report the schedule of a third person (especially a superior), use 辞書形 + 予定です."),
        dict(stem="{今度|こんど}の{旅行|りょこう}は、3{泊|ぱく}4{日|っか}（　　　）です。",
             correct="の{予定|よてい}",
             distractors=["な{予定|よてい}", "に{予定|よてい}", "のつもり"],
             en="This upcoming trip is scheduled to be four days and three nights.",
             notes_ja="「3泊4日」は名詞なので、「の予定」を付けます。「名詞＋のつもり」はここでは使えません。",
             notes_en="3泊4日 is a noun phrase, so it takes の予定."),
        dict(stem="{飛行機|ひこうき}は10{時|じ}ちょうどに{空港|くうこう}に（　　　）です。",
             correct="{着|つ}く{予定|よてい}",
             distractors=["{着|つ}くつもり", "{着|つ}いて{予定|よてい}", "{着|つ}くの{予定|よてい}"],
             en="The airplane is scheduled to arrive at the airport at 10 o'clock sharp.",
             notes_ja="飛行機の到着時刻は客観的なスケジュールなので「着く予定」を使います。飛行機に意志はないので「つもり」は使えません。",
             notes_en="An airplane has no personal will, so use 着く予定 (not つもり)."),
        dict(stem="A：{卒業式|そつぎょうしき}はいつですか。<br>B：{来月|らいげつ}の20{日|か}に（　　　）です。",
             correct="{行|おこな}う{予定|よてい}",
             distractors=["{行|おこな}い{予定|よてい}", "{行|おこな}って{予定|よてい}", "{行|おこな}うの{予定|よてい}"],
             en="A: When is the graduation ceremony? B: It is scheduled to be held on the 20th of next month.",
             notes_ja="動詞の辞書形「行う」にそのまま「予定」を付けます。動詞の後ろに「の」は入れません。",
             notes_en="Attach 予定 directly to the dictionary form 行う without の."),
    ],
)

# ---------------------------------------------------------------- 11 ようにする
GRAMMAR[11] = dict(
    name="ようにする", reading="ようにする",
    meaning_en="make an effort to do ~; try to ~; make sure to ~",
    similar="ようになる、ことにする、てみる",
    details=dict(
        formula="<strong>動詞辞書形</strong> ＋ <strong>ようにする／ようにしています</strong><br>"
                "<strong>動詞ない形</strong> ＋ <strong>ようにする／ようにしています</strong>",
        notes_ja="『いつも〜するように気をつける・努力する』という意味を表します。<br>"
                 "普段から心がけている習慣を言うときは、<strong>「〜ようにしています」</strong>の形をよく使います。<br>"
                 "例：{毎日|まいにち}{野菜|やさい}を<strong>{食|た}べるようにしています</strong>。<br>"
                 "例：{夜遅|よるおそ}くにコーヒーを<strong>{飲|の}まないようにしています</strong>。<br>"
                 "また、「{忘|わす}れないようにしてください」のように、『気をつけてね』とお願いするときにも使います。",
        notes_en="Attach ようにする to a verb's dictionary form or ない-form to mean 'make an effort to / make sure to ~'. "
                 "In the ongoing form 〜ようにしています, it describes a conscious daily habit ('I try to eat vegetables every day'). "
                 "〜ようにしてください is a polite request meaning 'please make sure to ~'.",
        nuance_ja="「〜ことにしている」が『自分でルールとしてパシッと決めている』のに対し、「〜ようにしている」は『100%できるとは限らないけれど、できるだけそうしようと努力している・気をつけている』という柔らかいニュアンスがあります。",
        nuance_en="Compared to 〜ことにしている (a strict self-imposed rule), 〜ようにしている feels softer: 'I consciously try my best to do this as a habit'.",
        trap_ja="①『試しに一度やってみる』は「〜ようにする」ではなく「<strong>〜てみる</strong>」を使います。<br>"
                "②能力や状態の変化（泳げるようになった）は「〜ようになる」です。「〜ようにする」は自分の意志で努力することに使います。<br>"
                "③ます形やて形には付きません。×食べますようにする → ○{食|た}べるようにする",
        trap_en="① To 'try doing something once to see how it is', use 〜てみる, NOT 〜ようにする. "
                "② For a change in ability/state, use 〜ようになる; 〜ようにする is for conscious effort. "
                "③ Attach only to the dictionary form or ない-form.",
        contrast=[
            dict(type="wrong", sentence="この{新|あたら}しいケーキ、おいしそうだから{食|た}べるようにします。",
                 reason_ja="『試しに一度食べてみる』ときは「食べてみます（〜てみる）」を使います。",
                 reason_en="Trying a cake once to see how it tastes requires 〜てみる (食べてみます), not 〜ようにする."),
            dict(type="correct", sentence="{健康|けんこう}のために、{毎朝|まいあさ}30{分|ぷん}{歩|ある}くようにしています。",
                 reason_ja="日頃の心がけ・習慣的な努力には「〜ようにしています」がぴったりです。",
                 reason_en="〜ようにしています fits an ongoing habit or conscious effort."),
            dict(type="correct", sentence="{会議|かいぎ}の{時間|じかん}に{遅|おく}れないようにしてください。",
                 reason_ja="「ない形＋ようにしてください」で『遅れないように気をつけてください』という意味になります。",
                 reason_en="ない-form + ようにしてください means 'please make sure not to be late'."),
        ],
        comparison=[
            dict(form="〜ようにしている", form_en="make an effort to (habit)", badge="心がけ・努力", badge_type="good",
                 nuance_ja="健康や目標のために『できるだけ〜しようと気をつけている』習慣を表します。",
                 nuance_en="A conscious ongoing effort or habit ('I try to ~').",
                 example="エレベーターを{使|つか}わず、{階段|かいだん}で{上|あ}がるようにしています。"),
            dict(form="〜てみる", form_en="try doing (to see)", badge="お試し", badge_type="both",
                 nuance_ja="どんな結果になるか知るために『試しに一度やってみる』ことです。",
                 nuance_en="Do something as a trial to see what it's like.",
                 example="この{靴|くつ}を{履|は}いてみてもいいですか。"),
            dict(form="〜ようになる", form_en="come to be able to", badge="変化", badge_type="neutral",
                 nuance_ja="前はできなかったことが『できるようになった』という状態の変化を表します。",
                 nuance_en="Describes a change in state or ability ('came to do / became able to').",
                 example="{日本語|にほんご}の{新聞|しんぶん}が{読|よ}めるようになりました。"),
        ],
    ),
    quiz=[
        dict(stem="{健康|けんこう}のために、{毎日|まいにち}{必|かなら}ず{朝|あさ}ご{飯|はん}を（　　　）。",
             correct="{食|た}べるようにしています",
             distractors=["{食|た}べようとしています", "{食|た}べるようになります", "{食|た}べてようにしています"],
             en="For my health, I make a point of eating breakfast every day.",
             notes_ja="日頃の習慣として心がけていることなので、辞書形＋「ようにしています」（食べるようにしています）が正解です。",
             notes_en="For an ongoing conscious habit, use dictionary form + ようにしています."),
        dict(stem="{明日|あした}は{大切|たいせつ}なテストがありますから、{絶対|ぜったい}に（　　　）してください。",
             correct="{遅刻|ちこく}しないように",
             distractors=["{遅刻|ちこく}しないことに", "{遅刻|ちこく}しなくように", "{遅刻|ちこく}しないそうに"],
             en="There is an important test tomorrow, so please make sure you are definitely not late.",
             notes_ja="「〜しないようにしてください」で『〜しないように気をつけてください』という注意・お願いになります。",
             notes_en="〜しないようにしてください means 'please be careful not to ~'."),
        dict(stem="{最近|さいきん}{太|ふと}ってきたので、{夜|よる}9{時|じ}の{後|あと}は{何|なに}も（　　　）。",
             correct="{食|た}べないようにしています",
             distractors=["{食|た}べないようになります", "{食|た}べなくようにしています", "{食|た}べないてみます"],
             en="Since I've been gaining weight lately, I try not to eat anything after 9 p.m.",
             notes_ja="『食べないように気をつけている』という習慣的な努力なので、「食べないようにしています」が正解です。",
             notes_en="Expresses an ongoing effort not to eat late: 食べないようにしています."),
        dict(stem="{習|なら}った{単語|たんご}を{忘|わす}れないために、{毎日|まいにち}ノートに（　　　）。",
             correct="{書|か}くようにしている",
             distractors=["{書|か}いてようにしている", "{書|か}きようにしている", "{書|か}くようになっている"],
             en="So as not to forget the words I learned, I make an effort to write them in my notebook every day.",
             notes_ja="辞書形「書く」に「ようにしている」を付けて、毎日の心がけを表します。",
             notes_en="Dictionary form 書く + ようにしている expresses a daily habit/effort."),
    ],
)

# ---------------------------------------------------------------- 12 ようになる
GRAMMAR[12] = dict(
    name="ようになる", reading="ようになる",
    meaning_en="come to do; become able to ~; reach the point where ~",
    similar="ようにする、ことになる、てくる",
    details=dict(
        formula="<strong>動詞辞書形（特に可能形）</strong> ＋ <strong>ようになる／ようになりました</strong><br>"
                "<strong>動詞ない形</strong> ＋ <strong>ようになる／ようになりました</strong>",
        notes_ja="時間がたって、<strong>『前は〜ではなかったが、今は〜の状態に変わった』</strong>という変化を表します。<br>"
                 "①<strong>能力の変化（可能形＋ようになる）</strong>：前はできなかったことができるようになった。<br>"
                 "例：やっと{自転車|じてんしゃ}に<strong>{乗|の}れるようになりました</strong>。<br>"
                 "②<strong>習慣の変化（辞書形／ない形＋ようになる）</strong>：前はしなかったことをするようになった（または、しなくなった）。<br>"
                 "例：{日本|にほん}に{来|き}てから、{納豆|なっとう}を<strong>{食|た}べるようになりました</strong>。",
        notes_en="Attach ようになる to a verb's dictionary form (especially a potential verb) or ない-form to express a change over time: "
                 "(1) Change in ability: 'became able to ~' (自転車に乗れるようになりました). "
                 "(2) Change in habit: 'came to do / stopped doing ~' (納豆を食べるようになりました / 食べなくなりました).",
        nuance_ja="練習や時間の経過によって『だんだん状態が変わった』ときに使います。"
                  "変化がすでに完了して今の状態になっていることを言うため、文末は過去形の<strong>「〜ようになりました」</strong>になることがとても多いです。"
                  "なお、「〜ないようになる」は「〜なくなる（例：{痛|いた}くなくなった／{行|い}かなくなった）」と言うことも多いです。",
        nuance_en="Usually appears in the past tense 〜ようになりました because the change has already taken place and resulted in the current state. "
                  "Note that 〜ないようになる is also frequently shortened to 〜なくなる (行かなくなった).",
        trap_ja="①イ形容詞やナ形容詞・名詞の変化には「〜ようになる」は使いません。そのまま「〜くなる／〜になる」を使います。×高くなるようになる → ○{高|たか}くなる<br>"
                "②自分の意志で努力することは「〜ようにする」、状態の変化は「〜ようになる」です。<br>"
                "③ます形やて形には付きません。×話せますようになった → ○{話|はな}せるようになった",
        trap_en="① For adjectives and nouns, use 〜くなる / 〜になる directly, NOT ようになる (○暖かくなった, ×暖かいようになった). "
                "② 〜ようにする = conscious effort; 〜ようになる = change in state/ability. "
                "③ Attach to the plain dictionary/potential form, not ます-form.",
        contrast=[
            dict(type="wrong", sentence="{毎日|まいにち}{練習|れんしゅう}して、50メートル{泳|およ}げますようになりました。",
                 reason_ja="「ように」の前は普通形（辞書形・ない形）です。「泳げます」ではなく「泳げる」にします。",
                 reason_en="Use the plain form 泳げる before ようになりました, not the polite 泳げます."),
            dict(type="correct", sentence="{毎日|まいにち}{練習|れんしゅう}して、50メートル{泳|およ}げるようになりました。",
                 reason_ja="可能動詞の辞書形「泳げる」＋「ようになりました」。",
                 reason_en="Potential dictionary form 泳げる + ようになりました."),
            dict(type="correct", sentence="{最近|さいきん}、{子供|こども}が{一人|ひとり}で{服|ふく}を{着|き}られるようになりました。",
                 reason_ja="成長による能力の変化を表しています。",
                 reason_en="Expresses a new ability gained through growth."),
        ],
        comparison=[
            dict(form="〜ようになる", form_en="come to do / become able to", badge="能力・習慣の変化", badge_type="good",
                 nuance_ja="前はできなかったこと・しなかったことが、今は『できる・する』状態に変わったことを表します。",
                 nuance_en="Change from not doing / not being able to do → doing / being able to do.",
                 example="{日本語|にほんご}で{電話|でんわ}がかけられるようになりました。"),
            dict(form="〜ようにする", form_en="try to / make sure to", badge="意識的な努力", badge_type="both",
                 nuance_ja="自分の意志で『〜しようと気をつける』ことを表します。",
                 nuance_en="Conscious effort by the speaker ('try to ~').",
                 example="{毎日|まいにち}{早|はや}く{起|お}きるようにしています。"),
            dict(form="〜ことになる", form_en="it has been decided that", badge="予定の決定", badge_type="neutral",
                 nuance_ja="会議や規則などで、これからの予定が『〜と決まった』ときに使います。",
                 nuance_en="An external decision about a future plan or rule.",
                 example="{来月|らいげつ}から{新|あたら}しい{部署|ぶしょ}で{働|はたら}くことになりました。"),
        ],
    ),
    quiz=[
        dict(stem="1{年間|ねんかん}{一生懸命|いっしょうけんめい}{勉強|べんきょう}して、{日本語|にほんご}で{手紙|てがみ}が（　　　）。",
             correct="{書|か}けるようになりました",
             distractors=["{書|か}けますようになりました", "{書|か}けるようにしました", "{書|か}いてなりました"],
             en="After studying hard for a year, I became able to write letters in Japanese.",
             notes_ja="『前は書けなかったが、今は書ける状態に変わった』という能力の変化なので、可能形「書ける」＋「ようになりました」が正解です。",
             notes_en="Change in ability takes potential plain form 書ける + ようになりました."),
        dict(stem="{前|まえ}はコーヒーが{嫌|きら}いでしたが、{最近|さいきん}はおいしく（　　　）。",
             correct="{飲|の}めるようになりました",
             distractors=["{飲|の}むようにしました", "{飲|の}んでなりました", "{飲|の}めますようになりました"],
             en="I used to dislike coffee, but recently I have come to be able to drink it deliciously.",
             notes_ja="『前は飲めなかったが、今は飲める状態になった』という変化を表すので「飲めるようになりました」が適切です。",
             notes_en="Describes a change from not being able to drink it to being able to: 飲めるようになりました."),
        dict(stem="{弟|おとうと}は5{歳|さい}になって、ひらがなが{全部|ぜんぶ}（　　　）。",
             correct="{読|よ}めるようになった",
             distractors=["{読|よ}むようにした", "{読|よ}んでなった", "{読|よ}めることにした"],
             en="My younger brother turned five and became able to read all the hiragana.",
             notes_ja="成長によって『読める状態に変わった』ので、「読めるようになった」が正解です。",
             notes_en="Growth into a new ability: 読めるようになった."),
        dict(stem="{眼鏡|めがね}を{変|か}えたら、{遠|とお}くの{小|ちい}さい{字|じ}もよく（　　　）。",
             correct="{見|み}えるようになりました",
             distractors=["{見|み}えるようにしました", "{見|み}えてなりました", "{見|み}えることに決まりました"],
             en="When I changed my glasses, I became able to see small print in the distance clearly too.",
             notes_ja="「見える」は自発・可能の意味を持つ動詞で、状態の変化を表す「見えるようになりました」と相性が抜群です。",
             notes_en="見える ('be visible / can see') pairs with ようになりました to show a change in state."),
    ],
)

# ---------------------------------------------------------------- 13 ことにする
GRAMMAR[13] = dict(
    name="ことにする", reading="ことにする",
    meaning_en="decide to do ~ (personal decision)",
    similar="ことになる、ようにする、つもりだ",
    details=dict(
        formula="する決定：<strong>動詞辞書形</strong> ＋ <strong>ことにする／ことにしました</strong><br>"
                "しない決定：<strong>動詞ない形</strong> ＋ <strong>ことにする／ことにしました</strong><br>"
                "継続しているマイルール：<strong>〜ことにしている／ことにしています</strong>",
        notes_ja="話し手（自分）が<strong>自分の意志で『〜しよう！』と決める</strong>ときに使います。<br>"
                 "すでに決めたことを報告するときは「<strong>〜ことにしました</strong>」、今この場で決めるときは「<strong>〜ことにします</strong>」と言います。<br>"
                 "例：いろいろ{考|かんが}えて、このパソコンを<strong>{買|か}うことにしました</strong>。<br>"
                 "また、「<strong>〜ことにしています</strong>」は『自分でそう決めて、いつも習慣にしている（マイルール）』を表します。<br>"
                 "例：{毎晩|まいばん}11{時|じ}には<strong>{寝|ね}ることにしています</strong>。",
        notes_en="Attach ことにする to a verb's dictionary form or ない-form to express making a personal decision ('I decide to ~'). "
                 "Use 〜ことにしました to report a decision already made, 〜ことにします for a decision made on the spot, and 〜ことにしています for a strict personal rule/habit ('I make it a rule to ~').",
        nuance_ja="「〜ことにする」は主語（自分）が主体的に『決断した！』という瞬間や結果に焦点があります。"
                  "一方、会社や学校、家族での話し合いなどで『（周りによって）〜ということに決まった』と言うときは、自動詞の「<strong>〜ことになる</strong>」を使います。",
        nuance_en="〜ことにする highlights the speaker's own active choice. "
                  "By contrast, 〜ことになる ('it has been decided that ~') uses the intransitive なる and presents the decision as an outcome reached externally or collectively.",
        trap_ja="①「た形」や「ます形」には付きません。×買ったことにします → ○{買|か}うことにします<br>"
                "（※「〜たことにする」は『本当はしていないのに、したフリをする』という別の文法になってしまいます）<br>"
                "②会社の命令で転勤するときなどに「転勤することにしました」と言うと、自分で勝手に決めたように聞こえます。「転勤することになりました」を使いましょう。",
        trap_en="① Attach to the dictionary form or ない-form, NOT the た-form (〜たことにする means 'pretend to have done ~'). "
                "② For company transfers or external rules, use 〜ことになりました rather than 〜ことにしました.",
        contrast=[
            dict(type="wrong", sentence="{夏休|なつやす}みは{北海道|ほっかいどう}へ{行|い}ったことにしました。",
                 reason_ja="これからの予定を決めるときは辞書形「行く」を使います（「行ったことにする」は『行ったとウソをつく』意味になります）。",
                 reason_en="Use the dictionary form 行く for a decision about a future plan (行ったことにする means 'pretend to have gone')."),
            dict(type="correct", sentence="{夏休|なつやす}みは{北海道|ほっかいどう}へ{行|い}くことにしました。",
                 reason_ja="辞書形 ＋ ことにしました（自分で決めた決定）。",
                 reason_en="Dictionary form + ことにしました (personal decision)."),
            dict(type="correct", sentence="{健康|けんこう}のために、エレベーターは{使|つか}わないことにしています。",
                 reason_ja="「ない形＋ことにしています」で『使わないと決めて習慣にしている』という意味になります。",
                 reason_en="ない-form + ことにしています expresses a personal rule."),
        ],
        comparison=[
            dict(form="〜ことにする", form_en="decide to do (own choice)", badge="自分の決定", badge_type="good",
                 nuance_ja="自分の意志で『こうしよう』と決断することを表します。",
                 nuance_en="An active decision made by the speaker's own will.",
                 example="{今日|きょう}はタクシーで{帰|かえ}ることにします。"),
            dict(form="〜ことになる", form_en="it is decided that (external)", badge="周囲の決定", badge_type="both",
                 nuance_ja="会社や話し合いなどで、自分の意志とは別に『そう決まった』ことを表します。",
                 nuance_en="An outcome decided by an organization, rule, or group discussion.",
                 example="{来月|らいげつ}、{大阪|おおさか}へ{出張|しゅっちょう}することになりました。"),
            dict(form="〜ようにする", form_en="try to do (effort)", badge="心がけ", badge_type="neutral",
                 nuance_ja="固い決定ではなく、『できるだけ〜しようと気をつける』ことです。",
                 nuance_en="Trying one's best to do something, softer than a firm rule.",
                 example="{毎日|まいにち}{果物|くだもの}を{食|た}べるようにしています。"),
        ],
    ),
    quiz=[
        dict(stem="どのシャツにするか{迷|まよ}いましたが、この{青|あお}いシャツを（　　　）。",
             correct="{買|か}うことにしました",
             distractors=["{買|か}うことになりました", "{買|か}うようにしました", "{買|か}ったことにしました"],
             en="I hesitated over which shirt to choose, but I decided to buy this blue shirt.",
             notes_ja="自分で迷った末に『これを買おう！』と自分の意志で決めたので、辞書形＋「ことにしました」が正解です。",
             notes_en="Since the speaker personally chose the blue shirt after hesitating, use 買うことにしました."),
        dict(stem="A：ご注文はお{決|き}まりですか。<br>B：はい、{私|わたし}はカレーライスに（　　　）。コーヒーも{付|つ}けてください。",
             correct="することにします",
             distractors=["することになります", "したことにします", "するようにします"],
             en="A: Are you ready to order? B: Yes, I'll decide on the curry and rice. Please include a coffee too.",
             notes_ja="その場で自分の注文を決めて宣言しているので、「することにします」（または名詞＋にします）を使います。",
             notes_en="Making a decision on the spot uses することにします."),
        dict(stem="{体|からだ}のために、{先月|せんげつ}からエレベーターに（　　　）。",
             correct="{乗|の}らないことにしています",
             distractors=["{乗|の}らないことになっています", "{乗|の}らなくことにしています", "{乗|の}らないてみます"],
             en="For the sake of my health, since last month I have made it a rule not to take the elevator.",
             notes_ja="自分で『乗らない！』と決めて継続しているマイルールなので、「ない形＋ことにしています」が正解です。",
             notes_en="A self-imposed ongoing rule takes ない-form + ことにしています."),
        dict(stem="{雨|あめ}がひどくなってきたので、{今日|きょう}のサッカーの{練習|れんしゅう}には（　　　）。",
             correct="{行|い}かないことにしました",
             distractors=["{行|い}かなかったことにしました", "{行|い}くなくことにしました", "{行|い}かないように成りました"],
             en="Because the rain got heavy, I decided not to go to today's soccer practice.",
             notes_ja="『行かないでおこう』と自分で決めたので、ない形「行かない」＋「ことにしました」にします。",
             notes_en="Personal decision not to go: 行かないことにしました."),
    ],
)

# ---------------------------------------------------------------- 14 ことになる
GRAMMAR[14] = dict(
    name="ことになる", reading="ことになる",
    meaning_en="it has been decided that ~; it turns out that ~",
    similar="ことにする、ようになる、予定だ",
    details=dict(
        formula="新しい決定：<strong>動詞辞書形／ない形</strong> ＋ <strong>ことになる／ことになりました</strong><br>"
                "決まり・規則・予定：<strong>動詞辞書形／ない形</strong> ＋ <strong>ことになっている／ことになっています</strong>",
        notes_ja="自分の個人の気持ちではなく、会社・学校・話し合い・周囲の事情などによって<strong>『〜ということに決まった』</strong>と伝える表現です。<br>"
                 "例：{来月|らいげつ}から{名古屋|なごや}で<strong>{働|はたら}くことになりました</strong>。<br>"
                 "また、<strong>「〜ことになっています」</strong>は、規則や以前から決まっている予定（『〜というルール／予定だ』）を表します。<br>"
                 "例：この{寮|りょう}では、{夜|よる}10{時|じ}までに<strong>{帰|かえ}ることになっています</strong>。",
        notes_en="Attach ことになる to a verb's dictionary form or ない-form to state that a decision or arrangement has been made ('it has been decided that ~ / I'm going to end up ~'). "
                 "The stative form 〜ことになっています expresses an established rule, custom, or pre-arranged schedule ('it is the rule that ~ / is scheduled to ~').",
        nuance_ja="日本人は、結婚や引っ越しなど本当は自分たちで決めたことでも、控えめに『自然な流れでそう決まりました』と伝えるために「来月、結婚することになりました」「引っ越すことになりました」とよく言います。"
                  "とても自然で丁寧な報告の表現です。",
        nuance_en="Even for personal milestones like marriage or moving house, Japanese speakers often use 〜ことになりました (結婚することになりました) to report the news modestly and politely, as if things naturally fell into place.",
        trap_ja="①能力の変化（泳げるようになった）には「〜ことになる」は使えません（「〜ようになる」を使います）。<br>"
                "②学校の校則や会社の規則を言うときは、「〜ことになりました」ではなく現在の状態を表す「<strong>〜ことになっています</strong>」を使います。<br>"
                "③ます形やて形には付きません。×行くことに成ります（ます形×） → ○{行|い}くことになります",
        trap_en="① Do not use 〜ことになる for changes in ability (use 〜ようになる). "
                "② For existing rules and regulations, use 〜ことになっています (not 〜ことになりました). "
                "③ Attach to the plain dictionary form or ない-form.",
        contrast=[
            dict(type="wrong", sentence="この{図書館|としょかん}では、{本|ほん}は2{週間|しゅうかん}で{返|かえ}すことにしています。",
                 reason_ja="「〜ことにしています」は個人のマイルールです。図書館の規則（みんなのルール）には「〜ことになっています」を使います。",
                 reason_en="ことにしています is a personal rule; institutional rules require ことになっています."),
            dict(type="correct", sentence="この{図書館|としょかん}では、{本|ほん}は2{週間|しゅうかん}で{返|かえ}すことになっています。",
                 reason_ja="規則・決まりを表す「辞書形＋ことになっています」。",
                 reason_en="Dictionary form + ことになっています states an institutional rule."),
            dict(type="correct", sentence="{部長|ぶちょう}の{代|か}わりに、{私|わたし}が{会議|かいぎ}に{出|で}ることになりました。",
                 reason_ja="会社の事情で『私が出席することに決まった』という報告です。",
                 reason_en="Reports an arrangement decided at work."),
        ],
        comparison=[
            dict(form="〜ことになった", form_en="it has been decided that", badge="決定の報告", badge_type="good",
                 nuance_ja="会社や話し合い、または周囲の流れで『新しくそう決まった』ことを報告します。",
                 nuance_en="Reports a new decision or arrangement.",
                 example="{急|きゅう}に{明日|あした}から{出張|しゅっちょう}することになりました。"),
            dict(form="〜ことになっている", form_en="it is the rule / scheduled that", badge="規則・予定", badge_type="both",
                 nuance_ja="以前から決まっているルールや法律、決まったスケジュールを表します。",
                 nuance_en="States an existing rule, custom, or fixed schedule.",
                 example="ゴミは{朝|あさ}8{時|じ}までに{出|だ}すことになっています。"),
            dict(form="〜ことにした", form_en="I decided to", badge="個人の決断", badge_type="neutral",
                 nuance_ja="他の誰でもない『自分自身の意志』で決めたことを表します。",
                 nuance_en="Expresses the speaker's own personal decision.",
                 example="{今日|きょう}は{外|そと}で{昼|ひる}ご{飯|はん}を{食|た}べることにしました。"),
        ],
    ),
    quiz=[
        dict(stem="{来月|らいげつ}から、{会社|かいしゃ}の{新|あたら}しい{事務所|じむしょ}で（　　　）。",
             correct="{働|はたら}くことになりました",
             distractors=["{働|はたら}くことにしました", "{働|はたら}くようにしました", "{働|はたら}いてなりました"],
             en="It has been decided that I will work at the company's new office starting next month.",
             notes_ja="会社での配置や事務所の移動は組織の決定なので、「働くことになりました」を使います。",
             notes_en="Company assignments are organizational decisions: 働くことになりました."),
        dict(stem="この{学校|がっこう}では、{教室|きょうしつ}の{中|なか}では{日本語|にほんご}しか（　　　）。",
             correct="{話|はな}さないことになっています",
             distractors=["{話|はな}さないことにしています", "{話|はな}さないようにしています", "{話|はな}さなくことになっています"],
             en="At this school, it is the rule to speak only Japanese inside the classroom.",
             notes_ja="学校全体の規則（ルール）を説明しているので、「〜ことになっています」が正解です。",
             notes_en="School-wide rules are expressed with 〜ことになっています."),
        dict(stem="みんなで{話|はな}し{合|あ}った{結果|けっか}、{今度|こんど}のパーティーは{来週|らいしゅう}の{土曜日|どようび}に（　　　）。",
             correct="{開|ひら}くことになりました",
             distractors=["{開|ひら}くことにしました", "{開|ひら}くようにしました", "{開|ひら}いたことになりました"],
             en="As a result of discussing it together, it was decided to hold the upcoming party next Saturday.",
             notes_ja="「みんなで話し合った結果」決まったことなので、「{開|ひら}くことになりました」が自然です。",
             notes_en="An outcome reached through group discussion takes 〜ことになりました."),
        dict(stem="{台風|たいふう}が{近|ちか}づいているため、{明日|あした}の{運動会|うんどうかい}は（　　　）。",
             correct="{中止|ちゅうし}することになりました",
             distractors=["{中止|ちゅうし}することにしました", "{中止|ちゅうし}するようになりました", "{中止|ちゅうし}してなりました"],
             en="Because a typhoon is approaching, it has been decided to cancel tomorrow's sports day.",
             notes_ja="行事の中止という全体の決定の報告なので、「中止することになりました」が正解です。",
             notes_en="Reporting an official cancellation uses 中止することになりました."),
    ],
)

# ---------------------------------------------------------------- 15 てみる
GRAMMAR[15] = dict(
    name="てみる", reading="てみる",
    meaning_en="try doing ~ (to see what it's like)",
    similar="ようにする、ようとする",
    details=dict(
        formula="<strong>動詞て形</strong> ＋ <strong>みる／みます／みました／みてください</strong>",
        notes_ja="動詞の「て形」に「みる」を付けると、『どんなものか・どうなるか知るために、<strong>試しに〜する</strong>』という意味になります。<br>"
                 "例：この{新|あたら}しいお{菓子|かし}を<strong>{食|た}べてみます</strong>。<br>"
                 "例：サイズが{合|あ}うかどうか、この{靴|くつ}を<strong>{履|は}いてみてもいいですか</strong>。<br>"
                 "「みる」は一段動詞（る動詞）として活用し、いつも<strong>ひらがな</strong>で書きます（漢字の「見る」は使いません）。",
        notes_en="Attach みる to the て-form of a verb to mean 'try doing ~ (as a test/trial to see what happens)'. "
                 "みる conjugates as a regular ichidan verb (みます, みました, みてください, みたい) and as an auxiliary verb is always written in hiragana.",
        nuance_ja="英語の try to do（努力する＝〜ようにする／〜ようとする）と try doing（試しにやってみる＝〜てみる）の違いに注意しましょう。"
                  "「〜てみる」は、実際にその動作をやってみて結果を確かめるときに使います。"
                  "相手に「ちょっとやってみて！」と軽く勧めるときは「〜てみてください」がとてもよく使われます。",
        nuance_en="Corresponds to English 'try doing ~' (experimenting with an action to check the result), NOT 'try to do ~' (making an effort = 〜ようにする or attempting = 〜ようとする).",
        trap_ja="①補助動詞の「みる」を漢字の「見る」と書かないこと。×食べて見る → ○{食|た}べてみる<br>"
                "②「見ます」にも付きます：「{見|み}てみます（試しに見てみる）」。<br>"
                "③『毎日野菜を食べるように努力している』のような習慣的努力には「〜てみる」ではなく「〜ようにする」を使います。",
        trap_en="① Write auxiliary みる in hiragana, not 見る. "
                "② It can even attach to 見る itself: 見てみます ('I'll take a look and see'). "
                "③ For ongoing effort, use 〜ようにする instead.",
        contrast=[
            dict(type="wrong", sentence="おいしそうだから、このスープを{飲|の}むようにします。",
                 reason_ja="『どんな味か試しに一口飲む』ときは「〜ようにする」ではなく「〜てみる」を使います。",
                 reason_en="Tasting soup to see how it is requires 飲んでみます, not 飲むようにします."),
            dict(type="correct", sentence="おいしそうだから、このスープを{飲|の}んでみます。",
                 reason_ja="て形 ＋ みます（試しに飲んでみる）。",
                 reason_en="て-form + みます (try drinking it)."),
            dict(type="correct", sentence="{分|わ}からないことがあったら、{先生|せんせい}に{聞|き}いてみてください。",
                 reason_ja="「〜てみてください」は『ぜひ試してみてください』という優しい勧めです。",
                 reason_en="〜てみてください gently encourages someone to try doing something."),
        ],
        comparison=[
            dict(form="〜てみる", form_en="try doing (as a trial)", badge="お試し", badge_type="good",
                 nuance_ja="結果がどうなるか確かめるために、実際に一度やってみることです。",
                 nuance_en="Actually perform the action once to see what happens or how it feels.",
                 example="もう{一度|いちど}{考|かんが}えてみます。"),
            dict(form="〜ようにする", form_en="make an effort to", badge="習慣・努力", badge_type="both",
                 nuance_ja="良い習慣を続けるために気をつけたり努力したりすることです。",
                 nuance_en="Conscious effort to maintain a good habit.",
                 example="{早寝早起|はやねはやお}きをするようにしています。"),
            dict(form="〜ようとする", form_en="attempt to / be about to", badge="直前・試み", badge_type="neutral",
                 nuance_ja="動作を始めようとした瞬間や、必死にやろうとした（けれどできなかった）場面で使います。",
                 nuance_en="Be just about to do something, or attempt to do it (often unsuccessfully).",
                 example="{家|いえ}を{出|で}ようとしたとき、{電話|でんわ}が{鳴|な}りました。"),
        ],
    ),
    quiz=[
        dict(stem="すいません、このズボンを（　　　）もいいですか。",
             correct="{履|は}いてみて",
             distractors=["{履|は}くみて", "{履|は}くようにして", "{履|は}いたみて"],
             en="Excuse me, may I try on these pants?",
             notes_ja="店でサイズが合うか『試しに履く』ときは、「て形＋みる」を使って「履いてみてもいいですか」と言います。",
             notes_en="To ask 'may I try them on?', combine てみる with てもいいですか: 履いてみてもいいですか."),
        dict(stem="{初|はじ}めてケーキを{作|つく}りました。よかったら、{一|ひと}つ（　　　）ください。",
             correct="{食|た}べてみて",
             distractors=["{食|た}べるみて", "{食|た}べて見って", "{食|た}べってみて"],
             en="I made a cake for the first time. If you like, please try eating one.",
             notes_ja="「食べる」のて形は「食べて」なので、「食べてみてください」が正解です。「食べって」は活用の誤りです。",
             notes_en="The て-form of 食べる is 食べて → 食べてみてください."),
        dict(stem="{彼|かれ}が{今|いま}{家|いえ}にいるかどうか{分|わ}からないけれど、とりあえず{電話|でんわ}を（　　　）。",
             correct="かけてみます",
             distractors=["かけるみます", "かけるようにします", "かけたみます"],
             en="I don't know whether he is home right now, but I'll try calling him for now.",
             notes_ja="「とりあえず（どうなるか分からないけれど試しに）」という言葉があるので、「かけてみます」がぴったりです。",
             notes_en="とりあえず ('for now / just to see') pairs naturally with 〜てみます."),
        dict(stem="インターネットで{調|しら}べても{分|わ}からなかったので、{図書館|としょかん}の{人|ひと}に（　　　）。",
             correct="{聞|き}いてみました",
             distractors=["{聞|き}くみました", "{聞|き}いたみました", "{聞|き}いておくました"],
             en="Since I couldn't figure it out even after looking it up on the internet, I tried asking the librarian.",
             notes_ja="「聞く」のて形「聞いて」に「みました」を付けて『試しに質問してみた』ことを表します。",
             notes_en="聞いて (て-form of 聞く) + みました = 'tried asking'."),
    ],
)

# ---------------------------------------------------------------- 16 てしまう
GRAMMAR[16] = dict(
    name="てしまう", reading="てしまう",
    meaning_en="finish completely; do ~ by mistake / regrettably",
    similar="ておく、てある、すぎる",
    details=dict(
        formula="<strong>動詞て形</strong> ＋ <strong>しまう／しまいます／しまった／しまいました</strong><br>"
                "会話の短縮形：<strong>〜てしまう → 〜ちゃう</strong> ／ <strong>〜でしまう → 〜じゃう</strong><br>"
                "（過去形：<strong>〜ちゃった ／ 〜じゃった</strong>）",
        notes_ja="動詞の「て形」に「しまう」を付けます。大きく2つの意味があります。<br>"
                 "①<strong>完了（全部〜し終わる）</strong>：最初から最後まで完全にやり終えること。<br>"
                 "例：この{本|ほん}は{面白|おもしろ}かったので、{一日|いちにち}で{全部|ぜんぶ}<strong>{読|よ}んでしまいました</strong>。<br>"
                 "②<strong>後悔・失敗・残念（うっかり〜した）</strong>：したくなかったのに起こってしまったこと。<br>"
                 "例：{電車|でんしゃ}の{中|なか}に{傘|かさ}を<strong>{忘|わす}れてしまいました</strong>。",
        notes_en="Attach しまう to the て-form of a verb. It has two main meanings: "
                 "(1) Complete action ('finish doing ~ completely': 一日で全部読んでしまいました), and "
                 "(2) Regret or unintended action ('accidentally / regrettably did ~': 傘を忘れてしまいました). "
                 "In casual speech, 〜てしまう contracts to 〜ちゃう and 〜でしまう contracts to 〜じゃう.",
        nuance_ja="試験や日常会話で特に多いのは②の『あ、やっちゃった！（失敗・残念・後悔）』のニュアンスです。"
                  "友達との会話では「忘れちゃった」「飲んじゃった」「食べちゃおう」のように短縮形（ちゃう／じゃう）が非常によく使われます。"
                  "「しまう」は五段動詞（う動詞）なので、ない形は「しまわない」です。",
        nuance_en="The 'regret/accident' sense is especially frequent in everyday Japanese. "
                  "In casual conversation, the contractions 〜ちゃう (from てしまう) and 〜じゃう (from でしまう) are used constantly.",
        trap_ja="①「〜でしまう（読んでしまう・飲んでしまう）」の短縮形は「ちゃう」ではなく濁音の「<strong>じゃう</strong>（読んじゃう・飲んじゃう）」です。<br>"
                "②補助動詞の「しまう」はひらがなで書きます。<br>"
                "③完了の意味では、未来の文「{明日|あした}までにやってしまいます（全部終わらせます）」のように前向きな文でも使えます。",
        trap_en="① After で (読んで, 飲んで), the casual contraction is じゃう (読んじゃう), not ちゃう. "
                "② Always write auxiliary しまう in hiragana. "
                "③ In the 'completion' sense, it can also be used positively for future plans ('I'll finish it up by tomorrow').",
        contrast=[
            dict(type="wrong", sentence="{大切|たいせつ}なコップを{落|お}として{割|わ}るしまいました。",
                 reason_ja="辞書形「割る」ではなく、て形「割って」に「しまいました」を付けます。",
                 reason_en="Attach しまいました to the て-form 割って, not the dictionary form 割る."),
            dict(type="correct", sentence="{大切|たいせつ}なコップを{落|お}として{割|わ}ってしまいました。",
                 reason_ja="て形 ＋ しまいました（残念・失敗の気持ち）。",
                 reason_en="て-form + しまいました (expresses regret over breaking the cup)."),
            dict(type="correct", sentence="{夏休|なつやす}みの{宿題|しゅくだい}は、7{月|がつ}中に{全部|ぜんぶ}やってしまいましょう。",
                 reason_ja="『全部終わらせる（完了）』の意味で使われています。",
                 reason_en="Used here in the 'finish completely' sense."),
        ],
        comparison=[
            dict(form="〜てしまう（後悔・失敗）", form_en="do ~ by mistake / regrettably", badge="残念・失敗", badge_type="bad",
                 nuance_ja="うっかりミスをしたときや、残念な結果になったときの気持ちを表します。",
                 nuance_en="Expresses regret or dismay over an unintended action or outcome.",
                 example="バスに{遅|おく}れてしまいました。"),
            dict(form="〜てしまう（完了）", form_en="finish ~ completely", badge="完全完了", badge_type="good",
                 nuance_ja="残さず最後までやりきることを表します。「全部」「すっかり」とよく一緒に使います。",
                 nuance_en="Completing an action thoroughly from start to finish.",
                 example="お{弁当|べんとう}を{全部|ぜんぶ}{食|た}べてしまいました。"),
            dict(form="〜ておく", form_en="do ~ in advance", badge="事前準備", badge_type="neutral",
                 nuance_ja="次のことのために『前もって準備する』という意味です。",
                 nuance_en="Do something in advance as preparation.",
                 example="{旅行|りょこう}の{前|まえ}に切符を{買|か}っておきます。"),
        ],
    ),
    quiz=[
        dict(stem="{急|いそ}いでいたので、{家|いえ}に{財布|さいふ}を（　　　）。",
             correct="{忘|わす}れてしまいました",
             distractors=["{忘|わす}れておきました", "{忘|わす}れてありました", "{忘|わす}れるしまいました"],
             en="Because I was in a hurry, I accidentally left my wallet at home.",
             notes_ja="うっかり財布を忘れた『失敗・残念』の気持ちなので、「忘れてしまいました」が正解です。「忘れておきました」だと『わざと準備として忘れた』ことになり不自然です。",
             notes_en="Accidentally forgetting one's wallet takes 忘れてしまいました (regret/mistake)."),
        dict(stem="このケーキはとてもおいしかったので、{一人|ひとり}で{全部|ぜんぶ}（　　　）。",
             correct="{食|た}べてしまいました",
             distractors=["{食|た}べてありました", "{食|た}べるしまいました", "{食|た}べたしまいました"],
             en="Because this cake was so delicious, I ate the whole thing by myself.",
             notes_ja="『残さず全部食べ終わった（完了）』を表すので、「て形＋しまいました」（食べてしまいました）にします。",
             notes_en="Expresses eating the whole thing completely: 食べてしまいました."),
        dict(stem="{朝寝坊|あさねぼう}をして、いつもの{電車|でんしゃ}に（　　　）。",
             correct="{乗|の}り{遅|おく}れてしまった",
             distractors=["{乗|の}り{遅|おく}れておいた", "{乗|の}り{遅|おく}れてあった", "{乗|の}り{遅|おく}れるしまった"],
             en="I overslept and ended up missing my usual train.",
             notes_ja="電車に乗り遅れるのは残念な失敗なので、「乗り遅れてしまった」が正解です。",
             notes_en="Missing a train is an unintended, regrettable event: 乗り遅れてしまった."),
        dict(stem="お{父|とう}さんの{大切|たいせつ}なカメラを{壊|こわ}して（　　　）、どうしよう。",
             correct="しまった",
             distractors=["おいた", "あった", "みた"],
             en="I accidentally broke my father's precious camera—what should I do?",
             notes_ja="「壊して＋しまった」で『うっかり壊してしまった（後悔）』を表します。",
             notes_en="壊してしまった expresses accidentally breaking something and regretting it."),
    ],
)

# ---------------------------------------------------------------- 17 ておく
GRAMMAR[17] = dict(
    name="ておく", reading="ておく",
    meaning_en="do ~ in advance (as preparation); leave ~ as is",
    similar="てある、てしまう、てみる",
    details=dict(
        formula="<strong>動詞て形</strong> ＋ <strong>おく／おきます／おきました／おいてください</strong><br>"
                "会話の短縮形：<strong>〜ておく → 〜とく</strong> ／ <strong>〜でおく → 〜どく</strong>",
        notes_ja="動詞の「て形」に「おく」を付けます。主な意味は2つあります。<br>"
                 "①<strong>事前の準備（前もって〜する）</strong>：これからの目的のために、あらかじめ準備として何かをしておく。<br>"
                 "例：{旅行|りょこう}の{前|まえ}に、ホテルを<strong>{予約|よやく}しておきます</strong>。<br>"
                 "②<strong>放置・そのままの状態を保つ</strong>：しばらくそのままにしておく。<br>"
                 "例：{次|つぎ}の{授業|じゅぎょう}でも{使|つか}うので、{黒板|こくばん}の{字|じ}は<strong>{消|け}さないでおいてください</strong>（そのままにしておいてください）。",
        notes_en="Attach おく to the て-form of a verb. It has two main uses: "
                 "(1) Preparation in advance ('do ~ beforehand for future use': ホテルを予約しておきます), and "
                 "(2) Leaving something in a certain state for the time being (窓を開けておいてください / 消さないでおいてください). "
                 "In casual speech, 〜ておく contracts to 〜とく and 〜でおく contracts to 〜どく.",
        nuance_ja="「〜ておく」は『これからの動作（操作する人）』に焦点があります。"
                  "一方、誰かが準備した<strong>結果の今の状態</strong>（窓が{開|あ}けてある・予約してある）を見たり報告したりするときは「<strong>〜てある</strong>」を使います。"
                  "会話では「買っとくね」「読んどいて」のように「〜とく／〜どく」と発音されることがとても多いです。",
        nuance_en="〜ておく focuses on the preparatory action itself ('I will do ~ in advance'), whereas 〜てある describes the resulting state after the preparation has been done ('it has been done and is ready').",
        trap_ja="①「ておく」の「おく」を漢字の「置く」と書かないこと（補助動詞なのでひらがなで書きます）。<br>"
                "②うっかり失敗したこと（財布を忘れた・遅刻した）には「〜ておく」は使えません（「〜てしまう」を使います）。<br>"
                "③「〜ないで＋おく」（〜ないでおく）は『あえて〜しないでそのままにする』という意味になります。",
        trap_en="① Always write auxiliary おく in hiragana, not 置く. "
                "② Never use 〜ておく for accidental mistakes (use 〜てしまう). "
                "③ 〜ないでおく means 'intentionally leave ~ undone for now'.",
        contrast=[
            dict(type="wrong", sentence="{明日|あした}はテストだから、{今夜|こんや}よく{復習|ふくしゅう}してあります。",
                 reason_ja="これから準備として復習するので、動作を表す「復習しておきます」を使います。",
                 reason_en="For an action you will do tonight as preparation, use 復習しておきます, not してあります."),
            dict(type="correct", sentence="{明日|あした}はテストだから、{今夜|こんや}よく{復習|ふくしゅう}しておきます。",
                 reason_ja="て形 ＋ おきます（テストのための事前準備）。",
                 reason_en="て-form + おきます (preparation before tomorrow's test)."),
            dict(type="correct", sentence="{部屋|へや}が{暑|あつ}いから、{窓|まど}を{開|あ}けておいてください。",
                 reason_ja="『{開|あ}けた状態のままにしておいてください』というお願いです。",
                 reason_en="Requests leaving the window open."),
        ],
        comparison=[
            dict(form="〜ておく", form_en="do ~ in advance (action)", badge="事前準備の動作", badge_type="good",
                 nuance_ja="これからやることのために『前もって〜する』という動作そのものを表します。",
                 nuance_en="Focuses on the action of preparing something beforehand.",
                 example="{客|きゃく}が{来|く}る{前|まえ}にお{茶|ちゃ}を{入|い}れておきます。"),
            dict(form="〜てある", form_en="has been done (resulting state)", badge="準備完了の状態", badge_type="both",
                 nuance_ja="誰かがすでに準備を終えていて、『今その状態になっている』ことを表します。",
                 nuance_en="Describes the current state resulting from someone's prior action.",
                 example="テーブルの{上|うえ}にお{皿|さら}が{並|なら}べてあります。"),
            dict(form="〜てしまう", form_en="finish completely / do by mistake", badge="完了・失敗", badge_type="neutral",
                 nuance_ja="全部やり終えることや、うっかり失敗してしまったことを表します。",
                 nuance_en="Completing an action entirely or doing it by mistake.",
                 example="{宿題|しゅくだい}を{忘|わす}れてしまいました。"),
        ],
    ),
    quiz=[
        dict(stem="{午後|ごご}から{友達|ともだち}が{遊|あそ}びに{来|く}るので、お{菓子|かし}とジュースを（　　　）。",
             correct="{買|か}っておきます",
             distractors=["{買|か}ってしまいます", "{買|か}ってあります", "{買|か}うおきます"],
             en="Since my friends are coming over this afternoon, I will buy snacks and juice in advance.",
             notes_ja="友達が来る前の『事前準備の動作』なので、「買っておきます」が正解です。目的語の助詞が「を」なので「買ってあります」よりも自然です。",
             notes_en="Buying snacks beforehand as preparation takes 買っておきます."),
        dict(stem="{次|つぎ}の{会議|かいぎ}までに、この{資料|しりょう}を{必|かなら}ず（　　　）ください。",
             correct="{読|よ}んでおいて",
             distractors=["{読|よ}んであって", "{読|よ}むおいて", "{読|よ}んだおいて"],
             en="Please be sure to read this material in advance before the next meeting.",
             notes_ja="会議の前に準備として読んでほしいというお願いなので、「て形＋おいてください」（読んでおいてください）が正解です。",
             notes_en="Asking someone to read material beforehand uses 読んでおいてください."),
        dict(stem="まだ{使|つか}うから、ハサミはそこに（　　　）ね。",
             correct="{出|だ}しておいて",
             distractors=["{出|だ}してあって", "{出|だ}すおいて", "{出|だ}したおいて"],
             en="I'm still going to use the scissors, so leave them out right there, okay?",
             notes_ja="『片付けないでそのままの状態にしておいて』という意味で「出しておいてね」を使います。",
             notes_en="Means 'leave them out as they are': 出しておいてね."),
        dict(stem="{忘|わす}れないうちに、{約束|やくそく}の{時間|じかん}を手帳に（　　　）ましょう。",
             correct="{書|か}いておき",
             distractors=["{書|か}いてあり", "{書|か}くおき", "{書|か}いたおき"],
             en="Let's write the appointment time down in our planner before we forget.",
             notes_ja="あとで困らないように前もってメモするので、「書いておきましょう」が正解です。",
             notes_en="Writing it down beforehand so as not to forget: 書いておきましょう."),
    ],
)

# ---------------------------------------------------------------- 18 てある
GRAMMAR[18] = dict(
    name="てある", reading="てある",
    meaning_en="has been done (resulting state of an intentional action)",
    similar="ておく、ている（自動詞）",
    details=dict(
        formula="<strong>名詞 が</strong> ＋ <strong>他動詞て形</strong> ＋ <strong>ある／あります</strong><br>"
                "（＝誰かが目的をもって〜して、今もその状態が続いている）",
        notes_ja="<strong>他動詞（を格をとる動詞）</strong>の「て形」に「ある（あります）」を付けます。<br>"
                 "『誰かが何かの目的でその動作をして、<strong>その結果の状態が今そこにある</strong>』ことを表します。<br>"
                 "目的語の名詞には「を」ではなく<strong>「が」</strong>（または「は」）を使うのが基本です。<br>"
                 "例：{壁|かべ}にポスター<strong>が{貼|は}ってあります</strong>。<br>"
                 "例：ホテルはもう<strong>{予約|よやく}してあります</strong>から、{安心|あんしん}してください（＝もう準備済みです）。",
        notes_en="Attach ある / あります to the て-form of a **transitive verb** (他動詞) to describe a state resulting from someone's intentional action ('has been done / is ready'). "
                 "The object is normally marked with が (or topicalized with は): 壁にポスターが貼ってあります ('A poster has been put up on the wall').",
        nuance_ja="「窓が{開|あ}いている（自動詞＋ている）」は、風で{開|あ}いたのか誰が{開|あ}けたのかに関係なく、ただ『{開|あ}いている状態』を描写します。"
                  "それに対して「窓が{開|あ}けてある（他動詞＋てある）」は、『空気を入れ替えるためなど、誰かがわざと{開|あ}けた結果、今{開|あ}いている』という<strong>人の意図・準備</strong>が感じられます。",
        nuance_en="Compare 窓が開いている (intransitive + ている: simply 'the window is open') with 窓が{開|あ}けてある (transitive + てある: 'the window has been opened [by someone on purpose]'). "
                  "〜てある also means 'I've already taken care of it' (ホテルは予約してあります).",
        trap_ja="①自動詞には「〜てある」は付きません。×窓が{開|あ}いてある・×電気がついてある → ○{窓|まど}が{開|あ}けてある・○{電気|でんき}がつけてある<br>"
                "②状態を描写するとき、名詞の助詞は「<strong>が</strong>」が基本です：「机の上に本<strong>が</strong>{置|お}いてあります」。<br>"
                "③{生|い}き{物|もの}（人・犬など）の動作には「〜てある」は使いません。",
        trap_en="① Use a transitive verb (開ける, つける, 並べる), NOT an intransitive verb: ×窓が{開|あ}いてある → ○窓が{開|あ}けてある. "
                "② Mark the item with が (or は): ポスターが貼ってあります. "
                "③ Cannot be used with intransitive states of people/animals.",
        contrast=[
            dict(type="wrong", sentence="{黒板|こくばん}に{今日|きょう}の{予定|よてい}が{書|か}いています。",
                 reason_ja="「予定」が自分で書くわけではないので、「書いています」ではなく「書いてあります」にします。",
                 reason_en="The schedule doesn't write itself; use 書いてあります ('is written')."),
            dict(type="correct", sentence="{黒板|こくばん}に{今日|きょう}の{予定|よてい}が{書|か}いてあります。",
                 reason_ja="名詞 ＋ が ＋ 他動詞て形 ＋ あります。",
                 reason_en="Noun + が + transitive て-form + あります."),
            dict(type="correct", sentence="{誕生日|たんじょうび}のケーキはもう{買|か}ってありますよ。",
                 reason_ja="『すでに買って準備が済んでいる』ことを伝えています。",
                 reason_en="Means 'The birthday cake has already been bought (and is ready).'"),
        ],
        comparison=[
            dict(form="他動詞 ＋ てある", form_en="has been done (intentional state)", badge="意図的な結果・準備済", badge_type="good",
                 nuance_ja="誰かが目的をもって行った結果の状態、または『すでに準備済みだ』ということを表します。",
                 nuance_en="Resulting state of a purposeful action, or 'already prepared'.",
                 example="{部屋|へや}はきれいに{掃除|そうじ}してあります。"),
            dict(form="自動詞 ＋ ている", form_en="is in the state of ~", badge="自然な状態", badge_type="both",
                 nuance_ja="誰がしたかに関係なく、目の前の客観的な状態をそのまま表します。",
                 nuance_en="Describes an objective state without implying anyone's intention.",
                 example="{道|みち}に{木|き}の{枝|えだ}が{落|お}ちています。"),
            dict(form="他動詞 ＋ ておく", form_en="do ~ in advance", badge="これからの準備動作", badge_type="neutral",
                 nuance_ja="これから準備の動作をするときに使います。",
                 nuance_en="Used when performing the preparatory action itself.",
                 example="パーティーの{前|まえ}に{部屋|へや}を{掃除|そうじ}しておきます。"),
        ],
    ),
    quiz=[
        dict(stem="{机|つくえ}の{上|うえ}に、きれいな{花|はな}が（　　　）。",
             correct="{飾|かざ}ってあります",
             distractors=["{飾|かざ}っています", "{飾|かざ}っておきます", "{飾|かざ}るあります"],
             en="Beautiful flowers have been arranged on the desk.",
             notes_ja="「花が」の後ろで、誰かが飾った結果の状態を表しているので、他動詞＋「てあります」（飾ってあります）が正解です。",
             notes_en="With 花が as the subject, the state resulting from someone arranging them is 飾ってあります."),
        dict(stem="A：{旅行|りょこう}の{切符|きっぷ}はどうしましたか。<br>B：{心配|しんぱい}しないでください。もう（　　　）よ。",
             correct="{買|か}ってあります",
             distractors=["{買|か}っておきます", "{買|か}っています", "{買|か}うあります"],
             en="A: What did you do about the tickets for the trip? B: Don't worry. They've already been bought.",
             notes_ja="「もう〜よ」と『すでに買って準備が完了している』ことを伝えているので、「買ってあります」が正解です。",
             notes_en="もう indicates the preparation is already complete: 買ってあります."),
        dict(stem="このノートには{大切|たいせつ}なことがたくさん（　　　）から、なくさないでね。",
             correct="{書|か}いてある",
             distractors=["{書|か}いている", "{書|か}いておく", "{書|か}くある"],
             en="A lot of important things are written in this notebook, so don't lose it.",
             notes_ja="ノートに文字が『書かれた状態で残っている』ので、「書いてある」を使います。",
             notes_en="Things 'are written' in the notebook: 書いてある."),
        dict(stem="{暑|あつ}いでしょう。{冷蔵庫|れいぞうこ}に{麦茶|むぎちゃ}が（　　　）から、どうぞ{飲|の}んでください。",
             correct="{冷|ひ}やしてあります",
             distractors=["{冷|ひ}やしています", "{冷|ひ}やしておきます", "{冷|ひ}やすあります"],
             en="You must be hot. Barley tea has been chilled in the refrigerator, so please go ahead and drink some.",
             notes_ja="「麦茶が」の後ろで、あらかじめ冷やして準備してある状態を表すので、他動詞「冷やす」＋「てあります」（冷やしてあります）が正解です。",
             notes_en="With 麦茶が as the subject, the state of having been chilled in advance is 冷やしてあります."),
    ],
)


# ---------------------------------------------------------------- 19 たり〜たりする
GRAMMAR[19] = dict(
    name="たり〜たりする", reading="たりたりする",
    meaning_en="do things like ~ and ~ (representative actions)",
    similar="し〜し、とか〜とか",
    details=dict(
        formula="<strong>動詞［た形］</strong>＋ <strong>り</strong>、<strong>動詞［た形］</strong>＋ <strong>りする</strong><br>"
                "<strong>イ形容詞［かった］</strong>＋ <strong>り</strong> ／ <strong>ナ形容詞・名詞［だった］</strong>＋ <strong>りする</strong>",
        notes_ja="たくさんの動作の中から、代表的な例を２つ挙げて『〜や〜などをする』と言いたいときに使います。"
                 "作り{方|かた}は、動詞の<strong>た形</strong>に「り」を付け、最後に必ず「<strong>します（した）</strong>」を置きます。<br>"
                 "例：休みの日は、<strong>本を読んだり、音楽を聞いたりします</strong>。",
        notes_en="Used to list two representative actions among others ('do things like A and B'). "
                 "Add り to the た-form of each verb and finish with する / します (or した / しました in the past).",
        nuance_ja="「Aて、Bて…」は動作の順番を表しますが、「Aたり、Bたりする」は順番に関係なく『ほかにもいろいろなことをするけれど、例えばAやBをする』というニュアンスになります。"
                  "また、「暑かったり寒かったりする」のように反対の言葉を並べると、『状態がいろいろ変わる』という意味にもなります。",
        nuance_en="Unlike て-form chaining (which shows sequence), 〜たり〜たりする picks out examples without implying order, "
                  "and implies there may be other activities too. Pairing opposites (暑かったり寒かったりする) means 'sometimes A, sometimes B'.",
        trap_ja="①文の最後に必ず「する（します／した／しました）」を付けます。×映画を見たり、買い物したりです。<br>"
                "②時制（現在・過去）は一番最後の「します／しました」で表します。<br>"
                "③１つ目の動詞だけ「たり」にして２つ目を辞書形にするのは誤りです。両方「〜たり」にします。",
        trap_en="① Always close with する / します / しました. "
                "② Tense is shown only on the final する (します vs. しました). "
                "③ Put たり on both verbs.",
        contrast=[
            dict(type="wrong", sentence="{日曜日|にちようび}は{部屋|へや}を{掃除|そうじ}したり、{洗濯|せんたく}します。",
                 reason_ja="２つ目の動詞にも「たり」を付けて、「洗濯したりします」にします。",
                 reason_en="The second verb also needs たり + します: 洗濯したりします."),
            dict(type="correct", sentence="{日曜日|にちようび}は{部屋|へや}を{掃除|そうじ}したり、{洗濯|せんたく}したりします。",
                 reason_ja="動詞た形＋り、動詞た形＋りします。",
                 reason_en="Verb た-form + り, Verb た-form + りします."),
            dict(type="correct", sentence="{最近|さいきん}は{暖|あたた}かかったり、{寒|さむ}かったりしますね。",
                 reason_ja="イ形容詞の過去形＋り で『{日|ひ}によって暖かさや寒さが変わる』ことを表します。",
                 reason_en="i-adjective かったり〜かったりします shows fluctuating weather."),
        ],
        comparison=[
            dict(form="〜たり、〜たりする", form_en="do things like ~ and ~", badge="動作の例示", badge_type="good",
                 nuance_ja="いくつかある行動の中から代表例を挙げるときに使います。順番は関係ありません。",
                 nuance_en="Lists representative actions without specifying order.",
                 example="{休日|きゅうじつ}はテニスをしたり、{映画|えいが}を{見|み}たりします。"),
            dict(form="〜て、〜て…", form_en="do A and then B", badge="動作の順番", badge_type="both",
                 nuance_ja="動作が起きた順番どおりに並べて述べるときに使います。",
                 nuance_en="Describes actions in chronological order.",
                 example="{朝|あさ}{起|お}きて、{顔|かお}を{洗|あら}って、{朝御飯|あさごはん}を{食|た}べます。"),
        ],
    ),
    quiz=[
        dict(stem="{昨日|きのう}の{日曜日|にちようび}は、{本|ほん}を{読|よ}んだり、テレビを（　　　）しました。",
             correct="{見|み}たり",
             distractors=["{見|み}て", "{見|み}る", "{見|み}た"],
             en="Last Sunday, I did things like reading books and watching TV.",
             notes_ja="前に「本を読んだり」があり、後ろに「しました」があるので、２つ目の動詞も「見たり」にします。",
             notes_en="Paired with 読んだり and followed by しました, the second verb must also be 見たり."),
        dict(stem="{夏休|なつやす}みは、{海|うみ}で（　　　）、{山|やま}に{登|のぼ}ったりしたいです。",
             correct="{泳|およ}いだり",
             distractors=["{泳|およ}いで", "{泳|およ}ぐたり", "{泳|およ}ぎたり"],
             en="During summer vacation, I want to do things like swimming in the sea and climbing mountains.",
             notes_ja="後ろに「山に登ったりしたいです」があるので、前も「泳ぐ」のた形＋り「泳いだり」にします。",
             notes_en="Paired with 登ったりしたいです, the first verb takes た-form + り: 泳いだり."),
        dict(stem="{飛行機|ひこうき}のチケットは、{季節|きせつ}によって{高|たか}かったり、（　　　）します。",
             correct="{安|やす}かったり",
             distractors=["{安|やす}いだったり", "{安|やす}くて", "{安|やす}かった"],
             en="Airplane tickets are sometimes expensive and sometimes cheap depending on the season.",
             notes_ja="イ形容詞の「〜たり」は「〜かったり」の形にします。「高かったり、安かったりします」が正解です。",
             notes_en="For i-adjectives, use かったり: 高かったり、安かったりします."),
        dict(stem="パーティーでは、みんなで{歌|うた}を{歌|うた}ったり、ダンスをしたり（　　　）。",
             correct="しました",
             distractors=["でした", "なりました", "ありました"],
             en="At the party, everyone did things like singing songs and dancing.",
             notes_ja="「〜たり、〜たり」の文末は必ず「する（します／しました）」で結びます。",
             notes_en="A 〜たり〜たり clause always closes with a form of する (しました)."),
    ],
)

# ---------------------------------------------------------------- 20 し、〜し
GRAMMAR[20] = dict(
    name="し、〜し", reading="しし",
    meaning_en="not only ~ but also ~; because ~ and ~",
    similar="から、ので、たり〜たりする",
    details=dict(
        formula="<strong>動詞・イ形容詞［普通形］</strong>＋ <strong>し</strong><br>"
                "<strong>ナ形容詞・名詞［普通形（だ／だった）］</strong>＋ <strong>し</strong>（※丁寧形「です・ます＋し」も可）",
        notes_ja="２つ以上の特徴を並べて褒めたり説明したりするときや、複数の理由を挙げて『だから〜だ』と結論を述べるときに使います。<br>"
                 "例：この店は<strong>安いし、おいしいし</strong>、いつも人気があります。",
        notes_en="Used to stack two or more qualities or reasons leading to a conclusion ('not only A, but also B, so...'). "
                 "Attaches to the plain form (note that na-adjectives and nouns keep だ before し).",
        nuance_ja="「〜し、〜し、それに…」のように、「も」を一緒に使うと『さらにこんなことも！』という追加の気持ちがよりはっきり出ます。"
                  "理由が１つだけではなく『ほかにも理由があるけれど』とやんわり言いたいときにも「もう遅いし、帰ろう」のように１つだけで使うことができます。",
        nuance_en="Often paired with the particle も (値段も安いし、味もいいし) to emphasize multiple points. "
                  "Can also be used once (もう遅いし、帰ろう) to imply 'among other reasons, it's late, so let's go home'.",
        trap_ja="①ナ形容詞と名詞の現在肯定には「<strong>だ</strong>」が必要です（○便利だし ／ ×便利し）。<br>"
                "②イ形容詞には「だ」を付けません（○安いし ／ ×安いだし）。",
        trap_en="① Na-adjectives and nouns require だ before し: ○静かだし, ×静かし. "
                "② i-adjectives never take だ: ○安いし, ×安いだし.",
        contrast=[
            dict(type="wrong", sentence="この{部屋|へや}は{広|ひろ}いし、{静|しず}かし、とても{住|す}みやすいです。",
                 reason_ja="「静か」はナ形容詞なので、「だ」を付けて「静かだし」にします。",
                 reason_en="静か is a na-adjective, so it needs だ before し: 静かだし."),
            dict(type="correct", sentence="この{部屋|へや}は{広|ひろ}いし、{静|しず}かだし、とても{住|す}みやすいです。",
                 reason_ja="イ形容詞（広いし）＋ナ形容詞（静かだし）の正しい形です。",
                 reason_en="Correct combination of i-adjective + し and na-adjective + だし."),
            dict(type="correct", sentence="{雨|あめ}も{降|ふ}っているし、{荷物|にもつ}も{多|おお}いから、タクシーに{乗|の}りましょう。",
                 reason_ja="複数の理由を「〜も〜し」で並べて提案につなげています。",
                 reason_en="Stacks multiple reasons using 〜も〜し."),
        ],
        comparison=[
            dict(form="〜し、〜し", form_en="because A and B (multiple reasons/qualities)", badge="複数の理由・特徴", badge_type="good",
                 nuance_ja="理由や特徴をいくつも積み重ねて述べるときに使います。",
                 nuance_en="Stacks multiple reasons or features.",
                 example="{田中|たなか}さんは{親切|しんせつ}だし、{仕事|しごと}も{早|はや}いし、{頼|たよ}りになります。"),
            dict(form="〜から／〜ので", form_en="because ~ (single main reason)", badge="直接の理由", badge_type="both",
                 nuance_ja="原因や理由を１つ直接示すときに使います。",
                 nuance_en="States a single direct cause or reason.",
                 example="{雨|あめ}が{降|ふ}っているので、タクシーで{行|い}きます。"),
        ],
    ),
    quiz=[
        dict(stem="このレストランは{料理|りょうり}もおいしい（　　　）、{値段|ねだん}も{安|やす}いから、よく{行|い}きます。",
             correct="し",
             distractors=["たり", "のに", "と"],
             en="Not only is the food at this restaurant delicious, the prices are cheap too, so I go there often.",
             notes_ja="「料理も〜、値段も〜」と良い点を並べて理由にしているので、「し」が入ります。",
             notes_en="Listing multiple positive points with も〜し: おいしいし."),
        dict(stem="{駅|えき}から{近|ちか}いし、（　　　）、このマンションを{借|か}りることにしました。",
             correct="{便利|べんり}だし",
             distractors=["{便利|べんり}し", "{便利|べんり}なだし", "{便利|べんり}いで"],
             en="It's close to the station and convenient too, so I decided to rent this apartment.",
             notes_ja="「便利」はナ形容詞なので、「だ」を付けて「便利だし」にします。",
             notes_en="便利 is a na-adjective, so it takes だし: 便利だし."),
        dict(stem="{今日|きょう}は{風|かぜ}も{強|つよ}いし、{外|そと}も（　　　）、{家|いえ}でゆっくりしましょう。",
             correct="{寒|さむ}いし",
             distractors=["{寒|さむ}いだし", "{寒|さむ}かったり", "{寒|さむ}いのに"],
             en="The wind is strong today and it's cold outside too, so let's relax at home.",
             notes_ja="イ形容詞「寒い」にはそのまま「し」を付けて「寒いし」にします。",
             notes_en="i-adjective 寒い attaches directly to し: 寒いし."),
        dict(stem="{彼|かれ}はスポーツも（　　　）、{歌|うた}も{上手|じょうず}で、クラスで{人気|にんき}があります。",
             correct="できるし",
             distractors=["できたり", "できるのに", "できれば"],
             en="He can play sports and is good at singing too, so he is popular in class.",
             notes_ja="２つの長所を並べる文なので、動詞の辞書形＋「し」（できるし）が入ります。",
             notes_en="Listing two strengths with 〜も…し: できるし."),
    ],
)

# ---------------------------------------------------------------- 21 ので
GRAMMAR[21] = dict(
    name="ので", reading="ので",
    meaning_en="because; since (polite / objective reason)",
    similar="から、し、ために",
    details=dict(
        formula="<strong>動詞・イ形容詞［普通形］</strong>＋ <strong>ので</strong><br>"
                "<strong>ナ形容詞・名詞［な／だった］</strong>＋ <strong>ので</strong>",
        notes_ja="理由や原因を丁寧に、やわらかく伝えるときに使います。"
                 "<strong>名詞とナ形容詞の現在肯定には「だ」ではなく「な」を使う</strong>のが一番大切なルールです。<br>"
                 "例：今日は<strong>休みなので</strong>、図書館は閉まっています。／道が<strong>静かなので</strong>、歩きやすいです。",
        notes_en="Expresses a cause or reason softly and politely. "
                 "Crucial rule: present affirmative nouns and na-adjectives take な (NOT だ) before ので: 休みなので, 静かなので.",
        nuance_ja="「〜から」は話し手の主観的な理由や主張を強く出すのに対し、「〜ので」は客観的な事情をそのまま伝える響きがあり、"
                  "丁寧にお願いするとき・断るとき・謝るときによく使われます。",
        nuance_en="Compared to から (subjective assertion), ので sounds more objective and soft, making it ideal for polite requests, apologies, and excuses.",
        trap_ja="①名詞・ナ形容詞に「だので」とは言いません。必ず「<strong>なので</strong>」にします（×雨だので → ○雨なので）。<br>"
                "②イ形容詞には「な」を付けません（×忙しいなので → ○忙しいので）。",
        trap_en="① Never say だので; use なので after nouns and na-adjectives. "
                "② Never put な after an i-adjective: ○忙しいので, ×忙しいなので.",
        contrast=[
            dict(type="wrong", sentence="{明日|あした}はテストだので、{今夜|こんや}は{勉強|べんきょう}します。",
                 reason_ja="名詞の後ろは「だので」ではなく「なので」にします。",
                 reason_en="After a noun, use なので, never だので."),
            dict(type="correct", sentence="{明日|あした}はテストなので、{今夜|こんや}は{勉強|べんきょう}します。",
                 reason_ja="名詞 ＋ なので。",
                 reason_en="Noun + なので."),
            dict(type="correct", sentence="ちょっと{用事|ようじ}がありますので、お{先|さき}に{失礼|しつれい}します。",
                 reason_ja="丁寧な会話では「ます＋ので」もよく使われます。",
                 reason_en="In polite speech, ます + ので is very natural."),
        ],
        comparison=[
            dict(form="〜ので", form_en="because / since (soft, objective)", badge="丁寧・客観的", badge_type="good",
                 nuance_ja="事情を穏やかに説明し、お願い・お詫び・断りをする場面に最適です。",
                 nuance_en="Soft, polite explanation of circumstances; great for requests and excuses.",
                 example="{電車|でんしゃ}が{遅|おく}れたので、{少|すこ}し{遅刻|ちこく}しました。"),
            dict(form="〜から", form_en="because (subjective reason)", badge="主観的・強い主張", badge_type="both",
                 nuance_ja="話し手自身の判断・命令・意志の理由を強く言うときに使います。",
                 nuance_en="Stronger, subjective reason; freely used with commands and volitional forms.",
                 example="{危|あぶ}ないから、そこに{触|さわ}らないでください。"),
        ],
    ),
    quiz=[
        dict(stem="{今日|きょう}は{日曜日|にちようび}（　　　）、{銀行|ぎんこう}は{閉|し}まっています。",
             correct="なので",
             distractors=["だので", "なから", "のに"],
             en="Since today is Sunday, the bank is closed.",
             notes_ja="名詞「日曜日」に「ので」をつなぐときは、「だ」を「な」に変えて「日曜日なので」にします。",
             notes_en="A noun takes なので before ので: 日曜日なので."),
        dict(stem="このかばんは{軽|かる}くて（　　　）、{毎日|まいにち}{使|つか}っています。",
             correct="{便利|べんり}なので",
             distractors=["{便利|べんり}だので", "{便利|べんり}でから", "{便利|べんり}なのに"],
             en="Since this bag is light and convenient, I use it every day.",
             notes_ja="ナ形容詞「便利」の後ろに「ので」が来るときも「な」を入れて「便利なので」にします。",
             notes_en="Na-adjective 便利 takes なので: 便利なので."),
        dict(stem="{荷物|にもつ}が{重|おも}くて{大変|たいへん}（　　　）、{少|すこ}し{手伝|てつだ}っていただけませんか。",
             correct="なので",
             distractors=["だので", "なのに", "だから"],
             en="Since the luggage is heavy and hard to carry, could you please help me a little?",
             notes_ja="ナ形容詞「大変」＋丁寧な依頼文なので、客観的で丁寧な理由を表す「なので」が最も自然です。",
             notes_en="With a polite request, 大変なので is the most appropriate form."),
        dict(stem="{外|そと}がだんだん（　　　）ので、{早|はや}く{家|いえ}に{帰|かえ}りましょう。",
             correct="{暗|くら}くなってきた",
             distractors=["{暗|くら}くなってきたな", "{暗|くら}くなってきます", "{暗|くら}いだった"],
             en="Since it has started getting dark outside, let's go home early.",
             notes_ja="動詞のた形「暗くなってきた」には、そのまま「ので」が続きます。",
             notes_en="Verb plain past 暗くなってきた attaches directly to ので."),
    ],
)

# ---------------------------------------------------------------- 22 のに
GRAMMAR[22] = dict(
    name="のに", reading="のに",
    meaning_en="although; even though; despite",
    similar="けれども、ても、ながら",
    details=dict(
        formula="<strong>動詞・イ形容詞［普通形］</strong>＋ <strong>のに</strong><br>"
                "<strong>ナ形容詞・名詞［な／だった］</strong>＋ <strong>のに</strong>",
        notes_ja="『Aから当然予想される結果と反対のことが起きた』というときに使い、驚き・残念・不満の気持ちを表します。"
                 "接続は「〜ので」とまったく同じで、<strong>名詞・ナ形容詞の現在肯定は「〜なのに」</strong>になります。<br>"
                 "例：薬を<strong>飲んだのに</strong>、まだ熱が下がりません。／<strong>日曜日なのに</strong>、仕事があります。",
        notes_en="Expresses surprise, disappointment, or dissatisfaction when the actual result goes against what was expected from A ('even though A, B happened'). "
                 "Like ので, present affirmative nouns and na-adjectives take な before のに (日曜日なのに, 静かなのに).",
        nuance_ja="単なる逆接の「〜けれども／〜が」と違い、「〜のに」には『普通なら〜のはずなのに、どうして！？』という話し手の感情（がっかり・不思議）が強く含まれます。",
        nuance_en="Unlike neutral けれども, のに carries strong speaker emotion (surprise, frustration, or regret that expectations were not met).",
        trap_ja="①名詞・ナ形容詞に「だのに」とは言いません。必ず「<strong>なのに</strong>」にします。<br>"
                "②文の後ろはすでに起きた事実が来ます。未来の依頼・命令・誘い（「〜てください」「〜ましょう」）は後ろに置けません（その場合は「〜けれども」を使います）。",
        trap_en="① Never say だのに; use なのに after nouns and na-adjectives. "
                "② The main clause must be an actual fact, NOT a request, command, or invitation (use けれども for those).",
        contrast=[
            dict(type="wrong", sentence="{春|はる}だのに、{今日|きょう}はとても{寒|さむ}いです。",
                 reason_ja="名詞「春」の後ろは「だのに」ではなく「なのに」にします。",
                 reason_en="After a noun, use なのに, not だのに."),
            dict(type="correct", sentence="{春|はる}なのに、{今日|きょう}はとても{寒|さむ}いです。",
                 reason_ja="名詞 ＋ なのに。",
                 reason_en="Noun + なのに."),
            dict(type="correct", sentence="せっかく{早|はや}く{起|お}きたのに、バスに{遅|おく}れてしまいました。",
                 reason_ja="「せっかく〜のに」で残念な気持ちをさらに強調できます。",
                 reason_en="せっかく〜のに highlights regret ('even though I took the trouble to wake up early...')."),
        ],
        comparison=[
            dict(form="〜のに", form_en="even though (unexpected fact, regret/surprise)", badge="事実・意外・残念", badge_type="good",
                 nuance_ja="すでに起きた予想外の事実に対して、残念・不満・驚きの気持ちを表します。",
                 nuance_en="Expresses surprise or regret over an unexpected actual fact.",
                 example="たくさん{勉強|べんきょう}したのに、テストができませんでした。"),
            dict(form="〜ても", form_en="even if (hypothetical condition)", badge="仮定条件", badge_type="both",
                 nuance_ja="これからの仮定や条件について『たとえ〜しても』と言うときに使います。",
                 nuance_en="Used for hypothetical conditions ('even if...').",
                 example="{明日|あした}、{雨|あめ}が{降|ふ}っても{試合|しあい}をします。"),
        ],
    ),
    quiz=[
        dict(stem="{目覚|めざ}まし{時計|どけい}をセットした（　　　）、{今朝|けさ}は{起|お}きられませんでした。",
             correct="のに",
             distractors=["ので", "から", "し"],
             en="Even though I set my alarm clock, I couldn't wake up this morning.",
             notes_ja="『セットしたなら起きられるはずだが、実際は起きられなかった』という残念な逆接なので、「のに」が正解です。",
             notes_en="Shows an unexpected, regrettable result contrary to setting the alarm: のに."),
        dict(stem="このカメラは{操作|そうさ}が（　　　）、とてもきれいな{写真|しゃしん}が{撮|と}れます。",
             correct="{簡単|かんたん}なのに",
             distractors=["{簡単|かんたん}だのに", "{簡単|かんたん}なので", "{簡単|かんたん}から"],
             en="Even though this camera is easy to operate, it takes very beautiful photos.",
             notes_ja="ナ形容詞「簡単」＋意外な事実の逆接なので、「簡単なのに」にします。",
             notes_en="Na-adjective 簡単 takes なのに to express positive surprise."),
        dict(stem="{今日|きょう}は（　　　）、この{店|みせ}にはお{客|きゃく}さんがたくさんいます。",
             correct="{平日|へいじつ}なのに",
             distractors=["{平日|へいじつ}だのに", "{平日|へいじつ}なので", "{平日|へいじつ}だから"],
             en="Even though today is a weekday, there are many customers in this shop.",
             notes_ja="名詞「平日」に「のに」がつながるので、「平日なのに」が正解です。",
             notes_en="Noun 平日 + なのに ('even though it's a weekday')."),
        dict(stem="エアコンをつけている（　　　）、{部屋|へや}がぜんぜん{涼|すず}しくなりません。",
             correct="のに",
             distractors=["ので", "ために", "ように"],
             en="Even though I have the air conditioner on, the room isn't getting cool at all.",
             notes_ja="エアコンをつけているにもかかわらず涼しくならないという不満・意外性を表すので「のに」が入ります。",
             notes_en="Despite having the AC on, the room isn't getting cool: のに."),
    ],
)

# ---------------------------------------------------------------- 23 かどうか
GRAMMAR[23] = dict(
    name="かどうか", reading="かどうか",
    meaning_en="whether or not ~",
    similar="か（疑問詞＋か）",
    details=dict(
        formula="<strong>動詞・イ形容詞［普通形］</strong>＋ <strong>かどうか</strong><br>"
                "<strong>ナ形容詞・名詞［だ なし］</strong>＋ <strong>かどうか</strong> ＋ わかります／{知|し}っています／{聞|き}きます 等",
        notes_ja="疑問詞（何・どこ・いつ・誰など）がない「はい／いいえ」で答える疑問文を、文の中に入れるときに使います。"
                 "<strong>名詞とナ形容詞の現在肯定には「だ」を付けず、そのまま「かどうか」をつなげる</strong>点に注意しましょう。<br>"
                 "例：明日、田中さんが<strong>来るかどうか</strong>知りません。／この話が<strong>本当かどうか</strong>調べてみます。",
        notes_en="Embeds a yes/no question inside a larger sentence ('whether or not ~'). "
                 "Attach directly to the plain form; present affirmative nouns and na-adjectives drop だ (本当かどうか, 暇かどうか).",
        nuance_ja="「〜かどうか」の代わりに、反対の言葉を並べて「行くか行かないか」「おいしいかおいしくないか」と言うこともできます。",
        nuance_en="Can also be phrased by pairing affirmative and negative forms (行くか行かないか).",
        trap_ja="①「いつ・どこ・何・誰」などの疑問詞がある文には「かどうか」は使えません（×何時かどうか → ○何時か）。<br>"
                "②名詞・ナ形容詞の直後に「だ」は入れません（×暇だかどうか → ○暇かどうか）。",
        trap_en="① Never use かどうか when there is a question word like いつ, どこ, 何, 誰 (use just か: 何時か分かりません). "
                "② Drop だ after nouns and na-adjectives: ○暇かどうか, ×暇だかどうか.",
        contrast=[
            dict(type="wrong", sentence="{会議|かいぎ}が{何時|なんじ}に{始|はじ}まるかどうか、{知|し}っていますか。",
                 reason_ja="「何時」という疑問詞があるので、「かどうか」ではなく「か」だけにします。",
                 reason_en="Because there is a question word (何時), use only か, not かどうか."),
            dict(type="correct", sentence="{会議|かいぎ}が{何時|なんじ}に{始|はじ}まるか、{知|し}っていますか。",
                 reason_ja="疑問詞があるときは「普通形＋か」にします。",
                 reason_en="With a question word, use plain form + か."),
            dict(type="correct", sentence="{明日|あした}のパーティーに{行|い}けるかどうか、まだわかりません。",
                 reason_ja="疑問詞のない「はい／いいえ」の内容なので「かどうか」を使います。",
                 reason_en="A yes/no question without a question word takes かどうか."),
        ],
        comparison=[
            dict(form="〜かどうか", form_en="whether or not ~ (yes/no embedded question)", badge="疑問詞なし", badge_type="good",
                 nuance_ja="「はい」か「いいえ」かを確かめたい・知りたいときに使います。",
                 nuance_en="Used for embedded yes/no questions without a wh-word.",
                 example="このキノコが{食|た}べられるかどうか、{調|しら}べてください。"),
            dict(form="疑問詞 ＋ 〜か", form_en="what / where / when / who ~ (wh- embedded question)", badge="疑問詞あり", badge_type="both",
                 nuance_ja="「いつ・どこ・誰・何・どう」などが入っている疑問文を文中に埋め込むときに使います。",
                 nuance_en="Used when the embedded clause contains a question word.",
                 example="バスがいつ{来|く}るか、わかりません。"),
        ],
    ),
    quiz=[
        dict(stem="この{靴|くつ}のサイズが{合|あ}う（　　　）、{一度|いちど}{履|は}いてみてもいいですか。",
             correct="かどうか",
             distractors=["かどう", "だかどうか", "かなにか"],
             en="May I try these shoes on once to see whether or not the size fits?",
             notes_ja="『サイズが合うか合わないか』を確かめたいので、動詞普通形＋「かどうか」が正解です。",
             notes_en="Checking whether the size fits or not: 合うかどうか."),
        dict(stem="{鈴木|すずき}さんが{明日|あした}（　　　）、{電話|でんわ}で{聞|き}いてみます。",
             correct="{暇|ひま}かどうか",
             distractors=["{暇|ひま}だかどうか", "{暇|ひま}などうか", "{暇|ひま}ますかどうか"],
             en="I'll ask Ms. Suzuki by phone whether or not she is free tomorrow.",
             notes_ja="ナ形容詞「暇」には「だ」や「な」を付けず、そのまま「暇かどうか」にします。",
             notes_en="Na-adjective 暇 attaches directly without だ or な: 暇かどうか."),
        dict(stem="{漢字|かんじ}の{書|か}き{方|かた}が（　　　）、{辞書|じしょ}でチェックしました。",
             correct="{正|ただ}しいかどうか",
             distractors=["{正|ただ}しいだかどうか", "{正|ただ}しいかどう", "{正|ただ}しかったり"],
             en="I checked in the dictionary whether or not the way of writing the kanji was correct.",
             notes_ja="イ形容詞「正しい」にそのまま「かどうか」をつなげて「正しいかどうか」にします。",
             notes_en="i-adjective 正しい attaches directly to かどうか."),
        dict(stem="{来月|らいげつ}の{旅行|りょこう}に（　　　）、{金曜日|きんようび}までに{返事|へんじ}をしてください。",
             correct="{参加|さんか}するかどうか",
             distractors=["{参加|さんか}しますかどうか", "{参加|さんか}するだかどうか", "{参加|さんか}しろかどうか"],
             en="Please reply by Friday as to whether or not you will participate in next month's trip.",
             notes_ja="「どうか」の前は動詞の普通形「参加する」を使います。「参加しますかどうか」とは言いません。",
             notes_en="Use the plain form 参加する before かどうか."),
    ],
)

# ---------------------------------------------------------------- 24 そうだ（様態）
GRAMMAR[24] = dict(
    name="そうだ（様態）", reading="そうだ",
    meaning_en="looks like ~; appears ~; seems about to ~",
    similar="そうだ（伝聞）、らしい、みたいだ",
    details=dict(
        formula="<strong>動詞［ます形（ますを取る）］</strong>＋ <strong>そうだ</strong><br>"
                "<strong>イ形容詞［〜い を取る］</strong>／<strong>ナ形容詞［語幹］</strong>＋ <strong>そうだ</strong><br>"
                "※例外：<strong>いい → よさそうだ</strong> ／ <strong>ない → なさそうだ</strong>",
        notes_ja="目で見た様子や雰囲気から『今にも〜しそうだ』『いかにも〜に見える』と予想・判断するときに使います。<br>"
                 "例：黒い雲が出てきました。雨が<strong>降りそうです</strong>。／このケーキはとても<strong>おいしそうです</strong>。<br>"
                 "特に<strong>「いい → よさそうだ」「ない → なさそうだ」</strong>の２つの例外はテストで最もよく聞かれます。",
        notes_en="Expresses a visual impression or judgment that something is about to happen ('looks delicious', 'looks like it's going to rain'). "
                 "Drop ます from verbs, drop い from i-adjectives, and drop な from na-adjectives. "
                 "Memorize the two irregular forms: いい → よさそうだ and ない → なさそうだ!",
        nuance_ja="名詞を修飾するときは「おいしそう<strong>な</strong>ケーキ」とナ形容詞と同じ形になり、動詞を修飾するときは「楽しそう<strong>に</strong>話しています」となります。",
        nuance_en="Conjugates like a na-adjective: おいしそうなケーキ (before a noun), 楽しそうに話す (before a verb).",
        trap_ja="①「いい」は「×いそうだ」ではなく「<strong>よさそうだ</strong>」、「ない」は「×なそうだ」ではなく「<strong>なさそうだ</strong>」になります。<br>"
                "②動詞の辞書形＋そうだ（降るそうだ）にすると、見た目ではなく『ニュースで聞いた（伝聞）』という意味に変わってしまいます。<br>"
                "③「きれい」「有名」など、最初から目で見てすぐわかる事実には様態の「そうだ」はあまり使いません。",
        trap_en="① いい becomes よさそうだ (never いそうだ), and ない becomes なさそうだ (never なそうだ). "
                "② Dictionary form + そうだ (降るそうだ) means 'I heard it will rain' (hearsay), NOT 'it looks like rain'!",
        contrast=[
            dict(type="wrong", sentence="このかばんは{頭|あたま}が{いいそうだ}ね。→ この{本|ほん}は{おもしろいそうです}。（目の前の本を見て）",
                 reason_ja="イ形容詞の「い」を残して「おもしろいそうです」と言うと『人から聞いた（伝聞）』になります。見た目なら「おもしろそうです」にします。",
                 reason_en="Keeping い makes it hearsay ('I heard it's interesting'). Drop い for visual impression: おもしろそうです."),
            dict(type="correct", sentence="この{本|ほん}はとてもおもしろそうですね。",
                 reason_ja="イ形容詞の「い」を取って「そうだ」を付けます。",
                 reason_en="Drop い from おもしろい and add そうですね."),
            dict(type="correct", sentence="{今日|きょう}は{天気|てんき}がよさそうですね。",
                 reason_ja="「いい」の様態は「よさそうだ」になります。",
                 reason_en="いい becomes よさそうだ."),
        ],
        comparison=[
            dict(form="ます形／語幹 ＋ そうだ（様態）", form_en="looks like ~ (visual impression)", badge="見た目・直感", badge_type="good",
                 nuance_ja="目で見た様子から『〜に見える』『今にも〜しそうだ』と感じたときに使います。",
                 nuance_en="Based on what you see right in front of you.",
                 example="かばんから{本|ほん}が{落|お}ちそうですよ。"),
            dict(form="普通形 ＋ そうだ（伝聞）", form_en="I heard that ~ (hearsay)", badge="情報・ニュース", badge_type="both",
                 nuance_ja="ニュースや人から聞いた情報をそのまま伝えるときに使います。",
                 nuance_en="Reports information heard from another source.",
                 example="{天気予報|てんきよほう}によると、{明日|あした}は{雨|あめ}が{降|ふ}るそうです。"),
        ],
    ),
    quiz=[
        dict(stem="{空|そら}が{暗|くら}くなってきましたね。もうすぐ{雨|あめ}が（　　　）です。",
             correct="{降|ふ}りそう",
             distractors=["{降|ふ}るそう", "{降|ふ}ったそう", "{降|ふ}りよう"],
             en="The sky has gotten dark, hasn't it? It looks like it's going to rain soon.",
             notes_ja="{空|そら}を見て『今にも雨が降るだろう』と予想しているので、ます形＋そう「降りそう」が正解です。「降るそう」は伝聞になってしまいます。",
             notes_en="Judging from the dark sky that it's about to rain requires ます-stem + そう: 降りそう."),
        dict(stem="このセーターは{軽|かる}くて、とても{頭|あたま}から{着|き}やすくて{具合|ぐあい}が（　　　）ですね。",
             correct="よさそう",
             distractors=["いいそう", "よくそう", "よいそう"],
             en="This sweater is light and looks like it will feel very nice and comfortable to wear.",
             notes_ja="「いい（よい）」に様態の「そうだ」が付くときは、例外の「よさそう」になります。",
             notes_en="The irregular visual-impression form of いい is よさそう."),
        dict(stem="{会議|かいぎ}はもうすぐ{終|お}わりますから、{時間|じかん}はあまり{問題|もんだい}が（　　　）です。",
             correct="なさそう",
             distractors=["ないそう", "なくそう", "なかったそう"],
             en="The meeting will end soon, so there doesn't seem to be much of a time problem.",
             notes_ja="「ない」に様態の「そうだ」が付くときは、「さ」が入って「なさそう」になります。",
             notes_en="ない becomes なさそう when expressing visual/situational impression."),
        dict(stem="{公園|こうえん}で{子供|こども}たちが（　　　）に{遊|あそ}んでいます。",
             correct="{楽|たの}しそう",
             distractors=["{楽|たの}しいそう", "{楽|たの}しさそう", "{楽|たの}しかったそう"],
             en="The children are playing happily in the park.",
             notes_ja="イ形容詞「楽しい」の「い」を取って「楽しそうに（遊ぶ）」と動詞を修飾します。",
             notes_en="Drop い from 楽しい and add そうに to modify the verb 遊んでいます."),
    ],
)

# ---------------------------------------------------------------- 25 そうだ（伝聞）
GRAMMAR[25] = dict(
    name="そうだ（伝聞）", reading="そうだ",
    meaning_en="I heard that ~; they say that ~",
    similar="そうだ（様態）、らしい、ということだ",
    details=dict(
        formula="<strong>動詞・イ形容詞［普通形］</strong>＋ <strong>そうだ</strong><br>"
                "<strong>ナ形容詞・名詞［普通形（だ／だった）］</strong>＋ <strong>そうだ</strong>",
        notes_ja="人から聞いた話や、ニュース・天気予報・新聞などで知った情報を他の人にそのまま伝えるときに使います。"
                 "文の初めに「<strong>〜によると</strong>（According to ~）」がよく一緒に使われます。<br>"
                 "例：天気予報によると、明日は<strong>雪が降るそうです</strong>。／あの店は<strong>有名だそうです</strong>。",
        notes_en="Used to report information heard from someone else, the news, or a weather forecast ('I heard that ~'). "
                 "Always attaches to the plain form (including だ for present affirmative nouns and na-adjectives). Often paired with 〜によると.",
        nuance_ja="話し手自身の意見や推測は入らず、『聞いたところでは〜だ』と情報をそのまま伝える表現です。",
        nuance_en="Conveys information objectively without adding the speaker's own conjecture.",
        trap_ja="①名詞・ナ形容詞の現在肯定には必ず「<strong>だ</strong>」を付けます（○静かだそうです ／ ×静かそうです←様態になってしまう）。<br>"
                "②伝聞の「そうだ」には過去形（×〜そうでした）や否定形（×〜そうではありません）はありません。前の普通形の{方|ほう}を変えます（降らなかったそうです）。",
        trap_en="① Keep だ after present affirmative nouns and na-adjectives (元気だそうです). "
                "② Hearsay そうだ never conjugates into the past or negative itself; conjugate the preceding plain form instead.",
        contrast=[
            dict(type="wrong", sentence="{田中|たなか}さんの{話|はなし}によると、あの{映画|えいが}はおもしろそうです。",
                 reason_ja="「〜の話によると」は聞いた情報（伝聞）なので、「い」を残して「おもしろいそうです」にします。",
                 reason_en="With 〜によると (hearsay), keep い: おもしろいそうです."),
            dict(type="correct", sentence="{田中|たなか}さんの{話|はなし}によると、あの{映画|えいが}はおもしろいそうです。",
                 reason_ja="イ形容詞普通形 ＋ そうです。",
                 reason_en="i-adjective plain form + そうです."),
            dict(type="correct", sentence="ニュースによると、{来月|らいげつ}からバスの{料金|りょうきん}が{上|あ}がるそうです。",
                 reason_ja="「ニュースによると」＋動詞普通形＋そうです。",
                 reason_en="ニュースによると + verb plain form + そうです."),
        ],
        comparison=[
            dict(form="普通形 ＋ そうだ（伝聞）", form_en="I heard that ~ (direct report)", badge="聞いた情報そのまま", badge_type="good",
                 nuance_ja="確かな情報源（〜によると）から得た内容をそのまま伝えます。",
                 nuance_en="Directly passes along what you heard or read.",
                 example="{先生|せんせい}の{話|はなし}では、{来週|らいしゅう}テストがあるそうです。"),
            dict(form="ます形／語幹 ＋ そうだ（様態）", form_en="looks like ~ (appearance)", badge="目で見た印象", badge_type="both",
                 nuance_ja="自分の目で見て『〜しそうだ』と感じたときに使います。",
                 nuance_en="Expresses how something looks to your own eyes.",
                 example="このりんごは{赤|あか}くておいしそうですね。"),
        ],
    ),
    quiz=[
        dict(stem="{天気予報|てんきよほう}によると、{明日|あした}は{一日中|いちにちじゅう}{風|かぜ}が（　　　）そうです。",
             correct="{強|つよ}い",
             distractors=["{強|つよ}", "{強|つよ}さ", "{強|つよ}いだ"],
             en="According to the weather forecast, the wind will be strong all day tomorrow.",
             notes_ja="「天気予報によると」があるので伝聞の「そうだ」です。イ形容詞の普通形「強い」をそのまま入れます。",
             notes_en="天気予報によると signals hearsay, which takes the full plain form 強い."),
        dict(stem="{佐藤|さとう}さんから{聞|き}いたんですが、{林|はやし}さんは{来月|らいげつ}{大阪|おおさか}へ（　　　）そうです。",
             correct="{引|ひ}っ{越|こ}す",
             distractors=["{引|ひ}っ{越|こ}し", "{引|ひ}っ{越|こ}します", "{引|ひ}っ{越|こ}して"],
             en="I heard from Ms. Sato that Mr. Hayashi is moving to Osaka next month.",
             notes_ja="「佐藤さんから聞いたんですが」と伝聞を表しているので、動詞の辞書形「引っ越す」＋「そうです」にします。",
             notes_en="Reporting what was heard from Ms. Sato requires the plain form 引っ越す + そうです."),
        dict(stem="{友達|ともだち}の{話|はなし}では、{駅|えき}の{前|まえ}にできたパン{屋|や}はとても（　　　）そうです。",
             correct="{人気|にんき}だ",
             distractors=["{人気|にんき}", "{人気|にんき}な", "{人気|にんき}で"],
             en="According to my friend, the bakery that opened in front of the station is very popular.",
             notes_ja="名詞・ナ形容詞に伝聞の「そうだ」が付くときは、「だ」を入れて「人気だそうです」にします。",
             notes_en="For hearsay, nouns and na-adjectives keep だ before そうです: 人気だそうです."),
        dict(stem="けさの新聞によると、{昨日|きのう}のサッカーの{試合|しあい}は{日本|にほん}が（　　　）そうです。",
             correct="{勝|か}った",
             distractors=["{勝|か}ち", "{勝|か}ちます", "{勝|か}って"],
             en="According to this morning's newspaper, Japan won yesterday's soccer match.",
             notes_ja="過去の出来事をニュースや新聞で知って伝えるので、普通形過去「勝った」＋「そうです」が正解です。",
             notes_en="Reporting a past event from the newspaper uses plain past 勝った + そうです."),
    ],
)

# ---------------------------------------------------------------- 26 らしい
GRAMMAR[26] = dict(
    name="らしい", reading="らしい",
    meaning_en="seems that ~ (based on information/evidence); typical of ~",
    similar="そうだ（伝聞）、ようだ、みたいだ",
    details=dict(
        formula="<strong>動詞・イ形容詞［普通形］</strong>＋ <strong>らしい</strong><br>"
                "<strong>ナ形容詞・名詞［だ なし］</strong>＋ <strong>らしい</strong>",
        notes_ja="見聞きした情報や周りの様子から『どうやら〜のようだ』と判断して言うときに使います。"
                 "<strong>名詞とナ形容詞の現在肯定には「だ」を付けません</strong>（○学生らしい ／ ×学生だらしい）。<br>"
                 "また、「名詞＋らしい」には『いかにもその性質をよく表している（春らしい暖かい{日|ひ}、子供らしい笑顔）』という意味もあります。",
        notes_en="Expresses a reasoned conjecture based on what you've heard or observed ('it seems that ~'). "
                 "Present affirmative nouns and na-adjectives drop だ before らしい. "
                 "Noun + らしい can also mean 'typical of / befitting ~' (春らしい天気 = spring-like weather).",
        nuance_ja="伝聞の「〜そうだ」が情報源の言葉をそのまま伝えるのに対し、「〜らしい」は『うわさや周りの状況から考えて、どうもそうみたいだ』という一歩引いた判断を表します。",
        nuance_en="While そうだ (hearsay) repeats a direct report verbatim, らしい synthesizes indirect clues or rumors ('word is that / apparently').",
        trap_ja="①名詞・ナ形容詞の現在肯定に「だ」は付けません（×静かだらしい → ○静からしい）。<br>"
                "②「〜らしい」はイ形容詞と同じように活用します（〜らしいです ／ 〜らしくないです）。",
        trap_en="① Drop だ after nouns and na-adjectives: ○静からしい, ×静かだらしい. "
                "② らしい conjugates like an i-adjective.",
        contrast=[
            dict(type="wrong", sentence="うわさでは、あのレストランはとても{有名|ゆうめい}だらしいですよ。",
                 reason_ja="ナ形容詞の後ろに「だ」は付けず、「有名らしいですよ」にします。",
                 reason_en="Drop だ before らしい: 有名らしいですよ."),
            dict(type="correct", sentence="うわさでは、あのレストランはとても{有名|ゆうめい}らしいですよ。",
                 reason_ja="ナ形容詞語幹 ＋ らしい。",
                 reason_en="Na-adjective stem + らしい."),
            dict(type="correct", sentence="{今日|きょう}はポカポカして、{春|はる}らしいいい{天気|てんき}ですね。",
                 reason_ja="「名詞＋らしい＋名詞」で『春にふさわしい』という典型性を表します。",
                 reason_en="春らしい天気 means 'weather typical of spring'."),
        ],
        comparison=[
            dict(form="〜らしい（推定・伝聞）", form_en="apparently / seems that ~", badge="間接情報からの推測", badge_type="good",
                 nuance_ja="うわさや周りの状況から『どうやら〜のようだ』と推測して言います。名詞・ナ形容詞に「だ」は付きません。",
                 nuance_en="Inferred from rumors or indirect evidence; drops だ.",
                 example="あそこに{人|ひと}が{集|あつ}まっていますね。{何|なに}かイベントがあるらしいです。"),
            dict(form="普通形 ＋ そうだ（伝聞）", form_en="I heard that ~", badge="直接聞いた情報", badge_type="both",
                 nuance_ja="確かな情報源から聞いたことをそのまま伝えます。名詞・ナ形容詞に「だ」が付きます。",
                 nuance_en="Direct report from a source; keeps だ.",
                 example="ニュースによると、{明日|あした}は{晴|は}れるそうです。"),
        ],
    ),
    quiz=[
        dict(stem="{隣|となり}の{部屋|へや}は{電気|でんき}が{消|き}えていますね。まだ{誰|だれ}も{帰|かえ}っていない（　　　）です。",
             correct="らしい",
             distractors=["そう", "だらしい", "なそう"],
             en="The lights in the next room are off. It seems nobody has come home yet.",
             notes_ja="電気が消えている様子を見て推測し、前の「帰っていない（普通形）」に直接つながるのは「らしい」です（様態の「そう」は「いない」に直接付きません）。",
             notes_en="Following the negative plain form 帰っていない based on observed evidence, らしい is correct."),
        dict(stem="{山田|やまだ}さんは、かぜで{今日|きょう}の{会議|かいぎ}を（　　　）らしいです。",
             correct="{休|やす}む",
             distractors=["{休|やす}み", "{休|やす}みます", "{休|やす}んで"],
             en="Apparently Mr. Yamada is absent from today's meeting with a cold.",
             notes_ja="「らしい」の前には動詞の普通形（辞書形「休む」）を置きます。",
             notes_en="Use the plain form 休む before らしい."),
        dict(stem="この{町|まち}は{緑|みどり}が{多|おお}くて、とても（　　　）らしいですよ。",
             correct="{静|しず}か",
             distractors=["{静|しず}かだ", "{静|しず}かな", "{静|しず}かで"],
             en="I hear this town has lots of greenery and is very quiet.",
             notes_ja="ナ形容詞「静か」に「らしい」が付くときは、「だ」や「な」を付けず「静からしい」にします。",
             notes_en="Na-adjectives drop だ/な before らしい: 静からしい."),
        dict(stem="このピンクのワンピースは、いつも{明|あか}るい{高橋|たかはし}さん（　　　）て、とても{似合|にあ}っていますね。",
             correct="らしく",
             distractors=["そうで", "だらしく", "なそうで"],
             en="This pink dress is so typical of the always-cheerful Ms. Takahashi and suits her very well.",
             notes_ja="『高橋さんという人の明るい性格にぴったり合っている』という典型性の「名詞＋らしい」をて形にした「らしくて」が正解です。",
             notes_en="Noun + らしくて ('typical of Ms. Takahashi and...')."),
    ],
)

# ---------------------------------------------------------------- 27 かもしれない
GRAMMAR[27] = dict(
    name="かもしれない", reading="かもしれない",
    meaning_en="might ~; maybe ~; perhaps ~",
    similar="だろう／でしょう、はずだ",
    details=dict(
        formula="<strong>動詞・イ形容詞［普通形］</strong>＋ <strong>かもしれない（かもしれません）</strong><br>"
                "<strong>ナ形容詞・名詞［だ なし］</strong>＋ <strong>かもしれない（かもしれません）</strong>",
        notes_ja="『はっきりとは分からないけれど、ひょっとしたら〜という可能性がある（30〜50％ぐらい）』と言いたいときに使います。"
                 "<strong>名詞とナ形容詞の現在肯定には「だ」を付けません</strong>。<br>"
                 "例：明日は雨が<strong>降るかもしれません</strong>。／この問題はちょっと<strong>複雑かもしれません</strong>。",
        notes_en="Expresses a possibility ('might / maybe', roughly 30–50% certainty). "
                 "Attaches to plain forms, dropping だ after present affirmative nouns and na-adjectives.",
        nuance_ja="「たぶん〜でしょう（70〜80％）」よりも確信が低く、『もしかしたらそうなる可能性もあるから気をつけよう』という場面でよく使われます。",
        nuance_en="Lower certainty than たぶん〜でしょう; often used when taking precautions ('it might rain, so I'll take an umbrella').",
        trap_ja="①名詞・ナ形容詞の直後に「だ」を付けません（×休みだかもしれません → ○休みかもしれません）。<br>"
                "②丁寧形は「かもしれません」、カジュアルな会話では短く「かも」とも言います（雨かも）。",
        trap_en="① Never put だ before かもしれない: ○休みかもしれません, ×休みだかもしれません. "
                "② Polite form is かもしれません.",
        contrast=[
            dict(type="wrong", sentence="{道|みち}が{混|こ}んでいるから、バスは{遅|おく}れるだかもしれません。",
                 reason_ja="動詞の後ろに「だ」は付きません。「遅れるかもしれません」にします。",
                 reason_en="Do not add だ after a verb: 遅れるかもしれません."),
            dict(type="correct", sentence="{道|みち}が{混|こ}んでいるから、バスは{遅|おく}れるかもしれません。",
                 reason_ja="動詞普通形 ＋ かもしれません。",
                 reason_en="Verb plain form + かもしれません."),
            dict(type="correct", sentence="あの{人|ひと}は、{新|あたら}しい{先生|せんせい}かもしれません。",
                 reason_ja="名詞「先生」に「だ」を付けず、そのまま「かもしれません」をつなげます。",
                 reason_en="Noun attaches directly without だ: 先生かもしれません."),
        ],
        comparison=[
            dict(form="〜かもしれない", form_en="might ~ (30–50% possibility)", badge="可能性（低〜中）", badge_type="good",
                 nuance_ja="『ひょっとすると〜ということもあり得る』という可能性を表します。",
                 nuance_en="Indicates that something is possible, though uncertain.",
                 example="{午後|ごご}から{雪|ゆき}になるかもしれません。"),
            dict(form="たぶん 〜でしょう／だろう", form_en="probably ~ (70–80% probability)", badge="推量（高）", badge_type="both",
                 nuance_ja="『たぶんそうなるだろう』と高い確率で予想するときに使います。",
                 nuance_en="Higher probability conjecture ('probably').",
                 example="たぶん{明日|あした}は{晴|は}れるでしょう。"),
            dict(form="〜はずだ", form_en="should be ~ (logical certainty)", badge="根拠のある確信", badge_type="neutral",
                 nuance_ja="はっきりした理由や根拠があって『当然〜になるはずだ』と確信しているときに使います。",
                 nuance_en="Strong expectation backed by a specific reason.",
                 example="{彼|かれ}は{日本|にほん}に{五年|ごねん}いたので、{日本語|にほんご}が{上手|じょうず}なはずです。"),
        ],
    ),
    quiz=[
        dict(stem="{夕方|ゆうがた}から{雨|あめ}が（　　　）しれませんから、{傘|かさ}を{持|も}っていきましょう。",
             correct="{降|ふ}るかも",
             distractors=["{降|ふ}りかも", "{降|ふ}りますかも", "{降|ふ}っただかも"],
             en="It might rain in the evening, so let's take an umbrella.",
             notes_ja="これからの可能性を表すので、動詞の辞書形「降る」＋「かもしれません」にします。",
             notes_en="Future possibility takes dictionary form 降る + かもしれません."),
        dict(stem="この{時計|とけい}は{古|ふる}いので、{時間|じかん}が{少|すこ}し（　　　）かもしれません。",
             correct="{正確|せいかく}ではない",
             distractors=["{正確|せいかく}だ", "{正確|せいかく}な", "{正確|せいかく}です"],
             en="Since this clock is old, the time might not be quite accurate.",
             notes_ja="古いので『正確ではない可能性がある』という文脈です。またナ形容詞肯定でも「だ／な／です」は「かもしれません」の前に入りません。",
             notes_en="Fits both context ('not accurate') and grammar (da/na/desu cannot precede かもしれません)."),
        dict(stem="あそこにいるのは、{中村|なかむら}さんの（　　　）かもしれません。",
             correct="{弟|おとうと}さん",
             distractors=["{弟|おとうと}さんだ", "{弟|おとうと}さんな", "{弟|おとうと}さんです"],
             en="The person over there might be Mr. Nakamura's younger brother.",
             notes_ja="名詞「弟さん」には「だ」や「な」を付けず、そのまま「かもしれません」をつなげます。",
             notes_en="Nouns attach directly to かもしれません without だ or な."),
        dict(stem="{夜|よる}は{風|かぜ}が（　　　）かもしれませんから、コートを{着|き}ていったほうがいいですよ。",
             correct="{冷|つめ}たい",
             distractors=["{冷|つめ}たいだ", "{冷|つめ}たく", "{冷|つめ}たさ"],
             en="The wind might be cold at night, so you'd better wear a coat.",
             notes_ja="イ形容詞「冷たい」はそのまま「かもしれません」につながります。「冷たいだ」とは言いません。",
             notes_en="i-adjectives attach directly in plain form: 冷たいかもしれません."),
    ],
)

# ---------------------------------------------------------------- 28 はずだ
GRAMMAR[28] = dict(
    name="はずだ", reading="はずだ",
    meaning_en="should be ~; is expected to ~ (logical expectation)",
    similar="はずがない、にちがいない、かもしれない",
    details=dict(
        formula="<strong>動詞・イ形容詞［普通形］</strong>＋ <strong>はずだ</strong><br>"
                "<strong>ナ形容詞［な］</strong>＋ <strong>はずだ</strong> ／ <strong>名詞［の］</strong>＋ <strong>はずだ</strong>",
        notes_ja="はっきりした理由や根拠があって『当然〜だと考えられる』『きっと〜に違いない』と強く予想するときに使います。"
                 "「はず」は形式名詞なので、<strong>ナ形容詞には「な」、名詞には「の」</strong>を付けてつなげます。<br>"
                 "例：昨日メールを送ったので、彼はもう<strong>知っているはずです</strong>。／今日は<strong>休みの日の借出はできないはずです</strong>（今日は<strong>日曜日のはずです</strong>）。",
        notes_en="Expresses confident expectation based on a clear reason or schedule ('should be / is supposed to be ~'). "
                 "Because はず is a formal noun, na-adjectives take な (静かなはずだ) and nouns take の (日曜日のはずだ).",
        nuance_ja="単なる当て推量ではなく、『カレンダーを見たから』『本人がそう言っていたから』など、客観的な根拠があるときに使います。",
        nuance_en="Always backed by objective grounds (a schedule, prior promise, or logical deduction).",
        trap_ja="①ナ形容詞は「<strong>〜なはずだ</strong>」、名詞は「<strong>〜のはずだ</strong>」です（「×だはずだ」とは言いません）。<br>"
                "②自分の意志で行うことには使いません（×私は明日勉強するはずです → ○勉強するつもりです）。",
        trap_en="① Use な after na-adjectives (上手なはずだ) and の after nouns (先生のはずだ); never use だはずだ. "
                "② Not used for one's own intentions (use つもりだ instead).",
        contrast=[
            dict(type="wrong", sentence="{田中|たなか}さんは{料理|りょうり}が{上手|じょうず}だはずです。",
                 reason_ja="ナ形容詞「上手」には「だ」ではなく「な」を付けて「上手なはずです」にします。",
                 reason_en="Na-adjectives take な before はず: 上手なはずです."),
            dict(type="correct", sentence="{田中|たなか}さんは{毎日|まいにち}{自炊|じすい}しているので、{料理|りょうり}が{上手|じょうず}なはずです。",
                 reason_ja="根拠（毎日自炊している）＋ ナ形容詞な ＋ はずです。",
                 reason_en="Logical ground + na-adjective な + はずです."),
            dict(type="correct", sentence="{会議|かいぎ}は{三階|さんがい}の{会議室|かいぎしつ}のはずですよ。",
                 reason_ja="名詞「会議室」＋ の ＋ はずです。",
                 reason_en="Noun + の + はずです."),
        ],
        comparison=[
            dict(form="〜はずだ", form_en="should be ~ (logical certainty)", badge="根拠のある確信", badge_type="good",
                 nuance_ja="予定表や理由から『当然〜であるはずだ』と確信しているときに使います。",
                 nuance_en="Strong expectation grounded in reason or schedule.",
                 example="{飛行機|ひこうき}は十{時|じ}に{着|つ}くはずです。"),
            dict(form="〜かもしれない", form_en="might be ~ (mere possibility)", badge="根拠の薄い可能性", badge_type="both",
                 nuance_ja="はっきりした根拠はないけれど『もしかしたら〜もあり得る』というときに使います。",
                 nuance_en="Possibility without strong certainty.",
                 example="{道|みち}が{混|こ}んでいて、{遅|おく}れるかもしれません。"),
        ],
    ),
    quiz=[
        dict(stem="{先月|せんげつ}{予約|よやく}したので、ホテルの{部屋|へや}はちゃんと（　　　）はずです。",
             correct="{取|と}れている",
             distractors=["{取|と}れています", "{取|と}れているの", "{取|と}れているな"],
             en="Since I made a reservation last month, the hotel room should be properly booked.",
             notes_ja="動詞の普通形「取れている」には、そのまま「はずです」が続きます。",
             notes_en="Verb plain form 取れている attaches directly to はずです."),
        dict(stem="{鈴木|すずき}さんは{十年|じゅうねん}もアメリカに{住|す}んでいたので、{英語|えいご}が（　　　）はずです。",
             correct="{上手|じょうず}な",
             distractors=["{上手|じょうず}だ", "{上手|じょうず}の", "{上手|じょうず}に"],
             en="Since Ms. Suzuki lived in America for ten years, her English should be good.",
             notes_ja="ナ形容詞「上手」が「はず」につながるときは「上手なはずです」にします。",
             notes_en="Na-adjective 上手 takes な before はずです."),
        dict(stem="カレンダーに○がついているから、{明日|あした}は（　　　）はずです。",
             correct="{休|やす}みの{日|ひ}の",
             distractors=["{休|やす}みの{日|ひ}だ", "{休|やす}みの{日|ひ}な", "{休|やす}みの{日|ひ}で"],
             en="Since there's a circle on the calendar, tomorrow should be a day off.",
             notes_ja="名詞「休みの日」が「はず」につながるときは「の」を付けて「休みの日のはずです」にします。",
             notes_en="Noun 休みの日 takes の before はずです."),
        dict(stem="かぎはさっきかばんのポケットに{入|い}れたから、この{中|なか}に（　　　）はずだ。",
             correct="ある",
             distractors=["あります", "あるの", "あったな"],
             en="I put the key in my bag pocket just now, so it should be inside here.",
             notes_ja="『今この中にあるはずだ』なので、動詞の辞書形「ある」＋「はずだ」が正解です。",
             notes_en="Present state expectation uses dictionary form ある + はずだ."),
    ],
)

# ---------------------------------------------------------------- 29 はずがない
GRAMMAR[29] = dict(
    name="はずがない", reading="はずがない",
    meaning_en="cannot possibly be ~; impossible that ~",
    similar="はずだ、わけがない",
    details=dict(
        formula="<strong>動詞・イ形容詞［普通形］</strong>＋ <strong>はずがない</strong><br>"
                "<strong>ナ形容詞［な］</strong>＋ <strong>はずがない</strong> ／ <strong>名詞［の］</strong>＋ <strong>はずがない</strong>",
        notes_ja="はっきりした根拠があって『絶対に〜ということはあり得ない！』と強く否定するときに使います。"
                 "接続は「〜はずだ」とまったく同じです。<br>"
                 "例：まじめな田中さんが、約束を<strong>忘れるはずがありません</strong>。",
        notes_en="Strongly denies a possibility based on solid grounds ('there is no way that ~ / cannot possibly ~'). "
                 "Takes the exact same connections as はずだ.",
        nuance_ja="「〜ないはずだ（たぶん〜ないだろう）」よりもさらに強い表現で、『100％そんなことはあり得ない』という強い確信を表します。",
        nuance_en="Stronger than 〜ないはずだ; expresses near-100% conviction that something is impossible.",
        trap_ja="①ナ形容詞は「〜なはずがない」、名詞は「〜のはずがない」になります。<br>"
                "②丁寧形は「はずがありません」または「はずはないです」と言います。",
        trap_en="① Na-adjectives take な and nouns take の before はずがない. "
                "② Polite form is はずがありません.",
        contrast=[
            dict(type="wrong", sentence="あの{人|ひと}はまだ{小学生|しょうがくせい}だから、{運転|うんてん}できるだはずがありません。",
                 reason_ja="動詞の後ろに「だ」は不要です。「運転できるはずがありません」にします。",
                 reason_en="Do not add だ after a verb: 運転できるはずがありません."),
            dict(type="correct", sentence="あの{人|ひと}はまだ{小学生|しょうがくせい}だから、{車|くるま}を{運転|うんてん}できるはずがありません。",
                 reason_ja="動詞辞書形 ＋ はずがありません。",
                 reason_en="Verb dictionary form + はずがありません."),
            dict(type="correct", sentence="こんなに{複雑|ふくざつ}な{問題|もんだい}が、{簡単|かんたん}なはずがありません。",
                 reason_ja="ナ形容詞 ＋ な ＋ はずがありません。",
                 reason_en="Na-adjective + な + はずがありません."),
        ],
        comparison=[
            dict(form="〜はずがない", form_en="cannot possibly be ~ (impossible)", badge="強い全面否定", badge_type="good",
                 nuance_ja="『絶対にそんなことはあり得ない』と可能性を強く打ち消します。",
                 nuance_en="Categorically rules out the possibility ('no way that ~').",
                 example="まだ一{時|じ}だから、{授業|じゅぎょう}が{終|お}わるはずがありません。"),
            dict(form="〜ないはずだ", form_en="should not ~ (expected not to)", badge="否定の予想", badge_type="both",
                 nuance_ja="予定や理由から『〜しないはずだ』と予想するときに使います。",
                 nuance_en="Expects that something will not happen based on a schedule/reason.",
                 example="{今日|きょう}は{祝日|しゅくじつ}だから、{彼|かれ}は{会社|かいしゃ}へ{来|こ}ないはずです。"),
        ],
    ),
    quiz=[
        dict(stem="{彼|かれ}は{今|いま}、外国へ{出張|しゅっちょう}しているから、{今日|きょう}のパーティーに（　　　）はずがありません。",
             correct="{来|こ}られる",
             distractors=["{来|こ}られます", "{来|こ}られるだ", "{来|こ}られるな"],
             en="Since he is currently on a business trip abroad, there is no way he can come to today's party.",
             notes_ja="外国にいるのだから『来られる可能性はゼロだ』という意味で、可能動詞普通形「来られる」＋「はずがありません」にします。",
             notes_en="Plain potential verb 来られる + はずがありません ('cannot possibly come')."),
        dict(stem="{昨日|きのう}{買|か}ったばかりの{新|あたら}しいパソコンが、もう（　　　）はずがありません。",
             correct="{壊|こわ}れる",
             distractors=["{壊|こわ}れます", "{壊|こわ}れるの", "{壊|こわ}れて"],
             en="A brand-new PC that I just bought yesterday cannot possibly break already.",
             notes_ja="動詞の辞書形「壊れる」＋「はずがありません」が正解です。",
             notes_en="Verb dictionary form 壊れる + はずがありません."),
        dict(stem="{駅前|えきまえ}のこんなに{大|おお}きくてきれいなマンションの家賃が、そんなに（　　　）はずがありません。",
             correct="{安|やす}い",
             distractors=["{安|やす}いだ", "{安|やす}いの", "{安|やす}いな"],
             en="The rent for such a big, beautiful apartment right in front of the station cannot possibly be that cheap.",
             notes_ja="イ形容詞「安い」にはそのまま「はずがありません」が続きます。",
             notes_en="i-adjective 安い attaches directly to はずがありません."),
        dict(stem="いつも{元気|げんき}でスポーツが{大好|だいす}きな{弟|おとうと}が、おなかが{すいていない}（　　　）。",
             correct="はずがない",
             distractors=["はずだない", "かもしれないない", "つもりがない"],
             en="There is no way my younger brother, who is always energetic and loves sports, isn't hungry.",
             notes_ja="『おなかがすいていないなんてあり得ない』と強く否定する「はずがない」が正解です。",
             notes_en="Strongly denies the possibility that he isn't hungry: はずがない."),
    ],
)

# ---------------------------------------------------------------- 30 ために
GRAMMAR[30] = dict(
    name="ために", reading="ために",
    meaning_en="in order to ~; for the sake of ~; because of ~",
    similar="ように、のに（用途）、ので",
    details=dict(
        formula="<strong>動詞［辞書形］</strong>＋ <strong>ために</strong>（目的：〜する目的で）<br>"
                "<strong>名詞 ＋ の</strong>＋ <strong>ために</strong>（目的・利益：〜のために）<br>"
                "※原因・理由の用法：普通形（ナ形な／名詞の）＋ ために（〜が原因で）",
        notes_ja="主に２つの意味があります。<br>"
                 "①<strong>目的</strong>：自分が意志をもって行う目標を表します（<strong>将来、自分の店を持つために</strong>貯金しています／<strong>家族のために</strong>料理を作ります）。<br>"
                 "②<strong>原因・理由</strong>：台風や事故などが原因で何かが起きたことを表します（大雪の<strong>ために</strong>、電車が止まりました）。",
        notes_en="Has two main uses: "
                 "(1) Purpose ('in order to ~ / for the sake of ~'): Verb dictionary form + ために or Noun + の + ために, when the subject intentionally works toward a goal. "
                 "(2) Cause/Reason ('due to / because of ~'): used in slightly formal contexts (台風のために電車が止まった).",
        nuance_ja="目的の「〜ために」は、前の動詞も後ろの動詞も<strong>同じ主語が自分の意志で行う動作（意志動詞）</strong>のときに使います。"
                  "可能動詞（話せる、見える）や無意志動詞（わかる、治る、忘れない）が目的のときは「〜ために」ではなく「<strong>〜ように</strong>」を使います。",
        nuance_en="For purpose, ために requires a volitional verb with the same subject in both clauses. "
                  "If the goal is a potential verb or non-volitional state (話せる, わかる, 忘れない), use ように instead!",
        trap_ja="①可能動詞や「〜ない」には目的の「ために」は使えません（×日本語が話せるために → ○日本語が話せるように）。<br>"
                "②名詞の後ろには必ず「<strong>の</strong>」を入れます（○健康のために ／ ×健康ために）。",
        trap_en="① Never use purpose ために after potential verbs or negative verbs (use ように: 話せるように, 忘れないように). "
                "② Always put の between a noun and ために: 健康のために.",
        contrast=[
            dict(type="wrong", sentence="{日本語|にほんご}が{上手|じょうず}に{話|はな}せるために、{毎日|まいにち}{練習|れんしゅう}しています。",
                 reason_ja="「話せる」は可能動詞（状態）なので、「ために」ではなく「ように」を使います。",
                 reason_en="話せる is a potential verb, so it requires ように, not ために."),
            dict(type="correct", sentence="{日本|にほん}へ{留学|りゅうがく}するために、{毎日|まいにち}{日本語|にほんご}を{勉強|べんきょう}しています。",
                 reason_ja="「留学する」は自分の意志で行う動作なので、「辞書形＋ために」を使います。",
                 reason_en="留学する is a volitional action, so 留学するために is correct."),
            dict(type="correct", sentence="{健康|けんこう}のために、{毎朝|まいあさ}ジョギングをしています。",
                 reason_ja="名詞 ＋ の ＋ ために。",
                 reason_en="Noun + の + ために."),
        ],
        comparison=[
            dict(form="意志動詞［辞書形］／名詞の ＋ ために", form_en="in order to ~ (volitional goal)", badge="意志的な目標", badge_type="good",
                 nuance_ja="『留学する』『家を買う』『試験に受かる』など、自分の意志で目指すはっきりした目標に使います。",
                 nuance_en="Used when pursuing an intentional goal (buy a house, study abroad).",
                 example="{新|あたら}しいパソコンを{買|か}うために、アルバイトをしています。"),
            dict(form="可能動詞・ない形 ＋ ように", form_en="so that ~ (state/ability goal)", badge="状態・可能の目標", badge_type="both",
                 nuance_ja="『〜できるようになる』『〜しないですむ』という状態を目指して行動するときに使います。",
                 nuance_en="Used when aiming to achieve a state or ability, or to avoid something.",
                 example="{遅刻|ちこく}しないように、{早|はや}く{家|いえ}を{出|で}ました。"),
        ],
    ),
    quiz=[
        dict(stem="{将来|しょうらい}、{自分|じぶん}のパン{屋|や}を（　　　）ために、{今|いま}お金を{貯|た}めています。",
             correct="{開|ひら}く",
             distractors=["{開|ひら}いた", "{開|ひら}きます", "{開|ひら}いて"],
             en="I am saving money now in order to open my own bakery in the future.",
             notes_ja="目的を表す「〜ために」の前は、意志動詞の辞書形「{開|ひら}く（ひらく）」を置きます。",
             notes_en="Purpose ために takes the verb dictionary form 開く."),
        dict(stem="{家族|かぞく}（　　　）、{週末|しゅうまつ}はいつもおいしい{料理|りょうり}を{作|つく}ります。",
             correct="のために",
             distractors=["ために", "なために", "にために"],
             en="For my family's sake, I always cook delicious meals on weekends.",
             notes_ja="名詞「家族」に「ために」をつなぐときは「の」を入れて「家族のために」にします。",
             notes_en="Noun + のために ('for the sake of my family')."),
        dict(stem="{大雨|おおあめ}が（　　　）ために、サッカーの{試合|しあい}は{来週|らいしゅう}に{延期|えんき}されました。",
             correct="{降|ふ}った",
             distractors=["{降|ふ}り", "{降|ふ}ります", "{降|ふ}ろう"],
             en="Because of the heavy rain, the soccer match was postponed until next week.",
             notes_ja="すでに起きた原因・理由を表す「〜ために」なので、過去形（た形）「降った」が入ります。",
             notes_en="Cause/reason ために for a past event takes the plain past form 降った."),
        dict(stem="{引|ひ}っ{越|こ}し（　　　）、{大|おお}きいダンボールを{十個|じゅっこ}{用意|ようい}しました。",
             correct="のために",
             distractors=["ように", "だために", "なように"],
             en="In preparation for moving house, I prepared ten large cardboard boxes.",
             notes_ja="名詞「引っ越し」の目的を表すので、「のために」が正解です（「ように」は名詞に直接付きません）。",
             notes_en="After the noun 引っ越し, purpose is expressed with のために."),
    ],
)

# ---------------------------------------------------------------- 31 ように
GRAMMAR[31] = dict(
    name="ように", reading="ように",
    meaning_en="so that ~; in order that ~",
    similar="ために、ようにする、ようになる",
    details=dict(
        formula="<strong>可能動詞・無意志動詞［辞書形］</strong>＋ <strong>ように</strong><br>"
                "<strong>動詞［ない形］</strong>＋ <strong>ように</strong>",
        notes_ja="『〜という状態が実現できるように』『〜という悪いことが起きないように』と願って行動するときに使います。<br>"
                 "前に来るのは、<strong>①可能動詞（話せる、見える、聞こえる）</strong>、<strong>②自分の意志でコントロールできない動詞（わかる、治る、間に合う）</strong>、<strong>③ない形（忘れない、かぜをひかない）</strong>です。",
        notes_en="Expresses purpose when the goal is a state, ability, or avoidance ('so that ~ can / so as not to ~'). "
                 "Preceded by: (1) potential verbs (話せる, 見える), (2) non-volitional verbs (わかる, 治る, 間に合う), or (3) negative ない-form (忘れない, 遅れない).",
        nuance_ja="また、後ろの教室の生徒が『前がよく見えるように』先生が字を大きく書く、のように<strong>前と後ろの主語が違うとき</strong>も「〜ように」を使います。",
        nuance_en="Also used whenever the subjects of the first and second clauses are different (e.g. the teacher writes big so that the students can see).",
        trap_ja="①「行く」「買う」「勉強する」のような意志動詞の辞書形には目的の「ように」は使いません（その場合は「〜ために」を使います）。<br>"
                "②「忘れないために」ではなく「<strong>忘れないように</strong>」と言います。",
        trap_en="① Do not use purpose ように directly after volitional dictionary verbs like 買う or 勉強する (use ために). "
                "② With negative forms ('so as not to forget'), always use 〜ないように.",
        contrast=[
            dict(type="wrong", sentence="{大切|たいせつ}な{約束|やくそく}を{忘|わす}れないために、手帳にメモしました。",
                 reason_ja="否定形「〜ない」の後ろは「ために」ではなく「ように」を使います。",
                 reason_en="After a negative ない-form, use ように, not ために."),
            dict(type="correct", sentence="{大切|たいせつ}な{約束|やくそく}を{忘|わす}れないように、{手帳|てちょう}にメモしました。",
                 reason_ja="動詞ない形 ＋ ように。",
                 reason_en="Verb ない-form + ように."),
            dict(type="correct", sentence="後ろの{席|せき}の{人|ひと}にもよく{聞|き}こえるように、{大|おお}きい{声|こえ}で{話|はな}しました。",
                 reason_ja="「聞こえる（無意志・可能）」＋ ように。",
                 reason_en="聞こえる + ように ('so that even people in the back seats can hear well')."),
        ],
        comparison=[
            dict(form="可能動詞・ない形 ＋ ように", form_en="so that ~ (ability / negative goal)", badge="状態・可能・否定", badge_type="good",
                 nuance_ja="可能動詞・無意志動詞・ない形に付き、『〜という状態になることを目指して』を表します。",
                 nuance_en="Attaches to potential/non-volitional/negative verbs to indicate a desired state.",
                 example="{終電|しゅうでん}に{間|ま}に{合|あ}うように、{走|はし}って{駅|えき}へ{行|い}きました。"),
            dict(form="意志動詞［辞書形］＋ ために", form_en="in order to ~ (volitional action)", badge="意志動作の目標", badge_type="both",
                 nuance_ja="自分の意志で行う動作を目指して行動するときに使います。",
                 nuance_en="Attaches to volitional dictionary-form verbs.",
                 example="{車|くるま}を{買|か}うために、{貯金|ちょきん}しています。"),
        ],
    ),
    quiz=[
        dict(stem="{漢字|かんじ}を{間違|まちが}えない（　　　）、もう{一度|いちど}ていねいに{見直|みなお}しました。",
             correct="ように",
             distractors=["ために", "のに", "そうに"],
             en="So as not to make any kanji mistakes, I carefully reviewed it one more time.",
             notes_ja="否定形「間違えない」の後ろで『〜しないように』という目的を表すので、「ように」が正解です。",
             notes_en="After a negative ない-form (間違えない), purpose is expressed with ように."),
        dict(stem="{早|はや}くかぜが（　　　）ように、{今日|きょう}は{温|あたた}かいスープを{飲|の}んで{寝|ね}ます。",
             correct="{治|なお}る",
             distractors=["{治|なお}り", "{治|なお}ります", "{治|なお}った"],
             en="So that my cold gets better quickly, I'll drink warm soup and go to bed today.",
             notes_ja="「治る」は無意志動詞（状態の変化）なので、辞書形「治る」＋「ように」にします。",
             notes_en="治る is a non-volitional verb, taking dictionary form 治る + ように."),
        dict(stem="{日本|にほん}の{新聞|しんぶん}が（　　　）ように、{毎日|まいにち}{新|あたら}しい{漢字|かんじ}を{覚|おぼ}えています。",
             correct="{読|よ}める",
             distractors=["{読|よ}みます", "{読|よ}んで", "{読|よ}んだ"],
             en="So that I can read Japanese newspapers, I memorize new kanji every day.",
             notes_ja="可能動詞の辞書形「読める」＋「ように」で『読める状態になることを目指して』を表します。",
             notes_en="Potential verb 読める + ように ('so that I can read')."),
        dict(stem="{小|ちい}さい{子供|こども}にも{意味|いみ}が（　　　）ように、やさしい{言葉|ことば}で{説明|せつめい}しました。",
             correct="わかる",
             distractors=["わかります", "わかって", "わかった"],
             en="I explained it in easy words so that even small children could understand the meaning.",
             notes_ja="「わかる」は状態を表す動詞なので、辞書形「わかる」＋「ように」が正解です。",
             notes_en="わかる takes dictionary form + ように."),
    ],
)

# ---------------------------------------------------------------- J(): shorthand ruby expansion
import re as _re

def _J(s):
    if not isinstance(s, str):
        return s
    s = s.replace('辞書形', '{辞書|じしょ}{形|けい}').replace('普通形', '{普通|ふつう}{形|けい}')
    s = _re.sub(r'(ます|て|ない|た|使役|受身|可能|意向|命令|禁止|条件|ば)形', lambda m: m.group(1) + '{形|けい}', s)
    s = s.replace('ナ形容詞', 'ナ{形容詞|けいようし}').replace('イ形容詞', 'イ{形容詞|けいようし}')
    s = s.replace('{{', '{')
    return s

def _walk(o):
    if isinstance(o, dict):
        return {k: (_walk(v) if k not in ('en', 'notes_en', 'reason_en', 'nuance_en', 'form_en', 'trap_en', 'meaning_en') else v) for k, v in o.items()}
    if isinstance(o, list):
        return [_walk(x) for x in o]
    return _J(o)

for _g in GRAMMAR:
    GRAMMAR[_g] = _walk(GRAMMAR[_g])
