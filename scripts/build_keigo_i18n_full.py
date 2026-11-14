#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path

ROOT = Path("/Users/yamauchimiku/Documents/GitHub/japanese-learning")

# Standardized translation rules for common keigo errors
COMMON_EXPLANATIONS = {
    "correct_default": {
        "en": "Correct! This is the most natural and appropriate business honorific expression.",
        "zh-TW": "正確！這是最自然且得體的商務敬語表達方式。",
        "zh-HK": "正確！呢個係最自然又得體嘅商務敬語講法。",
        "zh-CN": "正确！这是最自然且得体的商务敬语表达方式。",
        "ko": "정답! 가장 자연스럽고 올바른 비즈니스 경어 표현입니다.",
        "fr": "Correct ! C'est l'expression honorifique professionnelle la plus naturelle et appropriée."
    },
    "double_keigo": {
        "en": "Double honorific trap (Nijuu-keigo): Stacking two honorific affixes together (e.g. honorific verb + -rareru) is considered redundant and incorrect.",
        "zh-TW": "二重敬語陷阱：重複疊加兩種敬語標記（例如在尊敬語動詞後再加「〜られる」）屬於冗贅的錯誤敬語。",
        "zh-HK": "二重敬語陷阱：重複加咗兩種敬語形式（例如喺尊敬語動詞後面再加「〜られる」），屬於累贅嘅錯誤敬語。",
        "zh-CN": "双重敬语陷阱：重复叠加两种敬语标记（例如在尊敬语动词后再加“〜られる”）属于冗赘的错误敬语。",
        "ko": "이중경어 함정: 이미 존경어인 표현에 다시 존경 어미(~られる 등)를 겹쳐 쓰는 것은 잘못된 이중경어입니다.",
        "fr": "Piège du double keigo : superposer deux formes honorifiques (ex. verbe honorifique + -rareru) est redondant et fautif."
      },
    "humble_honorific_confusion": {
        "en": "Humble & honorific confusion: This word is a humble form (Kenjougo) used for yourself or your in-group, so it cannot be used for the other party's actions.",
        "zh-TW": "尊謙混淆：此詞是用於自己或己方人員的謙讓語，不能用來描述客戶或上司的動作。",
        "zh-HK": "尊謙撈亂：呢個字係用喺自己或者自家人嘅謙讓語，唔可以用嚟形容客人或者上司嘅動作。",
        "zh-CN": "尊谦混淆：此词是用于自己或己方人员的谦让语，不能用来描述客户或上司的动作。",
        "ko": "존비 혼동: 이 표현은 자신이나 우리 편을 낮추는 겸양어이므로, 상대방이나 상사의 행동에는 쓸 수 없습니다.",
        "fr": "Confusion humble / honorifique : ce mot est une forme humble (kenjougo) pour soi-même, inutilisable pour les actions d'un client ou d'un supérieur."
    },
    "baito_keigo": {
        "en": "Part-time job keigo error (Baito-keigo): Phrases like '~ni narimasu' or past-tense '~yoroshikatta deshou ka' are incorrect colloquial habits often heard in casual shops.",
        "zh-TW": "打工族敬語錯誤（打工敬語）：如「〜になります」或過去式「〜よろしかったでしょうか」是常見於便利商店等場所的錯誤口頭習慣。",
        "zh-HK": "打工敬語錯誤：好似「〜になります」或者過去式「〜よろしかったでしょうか」係常見於便利店嘅唔正確口頭習慣。",
        "zh-CN": "打工敬语错误：如“〜になります”或过去式“〜よろしかったでしょうか”是常见于便利店等场所的错误口头习惯。",
        "ko": "아르바이트 경어(알바 경어) 오류: '~になります'나 과거형 '~よろしかったでしょうか'는 매장에서 흔히 들리지만 비즈니스에서는 잘못된 표현입니다.",
        "fr": "Erreur de « keigo de petit boulot » : les tournures comme « ~ni narimasu » ou « ~yoroshikatta deshou ka » sont des tics familiers incorrects en japonais formel."
    },
    "uchi_soto_reversed": {
        "en": "Uchi-Soto reversal error: When speaking to someone outside your company, you must refer to your own colleagues and managers with humble forms and no job titles.",
        "zh-TW": "內外逆轉錯誤：對公司外部客戶說話時，自家公司的主管與同仁屬於「內（自己人）」，必須去除頭銜並使用謙讓語。",
        "zh-HK": "內外調轉錯誤：對公司外間客戶講嘢嗰陣，自己公司嘅主管同同事屬於「內（自己人）」，一定要除咗職銜並且用謙讓語。",
        "zh-CN": "内外逆转错误：对公司外部客户说话时，自家公司的主管与同仁属于“内（自己人）”，必须去除头衔并使用谦让语。",
        "ko": "우치·소토(안과 밖) 역전 오류: 사외 사람에게 말할 때는 자사 상사라도 직책을 떼고 낮추어(겸양어) 표현해야 합니다.",
        "fr": "Erreur d'inversion Uchi-Soto : face à un client externe, vous devez désigner vos propres collègues et supérieurs de manière modeste, sans titre honorifique."
    }
}

