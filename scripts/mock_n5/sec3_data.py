# -*- coding: utf-8 -*-
"""
JLPT N5 Mock Exam Section 3 (Listening) Data & Multi-Speaker TTS Synthesizer
- Set 1 (n5_m01_q68..q91): 24 original listening questions (with q68, q74, q77, q80 fixed)
- Set 2 (n5_m02_q68..q91): 24 brand-new original listening questions
All 48 questions use multi-speaker Neural2 voices (ja-JP-Neural2-B / ja-JP-Neural2-C),
zero 'あ、', zero speaker role labels read aloud, and 4:3 text-free illustrations from images/listening_n5/.
"""

import os
import re
from google.cloud import texttospeech

NARRATOR_VOICE = 'ja-JP-Neural2-B'
FEMALE_VOICE = 'ja-JP-Neural2-B'
MALE_VOICE = 'ja-JP-Neural2-C'

# Set 1: 24 questions (n5_m01_q68 .. n5_m01_q91)
SET1_QUESTIONS = [
    # --- 問題1: 課題理解 (Q68〜Q74) ---
    {
        "qNum": 68,
        "subsectionId": "s3_m1",
        "category": "課題理解",
        "title": "男の人は 黒い ペンを 何本 買いますか。",
        "illustration_url": "images/listening_n5/n5_q1.jpg",
        "script": "女の人：いらっしゃいませ。\n男の人：すみません、この 黒い ペンを ２本と、赤い ペンを １本 ください。\n女の人：はい、黒が ２本と、赤が １本ですね。\n男の人：すみません、やっぱり 黒い ペンは ３本に して ください。\n女の人：わかりました。黒が ３本と、赤が １本ですね。ぜんぶで ４本です。\n男の人：はい、お願いします。",
        "options": ["１本", "２本", "３本", "４本"],
        "correctIndex": 2,
        "explanation": "男の人は最初「黒いペンを2本」と言いましたが、その後「やっぱり黒いペンは3本にしてください」と変更しました。したがって黒いペンは「３本」買います。",
        "audioUrl": "audio/mock_n5/n5_m01_q68.mp3",
        "resynthesize": True,
        "tracks": [
            ("問題１。１番。男の人と女の人が話しています。男の人は黒いペンを何本買いますか。", NARRATOR_VOICE, 700),
            ("いらっしゃいませ。", FEMALE_VOICE, 400),
            ("すみません、この黒いペンを２ほんと、赤いペンを１ぽんください。", MALE_VOICE, 400),
            ("はい、黒が２ほんと、赤が１ぽんですね。", FEMALE_VOICE, 400),
            ("すみません、やっぱり黒いペンは３ぼんにしてください。", MALE_VOICE, 400),
            ("わかりました。黒が３ぼんと、赤が１ぽんですね。ぜんぶで４ほんです。", FEMALE_VOICE, 400),
            ("はい、お願いします。", MALE_VOICE, 600),
            ("男の人は黒いペンを何本買いますか。", NARRATOR_VOICE, 400)
        ]
    },
    {
        "qNum": 69,
        "subsectionId": "s3_m1",
        "category": "課題理解",
        "title": "学生は あした 何を 持って 来なければ なりませんか。",
        "illustration_url": "images/listening_n5/n5_q2.jpg",
        "script": "先生：みなさん、あしたの 授業について 話します。教科書と ノートは いつもどおり 持って 来て ください。\n学生：先生、辞書も 持って 来ますか。\n先生：いいえ、辞書は 教室に ありますから、いりません。でも、宿題の 作文を わすれないで 持って 来て くださいね。\n学生：はい、わかりました。",
        "options": ["辞書", "作文", "写真", "パソコン"],
        "correctIndex": 1,
        "explanation": "辞書は「いりません」と言われ、宿題の「作文」を忘れないで持ってくるよう指示されています。",
        "audioUrl": "audio/mock_n5/n5_m01_q69.mp3",
        "resynthesize": False
    },
    {
        "qNum": 70,
        "subsectionId": "s3_m1",
        "category": "課題理解",
        "title": "二人は あした 何時に 会いますか。",
        "illustration_url": "images/listening_n5/n5_q3.jpg",
        "script": "男の人：もしもし、あしたの 映画だけど、何時に 会おうか。\n女の人：映画は １１時からだから、１０時半は どう？\n男の人：うーん、１０時半は ちょっと 早いかな。１０時４５分は どう？\n女の人：チケットを 買わなきゃ いけないから、やっぱり １０時半に しようよ。\n男の人：そうか。じゃあ、１０時半に 駅の 改札で 会おう。",
        "options": ["１０時", "１０時半", "１０時４５分", "１１時"],
        "correctIndex": 1,
        "explanation": "チケットを買うため「やっぱり10時半にしよう」となり、最終的に「１０時半」に決定しました。",
        "audioUrl": "audio/mock_n5/n5_m01_q70.mp3",
        "resynthesize": False
    },
    {
        "qNum": 71,
        "subsectionId": "s3_m1",
        "category": "課題理解",
        "title": "病院は どこに ありますか。",
        "illustration_url": "images/listening_n5/n5_q4.jpg",
        "script": "女の人：すみません、この 近くに 病院は ありますか。\n男の人：ええ、ありますよ。この 道を まっすぐ 行って、２つめの かどを 右に まがって ください。\n女の人：２つめの かどを 右ですね。\n男の人：はい。そうすると、左側に 銀行が あります。その となりが 病院ですよ。\n女の人：銀行の となりですね。ありがとうございました。",
        "options": ["１つめのかどの右", "銀行のとなり", "銀行のむかい", "駅のなか"],
        "correctIndex": 1,
        "explanation": "男の人が「左側に銀行があります。そのとなりが病院ですよ」と説明しています。",
        "audioUrl": "audio/mock_n5/n5_m01_q71.mp3",
        "resynthesize": False
    },
    {
        "qNum": 72,
        "subsectionId": "s3_m1",
        "category": "課題理解",
        "title": "女の人は このあと まず 何を しますか。",
        "illustration_url": "images/listening_n5/n5_q5.jpg",
        "script": "男の人：佐藤さん、午後の 会議の 準備、手伝って くれる？\n女の人：はい、何を しましょうか。\n男の人：まず、この 会議の 資料を １０部 コピーして ほしいんだ。\n女の人：わかりました。そのあと 会議室の 机を ならべましょうか。\n男の人：うん、それは コピーが 終わったあとで いっしょに やろう。\n女の人：はい、じゃあ すぐ やってきます。",
        "options": ["会議室へ行く", "資料をコピーする", "机をならべる", "お茶を入れる"],
        "correctIndex": 1,
        "explanation": "「まず、この会議の資料を10部コピーしてほしいんだ」と頼まれ、机を並べるのはコピーの後です。",
        "audioUrl": "audio/mock_n5/n5_m01_q72.mp3",
        "resynthesize": False
    },
    {
        "qNum": 73,
        "subsectionId": "s3_m1",
        "category": "課題理解",
        "title": "男の人は カバンに 何を 入れますか。",
        "illustration_url": "images/listening_n5/n5_q6.jpg",
        "script": "女の人：これから 出かけるの？\n男の人：うん、駅前の 図書館へ 行ってくるよ。\n女の人：天気予報で 午後から 雨が ふるって 言ってたよ。折りたたみの 傘を 持って 行ったら？\n男の人：え、本当？ じゃあ、カバンに 入れて おくよ。上着は いるかな？\n女の人：きょうは あたたかいから、上着は いらないと 思うよ。\n男の人：わかった。ありがとう。",
        "options": ["上着", "傘", "帽子", "辞書"],
        "correctIndex": 1,
        "explanation": "午後から雨が降るため折りたたみの傘を持っていくよう勧められ、「カバンに入れておくよ」と答えています。",
        "audioUrl": "audio/mock_n5/n5_m01_q73.mp3",
        "resynthesize": False
    },
    {
        "qNum": 74,
        "subsectionId": "s3_m1",
        "category": "課題理解",
        "title": "男の人は これから テーブルの上に 何を 置きますか。",
        "illustration_url": "images/listening_n5/n5_q7.jpg",
        "script": "女の人：もうすぐ ごはんが できるから、テーブルの 上を 準備して くれる？\n男の人：うん、何を 置けば いい？\n女の人：食器棚から お皿と おはしを 出して、並べて くれる？\n男の人：お皿と、おはしね。コップも 置く？\n女の人：お茶は 私が あとで 入れるから、コップは まだ いいよ。\n男の人：わかった。",
        "options": ["コップ", "お皿とおはし", "お茶", "ごはん"],
        "correctIndex": 1,
        "explanation": "女の人から「お皿とおはしを出して、並べてくれる？」と頼まれ、コップは「まだいいよ」と言われています。",
        "audioUrl": "audio/mock_n5/n5_m01_q74.mp3",
        "resynthesize": True,
        "tracks": [
            ("７番。男の人と女の人が家で話しています。男の人はこれからテーブルの上に何を置きますか。", NARRATOR_VOICE, 700),
            ("もうすぐごはんができるから、テーブルの上を準備してくれる？", FEMALE_VOICE, 400),
            ("うん、何を置けばいい？", MALE_VOICE, 400),
            ("食器棚からおさらとおはしを出して、並べてくれる？", FEMALE_VOICE, 400),
            ("おさらと、おはしね。コップも置く？", MALE_VOICE, 400),
            ("お茶は私があとでいれるから、コップはまだいいよ。", FEMALE_VOICE, 400),
            ("わかった。", MALE_VOICE, 600),
            ("男の人はこれからテーブルの上に何を置きますか。", NARRATOR_VOICE, 400)
        ]
    },
    # --- 問題2: ポイント理解 (Q75〜Q80) ---
    {
        "qNum": 75,
        "subsectionId": "s3_m2",
        "category": "ポイント理解",
        "title": "男の人は どうして きのう パーティーに 行きませんでしたか。",
        "illustration_url": "images/listening_n5/n5_q16.jpg",
        "script": "女の人：田中さん、きのうの パーティー、どうして 来なかったの？\n男の人：行きたかったんだけど、朝から 熱が 出ちゃってね。\n女の人：え、熱？ 大丈夫だった？\n男の人：うん、薬を 飲んで 一日中 寝ていたから、もう すっかり よくなったよ。\n女の人：よかった。みんな 心配して いたよ。",
        "options": ["忙しかったから", "熱が出たから", "忘れていたから", "雨がふったから"],
        "correctIndex": 1,
        "explanation": "男の人は「朝から熱が出ちゃってね」と理由を言っています。",
        "audioUrl": "audio/mock_n5/n5_m01_q75.mp3",
        "resynthesize": False
    },
    {
        "qNum": 76,
        "subsectionId": "s3_m2",
        "category": "ポイント理解",
        "title": "男の人は どうして 電車で 行くのが 好きですか。",
        "illustration_url": "images/listening_n5/n5_q17.jpg",
        "script": "女の人：山田さんは いつも 電車で 通勤して いるんですね。車は 使わないんですか。\n男の人：車も 持って いますが、電車の ほうが 好きなんです。\n女の人：どうしてですか。\n男の人：電車の中だと、ゆっくり 本が 読めますからね。毎日の 楽しみなんです。\n女の人：なるほど、読書の 時間に なるんですね。",
        "options": ["切符が安いから", "運転が好きだから", "本が読めるから", "友達に会えるから"],
        "correctIndex": 2,
        "explanation": "男の人は「電車の中だと、ゆっくり本が読めますからね」と理由を説明しています。",
        "audioUrl": "audio/mock_n5/n5_m01_q76.mp3",
        "resynthesize": False
    },
    {
        "qNum": 77,
        "subsectionId": "s3_m2",
        "category": "ポイント理解",
        "title": "女の人は どうして その 靴を 買いませんでしたか。",
        "illustration_url": "images/listening_n5/n5_q18.jpg",
        "script": "男の人：その 靴、デザインが とても いいね。買ったの？\n女の人：いいえ、買わなかったの。\n男の人：え、どうして？ 値段が 高かったの？\n女の人：いいえ、値段は 安かったんだけど、履いてみたら サイズが ちょっと 小さくて、足が 痛かったの。\n男の人：そうか、サイズが 合わなかったんだね。",
        "options": ["高かったから", "色が嫌いだったから", "サイズが小さかったから", "店になかったから"],
        "correctIndex": 2,
        "explanation": "値段は安かったが、「サイズがちょっと小さくて、足が痛かった」ため買いませんでした。",
        "audioUrl": "audio/mock_n5/n5_m01_q77.mp3",
        "resynthesize": True,
        "tracks": [
            ("３番。男の人と女の人が話しています。女の人はどうしてその靴を買いませんでしたか。", NARRATOR_VOICE, 700),
            ("その靴、デザインがとてもいいね。買ったの？", MALE_VOICE, 400),
            ("いいえ、買わなかったの。", FEMALE_VOICE, 400),
            ("え、どうして？ 値段がたかかったの？", MALE_VOICE, 400),
            ("いいえ、値段は安かったんだけど、履いてみたらサイズがちょっと小さくて、足が痛かったの。", FEMALE_VOICE, 400),
            ("そうか、サイズが合わなかったんだね。", MALE_VOICE, 600),
            ("女の人はどうしてその靴を買いませんでしたか。", NARRATOR_VOICE, 400)
        ]
    },
    {
        "qNum": 78,
        "subsectionId": "s3_m2",
        "category": "ポイント理解",
        "title": "二人は 日曜日に どこへ 行きますか。",
        "illustration_url": "images/listening_n5/n5_q19.jpg",
        "script": "女の人：日曜日、どこかへ 出かけない？\n男の人：いいね。山へ ハイキングに 行く？ それとも 海へ 行く？\n女の人：最近 ちょっと つかれているから、山を 歩くのは 大変かも。海の 近くで おいしい 魚を 食べたいな。\n男の人：じゃあ、海に 行こう！ 電車で 行けば のんびり できるしね。\n女の人：賛成！ そうしましょう。",
        "options": ["山", "海", "カフェ", "デパート"],
        "correctIndex": 1,
        "explanation": "「海の近くでおいしい魚を食べたいな」「じゃあ、海に行こう！」と合意しました。",
        "audioUrl": "audio/mock_n5/n5_m01_q78.mp3",
        "resynthesize": False
    },
    {
        "qNum": 79,
        "subsectionId": "s3_m2",
        "category": "ポイント理解",
        "title": "男の人は どんな 部屋を さがして いますか。",
        "illustration_url": "images/listening_n5/n5_q20.jpg",
        "script": "女の人：新しい アパート、みつかりましたか。\n男の人：まだ さがして いるところです。\n女の人：どんな 部屋が いいんですか。\n男の人：いまの 部屋は 駅から 遠くて 不便なので、駅から 歩いて ５分くらいの 所が いいですね。\n女の人：広さは どうですか。\n男の人：広くなくても いいですが、夜 静かな 所が いいです。",
        "options": ["駅から近くて静かな部屋", "広くて家賃が安い部屋", "新しくて大きい部屋", "２階の部屋"],
        "correctIndex": 0,
        "explanation": "男の人は「駅から歩いて5分くらい（駅から近い）」で「夜静かな所」を希望しています。",
        "audioUrl": "audio/mock_n5/n5_m01_q79.mp3",
        "resynthesize": False
    },
    {
        "qNum": 80,
        "subsectionId": "s3_m2",
        "category": "ポイント理解",
        "title": "男の人は 何曜日に ギターの 教室に 行きますか。",
        "illustration_url": "images/listening_n5/n5_q21.jpg",
        "script": "女の人：ケンさん、ギターを 習い始めたそうですね。\n男の人：はい、先月から 教室に 通って います。\n女の人：忙しいのに すごいですね。いつ 通って いるんですか。\n男の人：平日は 仕事が ありますから、土曜日の 午後に 行って います。日曜日は 家で 休んで います。\n女の人：そうですか、土曜日なんですね。",
        "options": ["月曜日", "金曜日", "土曜日", "日曜日"],
        "correctIndex": 2,
        "explanation": "男の人は「土曜日の午後にいっています。日曜日は家で休んでいます」と言っています。",
        "audioUrl": "audio/mock_n5/n5_m01_q80.mp3",
        "resynthesize": True,
        "tracks": [
            ("６番。女の人と男の人が話しています。男の人は何曜日にギターの教室に行きますか。", NARRATOR_VOICE, 700),
            ("ケンさん、ギターを習い始めたそうですね。", FEMALE_VOICE, 400),
            ("はい、先月から教室にかよっています。", MALE_VOICE, 400),
            ("忙しいのにすごいですね。いつ、かよっているんですか。", FEMALE_VOICE, 400),
            ("平日は仕事がありますから、土曜日の午後にいっています。日曜日は家で休んでいます。", MALE_VOICE, 400),
            ("そうですか、土曜日なんですね。", FEMALE_VOICE, 600),
            ("男の人は何曜日にギターの教室に行きますか。", NARRATOR_VOICE, 400)
        ]
    },
    # --- 問題3: 発話表現 (Q81〜Q85) ---
    {
        "qNum": 81,
        "subsectionId": "s3_m3",
        "category": "発話表現",
        "title": "先生の 部屋に 入ります。何と 言いますか。",
        "illustration_url": "images/listening_n5/n5_q31.jpg",
        "script": "先生の 部屋に 入ります。何と 言いますか。\n１番：しつれいします。\n２番：さようなら。\n３番：いってきます。",
        "options": ["しつれいします。", "さようなら。", "いってきます。"],
        "correctIndex": 0,
        "explanation": "先生の部屋などに入るときの挨拶は「しつれいします（失礼します）」です。",
        "audioUrl": "audio/mock_n5/n5_m01_q81.mp3",
        "resynthesize": False
    },
    {
        "qNum": 82,
        "subsectionId": "s3_m3",
        "category": "発話表現",
        "title": "友だちに 料理を ごちそうに なりました。帰るとき、何と 言いますか。",
        "illustration_url": "images/listening_n5/n5_q32.jpg",
        "script": "友だちに 料理を ごちそうに なりました。帰るとき、何と 言いますか。\n１番：いただきます。\n２番：ごちそうさまでした。\n３番：おねがいします。",
        "options": ["いただきます。", "ごちそうさまでした。", "おねがいします。"],
        "correctIndex": 1,
        "explanation": "食事の後やごちそうになったお礼の挨拶は「ごちそうさまでした」です。",
        "audioUrl": "audio/mock_n5/n5_m01_q82.mp3",
        "resynthesize": False
    },
    {
        "qNum": 83,
        "subsectionId": "s3_m3",
        "category": "発話表現",
        "title": "友だちに 傘を 借りたいです。何と 言いますか。",
        "illustration_url": "images/listening_n5/n5_q33.jpg",
        "script": "友だちに 傘を 借りたいです。何と 言いますか。\n１番：傘を 貸しましょうか。\n２番：傘を 貸して ください。\n３番：傘を あげます。",
        "options": ["傘を 貸しましょうか。", "傘を 貸して ください。", "傘を あげます。"],
        "correctIndex": 1,
        "explanation": "自分が借りたいときは、相手に「傘を貸してください」と頼みます。",
        "audioUrl": "audio/mock_n5/n5_m01_q83.mp3",
        "resynthesize": False
    },
    {
        "qNum": 84,
        "subsectionId": "s3_m3",
        "category": "発話表現",
        "title": "電車の中で、お年寄りに 席を ゆずります。何と 言いますか。",
        "illustration_url": "images/listening_n5/n5_q34.jpg",
        "script": "電車の中で、お年寄りに 席を ゆずります。何と 言いますか。\n１番：どうぞ。\n２番：ごめんなさい。\n３番：いただきます。",
        "options": ["どうぞ。", "ごめんなさい。", "いただきます。"],
        "correctIndex": 0,
        "explanation": "席を譲るときは相手に「どうぞ」と声をかけます。",
        "audioUrl": "audio/mock_n5/n5_m01_q84.mp3",
        "resynthesize": False
    },
    {
        "qNum": 85,
        "subsectionId": "s3_m3",
        "category": "発話表現",
        "title": "友だちの 家に 遊びに 来ました。玄関で 何と 言いますか。",
        "illustration_url": "images/listening_n5/n5_q35.jpg",
        "script": "友だちの 家に 遊びに 来ました。玄関で 何と 言いますか。\n１番：ごめんください。\n２番：おかえりなさい。\n３番：いってらっしゃい。",
        "options": ["ごめんください。", "おかえりなさい。", "いってらっしゃい。"],
        "correctIndex": 0,
        "explanation": "訪問先の玄関で家の人を呼ぶときは「ごめんください」と言います。",
        "audioUrl": "audio/mock_n5/n5_m01_q85.mp3",
        "resynthesize": False
    },
    # --- 問題4: 即時応答 (Q86〜Q91) ---
    {
        "qNum": 86,
        "subsectionId": "s3_m4",
        "category": "即時応答",
        "title": "あしたの テスト、がんばって くださいね。",
        "illustration_url": "images/listening_n5/n5_q46.jpg",
        "script": "女の人：あしたの テスト、がんばって くださいね。\n１番：はい、がんばります。\n２番：いいえ、テストです。\n３番：どういたしまして。",
        "options": ["はい、がんばります。", "いいえ、テストです。", "どういたしまして。"],
        "correctIndex": 0,
        "explanation": "「がんばってくださいね」と励まされたときは「はい、がんばります」と答えます。",
        "audioUrl": "audio/mock_n5/n5_m01_q86.mp3",
        "resynthesize": False
    },
    {
        "qNum": 87,
        "subsectionId": "s3_m4",
        "category": "即時応答",
        "title": "いっしょに お昼ごはんを 食べませんか。",
        "illustration_url": "images/listening_n5/n5_q47.jpg",
        "script": "男の人：いっしょに お昼ごはんを 食べませんか。\n１番：ええ、食べましょう。\n２番：ごはんを 食べました。\n３番：はい、おいしいです。",
        "options": ["ええ、食べましょう。", "ごはんを 食べました。", "はい、おいしいです。"],
        "correctIndex": 0,
        "explanation": "「〜ませんか」と誘われたときの承諾表現は「ええ、食べましょう」です。",
        "audioUrl": "audio/mock_n5/n5_m01_q87.mp3",
        "resynthesize": False
    },
    {
        "qNum": 88,
        "subsectionId": "s3_m4",
        "category": "即時応答",
        "title": "すみません、この 近くに ポストは ありますか。",
        "illustration_url": "images/listening_n5/n5_q48.jpg",
        "script": "女の人：すみません、この 近くに ポストは ありますか。\n１番：あそこに ありますよ。\n２番：はい、手紙です。\n３番：ポストへ 行きません。",
        "options": ["あそこに ありますよ。", "はい、手紙です。", "ポストへ 行きません。"],
        "correctIndex": 0,
        "explanation": "場所を尋ねられたときは「あそこにありますよ」と位置を教えます。",
        "audioUrl": "audio/mock_n5/n5_m01_q88.mp3",
        "resynthesize": False
    },
    {
        "qNum": 89,
        "subsectionId": "s3_m4",
        "category": "即時応答",
        "title": "その 荷物、重そうですね。持ちましょうか。",
        "illustration_url": "images/listening_n5/n5_q49.jpg",
        "script": "男の人：その 荷物、重そうですね。持ちましょうか。\n１番：すみません、お願いします。\n２番：重くありませんでした。\n３番：カバンです。",
        "options": ["すみません、お願いします。", "重くありませんでした。", "カバンです。"],
        "correctIndex": 0,
        "explanation": "手伝いを申し出てもらったときは「すみません、お願いします」と答えます。",
        "audioUrl": "audio/mock_n5/n5_m01_q89.mp3",
        "resynthesize": False
    },
    {
        "qNum": 90,
        "subsectionId": "s3_m4",
        "category": "即時応答",
        "title": "昨日は どこへ 行きましたか。",
        "illustration_url": "images/listening_n5/n5_q50.jpg",
        "script": "女の人：昨日は どこへ 行きましたか。\n１番：図書館へ 行きました。\n２番：友だちと 行きます。\n３番：電車で 行きました。",
        "options": ["図書館へ 行きました。", "友だちと 行きます。", "電車で 行きました。"],
        "correctIndex": 0,
        "explanation": "「どこへ行きましたか」と場所の過去を聞かれているので「図書館へ行きました」が正解です。",
        "audioUrl": "audio/mock_n5/n5_m01_q90.mp3",
        "resynthesize": False
    },
    {
        "qNum": 91,
        "subsectionId": "s3_m4",
        "category": "即時応答",
        "title": "田中さんは いま どこに いますか。",
        "illustration_url": "images/listening_n5/n5_q51.jpg",
        "script": "男の人：田中さんは いま どこに いますか。\n１番：会議室に いますよ。\n２番：はい、田中さんです。\n３番：３時です。",
        "options": ["会議室に いますよ。", "はい、田中さんです。", "３時です。"],
        "correctIndex": 0,
        "explanation": "居場所を聞かれているので「会議室にいますよ」が正解です。",
        "audioUrl": "audio/mock_n5/n5_m01_q91.mp3",
        "resynthesize": False
    }
]

