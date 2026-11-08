# -*- coding: utf-8 -*-
"""
Master Builder & 5-Perspective Verifier for JLPT N1 Mock Exams (Rounds 1 to 10, 1,060 Questions)
"""

import os
import sys
import re
import json

BASE_DIR = "/Users/yamauchimiku/Documents/GitHub/japanese-learning"
sys.path.insert(0, os.path.join(BASE_DIR, "scripts"))
sys.path.insert(0, os.path.join(BASE_DIR, "scripts/n1_rewrite"))
sys.path.insert(0, os.path.join(BASE_DIR, "scripts/mock_n1"))

from n1_lib import R as add_ruby
from sec1_data import SEC1_ROUNDS
from sec2_data import SEC2_ROUNDS
from sec3_data import SET1_QUESTIONS, SET2_QUESTIONS


def disambiguate_polyphones(p):
    p2 = p.replace("一日中", "{一日中|いちにちじゅう}")
    p2 = re.sub(r'(?<=月)([一1１]日)', r'{\1|ついたち}', p2)
    p2 = re.sub(r'(?<![0-9０-９一二三四五六七八九十月{])([一1１]日)', r'{\1|いちにち}', p2)
    p2 = re.sub(r'(?<![0-9０-９一二三四五六七八九十{])([一1１]人)', r'{\1|ひとり}', p2)
    p2 = re.sub(r'(?<![0-9０-９一二三四五六七八九十{])([二2２]人)', r'{\1|ふたり}', p2)
    p2 = re.sub(r'(?<![0-9０-９{])(20|２０|二十)歳', r'{\1歳|はたち}', p2)
    # 分 with kanji numerals
    p2 = (p2.replace("一分", "{一分|いっぷん}")
            .replace("二分", "{二分|にふん}")
            .replace("三分", "{三分|さんぷん}")
            .replace("四分", "{四分|よんぷん}")
            .replace("五分", "{五分|ごふん}")
            .replace("六分", "{六分|ろっぷん}")
            .replace("七分", "{七分|ななふん}")
            .replace("八分", "{八分|はっぷん}")
            .replace("九分", "{九分|きゅうふん}")
            .replace("十分", "{十分|じゅうぶん}")
            .replace("十五分", "{十五分|じゅうごふん}")
            .replace("二十分", "{二十分|にじゅっぷん}")
            .replace("三十分", "{三十分|さんじゅっぷん}")
            .replace("四十分", "{四十分|よんじゅっぷん}")
            .replace("五十分", "{五十分|ごじゅっぷん}")
            .replace("数分", "{数分|すうふん}")
            .replace("何分", "{何分|なんぷん}")
            .replace("半分", "{半分|はんぶん}")
            .replace("自分", "{自分|じぶん}")
            .replace("気分", "{気分|きぶん}")
            .replace("成分", "{成分|せいぶん}")
            .replace("部分", "{部分|ぶぶん}")
            .replace("分野", "{分野|ぶんや}")
            .replace("分別", "{分別|ぶんべつ}")
            .replace("分析", "{分析|ぶんせき}")
            .replace("分担", "{分担|ぶんたん}")
            .replace("分量", "{分量|ぶんりょう}")
            .replace("処分", "{処分|しょぶん}")
            .replace("配分", "{配分|はいぶん}")
            .replace("区分", "{区分|くぶん}")
            .replace("随分", "{随分|ずいぶん}")
            .replace("当分", "{当分|とうぶん}")
            .replace("余分", "{余分|よぶん}")
            .replace("分科会", "{分科会|ぶんかかい}")
            .replace("分子", "{分子|ぶんし}")
            .replace("分散", "{分散|ぶんさん}")
            .replace("分離", "{分離|ぶんり}")
            .replace("分解", "{分解|ぶんかい}")
            .replace("分岐", "{分岐|ぶんき}"))
    p2 = re.sub(r'([0-9０-９]+)分', r'\1{分|ふん}', p2)
    p2 = p2.replace("日用品", "{日用品|にちようひん}")
    p2 = p2.replace("日配品", "{日配品|にっぱいひん}")
    p2 = p2.replace("生い立ち", "{生い立ち|おいたち}")
    p2 = p2.replace("空室", "{空室|くうしつ}")
    p2 = p2.replace("日常生活", "{日常生活|にちじょうせいかつ}")
    p2 = p2.replace("日常", "{日常|にちじょう}")
    p2 = p2.replace("日頃", "{日頃|ひごろ}")
    p2 = p2.replace("日々", "{日々|ひび}")
    p2 = p2.replace("数日", "{数日|すうじつ}")
    p2 = p2.replace("後日", "{後日|ごじつ}")
    p2 = p2.replace("前日", "{前日|ぜんじつ}")
    p2 = p2.replace("当日", "{当日|とうじつ}")
    p2 = p2.replace("翌日", "{翌日|よくじつ}")
    p2 = p2.replace("祝日", "{祝日|しゅくじつ}")
    p2 = p2.replace("平日", "{平日|へいじつ}")
    p2 = p2.replace("休日", "{休日|きゅうじつ}")
    p2 = p2.replace("連日", "{連日|れんじつ}")
    p2 = p2.replace("終日", "{終日|しゅうじつ}")
    p2 = p2.replace("来日", "{来日|らいにち}")
    p2 = p2.replace("日時", "{日時|にちじ}")
    p2 = p2.replace("日程", "{日程|にってい}")
    p2 = p2.replace("日当たり", "{日当たり|ひあたり}")
    p2 = p2.replace("日陰", "{日陰|ひかげ}")
    p2 = p2.replace("日差し", "{日差し|ひざし}")
    p2 = p2.replace("日帰り", "{日帰り|ひがえり}")
    p2 = p2.replace("日記", "{日記|にっき}")
    p2 = p2.replace("日誌", "{日誌|にっし}")
    p2 = p2.replace("日課", "{日課|にっか}")
    p2 = p2.replace("日光", "{日光|にっこう}")
    p2 = p2.replace("日没", "{日没|にちぼつ}")
    p2 = p2.replace("日食", "{日食|にっしょく}")
    p2 = p2.replace("日中", "{日中|にっちゅう}")
    p2 = p2.replace("明後日", "{明後日|あさって}")
    # 開
    p2 = p2.replace("開室", "{開室|かいしつ}").replace("閉室", "{閉室|へいしつ}").replace("開架", "{開架|かいか}").replace("閉架", "{閉架|へいか}").replace("開演", "{開演|かいえん}").replace("開場", "{開場|かいじょう}").replace("開園", "{開園|かいえん}").replace("閉園", "{閉園|へいえん}").replace("開通", "{開通|かいつう}").replace("開拓", "{開拓|かいたく}")
    p2 = re.sub(r'((?:パーティー|会|会議|展覧会|発表会|コンサート|クラス|講座|イベント|ページ|本|教科書|辞書|扉|窓|店|傘|幕|差)を\s*)開([きくけこかい])', r'\1{開|ひら}\2', p2)
    p2 = re.sub(r'開かれる', r'{開|ひら}かれる', p2)
    p2 = re.sub(r'開かれた', r'{開|ひら}かれた', p2)
    p2 = re.sub(r'開けた場所', r'{開|ひら}けた場所', p2)
    p2 = re.sub(r'(?<![{一-龥])開([きくけこかい])', r'{開|あ}\1', p2)
    # 空
    p2 = re.sub(r'((?:お腹|おなか|道|電車|バス|店|席|手|時間|予定)が\s*)空([きくけこかい])', r'\1{空|す}\2', p2)
    p2 = re.sub(r'(?<![{])空([きくけこかい])', r'{空|あ}\1', p2)
    p2 = re.sub(r'(?<![{一-龥])空(?![一-龥}|きくけこかい])', r'{空|そら}', p2)
    # 辛
    p2 = re.sub(r'(?<![{一-龥])辛([いくかっさす])', r'{辛|から}\1', p2)
    # 生
    p2 = re.sub(r'年生', r'年{生|せい}', p2)
    p2 = p2.replace("生演奏", "{生|なま}演奏").replace("生け花", "{生|い}け花").replace("生命力", "{生命力|せいめいりょく}")
    p2 = re.sub(r'生データ', r'{生|なま}データ', p2)
    p2 = re.sub(r'(?<![{一-龥])生の', r'{生|なま}の', p2)
    p2 = re.sub(r'(?<![{一-龥])生で', r'{生|なま}で', p2)
    p2 = re.sub(r'(?<![{一-龥])生まれ', r'{生|う}まれ', p2)
    p2 = re.sub(r'(?<![{一-龥])生まれる', r'{生|う}まれる', p2)
    p2 = re.sub(r'(?<![{一-龥])生き', r'{生|い}き', p2)
    p2 = re.sub(r'(?<![{一-龥])生える', r'{生|は}える', p2)
    p2 = re.sub(r'(?<![{一-龥])生え', r'{生|は}え', p2)
    p2 = re.sub(r'(?<![{一-龥])生か([しさすせそ])', r'{生|い}か\1', p2)
    p2 = re.sub(r'(?<![{一-龥])生じる', r'{生|しょう}じる', p2)
    p2 = re.sub(r'(?<![{一-龥])生じ', r'{生|しょう}じ', p2)
    p2 = re.sub(r'(?<![{一-龥])生([むみんまめも])', r'{生|う}\1', p2)
    p2 = re.sub(r'生ごみ', r'{生|なま}ごみ', p2)
    p2 = re.sub(r'生ゴミ', r'{生|なま}ゴミ', p2)
    # 方
    p2 = re.sub(r'([一-龥ぁ-ん]+)方', lambda m: m.group(0) if m.group(1) in ('の', 'た', 'る', 'い', 'ない', 'この', 'その', 'あの', 'どの') else f"{m.group(1)}{{方|かた}}", p2)
    p2 = re.sub(r'(この|その|あの|どの|ご希望の|参加の|利用の|お持ちの|初めての|多くの|一般の|地域の|担当の)\s*方', r'\1{方|かた}', p2)
    p2 = re.sub(r'(?<![{一-龥])方(?![一-龥}|])', r'{方|ほう}', p2)
    p2 = re.sub(r'（日）', r'（{日|にち}）', p2)
    p2 = re.sub(r'(?<=[月火水木金土・、])日(?=[・、）\s]|$)', r'{日|にち}', p2)
    p2 = re.sub(r'(休館|休園|休業|定休|開催|実施|集合|出発|返却|利用|記念|運動|文化|ごみ|ゴミ|収集|開館|閉館|受付|締切|締め切り|提出|指定|検査|診察|休診|営業|発行|最終|公開|発売|放送|更新|作成|開始|終了|希望|購入|作業|候補|期限|来館|決定|予定|合格|設けた|決まった|晴れた|雨の|風の|寒い|暑い|暖かい|涼しい|次の|前の|その|この|あの|どの)日', r'\1{日|び}', p2)
    p2 = re.sub(r'(?<![{一-龥0-9０-９])日(?![一-龥0-9０-９}|])', r'{日|ひ}', p2)
    p2 = p2.replace("何で", "{何|なん}で")
    return p2


