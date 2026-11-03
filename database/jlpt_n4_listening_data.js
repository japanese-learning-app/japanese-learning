window.JLPT_N4_LISTENING_DATA = {
  "test_id": "jlpt_n4_listening_test_01",
  "title": "JLPT N4 聴解実戦模試 第1回",
  "level": "N4",
  "total_questions": 28,
  "sections": [
    {
      "section_id": "sec1",
      "title": "問題1 課題理解",
      "count": 8,
      "desc": "質問を聞いて、次に何をすべきかを正確に聞き取る問題です。"
    },
    {
      "section_id": "sec2",
      "title": "問題2 ポイント理解",
      "count": 7,
      "desc": "質問を聞いた後、選択肢を読む時間があります。ポイントを聞き取ります。"
    },
    {
      "section_id": "sec3",
      "title": "問題3 発話表現",
      "count": 5,
      "desc": "場面に合わせてどのような表現を使うべきかを選ぶ問題です（3択）。"
    },
    {
      "section_id": "sec4",
      "title": "問題4 即時応答",
      "count": 8,
      "desc": "短い問いかけに対して、最も自然な返答を瞬時に選ぶ問題です（3択）。"
    }
  ],
  "questions": [
    {
      "q_num": 1,
      "section_id": "sec1",
      "section_name": "問題1 課題理解",
      "situation": "病院で看護師と男性が話しています。男性はこの後、まず何をしますか。",
      "speech_audio_text": "病院で看護師と男の人が話しています。男の人はこの後、まず何をしますか。看護師：佐藤さん、今日はお熱が38度ありますね。医師の診察の前に、まずこちらの体温計でもう一度熱を測っていただけますか。男：わかりました。あ、保険証は今出しますか。看護師：保険証とお薬手帳は、熱を測り終わった後で受付にお出しください。男：わかりました。じゃあ、今すぐ測りますね。男の人はこの後、まず何をしますか。",
      "prompt": "男の人はこの<ruby>後<rt>あと</rt></ruby>、まず<ruby>何<rt>なに</rt></ruby>をしますか。",
      "audio_file": "audio/listening/n4_q1.mp3",
      "choices": [
        "体温計でもう一度熱を測る。",
        "受付に保険証とお薬手帳を出す。",
        "薬局へ薬をもらいに行く。",
        "診察室に入って医師と話す。"
      ],
      "answer": 0,
      "explanation": {
        "ja": "看護師から「医師の診察の前に、まずこちらの体温計でもう一度熱を測ってください」と指示され、保険証は測った後でよいとされているため、選択肢1が正解です。",
        "en": "The nurse tells him to measure his temperature again first before handing in insurance cards. Choice 1 is correct.",
        "zh": "護士指示看診前先用體溫計再量一次體溫，健保卡等量完後再交，因此最先做的是選項1。",
        "ko": "간호사가 진료 전에 먼저 체온계로 열을 다시 재달라고 지시했고 보험증은 그 후에 내라고 했으므로 1번이 정답입니다."
      },
      "section": "問題1 課題理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】病院で看護師と男性が話しています。男性はこの後、まず何をしますか。</p>\n      <p class=\"text-xs text-slate-700\">病院で看護師と男の人が話しています。男の人はこの後、まず何をしますか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">看護師：</span>佐藤さん、今日はお熱が38度ありますね。医師の診察の前に、まずこちらの体温計でもう一度熱を測っていただけますか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>わかりました。あ、保険証は今出しますか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">看護師：</span>保険証とお薬手帳は、熱を測り終わった後で受付にお出しください。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>わかりました。じゃあ、今すぐ測りますね。男の人はこの後、まず何をしますか。</p>\n    </div>"
    },
    {
      "q_num": 2,
      "section_id": "sec1",
      "section_name": "問題1 課題理解",
      "situation": "会社で女性社員と課長が話しています。女性社員はこの後、何を準備しますか。",
      "speech_audio_text": "会社で女の人と課長が話しています。女の人はこの後、何を準備しますか。課長：高橋さん、午後の会議の資料、何部印刷した？女：15部印刷してホチキスで留めました。課長：ありがとう。あ、参加者が急に2名増えて17名になったんだ。追加で2部コピーしてくれるかい？女：わかりました。プロジェクターのリモコンも用意しておきましょうか。課長：それは僕が持っていくから大丈夫だよ。資料の追加だけお願いね。女：かしこまりました。女の人はこの後、何を準備しますか。",
      "prompt": "<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>はこの<ruby>後<rt>あと</rt></ruby>、<ruby>何<rt>なに</rt></ruby>を<ruby>準備<rt>じゅんび</rt></ruby>しますか。",
      "audio_file": "audio/listening/n4_q2.mp3",
      "choices": [
        "プロジェクターのリモコンを探す。",
        "会議資料を2部追加でコピーする。",
        "会議室の机と椅子を2つ並べる。",
        "15部印刷した資料を捨てる。"
      ],
      "answer": 1,
      "explanation": {
        "ja": "参加者が増えたため、課長から「追加で2部コピーしてくれるかい」と頼まれ、リモコンは課長が持っていくと言っているため、女性は選択肢2を行います。",
        "en": "The manager asks her to copy 2 additional sets of materials since attendees increased. Choice 2 is correct.",
        "zh": "由於與會人數增加，主管請她追加複印2份會議資料，投影機遙控器由主管自帶，因此女性要準備的是選項2。",
        "ko": "참석자가 늘어 과장이 회의 자료를 2부 추가 복사해 달라고 부탁했으므로 2번이 정답입니다."
      },
      "section": "問題1 課題理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】会社で女性社員と課長が話しています。女性社員はこの後、何を準備しますか。</p>\n      <p class=\"text-xs text-slate-700\">会社で女の人と課長が話しています。女の人はこの後、何を準備しますか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">課長：</span>高橋さん、午後の会議の資料、何部印刷した？</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>15部印刷してホチキスで留めました。</p>\n<p><span class=\"font-bold text-[#1995AD]\">課長：</span>ありがとう。あ、参加者が急に2名増えて17名になったんだ。追加で2部コピーしてくれるかい？</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>わかりました。プロジェクターのリモコンも用意しておきましょうか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">課長：</span>それは僕が持っていくから大丈夫だよ。資料の追加だけお願いね。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>かしこまりました。女の人はこの後、何を準備しますか。</p>\n    </div>"
    },
    {
      "q_num": 3,
      "section_id": "sec1",
      "section_name": "問題1 課題理解",
      "situation": "大学の事務室で留学生と職員が話しています。留学生は明日、何を持ってこなければなりませんか。",
      "speech_audio_text": "大学で留学生の男の人と職員が話しています。留学生は明日、何を持ってこなければなりませんか。男：すみません、奨学金の申し込み書類を持ってきました。職員：はい、拝見しますね。……申請書と成績証明書は揃っていますね。あ、証明写真が貼られていませんよ。男：あ、写真を貼るのを忘れていました！職員：裏面に名前を書いたカラー写真を1枚、明日までに持ってきてください。学生証のコピーは事務室で取れますから要りませんよ。男：わかりました。明日写真を持ってきます。留学生は明日、何を持ってこなければなりませんか。",
      "prompt": "<ruby>留学生<rt>りゅうがくせい</rt></ruby>は<ruby>明日<rt>あす</rt></ruby>、<ruby>何<rt>なに</rt></ruby>を<ruby>持<rt>も</rt></ruby>ってこなければなりませんか。",
      "audio_file": "audio/listening/n4_q3.mp3",
      "choices": [
        "成績証明書",
        "学生証のコピー",
        "裏面に名前を書いた証明写真1枚",
        "パスポートの原本"
      ],
      "answer": 2,
      "explanation": {
        "ja": "職員から「裏面に名前を書いたカラー写真を1枚、明日までに持ってきてください」と指示されているため、選択肢3が正解です。",
        "en": "The staff member instructs him to bring 1 color ID photo with his name written on the back tomorrow. Choice 3 is correct.",
        "zh": "職員告知背面寫有姓名的一張彩色證件照必須在明天帶過來，因此選項3正確。",
        "ko": "직원이 뒷면에 이름을 적은 컬러 증명사진 1장을 내일까지 가져오라고 지시했으므로 3번이 정답입니다."
      },
      "section": "問題1 課題理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】大学の事務室で留学生と職員が話しています。留学生は明日、何を持ってこなければなりませんか。</p>\n      <p class=\"text-xs text-slate-700\">大学で留学生の男の人と職員が話しています。留学生は明日、何を持ってこなければなりませんか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>すみません、奨学金の申し込み書類を持ってきました。職員：はい、拝見しますね。……申請書と成績証明書は揃っていますね。あ、証明写真が貼られていませんよ。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>あ、写真を貼るのを忘れていました！職員：裏面に名前を書いたカラー写真を1枚、明日までに持ってきてください。学生証のコピーは事務室で取れますから要りませんよ。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>わかりました。明日写真を持ってきます。留学生は明日、何を持ってこなければなりませんか。</p>\n    </div>"
    },
    {
      "q_num": 4,
      "section_id": "sec1",
      "section_name": "問題1 課題理解",
      "situation": "友達同士が明日の映画について電話で話しています。二人は明日、何時にどこで会いますか。",
      "speech_audio_text": "男の人と女の人が電話で話しています。二人は明日、何時にどこで会いますか。男：もしもし、明日の映画だけど、14時に映画館の前で待ち合わせでいい？女：映画が14時半からだから、少し早めに会ってチケットを発券しない？14時だと混んでいてギリギリになっちゃうかも。男：そうだね。じゃあ30分前の14時に駅の改札前はどう？女：うん、中央改札の前ならわかりやすいね。じゃあ14時に駅の中央改札で会おう！男：わかった、じゃあ明日ね！二人は明日、何時にどこで会いますか。",
      "prompt": "<ruby>二人<rt>ふたり</rt></ruby>は<ruby>明日<rt>あす</rt></ruby>、<ruby>何時<rt>なんじ</rt></ruby>にどこで<ruby>会<rt>あ</rt></ruby>いますか。",
      "audio_file": "audio/listening/n4_q4.mp3",
      "choices": [
        "13時30分に映画館の前",
        "14時に映画館の売店",
        "14時30分に駅のホーム",
        "14時に駅の中央改札前"
      ],
      "answer": 3,
      "explanation": {
        "ja": "男性が「じゃあ14時に駅の改札前はどう？」と提案し、女性が「中央改札の前ならわかりやすいね。14時に駅の中央改札で会おう」と合意しているため、選択肢4が正解です。",
        "en": "They agree to meet at 14:00 (2:00 PM) in front of the station's central ticket gate. Choice 4 is correct.",
        "zh": "兩人商定下午14點在車站的中央檢票口前碰面，因此選項4正確。",
        "ko": "두 사람은 내일 14시에 역 중앙 개찰구 앞에서 만나기로 합의했으므로 4번이 정답입니다."
      },
      "section": "問題1 課題理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】友達同士が明日の映画について電話で話しています。二人は明日、何時にどこで会いますか。</p>\n      <p class=\"text-xs text-slate-700\">男の人と女の人が電話で話しています。二人は明日、何時にどこで会いますか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>もしもし、明日の映画だけど、14時に映画館の前で待ち合わせでいい？</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>映画が14時半からだから、少し早めに会ってチケットを発券しない？14時だと混んでいてギリギリになっちゃうかも。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>そうだね。じゃあ30分前の14時に駅の改札前はどう？</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>うん、中央改札の前ならわかりやすいね。じゃあ14時に駅の中央改札で会おう！</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>わかった、じゃあ明日ね！二人は明日、何時にどこで会いますか。</p>\n    </div>"
    },
    {
      "q_num": 5,
      "section_id": "sec1",
      "section_name": "問題1 課題理解",
      "situation": "レストランで客と店員が話しています。店員はこの後、まず何を運んできますか。",
      "speech_audio_text": "レストランで客と店員が話しています。店員はこの後、まず何を運んできますか。客：すみません、パスタとハンバーグセットを注文したいんですが。店員：かしこまりました。セットにはコーヒーか紅茶がつきますが、食後にお持ちしますか。客：あ、外が暑かったので、アイスコーヒーを先にもらえますか。店員：かしこまりました。お冷とおしぼりもお持ちしますね。客：あ、お冷は今持っていますから大丈夫ですよ。アイスコーヒーだけお願いします。店員：承知いたしました。店員はこの後、まず何を運んできますか。",
      "prompt": "<ruby>店員<rt>てんいん</rt></ruby>はこの<ruby>後<rt>あと</rt></ruby>、まず<ruby>何<rt>なに</rt></ruby>を<ruby>運<rt>はこ</rt></ruby>んできますか。",
      "audio_file": "audio/listening/n4_q5.mp3",
      "choices": [
        "パスタとハンバーグ",
        "熱い紅茶",
        "アイスコーヒー",
        "氷の入ったお冷"
      ],
      "answer": 2,
      "explanation": {
        "ja": "客から「アイスコーヒーを先に」「お冷は持っているからアイスコーヒーだけでよい」と言われたため、まず運ぶのはアイスコーヒーです。選択肢3が正解です。",
        "en": "The customer requests iced coffee first and declines water, so the server brings iced coffee first. Choice 3 is correct.",
        "zh": "客人要求先上一杯冰咖啡，並表示不需要水，因此店員首先送上的是冰咖啡，選項3正確。",
        "ko": "손님이 아이스커피를 먼저 달라고 하고 물은 사양했으므로 점원이 먼저 가져올 것은 아이스커피입니다. 3번이 정답입니다."
      },
      "section": "問題1 課題理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】レストランで客と店員が話しています。店員はこの後、まず何を運んできますか。</p>\n      <p class=\"text-xs text-slate-700\">レストランで客と店員が話しています。店員はこの後、まず何を運んできますか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">客：</span>すみません、パスタとハンバーグセットを注文したいんですが。</p>\n<p><span class=\"font-bold text-[#1995AD]\">店員：</span>かしこまりました。セットにはコーヒーか紅茶がつきますが、食後にお持ちしますか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">客：</span>あ、外が暑かったので、アイスコーヒーを先にもらえますか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">店員：</span>かしこまりました。お冷とおしぼりもお持ちしますね。</p>\n<p><span class=\"font-bold text-[#1995AD]\">客：</span>あ、お冷は今持っていますから大丈夫ですよ。アイスコーヒーだけお願いします。</p>\n<p><span class=\"font-bold text-[#1995AD]\">店員：</span>承知いたしました。店員はこの後、まず何を運んできますか。</p>\n    </div>"
    },
    {
      "q_num": 6,
      "section_id": "sec1",
      "section_name": "問題1 課題理解",
      "situation": "駅の窓口で駅員と外国人観光客が話しています。観光客はこの後、どのホームへ行きますか。",
      "speech_audio_text": "駅で駅員と外国人の旅行客が話しています。旅行客はこの後、どのホームへ行きますか。客：すみません、京都駅に行きたいのですが、どの電車に乗ればいいですか。駅員：京都ですね。快速電車なら3番ホーム、特急電車なら4番ホームです。客：速く着く特急に乗りたいです。駅員：特急ですね。特急券はお持ちですか。客：はい、さっき券売機で買いました。駅員：では、4番ホームへお進みください。10分後に電車がまいります。客：ありがとうございます！旅行客はこの後、どのホームへ行きますか。",
      "prompt": "<ruby>旅行客<rt>りょこうきゃく</rt></ruby>はこの<ruby>後<rt>あと</rt></ruby>、どのホームへ<ruby>行<rt>い</rt></ruby>きますか。",
      "audio_file": "audio/listening/n4_q6.mp3",
      "choices": [
        "1番ホーム",
        "4番ホーム",
        "3番ホーム",
        "2番ホーム"
      ],
      "answer": 1,
      "explanation": {
        "ja": "特急券を持っており特急に乗りたいと希望したため、駅員から「4番ホームへお進みください」と案内されています。選択肢2が正解です。",
        "en": "The passenger has an express ticket and wants the limited express, so the attendant directs him to Platform 4. Choice 2 is correct.",
        "zh": "旅客持有特急券並想搭特急列車，站務員指示前往4號月台，因此選項2正確。",
        "ko": "승객이 특급을 타겠다고 하고 특급권을 소지하고 있어 역무원이 2번 홈으로 가라고 안내했으므로 2번이 정답입니다."
      },
      "section": "問題1 課題理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】駅の窓口で駅員と外国人観光客が話しています。観光客はこの後、どのホームへ行きますか。</p>\n      <p class=\"text-xs text-slate-700\">駅で駅員と外国人の旅行客が話しています。旅行客はこの後、どのホームへ行きますか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">客：</span>すみません、京都駅に行きたいのですが、どの電車に乗ればいいですか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">駅員：</span>京都ですね。快速電車なら3番ホーム、特急電車なら4番ホームです。</p>\n<p><span class=\"font-bold text-[#1995AD]\">客：</span>速く着く特急に乗りたいです。</p>\n<p><span class=\"font-bold text-[#1995AD]\">駅員：</span>特急ですね。特急券はお持ちですか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">客：</span>はい、さっき券売機で買いました。</p>\n<p><span class=\"font-bold text-[#1995AD]\">駅員：</span>では、4番ホームへお進みください。10分後に電車がまいります。</p>\n<p><span class=\"font-bold text-[#1995AD]\">客：</span>ありがとうございます！旅行客はこの後、どのホームへ行きますか。</p>\n    </div>"
    },
    {
      "q_num": 7,
      "section_id": "sec1",
      "section_name": "問題1 課題理解",
      "situation": "アパートで引っ越しの手伝いに来た男性と女性が話しています。男性はこの後、まず何をしますか。",
      "speech_audio_text": "アパートで男の人と女の人が話しています。男の人はこの後、まず何をしますか。男：手伝いに来たよ！何から始めようか？女：ありがとう、助かるわ。本や小物はもうダンボールに詰めたから、台所のお皿を割れないように新聞紙で包んでほしいの。男：わかった。ダンボールを車に運ぶのは後でいい？女：ええ、荷物が全部まとまってから一気に車へ運びましょう。お皿の新聞紙は流しの下にあるから使ってね。男：よし、じゃあお皿を包むね。男の人はこの後、まず何をしますか。",
      "prompt": "男の人はこの<ruby>後<rt>あと</rt></ruby>、まず<ruby>何<rt>なに</rt></ruby>をしますか。",
      "audio_file": "audio/listening/n4_q7.mp3",
      "choices": [
        "新しいアパートへ車を運転する。",
        "ダンボールを車へ運ぶ。",
        "本や小物をダンボールに詰める。",
        "台所のお皿を新聞紙で包む。"
      ],
      "answer": 3,
      "explanation": {
        "ja": "車への運搬は後回しにして「台所のお皿を割れないように新聞紙で包んでほしい」と頼まれ、男性も「じゃあお皿を包むね」と答えています。選択肢4が正解です。",
        "en": "The woman asks him to wrap the kitchen plates in newspaper first before moving boxes to the car. Choice 4 is correct.",
        "zh": "女性請他先用報紙把廚房的碗盤包好以防摔破，搬上車等全部打包完再做，因此選項4正確。",
        "ko": "차로 나르는 것은 나중에 하고 먼저 주방의 접시를 신문지로 싸달라고 부탁했으므로 4번이 정답입니다."
      },
      "section": "問題1 課題理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】アパートで引っ越しの手伝いに来た男性と女性が話しています。男性はこの後、まず何をしますか。</p>\n      <p class=\"text-xs text-slate-700\">アパートで男の人と女の人が話しています。男の人はこの後、まず何をしますか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>手伝いに来たよ！何から始めようか？</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>ありがとう、助かるわ。本や小物はもうダンボールに詰めたから、台所のお皿を割れないように新聞紙で包んでほしいの。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>わかった。ダンボールを車に運ぶのは後でいい？</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>ええ、荷物が全部まとまってから一気に車へ運びましょう。お皿の新聞紙は流しの下にあるから使ってね。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>よし、じゃあお皿を包むね。男の人はこの後、まず何をしますか。</p>\n    </div>"
    },
    {
      "q_num": 8,
      "section_id": "sec1",
      "section_name": "問題1 課題理解",
      "situation": "パン屋で店長とアルバイトの店員が話しています。アルバイトはこの後、何をしますか。",
      "speech_audio_text": "パン屋で店長とアルバイトの女性が話しています。アルバイトはこの後、何をしますか。店長：鈴木さん、焼き立てのカレーパンが焼き上がったよ。鈴木：はい、すぐに店頭の棚に並べますね。店長：ありがとう。あ、並べる前に、トングとトレーの消毒をして補充してくれるかい？ちょうど今、お客さんがたくさん入ってきて足りなくなりそうなんだ。鈴木：わかりました！トングとトレーを消毒して入り口に置いてから、パンを並べますね。アルバイトはこの後、何をしますか。",
      "prompt": "アルバイトはこの<ruby>後<rt>あと</rt></ruby>、<ruby>何<rt>なに</rt></ruby>をしますか。",
      "audio_file": "audio/listening/n4_q8.mp3",
      "choices": [
        "トングとトレーを消毒して入り口に補充する。",
        "カレーパンの生地をこねる。",
        "レジでお金の計算をする。",
        "外の看板を片付ける。"
      ],
      "answer": 0,
      "explanation": {
        "ja": "パンを並べる前に「トングとトレーの消毒をして補充して」と指示され、女性も「トングとトレーを消毒して置いてからパンを並べる」と答えています。選択肢1が正解です。",
        "en": "The manager instructs her to disinfect and restock tongs and trays before displaying the freshly baked bread. Choice 1 is correct.",
        "zh": "店長指示在擺放麵包前先消毒夾子和托盤並補充到門口，因此選項1正確。",
        "ko": "빵을 진열하기 전에 쟁반과 집게를 소독하여 입구에 보충해 달라고 지시했으므로 1번이 정답입니다."
      },
      "section": "問題1 課題理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】パン屋で店長とアルバイトの店員が話しています。アルバイトはこの後、何をしますか。</p>\n      <p class=\"text-xs text-slate-700\">パン屋で店長とアルバイトの女性が話しています。アルバイトはこの後、何をしますか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">店長：</span>鈴木さん、焼き立てのカレーパンが焼き上がったよ。鈴木：はい、すぐに店頭の棚に並べますね。</p>\n<p><span class=\"font-bold text-[#1995AD]\">店長：</span>ありがとう。あ、並べる前に、トングとトレーの消毒をして補充してくれるかい？ちょうど今、お客さんがたくさん入ってきて足りなくなりそうなんだ。鈴木：わかりました！トングとトレーを消毒して入り口に置いてから、パンを並べますね。アルバイトはこの後、何をしますか。</p>\n    </div>"
    },
    {
      "q_num": 9,
      "section_id": "sec2",
      "section_name": "問題2 ポイント理解",
      "situation": "友達同士の男性と女性が話しています。女性が先週の休日に海へ行かなかった理由は何ですか。",
      "speech_audio_text": "男の人と女の人が話しています。女の人が先週の休日に海へ行かなかった理由は何ですか。男：林さん、先週の日曜日は友達と海へ行くって言ってたよね。泳いできた？女：ううん、実は行けなくなっちゃったの。男：えっ、雨が降ったから？女：ううん、お天気はすごく良くて海日和だったんだけど、前日の夜に妹が急に高熱を出してしまって。両親が仕事でいなかったから、私が看病しなきゃいけなくて。男：そうだったんだ。大変だったね。女の人が先週の休日に海へ行かなかった理由は何ですか。",
      "prompt": "<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>が<ruby>先週<rt>せんしゅう</rt></ruby>の<ruby>休日<rt>きゅうじつ</rt></ruby>に<ruby>海<rt>うみ</rt></ruby>へ<ruby>行<rt>い</rt></ruby>かなかった<ruby>理由<rt>りゆう</rt></ruby>は<ruby>何<rt>なん</rt></ruby>ですか。",
      "audio_file": "audio/listening/n4_q9.mp3",
      "choices": [
        "台風で大雨が降ったから。",
        "妹が高熱を出して看病しなければならなかったから。",
        "電車のチケットを買い忘れたから。",
        "友達とケンカをしたから。"
      ],
      "answer": 1,
      "explanation": {
        "ja": "天気は良かったが「前日の夜に妹が急に高熱を出してしまい、看病しなければならなかった」と述べています。選択肢2が正解です。",
        "en": "She could not go because her younger sister suddenly ran a high fever and needed her care. Choice 2 is correct.",
        "zh": "原因並非天氣不好，而是前晚妹妹突然發高燒需要她在家照顧，因此選項2正確。",
        "ko": "날씨는 좋았으나 여동생이 갑자기 고열이 나서 간호해야 했기 때문이므로 2번이 정답입니다."
      },
      "section": "問題2 ポイント理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】友達同士の男性と女性が話しています。女性が先週の休日に海へ行かなかった理由は何ですか。</p>\n      <p class=\"text-xs text-slate-700\">男の人と女の人が話しています。女の人が先週の休日に海へ行かなかった理由は何ですか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>林さん、先週の日曜日は友達と海へ行くって言ってたよね。泳いできた？</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>ううん、実は行けなくなっちゃったの。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>えっ、雨が降ったから？</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>ううん、お天気はすごく良くて海日和だったんだけど、前日の夜に妹が急に高熱を出してしまって。両親が仕事でいなかったから、私が看病しなきゃいけなくて。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>そうだったんだ。大変だったね。女の人が先週の休日に海へ行かなかった理由は何ですか。</p>\n    </div>"
    },
    {
      "q_num": 10,
      "section_id": "sec2",
      "section_name": "問題2 ポイント理解",
      "situation": "職場で男性社員と女性社員が話しています。女性が新しいパソコンを気に入っている一番の理由は何ですか。",
      "speech_audio_text": "会社で男の人と女の人が話しています。女の人が新しいパソコンを気に入っている一番の理由は何ですか。男：新しい会社のパソコン、使い心地はどう？画面が大きくて見やすそうだね。女：うん、画面も綺麗なんだけど、一番嬉しいのは本体がすごく軽くなったことなの！前のパソコンは重くて、出張や在宅勤務で持ち運ぶのが本当に苦痛だったの。今のは片手で持てるくらい軽くて肩こりが全然しなくなったわ。男：持ち運びが楽なのは一番のメリットだね。女の人が新しいパソコンを気に入っている一番の理由は何ですか。",
      "prompt": "<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>が<ruby>新<rt>あたら</rt></ruby>しいパソコンを<ruby>気<rt>き</rt></ruby>に<ruby>入<rt>い</rt></ruby>っている<ruby>一番<rt>いちばん</rt></ruby>の<ruby>理由<rt>りゆう</rt></ruby>は<ruby>何<rt>なん</rt></ruby>ですか。",
      "audio_file": "audio/listening/n4_q10.mp3",
      "choices": [
        "画面のサイズが大きくなったこと",
        "値段が前の機種より安かったこと",
        "キーボードの文字が光ること",
        "本体がとても軽くて持ち運びが楽になったこと"
      ],
      "answer": 3,
      "explanation": {
        "ja": "画面も綺麗だが「一番嬉しいのは本体がすごく軽くなったこと。持ち運ぶのが苦痛だったのが片手で持てるくらい軽くなった」と述べています。選択肢4が正解です。",
        "en": "Her favorite feature is how lightweight the laptop is, making commuting and carrying it effortless. Choice 4 is correct.",
        "zh": "最讓她滿意的是機身變得非常輕巧，大幅減輕了出差和通勤攜帶的負擔，因此選項4正確。",
        "ko": "화면보다도 본체가 매우 가벼워져서 출장이나 재택 시 들고 다니기 편해진 점이 가장 마음에 든다고 했으므로 4번이 정답입니다."
      },
      "section": "問題2 ポイント理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】職場で男性社員と女性社員が話しています。女性が新しいパソコンを気に入っている一番の理由は何ですか。</p>\n      <p class=\"text-xs text-slate-700\">会社で男の人と女の人が話しています。女の人が新しいパソコンを気に入っている一番の理由は何ですか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>新しい会社のパソコン、使い心地はどう？画面が大きくて見やすそうだね。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>うん、画面も綺麗なんだけど、一番嬉しいのは本体がすごく軽くなったことなの！前のパソコンは重くて、出張や在宅勤務で持ち運ぶのが本当に苦痛だったの。今のは片手で持てるくらい軽くて肩こりが全然しなくなったわ。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>持ち運びが楽なのは一番のメリットだね。女の人が新しいパソコンを気に入っている一番の理由は何ですか。</p>\n    </div>"
    },
    {
      "q_num": 11,
      "section_id": "sec2",
      "section_name": "問題2 ポイント理解",
      "situation": "夫婦が新しい掃除機について話しています。二人がこの掃除機を買った決め手は何ですか。",
      "speech_audio_text": "夫と妻が話しています。二人がこの掃除機を買った決め手は何ですか。男：新しいコードレス掃除機、早速届いたね。女：ええ。デザインもシンプルで部屋に馴染むわね。男：うん。他の店で見た機種は軽かったけど、音が大きくて夜に使えそうになかったよね。女：そうそう！これは音がすごく静かだから、夜遅くに帰ってきてちょっと掃除したい時でも近所を気にせず使えるのが一番の決め手だったわね。男：吸引力も十分だし、いい買い物をしたね。二人がこの掃除機を買った決め手は何ですか。",
      "prompt": "<ruby>二人<rt>ふたり</rt></ruby>がこの<ruby>掃除機<rt>そうじき</rt></ruby>を<ruby>買<rt>か</rt></ruby>った<ruby>決<rt>き</rt></ruby>め<ruby>手<rt>て</rt></ruby>は<ruby>何<rt>なん</rt></ruby>ですか。",
      "audio_file": "audio/listening/n4_q11.mp3",
      "choices": [
        "音がとても静かで夜でも気兼ねなく使えること",
        "セールで半額になっていたこと",
        "重くて絶対に倒れないこと",
        "ゴミを自動でゴミ箱へ運んでくれること"
      ],
      "answer": 0,
      "explanation": {
        "ja": "女性が「音がすごく静かだから、夜遅くに掃除したい時でも近所を気にせず使えるのが一番の決め手だった」と語っています。選択肢1が正解です。",
        "en": "The deciding factor was its whisper-quiet operation, allowing vacuuming at night without disturbing neighbors. Choice 1 is correct.",
        "zh": "最關鍵的購買因素是運轉聲音非常安靜，深夜打掃也不用擔心吵到鄰居，因此選項1正確。",
        "ko": "소음이 매우 조용해서 밤늦게 청소하더라도 이웃 눈치를 보지 않고 쓸 수 있다는 점이 결정적 이유였으므로 1번이 정답입니다."
      },
      "section": "問題2 ポイント理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】夫婦が新しい掃除機について話しています。二人がこの掃除機を買った決め手は何ですか。</p>\n      <p class=\"text-xs text-slate-700\">夫と妻が話しています。二人がこの掃除機を買った決め手は何ですか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>新しいコードレス掃除機、早速届いたね。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>ええ。デザインもシンプルで部屋に馴染むわね。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>うん。他の店で見た機種は軽かったけど、音が大きくて夜に使えそうになかったよね。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>そうそう！これは音がすごく静かだから、夜遅くに帰ってきてちょっと掃除したい時でも近所を気にせず使えるのが一番の決め手だったわね。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>吸引力も十分だし、いい買い物をしたね。二人がこの掃除機を買った決め手は何ですか。</p>\n    </div>"
    },
    {
      "q_num": 12,
      "section_id": "sec2",
      "section_name": "問題2 ポイント理解",
      "situation": "料理教室で先生が野菜スープの作り方を説明しています。スープを美味しく仕上げる一番のポイントは何ですか。",
      "speech_audio_text": "料理教室で先生が生徒たちに話しています。スープを美味しく仕上げる一番のポイントは何ですか。先生：今日は旬の野菜をたっぷり使ったミネストローネを作ります。玉ねぎや人参、セロリをオリーブオイルで炒めますが、ここが一番大切です。強火で一気に炒めると焦げてしまいますので、弱火でじっくり10分間炒めて野菜の甘みを引き出してください。野菜がしんなりしてからトマトとスープを加えて煮込むと、砂糖を入れなくてもとてもコクのある美味しいスープに仕上がりますよ。スープを美味しく仕上げる一番のポイントは何ですか。",
      "prompt": "スープを<ruby>美味<rt>おい</rt></ruby>しく<ruby>仕上<rt>しあ</rt></ruby>げる<ruby>一番<rt>いちばん</rt></ruby>のポイントは<ruby>何<rt>なん</rt></ruby>ですか。",
      "audio_file": "audio/listening/n4_q12.mp3",
      "choices": [
        "強火で1分間で野菜を炒めること",
        "砂糖をスプーン3杯入れること",
        "野菜を弱火でじっくり炒めて甘みを引き出すこと",
        "野菜を炒めずに生のまま水に入れて煮ること"
      ],
      "answer": 2,
      "explanation": {
        "ja": "先生は「弱火でじっくり10分間炒めて野菜の甘みを引き出すことが一番大切」と説明しています。選択肢3が正解です。",
        "en": "The key secret is slowly sautéing the vegetables over low heat to extract natural sweetness. Choice 3 is correct.",
        "zh": "老師強調最關鍵的秘訣是用小火耐心慢炒10分鐘將蔬菜的甜味充分引出，因此選項3正確。",
        "ko": "약불에서 은근히 10분간 볶아 채소 본연의 단맛을 이끌어내는 것이 가장 중요하다고 설명했으므로 3번이 정답입니다."
      },
      "section": "問題2 ポイント理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】料理教室で先生が野菜スープの作り方を説明しています。スープを美味しく仕上げる一番のポイントは何ですか。</p>\n      <p class=\"text-xs text-slate-700 leading-relaxed\">料理教室で先生が生徒たちに話しています。スープを美味しく仕上げる一番のポイントは何ですか。先生：今日は旬の野菜をたっぷり使ったミネストローネを作ります。玉ねぎや人参、セロリをオリーブオイルで炒めますが、ここが一番大切です。強火で一気に炒めると焦げてしまいますので、弱火でじっくり10分間炒めて野菜の甘みを引き出してください。野菜がしんなりしてからトマトとスープを加えて煮込むと、砂糖を入れなくてもとてもコクのある美味しいスープに仕上がりますよ。スープを美味しく仕上げる一番のポイントは何ですか。</p>\n    </div>"
    },
    {
      "q_num": 13,
      "section_id": "sec2",
      "section_name": "問題2 ポイント理解",
      "situation": "日本語学校で先生と留学生が話しています。レポートの提出締め切りが変更された理由は何ですか。",
      "speech_audio_text": "学校で先生と学生が話しています。レポートの提出締め切りが変更された理由は何ですか。男：先生、今週金曜日締切の日本文化のレポートですが、締め切りが来週の月曜日に延びたと聞きました。本当ですか？女：ええ、本当ですよ。今週の木曜日と金曜日に学校のパソコン室のシステム改修工事が入ることになって、学生の皆さんが学内でパソコンやプリンターを使えなくなってしまったんです。男：そうだったんですね！自宅にプリンターがないので助かりました。女：月曜日の授業の最初に提出してくださいね。レポートの提出締め切りが変更された理由は何ですか。",
      "prompt": "レポートの<ruby>提出<rt>ていしゅつ</rt></ruby><ruby>締<rt>し</rt></ruby>め<ruby>切<rt>き</rt></ruby>りが<ruby>変更<rt>へんこう</rt></ruby>された<ruby>理由<rt>りゆう</rt></ruby>は<ruby>何<rt>なん</rt></ruby>ですか。",
      "audio_file": "audio/listening/n4_q13.mp3",
      "choices": [
        "パソコン室のシステム改修で学内の機器が使えなくなったから",
        "先生が急に出張することになったから",
        "学生全員が宿題を忘れてきたから",
        "台風で学校が休校になったから"
      ],
      "answer": 0,
      "explanation": {
        "ja": "先生から「パソコン室のシステム改修工事が入って学内のパソコンやプリンターが使えなくなったため」と説明されています。選択肢1が正解です。",
        "en": "The deadline was extended because school computer lab renovations made printers unavailable. Choice 1 is correct.",
        "zh": "原因是學校電腦室進行系統改修工程，導致學生無法在校內使用電腦與印表機，因此選項1正確。",
        "ko": "컴퓨터실 개수 공사로 교내 컴퓨터와 프린터를 사용할 수 없게 되었기 때문이므로 1번이 정답입니다."
      },
      "section": "問題2 ポイント理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】日本語学校で先生と留学生が話しています。レポートの提出締め切りが変更された理由は何ですか。</p>\n      <p class=\"text-xs text-slate-700\">学校で先生と学生が話しています。レポートの提出締め切りが変更された理由は何ですか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>先生、今週金曜日締切の日本文化のレポートですが、締め切りが来週の月曜日に延びたと聞きました。本当ですか？</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>ええ、本当ですよ。今週の木曜日と金曜日に学校のパソコン室のシステム改修工事が入ることになって、学生の皆さんが学内でパソコンやプリンターを使えなくなってしまったんです。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>そうだったんですね！自宅にプリンターがないので助かりました。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>月曜日の授業の最初に提出してくださいね。レポートの提出締め切りが変更された理由は何ですか。</p>\n    </div>"
    },
    {
      "q_num": 14,
      "section_id": "sec2",
      "section_name": "問題2 ポイント理解",
      "situation": "図書館で男性利用者と司書が話しています。雑誌の最新号が貸出できない理由は何ですか。",
      "speech_audio_text": "図書館で男の人と司書が話しています。雑誌の最新号が貸出できない理由は何ですか。男：すみません、この料理雑誌の今月出た最新号を借りたいのですが、自動貸出機でエラーになってしまって。司書：あ、申し訳ございません。当館では、雑誌の最新号は館内閲覧のみとなっておりまして、貸出ができない規則になっております。男：そうなんですか。どうして最新号は借りられないんですか。司書：最新号は読みたい方が非常に多いため、多くの方に館内で公平にご覧いただくためなんです。来月号が発売されましたら、この号もお貸し出しできるようになりますよ。男：なるほど、わかりました。雑誌の最新号が貸出できない理由は何ですか。",
      "prompt": "<ruby>雑誌<rt>ざっし</rt></ruby>の<ruby>最新号<rt>さいしんごう</rt></ruby>が<ruby>貸出<rt>かしだし</rt></ruby>できない<ruby>理由<rt>りゆう</rt></ruby>は<ruby>何<rt>なん</rt></ruby>ですか。",
      "audio_file": "audio/listening/n4_q14.mp3",
      "choices": [
        "雑誌に汚れや破れがあるから",
        "多くの利用者が館内で公平に読めるようにするため",
        "本棚の修理工事を行っているから",
        "雑誌の値段が高すぎるから"
      ],
      "answer": 1,
      "explanation": {
        "ja": "司書が「最新号は読みたい方が多いため、多くの方に館内で公平にご覧いただくため」と理由を説明しています。選択肢2が正解です。",
        "en": "Latest magazine issues cannot be borrowed to ensure all visitors can read them fairly inside the library. Choice 2 is correct.",
        "zh": "館員解釋最新一期雜誌想看的人很多，為了讓多數讀者能公平在館內閱覽，因此選項2正確。",
        "ko": "최신호는 읽고 싶어 하는 이용자가 많아 관내에서 많은 사람이 공평하게 읽을 수 있도록 하기 위함이므로 2번이 정답입니다."
      },
      "section": "問題2 ポイント理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】図書館で男性利用者と司書が話しています。雑誌の最新号が貸出できない理由は何ですか。</p>\n      <p class=\"text-xs text-slate-700\">図書館で男の人と司書が話しています。雑誌の最新号が貸出できない理由は何ですか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>すみません、この料理雑誌の今月出た最新号を借りたいのですが、自動貸出機でエラーになってしまって。司書：あ、申し訳ございません。当館では、雑誌の最新号は館内閲覧のみとなっておりまして、貸出ができない規則になっております。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>そうなんですか。どうして最新号は借りられないんですか。司書：最新号は読みたい方が非常に多いため、多くの方に館内で公平にご覧いただくためなんです。来月号が発売されましたら、この号もお貸し出しできるようになりますよ。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>なるほど、わかりました。雑誌の最新号が貸出できない理由は何ですか。</p>\n    </div>"
    },
    {
      "q_num": 15,
      "section_id": "sec2",
      "section_name": "問題2 ポイント理解",
      "situation": "スポーツクラブでトレーナーと女性が話しています。トレーナーが運動前のストレッチを推奨する一番の目的は何ですか。",
      "speech_audio_text": "スポーツクラブでトレーナーと女性が話しています。トレーナーが運動前のストレッチを勧める一番の目的は何ですか。女：先生、走る前に軽くストレッチをした方がいいですか。男：はい、絶対にしてください。運動前に筋肉や関節をゆっくり伸ばして温めることで、筋肉の柔軟性が高まり、肉離れや捻挫などのケガを予防することができるんです。体をほぐさずにいきなり走ると、心臓にも負担がかかりますからね。女：わかりました。怪我をしないように、まずしっかりストレッチします！トレーナーが運動前のストレッチを勧める一番の目的は何ですか。",
      "prompt": "トレーナーが<ruby>運動<rt>うんどう</rt></ruby><ruby>前<rt>まえ</rt></ruby>のストレッチを<ruby>勧<rt>すす</rt></ruby>める<ruby>一番<rt>いちばん</rt></ruby>の<ruby>目的<rt>もくてき</rt></ruby>は<ruby>何<rt>なん</rt></ruby>ですか。",
      "audio_file": "audio/listening/n4_q15.mp3",
      "choices": [
        "ウェアの着心地を確かめるため",
        "足の長さを伸ばすため",
        "柔軟性を高めて肉離れなどのケガを予防するため",
        "眠気を誘ってリラックスするため"
      ],
      "answer": 2,
      "explanation": {
        "ja": "トレーナーは「筋肉や関節を温めて柔軟性を高め、肉離れや捻挫などのケガを予防することができる」と説明しています。選択肢3が正解です。",
        "en": "The primary purpose is warming up joints and muscles to increase flexibility and prevent injuries like sprains and strains. Choice 3 is correct.",
        "zh": "教練說明伸展主要目的是提高肌肉關節的柔軟度，有效預防肌肉拉傷與扭傷等運動傷害，因此選項3正確。",
        "ko": "트레이너는 유연성을 높여 근육 부상이나 염좌 등 부상을 예방하는 것이 가장 큰 목적이라고 설명했으므로 3번이 정답입니다."
      },
      "section": "問題2 ポイント理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】スポーツクラブでトレーナーと女性が話しています。トレーナーが運動前のストレッチを推奨する一番の目的は何ですか。</p>\n      <p class=\"text-xs text-slate-700\">スポーツクラブでトレーナーと女性が話しています。トレーナーが運動前のストレッチを勧める一番の目的は何ですか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>先生、走る前に軽くストレッチをした方がいいですか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>はい、絶対にしてください。運動前に筋肉や関節をゆっくり伸ばして温めることで、筋肉の柔軟性が高まり、肉離れや捻挫などのケガを予防することができるんです。体をほぐさずにいきなり走ると、心臓にも負担がかかりますからね。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>わかりました。怪我をしないように、まずしっかりストレッチします！トレーナーが運動前のストレッチを勧める一番の目的は何ですか。</p>\n    </div>"
    },
    {
      "q_num": 16,
      "section_id": "sec3",
      "section_name": "問題3 発話表現",
      "situation": "レストランで食事が終わりました。お会計をしたいとき、店員に何と言いますか。",
      "speech_audio_text": "レストランで食事が終わりました。お会計をしたいとき、店員に何と言いますか。1、お会計をお願いします。2、ごちそうを食べてください。3、お金を払わせてください。",
      "prompt": "お<ruby>会計<rt>かいけい</rt></ruby>をしたいとき、<ruby>店員<rt>てんいん</rt></ruby>に<ruby>何<rt>なん</rt></ruby>と<ruby>言<rt>い</rt></ruby>いますか。",
      "audio_file": "audio/listening/n4_q16.mp3",
      "choices": [
        "お会計をお願いします。",
        "ごちそうを食べてください。",
        "お金を払わせてください。"
      ],
      "answer": 0,
      "explanation": {
        "ja": "会計を頼む標準的な表現は「お会計をお願いします」です。選択肢1が正解です。",
        "en": "'お会計をお願いします' (The check, please) is standard. Choice 1 is correct.",
        "zh": "結帳時最自然標準的說法是「お会計をお願いします」（請幫我結帳），因此選項1正確。",
        "ko": "계산을 요청할 때 표준적인 표현은 'お会計をお願いします(계산 부탁드립니다)'이므로 1번이 정답입니다."
      },
      "section": "問題3 発話表現",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】レストランで食事が終わりました。お会計をしたいとき、店員に何と言いますか。</p>\n      <p class=\"text-xs text-slate-700\">レストランで食事が終わりました。お会計をしたいとき、店員に何と言いますか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">お会計をお願いします。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">ごちそうを食べてください。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">お金を払わせてください。</p>\n    </div>"
    },
    {
      "q_num": 17,
      "section_id": "sec3",
      "section_name": "問題3 発話表現",
      "situation": "電車でお年寄りが乗ってきました。席を譲りたいとき、何と言いますか。",
      "speech_audio_text": "電車でお年寄りが乗ってきました。席を譲りたいとき、何と言いますか。1、ここに座ってもいいですか。2、どうぞ、お座りください。3、座ってあげますよ。",
      "prompt": "<ruby>席<rt>せき</rt></ruby>を<ruby>譲<rt>ゆず</rt></ruby>りたいとき、<ruby>何<rt>なん</rt></ruby>と<ruby>言<rt>い</rt></ruby>いますか。",
      "audio_file": "audio/listening/n4_q17.mp3",
      "choices": [
        "ここに座ってもいいですか。",
        "どうぞ、お座りください。",
        "座ってあげますよ。"
      ],
      "answer": 1,
      "explanation": {
        "ja": "席を譲るときの丁寧な表現は「どうぞ、お座りください」です。選択肢2が正解です。",
        "en": "'どうぞ、お座りください' (Please, have a seat) is polite and appropriate. Choice 2 is correct.",
        "zh": "讓座時最禮貌的表達是「どうぞ、お座りください」（請坐），因此選項2正確。",
        "ko": "자리를 양보할 때 정중한 표현은 'どうぞ、お座りください(어서 앉으세요)'이므로 2번이 정답입니다."
      },
      "section": "問題3 発話表現",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】電車でお年寄りが乗ってきました。席を譲りたいとき、何と言いますか。</p>\n      <p class=\"text-xs text-slate-700\">電車でお年寄りが乗ってきました。席を譲りたいとき、何と言いますか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">ここに座ってもいいですか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">どうぞ、お座りください。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">座ってあげますよ。</p>\n    </div>"
    },
    {
      "q_num": 18,
      "section_id": "sec3",
      "section_name": "問題3 発話表現",
      "situation": "友達の家を訪ねて、部屋に上がるとき何と言いますか。",
      "speech_audio_text": "友達の家を訪ねて、部屋に上がるとき何と言いますか。1、お邪魔します。2、いってきます。3、おかえりなさい。",
      "prompt": "<ruby>部屋<rt>へや</rt></ruby>に<ruby>上<rt>あ</rt></ruby>がるとき、<ruby>何<rt>なん</rt></ruby>と<ruby>言<rt>い</rt></ruby>いますか。",
      "audio_file": "audio/listening/n4_q18.mp3",
      "choices": [
        "おかえりなさい。",
        "いってきます。",
        "お邪魔します。"
      ],
      "answer": 2,
      "explanation": {
        "ja": "他人の家を訪問して中に入るときの挨拶は「お邪魔します」です。選択肢3が正解です。",
        "en": "'お邪魔します' is the traditional greeting when entering someone's home. Choice 3 is correct.",
        "zh": "進入他人住家時的禮貌問候語為「お邪魔します」（打擾了），因此選項3正確。",
        "ko": "남의 집에 들어갈 때 하는 전통 인사말은 'お邪魔します(실례하겠습니다)'이므로 3번이 정답입니다."
      },
      "section": "問題3 発話表現",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】友達の家を訪ねて、部屋に上がるとき何と言いますか。</p>\n      <p class=\"text-xs text-slate-700\">友達の家を訪ねて、部屋に上がるとき何と言いますか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">お邪魔します。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">いってきます。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">おかえりなさい。</p>\n    </div>"
    },
    {
      "q_num": 19,
      "section_id": "sec3",
      "section_name": "問題3 発話表現",
      "situation": "同僚が忙しそうに資料をコピーしています。手伝いを申し出るとき何と言いますか。",
      "speech_audio_text": "同僚が忙しそうにコピーしています。手伝いを申し出るとき何と言いますか。1、何か手伝いましょうか。2、手伝ってもらえませんか。3、手伝うべきですよ。",
      "prompt": "<ruby>手伝<rt>てつだ</rt></ruby>いを<ruby>申<rt>もう</rt></ruby>し<ruby>出<rt>で</rt></ruby>るとき、<ruby>何<rt>なん</rt></ruby>と<ruby>言<rt>い</rt></ruby>いますか。",
      "audio_file": "audio/listening/n4_q19.mp3",
      "choices": [
        "手伝ってもらえませんか。",
        "何か手伝いましょうか。",
        "手伝うべきですよ。"
      ],
      "answer": 1,
      "explanation": {
        "ja": "自分が相手を手伝う申し出は「何か手伝いましょうか」です。選択肢2が正解です。",
        "en": "'何か手伝いましょうか' (Shall I help you with something?) is the standard offer. Choice 2 is correct.",
        "zh": "主動提出協助對方應說「何か手伝いましょうか」（需要我幫忙做點什麼嗎？），因此選項2正確。",
        "ko": "도움을 제안할 때 적절한 표현은 '何か手伝いましょうか(무엇 좀 도와드릴까요?)'이므로 2번이 정답입니다."
      },
      "section": "問題3 発話表現",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】同僚が忙しそうに資料をコピーしています。手伝いを申し出るとき何と言いますか。</p>\n      <p class=\"text-xs text-slate-700\">同僚が忙しそうにコピーしています。手伝いを申し出るとき何と言いますか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">何か手伝いましょうか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">手伝ってもらえませんか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">手伝うべきですよ。</p>\n    </div>"
    },
    {
      "q_num": 20,
      "section_id": "sec3",
      "section_name": "問題3 発話表現",
      "situation": "道で通行人に駅の場所を尋ねたいです。何と言いますか。",
      "speech_audio_text": "道で通行人に駅の場所を尋ねたいです。何と言いますか。1、すみません、駅はどこにありますか。2、駅を教えてくださいませんか。3、駅に行ってもいいですか。",
      "prompt": "<ruby>駅<rt>えき</rt></ruby>の<ruby>場所<rt>ばしょ</rt></ruby>を<ruby>尋<rt>たず</rt></ruby>ねたいです。<ruby>何<rt>なん</rt></ruby>と<ruby>言<rt>い</rt></ruby>いますか。",
      "audio_file": "audio/listening/n4_q20.mp3",
      "choices": [
        "すみません、駅はどこにありますか。",
        "駅を教えてくださいませんか。",
        "駅に行ってもいいですか。"
      ],
      "answer": 0,
      "explanation": {
        "ja": "道を尋ねる最も自然な表現は「すみません、駅はどこにありますか」です。選択肢1が正解です。",
        "en": "'すみません、駅はどこにありますか' (Excuse me, where is the station?) is natural. Choice 1 is correct.",
        "zh": "詢問車站位置最自然的說法是「すみません、駅はどこにありますか」（不好意思，請問車站設在哪裡？），因此選項1正確。",
        "ko": "길을 물을 때 가장 자연스러운 표현은 'すみません、駅はどこにありますか'이므로 1번이 정답입니다."
      },
      "section": "問題3 発話表現",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】道で通行人に駅の場所を尋ねたいです。何と言いますか。</p>\n      <p class=\"text-xs text-slate-700\">道で通行人に駅の場所を尋ねたいです。何と言いますか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">すみません、駅はどこにありますか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">駅を教えてくださいませんか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">駅に行ってもいいですか。</p>\n    </div>"
    },
    {
      "q_num": 21,
      "section_id": "sec4",
      "section_name": "問題4 即時応答",
      "situation": "「週末、一緒に京都へ紅葉を見に行きませんか。」",
      "speech_audio_text": "週末、一緒に京都へ紅葉を見に行きませんか。 1、京都へは行きません。 2、紅葉は見ませんでしたよ。 3、いいですね！ぜひ行きましょう。",
      "prompt": "「週末、一緒に京都へ紅葉を見に行きませんか。」",
      "audio_file": "audio/listening/n4_q21.mp3",
      "choices": [
        "京都へは行きません。",
        "紅葉は見ませんでしたよ。",
        "いいですね！ぜひ行きましょう。"
      ],
      "answer": 2,
      "explanation": {
        "ja": "「週末、一緒に京都へ紅葉を見に行きませんか」という誘いに対し、「いいですね！ぜひ行きましょう（選択肢3）」と快く賛同するのが自然です。",
        "en": "Accepting an invitation to view autumn foliage in Kyoto with \"Sounds great! Let's go!\" (Choice 3).",
        "zh": "面對週末一起去京都看紅葉的邀約，欣然同意的選項3「太好了！一定要去」最為自然。",
        "ko": "주말에 교토로 단풍을 보러 가자는 권유에 흔쾌히 찬성하는 3번이 자연스럽습니다."
      },
      "section": "問題4 即時応答",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】「週末、一緒に京都へ紅葉を見に行きませんか。」</p>\n      <p class=\"text-xs text-slate-700\">週末、一緒に京都へ紅葉を見に行きませんか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">京都へは行きません。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">紅葉は見ませんでしたよ。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">いいですね！ぜひ行きましょう。</p>\n    </div>"
    },
    {
      "q_num": 22,
      "section_id": "sec4",
      "section_name": "問題4 即時応答",
      "situation": "「ちょっとペンを貸していただけませんか。」",
      "speech_audio_text": "ちょっとペンを貸していただけませんか。 1、ペンはありませんでした。 2、ペンを借りました。 3、ええ、どうぞ使ってください。",
      "prompt": "「ちょっとペンを貸していただけませんか。」",
      "audio_file": "audio/listening/n4_q22.mp3",
      "choices": [
        "ペンはありませんでした。",
        "ペンを借りました。",
        "ええ、どうぞ使ってください。"
      ],
      "answer": 2,
      "explanation": {
        "ja": "「ペンを貸していただけませんか」という丁寧な依頼に対し、「ええ、どうぞ使ってください（選択肢3）」と貸し出すのが自然です。",
        "en": "Lending a pen politely with \"Yes, please go ahead and use it\" (Choice 3).",
        "zh": "面對禮貌借筆的請求，答應並借給對方的選項3「好的，請用」最自然合適。",
        "ko": "펜을 빌려달라는 요청에 흔쾌히 빌려주는 3번이 정답입니다."
      },
      "section": "問題4 即時応答",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】「ちょっとペンを貸していただけませんか。」</p>\n      <p class=\"text-xs text-slate-700\">ちょっとペンを貸していただけませんか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">ペンはありませんでした。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">ペンを借りました。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">ええ、どうぞ使ってください。</p>\n    </div>"
    },
    {
      "q_num": 23,
      "section_id": "sec4",
      "section_name": "問題4 即時応答",
      "situation": "「今日はずいぶん寒くなりましたね。」",
      "speech_audio_text": "今日はずいぶん寒くなりましたね。 1、本当に、コートを着てきて正解でした。 2、はい、とても暖かくなりました。 3、寒いのは昨日でした。",
      "prompt": "「今日はずいぶん寒くなりましたね。」",
      "audio_file": "audio/listening/n4_q23.mp3",
      "choices": [
        "本当に、コートを着てきて正解でした。",
        "はい、とても暖かくなりました。",
        "寒いのは昨日でした。"
      ],
      "answer": 0,
      "explanation": {
        "ja": "寒さに対する共感を求められた際、「本当に、コートを着てきて正解でした（選択肢1）」と実感をもって応じるのが適切です。選択肢2は「寒くなった」に対し「暖かくなった」と答えていて矛盾します。",
        "en": "Agreeing that it got quite cold today by saying wearing a coat was the right choice (Choice 1).",
        "zh": "面對「今天變得很冷呢」的共鳴，回應「真的，穿大衣來穿對了（選項1）」最為自然。",
        "ko": "오늘 꽤 추워졌다는 말에 코트를 입고 오길 잘했다며 공감하는 1번이 정답입니다."
      },
      "section": "問題4 即時応答",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】「今日はずいぶん寒くなりましたね。」</p>\n      <p class=\"text-xs text-slate-700\">今日はずいぶん寒くなりましたね。</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">本当に、コートを着てきて正解でした。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">はい、とても暖かくなりました。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">寒いのは昨日でした。</p>\n    </div>"
    },
    {
      "q_num": 24,
      "section_id": "sec4",
      "section_name": "問題4 即時応答",
      "situation": "「明日のテスト、頑張ってくださいね！」",
      "speech_audio_text": "明日のテスト、頑張ってくださいね！ 1、頑張らなくてもいいですよ。 2、ありがとうございます、全力で頑張ります！ 3、テストは難しくありませんでした。",
      "prompt": "「明日のテスト、頑張ってくださいね！」",
      "audio_file": "audio/listening/n4_q24.mp3",
      "choices": [
        "頑張らなくてもいいですよ。",
        "ありがとうございます、全力で頑張ります！",
        "テストは難しくありませんでした。"
      ],
      "answer": 1,
      "explanation": {
        "ja": "応援の言葉「頑張ってくださいね」に対し、「ありがとうございます、全力で頑張ります！（選択肢2）」と感謝と意気込みを返すのが正解です。選択肢3は明日なのに過去形になっています。",
        "en": "Responding to encouragement with gratitude and determination (Choice 2).",
        "zh": "面對考試前的加油鼓勵，表達感謝並表示會全力以赴的選項2「謝謝您，我會全力加油的！」最合適。",
        "ko": "내일 시험 힘내라는 응원에 감사하며 전력을 다하겠다고 답하는 2번이 정답입니다."
      },
      "section": "問題4 即時応答",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】「明日のテスト、頑張ってくださいね！」</p>\n      <p class=\"text-xs text-slate-700\">明日のテスト、頑張ってくださいね！</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">頑張らなくてもいいですよ。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">ありがとうございます、全力で頑張ります！</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">テストは難しくありませんでした。</p>\n    </div>"
    },
    {
      "q_num": 25,
      "section_id": "sec4",
      "section_name": "問題4 即時応答",
      "situation": "「お茶のおかわりはいかがですか。」",
      "speech_audio_text": "お茶のおかわりはいかがですか。 1、ありがとうございます、もう一杯いただきます。 2、いいえ、もう十分いただきました。ごちそうさまです。 3、はい、お茶をどうぞ。",
      "prompt": "「お茶のおかわりはいかがですか。」",
      "audio_file": "audio/listening/n4_q25.mp3",
      "choices": [
        "ありがとうございます、もう一杯いただきます。",
        "いいえ、もう十分いただきました。ごちそうさまです。",
        "はい、お茶をどうぞ。"
      ],
      "answer": 0,
      "explanation": {
        "ja": "お茶のおかわりを勧められた際、喜んでいただく「ありがとうございます、もう一杯いただきます（選択肢1）」が適切です。選択肢3は勧められている側が相手にお茶を勧めており主客逆転しています。",
        "en": "Politely accepting another cup of tea with \"Thank you, I will have another cup\" (Choice 1).",
        "zh": "被詢問要不要續杯茶時，禮貌接受的選項1「謝謝您，那我再來一杯」最為自然。",
        "ko": "차를 더 마시겠냐는 권유에 감사하며 한 잔 더 받겠다는 1번이 자연스럽습니다."
      },
      "section": "問題4 即時応答",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】「お茶のおかわりはいかがですか。」</p>\n      <p class=\"text-xs text-slate-700\">お茶のおかわりはいかがですか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">ありがとうございます、もう一杯いただきます。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">いいえ、もう十分いただきました。ごちそうさまです。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">はい、お茶をどうぞ。</p>\n    </div>"
    },
    {
      "q_num": 26,
      "section_id": "sec4",
      "section_name": "問題4 即時応答",
      "situation": "「課長、企画書のチェックをお願いしてもよろしいでしょうか。」",
      "speech_audio_text": "課長、企画書のチェックをお願いしてもよろしいでしょうか。 1、うん、デスクに置いておいて。後で見ておくよ。 2、はい、私がチェックをお願いします。 3、ええ、企画書はまだ提出していません。",
      "prompt": "「課長、企画書のチェックをお願いしてもよろしいでしょうか。」",
      "audio_file": "audio/listening/n4_q26.mp3",
      "choices": [
        "うん、デスクに置いておいて。後で見ておくよ。",
        "はい、私がチェックをお願いします。",
        "ええ、企画書はまだ提出していません。"
      ],
      "answer": 0,
      "explanation": {
        "ja": "部下からのチェック依頼に対し、上司が「うん、デスクに置いておいて。後で見ておくよ（選択肢1）」と指示するのが自然です。選択肢2は上司が部下に依頼する形になっており誤りです。",
        "en": "The manager accepts the proposal draft and asks to leave it on the desk (Choice 1).",
        "zh": "面對部下請求檢查企劃書，主管回答「嗯，先放在桌上，我等下看（選項1）」最自然。",
        "ko": "기획서 확인 요청에 책상에 두면 나중에 보겠다고 답하는 1번이 자연스럽습니다."
      },
      "section": "問題4 即時応答",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】「課長、企画書のチェックをお願いしてもよろしいでしょうか。」</p>\n      <p class=\"text-xs text-slate-700\">課長、企画書のチェックをお願いしてもよろしいでしょうか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">うん、デスクに置いておいて。後で見ておくよ。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">はい、私がチェックをお願いします。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">ええ、企画書はまだ提出していません。</p>\n    </div>"
    },
    {
      "q_num": 27,
      "section_id": "sec4",
      "section_name": "問題4 即時応答",
      "situation": "「雨が降ってきましたね。傘を持っていますか。」",
      "speech_audio_text": "雨が降ってきましたね。傘を持っていますか。 1、ええ、雨は降っていませんよ。 2、はい、折りたたみ傘を持っているので大丈夫です。 3、いいえ、傘を差して帰りました。",
      "prompt": "「雨が降ってきましたね。傘を持っていますか。」",
      "audio_file": "audio/listening/n4_q27.mp3",
      "choices": [
        "ええ、雨は降っていませんよ。",
        "はい、折りたたみ傘を持っているので大丈夫です。",
        "いいえ、傘を差して帰りました。"
      ],
      "answer": 1,
      "explanation": {
        "ja": "雨が降ってきた際の傘の確認に対し、「はい、折りたたみ傘を持っているので大丈夫です（選択肢2）」と答えるのが自然です。選択肢1は降っている事実を否定しており不自然です。",
        "en": "Replying that one has a folding umbrella so it is fine (Choice 2).",
        "zh": "面對下雨天有沒有帶傘的關心，回答「有，我帶了折疊傘所以沒問題（選項2）」最為合情合理。",
        "ko": "비가 오는데 우산이 있냐는 질문에 접이식 우산이 있어 괜찮다고 답하는 2번이 자연스럽습니다."
      },
      "section": "問題4 即時応答",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】「雨が降ってきましたね。傘を持っていますか。」</p>\n      <p class=\"text-xs text-slate-700\">雨が降ってきましたね。傘を持っていますか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">ええ、雨は降っていませんよ。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">はい、折りたたみ傘を持っているので大丈夫です。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">いいえ、傘を差して帰りました。</p>\n    </div>"
    },
    {
      "q_num": 28,
      "section_id": "sec4",
      "section_name": "問題4 即時応答",
      "situation": "「お仕事、遅くまでお疲れ様でした。」",
      "speech_audio_text": "お仕事、遅くまでお疲れ様でした。 1、どういたしまして、仕事は楽しかったです。 2、はい、おはようございます。 3、お疲れ様でした！お先に失礼します。",
      "prompt": "「お仕事、遅くまでお疲れ様でした。」",
      "audio_file": "audio/listening/n4_q28.mp3",
      "choices": [
        "どういたしまして、仕事は楽しかったです。",
        "はい、おはようございます。",
        "お疲れ様でした！お先に失礼します。"
      ],
      "answer": 2,
      "explanation": {
        "ja": "退勤時の「お疲れ様でした」という労いに対し、お互いに労い合って退出する「お疲れ様でした！お先に失礼します（選択肢3）」が職場の最も基本的な挨拶です。",
        "en": "Returning the greeting and excusing oneself when leaving work (Choice 3).",
        "zh": "下班時面對對方的慰勞「工作到這麼晚辛苦了」，回答「您也辛苦了！我先告辭了（選項3）」是最標準的職場禮儀。",
        "ko": "퇴근 인사로 서로 수고했다고 격려하며 먼저 퇴근하겠다는 3번이 정답입니다."
      },
      "section": "問題4 即時応答",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】「お仕事、遅くまでお疲れ様でした。」</p>\n      <p class=\"text-xs text-slate-700\">お仕事、遅くまでお疲れ様でした。</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">どういたしまして、仕事は楽しかったです。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">はい、おはようございます。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">お疲れ様でした！お先に失礼します。</p>\n    </div>"
    }
  ]
};
