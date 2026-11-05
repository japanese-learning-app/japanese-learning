# -*- coding: utf-8 -*-
"""
N4 grammar textbook details + practice questions, gids 32-62 (hand-authored).
Format: see build_grammar.py docstring.
"""

GRAMMAR = {}

# ---------------------------------------------------------------- 32 がる／たがる
GRAMMAR[32] = dict(
    name="がる／たがる", reading="がる",
    meaning_en="show signs of feeling ~ / want to do ~ (third person)",
    similar="たい、ほしい、そうだ（様態）",
    details=dict(
        formula="<strong>イ形容詞（〜い → 〜がる）</strong>：ほしがる・さびしがる・{怖|こわ}がる<br>"
                "<strong>ナ形容詞（語幹 ＋ がる）</strong>：いやがる・{残念|ざんねん}がる<br>"
                "<strong>動詞ます形 ＋ たがる</strong>：{行|い}きたがる・{食|た}べたがる<br>"
                "※「<strong>〜がっている／〜たがっている</strong>」の形で使うことが多い",
        notes_ja="話し手（私）以外の第三者（あの人・子ども・ペットなど）が、気持ちや欲求を態度・言葉・表情に出しているときに使います。<br>"
                 "日本語では「たい」「ほしい」「うれしい」「さびしい」などの感情・願望を表す言葉は、そのままでは第三者の現在の気持ちに使えません。<br>"
                 "例：×弟は新しいゲームがほしいです。 → ○{弟|おとうと}は{新|あたら}しいゲームを<strong>ほしがっています</strong>。<br>"
                 "例：×妹も一緒に行きたいです。 → ○{妹|いもうと}も{一緒|いっしょ}に<strong>{行|い}きたがっています</strong>。<br>"
                 "注意：「〜がほしい」が「〜<strong>を</strong>ほしがる」、「〜が食べたい」が「〜<strong>を</strong>食べたがる」のように、助詞が「を」に変わることが多いです。",
        notes_en="Used when a third person (someone other than the speaker, such as a child, friend, or pet) openly shows a feeling or desire through their behavior, words, or expression. "
                 "In Japanese, words of inner feeling and desire (たい, ほしい, さびしい, etc.) cannot directly state a third person's present state in plain assertions. "
                 "Instead, attach がる / たがる (usually in the 〜がっている / 〜たがっている form). Note that the object particle often shifts from が to を (新しい靴をほしがっている).",
        nuance_ja="「〜たがっている」は、本人が「行きたい！」「食べたい！」と言ったり、そういう態度を見せたりしている客観的な様子を描写します。"
                  "そのため、目上の人（先生・上司など）に対して「先生も食べたがっています」と言うと、子ども扱いしているようで失礼になります。"
                  "目上の人には「先生も召し上がりたいそうです」「行かれるそうです」や「いかがですか」を使います。",
        nuance_en="Because 〜がる / 〜たがる describes observable outward behavior ('acting like they want to...'), using it for superiors (teachers, bosses) sounds patronizing and rude. "
                  "For superiors, use hearsay (〜たいそうです) or honorific expressions instead.",
        trap_ja="①自分の現在の気持ちには使いません。×私は水を飲みたがっています → ○{私|わたし}は{水|みず}が{飲|の}みたいです<br>"
                "②現在の様子を表すときは「〜がっています／〜たがっています」（ている形）にするのが自然です。<br>"
                "③助詞の変化に注意：「車がほしい」→「{車|くるま}<strong>を</strong>ほしがっている」<br>"
                "④目上の人には使わず、「〜たいそうです」「〜たいとおっしゃっています」を使います。",
        trap_en="① Never use がる/たがる for your own current feelings (use たい/ほしい). "
                "② For an ongoing state right now, use the ている form (ほしがっている / 行きたがっている). "
                "③ Watch the particle change from が to を (おもちゃをほしがる). "
                "④ Do not use it for superiors.",
        contrast=[
            dict(type="wrong", sentence="{弟|おとうと}は{新|あたら}しい{自転車|じてんしゃ}がほしいです。",
                 reason_ja="「ほしい」は話し手（私）の気持ちを表すので、第三者（弟）の文ではそのまま使えません。",
                 reason_en="ほしい directly expresses the speaker's own desire and cannot state a third person's state directly."),
            dict(type="correct", sentence="{弟|おとうと}は{新|あたら}しい{自転車|じてんしゃ}をほしがっています。",
                 reason_ja="第三者（弟）がほしそうにしている様子は「〜をほしがっています」で表します。",
                 reason_en="Use 〜をほしがっています to describe a third person showing that they want something."),
            dict(type="correct", sentence="{私|わたし}は{新|あたら}しい{自転車|じてんしゃ}がほしいです。",
                 reason_ja="主語が「私」のときは「〜がほしいです」を使います。",
                 reason_en="When the subject is 'I', use 〜がほしいです."),
        ],
        comparison=[
            dict(form="〜たい／〜ほしい", form_en="1st person desire", badge="自分", badge_type="good",
                 nuance_ja="話し手自身（私）の願望・欲求、または相手への直接の質問（何を飲みたいですか）に使います。",
                 nuance_en="Used for the speaker's own desire, or when asking the listener directly.",
                 example="{私|わたし}は{京都|きょうと}へ{行|い}きたいです。"),
            dict(form="〜たがる／〜がる", form_en="3rd person observable desire/feeling", badge="第三者・様子", badge_type="both",
                 nuance_ja="第三者が気持ちや欲求を態度・言葉に出している様子を客観的に表します。",
                 nuance_en="Describes a third person openly showing a desire or emotion.",
                 example="{娘|むすめ}は{犬|いぬ}を{飼|か}いたがっています。"),
            dict(form="〜たいそうだ／〜たいと言っている", form_en="hearsay of 3rd person desire", badge="伝聞", badge_type="neutral",
                 nuance_ja="本人から聞いた希望をそのまま伝える表現で、目上の人にも丁寧に使えます。",
                 nuance_en="Reports someone's stated wish via hearsay; polite enough to use for superiors.",
                 example="{田中|たなか}さんも{参加|さんか}したいと{言|い}っています。"),
        ],
    ),
    quiz=[
        dict(stem="うちの{猫|ねこ}は{外|そと}へ（　　　）、ドアの{前|まえ}でずっと{鳴|な}いています。",
             correct="{出|で}たがって", distractors=["{出|で}たくて", "{出|で}たそうで", "{出|で}ほしくて"],
             en="Our cat wants to go outside and keeps meowing in front of the door.",
             notes_ja="第三者（ここでは猫）が「外に出たい」という様子を態度で見せているので、「ます形＋たがる」のて形「出たがって」を使います。"
                      "「出たくて」は主に自分の気持ちに使います。",
             notes_en="Since a third party (the cat) is visibly showing a desire to go out, use 出たがって (from 出たがる). 出たくて is mainly for the speaker's own feeling."),
        dict(stem="{小|ちい}さい{息子|むすこ}は{暗|くら}い{部屋|へや}を（　　　）、{夜|よる}は{一人|ひとり}で{寝|ね}られません。",
             correct="{怖|こわ}がって", distractors=["{怖|こわ}くて", "{怖|こわ}いたがって", "{怖|こわ}そうに"],
             en="My young son is afraid of dark rooms and cannot sleep alone at night.",
             notes_ja="イ形容詞「怖い」の語幹に「がる」を付けた「怖がる」で、第三者（息子）が怖そうな態度を見せることを表します。助詞「を」とも自然につながります。",
             notes_en="Drop い from 怖い and add がる → 怖がる to show that a third person (my son) acts afraid of something (marked by を)."),
        dict(stem="{弟|おとうと}は、{兄|あに}が{買|か}ったばかりのカメラをとても（　　　）います。",
             correct="ほしがって", distractors=["ほしくて", "ほしがりて", "ほしそうに"],
             en="My younger brother really wants the camera that my older brother just bought.",
             notes_ja="第三者（弟）が「〜をほしい」と態度に出しているときは「〜をほしがっています」と言います。助詞が「を」なので「ほしくて」や「ほしそうに」は続きません。",
             notes_en="When a third person wants something (marked with を), use ほしがっています. ほしくて cannot take を + います."),
        dict(stem="A：{林|はやし}さんも{今度|こんど}のハイキングに{来|き}ますか。<br>B：ええ、とても（　　　）いましたよ。",
             correct="{行|い}きたがって", distractors=["{行|い}きたくて", "{行|い}きがって", "{行|い}きたいで"],
             en="A: Is Ms. Hayashi coming on the next hike too? B: Yes, she was really eager to go.",
             notes_ja="第三者（林さん）が行きたい様子を見せていたので、「ます形＋たがる」＋「ていました」で「行きたがっていました」となります。",
             notes_en="To describe a third person (Ms. Hayashi) showing eagerness to go, use Verb-masu stem + たがっていました (行きたがっていました)."),
    ],
)

# ---------------------------------------------------------------- 33 たばかり
GRAMMAR[33] = dict(
    name="たばかり", reading="たばかり",
    meaning_en="just finished doing ~",
    similar="たところだ、てから",
    details=dict(
        formula="<strong>動詞た形</strong> ＋ <strong>ばかりだ／ばかりの ＋ 名詞</strong><br>"
                "例：{食|た}べたばかりです／{買|か}ったばかりの{靴|くつ}",
        notes_ja="ある動作や出来事が終わってから、まだあまり時間が経っていないと話し手が感じていることを表します。<br>"
                 "例：さっき<strong>{昼|ひる}ごはんを{食|た}べたばかり</strong>なので、おなかがいっぱいです。<br>"
                 "実際に数分前のことだけでなく、数週間前・数か月前のことでも、話し手が主観的に「つい最近のことだ」と感じていれば使えます。<br>"
                 "例：{先月|せんげつ}{日本|にほん}へ<strong>{来|き}たばかり</strong>で、まだ{道|みち}がわかりません。<br>"
                 "後ろに名詞を置くときは「<strong>〜たばかりの ＋ 名詞</strong>」になります（{洗|あら}ったばかりのコップ）。",
        notes_en="Expresses that an action or event finished only a short time ago in the speaker's view. "
                 "Unlike 〜たところだ (which strictly requires only seconds or minutes to have passed), 〜たばかり reflects the speaker's subjective feeling: "
                 "you can say 先月日本に来たばかりです ('I just came to Japan last month'). "
                 "Before a noun, add の: 買ったばかりの服 ('clothes I just bought').",
        nuance_ja="「〜たところだ」は時計の上で本当に「たった今終わった直後」にしか使えませんが、「〜たばかりだ」は話し手の気持ち次第で、"
                  "「先月結婚したばかり」「去年入社したばかり」のようにも使えます。"
                  "また、「せっかく洗ったばかりなのに、また汚れた」のように、残念な気持ちを表す文でもよく使われます。",
        nuance_en="While 〜たところだ is strictly objective (moments after completion), 〜たばかりだ is subjective and works even with 先月 or 去年 if it feels recent to the speaker. "
                  "It is also frequently used with せっかく or なのに to express frustration ('I only just washed it, and it's dirty again').",
        trap_ja="①必ず動詞の<strong>た形</strong>に接続します。×食べるばかりだ（意味が変わる） → ○{食|た}べたばかりだ<br>"
                "②名詞を修飾するときは「の」が必要です。×買ったばかり靴 → ○{買|か}ったばかり<strong>の</strong>{靴|くつ}<br>"
                "③「先週たところだ」とは言えませんが、「{先週|せんしゅう}〜たばかりだ」は言えます。",
        trap_en="① Always use the past plain form (た-form) for 'just did': 食べたばかりだ (辞書形 + ばかり means 'do nothing but ~'). "
                "② Add の before a noun: 買ったばかりの靴. "
                "③ With time words like 先週 or 先月, use たばかり, never たところ.",
        contrast=[
            dict(type="wrong", sentence="{先月|せんげつ}この{会社|かいしゃ}に{入|はい}ったところです。",
                 reason_ja="「たところ」は動作の直後（数秒〜数分）にしか使えないため、「先月」とは一緒に使えません。",
                 reason_en="〜たところ only works immediately after an action (seconds/minutes), so it cannot pair with 先月."),
            dict(type="correct", sentence="{先月|せんげつ}この{会社|かいしゃ}に{入|はい}ったばかりです。",
                 reason_ja="話し手が「まだ最近だ」と感じていれば、「先月」と「〜たばかり」を一緒に使えます。",
                 reason_en="〜たばかり is subjective and works naturally with 先月."),
            dict(type="correct", sentence="これは{昨日|きのう}{買|か}ったばかりの{時計|とけい}です。",
                 reason_ja="名詞「時計」の前では「〜たばかりの＋名詞」の形にします。",
                 reason_en="Use 〜たばかりの before a noun (時計)."),
        ],
        comparison=[
            dict(form="Vた ＋ ばかりだ", form_en="just did (subjective recent past)", badge="主観的", badge_type="good",
                 nuance_ja="話し手が「つい最近だ」と感じれば、さっきのことにも、先月・去年のことにも使えます。",
                 nuance_en="Subjectively recent: works both for moments ago and for last month/year.",
                 example="{先月|せんげつ}{引|ひ}っ{越|こ}したばかりです。"),
            dict(form="Vた ＋ ところだ", form_en="just finished (strictly right now)", badge="直後のみ", badge_type="both",
                 nuance_ja="動作が終わったほんの直後の場面にだけ使います。「先月〜たところだ」とは言えません。",
                 nuance_en="Strictly right after an action finishes; cannot be used with 'last month'.",
                 example="たった{今|いま}、バスが{出|で}たところです。"),
            dict(form="V辞書形 ＋ ばかり", form_en="do nothing but ~", badge="限定", badge_type="neutral",
                 nuance_ja="た形ではなく辞書形や「て形＋ばかりいる」にすると、「そればかりする」という別の意味になります。",
                 nuance_en="With dictionary form or てばかりいる, it means 'do nothing but ~'.",
                 example="{休|やす}みの{日|ひ}は{寝|ね}てばかりいます。"),
        ],
    ),
    quiz=[
        dict(stem="さっき{昼|ひる}ごはんを（　　　）なので、まだおなかが{空|す}いていません。",
             correct="{食|た}べたばかり", distractors=["{食|た}べるばかり", "{食|た}べてばかり", "{食|た}べたところ"],
             en="Because I just ate lunch a little while ago, I'm not hungry yet.",
             notes_ja="「さっき〜したから、まだ…ない」と直後の状態・理由を述べるときは「た形＋ばかり（なので）」を使います。"
                      "「たところなので」より「たばかりなので」のほうが理由説明として自然です。",
             notes_en="Use Verb-た + ばかりなので to explain a reason based on having just done something a short while ago."),
        dict(stem="この{白い|しろい}シャツは、けさ（　　　）シャツなのに、コーヒーをこぼしてしまいました。",
             correct="{洗|あら}ったばかりの", distractors=["{洗|あら}ったばかりな", "{洗|あら}ったばかりで", "{洗|あら}うばかりの"],
             en="Even though this white shirt is one I just washed this morning, I spilled coffee on it.",
             notes_ja="後ろに名詞「シャツ」があるので、「た形＋ばかりの＋名詞」の形「洗ったばかりの」が正解です。",
             notes_en="When modifying a noun (シャツ), attach の after ばかり: 洗ったばかりのシャツ."),
        dict(stem="{兄|あに}は{先月|せんげつ}{大学|だいがく}を（　　　）で、{今月|こんげつ}から{銀行|ぎんこう}で{働|はたら}いています。",
             correct="{卒業|そつぎょう}したばかり", distractors=["{卒業|そつぎょう}したところ", "{卒業|そつぎょう}するばかり", "{卒業|そつぎょう}しているところ"],
             en="My older brother just graduated from university last month and has been working at a bank since this month.",
             notes_ja="「先月」のように少し前のことでも、話し手が「つい最近だ」と感じるときは「た形＋ばかり」を使います。「たところ」は「先月」と一緒には使えません。",
             notes_en="With time words like 先月 ('last month'), use 〜たばかり (subjective recency), not 〜たところ."),
        dict(stem="A：もうこの{小説|しょうせつ}を{全部|ぜんぶ}{読|よ}みましたか。<br>B：いいえ、{昨日|きのう}（　　　）ですから、まだ{最初|さいしょ}のページですよ。",
             correct="{買|か}ったばかり", distractors=["{買|か}ったところ", "{買|か}うばかり", "{買|か}っているところ"],
             en="A: Have you already read this whole novel? B: No, I just bought it yesterday, so I'm still on the first page.",
             notes_ja="「昨日」という時間語と一緒に「まだ買ったばかりだ」と主観的な新しさを表せるのは「買ったばかり」です。",
             notes_en="With 昨日 ('yesterday'), use 買ったばかり to express that you only just bought it."),
    ],
)

# ---------------------------------------------------------------- 34 ところだ
GRAMMAR[34] = dict(
    name="ところだ", reading="ところだ",
    meaning_en="just about to do / in the middle of doing / just did",
    similar="たばかり、ようとしている、最中だ",
    details=dict(
        formula="① <strong>動詞辞書形 ＋ ところだ</strong>：これからすぐ〜する（直前）<br>"
                "② <strong>動詞ている形 ＋ ところだ</strong>：{今|いま}ちょうど〜している（進行中）<br>"
                "③ <strong>動詞た形 ＋ ところだ</strong>：たった{今|いま}〜し{終|お}わった（直後）",
        notes_ja="前の動詞の形によって、動作のどの時点（直前・最中・直後）にいるかを表す表現です。<br>"
                 "①<strong>辞書形＋ところだ</strong>：「ちょうど今から〜する直前だ」<br>"
                 "例：これから{昼|ひる}ごはんを<strong>{食|た}べるところです</strong>。（＝まだ食べていない）<br>"
                 "②<strong>ている形＋ところだ</strong>：「今ちょうど〜している最中だ」<br>"
                 "例：{今|いま}、{資料|しりょう}を<strong>コピーしているところです</strong>。（＝今やっている）<br>"
                 "③<strong>た形＋ところだ</strong>：「たった今〜し終わった直後だ」<br>"
                 "例：たった{今|いま}、{駅|えき}に<strong>{着|つ}いたところです</strong>。（＝すぐ前に着いた）",
        notes_en="Depending on the verb form before ところだ, it pinpoints the exact stage of an action: "
                 "(1) Dictionary form + ところだ = just about to do (not started yet); "
                 "(2) ている form + ところだ = right in the middle of doing; "
                 "(3) た form + ところだ = just finished doing moments ago.",
        nuance_ja="電話や職場で「今どういう状況か」を相手にわかりやすく伝えるときによく使われます。"
                  "「ちょうど今〜するところです」「たった今〜したところです」のように、「ちょうど」「これから」「今」「たった今」などの副詞とセットで使われることが多いのが特徴です。",
        nuance_en="Very common on the phone or at work to report your exact status right now. "
                  "Frequently pairs with time adverbs: これから + Vる-ところだ, 今 + Vている-ところだ, and たった今 + Vた-ところだ.",
        trap_ja="①「これから」「今」「たった今」などの副詞を見て、辞書形・ている形・た形を正しく選びましょう。<br>"
                "②「た形＋ところだ」は本当に終わった直後（数秒〜数分）にしか使えません。「去年日本に来たところだ」は間違いです（→{来|き}たばかりだ）。<br>"
                "③「ているところだ」は継続動詞（調べる・作るなど）と一緒に使います。",
        trap_en="① Match time adverbs carefully: これから → Vる, 今 → Vている, たった今 → Vた. "
                "② Vた + ところだ works only seconds or minutes after completion (never with 昨日 or 先月). "
                "③ Vている + ところだ requires an action verb in progress.",
        contrast=[
            dict(type="wrong", sentence="たった{今|いま}、{家|いえ}を{出|で}るところです。",
                 reason_ja="「たった今」は過去の直後を表すので、辞書形「出るところ」とは合いません。",
                 reason_en="たった今 refers to the immediate past, so it clashes with the dictionary form 出るところ."),
            dict(type="correct", sentence="たった{今|いま}、{家|いえ}を{出|で}たところです。",
                 reason_ja="「たった今」には「た形＋ところだ」（直後）を合わせます。",
                 reason_en="Pair たった今 with Verb-た + ところだ ('just left right now')."),
            dict(type="correct", sentence="これから{家|いえ}を{出|で}るところです。",
                 reason_ja="「これから」には「辞書形＋ところだ」（直前）を合わせます。",
                 reason_en="Pair これから with Verb-dictionary form + ところだ ('just about to leave')."),
        ],
        comparison=[
            dict(form="V辞書形 ＋ ところだ", form_en="just about to do", badge="直前", badge_type="good",
                 nuance_ja="まだ始めておらず、「これからすぐ始める」という直前の時点を表します。",
                 nuance_en="Not started yet; about to begin right now.",
                 example="これから{会議|かいぎ}が{始|はじ}まるところです。"),
            dict(form="Vている ＋ ところだ", form_en="in the middle of doing", badge="進行中", badge_type="both",
                 nuance_ja="今まさにその動作を行っている最中であることを強調します。",
                 nuance_en="Emphasizes being right in the middle of an action.",
                 example="{今|いま}、{原因|げんいん}を{調|しら}べているところです。"),
            dict(form="Vた ＋ ところだ", form_en="just finished doing", badge="直後", badge_type="neutral",
                 nuance_ja="動作が終わったばかりのほんの直後の時点を表します。",
                 nuance_en="Marks the moment immediately after an action finishes.",
                 example="たった{今|いま}、電車が{行|い}ってしまったところです。"),
        ],
    ),
    quiz=[
        dict(stem="A：レポートはもう{書|か}き{終|お}わりましたか。<br>B：いいえ、これから（　　　）です。",
             correct="{書|か}くところ", distractors=["{書|か}いたところ", "{書|か}いたばかり", "{書|か}いているばかり"],
             en="A: Have you finished writing the report already? B: No, I'm just about to write it now.",
             notes_ja="「いいえ、これから〜」とあるので、まだ書いておらず、これから始める直前を表す「辞書形＋ところ（書くところ）」が正解です。",
             notes_en="With いいえ、これから ('No, from now...'), the action hasn't started yet, so use dictionary form + ところ (書くところ)."),
        dict(stem="A：すみません、{予約|よやく}の{時間|じかん}に{少|すこ}し{遅|おく}れそうです。<br>B：わかりました。{私|わたし}もたった{今|いま}レストランに（　　　）ですから、{大丈夫|だいじょうぶ}ですよ。",
             correct="{着|つ}いたところ", distractors=["{着|つ}くところ", "{着|つ}いているところ", "{着|つ}くばかり"],
             en="A: Sorry, it looks like I'll be a little late for our reservation time. B: Got it. I also just arrived at the restaurant right now, so it's fine.",
             notes_ja="「たった今」があるので、動作が完了した直後を表す「た形＋ところ（着いたところ）」を使います。",
             notes_en="たった今 ('just this instant') signals immediate completion, requiring Verb-た + ところ (着いたところ)."),
        dict(stem="A：{田中|たなか}さん、{会議|かいぎ}の{資料|しりょう}はありますか。<br>B：すみません、{今|いま}{急|いそ}いで（　　　）ですので、もう{少|すこ}しお{待|ま}ちください。",
             correct="コピーしているところ", distractors=["コピーするところ", "コピーしたところ", "コピーしたばかり"],
             en="A: Mr. Tanaka, do you have the meeting handouts? B: Sorry, I'm in the middle of copying them right now, so please wait a little longer.",
             notes_ja="「今急いで〜」「もう少しお待ちください」から、今まさに作業中であることがわかるので「ている形＋ところ（コピーしているところ）」が正解です。",
             notes_en="今急いで and 'please wait a bit longer' show the action is currently in progress: コピーしているところ."),
        dict(stem="これからお{風呂|ふろ}に（　　　）だったのに、{宅配便|たくはいびん}が届きました。",
             correct="{入|はい}るところ", distractors=["{入|はい}ったところ", "{入|はい}ったばかり", "{入|はい}るばかり"],
             en="Just as I was about to take a bath, a delivery package arrived.",
             notes_ja="「これから〜だったのに」と、動作の直前に邪魔が入った場面なので「辞書形＋ところ（入るところ）」を使います。",
             notes_en="これから...だったのに describes being right on the verge of doing something when interrupted: 入るところ."),
    ],
)

# ---------------------------------------------------------------- 35 受身（られる）
GRAMMAR[35] = dict(
    name="受身（られる）", reading="られる",
    meaning_en="passive voice: be done to ~ (direct & inanimate passive)",
    similar="てもらう、させられる、可能形",
    details=dict(
        formula="<strong>Ⅰグループ（五段）</strong>：う段 → <strong>あ段 ＋ れる</strong>（{書|か}く→{書|か}かれる、{買|か}う→{買|か}われる）<br>"
                "<strong>Ⅱグループ（一段）</strong>：る → <strong>られる</strong>（ほめる→ほめられる、{見|み}る→{見|み}られる）<br>"
                "<strong>Ⅲグループ</strong>：する → <strong>される</strong>、{来|く}る → <strong>{来|こ}られる</strong>",
        notes_ja="「A（私など）が B に〜される」のように、動作を受ける側から述べる文（受身文）です。<br>"
                 "①<strong>直接の受身（人から人へ）</strong>：動作をする人（B）には助詞「<strong>に</strong>」を付けます。<br>"
                 "例：{私|わたし}は{先生|せんせい}<strong>に</strong><strong>ほめられました</strong>。<br>"
                 "②<strong>物を主語にする受身（事実の説明）</strong>：有名な建物・本・イベントなどが「作られた・書かれた・{開|ひら}かれる」と言うときによく使います。動作主が特に決まっていないときは「に」は使いません。<br>"
                 "例：このお{寺|てら}は500{年前|ねんまえ}に<strong>{建|た}てられました</strong>。<br>"
                 "※発明・発見・生産などの受身で、元の材料や作者をはっきり示すときは「<strong>によって</strong>」や「<strong>から</strong>」を使います（この小説は有名な作家によって書かれました）。",
        notes_en="The passive voice describes an action from the receiver's perspective. "
                 "(1) Direct passive: 'A is [verb]-ed by B', where the doer B is marked by に (先生にほめられた). "
                 "(2) Inanimate passive for facts/events: used when buildings, books, or events are built, written, or held (このお寺は500年前に建てられた). "
                 "For creators/inventors, によって is often used; for raw materials, から/で is used.",
        nuance_ja="人から良いことをされたとき、受身「母に手伝われました」と言うと不自然になります。"
                  "感謝の気持ちがある場面では受身ではなく、「母に手伝ってもらいました」「母が手伝ってくれました」という授受表現を使うのが日本語の大切なルールです（ただし「ほめられる」「招待される」「頼まれる」は受身で自然に言えます）。",
        nuance_en="When someone does a helpful favor for you, using the passive (×母に料理を作られた) sounds unnatural or annoyed. "
                  "For appreciated favors, use てもらう / てくれる instead (though verbs like ほめられる 'be praised' and 招待される 'be invited' naturally use the passive).",
        trap_ja="①Ⅰグループの「う」で終わる動詞は「あ＋れる」ではなく「<strong>わ＋れる</strong>」です。{言|い}う→{言|い}<strong>わ</strong>れる、{笑|わら}う→{笑|わら}<strong>わ</strong>れる<br>"
                "②動作をする人は「<strong>に</strong>」で表します（×先生からほめられた → ○{先生|せんせい}<strong>に</strong>ほめられた）。<br>"
                "③Ⅱグループ（見られる・食べられる）の受身形は、可能形とまったく同じ形なので文脈で区別します。",
        trap_en="① Group 1 verbs ending in う change to われる (言う → 言われる, not ×言あれる). "
                "② Mark the agent (doer) with に: 先生にほめられた. "
                "③ For Group 2 verbs, the passive form (見られる) looks identical to the potential form; distinguish by context and particles.",
        contrast=[
            dict(type="wrong", sentence="{私|わたし}は{部長|ぶちょう}に{名前|なまえ}を{呼|よ}びられました。",
                 reason_ja="「呼ぶ」はⅠグループ動詞なので、「呼ばれる」になります。「呼びられる」は誤りです。",
                 reason_en="呼ぶ is a Group 1 verb, so its passive is 呼ばれる, not ×呼びられる."),
            dict(type="correct", sentence="{私|わたし}は{部長|ぶちょう}に{名前|なまえ}を{呼|よ}ばれました。",
                 reason_ja="Ⅰグループ「呼ぶ（bu）」→「呼ばれる（bareru）」。動作主の部長には「に」を付けます。",
                 reason_en="Group 1 呼ぶ → 呼ばれる, with the agent marked by に."),
            dict(type="correct", sentence="このホールで{来月|らいげつ}、{国際|こくさい}{会議|かいぎ}が{開|ひら}かれます。",
                 reason_ja="行事や建物の事実を述べるときは、誰が{開|ひら}くか言わずに「〜が{開|ひら}かれます」と受身で表します。",
                 reason_en="Events and public facts naturally use the agentless passive: 国際会議が{開|ひら}かれます."),
        ],
        comparison=[
            dict(form="Aは Bに V（ら）れる", form_en="direct passive", badge="直接受身", badge_type="good",
                 nuance_ja="AがBから直接その動作を受けることを表します（ほめられる・注意される・頼まれるなど）。",
                 nuance_en="A directly receives the action from B (be praised, warned, asked, etc.).",
                 example="{先生|せんせい}に{発音|はつおん}をほめられました。"),
            dict(form="（物が）V（ら）れる", form_en="inanimate / factual passive", badge="事実説明", badge_type="both",
                 nuance_ja="建物・本・イベント・製品などについて、客観的な事実を説明するときに使います。",
                 nuance_en="States objective facts about buildings, books, products, or events.",
                 example="この{歌|うた}は{世界中|せかいじゅう}で{歌|うた}われています。"),
            dict(form="Aは Bに Vてもらう", form_en="receive a favor", badge="感謝・恩恵", badge_type="neutral",
                 nuance_ja="相手が自分のために親切にしてくれたときは、受身ではなく「〜てもらう」を使います。",
                 nuance_en="When someone kindly does something for your benefit, use てもらう rather than passive.",
                 example="{先輩|せんぱい}に{仕事|しごと}を{手伝|てつだ}ってもらいました。"),
        ],
    ),
    quiz=[
        dict(stem="{宿題|しゅくだい}を{忘|わす}れて、{先生|せんせい}に（　　　）しまいました。",
             correct="{注意|ちゅうい}されて", distractors=["{注意|ちゅうい}して", "{注意|ちゅうい}させて", "{注意|ちゅうい}しられて"],
             en="I forgot my homework and ended up being warned by the teacher.",
             notes_ja="「先生に」とあり、私が先生から注意を受けた側なので、Ⅲグループ「注意する」の受身形「注意されて」が正解です。",
             notes_en="Since 'I' received the warning from the teacher (先生に), use the passive of 注意する → 注意されて."),
        dict(stem="この{古|ふる}いお{城|しろ}は、{約|やく}400{年前|ねんまえ}に（　　　）そうです。",
             correct="{建|た}てられた", distractors=["{建|た}てた", "{建|た}てさせた", "{建|た}てりられた"],
             en="I hear that this old castle was built about 400 years ago.",
             notes_ja="主語が「お城」なので、Ⅱグループ「建てる」の受身形「建てられた」を使います。",
             notes_en="The subject is the castle (お城), so use the passive of Group 2 建てる → 建てられた."),
        dict(stem="きのう、{駅|えき}の{前|まえ}で{知|し}らない{外国人|がいこくじん}に{英語|えいご}で{道|みち}を（　　　）。",
             correct="{聞|き}かれました", distractors=["{聞|き}きました", "{聞|き}かせました", "{聞|き}きられました"],
             en="Yesterday, I was asked for directions in English by a foreign stranger in front of the station.",
             notes_ja="「知らない外国人に（私が）道を〜」なので受身文にします。「聞く（kiku）」はⅠグループなので受身形は「聞かれました」です。",
             notes_en="'I' was asked by a stranger (外国人に), requiring the passive of Group 1 聞く → 聞かれました."),
        dict(stem="この{地域|ちいき}では、お{米|こめ}からおいしいお{酒|さけ}が（　　　）います。",
             correct="{作|つく}られて", distractors=["{作|つく}って", "{作|つく}らせて", "{作|つく}りられて"],
             en="In this region, delicious sake is made from rice.",
             notes_ja="主語が「お酒が」なので、Ⅰグループ「作る」の受身形「作られて（います）」が正解です。",
             notes_en="With お酒が as the subject, use the passive of Group 1 作る → 作られています."),
    ],
)

