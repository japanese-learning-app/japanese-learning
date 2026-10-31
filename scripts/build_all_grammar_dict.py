# -*- coding: utf-8 -*-
"""
Builder for database/jlpt_all_grammar_dict.js
Merges:
1. JLPT N2 grammar catalog (195 patterns with hiragana readings & lesson IDs)
2. JLPT N1 grammar catalog (127 core patterns)
3. JLPT N3 grammar catalog (182 patterns with hiragana readings from jlpt_n3_grammar_quiz_data.js)
4. JLPT N4 grammar catalog (60 core patterns)
5. JLPT N5 grammar catalog (35 core patterns)
6. JLPT N2 similar/related grammar expressions (917 patterns from jlpt_similar_grammar_dict.js)
Total: Over 1,400 JLPT grammar expressions and patterns.
"""

import json
import re

def clean_term(s):
    return re.sub(r'[〜～\s・()（）]', '', s or '')

def main():
    # 1. Load N2 grammar quiz data & hiragana map
    with open('scripts/build_grammar_textbook.py', 'r', encoding='utf-8') as f:
        textbook_script = f.read()

    match_hmap = re.search(r'const GRAMMAR_HIRAGANA_MAP = (\{.*?\n    \});', textbook_script, re.DOTALL)
    pairs = re.findall(r"(\d+):\s*[\x27\x22]([^\x27\x22]+)[\x27\x22]", match_hmap.group(1))
    n2_hiragana_map = {int(k): v for k, v in pairs}

    with open('database/jlpt_n2_grammar_quiz_data.js', 'r', encoding='utf-8') as f:
        n2_raw = f.read().split('=', 1)[1].strip().rstrip(';')
    n2_quiz_data = json.loads(n2_raw)

    n2_grammars = {}
    name_to_n2 = {}
    for q in n2_quiz_data:
        gid = q.get('grammar_id')
        gname = q.get('grammar')
        if gid not in n2_grammars:
            n2_grammars[gid] = {
                'id': gid,
                'name': gname,
                'reading': n2_hiragana_map.get(gid, q.get('reading', '')),
                'meaning_en': q.get('meaning_en', ''),
                'similar': q.get('similar', ''),
                'sentence_jp': q.get('sentence_jp', ''),
                'sentence_en': q.get('sentence_en', '')
            }
        name_to_n2[gname] = gid
        clean_name = clean_term(gname)
        name_to_n2[clean_name] = gid

    # Special manual mapping for known aliases
    name_to_n2['とか'] = 172 # とか(で)

    # 2. Load N3 grammar quiz data
    with open('database/jlpt_n3_grammar_quiz_data.js', 'r', encoding='utf-8') as f:
        n3_raw = f.read().split('=', 1)[1].strip().rstrip(';')
    n3_quiz_data = json.loads(n3_raw)

    N3_KANJI_READINGS = {
        "上げる": "あげる", "合う": "あう", "別に～ない": "べつに～ない",
        "中": "ちゅう／じゅう", "気味": "ぎみ", "一度に": "いちどに",
        "一方だ": "いっぽうだ", "一体": "いったい", "か何か": "かなにか",
        "代わりに": "かわりに", "結果": "けっか", "結局": "けっきょく",
        "決して〜ない": "けっして〜ない", "切れない": "きれない", "切る": "きる",
        "込む": "こむ", "向け": "むけ", "向き": "むき", "直す": "なおす",
        "に違いない": "にちがいない", "に反して": "にはんして", "に関する": "にかんする",
        "に比べて": "にくらべて", "に慣れる": "になれる", "に対して": "にたいして",
        "を中心に": "をちゅうしんに", "を込めて": "をこめて", "を通じて": "をつうじて",
        "最中に": "さいちゅうに", "際に": "さいに", "〜は（数量）": "〜は",
        "確かに": "たしかに", "例えば": "たとえば", "ている場合じゃない": "ているばあいじゃない",
        "的": "てき", "ても始まらない": "てもはじまらない", "て済む": "てすむ",
        "途中で": "とちゅうで", "と言えば": "といえば", "と言うと": "というと",
        "通す": "とおす", "と共に": "とともに", "とは限らない": "とはかぎらない",
        "上で": "うえで", "上に": "うえに", "は別として": "はべつとして",
        "は～で有名": "は～でゆうめい", "割に": "わりに", "ような気がする": "ようなきがする",
        "ように見える": "ようにみえる"
    }

    # 3. N1 Catalog (127 core patterns)
    N1_CATALOG = [
        {"term": "〜を皮切りに", "reading": "をかわきりに", "meaning": "〜を始まりとして次々に同じようなことが行われる。(starting with ~ as the first)"},
        {"term": "〜であれ", "reading": "であれ", "meaning": "たとえ〜であっても。〜でも。(whether it is ~ or ~)"},
        {"term": "〜極まりない", "reading": "きわまりない", "meaning": "これ以上ないほど非常に〜だ。(extremely; boundlessly ~)"},
        {"term": "〜を禁じ得ない", "reading": "をきんじえない", "meaning": "感情や涙などを抑えることができない。(cannot suppress; cannot help feeling ~)"},
        {"term": "〜に至っては", "reading": "にいたっては", "meaning": "極端な例として〜の場合は。(when it comes to ~ (extreme case))"},
        {"term": "〜まじき", "reading": "まじき", "meaning": "ある立場として決してあってはならない。(that should not be; unpardonable for)"},
        {"term": "〜ごとき", "reading": "ごとき", "meaning": "〜のような。あるいは〜なんて（軽視・謙遜）。(like; as if; such as)"},
        {"term": "〜ずくめ", "reading": "ずくめ", "meaning": "全体がそればかりである状態を表す。(entirely; full of; nothing but)"},
        {"term": "〜まみれ", "reading": "まみれ", "meaning": "汗・泥・血・借金など好ましくないものが表面全体についている。(covered in; smeared with)"},
        {"term": "〜ゆえに", "reading": "ゆえに", "meaning": "〜という理由・原因のために。(because of; due to)"},
        {"term": "〜ならでは", "reading": "ならでは", "meaning": "〜だけが持っている特別な素晴らしさを表す。(uniquely possible for; characteristic of)"},
        {"term": "〜にかかわる", "reading": "にかかわる", "meaning": "命や名誉など重大な事態に影響・関係する。(affecting; concerning (serious matter))"},
        {"term": "〜とあっては", "reading": "とあっては", "meaning": "〜という特別な事情・状況なら。(given that special situation)"},
        {"term": "〜たるもの", "reading": "たるもの", "meaning": "〜という身分・資格を持つ者ならば当然。(in the role/position of)"},
        {"term": "〜あっての", "reading": "あっての", "meaning": "〜が存在するからこそ成り立つ。(which exists only thanks to)"},
        {"term": "〜ともなると", "reading": "ともなると", "meaning": "その段階や特別な立場に達すると。(once one reaches the stage of)"},
        {"term": "〜なくして", "reading": "なくして", "meaning": "もし〜がなければ実現しない。(without ~; impossible without)"},
        {"term": "〜なしに", "reading": "なしに", "meaning": "〜をしないで。(without doing ~)"},
        {"term": "〜なりに", "reading": "なりに", "meaning": "その人・物相応に。(in one’s own way; commensurate with)"},
        {"term": "〜を踏まえて", "reading": "をふまえて", "meaning": "〜を前提・基礎として。(based on; taking into consideration)"},
        {"term": "〜に先駆けて", "reading": "にさきがけて", "meaning": "他の誰よりも先に。(ahead of; taking the lead in)"},
        {"term": "〜を契機に", "reading": "をけいきに", "meaning": "〜をきっかけとして大きな変化が起きる。(triggered by; using ~ as opportunity)"},
        {"term": "〜を機に", "reading": "をきに", "meaning": "〜をよい機会として行動を起こす。(taking the opportunity of)"},
        {"term": "〜と相まって", "reading": "とあいまって", "meaning": "〜と互いに影響し合ってより一層。(combined with; together with)"},
        {"term": "〜にかまけて", "reading": "にかまけて", "meaning": "一つのことばかりに夢中になって他を疎かにする。(being preoccupied with; neglecting other things)"},
        {"term": "〜にかこつけて", "reading": "にかこつけて", "meaning": "別の事柄を口実・言いがかりにして。(under the pretext of)"},
        {"term": "〜はおろか", "reading": "はおろか", "meaning": "〜はもちろんのこと、もっと簡単なことも。(let alone; not to speak of)"},
        {"term": "〜ならいざしらず", "reading": "ならいざしらず", "meaning": "〜ならともかく、そうではないのだから。(may be fine for ~, but definitely not)"},
        {"term": "〜ならまだしも", "reading": "ならまだしも", "meaning": "〜ならまだ許せるが。(would be understandable, but)"},
        {"term": "〜といえども", "reading": "といえども", "meaning": "たとえ〜であっても。(even though; despite being)"},
        {"term": "〜とはいえ", "reading": "とはいえ", "meaning": "事実を認めるが、しかし。(although; nonetheless)"},
        {"term": "〜からある", "reading": "からある", "meaning": "〜以上の大きさ・重さ・長さがある。(as much as; more than (size/weight))"},
        {"term": "〜からの", "reading": "からの", "meaning": "〜以上の数・金額・人数がある。(as many as; upwards of (cost/people))"},
        {"term": "〜そばから", "reading": "そばから", "meaning": "〜してもすぐに同じことが繰り返される。(no sooner than ~; right after)"},
        {"term": "〜が早いか", "reading": "がはやいか", "meaning": "〜するとほとんど同時に。(as soon as; no sooner had)"},
        {"term": "〜や否や", "reading": "やいなや", "meaning": "〜するとすぐその瞬間に。(the moment; right as)"},
        {"term": "〜なり", "reading": "なり", "meaning": "〜したとたん、予想外の次の動作を起こす。(immediately upon doing)"},
        {"term": "〜んばかり", "reading": "んばかり", "meaning": "今にも〜しそうな様子で。(as if about to; virtually)"},
        {"term": "〜とばかりに", "reading": "とばかりに", "meaning": "言葉には出さないが表情や態度で示す。(as if to say)"},
        {"term": "〜めく", "reading": "めく", "meaning": "〜の気配や傾向が強く感じられる。(take on the air of; show signs of)"},
        {"term": "〜ぶる", "reading": "ぶる", "meaning": "本当はそうでないのに、そのように振る舞う。(act like; pretend to be)"},
        {"term": "〜びる", "reading": "びる", "meaning": "その状態にふさわしく見える、大人びる。(seem mature; age-appropriate)"},
        {"term": "〜げ", "reading": "げ", "meaning": "いかにも〜ありそうな様子。(appearing to be; looking ~)"},
        {"term": "〜じみた", "reading": "じみた", "meaning": "〜のような好ましくない感じを帯びている。(tinted with; seeming like)"},
        {"term": "〜きらいがある", "reading": "きらいがある", "meaning": "望ましくない傾向・癖がある。(have a bad tendency to)"},
        {"term": "〜始末だ", "reading": "しまつだ", "meaning": "いろいろ悪いことが重なって最終的に困った結果になる。(end up in a bad state of)"},
        {"term": "〜っぱなし", "reading": "っぱなし", "meaning": "ある動作や状態を放置したままにする。(left in an ongoing/unfinished state)"},
        {"term": "〜ずにはすまない", "reading": "ずにはすまない", "meaning": "社会常識や立場上、〜しないでは済まされない。(cannot get away without doing)"},
        {"term": "〜ないではすまない", "reading": "ないではすまない", "meaning": "どうしても〜しなければ許されない。(cannot be excused without doing)"},
        {"term": "〜ずにはおかない", "reading": "ずにはおかない", "meaning": "必ず〜という結果をもたらす。(bound to; will inevitably cause)"},
        {"term": "〜ないではおかない", "reading": "ないではおかない", "meaning": "自然の勢いで必ず〜させてしまう。(cannot refrain from causing)"},
        {"term": "〜を余儀なくされる", "reading": "をよぎなくされる", "meaning": "やむを得ず〜させられる。(be forced to do)"},
        {"term": "〜を余儀なくさせる", "reading": "をよぎなくさせる", "meaning": "相手にやむを得ず〜を行わせる。(force someone to do)"},
        {"term": "〜に耐えない", "reading": "にたえない", "meaning": "感情が強すぎて抑えきれない。(cannot suppress feelings; deeply moved)"},
        {"term": "〜に堪えない", "reading": "にたえない", "meaning": "見る・聞くに値しない、ひどい状態。(cannot stand; unbearable to watch)"},
        {"term": "〜に足る", "reading": "にたる", "meaning": "〜する価値・能力が十分にある。(worthy of; sufficient for)"},
        {"term": "〜に堪える", "reading": "にたえる", "meaning": "〜するだけの十分な価値がある。(worthy of praise/reading)"},
        {"term": "〜に忍びない", "reading": "にしのびない", "meaning": "心が痛んで〜するのに耐えられない。(cannot bear to (see/do))"},
        {"term": "〜に及ばない", "reading": "におよばない", "meaning": "そこまでする必要はない。〜には及ばない。(no need to; falls short of)"},
        {"term": "〜までもない", "reading": "までもない", "meaning": "言うまでもなく明白である。する必要がない。(goes without saying; no need)"},
        {"term": "〜には及ばない", "reading": "にはおよばない", "meaning": "わざわざ〜する必要はない。(there is no need to)"},
        {"term": "〜にほかならない", "reading": "にほかならない", "meaning": "まさにそれ以外の何物でもない。(nothing other than; simply because)"},
        {"term": "〜にすぎない", "reading": "にすぎない", "meaning": "ただ〜だけで、それ以上の価値はない。(nothing more than; merely)"},
        {"term": "〜にとどまらない", "reading": "にとどまらない", "meaning": "ある範囲に収まらず、さらに広がる。(not limited to; extends beyond)"},
        {"term": "〜にとどまらず", "reading": "にとどまらず", "meaning": "〜だけでなく、より広い範囲に及ぶ。(not stopping at; but also)"},
        {"term": "〜もさることながら", "reading": "もさることながら", "meaning": "〜はもちろん、それ以上に。(not only ~, but even more so)"},
        {"term": "〜のみならず", "reading": "のみならず", "meaning": "〜だけでなく、その上。(not only ~, but also)"},
        {"term": "〜であれ〜であれ", "reading": "であれであれ", "meaning": "〜の場合でも、〜の場合でも同じだ。(whether A or B)"},
        {"term": "〜といい〜といい", "reading": "といいといい", "meaning": "〜を見ても〜を見ても、どれも。(both A and B)"},
        {"term": "〜こととて", "reading": "こととて", "meaning": "〜という理由・状況なので。(because; owing to the situation of)"},
        {"term": "〜とあって", "reading": "とあって", "meaning": "〜という特別な状況なので。(because of the special condition that)"},
        {"term": "〜をもって", "reading": "をもって", "meaning": "〜の手段で。あるいは〜の期日で終了する。(by means of; as of (cutoff))"},
        {"term": "〜を限りに", "reading": "をかぎりに", "meaning": "〜の時を最後に、以後はやめる。(as the final cutoff; starting from now no more)"},
        {"term": "〜ともなく", "reading": "ともなく", "meaning": "特に意識や目的を持たずに自然と。(without thinking; absentmindedly)"},
        {"term": "〜ともなしに", "reading": "ともなしに", "meaning": "意識せずにぼんやりと。(unconsciously; without clear aim)"},
        {"term": "〜ながらに", "reading": "ながらに", "meaning": "生まれたときや元の状態のままで。(while remaining in the state of)"},
        {"term": "〜きわまる", "reading": "きわまる", "meaning": "この上なく限界まで〜である。(extremely; reaches the peak of)"},
        {"term": "〜といったらない", "reading": "といったらない", "meaning": "言葉で言い表せないほどすごい。(beyond words; extraordinarily)"},
        {"term": "〜かぎりだ", "reading": "かぎりだ", "meaning": "最高に〜の気持ちだ。(feel supremely/extremely ~)"},
        {"term": "〜手前", "reading": "てまえ", "meaning": "周囲の目や相手の立場を考えると。(out of consideration for; given one’s stance)"},
        {"term": "〜そびれる", "reading": "そびれる", "meaning": "〜する機会を逃してしまう。(miss the opportunity to do)"},
        {"term": "〜かたわら", "reading": "かたわら", "meaning": "本業の一方で、別の活動も行う。(alongside; while doing one’s main job)"},
        {"term": "〜かたがた", "reading": "かたがた", "meaning": "ある目的のついでに別の用件も果たす。(while also doing; combining purposes)"},
        {"term": "〜がてら", "reading": "がてら", "meaning": "散歩やついでを兼ねて。(while on the occasion of; as a sideline)"},
        {"term": "〜をよそに", "reading": "をよそに", "meaning": "周囲の心配や反対をまったく気にせず。(disregarding; indifferent to)"},
        {"term": "〜をものともせず", "reading": "をものともせず", "meaning": "困難やプレッシャーに負けずに立ち向かう。(defying; braving (hardship/danger))"},
        {"term": "〜を押して", "reading": "をおして", "meaning": "病気や反対を無理に乗り越えて行う。(pushing through; despite illness/opposition)"},
        {"term": "〜をおいて〜ない", "reading": "をおいてない", "meaning": "〜以外には絶対にない・適任者はいない。(nobody/nothing else besides)"},
        {"term": "〜はさておき", "reading": "はさておき", "meaning": "今は脇に置いて、まず本題に入る。(putting aside; setting aside)"},
        {"term": "〜はどうあれ", "reading": "はどうあれ", "meaning": "どんな状況であろうと。(whatever the case may be)"},
        {"term": "〜拍子に", "reading": "ひょうしに", "meaning": "何かの勢いやはずみで思わぬことが起きる。(by the momentum of; right at the moment)"},
        {"term": "〜折に", "reading": "おりに", "meaning": "その機会・好機・タイミングで。(on the occasion of; when)"},
        {"term": "〜を境に", "reading": "をさかいに", "meaning": "それを区切りとして状況が一変する。(marking the boundary/turning point)"},
        {"term": "〜を経て", "reading": "をへて", "meaning": "年月・場所・経験を通過して。(through; via process/years)"},
        {"term": "〜を前提として", "reading": "をぜんていとして", "meaning": "〜をあらかじめ条件・前提として。(on the premise of)"},
        {"term": "〜をもってすれば", "reading": "をもってすれば", "meaning": "その能力や実力を使えば。(if done with one’s ability/power)"},
        {"term": "〜んがため", "reading": "んがため", "meaning": "強い目的のために努力する。(in order to achieve a major goal)"},
        {"term": "〜んとする", "reading": "んとする", "meaning": "今にも〜しようとする。(be about to do; attempt to)"},
        {"term": "〜てやまない", "reading": "てやまない", "meaning": "心から強く祈る・願い続ける。(never cease to; wholeheartedly wish)"},
        {"term": "〜てからというもの", "reading": "てからというもの", "meaning": "〜して以来ずっとその状態が続いている。(ever since doing ~)"},
        {"term": "〜にあって", "reading": "にあって", "meaning": "その特殊な時代や極限状況の中で。(in the special condition/circumstance of)"},
        {"term": "〜のも無理はない", "reading": "のもむりはない", "meaning": "そうなるのは当然で不思議ではない。(it is only natural; no wonder)"},
        {"term": "〜のみか", "reading": "のみか", "meaning": "〜だけでなく、その上さらに。(not only; not merely)"},
        {"term": "〜といったらありはしない", "reading": "といったらありはしない", "meaning": "この上なくひどい・困った状態だ。(utterly; extraordinarily bad)"},
        {"term": "〜の至り", "reading": "のいたり", "meaning": "この上ない最高の状態（光栄の至り、若気の至り）。(the pinnacle of; utmost)"},
        {"term": "〜の極み", "reading": "のきわみ", "meaning": "これ以上ない極限の境地（贅沢の極み、疲労の極み）。(the peak of; height of)"},
        {"term": "〜たりとも〜ない", "reading": "たりともない", "meaning": "最小の１単位でも絶対に〜ない。(not even a single (second/cent))"},
        {"term": "〜をおいてほかにない", "reading": "をおいてほかにない", "meaning": "それ以外には絶対にない。(none other than)"},
        {"term": "〜に値する", "reading": "にあたいする", "meaning": "そうするだけの価値が十分にある。(worthy of; deserve)"},
        {"term": "〜に難くない", "reading": "にかたくない", "meaning": "想像や推察が容易にできる。(not hard to imagine/foresee)"},
        {"term": "〜てはかなわない", "reading": "てはかなわない", "meaning": "我慢できないほど困る・嫌だ。(cannot endure; can’t stand)"},
        {"term": "〜てはたまらない", "reading": "てはたまらない", "meaning": "感情や欲求が強くて抑えられない。(unbearably; cannot help feeling)"},
        {"term": "〜てはならない", "reading": "てはならない", "meaning": "道徳や法律上、決してしてはいけない。(must never; shall not)"},
        {"term": "〜ないではいられない", "reading": "ないではいられない", "meaning": "どうしても我慢できず自然にしてしまう。(cannot resist doing; compelled to)"},
        {"term": "〜ずにはいられない", "reading": "ずにはいられない", "meaning": "抑えきれずに思わずしてしまう。(cannot help doing; spontaneous urge)"},
        {"term": "〜ざるを得ない", "reading": "ざるをえない", "meaning": "他に方法がなく、嫌でもしなければならない。(have no choice but to)"},
        {"term": "〜ようものなら", "reading": "ようものなら", "meaning": "もしそんなことをしたら大変なことになる。(if ever such a thing happens)"},
        {"term": "〜ばこそ", "reading": "ばこそ", "meaning": "まさにその理由があるからこそ。(precisely because)"},
        {"term": "〜なくしては", "reading": "なくしては", "meaning": "もし〜がなければ到底不可能だ。(impossible without ~)"},
        {"term": "〜ないことには", "reading": "ないことには", "meaning": "まず〜しなければ次の段階に進めない。(unless ~ is done, cannot)"},
        {"term": "〜としたところで", "reading": "としたところで", "meaning": "たとえそう仮定しても結果は同じだ。(even if we assume that)"},
        {"term": "〜にしたところで", "reading": "にしたところで", "meaning": "その立場から見ても同じことだ。(even from the standpoint of)"},
        {"term": "〜にしてみれば", "reading": "にしてみれば", "meaning": "その人の立場から考えれば。(from the viewpoint of)"},
        {"term": "〜からといって", "reading": "からといって", "meaning": "〜という理由だけで必ずしもそうとは限らない。(just because; simply because)"},
        {"term": "〜いかんだ", "reading": "いかんだ", "meaning": "その条件や成り行きによって決まる。(depends on)"},
        {"term": "〜いかんによって", "reading": "いかんによって", "meaning": "次第で結果が変わる。(depending on)"},
        {"term": "〜いかんにかかわらず", "reading": "いかんにかかわらず", "meaning": "どのような条件であっても関係なく。(regardless of)"}
    ]

    # 4. N4 Catalog (60 core patterns)
    N4_CATALOG = [
        {"term": "〜なければならない", "reading": "なければならない", "meaning": "義務・必然を表す。〜する必要がある。(must do ~; have to do ~)"},
        {"term": "〜なくてはならない", "reading": "なくてはならない", "meaning": "強い義務や必然を表す。(must do ~; have to do ~)"},
        {"term": "〜なくてもいい", "reading": "なくてもいい", "meaning": "不必要・許可を表す。〜する必要はない。(don't have to; need not do)"},
        {"term": "〜たことがある", "reading": "たことがある", "meaning": "過去の経験の有無を表す。(have experience of doing ~)"},
        {"term": "〜ほうがいい", "reading": "ほうがいい", "meaning": "相手への助言・勧告を表す。(had better do ~; should do ~)"},
        {"term": "〜すぎる", "reading": "すぎる", "meaning": "程度が度を越えて甚だしいことを表す。(too much; excessively ~)"},
        {"term": "〜やすい", "reading": "やすい", "meaning": "〜することが容易である、あるいは〜になりやすい傾向を表す。(easy to do ~)"},
        {"term": "〜にくい", "reading": "にくい", "meaning": "〜することが困難・しにくいことを表す。(hard / difficult to do ~)"},
        {"term": "〜つもりだ", "reading": "つもりだ", "meaning": "自分の明確な意志・計画を表す。(plan to; intend to ~)"},
        {"term": "〜予定だ", "reading": "よていだ", "meaning": "客観的に決まっている予定・スケジュールを表す。(scheduled to; plan to ~)"},
        {"term": "〜ようにする", "reading": "ようにする", "meaning": "習慣や努力として意識して心がけることを表す。(make an effort to do ~)"},
        {"term": "〜ようになる", "reading": "ようになる", "meaning": "能力や状況が以前と変化して可能になることを表す。(come to do; reach the stage of)"},
        {"term": "〜ことにする", "reading": "ことにする", "meaning": "自分の意志で決断・決定することを表す。(decide to do ~)"},
        {"term": "〜ことになる", "reading": "ことになる", "meaning": "規則や他者によって客観的に決定されたことを表す。(it is decided that ~)"},
        {"term": "〜てみる", "reading": "てみる", "meaning": "実際にどのような結果になるか試してみることを表す。(try doing ~ to see)"},
        {"term": "〜てしまう", "reading": "てしまう", "meaning": "動作の完了、または不本意・後悔の感情を表す。(completely do; regrettably do)"},
        {"term": "〜ておく", "reading": "ておく", "meaning": "将来のためにあらかじめ準備しておくことを表す。(do in advance; prepare)"},
        {"term": "〜てある", "reading": "てある", "meaning": "目的を持って行われた行為の結果がそのまま残っている状態。(has been done; kept in state)"},
        {"term": "〜たり〜たりする", "reading": "たりたりする", "meaning": "代表的な動作を並列して例示する。(do things like ~ and ~)"},
        {"term": "〜し〜し", "reading": "しし", "meaning": "複数の理由や特徴を並べて述べる。(not only ~ but also ~; because ~ and ~)"},
        {"term": "〜ので", "reading": "ので", "meaning": "客観的な原因・理由を穏やかに伝える。(because; since (polite / objective))"},
        {"term": "〜のに", "reading": "のに", "meaning": "予想や期待に反した結果に対する不満・意外感を表す。(although; even though; despite)"},
        {"term": "〜かどうか", "reading": "かどうか", "meaning": "〜であるかそうでないか、不確定な事柄を表す。(whether or not)"},
        {"term": "〜そうだ（様態）", "reading": "そうだ", "meaning": "目で見える様子から直感的に推測する（雨が降りそうだ）。(looks like; seems about to)"},
        {"term": "〜そうだ（伝聞）", "reading": "そうだ", "meaning": "人から聞いたり情報源から得た内容を伝える。(I heard that; reportedly)"},
        {"term": "〜らしい", "reading": "らしい", "meaning": "根拠のある推量、またはその性質に典型的にふさわしい様子。(seems like; typical of)"},
        {"term": "〜かもしれない", "reading": "かもしれない", "meaning": "その可能性が五分五分以下でもあり得ることを表す。(might; maybe; perhaps)"},
        {"term": "〜はずだ", "reading": "はずだ", "meaning": "理由や根拠に基づいて当然そうなるはずだと確信する。(should be; expected to)"},
        {"term": "〜はずがない", "reading": "はずがない", "meaning": "強い根拠に基づいて絶対にあり得ないと否定する。(cannot be; impossible that)"},
        {"term": "〜ために", "reading": "ために", "meaning": "目的（〜のために努力する）または原因・理由を表す。(in order to; because of)"},
        {"term": "〜ように", "reading": "ように", "meaning": "目的や目標の状態が実現するように願ったり努力する。(so that; in order to)"},
        {"term": "〜がる", "reading": "がる", "meaning": "第三者の感情や希望が外見に表れている様子を表す。(show signs of feeling ~)"},
        {"term": "〜たばかり", "reading": "たばかり", "meaning": "動作が行われてから心理的に時間がほとんど経っていないこと。(just finished doing)"},
        {"term": "〜ところだ", "reading": "ところだ", "meaning": "直前（〜するところ）・最中（〜しているところ）・直後（〜したところ）。(just about to / in middle of / just did)"},
        {"term": "〜受身（られる）", "reading": "られる", "meaning": "他から行為を受ける受身表現（被害受身を含む）。(passive voice)"},
        {"term": "〜使役（させる）", "reading": "させる", "meaning": "他者に指示や許可を与えて動作を行わせる。(causative voice; make / let do)"},
        {"term": "〜使役受身（させられる）", "reading": "させられる", "meaning": "嫌々ながら他者に無理やり動作をさせられる。(causative-passive; forced to do)"},
        {"term": "〜お〜になる", "reading": "おになる", "meaning": "相手の動作を高めて敬意を示す最高位の尊敬語。(honorific expression)"},
        {"term": "〜お〜する", "reading": "おする", "meaning": "自分の動作をへりくだって相手に敬意を示す謙譲語。(humble expression)"},
        {"term": "〜てあげる", "reading": "てあげる", "meaning": "相手のために親切で行為をしてあげる。(do something for someone)"},
        {"term": "〜てもらう", "reading": "てもらう", "meaning": "相手にお願いして行為をしてもらう。(have someone do something for me)"},
        {"term": "〜てくれる", "reading": "てくれる", "meaning": "他者が自分のために好意で行為をしてくれる。(someone kindly does something for me)"},
        {"term": "〜たら", "reading": "たら", "meaning": "一般的な条件や、〜した後の確定事実を表す。(if / when (conditional))"},
        {"term": "〜なら", "reading": "なら", "meaning": "話題の提示や相手の話を前提とした条件を表す。(if it is the case that; speaking of)"},
        {"term": "〜ば", "reading": "ば", "meaning": "仮定条件や恒常的な法則を表す。(if (hypothetical condition))"},
        {"term": "〜と", "reading": "と", "meaning": "ある条件が満たされると必然的に次のことが起きる。(whenever; naturally follows that)"},
        {"term": "〜について", "reading": "について", "meaning": "話や思考の対象・テーマを表す。(about; regarding; concerning)"},
        {"term": "〜あいだ", "reading": "あいだ", "meaning": "ある事態が続いている時間全体を表す。(during; while (continuously))"},
        {"term": "〜あいだに", "reading": "あいだに", "meaning": "ある期間のうちの一瞬・特定時点で何かが起きること。(while; in the middle of)"},
        {"term": "〜までに", "reading": "までに", "meaning": "ある行為や期限の最終リミットを表す。(by; before (deadline))"},
        {"term": "〜ていく", "reading": "ていく", "meaning": "現在から未来へ向かう変化や、遠ざかる動作を表す。(go on doing; change into future)"},
        {"term": "〜てくる", "reading": "てくる", "meaning": "過去から現在までの継続や、出現・接近する動作を表す。(come to do; start doing; continue up to now)"},
        {"term": "〜方（かた）", "reading": "かた", "meaning": "動作の方法・やり方を表す（使い方、作り方）。(way of doing; manner)"},
        {"term": "〜始める", "reading": "はじめる", "meaning": "動作が開始されることを表す。(start doing ~)"},
        {"term": "〜終わる", "reading": "おわる", "meaning": "動作が最後まで終了することを表す。(finish doing ~)"},
        {"term": "〜続ける", "reading": "つづける", "meaning": "同じ動作や状態が中断せず継続することを表す。(continue doing ~)"},
        {"term": "〜直す", "reading": "なおす", "meaning": "より良い結果を目指してもう一度最初からやり直す。(redo; do over again)"},
        {"term": "〜出す", "reading": "だす", "meaning": "急に、あるいは勢いよく動作が開始されること（泣き出す、雨が降り出す）。(burst out; suddenly start)"},
        {"term": "〜ばかり", "reading": "ばかり", "meaning": "同じことばかり繰り返したり、限定する意味を表す。(only; nothing but)"}
    ]

    # 5. N5 Catalog (35 core patterns)
    N5_CATALOG = [
        {"term": "〜です / 〜だ", "reading": "です／だ", "meaning": "判断や断定を表す基本述語。(to be; copula)"},
        {"term": "〜ではありません / 〜じゃない", "reading": "ではありません／じゃない", "meaning": "名詞・な形容詞の否定形。(is not; negative copula)"},
        {"term": "〜ます / 〜ません", "reading": "ます／ません", "meaning": "動詞の丁寧語の肯定・否定表現。(polite verb present affirmative/negative)"},
        {"term": "〜ました / 〜ませんでした", "reading": "ました／ませんでした", "meaning": "動詞の丁寧語の過去形・過去否定形。(polite verb past affirmative/negative)"},
        {"term": "〜てください", "reading": "てください", "meaning": "相手に親切や丁寧にお願い・指示する表現。(please do ~)"},
        {"term": "〜ないでください", "reading": "ないでください", "meaning": "相手に〜しないよう丁寧にお願い・禁止する表現。(please do not do ~)"},
        {"term": "〜てもいい", "reading": "てもいい", "meaning": "相手からの許可や受容を表す。(may do ~; permission)"},
        {"term": "〜てはいけない", "reading": "てはいけない", "meaning": "規則や社会通念上、してはならない禁止を表す。(must not do ~; prohibition)"},
        {"term": "〜から（理由）", "reading": "から", "meaning": "話者の主観的な原因や理由を表す。(because; since)"},
        {"term": "〜から〜まで", "reading": "からまで", "meaning": "時間や場所の起点と終点を表す。(from ~ to ~)"},
        {"term": "〜ましょう", "reading": "ましょう", "meaning": "相手に一緒に行動しようと誘ったり、自ら進んで申し出る。(let's ~; shall I ~)"},
        {"term": "〜ましょうか", "reading": "ましょうか", "meaning": "相手への提案や、自分が手伝おうかと尋ねる。(shall we ~?; shall I help you with ~?)"},
        {"term": "〜たい", "reading": "たい", "meaning": "話者自身の希望や願望を表す。(want to do ~)"},
        {"term": "〜たくない", "reading": "たくない", "meaning": "話者自身の否定的な意向を表す。(do not want to do ~)"},
        {"term": "〜ている", "reading": "ている", "meaning": "今まさに動作が進行中であること、または結果の状態が残っていること。(is doing; state)"},
        {"term": "〜まえに", "reading": "まえに", "meaning": "ある動作や時間の前に別の行為を行うこと。(before doing ~)"},
        {"term": "〜あとで", "reading": "あとで", "meaning": "ある動作が終わった後で別の行為を行うこと。(after doing ~)"},
        {"term": "〜てから", "reading": "てから", "meaning": "前の動作が完了したことを確認してから次の動作に移る順序を表す。(after doing ~; sequence)"},
        {"term": "〜より〜のほうが", "reading": "よりのほうが", "meaning": "２つのものを比較して一方がより程度が高いことを表す。(A is more ~ than B)"},
        {"term": "〜の中で〜がいちばん", "reading": "のなかでがいちばん", "meaning": "あるグループや範囲の中で最高・最上であることを表す。(the most ~ among ...)"},
        {"term": "〜が好き / 嫌い", "reading": "がすき／きらい", "meaning": "感情や好みの対象を表す助詞「が」。(like / dislike ~)"},
        {"term": "〜が上手 / 下手", "reading": "がじょうず／へた", "meaning": "能力やスキルの高低の対象を表す助詞「が」。(good at / poor at ~)"},
        {"term": "〜がある / いる", "reading": "がある／いる", "meaning": "無生物（物・植物など）には「ある」、生物（人・動物）には「いる」を用いて存在を表す。(there is / exists)"},
        {"term": "〜へ行く / 来る / 帰る", "reading": "へいく／くる／かえる", "meaning": "移動の方向や目的地を表す助詞「へ」。(go / come / return to ~)"},
        {"term": "〜に会う", "reading": "にあう", "meaning": "相手と面会・対面する対象を表す助詞「に」。(meet with someone)"},
        {"term": "〜で（手段・場所）", "reading": "で", "meaning": "動作が行われる場所や、利用する交通手段・道具を表す助詞「で」。(by means of; at / in)"},
        {"term": "〜と（共同・並立）", "reading": "と", "meaning": "一緒に行動する相手や、名詞と名詞をすべて並べる助詞「と」。(together with; and)"},
        {"term": "〜も", "reading": "も", "meaning": "同じ事柄が当てはまることを表す助詞「も」。(also; too)"},
        {"term": "〜まだ / もう", "reading": "まだ／もう", "meaning": "未完了「まだ〜ていない」、完了「もう〜した」を表す副詞。(not yet / already)"},
        {"term": "〜どのくらい / いくら", "reading": "どのくらい／いくら", "meaning": "期間・時間・金額・数量を尋ねる疑問表現。(how much; how long)"},
        {"term": "〜ませんか", "reading": "ませんか", "meaning": "相手の意向を尊重しながら丁寧に誘う表現。(won't you ~?; would you like to ~?)"},
        {"term": "〜こと（名詞化）", "reading": "こと", "meaning": "動詞を名詞の形に変えて文の主語や目的にする。(doing ~; the act of)"},
        {"term": "〜ことができる", "reading": "ことができる", "meaning": "能力や状況において実行が可能であることを表す。(can do ~; able to do ~)"},
        {"term": "〜たことがある", "reading": "たことがある", "meaning": "過去にそのような経験をしたことがあることを表す。(have the experience of doing ~)"}
    ]

    # 6. Load JLPT similar grammar dict (917 entries)
    with open('database/jlpt_similar_grammar_dict.js', 'r', encoding='utf-8') as f:
        similar_raw = f.read().split('=', 1)[1].strip().rstrip(';')
    similar_dict = json.loads(similar_raw)

    all_entries = []
    seen_terms = set()

    # Priority 1: N2 core grammars (195 entries)
    for gid in sorted(n2_grammars.keys()):
        g = n2_grammars[gid]
        term = g['name']
        reading = g['reading']
        clean = clean_term(term)
        seen_terms.add(clean)
        all_entries.append({
            'term': term,
            'reading': reading,
            'meaning': f"【N2基本文法】{g['meaning_en']}",
            'level': "JLPT N2 文法",
            'levelClass': "n2",
            'levelCode': "N2",
            'n2_id': gid,
            'n2_name': term
        })

    # Priority 2: N1 Catalog (127 entries)
    for item in N1_CATALOG:
        clean = clean_term(item['term'])
        if clean in seen_terms:
            continue
        seen_terms.add(clean)
        all_entries.append({
            'term': item['term'],
            'reading': item['reading'],
            'meaning': item['meaning'],
            'level': "JLPT N1 文法",
            'levelClass': "n1",
            'levelCode': "N1"
        })

    # Priority 3: N3 Quiz Data (182 entries)
    for item in n3_quiz_data:
        g = item.get('grammar')
        clean = clean_term(g)
        if clean in seen_terms:
            continue
        seen_terms.add(clean)
        reading = N3_KANJI_READINGS.get(g, clean)
        all_entries.append({
            'term': g,
            'reading': reading,
            'meaning': item.get('meaning_en', ''),
            'level': "JLPT N3 文法",
            'levelClass': "n3",
            'levelCode': "N3"
        })

    # Priority 4: N4 Catalog (60 entries)
    for item in N4_CATALOG:
        clean = clean_term(item['term'])
        if clean in seen_terms:
            continue
        seen_terms.add(clean)
        all_entries.append({
            'term': item['term'],
            'reading': item['reading'],
            'meaning': item['meaning'],
            'level': "JLPT N4 文法",
            'levelClass': "n4",
            'levelCode': "N4"
        })

    # Priority 5: N5 Catalog (35 entries)
    for item in N5_CATALOG:
        clean = clean_term(item['term'])
        if clean in seen_terms:
            continue
        seen_terms.add(clean)
        all_entries.append({
            'term': item['term'],
            'reading': item['reading'],
            'meaning': item['meaning'],
            'level': "JLPT N5 文法",
            'levelClass': "n5",
            'levelCode': "N5"
        })

    # Priority 6: Similar/Related grammar expressions (917 entries)
    for k, v in similar_dict.items():
        clean_k = clean_term(k)
        m = v.get('meaning', '')
        r = v.get('reading', k)

        # Check if mapped to N2 grammar
        n2_id = None
        n2_name = None
        match_n2 = re.search(r'【関連文法】「([^」]+)」', m)
        if match_n2:
            target = match_n2.group(1)
            clean_target = clean_term(target)
            if clean_target in name_to_n2:
                n2_id = name_to_n2[clean_target]
                n2_name = target
        elif clean_k in name_to_n2:
            n2_id = name_to_n2[clean_k]
            n2_name = k

        level = "JLPT N2 関連表現"
        levelClass = "n2-rel"

        if clean_k in seen_terms:
            # If already added as core N1-N5 grammar, keep that entry but ensure n2_id is linked if relevant
            for entry in all_entries:
                if clean_term(entry['term']) == clean_k and n2_id and not entry.get('n2_id'):
                    entry['n2_id'] = n2_id
                    entry['n2_name'] = n2_name
            continue
        else:
            seen_terms.add(clean_k)

        all_entries.append({
            'term': k,
            'reading': r,
            'meaning': m,
            'level': level,
            'levelClass': levelClass,
            'levelCode': "N2",
            'n2_id': n2_id,
            'n2_name': n2_name
        })

    print(f"Total compiled JLPT grammar entries: {len(all_entries)}")

    output_path = 'database/jlpt_all_grammar_dict.js'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('// JLPT All Levels (N1-N5) Grammar & Expression Dictionary\n')
        f.write('// Auto-generated by scripts/build_all_grammar_dict.py\n')
        f.write('window.JLPT_ALL_GRAMMAR_DICT = ')
        f.write(json.dumps(all_entries, ensure_ascii=False, indent=2))
        f.write(';\n')

    print(f"Successfully generated {output_path} ({len(all_entries)} items).")

if __name__ == '__main__':
    main()