def ruby_preserving_tags(text):
    """Apply Janome+compound add_ruby while preserving HTML tags like <u>...</u>, <b>...</b>, <span...>...</span>, <br>."""
    if not text:
        return ""
    parts = re.split(r'(<[^>]+>)', text)
    out = []
    for p in parts:
        if p.startswith('<') and p.endswith('>'):
            out.append(p)
        else:
            p2 = disambiguate_polyphones(p)
            out.append(add_ruby(p2))
    return "".join(out)


def format_blank_sentence(sent, is_ruby=False):
    if is_ruby:
        s = ruby_preserving_tags(sent)
    else:
        s = sent
    s = s.replace("（　）", "（<span class='jlpt-underline-blank'></span>）")
    return s


def format_star_sentence(prefix, suffix, star_pos, is_ruby=False):
    slots = []
    for idx in range(1, 5):
        if idx == star_pos:
            slots.append("<span class='jlpt-underline-blank' style='text-align:center;font-weight:900;color:#127285;'>★</span>")
        else:
            slots.append("<span class='jlpt-underline-blank'></span>")
    slots_html = " ".join(slots)
    p = ruby_preserving_tags(prefix) if is_ruby else prefix
    sf = ruby_preserving_tags(suffix) if is_ruby else suffix
    return f"{p} {slots_html} {sf}".strip()