# ---------------------------------------------------------------- 36 使役（させる）
GRAMMAR[36] = dict(
    name="使役（させる）", reading="させる",
    meaning_en="causative voice: make / let someone do ~",
    similar="させられる、てあげる、てもらう",
    details=dict(
        formula="<strong>Ⅰグループ（五段）</strong>：う段 → <strong>あ段 ＋ せる</strong>（{行|い}く→{行|い}かせる、{買|か}う→{買|か}わせる）<br>"
                "<strong>Ⅱグループ（一段）</strong>：る → <strong>させる</strong>（{食|た}べる→{食|た}べさせる、{着|き}る→{着|き}させる）<br>"
                "<strong>Ⅲグループ</strong>：する → <strong>させる</strong>、{来|く}る → <strong>{来|こ}させる</strong>",
        notes_ja="上の立場の人（親・先生・上司など）が、下の立場の人（子ども・生徒・部下など）に何かをさせるときに使います。意味は文脈によって2つあります。<br>"
                 "①<strong>指示（〜させる）</strong>：やりたくない・関係なく、指示してやらせる。<br>"
                 "例：{母|はは}は{弟|おとうと}に{野菜|やさい}を<strong>{食|た}べさせました</strong>。<br>"
                 "②<strong>許可・放任（〜させてやる／〜させる）</strong>：本人がやりたいことを許してやらせる。<br>"
                 "例：{両親|りょうしん}は{私|わたし}に{好|す}きな{仕事|しごと}を<strong>させてくれました</strong>。<br>"
                 "<strong>★助詞のルール</strong>：<br>"
                 "・元の動詞が<strong>他動詞（〜をV）</strong>のとき：動作をする人は「<strong>に</strong>」（子ども<strong>に</strong>部屋<strong>を</strong>掃除させる）<br>"
                 "・元の動詞が<strong>自動詞（〜をを使わないV）</strong>のとき：動作をする人は「<strong>を</strong>」（または許可なら「に」）（部下<strong>を</strong>出張させる／娘<strong>を</strong>留学させる）",
        notes_en="Used when someone in a higher position (parent, teacher, boss) makes or lets someone in a lower position do something. "
                 "It has two meanings depending on context: (1) directive ('make someone do') and (2) permission ('let someone do'). "
                 "Particle rule: With a transitive verb (which already takes を), the person made to act is marked by に (子どもに野菜を食べさせる). "
                 "With an intransitive verb, the person is usually marked by を (部下を出張させる).",
        nuance_ja="使役形は「上から下への指示・許可」を表すため、目上の人に対して「部長を行かせます」「先生に座らせます」と言うことは絶対にできません。"
                  "目上の人に何かをしてもらうときは「部長に行っていただきます」「先生におかけいただきます」のような敬語・授受表現を使います。",
        nuance_en="Because the causative inherently implies authority over the other person, you can NEVER use it for superiors (×先生に書かせる). "
                  "To ask or have a superior do something, use てもらう / ていただく.",
        trap_ja="①Ⅰグループの「う」で終わる動詞は「<strong>わ＋せる</strong>」になります。{手伝|てつだ}う→{手伝|てつだ}<strong>わ</strong>せる、{洗|あら}う→{洗|あら}<strong>わ</strong>せる<br>"
                "②1つの文に「を」は2つ使えません。×子どもを野菜を食べさせる → ○{子|こ}ども<strong>に</strong>{野菜|やさい}<strong>を</strong>{食|た}べさせる<br>"
                "③自動詞（行く・休む・笑うなど）の使役では、人を「<strong>を</strong>」で表します（{生徒|せいと}<strong>を</strong>{帰|かえ}らせる）。",
        trap_en="① Group 1 verbs ending in う become わせる (手伝う → 手伝わせる). "
                "② Never put two を particles in the same clause: ×子どもを野菜を食べさせる → ○子どもに野菜を食べさせる. "
                "③ With intransitive verbs (行く, 帰る, 笑う), mark the person with を (生徒を帰らせる).",
        contrast=[
            dict(type="wrong", sentence="{母|はは}は{妹|いもうと}を{部屋|へや}を{片付|かたづ}けさせました。",
                 reason_ja="「部屋を片付ける」にすでに「を」があるため、動作をする人（妹）に「を」は使えません。",
                 reason_en="Since 部屋を already uses を, you cannot mark 妹 with a second を."),
            dict(type="correct", sentence="{母|はは}は{妹|いもうと}に{部屋|へや}を{片付|かたづ}けさせました。",
                 reason_ja="他動詞（〜を片付ける）の使役では、動作をする人を「に」で表します。",
                 reason_en="With a transitive verb taking を, mark the person who does the action with に."),
            dict(type="correct", sentence="{部長|ぶちょう}は{田中|たなか}さんを{大阪|おおさか}へ{出張|しゅっちょう}させました。",
                 reason_ja="自動詞（出張する）の使役では、動作をする人を「を」で表します。",
                 reason_en="With an intransitive verb (出張する), mark the person with を."),
        ],
        comparison=[
            dict(form="Aは Bに Nを V（さ）せる", form_en="causative of transitive verb", badge="他動詞", badge_type="good",
                 nuance_ja="目的語「Nを」があるので、動作をする人Bには必ず「に」を使います。",
                 nuance_en="Because Nを is present, the person B takes に.",
                 example="{先生|せんせい}は{生徒|せいと}に{作文|さくぶん}を{書|か}かせました。"),
            dict(form="Aは Bを V（さ）せる", form_en="causative of intransitive verb", badge="自動詞", badge_type="both",
                 nuance_ja="自動詞には「Nを」がないため、動作をする人Bを「を」で表します。",
                 nuance_en="With no direct object Nを, the person B takes を.",
                 example="お{客|きゃく}さまを{長|なが}く{待|ま}たせてはいけません。"),
            dict(form="Aは Bに Vてもらう", form_en="ask/have someone do (equal/polite)", badge="依頼", badge_type="neutral",
                 nuance_ja="上下関係のない相手や目上の人に頼んでやってもらうときは「〜てもらう／〜ていただく」を使います。",
                 nuance_en="When asking a peer or superior for help, use てもらう / ていただく instead of causative.",
                 example="{友人|ゆうじん}に{荷物|にもつ}を{運|はこ}んでもらいました。"),
        ],
    ),
    quiz=[
        dict(stem="{母|はは}は{毎日|まいにち}、{晩|ばん}ごはんの{前|まえ}に{弟|おとうと}に{手|て}を（　　　）います。",
             correct="{洗|あら}わせて", distractors=["{洗|あら}われて", "{洗|あら}あせて", "{洗|あら}いさせて"],
             en="Every day before dinner, my mother makes my younger brother wash his hands.",
             notes_ja="母が弟に「手を洗う」ように指示しているので使役形を使います。Ⅰグループ「洗う（arau）」の使役形は「わ＋せる」で「洗わせて」です。",
             notes_en="The mother makes the younger brother wash his hands. Group 1 洗う becomes 洗わせる → 洗わせて."),
        dict(stem="{熱|ねつ}がある{社員|しゃいん}を{無理|むり}に{働|はたら}かせないで、すぐに（　　　）ください。",
             correct="{休|やす}ませて", distractors=["{休|やす}まれて", "{休|やす}みさせて", "{休|やす}まられて"],
             en="Don't make an employee with a fever work unreasonably; please let them rest right away.",
             notes_ja="社員を「休む」ようにさせる（許可・配慮する）場面なので、Ⅰグループ「休む（yasumu）」の使役形「休ませて（ください）」が正解です。",
             notes_en="To let the employee rest, use the causative of Group 1 休む → 休ませて（ください）."),
        dict(stem="{先生|せんせい}は、{黒板|こくばん}の{字|じ}が{見|み}えにくい{生徒|せいと}を{前|まえ}の{席|せき}に（　　　）。",
             correct="{座|すわ}らせました", distractors=["{座|すわ}られました", "{座|すわ}りさせました", "{座|すわ}らせられました"],
             en="The teacher had the student who couldn't see the blackboard well sit in a front seat.",
             notes_ja="先生が「生徒を前の席に座る」ようにさせたので、Ⅰグループ「座る（suwaru）」の使役形「座らせました」を使います。",
             notes_en="The teacher had the student sit in the front seat: Group 1 座る → 座らせました."),
        dict(stem="うちでは、{子|こ}どもに{自分|じぶん}の{服|ふく}を{自分|じぶん}で（　　　）ようにしています。",
             correct="たたませる", distractors=["たたまれる", "たたみさせる", "たたまされる"],
             en="At our house, we make it a rule to have our children fold their own clothes by themselves.",
             notes_ja="親が子どもに服を「たたむ」ようにさせるので使役形にします。Ⅰグループ「たたむ（tatamu）」の使役形は「たたませる」です。",
             notes_en="Parents have the children fold their own clothes: Group 1 たたむ → たたませる."),
    ],
)

# ---------------------------------------------------------------- 37 使役受身（させられる）
GRAMMAR[37] = dict(
    name="使役受身（させられる）", reading="させられる",
    meaning_en="causative-passive: be made to do ~",
    similar="させる、られる、なければならない",
    details=dict(
        formula="<strong>Ⅰグループ（五段）</strong>：う段 → <strong>あ段 ＋ せられる</strong>（短縮形：<strong>あ段 ＋ される</strong>）<br>"
                "　例：{書|か}く → {書|か}かせられる ／ <strong>{書|か}かされる</strong>、{買|か}う → {買|か}わせられる ／ <strong>{買|か}わされる</strong><br>"
                "　※「<strong>す</strong>」で終わる動詞（{話|はな}す・{直|なお}す）は短縮形なし → <strong>{話|はな}させられる</strong><br>"
                "<strong>Ⅱグループ（一段）</strong>：る → <strong>させられる</strong>（{食|た}べさせられる）<br>"
                "<strong>Ⅲグループ</strong>：する → <strong>させられる</strong>、{来|く}る → <strong>{来|こ}させられる</strong>",
        notes_ja="「（私は）本当はやりたくないのに、誰かに指示されてしかたなく〜した」という気持ちを表す文です。<br>"
                 "指示した人（先生・上司・先輩など）には助詞「<strong>に</strong>」を付けます。<br>"
                 "例：{私|わたし}は{子供のころ|こどものころ}、{母|はは}<strong>に</strong>{嫌|きら}いなニンジンを<strong>{食|た}べさせられました</strong>。<br>"
                 "例：{会議|かいぎ}で{急|きゅう}にスピーチを<strong>させられて</strong>、とても{困|こま}りました。<br>"
                 "<strong>★Ⅰグループの短い形（〜される）</strong>：<br>"
                 "Ⅰグループ（「す」で終わる動詞以外）では、日常会話で「〜せられる」より短い「<strong>〜される</strong>」がよく使われます。<br>"
                 "例：{待|ま}たせられる → <strong>{待|ま}たされる</strong>、{飲|の}ませられる → <strong>{飲|の}まされる</strong>、{歩|ある}かせられる → <strong>{歩|ある}かされる</strong>",
        notes_en="Expresses being made to do something against one's will ('I didn't want to, but had no choice because someone told me to'). "
                 "The person who made you do it is marked with に. "
                 "For Group 1 verbs (except those ending in す like 話す), the shorter contracted form 〜される is very common in speech: "
                 "書かせられる → 書かされる, 待たせられる → 待たされる, 手伝わせられる → 手伝わされる.",
        nuance_ja="使役受身には「本当はやりたくなかった」「大変だった」「困った」という被害・不満のニュアンスが強く含まれます。"
                  "そのため、自分が喜んでやったことや、感謝していることには使えません（×先生に合格させられた → ○先生のおかげで合格できた）。",
        nuance_en="Because the causative-passive strongly conveys reluctance or annoyance ('I was forced/made to...'), never use it when you are grateful or happy about the result.",
        trap_ja="①Ⅰグループの「<strong>す</strong>」で終わる動詞（話す・出す・直す）には短い形「〜される」がありません。×話される（ただの受身） → ○{話|はな}<strong>させられる</strong><br>"
                "②Ⅱグループ・Ⅲグループにも短い形はありません。×食べされる → ○{食|た}べ<strong>させられる</strong>、×しされる → ○<strong>させられる</strong><br>"
                "③Ⅰグループの「う」で終わる動詞は「<strong>わされる／わせられる</strong>」（{手伝|てつだ}わされる）。",
        trap_en="① Group 1 verbs ending in す (話す, 出す, 直す) CANNOT use the short form: use 話させられる (not ×話される). "
                "② Group 2 and Group 3 verbs have NO short form: 食べさせられる (never ×食べされる), させられる (never ×しされる). "
                "③ Group 1 verbs ending in う become わされる / わせられる (手伝わされる).",
        contrast=[
            dict(type="wrong", sentence="{母|はは}にピーマンを{食|た}べされました。",
                 reason_ja="「食べる」はⅡグループ動詞なので、「〜される」の短縮形は使えません。「食べさせられました」にします。",
                 reason_en="食べる is a Group 2 verb and has no contracted 〜される form; use 食べさせられました."),
            dict(type="correct", sentence="{母|はは}にピーマンを{食|た}べさせられました。",
                 reason_ja="Ⅱグループ動詞の使役受身は「る → させられる」だけです。",
                 reason_en="For Group 2 verbs, replace る with させられる: 食べさせられました."),
            dict(type="correct", sentence="{寒|さむ}い{外|そと}で30{分|ぷん}も{待|ま}たされました。",
                 reason_ja="Ⅰグループ「待つ」の使役受身「待たせられた」の短縮形「待たされた」は、とても自然によく使われます。",
                 reason_en="For Group 1 待つ, the short causative-passive 待たされました is very natural."),
        ],
        comparison=[
            dict(form="Aは Bに Vさせられる／Vされる", form_en="causative-passive (be made to do)", badge="不本意", badge_type="good",
                 nuance_ja="やりたくないのに指示されてしかたなくやらされたときに使います。",
                 nuance_en="Used when made to do something reluctantly.",
                 example="{部長|ぶちょう}に{土曜日|どようび}も{仕事|しごと}をさせられました。"),
            dict(form="Aは Bに Vさせる", form_en="causative (make someone do)", badge="指示する側", badge_type="both",
                 nuance_ja="上の立場のAが、下のBにやらせる側から述べる文です。",
                 nuance_en="States the action from the perspective of the person giving the order.",
                 example="{部長|ぶちょう}は{私|わたし}に{仕事|しごと}をさせました。"),
            dict(form="Vなければならない", form_en="must do (obligation)", badge="義務", badge_type="neutral",
                 nuance_ja="誰かに無理にやらせられたというより、規則や必要があって「〜する必要がある」と客観的に述べます。",
                 nuance_en="States an objective duty or necessity rather than feeling made to do it by someone.",
                 example="{土曜日|どようび}も{仕事|しごと}をしなければなりません。"),
        ],
    ),
    quiz=[
        dict(stem="{兄|あに}が{引|ひ}っ{越|こ}すとき、{私|わたし}は{一日|いちにち}{中|じゅう}、{重|おも}い{荷物|にもつ}を（　　　）とても{疲|つか}れました。",
             correct="{運|はこ}ばされて", distractors=["{運|はこ}ばせて", "{運|はこ}ばれて", "{運|はこ}びさせられて"],
             en="When my older brother moved house, I was made to carry heavy luggage all day long and got very tired.",
             notes_ja="私が兄に頼まれてしかたなく荷物を運んだ場面なので、Ⅰグループ「運ぶ（hakobu）」の使役受身（短縮形）「運ばされて」が正解です。「運ばれて」だと私が荷物のように運ばれる意味になってしまいます。",
             notes_en="Since 'I' was made to carry heavy luggage, use the causative-passive of 運ぶ → 運ばされて. (運ばれて would mean I myself was carried!)"),
        dict(stem="きのうのパーティーで、{先輩|せんぱい}に{みんな}の{前|まえ}で{歌|うた}を（　　　）、{本当|ほんとう}に{恥|はず}かしかったです。",
             correct="{歌|うた}わされて", distractors=["{歌|うた}わせて", "{歌|うた}われて", "{歌|うた}いされて"],
             en="At yesterday's party, I was made to sing a song in front of everyone by my senior, and I was really embarrassed.",
             notes_ja="先輩に言われて嫌々歌ったので使役受身にします。Ⅰグループ「歌う（utau）」の使役受身（短縮形）は「わ＋される」で「歌わされて」です。",
             notes_en="Made to sing reluctantly by a senior: Group 1 歌う takes わされる → 歌わされて."),
        dict(stem="レポートに{間違|まちが}いがたくさんあったので、{先生|せんせい}にもう{一度|いちど}（　　　）。",
             correct="{書|か}き{直|なお}させられました", distractors=["{書|か}き{直|なお}されました", "{書|か}き{直|なお}させました", "{書|か}き{直|なお}しさせられました"],
             en="Because there were many mistakes in my report, I was made to rewrite it by the teacher.",
             notes_ja="「書き直す」は「す」で終わるⅠグループ動詞なので、短縮形はなく「書き直させられました」になります。「書き直されました」は単なる受身です。",
             notes_en="書き直す ends in す, so it has no contracted form; use 書き直させられました."),
        dict(stem="{病院|びょういん}がすごく{混|こ}んでいて、{受付|うけつけ}で2{時間|じかん}も（　　　）。",
             correct="{待|ま}たされました", distractors=["{待|ま}たせました", "{待|ま}たれました", "{待|ま}ちさせられました"],
             en="The hospital was very crowded, and I was made to wait for two whole hours at the reception desk.",
             notes_ja="自分が意図せず長く待つことになった被害を表すので、Ⅰグループ「待つ（matsu）」の使役受身「待たされました」を使います。",
             notes_en="Being made to wait for a long time uses the causative-passive of 待つ → 待たされました."),
    ],
)

# ---------------------------------------------------------------- 38 お〜になる
GRAMMAR[38] = dict(
    name="お〜になる", reading="おになる",
    meaning_en="honorific expression (respectful action of superior)",
    similar="れる／られる（尊敬）、お〜ください、特別な尊敬語",
    details=dict(
        formula="<strong>お ＋ 動詞ます形 ＋ になる</strong>（和語・Ⅰ／Ⅱグループ）<br>"
                "　例：{読|よ}む → <strong>お{読|よ}みになる</strong>、{帰|かえ}る → <strong>お{帰|かえ}りになる</strong><br>"
                "<strong>ご ＋ サ変動詞の漢字2字 ＋ になる</strong><br>"
                "　例：{利用|りよう}する → <strong>ご{利用|りよう}になる</strong>、{出席|しゅっせき}する → <strong>ご{出席|しゅっせき}になる</strong>",
        notes_ja="目上の人（先生・社長・お客さんなど）の動作を高めて、敬意を表す<strong>尊敬語（そんけいご）</strong>の形です。<br>"
                 "例：{先生|せんせい}はもう<strong>お{帰|かえ}りになりました</strong>。<br>"
                 "例：{社長|しゃちょう}はこの{新聞|しんぶん}を<strong>お{読|よ}みになりますか</strong>。<br>"
                 "<strong>★使えない動詞に注意！</strong><br>"
                 "①ます形が<strong>1音（1文字）の動詞</strong>（見る・寝る・着る・来る・する・いる）には使えません。<br>"
                 "②<strong>特別な尊敬語がある動詞</strong>は、そちらを優先して使います：<br>"
                 "　・行く／来る／いる → <strong>いらっしゃる</strong><br>"
                 "　・食べる／飲む → <strong>{召|め}し{上|あ}がる</strong><br>"
                 "　・言う → <strong>おっしゃる</strong><br>"
                 "　・見る → <strong>ご{覧|らん}になる</strong><br>"
                 "　・する → <strong>なさる</strong><br>"
                 "　・知っている → <strong>ご{存|ぞん}じだ</strong>",
        notes_en="An honorific pattern (尊敬語) that elevates the actions of a superior (teacher, company president, customer) to show respect. "
                 "Attach お + Verb-masu stem + になる (or ご + 2-kanji Sino-Japanese noun + になる). "
                 "Important exceptions: (1) Cannot be used with single-mora stems (見る, 寝る, 着る, 来る, する, いる). "
                 "(2) Verbs that have special suppletive honorific forms use those instead: 行く/来る/いる → いらっしゃる, 食べる/飲む → 召し上がる, 言う → おっしゃる, 見る → ご覧になる, する → なさる, 知っている → ご存じだ.",
        nuance_ja="受身形と同じ形の尊敬語「〜（ら）れる」（読まれる・帰られる）よりも、「お〜になる」（お読みになる・お帰りになる）のほうが敬意が高く、丁寧な印象を与えます。"
                  "また、「お＋ます形＋ください」（お書きください・お待ちください）は、相手に丁寧に動作を勧めたり頼んだりする表現です。",
        nuance_en="お〜になる shows a higher degree of respect than the passive-form honorific 〜（ら）れる (お読みになる is more respectful than 読まれる). "
                  "Replacing になる with ください (お待ちください) creates a polite request.",
        trap_ja="①自分の動作には絶対に使えません（×私はお読みになります → ○{私|わたし}はお{読|よ}みします／{読|よ}みます）。<br>"
                "②ます形が1文字の動詞には使えません（×お見になる → ○<strong>ご{覧|らん}になる</strong>、×お着になる → ○お{召|め}しになる／{着|き}られる）。<br>"
                "③「食べる・飲む・行く・来る・言う」は特別な尊敬語（{召|め}し{上|あ}がる・いらっしゃる・おっしゃる）を使います。",
        trap_en="① Never use お〜になる for your own actions (that requires humble language). "
                "② Do not use it with 1-mora stems: ×お見になる → ○ご覧になる. "
                "③ Use special honorific verbs where they exist (召し上がる, いらっしゃる, おっしゃる).",
        contrast=[
            dict(type="wrong", sentence="{先生|せんせい}、もうその{映画|えいが}をお{見|み}になりましたか。",
                 reason_ja="「見る」はます形が「見（み）」の1文字なので「お見になる」とは言えません。",
                 reason_en="見る has a single-mora stem (み), so ×お見になる is ungrammatical."),
            dict(type="correct", sentence="{先生|せんせい}、もうその{映画|えいが}をご{覧|らん}になりましたか。",
                 reason_ja="「見る」の尊敬語には特別な形「ご覧になる」を使います。",
                 reason_en="Use the special honorific ご覧になる for 見る."),
            dict(type="correct", sentence="{社長|しゃちょう}はさっきお{帰|かえ}りになりました。",
                 reason_ja="目上の人（社長）の「帰る」には「お帰りになる」が自然に使えます。",
                 reason_en="お帰りになる is the standard respectful form of 帰る for a superior."),
        ],
        comparison=[
            dict(form="お ＋ Vます形 ＋ になる", form_en="standard honorific pattern", badge="尊敬語・高", badge_type="good",
                 nuance_ja="敬意が高く、先生・上司・お客様への丁寧な尊敬表現として広く使われます。",
                 nuance_en="High-respect honorific widely used for teachers, bosses, and customers.",
                 example="{部長|ぶちょう}はもうお{出|で}かけになりました。"),
            dict(form="特別な尊敬語（いらっしゃる等）", form_en="special suppletive honorifics", badge="最優先", badge_type="both",
                 nuance_ja="行く・来る・いる・食べる・言う・見る・する等は、決まった特別な形を使います。",
                 nuance_en="Common core verbs have dedicated honorific forms that must be used instead.",
                 example="どうぞ{温|あたた}かいうちにお{召|め}し{上|あ}がりください。"),
            dict(form="V（ら）れる（尊敬）", form_en="passive-form honorific", badge="尊敬語・軽", badge_type="neutral",
                 nuance_ja="「お〜になる」より少し軽めですが、どの動詞にも付けやすく会話やニュースでよく使われます。",
                 nuance_en="Slightly lighter in respect than お〜になる, but attaches to almost any verb.",
                 example="{先生|せんせい}は{何時|なんじ}ごろ{来|こ}られますか。"),
        ],
    ),
    quiz=[
        dict(stem="{課長|かちょう}は5{時|じ}ごろにはもう（　　　）ましたよ。",
             correct="お{帰|かえ}りになり", distractors=["お{帰|かえ}りし", "ご{帰|かえ}りになり", "お{帰|かえ}りなさり"],
             en="The section manager already went home around 5 o'clock.",
             notes_ja="目上の人（課長）の行動「帰る」を高める尊敬語なので、「お＋ます形＋になる」の「お帰りになりました」が正解です。「お帰りする」は謙譲語になってしまいます。",
             notes_en="Since the subject is the section manager (課長), use the honorific お帰りになりました. お帰りし is humble and cannot describe the manager's own going home."),
        dict(stem="お{客|きゃく}さま、どの{本|ほん}を（　　　）ますか。",
             correct="お{探|さが}しになり", distractors=["お{探|さが}しいたし", "ご{探|さが}しになり", "お{探|さが}しし"],
             en="Customer, which book are you looking for?",
             notes_ja="お客さまの動作「探す」に対する尊敬語なので、「お探しになりますか」を使います。「お探しいたします／お探しします」は店員自身の動作（謙譲語）です。",
             notes_en="Asking about the customer's action requires the honorific お探しになりますか. お探しいたし / お探しし are humble forms for the speaker's own action."),
        dict(stem="{先生|せんせい}、{先月|せんげつ}{出|で}た{新|あたら}しい{辞書|じしょ}をもう（　　　）ましたか。",
             correct="ご{覧|らん}になり", distractors=["お{見|み}になり", "お{見|み}し", "{拝見|はいけん}し"],
             en="Professor, have you already seen the new dictionary that came out last month?",
             notes_ja="目上の人（先生）が「見る」の尊敬語は「ご覧になる」です。「お見になる」は間違いで、「拝見する」は自分がするときに使う謙譲語です。",
             notes_en="The honorific for 見る is ご覧になる. ×お見になる does not exist, and 拝見する is humble (for the speaker's action)."),
        dict(stem="{部長|ぶちょう}は{今|いま}、{会議室|かいぎしつ}で{大切|たいせつ}なお{客|きゃく}さまと（　　　）ています。",
             correct="お{話|はな}しになっ", distractors=["お{話|はな}しし", "ご{話|はな}しになっ", "{申|もう}し{上|あ}げ"],
             en="The department manager is currently speaking with an important client in the conference room.",
             notes_ja="部長が話している様子を高める尊敬語は「お話しになっています」です。「お話しする」「申し上げる」は謙譲語なので部長の動作には使えません。",
             notes_en="To respectfully describe the department manager talking, use お話しになっています. お話しし and 申し上げ are humble forms."),
    ],
)

