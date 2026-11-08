# -*- coding: utf-8 -*-
"""
Master Builder & 5-Perspective Verifier for JLPT N5 Mock Exams (Rounds 1 to 10, 910 Questions)
"""

import os
import sys
import re
import json

BASE_DIR = "/Users/yamauchimiku/Documents/GitHub/japanese-learning"
sys.path.insert(0, os.path.join(BASE_DIR, "scripts"))
sys.path.insert(0, os.path.join(BASE_DIR, "scripts/n1_rewrite"))
sys.path.insert(0, os.path.join(BASE_DIR, "scripts/mock_n5"))

from n1_lib import R as add_ruby
from round1_data import ROUND1_SEC1, ROUND1_SEC2
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
    p2 = p2.replace("五分", "{五分|ごふん}").replace("十分", "{十分|じゅっぷん}").replace("十五分", "{十五分|じゅうごふん}").replace("三十分", "{三十分|さんじゅっぷん}")
    # 開
    p2 = re.sub(r'((?:パーティー|会|クラス|講座|イベント|ページ|本|教科書|辞書)を\s*)開([きくけこかい])', r'\1{開|ひら}\2', p2)
    p2 = re.sub(r'(?<![{一-龥])開([きくけこかい])', r'{開|あ}\1', p2)
    # 空
    p2 = re.sub(r'((?:お腹|おなか|道|電車|バス|店)が\s*)空([きくけこかい])', r'\1{空|す}\2', p2)
    p2 = re.sub(r'(?<![{一-龥])空([きくけこかい])', r'{空|あ}\1', p2)
    p2 = re.sub(r'(?<![{一-龥])空(?![一-龥}|きくけこかい])', r'{空|そら}', p2)
    # 辛
    p2 = re.sub(r'(?<![{一-龥])辛([いくかっ])', r'{辛|から}\1', p2)
    # 生
    p2 = re.sub(r'(?<![{一-龥])生まれ', r'{生|う}まれ', p2)
    p2 = re.sub(r'(?<![{一-龥])生き', r'{生|い}き', p2)
    p2 = re.sub(r'(?<![{一-龥])生える', r'{生|は}える', p2)
    p2 = re.sub(r'(?<![{一-龥])生え', r'{生|は}え', p2)
    # 方
    p2 = re.sub(r'([一-龥ぁ-ん]+)方', lambda m: m.group(0) if m.group(1) in ('の', 'た', 'る', 'い', 'ない', 'この', 'その', 'あの', 'どの') else f"{m.group(1)}{{方|かた}}", p2)
    p2 = re.sub(r'(この|その|あの|どの|ご希望の|参加の|利用の)\s*方', r'\1{方|かた}', p2)
    p2 = re.sub(r'(?<![{一-龥])方(?![一-龥}|])', r'{方|ほう}', p2)
    p2 = re.sub(r'（日）', r'（{日|にち}）', p2)
    p2 = re.sub(r'(?<=[月火水木金土・、])日(?=[・、）\s]|$)', r'{日|にち}', p2)
    p2 = re.sub(r'(休館|休園|休業|定休|開催|実施|集合|出発|返却|利用|記念|運動|文化|ごみ|ゴミ|収集)日', r'\1{日|び}', p2)
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
    """Convert （　） to （<span class='jlpt-underline-blank'></span>） with optional ruby on surrounding text."""
    if is_ruby:
        s = ruby_preserving_tags(sent)
    else:
        s = sent
    s = s.replace("（　）", "（<span class='jlpt-underline-blank'></span>）")
    return s


def format_star_sentence(prefix, suffix, star_pos, is_ruby=False):
    """Build 4-slot star sentence with ★ at star_pos (1..4)."""
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
    """Deterministically place `correct` at index `seed % 4` among `distractors`."""
    idx = seed % 4
    d = list(distractors)
    opts = d[:idx] + [correct] + d[idx:]
    return opts, idx