def make_options_4(correct, distractors, seed):
    idx = seed % 4
    d = list(distractors)
    opts = d[:idx] + [correct] + d[idx:]
    return opts, idx


def build_section_questions(round_num, sec1_src, sec2_src, sec3_pool):
    questions = []

    # --- SECTION 1: 言語知識（文字・語彙・文法） (Q1..Q45) ---
    # m1: 漢字読み (Q1..6, 6 items)
    for item in sec1_src["m1"]:
        q_num = item["qNum"]
        opts, c_idx = make_options_4(item["correct"], item["distractors"], round_num * 7 + q_num)
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec1",
            "subsectionId": "s1_m1",
            "category": "漢字読み",
            "qNum": q_num,
            "title": item["sentence"],
            "titleRuby": ruby_preserving_tags(item["sentence"]),
            "options": opts,
            "optionsRuby": opts,
            "correctIndex": c_idx,
            "weight": 1.0,
            "explanation": item["explanation"]
        })

    # m2: 文脈規定 (Q7..13, 7 items)
    for item in sec1_src["m2"]:
        q_num = item["qNum"]
        opts, c_idx = make_options_4(item["correct"], item["distractors"], round_num * 11 + q_num)
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec1",
            "subsectionId": "s1_m2",
            "category": "文脈規定",
            "qNum": q_num,
            "title": format_blank_sentence(item["sentence"], is_ruby=False),
            "titleRuby": format_blank_sentence(item["sentence"], is_ruby=True),
            "options": opts,
            "optionsRuby": [ruby_preserving_tags(o) for o in opts],
            "correctIndex": c_idx,
            "weight": 1.0,
            "explanation": item["explanation"]
        })

    # m3: 言い換え類義 (Q14..19, 6 items)
    for item in sec1_src["m3"]:
        q_num = item["qNum"]
        opts, c_idx = make_options_4(item["correct"], item["distractors"], round_num * 13 + q_num)
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec1",
            "subsectionId": "s1_m3",
            "category": "言い換え類義",
            "qNum": q_num,
            "title": item["sentence"],
            "titleRuby": ruby_preserving_tags(item["sentence"]),
            "options": opts,
            "optionsRuby": [ruby_preserving_tags(o) for o in opts],
            "correctIndex": c_idx,
            "weight": 1.0,
            "explanation": item["explanation"]
        })

    # m4: 用法 (Q20..25, 6 items)
    for item in sec1_src["m4"]:
        q_num = item["qNum"]
        opts, c_idx = make_options_4(item["correct"], item["distractors"], round_num * 17 + q_num)
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec1",
            "subsectionId": "s1_m4",
            "category": "用法",
            "qNum": q_num,
            "title": item["sentence"],
            "titleRuby": ruby_preserving_tags(item["sentence"]),
            "options": opts,
            "optionsRuby": [ruby_preserving_tags(o) for o in opts],
            "correctIndex": c_idx,
            "weight": 1.5,
            "explanation": item["explanation"]
        })

    # m5: 文法形式の判断 (Q26..35, 10 items)
    for item in sec1_src["m5"]:
        q_num = item["qNum"]
        opts, c_idx = make_options_4(item["correct"], item["distractors"], round_num * 19 + q_num)
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec1",
            "subsectionId": "s1_m5",
            "category": "文法形式の判断",
            "qNum": q_num,
            "title": format_blank_sentence(item["sentence"], is_ruby=False),
            "titleRuby": format_blank_sentence(item["sentence"], is_ruby=True),
            "options": opts,
            "optionsRuby": [ruby_preserving_tags(o) for o in opts],
            "correctIndex": c_idx,
            "weight": 1.2,
            "explanation": item["explanation"]
        })

    # m6: 文の組み立て ★ (Q36..40, 5 items)
    for item in sec1_src["m6"]:
        q_num = item["qNum"]
        star_pos = item["star_pos"]
        chunks = item["chunks"]
        correct_chunk = chunks[star_pos - 1]
        other_chunks = [c for i, c in enumerate(chunks) if i != (star_pos - 1)]
        opts, c_idx = make_options_4(correct_chunk, other_chunks, round_num * 23 + q_num)
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec1",
            "subsectionId": "s1_m6",
            "category": "文の組み立て",
            "qNum": q_num,
            "star_pos": star_pos,
            "title": format_star_sentence(item["prefix"], item["suffix"], star_pos, is_ruby=False),
            "titleRuby": format_star_sentence(item["prefix"], item["suffix"], star_pos, is_ruby=True),
            "options": opts,
            "optionsRuby": [ruby_preserving_tags(o) for o in opts],
            "correctIndex": c_idx,
            "weight": 1.5,
            "explanation": item["explanation"]
        })

    # m7: 文章の文法 (Q41..45, 5 items)
    m7_data = sec1_src["m7"]
    p_plain = m7_data["passage"]
    p_ruby = ruby_preserving_tags(p_plain).replace("\n", "<br>")
    for item in m7_data["items"]:
        q_num = item["qNum"]
        target = item["target"]
        opts, c_idx = make_options_4(item["correct"], item["distractors"], round_num * 29 + q_num)
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec1",
            "subsectionId": "s1_m7",
            "category": "文章の文法",
            "qNum": q_num,
            "passage": p_plain,
            "passageRuby": p_ruby,
            "title": f"空欄 {target} に入る最もよいものはどれですか。",
            "titleRuby": f"<ruby>空欄<rt>くうらん</rt></ruby> {target} に<ruby>入<rt>はい</rt></ruby>る<ruby>最<rt>もっと</rt></ruby>もよいものはどれですか。",
            "options": opts,
            "optionsRuby": [ruby_preserving_tags(o) for o in opts],
            "correctIndex": c_idx,
            "weight": 1.5,
            "explanation": item["explanation"]
        })

    # --- SECTION 2: 読解 (Q46..Q71, 26 questions) ---
    # m1: 内容理解（短文） (Q46..49, 4 items)
    for item in sec2_src["m1"]:
        q_num = item["qNum"]
        p_plain = item["passage"]
        ev_plain = item["evidence"]
        ev_ruby = ruby_preserving_tags(ev_plain)
        p_ruby = ruby_preserving_tags(p_plain).replace("\n", "<br>")
        opts, c_idx = make_options_4(item["correct"], item["distractors"], round_num * 31 + q_num)
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec2",
            "subsectionId": "s2_m1",
            "category": "内容理解（短文）",
            "qNum": q_num,
            "passage": p_plain,
            "passageRuby": p_ruby,
            "evidence": ev_ruby,
            "evidencePlain": ev_plain,
            "title": item["question"],
            "titleRuby": ruby_preserving_tags(item["question"]),
            "options": opts,
            "optionsRuby": [ruby_preserving_tags(o) for o in opts],
            "correctIndex": c_idx,
            "weight": 2.0,
            "explanation": item["explanation"]
        })

    # m2: 内容理解（中文） (Q50..58, 3 passages x 3 questions = 9 items)
    m2_list = sec2_src["m2"]
    if isinstance(m2_list, dict):
        m2_list = [m2_list]
    for m2_data in m2_list:
        p_plain = m2_data["passage"]
        p_ruby = ruby_preserving_tags(p_plain).replace("\n", "<br>")
        for item in m2_data["items"]:
            q_num = item["qNum"]
            ev_plain = item["evidence"]
            ev_ruby = ruby_preserving_tags(ev_plain)
            opts, c_idx = make_options_4(item["correct"], item["distractors"], round_num * 37 + q_num)
            questions.append({
                "id": len(questions) + 1,
                "sectionId": "sec2",
                "subsectionId": "s2_m2",
                "category": "内容理解（中文）",
                "qNum": q_num,
                "passage": p_plain,
                "passageRuby": p_ruby,
                "evidence": ev_ruby,
                "evidencePlain": ev_plain,
                "title": item["question"],
                "titleRuby": ruby_preserving_tags(item["question"]),
                "options": opts,
                "optionsRuby": [ruby_preserving_tags(o) for o in opts],
                "correctIndex": c_idx,
                "weight": 2.2,
                "explanation": item["explanation"]
            })

    # m3: 内容理解（長文） (Q59..62, 1 passage x 4 questions = 4 items)
    m3_data = sec2_src["m3"]
    p_plain = m3_data["passage"]
    p_ruby = ruby_preserving_tags(p_plain).replace("\n", "<br>")
    for item in m3_data["items"]:
        q_num = item["qNum"]
        ev_plain = item["evidence"]
        ev_ruby = ruby_preserving_tags(ev_plain)
        opts, c_idx = make_options_4(item["correct"], item["distractors"], round_num * 41 + q_num)
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec2",
            "subsectionId": "s2_m3",
            "category": "内容理解（長文）",
            "qNum": q_num,
            "passage": p_plain,
            "passageRuby": p_ruby,
            "evidence": ev_ruby,
            "evidencePlain": ev_plain,
            "title": item["question"],
            "titleRuby": ruby_preserving_tags(item["question"]),
            "options": opts,
            "optionsRuby": [ruby_preserving_tags(o) for o in opts],
            "correctIndex": c_idx,
            "weight": 2.5,
            "explanation": item["explanation"]
        })

    # m4: 統合理解 (Q63..65, 1 A/B passage x 3 questions = 3 items)
    m4_data = sec2_src["m4"]
    p_plain = m4_data["passage"]
    p_ruby = ruby_preserving_tags(p_plain).replace("\n", "<br>")
    for item in m4_data["items"]:
        q_num = item["qNum"]
        ev_plain = item["evidence"]
        ev_ruby = ruby_preserving_tags(ev_plain)
        opts, c_idx = make_options_4(item["correct"], item["distractors"], round_num * 43 + q_num)
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec2",
            "subsectionId": "s2_m4",
            "category": "統合理解",
            "qNum": q_num,
            "passage": p_plain,
            "passageRuby": p_ruby,
            "evidence": ev_ruby,
            "evidencePlain": ev_plain,
            "title": item["question"],
            "titleRuby": ruby_preserving_tags(item["question"]),
            "options": opts,
            "optionsRuby": [ruby_preserving_tags(o) for o in opts],
            "correctIndex": c_idx,
            "weight": 2.5,
            "explanation": item["explanation"]
        })

    # m5: 主張理解（長文） (Q66..69, 1 passage x 4 questions = 4 items)
    m5_data = sec2_src["m5"]
    p_plain = m5_data["passage"]
    p_ruby = ruby_preserving_tags(p_plain).replace("\n", "<br>")
    for item in m5_data["items"]:
        q_num = item["qNum"]
        ev_plain = item["evidence"]
        ev_ruby = ruby_preserving_tags(ev_plain)
        opts, c_idx = make_options_4(item["correct"], item["distractors"], round_num * 47 + q_num)
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec2",
            "subsectionId": "s2_m5",
            "category": "主張理解（長文）",
            "qNum": q_num,
            "passage": p_plain,
            "passageRuby": p_ruby,
            "evidence": ev_ruby,
            "evidencePlain": ev_plain,
            "title": item["question"],
            "titleRuby": ruby_preserving_tags(item["question"]),
            "options": opts,
            "optionsRuby": [ruby_preserving_tags(o) for o in opts],
            "correctIndex": c_idx,
            "weight": 2.8,
            "explanation": item["explanation"]
        })

    # m6: 情報検索 (Q70..71, 1 passage x 2 questions = 2 items)
    m6_data = sec2_src["m6"]
    p_plain = m6_data["passage"]
    p_ruby = ruby_preserving_tags(p_plain).replace("\n", "<br>")
    for item in m6_data["items"]:
        q_num = item["qNum"]
        ev_plain = item["evidence"]
        ev_ruby = ruby_preserving_tags(ev_plain)
        opts, c_idx = make_options_4(item["correct"], item["distractors"], round_num * 53 + q_num)
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec2",
            "subsectionId": "s2_m6",
            "category": "情報検索",
            "qNum": q_num,
            "passage": p_plain,
            "passageRuby": p_ruby,
            "evidence": ev_ruby,
            "evidencePlain": ev_plain,
            "title": item["question"],
            "titleRuby": ruby_preserving_tags(item["question"]),
            "options": opts,
            "optionsRuby": [ruby_preserving_tags(o) for o in opts],
            "correctIndex": c_idx,
            "weight": 2.5,
            "explanation": item["explanation"]
        })

    # --- SECTION 3: 聴解 (Q72..Q106, 35 questions) ---
    for l_item in sec3_pool:
        q_num = l_item["qNum"]
        sub_id = l_item["subsectionId"]
        orig_opts = list(l_item["options"])
        orig_cidx = l_item["correctIndex"]
        # Rotate options for s3_m1, s3_m2, s3_m3, s3_m5 in rounds > 1 (do NOT rotate s3_m4 即時応答 since choices are read in audio)
        if sub_id in ("s3_m1", "s3_m2", "s3_m3", "s3_m5") and round_num > 1:
            shift = (round_num + q_num) % len(orig_opts)
            opts = orig_opts[shift:] + orig_opts[:shift]
            c_idx = (orig_cidx - shift) % len(orig_opts)
        else:
            opts = orig_opts
            c_idx = orig_cidx

        script_plain = l_item["script"]
        script_ruby = ruby_preserving_tags(script_plain).replace("\n", "<br>")
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec3",
            "subsectionId": sub_id,
            "category": l_item["category"],
            "qNum": q_num,
            "has_illustration": True,
            "illustration_url": l_item["illustration_url"],
            "audioUrl": l_item["audioUrl"],
            "title": l_item["title"],
            "titleRuby": ruby_preserving_tags(l_item["title"]),
            "script": script_plain,
            "scriptRuby": script_ruby,
            "options": opts,
            "optionsRuby": [ruby_preserving_tags(o) for o in opts],
            "correctIndex": c_idx,
            "weight": 1.8,
            "explanation": l_item["explanation"]
        })

    return questions


