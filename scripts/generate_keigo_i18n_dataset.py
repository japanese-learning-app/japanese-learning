#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path

ROOT = Path("/Users/yamauchimiku/Documents/GitHub/japanese-learning")

# Load existing practice data
p_js = (ROOT / "database/business_keigo_practice_data.js").read_text(encoding="utf-8")

# Extract kq questions
kq_items = []
kq_blocks = re.findall(r'\{\s*"id":\s*"(kq_\d+)"[\s\S]*?"choices":\s*(\[[\s\S]*?\])\s*,\s*"registers":\s*(\{[\s\S]*?\})\s*\}', p_js)

print(f"Found {len(kq_blocks)} kq blocks")

