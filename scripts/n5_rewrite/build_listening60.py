# -*- coding: utf-8 -*-
"""
Build database/jlpt_n5_listening_data.js (N5 listening, ~60 questions, with illustrations) from
  data_lis_1.py (問題1 課題理解) data_lis_2.py (問題2 ポイント理解) data_lis_3.py (問題3 発話表現) data_lis_4.py (問題4 即時応答)
Usage:
  python3 build_listening60.py --check           validate only
  python3 build_listening60.py                   write the JS (illustration flag only if the JPG exists)
  python3 build_listening60.py --audio           (re)synthesise MP3s whose text changed (manifest: listening_audio_manifest.json)
  python3 build_listening60.py --audio --only 3 7   force these question numbers
"""
import os, sys, re, json, hashlib, random, importlib.util, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from n5_lib import R, P, lint_ruby, place_choices, balanced_targets, sensitive_hits, write_js, KANJI, _counter, parse_num, num_reading
REPO = os.path.dirname(os.path.dirname(HERE))
SECS = {'1': '問題1 課題理解', '2': '問題2 ポイント理解', '3': '問題3 発話表現', '4': '問題4 即時応答'}
IMG_DIR = 'images/listening_n5'
errs, warns = [], []

def load_items():
    out = []
    for s in '1234':
        p = os.path.join(HERE, f'data_lis_{s}.py')
        if not os.path.exists(p):
            warns.append(f'missing data_lis_{s}.py'); continue
        spec = importlib.util.spec_from_file_location(f'data_lis_{s}', p)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for it in m.ITEMS:
            it = dict(it); it['sec'] = s; out.append(it)
    return out

# ---------------------------------------------------------------- speech text (what TTS actually reads)
_EXPL = re.compile(r'\{([^{}|]+)\|([^{}|]+)\}')
RISKY = [('来られ', 'こられ'), ('来ます', 'きます'), ('来ました', 'きました'), ('来ませ', 'きませ'), ('来て', 'きて'), ('午後', 'ごご'), ('午前', 'ごぜん'), ('この後', 'このあと'), ('その後', 'そのあと'), ('後で', 'あとで'), ('食べた後', '食べたあと'), ('今日', 'きょう'), ('明日', 'あした'),
         ('昨日', 'きのう'), ('大人', 'おとな'), ('何人', 'なんにん'), ('一日', 'いちにち'), ('今朝', 'けさ'), ('今年', 'ことし'),
         ('去年', 'きょねん'), ('来週', 'らいしゅう'), ('来月', 'らいげつ'), ('来年', 'らいねん'), ('先週', 'せんしゅう'), ('今週', 'こんしゅう'),
         ('今月', 'こんげつ'), ('先月', 'せんげつ'), ('上手', 'じょうず'), ('下手', 'へた'), ('毎朝', 'まいあさ'), ('毎晩', 'まいばん'),
         ('来ない', 'こない'), ('来なけれ', 'こなけれ'), ('来なかった', 'こなかった'), ('一人', 'ひとり'), ('二人', 'ふたり'), ('何曜日', 'なんようび'),
         ('何時', 'なんじ'), ('何を', 'なにを'), ('何が', 'なにが'), ('何も', 'なにも'), ('何に', 'なにに'), ('何か', 'なにか'), ('何と', 'なんと'),
         ('何の', 'なんの'), ('何です', 'なんです'), ('何だ', 'なんだ'), ('何分', 'なんぷん'), ('何枚', 'なんまい'), ('何本', 'なんぼん'), ('何個', 'なんこ'), ('何階', 'なんがい'),
         ('何円', 'なんえん'), ('何月', 'なんがつ'), ('何日', 'なんにち'), ('何歳', 'なんさい'), ('何冊', 'なんさつ'), ('何回', 'なんかい'),
         ('何台', 'なんだい'), ('何番', 'なんばん')]
_NUM = re.compile(r'([0-9０-９]+)(時間|週間|時|分|日|人|歳|月|円|本|枚|冊|個|回|階|番|台|匹|杯|年|度|つ)')