def select_listening_pool(round_num):
    if round_num == 1:
        return SET1_QUESTIONS
    elif round_num == 2:
        return SET2_QUESTIONS
    else:
        pool = []
        for idx in range(35):
            use_set2 = ((round_num * 3 + idx * 5) % 2 == 1)
            pool.append(SET2_QUESTIONS[idx] if use_set2 else SET1_QUESTIONS[idx])
        return pool


N1_SECTIONS_META = [
    {
        "id": "sec1",
        "title": "言語知識（文字・語彙・文法）",
        "titleEn": "Language Knowledge (Vocabulary & Grammar)",
        "timeMinutes": 55,
        "maxScore": 60,
        "subsections": [
            {
                "id": "s1_m1",
                "number": "問題1",
                "name": "漢字読み",
                "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
                "instructionEn": "Choose the best reading of the underlined word from 1, 2, 3, or 4."
            },
            {
                "id": "s1_m2",
                "number": "問題2",
                "name": "文脈規定",
                "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
                "instructionEn": "Choose the best word to fill in the parentheses ( ) in the context."
            },
            {
                "id": "s1_m3",
                "number": "問題3",
                "name": "言い換え類義",
                "instruction": "＿＿の言葉に意味が最も近いものを、１・２・３・４から一つ選びなさい。",
                "instructionEn": "Which word or phrase has almost the same meaning as the underlined expression?"
            },
            {
                "id": "s1_m4",
                "number": "問題4",
                "name": "用法",
                "instruction": "次の言葉の使い方として最もよいものを、１・２・３・４から一つ選びなさい。",
                "instructionEn": "Choose the sentence that uses the given word in the most natural way."
            },
            {
                "id": "s1_m5",
                "number": "問題5",
                "name": "文法形式の判断",
                "instruction": "次の文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
                "instructionEn": "Choose the best grammatical form to go into the parentheses ( )."
            },
            {
                "id": "s1_m6",
                "number": "問題6",
                "name": "文の組み立て",
                "instruction": "次の文の ★ に入る最もよいものを、１・２・３・４から一つ選びなさい。",
                "instructionEn": "Which word goes into the ★ slot when ordering the four choices to make a natural sentence?"
            },
            {
                "id": "s1_m7",
                "number": "問題7",
                "name": "文章の文法",
                "instruction": "次の文章を読んで、文章全体の趣旨を踏まえて、［41］から［45］の中に入る最もよいものを、１・２・３・４から一つ選びなさい。",
                "instructionEn": "Read the passage and choose the best expression for each blank [41] to [45]."
            }
        ]
    },
    {
        "id": "sec2",
        "title": "読解",
        "titleEn": "Reading Comprehension",
        "timeMinutes": 55,
        "maxScore": 60,
        "subsections": [
            {
                "id": "s2_m1",
                "number": "問題8",
                "name": "内容理解（短文）",
                "instruction": "次の文章を読んで、後の問いに対する答えとして最もよいものを、１・２・３・４から一つ選びなさい。",
                "instructionEn": "Read the short passages and choose the best answer to each question."
            },
            {
                "id": "s2_m2",
                "number": "問題9",
                "name": "内容理解（中文）",
                "instruction": "次の文章を読んで、後の問いに対する答えとして最もよいものを、１・２・３・４から一つ選びなさい。",
                "instructionEn": "Read the medium-length passages and answer the questions below."
            },
            {
                "id": "s2_m3",
                "number": "問題10",
                "name": "内容理解（長文）",
                "instruction": "次の文章を読んで、後の問いに対する答えとして最もよいものを、１・２・３・４から一つ選びなさい。",
                "instructionEn": "Read the long passage and answer the questions below."
            },
            {
                "id": "s2_m4",
                "number": "問題11",
                "name": "統合理解",
                "instruction": "次のAとBの文章を読んで、後の問いに対する答えとして最もよいものを、１・２・３・４から一つ選びなさい。",
                "instructionEn": "Read both passages A and B and choose the best answer to each question."
            },
            {
                "id": "s2_m5",
                "number": "問題12",
                "name": "主張理解（長文）",
                "instruction": "次の文章を読んで、後の問いに対する答えとして最もよいものを、１・２・３・４から一つ選びなさい。",
                "instructionEn": "Read the long opinion passage and answer the questions below."
            },
            {
                "id": "s2_m6",
                "number": "問題13",
                "name": "情報検索",
                "instruction": "右のページを見て、下の問いに対する答えとして最もよいものを、１・２・３・４から一つ選びなさい。",
                "instructionEn": "Look at the information notice and choose the best answer to each question."
            }
        ]
    },
    {
        "id": "sec3",
        "title": "聴解",
        "titleEn": "Listening Comprehension",
        "timeMinutes": 60,
        "maxScore": 60,
        "subsections": [
            {
                "id": "s3_m1",
                "number": "問題1",
                "name": "課題理解",
                "instruction": "まず質問を聞いてください。それから話を聞いて、問題用紙の１から４の中から、最もよいものを一つ選んでください。",
                "instructionEn": "First listen to the question. Then listen to the conversation and choose the best answer from 1 to 4."
            },
            {
                "id": "s3_m2",
                "number": "問題2",
                "name": "ポイント理解",
                "instruction": "まず質問を聞いてください。そのあと、問題用紙のせんたくしを読んでください。読む時間があります。それから話を聞いて、問題用紙の１から４の中から、最もよいものを一つ選んでください。",
                "instructionEn": "First listen to the question. Then read the choices and listen to the conversation."
            },
            {
                "id": "s3_m3",
                "number": "問題3",
                "name": "概要理解",
                "instruction": "問題用紙に何も印刷されていません。この問題は、全体としてどんな内容かを聞く問題です。話の前に質問はありません。まず話を聞いてください。それから、質問とせんたくしを聞いて、１から４の中から、最もよいものを一つ選んでください。",
                "instructionEn": "Listen to the talk first, then listen to the question and choices to select the best answer."
            },
            {
                "id": "s3_m4",
                "number": "問題4",
                "name": "即時応答",
                "instruction": "問題用紙に何も印刷されていません。まず文を聞いてください。それから、それに対する返事を聞いて、１から３の中から、最もよいものを一つ選んでください。",
                "instructionEn": "Listen to the short statement and choose the best response from 1 to 3."
            },
            {
                "id": "s3_m5",
                "number": "問題5",
                "name": "統合理解",
                "instruction": "まず話を聞いてください。それから、質問とせんたくしを聞いて、１から４の中から、最もよいものを一つ選んでください。",
                "instructionEn": "Listen to the discussion and choose the best answer from 1 to 4."
            }
        ]
    }
]