def build_section_questions(round_num, sec1_src, sec2_src, sec3_pool):
    questions = []

    # --- SECTION 1: 文字・語彙 (Q1..Q35) ---
    # m1: 漢字読み (Q1..12)
    for item in sec1_src["m1"]:
        q_num = item["qNum"]
        opts, c_idx = make_options_4(item["correct"], item["distractors"], round_num * 7 + q_num)
        title_plain = item["sentence"]
        # For Kanji reading, keep target kanji un-rubied in title, and rubied in titleRuby (after submission)
        title_ruby = ruby_preserving_tags(item["sentence"])
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec1",
            "subsectionId": "s1_m1",
            "category": "漢字読み",
            "qNum": q_num,
            "title": title_plain,
            "titleRuby": title_ruby,
            "options": opts,
            "optionsRuby": opts,
            "correctIndex": c_idx,
            "weight": 1.0,
            "explanation": item["explanation"]
        })

    # m2: 表記 (Q13..20)
    for item in sec1_src["m2"]:
        q_num = item["qNum"]
        opts, c_idx = make_options_4(item["correct"], item["distractors"], round_num * 11 + q_num)
        title_plain = item["sentence"]
        title_ruby = ruby_preserving_tags(item["sentence"])
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec1",
            "subsectionId": "s1_m2",
            "category": "表記",
            "qNum": q_num,
            "title": title_plain,
            "titleRuby": title_ruby,
            "options": opts,
            "optionsRuby": opts,
            "correctIndex": c_idx,
            "weight": 1.0,
            "explanation": item["explanation"]
        })

    # m3: 文脈規定 (Q21..30)
    for item in sec1_src["m3"]:
        q_num = item["qNum"]
        opts, c_idx = make_options_4(item["correct"], item["distractors"], round_num * 13 + q_num)
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec1",
            "subsectionId": "s1_m3",
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

    # m4: 言い換え類義 (Q31..35)
    for item in sec1_src["m4"]:
        q_num = item["qNum"]
        opts, c_idx = make_options_4(item["correct"], item["distractors"], round_num * 17 + q_num)
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec1",
            "subsectionId": "s1_m4",
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

    # --- SECTION 2: 文法・読解 (Q36..Q67) ---
    # m1: 文法形式の判断 (Q36..51)
    for item in sec2_src["m1"]:
        q_num = item["qNum"]
        opts, c_idx = make_options_4(item["correct"], item["distractors"], round_num * 19 + q_num)
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec2",
            "subsectionId": "s2_m1",
            "category": "文法形式の判断",
            "qNum": q_num,
            "title": format_blank_sentence(item["sentence"], is_ruby=False),
            "titleRuby": format_blank_sentence(item["sentence"], is_ruby=True),
            "options": opts,
            "optionsRuby": [ruby_preserving_tags(o) for o in opts],
            "correctIndex": c_idx,
            "weight": 1.5,
            "explanation": item["explanation"]
        })

    # m2: 文の組み立て ★ (Q52..56)
    for item in sec2_src["m2"]:
        q_num = item["qNum"]
        star_pos = item["star_pos"]  # 1..4
        chunks = item["chunks"]      # 4 chunks in correct grammatical order
        correct_chunk = chunks[star_pos - 1]
        other_chunks = [c for i, c in enumerate(chunks) if i != (star_pos - 1)]
        opts, c_idx = make_options_4(correct_chunk, other_chunks, round_num * 23 + q_num)
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec2",
            "subsectionId": "s2_m2",
            "category": "文の組み立て",
            "qNum": q_num,
            "star_pos": star_pos,
            "title": format_star_sentence(item["prefix"], item["suffix"], star_pos, is_ruby=False),
            "titleRuby": format_star_sentence(item["prefix"], item["suffix"], star_pos, is_ruby=True),
            "options": opts,
            "optionsRuby": [ruby_preserving_tags(o) for o in opts],
            "correctIndex": c_idx,
            "weight": 2.0,
            "explanation": item["explanation"]
        })

    # m3: 文章の文法 (Q57..61)
    m3_data = sec2_src["m3"]
    p_plain = m3_data["passage"]
    p_ruby = ruby_preserving_tags(p_plain).replace("\n", "<br>")
    for item in m3_data["items"]:
        q_num = item["qNum"]
        target = item["target"]
        opts, c_idx = make_options_4(item["correct"], item["distractors"], round_num * 29 + q_num)
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec2",
            "subsectionId": "s2_m3",
            "category": "文章の文法",
            "qNum": q_num,
            "passage": p_plain,
            "passageRuby": p_ruby,
            "title": f"空欄 {target} に 入る ものは どれですか。",
            "titleRuby": f"<ruby>空欄<rt>くうらん</rt></ruby> {target} に <ruby>入<rt>はい</rt></ruby>る ものは どれですか。",
            "options": opts,
            "optionsRuby": [ruby_preserving_tags(o) for o in opts],
            "correctIndex": c_idx,
            "weight": 2.0,
            "explanation": item["explanation"]
        })

    # m4: 内容理解（短文） (Q62..64)
    for item in sec2_src["m4"]:
        q_num = item["qNum"]
        p_plain = item["passage"]
        ev_plain = item["evidence"]
        ev_ruby = ruby_preserving_tags(ev_plain)
        # Ensure ev_ruby appears inside p_ruby for highlight
        p_ruby = ruby_preserving_tags(p_plain).replace("\n", "<br>")
        opts, c_idx = make_options_4(item["correct"], item["distractors"], round_num * 31 + q_num)
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec2",
            "subsectionId": "s2_m4",
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
            "weight": 3.0,
            "explanation": item["explanation"]
        })

    # m5: 内容理解（中文） (Q65..66)
    m5_data = sec2_src["m5"]
    p_plain = m5_data["passage"]
    p_ruby = ruby_preserving_tags(p_plain).replace("\n", "<br>")
    for item in m5_data["items"]:
        q_num = item["qNum"]
        ev_plain = item["evidence"]
        ev_ruby = ruby_preserving_tags(ev_plain)
        opts, c_idx = make_options_4(item["correct"], item["distractors"], round_num * 37 + q_num)
        questions.append({
            "id": len(questions) + 1,
            "sectionId": "sec2",
            "subsectionId": "s2_m5",
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
            "weight": 3.5,
            "explanation": item["explanation"]
        })

    # m6: 情報検索 (Q67)
    m6_item = sec2_src["m6"]
    q_num = m6_item["qNum"]
    p_plain = m6_item["passage"]
    p_ruby = ruby_preserving_tags(p_plain).replace("\n", "<br>")
    ev_plain = m6_item["evidence"]
    ev_ruby = ruby_preserving_tags(ev_plain)
    opts, c_idx = make_options_4(m6_item["correct"], m6_item["distractors"], round_num * 41 + q_num)
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
        "title": m6_item["question"],
        "titleRuby": ruby_preserving_tags(m6_item["question"]),
        "options": opts,
        "optionsRuby": [ruby_preserving_tags(o) for o in opts],
        "correctIndex": c_idx,
        "weight": 4.0,
        "explanation": m6_item["explanation"]
    })

    # --- SECTION 3: 聴解 (Q68..Q91) ---
    for l_item in sec3_pool:
        q_num = l_item["qNum"]
        sub_id = l_item["subsectionId"]
        orig_opts = list(l_item["options"])
        orig_cidx = l_item["correctIndex"]
        # For s3_m1 and s3_m2 (where options are not read aloud in the audio), shift options per round to balance correctIndex
        if sub_id in ("s3_m1", "s3_m2") and round_num > 1:
            shift = (round_num + q_num) % len(orig_opts)
            opts = orig_opts[shift:] + orig_opts[:shift]
            c_idx = (orig_cidx - shift) % len(orig_opts)
        else:
            # For s3_m3 and s3_m4, options 1, 2, 3 are read aloud in the audio, so keep exact option order!
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
            "weight": 2.5,
            "explanation": l_item["explanation"]
        })

    return questions


