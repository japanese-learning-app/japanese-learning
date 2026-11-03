# -*- coding: utf-8 -*-
"""N5 grammar ids 24-46 (hand-authored). Format: see build_grammar.py docstring.
English fields may embed Japanese inside «…» (converted to ruby by en())."""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n5_lib import R


def en(s):
    return re.sub(r'«(.+?)»', lambda m: R(m.group(1)), s)


GRAMMAR = {}

# ---------------------------------------------------------------- 24
GRAMMAR[24] = dict(
    name="Nへ行く／来る／帰る", reading="Nへいく／くる／かえる",
    meaning_en="go / come / return to a place (destination particle へ)",
    similar="Nに行く、〜に行く（目的）、どこへも",
    details=dict(
        formula="<strong>場所</strong> ＋ <strong>へ</strong> ＋ 行きます／来ます／帰ります",
        notes_ja="助詞の「へ」は「え」と読みます。移動の動詞（行きます・来ます・帰ります）の前に、行き先の場所をおきます。<br>"
                 "例：{学校|がっこう}<strong>へ</strong>行きます／{日本|にほん}<strong>へ</strong>来ました／{家|うち}<strong>へ</strong>帰ります。<br>"
                 "疑問詞とも使えます：どこ<strong>へ</strong>行きますか。否定は「どこ<strong>へも</strong>行きません」（どこにも行かない）。<br>"
                 "目的を言うときは「ます形＋に」：{図書館|としょかん}へ{本|ほん}を{借|か}り<strong>に</strong>行きます。<br>"
                 "活用：行きます・行きません・行きました・行きませんでした／来ます・来ません・来ました／帰ります・帰りません・帰りました。",
        notes_en=en("The particle へ is pronounced “e”, not “he”. Put the destination before a verb of movement: "
                    "<strong>place + へ + 行きます / 来ます / 帰ります</strong>. Examples: «{学校|がっこう}へ行きます» (I go to school), «{日本|にほん}へ来ました» (I came to Japan), "
                    "«{家|うち}へ帰ります» (I go home). With a question word: «どこへ行きますか»; negative: «どこへも行きません» (I'm not going anywhere). "
                    "To state the purpose, use the masu-stem + に: «{図書館|としょかん}へ{本|ほん}を{借|か}りに行きます» (I go to the library to borrow a book)."),
        nuance_ja="「へ」は、<strong>行き先に向かって進む「方向」</strong>を表す助詞です。「行く」は話し手のいる場所から離れていく移動、「来る」は話し手のいる場所"
                  "（話し手が基準にしている場所）に近づく移動、「帰る」は自分の家・国・職場など<strong>もとの場所に戻る</strong>移動です。"
                  "N5では「へ」と「に」のどちらも使え、意味はほとんど変わりません。「へ」はやわらかく方向を示し、手紙や荷物の送り先にも使えます。",
        nuance_en=en("へ marks the <strong>direction you move toward</strong>. «行く» moves away from the speaker's place, «来る» moves toward the speaker's place (or the place the speaker is using as the base), "
                     "and «帰る» means going <strong>back to where you belong</strong> (home, your country, your workplace). At N5, へ and に are interchangeable for destinations; "
                     "へ sounds slightly softer and stresses the direction, and it is also used for where a letter or parcel is sent."),
        trap_ja="①「学校を行きます」のように、行き先に「を」は使えません。「を」は動作の対象（本を読む）や、通る場所（道を歩く）に使います。<br>"
                "②「学校で行きます」も誤りです。「で」は手段（電車で行く）か、動作をする場所（学校で勉強する）です。<br>"
                "③「来る」と英語の come は同じではありません。電話で「今すぐ来て」と言われたら、日本語では「今、<strong>行きます</strong>」と答えます（相手のいる場所へ向かうので「行く」）。英語では “I'm coming.” です。<br>"
                "④時刻には「へ」ではなく「に」を使います：{七時|しちじ}に行きます（×七時へ行きます）。",
        trap_en=en("① You cannot mark the destination with を: ×«学校を行きます». を is for the object of an action («本を読む») or the route you pass along («道を歩く»).<br>"
                   "② ×«学校で行きます» is also wrong: で marks a means («電車で行く») or the place where an action happens («学校で勉強する»).<br>"
                   "③ Japanese «来る» is not the same as English “come”. If someone phones you and says “come now”, you reply «今、<strong>行きます</strong>» because you are moving to the listener's place; English says “I'm coming.”<br>"
                   "④ Times take に, not へ: «{七時|しちじ}に行きます» (×«七時へ行きます»)."),
        contrast=[
            dict(type="wrong", reason_ja="行き先に「を」は使えません。目的地は「へ」（または「に」）です。",
                 reason_en="You cannot mark a destination with を. Use へ (or に).",
                 sentence="{私|わたし}は{毎日|まいにち}{学校|がっこう}を{行|い}きます。"),
            dict(type="correct", reason_ja="目的地を「へ」で示す、いちばん基本の形です。",
                 reason_en="The basic pattern: destination + へ + movement verb.",
                 sentence="{私|わたし}は{毎日|まいにち}{学校|がっこう}<strong>へ</strong>{行|い}きます。"),
            dict(type="correct", reason_ja="行き先は「へ」、目的は「ます形＋に」で言います。",
                 reason_en="Destination with へ, purpose with the masu-stem + に.",
                 sentence="{図書館|としょかん}<strong>へ</strong>{本|ほん}を{借|か}り<strong>に</strong>{行|い}きます。"),
        ],
        comparison=[
            dict(form="Nへ行く", form_en="go toward N (direction)", badge="方向", badge_type="both",
                 nuance_ja="向かう方向をやわらかく示します。手紙や荷物の送り先にも使えます。",
                 nuance_en="Softly points to the direction; also usable for where something is sent.",
                 example="{来週|らいしゅう}、{京都|きょうと}<strong>へ</strong>{行|い}きます。"),
            dict(form="Nに行く", form_en="go to N (arrival point)", badge="ほぼ同じ", badge_type="both",
                 nuance_ja="到着する場所をはっきり示します。N5ではどちらも正解です。時刻・曜日には「に」しか使えません。",
                 nuance_en="Names the point you arrive at. Both are correct at N5; only に works with times and days.",
                 example="{毎朝|まいあさ}、{七時|しちじ}に{会社|かいしゃ}に{行|い}きます。"),
            dict(form="Nで行く", form_en="go by N (means)", badge="区別注意", badge_type="bad",
                 nuance_ja="「で」は手段（乗り物など）です。行き先ではありません。",
                 nuance_en="で marks the means of transport, not the destination.",
                 example="{電車|でんしゃ}<strong>で</strong>{会社|かいしゃ}へ{行|い}きます。"),
        ]),
    quiz=[
        dict(stem="{明日|あした}は{図書館|としょかん}（　　　）{行|い}って、{日本語|にほんご}を{勉強|べんきょう}します。",
             correct="へ", distractors=["で", "を", "が"],
             en="Tomorrow I'll go to the library and study Japanese.",
             notes_ja="「図書館」は行き先なので「へ」。「で」は動作の場所、「を」は動作の対象、「が」は主語につくので、ここには入りません。",
             notes_en=en("«図書館» is the destination, so へ. で marks where an action happens, を marks an object and が marks a subject; none of them fit before «行って».")),
        dict(stem="A: いつ{日本|にほん}（　　　）{来|き}ましたか。B: {去年|きょねん}の{春|はる}です。",
             correct="へ", distractors=["で", "を", "が"],
             en="A: When did you come to Japan? B: Last spring.",
             notes_ja="「来ました」の行き先は「日本へ」。（「日本に」でも同じ意味です。）「日本が来ました」「日本を来ました」「日本で来ました」は意味が通じません。",
             notes_en=en("The destination of «来ました» is marked with へ («日本へ»; に would also be fine). «日本が / を / で来ました» make no sense.")),
        dict(stem="{毎日|まいにち}、{仕事|しごと}のあと、まっすぐ{家|うち}（　　　）{帰|かえ}ります。",
             correct="へ", distractors=["で", "を", "が"],
             en="Every day after work I go straight home.",
             notes_ja="帰る場所（家）は「へ」で示します。「家を帰る」は誤りです（「家を出る」なら「を」が使えます）。",
             notes_en=en("The place you return to takes へ. ×«家を帰ります» is wrong (although «家を出ます» is fine, because you leave the house).")),
        dict(stem="{日曜日|にちようび}は{雨|あめ}でしたから、どこ（　　　）も{行|い}きませんでした。",
             correct="へ", distractors=["を", "が", "と"],
             en="It rained on Sunday, so I didn't go anywhere.",
             notes_ja="「どこへも〜ません」で「どこにも行かなかった」。「どこをも」「どこがも」「どことも」とは言いません。",
             notes_en=en("«どこへも〜ません» means “not anywhere”. ×«どこをも / どこがも / どことも» are not used.")),
    ])