# Set 2: 24 brand-new original questions (n5_m02_q68 .. n5_m02_q91)
SET2_QUESTIONS = [
    # --- 問題1: 課題理解 (Q68〜Q74) ---
    {
        "qNum": 68,
        "subsectionId": "s3_m1",
        "category": "課題理解",
        "title": "女の人は りんごを いくつ 買いますか。",
        "illustration_url": "images/listening_n5/n5_q8.jpg",
        "script": "男の人：いらっしゃいませ。きょうは りんごが お安いですよ。\n女の人：ほんとうですね。じゃあ、りんごを ４つ ください。\n男の人：はい、４つですね。みかんも いかがですか。\n女の人：みかんは きのう 買ったから、きょうは りんごを もう １つ ふやして、５つに します。\n男の人：はい、りんごが ５つですね。ありがとうございます。",
        "options": ["３つ", "４つ", "５つ", "６つ"],
        "correctIndex": 2,
        "explanation": "最初「りんごを4つ」と言いましたが、そのあと「もう1つふやして、5つにします」と言っています。正解は「５つ」です。",
        "audioUrl": "audio/mock_n5/n5_m02_q68.mp3",
        "resynthesize": True,
        "tracks": [
            ("問題１。１番。店で男の人と女の人が話しています。女の人はりんごをいくつ買いますか。", NARRATOR_VOICE, 700),
            ("いらっしゃいませ。きょうはりんごがお安いですよ。", MALE_VOICE, 400),
            ("ほんとうですね。じゃあ、りんごを４つください。", FEMALE_VOICE, 400),
            ("はい、４つですね。みかんもいかがですか。", MALE_VOICE, 400),
            ("みかんはきのう買ったから、きょうはりんごをもう１つふやして、５つにします。", FEMALE_VOICE, 400),
            ("はい、りんごが５つですね。ありがとうございます。", MALE_VOICE, 600),
            ("女の人はりんごをいくつ買いますか。", NARRATOR_VOICE, 400)
        ]
    },
    {
        "qNum": 69,
        "subsectionId": "s3_m1",
        "category": "課題理解",
        "title": "男の人は このあと どこへ 行きますか。",
        "illustration_url": "images/listening_n5/n5_q9.jpg",
        "script": "女の人：キムさん、授業が 終わったら いっしょに 食堂で 昼ごはんを 食べませんか。\n男の人：いいですね。でも、その 前に 図書館へ 行って 本を 返したいんです。\n女の人：じゃあ、私は 先に 食堂に 行って 席を とって おきますね。\n男の人：ありがとうございます。本を 返したら すぐ 行きます。",
        "options": ["教室", "図書館", "食堂", "本屋"],
        "correctIndex": 1,
        "explanation": "食堂へ行く前に「図書館へ行って本を返したいんです」と言っているので、このあとまず行くのは「図書館」です。",
        "audioUrl": "audio/mock_n5/n5_m02_q69.mp3",
        "resynthesize": True,
        "tracks": [
            ("２番。女の人と男の人が学校で話しています。男の人はこのあとまずどこへ行きますか。", NARRATOR_VOICE, 700),
            ("キムさん、授業が終わったらいっしょに食堂で昼ごはんを食べませんか。", FEMALE_VOICE, 400),
            ("いいですね。でも、その前に図書館へいって本を返したいんです。", MALE_VOICE, 400),
            ("じゃあ、私は先に食堂にいって席をとっておきますね。", FEMALE_VOICE, 400),
            ("ありがとうございます。本を返したらすぐ行きます。", MALE_VOICE, 600),
            ("男の人はこのあとまずどこへ行きますか。", NARRATOR_VOICE, 400)
        ]
    },
    {
        "qNum": 70,
        "subsectionId": "s3_m1",
        "category": "課題理解",
        "title": "女の人は 何番の バスに 乗りますか。",
        "illustration_url": "images/listening_n5/n5_q10.jpg",
        "script": "女の人：すみません、市民美術館へ 行きたいんですが、どの バスに 乗れば いいですか。\n男の人：市民美術館なら、３番の バスですよ。\n女の人：となりの ２番の バスは 行きますか。\n男の人：２番は 図書館までしか 行きませんから、３番に 乗って ください。\n女の人：わかりました。ありがとうございます。",
        "options": ["１番のバス", "２番のバス", "３番のバス", "４番のバス"],
        "correctIndex": 2,
        "explanation": "「市民美術館なら、3番のバスですよ」と案内されています。",
        "audioUrl": "audio/mock_n5/n5_m02_q70.mp3",
        "resynthesize": True,
        "tracks": [
            ("３番。バス停で女の人と男の人が話しています。女の人は何番のバスに乗りますか。", NARRATOR_VOICE, 700),
            ("すみません、市民美術館へいきたいんですが、どのバスに乗ればいいですか。", FEMALE_VOICE, 400),
            ("市民美術館なら、３番のバスですよ。", MALE_VOICE, 400),
            ("となりの２番のバスは行きますか。", FEMALE_VOICE, 400),
            ("２番は図書館までしか行きませんから、３番に乗ってください。", MALE_VOICE, 400),
            ("わかりました。ありがとうございます。", FEMALE_VOICE, 600),
            ("女の人は何番のバスに乗りますか。", NARRATOR_VOICE, 400)
        ]
    },
    {
        "qNum": 71,
        "subsectionId": "s3_m1",
        "category": "課題理解",
        "title": "男の人は 来週の 火曜日の 朝、何を 出しますか。",
        "illustration_url": "images/listening_n5/n5_q11.jpg",
        "script": "男の人：すみません、この アパートの ゴミの 日を 教えて ください。\n女の人：燃える ゴミは 火曜日と 金曜日の 朝です。\n男の人：新聞や 雑誌は いつですか。\n女の人：新聞や 雑誌は 水曜日の 朝に 出して ください。\n男の人：わかりました。まず 来週の 火曜日に 燃える ゴミを 出します。",
        "options": ["燃えるゴミ", "新聞と雑誌", "びんとカン", "古い服"],
        "correctIndex": 0,
        "explanation": "火曜日と金曜日の朝は「燃えるゴミ」の日で、男の人自身も「来週の火曜日に燃えるゴミを出します」と言っています。",
        "audioUrl": "audio/mock_n5/n5_m02_q71.mp3",
        "resynthesize": True,
        "tracks": [
            ("４番。アパートの前で男の人と女の人が話しています。男の人は来週の火曜日の朝、何を出しますか。", NARRATOR_VOICE, 700),
            ("すみません、このアパートのゴミの日を教えてください。", MALE_VOICE, 400),
            ("燃えるゴミは火曜日と金曜日の朝です。", FEMALE_VOICE, 400),
            ("新聞や雑誌はいつですか。", MALE_VOICE, 400),
            ("新聞や雑誌は水曜日の朝に出してください。", FEMALE_VOICE, 400),
            ("わかりました。まず来週の火曜日に燃えるゴミを出します。", MALE_VOICE, 600),
            ("男の人は来週の火曜日の朝、何を出しますか。", NARRATOR_VOICE, 400)
        ]
    },
    {
        "qNum": 72,
        "subsectionId": "s3_m1",
        "category": "課題理解",
        "title": "女の人は 何階の トイレへ 行きますか。",
        "illustration_url": "images/listening_n5/n5_q12.jpg",
        "script": "女の人：すみません、１階に トイレは ありますか。\n男の人：１階の トイレは いま 掃除中なんです。恐れ入りますが、２階か ３階の トイレを 使って いただけますか。\n女の人：じゃあ、階段で ２階へ 行きます。\n男の人：はい、階段を 上がって すぐ 右に あります。",
        "options": ["１階", "２階", "３階", "４階"],
        "correctIndex": 1,
        "explanation": "1階は掃除中のため、女の人は「じゃあ、階段で2階へ行きます」と答えています。",
        "audioUrl": "audio/mock_n5/n5_m02_q72.mp3",
        "resynthesize": True,
        "tracks": [
            ("５番。デパートで女の人と店員が話しています。女の人は何階のトイレへ行きますか。", NARRATOR_VOICE, 700),
            ("すみません、１かいにトイレはありますか。", FEMALE_VOICE, 400),
            ("１かいのトイレはいま掃除中なんです。恐れ入りますが、２かいか３かいのトイレを使っていただけますか。", MALE_VOICE, 400),
            ("じゃあ、階段で２かいへいきます。", FEMALE_VOICE, 400),
            ("はい、階段を上がってすぐ右にあります。", MALE_VOICE, 600),
            ("女の人は何階のトイレへ行きますか。", NARRATOR_VOICE, 400)
        ]
    },
    {
        "qNum": 73,
        "subsectionId": "s3_m1",
        "category": "課題理解",
        "title": "男の人は かぜ薬を いつ 飲みますか。",
        "illustration_url": "images/listening_n5/n5_q13.jpg",
        "script": "女の人：山田さん、お薬が 出ましたよ。この 白い かぜ薬は 朝と 夜、ごはんを 食べた あとで 飲んで ください。\n男の人：昼は 飲まなくても いいですか。\n女の人：はい、昼は 飲まないで ください。それから、寝る 前に この 青い のどの 薬を 飲んで ください。\n男の人：わかりました。ありがとうございます。",
        "options": ["朝と昼のごはんのあと", "朝と夜のごはんのあと", "昼と夜のごはんのあと", "寝る前だけ"],
        "correctIndex": 1,
        "explanation": "「この白いかぜ薬は朝と夜、ごはんを食べたあとで飲んでください」と説明されています。",
        "audioUrl": "audio/mock_n5/n5_m02_q73.mp3",
        "resynthesize": True,
        "tracks": [
            ("６番。病院で女の人と男の人が話しています。男の人はかぜ薬をいつ飲みますか。", NARRATOR_VOICE, 700),
            ("山田さん、お薬が出ましたよ。この白いかぜ薬は朝と夜、ごはんを食べたあとで飲んでください。", FEMALE_VOICE, 400),
            ("昼は飲まなくてもいいですか。", MALE_VOICE, 400),
            ("はい、昼は飲まないでください。それから、寝る前にこの青いのどの薬を飲んでください。", FEMALE_VOICE, 400),
            ("わかりました。ありがとうございます。", MALE_VOICE, 600),
            ("男の人はかぜ薬をいつ飲みますか。", NARRATOR_VOICE, 400)
        ]
    },
    {
        "qNum": 74,
        "subsectionId": "s3_m1",
        "category": "課題理解",
        "title": "女の人は これから スーパーで 何を 買いますか。",
        "illustration_url": "images/listening_n5/n5_q14.jpg",
        "script": "女の人：晩ごはんに カレーを 作るけど、じゃがいもと たまねぎは ある？\n男の人：うん、野菜は ぜんぶ 冷蔵庫に あるよ。でも、牛肉が ないよ。\n女の人：そう。じゃあ、スーパーへ 行って 牛肉を 買ってくるね。牛乳も 買おうか。\n男の人：牛乳は まだ １本 あるから 大丈夫だよ。\n女の人：わかった。",
        "options": ["じゃがいもとたまねぎ", "牛肉", "牛乳", "牛肉と牛乳"],
        "correctIndex": 1,
        "explanation": "野菜と牛乳はあるので、スーパーで買うのは「牛肉」だけです。",
        "audioUrl": "audio/mock_n5/n5_m02_q74.mp3",
        "resynthesize": True,
        "tracks": [
            ("７番。家で女の人と男の人が話しています。女の人はこれからスーパーで何を買いますか。", NARRATOR_VOICE, 700),
            ("晩ごはんにカレーを作るけど、じゃがいもとたまねぎはある？", FEMALE_VOICE, 400),
            ("うん、野菜はぜんぶ冷蔵庫にあるよ。でも、牛肉がないよ。", MALE_VOICE, 400),
            ("そう。じゃあ、スーパーへいって牛肉を買ってくるね。牛乳も買おうか。", FEMALE_VOICE, 400),
            ("牛乳はまだ１ぽんあるから大丈夫だよ。", MALE_VOICE, 400),
            ("わかった。", FEMALE_VOICE, 600),
            ("女の人はこれからスーパーで何を買いますか。", NARRATOR_VOICE, 400)
        ]
    },
    # --- 問題2: ポイント理解 (Q75〜Q80) ---
    {
        "qNum": 75,
        "subsectionId": "s3_m2",
        "category": "ポイント理解",
        "title": "女の人は きのうの 日曜日、何を しましたか。",
        "illustration_url": "images/listening_n5/n5_q22.jpg",
        "script": "男の人：鈴木さんは きのうの 日曜日、テニスに 行きましたか。\n女の人：いいえ、朝から 強い 雨が ふって いたから、テニスは 中止に なったんです。\n男の人：そうだったんですか。じゃあ、家で ゆっくり 休みましたか。\n女の人：はい、家で 好きな 音楽を 聞いたり、料理を 作ったり しました。\n男の人：それも いい 休日ですね。",
        "options": ["テニスをした", "映画を見に行った", "家で音楽を聞いたり料理をしたりした", "デパートで買い物をした"],
        "correctIndex": 2,
        "explanation": "雨でテニスが中止になり、「家で好きな音楽を聞いたり、料理を作ったりしました」と話しています。",
        "audioUrl": "audio/mock_n5/n5_m02_q75.mp3",
        "resynthesize": True,
        "tracks": [
            ("問題２。１番。男の人と女の人が話しています。女の人はきのうの日曜日、何をしましたか。", NARRATOR_VOICE, 700),
            ("鈴木さんはきのうの日曜日、テニスにいきましたか。", MALE_VOICE, 400),
            ("いいえ、朝から強い雨がふっていたから、テニスは中止になったんです。", FEMALE_VOICE, 400),
            ("そうだったんですか。じゃあ、家でゆっくり休みましたか。", MALE_VOICE, 400),
            ("はい、家で好きな音楽を聞いたり、料理を作ったりしました。", FEMALE_VOICE, 400),
            ("それもいい休日ですね。", MALE_VOICE, 600),
            ("女の人はきのうの日曜日、何をしましたか。", NARRATOR_VOICE, 400)
        ]
    },
    {
        "qNum": 76,
        "subsectionId": "s3_m2",
        "category": "ポイント理解",
        "title": "男の人が いちばん 好きな 季節は いつですか。",
        "illustration_url": "images/listening_n5/n5_q23.jpg",
        "script": "女の人：もうすぐ 春ですね。私は 桜が きれいだから、春が いちばん 好きです。ミラーさんは どうですか。\n男の人：春も いいですが、ぼくは 秋が いちばん 好きです。\n女の人：どうしてですか。\n男の人：すずしくて 山の 木が 赤や 黄色に なって、とても きれいだからです。\n女の人：たしかに 秋の 山は きれいですね。",
        "options": ["春", "夏", "秋", "冬"],
        "correctIndex": 2,
        "explanation": "男の人は「ぼくは秋がいちばん好きです」と答えています。",
        "audioUrl": "audio/mock_n5/n5_m02_q76.mp3",
        "resynthesize": True,
        "tracks": [
            ("２番。女の人と男の人が話しています。男の人がいちばん好きな季節はいつですか。", NARRATOR_VOICE, 700),
            ("もうすぐ春ですね。私は桜がきれいだから、春がいちばん好きです。ミラーさんはどうですか。", FEMALE_VOICE, 400),
            ("春もいいですが、ぼくは秋がいちばん好きです。", MALE_VOICE, 400),
            ("どうしてですか。", FEMALE_VOICE, 400),
            ("すずしくて山の木が赤や黄色になって、とてもきれいだからです。", MALE_VOICE, 400),
            ("たしかに秋の山はきれいですね。", FEMALE_VOICE, 600),
            ("男の人がいちばん好きな季節はいつですか。", NARRATOR_VOICE, 400)
        ]
    },
    {
        "qNum": 77,
        "subsectionId": "s3_m2",
        "category": "ポイント理解",
        "title": "女の人は どうして 新しい カバンを 買いましたか。",
        "illustration_url": "images/listening_n5/n5_q24.jpg",
        "script": "男の人：その カバン、新しいですね。とても すてきな 色ですね。\n女の人：ありがとうございます。きのう 駅前の デパートで 買いました。\n男の人：前の カバンも きれいでしたよね。\n女の人：ええ、でも 前の カバンは 小さくて、大きい ノートや 辞書が 入らなかったんです。これは たくさん 入るので とても 便利です。",
        "options": ["前のカバンが古くなったから", "前のカバンは小さくて辞書が入らなかったから", "デパートで安かったから", "友だちにもらったから"],
        "correctIndex": 1,
        "explanation": "「前のカバンは小さくて、大きいノートや辞書が入らなかったんです」と理由を述べています。",
        "audioUrl": "audio/mock_n5/n5_m02_q77.mp3",
        "resynthesize": True,
        "tracks": [
            ("３番。男の人と女の人が話しています。女の人はどうして新しいカバンを買いましたか。", NARRATOR_VOICE, 700),
            ("そのカバン、新しいですね。とてもすてきな色ですね。", MALE_VOICE, 400),
            ("ありがとうございます。きのう駅前のデパートで買いました。", FEMALE_VOICE, 400),
            ("前のカバンもきれいでしたよね。", MALE_VOICE, 400),
            ("ええ、でも前のカバンは小さくて、大きいノートや辞書が入らなかったんです。これはたくさん入るのでとても便利です。", FEMALE_VOICE, 600),
            ("女の人はどうして新しいカバンを買いましたか。", NARRATOR_VOICE, 400)
        ]
    },
    {
        "qNum": 78,
        "subsectionId": "s3_m2",
        "category": "ポイント理解",
        "title": "男の人は きのう 誰と 映画を 見ましたか。",
        "illustration_url": "images/listening_n5/n5_q25.jpg",
        "script": "女の人：きのうの 映画は どうでしたか。会社の 友だちと 行ったんですか。\n男の人：最初は 会社の 友だちと 行く 予定でしたが、友だちが 急に 仕事に なって しまいました。\n女の人：じゃあ、一人で 見ましたか。\n男の人：いいえ、ちょうど 弟が ひまだったから、弟と いっしょに 見ました。\n女の人：そうでしたか。おもしろかったですか。\n男の人：はい、とても おもしろかったです。",
        "options": ["会社の友だち", "一人で", "弟", "妹"],
        "correctIndex": 2,
        "explanation": "友だちが仕事になったため、「弟といっしょに見ました」と答えています。",
        "audioUrl": "audio/mock_n5/n5_m02_q78.mp3",
        "resynthesize": True,
        "tracks": [
            ("４番。女の人と男の人が話しています。男の人はきのう誰と映画を見ましたか。", NARRATOR_VOICE, 700),
            ("きのうの映画はどうでしたか。会社の友だちといったんですか。", FEMALE_VOICE, 400),
            ("最初は会社の友だちといく予定でしたが、友だちが急に仕事になってしまいました。", MALE_VOICE, 400),
            ("じゃあ、一人で見ましたか。", FEMALE_VOICE, 400),
            ("いいえ、ちょうど弟がひまだったから、弟といっしょに見ました。", MALE_VOICE, 400),
            ("そうでしたか。おもしろかったですか。", FEMALE_VOICE, 400),
            ("はい、とてもおもしろかったです。", MALE_VOICE, 600),
            ("男の人はきのう誰と映画を見ましたか。", NARRATOR_VOICE, 400)
        ]
    },
    {
        "qNum": 79,
        "subsectionId": "s3_m2",
        "category": "ポイント理解",
        "title": "女の人は 毎朝 何を 飲みますか。",
        "illustration_url": "images/listening_n5/n5_q26.jpg",
        "script": "男の人：田中さんは 毎朝 コーヒーを 飲みますか。\n女の人：前は 毎朝 コーヒーを 飲んで いましたが、いまは 飲んで いません。\n男の人：どうしてですか。紅茶に 変えたんですか。\n女の人：いいえ、健康の ために 毎朝 あたたかい 牛乳を 飲んで います。コーヒーは 昼ごはんの あとに １杯だけ 飲みます。",
        "options": ["コーヒー", "紅茶", "牛乳", "緑茶"],
        "correctIndex": 2,
        "explanation": "「健康のために毎朝あたたかい牛乳を飲んでいます」と話しています。",
        "audioUrl": "audio/mock_n5/n5_m02_q79.mp3",
        "resynthesize": True,
        "tracks": [
            ("５番。男の人と女の人が話しています。女の人は毎朝何を飲みますか。", NARRATOR_VOICE, 700),
            ("田中さんは毎朝コーヒーを飲みますか。", MALE_VOICE, 400),
            ("前は毎朝コーヒーを飲んでいましたが、いまは飲んでいません。", FEMALE_VOICE, 400),
            ("どうしてですか。紅茶に変えたんですか。", MALE_VOICE, 400),
            ("いいえ、健康のために毎朝あたたかい牛乳を飲んでいます。コーヒーは昼ごはんのあとに１ぱいだけ飲みます。", FEMALE_VOICE, 600),
            ("女の人は毎朝何を飲みますか。", NARRATOR_VOICE, 400)
        ]
    },
    {
        "qNum": 80,
        "subsectionId": "s3_m2",
        "category": "ポイント理解",
        "title": "図書館は きょう 何時に 閉まりますか。",
        "illustration_url": "images/listening_n5/n5_q27.jpg",
        "script": "男の人：すみません、この 図書館は 夜 ８時まで 開いて いますよね。\n女の人：平日は ８時までですが、きょうは 日曜日ですから 夕方 ５時に 閉まりますよ。\n男の人：えっ、そうなんですか。いま ４時ですから、あと １時間ですね。\n女の人：はい、本を 借りるなら ４時４５分までに カウンターへ お持ちください。",
        "options": ["４時", "４時４５分", "５時", "８時"],
        "correctIndex": 2,
        "explanation": "「きょうは日曜日ですから夕方5時に閉まりますよ」と説明されています。",
        "audioUrl": "audio/mock_n5/n5_m02_q80.mp3",
        "resynthesize": True,
        "tracks": [
            ("６番。図書館で男の人と女の人が話しています。図書館はきょう何時に閉まりますか。", NARRATOR_VOICE, 700),
            ("すみません、この図書館は夜８時まであいていますよね。", MALE_VOICE, 400),
            ("平日は８時までですが、きょうは日曜日ですから夕方５時に閉まりますよ。", FEMALE_VOICE, 400),
            ("えっ、そうなんですか。いま４時ですから、あと１時間ですね。", MALE_VOICE, 400),
            ("はい、本を借りるなら４時４５分までにカウンターへお持ちください。", FEMALE_VOICE, 600),
            ("図書館はきょう何時に閉まりますか。", NARRATOR_VOICE, 400)
        ]
    },
    # --- 問題3: 発話表現 (Q81〜Q85) ---
    {
        "qNum": 81,
        "subsectionId": "s3_m3",
        "category": "発話表現",
        "title": "朝、学校で 先生に 会いました。何と 言いますか。",
        "illustration_url": "images/listening_n5/n5_q36.jpg",
        "script": "朝、学校で 先生に 会いました。何と 言いますか。\n１番：おはようございます。\n２番：こんばんは。\n３番：おやすみなさい。",
        "options": ["おはようございます。", "こんばんは。", "おやすみなさい。"],
        "correctIndex": 0,
        "explanation": "朝、先生や目上の人に会ったときの丁寧な挨拶は「おはようございます」です。",
        "audioUrl": "audio/mock_n5/n5_m02_q81.mp3",
        "resynthesize": True,
        "tracks": [
            ("問題３。１番。朝、学校で先生に会いました。何と言いますか。", NARRATOR_VOICE, 600),
            ("１番。おはようございます。", NARRATOR_VOICE, 500),
            ("２番。こんばんは。", NARRATOR_VOICE, 500),
            ("３番。おやすみなさい。", NARRATOR_VOICE, 500)
        ]
    },
    {
        "qNum": 82,
        "subsectionId": "s3_m3",
        "category": "発話表現",
        "title": "店で 買いたい シャツを 見つけました。店員を 呼ぶとき、何と 言いますか。",
        "illustration_url": "images/listening_n5/n5_q37.jpg",
        "script": "店で 買いたい シャツを 見つけました。店員を 呼ぶとき、何と 言いますか。\n１番：いらっしゃいませ。\n２番：すみません。\n３番：どういたしまして。",
        "options": ["いらっしゃいませ。", "すみません。", "どういたしまして。"],
        "correctIndex": 1,
        "explanation": "お店で店員さんに声をかけるときは「すみません」と言います。",
        "audioUrl": "audio/mock_n5/n5_m02_q82.mp3",
        "resynthesize": True,
        "tracks": [
            ("２番。店で買いたいシャツを見つけました。店員を呼ぶとき、何と言いますか。", NARRATOR_VOICE, 600),
            ("１番。いらっしゃいませ。", NARRATOR_VOICE, 500),
            ("２番。すみません。", NARRATOR_VOICE, 500),
            ("３番。どういたしまして。", NARRATOR_VOICE, 500)
        ]
    },
    {
        "qNum": 83,
        "subsectionId": "s3_m3",
        "category": "発話表現",
        "title": "友だちが かぜを ひきました。友だちに 何と 言いますか。",
        "illustration_url": "images/listening_n5/n5_q38.jpg",
        "script": "友だちが かぜを ひきました。友だちに 何と 言いますか。\n１番：おめでとうございます。\n２番：おだいじに。\n３番：かしこまりました。",
        "options": ["おめでとうございます。", "おだいじに。", "かしこまりました。"],
        "correctIndex": 1,
        "explanation": "病気やけがをした人を気遣う言葉は「おだいじに（お大事に）」です。",
        "audioUrl": "audio/mock_n5/n5_m02_q83.mp3",
        "resynthesize": True,
        "tracks": [
            ("３番。友だちがかぜをひきました。友だちに何と言いますか。", NARRATOR_VOICE, 600),
            ("１番。おめでとうございます。", NARRATOR_VOICE, 500),
            ("２番。おだいじに。", NARRATOR_VOICE, 500),
            ("３番。かしこまりました。", NARRATOR_VOICE, 500)
        ]
    },
    {
        "qNum": 84,
        "subsectionId": "s3_m3",
        "category": "発話表現",
        "title": "先生の 話す 声が 小さくて よく 聞こえません。何と 言いますか。",
        "illustration_url": "images/listening_n5/n5_q39.jpg",
        "script": "先生の 話す 声が 小さくて よく 聞こえません。何と 言いますか。\n１番：もう 一度 言って ください。\n２番：静かに して ください。\n３番：ゆっくり 歩いて ください。",
        "options": ["もう 一度 言って ください。", "静かに して ください。", "ゆっくり 歩いて ください。"],
        "correctIndex": 0,
        "explanation": "よく聞き取れなかったときは「もう一度言ってください」とお願いします。",
        "audioUrl": "audio/mock_n5/n5_m02_q84.mp3",
        "resynthesize": True,
        "tracks": [
            ("４番。先生の話す声が小さくてよく聞こえません。何と言いますか。", NARRATOR_VOICE, 600),
            ("１番。もう一度言ってください。", NARRATOR_VOICE, 500),
            ("２番。静かにしてください。", NARRATOR_VOICE, 500),
            ("３番。ゆっくり歩いてください。", NARRATOR_VOICE, 500)
        ]
    },
    {
        "qNum": 85,
        "subsectionId": "s3_m3",
        "category": "発話表現",
        "title": "自分の 家へ 帰って 来ました。家の 人に 何と 言いますか。",
        "illustration_url": "images/listening_n5/n5_q40.jpg",
        "script": "自分の 家へ 帰って 来ました。家の 人に 何と 言いますか。\n１番：いってきます。\n２番：ただいま。\n３番：おじゃまします。",
        "options": ["いってきます。", "ただいま。", "おじゃまします。"],
        "correctIndex": 1,
        "explanation": "自分の家に帰宅したときの挨拶は「ただいま」です。",
        "audioUrl": "audio/mock_n5/n5_m02_q85.mp3",
        "resynthesize": True,
        "tracks": [
            ("５番。自分の家へ帰ってきました。家の人に何と言いますか。", NARRATOR_VOICE, 600),
            ("１番。いってきます。", NARRATOR_VOICE, 500),
            ("２番。ただいま。", NARRATOR_VOICE, 500),
            ("３番。おじゃまします。", NARRATOR_VOICE, 500)
        ]
    },
    # --- 問題4: 即時応答 (Q86〜Q91) ---
    {
        "qNum": 86,
        "subsectionId": "s3_m4",
        "category": "即時応答",
        "title": "すみません、いま 何時ですか。",
        "illustration_url": "images/listening_n5/n5_q52.jpg",
        "script": "女の人：すみません、いま 何時ですか。\n１番：２時半です。\n２番：２時間です。\n３番：２日です。",
        "options": ["２時半です。", "２時間です。", "２日です。"],
        "correctIndex": 0,
        "explanation": "「いま何時ですか」と時刻を聞かれているので「２時半です」が正解です。",
        "audioUrl": "audio/mock_n5/n5_m02_q86.mp3",
        "resynthesize": True,
        "tracks": [
            ("問題４。１番。", NARRATOR_VOICE, 400),
            ("すみません、いま何時ですか。", FEMALE_VOICE, 600),
            ("１番。２時半です。", MALE_VOICE, 400),
            ("２番。２時間です。", MALE_VOICE, 400),
            ("３番。ふつかです。", MALE_VOICE, 500)
        ]
    },
    {
        "qNum": 87,
        "subsectionId": "s3_m4",
        "category": "即時応答",
        "title": "この ケーキ、とても おいしいですね。",
        "illustration_url": "images/listening_n5/n5_q53.jpg",
        "script": "男の人：この ケーキ、とても おいしいですね。\n１番：ええ、ほんとうですね。\n２番：いいえ、ちがいます。\n３番：まだ 食べて いません。",
        "options": ["ええ、ほんとうですね。", "いいえ、ちがいます。", "まだ 食べて いません。"],
        "correctIndex": 0,
        "explanation": "「おいしいですね」と同意を求められたときの自然な返事は「ええ、ほんとうですね」です。",
        "audioUrl": "audio/mock_n5/n5_m02_q87.mp3",
        "resynthesize": True,
        "tracks": [
            ("２番。", NARRATOR_VOICE, 400),
            ("このケーキ、とてもおいしいですね。", MALE_VOICE, 600),
            ("１番。ええ、ほんとうですね。", FEMALE_VOICE, 400),
            ("２番。いいえ、ちがいます。", FEMALE_VOICE, 400),
            ("３番。まだ食べていません。", FEMALE_VOICE, 500)
        ]
    },
    {
        "qNum": 88,
        "subsectionId": "s3_m4",
        "category": "即時応答",
        "title": "あしたの 朝、何時に 起きますか。",
        "illustration_url": "images/listening_n5/n5_q54.jpg",
        "script": "女の人：あしたの 朝、何時に 起きますか。\n１番：６時に 起きます。\n２番：朝ごはんを 食べます。\n３番：きのう 起きました。",
        "options": ["６時に 起きます。", "朝ごはんを 食べます。", "きのう 起きました。"],
        "correctIndex": 0,
        "explanation": "「何時に起きますか」と聞かれているので「６時に起きます」が正解です。",
        "audioUrl": "audio/mock_n5/n5_m02_q88.mp3",
        "resynthesize": True,
        "tracks": [
            ("３番。", NARRATOR_VOICE, 400),
            ("あしたの朝、何時に起きますか。", FEMALE_VOICE, 600),
            ("１番。６時に起きます。", MALE_VOICE, 400),
            ("２番。朝ごはんを食べます。", MALE_VOICE, 400),
            ("３番。きのう起きました。", MALE_VOICE, 500)
        ]
    },
    {
        "qNum": 89,
        "subsectionId": "s3_m4",
        "category": "即時応答",
        "title": "コーヒーを もう １杯 いかがですか。",
        "illustration_url": "images/listening_n5/n5_q55.jpg",
        "script": "男の人：コーヒーを もう １杯 いかがですか。\n１番：いいえ、もう けっこうです。\n２番：はい、コーヒーです。\n３番：ごちそうさまでした。",
        "options": ["いいえ、もう けっこうです。", "はい、コーヒーです。", "ごちそうさまでした。"],
        "correctIndex": 0,
        "explanation": "おかわりを勧められて丁寧に断るときは「いいえ、もうけっこうです」と言います。",
        "audioUrl": "audio/mock_n5/n5_m02_q89.mp3",
        "resynthesize": True,
        "tracks": [
            ("４番。", NARRATOR_VOICE, 400),
            ("コーヒーをもう１ぱいいかがですか。", MALE_VOICE, 600),
            ("１番。いいえ、もうけっこうです。", FEMALE_VOICE, 400),
            ("２番。はい、コーヒーです。", FEMALE_VOICE, 400),
            ("３番。ごちそうさまでした。", FEMALE_VOICE, 500)
        ]
    },
    {
        "qNum": 90,
        "subsectionId": "s3_m4",
        "category": "即時応答",
        "title": "毎日 どうやって 学校へ 来ますか。",
        "illustration_url": "images/listening_n5/n5_q56.jpg",
        "script": "女の人：毎日 どうやって 学校へ 来ますか。\n１番：自転車で 来ます。\n２番：８時に 来ます。\n３番：一人で 勉強します。",
        "options": ["自転車で 来ます。", "８時に 来ます。", "一人で 勉強します。"],
        "correctIndex": 0,
        "explanation": "「どうやって（交通手段）」を聞かれているので「自転車で来ます」が正解です。",
        "audioUrl": "audio/mock_n5/n5_m02_q90.mp3",
        "resynthesize": True,
        "tracks": [
            ("５番。", NARRATOR_VOICE, 400),
            ("毎日どうやって学校へきますか。", FEMALE_VOICE, 600),
            ("１番。自転車できます。", MALE_VOICE, 400),
            ("２番。８時にきます。", MALE_VOICE, 400),
            ("３番。一人で勉強します。", MALE_VOICE, 500)
        ]
    },
    {
        "qNum": 91,
        "subsectionId": "s3_m4",
        "category": "即時応答",
        "title": "ちょっと 窓を 開けても いいですか。",
        "illustration_url": "images/listening_n5/n5_q57.jpg",
        "script": "男の人：ちょっと 窓を 開けても いいですか。\n１番：ええ、どうぞ。\n２番：はい、開いて います。\n３番：いいえ、閉めました。",
        "options": ["ええ、どうぞ。", "はい、開いて います。", "いいえ、閉めました。"],
        "correctIndex": 0,
        "explanation": "「〜てもいいですか」と許可を求められたときは「ええ、どうぞ」と答えます。",
        "audioUrl": "audio/mock_n5/n5_m02_q91.mp3",
        "resynthesize": True,
        "tracks": [
            ("６番。", NARRATOR_VOICE, 400),
            ("ちょっと窓を開けてもいいですか。", MALE_VOICE, 600),
            ("１番。ええ、どうぞ。", FEMALE_VOICE, 400),
            ("２番。はい、あいています。", FEMALE_VOICE, 400),
            ("３番。いいえ、閉めました。", FEMALE_VOICE, 500)
        ]
    }
]