def build_all_rounds():
    rounds_obj = {}
    for r in range(1, 11):
        sec1_src = SEC1_ROUNDS[r]
        sec2_src = SEC2_ROUNDS[r]
        sec3_pool = select_listening_pool(r)
        qs = build_section_questions(r, sec1_src, sec2_src, sec3_pool)
        sections_meta = json.loads(json.dumps(N1_SECTIONS_META))
        for sec in sections_meta:
            sec["name"] = sec["title"]
            for sub in sec["subsections"]:
                sub["desc"] = sub["instruction"]
                sub["count"] = sum(1 for q in qs if q["subsectionId"] == sub["id"])
        rounds_obj[str(r)] = {
            "level": "N1",
            "round": r,
            "title": f"JLPT N1 実戦模擬試験（第{r}回）",
            "totalQuestions": len(qs),
            "totalTimeMinutes": 170,
            "passScore": 100,
            "maxTotalScore": 180,
            "benchmarks": {
                "lang": 19,
                "reading": 19,
                "listening": 19
            },
            "sections": sections_meta,
            "questions": qs
        }
    return rounds_obj


def audit_all_rounds(rounds_obj):
    print("=== Running 5-Perspective Quality Audit on N1 Mock Exams (10 Rounds, 1,060 Questions) ===")
    errors = []
    banned_words = ["公式", "準拠", "Google", "Neural2", "LINE", "Zoom", "YouTube", "Netflix", "Amazon", "Facebook", "Twitter", "Instagram", "TikTok"]
    all_written_titles = {}

    for r_str, r_data in rounds_obj.items():
        qs = r_data["questions"]
        if len(qs) != 106:
            errors.append(f"Round {r_str}: expected 106 questions, got {len(qs)}")

        star_counts = {1: 0, 2: 0, 3: 0, 4: 0}
        ans_counts = {0: 0, 1: 0, 2: 0, 3: 0}

        for q in qs:
            q_id = f"R{r_str}_Q{q['qNum']}"
            c_idx = q["correctIndex"]
            ans_counts[c_idx] = ans_counts.get(c_idx, 0) + 1

            opts = q["options"]
            if len(set(opts)) != len(opts):
                errors.append(f"{q_id}: duplicate options {opts}")
            if not (0 <= c_idx < len(opts)):
                errors.append(f"{q_id}: invalid correctIndex {c_idx} for {len(opts)} options")

            if q["subsectionId"] == "s1_m6":
                sp = q.get("star_pos")
                if sp not in (1, 2, 3, 4):
                    errors.append(f"{q_id}: invalid star_pos {sp}")
                else:
                    star_counts[sp] += 1

            if q["sectionId"] in ("sec1", "sec2") and q["subsectionId"] not in ("s1_m7", "s2_m2", "s2_m3", "s2_m4", "s2_m5", "s2_m6"):
                norm_title = re.sub(r"<[^>]+>", "", q["title"]).strip()
                key = f"{q['subsectionId']}::{norm_title}"
                if key in all_written_titles:
                    errors.append(f"Duplicate written question across rounds: {q_id} matches {all_written_titles[key]} -> {norm_title}")
                else:
                    all_written_titles[key] = q_id

            if q["sectionId"] == "sec3":
                audio_rel = q.get("audioUrl", "")
                illus_rel = q.get("illustration_url", "")
                if not os.path.exists(os.path.join(BASE_DIR, audio_rel)):
                    errors.append(f"{q_id}: missing audio file {audio_rel}")
                if not os.path.exists(os.path.join(BASE_DIR, illus_rel)):
                    errors.append(f"{q_id}: missing illustration file {illus_rel}")
                if re.search(r'(?:^|[\s「（『。！？\n：])あ、', q.get("script", "")):
                    errors.append(f"{q_id}: contains banned 'あ、' in listening script")

            blob = json.dumps(q, ensure_ascii=False)
            for bw in banned_words:
                if bw in blob:
                    errors.append(f"{q_id}: contains banned word '{bw}'")

        if any(v == 0 for v in star_counts.values()):
            errors.append(f"Round {r_str}: unbalanced star positions {star_counts}")

        print(f"  Round {r_str}: {len(qs)} Qs | Answer dist: {ans_counts} | Star pos dist: {star_counts}")

    if errors:
        print("ERRORS FOUND:")
        for e in errors[:30]:
            print("  -", e)
        sys.exit(1)
    print("=== All 10 Rounds (1,060 Questions) Passed 5-Perspective Audit with ZERO Errors! ===")