# ---------------------------------------------------------------- 39 お〜する／ご〜する
GRAMMAR[39] = dict(
    name="お〜する／ご〜する", reading="おする",
    meaning_en="humble expression (humble action toward superior)",
    similar="お〜になる、ていただく、特別な謙譲語",
    details=dict(
        formula="<strong>お ＋ 動詞ます形 ＋ する（／いたす）</strong>（和語・Ⅰ／Ⅱグループ）<br>"
                "　例：{持|も}つ → <strong>お{持|も}ちする</strong>、{送|おく}る → <strong>お{送|おく}りする</strong><br>"
                "<strong>ご ＋ サ変動詞の漢字2字 ＋ する（／いたす）</strong><br>"
                "　例：{案内|あんない}する → <strong>ご{案内|あんない}する</strong>、{説明|せつめい}する → <strong>ご{説明|せつめい}する</strong>",
        notes_ja="話し手（私・私たち）が目上の人（先生・上司・お客さんなど）に対して行う動作をへりくだって表す<strong>謙譲語（けんじょうご）</strong>です。<br>"
                 "例：{先生|せんせい}、お{荷物|にもつ}を<strong>お{持|も}ちしましょうか</strong>。<br>"
                 "例：こちらのお{席|せき}へ<strong>ご{案内|あんない}します</strong>。<br>"
                 "「する」を「<strong>いたす</strong>」に変えると、さらに丁寧になります（ご{連絡|れんらく}いたします）。<br>"
                 "<strong>★特別な謙譲語がある動詞</strong>は、そちらを使います：<br>"
                 "　・行く／来る → <strong>{伺|うかが}う・{参|まい}る</strong><br>"
                 "　・聞く／訪ねる → <strong>{伺|うかが}う</strong><br>"
                 "　・言う → <strong>{申|もう}す・{申|もう}し{上|あ}げる</strong><br>"
                 "　・見る → <strong>{拝見|はいけん}する</strong><br>"
                 "　・会う → <strong>お{目|め}にかかる</strong><br>"
                 "　・もらう／食べる／飲む → <strong>いただく</strong><br>"
                 "　・あげる → <strong>さしあげる</strong>",
        notes_en="A humble pattern (謙譲語) used when the speaker performs an action directed toward or for the benefit of a superior (teacher, boss, customer). "
                 "Use お + Verb-masu stem + する/いたす for native Japanese verbs, and ご + 2-kanji Sino-Japanese noun + する/いたす for suru-verbs. "
                 "When a verb has a special humble form, use that instead: 行く/来る → 伺う/参る, 聞く → 伺う, 言う → 申す/申し上げる, 見る → 拝見する, 会う → お目にかかる, もらう/食べる/飲む → いただく, あげる → さしあげる.",
        nuance_ja="「お〜する／ご〜する」は、自分の動作が<strong>相手（目上の人）に向かっているとき</strong>にだけ使えます。"
                  "例えば、先生のために荷物を持つなら「お持ちします」と言えますが、自分一人で家で本を読むときに「私は毎晩本をお読みします」とは言えません（相手に関係のない自分の動作には使いません）。",
        nuance_en="お〜する / ご〜する can ONLY be used when your action involves or benefits the respected person (e.g., carrying their bag, guiding them, contacting them). "
                  "You cannot use it for purely private actions that don't affect anyone else (×毎晩家で本をお読みします).",
        trap_ja="①目上の人の動作には絶対に使えません（×先生がお持ちします → ○{先生|せんせい}がお{持|も}ちになります）。<br>"
                "②和語には「<strong>お</strong>」、漢語（漢字2字＋する）には「<strong>ご</strong>」を付けます（○お{手伝|てつだ}いする、○ご{紹介|しょうかい}する）。"
                "※例外：電話・返事・約束などは漢語でも「<strong>お</strong>」（お{電話|でんわ}する・お{返事|へんじ}する・お{約束|やくそく}する）。<br>"
                "③「見る・聞く・行く・言う・会う」は特別な謙譲語（{拝見|はいけん}する・{伺|うかが}う・{申|もう}し{上|あ}げる・お{目|め}にかかる）を使います。",
        trap_en="① Never use お〜する for a superior's action (use お〜になる). "
                "② Native verbs take お (お手伝いする); 2-kanji Sino-Japanese nouns take ご (ご紹介する), except common daily words like お電話する, お返事する, お約束する. "
                "③ Use special humble verbs for 見る (拝見する), 聞く/行く (伺う), 言う (申し上げる), 会う (お目にかかる).",
        contrast=[
            dict(type="wrong", sentence="{先生|せんせい}、その{重|おも}いカバンをお{持|も}ちになりましょうか。",
                 reason_ja="カバンを持つのは「私」なので、尊敬語「お〜になる」は使えません。",
                 reason_en="Since 'I' am the one offering to carry the bag, the honorific お〜になる is wrong."),
            dict(type="correct", sentence="{先生|せんせい}、その{重|おも}いカバンをお{持|も}ちしましょうか。",
                 reason_ja="私が先生のために持つ動作なので、謙譲語「お持ちする」を使います。",
                 reason_en="Use the humble form お持ちしましょうか for your own action done for the teacher."),
            dict(type="correct", sentence="{詳|くわ}しい{予定|よてい}は、あとでご{連絡|れんらく}いたします。",
                 reason_ja="漢語「連絡する」には「ご〜する／いたす」を使って丁寧に伝えます。",
                 reason_en="With the Sino-Japanese verb 連絡する, use ご連絡いたします."),
        ],
        comparison=[
            dict(form="お ＋ Vます形 ＋ する／いたす", form_en="humble pattern (native verbs)", badge="謙譲語・和語", badge_type="good",
                 nuance_ja="自分が目上の人のために行う和語の動作（持つ・送る・手伝うなど）に使います。",
                 nuance_en="Used for native verbs when doing something for/toward a superior.",
                 example="{駅|えき}までお{送|おく}りします。"),
            dict(form="ご ＋ 漢字2字 ＋ する／いたす", form_en="humble pattern (Sino-Japanese verbs)", badge="謙譲語・漢語", badge_type="both",
                 nuance_ja="案内する・説明する・紹介する・連絡するなどの漢語動詞に使います。",
                 nuance_en="Used with 2-kanji suru-verbs (案内, 説明, 紹介, 連絡).",
                 example="{会議室|かいぎしつ}までご{案内|あんない}いたします。"),
            dict(form="特別な謙譲語（伺う・拝見する等）", form_en="special suppletive humble verbs", badge="最優先", badge_type="neutral",
                 nuance_ja="行く・聞く（伺う）、見る（拝見する）、会う（お目にかかる）などは特別な形を使います。",
                 nuance_en="Core verbs use dedicated humble vocabulary instead of お〜する.",
                 example="{先生|せんせい}のメールを{拝見|はいけん}しました。"),
        ],
    ),
    quiz=[
        dict(stem="{先生|せんせい}、そのお{荷物|にもつ}は{重|おも}そうですから、{私|わたし}が（　　　）ましょうか。",
             correct="お{持|も}ちし", distractors=["お{持|も}ちになり", "ご{持|も}ちし", "{持|も}たれ"],
             en="Professor, that luggage looks heavy, so shall I carry it for you?",
             notes_ja="主語が「私が」で、先生のために荷物を持つ動作なので、謙譲語「お持ちしましょうか」が正解です。「お持ちになり」「持たれ」は尊敬語です。",
             notes_en="Since 'I' (私が) am carrying the luggage for the professor, use the humble form お持ちしましょうか."),
        dict(stem="お{客|きゃく}さま、お{部屋|へや}の{準備|じゅんび}ができましたので、{私|わたし}が（　　　）ます。",
             correct="ご{案内|あんない}いたし", distractors=["ご{案内|あんない}になり", "お{案内|あんない}いたし", "ご{案内|あんない}され"],
             en="Customer, your room is ready, so I will show you the way.",
             notes_ja="「私が」お客さまを「案内する」ので、漢語の謙譲語「ご＋案内＋いたします」を使います。「お案内」とは言いません。",
             notes_en="'I' am guiding the customer, so use the humble Sino-Japanese form ご案内いたします."),
        dict(stem="{部長|ぶちょう}、さきほど{送|おく}ってくださった{資料|しりょう}を（　　　）ました。",
             correct="{拝見|はいけん}し", distractors=["ご{覧|らん}になり", "お{見|み}し", "お{目|め}にかかり"],
             en="Manager, I have looked at the documents you sent me earlier.",
             notes_ja="私が部長の資料を「見た」ので、「見る」の特別な謙譲語「拝見しました」が正解です。「ご覧になり」は尊敬語、「お目にかかり」は「会う」の謙譲語です。",
             notes_en="Since 'I' looked at the manager's documents, use 拝見しました (humble for 見る). ご覧になる is honorific, and お目にかかる means 'meet'."),
        dict(stem="{明日|あした}の{午後|ごご}、もう{一度|いちど}こちらから（　　　）ますので、よろしくお{願|ねが}いいたします。",
             correct="お{電話|でんわ}し", distractors=["お{電話|でんわ}になり", "ご{電話|でんわ}になり", "{電話|でんわ}なさり"],
             en="Tomorrow afternoon, I will call you again from here, so thank you in advance.",
             notes_ja="自分から相手に電話をかける謙譲語です。「電話する」は例外的に「ご」ではなく「お」を付けて「お電話します」と言います。他の選択肢はすべて尊敬語です。",
             notes_en="Calling the other person takes the humble form お電話します (電話 exceptionally takes お rather than ご). All other options are honorific."),
    ],
)

# ---------------------------------------------------------------- 40 てあげる
GRAMMAR[40] = dict(
    name="てあげる", reading="てあげる",
    meaning_en="do something for someone",
    similar="てもらう、てくれる、てさしあげる",
    details=dict(
        formula="<strong>動詞て形 ＋ あげる</strong>（同等・友人・家族に）<br>"
                "<strong>動詞て形 ＋ さしあげる</strong>（目上の人に・謙譲）<br>"
                "<strong>動詞て形 ＋ やる</strong>（弟・妹・子ども・ペット・植物に）",
        notes_ja="話し手（私）や主語が、相手のために親切で何かをしてあげることを表します。相手には助詞「<strong>に</strong>」を付けます。<br>"
                 "例：{私|わたし}は{友|とも}だち<strong>に</strong>{本|ほん}を<strong>{貸|か}してあげました</strong>。<br>"
                 "例：{母|はは}の{誕生日|たんじょうび}に、{晩|ばん}ごはんを<strong>{作|つく}ってあげました</strong>。<br>"
                 "相手が動物・植物・小さい弟や妹のときは「<strong>〜てやる</strong>」も使われます。<br>"
                 "例：{毎朝|まいあさ}、{庭|にわ}の{花|はな}に{水|みず}を<strong>やって</strong>（／<strong>あげて</strong>）います。",
        notes_en="Expresses doing an action for someone's benefit. The recipient of the favor is marked with に. "
                 "Use 〜てあげる for equals, friends, or family; 〜てさしあげる for superiors (though see the nuance trap below); and 〜てやる for pets, plants, or younger siblings.",
        nuance_ja="<strong>★一番大切な注意点</strong>：<br>"
                  "「〜てあげる」は「あなたのために親切にしてあげるよ」という恩着せがましい（上から目線の）響きが出やすい表現です。"
                  "そのため、目上の人（先生・上司・お客さん）に直接「私が手伝ってあげます」「教えてあげましょうか」と言うと大変失礼になります！<br>"
                  "目上の人に申し出るときは「<strong>お{手伝|てつだ}いしましょうか</strong>」「<strong>お{持|も}ちしましょうか</strong>」を使います。",
        nuance_en="Crucial etiquette point: Telling someone directly (especially a superior) 「〜てあげます」 or 「〜てあげましょうか」 sounds patronizing, as if you are bragging about doing them a favor. "
                  "When offering help to a superior or acquaintance, use 「お＋ます形＋しましょうか」 (お手伝いしましょうか) or 「〜ましょうか」 instead!",
        trap_ja="①「私」のために誰かがしてくれたときには使えません（×友達が私に教えてあげた → ○{友|とも}だちが{私|わたし}に{教|おし}えて<strong>くれた</strong>）。<br>"
                "②目上の人に直接「〜てあげましょうか」とは言いません → 「<strong>お〜しましょうか／〜ましょうか</strong>」を使います。<br>"
                "③相手を表す助詞は「<strong>に</strong>」です（{祖母|そぼ}<strong>に</strong>{荷物|にもつ}を{持|も}ってあげた）。",
        trap_en="① Never use てあげる when someone does something for YOU (use てくれる: 友達が私に教えてくれた). "
                "② Never offer help to a superior with てあげましょうか; use お〜しましょうか or 〜ましょうか. "
                "③ Mark the beneficiary with に.",
        contrast=[
            dict(type="wrong", sentence="（{先生|せんせい}に）{先生|せんせい}、{私|わたし}がコピーしてあげましょうか。",
                 reason_ja="目上の人に直接「〜てあげましょうか」と言うと、恩着せがましくて失礼になります。",
                 reason_en="Saying 〜てあげましょうか directly to a superior sounds patronizing and rude."),
            dict(type="correct", sentence="（{先生|せんせい}に）{先生|せんせい}、{私|わたし}がコピーしましょうか。",
                 reason_ja="目上の人に手伝いを申し出るときは「〜ましょうか」「お〜しましょうか」を使います。",
                 reason_en="Offer help to a superior with 〜ましょうか or お〜しましょうか."),
            dict(type="correct", sentence="{私|わたし}は{妹|いもうと}に{数学|すうがく}の{宿題|しゅくだい}を{教|おし}えてあげました。",
                 reason_ja="家族や友達のためにしてあげたことを客観的に話すときは「〜てあげました」が自然です。",
                 reason_en="When recounting what you did for a sibling or friend, 〜てあげました is natural."),
        ],
        comparison=[
            dict(form="Aは Bに Vてあげる", form_en="do a favor for B", badge="自分→相手", badge_type="good",
                 nuance_ja="私（または第三者A）がBのために何かをしてあげるときに使います（Bに「私」は来ません）。",
                 nuance_en="I (or A) do something for B's benefit (B cannot be 'me').",
                 example="{友|とも}だちに{空港|くうこう}の{道|みち}を{調|しら}べてあげました。"),
            dict(form="お ＋ Vます形 ＋ しましょうか", form_en="polite offer of help", badge="目上への申し出", badge_type="both",
                 nuance_ja="目上の人や相手に直接「やりましょうか」と親切を申し出るときの丁寧で自然な表現です。",
                 nuance_en="The natural, polite way to offer help directly to a superior or listener.",
                 example="タクシーをお{呼|よ}びしましょうか。"),
            dict(form="Aが（私に）Vてくれる", form_en="someone does a favor for me", badge="相手→自分", badge_type="neutral",
                 nuance_ja="相手Aが「私（や私の家族）」のために何かをしてくれたときに使います。",
                 nuance_en="Used when someone does a favor for me (or my in-group).",
                 example="{友|とも}だちが{私|わたし}に{傘|かさ}を{貸|か}してくれました。"),
        ],
    ),
    quiz=[
        dict(stem="{祖母|そぼ}が{スマホ|すまほ}の{使|つか}い{方|かた}がわからないと{言|い}っていたので、{私|わたし}が（　　　）。",
             correct="{教|おし}えてあげました", distractors=["{教|おし}えてくれました", "{教|おし}えてもらいました", "{教|おし}えられました"],
             en="My grandmother said she didn't know how to use her smartphone, so I taught her.",
             notes_ja="主語が「私が」で、祖母のために教えたので「て形＋あげました（教えてあげました）」が正解です。「てくれました」「てもらいました」は自分が教えてもらう側になってしまいます。",
             notes_en="Since 'I' (私が) taught my grandmother for her benefit, use 教えてあげました."),
        dict(stem="{風邪|かぜ}をひいて{寝|ね}ているルームメイトに、{温|あたた}かいスープを（　　　）。",
             correct="{作|つく}ってあげました", distractors=["{作|つく}ってくれました", "{作|つく}ってもらいました", "{作|つく}らされました"],
             en="I made warm soup for my roommate who was in bed with a cold.",
             notes_ja="（私が）ルームメイトのためにスープを作ったので「作ってあげました」を使います。",
             notes_en="'I' made soup for my sick roommate's benefit: 作ってあげました."),
        dict(stem="{毎朝|まいあさ}、{学校|がっこう}へ{行|い}く{前|まえ}に{犬|いぬ}に{散歩|さんぽ}をさせたり、えさを（　　　）しています。",
             correct="やったり", distractors=["くれたり", "もらったり", "いただいたり"],
             en="Every morning before going to school, I walk the dog and feed it.",
             notes_ja="ペットや植物に水・えさなどを与えるときは「あげる」または「やる（やったり）」を使います。「くれる・もらう・いただく」は自分が受け取る側なので使えません。",
             notes_en="When giving food or water to pets or plants, use やる (やったり) or あげる, not receiving verbs."),
        dict(stem="{小|ちい}さい{妹|いもうと}が{靴|くつ}を{履|は}けなかったので、{兄|あに}が（　　　）いました。",
             correct="{履|は}かせてあげて", distractors=["{履|は}かせてくれて", "{履|は}かせてもらって", "{履|は}かされて"],
             en="Because our little sister couldn't put on her shoes, my older brother was putting them on for her.",
             notes_ja="兄が妹のために靴を履かせていたので「履かせてあげていました」が正解です。",
             notes_en="The older brother was helping the little sister put on her shoes for her benefit: 履かせてあげていました."),
    ],
)

# ---------------------------------------------------------------- 41 てもらう
GRAMMAR[41] = dict(
    name="てもらう", reading="てもらう",
    meaning_en="have someone do something for oneself (receive favor)",
    similar="てくれる、てあげる、ていただく",
    details=dict(
        formula="<strong>動詞て形 ＋ もらう</strong>（同等・友人・家族から）<br>"
                "<strong>動詞て形 ＋ いただく</strong>（目上の人から・謙譲）<br>"
                "文型：<strong>A（私）は B（相手）に 〜てもらう／〜ていただく</strong>",
        notes_ja="話し手（私）や主語Aが、相手Bに頼んだりして、自分のために何かをしてもらい、ありがたいと感じていることを表します。<br>"
                 "動作をしてくれる相手Bには助詞「<strong>に</strong>」（または「から」）を付けます。<br>"
                 "例：{私|わたし}は{友|とも}だち<strong>に</strong>パソコンの{直|なお}し{方|かた}を<strong>{教|おし}えてもらいました</strong>。<br>"
                 "相手が目上の人（先生・上司など）のときは、謙譲語の「<strong>〜ていただく</strong>」を使います。<br>"
                 "例：{私|わたし}は{先生|せんせい}<strong>に</strong>{推薦状|すいせんじょう}を<strong>{書|か}いていただきました</strong>。<br>"
                 "また、「<strong>〜てもらえませんか／〜ていただけませんか</strong>」は、とても丁寧な依頼表現になります。",
        notes_en="Expresses receiving the benefit of someone doing an action for you (often because you asked them to), with a feeling of gratitude. "
                 "The person who performs the action is marked by に, while the receiver ('I') is the topic (は). "
                 "When the doer is a superior, use the humble equivalent 〜ていただく. "
                 "In the negative question form (〜てもらえませんか / 〜ていただけませんか), it becomes a polite request ('Could I have you do ~?').",
        nuance_ja="「友達に手伝ってもらった」と「友達が手伝ってくれた」は同じ事実を表しますが、視点が違います。"
                  "「〜てもらった」は「<strong>私が</strong>（頼んで）助けてもらった」と受け取る側（私）が主語になり、「〜てくれた」は「<strong>友達が</strong>（自分から親切に）助けてくれた」と動作主（友達）が主語になります。",
        nuance_en="Both 友達に手伝ってもらった and 友達が手伝ってくれた describe the same event, but from different viewpoints: "
                  "てもらう makes 'I' the topic (often implying I asked for help), whereas てくれる makes the friend the subject (highlighting their voluntary kindness).",
        trap_ja="①「〜てもらう」では、動作をする相手に必ず「<strong>に</strong>」を付けます（×友達が手伝ってもらった → ○{友|とも}だち<strong>に</strong>{手伝|てつだ}ってもらった）。<br>"
                "②目上の人にしてもらったときは「〜てもらう」より「<strong>〜ていただく</strong>」が丁寧です。<br>"
                "③感謝の場面で受身「先生に直された」を使うと不満そうに聞こえるので、「{先生|せんせい}に{直|なお}していただいた／もらった」を使います。",
        trap_en="① With てもらう, the person who does the action takes に, NOT が (○友達に手伝ってもらった, ×友達が手伝ってもらった). "
                "② For superiors, upgrade てもらう to ていただく. "
                "③ Use てもらう/ていただく instead of the passive voice when you are grateful for someone's action.",
        contrast=[
            dict(type="wrong", sentence="{私|わたし}は{友|とも}だちが{空港|くうこう}まで{送|おく}ってもらいました。",
                 reason_ja="「〜てもらう」の文では、動作をする人（友だち）の助詞は「が」ではなく「に」です。",
                 reason_en="With てもらう, the person who performs the action must be marked with に, not が."),
            dict(type="correct", sentence="{私|わたし}は{友|とも}だちに{空港|くうこう}まで{送|おく}ってもらいました。",
                 reason_ja="「（私は）友だちに〜てもらいました」で正しい助詞の組み合わせになります。",
                 reason_en="（私は）友だちに送ってもらいました uses the correct particle に."),
            dict(type="correct", sentence="{先生|せんせい}に{作文|さくぶん}の{間違|まちが}いを{直|なお}していただきました。",
                 reason_ja="目上の人（先生）にしてもらったときは、謙譲語「〜ていただく」を使います。",
                 reason_en="When a superior (the teacher) does a favor for you, use 〜ていただく."),
        ],
        comparison=[
            dict(form="（私は）Bに Vてもらう", form_en="have B do ~ for me", badge="自分が主語", badge_type="good",
                 nuance_ja="「私」を主語（は）にして、B（に）から恩恵を受け取ったことを表します。",
                 nuance_en="'I' am the topic (は), receiving the favor from B (に).",
                 example="{兄|あに}に{自転車|じてんしゃ}を{直|なお}してもらいました。"),
            dict(form="（私は）Bに Vていただく", form_en="humble form of てもらう", badge="目上・謙譲", badge_type="both",
                 nuance_ja="相手Bが目上の人（先生・上司・先輩など）のときに使う丁寧な表現です。",
                 nuance_en="Polite humble version used when B is a superior.",
                 example="{部長|ぶちょう}にいいアドバイスをしていただきました。"),
            dict(form="Bが（私に）Vてくれる", form_en="B kindly does ~ for me", badge="相手が主語", badge_type="neutral",
                 nuance_ja="相手Bを主語（が）にして、Bが自分から親切にしてくれたことを表します。",
                 nuance_en="B is the subject (が), highlighting B's voluntary kindness toward me.",
                 example="{兄|あに}が{自転車|じてんしゃ}を{直|なお}してくれました。"),
        ],
    ),
    quiz=[
        dict(stem="{漢字|かんじ}の{読|よ}み{方|かた}がわからなかったので、{隣|となり}の{席|せき}の{鈴木|すずき}さんに（　　　）。",
             correct="{教|おし}えてもらいました", distractors=["{教|おし}えてくれました", "{教|おし}えてあげました", "{教|おし}えさせました"],
             en="Because I didn't know how to read the kanji, I had Ms. Suzuki in the next seat tell me.",
             notes_ja="「鈴木さんに」と助詞「に」があるので、私が鈴木さんから恩恵を受けた「教えてもらいました」が正解です。「教えてくれました」なら「鈴木さんが」になります。",
             notes_en="Because Ms. Suzuki is marked with に (鈴木さんに), use 教えてもらいました. (教えてくれました would require 鈴木さんが.)"),
        dict(stem="{日本|にほん}へ{留学|りゅうがく}するとき、{大学|だいがく}の{先生|せんせい}に{推薦状|すいせんじょう}を（　　　）。",
             correct="{書|か}いていただきました", distractors=["{書|か}いてくださいました", "{書|か}いてさしあげました", "{書|か}かれました"],
             en="When I went to study abroad in Japan, I had my university professor write a letter of recommendation for me.",
             notes_ja="「大学の先生に」とあり、私が先生に書いてもらったので、「〜てもらう」の謙譲語「書いていただきました」が正解です（「くださいました」は「先生が」のとき）。",
             notes_en="With 大学の先生に, use the humble form of てもらう → 書いていただきました. (書いてくださいました requires 先生が.)"),
        dict(stem="すみません、シャッターを{押|お}すので、ここで{写真|しゃしん}を{一枚|いちまい}（　　　）ませんか。",
             correct="{撮|と}っていただけ", distractors=["{撮|と}ってくださり", "{撮|と}ってさしあげ", "{撮|と}りになれ"],
             en="Excuse me, could I have you take one photo here?",
             notes_ja="相手に丁寧に頼む表現「〜ていただけませんか（〜てもらえませんか）」が正解です。",
             notes_en="〜ていただけませんか is the standard polite way to ask someone for a favor ('Could I have you take...?')."),
        dict(stem="{引|ひ}っ{越|こ}しの{日|ひ}は、{友|とも}だち3{人|にん}に{来|き}て（　　　）ので、{早|はや}く{片付|かたづ}きました。",
             correct="もらった", distractors=["くれた", "あげた", "やった"],
             en="On moving day, I had three friends come over to help, so things got tidied up quickly.",
             notes_ja="「友だち3人に」と助詞「に」が使われているので、「来てもらった」が正解です。",
             notes_en="Since the friends are marked with に (友だち3人に), use もらった (来てもらった)."),
    ],
)

# ---------------------------------------------------------------- 42 てくれる
GRAMMAR[42] = dict(
    name="てくれる", reading="てくれる",
    meaning_en="someone kindly does something for me/us",
    similar="てもらう、てあげる、てくださる",
    details=dict(
        formula="<strong>動詞て形 ＋ くれる</strong>（同等・友人・家族が私に）<br>"
                "<strong>動詞て形 ＋ くださる</strong>（目上の人が私に・尊敬）<br>"
                "文型：<strong>A（相手）が（私／うちの家族に）〜てくれる／〜てくださる</strong>",
        notes_ja="誰か（A）が、話し手（私）や私の家族・仲間のために、親切で何かをしてくれることを表します。<br>"
                 "動作をする人Aが主語になるので、助詞は「<strong>が</strong>」（または「は」）を使います。「私に」は省略されることが多いです。<br>"
                 "例：{雨|あめ}が{降|ふ}ってきたとき、{田中|たなか}さん<strong>が</strong>{傘|かさ}を<strong>{貸|か}してくれました</strong>。<br>"
                 "例：{母|はは}<strong>が</strong>お{弁当|べんとう}を<strong>{作|つく}ってくれました</strong>。<br>"
                 "相手が目上の人（先生・上司など）のときは、尊敬語の「<strong>〜てくださる</strong>」を使います。<br>"
                 "例：{先生|せんせい}<strong>が</strong>{丁寧|ていねい}に<strong>{教|おし}えてくださいました</strong>。",
        notes_en="Expresses that someone (the subject, marked with が or は) kindly does something for the speaker ('me') or the speaker's in-group (family, team). "
                 "私に is usually omitted because てくれる already implies the benefit comes toward the speaker. "
                 "When the subject is a superior, use the honorific equivalent 〜てくださる.",
        nuance_ja="「〜てくれる」は、頼んでいなくても相手が自分から進んで親切にしてくれた場面にぴったりです。"
                  "また、自分の家族（母・兄など）に対しても「母が作ってくれた」と感謝を込めて普通に使います。"
                  "疑問文「〜てくれませんか／〜てくださいませんか」にすると、相手への依頼になります。",
        nuance_en="〜てくれる highlights the doer's goodwill and initiative—even when you didn't ask them first. "
                  "It is also naturally used for your own family members when they do something nice for you (母が作ってくれた). "
                  "In questions (〜てくれませんか / 〜てくださいませんか), it makes a polite request.",
        trap_ja="①動作をする相手Aには助詞「<strong>が</strong>（は）」を付けます。「に」は使いません（×友達に教えてくれた → ○{友|とも}だち<strong>が</strong>{教|おし}えてくれた）。<br>"
                "②自分が相手にしてあげたことには使えません（×私が友達に教えてくれた → ○{私|わたし}が{友|とも}だちに{教|おし}えて<strong>あげた</strong>）。<br>"
                "③「くださる」のます形は「くださり」ではなく「<strong>ください（ます／ました）</strong>」です。",
        trap_en="① Mark the doer with が (or は), NOT に (○友達が教えてくれた, ×友達に教えてくれた). "
                "② Never use てくれる when 'I' am the doer (use てあげる). "
                "③ Note the irregular polite conjugation of くださる: くださいます / くださいました (not ×くださります).",
        contrast=[
            dict(type="wrong", sentence="{友|とも}だちに{駅|えき}まで{迎|むか}えに{来|き}てくれました。",
                 reason_ja="「〜てくれる」の主語は動作をする人（友だち）なので、助詞は「に」ではなく「が」にします。",
                 reason_en="With てくれる, the person doing the favor is the subject and takes が, not に."),
            dict(type="correct", sentence="{友|とも}だちが{駅|えき}まで{迎|むか}えに{来|き}てくれました。",
                 reason_ja="「友だちが（私を）迎えに来てくれた」で正しい文になります。",
                 reason_en="友だちが迎えに来てくれました correctly marks the friend as the subject with が."),
            dict(type="correct", sentence="{課長|かちょう}がおいしいコーヒーを{入|い}れてくださいました。",
                 reason_ja="目上の人（課長）がしてくれたときには、尊敬語「〜てくださる（くださいました）」を使います。",
                 reason_en="When a superior does a favor for you, use 〜てくださる (くださいました)."),
        ],
        comparison=[
            dict(form="Aが（私に）Vてくれる", form_en="A does ~ for me (equal/family)", badge="相手が主語", badge_type="good",
                 nuance_ja="友達や家族Aが、私のために親切に何かをしてくれたことを表します。",
                 nuance_en="A friend or family member A kindly does something for me.",
                 example="{姉|あね}がマフラーを{編|あ}んでくれました。"),
            dict(form="Aが（私に）Vてくださる", form_en="honorific form of てくれる", badge="目上が主語", badge_type="both",
                 nuance_ja="目上の人Aが、私のために親切にしてくださったときに使います。",
                 nuance_en="Honorific version used when a superior A kindly does something for me.",
                 example="{先生|せんせい}が{本|ほん}を{貸|か}してくださいました。"),
            dict(form="（私は）Aに Vてもらう", form_en="I have A do ~ for me", badge="自分が主語", badge_type="neutral",
                 nuance_ja="「私」を主語にして、A（に）に頼んでやってもらったことを表します。",
                 nuance_en="Makes 'I' the topic and marks the doer A with に.",
                 example="{姉|あね}にマフラーを{編|あ}んでもらいました。"),
        ],
    ),
    quiz=[
        dict(stem="{私|わたし}が{重|おも}いスーツケースを{持|も}っていたら、{知|し}らない{人|ひと}が{階段|かいだん}の{上|うえ}まで（　　　）。",
             correct="{運|はこ}んでくれました", distractors=["{運|はこ}んでもらいました", "{運|はこ}んであげました", "{運|はこ}ばれました"],
             en="When I was carrying a heavy suitcase, a stranger kindly carried it to the top of the stairs for me.",
             notes_ja="主語が「知らない人が」となっており、私のために運んでくれたので「運んでくれました」が正解です。「もらいました」なら「知らない人に」になります。",
             notes_en="Since the stranger is marked with が (知らない人が) and helped 'me', use 運んでくれました."),
        dict(stem="{私|わたし}の{誕生日|たんじょうび}に、{母|はは}が{私|わたし}の{大好|だいす}きなケーキを（　　　）。",
             correct="{焼|や}いてくれました", distractors=["{焼|や}いてもらいました", "{焼|や}いてあげました", "{焼|や}いてやりました"],
             en="On my birthday, my mother baked my favorite cake for me.",
             notes_ja="「母が」「私の誕生日に（私のために）」焼いたので、「焼いてくれました」を使います。",
             notes_en="My mother (母が) baked it for me on my birthday: 焼いてくれました."),
        dict(stem="{仕事|しごと}でわからないことがあったとき、{部長|ぶちょう}が{大変|たいへん}{丁寧|ていねい}に（　　　）。",
             correct="{説明|せつめい}してくださいました", distractors=["{説明|せつめい}していただきました", "{説明|せつめい}してさしあげました", "{説明|せつめい}してくださいりました"],
             en="When there was something I didn't understand at work, the department manager explained it to me very politely.",
             notes_ja="目上の人「部長が」主語なので、「てくれる」の尊敬語「説明してくださいました」が正解です（「くださる」のます形は「くださいます」）。",
             notes_en="The superior is the subject (部長が), requiring the honorific てくださる → 説明してくださいました."),
        dict(stem="A：すてきな腕時計ですね。<br>B：ありがとうございます。{大学|だいがく}に{入|はい}ったとき、{祖父|そふ}が（　　　）んです。",
             correct="{買|か}ってくれた", distractors=["{買|か}ってもらった", "{買|か}ってあげた", "{買|か}わされた"],
             en="A: That's a lovely wristwatch. B: Thank you. My grandfather bought it for me when I entered university.",
             notes_ja="「祖父が」主語なので、私に買ってくれたことを表す「買ってくれた（んです）」が正解です。",
             notes_en="With 祖父が as the subject, use 買ってくれたんです to mean 'my grandfather bought it for me'."),
    ],
)