def select_listening_pool(round_num):
    """Select 24 listening questions for `round_num` from SET1_QUESTIONS and SET2_QUESTIONS."""
    if round_num == 1:
        return SET1_QUESTIONS
    elif round_num == 2:
        return SET2_QUESTIONS
    else:
        pool = []
        for idx in range(24):
            # Deterministically interleave Set 1 and Set 2 per round and question
            use_set2 = ((round_num * 3 + idx * 5) % 2 == 1)
            pool.append(SET2_QUESTIONS[idx] if use_set2 else SET1_QUESTIONS[idx])
        return pool


N5_SECTIONS_META = [
    {
        "id": "sec1",
        "title": "言語知識（文字・語彙）",
        "titleEn": "Language Knowledge (Vocabulary)",
        "timeMinutes": 20,
        "maxScore": 60,
        "subsections": [
            {
                "id": "s1_m1",
                "number": "問題1",
                "name": "漢字読み",
                "instruction": "<ruby>＿＿<rt></rt></ruby>の　ことばは　ひらがなで　どう　かきますか。１・２・３・４から　いちばん　いい　ものを　ひとつ　えらんで　ください。",
                "instructionEn": "How do you write the underlined word in hiragana? Choose the best one from 1, 2, 3, or 4."
            },
            {
                "id": "s1_m2",
                "number": "問題2",
                "name": "表記",
                "instruction": "<ruby>＿＿<rt></rt></ruby>の　ことばは　どう　かきますか。１・２・３・４から　いちばん　いい　ものを　ひとつ　えらんで　ください。",
                "instructionEn": "How do you write the underlined word? Choose the best one from 1, 2, 3, or 4."
            },
            {
                "id": "s1_m3",
                "number": "問題3",
                "name": "文脈規定",
                "instruction": "（　）に　なにを　いれますか。１・２・３・４から　いちばん　いい　ものを　ひとつ　えらんで　ください。",
                "instructionEn": "What goes into the parentheses ( )? Choose the best one from 1, 2, 3, or 4."
            },
            {
                "id": "s1_m4",
                "number": "問題4",
                "name": "言い換え類義",
                "instruction": "<ruby>＿＿<rt></rt></ruby>の　ぶんと　だいたい　おなじ　いみの　ぶんが　あります。１・２・３・４から　いちばん　いい　ものを　ひとつ　えらんで　ください。",
                "instructionEn": "Which sentence has almost the same meaning as the given sentence? Choose the best one from 1, 2, 3, or 4."
            }
        ]
    },
    {
        "id": "sec2",
        "title": "言語知識（文法）・読解",
        "titleEn": "Language Knowledge (Grammar) & Reading",
        "timeMinutes": 40,
        "maxScore": 60,
        "subsections": [
            {
                "id": "s2_m1",
                "number": "問題1",
                "name": "文法形式の判断",
                "instruction": "（　）に　なにを　いれますか。１・２・３・４から　いちばん　いい　ものを　ひとつ　えらんで　ください。",
                "instructionEn": "What goes into the parentheses ( )? Choose the best one from 1, 2, 3, or 4."
            },
            {
                "id": "s2_m2",
                "number": "問題2",
                "name": "文の組み立て",
                "instruction": "★に　はいる　ものは　どれですか。１・２・３・４から　いちばん　いい　ものを　ひとつ　えらんで　ください。",
                "instructionEn": "Which word goes into the ★ slot when ordering the four choices to make a natural sentence?"
            },
            {
                "id": "s2_m3",
                "number": "問題3",
                "name": "文章の文法",
                "instruction": "<ruby>つぎ<rt>次</rt></ruby>の　ぶんしょうを　よんで、［57］から［61］の　なかに　はいる　いちばん　いい　ものを　１・２・３・４から　ひとつ　えらんで　ください。",
                "instructionEn": "Read the following passage and choose the best word for each blank [57] to [61]."
            },
            {
                "id": "s2_m4",
                "number": "問題4",
                "name": "内容理解（短文）",
                "instruction": "<ruby>つぎ<rt>次</rt></ruby>の　ぶんしょうを　よんで、しつもんに　こたえて　ください。こたえは　１・２・３・４から　いちばん　いい　ものを　ひとつ　えらんで　ください。",
                "instructionEn": "Read the short passages and choose the best answer to the question."
            },
            {
                "id": "s2_m5",
                "number": "問題5",
                "name": "内容理解（中文）",
                "instruction": "<ruby>つぎ<rt>次</rt></ruby>の　ぶんしょうを　よんで、しつもんに　こたえて　ください。こたえは　１・２・３・４から　いちばん　いい　ものを　ひとつ　えらんで　ください。",
                "instructionEn": "Read the medium-length passage and answer the questions below."
            },
            {
                "id": "s2_m6",
                "number": "問題6",
                "name": "情報検索",
                "instruction": "みぎの　おしらせを　みて、しつもんに　こたえて　ください。こたえは　１・２・３・４から　いちばん　いい　ものを　ひとつ　えらんで　ください。",
                "instructionEn": "Look at the notice and choose the best answer to the question."
            }
        ]
    },
    {
        "id": "sec3",
        "title": "聴解",
        "titleEn": "Listening Comprehension",
        "timeMinutes": 30,
        "maxScore": 60,
        "subsections": [
            {
                "id": "s3_m1",
                "number": "問題1",
                "name": "課題理解",
                "instruction": "はじめに　しつもんを　きいて　ください。それから　はなしを　きいて、もんだいようしの　１から　４の　なかから、いちばん　いい　ものを　ひとつ　えらんで　ください。",
                "instructionEn": "First listen to the question. Then listen to the conversation and choose the best answer from 1 to 4."
            },
            {
                "id": "s3_m2",
                "number": "問題2",
                "name": "ポイント理解",
                "instruction": "はじめに　しつもんを　きいて　ください。それから　はなしを　きいて、もんだいようしの　１から　４の　なかから、いちばん　いい　ものを　ひとつ　えらんで　ください。",
                "instructionEn": "First listen to the question. Then listen to the conversation and choose the best answer."
            },
            {
                "id": "s3_m3",
                "number": "問題3",
                "name": "発話表現",
                "instruction": "えを　みながら　しつもんを　きいて　ください。やじるしの　ひとは　なんと　いいますか。１から　３の　なかから、いちばん　いい　ものを　ひとつ　えらんで　ください。",
                "instructionEn": "Look at the picture and listen. What does the person say? Choose the best one from 1 to 3."
            },
            {
                "id": "s3_m4",
                "number": "問題4",
                "name": "即時応答",
                "instruction": "えなどが　ありません。ぶんを　きいて、１から　３の　なかから、いちばん　いい　ものを　ひとつ　えらんで　ください。",
                "instructionEn": "Listen to the short statement and choose the best response from 1 to 3."
            }
        ]
    }
]


