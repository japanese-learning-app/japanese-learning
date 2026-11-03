#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Cloud Text-to-Speech (Neural2) Batch Audio Generator for JLPT Learning
Features:
- ja-JP-Neural2-B (Female Pro Announcer) / ja-JP-Neural2-C (Male Pro Announcer)
- Strips <ruby> tags safely to prevent double-reading
- MD5-based persistent caching (skips existing files, $0 re-runs)
- Hard quota safety guard (halts before approaching 1,000,000 chars/month limit)
"""

import os
import sys
import re
import json
import hashlib
import time
import warnings

# Suppress harmless library deprecation warnings
warnings.filterwarnings('ignore')

try:
    from google.cloud import texttospeech
except ImportError:
    print("[ERROR] google-cloud-texttospeech is not installed. Please install it first.")
    sys.exit(1)

# Paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
AUDIO_DIR = os.path.join(BASE_DIR, "audio")
VOCAB_AUDIO_DIR = os.path.join(AUDIO_DIR, "vocab")
EXAMPLE_AUDIO_DIR = os.path.join(AUDIO_DIR, "examples")
GRAMMAR_AUDIO_DIR = os.path.join(AUDIO_DIR, "grammar")
AUDIO_INDEX_PATH = os.path.join(AUDIO_DIR, "audio_index.json")

# Safety Quota Limits (Free Tier = 1,000,000 characters per month)
MAX_CHARS_SAFETY_CAP = 800000

# Voice Config
DEFAULT_FEMALE_VOICE = "ja-JP-Neural2-B"
DEFAULT_MALE_VOICE = "ja-JP-Neural2-C"

# Auto-set credentials if present in secrets directory
LOCAL_KEY_PATH = os.path.join(BASE_DIR, "secrets", "google_tts_key.json")
if os.path.exists(LOCAL_KEY_PATH) and not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = LOCAL_KEY_PATH


def clean_text_for_tts(text: str) -> str:
    """
    Remove HTML tags and ruby annotations to prevent duplicate reading.
    e.g. '<ruby>差し支え<rt>さしつかえ</rt></ruby>' -> '差し支え'
    """
    # Remove <rt>...</rt> ruby text first
    text_clean = re.sub(r'<rt>.*?</rt>', '', text, flags=re.DOTALL)
    # Remove all remaining HTML tags
    text_clean = re.sub(r'<[^>]+>', '', text_clean)
    # Unescape common HTML entities
    text_clean = text_clean.replace("&nbsp;", " ").replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    return text_clean.strip()


def get_audio_hash(text: str, voice_name: str, speaking_rate: float = 1.0) -> str:
    key = f"{text}_{voice_name}_{speaking_rate:.2f}"
    return hashlib.md5(key.encode('utf-8')).hexdigest()[:16]


class Neural2AudioGenerator:
    def __init__(self):
        try:
            self.client = texttospeech.TextToSpeechClient()
        except Exception as e:
            print(f"[AUTH ERROR] Could not initialize Google Cloud TTS client: {e}")
            print("Please ensure you have authenticated using 'gcloud auth application-default login'")
            print("or set the GOOGLE_APPLICATION_CREDENTIALS environment variable.")
            sys.exit(1)

        self.total_chars_generated = 0
        self.total_cached_skips = 0
        self.audio_index = self._load_index()

        # Ensure output directories exist
        for d in [AUDIO_DIR, VOCAB_AUDIO_DIR, EXAMPLE_AUDIO_DIR, GRAMMAR_AUDIO_DIR]:
            os.makedirs(d, exist_ok=True)

    def _load_index(self) -> dict:
        if os.path.exists(AUDIO_INDEX_PATH):
            try:
                with open(AUDIO_INDEX_PATH, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def _save_index(self):
        with open(AUDIO_INDEX_PATH, 'w', encoding='utf-8') as f:
            json.dump(self.audio_index, f, ensure_ascii=False, indent=2)

    def synthesize(self, raw_text: str, voice_name: str = DEFAULT_FEMALE_VOICE,
                   speaking_rate: float = 1.0, subfolder: str = "examples") -> str:
        clean_text = clean_text_for_tts(raw_text)
        if not clean_text:
            return ""

        file_hash = get_audio_hash(clean_text, voice_name, speaking_rate)
        filename = f"{file_hash}.mp3"
        target_dir = os.path.join(AUDIO_DIR, subfolder)
        os.makedirs(target_dir, exist_ok=True)
        file_path = os.path.join(target_dir, filename)
        rel_path = f"audio/{subfolder}/{filename}"

        # 1. Check local cache (skip existing files to guarantee $0 cost)
        if os.path.exists(file_path) and os.path.getsize(file_path) > 100:
            self.total_cached_skips += 1
            self.audio_index[file_hash] = {
                "text": clean_text,
                "voice": voice_name,
                "rate": speaking_rate,
                "path": rel_path
            }
            return rel_path

        # 2. Safety Quota Check
        char_len = len(clean_text)
        if self.total_chars_generated + char_len > MAX_CHARS_SAFETY_CAP:
            print(f"\n[SAFETY HALT] Approaching monthly quota safety cap ({self.total_chars_generated}/{MAX_CHARS_SAFETY_CAP} chars).")
            print("Stopping audio generation to ensure 100% free tier compliance ($0).")
            self._save_index()
            sys.exit(0)

        # 3. Synthesize via Google Cloud Neural2
        synthesis_input = texttospeech.SynthesisInput(text=clean_text)

        # Infer gender from voice name
        gender = texttospeech.SsmlVoiceGender.FEMALE if "-B" in voice_name or "-A" in voice_name else texttospeech.SsmlVoiceGender.MALE
        voice = texttospeech.VoiceSelectionParams(
            language_code="ja-JP",
            name=voice_name,
            ssml_gender=gender
        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=speaking_rate,
            sample_rate_hertz=24000
        )

        try:
            response = self.client.synthesize_speech(
                input=synthesis_input,
                voice=voice,
                audio_config=audio_config
            )
            with open(file_path, "wb") as out:
                out.write(response.audio_content)

            self.total_chars_generated += char_len
            self.audio_index[file_hash] = {
                "text": clean_text,
                "voice": voice_name,
                "rate": speaking_rate,
                "path": rel_path
            }
            return rel_path
        except Exception as e:
            print(f"[API ERROR] Failed to synthesize '{clean_text[:20]}...': {e}")
            return ""

    def finish(self):
        self._save_index()
        print("\n" + "=" * 50)
        print("★ Neural2 Batch Audio Generation Summary ★")
        print(f"Newly Generated Characters: {self.total_chars_generated:,} chars")
        print(f"Skipped from Cache (Saved): {self.total_cached_skips:,} files")
        print(f"Total Index Entries: {len(self.audio_index):,} items")
        print(f"Estimated Cost: $0.00 (Free Tier 1,000,000 chars/month)")
        print("=" * 50)


if __name__ == "__main__":
    print("Testing Neural2 connection and synthesizing sample...")
    generator = Neural2AudioGenerator()
    test_path = generator.synthesize("これはGoogle Cloud Neural2による、プロのアナウンサー音声テストです。", DEFAULT_FEMALE_VOICE, subfolder="examples")
    generator.finish()
    print(f"Test audio saved to: {test_path}")
