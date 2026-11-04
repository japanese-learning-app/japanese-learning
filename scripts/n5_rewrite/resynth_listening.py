# -*- coding: utf-8 -*-
"""Re-synthesise selected N5 listening MP3s (audio/listening/n5_q{N}.mp3, mirrored to public/audio/listening/).
Usage: python3 scripts/n5_rewrite/resynth_listening.py 8 11 22 23
Voices: narrator/female = ja-JP-Neural2-B, male = ja-JP-Neural2-C. Role labels are never spoken.
Pauses: 0.8s between speakers, 1.8s after the question, 1.5s between read-aloud choices.
"""
import os, re, sys, shutil
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS', os.path.join(REPO, 'secrets/google_tts_key.json'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from google.cloud import texttospeech
import json
F, M = 'ja-JP-Neural2-B', 'ja-JP-Neural2-C'
MALE_LABELS = ('男', '男の人', '男の学生')
txt = open(os.path.join(REPO, 'database/jlpt_n5_listening_data.js'), encoding='utf-8').read()
i = txt.index('=', txt.index('JLPT_N5_LISTENING_DATA')) + 1
DATA, _ = json.JSONDecoder().raw_decode(txt, i + len(txt[i:]) - len(txt[i:].lstrip()))
Q = {q['q_num']: q for q in DATA['questions']}
client = texttospeech.TextToSpeechClient()

def tts(text, voice, rate=0.92):
    r = client.synthesize_speech(
        input=texttospeech.SynthesisInput(text=text),
        voice=texttospeech.VoiceSelectionParams(language_code='ja-JP', name=voice),
        audio_config=texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3, speaking_rate=rate))
    return r.audio_content

def pause(ms, voice=F):
    r = client.synthesize_speech(
        input=texttospeech.SynthesisInput(ssml=f'<speak><break time="{ms}ms"/></speak>'),
        voice=texttospeech.VoiceSelectionParams(language_code='ja-JP', name=voice),
        audio_config=texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3, speaking_rate=0.92))
    return r.audio_content

def fix_tts(t):
    t = t.replace('。。', '。')
    t = re.sub(r'(?<![0-9０-９])1番、', 'いちばん、', t)
    t = re.sub(r'(?<![0-9０-９])2番、', 'にばん、', t)
    t = re.sub(r'(?<![0-9０-９])3番、', 'さんばん、', t)
    t = t.replace('第8問', 'だいはちもん').replace('第11問', 'だいじゅういちもん').replace('第22問', 'だいにじゅうにもん').replace('第23問', 'だいにじゅうさんもん')
    t = t.replace('来なくて', 'こなくて')
    t = t.replace('3連休', 'さんれんきゅう').replace('7時', 'しちじ').replace('30分', 'さんじゅっぷん')
    return t

def build(n):
    parts = [p for p in Q[n]['speech_audio_text'].split('\n') if p.strip()]
    out = bytearray()
    for p in parts:
        m = re.match(r'^(先生|女の先生|男の学生|男の人|女の人|男|女|医者|駅員)：(.*)$', p)
        if m:
            voice = M if m.group(1) in MALE_LABELS else F
            out += tts(fix_tts(m.group(2)), voice); out += pause(800, voice)
        elif re.match(r'^[123]番、', p):
            out += tts(fix_tts(p), F); out += pause(1500)
        elif p.startswith('質問'):
            out += pause(600); out += tts(fix_tts(p), F); out += pause(1800)
        else:
            out += tts(fix_tts(p), F); out += pause(1000)
    return bytes(out)

for a in sys.argv[1:]:
    n = int(a)
    data = build(n)
    for d in ('audio/listening', 'public/audio/listening'):
        path = os.path.join(REPO, d, f'n5_q{n}.mp3')
        if os.path.isdir(os.path.dirname(path)):
            open(path, 'wb').write(data)
    print('wrote n5_q%d.mp3 (%d bytes)' % (n, len(data)))