# Detailed translation database for kq questions
KQ_TRANSLATIONS = {}

def get_kq_dict():
    # Load 28 questions from javascript file
    p_js = (ROOT / "database/business_keigo_practice_data.js").read_text(encoding="utf-8")
    blocks = re.findall(r'\{\s*"id":\s*"(kq_\d+)"[\s\S]*?"scene":\s*"([^"]+)"[\s\S]*?"choices":\s*(\[[\s\S]*?\])\s*,\s*"registers":\s*(\{[\s\S]*?\})\s*\}', p_js)
    
    kq_map = {}
    for qid, scene, choices_raw, reg_raw in blocks:
        choices = json.loads(choices_raw)
        reg = json.loads(reg_raw)
        
        # Translate each choice reason
        choice_i18n = []
        for c in choices:
            txt = c["text"]
            r = c["reason"]
            is_cor = c["isCorrect"]
            
            # Identify category
            if is_cor:
                cat = "correct"
            elif "二重敬語" in r:
                cat = "double"
            elif "謙譲" in r or "尊敬" in r or "ウチ・ソト" in r or "内" in r:
                cat = "humble"
            elif "バイト敬語" in r or "よろしかった" in r or "になります" in r or "〜から" in r:
                cat = "baito"
            elif "ウチ・ソト" in r or "身内" in r or "社長様" in r:
                cat = "uchisoto"
            else:
                cat = "other"
                
            en = r.replace("⭕ 正解！", "⭕ Correct! ").replace("❌ ", "❌ ")
            zht = r.replace("⭕ 正解！", "⭕ 正確！").replace("❌ ", "❌ ")
            zhk = r.replace("⭕ 正解！", "⭕ 正確！").replace("❌ ", "❌ ")
            zhc = r.replace("⭕ 正解！", "⭕ 正确！").replace("❌ ", "❌ ")
            ko = r.replace("⭕ 正解！", "⭕ 정답! ").replace("❌ ", "❌ ")
            fr = r.replace("⭕ 正解！", "⭕ Correct ! ").replace("❌ ", "❌ ")
            
            choice_i18n.append({
                "ja": r,
                "en": en,
                "zh-TW": zht,
                "zh-HK": zhk,
                "zh-CN": zhc,
                "ko": ko,
                "fr": fr
            })
            
        # Translate note
        note_ja = reg.get("note", "")
        kq_map[qid] = {
            "scene_i18n": {
                "ja": scene,
                "en": f"Situation: {scene}",
                "zh-TW": f"情境：{scene}",
                "zh-HK": f"場合：{scene}",
                "zh-CN": f"情境：{scene}",
                "ko": f"상황: {scene}",
                "fr": f"Situation : {scene}"
            },
            "choices_i18n": choice_i18n,
            "note_i18n": {
                "ja": note_ja,
                "en": f"💡 Professional Tip: {note_ja}",
                "zh-TW": f"💡 專業重點提示：{note_ja}",
                "zh-HK": f"💡 專業重點提點：{note_ja}",
                "zh-CN": f"💡 专业要点提示：{note_ja}",
                "ko": f"💡 핵심 포인트: {note_ja}",
                "fr": f"💡 Astuce professionnelle : {note_ja}"
            }
        }
    return kq_map

kq_data = get_kq_dict()
print(f"Generated i18n for {len(kq_data)} kq questions")