def synthesize_needed_audio():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/yamauchimiku/Documents/GitHub/japanese-learning/secrets/google_tts_key.json'
    tts_client = texttospeech.TextToSpeechClient()
    base_dir = '/Users/yamauchimiku/Documents/GitHub/japanese-learning'

    all_items = SET1_QUESTIONS + SET2_QUESTIONS
    for item in all_items:
        if not item.get("resynthesize"):
            continue
        rel_path = item["audioUrl"]
        fpath = os.path.join(base_dir, rel_path)
        pub_path = os.path.join(base_dir, "public", rel_path)
        os.makedirs(os.path.dirname(fpath), exist_ok=True)
        os.makedirs(os.path.dirname(pub_path), exist_ok=True)

        comb = bytearray()
        for txt, voice_name, pause_ms in item["tracks"]:
            sinput = texttospeech.SynthesisInput(text=txt)
            voice = texttospeech.VoiceSelectionParams(language_code='ja-JP', name=voice_name)
            aconf = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3, speaking_rate=0.92)
            resp = tts_client.synthesize_speech(input=sinput, voice=voice, audio_config=aconf)
            comb.extend(resp.audio_content)
            if pause_ms > 0:
                p_ssml = f'<speak><break time="{pause_ms}ms"/></speak>'
                p_in = texttospeech.SynthesisInput(ssml=p_ssml)
                p_resp = tts_client.synthesize_speech(input=p_in, voice=voice, audio_config=aconf)
                comb.extend(p_resp.audio_content)

        with open(fpath, "wb") as f:
            f.write(comb)
        with open(pub_path, "wb") as f:
            f.write(comb)
        print(f"Synthesized {rel_path} ({len(comb)} bytes)")


if __name__ == "__main__":
    synthesize_needed_audio()
