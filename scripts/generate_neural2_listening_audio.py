# -*- coding: utf-8 -*-
"""
Google Cloud Neural2 音声ファイル実生成スクリプト
Mac上の audio/listening/ および audio/mock_.../ に本物の高品質mp3音声を生成・保存
"""

import os
import sys
import json
import time
from google.cloud import texttospeech

BASE_DIR = "/Users/yamauchimiku/Documents/GitHub/japanese-learning"
KEY_PATH = os.path.join(BASE_DIR, "secrets/google_tts_key.json")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = KEY_PATH

client = texttospeech.TextToSpeechClient()

FEMALE_VOICE = texttospeech.VoiceSelectionParams(language_code="ja-JP", name="ja-JP-Neural2-B")
MALE_VOICE = texttospeech.VoiceSelectionParams(language_code="ja-JP", name="ja-JP-Neural2-C")
AUDIO_CONFIG = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3,
    speaking_rate=0.95,
    pitch=0.0
)

def clean_tts_text(text):
    text = text.replace("この後", "このあと")
    text = text.replace("持って来なければ", "持ってこなければ")
    text = text.replace("来なければ", "こなければ")
    text = text.replace("来なかった", "こなかった")
    text = text.replace("来なくて", "こなくて")
    text = text.replace("来られる", "こられる")
    text = text.replace("問題一", "問題１")
    text = text.replace("一番", "１番")
    text = text.replace("Zoom", "オンラインミーティング")
    text = text.replace("zoom", "オンラインミーティング")
    text = text.replace("ソニー", "大手電機メーカー")
    text = text.replace("パナソニック", "大手家電メーカー")
    return text

def synthesize_to_file(text, out_path, is_male=False):
    if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
        return True # already exists
    
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    clean_t = clean_tts_text(text)
    voice = MALE_VOICE if is_male else FEMALE_VOICE
    sinput = texttospeech.SynthesisInput(text=clean_t)
    
    try:
        resp = client.synthesize_speech(input=sinput, voice=voice, audio_config=AUDIO_CONFIG)
        with open(out_path, "wb") as f:
            f.write(resp.audio_content)
        # also copy to public
        pub_path = out_path.replace("/audio/", "/public/audio/")
        os.makedirs(os.path.dirname(pub_path), exist_ok=True)
        with open(pub_path, "wb") as pf:
            pf.write(resp.audio_content)
        return True
    except Exception as e:
        print(f"Error synthesizing {out_path}: {e}")
        return False

def main():
    print("==================================================")
    print("SYNTHESIZING REAL GOOGLE CLOUD NEURAL2 AUDIOS TO MAC")
    print("==================================================")

    # 1. Synthesize for N5 Mock listening questions (Rounds 1 to 5)
    r_path = os.path.join(BASE_DIR, "database/jlpt_n5_mock_rounds.js")
    with open(r_path, "r", encoding="utf-8") as f:
        content = f.read()
        json_str = content.replace("window.JLPT_N5_MOCK_ROUNDS = ", "")
        pos = json_str.find("window.JLPT_N5_MOCK_DATA")
        if pos != -1:
            json_str = json_str[:pos].strip()
        if json_str.endswith(";"):
            json_str = json_str[:-1]
        rounds = json.loads(json_str)

    count = 0
    # Process N5 rounds
    for r_num in [1, 2, 3]:
        r_data = rounds.get(str(r_num)) or rounds.get(r_num)
        if not r_data: continue
        for q in r_data["questions"]:
            if q["sectionId"] == "sec3":
                q_num = q["qNum"]
                txt = q.get("speech_audio_text") or q.get("speech_dialogue") or q["title"]
                out_p = os.path.join(BASE_DIR, f"audio/mock_n5/n5_r{r_num}_q{q_num:02d}.mp3")
                is_male = (q_num % 2 == 0)
                success = synthesize_to_file(txt, out_p, is_male)
                if success:
                    count += 1
                    if count % 5 == 0:
                        print(f"Synthesized {count} audios... (latest: {os.path.basename(out_p)})")
                time.sleep(0.1)

    print(f"\nSuccessfully generated & saved {count} Google Neural2 audios to Mac disk!")

if __name__ == '__main__':
    main()
