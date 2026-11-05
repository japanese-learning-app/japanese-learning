# JLPT 全レベル（N5〜N1）教材・音声・イラスト・模擬試験10回分 完全引き継ぎ書

最終更新: 2026-11-05
対象リポジトリ: `/Users/yamauchimiku/Documents/GitHub/japanese-learning`
参照必須スキル: `/Users/yamauchimiku/.gemini/config/skills/jlpt-page-builder/SKILL.md`（作業開始前に必ず `read_file` で全文を確認すること）

---

## 1. 完了・コミット済みの作業

1. **Step 1: JLPT N5 聴解（全60問）＆ 読解（全30パッセージ）**（コミット `3348600`）
   - `database/jlpt_n5_listening_data.js` / `database/jlpt_n5_reading_data.js`
   - 全60問に4:3イラスト（文字・数字・矢印・ロゴ完全禁止）を付与、男女別音声（女性・ナレーター `ja-JP-Neural2-B`、男性 `ja-JP-Neural2-C`）でターン分割合成、「あ、」完全排除、全音声ファイルを `read_file` で聴き取り検証済み。
2. **Step 2a: JLPT N2 聴解（全31問）＆ 読解（全18パッセージ・30問）**（コミット `03ce4e0`）
   - `database/jlpt_n2_listening_data.js` / `database/jlpt_n2_reading_data.js`
   - 全31問に4:3イラスト付与、男女別Neural2音声合成（問題3の即時応答11問は選択肢1〜3も音声内で読み上げ）、全31ファイルの聴き取り検証・再合成完了、読解18パッセージ（短文5・中文4・情報検索2・統合理解2・主張理解5＝計30問）作成・5視点チェック済み。
3. **Step 2b: JLPT N2 文法テキスト・文法問題・語彙カード・語彙クイズの全件精査・修正**（コミット `eb8b472`）
   - `database/jlpt_n2_grammar_details.js`（全195項目）
   - `database/jlpt_n2_grammar_quiz_data.js`（全1,507問：センシティブ・サービス名を含む6問の書き換え、`<ruby>怒<rt>おこ</rt></ruby>ら` / `<ruby>日本<rt>にほん</rt></ruby>` 修正、`sentence_furigana` 同期、備考欄クリーン化、「準拠」排除）
   - `database/jlpt_n2_vocab_full_data.js`（全3,436枚：機械的テンプレ文・重複文・同音異義ミスマッチ・センシティブ文の計794枚をすべて専用例文に書き換え、英訳欠損復元、全3,436枚の `janome`＋複合語辞書による `<ruby>` 検証）
   - `database/jlpt_n2_vocab_quiz_data.js`（全896問：センシティブ・サービス名・公式表現を含む19問および類義語欄の修正）

---

## 2. 残りのタスク一覧（1つずつ順番に別チャットで実施）

各ステップ完了時には必ず以下を実行してからコミットすること：
- **5つの視点からの品質チェック**（①Google TTS発音、②日本語の自然さ・センシティブ/ブランド名ゼロ、③正解の唯一性とルビの正確性、④機械的テンプレ文・重複文・同音異義ミスマッチゼロ、⑤出題分野と正解番号の網羅性）
- **生徒データ整合性検証**: `python3 scripts/verify_all_students_integrity.py`

### 次回以降の実施順序

#### 【次タスク】Step 3a: JLPT N4 聴解・読解の作成・5視点チェック・コミット
- **対象ファイル**:
  - `database/jlpt_n4_listening_data.js`, `jlpt_n4_listening.html`, `audio/listening/n4/`, `images/listening/n4/`
  - `database/jlpt_n4_reading_data.js`, `jlpt_n4_reading.html`
