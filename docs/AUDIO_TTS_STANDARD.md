# Google TTS 最優先（Google TTS First）音声標準仕様書

## 1. 概要
本アプリ（Japanese Learning App）におけるすべての日本語音声再生（フラッシュカード・単語・例文・教科書・JLPT問題・解説・辞書等）は、**「Google TTS 最優先（Google TTS First）」** を絶対標準とします。

## 2. 目的
- ブラウザ標準内蔵音声（macOSのKyoko、iOSのSiri、WindowsのHaruka等）の機械的で平坦なロボット発音・不自然なイントネーションを完全排除する。
- Google のニューラル言語モデルによる最高品質・高自然度の日本語ネイティブ音声を全機能・全画面で一貫して提供する。

## 3. 実装仕様
1. **Google TTS エンドポイント**:
   - `https://translate.google.com/translate_tts?ie=UTF-8&tl=ja&client=tw-ob&q=${encodeURIComponent(chunk)}`
   - 新規 Audio オブジェクト (`new Audio(url)`) を使用して再生する。
2. **長文チャンクキュー再生**:
   - 例文が長い場合、句読点（`。！？\n`）で170文字以内のチャンクに分割し、順番にキューで連続再生する。
   - 長文だからといって機械音声（SpeechSynthesis）へフォールバックさせない。
3. **ふりがな二重読み防止**:
   - 音声再生テキストからは、必ず事前に `<rt>...</rt>` および `<rp>...</rp>` を完全除去する。
4. **自動フォールバック（セーフティネット）**:
   - オフライン時やネットワークエラー、ブラウザ制限等で `audio.play()` が拒絶された場合のみ、自動的に `window.speechSynthesis`（Web Speech API）で安全に発話する。

## 4. 提供共通API
すべてのスクリプト・画面で以下の標準関数を使用すること：
- `window.playGoogleTTS(textOrTarget, onEnd)`
- `window.speakJapanese(textOrTarget, onEnd)`
- `window.speakJapaneseSequence(firstTarget, secondTarget)`
- `window.speakJapaneseText(text, onEnd)`
- `window.stopJapaneseSpeech()` / `window.stopGoogleTTS()`
