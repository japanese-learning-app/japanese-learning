/**
 * Google TTS Standard Engine for Japanese Learning App
 * 100% Google TTS First architecture across all flashcards, quizzes, dictionaries, and textbooks.
 * Features:
 *  - Automatic ruby (<rt>) and HTML tag sanitization (prevents double readings)
 *  - Long sentence chunking with queue playback (prevents fallback on long examples)
 *  - Natural pause between sentences and dialogue turns
 *  - Robust automatic fallback to Web Speech API when offline or network fails
 */
(function(global) {
  'use strict';

  let globalAudioInstance = null;
  let audioQueue = [];
  let isPlayingQueue = false;

  function stopAllSpeech() {
    audioQueue = [];
    isPlayingQueue = false;
    if (globalAudioInstance) {
      try {
        globalAudioInstance.pause();
        globalAudioInstance.currentTime = 0;
      } catch (e) {}
      globalAudioInstance = null;
    }
    if ('speechSynthesis' in global) {
      try {
        global.speechSynthesis.cancel();
        if (global.speechSynthesis.paused) {
          global.speechSynthesis.resume();
        }
      } catch (e) {}
    }
  }

  function cleanJapaneseForTTS(text) {
    if (!text) return '';
    let s = String(text).trim();
    // 括弧で全体が囲まれている場合は展開
    s = s.replace(/^[（\(\[【](.*?)[）\)\]】]$/, '$1').trim();
    // <rt>タグ（ふりがな）と<rp>タグを除去
    s = s.replace(/<rt[^>]*>[\s\S]*?<\/rt>/gi, '');
    s = s.replace(/<rp[^>]*>[\s\S]*?<\/rp>/gi, '');
    // <br>を句点に置換
    s = s.replace(/<br\s*\/?>/gi, '。');
    // その他のHTMLタグを除去
    s = s.replace(/<[^>]+>/g, '');
    // 記号や空欄の調整
    s = s.replace(/（\s*）|\(　*\)|（　*）/g, '、');
    s = s.replace(/[💬🎯💡⚠️❌⭕✅🔊⭐📥🌐📄📽️]/g, '');
    // 発話ラベル除去
    s = s.replace(/^[ABａｂＡＢ][:：]\s*/g, '');
    s = s.replace(/[。、!?！？]\s*[ABａｂＡＢ][:：]\s*/g, '。');
    // 外国語訳の除去
    s = s.replace(/([。！？])\s*[a-zA-Z\u00C0-\u024F\uAC00-\uD7A3]+[\s\S]*$/, '$1');
    s = s.replace(/([。！？])\s*[\u4e00-\u9fff]{3,}[\s\S]*$/, '$1');
    s = s.replace(/[。]+/g, '。');
    return s.replace(/\s+/g, ' ').trim();
  }

  function playGoogleTTS(textOrTarget, onEnd = null) {
    stopAllSpeech();

    let rawText = '';
    if (textOrTarget && typeof textOrTarget === 'object') {
      let r = (textOrTarget.reading || '').trim().replace(/^[（\(\[【](.*?)[）\)\]】]$/, '$1');
      r = r.split(/[/／・]/)[0].trim();
      rawText = r || textOrTarget.word || '';
    } else {
      rawText = String(textOrTarget || '');
    }

    const clean = cleanJapaneseForTTS(rawText);
    if (!clean) {
      if (onEnd) onEnd();
      return;
    }

    // 170文字以下のチャンクに分割
    const chunks = [];
    const parts = clean.split(/(?<=[。！？\n])/);
    let buf = '';
    for (const p of parts) {
      const s = p.trim();
      if (!s) continue;
      if ((buf + ' ' + s).length <= 170) {
        buf = buf ? (buf + ' ' + s) : s;
      } else {
        if (buf) chunks.push(buf);
        if (s.length <= 170) {
          buf = s;
        } else {
          for (let i = 0; i < s.length; i += 160) {
            chunks.push(s.slice(i, i + 160));
          }
          buf = '';
        }
      }
    }
    if (buf) chunks.push(buf);
    if (chunks.length === 0) chunks.push(clean.slice(0, 170));

    audioQueue = chunks;
    isPlayingQueue = true;

    function playNext() {
      if (!isPlayingQueue || audioQueue.length === 0) {
        isPlayingQueue = false;
        globalAudioInstance = null;
        if (onEnd) onEnd();
        return;
      }

      const chunk = audioQueue.shift();
      const url = `https://translate.google.com/translate_tts?ie=UTF-8&tl=ja&client=tw-ob&q=${encodeURIComponent(chunk)}`;
      const audio = new Audio(url);
      globalAudioInstance = audio;

      audio.onended = () => {
        playNext();
      };
      audio.onerror = (err) => {
        console.warn('Google TTS playback failed, falling back to Web Speech API:', err);
        fallbackSpeech(chunk + (audioQueue.length ? ' ' + audioQueue.join(' ') : ''), onEnd);
      };

      const p = audio.play();
      if (p !== undefined) {
        p.catch(err => {
          console.warn('Google TTS audio play catch, falling back:', err);
          fallbackSpeech(chunk + (audioQueue.length ? ' ' + audioQueue.join(' ') : ''), onEnd);
        });
      }
    }

    playNext();
  }

  function fallbackSpeech(text, onEnd = null) {
    if (!('speechSynthesis' in global)) {
      if (onEnd) onEnd();
      return;
    }
    try {
      global.speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(text);
      u.lang = 'ja-JP';
      u.rate = 0.92;
      const voices = global.speechSynthesis.getVoices();
      const jaVoice = voices.find(v => (v.lang === 'ja-JP' || v.lang === 'ja_JP') && v.name.includes('Google')) ||
                      voices.find(v => (v.lang === 'ja-JP' || v.lang === 'ja_JP') && (v.name.includes('Kyoko') || v.name.includes('Otoya') || v.name.includes('Siri') || v.name.includes('Nanami') || v.name.includes('Keita'))) ||
                      voices.find(v => v.lang === 'ja-JP' || v.lang === 'ja_JP');
      if (jaVoice) u.voice = jaVoice;
      u.onend = () => { if (onEnd) onEnd(); };
      u.onerror = () => { if (onEnd) onEnd(); };
      global.speechSynthesis.speak(u);
    } catch (e) {
      if (onEnd) onEnd();
    }
  }

  // 連続再生（単語を発音後、例文を続けて再生）
  function playGoogleTTSSequence(firstTarget, secondTarget) {
    if (!firstTarget && !secondTarget) return;
    if (!secondTarget) {
      playGoogleTTS(firstTarget);
      return;
    }
    if (!firstTarget) {
      playGoogleTTS(secondTarget);
      return;
    }

    playGoogleTTS(firstTarget, () => {
      setTimeout(() => {
        playGoogleTTS(secondTarget);
      }, 380);
    });
  }

  // Export to global scope
  global.playGoogleTTS = playGoogleTTS;
  global.playGoogleTTSSequence = playGoogleTTSSequence;
  global.speakJapanese = playGoogleTTS;
  global.speakJapaneseSequence = playGoogleTTSSequence;
  global.speakJapaneseText = playGoogleTTS;
  global.speakText = playGoogleTTS;
  global.stopJapaneseSpeech = stopAllSpeech;
  global.stopGoogleTTS = stopAllSpeech;
  global.cleanJapaneseForTTS = cleanJapaneseForTTS;

})(typeof window !== 'undefined' ? window : this);