def build_all_rounds():
    rounds_obj = {}
    for r in range(1, 11):
        sec1_src = ROUND1_SEC1 if r == 1 else SEC1_ROUNDS[r]
        sec2_src = ROUND1_SEC2 if r == 1 else SEC2_ROUNDS[r]
        sec3_pool = select_listening_pool(r)
        qs = build_section_questions(r, sec1_src, sec2_src, sec3_pool)
        rounds_obj[str(r)] = {
            "level": "N5",
            "round": r,
            "title": f"JLPT N5 実戦模擬試験（第{r}回）",
            "totalTimeMinutes": 90,
            "passScore": 80,
            "maxTotalScore": 180,
            "benchmarks": {
                "langReading": 38,
                "listening": 19
            },
            "sections": N5_SECTIONS_META,
            "questions": qs
        }
    return rounds_obj


def audit_all_rounds(rounds_obj):
    print("=== Running 5-Perspective Quality Audit on N5 Mock Exams (10 Rounds, 910 Questions) ===")
    errors = []
    banned_words = ["公式", "準拠", "Google", "Neural2", "LINE", "Zoom", "YouTube", "Netflix", "Amazon", "Facebook", "Twitter", "Instagram", "TikTok"]
    all_written_titles = {}

    for r_str, r_data in rounds_obj.items():
        qs = r_data["questions"]
        if len(qs) != 91:
            errors.append(f"Round {r_str}: expected 91 questions, got {len(qs)}")

        star_counts = {1: 0, 2: 0, 3: 0, 4: 0}
        ans_counts = {0: 0, 1: 0, 2: 0, 3: 0}

        for q in qs:
            q_id = f"R{r_str}_Q{q['qNum']}"
            c_idx = q["correctIndex"]
            ans_counts[c_idx] = ans_counts.get(c_idx, 0) + 1

            # Check options length & uniqueness
            opts = q["options"]
            if len(set(opts)) != len(opts):
                errors.append(f"{q_id}: duplicate options {opts}")
            if not (0 <= c_idx < len(opts)):
                errors.append(f"{q_id}: invalid correctIndex {c_idx} for {len(opts)} options")

            # Check star position
            if q["subsectionId"] == "s2_m2":
                sp = q.get("star_pos")
                if sp not in (1, 2, 3, 4):
                    errors.append(f"{q_id}: invalid star_pos {sp}")
                else:
                    star_counts[sp] += 1

            # Check written uniqueness across rounds
            if q["sectionId"] in ("sec1", "sec2") and q["subsectionId"] != "s2_m3":
                norm_title = re.sub(r"<[^>]+>", "", q["title"]).strip()
                key = f"{q['subsectionId']}::{norm_title}"
                if key in all_written_titles:
                    errors.append(f"Duplicate written question across rounds: {q_id} matches {all_written_titles[key]} -> {norm_title}")
                else:
                    all_written_titles[key] = q_id

            # Check audio & illustration existence for sec3
            if q["sectionId"] == "sec3":
                audio_rel = q.get("audioUrl", "")
                illus_rel = q.get("illustration_url", "")
                if not os.path.exists(os.path.join(BASE_DIR, audio_rel)):
                    errors.append(f"{q_id}: missing audio file {audio_rel}")
                if not os.path.exists(os.path.join(BASE_DIR, illus_rel)):
                    errors.append(f"{q_id}: missing illustration file {illus_rel}")
                if re.search(r'(?<![ゃャ])あ、', q.get("script", "")):
                    errors.append(f"{q_id}: contains banned 'あ、' in listening script")

            # Check banned terms
            blob = json.dumps(q, ensure_ascii=False)
            for bw in banned_words:
                if bw in blob:
                    errors.append(f"{q_id}: contains banned word '{bw}'")

        # Ensure all 4 star positions are used in each round's 5 star questions
        if any(v == 0 for v in star_counts.values()):
            errors.append(f"Round {r_str}: unbalanced star positions {star_counts}")

        print(f"  Round {r_str}: {len(qs)} Qs | Answer dist: {ans_counts} | Star pos dist: {star_counts}")

    if errors:
        print("ERRORS FOUND:")
        for e in errors[:30]:
            print("  -", e)
        sys.exit(1)
    print("=== All 10 Rounds (910 Questions) Passed 5-Perspective Audit with ZERO Errors! ===")