# ---------------------------------------------------------------- 43 たら
GRAMMAR[43] = dict(
    name="たら", reading="たら",
    meaning_en="if / when ~ (conditional & temporal discovery)",
    similar="ば、と、なら",
    details=dict(
        formula="<strong>動詞た形 ＋ ら</strong>（{行|い}ったら、{食|た}べたら、来たら）<br>"
                "<strong>イ形容詞（〜い → 〜かったら）</strong>（{安|やす}かったら、よかったら）<br>"
                "<strong>ナ形容詞・名詞 ＋ だったら</strong>（{暇|ひま}だったら、{雨|あめ}だったら）<br>"
                "<strong>否定（〜ない → 〜なかったら）</strong>（わからなかったら）",
        notes_ja="すべての普通形過去（た形・かった・だった・なかった）に「ら」を付けるだけで作れる、一番使いやすい条件表現です。大きく3つの使い{方|かた}があります。<br>"
                 "①<strong>仮定条件（もし〜たら）</strong>：「もしそうなったら、〜する／〜しよう／〜てください」<br>"
                 "例：もし{明日|あした}<strong>{雨|あめ}が{降|ふ}ったら</strong>、{試合|しあい}は{中止|ちゅうし}です。<br>"
                 "②<strong>確定条件（〜したあとで／〜したとき）</strong>：未来に必ず起きることが終わった時点で次の動作をする。<br>"
                 "例：{駅|えき}に<strong>{着|つ}いたら</strong>、すぐに{電話|でんわ}してください。<br>"
                 "③<strong>発見・偶然の結果（〜してみたら、…だった）</strong>：文末は過去形になります。<br>"
                 "例：{窓|まど}を<strong>{開|あ}けたら</strong>、{雪|ゆき}が{降|ふ}っていました。",
        notes_en="Formed simply by adding ら to any plain past form (た, かった, だった, なかった). It is the most versatile conditional in Japanese, with three main uses: "
                 "(1) Hypothetical condition ('if ~'): もし安かったら買います; "
                 "(2) Temporal sequence ('when / once ~ has happened'): 駅に着いたら電話してください; "
                 "(3) Discovery / unexpected past result ('when I did ~, I found that...'): 窓を開けたら雪が降っていた.",
        nuance_ja="「ば」や「と」と違い、「たら」の後ろには<strong>依頼（〜てください）・誘い（〜ましょう）・意志（〜つもりだ）・希望（〜たい）</strong>など、どんな文でも自由に置くことができます。"
                  "迷ったときに会話で一番安全に使えるのが「たら」です。",
        nuance_en="Unlike ば and と (which restrict commands, requests, and volition in the main clause), たら allows ANY sentence ending—requests (〜てください), invitations (〜ましょう), desires (〜たい), or past discoveries.",
        trap_ja="①「Aたら、B」は、必ず<strong>Aが起きたあとにBが起きる</strong>順番です。「これから日本へ行くなら」のようにAがBより後のことには「なら」を使います。<br>"
                "②イ形容詞の接続は「〜かったら」です（×安いだったら → ○<strong>{安|やす}かったら</strong>）。<br>"
                "③後ろが「〜てください」「〜ましょう」のときは、「と」ではなく「<strong>たら</strong>」を使います（○{着|つ}いたら{連絡|れんらく}してください、×着くと連絡してください）。",
        trap_en="① In 'A たら B', A must happen BEFORE B. "
                "② For i-adjectives, use 〜かったら (○安かったら, ×安いだったら). "
                "③ When the main clause is a request (〜てください) or invitation (〜ましょう), use たら, never と.",
        contrast=[
            dict(type="wrong", sentence="{家|いえ}に{帰|かえ}ると、すぐにお{風呂|ふろ}に{入|はい}ってください。",
                 reason_ja="「と」の後ろには依頼「〜てください」を置くことができません。",
                 reason_en="と cannot be followed by a request like 〜てください."),
            dict(type="correct", sentence="{家|いえ}に{帰|かえ}ったら、すぐにお{風呂|ふろ}に{入|はい}ってください。",
                 reason_ja="「〜したあとで…してください」という依頼には「たら」を使います。",
                 reason_en="たら freely allows requests (〜てください) once the first action is completed."),
            dict(type="correct", sentence="けさカーテンを{開|あ}けたら、{外|そと}が{真|ま}っ{白|しろ}でした。",
                 reason_ja="「〜してみたら、…だった」という過去の発見を表すのも「たら」の大切な用法です。",
                 reason_en="たら + past tense naturally expresses a discovery upon doing something."),
        ],
        comparison=[
            dict(form="〜たら", form_en="if / when / upon doing", badge="万能・会話", badge_type="good",
                 nuance_ja="仮定にも「〜したあとで」にも過去の発見にも使え、文末に依頼・意志も置けます。",
                 nuance_en="Works for 'if', 'when/after', and past discovery; allows requests and volition.",
                 example="{時間|じかん}があったら、{手伝|てつだ}ってください。"),
            dict(form="〜と", form_en="whenever / natural consequence", badge="必然・習慣", badge_type="both",
                 nuance_ja="自然現象・機械の操作・道案内など、必ずそうなることに使います（依頼は不可）。",
                 nuance_en="Natural laws, machine operation, directions; no requests allowed.",
                 example="このボタンを{押|お}すと、お{釣|つ}りが{出|で}ます。"),
            dict(form="〜なら", form_en="if it's the case that ~", badge="話題・助言", badge_type="neutral",
                 nuance_ja="相手が言ったことを受けて「それなら〜がいいよ」とアドバイスするときに使います。",
                 nuance_en="Picks up on what the listener said to offer advice or suggestions.",
                 example="{京都|きょうと}へ{行|い}くなら、{秋|あき}がいいですよ。"),
        ],
    ),
    quiz=[
        dict(stem="{空港|くうこう}に（　　　）、すぐにお{母|かあ}さんにメッセージを送ってくださいね。",
             correct="{着|つ}いたら", distractors=["{着|つ}くと", "{着|つ}くなら", "{着|つ}けば"],
             en="When you arrive at the airport, please send a message to your mother right away.",
             notes_ja="未来のある動作（空港に着く）が完了したあとで「〜してください」と依頼する文なので、「着いたら」が唯一自然です。「と」「ば」には依頼が続きません。",
             notes_en="For 'once you arrive, please do ~', only 着いたら works. と and ば cannot take requests here, and なら means 'before going/if you plan to arrive'."),
        dict(stem="もしサイズが（　　　）、{別|べつ}のものと{交換|こうかん}できますか。",
             correct="{合|あ}わなかったら", distractors=["{合|あ}わないと", "{合|あ}わないかったら", "{合|あ}わなければで"],
             en="If the size doesn't fit, can I exchange it for another one?",
             notes_ja="「もし〜ない場合」の仮定条件で、後ろで質問・許可を求めているので「ない→なかったら」の「合わなかったら」が正解です。",
             notes_en="In a hypothetical 'if it doesn't fit' followed by a question about permission, use the negative past + ら: 合わなかったら."),
        dict(stem="きのう、{急|いそ}いで{駅|えき}へ（　　　）、ちょうど{電車|でんしゃ}が{出|で}たところでした。",
             correct="{行|い}ったら", distractors=["{行|い}けば", "{行|い}くなら", "{行|い}ったなら"],
             en="Yesterday, when I hurried to the station, the train had just left.",
             notes_ja="過去の出来事で「〜してみたら、…だった」という発見・偶然の結果を表すには「たら（行ったら）」を使います。",
             notes_en="To express what you discovered when you got there in the past ('when I went, it had just left'), use 行ったら."),
        dict(stem="{明日|あした}お{天気|てんき}が（　　　）、{公園|こうえん}でお{弁当|べんとう}を{食|た}べましょう。",
             correct="よかったら", distractors=["いいだったら", "よくたら", "いいと"],
             en="If the weather is nice tomorrow, let's eat boxed lunches in the park.",
             notes_ja="「いい（よい）」のたら形は「よかったら」です。後ろが「〜ましょう（誘い）」なので「いいと」は使えません。",
             notes_en="The たら-form of いい is よかったら. いいと cannot be followed by an invitation (〜ましょう)."),
    ],
)

# ---------------------------------------------------------------- 44 なら
GRAMMAR[44] = dict(
    name="なら", reading="なら",
    meaning_en="if it is the case that ~; speaking of ~",
    similar="たら、ば、と",
    details=dict(
        formula="<strong>動詞・イ形容詞の普通形 ＋ なら</strong>（{行|い}くなら、{行|い}ったなら、{高|たか}いなら）<br>"
                "<strong>ナ形容詞・名詞（だ → なら）</strong>（{嫌|いや}なら、{学生|がくせい}なら、{明日|あした}なら）",
        notes_ja="相手が言ったことや、目の前の状況を受けて、「もしそうなら〜」「〜のことなら…」と話題に取り上げて、意見・アドバイス・提案・依頼を述べるときに使います。<br>"
                 "例：A「{来週|らいしゅう}、{北海道|ほっかいどう}へ{行|い}くんです。」<br>"
                 "　　B「{北海道|ほっかいどう}へ<strong>{行|い}くなら</strong>、{厚|あつ}いコートを{持|も}って{行|い}った{方|ほう}がいいですよ。」<br>"
                 "例：A「{田中|たなか}さんはどこですか。」<br>"
                 "　　B「{田中|たなか}さん<strong>なら</strong>、さっき{会議室|かいぎしつ}へ{行|い}きましたよ。」",
        notes_en="Used to pick up on something the listener just said or a known topic ('If that's the case...', 'Speaking of X...') and follow up with advice, a suggestion, a request, or information. "
                 "Attach なら directly to verbs and i-adjectives in plain form, and directly to nouns and na-adjective stems (without だ).",
        nuance_ja="<strong>★「たら」と「なら」の決定的な違い（時間の順番）</strong>：<br>"
                  "・北海道へ<strong>行ったら</strong>、ラーメンを食べてください。（北海道に<strong>着いたあとで</strong>食べる）<br>"
                  "・北海道へ<strong>行くなら</strong>、コートを買った{方|ほう}がいいですよ。（北海道へ<strong>行く前に</strong>買う）<br>"
                  "このように、これから相手が何かをする<strong>前</strong>にアドバイスするときは、必ず「辞書形＋なら」を使います。",
        nuance_en="Key difference between たら and なら (time order): "
                  "北海道へ行ったら means 'After you arrive in Hokkaido, do B'. "
                  "北海道へ行くなら means 'If you are going to go to Hokkaido, do B (even BEFORE you go, like buying a coat or booking a hotel)'.",
        trap_ja="①名詞・ナ形容詞には「だ」を付けずに直接「なら」を付けます（×学生だなら → ○<strong>{学生|がくせい}なら</strong>、×暇だなら → ○<strong>{暇|ひま}なら</strong>）。<br>"
                "②季節や自然の決まった変化には「なら」は使えません（×春なら暖かくなる → ○{春|はる}に<strong>なると／なったら</strong>{暖|あたた}かくなる）。<br>"
                "③これから行く前の準備について言うときは「行ったら」ではなく「<strong>{行|い}くなら</strong>」です。",
        trap_en="① Do NOT put だ before なら with nouns or na-adjectives: ○学生なら, ○静かなら (×学生だなら). "
                "② Do not use なら for natural or inevitable changes (×春なら暖かくなる → ○春になると暖かくなる). "
                "③ When the second action happens BEFORE the first (e.g., booking a ticket before traveling), you must use 辞書形 + なら.",
        contrast=[
            dict(type="wrong", sentence="{来月|らいげつ}{海外|かいがい}へ{旅行|りょこう}したら、{今|いま}のうちにパスポートを{作|つく}ってください。",
                 reason_ja="パスポートを作るのは「旅行する前」なので、「〜したあとで」を表す「たら」は使えません。",
                 reason_en="You must get a passport BEFORE traveling, so たら (which means 'after doing A') is illogical here."),
            dict(type="correct", sentence="{来月|らいげつ}{海外|かいがい}へ{旅行|りょこう}するなら、{今|いま}のうちにパスポートを{作|つく}ってください。",
                 reason_ja="「旅行するつもりなら（その前に）〜してください」には「辞書形＋なら」を使います。",
                 reason_en="辞書形 + なら means 'if it is the case that you plan to travel, do this (beforehand)'."),
            dict(type="correct", sentence="A：ハサミはどこですか。 B：ハサミなら、その{引|ひ}き{出|だ}しの{中|なか}ですよ。",
                 reason_ja="相手が探している「ハサミ」を話題に取り上げるときは「名詞＋なら」がぴったりです。",
                 reason_en="Noun + なら picks up on the item the listener just asked about ('If it's scissors you're looking for...')."),
        ],
        comparison=[
            dict(form="〜なら", form_en="if it is the case that / speaking of", badge="話題・助言", badge_type="good",
                 nuance_ja="相手の言葉や予定を受けて、「それなら〜」と助言・提案するときに使います（前後の時間順は自由）。",
                 nuance_en="Responds to the listener's topic/plan with advice; B can happen before A.",
                 example="パソコンを{買|か}うなら、{駅|えき}の{前|まえ}の{店|みせ}が{安|やす}いですよ。"),
            dict(form="〜たら", form_en="once / after / if", badge="AのあとでB", badge_type="both",
                 nuance_ja="必ずAが完了したあとにBをするという時間の順番があります。",
                 nuance_en="A must happen before B takes place.",
                 example="パソコンを{買|か}ったら、{設定|せってい}を{手伝|てつだ}いますよ。"),
            dict(form="〜ば", form_en="if (general condition)", badge="一般条件", badge_type="neutral",
                 nuance_ja="「〜すれば、…できる」のように、ある結果を得るための条件を客観的に述べます。",
                 nuance_en="States a general or logical condition required for a result.",
                 example="{予約|よやく}すれば、{安|やす}く{買|か}えます。"),
        ],
    ),
    quiz=[
        dict(stem="A：これからスーパーへ{買|か}い{物|もの}に{行|い}きます。<br>B：スーパーへ（　　　）、ついでに{牛乳|ぎゅうにゅう}も{買|か}ってきてくれませんか。",
             correct="{行|い}くなら", distractors=["{行|い}ったら", "{行|い}くと", "{行|い}けば"],
             en="A: I'm going to the supermarket to shop now. B: If you're going to the supermarket, could you buy some milk on the way too?",
             notes_ja="相手が「これから行く」と言ったのを受けて、「それなら〜してくれませんか」と頼む場面なので「行くなら」が最も自然です。",
             notes_en="Picking up on what Speaker A just said ('I'm going to the supermarket') to make a request requires 行くなら."),
        dict(stem="{温泉|おんせん}へ{行|い}きたいんですが、どこかいいところを{知|し}っていますか。<br>― {温泉|おんせん}（　　　）、{箱根|はこね}が{有名|ゆうめい}でいいですよ。",
             correct="なら", distractors=["だなら", "たら", "と"],
             en="I'd like to go to a hot spring; do you know any good places? — If it's hot springs you're looking for, Hakone is famous and nice.",
             notes_ja="相手の話題「温泉」を取り上げて勧めるときは、名詞に直接「なら」を付けます。「だなら」とは言いません。",
             notes_en="Attach なら directly to the noun (温泉なら) to pick up the topic and give a recommendation. ×だなら is ungrammatical."),
        dict(stem="{新|あたら}しいアパートを（　　　）、{契約|けいやく}する{前|まえ}に{夜|よる}の{周|まわ}りの{静|しず}かさも{確認|かくにん}した{方|ほう}がいいですよ。",
             correct="{借|か}りるなら", distractors=["{借|か}りたら", "{借|か}りると", "{借|か}りたなら"],
             en="If you are going to rent a new apartment, you should also check how quiet the neighborhood is at night before signing the contract.",
             notes_ja="「契約する前に確認する」のは「借りる前」の行動なので、Aの前にBをする「辞書形＋なら（借りるなら）」が正解です。",
             notes_en="Checking the neighborhood happens BEFORE renting/signing, so only 借りるなら ('if you intend to rent') works."),
        dict(stem="その{雑誌|ざっし}、もう{読|よ}まない（　　　）、{私|わたし}にくださいませんか。",
             correct="なら", distractors=["たら", "ば", "と"],
             en="If you're not going to read that magazine anymore, could you give it to me?",
             notes_ja="「もう読まない（状態・予定）なら、ください」と現在の意志・状況を受けて依頼しているので「読まないなら」が正解です。",
             notes_en="Following the negative plain form 読まない with a request ('if it's the case that you won't read it anymore'), use なら."),
    ],
)

# ---------------------------------------------------------------- 45 ば
GRAMMAR[45] = dict(
    name="ば", reading="ば",
    meaning_en="if ~ (general / hypothetical condition)",
    similar="たら、と、なら",
    details=dict(
        formula="<strong>Ⅰグループ</strong>：う段 → <strong>え段 ＋ ば</strong>（{行|い}く→{行|い}けば、{読|よ}む→{読|よ}めば）<br>"
                "<strong>Ⅱグループ</strong>：る → <strong>れば</strong>（{食|た}べる→{食|た}べれば、{見|み}る→{見|み}れば）<br>"
                "<strong>Ⅲグループ</strong>：する → <strong>すれば</strong>、{来|く}る → <strong>{来|く}れば</strong><br>"
                "<strong>イ形容詞</strong>：〜い → <strong>〜ければ</strong>（{安|やす}い→{安|やす}ければ、いい→<strong>よければ</strong>）<br>"
                "<strong>否定</strong>：〜ない → <strong>〜なければ</strong>（{行|い}かなければ）",
        notes_ja="「もしAという条件が満たされれば、Bになる／Bができる」という仮定条件や、一般的な法則・ことわざを表す文型です。<br>"
                 "例：{薬|くすり}を<strong>{飲|の}めば</strong>、すぐによくなりますよ。<br>"
                 "例：{天気|てんき}が<strong>よければ</strong>、ここから{富士山|ふじさん}が{見|み}えます。<br>"
                 "例：{説明|せつめい}を<strong>{聞|き}けば</strong>、だれでもわかります。<br>"
                 "特に後ろに<strong>可能動詞（〜できる・見える・間に合う）</strong>や状態を表す言葉が来るときによく使われます。",
        notes_en="Expresses a hypothetical or general condition ('Provided that A, then B happens / is possible'). "
                 "Frequently used when the main clause expresses potential/ability (〜できる, 見える, 間に合う), a desirable outcome, or a general truth/proverb.",
        nuance_ja="「ば」は「どうすればうまくいくか」という条件に注目する表現です。"
                  "そのため、前半と後半がどちらも同じ人の動作で、後ろに「〜てください」「〜ましょう」が来るときには原則として使えません（×駅に着けば電話してください → ○{駅|えき}に{着|つ}いたら{電話|でんわ}してください）。"
                  "ただし、前半が<strong>状態（形容詞・ある・いる・わかる等）</strong>のときは、後ろに「〜てください」が置けます（お{時間|じかん}が<strong>あれば</strong>、{来|き}てください）。",
        nuance_en="Rule on requests/volition with ば: When the first clause is an action verb (着く, 行く, 食べる), the second clause CANNOT be a command, request (〜てください), or invitation (〜ましょう)—use たら instead. "
                  "However, if the first clause is a state (an adjective, ある, いる, or negative 〜なければ), requests ARE allowed (質問があれば、聞いてください).",
        trap_ja="①「いい」のば形は「×いければ」ではなく「<strong>よければ</strong>」です。<br>"
                "②動作動詞の「ば」の後ろに「〜てください」は使えません（×読み終われば返してください → ○{読|よ}み{終|お}わったら{返|かえ}してください）。<br>"
                "③過去に実際に起きた1回の出来事（発見）には使えません（×窓を{開|あ}ければ雪が降っていた → ○{窓|まど}を{開|あ}けたら{雪|ゆき}が{降|ふ}っていた）。",
        trap_en="① The ば-form of いい is よければ (never ×いければ). "
                "② Do not follow an action verb + ば with 〜てください (use たら). "
                "③ Never use ば for a single past event/discovery ('When I opened the window, it was snowing' requires たら).",
        contrast=[
            dict(type="wrong", sentence="この{本|ほん}を{読|よ}み{終|お}われば、{図書館|としょかん}に{返|かえ}してください。",
                 reason_ja="動作を表す動詞（読み終わる）の「ば」の後ろには、依頼「〜てください」は置けません。",
                 reason_en="An action verb in the ば-form cannot be followed by a request (〜てください)."),
            dict(type="correct", sentence="この{本|ほん}を{読|よ}めば、{日本|にほん}の{歴史|れきし}がよくわかります。",
                 reason_ja="「〜すれば、…わかる／できる」のように条件と結果（可能・状態）を述べるときに「ば」が自然です。",
                 reason_en="ば is ideal when stating the condition needed to achieve a result or ability (よくわかります)."),
            dict(type="correct", sentence="わからないことがあれば、いつでも{聞|き}いてください。",
                 reason_ja="前半が状態動詞「ある」や形容詞のときは、後ろに「〜てください」を置くことができます。",
                 reason_en="When the condition is a state verb like ある or an adjective, 〜てください is allowed."),
        ],
        comparison=[
            dict(form="〜ば", form_en="if / provided that", badge="条件・可能", badge_type="good",
                 nuance_ja="「〜すれば、…できる／よくなる」という条件を強調するときに最もよく使われます。",
                 nuance_en="Highlights the condition required for a positive result or possibility.",
                 example="{急|いそ}げば、8{時|じ}の{電車|でんしゃ}に{間|ま}に{合|あ}います。"),
            dict(form="〜たら", form_en="if / when (all-purpose)", badge="万能・順序", badge_type="both",
                 nuance_ja="動作が完了したあとの依頼（〜てください）や過去の発見にも幅広く使えます。",
                 nuance_en="Works with action verbs + requests, temporal completion, and past discoveries.",
                 example="{駅|えき}に{着|つ}いたら、{電話|でんわ}してください。"),
            dict(form="〜と", form_en="whenever / automatic result", badge="自動的結果", badge_type="neutral",
                 nuance_ja="条件というより「Aをすると、いつも自動的にBになる」という必然を表します。",
                 nuance_en="Expresses an automatic, inevitable consequence rather than a condition.",
                 example="{右|みぎ}に{曲|ま}がると、{郵便局|ゆうびんきょく}があります。"),
        ],
    ),
    quiz=[
        dict(stem="{今|いま}すぐタクシーに（　　　）、{会議|かいぎ}の{時間|じかん}に{間|ま}に{合|あ}いますよ。",
             correct="{乗|の}れば", distractors=["{乗|の}るなら", "{乗|の}ればで", "{乗|の}りに"],
             en="If you take a taxi right now, you'll make it in time for the meeting.",
             notes_ja="「〜すれば、間に合う（可能）」と条件を述べる文なので、Ⅰグループ「乗る（noru）」のば形「乗れば」が正解です。",
             notes_en="To state the condition for making it in time (間に合います), use the ば-form of 乗る → 乗れば."),
        dict(stem="{値段|ねだん}がもう{少|すこ}し（　　　）、このパソコンを{買|か}いたいです。",
             correct="{安|やす}ければ", distractors=["{安|やす}いば", "{安|やす}いならで", "{安|やす}かったば"],
             en="If the price were a little cheaper, I would want to buy this computer.",
             notes_ja="イ形容詞「安い」のば形は、「い」を「ければ」に変えた「安ければ」です。",
             notes_en="For i-adjectives, replace い with ければ: 安い → 安ければ."),
        dict(stem="ご{都合|つごう}が（　　　）、{今度|こんど}の{土曜日|どようび}に{一緒|いっしょ}に{食事|しょくじ}をしませんか。",
             correct="よければ", distractors=["いければ", "いいば", "よくば"],
             en="If it is convenient for you, would you like to have a meal together this Saturday?",
             notes_ja="「いい（よい）」のば形は常に「よければ」です。「いければ」や「いいば」は誤りです。",
             notes_en="The ば-form of いい is always よければ (never ×いければ or ×いいば)."),
        dict(stem="{辞書|じしょ}で（　　　）、その{言葉|ことば}の{意味|いみ}がすぐにわかりますよ。",
             correct="{調|しら}べれば", distractors=["{調|しら}べば", "{調|しら}べるば", "{調|しら}べたらば"],
             en="If you look it up in a dictionary, you'll understand the meaning of that word right away.",
             notes_ja="「調べる」はⅡグループ動詞なので、「る」を「れば」に変えて「調べれば」になります。",
             notes_en="調べる is a Group 2 verb; replace る with れば → 調べれば."),
    ],
)

# ---------------------------------------------------------------- 46 と
GRAMMAR[46] = dict(
    name="と", reading="と",
    meaning_en="whenever ~; naturally follows that ~",
    similar="たら、ば、なら",
    details=dict(
        formula="<strong>動詞・イ形容詞の普通形（非過去） ＋ と</strong>（{押|お}すと、{行|い}かないと、{寒|さむ}いと）<br>"
                "<strong>ナ形容詞・名詞 ＋ だと</strong>（{静|しず}かだと、{雨|あめ}だと）",
        notes_ja="「Aが起きると、いつも必ず（自動的に・自然に）Bが起きる」という決まった結果を表す文型です。主に次の4つの場面で使います。<br>"
                 "①<strong>自然現象・季節の変化</strong>：{春|はる}に<strong>なると</strong>、{桜|さくら}が{咲|さ}きます。<br>"
                 "②<strong>機械の操作・計算</strong>：このボタンを<strong>{押|お}すと</strong>、ドアが{閉|し}まります。<br>"
                 "③<strong>道案内</strong>：あの{橋|はし}を<strong>{渡|わた}ると</strong>、{左|ひだり}に{病院|びょういん}があります。<br>"
                 "④<strong>個人的な習慣</strong>：{私|わたし}は{毎朝|まいあさ}{起|お}きる<strong>と</strong>、まず{水|みず}を{飲|の}みます。",
        notes_en="Expresses an automatic, natural, or habitual consequence ('Whenever A happens, B inevitably follows'). "
                 "Used for: (1) nature and seasons (春になると暖かくなる), (2) machine operation and math (このボタンを押すと水が出る), "
                 "(3) giving directions (角を曲がると駅がある), and (4) personal habits (朝起きるとコーヒーを飲む).",
        nuance_ja="<strong>★一番大事なルール（文末の制限）</strong>：<br>"
                  "「と」は「自然・自動的にそうなること」を表すため、後ろの文に<strong>自分の意志（〜つもりだ・〜たい）や、相手への働きかけ（〜てください・〜ましょう・〜ませんか）を置くことは絶対にできません</strong>。<br>"
                  "依頼や誘いを言いたいときは「<strong>たら</strong>」を使います。",
        nuance_en="Crucial restriction: Because と expresses an automatic, non-volitional consequence, the main clause can NEVER be a request (〜てください), invitation (〜ましょう), desire (〜たい), or intention (〜つもりだ). Use たら for those!",
        trap_ja="①後ろに「〜てください」「〜ましょう」「〜たいです」があるときは「と」は使えません（×着くと電話してください → ○{着|つ}い<strong>たら</strong>{電話|でんわ}してください）。<br>"
                "②「と」の前は必ず<strong>現在形（辞書形・ない形・〜い・〜だ）</strong>です。過去形「〜たと」とは言いません。<br>"
                "③名詞・ナ形容詞の後ろは「<strong>だと</strong>」になります（{雨|あめ}<strong>だと</strong>、{洗濯物|せんたくもの}が{乾|かわ}きません）。",
        trap_en="① Never use と before 〜てください, 〜ましょう, or 〜たい (use たら). "
                "② The verb before と must be in the non-past plain form (never ×行ったと). "
                "③ Nouns and na-adjectives take だと (静かだと).",
        contrast=[
            dict(type="wrong", sentence="{明日|あした}{時間|じかん}があると、{映画|えいが}を{見|み}に{行|い}きましょう。",
                 reason_ja="「〜ましょう」（誘い・意志）が後ろにある文では、「と」は使えません。",
                 reason_en="と cannot be followed by a volitional expression like 〜ましょう."),
            dict(type="correct", sentence="この{角|かど}を{右|みぎ}に{曲|ま}がると、{大|おお}きな{銀行|ぎんこう}が見えます。",
                 reason_ja="道案内で「曲がれば自動的に見える」という決まった結果には「と」がぴったりです。",
                 reason_en="Giving directions ('turn right and you'll see a bank') is a classic use of と."),
            dict(type="correct", sentence="{冬|ふゆ}になると、この{町|まち}では{毎日|まいにち}{雪|ゆき}が{降|ふ}ります。",
                 reason_ja="季節の変化や自然現象には「と」を使います。",
                 reason_en="Seasonal changes and natural phenomena take と."),
        ],
        comparison=[
            dict(form="〜と", form_en="whenever / natural consequence", badge="自然・機械・道", badge_type="good",
                 nuance_ja="自然現象・機械・道案内・習慣など、100％決まって起きる結果に使います（意志・依頼は不可）。",
                 nuance_en="Inevitable results: nature, machines, directions, habits (no volition/requests).",
                 example="100{円|えん}を{入|い}れると、{切符|きっぷ}が{出|で}ます。"),
            dict(form="〜たら", form_en="if / when (allows requests)", badge="依頼・意志OK", badge_type="both",
                 nuance_ja="1回きりの未来の予定や、後ろに「〜てください」「〜ましょう」が来るときに使います。",
                 nuance_en="Used for one-time future events and whenever the main clause is a request or invitation.",
                 example="{切符|きっぷ}を{買|か}ったら、{中|なか}へ{入|はい}りましょう。"),
            dict(form="〜ば", form_en="if (hypothetical condition)", badge="仮定条件", badge_type="neutral",
                 nuance_ja="「もし〜すれば、…できる」と条件を仮定して述べるときに使います。",
                 nuance_en="Focuses on the condition required for something to be possible.",
                 example="このアプリを{使|つか}えば、{簡単|かんたん}に{予約|よやく}できます。"),
        ],
    ),
    quiz=[
        dict(stem="この{道|みち}をまっすぐ（　　　）、{右|みぎ}に{市役所|しやくしょ}があります。",
             correct="{行|い}くと", distractors=["{行|い}ったらで", "{行|い}くなら", "{行|い}ったと"],
             en="If you go straight down this road, the city hall is on your right.",
             notes_ja="道案内で「〜すると、そこに…がある」と決まった事実を述べるときは「辞書形＋と（行くと）」を使います。",
             notes_en="When giving directions ('go straight and there is...'), use dictionary form + と (行くと)."),
        dict(stem="{秋|あき}に（　　　）、{山|やま}の{木|き}の{葉|は}が{赤|あか}や{黄色|きいろ}に{変|か}わります。",
             correct="なると", distractors=["なるなら", "なったと", "なればで"],
             en="When autumn comes, the leaves on the mountain trees turn red and yellow.",
             notes_ja="季節の変化や自然現象（「秋になると〜」）には「と」を使います。「なるなら」は自然現象には使えません。",
             notes_en="Seasonal and natural changes always take と (秋になると). なら cannot be used for natural laws."),
        dict(stem="このガラスは、{強|つよ}く（　　　）、すぐに{割|わ}れてしまいます。",
             correct="たたくと", distractors=["たたいたと", "たたくなら", "たたけばで"],
             en="If you hit this glass hard, it breaks right away.",
             notes_ja="物理的な性質・必然的な結果を表すので、現在形（辞書形）＋「と」の「たたくと」が正解です。「たたいたと」とは言えません。",
             notes_en="For an automatic physical consequence, use non-past plain form + と (たたくと). Past tense + と is ungrammatical here."),
        dict(stem="{祖父|そふ}は{毎晩|まいばん}お{酒|さけ}を（　　　）、すぐ{顔|かお}が{赤|あか}くなります。",
             correct="{飲|の}むと", distractors=["{飲|の}むなら", "{飲|の}んだと", "{飲|の}めばで"],
             en="Whenever my grandfather drinks alcohol every evening, his face turns red right away.",
             notes_ja="「〜すると、いつも決まってそうなる」という体質・習慣的な変化には「飲むと」を使います。",
             notes_en="For a habitual or physiological reaction that happens every time, use 飲むと."),
    ],
)

