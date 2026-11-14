# -*- coding: utf-8 -*-
"""
Comprehensive Ruby & Furigana Fixer for All Flashcards and Practice Tests
Fixes all compound word splitting errors (e.g. 洗濯物 as せんたくぶつ),
inverted rubies (つぎ with 次 rt), kanji-as-ruby bugs, and TTS phonetic misreadings.
"""

import os
import re

REPLACEMENTS = {
    # 1. 逆転ルビ修正
    "<ruby>つぎ<rt>次</rt></ruby>": "<ruby>次<rt>つぎ</rt></ruby>",
    
    # 2. 洗濯物・〜物（もの）の修正
    "<ruby>洗濯<rt>せんたく</rt></ruby><ruby>物<rt>ぶつ</rt></ruby>": "<ruby>洗濯物<rt>せんたくもの</rt></ruby>",
    "<ruby>洗濯<rt>せんたく</rt></ruby><ruby>物<rt>もの</rt></ruby>": "<ruby>洗濯物<rt>せんたくもの</rt></ruby>",
    "<ruby>洗濯物<rt>せんたくぶつ</rt></ruby>": "<ruby>洗濯物<rt>せんたくもの</rt></ruby>",
    "<ruby>生<rt>い</rt></ruby>き<ruby>物<rt>ぶつ</rt></ruby>": "<ruby>生き物<rt>いきもの</rt></ruby>",
    "<ruby>調<rt>しら</rt></ruby>べ<ruby>物<rt>ぶつ</rt></ruby>": "<ruby>調べ物<rt>しらべもの</rt></ruby>",
    "<ruby>探<rt>さが</rt></ruby>し<ruby>物<rt>ぶつ</rt></ruby>": "<ruby>探し物<rt>さがしもの</rt></ruby>",
    "<ruby>炒<rt>いた</rt></ruby>め<ruby>物<rt>ぶつ</rt></ruby>": "<ruby>炒め物<rt>いためもの</rt></ruby>",
    "<ruby>届<rt>とど</rt></ruby>け<ruby>物<rt>ぶつ</rt></ruby>": "<ruby>届け物<rt>とどけもの</rt></ruby>",
    "なくし<ruby>物<rt>ぶつ</rt></ruby>": "なくし<ruby>物<rt>もの</rt></ruby>",
    "たくさん<ruby>物<rt>ぶつ</rt></ruby>が入る": "たくさん<ruby>物<rt>もの</rt></ruby>が入る",
    "たくさん<ruby>物<rt>ぶつ</rt></ruby>が<ruby>入": "たくさん<ruby>物<rt>もの</rt></ruby>が<ruby>入",
    "<ruby>落<rt>お</rt></ruby>とし<ruby>物<rt>ぶつ</rt></ruby>": "<ruby>落とし物<rt>おとしもの</rt></ruby>",
    "<ruby>忘<rt>わす</rt></ruby>れ<ruby>物<rt>ぶつ</rt></ruby>": "<ruby>忘れ物<rt>わすれもの</rt></ruby>",
    "<ruby>買<rt>か</rt></ruby>い<ruby>物<rt>ぶつ</rt></ruby>": "<ruby>買い物<rt>かいもの</rt></ruby>",
    "<ruby>食<rt>た</rt></ruby>べ<ruby>物<rt>ぶつ</rt></ruby>": "<ruby>食べ物<rt>たべもの</rt></ruby>",
    "<ruby>飲<rt>の</rt></ruby>み<ruby>物<rt>ぶつ</rt></ruby>": "<ruby>飲み物<rt>のみもの</rt></ruby>",
    "<ruby>乗<rt>の</rt></ruby>り<ruby>物<rt>ぶつ</rt></ruby>": "<ruby>乗り物<rt>のりもの</rt></ruby>",
    "<ruby>建<rt>た</rt></ruby>て<ruby>物<rt>ぶつ</rt></ruby>": "<ruby>建物<rt>たてもの</rt></ruby>",
    "<ruby>建物<rt>たてぶつ</rt></ruby>": "<ruby>建物<rt>たてもの</rt></ruby>",
    "<ruby>果物<rt>くだぶつ</rt></ruby>": "<ruby>果物<rt>くだもの</rt></ruby>",
    "<ruby>着物<rt>きぶつ</rt></ruby>": "<ruby>着物<rt>きもの</rt></ruby>",
    "<ruby>着物<rt>ちゃくぶつ</rt></ruby>": "<ruby>着物<rt>きもの</rt></ruby>",
    "<ruby>荷物<rt>かぶつ</rt></ruby>": "<ruby>荷物<rt>にもつ</rt></ruby>",
    "<ruby>宝物<rt>たからぶつ</rt></ruby>": "<ruby>宝物<rt>たからもの</rt></ruby>",
    "<ruby>贈り物<rt>おくりぶつ</rt></ruby>": "<ruby>贈り物<rt>おくりもの</rt></ruby>",

    # 3. 「〜中」
    "<ruby>部屋<rt>へや</rt></ruby><ruby>中<rt>ちゅう</rt></ruby>": "<ruby>部屋中<rt>へやじゅう</rt></ruby>",
    "<ruby>部屋中<rt>へやちゅう</rt></ruby>": "<ruby>部屋中<rt>へやじゅう</rt></ruby>",
    "<ruby>世界<rt>せかい</rt></ruby><ruby>中<rt>ちゅう</rt></ruby>": "<ruby>世界中<rt>せかいじゅう</rt></ruby>",
    "<ruby>世界中<rt>せかいちゅう</rt></ruby>": "<ruby>世界中<rt>せかいじゅう</rt></ruby>",
    "<ruby>町<rt>まち</rt></ruby><ruby>中<rt>ちゅう</rt></ruby>": "<ruby>町中<rt>まちじゅう</rt></ruby>",
    "<ruby>町中<rt>まちちゅう</rt></ruby>": "<ruby>町中<rt>まちじゅう</rt></ruby>",
    "<ruby>一日<rt>いちにち</rt></ruby><ruby>中<rt>ちゅう</rt></ruby>": "<ruby>一日中<rt>いちにちじゅう</rt></ruby>",
    "<ruby>一日中<rt>いちにちちゅう</rt></ruby>": "<ruby>一日中<rt>いちにちじゅう</rt></ruby>",
    "<ruby>一年中<rt>いちねんちゅう</rt></ruby>": "<ruby>一年中<rt>いちねんじゅう</rt></ruby>",
    "<ruby>家中<rt>かちゅう</rt></ruby>": "<ruby>家中<rt>いえじゅう</rt></ruby>",
    "<ruby>夜中<rt>よちゅう</rt></ruby>": "<ruby>夜中<rt>よなか</rt></ruby>",

    # 4. 「人」
    "<ruby>社会<rt>しゃかい</rt></ruby><ruby>人<rt>ひと</rt></ruby>": "<ruby>社会人<rt>しゃかいじん</rt></ruby>",
    "<ruby>社会人<rt>しゃかいひと</rt></ruby>": "<ruby>社会人<rt>しゃかいじん</rt></ruby>",
    "<ruby>一<rt>いち</rt></ruby><ruby>人<rt>にん</rt></ruby>": "<ruby>一人<rt>ひとり</rt></ruby>",
    "<ruby>一人<rt>いちにん</rt></ruby>": "<ruby>一人<rt>ひとり</rt></ruby>",
    "<ruby>二<rt>に</rt></ruby><ruby>人<rt>にん</rt></ruby>": "<ruby>二人<rt>ふたり</rt></ruby>",
    "<ruby>二人<rt>ににん</rt></ruby>": "<ruby>二人<rt>ふたり</rt></ruby>",
    "お<ruby>二人<rt>ににん</rt></ruby>": "お<ruby>二人<rt>ふたり</rt></ruby>",
    "<ruby>大人<rt>だいじん</rt></ruby>": "<ruby>大人<rt>おとな</rt></ruby>",

    # 5. 「方」
    "<ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>ほう</rt></ruby>": "<ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>",
    "<ruby>行<rt>い</rt></ruby>き<ruby>方<rt>ほう</rt></ruby>": "<ruby>行<rt>い</rt></ruby>き<ruby>方<rt>かた</rt></ruby>",
    "<ruby>作<rt>つく</rt></ruby>り<ruby>方<rt>ほう</rt></ruby>": "<ruby>作<rt>つく</rt></ruby>り<ruby>方<rt>かた</rt></ruby>",
    "<ruby>読<rt>よ</rt></ruby>み<ruby>方<rt>ほう</rt></ruby>": "<ruby>読<rt>よ</rt></ruby>み<ruby>方<rt>かた</rt></ruby>",
    "<ruby>書<rt>か</rt></ruby>き<ruby>方<rt>ほう</rt></ruby>": "<ruby>書<rt>か</rt></ruby>き<ruby>方<rt>かた</rt></ruby>",
    "<ruby>話<rt>はな</rt></ruby>し<ruby>方<rt>ほう</rt></ruby>": "<ruby>話<rt>はな</rt></ruby>し<ruby>方<rt>かた</rt></ruby>",
    "<ruby>考<rt>かんが</rt></ruby>え<ruby>方<rt>ほう</rt></ruby>": "<ruby>考<rt>かんが</rt></ruby>え<ruby>方<rt>かた</rt></ruby>",
    "<ruby>食<rt>た</rt></ruby>べ<ruby>方<rt>ほう</rt></ruby>": "<ruby>食<rt>た</rt></ruby>べ<ruby>方<rt>かた</rt></ruby>",
    "<ruby>過<rt>す</rt></ruby>ごし<ruby>方<rt>ほう</rt></ruby>": "<ruby>過<rt>す</rt></ruby>ごし<ruby>方<rt>かた</rt></ruby>",
    "<ruby>教<rt>おし</rt></ruby>え<ruby>方<rt>ほう</rt></ruby>": "<ruby>教<rt>おし</rt></ruby>え<ruby>方<rt>かた</rt></ruby>",
    "<ruby>調<rt>しら</rt></ruby>べ<ruby>方<rt>ほう</rt></ruby>": "<ruby>調<rt>しら</rt></ruby>べ<ruby>方<rt>かた</rt></ruby>",
    "やり<ruby>方<rt>ほう</rt></ruby>": "やり<ruby>方<rt>かた</rt></ruby>",
    "見<ruby>方<rt>ほう</rt></ruby>": "見<ruby>方<rt>かた</rt></ruby>",
    "歩き<ruby>方<rt>ほう</rt></ruby>": "歩き<ruby>方<rt>かた</rt></ruby>",
    "使い方<rt>つかいほう</rt>": "使い方<rt>つかいかた</rt>",
    "作り方<rt>つくりほう</rt>": "作り方<rt>つくりかた</rt>",
    "やり方<rt>やりほう</rt>": "やり方<rt>やりかた</rt>",

    # 人を表す敬称「方（かた）」
    "くださった<ruby>方<rt>ほう</rt></ruby>": "くださった<ruby>方<rt>かた</rt></ruby>",
    "年配の<ruby>方<rt>ほう</rt></ruby>": "年配の<ruby>方<rt>かた</rt></ruby>",
    "<ruby>年配<rt>ねんぱい</rt></ruby>の<ruby>方<rt>ほう</rt></ruby>": "<ruby>年配<rt>ねんぱい</rt></ruby>の<ruby>方<rt>かた</rt></ruby>",
    "1番の<ruby>方<rt>ほう</rt></ruby>": "1番の<ruby>方<rt>かた</rt></ruby>",
    ">番<rt>ばん</rt></ruby>の<ruby>方<rt>ほう</rt></ruby>": ">番<rt>ばん</rt></ruby>の<ruby>方<rt>かた</rt></ruby>",
    "お知り合いの<ruby>方<rt>ほう</rt></ruby>": "お知り合いの<ruby>方<rt>かた</rt></ruby>",
    "y>合<rt>あ</rt></ruby>いの<ruby>方<rt>ほう</rt></ruby>": "y>合<rt>あ</rt></ruby>いの<ruby>方<rt>かた</rt></ruby>",
    "いらっしゃる<ruby>方<rt>ほう</rt></ruby>": "いらっしゃる<ruby>方<rt>かた</rt></ruby>",
    "追加の<ruby>方<rt>ほう</rt></ruby>": "追加の<ruby>方<rt>かた</rt></ruby>",
    "加<rt>ついか</rt></ruby>の<ruby>方<rt>ほう</rt></ruby>": "加<rt>ついか</rt></ruby>の<ruby>方<rt>かた</rt></ruby>",
    "ご希望の<ruby>方<rt>ほう</rt></ruby>": "ご希望の<ruby>方<rt>かた</rt></ruby>",
    "望<rt>きぼう</rt></ruby>の<ruby>方<rt>ほう</rt></ruby>": "望<rt>きぼう</rt></ruby>の<ruby>方<rt>かた</rt></ruby>",

    # 6. ルビタグ内に漢字が入っているバグ
    "<ruby>試着<rt>試着</rt></ruby>": "<ruby>試着<rt>しちゃく</rt></ruby>",
    "<ruby>試着室<rt>試着室</rt></ruby>": "<ruby>試着室<rt>しちゃくしつ</rt></ruby>",
    "<ruby>淹<rt>淹</rt></ruby>れて": "<ruby>淹<rt>い</rt></ruby>れて",
    "<ruby>淹<rt>淹</rt></ruby>れたて": "<ruby>淹<rt>い</rt></ruby>れたて",
    "<ruby>淹<rt>淹</rt></ruby>れる": "<ruby>淹<rt>い</rt></ruby>れる",
    "<ruby>癒<rt>癒</rt></ruby>やす": "<ruby>癒<rt>いや</rt></ruby>やす",
    "<ruby>癒<rt>癒</rt></ruby>やせる": "<ruby>癒<rt>いや</rt></ruby>やせる",
    "<ruby>癒<rt>癒</rt></ruby>やしたい": "<ruby>癒<rt>いや</rt></ruby>やしたい",
    "<ruby>癒<rt>癒</rt></ruby>やしたり": "<ruby>癒<rt>いや</rt></ruby>やしたり",
    "<ruby>頑<rt>頑</rt></ruby>なに": "<ruby>頑<rt>かたくな</rt></ruby>に",
    "<ruby>日<rt>ひ</rt></ruby><ruby>々<rt>々</rt></ruby>": "<ruby>日々<rt>ひび</rt></ruby>",
    "<ruby>花<rt>はな</rt></ruby><ruby>々<rt>々</rt></ruby>": "<ruby>花々<rt>はなばな</rt></ruby>",
    "<ruby>高<rt>だか</rt></ruby><ruby>々<rt>々</rt></ruby>": "<ruby>高々<rt>たかだか</rt></ruby>",
    "<ruby>高<rt>こう</rt></ruby><ruby>々<rt>々</rt></ruby>": "<ruby>高々<rt>たかだか</rt></ruby>",
    "<ruby>既<rt>すんで</rt></ruby><ruby>読<rt>読</rt></ruby>": "<ruby>既読<rt>きどく</rt></ruby>",
    "<ruby>筆<rt>ふで</rt></ruby><ruby>圧<rt>圧</rt></ruby>": "<ruby>筆圧<rt>ひつあつ</rt></ruby>",
    "４<ruby>択<rt>択</rt></ruby>": "４<ruby>択<rt>たく</rt></ruby>",
    "<ruby>従量制<rt>従量制</rt></ruby>": "<ruby>従量制<rt>じゅうりょうせい</rt></ruby>",
    "<ruby>蓄光石<rt>蓄光石</rt></ruby>": "<ruby>蓄光石<rt>ちっこうせき</rt></ruby>",
    "<ruby>営<rt>営</rt></ruby>い": "<ruby>営<rt>いとな</rt></ruby>い",
    "<ruby>名称<rt>めい称</rt></ruby>": "<ruby>名称<rt>めいしょう</rt></ruby>",
    "<ruby>協<rt>きょう</rt></ruby><ruby>働<rt>働</rt></ruby>": "<ruby>協働<rt>きょうどう</rt></ruby>",
    "<ruby>順<rt>じゅん</rt></ruby><ruby>従<rt>従</rt></ruby>": "<ruby>順従<rt>じゅんじゅう</rt></ruby>",
    "<ruby>諫<rt>諫</rt></ruby>める": "<ruby>諫<rt>いさ</rt></ruby>める",
    "<ruby>違<rt>違</rt></ruby>": "<ruby>違<rt>ちが</rt></ruby>",
    "<ruby>疲<rt>疲</rt></ruby>": "<ruby>疲<rt>つか</rt></ruby>",
    "<ruby>専<rt>専</rt></ruby>": "<ruby>専<rt>せん</rt></ruby>",
    "<ruby>巨<rt>巨</rt></ruby>": "<ruby>巨<rt>きょ</rt></ruby>",
    "<ruby>押<rt>押</rt></ruby>": "<ruby>押<rt>お</rt></ruby>",
    "<ruby>備<rt>備</rt></ruby>な": "<ruby>不備<rt>ふび</rt></ruby>な",
    "<ruby>釉薬<rt>釉薬</rt></ruby>": "<ruby>釉薬<rt>ゆうやく</rt></ruby>",
    "<ruby>催行人<rt>催行人</rt></ruby>": "<ruby>催行人<rt>さいこうにん</rt></ruby>",

    # 7. 明らかな誤読・文字化けバグ
    "<ruby>日本語<rt>にほんかたり</rt></ruby>": "<ruby>日本語<rt>にほんご</rt></ruby>",
    "<ruby>授業<rt>じっけん</rt></ruby>": "<ruby>授業<rt>じゅぎょう</rt></ruby>",
    "<ruby>練習<rt>れんしゅうする</rt></ruby>": "<ruby>練習<rt>れんしゅう</rt></ruby>",
    "<ruby>今<rt>いま</rt></ruby><ruby>手<rt>て</rt></ruby>が": "<ruby>今<rt>いま</rt></ruby>、<ruby>手<rt>て</rt></ruby>が",
    "<ruby>八百屋<rt>はっぴゃくや</rt></ruby>": "<ruby>八百屋<rt>やおや</rt></ruby>",
    "<ruby>床屋<rt>ゆかや</rt></ruby>": "<ruby>床屋<rt>とこや</rt></ruby>",
    "<ruby>部屋<rt>ぶや</rt></ruby>": "<ruby>部屋<rt>へや</rt></ruby>",
    "<ruby>時計<rt>じけい</rt></ruby>": "<ruby>時計<rt>とけい</rt></ruby>",
    "<ruby>眼鏡<rt>がんきょう</rt></ruby>": "<ruby>眼鏡<rt>めがね</rt></ruby>",
    "<ruby>今年<rt>こんねん</rt></ruby>": "<ruby>今年<rt>ことし</rt></ruby>",
    "<ruby>去年<rt>こねん</rt></ruby>": "<ruby>去年<rt>きょねん</rt></ruby>",
    "<ruby>今朝<rt>こんちょう</rt></ruby>": "<ruby>今朝<rt>けさ</rt></ruby>",
    "<ruby>夕方<rt>ゆうほう</rt></ruby>": "<ruby>夕方<rt>ゆうがた</rt></ruby>",
    "<ruby>二十日<rt>にじゅうにち</rt></ruby>": "<ruby>二十日<rt>はつか</rt></ruby>",
    "<ruby>十四日<rt>じゅうよんにち</rt></ruby>": "<ruby>十四日<rt>じゅうよっか</rt></ruby>",
    "<ruby>二十四日<rt>にじゅうよんにち</rt></ruby>": "<ruby>二十四日<rt>にじゅうよっか</rt></ruby>",
    "<ruby>上手<rt>じょうて</rt></ruby>": "<ruby>上手<rt>じょうず</rt></ruby>",
    "<ruby>下手<rt>したて</rt></ruby>": "<ruby>下手<rt>へた</rt></ruby>",
    "<ruby>苦手<rt>くしゅ</rt></ruby>": "<ruby>苦手<rt>にがて</rt></ruby>",
    "<ruby>苦手<rt>にがしゅ</rt></ruby>": "<ruby>苦手<rt>にがて</rt></ruby>",
    "ピリッと<ruby>辛<rt>つら</rt></ruby>い": "ピリッと<ruby>辛<rt>から</rt></ruby>い",
    "ピアノの<ruby>難曲<rt>なんきょく</rt></ruby>を<ruby>弾<rt>はじ</rt></ruby>き": "ピアノの<ruby>難曲<rt>なんきょく</rt></ruby>を<ruby>弾<rt>ひ</rt></ruby>き",
    "受付の<ruby>札<rt>さつ</rt></ruby>": "受付の<ruby>札<rt>ふだ</rt></ruby>",

    # 8. スラッシュ入りルビ
    "<ruby>十<rt>じゅう とお</rt></ruby>": "<ruby>十<rt>じゅう</rt></ruby>",
    "<ruby>四<rt>し / よん</rt></ruby>": "<ruby>四<rt>よん</rt></ruby>",
    "<ruby>何<rt>なん/なに</rt></ruby>してるの？": "<ruby>何<rt>なに</rt></ruby>してるの？",
    "<ruby>九<rt>きゅう / く</rt></ruby>時間": "<ruby>九<rt>く</rt></ruby>時間",
    "<ruby>七<rt>しち / なな</rt></ruby>転び八起き": "<ruby>七<rt>なな</rt></ruby>転び八起き",
    "<ruby>空<rt>あく / す</rt></ruby>く": "<ruby>空<rt>あ</rt></ruby>く",
    "<ruby>描<rt>かく / えが</rt></ruby>く": "<ruby>描<rt>えが</rt></ruby>く",
    "<ruby>抱<rt>だく / いだ</rt></ruby>く": "<ruby>抱<rt>いだ</rt></ruby>く",
    "<ruby>札<rt>さつ / ふだ</rt></ruby>": "<ruby>札<rt>ふだ</rt></ruby>",
    "<ruby>市場<rt>しじょう / いちば</rt></ruby>": "<ruby>市場<rt>しじょう</rt></ruby>",
    "<ruby>翌年<rt>よくとし / よくねん</rt></ruby>": "<ruby>翌年<rt>よくねん</rt></ruby>",
    "<ruby>留<rt>とめる / とど</rt></ruby>める": "<ruby>留<rt>とど</rt></ruby>める",
    "<ruby>留<rt>とまる / とど</rt></ruby>まる": "<ruby>留<rt>とど</rt></ruby>まる",
    "<ruby>弾<rt>ひく / はじ</rt></ruby>く": "<ruby>弾<rt>ひ</rt></ruby>く",
    "<ruby>辛<rt>からい / つら</rt></ruby>い": "<ruby>辛<rt>から</rt></ruby>い",
    "<ruby>手が空<rt>てがあく / す</rt></ruby>く": "<ruby>手<rt>て</rt></ruby>が<ruby>空<rt>あ</rt></ruby>く",
}

ROOT_DIRS = [
    '/Users/yamauchimiku/Documents/GitHub/japanese-learning',
    '/Users/yamauchimiku/.gemini/antigravity/scratch/japanese-flashcards'
]

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original = f.read()
    except Exception as e:
        return 0

    modified = original
    for target, repl in REPLACEMENTS.items():
        if target in modified:
            modified = modified.replace(target, repl)

    if modified != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(modified)
        return 1
    return 0

def main():
    total_modified = 0
    for root in ROOT_DIRS:
        if not os.path.exists(root):
            continue
        print(f"Scanning {root}...")
        for dirpath, dirnames, filenames in os.walk(root):
            if any(p in dirpath for p in ['.git', 'node_modules', '.gemini']):
                continue
            for f in filenames:
                if f.endswith(('.js', '.json', '.html')):
                    p = os.path.join(dirpath, f)
                    if process_file(p):
                        rel = os.path.relpath(p, root)
                        print(f"  Fixed: {rel}")
                        total_modified += 1

    print(f"\nDone! Modified {total_modified} files.")

if __name__ == '__main__':
    main()
