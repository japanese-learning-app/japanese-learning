window.JLPT_N3_LISTENING_DATA = {
  "test_id": "jlpt_n3_listening_test_01",
  "title": "JLPT N3 聴解実戦模試 第1回",
  "level": "N3",
  "total_questions": 28,
  "sections": [
    {
      "section_id": "sec1",
      "title": "問題1 課題理解",
      "count": 6,
      "desc": "質問を聞いて、次に何をすべきかを正確に聞き取る問題です。"
    },
    {
      "section_id": "sec2",
      "title": "問題2 ポイント理解",
      "count": 6,
      "desc": "質問を聞いた後、選択肢を読む時間があります。ポイントを聞き取ります。"
    },
    {
      "section_id": "sec3",
      "title": "問題3 概要理解",
      "count": 3,
      "desc": "全体の話の流れや話し手の主張・言いたいことを聞き取ります。"
    },
    {
      "section_id": "sec4",
      "title": "問題4 発話表現",
      "count": 4,
      "desc": "状況に合わせてどのような表現を使うべきかを選ぶ問題です（3択）。"
    },
    {
      "section_id": "sec5",
      "title": "問題5 即時応答",
      "count": 9,
      "desc": "短い問いかけに対して、最も自然な返答を瞬時に選ぶ問題です（3択）。"
    }
  ],
  "questions": [
    {
      "q_num": 1,
      "section_id": "sec1",
      "section_name": "問題1 課題理解",
      "situation": "会社で女性と男性が明日の会議の準備について話しています。男性はこのあと、まず何をしますか。",
      "speech_audio_text": "会社で女性と男性が明日の会議の準備について話しています。男の人はこのあと、まず何をしますか。女：田中さん、明日の企画会議の資料、印刷は終わった？男：はい、人数分の20部、もうコピーしてあります。女：ありがとう。あ、プロジェクターの動作確認はしてくれた？男：あ、まだです。すぐに会議室に行って電源が入るか試してきます。女：お願いね。あ、その前に、参加者の名簿に一部変更があったから、パソコンの最新データを印刷し直して差し替えてもらえる？男：わかりました。じゃあ、まず名簿を直して差し替えてから、会議室へ向かいます。女：よろしくね。男の人はこのあと、まず何をしますか。",
      "prompt": "男の人はこの<ruby>後<rt>あと</rt></ruby>、まず<ruby>何<rt>なに</rt></ruby>をしますか。",
      "audio_file": "audio/listening/n3_q1.mp3",
      "choices": [
        "名簿の最新データを印刷して差し替える。",
        "会議室を予約する。",
        "プロジェクターの動作確認をする。",
        "企画会議の資料を20部コピーする。"
      ],
      "answer": 0,
      "explanation": {
        "ja": "男性はプロジェクターの確認に行こうとしますが、女性から「その前に、名簿に一部変更があったから差し替えて」と頼まれ、「まず名簿を直して差し替えてから会議室に向かいます」と答えています。したがって、まず行うのは選択肢1です。",
        "en": "The man offers to check the projector, but the woman asks him to update and replace the attendee roster first. The man agrees to replace the roster before going to the meeting room, so Choice 1 is correct.",
        "zh": "男性本想先去確認投影機，但女性請他先替換有變更的最新名單，男性回答「先改好名單替換後再去會議室」，因此最先做的是選項1。",
        "ko": "남성은 프로젝터 확인을 하려 하지만, 여성이 그 전에 변경된 명단을 교체해 달라고 부탁하고, 남성이 '먼저 명단을 고쳐 교체한 후 회의실로 가겠다'고 했으므로 1번이 정답입니다."
      },
      "section": "問題1 課題理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】会社で女性と男性が明日の会議の準備について話しています。男性はこのあと、まず何をしますか。</p>\n      <p class=\"text-xs text-slate-700\">会社で女性と男性が明日の会議の準備について話しています。男の人はこのあと、まず何をしますか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>田中さん、明日の企画会議の資料、印刷は終わった？</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>はい、人数分の20部、もうコピーしてあります。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>ありがとう。あ、プロジェクターの動作確認はしてくれた？</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>あ、まだです。すぐに会議室に行って電源が入るか試してきます。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>お願いね。あ、その前に、参加者の名簿に一部変更があったから、パソコンの最新データを印刷し直して差し替えてもらえる？</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>わかりました。じゃあ、まず名簿を直して差し替えてから、会議室へ向かいます。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>よろしくね。男の人はこのあと、まず何をしますか。</p>\n    </div>"
    },
    {
      "q_num": 2,
      "section_id": "sec1",
      "section_name": "問題1 課題理解",
      "situation": "旅行会社で男性客と店員が話しています。男性客はこのあと、何を記入しますか。",
      "speech_audio_text": "旅行会社で男の人と店員が話しています。男の人はこのあと、何を記入しますか。店員：いらっしゃいませ。京都旅行のツアーをご検討ですね。男：はい。この3日間のフリープランに申し込みたいんですが。店員：ありがとうございます。こちらのプランですね。お申し込みにあたりまして、まずこちらの申込用紙にお名前とご連絡先、ご希望の出発日をご記入いただけますか。男：わかりました。アンケートの欄も書いたほうがいいですか。店員：アンケートは任意ですので、お帰りの際にお時間があればで結構ですよ。男：わかりました。じゃあ、ここを書きますね。男の人はこのあと、何を記入しますか。",
      "prompt": "男の人はこの<ruby>後<rt>あと</rt></ruby>、<ruby>何<rt>なに</rt></ruby>を<ruby>記入<rt>きにゅう</rt></ruby>しますか。",
      "audio_file": "audio/listening/n3_q2.mp3",
      "choices": [
        "アンケート用紙のすべての項目",
        "申込用紙の名前・連絡先・出発日",
        "ホテルの宿泊名簿",
        "新幹線の座席希望票"
      ],
      "answer": 1,
      "explanation": {
        "ja": "店員が「まずこちらの申込用紙にお名前とご連絡先、ご希望の出発日をご記入いただけますか」と案内し、アンケートについては「任意でお帰りの際で結構」と言っているため、男性が今記入するのは選択肢2です。",
        "en": "The clerk instructs the man to fill in his name, contact info, and desired departure date on the application form, noting the survey is optional. Choice 2 is correct.",
        "zh": "店員引導男性先在申請表上填寫姓名、聯絡方式和出發日期，並表示問卷可等離開時再填，因此現在填寫的是選項2。",
        "ko": "직원이 먼저 신청서에 이름, 연락처, 희망 출발일을 작성해 달라고 안내했으며 설문은 나중에 해도 된다고 했으므로 2번이 정답입니다."
      },
      "section": "問題1 課題理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】旅行会社で男性客と店員が話しています。男性客はこのあと、何を記入しますか。</p>\n      <p class=\"text-xs text-slate-700\">旅行会社で男の人と店員が話しています。男の人はこのあと、何を記入しますか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">店員：</span>いらっしゃいませ。京都旅行のツアーをご検討ですね。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>はい。この3日間のフリープランに申し込みたいんですが。</p>\n<p><span class=\"font-bold text-[#1995AD]\">店員：</span>ありがとうございます。こちらのプランですね。お申し込みにあたりまして、まずこちらの申込用紙にお名前とご連絡先、ご希望の出発日をご記入いただけますか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>わかりました。アンケートの欄も書いたほうがいいですか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">店員：</span>アンケートは任意ですので、お帰りの際にお時間があればで結構ですよ。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>わかりました。じゃあ、ここを書きますね。男の人はこのあと、何を記入しますか。</p>\n    </div>"
    },
    {
      "q_num": 3,
      "section_id": "sec1",
      "section_name": "問題1 課題理解",
      "situation": "料理教室で先生が生徒たちに話しています。生徒たちは明日、何を持ってこなければなりませんか。",
      "speech_audio_text": "料理教室で先生が生徒たちに話しています。生徒たちは明日、何を持ってこなければなりませんか。先生：みなさん、今日はお疲れ様でした。明日は本格的な和食を作ります。エプロンと三角巾、筆記用具は今日と同じように各自持ってきてください。包丁やまな板などの調理器具はこちらで用意してあります。あ、それから、明日は作った料理を持ち帰るための密閉タッパーを必ず持参してください。大きさは中くらいのものが2つあるといいですね。生徒たちは明日、何を持ってこなければなりませんか。",
      "prompt": "<ruby>生徒<rt>せいと</rt></ruby>たちは<ruby>明日<rt>あす</rt></ruby>、<ruby>何<rt>なに</rt></ruby>を<ruby>持<rt>も</rt></ruby>ってこなければなりませんか。",
      "audio_file": "audio/listening/n3_q3.mp3",
      "choices": [
        "包丁とまな板",
        "和食の調味料と食材",
        "エプロン、三角巾、筆記用具、料理を持ち帰るタッパー",
        "三角巾と大きなフライパン"
      ],
      "answer": 2,
      "explanation": {
        "ja": "先生は「エプロンと三角巾、筆記用具は今日と同じように各自持参」「調理器具はこちらで用意」「料理を持ち帰る密閉タッパーを必ず持参」と指示しているため、持参が必要なのは選択肢3です。",
        "en": "The instructor states that students must bring aprons, bandanas, stationery, and food containers to take their cooking home, while cooking utensils are provided. Choice 3 is correct.",
        "zh": "老師要求大家自備圍裙、三角巾、文具以及帶菜回家用的密封保鮮盒，烹飪用具則由教室提供，因此選項3正確。",
        "ko": "선생님이 앞치마, 삼각건, 필기도구 및 만든 요리를 담아갈 밀폐용기를 가져오라고 안내하고 조리도구는 준비되어 있다고 했으므로 3번이 정답입니다."
      },
      "section": "問題1 課題理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】料理教室で先生が生徒たちに話しています。生徒たちは明日、何を持ってこなければなりませんか。</p>\n      <p class=\"text-xs text-slate-700\">料理教室で先生が生徒たちに話しています。生徒たちは明日、何を持ってこなければなりませんか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">先生：</span>みなさん、今日はお疲れ様でした。明日は本格的な和食を作ります。エプロンと三角巾、筆記用具は今日と同じように各自持ってきてください。包丁やまな板などの調理器具はこちらで用意してあります。あ、それから、明日は作った料理を持ち帰るための密閉タッパーを必ず持参してください。大きさは中くらいのものが2つあるといいですね。生徒たちは明日、何を持ってこなければなりませんか。</p>\n    </div>"
    },
    {
      "q_num": 4,
      "section_id": "sec1",
      "section_name": "問題1 課題理解",
      "situation": "大学で留学生と職員が話しています。留学生はこのあと、まずどこへ行きますか。",
      "speech_audio_text": "大学で留学生の男の人と事務室の職員が話しています。留学生はこのあと、まずどこへ行きますか。男：すみません、在学証明書を発行してほしいのですが。職員：在学証明書ですね。あちらの自動発行機で学生証を通せばすぐに印刷できますよ。男：あ、そうなんですか。でも、今日財布を忘れてしまって、発行手数料の200円が手元にないんです。電子マネーは使えますか。職員：自動機は現金のみなんです。でも、2階の学生支援課に行けば、スマートフォンのコード決済で支払い手続きができますよ。男：助かりました！じゃあ2階に行ってきます。留学生はこのあと、まずどこへ行きますか。",
      "prompt": "<ruby>留学生<rt>りゅうがくせい</rt></ruby>はこの<ruby>後<rt>あと</rt></ruby>、まずどこへ<ruby>行<rt>い</rt></ruby>きますか。",
      "audio_file": "audio/listening/n3_q4.mp3",
      "choices": [
        "1階の自動発行機",
        "学内のATM",
        "自宅（財布を取りに戻る）",
        "2階の学生支援課"
      ],
      "answer": 3,
      "explanation": {
        "ja": "留学生は手元に現金がないため、職員から「2階の学生支援課に行けばスマートフォンのコード決済で支払いができる」と案内され、「じゃあ2階に行ってきます」と言っています。したがって、選択肢4が正解です。",
        "en": "Because the student has no cash, the staff advises him to go to Student Support on the 2nd floor where mobile QR payment is accepted. Choice 4 is correct.",
        "zh": "留學生因沒帶現金，職員告訴他可去2樓的學生支援課使用手機二維碼支付，留學生回答「那我先去2樓」，因此選項4正確。",
        "ko": "유학생이 현금이 없자 직원이 2층 학생지원과에 가면 스마트폰 결제가 가능하다고 안내했고, 유학생이 2층으로 가겠다고 했으므로 4번이 정답입니다."
      },
      "section": "問題1 課題理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】大学で留学生と職員が話しています。留学生はこのあと、まずどこへ行きますか。</p>\n      <p class=\"text-xs text-slate-700\">大学で留学生の男の人と事務室の職員が話しています。留学生はこのあと、まずどこへ行きますか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>すみません、在学証明書を発行してほしいのですが。職員：在学証明書ですね。あちらの自動発行機で学生証を通せばすぐに印刷できますよ。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>あ、そうなんですか。でも、今日財布を忘れてしまって、発行手数料の200円が手元にないんです。電子マネーは使えますか。職員：自動機は現金のみなんです。でも、2階の学生支援課に行けば、スマートフォンのコード決済で支払い手続きができますよ。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>助かりました！じゃあ2階に行ってきます。留学生はこのあと、まずどこへ行きますか。</p>\n    </div>"
    },
    {
      "q_num": 5,
      "section_id": "sec1",
      "section_name": "問題1 課題理解",
      "situation": "アパートで女性と大家さんが話しています。女性はこのあと、どうしますか。",
      "speech_audio_text": "アパートで女性と大家の男性が話しています。女の人はこのあと、どうしますか。女：大家さん、お風呂の換気扇から変な音がするんです。昨日の夜から急にカラカラと音が鳴り始めて。男：そうですか。ちょっと見せてもらえますか。……ああ、モーターの部品が古くなっているようですね。交換が必要です。女：修理代はどうなりますか。男：通常の劣化ですから、費用はこちらで負担しますよ。ただ、業者を手配するので、明日の午後は在宅されていますか。女：明日の午後は家にいます。男：では、明日の午後2時に業者に来てもらうよう連絡しておきますね。女の人はこのあと、どうしますか。",
      "prompt": "<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>はこの<ruby>後<rt>あと</rt></ruby>、どうしますか。",
      "audio_file": "audio/listening/n3_q5.mp3",
      "choices": [
        "自分で換気扇の部品を買いに行く。",
        "修理業者に電話して日程を調整する。",
        "明日の午後2時に自宅で修理業者を待つ。",
        "修理代の費用を銀行で振り込む。"
      ],
      "answer": 2,
      "explanation": {
        "ja": "大家さんが修理費用を負担し、業者の手配も大家さんが「午後2時に来るよう連絡しておく」と約束したため、女性は明日午後2時に自宅で業者を待つことになります。選択肢3が正解です。",
        "en": "The landlord covers the repair costs and contacts the technician, so the woman just needs to wait at home tomorrow at 2:00 PM for the repair. Choice 3 is correct.",
        "zh": "房東負責承擔費用並聯絡維修師傅明天下午2點上門，女性只需明天下午在家等待師傅即可，因此選項3正確。",
        "ko": "집주인이 수리비를 부담하고 내일 오후 2시에 업자가 오도록 연락하겠다고 했으므로 여성은 내일 오후 2시에 집에서 수리 업자를 기다리게 됩니다. 3번이 정답입니다."
      },
      "section": "問題1 課題理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】アパートで女性と大家さんが話しています。女性はこのあと、どうしますか。</p>\n      <p class=\"text-xs text-slate-700\">アパートで女性と大家の男性が話しています。女の人はこのあと、どうしますか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>大家さん、お風呂の換気扇から変な音がするんです。昨日の夜から急にカラカラと音が鳴り始めて。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>そうですか。ちょっと見せてもらえますか。……ああ、モーターの部品が古くなっているようですね。交換が必要です。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>修理代はどうなりますか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>通常の劣化ですから、費用はこちらで負担しますよ。ただ、業者を手配するので、明日の午後は在宅されていますか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>明日の午後は家にいます。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>では、明日の午後2時に業者に来てもらうよう連絡しておきますね。女の人はこのあと、どうしますか。</p>\n    </div>"
    },
    {
      "q_num": 6,
      "section_id": "sec1",
      "section_name": "問題1 課題理解",
      "situation": "職場で課長と女性社員が話しています。女性社員はこのあと、まず何をしますか。",
      "speech_audio_text": "職場で課長と女性社員が話しています。女の人はこのあと、まず何をしますか。課長：佐藤さん、来月の新入社員研修の会場についてなんだけど。佐藤：はい、本社の大ホールを予約してありますが。課長：それがね、来月急に役員会議が入ってしまって、大ホールが使えなくなったんだ。佐藤：えっ、そうなんですか。課長：申し訳ないけど、近隣の貸し会議室で30名入れるところを至急探してくれるかい？空き状況が確認できたら仮予約を入れてほしい。費用の見積もりはそのあとに提出してもらえばいいから。佐藤：かしこまりました。すぐに近隣の施設を調べて空きを確認します。女の人はこのあと、まず何をしますか。",
      "prompt": "<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>はこの<ruby>後<rt>あと</rt></ruby>、まず<ruby>何<rt>なに</rt></ruby>をしますか。",
      "audio_file": "audio/listening/n3_q6.mp3",
      "choices": [
        "役員会議の日程を変更する。",
        "近隣の貸し会議室の空き状況を調べて仮予約する。",
        "新入社員研修の費用見積書を作成する。",
        "本社の大ホールの机と椅子を片付ける。"
      ],
      "answer": 1,
      "explanation": {
        "ja": "課長から「近隣の貸し会議室で30名入れるところを至急探して空き状況を確認し、仮予約を入れてほしい」と指示され、女性は「すぐに近隣の施設を調べて空きを確認します」と答えています。選択肢2が正解です。",
        "en": "The manager asks her to urgently search nearby rental rooms for 30 people and make a tentative reservation. Choice 2 is correct.",
        "zh": "主管指示她緊急尋找附近可容納30人的外租會議室確認空位並進行預約，女性回答立即去查，因此選項2正確。",
        "ko": "과장이 인근 대여 회의실 중 30명이 들어갈 수 있는 곳을 긴급히 찾아 공실 확인 및 가예약을 해달라고 지시했고 여성이 즉시 확인하겠다고 했으므로 2번이 정답입니다."
      },
      "section": "問題1 課題理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】職場で課長と女性社員が話しています。女性社員はこのあと、まず何をしますか。</p>\n      <p class=\"text-xs text-slate-700 leading-relaxed\">職場で課長と女性社員が話しています。女の人はこのあと、まず何をしますか。課長：佐藤さん、来月の新入社員研修の会場についてなんだけど。佐藤：はい、本社の大ホールを予約してありますが。課長：それがね、来月急に役員会議が入ってしまって、大ホールが使えなくなったんだ。佐藤：えっ、そうなんですか。課長：申し訳ないけど、近隣の貸し会議室で30名入れるところを至急探してくれるかい？空き状況が確認できたら仮予約を入れてほしい。費用の見積もりはその後に提出してもらえばいいから。佐藤：かしこまりました。すぐに近隣の施設を調べて空きを確認します。女の人はこのあと、まず何をしますか。</p>\n    </div>"
    },
    {
      "q_num": 7,
      "section_id": "sec2",
      "section_name": "問題2 ポイント理解",
      "situation": "女性と男性が毎日の運動について話しています。男性が毎朝走るのをやめた理由は何ですか。",
      "speech_audio_text": "女の人と男の人が話しています。男の人が毎朝走るのをやめた理由は何ですか。女：木村さん、最近ジョギングはどうですか？続いていますか？男：実はね、先月でやめちゃったんだ。女：えっ、あんなに熱心だったのに、膝でも痛めたんですか？男：いや、体は全然平気なんだけどね。朝走ると午前中すっきりするんだけど、午後になると急激に眠くなって仕事に集中できなくなっちゃって。女：あー、朝にエネルギーを使いすぎちゃったんですね。男：そうなんだよ。だから今は仕事終わりの夜に軽くウォーキングするだけに変えたんだ。そしたら夜もぐっすり眠れるようになってね。男の人が毎朝走るのをやめた理由は何ですか。",
      "prompt": "<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>が<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>走<rt>はし</rt></ruby>るのをやめた<ruby>理由<rt>りゆう</rt></ruby>は<ruby>何<rt>なん</rt></ruby>ですか。",
      "audio_file": "audio/listening/n3_q7.mp3",
      "choices": [
        "走っているときに膝を痛めてしまったから。",
        "夜のウォーキングの方が痩せると聞いたから。",
        "朝起きるのが辛くて続けられなくなったから。",
        "朝走ると午後に強い眠気が出て仕事に影響したから。"
      ],
      "answer": 3,
      "explanation": {
        "ja": "男性は「朝走ると午前中はすっきりするが、午後になると急激に眠くなって仕事に集中できなくなった」と理由を説明しています。したがって、選択肢4が正解です。",
        "en": "The man explains that running in the morning made him excessively sleepy in the afternoon, disrupting his focus at work. Choice 4 is correct.",
        "zh": "男性解釋早晨跑步雖然上午神清氣爽，但下午會非常想睡導致無法專注於工作，因此選項4正確。",
        "ko": "남성은 아침에 달리면 오전에는 상쾌하지만 오후에 너무 졸려서 일에 집중할 수 없게 되었기 때문이라고 설명했으므로 4번이 정답입니다."
      },
      "section": "問題2 ポイント理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】女性と男性が毎日の運動について話しています。男性が毎朝走るのをやめた理由は何ですか。</p>\n      <p class=\"text-xs text-slate-700\">女の人と男の人が話しています。男の人が毎朝走るのをやめた理由は何ですか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>木村さん、最近ジョギングはどうですか？続いていますか？</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>実はね、先月でやめちゃったんだ。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>えっ、あんなに熱心だったのに、膝でも痛めたんですか？</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>いや、体は全然平気なんだけどね。朝走ると午前中すっきりするんだけど、午後になると急激に眠くなって仕事に集中できなくなっちゃって。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>あー、朝にエネルギーを使いすぎちゃったんですね。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>そうなんだよ。だから今は仕事終わりの夜に軽くウォーキングするだけに変えたんだ。そしたら夜もぐっすり眠れるようになってね。男の人が毎朝走るのをやめた理由は何ですか。</p>\n    </div>"
    },
    {
      "q_num": 8,
      "section_id": "sec2",
      "section_name": "問題2 ポイント理解",
      "situation": "洋菓子店で店長と店員が話しています。新しく発売したプリンが人気を集めている一番の理由は何ですか。",
      "speech_audio_text": "洋菓子店で店長と店員が話しています。新しく発売したプリンが人気を集めている一番の理由は何ですか。店長：新作のほうじ茶プリン、連日完売しているそうだね。何がそんなにお客さんに受けているのかな？店員：パッケージのデザインも可愛いと好評なんですが、一番はお茶の香りと甘さ控えめな味付けですね。最近は健康志向のお客様が多くて、甘すぎるデザートを敬遠される方が多いんです。うちのは地元の高級茶葉の香りを生かして後味がすっきりしているので、大人の方に特に喜ばれています。店長：なるほど、素材の良さと上品な甘さが受けたんだね。新しく発売したプリンが人気を集めている一番の理由は何ですか。",
      "prompt": "<ruby>新<rt>あたら</rt></ruby>しく<ruby>発売<rt>はつばい</rt></ruby>したプリンが<ruby>人気<rt>にんき</rt></ruby>を<ruby>集<rt>あつ</rt></ruby>めている<ruby>一番<rt>いちばん</rt></ruby>の<ruby>理由<rt>りゆう</rt></ruby>は<ruby>何<rt>なん</rt></ruby>ですか。",
      "audio_file": "audio/listening/n3_q8.mp3",
      "choices": [
        "甘さ控えめで高級茶葉の香りを生かしたすっきりした味だから。",
        "テレビ番組で有名人に紹介されたから。",
        "他店よりも値段が圧倒的に安いから。",
        "賞味期限が長くてお土産に便利だから。"
      ],
      "answer": 0,
      "explanation": {
        "ja": "店員は「一番はお茶の香りと甘さ控えめな味付け」「地元の高級茶葉の香りを生かして後味がすっきりしている点」と述べています。選択肢1が正解です。",
        "en": "The clerk states that the main appeal is the moderately sweet taste highlighting the aroma of local premium tea with a refreshing aftertaste. Choice 1 is correct.",
        "zh": "店員說明最主要的原因是甜度適中，突顯當地高級茶葉的香氣且回味清爽，深受注重健康的顧客喜愛，因此選項1正確。",
        "ko": "점원이 가장 큰 이유는 차의 향과 적당한 단맛, 현지 고급 찻잎의 향을 살린 깔끔한 뒷맛이라고 설명했으므로 1번이 정답입니다."
      },
      "section": "問題2 ポイント理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】洋菓子店で店長と店員が話しています。新しく発売したプリンが人気を集めている一番の理由は何ですか。</p>\n      <p class=\"text-xs text-slate-700\">洋菓子店で店長と店員が話しています。新しく発売したプリンが人気を集めている一番の理由は何ですか。店長：新作のほうじ茶プリン、連日完売しているそうだね。何がそんなにお客さんに受けているのかな？</p>\n<p><span class=\"font-bold text-[#1995AD]\">店員：</span>パッケージのデザインも可愛いと好評なんですが、一番はお茶の香りと甘さ控えめな味付けですね。最近は健康志向のお客様が多くて、甘すぎるデザートを敬遠される方が多いんです。うちのは地元の高級茶葉の香りを生かして後味がすっきりしているので、大人の方に特に喜ばれています。店長：なるほど、素材の良さと上品な甘さが受けたんだね。新しく発売したプリンが人気を集めている一番の理由は何ですか。</p>\n    </div>"
    },
    {
      "q_num": 9,
      "section_id": "sec2",
      "section_name": "問題2 ポイント理解",
      "situation": "会社で男性と女性が話しています。女性が今の会社へ転職を決めた決め手は何ですか。",
      "speech_audio_text": "会社で男の人と女の人が話しています。女の人が今の会社へ転職を決めた決め手は何ですか。男：林さんは前の会社でも同じウェブデザイナーをしていたんだよね。どうして今の会社に移ったの？給料が大幅に上がったとか？女：ううん、お給料は前の会社とほとんど変わらないよ。前も職場の人間関係は良かったし。男：へえ、じゃあ何が決め手だったの？女：一番は、完全リモートワークとフレックスタイム制が導入されているところかな。通勤に往復2時間かかっていたのがなくなって、自分の勉強や趣味の時間に充てられるようになったのが本当に大きいよ。男：なるほど、柔軟な働き方に惹かれたんだね。女の人が今の会社へ転職を決めた決め手は何ですか。",
      "prompt": "<ruby>女<rt>おんな</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>が<ruby>今<rt>いま</rt></ruby>の<ruby>会社<rt>かいしゃ</rt></ruby>へ<ruby>転職<rt>てんしょく</rt></ruby>を<ruby>決<rt>き</rt></ruby>めた<ruby>決<rt>き</rt></ruby>め<ruby>手<rt>て</rt></ruby>は<ruby>何<rt>なん</rt></ruby>ですか。",
      "audio_file": "audio/listening/n3_q9.mp3",
      "choices": [
        "給料が前の会社より大幅に高かったから。",
        "完全リモートワークなど柔軟な働き方ができるから。",
        "前の会社で人間関係のトラブルがあったから。",
        "海外勤務のチャンスがあるから。"
      ],
      "answer": 1,
      "explanation": {
        "ja": "給料や人間関係ではなく、「完全リモートワークとフレックスタイム制が導入されているところ。通勤の往復2時間がなくなったのが一番大きい」と語っています。選択肢2が正解です。",
        "en": "She specifies that fully remote work and flextime allowing her to save a 2-hour daily commute was the deciding factor. Choice 2 is correct.",
        "zh": "女性說明薪資和人際關係並非主因，最關鍵的是全遠程工作和彈性工時制度，省去了每天2小時的通勤時間，因此選項2正確。",
        "ko": "급여나 인간관계가 아니라 '완전 재택근무와 플렉스타임제가 도입되어 왕복 2시간의 통근 시간이 없어진 점'이 결정적이었다고 말했으므로 2번이 정답입니다."
      },
      "section": "問題2 ポイント理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】会社で男性と女性が話しています。女性が今の会社へ転職を決めた決め手は何ですか。</p>\n      <p class=\"text-xs text-slate-700\">会社で男の人と女の人が話しています。女の人が今の会社へ転職を決めた決め手は何ですか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>林さんは前の会社でも同じウェブデザイナーをしていたんだよね。どうして今の会社に移ったの？給料が大幅に上がったとか？</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>ううん、お給料は前の会社とほとんど変わらないよ。前も職場の人間関係は良かったし。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>へえ、じゃあ何が決め手だったの？</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>一番は、完全リモートワークとフレックスタイム制が導入されているところかな。通勤に往復2時間かかっていたのがなくなって、自分の勉強や趣味の時間に充てられるようになったのが本当に大きいよ。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>なるほど、柔軟な働き方に惹かれたんだね。女の人が今の会社へ転職を決めた決め手は何ですか。</p>\n    </div>"
    },
    {
      "q_num": 10,
      "section_id": "sec2",
      "section_name": "問題2 ポイント理解",
      "situation": "女性と男性が休日の過ごし方について話しています。男性が家庭菜園を始めたきっかけは何ですか。",
      "speech_audio_text": "女の人と男の人が話しています。男の人が家庭菜園を始めたきっかけは何ですか。女：高橋さん、ベランダでトマトやハーブを育てているそうですね。男：そうなんですよ。毎朝水をあげるのが楽しみで。女：元々植物を育てるのが好きだったんですか？男：いや、全然。料理もたまにするくらいで。実はこの前の休日に近所の農園で野菜の収穫体験イベントに参加したんです。そこで採れたてのトマトを食べたら、あまりの美味しさに感動してしまって。自分でも育ててみたいと思ったのがきっかけなんです。女：自分で育てた採れたては格別でしょうね。男の人が家庭菜園を始めたきっかけは何ですか。",
      "prompt": "<ruby>男<rt>おとこ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>が<ruby>家庭<rt>かてい</rt></ruby><ruby>菜園<rt>さいえん</rt></ruby>を<ruby>始<rt>はじ</rt></ruby>めたきっかけは<ruby>何<rt>なん</rt></ruby>ですか。",
      "audio_file": "audio/listening/n3_q10.mp3",
      "choices": [
        "食費を節約するため。",
        "ベランダの日当たりを活かして部屋を涼しくしたかったから。",
        "友人からトマトの苗をプレゼントされたから。",
        "収穫体験で食べた採れたてトマトの美味しさに感動したから。"
      ],
      "answer": 3,
      "explanation": {
        "ja": "男性は「近所の農園で野菜収穫体験に参加し、そこで採れたてのトマトを食べたら美味しさに感動して自分でも育ててみたいと思った」ときっかけを述べています。選択肢4が正解です。",
        "en": "The man explains he was inspired to start gardening after tasting delicious freshly harvested tomatoes at a local farm picking event. Choice 4 is correct.",
        "zh": "男性說自己參加附近農園的採摘體驗活動時，被現摘番茄的美味深深感動，從而想要自己種植，因此選項4正確。",
        "ko": "남성은 근처 농원에서 채소 수확 체험에 참여했을 때 갓 수확한 토마토의 맛에 감동하여 직접 길러보고 싶어졌다고 계기를 밝혔으므로 4번이 정답입니다."
      },
      "section": "問題2 ポイント理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】女性と男性が休日の過ごし方について話しています。男性が家庭菜園を始めたきっかけは何ですか。</p>\n      <p class=\"text-xs text-slate-700\">女の人と男の人が話しています。男の人が家庭菜園を始めたきっかけは何ですか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>高橋さん、ベランダでトマトやハーブを育てているそうですね。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>そうなんですよ。毎朝水をあげるのが楽しみで。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>元々植物を育てるのが好きだったんですか？</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>いや、全然。料理もたまにするくらいで。実はこの前の休日に近所の農園で野菜の収穫体験イベントに参加したんです。そこで採れたてのトマトを食べたら、あまりの美味しさに感動してしまって。自分でも育ててみたいと思ったのがきっかけなんです。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>自分で育てた採れたては格別でしょうね。男の人が家庭菜園を始めたきっかけは何ですか。</p>\n    </div>"
    },
    {
      "q_num": 11,
      "section_id": "sec2",
      "section_name": "問題2 ポイント理解",
      "situation": "大学で先輩と後輩がゼミの発表について話しています。先輩は後輩のスライドのどこを直すべきだと言っていますか。",
      "speech_audio_text": "大学で先輩の女性と後輩の男性が話しています。先輩は後輩のスライドのどこを直すべきだと言っていますか。男：先輩、明日のゼミ発表のスライドを作ったので見ていただけますか。女：うん、いいよ。……全体の構成や分析データはすごく説得力があるね。男：本当ですか！よかったです。女：ただね、1枚のスライドに文字を詰め込みすぎているかな。フォントが小さくて後ろの席からだと読みにくいと思うよ。グラフやキーワードだけを残して、詳しい説明は口頭で話すようにした方が聞き手に伝わりやすいよ。男：なるほど、文字を減らして要点だけに絞るんですね。直します！先輩は後輩のスライドのどこを直すべきだと言っていますか。",
      "prompt": "<ruby>先輩<rt>せんぱい</rt></ruby>は<ruby>後輩<rt>こうはい</rt></ruby>のスライドのどこを<ruby>直<rt>なお</rt></ruby>すべきだと<ruby>言<rt>い</rt></ruby>っていますか。",
      "audio_file": "audio/listening/n3_q11.mp3",
      "choices": [
        "文字の詰め込みすぎをやめ、要点とグラフ中心にすること",
        "発表の構成全体を最初からやり直すこと",
        "分析データの計算ミスを直すこと",
        "スライドの背景の色を派手にすること"
      ],
      "answer": 0,
      "explanation": {
        "ja": "先輩は「1枚のスライドに文字を詰め込みすぎてフォントが小さい」「文字を減らしてグラフやキーワードを残し、詳しい説明は口頭でするように」と指摘しています。選択肢1が正解です。",
        "en": "The senior advises reducing text overload, enlarging fonts, and focusing on graphs and keywords while elaborating verbally. Choice 1 is correct.",
        "zh": "學姐指出每張簡報文字塞得太滿導致字體過小，建議精簡文字，僅保留圖表和關鍵詞，詳細內容用口頭說明，因此選項1正確。",
        "ko": "선배는 슬라이드 1장에 글씨가 너무 빽빽해서 폰트가 작아 보이지 않는다며 글자를 줄이고 그래프와 핵심어 위주로 정리하라고 조언했으므로 1번이 정답입니다."
      },
      "section": "問題2 ポイント理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】大学で先輩と後輩がゼミの発表について話しています。先輩は後輩のスライドのどこを直すべきだと言っていますか。</p>\n      <p class=\"text-xs text-slate-700\">大学で先輩の女性と後輩の男性が話しています。先輩は後輩のスライドのどこを直すべきだと言っていますか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>先輩、明日のゼミ発表のスライドを作ったので見ていただけますか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>うん、いいよ。……全体の構成や分析データはすごく説得力があるね。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>本当ですか！よかったです。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>ただね、1枚のスライドに文字を詰め込みすぎているかな。フォントが小さくて後ろの席からだと読みにくいと思うよ。グラフやキーワードだけを残して、詳しい説明は口頭で話すようにした方が聞き手に伝わりやすいよ。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>なるほど、文字を減らして要点だけに絞るんですね。直します！先輩は後輩のスライドのどこを直すべきだと言っていますか。</p>\n    </div>"
    },
    {
      "q_num": 12,
      "section_id": "sec2",
      "section_name": "問題2 ポイント理解",
      "situation": "家具屋で夫婦がダイニングテーブルを見ています。二人がこのテーブルを買うことに決めた理由は何ですか。",
      "speech_audio_text": "家具屋で夫と妻が話しています。二人がこのテーブルを買うことに決めた理由は何ですか。女：この木製のテーブル、部屋のフローリングの色と合いそうね。男：そうだね。でも、ちょっとサイズが大きくないかな？リビングが狭くなっちゃうかも。女：あ、見て。これ、普段は2人用のコンパクトな大きさだけど、来客のときは天板を広げて4人用や6人用に伸ばせる伸縮式なんだって！男：へえ、本当だ！普段はすっきり置けて、友達を呼んだときだけ広げられるのは便利だね。デザインもシンプルだし、これにしようか。女：うん、そうしましょ！二人がこのテーブルを買うことに決めた理由は何ですか。",
      "prompt": "<ruby>二人<rt>ふたり</rt></ruby>がこのテーブルを<ruby>買<rt>か</rt></ruby>うことに<ruby>決<rt>き</rt></ruby>めた<ruby>理由<rt>りゆう</rt></ruby>は<ruby>何<rt>なん</rt></ruby>ですか。",
      "audio_file": "audio/listening/n3_q12.mp3",
      "choices": [
        "展示品処分セールで値段が半額になっていたから。",
        "重くて絶対に動かない頑丈な作りだったから。",
        "普段はコンパクトで、来客時に天板を広げられる伸縮式だから。",
        "最初から6人用の固定された特大サイズだったから。"
      ],
      "answer": 2,
      "explanation": {
        "ja": "普段は2人用のコンパクトなサイズで、友達が来た時だけ天板を広げられる伸縮式の機能性が決め手となったため、選択肢3が正解です。",
        "en": "They decided on the table because it is expandable: compact for everyday use, yet easily extended for guests. Choice 3 is correct.",
        "zh": "兩人決定購買的原因是這張桌子是可伸縮式，平時兩人用非常小巧，有客人時可展開變大，兼具實用性，因此選項3正確。",
        "ko": "평소에는 2인용으로 컴팩트하게 쓰다가 손님이 왔을 때만 상판을 넓혀 쓸 수 있는 확장형 기능이 마음에 들었기 때문이므로 3번이 정답입니다."
      },
      "section": "問題2 ポイント理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】家具屋で夫婦がダイニングテーブルを見ています。二人がこのテーブルを買うことに決めた理由は何ですか。</p>\n      <p class=\"text-xs text-slate-700\">家具屋で夫と妻が話しています。二人がこのテーブルを買うことに決めた理由は何ですか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>この木製のテーブル、部屋のフローリングの色と合いそうね。</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>そうだね。でも、ちょっとサイズが大きくないかな？リビングが狭くなっちゃうかも。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>あ、見て。これ、普段は2人用のコンパクトな大きさだけど、来客のときは天板を広げて4人用や6人用に伸ばせる伸縮式なんだって！</p>\n<p><span class=\"font-bold text-[#1995AD]\">男：</span>へえ、本当だ！普段はすっきり置けて、友達を呼んだときだけ広げられるのは便利だね。デザインもシンプルだし、これにしようか。</p>\n<p><span class=\"font-bold text-[#1995AD]\">女：</span>うん、そうしましょ！二人がこのテーブルを買うことに決めた理由は何ですか。</p>\n    </div>"
    },
    {
      "q_num": 13,
      "section_id": "sec3",
      "section_name": "問題3 概要理解",
      "situation": "ラジオで専門家が話しています。",
      "speech_audio_text": "ラジオで専門家が話しています。最近、電子マネーやクレジットカードによるキャッシュレス決済が急速に普及しています。財布を持たずにスマートフォン一つで買い物ができる便利さは大きな魅力です。しかしその一方で、現金を直接手渡す感覚がないため、自分がいくら使ったのか実感が湧きにくく、気付かないうちに使いすぎてしまうというトラブルも増えています。利用明細をアプリで定期的に確認したり、月に使える上限額を設定したりするなど、便利さに流されず自己管理を行う工夫がこれまで以上に大切になっています。専門家は何について話していますか。",
      "prompt": "<ruby>専門家<rt>せんもんか</rt></ruby>は<ruby>何<rt>なに</rt></ruby>について<ruby>話<rt>はな</rt></ruby>していますか。",
      "audio_file": "audio/listening/n3_q13.mp3",
      "choices": [
        "キャッシュレス決済の便利さと、使いすぎを防ぐ自己管理の大切さ",
        "スマートフォンの最新機種の選び方",
        "クレジットカードのポイントを効率よく貯める方法",
        "現金による買い物が最も安全である理由"
      ],
      "answer": 0,
      "explanation": {
        "ja": "専門家はキャッシュレス決済の利便性に触れつつ、お金を使った実感が薄れて使いすぎてしまう問題点を指摘し、上限設定など自己管理が重要であると語っています。選択肢1が正解です。",
        "en": "The speaker addresses the convenience of cashless payments while emphasizing the danger of overspending and the importance of budgeting and self-control. Choice 1 is correct.",
        "zh": "專家在肯定無現金支付便利性的同時，指出容易缺乏花錢實感而過度消費的問題，強調定期查看明細及設定上限等自我管理的重要性，因此選項1正確。",
        "ko": "전문가는 간편결제의 편리함을 언급하면서도 과소비 위험을 지적하고 이용 한도 설정 등 자기관리의 중요성을 강조하고 있으므로 1번이 정답입니다."
      },
      "section": "問題3 概要理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】ラジオで専門家が話しています。</p>\n      <p class=\"text-xs text-slate-700 leading-relaxed\">ラジオで専門家が話しています。最近、電子マネーやクレジットカードによるキャッシュレス決済が急速に普及しています。財布を持たずにスマートフォン一つで買い物ができる便利さは大きな魅力です。しかしその一方で、現金を直接手渡す感覚がないため、自分がいくら使ったのか実感が湧きにくく、気付かないうちに使いすぎてしまうというトラブルも増えています。利用明細をアプリで定期的に確認したり、月に使える上限額を設定したりするなど、便利さに流されず自己管理を行う工夫がこれまで以上に大切になっています。専門家は何について話していますか。</p>\n    </div>"
    },
    {
      "q_num": 14,
      "section_id": "sec3",
      "section_name": "問題3 概要理解",
      "situation": "テレビでアナウンサーが話しています。",
      "speech_audio_text": "テレビでアナウンサーが話しています。全国の多くの地域で、空き家の増加が社会的な課題となっています。しかし最近、この空き家を改修しておしゃれなカフェやシェアオフィス、旅行者のためのゲストハウスとして再生させる取り組みが注目を集めています。古い日本家屋の温かみを残した空間は若者や観光客に新鮮に受け入れられており、地域の活気を取り戻すきっかけにもなっています。放置すれば危険な空き家も、アイデア次第で町の新しい魅力へと生まれ変わるのです。アナウンサーは何について伝えていますか。",
      "prompt": "アナウンサーは<ruby>何<rt>なに</rt></ruby>について<ruby>伝<rt>つた</rt></ruby>えていますか。",
      "audio_file": "audio/listening/n3_q14.mp3",
      "choices": [
        "古い日本家屋をすべて取り壊して新しいビルを建てる計画",
        "空き家をカフェやオフィスとして再生し、地域の魅力にする取り組み",
        "空き家が増える原因とその撤去費用について",
        "若者が都会から離れたがらない理由"
      ],
      "answer": 1,
      "explanation": {
        "ja": "社会問題となっている空き家を改修してカフェやゲストハウスに再生し、町の新しい魅力や地域活性化につなげている事例を伝えています。選択肢2が正解です。",
        "en": "The announcer highlights projects that renovate vacant houses into cafes and guesthouses, revitalizing the local community. Choice 2 is correct.",
        "zh": "主播介紹了將閒置空屋改造成咖啡館、共享辦公室或民宿，從而為地方注入新活力的再生舉措，因此選項2正確。",
        "ko": "아나운서는 사회적 문제가 된 빈집을 개조하여 카페나 게스트하우스 등으로 재생시켜 지역 활성화로 이어지게 하는 시도에 대해 전하고 있으므로 2번이 정답입니다."
      },
      "section": "問題3 概要理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】テレビでアナウンサーが話しています。</p>\n      <p class=\"text-xs text-slate-700 leading-relaxed\">テレビでアナウンサーが話しています。全国の多くの地域で、空き家の増加が社会的な課題となっています。しかし最近、この空き家を改修しておしゃれなカフェやシェアオフィス、旅行者のためのゲストハウスとして再生させる取り組みが注目を集めています。古い日本家屋の温かみを残した空間は若者や観光客に新鮮に受け入れられており、地域の活気を取り戻すきっかけにもなっています。放置すれば危険な空き家も、アイデア次第で町の新しい魅力へと生まれ変わるのです。アナウンサーは何について伝えていますか。</p>\n    </div>"
    },
    {
      "q_num": 15,
      "section_id": "sec3",
      "section_name": "問題3 概要理解",
      "situation": "講演会である作家が話しています。",
      "speech_audio_text": "講演会である作家が話しています。本を読むとき、最後まで一気に速く読もうとする人が多いですが、私は少し立ち止まりながら読むことをおすすめしています。心に響いた一文があればページをめくる手を止め、なぜその言葉が自分に刺さったのか、自分の経験と重ね合わせて考えてみるのです。速くたくさん読むことよりも、一冊の本と深く対話することの方が、読書から得られる心の栄養はずっと豊かなものになります。作家が一番伝えたいことは何ですか。",
      "prompt": "<ruby>作家<rt>さっか</rt></ruby>が<ruby>一番<rt>いちばん</rt></ruby><ruby>伝<rt>つた</rt></ruby>えたいことは<ruby>何<rt>なん</rt></ruby>ですか。",
      "audio_file": "audio/listening/n3_q15.mp3",
      "choices": [
        "1日に1冊以上の本を速読する読書技術",
        "小説よりもビジネス書や実用書を読むべきだということ",
        "読書は速く読むことより、立ち止まって深く対話しながら読むことが大切だということ",
        "本を読むときはメモを取らずに記憶すること"
      ],
      "answer": 2,
      "explanation": {
        "ja": "作家は、速くたくさん読むことよりも、心に響いた言葉で立ち止まり、自分の経験と対話しながら深く読むことの大切さを説いています。選択肢3が正解です。",
        "en": "The author emphasizes that rather than rushing to read quickly, it is far more enriching to pause and engage deeply with resonant passages. Choice 3 is correct.",
        "zh": "作家強調與其追求快速大量閱讀，不如在觸動心靈的字句前停下腳步、結合自身經驗深度體會，因此選項3正確。",
        "ko": "작가는 빨리 많이 읽는 것보다 마음에 와닿은 문장에서 멈추어 자신의 경험과 대화하듯 깊이 있게 읽는 것이 중요하다고 설명하고 있으므로 3번이 정답입니다."
      },
      "section": "問題3 概要理解",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】講演会である作家が話しています。</p>\n      <p class=\"text-xs text-slate-700 leading-relaxed\">講演会である作家が話しています。本を読むとき、最後まで一気に速く読もうとする人が多いですが、私は少し立ち止まりながら読むことをおすすめしています。心に響いた一文があればページをめくる手を止め、なぜその言葉が自分に刺さったのか、自分の経験と重ね合わせて考えてみるのです。速くたくさん読むことよりも、一冊の本と深く対話することの方が、読書から得られる心の栄養はずっと豊かなものになります。作家が一番伝えたいことは何ですか。</p>\n    </div>"
    },
    {
      "q_num": 16,
      "section_id": "sec4",
      "section_name": "問題4 発話表現",
      "situation": "同僚が重そうなダンボール箱を運んでいます。手伝いたいとき、何と言いますか。",
      "speech_audio_text": "同僚が重そうなダンボール箱を運んでいます。手伝いたいとき、何と言いますか。1、持ってもらえませんか。2、一つお持ちしましょうか。3、運んであげてください。",
      "prompt": "<ruby>同僚<rt>どうりょう</rt></ruby>が<ruby>重<rt>おも</rt></ruby>そうな箱を運んでいます。<ruby>手伝<rt>てつだ</rt></ruby>いたいとき、<ruby>何<rt>なん</rt></ruby>と<ruby>言<rt>い</rt></ruby>いますか。",
      "audio_file": "audio/listening/n3_q16.mp3",
      "choices": [
        "一つお持ちしましょうか。",
        "持ってもらえませんか。",
        "運んであげてください。"
      ],
      "answer": 0,
      "explanation": {
        "ja": "自分が相手を手伝う申し出の敬語表現として「（私がお荷物を）一つお持ちしましょうか」が最も適切です。1は自分が頼む表現、3は第三者に指示する表現です。",
        "en": "'一つお持ちしましょうか' (Shall I carry one for you?) is the standard polite offer to help. Choice 1 is correct.",
        "zh": "主動提出幫對方分擔行李的禮貌表現為「一つお持ちしましょうか」（我來幫您拿一個吧？），因此選項1正確。",
        "ko": "자신이 도와주겠다고 공손히 제안할 때는 '一つお持ちしましょうか(하나 들어 드릴까요?)'가 가장 적절하므로 1번이 정답입니다."
      },
      "section": "問題4 発話表現",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】同僚が重そうなダンボール箱を運んでいます。手伝いたいとき、何と言いますか。</p>\n      <p class=\"text-xs text-slate-700\">同僚が重そうなダンボール箱を運んでいます。手伝いたいとき、何と言いますか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">持ってもらえませんか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">一つお持ちしましょうか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">運んであげてください。</p>\n    </div>"
    },
    {
      "q_num": 17,
      "section_id": "sec4",
      "section_name": "問題4 発話表現",
      "situation": "会議中、先輩のペンを借りたいです。何と言いますか。",
      "speech_audio_text": "会議中、先輩のペンを借りたいです。何と言いますか。1、ペンを使わせてくださいませんか。2、ペンを貸してあげますよ。3、ペンを使ってよろしいです。",
      "prompt": "<ruby>会議中<rt>かいぎちゅう</rt></ruby>、<ruby>先輩<rt>せんぱい</rt></ruby>のペンを<ruby>借<rt>か</rt></ruby>りたいです。<ruby>何<rt>なん</rt></ruby>と<ruby>言<rt>い</rt></ruby>いますか。",
      "audio_file": "audio/listening/n3_q17.mp3",
      "choices": [
        "ペンを貸してあげますよ。",
        "ペンを使わせてくださいませんか。",
        "ペンを使ってよろしいです。"
      ],
      "answer": 1,
      "explanation": {
        "ja": "相手の物を借りる許可を丁寧に求める表現は「〜させてくださいませんか」です。「使わせてくださいませんか」が正解です。",
        "en": "'使わせてくださいませんか' (Would you please allow me to use your pen?) is the polite request for permission. Choice 2 is correct.",
        "zh": "向長輩前輩禮貌請求借用物品時，應使用「使わせてくださいませんか」（能否讓我用一下您的筆？），因此選項2正確。",
        "ko": "상대방의 물건을 빌려 쓰고자 정중히 허가를 구할 때는 '使わせてくださいませんか(제가 쓰게 해주시지 않겠습니까?)'가 맞으므로 2번이 정답입니다."
      },
      "section": "問題4 発話表現",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】会議中、先輩のペンを借りたいです。何と言いますか。</p>\n      <p class=\"text-xs text-slate-700\">会議中、先輩のペンを借りたいです。何と言いますか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">ペンを使わせてくださいませんか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">ペンを貸してあげますよ。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">ペンを使ってよろしいです。</p>\n    </div>"
    },
    {
      "q_num": 18,
      "section_id": "sec4",
      "section_name": "問題4 発話表現",
      "situation": "エレベーターに乗ろうとしたら、ドアが閉まりそうになりました。乗せてほしいとき、何と言いますか。",
      "speech_audio_text": "エレベーターに乗ろうとしたら、ドアが閉まりそうになりました。乗せてほしいとき、何と言いますか。1、閉めていただけますか。2、すみません、開けてもらえますか。3、乗ってくださいますか。",
      "prompt": "エレベーターのドアが<ruby>閉<rt>し</rt></ruby>まりそうです。<ruby>乗<rt>の</rt></ruby>せてほしいとき、<ruby>何<rt>なん</rt></ruby>と<ruby>言<rt>い</rt></ruby>いますか。",
      "audio_file": "audio/listening/n3_q18.mp3",
      "choices": [
        "閉めていただけますか。",
        "乗ってくださいますか。",
        "すみません、開けてもらえますか。"
      ],
      "answer": 2,
      "explanation": {
        "ja": "閉まりそうなドアを開けて中に乗せてほしいときは「すみません、開けてもらえますか」と頼みます。選択肢3が正解です。",
        "en": "'すみません、開けてもらえますか' (Excuse me, could you hold/open the door for me?) is the proper phrasing. Choice 3 is correct.",
        "zh": "希望對方開門讓自己進入電梯時，應說「すみません、開けてもらえますか」（不好意思，能幫忙開一下門嗎？），因此選項3正確。",
        "ko": "닫히려는 엘리베이터 문을 열어 달라고 부탁할 때는 'すみません、開けてもらえますか(죄송합니다, 문 좀 열어주시겠습니까?)'가 자연스러우므로 3번이 정답입니다."
      },
      "section": "問題4 発話表現",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】エレベーターに乗ろうとしたら、ドアが閉まりそうになりました。乗せてほしいとき、何と言いますか。</p>\n      <p class=\"text-xs text-slate-700\">エレベーターに乗ろうとしたら、ドアが閉まりそうになりました。乗せてほしいとき、何と言いますか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">閉めていただけますか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">すみません、開けてもらえますか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">乗ってくださいますか。</p>\n    </div>"
    },
    {
      "q_num": 19,
      "section_id": "sec4",
      "section_name": "問題4 発話表現",
      "situation": "取引先から電話がかかってきましたが、担当者は席を外しています。何と言いますか。",
      "speech_audio_text": "取引先から電話がかかってきましたが、担当者は席を外しています。何と言いますか。1、担当の者はただいま席を外しております。2、担当の人はどこかへ行ってしまいました。3、担当の方はいらっしゃいません。",
      "prompt": "<ruby>担当者<rt>たんとうしゃ</rt></ruby>が<ruby>席<rt>せき</rt></ruby>を<ruby>外<rt>はず</rt></ruby>しています。<ruby>何<rt>なん</rt></ruby>と<ruby>言<rt>い</rt></ruby>いますか。",
      "audio_file": "audio/listening/n3_q19.mp3",
      "choices": [
        "担当の人はどこかへ行ってしまいました。",
        "担当の者はただいま席を外しております。",
        "担当の方はいらっしゃいません。"
      ],
      "answer": 1,
      "explanation": {
        "ja": "自社の社員を外部に対してへりくだって伝える謙譲・ビジネス敬語として「担当の者はただいま席を外しております」が正しい表現です。選択肢2が正解です。",
        "en": "'担当の者はただいま席を外しております' (The person in charge is away from their desk at the moment) is the standard business humble form. Choice 2 is correct.",
        "zh": "商務電話中向客戶說明自己公司的同仁暫時不在座位上時，謙讓語標準說法是「担当の者はただいま席を外しております」，因此選項2正確。",
        "ko": "비즈니스 전화에서 자기 회사 담당자가 자리를 비웠음을 거래처에 공손히 알릴 때는 '担当の者はただいま席を外しております'가 정확합니다."
      },
      "section": "問題4 発話表現",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】取引先から電話がかかってきましたが、担当者は席を外しています。何と言いますか。</p>\n      <p class=\"text-xs text-slate-700\">取引先から電話がかかってきましたが、担当者は席を外しています。何と言いますか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">担当の者はただいま席を外しております。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">担当の人はどこかへ行ってしまいました。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">担当の方はいらっしゃいません。</p>\n    </div>"
    },
    {
      "q_num": 20,
      "section_id": "sec5",
      "section_name": "問題5 即時応答",
      "situation": "「山田さん、今度の土曜日、一緒にハイキングに行かない？」",
      "speech_audio_text": "山田さん、今度の土曜日、一緒にハイキングに行かない？ 1、ええ、ぜひ喜んで！ 2、あいにくその日は先約があるんだ、また誘ってね。 3、はい、先週ハイキングに行きましたよ。",
      "prompt": "「山田さん、今度の土曜日、一緒にハイキングに行かない？」",
      "audio_file": "audio/listening/n3_q20.mp3",
      "choices": [
        "ええ、ぜひ喜んで！",
        "あいにくその日は先約があるんだ、また誘ってね。",
        "はい、先週ハイキングに行きましたよ。"
      ],
      "answer": 0,
      "explanation": {
        "ja": "「今度の土曜日、一緒にハイキングに行かない？」という誘いに対し、快く応じる「ええ、ぜひ喜んで！（選択肢1）」が適切です。選択肢3は「今度の土曜日」の誘いに対し過去の行動を答えていて不自然です。",
        "en": "Accepting an invitation to go hiking on Saturday with enthusiasm (Choice 1) is natural.",
        "zh": "面對週六一起去健行的邀約，欣然答應的選項1「好啊，非常樂意！」最為合適。",
        "ko": "이번 주 토요일 하이킹 제안에 기꺼이 응하는 1번이 자연스럽습니다."
      },
      "section": "問題5 即時応答",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】「山田さん、今度の土曜日、一緒にハイキングに行かない？」</p>\n      <p class=\"text-xs text-slate-700\">山田さん、今度の土曜日、一緒にハイキングに行かない？</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">ええ、ぜひ喜んで！</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">あいにくその日は先約があるんだ、また誘ってね。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">はい、先週ハイキングに行きましたよ。</p>\n    </div>"
    },
    {
      "q_num": 21,
      "section_id": "sec5",
      "section_name": "問題5 即時応答",
      "situation": "「こちらの傘、お忘れ物ではございませんか。」",
      "speech_audio_text": "こちらの傘、お忘れ物ではございませんか。 1、いいえ、傘は持っていませんよ。 2、あ、私のです！親切にありがとうございます。 3、はい、傘を忘れて帰るところでした。",
      "prompt": "「こちらの傘、お忘れ物ではございませんか。」",
      "audio_file": "audio/listening/n3_q21.mp3",
      "choices": [
        "いいえ、傘は持っていませんよ。",
        "あ、私のです！親切にありがとうございます。",
        "はい、傘を忘れて帰るところでした。"
      ],
      "answer": 1,
      "explanation": {
        "ja": "店員などからの「お忘れ物ではございませんか」という声かけに対し、自分の傘であることに気づいて礼を言う「あ、私のです！親切にありがとうございます（選択肢2）」が自然です。",
        "en": "Recognizing the forgotten umbrella and thanking the finder (Choice 2) is natural and polite.",
        "zh": "面對店員「這是您遺落的雨傘嗎？」的提醒，確認是自己的並表達感謝的選項2最為自然。",
        "ko": "우산을 두고 가지 않았냐는 물음에 자신의 것임을 확인하고 감사 인사를 하는 2번이 자연스럽습니다."
      },
      "section": "問題5 即時応答",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】「こちらの傘、お忘れ物ではございませんか。」</p>\n      <p class=\"text-xs text-slate-700\">こちらの傘、お忘れ物ではございませんか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">いいえ、傘は持っていませんよ。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">あ、私のです！親切にありがとうございます。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">はい、傘を忘れて帰るところでした。</p>\n    </div>"
    },
    {
      "q_num": 22,
      "section_id": "sec5",
      "section_name": "問題5 即時応答",
      "situation": "「課長、この企画書の修正、明日までにお願いできますでしょうか。」",
      "speech_audio_text": "課長、この企画書の修正、明日までにお願いできますでしょうか。 1、いえ、明日までに作っておきますね。 2、承知いたしました。直ちに修正いたします。 3、うん、明日の昼までには見ておくよ。",
      "prompt": "「課長、この企画書の修正、明日までにお願いできますでしょうか。」",
      "audio_file": "audio/listening/n3_q22.mp3",
      "choices": [
        "いえ、明日までに作っておきますね。",
        "承知いたしました。直ちに修正いたします。",
        "うん、明日の昼までには見ておくよ。"
      ],
      "answer": 2,
      "explanation": {
        "ja": "部下からの「明日までに確認・修正をお願いできますか」という依頼に対し、上司が「うん、明日の昼までには見ておくよ（選択肢3）」と引き受けるのが適切です。選択肢2は上司が部下に敬語で返しており主客逆転しています。",
        "en": "The boss naturally agrees to review the proposal draft by noon tomorrow (Choice 3).",
        "zh": "部下請求課長在明天前過目修改企劃書，主管答應「嗯，明天中午前我會看一下（選項3）」最為符合上下級語境。",
        "ko": "기획서 검토 요청에 상사가 내일 점심까지 봐두겠다고 수락하는 3번이 자연스럽습니다."
      },
      "section": "問題5 即時応答",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】「課長、この企画書の修正、明日までにお願いできますでしょうか。」</p>\n      <p class=\"text-xs text-slate-700\">課長、この企画書の修正、明日までにお願いできますでしょうか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">いえ、明日までに作っておきますね。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">承知いたしました。直ちに修正いたします。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">うん、明日の昼までには見ておくよ。</p>\n    </div>"
    },
    {
      "q_num": 23,
      "section_id": "sec5",
      "section_name": "問題5 即時応答",
      "situation": "「今日はずいぶん道路が混んでいましたね。」",
      "speech_audio_text": "今日はずいぶん道路が混んでいましたね。 1、本当に、いつもの倍くらい時間がかかりましたよ。 2、ええ、車が少なくてとても走りやすかったですね。 3、はい、電車が遅延していたそうですね。",
      "prompt": "「今日はずいぶん道路が混んでいましたね。」",
      "audio_file": "audio/listening/n3_q23.mp3",
      "choices": [
        "本当に、いつもの倍くらい時間がかかりましたよ。",
        "ええ、車が少なくてとても走りやすかったですね。",
        "はい、電車が遅延していたそうですね。"
      ],
      "answer": 0,
      "explanation": {
        "ja": "「道路が混んでいた（渋滞していた）」という発話に対し、「本当に、いつもの倍くらい時間がかかりましたよ（選択肢1）」と実感をもって共感するのが適切です。選択肢2は意味が反対です。",
        "en": "Agreeing with how congested the roads were and noting it took twice as long (Choice 1) matches conversational flow.",
        "zh": "面對「今天路上真堵啊」的感嘆，同調表示「真的，花的時間差不多是平時的兩倍呢（選項1）」最自然。",
        "ko": "도로가 많이 막혔다는 말에 평소의 두 배나 걸렸다며 깊이 공감하는 1번이 정답입니다."
      },
      "section": "問題5 即時応答",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】「今日はずいぶん道路が混んでいましたね。」</p>\n      <p class=\"text-xs text-slate-700\">今日はずいぶん道路が混んでいましたね。</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">本当に、いつもの倍くらい時間がかかりましたよ。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">ええ、車が少なくてとても走りやすかったですね。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">はい、電車が遅延していたそうですね。</p>\n    </div>"
    },
    {
      "q_num": 24,
      "section_id": "sec5",
      "section_name": "問題5 即時応答",
      "situation": "「ちょっとお聞きしたいことがあるんですが、今お時間よろしいですか。」",
      "speech_audio_text": "ちょっとお聞きしたいことがあるんですが、今お時間よろしいですか。 1、いえ、時間はまだありますよ。 2、はい、何でしょうか。 3、どういたしまして、お気になさらず。",
      "prompt": "「ちょっとお聞きしたいことがあるんですが、今お時間よろしいですか。」",
      "audio_file": "audio/listening/n3_q24.mp3",
      "choices": [
        "いえ、時間はまだありますよ。",
        "はい、何でしょうか。",
        "どういたしまして、お気になさらず。"
      ],
      "answer": 1,
      "explanation": {
        "ja": "「今お時間よろしいですか（相談や質問が可能か）」と尋ねられた際、用件を促す「はい、何でしょうか（選択肢2）」が標準的で最も自然な応答です。",
        "en": "When asked if you have a moment to talk, the standard polite response is \"Yes, what is it?\" (Choice 2).",
        "zh": "被詢問「現在方便打擾一下嗎？有些事情想請教您」，最標準自然的回答是選項2「好的，請問是什麼事呢？」。",
        "ko": "시간이 괜찮냐는 질문에 무엇인지 묻는 2번이 가장 자연스럽고 표준적인 응답입니다."
      },
      "section": "問題5 即時応答",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】「ちょっとお聞きしたいことがあるんですが、今お時間よろしいですか。」</p>\n      <p class=\"text-xs text-slate-700\">ちょっとお聞きしたいことがあるんですが、今お時間よろしいですか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">いえ、時間はまだありますよ。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">はい、何でしょうか。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">どういたしまして、お気になさらず。</p>\n    </div>"
    },
    {
      "q_num": 25,
      "section_id": "sec5",
      "section_name": "問題5 即時応答",
      "situation": "「この前貸してくれた本、すごく面白くて一気に読んじゃったよ！」",
      "speech_audio_text": "この前貸してくれた本、すごく面白くて一気に読んじゃったよ！ 1、気に入ってもらえてよかった！ 2、どういたしまして、本を読んでくれてすみません。 3、ええ、とてもつまらない本でしたね。",
      "prompt": "「この前貸してくれた本、すごく面白くて一気に読んじゃったよ！」",
      "audio_file": "audio/listening/n3_q25.mp3",
      "choices": [
        "気に入ってもらえてよかった！",
        "どういたしまして、本を読んでくれてすみません。",
        "ええ、とてもつまらない本でしたね。"
      ],
      "answer": 0,
      "explanation": {
        "ja": "貸した本が面白かったと褒められた際、貸した側として素直に喜ぶ「気に入ってもらえてよかった！（選択肢1）」が友達同士の自然な会話です。",
        "en": "Reacting with joy when someone praises the book you lent them (\"I am glad you liked it!\", Choice 1) is authentic.",
        "zh": "借給對方的書被誇讚非常有趣一口氣讀完了，借書人高興地回答「你喜歡真是太好了！（選項1）」最為自然。",
        "ko": "빌려준 책이 재미있었다는 칭찬에 마음에 들어서 다행이라고 기뻐하는 1번이 자연스럽습니다."
      },
      "section": "問題5 即時応答",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】「この前貸してくれた本、すごく面白くて一気に読んじゃったよ！」</p>\n      <p class=\"text-xs text-slate-700\">この前貸してくれた本、すごく面白くて一気に読んじゃったよ！</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">気に入ってもらえてよかった！</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">どういたしまして、本を読んでくれてすみません。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">ええ、とてもつまらない本でしたね。</p>\n    </div>"
    },
    {
      "q_num": 26,
      "section_id": "sec5",
      "section_name": "問題5 即時応答",
      "situation": "「この雨、夕方には上がるそうですよ。」",
      "speech_audio_text": "この雨、夕方には上がるそうですよ。 1、じゃあ、傘を持って出かける必要はありませんね。 2、ええ、夕方から大雨になるんですね。 3、そうですか、帰る頃には止んでいそうですね。",
      "prompt": "「この雨、夕方には上がるそうですよ。」",
      "audio_file": "audio/listening/n3_q26.mp3",
      "choices": [
        "じゃあ、傘を持って出かける必要はありませんね。",
        "ええ、夕方から大雨になるんですね。",
        "そうですか、帰る頃には止んでいそうですね。"
      ],
      "answer": 2,
      "explanation": {
        "ja": "「雨が夕方には上がる（止む）」という天気情報に対し、「そうですか、帰る頃には止んでいそうですね（選択肢3）」と状況を結びつけて納得するのが自然です。選択肢1は今降っているのに傘がいらないというのは矛盾します。",
        "en": "\"雨が上がる\" means the rain will stop. Choice 3 naturally deduces that it will likely be clear when heading home.",
        "zh": "「雨が上がる」是雨停的意思。得知傍晚雨會停，選項3「是嗎，那回去的時候應該已經停了呢」最符合生活常理。",
        "ko": "'雨が上がる'(비가 그치다)라는 정보에 귀가할 때쯤엔 그쳐 있겠다고 반응하는 3번이 자연스럽습니다."
      },
      "section": "問題5 即時応答",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】「この雨、夕方には上がるそうですよ。」</p>\n      <p class=\"text-xs text-slate-700\">この雨、夕方には上がるそうですよ。</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">じゃあ、傘を持って出かける必要はありませんね。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">ええ、夕方から大雨になるんですね。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">そうですか、帰る頃には止んでいそうですね。</p>\n    </div>"
    },
    {
      "q_num": 27,
      "section_id": "sec5",
      "section_name": "問題5 即時応答",
      "situation": "「新商品のサンプル、もう届いているはずなんですが……」",
      "speech_audio_text": "新商品のサンプル、もう届いているはずなんですが……。 1、届いたら注文することにしましょう。 2、今、受付に届いていないか確認してきますね。 3、ええ、来週発送される予定だそうですよ。",
      "prompt": "「新商品のサンプル、もう届いているはずなんですが……。」",
      "audio_file": "audio/listening/n3_q27.mp3",
      "choices": [
        "届いたら注文することにしましょう。",
        "今、受付に届いていないか確認してきますね。",
        "ええ、来週発送される予定だそうですよ。"
      ],
      "answer": 1,
      "explanation": {
        "ja": "「もう届いているはずなのに見当たらない」という困りごとに対し、自ら進んで確認しに行く「今、受付に届いていないか確認してきますね（選択肢2）」が協調的な同僚の受け答えとして最適です。",
        "en": "Offering to check at reception when an expected sample package is missing (Choice 2) is proactive and helpful.",
        "zh": "聽到預計送達的樣品還沒看到，主動表示去前台確認的選項2「我現在去櫃檯確認看看有沒有送達」最為合適。",
        "ko": "도착해 있어야 할 샘플이 보이지 않는 상황에서 안내데스크에 확인하러 가겠다는 2번이 자연스럽습니다."
      },
      "section": "問題5 即時応答",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】「新商品のサンプル、もう届いているはずなんですが……」</p>\n      <p class=\"text-xs text-slate-700\">新商品のサンプル、もう届いているはずなんですが……。</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">届いたら注文することにしましょう。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">今、受付に届いていないか確認してきますね。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">ええ、来週発送される予定だそうですよ。</p>\n    </div>"
    },
    {
      "q_num": 28,
      "section_id": "sec5",
      "section_name": "問題5 即時応答",
      "situation": "「鈴木さん、明日のプレゼン、落ち着いて頑張ってね！」",
      "speech_audio_text": "鈴木さん、明日のプレゼン、落ち着いて頑張ってね！ 1、ええ、とても上手に発表できましたよ。 2、落ち着いて聞いてくださって助かりました。 3、ありがとうございます、深呼吸して全力を尽くします！",
      "prompt": "「鈴木さん、明日のプレゼン、落ち着いて頑張ってね！」",
      "audio_file": "audio/listening/n3_q28.mp3",
      "choices": [
        "ええ、とても上手に発表できましたよ。",
        "落ち着いて聞いてくださって助かりました。",
        "ありがとうございます、深呼吸して全力を尽くします！"
      ],
      "answer": 2,
      "explanation": {
        "ja": "明日のプレゼンに対する応援・激励に対し、「ありがとうございます、深呼吸して全力を尽くします！（選択肢3）」と感謝と前向きな決意を述べるのが正解です。選択肢1はまだ明日なのに過去形になっており不自然です。",
        "en": "Accepting encouragement for tomorrow's presentation with gratitude and determination (Choice 3) is natural.",
        "zh": "面對明天簡報的鼓勵與加油，道謝並表示會深呼吸全力以赴的選項3「謝謝您，我會深呼吸全力以赴的！」最為恰當。",
        "ko": "내일 발표에 대한 격려에 감사하며 전력을 다하겠다고 각오를 밝히는 3번이 정답입니다."
      },
      "section": "問題5 即時応答",
      "script_html": "<div class=\"space-y-2 text-sm leading-relaxed\">\n      <p class=\"text-xs font-bold text-slate-500 mb-2\">【場面】「鈴木さん、明日のプレゼン、落ち着いて頑張ってね！」</p>\n      <p class=\"text-xs text-slate-700\">鈴木さん、明日のプレゼン、落ち着いて頑張ってね！</p>\n<p class=\"text-xs text-slate-600 pl-4\">1、</p>\n<p class=\"text-xs text-slate-700\">ええ、とても上手に発表できましたよ。</p>\n<p class=\"text-xs text-slate-600 pl-4\">2、</p>\n<p class=\"text-xs text-slate-700\">落ち着いて聞いてくださって助かりました。</p>\n<p class=\"text-xs text-slate-600 pl-4\">3、</p>\n<p class=\"text-xs text-slate-700\">ありがとうございます、深呼吸して全力を尽くします！</p>\n    </div>"
    }
  ]
};
