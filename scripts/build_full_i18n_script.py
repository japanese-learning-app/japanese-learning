# -*- coding: utf-8 -*-
import json
from pathlib import Path

ROOT = Path("/Users/yamauchimiku/Documents/GitHub/japanese-learning")
step2_raw = json.loads((ROOT / "scripts/step2_raw.json").read_text(encoding="utf-8"))
step3_raw = json.loads((ROOT / "scripts/step3_raw.json").read_text(encoding="utf-8"))

# We will create a rich dictionary of translations for each question
# Let's inspect the questions prompts
for q in step2_raw:
    print(q["id"], q["prompt"][:40])