def _num_to_kana(m):
    n, c = m.group(1), m.group(2)
    try:
        val = parse_num(n)
        if c == '人' and val == 1: return 'ひとり'
        if c == '人' and val == 2: return 'ふたり'
        if c == '日' and val in (1,): warns.append('1日 in speech'); return m.group(0)
        if c == '番':       # 1番 2番 ... (also prompts like 3番線 -> handled by caller)
            return num_reading(val) + 'ばん'
        full, _ = _counter(c, val)
        return full
    except Exception as e:
        warns.append(f'tts number {m.group(0)}: {e}'); return m.group(0)

def tts_text(src):
    t = _EXPL.sub(lambda m: m.group(2), src)           # {漢字|よみ} -> よみ
    t = re.sub(r'<[^>]+>', '', t)
    t = t.replace('0', '0')
    for a, b in RISKY:
        t = t.replace(a, b)
    t = re.sub(r'[0-9０-９]+(?:\.[0-9]+)?(?:[:：][0-9]+)?(?![0-9時分日人歳月円本枚冊個回階番台匹杯年度つ%％])', lambda m: num_reading(int(m.group(0))) if m.group(0).isdigit() else m.group(0), t) if False else t
    t = _NUM.sub(_num_to_kana, t)
    t = re.sub(r'([0-9]+)', lambda m: num_reading(int(m.group(1))), t)   # remaining bare numbers
    return t.replace('。。', '。').strip()

def speech_segments(n, it):
    """[(voice, text, pause_ms)]  voice: 'n' narrator, 'f','m' speakers."""
    V = {'n': 'ja-JP-Neural2-B', 'f': 'ja-JP-Neural2-B', 'm': 'ja-JP-Neural2-C'}
    head = f"だい{num_reading(n)}もん。"
    pr = tts_text(it['prompt'])
    seg = []
    if it['sec'] in '12':
        seg.append(('n', head + pr, 1000))
        for who, line in it['dialogue']:
            seg.append((who, tts_text(line), 800))
        seg.append(('n', '質問。' + pr, 1800))
    elif it['sec'] == '3':
        seg.append(('n', head + pr, 1200))
        for i, c in enumerate(it['choices']):
            seg.append(('n', f"{['いち','に','さん'][i]}ばん、{tts_text(c)}", 1500))
        seg.append(('n', '質問。' + pr, 1800))
    else:
        asker = 'f' if n % 2 == 0 else 'm'
        replier = 'm' if asker == 'f' else 'f'
        seg.append(('n', head, 600))
        seg.append((asker, pr, 1200))
        for i, c in enumerate(it['choices']):
            seg.append((replier, f"{['いち','に','さん'][i]}ばん、{tts_text(c)}", 1500))
        seg.append(('n', '質問。発話を聞いて、最も適した返答を選んでください。', 1800))
    return [(V[v], t, p, v) for v, t, p in seg]

def speech_plain(n, it):
    """human-readable speech_audio_text (kept for the page's fallback TTS and review)."""
    segs = speech_segments(n, it)
    lines = []
    for v, t, p, role in segs:
        lines.append(t)
    return '\n\n'.join(lines)

