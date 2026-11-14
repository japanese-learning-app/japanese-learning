#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path

ROOT = Path("/Users/yamauchimiku/Documents/GitHub/japanese-learning")
step2_raw = json.loads((ROOT / "scripts/step2_raw.json").read_text(encoding="utf-8"))
step3_raw = json.loads((ROOT / "scripts/step3_raw.json").read_text(encoding="utf-8"))

def clean(text):
    return re.sub(r'\s+', ' ', text).strip()

# Specialized translations map for Step 2
# We map each qid with high accuracy
I18N_STEP2 = {}

# We create detailed mappings for each question
