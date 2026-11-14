#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate complete natural translations for Keigo learning module in 6 languages:
- en: English
- zh-TW: 繁體中文 (台灣)
- zh-HK: 繁體中文 (香港粵語)
- zh-CN: 简体中文
- ko: 한국어
- fr: Français
"""

import json
import re
from pathlib import Path

ROOT = Path("/Users/yamauchimiku/Documents/GitHub/japanese-learning")
p_text = (ROOT / "database/business_keigo_practice_data.js").read_text(encoding="utf-8")

m_q = re.search(r'window\.KEIGO_STEP2_QUIZ\s*=\s*(\[[\s\S]*?\]);\s*window\.KEIGO_STEP3_SITUATIONS', p_text)
step2 = json.loads(m_q.group(1))

m_s = re.search(r'window\.KEIGO_STEP3_SITUATIONS\s*=\s*(\[[\s\S]*?\]);\s*window\.KEIGO_STEP3_EMAILS', p_text)
sits = json.loads(m_s.group(1))

m_e = re.search(r'window\.KEIGO_STEP3_EMAILS\s*=\s*(\[[\s\S]*?\]);\s*window\.KEIGO_SPOKEN_VARIATIONS_MAP', p_text)
emails = json.loads(m_e.group(1))

print(f"Loaded: Step2={len(step2)}, Sits={len(sits)}, Emails={len(emails)}")