# ---------------------------------------------------------------- build
def build():
    items = load_items()
    out, seen_prompts = [], set()
    rng = random.Random(20261104)
    # answer balancing for 4-choice sections
    for sec in '12':
        idx = [i for i, it in enumerate(items) if it['sec'] == sec]
        tg = balanced_targets(len(idx), seed=int(sec) * 77)
        for i, t in zip(idx, tg):
            it = items[i]
            c = it['choices']
            if len(c) != 4: errs.append(f"sec{sec} '{it['title']}': needs 4 choices"); continue
            try:
                new, a = place_choices(c[it['answer']], [x for k, x in enumerate(c) if k != it['answer']], t, rng)
                it['choices'], it['answer'] = new, a
            except Exception as e:
                errs.append(f"sec{sec} '{it['title']}': {e}")
    n = 0
    for it in items:
        n += 1
        sec = it['sec']
        if sec in '34' and len(it['choices']) != 3: errs.append(f"q{n}: sec{sec} needs 3 choices")
        if len(set(it['choices'])) != len(it['choices']): errs.append(f'q{n}: duplicate choices')
        if sec in '12' and not it.get('dialogue'): errs.append(f'q{n}: no dialogue')
        if not it['prompt'].endswith(('。', '？', '?')): errs.append(f"q{n}: prompt must end with 。: {it['prompt']}")
        if it['prompt'] in seen_prompts and sec in '34': errs.append(f"q{n}: duplicate prompt {it['prompt']}")
        seen_prompts.add(it['prompt'])
        ex = it['exp']
        for k in ('ja', 'en', 'zh', 'ko'):
            if not ex.get(k): errs.append(f'q{n}: exp.{k} missing')
            if re.search(r'(選択肢|[1-4１-４]番|No\. ?[1-4]|选项|選項[1-4]|[1-4]번)', ex.get(k, '')): errs.append(f'q{n}: exp.{k} contains option number: {ex.get(k)[:40]}')
        if not it.get('img'): errs.append(f'q{n}: no img brief')
        allt = it['prompt'] + ''.join(it['choices']) + ''.join(t for _, t in it.get('dialogue', [])) + ex['ja']
        h = sensitive_hits(allt)
        if h: errs.append(f'q{n}: sensitive {h}')
        for bad in ('Zoom', 'LINE', 'Google', 'Amazon', 'ユニクロ', 'マクドナルド', 'セブン', 'ローソン', 'ファミリーマート', 'スタバ', 'スターバックス'):
            if bad in allt: errs.append(f'q{n}: brand {bad}')
        try:
            prompt_ruby = R(it['prompt'])
            choices_ruby = [R(c) for c in it['choices']]
            exja = R(it['exp']['ja'])
            dlg_html = ''
            if sec in '12':
                for who, line in it['dialogue']:
                    lab = '女' if who == 'f' else '男'
                    dlg_html += f'<p><span class="font-bold text-[#1995AD]">{R(lab + "の人")}：</span>{R(line)}</p>'
                dlg_html = f'<p class="text-xs font-bold text-slate-400 mb-1">{R("第%d問。" % n)}{prompt_ruby}</p>' + dlg_html
            else:
                dlg_html = f'<p class="text-xs font-bold text-slate-400 mb-1">{R("第%d問。" % n)}{prompt_ruby}</p>'
                for i, c in enumerate(choices_ruby):
                    dlg_html += f'<p><span class="font-bold text-[#1995AD]">{i+1}{R("番")}：</span>{c}</p>'
            dlg_html += f'<p class="text-xs font-bold text-[#B8596E] mt-2">{R("質問")}。{prompt_ruby if sec in "123" else R("発話を聞いて、最も適した返答を選んでください。")}</p>'
            script_html = f'<div class="space-y-2 text-sm leading-relaxed">{dlg_html}</div>'
        except Exception as e:
            errs.append(f'q{n}: ruby error {e}'); continue
        for k, h in (('prompt', prompt_ruby), ('choices', ''.join(choices_ruby)), ('exp', exja), ('script', script_html)):
            l = lint_ruby(h)
            if l: errs.append(f'q{n}: ruby leak in {k}: {"".join(l)}')
        a = it['answer'] + 1
        pre = {'ja': R(f'正解は{a}番です。'), 'en': f'The correct answer is No. {a}. ', 'zh': f'正確答案是第{a}個選項。', 'ko': f'정답은 {a}번입니다. '}
        img_rel = f'{IMG_DIR}/n5_q{n}.jpg'
        has_img = os.path.exists(os.path.join(REPO, img_rel))
        out.append({
            'id': f'n5_lis_q{n}', 'section': SECS[sec], 'q_num': n, 'title': it['title'],
            'has_illustration': has_img, 'illustration_url': img_rel,
            'prompt': P(it['prompt']), 'prompt_ruby': prompt_ruby,
            'speech_audio_text': speech_plain(n, it),
            'choices': choices_ruby, 'answer': it['answer'],
            'explanation': {'ja': pre['ja'] + exja, 'en': pre['en'] + ex['en'], 'zh': pre['zh'] + ex['zh'], 'ko': pre['ko'] + ex['ko']},
            'audio_file': f'audio/listening/n5_q{n}.mp3', 'script_html': script_html,
            '_img_brief': it['img'], '_segments': [(v, t, p) for v, t, p, r in speech_segments(n, it)],
        })
    # report
    for sec in '1234':
        ans = [q['answer'] for q, it in zip(out, items) if it['sec'] == sec]
        runs = [i + 1 for i in range(2, len(ans)) if ans[i] == ans[i - 1] == ans[i - 2]]
        print(f'sec{sec}: {len(ans)} questions, answer dist {sorted(collections.Counter(ans).items())}, 3-runs {runs}')
        if runs: errs.append(f'sec{sec}: 3 consecutive same answers at {runs}')
        if sec in '34':
            d = collections.Counter(ans)
            if max(d.values()) - min(d.get(k, 0) for k in range(3)) > 2: errs.append(f'sec{sec}: answer positions unbalanced {dict(d)}')
    return out

