#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
High quality 6-language Keigo explanation database generator.
Languages:
  en: English
  zh-TW: 繁體中文 (台灣)
  zh-HK: 繁體中文 (香港粵語)
  zh-CN: 简体中文
  ko: 한국어
  fr: Français
"""
import json
import re
from pathlib import Path

ROOT = Path("/Users/yamauchimiku/Documents/GitHub/japanese-learning")
step2_raw = json.loads((ROOT / "scripts/step2_raw.json").read_text(encoding="utf-8"))
step3_raw = json.loads((ROOT / "scripts/step3_raw.json").read_text(encoding="utf-8"))

# Common terminology dictionary
COMMON_TERMS = {
    "二重敬語": {
        "en": "Double honorific error (二重敬語): Stacking multiple honorifics on the same verb is grammatically incorrect.",
        "zh-TW": "二重敬語錯誤：該動詞本身已是尊敬語，重複疊加尊敬助動詞屬於文法錯誤。",
        "zh-HK": "二重敬語錯誤：呢個動詞本身已經係尊敬語，重複加多個尊敬助動詞屬於文法錯誤。",
        "zh-CN": "双重敬语错误：该动词本身已是尊敬语，重复叠加尊敬助动词在语法上是错误的。",
        "ko": "이중경어 오류: 이미 존경어인 표현에 존경 조동사를 또 겹쳐 쓰는 것은 어법상 틀린 표현입니다.",
        "fr": "Erreur de double keigo : accumuler plusieurs formes honorifiques sur le même verbe est grammaticalement fautif."
    },
    "バイト敬語": {
        "en": "Part-time job keigo error (バイト敬語): Casual service habit (e.g. '~ni narimasu', '~kara') that is improper in professional business.",
        "zh-TW": "打工族敬語（バイト敬語）：常見於餐飲超商的非正規口頭習慣，在正式商務中視為錯誤。",
        "zh-HK": "打工敬語（バイト敬語）：餐廳便利店常見嘅口頭誤用習慣，喺正式商務上係唔合格嘅。",
        "zh-CN": "打工族敬语（バイト敬語）：餐饮店便利店常见的非正规口头习惯，在正式商务中属于误用。",
        "ko": "아르바이트 경어(バイト敬語): 매장이나 식당에서 굳어진 잘못된 말투로, 정규 비즈니스에서는 오답입니다.",
        "fr": "Keigo de petit boulot (Baito-keigo) : mauvaise habitude du commerce de proximité, incorrecte en milieu d'affaires."
    },
    "ウチ・ソト": {
        "en": "In-group vs Out-group rule (ウチ・ソト): Always use humble speech for your own company/family when talking to external clients, even about your boss.",
        "zh-TW": "內外有別原則（ウチ・ソト）：面對社外客戶提及自家主管或家人時，必須去掉職銜並一律使用謙讓語。",
        "zh-HK": "內外有別原則（ウチ・ソト）：面對出面客戶提到自己上司或者家人，一定要除去職位並一律用謙讓語。",
        "zh-CN": "内外有别原则（ウチ・ソト）：对外部客户提及自家领导或家人时，必须去除职衔并一律使用谦让语。",
        "ko": "우치·소토(사내외 구별) 원칙: 사외 고객에게 자사 상사나 가족을 언급할 때는 직함을 떼고 반드시 겸양어를 써야 합니다.",
        "fr": "Règle Uchi/Soto : envers les clients externes, on emploie toujours l'humilité pour son propre groupe (patron inclus)."
    }
}

