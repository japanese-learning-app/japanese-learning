#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates database/keigo_i18n_data.js with complete natural translations in 6 languages.
"""
import json
import re
from pathlib import Path

ROOT = Path("/Users/yamauchimiku/Documents/GitHub/japanese-learning")
step2_raw = json.loads((ROOT / "scripts/step2_raw.json").read_text(encoding="utf-8"))
step3_raw = json.loads((ROOT / "scripts/step3_raw.json").read_text(encoding="utf-8"))

def build_i18n():
    db_step2 = {}
    
    # 28 curated questions translations
    for q in step2_raw:
        qid = q["id"]
        choices_i18n = []
        for i, c in enumerate(q["choices"]):
            r = c["reason"]
            is_ok = c["isCorrect"]
            
            # Smart natural translation mapper based on reason text and question id
            en, zht, zhh, zhc, ko, fr = translate_reason(qid, i, r, is_ok)
            choices_i18n.append({
                "en": en,
                "zh-TW": zht,
                "zh-HK": zhh,
                "zh-CN": zhc,
                "ko": ko,
                "fr": fr
            })
            
        note_en, note_zht, note_zhh, note_zhc, note_ko, note_fr = translate_note(qid, q["note"])
        db_step2[qid] = {
            "choices": choices_i18n,
            "note": {
                "en": note_en,
                "zh-TW": note_zht,
                "zh-HK": note_zhh,
                "zh-CN": note_zhc,
                "ko": note_ko,
                "fr": note_fr
            }
        }
        
    db_sits = {}
    for s in step3_raw["sits"]:
        sid = s["id"]
        ng_en, ng_zht, ng_zhh, ng_zhc, ng_ko, ng_fr = translate_sit_ng(sid, s["ngTrap"])
        exp_en, exp_zht, exp_zhh, exp_zhc, exp_ko, exp_fr = translate_sit_exp(sid, s["explanation"])
        db_sits[sid] = {
            "ngTrap": {"en": ng_en, "zh-TW": ng_zht, "zh-HK": ng_zhh, "zh-CN": ng_zhc, "ko": ng_ko, "fr": ng_fr},
            "explanation": {"en": exp_en, "zh-TW": exp_zht, "zh-HK": exp_zhh, "zh-CN": exp_zhc, "ko": exp_ko, "fr": exp_fr}
        }
        
    db_emails = {}
    for e in step3_raw["emails"]:
        eid = e["id"]
        exp_en, exp_zht, exp_zhh, exp_zhc, exp_ko, exp_fr = translate_email_exp(eid, e["explanation"])
        db_emails[eid] = {
            "explanation": {"en": exp_en, "zh-TW": exp_zht, "zh-HK": exp_zhh, "zh-CN": exp_zhc, "ko": exp_ko, "fr": exp_fr}
        }
        
    return db_step2, db_sits, db_emails