# ---------------------------------------------------------------- 47 について
GRAMMAR[47] = dict(
    name="について", reading="について",
    meaning_en="about; regarding; concerning",
    similar="に対して、によって、のために",
    details=dict(
        formula="<strong>名詞 ＋ について</strong>（＋ 話す・聞く・調べる・考える・書く）<br>"
                "<strong>名詞 ＋ についての ＋ 名詞</strong>（または <strong>〜に関する ＋ 名詞</strong>）<br>"
                "例：{日本|にほん}の{文化|ぶんか}<strong>について</strong>{調|しら}べる／{将来|しょうらい}<strong>についての</strong>{計画|けいかく}",
        notes_ja="話したり、聞いたり、調べたり、考えたり、書いたりする「テーマ・内容（何についてか）」を表す表現です。<br>"
                 "例：{今日|きょう}は{環境問題|かんきょうもんだい}<strong>について</strong>スピーチをします。<br>"
                 "例：この{計画|けいかく}<strong>について</strong>、どう{思|おも}いますか。<br>"
                 "後ろに名詞が来るときは、「<strong>〜についての ＋ 名詞</strong>」になります。<br>"
                 "例：{日本|にほん}の{歴史|れきし}<strong>についての</strong>{本|ほん}を{読|よ}んでいます。",
        notes_en="Means 'about / regarding / concerning' and marks the topic or subject matter of speaking, asking, researching, thinking, or writing. "
                 "When modifying a following noun, add の: 名詞 + についての + 名詞 (日本の文化についての本).",
        nuance_ja="単に「〜のことを話す」と言うよりも、少しテーマ性がある話題（文化・歴史・計画・将来の進路・使い{方|かた}の説明など）について深く話したり調べたりするときによく使われます。",
        nuance_en="More specific than simply 〜のことを, 〜について is used when discussing, researching, or explaining a defined topic or theme.",
        trap_ja="①後ろに名詞が来るときは必ず「<strong>の</strong>」を入れます（×日本の文化について本 → ○{日本|にほん}の{文化|ぶんか}<strong>についての</strong>{本|ほん}）。<br>"
                "②相手の態度・対象を表す「〜に対して」（お客様に対して丁寧にする）や、手段・原因を表す「〜によって」と混同しないようにしましょう。",
        trap_en="① Always include の before a noun: ○日本の文化についての本 (×日本の文化について本). "
                "② Do not confuse it with にとって ('from the standpoint of') or に対して ('toward / in contrast to').",
        contrast=[
            dict(type="wrong", sentence="{図書館|としょかん}で{宇宙|うちゅう}について{本|ほん}を{借|か}りました。",
                 reason_ja="後ろに名詞「本」を直接つなげることはできません。「についての」にします。",
                 reason_en="について cannot directly modify a noun without の."),
            dict(type="correct", sentence="{図書館|としょかん}で{宇宙|うちゅう}についての{本|ほん}を{借|か}りました。",
                 reason_ja="名詞「本」を修飾するときは「名詞＋についての＋名詞」にします。",
                 reason_en="Use 名詞 + についての + 名詞 to modify a noun ('a book about space')."),
            dict(type="correct", sentence="{新|あたら}しい{商品|しょうひん}について、{アンケート|あんけーと}を{行|おこな}いました。",
                 reason_ja="動詞（行う・調べる・話すなど）にかかるときは「について」のまま使います。",
                 reason_en="Use について directly when it modifies a verb phrase."),
        ],
        comparison=[
            dict(form="N ＋ について", form_en="about / concerning (topic)", badge="テーマ・内容", badge_type="good",
                 nuance_ja="話す・調べる・考える・書くなどの「テーマ・内容」を表します。",
                 nuance_en="Marks the subject matter of speaking, researching, thinking, or writing.",
                 example="{将来|しょうらい}の{仕事|しごと}について{考|かんが}えています。"),
            dict(form="N ＋ にとって", form_en="for / from the standpoint of", badge="立場・評価", badge_type="both",
                 nuance_ja="「〜の立場から見ると（大切だ・難しい）」と評価するときに使います。",
                 nuance_en="Marks the person from whose standpoint something is judged (important, hard, etc.).",
                 example="{私|わたし}にとって、{家族|かぞく}が{一番|いちばん}{大切|たいせつ}です。"),
            dict(form="N ＋ のために", form_en="for the sake/purpose of", badge="目的・利益", badge_type="neutral",
                 nuance_ja="目的や、誰かの利益のために行動することを表します。",
                 nuance_en="Expresses purpose or doing something for someone's benefit.",
                 example="{健康|けんこう}のために、{毎日|まいにち}{歩|ある}いています。"),
        ],
    ),
    quiz=[
        dict(stem="{来週|らいしゅう}の{授業|じゅぎょう}で、{自分|じぶん}の{国|くに}の{行事|ぎょうじ}（　　　）{発表|はっぴょう}します。",
             correct="について", distractors=["にとって", "になって", "につれて"],
             en="In next week's class, I will give a presentation about events in my country.",
             notes_ja="「発表する」のテーマ・内容を表すので「について」が正解です。「にとって」は立場、「につれて」は変化を表します。",
             notes_en="To mark the topic of a presentation (発表します), use について ('about')."),
        dict(stem="{日本の昔話|にほんのむかしばなし}（　　　）{絵本|えほん}を{図書館|としょかん}で{探|さが}しています。",
             correct="についての", distractors=["について", "についてな", "にとっての"],
             en="I am looking for a picture book about Japanese folktales at the library.",
             notes_ja="後ろに名詞「絵本」が続くので、「〜についての＋名詞」の形が正解です。",
             notes_en="Since a noun (絵本) follows immediately, use についての ('a picture book about ~')."),
        dict(stem="A：すみません、{入会|にゅうかい}の{手続|てつづ}き（　　　）お{伺|うかが}いしたいんですが。<br>B：はい、こちらへどうぞ。",
             correct="について", distractors=["にとって", "によって", "にたいして"],
             en="A: Excuse me, I would like to ask about the membership registration procedure. B: Yes, right this way please.",
             notes_ja="「〜の内容に関して質問したい（伺いたい）」という場面なので「について」を使います。",
             notes_en="When asking a question regarding a specific topic (手続きについてお伺いしたい), use について."),
        dict(stem="{今日|きょう}の{会議|かいぎ}では、{来月|らいげつ}のイベントの{予算|よさん}（　　　）{話|はな}し{合|あ}いました。",
             correct="について", distractors=["にとって", "によってで", "につけて"],
             en="In today's meeting, we discussed the budget for next month's event.",
             notes_ja="「話し合う」の議題・テーマを示すので「予算について」が正解です。",
             notes_en="To indicate the subject discussed in a meeting (話し合いました), use について."),
    ],
)

# ---------------------------------------------------------------- 48 あいだ
GRAMMAR[48] = dict(
    name="あいだ", reading="あいだ",
    meaning_en="during the whole time ~; while ~",
    similar="あいだに、ながら、うちは",
    details=dict(
        formula="<strong>動詞ている形 ＋ あいだ</strong>（{寝|ね}ているあいだ、{待|ま}っているあいだ）<br>"
                "<strong>イ形容詞（〜い） ＋ あいだ</strong>（{若|わか}いあいだ、{涼|すず}しいあいだ）<br>"
                "<strong>ナ形容詞 ＋ な ＋ あいだ</strong>（{元気|げんき}なあいだ、{静|しず}かなあいだ）<br>"
                "<strong>名詞 ＋ の ＋ あいだ</strong>（{夏休|なつやす}みのあいだ、{留守|るす}のあいだ）",
        notes_ja="「Aが続いている期間ずっと、Bの状態・動作も続く」ことを表します（Aの長さとBの長さがほぼ同じです）。<br>"
                 "例：{母|はは}が{買|か}い{物|もの}を<strong>しているあいだ</strong>、{私|わたし}はずっと{車|くるま}で<strong>{待|ま}っていました</strong>。<br>"
                 "例：<strong>{夏休|なつやす}みのあいだ</strong>、{毎日|まいにち}プールで<strong>{泳|およ}ぎました</strong>。<br>"
                 "後ろの文（B）には、「ずっと〜していた」「〜していた」「毎日〜した」のように、<strong>継続する動詞や状態</strong>が来ます。",
        notes_en="Expresses that throughout the entire time A continues, action or state B also continues concurrently (the duration of A and B match). "
                 "Because B spans the whole period, the main clause must be a continuous action or state (ずっと待っていた, 寝ていた, 毎日働いた), not a momentary one-off event.",
        nuance_ja="<strong>★「あいだ」と「あいだに」の違い</strong>：<br>"
                  "・<strong>あいだ</strong>：その期間<strong>ずっと続けて</strong>何かをする（赤ちゃんが寝ている<strong>あいだ</strong>、ずっと本を読んでいた）。<br>"
                  "・<strong>あいだに</strong>：その期間の<strong>どこか1点で</strong>何かをする／起きる（赤ちゃんが寝ている<strong>あいだに</strong>、洗濯を終えた）。",
        nuance_en="Key distinction: あいだ means B continues for the WHOLE duration of A (I read a book the whole time the baby slept). "
                  "あいだに means a single event B happens at SOME POINT within the span of A (While the baby was sleeping, I finished the laundry).",
        trap_ja="①名詞の後ろには「<strong>の</strong>」が必要です（×夏休みあいだ → ○{夏休|なつやす}み<strong>の</strong>あいだ）。<br>"
                "②動詞は原則として「<strong>ている形</strong>」（または「ない形」）を使います（{待|ま}っているあいだ）。<br>"
                "③後ろが一瞬で終わる動作（電気が消えた・荷物が届いた）のときは「あいだ」ではなく「<strong>あいだに</strong>」を使います。",
        trap_en="① Always put の between a noun and あいだ: 夏休みのあいだ. "
                "② Verbs before あいだ must express a state/duration, typically in the ている form (待っているあいだ). "
                "③ If the main clause is a punctual/single event (a package arrived, someone called), use あいだに, NOT あいだ.",
        contrast=[
            dict(type="wrong", sentence="{私|わたし}がお{風呂|ふろ}に{入|はい}っているあいだ、{電話|でんわ}がかかってきました。",
                 reason_ja="「電話がかかってきた」は期間中の1点で起きた出来事なので、「あいだ」ではなく「あいだに」を使います。",
                 reason_en="A phone call coming in is a momentary event within that time span, requiring あいだに rather than あいだ."),
            dict(type="correct", sentence="{私|わたし}が{料理|りょうり}を{作|つく}っているあいだ、{子|こ}どもたちはテレビを{見|み}ていました。",
                 reason_ja="料理を作っている期間ずっとテレビを見ていたので、「あいだ」が使えます。",
                 reason_en="The children watched TV throughout the time I was cooking, so あいだ is correct."),
            dict(type="correct", sentence="{冬休|ふゆやす}みのあいだ、ずっと{祖母|そぼ}の{家|いえ}にいました。",
                 reason_ja="名詞「冬休み」には「の」を付けて「冬休みのあいだ」とし、継続する状態「ずっと〜にいた」が続きます。",
                 reason_en="Noun + の + あいだ paired with a continuous state (ずっと祖母の家にいました)."),
        ],
        comparison=[
            dict(form="〜あいだ", form_en="throughout the whole time ~", badge="期間ずっと", badge_type="good",
                 nuance_ja="Aの期間ずっとBの動作や状態が続くときに使います（後ろは継続表現）。",
                 nuance_en="B continues throughout the entire span of A.",
                 example="{雨|あめ}が{降|ふ}っているあいだ、{ホテル}で{休|やす}んでいました。"),
            dict(form="〜あいだに", form_en="at some point while ~", badge="期間中に1回", badge_type="both",
                 nuance_ja="Aが続いている期間の中に、Bという出来事が起きたり完了したりするときに使います。",
                 nuance_en="A single event or completion B occurs within the time window of A.",
                 example="{雨|あめ}が{降|ふ}らないあいだに、{買|か}い{物|もの}へ{行|い}きましょう。"),
            dict(form="Vます形 ＋ ながら", form_en="while doing (same person)", badge="同時進行", badge_type="neutral",
                 nuance_ja="{一人|ひとり}の人が2つの動作を同時に行うときに使います（主語が同じ）。",
                 nuance_en="One person performs two actions simultaneously (same subject).",
                 example="{音楽|おんがく}を{聞|き}きながら、{掃除|そうじ}をします。"),
        ],
    ),
    quiz=[
        dict(stem="{母|はは}が{銀行|ぎんこう}で{手続|てつづ}きをしている（　　　）、{私|わたし}はロビーのソファーでずっと{待|ま}っていました。",
             correct="あいだ", distractors=["あいだに", "ながら", "までに"],
             en="While my mother was handling procedures at the bank, I was waiting on the lobby sofa the whole time.",
             notes_ja="後半に「ずっと待っていました」と継続する動作があるので、「〜あいだ」が正解です。「ながら」は主語が同じときにしか使えません。",
             notes_en="ずっと待っていました spans the entire duration, requiring あいだ. (ながら cannot be used when the subjects differ.)"),
        dict(stem="（　　　）、{毎日|まいにち}{図書館|としょかん}へ{行|い}ってレポートを{書|か}いていました。",
             correct="{夏休|なつやす}みのあいだ", distractors=["{夏休|なつやす}みあいだ", "{夏休|なつやす}みなあいだ", "{夏休|なつやす}みのあいだに"],
             en="During summer vacation, I went to the library every day and worked on my report.",
             notes_ja="名詞「夏休み」には「の」を付けて「夏休みのあいだ」とし、後半の「毎日〜していた」という継続的な習慣につなげます。",
             notes_en="Attach の after the noun (夏休みのあいだ) when describing a continuous habit across the whole vacation."),
        dict(stem="{電車|でんしゃ}に（　　　）、ずっと{窓|まど}から{外|そと}の{景色|けしき}を{見|み}ていました。",
             correct="{乗|の}っているあいだ", distractors=["{乗|の}るあいだ", "{乗|の}っているあいだに", "{乗|の}りあいだ"],
             en="While riding on the train, I was looking at the scenery outside the window the whole time.",
             notes_ja="「ずっと〜見ていました」と継続しているので「ている形＋あいだ（乗っているあいだ）」が正解です。",
             notes_en="With ずっと見ていました spanning the ride, use Verb-ている + あいだ (乗っているあいだ)."),
        dict(stem="{両親|りょうしん}が{共働|ともばたら}きで{昼間|ひるま}いない（　　　）、{祖母|そぼ}が{私|わたし}たちの{世話|せわ}をしてくれていました。",
             correct="あいだ", distractors=["あいだに", "ながら", "までに"],
             en="While my parents were both working and away during the daytime, my grandmother used to take care of us.",
             notes_ja="両親が昼間いない時間帯ずっと祖母が世話をしてくれていたので、「あいだ」を使います。",
             notes_en="Taking care of us lasted throughout the time our parents were away, so use あいだ."),
    ],
)

# ---------------------------------------------------------------- 49 あいだに
GRAMMAR[49] = dict(
    name="あいだに", reading="あいだに",
    meaning_en="while ~ (an event happens within that time span)",
    similar="あいだ、うちに、までに",
    details=dict(
        formula="<strong>動詞ている形／ない形 ＋ あいだに</strong>（{寝|ね}ているあいだに、{忘|わす}れないあいだに）<br>"
                "<strong>イ形容詞（〜い） ＋ あいだに</strong>（{明|あか}るいあいだに、{若|わか}いあいだに）<br>"
                "<strong>ナ形容詞 ＋ な ＋ あいだに</strong>（{静|しず}かなあいだに）<br>"
                "<strong>名詞 ＋ の ＋ あいだに</strong>（{留守|るす}のあいだに、{休|やす}みのあいだに）",
        notes_ja="「Aという状態が続いている期間の中のどこかで、Bという出来事が起きる／Bの動作を完了させる」ことを表します。<br>"
                 "例：{私|わたし}が<strong>{留守|るす}のあいだに</strong>、{宅配便|たくはいびん}が<strong>{届|とど}きました</strong>。<br>"
                 "例：{赤|あか}ちゃんが<strong>{寝|ね}ているあいだに</strong>、{晩|ばん}ごはんの{支度|したく}を<strong>してしまいましょう</strong>。<br>"
                 "例：{外|そと}が<strong>{明|あか}るいあいだに</strong>、{家|いえ}に<strong>{帰|かえ}った{方|ほう}がいいですよ</strong>。<br>"
                 "後ろの文（B）には、1回で終わる動作や変化（届いた・止んだ・済ませる・メモする）が来ます。",
        notes_en="Expresses that a single event, change, or completed action B takes place WITHIN the time window in which state A holds true. "
                 "Unlike あいだ (where B lasts the whole time), the main clause after あいだに is a punctual or bounded event (a package arrived, the rain stopped, I'll finish cooking).",
        nuance_ja="「〜あいだに」は、「その状態が変わってしまう前に（チャンスを逃さず）〜しよう」という意味でもよく使われます（スープが温かいうちに／あいだに飲む、暗くならないあいだに帰る）。",
        nuance_en="Often used in the sense of seizing a window of opportunity before conditions change (e.g., finishing housework while the baby is asleep, or heading home while it is still light out).",
        trap_ja="①後ろに「ずっと〜していた」が来るときは「あいだに」は使えません（×寝ているあいだにずっと本を読んでいた → ○{寝|ね}ている<strong>あいだ</strong>ずっと{本|ほん}を{読|よ}んでいた）。<br>"
                "②逆に、後ろが瞬間動詞・完了表現（届いた・消えた・食べてしまった）のときは必ず「<strong>あいだに</strong>」にします。<br>"
                "③名詞には「<strong>の</strong>」を付けます（{夏休|なつやす}み<strong>の</strong>あいだに{免許|めんきょ}を{取|と}った）。",
        trap_en="① Never use あいだに when the main clause has ずっと or describes an unbroken state lasting the whole time (use あいだ). "
                "② Always use あいだに when the main clause is a single event or completion. "
                "③ Remember の after nouns: 留守のあいだに.",
        contrast=[
            dict(type="wrong", sentence="{母|はは}が{昼寝|ひるね}をしているあいだに、{私|わたし}もずっと{寝|ね}ていました。",
                 reason_ja="「ずっと寝ていました」は期間全体にわたる継続なので、「あいだに」ではなく「あいだ」にします。",
                 reason_en="ずっと寝ていました lasts the whole period, so use あいだ, not あいだに."),
            dict(type="correct", sentence="{母|はは}が{昼寝|ひるね}をしているあいだに、{洗濯|せんたく}と{掃除|そうじ}を{終|お}わらせました。",
                 reason_ja="昼寝の期間中に洗濯と掃除を完了させたので、「あいだに」が正解です。",
                 reason_en="Finishing the laundry and cleaning occurred within the nap window, so あいだに is right."),
            dict(type="correct", sentence="{知|し}らないあいだに、{外|そと}の{雨|あめ}がやんでいました。",
                 reason_ja="「雨がやむ」は期間のある時点で起きた変化なので、「あいだに」を使います。",
                 reason_en="The rain stopping is a change that happened at some point while I didn't notice: 知らないあいだに."),
        ],
        comparison=[
            dict(form="〜あいだに", form_en="within the time while ~", badge="期間内に完了・発生", badge_type="good",
                 nuance_ja="Aの期間の中のどこかの時点で、Bが起きる／Bを終わらせるときに使います。",
                 nuance_en="Event B happens or finishes at some point within period A.",
                 example="{電車|でんしゃ}に{乗|の}っているあいだに、この{本|ほん}を{読|よ}み{終|お}わりました。"),
            dict(form="〜あいだ", form_en="throughout the whole time ~", badge="期間ずっと継続", badge_type="both",
                 nuance_ja="Aの期間ずっと最初から最後までBが続くときに使います。",
                 nuance_en="Action/state B continues throughout the entire duration of A.",
                 example="{電車|でんしゃ}に{乗|の}っているあいだ、ずっと{寝|ね}ていました。"),
            dict(form="〜までに", form_en="by (a deadline)", badge="期限", badge_type="neutral",
                 nuance_ja="期間ではなく「5時までに」「金曜日までに」のように期限の時点を表します。",
                 nuance_en="Marks a specific point-in-time deadline ('by 5 o'clock') rather than a span.",
                 example="5{時|じ}までにレポートを{出|だ}してください。"),
        ],
    ),
    quiz=[
        dict(stem="{私|わたし}がシャワーを{浴|あ}びている（　　　）、{誰|だれ}かから{電話|でんわ}があったようです。",
             correct="あいだに", distractors=["あいだ", "ながら", "までに"],
             en="It seems there was a phone call from someone while I was taking a shower.",
             notes_ja="「電話があった」はシャワーを浴びている期間の中の1点で起きた出来事なので、「あいだに」が正解です。",
             notes_en="A phone call coming in is a single event occurring within the time span of the shower, so use あいだに."),
        dict(stem="{忘|わす}れない（　　　）、{今|いま}すぐ手帳に{約束|やくそく}の{時間|じかん}をメモしておきましょう。",
             correct="あいだに", distractors=["あいだ", "ながら", "あとで"],
             en="While we haven't forgotten, let's jot down the appointment time in our planner right now.",
             notes_ja="「忘れない状態が続いている期間内にメモする」という完了動作なので、「忘れないあいだに」が正解です。",
             notes_en="Jotting down a note within the window before forgetting requires ない-form + あいだに."),
        dict(stem="しばらく{会|あ}わない（　　　）、{甥|おい}の{背|せ}がとても{高|たか}くなっていてびっくりしました。",
             correct="あいだに", distractors=["あいだで", "ながら", "までに"],
             en="While I hadn't seen him for a while, my nephew had grown very tall, which surprised me.",
             notes_ja="会わない期間のうちに「背が高くなる」という変化が起きたので、「あいだに」を使います。",
             notes_en="A change (growing tall) took place during the period we didn't meet, so use あいだに."),
        dict(stem="（　　　）、{自転車|じてんしゃ}の{乗|の}り{方|かた}をすっかりマスターしました。",
             correct="{夏休|なつやす}みのあいだに", distractors=["{夏休|なつやす}みのあいだ", "{夏休|なつやす}みあいだに", "{夏休|なつやす}みのながら"],
             en="During summer vacation, I completely mastered how to ride a bicycle.",
             notes_ja="「すっかりマスターした」は期間内に完了した変化・達成なので、「名詞＋の＋あいだに」が正解です。",
             notes_en="Mastering how to ride a bike is a completed achievement within the vacation window: 夏休みのあいだに."),
    ],
)

# ---------------------------------------------------------------- 50 までに
GRAMMAR[50] = dict(
    name="までに", reading="までに",
    meaning_en="by (a deadline); before ~",
    similar="まで、あいだに、まえに",
    details=dict(
        formula="<strong>時刻・{日|ひ}・期限の名詞 ＋ までに</strong>（5{時|じ}までに、{金曜日|きんようび}までに、{来週|らいしゅう}までに）<br>"
                "<strong>動詞辞書形 ＋ までに</strong>（{会議|かいぎ}が{始|はじ}まるまでに、{卒業|そつぎょう}するまでに）",
        notes_ja="動作や作業を完了させる<strong>期限（タイムリミット）</strong>を表します。「その時点より前に、1回その動作を終える」という意味です。<br>"
                 "例：この{書類|しょるい}は、{今週|こんしゅう}の<strong>{金曜日|きんようび}までに</strong>{出|だ}してください。<br>"
                 "例：{夜|よる}10{時|じ}<strong>までに</strong>は{家|いえ}に{帰|かえ}ります。<br>"
                 "例：{先生|せんせい}が<strong>{来|く}るまでに</strong>、{教室|きょうしつ}を{掃除|そうじ}しておきましょう。<br>"
                 "後ろには「出す・返す・帰る・連絡する・終わらせる・決める」など、<strong>完了する動詞</strong>が来ます。",
        notes_en="Marks a deadline ('by [time]', 'before [event] happens'). The action in the main clause must be completed at or before that point in time. "
                 "Can attach to time nouns (5時までに, 金曜日までに) or to verbs in the dictionary form (会議が始まるまでに).",
        nuance_ja="<strong>★「まで」と「までに」の超重要な違い</strong>：<br>"
                  "・5時<strong>まで</strong>働きます。＝ 5時まで<strong>ずっと続けて</strong>働く（継続）。<br>"
                  "・5時<strong>までに</strong>帰ります。＝ 5時を期限として、それより前に<strong>帰る動作を完了する</strong>（期限）。<br>"
                  "「返す・出す・連絡する・着く」のような瞬間的な動作には、必ず「<strong>までに</strong>」を使います。",
        nuance_en="Crucial distinction between まで and までに: "
                  "まで means 'until' (an action or state continues non-stop up to that time: 5時まで働く / 待つ / いる). "
                  "までに means 'by' (a deadline by which a single action must be completed: 5時までに帰る / 出す / 返す).",
        trap_ja="①「待つ・寝る・働く・いる」のように継続する動詞には「までに」ではなく「<strong>まで</strong>」を使います（×3時までに待ちます → ○3{時|じ}<strong>まで</strong>{待|ま}ちます）。<br>"
                "②逆に「返す・提出する・申し込む」に「まで」を使うのは誤りです（×金曜日まで出してください → ○{金曜日|きんようび}<strong>までに</strong>{出|だ}してください）。<br>"
                "③動詞に付けるときは<strong>辞書形</strong>です（×始まったまでに → ○<strong>{始|はじ}まるまでに</strong>）。",
        trap_en="① With continuous verbs like 待つ, 働く, 寝る, いる, use まで ('until'), NOT までに. "
                "② With completion/punctual verbs like 返す, 出す, 申し込む, 帰る, use までに ('by'), NOT まで. "
                "③ Before までに, verbs must be in the dictionary form (始まるまでに).",
        contrast=[
            dict(type="wrong", sentence="{図書館|としょかん}の{本|ほん}は{来週|らいしゅう}の{火曜日|かようび}まで{返|かえ}さなければなりません。",
                 reason_ja="「本を返す」は継続する動作ではなく期限までに完了させる動作なので、「まで」は使えません。",
                 reason_en="Returning a book is a one-time completion with a deadline, so まで ('until') is wrong."),
            dict(type="correct", sentence="{図書館|としょかん}の{本|ほん}は{来週|らいしゅう}の{火曜日|かようび}までに{返|かえ}さなければなりません。",
                 reason_ja="返却の期限（タイムリミット）を表すので「までに」を使います。",
                 reason_en="Use までに to mark the deadline ('by next Tuesday')."),
            dict(type="correct", sentence="{今日|きょう}は{夕方|ゆうがた}6{時|じ}まで{図書館|としょかん}で{勉強|べんきょう}します。",
                 reason_ja="「6時までずっと勉強を続ける」という継続には「まで」を使います。",
                 reason_en="Studying continuously until 6 PM uses まで."),
        ],
        comparison=[
            dict(form="〜までに", form_en="by (a deadline)", badge="期限・完了", badge_type="good",
                 nuance_ja="その時刻・日付をタイムリミットとして、それより前に動作を完了させるときに使います。",
                 nuance_en="Marks a deadline by which an action must be completed.",
                 example="{明日|あした}の{朝|あさ}9{時|じ}までにメールを{送|おく}ってください。"),
            dict(form="〜まで", form_en="until (continuous)", badge="継続の終わり", badge_type="both",
                 nuance_ja="ある動作や状態が、その時刻までずっと続くことを表します。",
                 nuance_en="Marks the endpoint up to which a continuous action or state lasts.",
                 example="{明日|あした}の{朝|あさ}9{時|じ}までここで{待|ま}っています。"),
            dict(form="〜まえに", form_en="before doing ~", badge="動作の前後", badge_type="neutral",
                 nuance_ja="期限というより、単に「Aをする前にBをする」という動作の順番を表します。",
                 nuance_en="Simply states the sequence of actions ('do B before A') without emphasizing a strict deadline.",
                 example="{寝|ね}るまえに{歯|は}をみがきます。"),
        ],
    ),
    quiz=[
        dict(stem="パーティーに{参加|さんか}する{人|ひと}は、{今月|こんげつ}の20{日|はつか}（　　　）{申|もう}し{込|こ}んでください。",
             correct="までに", distractors=["まで", "あいだに", "あいだ"],
             en="Those who will participate in the party, please sign up by the 20th of this month.",
             notes_ja="「申し込む」の締め切り（期限）を表すので「までに」が正解です。「まで」は継続にしか使えません。",
             notes_en="Signing up has a deadline ('by the 20th'), requiring までに."),
        dict(stem="お{客|きゃく}さまが（　　　）、{会議室|かいぎしつ}の{準備|じゅんび}を{終|お}わらせておきましょう。",
             correct="{来|く}るまでに", distractors=["{来|き}たまでに", "{来|く}るまで", "{来|く}るあいだ"],
             en="Let's finish preparing the conference room by the time the client arrives.",
             notes_ja="「準備を終わらせる」期限を動詞で表すときは「辞書形＋までに（来るまでに）」を使います。",
             notes_en="To set an event as the deadline for finishing preparations, use Verb-dictionary form + までに (来るまでに)."),
        dict(stem="このレポートは、{来週|らいしゅう}の{月曜日|げつようび}の{正午|しょうご}（　　　）{提出|ていしゅつ}しなければなりません。",
             correct="までに", distractors=["まで", "ながら", "うちに"],
             en="This report must be submitted by noon next Monday.",
             notes_ja="「提出する」のタイムリミットなので「までに」が正解です。",
             notes_en="Submitting a report has a deadline, so use までに ('by noon next Monday')."),
        dict(stem="電車が（　　　）、{駅|えき}の売店でお{茶|ちゃ}と{新聞|しんぶん}を{買|か}いました。",
             correct="{出|で}るまでに", distractors=["{出|で}たまでに", "{出|で}るまでで", "{出|で}るながら"],
             en="Before the train departed (by departure time), I bought tea and a newspaper at the station kiosk.",
             notes_ja="電車の発車時刻をタイムリミットとして買い物を済ませたので、「辞書形＋までに（出るまでに）」が正解です。",
             notes_en="Buying items before the train's departure deadline uses dictionary form + までに (出るまでに)."),
    ],
)

# ---------------------------------------------------------------- 51 ていく
GRAMMAR[51] = dict(
    name="ていく", reading="ていく",
    meaning_en="go on doing ~; change continuing into the future; move away",
    similar="てくる、てしまう、ている",
    details=dict(
        formula="<strong>動詞て形 ＋ いく（／いきます）</strong><br>"
                "① <strong>移動（〜から離れる）</strong>：{飛|と}んでいく、{走|はし}っていく<br>"
                "② <strong>動作をしてから行く</strong>：{買|か}っていく、{着|き}ていく<br>"
                "③ <strong>現在から未来への変化・継続</strong>：{寒|さむ}くなっていく、これからも{頑張|がんば}っていく",
        notes_ja="「いく」には、話し手のいる場所から<strong>離れていく</strong>方向や、<strong>今から未来へ向かって</strong>変化・継続が進むという意味があります。<br>"
                 "①<strong>空間的な移動（離れる）</strong>：{鳥|とり}が{空|そら}へ<strong>{飛|と}んでいきました</strong>。<br>"
                 "②<strong>〜してから（あちらへ）行く</strong>：お{弁当|べんとう}を<strong>{持|も}っていきます</strong>。<br>"
                 "③<strong>今から未来への継続・変化</strong>：<br>"
                 "例：これからもっと<strong>{寒|さむ}くなっていきます</strong>。<br>"
                 "例：{卒業|そつぎょう}しても、この{勉強|べんきょう}を<strong>{続|つづ}けていきたい</strong>です。",
        notes_en="Combines a て-form verb with いく to show movement away from the speaker or progression from the present into the future: "
                 "(1) Physical movement away: 鳥が飛んでいった ('the bird flew away'); "
                 "(2) Doing an action and then going somewhere: お弁当を持っていく ('take a bento and go'); "
                 "(3) Change or continuation from now into the future: これから寒くなっていく ('it will get colder from now on'), これからも頑張っていく ('I'll keep doing my best going forward').",
        nuance_ja="「ていく」と「てくる」を区別するコツは、<strong>基準点（私・現在）から離れるか、近づくか</strong>です。<br>"
                  "・過去から今までずっと続いたこと → <strong>〜てきた</strong>（今まで頑張ってきた）<br>"
                  "・今から未来へ続けていくこと → <strong>〜ていく</strong>（これからも頑張っていく）<br>"
                  "※「ていく」は漢字の「行く」ではなく、ひらがなで「<strong>ていく</strong>」と書くのが普通です。",
        nuance_en="To choose between ていく and てくる, look at the direction relative to 'here / now': "
                  "Past → Now uses てきた (今まで頑張ってきた). "
                  "Now → Future uses ていく (これからも頑張っていく). "
                  "As a subsidiary verb, いく is normally written in hiragana.",
        trap_ja="①「今まで〜」には「ていく」は使えません（×今まで頑張っていきました → ○{今|いま}まで{頑張|がんば}って<strong>きました</strong>）。<br>"
                "②「これから〜」には「てくる」ではなく「<strong>ていく</strong>」を使います（これから{増|ふ}えて<strong>いく</strong>でしょう）。<br>"
                "③話し手に近づいてくる動きには「てくる」、遠ざかる動きには「<strong>ていく</strong>」を使います。",
        trap_en="① With 今まで ('up to now'), use てきた, never ていく. "
                "② With これから ('from now on'), use ていく, not てくる. "
                "③ Movement away from the speaker takes ていく; movement toward the speaker takes てくる.",
        contrast=[
            dict(type="wrong", sentence="これからもずっとこの{町|まち}に{住|す}んでくるつもりです。",
                 reason_ja="「これからも（未来へ向かって）」継続することには、「てくる」ではなく「ていく」を使います。",
                 reason_en="For continuation from now into the future (これからも), use ていく, not てくる."),
            dict(type="correct", sentence="これからもずっとこの{町|まち}に{住|す}んでいくつもりです。",
                 reason_ja="現在から未来へ動作を続けていく意志を表すので「住んでいく」が正解です。",
                 reason_en="住んでいくつもりです correctly projects continuation from the present into the future."),
            dict(type="correct", sentence="11{月|がつ}になって、だんだん{夜|よる}が{長|なが}くなっていきます。",
                 reason_ja="これから先に向かって変化が進んでいく様子を「〜なっていく」で表します。",
                 reason_en="なっていきます describes a gradual change progressing onward from now."),
        ],
        comparison=[
            dict(form="Vて ＋ いく", form_en="go on doing / change into future / move away", badge="現在→未来・遠ざかる", badge_type="good",
                 nuance_ja="今から未来へ向かう変化・継続や、話し手から遠ざかる移動を表します。",
                 nuance_en="Progression from now into the future, or movement away from the speaker.",
                 example="これからも{日本語|にほんご}を{勉強|べんきょう}していきます。"),
            dict(form="Vて ＋ くる", form_en="have been doing / come to do / approach", badge="過去→現在・近づく", badge_type="both",
                 nuance_ja="過去から現在までの継続・変化や、話し手に近づく移動、変化の始まりを表します。",
                 nuance_en="Continuation from the past up to now, movement toward the speaker, or onset of change.",
                 example="{高校|こうこう}のときから{日本語|にほんご}を{勉強|べんきょう}してきました。"),
            dict(form="Vて ＋ しまう", form_en="finish completely / end up doing", badge="完了・残念", badge_type="neutral",
                 nuance_ja="動作が完全に終わることや、残念な結果になったことを表します。",
                 nuance_en="Expresses complete finishing or an unintended/regrettable outcome.",
                 example="お{菓子|かし}を{全部|ぜんぶ}{食|た}べてしまいました。"),
        ],
    ),
    quiz=[
        dict(stem="{日本|にほん}では、これから{少子化|しょうしか}がもっと（　　　）と{言|い}われています。",
             correct="{進|すす}んでいく", distractors=["{進|すす}んでくる", "{進|すす}みいく", "{進|すす}んでおく"],
             en="In Japan, it is said that the declining birthrate will progress even further from now on.",
             notes_ja="「これから（未来へ向かって）」変化が進むことを表すので、「て形＋いく（進んでいく）」が正解です。",
             notes_en="With これから ('from now on'), use ていく (進んでいく) to describe a trend continuing into the future."),
        dict(stem="{パーティー}には、{私|わたし}が{作|つく}ったサンドイッチを（　　　）つもりです。",
             correct="{持|も}っていく", distractors=["{持|も}ってくる", "{持|も}ちいく", "{持|も}っておく"],
             en="I plan to take the sandwiches I made to the party.",
             notes_ja="サンドイッチを持ってパーティー会場へ「行く」ので、「持っていく」が正解です。",
             notes_en="Taking sandwiches and going to the party venue uses 持っていく."),
        dict(stem="{帽子|ぼうし}が{強|つよ}い{風|かぜ}で、{向|む}こうの{川|かわ}の{方|ほう}へ（　　　）しまいました。",
             correct="{飛|と}んでいって", distractors=["{飛|と}んできて", "{飛|と}びいって", "{飛|と}んであって"],
             en="My hat flew away toward the river over there in the strong wind.",
             notes_ja="「向こうの川の{方|ほう}へ」話し手から離れて遠ざかっていったので、「飛んでいって（しまいました）」を使います。",
             notes_en="Moving away from the speaker toward 'over there' (向こうの方へ) requires 飛んでいって."),
        dict(stem="どんなに{難|むずか}しくても、{夢|ゆめ}のためにこれからも{努力|どりょく}を（　　　）たいです。",
             correct="{続|つづ}けていき", distractors=["{続|つづ}けてき", "{続|つづ}きいき", "{続|つづ}けてあり"],
             en="No matter how difficult it is, I want to keep making efforts for my dream from now on too.",
             notes_ja="「これからも」未来に向かって努力を継続したいので、「続けていきたい」が正解です。",
             notes_en="With これからも ('from now on as well'), use 続けていきたい to express continuing into the future."),
    ],
)

