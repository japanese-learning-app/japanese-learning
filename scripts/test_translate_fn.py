# -*- coding: utf-8 -*-
import json, re

# Test sample translations function
def get_sample_translation():
    return {
        "en": "⭕ Correct! 'おっしゃる' is the proper honorific form of '言う'.",
        "zh-TW": "⭕ 正確！「おっしゃる」是「言う」的正統尊敬語。",
        "zh-HK": "⭕ 正確！「おっしゃる」係「言う」嘅正統尊敬語。",
        "zh-CN": "⭕ 正确！“おっしゃる”是“言う”的标准尊敬语。",
        "ko": "⭕ 정답! 'おっしゃる'는 '言う'의 올바른 존경어입니다.",
        "fr": "⭕ Correct ! « Ossharu » est la forme honorifique appropriée de « iu »."
    }

print("Sample ok:", get_sample_translation()["en"])