- **必須要件**:
  - 全問に4:3場面イラスト（文字・数字・看板・矢印・ロゴ一切なし）を生成・設定し、目視確認すること。
  - 男女別Neural2音声（`ja-JP-Neural2-B` / `ja-JP-Neural2-C`）で1セリフずつターン分割合成し、役名ラベルは絶対に読まないこと。
  - 感嘆詞「あ、」を完全排除すること。
  - 発話表現・即時応答では選択肢（1番… 2番… 3番…）も音声で読み上げること。
  - 生成した全MP3ファイルを `read_file` で実際に聴き取って発音ミス（日付・階数・金額・多音字・カ変活用）がないか全件確認すること。
  - 読解はN4レベルの短文・中文・情報検索をバランスよく拡充し、ルビと根拠ハイライト・4言語解説を完備すること。

#### Step 3b: JLPT N4 文法テキスト・文法問題・語彙カード・語彙クイズの精査・修正・コミット
- **対象ファイル**:
  - `database/jlpt_n4_grammar_details.js`
  - `database/jlpt_n4_grammar_quiz_data.js`
  - `database/jlpt_n4_vocab_full_data.js`
  - `database/jlpt_n4_vocab_quiz_data.js`
- **必須要件**:
  - `SKILL.md` 第21節に記載された全22種類の機械的テンプレート文（「先生や友達と一緒に、…について楽しく勉強しました。」「毎日しっかりと練習を続けて、上手に…ことができるようになりました。」等）を1件残らず検出し、各単語専用の自然な例文・英訳に書き換えること。
  - `janome` トークン境界チェックで同音異義語・部分文字列の誤マッチを検出し修正すること。
  - センシティブ表現・ブランド名・「公式」「準拠」を完全排除し、ルビと正解整合性を全件検証すること。

#### Step 4a: JLPT N3 聴解・読解の作成・5視点チェック・コミット
- **対象ファイル**:
  - `database/jlpt_n3_listening_data.js`, `jlpt_n3_listening.html`, `audio/listening/n3/`, `images/listening/n3/`
  - `database/jlpt_n3_reading_data.js`, `jlpt_n3_reading.html`

#### Step 4b: JLPT N3 文法テキスト・文法問題・語彙カード・語彙クイズの精査・修正・コミット
- **対象ファイル**:
  - `database/jlpt_n3_grammar_details.js`
  - `database/jlpt_n3_grammar_quiz_data.js`
  - `database/jlpt_n3_vocab_full_data.js`
  - `database/jlpt_n3_vocab_quiz_data.js`

#### Step 5a: JLPT N1 聴解・読解の作成・5視点チェック・コミット
- **対象ファイル**:
  - `database/jlpt_n1_listening_data.js`, `jlpt_n1_listening.html`, `audio/listening/n1/`, `images/listening/n1/`
  - `database/jlpt_n1_reading_data.js`, `jlpt_n1_reading.html`

#### Step 5b: JLPT N1 文法テキスト・文法問題・語彙カード・語彙クイズの精査・修正・コミット
- **対象ファイル**:
  - `database/jlpt_n1_grammar_details.js`
  - `database/jlpt_n1_grammar_quiz_data.js`
  - `database/jlpt_n1_vocab_full_data.js`
  - `database/jlpt_n1_vocab_quiz_data.js`

#### Step 6: 模擬試験 10回分の作成・コミット（N5 ➔ N4 ➔ N3 ➔ N2 ➔ N1 の順）
- **対象ファイル**:
  - 各レベルの `jlpt_n{5,4,3,2,1}_mock.html` および `database/jlpt_n{5,4,3,2,1}_mock_data.js`（またはラウンド別データファイル）
- **必須要件**:
  - 既存のN5模擬試験1回分を参考に、各レベル10回分を作成。
  - フラッシュカード・文法道場・読解・聴解の既存問題との重複は完全禁止（100%初見のオリジナル問題）。
  - 試験本番同様に問題文・選択肢のルビ非表示（指示文のみルビ可）、二重下線禁止（`.jlpt-underline-blank` 使用）、★の位置分散（1〜4番目に均等配分）、IRT尺度得点シミュレーション採点、聴解音声のマルチスピーカー合成と全件聴き取り確認を徹底。

#### Step 7: 全レベル（N1〜N5）横断の最終5視点チェック＆コミット
- 全レベルのリスニング音声・読解・文法・語彙・模擬試験10回分について、5つの視点から最終総点検を実施。