def main():
    rounds_obj = build_all_rounds()
    audit_all_rounds(rounds_obj)

    rounds_js = "// JLPT N5 実戦模擬試験 全10回データ (自動生成・5視点検証済み)\n"
    rounds_js += "window.JLPT_N5_MOCK_ROUNDS = " + json.dumps(rounds_obj, ensure_ascii=False, indent=2) + ";\n"
    rounds_js += "window.JLPT_N5_MOCK_DATA = window.JLPT_N5_MOCK_ROUNDS['1'];\n"

    r1_js = "// JLPT N5 実戦模擬試験 第1回データ\n"
    r1_js += "window.JLPT_N5_MOCK_DATA = " + json.dumps(rounds_obj["1"], ensure_ascii=False, indent=2) + ";\n"

    for rel_dir in ("database", "public/database"):
        out_rounds = os.path.join(BASE_DIR, rel_dir, "jlpt_n5_mock_rounds.js")
        out_data = os.path.join(BASE_DIR, rel_dir, "jlpt_n5_mock_data.js")
        with open(out_rounds, "w", encoding="utf-8") as f:
            f.write(rounds_js)
        with open(out_data, "w", encoding="utf-8") as f:
            f.write(r1_js)
        print(f"Wrote {out_rounds} and {out_data}")


if __name__ == "__main__":
    main()