if __name__ == '__main__':
    out = build()
    for w in dict.fromkeys(warns): print('WARN', w)
    if errs:
        print(len(errs), 'ERRORS'); [print(' -', e) for e in errs[:80]]
        if '--force' not in sys.argv: sys.exit(1)
    pub = [{k: v for k, v in q.items() if not k.startswith('_')} for q in out]
    if '--check' not in sys.argv and '--audio' not in sys.argv:
        data = {'test_id': 'jlpt_n5_listening_test_01', 'title': 'JLPT N5 聴解実戦模試 第1回', 'level': 'N5',
                'total_questions': len(pub), 'questions': pub}
        write_js(os.path.join(REPO, 'database/jlpt_n5_listening_data.js'), [], [('JLPT_N5_LISTENING_DATA', data)])
        json.dump({q['q_num']: q['_img_brief'] for q in out}, open(os.path.join(HERE, 'listening_img_briefs.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('wrote', len(pub), 'questions;', sum(q['has_illustration'] for q in pub), 'have illustrations')
    if '--audio' in sys.argv:
        os.environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS', os.path.join(REPO, 'secrets/google_tts_key.json'))
        from google.cloud import texttospeech
        cl = texttospeech.TextToSpeechClient()
        mf_path = os.path.join(HERE, 'listening_audio_manifest.json')
        mf = json.load(open(mf_path)) if os.path.exists(mf_path) else {}
        only = set(int(x) for x in sys.argv[sys.argv.index('--only') + 1:]) if '--only' in sys.argv else set()
        def synth(text, voice, ssml=False):
            inp = texttospeech.SynthesisInput(ssml=text) if ssml else texttospeech.SynthesisInput(text=text)
            r = cl.synthesize_speech(input=inp, voice=texttospeech.VoiceSelectionParams(language_code='ja-JP', name=voice),
                                     audio_config=texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3, speaking_rate=0.92))
            return r.audio_content
        chars = 0
        for q in out:
            n = q['q_num']; segs = q['_segments']
            h = hashlib.sha1(json.dumps(segs, ensure_ascii=False).encode()).hexdigest()
            dst = [os.path.join(REPO, 'audio/listening', f'n5_q{n}.mp3'), os.path.join(REPO, 'public/audio/listening', f'n5_q{n}.mp3')]
            if mf.get(str(n)) == h and os.path.exists(dst[0]) and not (only and n in only): continue
            if only and n not in only and mf.get(str(n)) == h: continue
            buf = bytearray()
            for voice, text, pause in segs:
                buf += synth(text, voice); chars += len(text)
                if pause: buf += synth(f'<speak><break time="{pause}ms"/></speak>', voice, ssml=True)
            for d in dst:
                os.makedirs(os.path.dirname(d), exist_ok=True); open(d, 'wb').write(buf)
            mf[str(n)] = h
            json.dump(mf, open(mf_path, 'w'), indent=1)
            print(f'n5_q{n}.mp3 {len(buf)} bytes')
        print('synthesised characters:', chars)
