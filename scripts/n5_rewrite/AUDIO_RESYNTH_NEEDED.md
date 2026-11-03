# N5 listening: MP3s that must be re-synthesised

Source of truth: `database/jlpt_n5_listening_data.js` (`speech_audio_text` of each question).
Files: `audio/listening/n5_q{N}.mp3`. (`speech_audio_text` already contains the new text; `script_html` is in sync.)
The old MP3s still give the same correct answer, so nothing is *broken* until re-synthesis – only the audio no longer matches the on-screen script.

## A. REQUIRED (spoken script changed)

- **n5_q8** (遅刻の理由) – removed the bus "accident" (事故 = sensitive topic) and made the spoken reason match the answer choice
  ("バスがなかなか来なかったから").
  - before: `いつものバスが事故で来なくて、30分もバス停で待ったんです。` / `そうでしたか。事故なら仕方ありませんね。`
  - after:  `いつものバスがなかなか来なくて、30分もバス停で待ったんです。` / `そうでしたか。それなら仕方ありませんね。`
  - new speech text:
    ```
    第8問。男の人は、どうして遅刻しましたか。。

    先生：李さん、今日はどうして遅れたのですか。寝坊ですか。
    男：いいえ、朝7時に起きたのですが、いつものバスがなかなか来なくて、30分もバス停で待ったんです。
    先生：そうでしたか。それなら仕方ありませんね。席についてください。

    質問。男の人は、どうして遅刻しましたか。。
    ```
- **n5_q11** (休みの旅行先) – the old reason was illogical ("天気が悪くなりそうだったので、海へ行きました" – bad weather → going to the sea).
  - before: `…天気が悪くなりそうだったので、海へ行きました。`
  - after:  `…友達が魚を食べたいと言ったので、海へ行きました。`
  - new speech text:
    ```
    第11問。女の人は先週の休みにどこへ行きましたか。。

    男：先週の3連休、どこかへ行きましたか。
    女：最初は山へ登るつもりだったんですが、友達が魚を食べたいと言ったので、海へ行きました。おいしい魚をたくさん食べてのんびりしました。
    男：いいですね。私も海へ行きたくなりました。

    質問。女の人は先週の休みにどこへ行きましたか。。
    ```

## B. OPTIONAL – answer-position balance for the read-aloud 3-choice questions (NOT applied)

Q21–Q24 all have the correct answer at "1番" (4 in a row). Their options are read aloud as "1番、…2番、…3番、…", so the
order can only be changed together with the MP3. To apply: re-synthesise n5_q22 and n5_q23 with the texts below, then set
`REORDER_3CHOICE = True` in `scripts/n5_rewrite/fix_listening_reading.py` and re-run it (it reorders the choices, updates
`answer`, explanation numbers and `speech_audio_text`/`script_html` automatically). Result: answers become 1, 3, 2, 1 for Q21–Q24.

- **n5_q22** → correct answer becomes 3番:
  ```
  第22問。一緒に映画を見に行きませんか。。

  1番、はい、見ました。
  2番、いいえ、見ませんでした。
  3番、ええ、行きましょう。

  質問。発話を聞いて、最も適した返答を選んでください。。
  ```
- **n5_q23** → correct answer becomes 2番:
  ```
  第23問。この料理、辛いですか。。

  1番、はい、甘いです。
  2番、いいえ、あまり辛くないです。
  3番、とてもおいしかったです。

  質問。発話を聞いて、最も適した返答を選んでください。。
  ```

Note: every `speech_audio_text` ends sentences with `。。` (e.g. `…ますか。。`) because the prompt already ends in `。`; the double
period is harmless for TTS, but may be collapsed to one when re-synthesising. (`script_html` shows a single `。`.)