# ---------------------------------------------------------------- 52 てくる
GRAMMAR[52] = dict(
    name="てくる", reading="てくる",
    meaning_en="come to do ~; start doing ~; continue up to now",
    similar="ていく、はじめる、だす",
    details=dict(
        formula="<strong>動詞て形 ＋ くる（／きます・きました）</strong><br>"
                "① <strong>移動（こちらへ近づく）</strong>：{走|はし}ってくる、{帰|かえ}ってくる<br>"
                "② <strong>行って何かをして戻る</strong>：ちょっと{買|か}ってくる、{手|て}を{洗|あら}ってくる<br>"
                "③ <strong>変化の始まり（出現）</strong>：{雨|あめ}が{降|ふ}ってきた、おなかが{空|す}いてきた<br>"
                "④ <strong>過去から現在までの継続</strong>：ずっと{守|まも}ってきた、10{年|ねん}{働|はたら}いてきた",
        notes_ja="「くる」には、話し手のいる場所や現在に向かって近づいてくるイメージがあり、4つの大切な使い{方|かた}があります。<br>"
                 "①<strong>こちらへ近づく移動</strong>：{向|む}こうから{犬|いぬ}が<strong>{走|はし}ってきました</strong>。<br>"
                 "②<strong>（どこかへ行って）〜してここへ戻る</strong>：ちょっとコンビニでお{弁当|べんとう}を<strong>{買|か}ってきます</strong>。<br>"
                 "③<strong>変化の始まり（〜し始める・だんだん〜なる）</strong>：あ、{雨|あめ}が<strong>{降|ふ}ってきました</strong>。／だんだん{暖|あたた}かく<strong>なってきました</strong>。<br>"
                 "④<strong>過去から現在までの継続</strong>：{私|わたし}はこれまで{一生懸命|いっしょうけんめい}<strong>{練習|れんしゅう}してきました</strong>。",
        notes_en="Combines a て-form verb with くる to express movement toward the speaker/present or the emergence of a new state: "
                 "(1) Approaching the speaker: 犬が走ってきた ('a dog came running toward me'); "
                 "(2) Going somewhere to do an action and coming back: ちょっと飲み物を買ってきます ('I'll go buy a drink and be right back'); "
                 "(3) Onset of a change/sensation: 雨が降ってきた ('it started raining'), 眠くなってきた ('I've started getting sleepy'); "
                 "(4) Continuation from the past up to the present: 今までずっと頑張ってきた ('I've worked hard up to now').",
        nuance_ja="特に会話で毎日使うのが②「ちょっと〜てきます（行ってすぐ戻ります）」と、③「雨が降ってきた／おなかが{空|す}いてきた／わかってきた（新しい状態や感覚が現れた）」の用法です。",
        nuance_en="Usages (2) 'go do ~ and come right back' (ちょっと手を洗ってきます) and (3) 'a natural change or bodily sensation has begun' (雨が降ってきた, 頭が痛くなってきた) are indispensable in daily conversation.",
        trap_ja="①「これから未来へ」続くことには「てくる」ではなく「<strong>ていく</strong>」を使います。<br>"
                "②「ちょっと買ってきます」は「買って（ここへ）戻ってきます」という意味で、自分が今いる場所に戻る前提のときに使います。<br>"
                "③補助動詞の「くる」は漢字「来る」ではなく、ひらがな「<strong>てくる</strong>」で書きます。",
        trap_en="① For continuation into the future (これから), use ていく, not てくる. "
                "② ちょっと〜てきます implies you will go do the action and return to the current spot. "
                "③ Write the subsidiary verb くる in hiragana.",
        contrast=[
            dict(type="wrong", sentence="{子供|こども}のころから{今|いま}まで、ずっとピアノを{習|なら}っていきました。",
                 reason_ja="「子供のころから今まで（過去→現在）」の継続には「ていく」ではなく「てくる」を使います。",
                 reason_en="For continuation from childhood up to the present (今まで), use てきました, not ていきました."),
            dict(type="correct", sentence="{子供|こども}のころから{今|いま}まで、ずっとピアノを{習|なら}ってきました。",
                 reason_ja="過去から現在までの継続は「〜てきました」で表します。",
                 reason_en="習ってきました correctly expresses an action continuing from the past up to now."),
            dict(type="correct", sentence="{空|そら}が{暗|くら}くなって、{冷|つめ}たい{風|かぜ}が{吹|ふ}いてきました。",
                 reason_ja="自然現象や感覚が新しく始まったことを「〜てきました」で表します。",
                 reason_en="吹いてきました naturally expresses the onset of a physical/natural phenomenon."),
        ],
        comparison=[
            dict(form="Vて ＋ くる（変化・出現）", form_en="start to / come to be", badge="変化の始まり", badge_type="good",
                 nuance_ja="自然現象（雨が降ってきた）や、体の感覚（おなかが{空|す}いてきた）、理解（わかってきた）が現れたときに使います。",
                 nuance_en="Used when natural phenomena, bodily sensations, or gradual understanding emerge.",
                 example="だんだん{日本語|にほんご}の{会話|かいわ}がわかってきました。"),
            dict(form="Vて ＋ くる（行って戻る）", form_en="go do ~ and come back", badge="往復", badge_type="both",
                 nuance_ja="「ちょっと〜して（ここへ）戻ってきます」という日常の外出・移動に使います。",
                 nuance_en="Go somewhere, perform the action, and return to the starting place.",
                 example="ちょっと{郵便局|ゆうびんきょく}で{切手|きって}を{買|か}ってきます。"),
            dict(form="Vて ＋ いく", form_en="continue into the future / move away", badge="現在→未来", badge_type="neutral",
                 nuance_ja="現在から未来に向かって続くこと、または話し手から離れていく移動を表します。",
                 nuance_en="Continuation from now into the future, or movement away from the speaker.",
                 example="これからもっと{暑|あつ}くなっていくでしょう。"),
        ],
    ),
    quiz=[
        dict(stem="ここで{少|すこ}し{待|ま}っていてください。ちょっと売店で{飲|の}み{物|もの}を（　　　）から。",
             correct="{買|か}ってきます", distractors=["{買|か}っていきます", "{買|か}いきます", "{買|か}っておきます"],
             en="Please wait here for a moment. I'll go buy some drinks at the kiosk and be right back.",
             notes_ja="相手を待たせて「行って買って、ここへ戻ってくる」場面なので「買ってきます」が正解です。",
             notes_en="Going to buy something and returning to where the listener is waiting requires 買ってきます."),
        dict(stem="{朝|あさ}から{何|なに}も{食|た}べていないので、だんだんおなかが（　　　）。",
             correct="{空|す}いてきました", distractors=["{空|す}いていきました", "{空|す}ききました", "{空|す}いておきました"],
             en="Since I haven't eaten anything since morning, I've gradually started getting hungry.",
             notes_ja="体の感覚や状態の変化が始まって現在に至ることを表すので、「{空|す}いてきました」が正解です。",
             notes_en="For the gradual onset of a physical sensation up to the present ('have gotten hungry'), use {空|す}いてきました."),
        dict(stem="この{伝統的|でんとうてき}な{祭|まつ}りは、{昔|むかし}から{町|まち}の{人|ひと}たちによってずっと（　　　）。",
             correct="{守|まも}られてきました", distractors=["{守|まも}られていきました", "{守|まも}りきました", "{守|まも}られておきました"],
             en="This traditional festival has been protected by the townspeople since long ago.",
             notes_ja="「昔から（現在まで）ずっと」続いてきたことを表すので、「守られてきました」が正解です。",
             notes_en="For something passed down continuously from the past (昔から) up to now, use 守られてきました."),
        dict(stem="あ、ポツポツと{雨|あめ}が（　　　）よ。{早|はや}く{洗濯物|せんたくもの}を{入|い}れましょう。",
             correct="{降|ふ}ってきました", distractors=["{降|ふ}っていきました", "{降|ふ}りきました", "{降|ふ}ってありました"],
             en="Oh, it's started raining in drops. Let's bring the laundry inside quickly.",
             notes_ja="雨が降り始めた（出現した）ことを表すには「降ってきました」を使います。",
             notes_en="To express that rain has just started falling, use 降ってきました."),
    ],
)

# ---------------------------------------------------------------- 53 方（かた）
GRAMMAR[53] = dict(
    name="方（かた）", reading="かた",
    meaning_en="way of doing ~; how to ~",
    similar="どうやって、方法、ように",
    details=dict(
        formula="<strong>動詞ます形 ＋ {方|かた}</strong>（{書|か}き{方|かた}、{読|よ}み{方|かた}、{使|つか}い{方|かた}、{作|つく}り{方|かた}）<br>"
                "<strong>サ変動詞の漢字 ＋ の ＋ し{方|かた}</strong>（{予約|よやく}のし{方|かた}、{洗濯|せんたく}のし{方|かた}）<br>"
                "<strong>「来ます」→ {来|き}{方|かた}</strong>（ほとんど使わず「{行|い}き{方|かた}」を使う）<br>"
                "※前の助詞「を・へ・が」はすべて「<strong>の</strong>」に変わる（料理<strong>を</strong>作る → {料理|りょうり}<strong>の</strong>{作|つく}り{方|かた}）",
        notes_ja="動詞のます形に「{方|かた}」を付けると、「〜する方法（どうやって〜するか）」という<strong>名詞</strong>になります。<br>"
                 "例：この{漢字|かんじ}の<strong>{読|よ}み{方|かた}</strong>を{教|おし}えてください。<br>"
                 "例：{新|あたら}しいコピー{機|き}の<strong>{使|つか}い{方|かた}</strong>がわかりません。<br>"
                 "「〜する」の動詞（予約する・勉強する・掃除する）は、「×予約し{方|かた}」ではなく「<strong>{予約|よやく}のし{方|かた}</strong>」のように「の」を入れます。<br>"
                 "また、「〜{方|かた}」全体が1つの名詞になるので、前の言葉は「を・へ・が」ではなく助詞「<strong>の</strong>」でつなぎます（{駅|えき}へ{行|い}く → {駅|えき}<strong>への／の</strong>{行|い}き{方|かた}）。",
        notes_en="Attaching 方 (かた) to a verb's ます-stem turns it into a noun meaning 'the way of doing ~ / how to ~'. "
                 "Because the resulting word is a noun, the object or target before it takes the particle の instead of を or が (漢字を読む → 漢字の読み{方|かた}). "
                 "For suru-verbs (予約する, 料理する), insert の before し方: 予約のし{方|かた}, 料理のし方.",
        nuance_ja="単に「どうやって〜しますか」と手順を聞くだけでなく、「あの人の<strong>話し{方|かた}</strong>はやさしい」「<strong>歩き{方|かた}</strong>が父に似ている」のように、その人の<strong>やり方の様子・癖・スタイル</strong>を表すときにもよく使われます。",
        nuance_en="Besides asking 'how to do something' (使い{方|かた}を教えてください), 〜方 also describes someone's manner, style, or habit of doing something (話し{方|かた}が丁寧だ 'their way of speaking is polite').",
        trap_ja="①「名詞＋を＋〜{方|かた}」とは言えません。助詞は必ず「<strong>の</strong>」に変えます（×箸を使い{方|かた} → ○お{箸|はし}<strong>の</strong>{使|つか}い{方|かた}）。<br>"
                "②サ変動詞は「<strong>Nのし{方|かた}</strong>」にします（×勉強し{方|かた} → ○{勉強|べんきょう}<strong>の</strong>し{方|かた}）。<br>"
                "③辞書形には付きません（×読む{方|かた} → ○<strong>{読|よ}み{方|かた}</strong>）。※「読むほう」になると比較の意味になります。",
        trap_en="① Change を to の before a 〜方 noun: ○お箸の使い{方|かた} (×お箸を使い{方|かた}). "
                "② For suru-verbs, use N + の + し方: ○掃除のし方 (×掃除し方). "
                "③ Always attach 方 (かた) to the ます-stem, never the dictionary form.",
        contrast=[
            dict(type="wrong", sentence="すみません、この{券売機|けんばいき}で{切符|きっぷ}を{買|か}い{方|かた}がわかりません。",
                 reason_ja="「買い{方|かた}」は名詞なので、前の「切符」には「を」ではなく「の」を付けます。",
                 reason_en="Since 買い{方|かた} is a noun, it cannot take the direct object particle を; use の instead."),
            dict(type="correct", sentence="すみません、この{券売機|けんばいき}での{切符|きっぷ}の{買|か}い{方|かた}がわかりません。",
                 reason_ja="「名詞＋の＋ます形＋{方|かた}」で「切符の買い{方|かた}」になります。",
                 reason_en="切符の買い{方|かた} correctly connects the noun with の."),
            dict(type="correct", sentence="インターネットでのホテルの{予約|よやく}のし{方|かた}を{教|おし}えてもらいました。",
                 reason_ja="「予約する」は「予約のし{方|かた}」の形にします。",
                 reason_en="For the suru-verb 予約する, use 予約のし{方|かた}."),
        ],
        comparison=[
            dict(form="Nの ＋ Vます形 ＋ {方|かた}", form_en="how to do / way of doing", badge="名詞化", badge_type="good",
                 nuance_ja="「〜する方法」や「〜する様子・スタイル」を1つの名詞として表します。",
                 nuance_en="Turns 'how to do ~' or 'manner of doing ~' into a noun phrase.",
                 example="おいしいケーキの{作|つく}り{方|かた}を{習|なら}いました。"),
            dict(form="どうやって ＋ Vますか", form_en="how do you do ~?", badge="疑問副詞", badge_type="both",
                 nuance_ja="動詞の文のまま「どのような方法で〜しますか」と質問するときに使います。",
                 nuance_en="Asks 'how / by what means' directly with a verb predicate.",
                 example="このケーキはどうやって{作|つく}りますか。"),
            dict(form="V辞書形 ＋ {方|ほう}がいい", form_en="had better / comparably ~", badge="比較・助言", badge_type="neutral",
                 nuance_ja="辞書形やた形の後ろに「{方|ほう}」が付くと、読み{方|かた}は「ほう」になり、比較や助言を表します。",
                 nuance_en="After plain verb forms, 方 is read ほう and expresses comparison or advice.",
                 example="{早|はや}く{寝|ね}た{方|ほう}がいいですよ。"),
        ],
    ),
    quiz=[
        dict(stem="すみません、ここから{市民病院|しみんびょういん}までの（　　　）を{教|おし}えていただけませんか。",
             correct="{行|い}き{方|かた}", distractors=["{行|い}く{方|かた}", "{行|い}いた{方|かた}", "{行|い}って{方|かた}"],
             en="Excuse me, could you tell me how to get to the City Hospital from here?",
             notes_ja="「行く方法」を表すには、ます形「行き」＋「{方|かた}」で「行き方」にします。",
             notes_en="Attach 方 (かた) to the ます-stem of 行く → 行き方 ('how to get to')."),
        dict(stem="{祖母|そぼ}に、おいしくて{簡単|かんたん}なお{味噌汁|みそしる}（　　　）を{教|おし}えてもらいました。",
             correct="の{作|つく}り{方|かた}", distractors=["を{作|つく}り{方|かた}", "の{作|つく}る{方|かた}", "を{作|つく}る{方|かた}"],
             en="I had my grandmother teach me how to make delicious and easy miso soup.",
             notes_ja="「作り{方|かた}」は名詞なので、前の「お味噌汁」とは「を」ではなく「の」でつなぎ、「お味噌汁の作り{方|かた}」にします。",
             notes_en="Since 作り{方|かた} is a noun, link the preceding object with の (お味噌汁の作り{方|かた}), never を."),
        dict(stem="このアプリでの{飛行機の切符|ひこうきのきっぷ}の（　　　）がわからないので、{手伝|てつだ}ってください。",
             correct="{予約|よやく}のし{方|かた}", distractors=["{予約|よやく}し{方|かた}", "{予約|よやく}する{方|かた}", "{予約|よやく}を{方|かた}"],
             en="I don't know how to book a plane ticket on this app, so please help me.",
             notes_ja="Ⅲグループ（する動詞）の「予約する」を「〜{方|かた}」にするときは、「の」を入れて「予約のし{方|かた}」にします。",
             notes_en="For suru-verbs like 予約する, insert の before し方 → 予約のし{方|かた}."),
        dict(stem="{鈴木|すずき}さんはいつも{丁寧|ていねい}で、お客さまとの（　　　）がとても{上手|じょうず}です。",
             correct="{話|はな}し{方|かた}", distractors=["{話|はな}す{方|かた}", "{話|はな}して{方|かた}", "{話|はな}した{方|かた}"],
             en="Ms. Suzuki is always polite and very good at the way she speaks with customers.",
             notes_ja="「話す様子・スキル」を表す名詞は、ます形「話し」＋「{方|かた}」の「話し{方|かた}」です。",
             notes_en="Use Verb-masu stem + 方 (話し{方|かた}) to refer to someone's manner or skill of speaking."),
    ],
)

# ---------------------------------------------------------------- 54 始める
GRAMMAR[54] = dict(
    name="始める", reading="はじめる",
    meaning_en="start doing ~",
    similar="出す、てくる、ようになる",
    details=dict(
        formula="<strong>動詞ます形 ＋ {始|はじ}める（／{始|はじ}めました）</strong><br>"
                "例：{読|よ}み{始|はじ}める、{習|なら}い{始|はじ}める、{降|ふ}り{始|はじ}める、{作|つく}り{始|はじ}める",
        notes_ja="継続する動作や習慣、自然現象などが「スタートする（始まる）」ことを表す複合動詞です。<br>"
                 "例：{私|わたし}は{去年|きょねん}から{日本語|にほんご}を<strong>{習|なら}い{始|はじ}めました</strong>。<br>"
                 "例：さっきから{雪|ゆき}が<strong>{降|ふ}り{始|はじ}めました</strong>。<br>"
                 "例：8{時|じ}になったので、みんなが{テスト|てすと}の{問題|もんだい}を<strong>{解|と}き{始|はじ}めました</strong>。<br>"
                 "後ろの「始める」はⅡグループ（一段）動詞なので、「始めます・始めない・始めた」と活用します。",
        notes_en="Attach 始める to the ます-stem of a verb to mean 'start doing ~ / begin to ~'. "
                 "Used both for intentional actions/habits (日本語を習い始めた) and for natural processes (雨が降り始めた). "
                 "As a compound verb, it conjugates as a Group 2 verb (始めます, 始めない, 始めた).",
        nuance_ja="<strong>★「〜始める」と「〜出す」の違い</strong>：<br>"
                  "・<strong>〜始める</strong>：予定していたことや、自然な流れで始まることに落ち着いて使えます（勉強し始める・春になって花が咲き始める）。<br>"
                  "・<strong>〜出す</strong>：予想していなかったことが<strong>急に・突然</strong>始まるときに使います（赤ちゃんが急に泣き出した・突然走り出した）。",
        nuance_en="Difference between 始める and 出す: "
                  "〜始める describes a normal, planned, or expected beginning (本を読み始めた). "
                  "〜出す emphasizes a sudden, unexpected, or impulsive outburst (急に泣き出した, 突然笑い出した).",
        trap_ja="①て形や辞書形ではなく、必ず<strong>ます形</strong>に付けます（×読んで始める → ○<strong>{読|よ}み{始|はじ}める</strong>）。<br>"
                "②「始める」は他動詞の形ですが、複合動詞「〜始める」になると、「雨が降り始める」「花が咲き始める」のように自動詞にも付きます（×降り始まる とは言いません！）。<br>"
                "③一瞬で終わる動詞（着く・起きる・見つける）には原則として付きません。",
        trap_en="① Attach 始める to the ます-stem, never the て-form or dictionary form (読み始める). "
                "② Even when the first verb is intransitive (雨が降る, 花が咲く), the compound always uses 始める (降り始める, 咲き始める), NEVER ×降り始まる! "
                "③ Cannot attach to punctual verbs that finish in a single instant (like 着く or 起きる) unless plural subjects do it one after another.",
        contrast=[
            dict(type="wrong", sentence="3{月|がつ}のおわりごろから、{桜|さくら}の{花|はな}が{咲|さ}き{始|はじ}まりました。",
                 reason_ja="複合動詞では、前が自動詞「咲く」でも後ろは「始まる」ではなく「始める」を使います。",
                 reason_en="In verb compounds, always use 始める (咲き始めました), never ×咲き始まりました."),
            dict(type="correct", sentence="3{月|がつ}のおわりごろから、{桜|さくら}の{花|はな}が{咲|さ}き{始|はじ}めました。",
                 reason_ja="「ます形（咲き）＋始めました」で正しい複合動詞になります。",
                 reason_en="咲き始めました is the correct compound verb form."),
            dict(type="correct", sentence="{健康|けんこう}のために、{先週|せんしゅう}から{毎朝|まいあさ}{走|はし}り{始|はじ}めました。",
                 reason_ja="新しい習慣をスタートしたことを「走り始めました」で表します。",
                 reason_en="走り始めました naturally expresses starting a new daily habit."),
        ],
        comparison=[
            dict(form="Vます形 ＋ {始|はじ}める", form_en="start doing (normal/planned)", badge="開始・習慣", badge_type="good",
                 nuance_ja="予定していた動作や新しい習慣、季節の変化などが普通に始まるときに使います。",
                 nuance_en="Normal, planned, or gradual start of an action, habit, or seasonal change.",
                 example="{息子|むすこ}は3{歳|さい}からピアノを{習|なら}い{始|はじ}めました。"),
            dict(form="Vます形 ＋ {出|だ}す", form_en="suddenly start / burst out", badge="突然・予想外", badge_type="both",
                 nuance_ja="急に・突然・思いがけず動作や現象が始まったときに使います。",
                 nuance_en="Sudden, unexpected onset or emotional outburst.",
                 example="{空|そら}が{急|きゅう}に{暗|くら}くなって、{大粒|おおつぶ}の{雨|あめ}が{降|ふ}り{出|だ}しました。"),
            dict(form="Vて ＋ くる", form_en="begin to / come to (toward speaker)", badge="感覚・出現", badge_type="neutral",
                 nuance_ja="おなかが{空|す}いてきた・わかってきたなど、感覚や変化がじわじわ現れるときに使います。",
                 nuance_en="Gradual emergence of a bodily sensation or change reaching the speaker.",
                 example="だんだん{眠|ねむ}くなってきました。"),
        ],
    ),
    quiz=[
        dict(stem="{弟|おとうと}は、{来月|らいげつ}の{試合|しあい}のために{毎日|まいにち}プールで（　　　）。",
             correct="{泳|およ}ぎ{始|はじ}めました", distractors=["{泳|およ}いで{始|はじ}めました", "{泳|およ}ぎ{始|はじ}まりました", "{泳|およ}ぐ{始|はじ}めました"],
             en="My younger brother has started swimming in the pool every day for next month's match.",
             notes_ja="動詞のます形「泳ぎ」＋「始めました」が正解です。て形や辞書形には付かず、「泳ぎ始まりました」とも言いません。",
             notes_en="Attach 始めました to the ます-stem (泳ぎ始めました). Never use て-form or 始まりました."),
        dict(stem="{暖|あたた}かくなって、{庭|にわ}のチューリップが{少|すこ}しずつ（　　　）。",
             correct="{咲|さ}き{始|はじ}めました", distractors=["{咲|さ}き{始|はじ}まりました", "{咲|さ}いて{始|はじ}めました", "{咲|さ}き{出|だ}せました"],
             en="It has gotten warmer, and the tulips in the garden have gradually started blooming.",
             notes_ja="前が自動詞「咲く」でも、複合動詞は必ず「咲き始めました」になります。「咲き始まりました」はよくある間違いです。",
             notes_en="Even with intransitive 咲く, the compound verb is always 咲き始めました (never ×咲き始まりました)."),
        dict(stem="A：その{小説|しょうせつ}はおもしろいですか。<br>B：きのう（　　　）ばかりなので、まだわかりません。",
             correct="{読|よ}み{始|はじ}めた", distractors=["{読|よ}んで{始|はじ}めた", "{読|よ}む{始|はじ}めた", "{読|よ}み{始|はじ}まった"],
             en="A: Is that novel interesting? B: Since I only just started reading it yesterday, I don't know yet.",
             notes_ja="ます形「読み」＋「始めた（ばかり）」で「読み始めたばかり」となります。",
             notes_en="Combine the ます-stem 読み with 始めた (+ ばかり) → 読み始めたばかり."),
        dict(stem="このデパートは、{朝|あさ}10{時|じ}になるとお{客|きゃく}さんがたくさん（　　　）。",
             correct="{入|はい}り{始|はじ}めます", distractors=["{入|はい}り{始|はじ}まります", "{入|はい}って{始|はじ}めます", "{入|はい}る{始|はじ}めます"],
             en="At this department store, when 10 AM comes, customers start coming in in large numbers.",
             notes_ja="次々にお客さんが入る動作が始まるので、ます形「入り」＋「始めます」が正解です。",
             notes_en="When many people start entering one after another, use 入り始めます."),
    ],
)