def main():
    rounds_obj = build_all_rounds()
    audit_all_rounds(rounds_obj)

    rounds_js = "// JLPT N1 実戦模擬試験 全10回データ (自動生成・5視点検証済み)\n"
    rounds_js += "window.JLPT_N1_MOCK_ROUNDS = " + json.dumps(rounds_obj, ensure_ascii=False, indent=2) + ";\n"
    rounds_js += "window.JLPT_N1_MOCK_DATA = window.JLPT_N1_MOCK_ROUNDS['1'];\n"

    r1_js = "// JLPT N1 実戦模擬試験 第1回データ\n"
    r1_js += "window.JLPT_N1_MOCK_DATA = " + json.dumps(rounds_obj["1"], ensure_ascii=False, indent=2) + ";\n"

    for rel_dir in ("database", "public/database"):
        out_rounds = os.path.join(BASE_DIR, rel_dir, "jlpt_n1_mock_rounds.js")
        out_data = os.path.join(BASE_DIR, rel_dir, "jlpt_n1_mock_data.js")
        with open(out_rounds, "w", encoding="utf-8") as f:
            f.write(rounds_js)
        with open(out_data, "w", encoding="utf-8") as f:
            f.write(r1_js)
        print(f"Wrote {out_rounds} and {out_data}")


if __name__ == "__main__":
    main()
