#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Full professional 6-language Keigo explanation database generator.
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

def build_data():
    db_step2 = {}
    
    # We define comprehensive translations for kq_01 to kq_28
    # kq_01: 上司に送った企画書を確認したか聞く
    db_step2["kq_01"] = {
        "choices": [
            {
                "en": "⭕ Correct! 'ご覧になる' is the proper honorific form (Sonkeigo) of '見る' (to look/read). Highly polite and natural when asking a superior.",
                "zh-TW": "⭕ 正確！使用動詞「見る（看）」的正統尊敬語「ご覧になる」，向長官詢問是否已審閱企劃書最為自然得體。",
                "zh-HK": "⭕ 正確！採用咗動詞「見る（睇）」嘅標準尊敬語「ご覧になる」，問長官過目咗未最為自然得體。",
                "zh-CN": "⭕ 正确！使用动词“見る（看）”的标准尊敬语“ご覧になる”，向领导询问是否已审阅企划书最为自然得体。",
                "ko": "⭕ 정답! '見る(보다)'의 표준 존경어인 'ご覧になる'를 사용하여 부장님께 기획서를 검토하셨는지 여쭙는 가장 자연스럽고 정중한 표현입니다.",
                "fr": "⭕ Correct ! Utilise la forme honorifique standard (Sonkeigo) « Goran ni naru » de « miru » (voir/consulter), parfait pour s'adresser à un supérieur."
            },
            {
                "en": "❌ Double Honorific (二重敬語): 'ご覧になる' is already honorific; adding another honorific auxiliary ('〜になられる') creates an incorrect redundancy.",
                "zh-TW": "❌ 二重敬語錯誤：「ご覧になる」本身已經是尊敬語，再疊加「〜になられる」屬於語法錯誤的重複敬語。",
                "zh-HK": "❌ 二重敬語錯誤：「ご覧になる」本身已經係尊敬語，再加「〜になられる」屬於文法錯誤嘅重複敬語。",
                "zh-CN": "❌ 双重敬语错误：“ご覧になる”本身已经是尊敬语，再叠加“〜になられる”属于语法错误的重复敬语。",
                "ko": "❌ 이중경어 오류: 'ご覧になる' 자체가 이미 존경어이므로, 여기에 다시 '~になられる'를 덧붙인 것은 어법에 맞지 않는 이중경어입니다.",
                "fr": "❌ Double keigo : « Goran ni naru » étant déjà honorifique, lui ajouter « ~ni narareru » constitue une redondance fautive."
            },
            {
                "en": "❌ Confusion with Humble Speech (謙譲語): '拝見する' is a humble verb used only for one's own actions, never for superiors.",
                "zh-TW": "❌ 謙讓語與尊敬語混淆：「拝見する」是用來貶低自身動作以示謙遜的謙讓語，絕不能用於長官的行為。",
                "zh-HK": "❌ 謙讓語同尊敬語搞亂：「拝見する」係用嚟貶低自己動作以表謙虛嘅謙讓語，絕對唔可以用喺長官身上。",
                "zh-CN": "❌ 谦让语与尊敬语混淆：“拝見する”是用于放低自身行为的谦让语，绝不可用于描述上级的动作。",
                "ko": "❌ 겸양어와 존경어 혼동: '拝見する'는 자신의 행동을 낮추는 겸양어이므로, 상사의 행동에는 절대 쓸 수 없습니다.",
                "fr": "❌ Confusion d'humilité : « Haiken suru » est un verbe d'humilité (Kenjougo) réservé à ses propres actions, jamais pour un supérieur."
            },
            {
                "en": "❌ Misused Vocabulary: 'お目にかかる' is humble for 'to meet (会う)', not 'to read/see documents'.",
                "zh-TW": "❌ 詞彙誤用：「お目にかかる」是「會面（会う）」的謙讓語，不能用作審閱文件的意思。",
                "zh-HK": "❌ 詞彙用錯：「お目にかかる」係「見面（会う）」嘅謙讓語，唔可以用嚟表達睇文件。",
                "zh-CN": "❌ 词汇误用：“お目にかかる”是“会面（会う）”的谦让语，不能用于审阅文件的含义。",
                "ko": "❌ 어휘 오용: 'お目にかかる'는 '만나다(会う)'의 겸양어이며, 서류를 검토한다는 의미로는 쓸 수 없습니다.",
                "fr": "❌ Erreur de vocabulaire : « Ome ni kakaru » signifie humblement « rencontrer (une personne) », et non « lire/consulter des documents »."
            }
        ],
        "note": {
            "en": "💡 Nuance Tip: While 'ご覧になりましたでしょうか' is grammatically correct, it can sound quite formal. In verbal office chats, 'ご確認いただけましたでしょうか？' (Were you able to check it?) or 'ご覧いただけましたか？' sounds much softer and approachable.",
            "zh-TW": "💡 語境與語氣精解：雖然「ご覧になりましたでしょうか」文法完全正確，但在口頭對話中有時略顯生硬。在日常溝通中改用「ご確認いただけましたでしょうか？」（您確認過了嗎？）或「ご覧いただけましたか？」會更加親切自然。",
            "zh-HK": "💡 語境同口吻重點：雖然「ご覧になりましたでしょうか」文法完全啱，但口語講起上嚟有少少太硬。日常口語講「ご確認いただけましたでしょうか？」（您睇過咗未呀？）或者「ご覧いただけましたか？」會更加自然舒服。",
            "zh-CN": "💡 语境与语气精解：虽然“ご覧になりましたでしょうか”语法正确，但口头交流时略显正式生硬。日常沟通改说“ご確認いただけましたでしょうか？”或“ご覧いただけましたか？”更加温和自然。",
            "ko": "💡 뉘앙스 포인트: 'ご覧になりましたでしょうか'는 올바른 문법이지만 구두로는 다소 딱딱할 수 있습니다. 일상 업무 대화에서는 'ご確認いただけましたでしょうか?(확인해 주셨습니까?)'나 'ご覧いただけましたか?'가 훨씬 부드럽고 자연스럽습니다.",
            "fr": "💡 Nuance pratique : bien que « Goran ni narimashita deshou ka » soit correct, cela peut sembler rigide à l'oral. Au bureau, préférer « Gokakunin itadakemashita deshou ka ? » pour un ton plus doux et naturel."
        }
    }
    
    # We will write a smart mapper that translates all remaining 27 questions with full natural sentences
    return db_step2

print("Template ready")
