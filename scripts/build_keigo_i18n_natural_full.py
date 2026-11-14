#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path

ROOT = Path("/Users/yamauchimiku/Documents/GitHub/japanese-learning")
step2_raw = json.loads((ROOT / "scripts/step2_raw.json").read_text(encoding="utf-8"))
step3_raw = json.loads((ROOT / "scripts/step3_raw.json").read_text(encoding="utf-8"))

# Translations database
I18N_STEP2 = {}
I18N_STEP3_SITUATIONS = {}
I18N_STEP3_EMAILS = {}

# Common patterns for catalog questions (351 items)
I18N_CATALOG_GENERIC = {
    "correct": {
        "en": "⭕ Correct! This is the most natural and proper business keigo expression in this context.",
        "zh-TW": "⭕ 正確！這是此商務情境中最自然、最符合規範的正確敬語。",
        "zh-HK": "⭕ 正確！呢個係呢個商務情境中最自然、最合乎規矩嘅正確敬語。",
        "zh-CN": "⭕ 正确！这是该商务场景中最自然、最规范的正确敬语表达。",
        "ko": "⭕ 정답! 해당 비즈니스 상황에서 가장 자연스럽고 올바른 표준 경어 표현입니다.",
        "fr": "⭕ Correct ! C'est l'expression keigo la plus naturelle et appropriée dans cette situation professionnelle."
    },
    "double": {
        "en": "❌ Double Honorific (二重敬語): The verb is already honorific; adding another honorific auxiliary (-reru/-rareru) is grammatically incorrect and overly wordy.",
        "zh-TW": "❌ 二重敬語錯誤：該動詞本身已經是尊敬語，再疊加尊敬助動詞「〜られる」屬於重複敬語，文法上不正確。",
        "zh-HK": "❌ 二重敬語錯誤：呢個動詞本身已經係尊敬語，再加多個尊敬助動詞「〜られる」屬於多餘重複，文法上係錯嘅。",
        "zh-CN": "❌ 双重敬语错误：该动词本身已经是尊敬语，再叠加尊敬助动词“〜られる”属于冗余重复，在语法上是不正确的。",
        "ko": "❌ 이중경어 오류: 해당 동사 자체가 이미 존경어이므로 존경 조동사 '~られる'를 불필요하게 덧붙인 것은 어법에 어긋납니다.",
        "fr": "❌ Erreur de double keigo : le verbe étant déjà honorifique, lui ajouter un autre auxiliaire (-reru/-rareru) constitue une redondance fautive."
    },
    "humble_confuse": {
        "en": "❌ Confusion between Kenjougo (Humble) and Sonkeigo (Respectful): Kenjougo lowers oneself/in-group and cannot be used for the actions of superiors, customers, or external partners.",
        "zh-TW": "❌ 謙讓語與尊敬語混淆：謙讓語是用於壓低自身或我方動作以表謙遜，絕對不可用於抬高主管、客戶或外部夥伴。",
        "zh-HK": "❌ 謙讓語同尊敬語搞亂：謙讓語係用嚟貶低自己或者自己公司動作，絕對唔可以用喺主管、客戶或者外部夥伴身上。",
        "zh-CN": "❌ 谦让语与尊敬语混淆：谦让语用于放低自身或我方行为以示谦逊，绝不能用于描述长官、客户或外部合作方的行为。",
        "ko": "❌ 겸양어와 존경어 혼동: 겸양어는 자신이나 자사 측의 동작을 낮추는 말이므로, 상사나 고객·외부 상대의 동작에는 사용할 수 없습니다.",
        "fr": "❌ Confusion Sonkeigo/Kenjougo : le kenjougo (modestie) abaisse sa propre action et ne doit jamais être utilisé pour qualifier l'action d'un client ou supérieur."
    },
    "baito": {
        "en": "❌ Part-Time Keigo (バイト敬語): A common habit in casual shops (e.g., '~ni narimasu', '~kara'). It is grammatically incorrect and strongly frowned upon in formal business.",
        "zh-TW": "❌ 打工族敬語（バイト敬語）：餐飲及超商常見的口頭誤用（如「〜になります」「〜から」），在正式商務或JLPT中均視為錯誤。",
        "zh-HK": "❌ 打工敬語（バイト敬語）：餐廳同便利店常見嘅口頭誤用（例如「〜になります」「〜から」），喺正式商務場合或JLPT中係唔合格嘅。",
        "zh-CN": "❌ 打工族敬语（バイト敬語）：餐饮店、便利店常见的口头误用（如“〜になります”、“〜から”），在正规商务及JLPT考试中均属错误。",
        "ko": "❌ 아르바이트 경어(バイト敬語): 매장·편의점 알바에서 굳어진 잘못된 습관(예: '~になります', '~から')으로, 정규 비즈니스와 시험에서는 오답입니다.",
        "fr": "❌ Keigo de petit boulot (Baito-keigo) : habitude orale incorrecte courante dans le commerce (ex. « ~ni narimasu »). Inacceptable dans le milieu professionnel formel."
    }
}

