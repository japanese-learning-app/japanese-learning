#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path

ROOT = Path("/Users/yamauchimiku/Documents/GitHub/japanese-learning")
p_text = (ROOT / "database/business_keigo_practice_data.js").read_text(encoding="utf-8")

m_q = re.search(r'window\.KEIGO_STEP2_QUIZ\s*=\s*(\[[\s\S]*?\]);\s*window\.KEIGO_STEP3_SITUATIONS', p_text)
step2_quiz = json.loads(m_q.group(1))

m_s = re.search(r'window\.KEIGO_STEP3_SITUATIONS\s*=\s*(\[[\s\S]*?\]);\s*window\.KEIGO_STEP3_EMAILS', p_text)
step3_sits = json.loads(m_s.group(1))

m_e = re.search(r'window\.KEIGO_STEP3_EMAILS\s*=\s*(\[[\s\S]*?\]);\s*window\.KEIGO_SPOKEN_VARIATIONS_MAP', p_text)
step3_emails = json.loads(m_e.group(1))

# Check data IDs
print("Step 2 IDs:", [q["id"] for q in step2_quiz])
print("Step 3 Sit IDs:", [s["id"] for s in step3_sits])
print("Step 3 Email IDs:", [e["id"] for e in step3_emails])