# ---------------------------------------------------------------- 25
GRAMMAR[25] = dict(
    name="Nに会う", reading="Nにあう", meaning_en="to meet / see (a person)",
    similar="Nと会う、Nに会いに行く、Nを見る",
    details=dict(
        formula="<strong>人</strong> ＋ <strong>に</strong> ＋ 会います（会う）",
        notes_ja="「会う」は、会う相手を「に」で表します。<br>"
                 "例：{友達|ともだち}<strong>に</strong>会います／{先生|せんせい}<strong>に</strong>会いました／{駅|えき}で{田中|たなか}さん<strong>に</strong>会いました。<br>"
                 "会う場所は「で」：{駅|えき}<strong>で</strong>会います。{待|ま}ち合わせるように、おたがいに約束して会うときは「と」も使えます：{友達|ともだち}<strong>と</strong>{駅|えき}で会います。<br>"
                 "会いに行く：{母|はは}に会い<strong>に</strong>行きます（ます形＋に行く）。<br>"
                 "活用：会います・会いません・会いました・会いませんでした／会う・会わない（×会いない）・会った。",
        notes_en=en("«会う» marks the person you meet with に: «{友達|ともだち}に会います», «{先生|せんせい}に会いました». The place where you meet takes で: «{駅|えき}で会います». "
                    "If two people arrange to meet each other, と also works: «{友達|ともだち}と{駅|えき}で会います» (I'll meet a friend at the station). "
                    "To say “go to see someone”, use the masu-stem + に行く: «{母|はは}に会いに行きます». Plain negative: «会わない» (not ×会いない)."),
        nuance_ja="「Nに会う」は、<strong>人に実際に顔を合わせる</strong>ことを表します。「に」は、会う相手を「向かう先」として示します。町で先生にばったり会うときも、"
                  "来週母に会うように予定しているときも使えます。「Nと会う」は「二人で約束して会う」感じで、対等な待ち合わせに向いています。"
                  "会う相手は<strong>人</strong>です。物や場所には使いません（映画を見る・図書館に行く）。",
        nuance_en=en("“N に会う” means to <strong>actually come face to face with a person</strong>; に shows the person as the “target” you meet. It works for chance meetings (bumping into a teacher in town) "
                     "and for planned ones (seeing my mother next week). “N と会う” feels like two people arranging to meet each other as equals. The object of 会う is always a <strong>person</strong>; "
                     "for things use «見る», for places use «行く»."),
        trap_ja="①英語の “meet my friend”（目的語）に引かれて「友達を会います」と言うのは誤りです。<strong>「会う」は「を」を取りません</strong>。<br>"
                "②「見る」と区別します。映画やテレビは「見る」、人と顔を合わせるのは「会う」です。「先生を見ました」は、遠くから目にしただけの意味になります。<br>"
                "③場所に「に」を使うと「に」が重なります。×{駅|えき}に先生に会いました → ○{駅|えき}<strong>で</strong>先生に会いました。<br>"
                "④「友達と会う」と「友達に会う」は似ていますが、「と」は二人が約束して会うとき、「に」は相手のところへ行く・相手に出会うときによく使います。",
        trap_en=en("① Because English says “meet my friend”, learners say ×«友達を会います». <strong>«会う» never takes を.</strong><br>"
                   "② Do not confuse it with «見る»: «映画を見る» (watch a film) vs. «人に会う» (meet a person). «先生を見ました» only means you caught sight of the teacher.<br>"
                   "③ Do not stack に for place and person: ×«駅に先生に会いました» → ○«{駅|えき}で{先生|せんせい}に会いました».<br>"
                   "④ «友達と会う» and «友達に会う» are close; と suits an arranged meet-up of two people, に suits going to see someone or running into someone."),
        contrast=[
            dict(type="wrong", reason_ja="「会う」は「を」を使いません。会う相手は「に」です。",
                 reason_en="会う does not take を. The person you meet takes に.",
                 sentence="{昨日|きのう}、{駅|えき}で{先生|せんせい}を{会|あ}いました。"),
            dict(type="correct", reason_ja="場所は「で」、会った相手は「に」。",
                 reason_en="で for the place, に for the person you met.",
                 sentence="{昨日|きのう}、{駅|えき}で{先生|せんせい}<strong>に</strong>{会|あ}いました。"),
            dict(type="correct", reason_ja="約束して二人で会うときは「と」も自然です。",
                 reason_en="For an arranged meet-up of two people, と is natural too.",
                 sentence="{日曜日|にちようび}は{友達|ともだち}<strong>と</strong>{駅|えき}で{会|あ}います。"),
        ],
        comparison=[
            dict(form="Nに会う", form_en="meet / see N (a person)", badge="基本", badge_type="both",
                 nuance_ja="相手に会うことを表す基本の形です。偶然会う・訪ねて会う、どちらにも使えます。",
                 nuance_en="The basic pattern; works for chance meetings and for visiting someone.",
                 example="{来週|らいしゅう}、{国|くに}の{母|はは}<strong>に</strong>{会|あ}います。"),
            dict(form="Nと会う", form_en="meet N (by arrangement)", badge="待ち合わせ", badge_type="both",
                 nuance_ja="二人が約束して会う感じです。場所と時間を決めて会うときによく使います。",
                 nuance_en="Two people meet by arrangement; common when fixing a place and time.",
                 example="{土曜日|どようび}に{駅|えき}で{友達|ともだち}<strong>と</strong>{会|あ}います。"),
            dict(form="Nを見る", form_en="look at / see N (with the eyes)", badge="別の動詞", badge_type="neutral",
                 nuance_ja="目で見ることです。人と顔を合わせて会うわけではありません。",
                 nuance_en="Just looking with your eyes; it does not mean you met the person.",
                 example="{公園|こうえん}で{先生|せんせい}<strong>を</strong>{見|み}ましたが、{話|はな}しませんでした。"),
        ]),
    quiz=[
        dict(stem="{昨日|きのう}、{駅|えき}で{先生|せんせい}（　　　）{会|あ}いました。",
             correct="に", distractors=["を", "で", "へ"],
             en="Yesterday I met my teacher at the station.",
             notes_ja="会った相手には「に」。「先生を会いました」は誤り、「で」は場所に使います（駅で）。「へ」は「会う」と合いません。",
             notes_en=en("The person you meet takes に. ×«先生を会いました» is wrong; で marks the place (already used for «駅で»); へ does not go with «会う».")),
        dict(stem="{来週|らいしゅう}、{国|くに}の{母|はは}（　　　）{会|あ}いに{行|い}きます。",
             correct="に", distractors=["を", "で", "から"],
             en="Next week I'm going to see my mother back home.",
             notes_ja="「母に会いに行く」＝母に会うために行く。会う相手は「に」です。「母を会いに」は誤り。",
             notes_en=en("«母に会いに行く» = go in order to see my mother. The person takes に; ×«母を会いに» is wrong.")),
        dict(stem="A: {週末|しゅうまつ}、{誰|だれ}（　　　）{会|あ}いましたか。B: {高校|こうこう}の{友達|ともだち}に{会|あ}いました。",
             correct="に", distractors=["を", "で", "まで"],
             en="A: Who did you see at the weekend? B: I met a friend from high school.",
             notes_ja="「誰に会いましたか」と、会った相手をたずねる文です。答えの「友達に会いました」と同じ「に」。",
             notes_en=en("«誰に会いましたか» asks who you met; the answer «友達に会いました» uses the same に.")),
        dict(stem="{駅|えき}の{前|まえ}で{林|はやし}さん（　　　）{会|あ}って、{一緒|いっしょ}にお{茶|ちゃ}を{飲|の}みました。",
             correct="に", distractors=["を", "で", "まで"],
             en="I met Mr. Hayashi in front of the station, and we had tea together.",
             notes_ja="「駅の前で」が場所なので、人には「に」。「林さんで会って」は意味が通じません。",
             notes_en=en("«駅の前で» already marks the place, so the person gets に. ×«林さんで会って» does not make sense.")),
    ])