# ---------------------------------------------------------------- 55 終わる
GRAMMAR[55] = dict(
    name="終わる", reading="おわる",
    meaning_en="finish doing ~",
    similar="てしまう、おえる、たところだ",
    details=dict(
        formula="<strong>動詞ます形 ＋ {終|お}わる（／{終|お}わりました）</strong><br>"
                "例：{読|よ}み{終|お}わる、{食|た}べ{終|お}わる、{書|か}き{終|お}わる、{使|つか}い{終|お}わる",
        notes_ja="ある量やまとまりのある動作（本を読む・食事を食べる・レポートを書くなど）が、最後まで終わることを表します。<br>"
                 "例：この{本|ほん}を<strong>{読|よ}み{終|お}わったら</strong>、{貸|か}してください。<br>"
                 "例：やっと{夏休|なつやす}みの{宿題|しゅくだい}を<strong>{書|か}き{終|お}わりました</strong>。<br>"
                 "例：パソコンを<strong>{使|つか}い{終|お}わったら</strong>、{電源|でんげん}を{切|き}ってください。<br>"
                 "後ろの「終わる」はⅠグループ（五段）動詞なので、「終わります・終わらない・終わった・終われば」と活用します。",
        notes_en="Attach 終わる to the ます-stem of an action verb to mean 'finish doing ~'. "
                 "Used for actions that have a natural endpoint or quantity to complete (reading a book, eating a meal, writing a report, using a tool). "
                 "Conjugates as a Group 1 verb (終わります, 終わらない, 終わった).",
        nuance_ja="「〜終わる」と似た言葉に「〜終える」がありますが、日常会話では「<strong>〜終わる</strong>」が圧倒的によく使われます（食べ終わる・読み終わる）。"
                  "また、「〜てしまう」は「全部食べてしまった（残念・完了）」のように感情や勢いが入りますが、「〜終わる」は客観的に「動作の最後まで終わった」ことを表します。",
        nuance_en="While 〜終える is a more formal literary equivalent, 〜終わる is standard in everyday speech. "
                  "Unlike 〜てしまう (which can imply regret or doing something in one go), 〜終わる neutrally states that an activity has reached its completion.",
        trap_ja="①て形ではなく、必ず<strong>ます形</strong>に付けます（×食べて終わる → ○<strong>{食|た}べ{終|お}わる</strong>）。<br>"
                "②意志のない自然現象には使えません（×雨が降り終わった → ○{雨|あめ}が<strong>やんだ</strong>）。<br>"
                "③一瞬で終わる動詞（起きる・着く・落ちる・壊れる）には付きません。",
        trap_en="① Attach 終わる to the ます-stem, never the て-form (○食べ終わる, ×食べて終わる). "
                "② Do not use it for weather/natural phenomena: say 雨がやんだ ('the rain stopped'), NOT ×雨が降り終わった. "
                "③ Cannot attach to instantaneous verbs like 着く or 壊れる.",
        contrast=[
            dict(type="wrong", sentence="お{昼|ひる}ごはんを{食|た}べて{終|お}わったら、{散歩|さんぽ}に{行|い}きましょう。",
                 reason_ja="「終わる」の前はて形ではなく、ます形「食べ」にします。",
                 reason_en="終わる attaches to the ます-stem (食べ), not the て-form (食べて)."),
            dict(type="correct", sentence="お{昼|ひる}ごはんを{食|た}べ{終|お}わったら、{散歩|さんぽ}に{行|い}きましょう。",
                 reason_ja="ます形「食べ」＋「終わったら」で正しい形になります。",
                 reason_en="食べ終わったら correctly attaches 終わる to the ます-stem."),
            dict(type="correct", sentence="{借|か}りていたDVDをすべて{見|み}終わったので、{店|みせ}に{返|かえ}しました。",
                 reason_ja="ます形が1文字の動詞「見る（み）」にもそのまま「見終わる」と付けられます。",
                 reason_en="Even 1-mora stems like 見 (from 見る) attach directly: 見終わった."),
        ],
        comparison=[
            dict(form="Vます形 ＋ {終|お}わる", form_en="finish doing ~", badge="完了・客観", badge_type="good",
                 nuance_ja="食事・読書・作業など、あるまとまりのある動作が最後まで完了したことを表します。",
                 nuance_en="Neutrally states that a bounded activity (reading, eating, working) is finished.",
                 example="{晩|ばん}ごはんを{食|た}べ{終|お}わりました。"),
            dict(form="Vて ＋ しまう", form_en="finish completely / end up doing", badge="完了・心理", badge_type="both",
                 nuance_ja="すっかり完了したことや、「うっかり〜してしまった」という後悔・残念な気持ちを表します。",
                 nuance_en="Emphasizes total completion or regret over an unintended action.",
                 example="ケーキを{全部|ぜんぶ}{食|た}べてしまいました。"),
            dict(form="Vた ＋ ところだ", form_en="just finished (moments ago)", badge="直後の時点", badge_type="neutral",
                 nuance_ja="終わった「直後のタイミング」に焦点を当てる表現です（「食べ終わったところです」と組み合わせることも多い）。",
                 nuance_en="Focuses on the timing ('just moments ago'); often combined as 食べ終わったところだ.",
                 example="たった{今|いま}、{掃除|そうじ}をしたところです。"),
        ],
    ),
    quiz=[
        dict(stem="その{雑誌|ざっし}を（　　　）、{次|つぎ}に{私|わたし}にも{見|み}せてくださいね。",
             correct="{読|よ}み{終|お}わったら", distractors=["{読|よ}んで{終|お}わったら", "{読|よ}む{終|お}わったら", "{読|よ}み{終|お}わると"],
             en="When you finish reading that magazine, please show it to me next.",
             notes_ja="ます形「読み」＋「終わる」で、後ろに依頼「見せてくださいね」が続くので「たら」の形「読み終わったら」が正解です。",
             notes_en="Use ます-stem 読み + 終わったら (since the main clause is a request, と cannot be used)."),
        dict(stem="ハサミを（　　　）あとは、かならず{元|もと}の{引|ひ}き{出|だ}しに{戻|もど}してください。",
             correct="{使|つか}い{終|お}わった", distractors=["{使|つか}って{終|お}わった", "{使|つか}う{終|お}わった", "{使|つか}い{終|お}わるの"],
             en="After you finish using the scissors, please always put them back in the original drawer.",
             notes_ja="「あと」につながる過去形（た形）で、ます形「使い」＋「終わった」の「使い終わった」が正解です。",
             notes_en="Before あと, use the past plain form of 使い終わる → 使い終わった."),
        dict(stem="3{時間|じかん}かかって、ようやく{長|なが}いレポートを{最後|さいご}まで（　　　）。",
             correct="{書|か}き{終|お}わりました", distractors=["{書|か}いて{終|お}わりました", "{書|か}く{終|お}わりました", "{書|か}き{始|はじ}まりました"],
             en="Taking three hours, I finally finished writing the long report all the way to the end.",
             notes_ja="「最後まで」とあるので、完了を表す「ます形（書き）＋終わりました」が正解です。",
             notes_en="With 最後まで ('to the very end'), use 書き終わりました ('finished writing')."),
        dict(stem="お{皿|さら}をすべて（　　　）から、リビングでゆっくりお{茶|ちゃ}を{飲|の}みました。",
             correct="{洗|あら}い{終|お}わって", distractors=["{洗|あら}って{終|お}わって", "{洗|あら}우{終|お}わって", "{洗|あら}い{終|お}わるて"],
             en="After finishing washing all the dishes, I relaxed and drank tea in the living room.",
             notes_ja="「〜てから」の前なので、ます形「洗い」＋「終わる」のて形「洗い終わって（から）」が正解です。",
             notes_en="Before から ('after doing ~'), use the て-form of 洗い終わる → 洗い終わってから."),
    ],
)

# ---------------------------------------------------------------- 56 続ける
GRAMMAR[56] = dict(
    name="続ける", reading="つづける",
    meaning_en="continue doing ~",
    similar="ている、ていく、っぱなし",
    details=dict(
        formula="<strong>動詞ます形 ＋ {続|つづ}ける（／{続|つづ}けました）</strong><br>"
                "例：{歩|ある}き{続|つづ}ける、{降|ふ}り{続|つづ}ける、{考|かんが}え{続|つづ}ける、{働|はたら}き{続|つづ}ける",
        notes_ja="同じ動作や状態を、途中でやめずにずっと繰り返したり継続したりすることを表します。<br>"
                 "例：3{時間|じかん}も<strong>{歩|ある}き{続|つづ}けた</strong>ので、{足|あし}が{痛|いた}くなりました。<br>"
                 "例：きのうから{雨|あめ}が<strong>{降|ふ}り{続|つづ}いています</strong>。<br>"
                 "例：あきらめないで<strong>{頑張|がんば}り{続|つづ}ければ</strong>、きっと{夢|ゆめ}はかないます。<br>"
                 "後ろの「続ける」はⅡグループ（一段）動詞なので、「続けます・続けない・続けた・続けて」と活用します。",
        notes_en="Attach 続ける to the ます-stem of a verb to mean 'continue doing ~ / keep on doing ~ without stopping'. "
                 "Works for both intentional human actions (歩き続けた, 練習し続ける) and continuous natural events (雨が降り続いている). "
                 "Conjugates as a Group 2 verb (続けます, 続けない, 続けた).",
        nuance_ja="単に「歩いている」「雨が降っている」と言うよりも、「休まずに・長い間ずっとその動作を途切れさせない」という<strong>持続の長さ・根気強さ</strong>が強調されます。",
        nuance_en="Compared to simple 〜ている, 〜続ける emphasizes the unbroken duration, persistence, or intensity of keeping an action going over time.",
        trap_ja="①て形ではなく、必ず<strong>ます形</strong>に付けます（×歩いて続ける → ○<strong>{歩|ある}き{続|つづ}ける</strong>）。<br>"
                "②前が自動詞（雨が降る・風が吹く）のときも、複合動詞では「×降り続く」ではなく「<strong>{降|ふ}り{続|つづ}ける</strong>」を使うのが一般的です。<br>"
                "③一瞬で終わる動詞（壊れる・着く・見つける）には付きません。",
        trap_en="① Attach 続ける to the ます-stem, never the て-form (○歩き続ける, ×歩いて続ける). "
                "② Even with intransitive verbs like 降る, use 降り続ける (降り続いています) rather than ×降り続く. "
                "③ Only attaches to verbs that can last over a period of time.",
        contrast=[
            dict(type="wrong", sentence="きのうの{夜|よる}から、{雪|ゆき}が{降|ふ}って{続|つづ}いています。",
                 reason_ja="複合動詞「〜続ける」の前は、て形ではなくます形「降り」にします。",
                 reason_en="Use the ます-stem 降り before 続ける, not the て-form 降って."),
            dict(type="correct", sentence="きのうの{夜|よる}から、{雪|ゆき}が{降|ふ}り{続|つづ}いています。",
                 reason_ja="ます形「降り」＋「続けています」で「ずっとやまずに降っている」ことを表します。",
                 reason_en="降り続けています naturally expresses that snow has kept falling non-stop."),
            dict(type="correct", sentence="{彼女|かのじょ}は10{年間|ねんかん}、{毎日|まいにち}{日記|にっき}を{書|か}き{続|つづ}けています。",
                 reason_ja="長い期間やめずに習慣を継続していることを「書き続けています」で表します。",
                 reason_en="書き続けています highlights keeping up a daily habit over ten years."),
        ],
        comparison=[
            dict(form="Vます形 ＋ {続|つづ}ける", form_en="keep on doing non-stop", badge="持続の強調", badge_type="good",
                 nuance_ja="途中で休んだりやめたりせず、ずっと同じ動作や状態を続けることを強調します。",
                 nuance_en="Emphasizes keeping an action or state going without stopping or quitting.",
                 example="{選手|せんしゅ}たちは{最後|さいご}まで{走|はし}り{続|つづ}けました。"),
            dict(form="Vて ＋ いく／くる", form_en="continue into future / up to now", badge="時間軸の方向", badge_type="both",
                 nuance_ja="過去から現在まで（てきた）、または現在から未来へ（ていく）という時間の流れを表します。",
                 nuance_en="Focuses on the directional timeline (past-to-now vs. now-to-future).",
                 example="これからもこの{伝統|でんとう}を{守|まも}っていきます。"),
            dict(form="Vます形 ＋ っぱなし", form_en="leave ~ on/open (neglect)", badge="放置・不満", badge_type="neutral",
                 nuance_ja="「テレビをつけっぱなしにする」のように、本来消したり片付けたりすべきものを放置する意味です。",
                 nuance_en="Means leaving something in an improper state (e.g., leaving the TV on or door open).",
                 example="テレビをつけっぱなしで{寝|ね}てしまいました。"),
        ],
    ),
    quiz=[
        dict(stem="{満員電車|まんいんでんしゃ}の{中|なか}で1{時間|じかん}ずっと（　　　）ので、{足|あし}がすっかり{疲|つか}れました。",
             correct="{立|た}ち{続|つづ}けた", distractors=["{立|た}って{続|つづ}けた", "{立|た}つ{続|つづ}けた", "{立|た}ち{続|つづ}いた"],
             en="Because I kept standing for a whole hour inside the packed train, my legs got completely tired.",
             notes_ja="「立つ」のます形「立ち」＋「続けた」で、1時間ずっと立ったままだったことを表します。",
             notes_en="Combine the ます-stem 立ち with 続けた → 立ち続けた ('kept standing')."),
        dict(stem="{台風|たいふう}のせいで、おとといから{強|つよ}い{風|かぜ}が（　　　）います。",
             correct="{吹|ふ}き{続|つづ}けて", distractors=["{吹|ふ}いて{続|つづ}けて", "{吹|ふ}く{続|つづ}けて", "{吹|ふ}き{続|つづ}いて"],
             en="Because of the typhoon, strong winds have kept blowing since the day before yesterday.",
             notes_ja="ます形「吹き」＋「続けています」で、強い風がやまずに続いている様子を表します。",
             notes_en="Use ます-stem 吹き + 続けています to show the wind has kept blowing continuously."),
        dict(stem="どんなに{失敗|しっぱい}しても、あきらめないで（　　　）ことが{大切|たいせつ}です。",
             correct="{挑戦|ちょうせん}し{続|つづ}ける", distractors=["{挑戦|ちょうせん}して{続|つづ}ける", "{挑戦|ちょうせん}する{続|つづ}ける", "{挑戦|ちょうせん}し{続|つづ}く"],
             en="No matter how many times you fail, it is important to keep challenging yourself without giving up.",
             notes_ja="Ⅲグループ「挑戦する」のます形「挑戦し」＋「続ける」で「挑戦し続ける」になります。",
             notes_en="Attach 続ける to the ます-stem of 挑戦する → 挑戦し続ける."),
        dict(stem="ステージの{上|うえ}で2{時間|じかん}も（　　　）あの{歌手|かしゅ}は、{本当|ほんとう}にすごいと{思|おも}います。",
             correct="{歌|うた}い{続|つづ}ける", distractors=["{歌|うた}って{続|つづ}ける", "{歌|うた}う{続|つづ}ける", "{歌|うた}い{続|つづ}く"],
             en="I think that singer who keeps singing on stage for two whole hours is truly amazing.",
             notes_ja="ます形「歌い」＋「続ける」で「歌い続ける」が正解です。",
             notes_en="Combine the ます-stem 歌い with 続ける → 歌い続ける."),
    ],
)

# ---------------------------------------------------------------- 57 直す
GRAMMAR[57] = dict(
    name="直す", reading="なおす",
    meaning_en="redo; do ~ over again",
    similar="もう一度〜する、てみる、替える",
    details=dict(
        formula="<strong>動詞ます形 ＋ {直|なお}す（／{直|なお}しました）</strong><br>"
                "例：{書|か}き{直|なお}す、{考|かんが}え{直|なお}す、やり{直|なお}す、{読|よ}み{直|なお}す、{買|か}い{直|なお}す",
        notes_ja="一度やったことがうまくいかなかったり、間違いがあったりしたときに、「もう一度最初からやり直す（より良い状態にする）」ことを表します。<br>"
                 "例：{字|じ}を{間違|まちが}えたので、もう{一度|いちど}<strong>{書|か}き{直|なお}しました</strong>。<br>"
                 "例：{計画|けいかく}に{無理|むり}がないか、もう{少|すこ}し<strong>{考|かんが}え{直|なお}して</strong>みましょう。<br>"
                 "例：{サイズ}が{合|あ}わなかったので、{靴|くつ}を<strong>{買|か}い{直|なお}しました</strong>。<br>"
                 "後ろの「直す」はⅠグループ（五段）動詞なので、「直します・直さない・直した・直せば」と活用します。",
        notes_en="Attach 直す to the ます-stem of a verb to mean 'do ~ over again / redo ~ (to fix a mistake or get a better result)'. "
                 "Common examples include 書き直す (rewrite), やり直す (do over), 考え直す (reconsider), 読み直す (reread), and かけ直す (call back). "
                 "Conjugates as a Group 1 verb (直します, 直さない, 直した).",
        nuance_ja="単に2回目をやるのではなく、「1回目に不{十分|じゅうぶん}な点やミスがあったから、<strong>正しく／もっと良くするために</strong>もう一度する」というニュアンスがあります。"
                  "電話がつながらなくて「あとで<strong>かけ直します</strong>」という表現も非常によく使われます。",
        nuance_en="Implies not merely repeating an action, but redoing it in order to correct a flaw, improve the result, or try again after an unsuccessful attempt (such as 電話をかけ直す 'call back later').",
        trap_ja="①て形ではなく、必ず<strong>ます形</strong>に付けます（×書いて直す → ○<strong>{書|か}き{直|なお}す</strong>）。<br>"
                "②「直す」の使役受身は、「す」で終わる動詞なので短縮形がなく「<strong>〜{直|なお}させられる</strong>」になります。<br>"
                "③自分の意志でやり直せない自然現象には使えません（×雨が降り直す）。",
        trap_en="① Attach 直す to the ます-stem, never the て-form (○書き直す, ×書いて直す). "
                "② Since 直す ends in す, its causative-passive is 直させられる (not ×直される). "
                "③ Only attaches to volitional actions that a person can redo.",
        contrast=[
            dict(type="wrong", sentence="テストの{答|こた}えを{間違|まちが}えたので、消しゴムで{消|け}して{書|か}いて{直|なお}しました。",
                 reason_ja="複合動詞「〜直す」の前は、て形ではなくます形「書き」にします。",
                 reason_en="Before 直す, use the ます-stem 書き, not the て-form 書いて."),
            dict(type="correct", sentence="テストの{答|こた}えを{間違|まちが}えたので、消しゴムで{消|け}して{書|か}き{直|なお}しました。",
                 reason_ja="ます形「書き」＋「直しました」で「もう一度正しく書いた」という意味になります。",
                 reason_en="書き直しました correctly expresses rewriting the answer."),
            dict(type="correct", sentence="{今|いま}は{忙|いそが}しそうですから、あとで{電話|でんわ}をかけ{直|なお}します。",
                 reason_ja="電話をもう一度かけることは「かけ直す」と言います。",
                 reason_en="かけ直します is the natural idiomatic expression for calling back later."),
        ],
        comparison=[
            dict(form="Vます形 ＋ {直|なお}す", form_en="redo / do over to improve", badge="やり直し・改善", badge_type="good",
                 nuance_ja="うまくいかなかったことや間違えたことを、もう一度最初からやり直すときに使います。",
                 nuance_en="Redoing an action to correct a mistake or get a better outcome.",
                 example="もう{一度|いちど}{最初|さいしょ}からやり{直|なお}しましょう。"),
            dict(form="Vます形 ＋ {替|か}える", form_en="replace / switch to another", badge="別の物に交換", badge_type="both",
                 nuance_ja="「乗り換える・着替える・買い替える」のように、今までとは別の物に変えるときに使います。",
                 nuance_en="Switching from one thing to a different one (changing trains, changing clothes).",
                 example="{古|ふる}い{冷蔵庫|れいぞうこ}を{新|あたら}しいものに{買|か}い{替|か}えました。"),
            dict(form="Vて ＋ みる", form_en="try doing ~", badge="試し", badge_type="neutral",
                 nuance_ja="結果がどうなるかわからないことを、試しにやってみるときに使います（「考え直してみる」と組み合わせることも多い）。",
                 nuance_en="Doing something as a trial to see what happens.",
                 example="もう{一度|いちど}{話|はな}してみます。"),
        ],
    ),
    quiz=[
        dict(stem="{作|つく}ったスープの{味|あじ}が{薄|うす}かったので、{塩|しお}を{入|い}れて{味|あじ}を（　　　）。",
             correct="{調|ととの}え{直|なお}しました", distractors=["{調|ととの}えて{直|なお}しました", "{調|ととの}える{直|なお}しました", "{調|ととの}え{続|つづ}けました"],
             en="Because the soup I made tasted weak, I added salt and readjusted the seasoning.",
             notes_ja="一度作った味をもう一度調整して良くしたので、ます形「調え」＋「直しました」が正解です。",
             notes_en="Readjusting the flavor to improve it uses ます-stem + 直しました (調え直しました)."),
        dict(stem="{彼|かれ}の{意見|いけん}を{聞|き}いて、{自分|じぶん}の{計画|けいかく}をもう{一度|いちど}（　　　）ことにしました。",
             correct="{考|かんが}え{直|なお}す", distractors=["{考|かんが}えて{直|なお}す", "{考|かんが}える{直|なお}す", "{考|かんが}え{始|はじ}まる"],
             en="After hearing his opinion, I decided to reconsider my plan once more.",
             notes_ja="「もう一度考えて改める」という意味なので、ます形「考え」＋「直す」の「考え直す」が正解です。",
             notes_en="'Reconsider / think over again' is expressed by 考え直す."),
        dict(stem="{写真|しゃしん}が{暗|くら}く{写|うつ}ってしまったので、{明|あか}るい{場所|ばしょ}でもう{一枚|いちまい}（　　　）。",
             correct="{撮|と}り{直|なお}しました", distractors=["{撮|と}って{直|なお}しました", "{撮|と}る{直|なお}しました", "{撮|と}り{終|お}わりました"],
             en="Because the photo came out dark, I retook another one in a bright place.",
             notes_ja="うまく撮れなかったのでもう一度撮影した場面には、ます形「撮り」＋「直しました」を使います。",
             notes_en="Retaking a photo because the first one was too dark uses 撮り直しました."),
        dict(stem="{並|なら}べた{本|ほん}の{順番|じゅんばん}がバラバラだったので、{番号順|ばんごうじゅん}に（　　　）。",
             correct="{並|なら}べ{直|なお}しました", distractors=["{並|なら}べて{直|なお}しました", "{並|なら}べる{直|なお}しました", "{並|なら}べ{出|だ}しました"],
             en="Because the order of the lined-up books was mixed up, I rearranged them in numerical order.",
             notes_ja="正しい順番でもう一度並べたので、ます形「並べ」＋「直しました」が正解です。",
             notes_en="Rearranging the books into the proper order uses 並べ直しました."),
    ],
)

# ---------------------------------------------------------------- 58 出す
GRAMMAR[58] = dict(
    name="出す", reading="だす",
    meaning_en="suddenly start doing ~; burst out ~",
    similar="始める、てくる、てしまう",
    details=dict(
        formula="<strong>動詞ます形 ＋ {出|だ}す（／{出|だ}しました）</strong><br>"
                "例：{泣|な}き{出|だ}す、{笑|わら}い{出|だ}す、{走|はし}り{出|だ}す、{降|ふ}り{出|だ}す、{飛|と}び{出|だ}す",
        notes_ja="今までしていなかった動作や自然現象が、<strong>急に・突然・思いがけず始まる</strong>ことを表します。<br>"
                 "例：{赤|あか}ちゃんが{急|きゅう}に{大|おお}きな{声|こえ}で<strong>{泣|な}き{出|だ}しました</strong>。<br>"
                 "例：{彼|かれ}の{冗談|じょうだん}を{聞|き}いて、みんながいっせいに<strong>{笑|わら}い{出|だ}しました</strong>。<br>"
                 "例：{傘|かさ}を{持|も}っていないのに、{突然|とつぜん}{雨|あめ}が<strong>{降|ふ}り{出|だ}しました</strong>。<br>"
                 "※また、「カバンから財布を<strong>{取|と}り{出|だ}す</strong>」「{部屋|へや}から<strong>{飛|と}び{出|だ}す</strong>」のように、「中から外へ出る／出す」という元の意味でも使われます。",
        notes_en="Attach 出す to the ます-stem of a verb to express two main meanings: "
                 "(1) Suddenly or unexpectedly start doing ~ / burst out doing ~ (急に泣き出した, 笑い出した, 雨が降り出した, 走り出した); "
                 "(2) Move or take something from inside to outside (カバンから取り出す, 部屋から飛び出す). "
                 "Conjugates as a Group 1 verb (出します, 出さない, 出した).",
        nuance_ja="「〜始める」との一番の違いは、<strong>「急に・突然」という驚きや勢い</strong>があることです。"
                  "そのため、計画的に始める習慣（×来月から日本語を習い出します）や、自分の意志で「さあ、〜出そう！」と勧誘する文（×そろそろ食べ出しましょう）には使えません（→「{習|なら}い{始|はじ}めます」「{食|た}べ{始|はじ}めましょう」を使います）。",
        nuance_en="Unlike 〜始める, 〜出す carries a strong nuance of suddenness, spontaneity, or surprise. "
                  "Therefore, it CANNOT be used for planned habits (×来月から勉強し出す) or volitional invitations (×さあ、食べ出しましょう → use 食べ始めましょう).",
        trap_ja="①て形ではなく、必ず<strong>ます形</strong>に付けます（×泣いて出した → ○<strong>{泣|な}き{出|だ}した</strong>）。<br>"
                "②計画的な予定や「〜ましょう」「〜てください」には「〜出す」ではなく「<strong>〜{始|はじ}める</strong>」を使います。<br>"
                "③副詞「{急|きゅう}に」「{突然|とつぜん}」とセットで使われることがとても多いです。",
        trap_en="① Attach 出す to the ます-stem, never the て-form (○泣き出した, ×泣いて出した). "
                "② Do not use 〜出す for planned actions, requests (〜てください), or invitations (〜ましょう); use 〜始める instead. "
                "③ Frequently pairs with adverbs like 急に or 突然.",
        contrast=[
            dict(type="wrong", sentence="{時間|じかん}になりましたから、どうぞ{試験|しけん}の{問題|もんだい}を{書|か}き{出|だ}してください。",
                 reason_ja="予定された開始や「〜てください」の依頼には「〜出す」は使えません（別の意味「抜き出して書く」になってしまいます）。",
                 reason_en="For a scheduled start or request (〜てください), use 書き始めてください, not 書き出す."),
            dict(type="correct", sentence="{時間|じかん}になりましたから、どうぞ{試験|しけん}の{問題|もんだい}を{書|か}き{始|はじ}めてください。",
                 reason_ja="予定通りの開始には「〜始める」を使います。",
                 reason_en="Use 書き始めてください for starting a scheduled activity."),
            dict(type="correct", sentence="{犬|いぬ}が{急|きゅう}に{向|む}こうへ{走|はし}り{出|だ}したので、びっくりしました。",
                 reason_ja="「急に〜した」という予想外の飛び出し・開始には「走り出した」がぴったりです。",
                 reason_en="急に走り出した naturally captures the dog suddenly bolting off."),
        ],
        comparison=[
            dict(form="Vます形 ＋ {出|だ}す", form_en="suddenly start / burst out", badge="突然・衝動", badge_type="good",
                 nuance_ja="「急に・突然」思いがけず動作や現象が始まったとき（泣き出す・笑い出す・降り出す）に使います。",
                 nuance_en="Sudden, unexpected onset or emotional outburst.",
                 example="{赤|あか}ちゃんが{急|きゅう}に{泣|な}き{出|だ}しました。"),
            dict(form="Vます形 ＋ {始|はじ}める", form_en="start doing (planned/normal)", badge="予定・通常開始", badge_type="both",
                 nuance_ja="予定していたことや習慣、季節の変化などが普通に始まるときに使います。",
                 nuance_en="Planned, deliberate, or gradual beginning.",
                 example="{来週|らいしゅう}から{新|あたら}しい{仕事|しごと}をし{始|はじ}めます。"),
            dict(form="Vます形 ＋ {出|だ}す（中→外）", form_en="take out / jump out", badge="中から外へ", badge_type="neutral",
                 nuance_ja="ポケットから取り出す、家から飛び出すなど、中から外への移動を表します。",
                 nuance_en="Physical movement from inside to outside.",
                 example="カバンから{手帳|てちょう}を{取|と}り{出|だ}しました。"),
        ],
    ),
    quiz=[
        dict(stem="{静|しず}かな{図書館|としょかん}の{中|なか}で、{隣|となり}の{人|ひと}が{急|きゅう}に（　　　）ので驚きました。",
             correct="{歌|うた}い{出|だ}した", distractors=["{歌|うた}って{出|だ}した", "{歌|うた}う{出|だ}した", "{歌|うた}い{終|お}わった"],
             en="Inside the quiet library, the person next to me suddenly started singing, which surprised me.",
             notes_ja="「急に〜ので驚きました」とあるので、突然動作が始まる「ます形（歌い）＋出した」が正解です。",
             notes_en="急に...驚きました signals a sudden, unexpected outburst: 歌い出した."),
        dict(stem="さっきまでいい{天気|てんき}だったのに、{突然|とつぜん}{強|つよ}い{雨|あめ}が（　　　）。",
             correct="{降|ふ}り{出|だ}しました", distractors=["{降|ふ}って{出|だ}しました", "{降|ふ}る{出|だ}しました", "{降|ふ}り{直|なお}しました"],
             en="Even though the weather was nice until a moment ago, heavy rain suddenly started falling.",
             notes_ja="「突然」雨が降り始めた場面なので、ます形「降り」＋「出しました」を使います。",
             notes_en="For sudden, unexpected rain (突然), use 降り出しました."),
        dict(stem="ポケットの{中|なか}から{小銭|こぜに}を（　　　）、{自動販売機|じどうはんばいき}に{入|い}れました。",
             correct="{取|と}り{出|だ}して", distractors=["{取|と}って{出|だ}して", "{取|と}る{出|だ}して", "{取|と}り{始|はじ}めて"],
             en="I took small change out of my pocket and put it into the vending machine.",
             notes_ja="中（ポケット）から外へ出す動作を表す複合動詞「ます形（取り）＋出して」が正解です。",
             notes_en="Taking something out from inside a pocket or bag is 取り出す → 取り出して."),
        dict(stem="{友|とも}だちの{顔|かお}を{見|み}た{瞬間|しゅんかん}、おかしくなって思わず（　　　）しまいました。",
             correct="{笑|わら}い{出|だ}して", distractors=["{笑|わら}って{出|だ}して", "{笑|わら}う{出|だ}して", "{笑|わら}い{直|なお}して"],
             en="The moment I saw my friend's face, it was so funny that I couldn't help bursting out laughing.",
             notes_ja="「思わず（急に）笑い始めた」という感情の吹き出しには、ます形「笑い」＋「出して」を使います。",
             notes_en="Bursting out laughing involuntarily uses 笑い出して."),
    ],
)

# ---------------------------------------------------------------- 59 ばかり
GRAMMAR[59] = dict(
    name="ばかり", reading="ばかり",
    meaning_en="only ~; nothing but ~",
    similar="だけ、しか〜ない、たばかり",
    details=dict(
        formula="<strong>名詞 ＋ ばかり ＋ 動詞</strong>（お{菓子|かし}ばかり{食|た}べる、ゲームばかりする）<br>"
                "<strong>動詞て形 ＋ ばかりいる</strong>（{寝|ね}てばかりいる、{遊|あそ}んでばかりいる）<br>"
                "※助詞「を・が」は省略して直接「ばかり」を付ける（「に・で・と」は残ることが多い）",
        notes_ja="他にもやるべきことや選択肢があるのに、<strong>同じ物や同じ動作ばかりを何度も繰り返す（そればっかりだ）</strong>ことを表します。<br>"
                 "①<strong>名詞 ＋ ばかり</strong>：<br>"
                 "例：{弟|おとうと}は{野菜|やさい}を{食|た}べないで、<strong>お{肉|にく}ばかり</strong>{食|た}べています。<br>"
                 "②<strong>動詞て形 ＋ ばかりいる</strong>：<br>"
                 "例：{休|やす}みの{日|ひ}は、{一日|いちにち}{中|じゅう}<strong>{寝|ね}てばかりいます</strong>。<br>"
                 "例：うちの{子|こ}は{勉強|べんきょう}しないで、<strong>{遊|あそ}んでばかりいます</strong>。",
        notes_en="Expresses that someone repeatedly chooses the same thing or keeps doing the same action to the exclusion of everything else ('nothing but ~ / always doing ~'). "
                 "(1) Noun + ばかり (replaces を/が): 甘い物ばかり食べる ('eat nothing but sweets'). "
                 "(2) Verb て-form + ばかりいる: 遊んでばかりいる ('do nothing but play').",
        nuance_ja="<strong>★「だけ」と「ばかり」の違い</strong>：<br>"
                  "・<strong>だけ</strong>：客観的に数量や範囲を限定します（今日はリンゴを<strong>1つだけ</strong>食べた）。<br>"
                  "・<strong>ばかり</strong>：「何回もそればっかり繰り返している」という偏りを表し、多くの場合、話し手の<strong>不満・あきれ・注意</strong>の気持ちが含まれます（あの人はいつも文句<strong>ばかり</strong>言っている）。",
        nuance_en="Difference between だけ and ばかり: "
                  "だけ neutrally limits a quantity or single choice (水を1杯だけ飲んだ). "
                  "ばかり implies repeated, unbalanced behavior ('always doing X and nothing else') and often carries a critical or exasperated tone.",
        trap_ja="①「名詞＋を／が」の「を・が」は消えます（×肉をばかり食べる → ○{肉|にく}<strong>ばかり</strong>{食|た}べる）。<br>"
                "②「て形＋ばかり」は後ろに「<strong>いる（います）</strong>」を伴って「〜てばかりいる」の形で使います。<br>"
                "③「1つばかり」「1回ばかり」のような1回きりの数量限定には「<strong>だけ</strong>」を使います（「た形＋ばかり」は『たった今〜した』という別の文法です）。",
        trap_en="① Drop を and が before ばかり (○甘い物ばかり食べる, ×甘い物をばかり食べる). "
                "② With a て-form verb, follow ばかり with いる: 寝てばかりいる. "
                "③ Remember that Verb-た + ばかり means 'just did ~', whereas Verb-て + ばかりいる means 'do nothing but ~'.",
        contrast=[
            dict(type="wrong", sentence="お{菓子|かし}をばかり{食|た}べていると、おなかがいっぱいになりますよ。",
                 reason_ja="「ばかり」の前に目的語の助詞「を」は付けません。",
                 reason_en="Drop the object particle を when attaching ばかり to a noun."),
            dict(type="correct", sentence="お{菓子|かし}ばかり{食|た}べていると、おなかがいっぱいになりますよ。",
                 reason_ja="「お菓子を」の「を」を取って「お菓子ばかり」にします。",
                 reason_en="お菓子ばかり correctly replaces を with ばかり."),
            dict(type="correct", sentence="スマホを{見|み}てばかりいないで、{早|はや}く{宿題|しゅくだい}をしなさい。",
                 reason_ja="「て形＋ばかりいないで」で「そればかり続けるのをやめなさい」と注意する自然な表現になります。",
                 reason_en="Verb-て + ばかりいないで naturally scolds someone for doing nothing but that action."),
        ],
        comparison=[
            dict(form="Nばかり ／ Vてばかりいる", form_en="nothing but / keep doing only ~", badge="反復・偏り", badge_type="good",
                 nuance_ja="同じことばかり何度も繰り返している（偏っている）ことを表し、注意や不満によく使います。",
                 nuance_en="Repeatedly doing or choosing the same thing; often expresses criticism.",
                 example="ゲームをしてばかりいないで、{外|そと}で{運動|うんどう}しなさい。"),
            dict(form="Nだけ", form_en="only / just (objective limit)", badge="客観的限定", badge_type="both",
                 nuance_ja="感情を含まず、数や範囲が「それだけ」であることを客観的に表します。",
                 nuance_en="Neutrally states an objective limit or quantity.",
                 example="{今日|きょう}は{午前中|ごぜんちゅう}だけ{仕事|しごと}があります。"),
            dict(form="Vた ＋ ばかりだ", form_en="just finished doing ~", badge="完了直後", badge_type="neutral",
                 nuance_ja="た形に付くと「終わってからまだ時間が経っていない」というまったく別の意味になります。",
                 nuance_en="After the た-form, ばかり means 'just finished doing ~'.",
                 example="さっき{昼|ひる}ごはんを{食|た}べたばかりです。"),
        ],
    ),
    quiz=[
        dict(stem="{弟|おとうと}は{毎日|まいにち}、{部屋|へや}でマンガを（　　　）いて、ちっとも{勉強|べんきょう}しません。",
             correct="{読|よ}んでばかり", distractors=["{読|よ}んだばかり", "{読|よ}むだけ", "{読|よ}みばかり"],
             en="My younger brother does nothing but read manga in his room every day and doesn't study at all.",
             notes_ja="後ろに「いて（います）」があり、「いつもそればかり繰り返している」と不満を述べる文なので「て形＋ばかり（読んでばかり）」が正解です。「読んだばかり」には「いて」が続きません。",
             notes_en="Followed by いて and expressing criticism of repeated behavior, use Verb-て + ばかりいて (読んでばかりいて)."),
        dict(stem="{健康|けんこう}に{良|よ}くないですから、{甘|あま}いジュース（　　　）{飲|の}むのはやめましょう。",
             correct="ばかり", distractors=["をばかり", "たばかり", "しか"],
             en="Because it's not good for your health, let's stop drinking nothing but sweet juice.",
             notes_ja="名詞「ジュース」に直接「ばかり」を付けて、偏って飲むことを表します。「をばかり」は誤りで、「しか」の後ろは否定形になります。",
             notes_en="Attach ばかり directly to the noun (ジュースばかり), dropping を. (しか requires a negative verb.)"),
        dict(stem="このごろ{週末|しゅうまつ}になると{雨|あめ}（　　　）{降|ふ}って、どこへも{出|で}かけられません。",
             correct="ばかり", distractors=["がばかり", "たばかり", "しか"],
             en="Lately, whenever the weekend comes, it does nothing but rain, so I can't go out anywhere.",
             notes_ja="「雨が」の「が」を省略して「雨ばかり降って」とすることで、毎週末繰り返される雨への不満を表します。",
             notes_en="Replace が with ばかり (雨ばかり降って) to complain that it rains every single weekend."),
        dict(stem="そんなにお{金|かね}を（　　　）いると、すぐに{貯金|ちょきん}がなくなってしまいますよ。",
             correct="{使|つか}ってばかり", distractors=["{使|つか}ったばかり", "{使|つか}いばかり", "{使|つか}うだけ"],
             en="If you keep doing nothing but spending money like that, your savings will run out right away.",
             notes_ja="「〜てばかりいると」の形を作るので、て形＋ばかりの「使ってばかり」が正解です。",
             notes_en="Before いると, use Verb-て + ばかり → 使ってばかりいると ('if you keep just spending money')."),
    ],
)

# ---------------------------------------------------------------- 60 受身（持ち主・迷惑の受身）
GRAMMAR[60] = dict(
    name="受身（持ち主・迷惑の受身）", reading="うけみ",
    meaning_en="possessor / adversative passive (have one's ~ done; suffer from ~)",
    similar="られる（直接受身）、てしまう、させられる",
    details=dict(
        formula="① <strong>持ち主の受身</strong>：<strong>私（持ち主）は ＋ 相手 に ＋ 自分の物／体 を ＋ 動詞受身形</strong><br>"
                "　例：{私|わたし}は{隣|となり}の{人|ひと}<strong>に</strong><strong>{足|あし}を{踏|ふ}まれました</strong>。<br>"
                "② <strong>迷惑の受身（自動詞の受身）</strong>：<strong>私は ＋ 人／雨 に ＋ 自動詞の受身形</strong><br>"
                "　例：{私|わたし}は{帰|かえ}り{道|みち}で<strong>{雨|あめ}に{降|ふ}られました</strong>。",
        notes_ja="日本語でとてもよく使われる、<strong>被害・迷惑（困った気持ち）</strong>を表す2種類の受身です。<br>"
                 "①<strong>持ち主の受身</strong>：自分の体の一部（足・頭・手）や、自分の持ち物（靴・カバン・日記・ケーキ）に何かをされて困ったとき、「私の足が踏まれた」ではなく「<strong>{私|わたし}は</strong>{足|あし}<strong>を</strong>{踏|ふ}まれた」と<strong>持ち主（私）を主語</strong>にします。<br>"
                 "例：{弟|おとうと}<strong>に</strong>{私|わたし}のプリン<strong>を</strong><strong>{食|た}べられました</strong>。<br>"
                 "②<strong>自動詞の迷惑受身</strong>：英語にはない日本語独特の受身で、「雨が降る」「赤ちゃんが泣く」「客が来る」などの自動詞を受身にして「それで私が困った」ことを表します。<br>"
                 "例：{夜中|よなか}に{赤|あか}ちゃん<strong>に</strong><strong>{泣|な}かれて</strong>、{眠|ねむ}れませんでした。",
        notes_en="Two distinctively Japanese passive patterns that express suffering inconvenience or trouble (adversative passive): "
                 "(1) Possessor passive: When someone does something to a part of your body or your possession, 'I' (the owner) becomes the topic (は), the doer takes に, and your body part/possession takes を: 私は犬に手をかまれた ('I had my hand bitten by a dog'). "
                 "(2) Indirect/Intransitive passive: Even intransitive verbs like 降る, 泣く, or 来る can be made passive to show that the speaker was inconvenienced by the event: 雨に降られた ('I got caught in the rain').",
        nuance_ja="英語などでは「私の財布が盗まれた（My wallet was stolen）」と物を主語にしますが、日本語では「<strong>（私は）</strong>財布<strong>を</strong>盗まれた」と被害を受けた人を主語にし、物を「を」で表すのが自然です。",
        nuance_en="Whereas English makes the object the subject ('My foot was stepped on', 'My wallet was stolen'), natural Japanese makes the person who suffered the trouble the subject/topic and marks the object with を: （私は）足を踏まれた / 財布を盗まれた.",
        trap_ja="①持ち主の受身では、自分の持ち物・体には「が」ではなく「<strong>を</strong>」を付けます（△私の足が踏まれた → ○（{私|わたし}は）{足|あし}<strong>を</strong>{踏|ふ}まれた）。<br>"
                "②動作をした人や原因（雨・犬・弟など）には必ず「<strong>に</strong>」を付けます（<strong>{雨|あめ}に</strong>{降|ふ}られた）。<br>"
                "③良いこと・ありがたいことには迷惑の受身は使えません（×母にケーキを作られた → ○{母|はは}がケーキを{作|つく}って<strong>くれた</strong>）。",
        trap_en="① Mark your affected possession or body part with を, not が: 足を踏まれた, カバンを汚された. "
                "② Mark the source of the trouble (the person, dog, or rain) with に: 雨に降られた. "
                "③ Never use this pattern when you are happy about the action (use てくれる / てもらう).",
        contrast=[
            dict(type="wrong", sentence="{満員電車|まんいんでんしゃ}で、{隣|となり}の{人|ひと}に{私|わたし}の{足|あし}が{踏|ふ}まれました。",
                 reason_ja="自分の体や持ち物が被害を受けたときは、持ち主（私）を主語にして「足を踏まれました」と言うのが自然です。",
                 reason_en="In Japanese, make the owner ('I') the topic and mark the body part with を: 足を踏まれました."),
            dict(type="correct", sentence="{満員電車|まんいんでんしゃ}で、{隣|となり}の{人|ひと}に{足|あし}を{踏|ふ}まれました。",
                 reason_ja="「（私は）隣の人に足を踏まれました」が自然な持ち主の受身です。",
                 reason_en="（私は）隣の人に足を踏まれました is the natural possessor passive."),
            dict(type="correct", sentence="{傘|かさ}を{持|も}っていなかったのに、{帰|かえ}りに{雨|あめ}に{降|ふ}られました。",
                 reason_ja="自動詞「降る」の受身「雨に降られる」で、雨のせいで濡れて困ったことを表します。",
                 reason_en="雨に降られました uses the intransitive passive to show you suffered from getting caught in the rain."),
        ],
        comparison=[
            dict(form="（私は）Bに Nを V（ら）れる", form_en="possessor passive (have one's N ~ed)", badge="持ち主の受身", badge_type="good",
                 nuance_ja="自分の体や持ち物（N）がBに何かされて迷惑を受けたときに使います。",
                 nuance_en="Used when your body part or possession N is affected by B.",
                 example="{冷蔵庫|れいぞうこ}のケーキを{妹|いもうと}に{食|た}べられました。"),
            dict(form="（私は）Bに 自動詞（ら）れる", form_en="adversative passive of intransitive verb", badge="迷惑の受身", badge_type="both",
                 nuance_ja="Bが勝手に何かをした（雨が降った・客が来た・泣いた）せいで自分が困ったときに使います。",
                 nuance_en="Used when B's intransitive action (raining, crying, leaving) causes trouble for you.",
                 example="{忙|いそが}しいときに{友|とも}だちに{来|こ}られて{困|こま}りました。"),
            dict(form="Bが（私に）Vてくれる", form_en="B kindly does ~ for me", badge="感謝・恩恵", badge_type="neutral",
                 nuance_ja="迷惑ではなく、相手が親切でしてくれたことには「〜てくれる／〜てもらう」を使います。",
                 nuance_en="When the action is helpful rather than troublesome, use てくれる / てもらう.",
                 example="{妹|いもうと}が{部屋|へや}を{掃除|そうじ}してくれました。"),
        ],
    ),
    quiz=[
        dict(stem="{バス}の{中|なか}で、{後|うし}ろの{人|ひと}に{新|あたら}しい{白い|しろい}{靴|くつ}を（　　　）しまいました。",
             correct="{踏|ふ}まれて", distractors=["{踏|ふ}ませて", "{踏|ふ}んでくれて", "{踏|ふ}みられて"],
             en="On the bus, I had my new white shoes stepped on by the person behind me.",
             notes_ja="自分の持ち物（白い靴を）が後ろの人に踏まれて被害を受けた「持ち主の受身」なので、Ⅰグループ「踏む（fumu）」の受身形「踏まれて」が正解です。",
             notes_en="Since your own shoes (白い靴を) were stepped on by the person behind you (後ろの人に), use the passive of Group 1 踏む → 踏まれて."),
        dict(stem="{大切|たいせつ}に{取|と}っておいたお{菓子|かし}を、{兄|あに}に{全部|ぜんぶ}（　　　）がっかりしました。",
             correct="{食|た}べられて", distractors=["{食|た}べさせて", "{食|た}べてくれて", "{食|た}べてもらって"],
             en="I was disappointed because I had all the sweets I had been saving carefully eaten by my older brother.",
             notes_ja="自分のお菓子を兄に食べられてがっかりした被害の受身なので、「食べられて」が正解です。",
             notes_en="Having your saved sweets eaten by your brother to your disappointment uses the possessor passive 食べられて."),
        dict(stem="{洗濯物|せんたくもの}を{外|そと}に{干|ほ}したまま{出|で}かけたら、{急|きゅう}に{雨|あめ}に（　　　）しまいました。",
             correct="{降|ふ}られて", distractors=["{降|ふ}らせて", "{降|ふ}ってくれて", "{降|ふ}りられて"],
             en="When I went out leaving the laundry hanging outside, I suddenly got hit by rain (and suffered for it).",
             notes_ja="自動詞「降る」の迷惑の受身「雨に降られる」の形「降られて」が正解です。",
             notes_en="Use the adversative passive of intransitive 降る → 雨に降られて ('suffered from it raining')."),
        dict(stem="{飛行機|ひこうき}の{中|なか}で、{隣|となり}の{席|せき}の{赤|あか}ちゃんにずっと（　　　）、{少|すこ}しも{寝|ね}られませんでした。",
             correct="{泣|な}かれて", distractors=["{泣|な}かせて", "{泣|な}いてくれて", "{泣|な}きられて"],
             en="On the plane, the baby in the next seat kept crying (to my trouble), so I couldn't sleep at all.",
             notes_ja="赤ちゃんが泣いたせいで私が眠れず困った「自動詞の迷惑受身」なので、Ⅰグループ「泣く（naku）」の受身形「泣かれて」が正解です。",
             notes_en="Suffering inconvenience because a baby kept crying uses the adversative passive of Group 1 泣く → 泣かれて."),
    ],
)

# ---------------------------------------------------------------- 61 使役＋授受（させてあげる・もらう・くれる）
GRAMMAR[61] = dict(
    name="使役＋授受（させてあげる・もらう・くれる）", reading="させてくれる",
    meaning_en="let me do ~ / kindly allow to do ~",
    similar="させる、てもらう、てくれる",
    details=dict(
        formula="<strong>動詞使役形のて形（〜させて／〜せて） ＋ あげる・もらう・くれる</strong><br>"
                "・<strong>〜させてくれる（／くださる）</strong>：（相手が私に）〜するのを許してくれる<br>"
                "・<strong>〜させてもらう（／いただく）</strong>：（私が相手に許しを得て）〜する<br>"
                "・<strong>〜させてあげる</strong>：（私が相手に）〜するのを許してあげる<br>"
                "★依頼：<strong>〜させてください／〜させていただけませんか</strong>（私に〜することを許してください）",
        notes_ja="使役形（〜させる＝やらせる・許可する）に「てあげる・てもらう・てくれる」を組み合わせた、日常会話やビジネスで超頻出の表現です。<br>"
                 "①<strong>〜させてくれる／くださる</strong>：周りの人が私の希望を聞いて、自由にやらせてくれる。<br>"
                 "例：{両親|りょうしん}は{私|わたし}に{好|す}きな{楽器|がっき}を<strong>{習|なら}わせてくれました</strong>。<br>"
                 "②<strong>〜させてもらう／いただく</strong>：相手の許可をもらって、自分が何かをする。<br>"
                 "例：{今日|きょう}は{少|すこ}し{早|はや}く<strong>{帰|かえ}らせていただきます</strong>。<br>"
                 "③<strong>〜させてください／〜させていただけませんか</strong>：「私が〜するのを許可してください」という丁寧なお願い。<br>"
                 "例：この{仕事|しごと}は、ぜひ{私|わたし}に<strong>やらせてください</strong>。",
        notes_en="Combines the causative て-form (〜させて / 〜せて) with giving/receiving verbs to express granting or receiving permission: "
                 "(1) 〜させてくれる / くださる: Someone kindly lets me do what I want (両親が留学させてくれた). "
                 "(2) 〜させてもらう / いただく: I have someone let me do ~ / I take the liberty of doing ~ (休ませていただきました). "
                 "(3) 〜させてください / 〜させていただけませんか: 'Please let me do ~ / Could you allow me to do ~?'",
        nuance_ja="<strong>★「〜てください」と「〜させてください」の違い（誰がするか！）</strong>：<br>"
                  "・<strong>{考|かんが}えてください</strong> ＝ <strong>あなたが</strong>考えてください（相手への依頼）。<br>"
                  "・<strong>{考|かんが}えさせてください</strong> ＝ <strong>私に</strong>考える時間をください・<strong>私が</strong>考えるのを許してください（許可の依頼）。",
        nuance_en="Crucial distinction between 〜てください and 〜させてください: "
                  "〜てください asks the LISTENER to do the action ('Please do ~'). "
                  "〜させてください asks the listener to allow the SPEAKER ('me') to do the action ('Please let me do ~').",
        trap_ja="①<strong>誰が動作をするのか</strong>を必ず確認しましょう。自分がやりたいときの許可のお願いは「<strong>〜させてください／〜させていただけませんか</strong>」です。<br>"
                "②Ⅰグループの使役て形は「<strong>〜せて</strong>」（行く→{行|い}かせて、買う→{買|か}わせて、休む→{休|やす}ませて）です。「×行きさせて」にしないよう注意！<br>"
                "③自分がすることを申し出るときに「×私が説明していただきます」とは言えません → 「{私|わたし}が{説明|せつめい}<strong>させていただきます</strong>」または「ご{説明|せつめい}いたします」にします。",
        trap_en="① Always check WHO performs the action: if 'I' want to do it with your permission, use 〜させてください / 〜させていただけませんか (not 〜てください). "
                "② Watch Group 1 causative forms: 休ませて, 行かせて, 買わせて (never ×休みさせて). "
                "③ When humble 'I' do the action with permission, use させていただきます (never ×していただきます, which means someone else does it for me).",
        contrast=[
            dict(type="wrong", sentence="{部長|ぶちょう}、きょうは{熱|ねつ}があるので、{私|わたし}は{早|はや}く{帰|かえ}っていただけませんか。",
                 reason_ja="「帰っていただけませんか」だと「部長が帰ってください」という意味になってしまいます。",
                 reason_en="帰っていただけませんか asks the manager to go home! To ask permission for yourself to go home, you need the causative."),
            dict(type="correct", sentence="{部長|ぶちょう}、きょうは{熱|ねつ}があるので、{早|はや}く{帰|かえ}らせていただけませんか。",
                 reason_ja="「（私が）帰るのを許可していただけませんか」なので、使役＋ていただくの「帰らせていただけませんか」にします。",
                 reason_en="帰らせていただけませんか correctly asks 'Could you let me go home early?'"),
            dict(type="correct", sentence="すぐには{決|き}められないので、もう{少|すこ}し{考|かんが}えさせてください。",
                 reason_ja="「私に考える時間をください（私が考えるのを許してください）」は「考えさせてください」で表します。",
                 reason_en="考えさせてください means 'Please let me think about it a little longer.'"),
        ],
        comparison=[
            dict(form="V（さ）せてください", form_en="please let me do ~", badge="自分がする許可", badge_type="good",
                 nuance_ja="話し手（私）が何かをすることについて、相手に許可やチャンスを求めるときに使います。",
                 nuance_en="Asks permission for the speaker ('me') to perform the action.",
                 example="ぜひ{私|わたし}にも{手伝|てつだ}わせてください。"),
            dict(form="Vてください", form_en="please do ~ (listener acts)", badge="相手がする依頼", badge_type="both",
                 nuance_ja="相手（あなた）にその動作をしてほしいと頼むときに使います。",
                 nuance_en="Asks the listener ('you') to perform the action.",
                 example="すみません、ちょっと{手伝|てつだ}ってください。"),
            dict(form="V（さ）せてくれる／くださる", form_en="kindly let me do ~", badge="許可への感謝", badge_type="neutral",
                 nuance_ja="親や先生・上司が、私のやりたいことを許してくれたときに感謝を込めて使います。",
                 nuance_en="Expresses gratitude that someone allowed you to do what you wanted.",
                 example="{父|ちち}は{私|わたし}を{日本|にほん}へ{留学|りゅうがく}させてくれました。"),
        ],
    ),
    quiz=[
        dict(stem="とても{大事|だいじ}なことなので、{家族|かぞく}と{相談|そうだん}してから（　　　）ください。",
             correct="{決|き}めさせて", distractors=["{決|き}めて", "{決|き}められて", "{決|き}まりて"],
             en="Because it is a very important matter, please let me decide after consulting with my family.",
             notes_ja="相談して決めるのは「私」なので、「私が決めるのを待って許してください」という意味の「決めさせてください」が正解です。「決めてください」だと相手に決めてもらう意味になります。",
             notes_en="Since 'I' am the one who will consult my family and decide, use 決めさせてください ('please let me decide')."),
        dict(stem="{体調|たいちょう}が{悪|わる}いので、すみませんが、{午後|ごご}の{授業|じゅぎょう}を（　　　）いただけませんか。",
             correct="{休|やす}ませて", distractors=["{休|やす}んで", "{休|やす}みさせて", "{休|やす}まれて"],
             en="Because I am feeling unwell, I'm sorry, but could you let me take the afternoon class off?",
             notes_ja="授業を休むのは「私」なので、許可を求める「休ませていただけませんか」が正解です。Ⅰグループ「休む」の使役て形は「休ませて」です。",
             notes_en="'I' am the one taking the class off, so ask for permission with Group 1 休む → 休ませていただけませんか."),
        dict(stem="{私|わたし}の{両親|りょうしん}は、{私|わたし}がやりたいと{言|い}ったことは{何|なん}でも（　　　）。",
             correct="やらせてくれました", distractors=["やらせてあげました", "やってあげました", "やらされました"],
             en="My parents kindly let me do whatever I said I wanted to do.",
             notes_ja="主語が「両親は」で、私にやりたいことを許可してくれたので、「やらせてくれました」が正解です。",
             notes_en="My parents (両親は) kindly allowed me to do what I wanted: やらせてくれました."),
        dict(stem="このたびのイベントの{結果|けっか}について、{私|わたし}からご（　　　）いただきます。",
             correct="{報告|ほうこく}させて", distractors=["{報告|ほうこく}して", "{報告|ほうこく}されて", "{報告|ほうこく}なさって"],
             en="Allow me to report on the results of this recent event.",
             notes_ja="「私から（私が）報告します」をへりくだって丁寧に言う表現は「ご報告させていただきます」です。「報告していただきます」は相手にしてもらう意味なので使えません。",
             notes_en="When 'I' (私から) humbly make the report, use ご報告させていただきます. (していただきます means having someone else do it.)"),
    ],
)

# ---------------------------------------------------------------- 62 ても（逆接の仮定）
GRAMMAR[62] = dict(
    name="ても（逆接の仮定）", reading="ても",
    meaning_en="even if ~; even though ~",
    similar="のに、けれども、たら",
    details=dict(
        formula="<strong>動詞て形 ＋ も</strong>（{行|い}っても、{食|た}べても、{聞|き}いても）<br>"
                "<strong>イ形容詞（〜い → 〜くても）</strong>（{高|たか}くても、{忙|いそが}しくても、よくても）<br>"
                "<strong>ナ形容詞・名詞 ＋ でも</strong>（{静|しず}かでも、{雨|あめ}でも、{日曜日|にちようび}でも）<br>"
                "<strong>否定（〜ない → 〜なくても）</strong>（わからなくても、{安|やす}くなくても）<br>"
                "※「<strong>いくら／どんなに ＋ 〜ても</strong>」とよく一緒に使う",
        notes_ja="「もしAという条件になっても、普通予想される結果とは反対にBだ（条件に関係なくBだ）」という<strong>逆接の仮定条件</strong>を表します。<br>"
                 "例：{明日|あした}<strong>{雨|あめ}が{降|ふ}っても</strong>、サッカーの{試合|しあい}はあります。<br>"
                 "例：このパソコンは、<strong>{高|たか}くても</strong>{買|か}いたいです。<br>"
                 "例：<strong>いくら{食|た}べても</strong>、ちっとも{太|ふと}りません。<br>"
                 "例：{辞書|じしょ}を<strong>{見|み}なくても</strong>、この{新聞|しんぶん}が{読|よ}めます。<br>"
                 "「<strong>いくら〜ても</strong>」「<strong>どんなに〜ても</strong>」「<strong>何{回|かい}〜ても</strong>」と一緒に使うと、「程度がどれだけ大きくても結果は変わらない」と強調できます。",
        notes_en="Expresses a concessive condition ('even if ~ / no matter how ~'). Regardless of condition A, the expected consequence does not happen or B holds true anyway. "
                 "Formed with Verb て-form + も, i-adjective 〜くても, na-adjective/noun + でも, and negative 〜なくても. "
                 "Often paired with いくら or どんなに ('no matter how much ~').",
        nuance_ja="<strong>★「〜ても」と「〜のに」の大切な違い</strong>：<br>"
                  "・<strong>〜ても</strong>：まだ起きていない未来の仮定（もし明日雨が<strong>降っても</strong>行きます）や、いつでも成り立つ一般的なこと、文末が<strong>意志・依頼・推量</strong>の文に使えます。<br>"
                  "・<strong>〜のに</strong>：<strong>すでに確定している事実</strong>に対する不満・驚きにしか使えず、後ろに「〜ましょう」「〜てください」「〜たい」は置けません。",
        nuance_en="Key difference between 〜ても and 〜のに: "
                  "〜ても works for hypothetical future situations ('Even if it rains tomorrow, I'll go') and allows volition, requests (〜てください), and desires (〜たい) in the main clause. "
                  "〜のに is strictly for already-established facts and expresses frustration/surprise; it cannot take requests or future intentions.",
        trap_ja="①イ形容詞は「<strong>〜くても</strong>」（{寒|さむ}くても）、ナ形容詞と名詞は「<strong>〜でも</strong>」（{嫌|いや}でも・{休日|きゅうじつ}でも）になります。<br>"
                "②否定形「〜ない」はイ形容詞と同じように「<strong>〜なくても</strong>」になります（×行かないでも → ○<strong>{行|い}かなくても</strong>）。<br>"
                "③仮定の話（「もし明日〜」「これから〜したい」）には「のに」ではなく必ず「<strong>ても</strong>」を使います。",
        trap_en="① i-adjectives take 〜くても (高くても); na-adjectives and nouns take でも (便利でも, 雨でも). "
                "② Negatives conjugate like i-adjectives: 〜ない → 〜なくても (行かなくても). "
                "③ For hypothetical conditions or when the main clause expresses intention/desire (〜たい, 〜つもりだ, 〜てください), use ても, NOT のに.",
        contrast=[
            dict(type="wrong", sentence="もし{明日|あした}{雨|あめ}が{降|ふ}るのに、{私|わたし}はハイキングに{行|い}きます。",
                 reason_ja="「もし明日〜」という未来の仮定条件や、意志を表す文では「のに」は使えません。",
                 reason_en="のに cannot be used for a hypothetical future condition ('if it rains tomorrow')."),
            dict(type="correct", sentence="もし{明日|あした}{雨|あめ}が{降|ふ}っても、{私|わたし}はハイキングに{行|い}きます。",
                 reason_ja="仮定の逆接「たとえ雨が降っても、行く」には「〜ても」を使います。",
                 reason_en="ても is the correct form for 'even if it rains tomorrow, I will go'."),
            dict(type="correct", sentence="どんなに{忙|いそが}しくても、{朝|あさ}ごはんはかならず{食|た}べるようにしています。",
                 reason_ja="「どんなに＋イ形容詞（〜くても）」で、どんな場合でも変わらない習慣を表します。",
                 reason_en="どんなに忙しくても expresses an unshakeable habit ('no matter how busy I am')."),
        ],
        comparison=[
            dict(form="〜ても／〜でも", form_en="even if ~ (hypothetical / general)", badge="仮定・一般条件", badge_type="good",
                 nuance_ja="未来の仮定や「いくら〜ても」という一般条件に使え、文末に意志・依頼・希望も置けます。",
                 nuance_en="Works for hypothetical conditions and general truths; allows volition/requests.",
                 example="{少|すこ}し{高|たか}くても、{丈夫|じょうぶ}なカバンを{買|か}いたいです。"),
            dict(form="〜のに", form_en="even though ~ (factual regret/surprise)", badge="事実・不満", badge_type="both",
                 nuance_ja="すでに起きた事実に対して「〜したのに（残念だ・おかしい）」と不満や驚きを表します。",
                 nuance_en="Used only for established facts to express frustration, regret, or surprise.",
                 example="{薬|くすり}を{飲|の}んだのに、まだ{熱|ねつ}が{下|さ}がりません。"),
            dict(form="〜たら", form_en="if / when ~ (normal condition)", badge="順接の仮定", badge_type="neutral",
                 nuance_ja="「もしAなら、普通にBする」という順当な条件を表します。",
                 nuance_en="Expresses a normal, expected consequence ('if A, then B').",
                 example="{明日|あした}{雨|あめ}が{降|ふ}ったら、{家|いえ}にいます。"),
        ],
    ),
    quiz=[
        dict(stem="この{薬|くすり}を（　　　）よくならないときは、もう{一度|いちど}{病院|びょういん}へ{来|き}てください。",
             correct="{飲|の}んでも", distractors=["{飲|の}むのに", "{飲|の}めば", "{飲|の}むと"],
             en="If you don't get better even after taking this medicine, please come to the hospital again.",
             notes_ja="薬を飲むと普通はよくなるのに、反対に「よくならない場合」を仮定しているので、逆接の仮定「飲んでも」が正解です。",
             notes_en="Since not getting better goes against the expected result of taking medicine, use the hypothetical concessive 飲んでも ('even if you take it')."),
        dict(stem="{家賃|やちん}がもう{少|すこ}し（　　　）、{駅|えき}から{近|ちか}いアパートに{住|す}みたいです。",
             correct="{高|たか}くても", distractors=["{高|たか}いでも", "{高|たか}いのに", "{高|たか}かったらで"],
             en="Even if the rent is a little higher, I want to live in an apartment close to the station.",
             notes_ja="イ形容詞「高い」のても形は「高くても」です。後ろが希望「住みたいです」なので、仮定の「ても」を使います（「のに」は使えません）。",
             notes_en="The ても-form of i-adjective 高い is 高くても. Since the main clause expresses a desire (住みたいです), のに cannot be used."),
        dict(stem="うちの{近|ちか}くのスーパーは、{日曜日|にちようび}や{祝日|しゅくじつ}（　　　）{夜|よる}11{時|じ}まで{開|あ}いています。",
             correct="でも", distractors=["ても", "くても", "だても"],
             en="The supermarket near my house is open until 11 PM even on Sundays and holidays.",
             notes_ja="名詞「日曜日や祝日」には「でも」を付けます。「だても」や「ても」は名詞には付きません。",
             notes_en="Attach でも directly to nouns (日曜日や祝日でも)."),
        dict(stem="どんなに{説明|せつめい}を（　　　）、この{機械|きかい}の{動|うご}く{仕組|しく}みがわかりません。",
             correct="{聞|き}いても", distractors=["{聞|き}けば", "{聞|き}くと", "{聞|き}くなら"],
             en="No matter how much I listen to the explanation, I don't understand how this machine works.",
             notes_ja="「どんなに〜ても（わからない）」のセットで、「どれだけ聞いても理解できない」という逆接を表します。",
             notes_en="どんなに pairs with 〜ても (どんなに聞いても) to mean 'no matter how much I listen'."),
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
