# -*- coding: utf-8 -*-
"""
JLPT N4 Listening Comprehension Data (28 Questions, Multi-Speaker Audio & 4:3 Illustrations)
1. 問題1 課題理解 (8問) - 4択
2. 問題2 ポイント理解 (7問) - 4択
3. 問題3 発話表現 (5問) - 3択 (音声内で選択肢1〜3も読み上げ)
4. 問題4 即時応答 (8問) - 3択 (音声内で選択肢1〜3も読み上げ)
"""
import os, sys, re, json, hashlib, random, collections

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, 'n5_rewrite'))
from n5_lib import R, P, lint_ruby, place_choices, balanced_targets, sensitive_hits, write_js, num_reading, parse_num, _counter

SECS = {
    '1': '問題1 課題理解',
    '2': '問題2 ポイント理解',
    '3': '問題3 発話表現',
    '4': '問題4 即時応答',
}

def RR(t):
    """Apply explicit disambiguations before calling R(t)."""
    def rep_outside(src, old, new):
        return re.sub(r'(?<![{|])' + re.escape(old), new, src)
    t = rep_outside(t, '何と言', '{何|なん}と言')
    t = rep_outside(t, '十分', '{十分|じゅうぶん}')
    t = rep_outside(t, '一日中', '{一日中|いちにちじゅう}')
    t = rep_outside(t, '一日おき', '{一日|いちにち}おき')
    t = rep_outside(t, '何部', '{何部|なんぶ}')
    t = rep_outside(t, '15部', '15{部|ぶ}')
    t = rep_outside(t, '2部', '2{部|ぶ}')
    t = rep_outside(t, '2名', '2{名|めい}')
    t = rep_outside(t, '17名', '17{名|めい}')
    t = rep_outside(t, '一番', '{一番|いちばん}')
    t = rep_outside(t, '海日和', '{海日和|うみびより}')
    t = rep_outside(t, '前日', '{前日|ぜんじつ}')
    t = rep_outside(t, '休日', '{休日|きゅうじつ}')
    t = rep_outside(t, '日曜日', '{日曜日|にちようび}')
    t = rep_outside(t, '月曜日', '{月曜日|げつようび}')
    t = rep_outside(t, '火曜日', '{火曜日|かようび}')
    t = rep_outside(t, '水曜日', '{水曜日|すいようび}')
    t = rep_outside(t, '木曜日', '{木曜日|もくようび}')
    t = rep_outside(t, '金曜日', '{金曜日|きんようび}')
    t = rep_outside(t, '土曜日', '{土曜日|どようび}')
    t = rep_outside(t, '気にせず', '{気|き}にせず')
    t = rep_outside(t, '気兼ねなく', '{気兼|きが}ねなく')
    t = rep_outside(t, '気に入って', '{気|き}に{入|い}って')
    t = rep_outside(t, '気に入り', '{気|き}に{入|い}り')
    t = rep_outside(t, '生かす', '{生|い}かす')
    t = rep_outside(t, '生のまま', '{生|なま}のまま')
    t = rep_outside(t, '生地', '{生地|きじ}')
    t = rep_outside(t, '留学生', '{留学生|りゅうがくせい}')
    t = rep_outside(t, '小学生', '{小学生|しょうがくせい}')
    t = rep_outside(t, '中学生', '{中学生|ちゅうがくせい}')
    t = rep_outside(t, '高校生', '{高校生|こうこうせい}')
    t = rep_outside(t, '大学生', '{大学生|だいがくせい}')
    t = rep_outside(t, '生活', '{生活|せいかつ}')
    t = rep_outside(t, '生中継', '{生中継|なまちゅうけい}')
    t = rep_outside(t, '作り方', '{作|つく}り{方|かた}')
    t = rep_outside(t, '行き方', '{行|い}き{方|かた}')
    t = rep_outside(t, '使い方', '{使|つか}い{方|かた}')
    t = rep_outside(t, 'やり方', 'やり{方|かた}')
    t = rep_outside(t, '読み方', '{読|よ}み{方|かた}')
    t = rep_outside(t, '書き方', '{書|か}き{方|かた}')
    t = rep_outside(t, '見方', '{見方|みかた}')
    t = rep_outside(t, '夕方', '{夕方|ゆうがた}')
    t = rep_outside(t, '仕方', '{仕方|しかた}')
    t = rep_outside(t, '読みたい方', '{読|よ}みたい{方|かた}')
    t = rep_outside(t, '多くの方', '{多|おお}くの{方|かた}')
    t = rep_outside(t, 'した方がいい', 'した{方|ほう}がいい')
    t = rep_outside(t, 'お冷', 'お{冷|ひや}')
    t = rep_outside(t, 'お年寄り', 'お{年寄|としよ}り')
    t = rep_outside(t, 'お疲れ様', 'お{疲|つか}れ{様|さま}')
    t = rep_outside(t, 'お先に', 'お{先|さき}に')
    t = rep_outside(t, 'お邪魔', 'お{邪魔|じゃま}')
    t = rep_outside(t, '肉離れ', '{肉離|にくばな}れ')
    t = rep_outside(t, '着心地', '{着心地|きごこち}')
    t = rep_outside(t, '使い心地', '{使|つか}い{心地|ごこち}')
    t = rep_outside(t, '決め手', '{決|き}め{手|て}')
    t = rep_outside(t, '片手', '{片手|かたて}')
    t = rep_outside(t, '手伝い', '{手伝|てつだ}い')
    t = rep_outside(t, '手伝って', '{手伝|てつだ}って')
    t = rep_outside(t, '手伝う', '{手伝|てつだ}う')
    t = rep_outside(t, 'お薬手帳', 'お{薬手帳|くすりてちょう}')
    t = rep_outside(t, '焼き立て', '{焼|や}き{立|た}て')
    t = rep_outside(t, '焼き上がった', '{焼|や}き{上|あ}がった')
    t = rep_outside(t, '入って', '{入|はい}って')
    t = rep_outside(t, '入った', '{入|はい}った')
    t = rep_outside(t, '入れて', '{入|い}れて')
    t = rep_outside(t, '入れな', '{入|い}れな')
    t = rep_outside(t, 'お貸し出し', 'お{貸|か}し{出|だ}し')
    t = rep_outside(t, '貸出', '{貸出|かしだし}')
    t = rep_outside(t, '申し出', '{申|もう}し{出|で}')
    t = rep_outside(t, '申し込み', '{申|もう}し{込|こ}み')
    t = rep_outside(t, '締め切り', '{締|し}め{切|き}り')
    t = rep_outside(t, '締切', '{締切|しめきり}')
    t = rep_outside(t, '測り終わった', '{測|はか}り{終|お}わった')
    t = rep_outside(t, '引き出して', '{引|ひ}き{出|だ}して')
    t = rep_outside(t, '引き出す', '{引|ひ}き{出|だ}す')
    t = rep_outside(t, '引っ越し', '{引|ひ}っ{越|こ}し')
    t = rep_outside(t, '待ち合わせ', '{待|ま}ち{合|あ}わせ')
    t = rep_outside(t, '持ち運び', '{持|も}ち{運|はこ}び')
    t = rep_outside(t, '持ち運ぶ', '{持|も}ち{運|はこ}ぶ')
    t = rep_outside(t, 'お持ち', 'お{持|も}ち')
    t = rep_outside(t, '持ってきて', '{持|も}ってきて')
    t = rep_outside(t, '持ってきた', '{持|も}ってきた')
    t = rep_outside(t, '持ってきます', '{持|も}ってきます')
    t = rep_outside(t, '持っていく', '{持|も}っていく')
    t = rep_outside(t, '持ってこなければ', '{持|も}ってこなければ')
    t = rep_outside(t, '着てきて', '{着|き}てきて')
    t = rep_outside(t, '帰ってきて', '{帰|かえ}ってきて')
    t = rep_outside(t, '降ってきました', '{降|ふ}ってきました')
    t = rep_outside(t, '降った', '{降|ふ}った')
    t = rep_outside(t, '大雨が降った', '{大雨|おおあめ}が{降|ふ}った')
    t = rep_outside(t, '降っていません', '{降|ふ}っていません')
    t = rep_outside(t, '見に行きませんか', '{見|み}に{行|い}きませんか')
    t = rep_outside(t, '行きましょう', '{行|い}きましょう')
    t = rep_outside(t, '行きません', '{行|い}きません')
    t = rep_outside(t, '行きますか', '{行|い}きますか')
    t = rep_outside(t, '行かなかった', '{行|い}かなかった')
    t = rep_outside(t, '行く', '{行|い}く')
    t = rep_outside(t, '行けなく', '{行|い}けなく')
    t = rep_outside(t, '行っても', '{行|い}っても')
    t = rep_outside(t, '行っている', '{行|おこな}っている')
    t = rep_outside(t, '行います', '{行|おこな}います')
    t = rep_outside(t, '受付', '{受付|うけつけ}')
    t = rep_outside(t, 'お出し', 'お{出|だ}し')
    t = rep_outside(t, 'お座り', 'お{座|すわ}り')
    t = rep_outside(t, '美味しい', '{美味|おい}しい')
    t = rep_outside(t, '美味しく', '{美味|おい}しく')
    t = rep_outside(t, '仕上げる', '{仕上|しあ}げる')
    t = rep_outside(t, '仕上がります', '{仕上|しあ}がります')
    t = rep_outside(t, '玉ねぎ', '{玉|たま}ねぎ')
    t = rep_outside(t, '人参', '{人参|にんじん}')
    t = rep_outside(t, '強火', '{強火|つよび}')
    t = rep_outside(t, '弱火', '{弱火|よわび}')
    t = rep_outside(t, '一気に', '{一気|いっき}に')
    t = rep_outside(t, 'お皿', 'お{皿|さら}')
    t = rep_outside(t, '流し', '{流|なが}し')
    t = rep_outside(t, '店頭', '{店頭|てんとう}')
    t = rep_outside(t, '入り口', '{入|い}り{口|ぐち}')
    t = rep_outside(t, '看病', '{看病|かんびょう}')
    t = rep_outside(t, '高熱', '{高熱|こうねつ}')
    t = rep_outside(t, 'お天気', 'お{天気|てんき}')
    t = rep_outside(t, '肩こり', '{肩|かた}こり')
    t = rep_outside(t, '吸引力', '{吸引力|きゅういんりょく}')
    t = rep_outside(t, '買い忘れ', '{買|か}い{忘|わす}れ')
    t = rep_outside(t, '見やすそう', '{見|み}やすそう')
    t = rep_outside(t, 'わかりやす', 'わかりやす')
    t = rep_outside(t, '運動前', '{運動前|うんどうまえ}')
    t = rep_outside(t, '館内閲覧', '{館内閲覧|かんないえつらん}')
    t = rep_outside(t, '最新号', '{最新号|さいしんごう}')
    t = rep_outside(t, '来月号', '{来月号|らいげつごう}')
    t = rep_outside(t, 'この号', 'この{号|ごう}')
    t = rep_outside(t, 'ご覧', 'ご{覧|らん}')
    t = rep_outside(t, '怪我', '{怪我|けが}')
    t = rep_outside(t, '捻挫', '{捻挫|ねんざ}')
    t = rep_outside(t, 'お会計', 'お{会計|かいけい}')
    t = rep_outside(t, '通行人', '{通行人|つうこうにん}')
    t = rep_outside(t, '紅葉', '{紅葉|もみじ}')
    t = rep_outside(t, '一杯', '{一杯|いっぱい}')
    t = rep_outside(t, '折りたたみ傘', '{折|お}りたたみ{傘|がさ}')
    t = rep_outside(t, '差して', '{差|さ}して')
    t = rep_outside(t, '14時半', '14{時半|じはん}')
    t = rep_outside(t, '10分間', '10{分間|ぷんかん}')
    t = rep_outside(t, '1分間', '1{分間|ぷんかん}')
    t = rep_outside(t, '10分後', '10{分後|ぷんご}')
    t = rep_outside(t, '30分前', '30{分前|ぷんまえ}')
    return R(t)


ITEMS = [
    # ==================== 問題1 課題理解 (8問: Q1〜Q8) ====================
    dict(
        sec='1',
        title='病院での検温と受付手順',
        situation='病院で女の看護師と男の人が話しています。男の人はこのあと、まず何をしますか。',
        prompt='男の人はこのあと、まず何をしますか。',
        dialogue=[
            ('f', '佐藤さん、今日はお熱が38度ありますね。医師の診察の前に、まずこちらの体温計でもう一度熱を測っていただけますか。'),
            ('m', 'わかりました。それから、保険証は今出しますか。'),
            ('f', '保険証とお薬手帳は、熱を測り終わった後で受付にお出しください。'),
            ('m', 'わかりました。じゃあ、今すぐ測りますね。'),
        ],
        choices=[
            '体温計でもう一度熱を測る。',
            '受付に保険証とお薬手帳を出す。',
            '薬局へ薬をもらいに行く。',
            '診察室に入って医師と話す。',
        ],
        answer=0,
        exp=dict(
            ja='看護師から「医師の診察の前に、まずこちらの体温計でもう一度熱を測っていただけますか」と指示され、保険証は熱を測り終わった後で受付に出すことになっているため、まず行うのは検温です。',
            en='The nurse instructs him to take his temperature again with the thermometer first before the doctor\'s exam, and to hand in his insurance card afterward.',
            zh='護理師指示看診前先用體溫計再量一次體溫，健保卡等量完體溫後再交到櫃檯，因此最先做的是量體溫。',
            ko='간호사가 의사 진료 전에 먼저 체온계로 열을 다시 재달라고 지시했고 보험증은 열을 다 잰 후에 접수처에 내라고 했으므로 가장 먼저 할 일은 체온 측정입니다.',
        ),
        img='images/listening_n4/n4_q1.jpg',
    ),
    dict(
        sec='1',
        title='会議資料の追加コピー',
        situation='会社で男の課長と女の社員が話しています。女の社員はこのあと、何を準備しますか。',
        prompt='女の社員はこのあと、何を準備しますか。',
        dialogue=[
            ('m', '高橋さん、午後の会議の資料、何部印刷した？'),
            ('f', '15部印刷してホチキスで留めました。'),
            ('m', 'ありがとう。そういえば、参加者が急に2名増えて17名になったんだ。追加で2部コピーしてくれるかい？'),
            ('f', 'わかりました。プロジェクターのリモコンも用意しておきましょうか。'),
            ('m', 'それは僕が持っていくから大丈夫だよ。資料の追加だけお願いね。'),
            ('f', 'かしこまりました。'),
        ],
        choices=[
            'プロジェクターのリモコンを探す。',
            '会議資料を2部追加でコピーする。',
            '会議室の机と椅子を2つ並べる。',
            '15部印刷した資料を捨てる。',
        ],
        answer=1,
        exp=dict(
            ja='参加者が2名増えたため、課長から「追加で2部コピーしてくれるかい」と頼まれています。プロジェクターのリモコンは課長が持っていくと言っているため、女の社員は会議資料を2部追加でコピーします。',
            en='Because two more attendees joined, the manager asks her to make two additional copies of the meeting materials, while he brings the projector remote himself.',
            zh='由於與會人數增加了2位，課長請她追加複印2份會議資料，而投影機遙控器由課長自己帶去。',
            ko='참석자가 2명 늘어나서 과장이 회의 자료를 2부 추가 복사해 달라고 부탁했고 리모컨은 과장이 가져간다고 했습니다.',
        ),
        img='images/listening_n4/n4_q2.jpg',
    ),
    dict(
        sec='1',
        title='奨学金申し込みの不足書類',
        situation='大学の事務室で男の留学生と女の職員が話しています。留学生は明日、何を持ってこなければなりませんか。',
        prompt='留学生は明日、何を持ってこなければなりませんか。',
        dialogue=[
            ('m', 'すみません、奨学金の申し込み書類を持ってきました。'),
            ('f', 'はい、拝見しますね。申請書と成績証明書は揃っていますね。ただ、証明写真が貼られていませんよ。'),
            ('m', 'すみません、写真を貼るのを忘れていました！'),
            ('f', '裏面に名前を書いたカラー写真を1枚、明日までに持ってきてください。学生証のコピーは事務室で取れますから要りませんよ。'),
            ('m', 'わかりました。明日写真を持ってきます。'),
        ],
        choices=[
            '成績証明書',
            '学生証のコピー',
            '裏面に名前を書いた証明写真1枚',
            'パスポートの原本',
        ],
        answer=2,
        exp=dict(
            ja='申請書と成績証明書は揃っており、学生証のコピーは不要ですが、職員から「裏面に名前を書いたカラー写真を1枚、明日までに持ってきてください」と指示されています。',
            en='The application form and transcript are already complete, and a student ID copy is unnecessary, so the staff member instructs him to bring one color ID photo with his name written on the back by tomorrow.',
            zh='申請書與成績證明書都已齊全，學生證影本也不需要，職員指示明天之前帶一張背面寫上姓名的彩色證件照過來。',
            ko='신청서와 성적증명서는 갖춰져 있고 학생증 사본은 필요 없으며, 직원이 뒷면에 이름을 적은 컬러 증명사진 1장을 내일까지 가져오라고 지시했습니다.',
        ),
        img='images/listening_n4/n4_q3.jpg',
    ),
    dict(
        sec='1',
        title='映画の待ち合わせ時間と場所',
        situation='男の人と女の人が明日の映画について電話で話しています。二人は明日、何時にどこで会いますか。',
        prompt='二人は明日、何時にどこで会いますか。',
        dialogue=[
            ('m', 'もしもし、明日の映画だけど、14時に映画館の前で待ち合わせでいい？'),
            ('f', '映画が14時半からだから、少し早めに会ってチケットを発券しない？映画館の前だと混んでいてわかりにくいし。'),
            ('m', 'そうだね。じゃあ30分前の14時に駅の改札前はどう？'),
            ('f', 'うん、中央改札の前ならわかりやすいね。じゃあ14時に駅の中央改札で会おう！'),
            ('m', 'わかった、じゃあ明日ね！'),
        ],
        choices=[
            '13時30分に映画館の前',
            '14時に映画館の売店',
            '14時30分に駅のホーム',
            '14時に駅の中央改札前',
        ],
        answer=3,
        exp=dict(
            ja='男の人が「30分前の14時に駅の改札前はどう？」と提案し、女の人が「中央改札の前ならわかりやすいね。じゃあ14時に駅の中央改札で会おう」と合意しています。',
            en='The man suggests meeting at the station ticket gate at 14:00 (30 minutes before the 14:30 movie), and the woman agrees to meet in front of the station\'s central ticket gate at 14:00.',
            zh='男生提議在電影開演前30分鐘的14點於車站檢票口前見面，女生也同意14點在車站的中央檢票口前碰面。',
            ko='남자가 30분 전인 14시에 역 개찰구 앞이 어떠냐고 제안했고 여자가 14시에 역 중앙 개찰구 앞에서 만나자고 동의했습니다.',
        ),
        img='images/listening_n4/n4_q4.jpg',
    ),
    dict(
        sec='1',
        title='レストランでの飲み物注文',
        situation='レストランで男の客と女の店員が話しています。店員はこのあと、まず何を運んできますか。',
        prompt='店員はこのあと、まず何を運んできますか。',
        dialogue=[
            ('m', 'すみません、パスタとハンバーグセットを注文したいんですが。'),
            ('f', 'かしこまりました。セットにはコーヒーか紅茶がつきますが、食後にお持ちしますか。'),
            ('m', '外が暑かったので、アイスコーヒーを先にもらえますか。'),
            ('f', 'かしこまりました。お冷とおしぼりもお持ちしますね。'),
            ('m', 'お冷は今持っていますから大丈夫ですよ。アイスコーヒーだけお願いします。'),
            ('f', '承知いたしました。'),
        ],
        choices=[
            'パスタとハンバーグ',
            '熱い紅茶',
            'アイスコーヒー',
            '氷の入ったお冷',
        ],
        answer=2,
        exp=dict(
            ja='男の客から「アイスコーヒーを先にもらえますか」「お冷は今持っていますから大丈夫ですよ。アイスコーヒーだけお願いします」と言われたため、店員がまず運んでくるのはアイスコーヒーです。',
            en='The customer asks for iced coffee before the meal and says he already has water, so the server will bring the iced coffee first.',
            zh='男客人要求先上冰咖啡，並表示自己已經有水了只需要冰咖啡，因此店員最先送來的是冰咖啡。',
            ko='손님이 아이스커피를 먼저 달라고 하고 물은 이미 가지고 있으니 아이스커피만 부탁한다고 했으므로 점원이 먼저 가져올 것은 아이스커피입니다.',
        ),
        img='images/listening_n4/n4_q5.jpg',
    ),
    dict(
        sec='1',
        title='京都行き特急電車の乗車ホーム',
        situation='駅の窓口で男の旅行客と女の駅員が話しています。旅行客はこのあと、どのホームへ行きますか。',
        prompt='旅行客はこのあと、どのホームへ行きますか。',
        dialogue=[
            ('m', 'すみません、京都駅に行きたいのですが、どの電車に乗ればいいですか。'),
            ('f', '京都ですね。快速電車なら3番ホーム、特急電車なら4番ホームです。'),
            ('m', '速く着く特急に乗りたいです。'),
            ('f', '特急ですね。特急券はお持ちですか。'),
            ('m', 'はい、さっき券売機で買いました。'),
            ('f', 'では、4番ホームへお進みください。10分後に電車がまいります。'),
            ('m', 'ありがとうございます！'),
        ],
        choices=[
            '1番ホーム',
            '4番ホーム',
            '3番ホーム',
            '2番ホーム',
        ],
        answer=1,
        exp=dict(
            ja='旅行客は特急電車に乗りたいと希望し、すでに特急券も持っているため、駅員から「では、4番ホームへお進みください」と案内されています。',
            en='The traveler wants to take the limited express train and already has an express ticket, so the station attendant directs him to Platform 4.',
            zh='旅客希望搭乘較快的特急列車且已經買好特急券，站務員便指引他前往4號月台。',
            ko='여행객이 특급열차를 타고 싶어 하고 이미 특급권도 가지고 있어서 역무원이 4번 홈으로 가라고 안내했습니다.',
        ),
        img='images/listening_n4/n4_q6.jpg',
    ),
    dict(
        sec='1',
        title='引っ越し作業の手伝い手順',
        situation='アパートで引っ越しの手伝いに来た男の人と女の人が話しています。男の人はこのあと、まず何をしますか。',
        prompt='男の人はこのあと、まず何をしますか。',
        dialogue=[
            ('m', '手伝いに来たよ！何から始めようか？'),
            ('f', 'ありがとう、助かるわ。本や小物はもうダンボールに詰めたから、台所のお皿を割れないように新聞紙で包んでほしいの。'),
            ('m', 'わかった。ダンボールを車に運ぶのは後でいい？'),
            ('f', 'ええ、荷物が全部まとまってから一気に車へ運びましょう。お皿の新聞紙は流しの下にあるから使ってね。'),
            ('m', 'よし、じゃあお皿を包むね。'),
        ],
        choices=[
            '新しいアパートへ車を運転する。',
            'ダンボールを車へ運ぶ。',
            '本や小物をダンボールに詰める。',
            '台所のお皿を新聞紙で包む。',
        ],
        answer=3,
        exp=dict(
            ja='本や小物はすでに箱詰めが終わっており、車への運搬は後で行うことになったため、男の人はまず「台所のお皿を割れないように新聞紙で包む」作業をします。',
            en='Books and small items are already packed and moving boxes to the car will be done later, so the man will wrap the kitchen plates in newspaper first.',
            zh='書籍和小物品已經裝箱，搬上車等全部打包完再一起進行，因此男生首先要做的是用報紙把廚房的盤子包起來。',
            ko='책과 소품은 이미 상자에 담았고 차로 나르는 일은 나중에 하기로 했으므로 남자가 먼저 할 일은 부엌 접시를 신문지로 싸는 것입니다.',
        ),
        img='images/listening_n4/n4_q7.jpg',
    ),
    dict(
        sec='1',
        title='パン屋での開店・接客準備',
        situation='パン屋で男の店長と女のアルバイト店員が話しています。アルバイト店員はこのあと、まず何をしますか。',
        prompt='アルバイト店員はこのあと、まず何をしますか。',
        dialogue=[
            ('m', '鈴木さん、焼き立てのカレーパンが焼き上がったよ。'),
            ('f', 'はい、すぐに店頭の棚に並べますね。'),
            ('m', 'ありがとう。ただ、並べる前に、トングとトレーの消毒をして補充してくれるかい？ちょうど今、お客さんがたくさん入ってきて足りなくなりそうなんだ。'),
            ('f', 'わかりました！トングとトレーを消毒して入り口に置いてから、パンを並べますね。'),
        ],
        choices=[
            'トングとトレーを消毒して入り口に補充する。',
            'カレーパンの生地をこねる。',
            'レジでお金の計算をする。',
            '外の看板を片付ける。',
        ],
        answer=0,
        exp=dict(
            ja='店長から「パンを並べる前に、トングとトレーの消毒をして補充してくれるかい」と指示され、アルバイト店員も「トングとトレーを消毒して入り口に置いてから、パンを並べますね」と答えています。',
            en='The bakery manager asks her to disinfect and restock the tongs and trays before putting out the curry bread, and she agrees to do that first.',
            zh='店長指示在把咖哩麵包擺上架之前，先消毒夾子和托盤並補充到入口處，打工店員也回答會先完成這件事。',
            ko='점장이 빵을 진열하기 전에 집게와 쟁반을 소독해서 입구에 보충해 달라고 지시했고 아르바이트생도 그렇게 하겠다고 답했습니다.',
        ),
        img='images/listening_n4/n4_q8.jpg',
    ),

    # ==================== 問題2 ポイント理解 (7問: Q9〜Q15) ====================
    dict(
        sec='2',
        title='休日に海へ行けなかった理由',
        situation='男の人と女の人が話しています。女の人が先週の休日に海へ行かなかった理由は何ですか。',
        prompt='女の人が先週の休日に海へ行かなかった理由は何ですか。',
        dialogue=[
            ('m', '林さん、先週の日曜日は友達と海へ行くって言ってたよね。泳いできた？'),
            ('f', 'ううん、実は行けなくなっちゃったの。'),
            ('m', 'えっ、雨が降ったから？'),
            ('f', 'ううん、お天気はすごく良くて海日和だったんだけど、前日の夜に妹が急に高熱を出してしまって。両親が仕事でいなかったから、私が看病しなきゃいけなくて。'),
            ('m', 'そうだったんだ。大変だったね。'),
        ],
        choices=[
            '台風で大雨が降ったから。',
            '妹が高熱を出して看病しなければならなかったから。',
            '電車のチケットを買い忘れたから。',
            '友達と約束の日を間違えたから。',
        ],
        answer=1,
        exp=dict(
            ja='天気はとても良かったのですが、「前日の夜に妹が急に高熱を出してしまって、両親が仕事でいなかったから、私が看病しなきゃいけなくて」と理由を話しています。',
            en='Although the weather was great for the beach, her younger sister suddenly developed a high fever the night before and she had to stay home to nurse her.',
            zh='雖然天氣非常好，但因為前一天晚上妹妹突然發高燒，父母又因工作不在家，她必須留在家裡照顧妹妹。',
            ko='날씨는 매우 좋았지만 전날 밤에 여동생이 갑자기 고열이 났고 부모님이 일 때문에 안 계셔서 여동생을 간호해야 했기 때문입니다.',
        ),
        img='images/listening_n4/n4_q9.jpg',
    ),
    dict(
        sec='2',
        title='新しいパソコンを気に入っている理由',
        situation='会社で男の人と女の人が話しています。女の人が新しいパソコンを気に入っている一番の理由は何ですか。',
        prompt='女の人が新しいパソコンを気に入っている一番の理由は何ですか。',
        dialogue=[
            ('m', '新しい会社のパソコン、使い心地はどう？画面が大きくて見やすそうだね。'),
            ('f', 'うん、画面も綺麗なんだけど、一番嬉しいのは本体がすごく軽くなったことなの！前のパソコンは重くて、出張や在宅勤務で持ち運ぶのが本当に大変だったの。今のは片手で持てるくらい軽くて肩こりが全然しなくなったわ。'),
            ('m', '持ち運びが楽なのは一番のメリットだね。'),
        ],
        choices=[
            '画面のサイズが大きくなったこと',
            '値段が前の機種より安かったこと',
            'キーボードの文字が光ること',
            '本体がとても軽くて持ち運びが楽になったこと',
        ],
        answer=3,
        exp=dict(
            ja='女の人は画面の綺麗さにも触れつつ、「一番嬉しいのは本体がすごく軽くなったことなの！片手で持てるくらい軽くて肩こりが全然しなくなった」と述べています。',
            en='While the screen is nice, she says what makes her happiest is how lightweight the new laptop is, making it effortless to carry around.',
            zh='雖然螢幕也很清晰，但她表示最開心的是機身變得非常輕巧，單手就能拿起，出差或居家辦公攜帶時輕鬆許多。',
            ko='화면도 깨끗하지만 가장 기쁜 점은 본체가 한 손으로 들 수 있을 만큼 매우 가벼워져서 들고 다니기 편해졌다는 것입니다.',
        ),
        img='images/listening_n4/n4_q10.jpg',
    ),
    dict(
        sec='2',
        title='新しい掃除機を買った決め手',
        situation='家で夫と妻が新しい掃除機について話しています。二人がこの掃除機を買った一番の決め手は何ですか。',
        prompt='二人がこの掃除機を買った一番の決め手は何ですか。',
        dialogue=[
            ('m', '新しいコードレス掃除機、早速届いたね。'),
            ('f', 'ええ。デザインもシンプルで部屋に馴染むわね。'),
            ('m', 'うん。他の店で見た機種は軽かったけど、音が大きくて夜に使えそうになかったよね。'),
            ('f', 'そうそう！これは音がすごく静かだから、夜遅くに帰ってきてちょっと掃除したい時でも近所を気にせず使えるのが一番の決め手だったわね。'),
            ('m', '吸引力も十分だし、いい買い物をしたね。'),
        ],
        choices=[
            '音がとても静かで夜でも気兼ねなく使えること',
            'セールで半額になっていたこと',
            '重くて絶対に倒れないこと',
            'ゴミを自動でゴミ箱へ運んでくれること',
        ],
        answer=0,
        exp=dict(
            ja='妻が「これは音がすごく静かだから、夜遅くに帰ってきてちょっと掃除したい時でも近所を気にせず使えるのが一番の決め手だったわね」と話しています。',
            en='The wife explains that the biggest deciding factor was how quiet it is, allowing them to vacuum late at night without worrying about bothering the neighbors.',
            zh='太太提到最關鍵的決定因素是這台吸塵器聲音非常安靜，即使很晚回家想稍微打掃也不用擔心吵到鄰居。',
            ko='아내가 소리가 매우 조용해서 밤늦게 돌아와 청소하고 싶을 때도 이웃 눈치를 보지 않고 쓸 수 있다는 점이 가장 큰 결정적 이유였다고 말했습니다.',
        ),
        img='images/listening_n4/n4_q11.jpg',
    ),
    dict(
        sec='2',
        title='野菜スープを美味しく作るポイント',
        situation='料理教室で女の先生が野菜スープの作り方を説明しています。スープを美味しく仕上げる一番のポイントは何ですか。',
        prompt='スープを美味しく仕上げる一番のポイントは何ですか。',
        dialogue=[
            ('f', '今日は旬の野菜をたっぷり使ったミネストローネを作ります。玉ねぎや人参、セロリをオリーブオイルで炒めますが、ここが一番大切です。強火で一気に炒めると焦げてしまいますので、弱火でじっくり10分間炒めて野菜の甘みを引き出してください。野菜がしんなりしてからトマトとスープを加えて煮込むと、砂糖を入れなくてもとてもコクのある美味しいスープに仕上がりますよ。'),
        ],
        choices=[
            '強火で1分間で野菜を炒めること',
            '砂糖をスプーン3杯入れること',
            '野菜を弱火でじっくり炒めて甘みを引き出すこと',
            '野菜を炒めずに生のまま水に入れて煮ること',
        ],
        answer=2,
        exp=dict(
            ja='先生は「ここが一番大切です。強火で一気に炒めると焦げてしまいますので、弱火でじっくり10分間炒めて野菜の甘みを引き出してください」と説明しています。',
            en='The instructor emphasizes that the most important point is to sauté the vegetables slowly over low heat for 10 minutes to draw out their natural sweetness.',
            zh='老師強調最重要的秘訣是用小火耐心慢炒10分鐘，將蔬菜本身的甜味充分引出來。',
            ko='선생님은 센 불로 볶으면 타버리므로 약불에서 은근히 10분간 볶아 채소의 단맛을 끌어내는 것이 가장 중요하다고 설명했습니다.',
        ),
        img='images/listening_n4/n4_q12.jpg',
    ),
    dict(
        sec='2',
        title='レポート提出締め切りが延びた理由',
        situation='日本語学校で男の留学生と女の先生が話しています。レポートの提出締め切りが変更された理由は何ですか。',
        prompt='レポートの提出締め切りが変更された理由は何ですか。',
        dialogue=[
            ('m', '先生、今週金曜日締切の日本文化のレポートですが、締め切りが来週の月曜日に延びたと聞きました。本当ですか？'),
            ('f', 'ええ、本当ですよ。今週の木曜日と金曜日に学校のパソコン室のシステム改修工事が入ることになって、学生の皆さんが学内でパソコンやプリンターを使えなくなってしまったんです。'),
            ('m', 'そうだったんですね！自宅にプリンターがないので助かりました。'),
            ('f', '月曜日の授業の最初に提出してくださいね。'),
        ],
        choices=[
            'パソコン室のシステム改修で学内の機器が使えなくなったから',
            '先生が急に出張することになったから',
            '学生全員が宿題を忘れてきたから',
            '台風で学校が休校になったから',
        ],
        answer=0,
        exp=dict(
            ja='先生から「今週の木曜日と金曜日に学校のパソコン室のシステム改修工事が入ることになって、学生の皆さんが学内でパソコンやプリンターを使えなくなってしまったんです」と説明されています。',
            en='The teacher explains that system renovation work in the school computer room on Thursday and Friday made the school computers and printers unavailable to students.',
            zh='老師說明因為週四和週五學校電腦室進行系統改修工程，導致學生無法在校內使用電腦和印表機，因此延長了繳交期限。',
            ko='목요일과 금요일에 학교 컴퓨터실 시스템 개수 공사가 있어서 학생들이 교내에서 컴퓨터와 프린터를 사용할 수 없게 되었기 때문입니다.',
        ),
        img='images/listening_n4/n4_q13.jpg',
    ),
    dict(
        sec='2',
        title='図書館で雑誌の最新号が借りられない理由',
        situation='図書館で男の人と女の司書が話しています。雑誌の最新号が貸出できない理由は何ですか。',
        prompt='雑誌の最新号が貸出できない理由は何ですか。',
        dialogue=[
            ('m', 'すみません、この料理雑誌の今月出た最新号を借りたいのですが、自動貸出機でエラーになってしまって。'),
            ('f', '申し訳ございません。当館では、雑誌の最新号は館内閲覧のみとなっておりまして、貸出ができない規則になっております。'),
            ('m', 'そうなんですか。どうして最新号は借りられないんですか。'),
            ('f', '最新号は読みたい方が非常に多いため、多くの方に館内で公平にご覧いただくためなんです。来月号が発売されましたら、この号もお貸し出しできるようになりますよ。'),
            ('m', 'なるほど、わかりました。'),
        ],
        choices=[
            '雑誌に汚れや破れがあるから',
            '多くの利用者が館内で公平に読めるようにするため',
            '本棚の修理工事を行っているから',
            '雑誌の値段が高すぎるから',
        ],
        answer=1,
        exp=dict(
            ja='司書は最新号が借りられない理由について、「最新号は読みたい方が非常に多いため、多くの方に館内で公平にご覧いただくためなんです」と説明しています。',
            en='The librarian explains that because very many people want to read the latest issue, it is kept for in-library browsing only so that many visitors can read it fairly.',
            zh='圖書館員解釋因為想看最新一期雜誌的人非常多，為了讓更多讀者能在館內公平閱覽，最新一期僅限館內閱讀。',
            ko='사서는 최신호를 읽고 싶어 하는 이용자가 매우 많아서 많은 사람이 관내에서 공평하게 볼 수 있도록 하기 위해서라고 설명했습니다.',
        ),
        img='images/listening_n4/n4_q14.jpg',
    ),
    dict(
        sec='2',
        title='運動前にストレッチをする一番の目的',
        situation='スポーツクラブで女の人と男のトレーナーが話しています。トレーナーが運動前のストレッチを勧める一番の目的は何ですか。',
        prompt='トレーナーが運動前のストレッチを勧める一番の目的は何ですか。',
        dialogue=[
            ('f', '先生、走る前に軽くストレッチをした方がいいですか。'),
            ('m', 'はい、絶対にしてください。運動前に筋肉や関節をゆっくり伸ばして温めることで、筋肉の柔軟性が高まり、肉離れや捻挫などの怪我を予防することができるんです。体をほぐさずにいきなり走ると、体にも負担がかかりますからね。'),
            ('f', 'わかりました。怪我をしないように、まずしっかりストレッチします！'),
        ],
        choices=[
            'ウェアの着心地を確かめるため',
            '身長を伸ばすため',
            '柔軟性を高めて肉離れなどの怪我を予防するため',
            '眠気を誘ってリラックスするため',
        ],
        answer=2,
        exp=dict(
            ja='トレーナーは「運動前に筋肉や関節をゆっくり伸ばして温めることで、筋肉の柔軟性が高まり、肉離れや捻挫などの怪我を予防することができるんです」と説明しています。',
            en='The trainer explains that stretching warms up muscles and joints, increasing flexibility and preventing injuries such as muscle strains and sprains.',
            zh='教練說明運動前慢慢伸展溫暖肌肉與關節，能提高肌肉柔軟度，預防肌肉拉傷或扭傷等運動傷害。',
            ko='트레이너는 운동 전에 근육과 관절을 천천히 늘려 따뜻하게 함으로써 유연성을 높이고 근육 파열이나 염좌 같은 부상을 예방할 수 있다고 설명했습니다.',
        ),
        img='images/listening_n4/n4_q15.jpg',
    ),

    # ==================== 問題3 発話表現 (5問: Q16〜Q20, 3択) ====================
    dict(
        sec='3',
        title='レストランでお会計を頼む表現',
        situation='レストランで食事が終わりました。お会計をしたいとき、店員に何と言いますか。',
        prompt='レストランで食事が終わりました。お会計をしたいとき、店員に何と言いますか。',
        choices=[
            'すみません、お会計をお願いします。',
            'ごちそうを食べてください。',
            'お釣りを払わせてください。',
        ],
        answer=0,
        exp=dict(
            ja='飲食店で食事を終えて支払いを頼むときは、「すみません、お会計をお願いします」と言うのが自然で丁寧な表現です。',
            en='When asking for the bill after finishing a meal at a restaurant, "Sumimasen, o-kaikei o onegaishimasu" (Excuse me, the check please) is the standard polite expression.',
            zh='在餐廳用完餐想結帳時，說「すみません、お会計をお願いします」（不好意思，麻煩結帳）是最自然禮貌的說法。',
            ko='식당에서 식사를 마치고 계산을 요청할 때는 "すみません、お会計をお願いします(저기요, 계산 부탁합니다)"라고 말하는 것이 자연스럽습니다.',
        ),
        img='images/listening_n4/n4_q16.jpg',
    ),
    dict(
        sec='3',
        title='電車でお年寄りに席を譲る表現',
        situation='電車でお年寄りが乗ってきました。席を譲りたいとき、何と言いますか。',
        prompt='電車でお年寄りが乗ってきました。席を譲りたいとき、何と言いますか。',
        choices=[
            'ここに座ってもいいですか。',
            'よかったら、どうぞお座りください。',
            'そこに座ってあげますよ。',
        ],
        answer=1,
        exp=dict(
            ja='電車やバスで席を譲るときは、相手を敬って「よかったら、どうぞお座りください」と声をかけるのが丁寧で適切です。',
            en='When offering your seat to an elderly person on a train, "Yokattara, douzo o-suwari kudasai" (Please have a seat if you\'d like) is polite and considerate.',
            zh='在電車上想讓座給年長者時，禮貌且體貼的說法是「よかったら、どうぞお座りください」（如果不介意的話，請坐）。',
            ko='전철에서 어르신께 자리를 양보할 때는 "よかったら、どうぞお座りください(괜찮으시다면 이쪽에 앉으세요)"라고 정중하게 권하는 것이 적절합니다.',
        ),
        img='images/listening_n4/n4_q17.jpg',
    ),
    dict(
        sec='3',
        title='友達の家に入るときの挨拶',
        situation='友達の家を訪ねて、部屋に上がるとき何と言いますか。',
        prompt='友達の家を訪ねて、部屋に上がるとき何と言いますか。',
        choices=[
            'おかえりなさい。',
            'いってきます。',
            'お邪魔します。',
        ],
        answer=2,
        exp=dict(
            ja='よそのお宅や友達の家を訪問して中に入るときは、「お邪魔します」と挨拶するのが日本の基本的なマナーです。',
            en='When stepping into someone else\'s home as a guest, "O-jama shimasu" (Excuse me for intruding / Thank you for having me) is the standard Japanese greeting.',
            zh='拜訪朋友或他人家裡、要進屋時，說「お邪魔します」（打擾了）是日本基本的禮貌問候。',
            ko='친구나 다른 사람의 집을 방문하여 안으로 들어갈 때는 "お邪魔します(실례합니다)"라고 인사하는 것이 기본 예절입니다.',
        ),
        img='images/listening_n4/n4_q18.jpg',
    ),
    dict(
        sec='3',
        title='忙しそうな同僚に手伝いを申し出る表現',
        situation='同僚が忙しそうに資料をコピーしています。手伝いを申し出るとき何と言いますか。',
        prompt='同僚が忙しそうに資料をコピーしています。手伝いを申し出るとき何と言いますか。',
        choices=[
            '早く手伝ってもらえませんか。',
            '大変そうですね。何か手伝いましょうか。',
            '一人でコピーするべきですよ。',
        ],
        answer=1,
        exp=dict(
            ja='自分が相手の仕事を手伝うと申し出るときは、「〜ましょうか」を使って「大変そうですね。何か手伝いましょうか」と声をかけます。「〜てもらえませんか」は相手に依頼する表現なので逆になります。',
            en='When offering to help a busy colleague, use the "-mashou ka" form: "Taihen sou desu ne. Nanika tetsudaimashou ka" (That looks busy. Shall I help you with something?).',
            zh='主動向忙碌的同事提出幫忙時，應使用「〜ましょうか」句型說「大変そうですね。何か手伝いましょうか」（看起來很忙呢，需要我幫忙什麼嗎？）。',
            ko='바빠 보이는 동료에게 도움을 제안할 때는 "~ましょうか"를 사용하여 "大変そうですね。何か手伝いましょうか(힘들어 보이네요. 뭔가 도와드릴까요?)"라고 말합니다.',
        ),
        img='images/listening_n4/n4_q19.jpg',
    ),
    dict(
        sec='3',
        title='通行人に駅の場所を尋ねる表現',
        situation='道で通行人に駅の場所を尋ねたいです。何と言いますか。',
        prompt='道で通行人に駅の場所を尋ねたいです。何と言いますか。',
        choices=[
            'すみません、駅へはどの道を行けばいいですか。',
            '駅を案内してあげましょうか。',
            '駅に行ってもかまいませんか。',
        ],
        answer=0,
        exp=dict(
            ja='道で知らない人に駅への行き方を尋ねるときは、「すみません、駅へはどの道を行けばいいですか」と聞くのが自然で丁寧です。',
            en='When asking a passerby for directions to the station, "Sumimasen, eki e wa dono michi o ikeba ii desu ka" (Excuse me, which way should I go to get to the station?) is natural and polite.',
            zh='在路上向行人詢問去車站的路線時，說「すみません、駅へはどの道を行けばいいですか」（不好意思，請問去車站要走哪條路？）最自然有禮。',
            ko='길에서 행인에게 역으로 가는 길을 물을 때는 "すみません、駅へはどの道を行けばいいですか(실례합니다, 역에는 어느 길로 가면 됩니까?)"라고 묻는 것이 자연스럽습니다.',
        ),
        img='images/listening_n4/n4_q20.jpg',
    ),

    # ==================== 問題4 即時応答 (8問: Q21〜Q28, 3択) ====================
    dict(
        sec='4',
        title='週末の紅葉狩りへの誘い',
        situation='週末、一緒に京都へ紅葉を見に行きませんか。',
        prompt='週末、一緒に京都へ紅葉を見に行きませんか。',
        choices=[
            '京都へは行ったことがありません。',
            '昨日は紅葉がきれいでしたね。',
            'いいですね！ぜひ行きましょう。',
        ],
        answer=2,
        exp=dict(
            ja='「〜ませんか」というお出かけの誘いに対して、喜んで応じる「いいですね！ぜひ行きましょう」が最も自然な返答です。',
            en='In response to an invitation ("Won\'t you go see the autumn leaves in Kyoto with me this weekend?"), enthusiastically accepting with "Sounds great! Let\'s definitely go" is most natural.',
            zh='面對「週末要不要一起去京都看紅葉？」的邀約，欣然答應的「いいですね！ぜひ行きましょう」（太好了！我們一定要去）最為自然。',
            ko='"주말에 함께 교토에 단풍 보러 가지 않겠습니까?"라는 권유에 기쁘게 수락하는 "いいですね！ぜひ行きましょう(좋네요! 꼭 갑시다)"가 가장 자연스럽습니다.',
        ),
        img='images/listening_n4/n4_q21.jpg',
    ),
    dict(
        sec='4',
        title='ペンを貸してほしいという依頼への返答',
        situation='すみません、ちょっとそのペンを貸していただけませんか。',
        prompt='すみません、ちょっとそのペンを貸していただけませんか。',
        choices=[
            'ええ、どうぞ使ってください。',
            'はい、今からペンを借りますね。',
            'いいえ、ペンは書きませんでした。',
        ],
        answer=0,
        exp=dict(
            ja='「ペンを貸していただけませんか」という丁寧な依頼に対し、快く貸してあげる「ええ、どうぞ使ってください」が正解です。',
            en='When politely asked "Could you lend me that pen for a moment?", replying "Sure, please go ahead and use it" is appropriate.',
            zh='面對「不好意思，可以借我一下那支筆嗎？」的禮貌請求，爽快借出的「ええ、どうぞ使ってください」（好的，請用）是正確回應。',
            ko='"죄송합니다만 잠깐 그 펜 좀 빌려주시겠습니까?"라는 정중한 부탁에 흔쾌히 빌려주는 "ええ、どうぞ使ってください(네, 어서 쓰세요)"가 정답입니다.',
        ),
        img='images/listening_n4/n4_q22.jpg',
    ),
    dict(
        sec='4',
        title='寒くなった天気への共感',
        situation='今朝はずいぶん寒くなりましたね。',
        prompt='今朝はずいぶん寒くなりましたね。',
        choices=[
            'はい、とても暑くて大変ですね。',
            '本当に。厚いコートを着てきて正解でした。',
            'ええ、寒いのは来週からですよ。',
        ],
        answer=1,
        exp=dict(
            ja='「今朝はずいぶん寒くなりましたね」という呼びかけに対し、寒さに共感して「本当に。厚いコートを着てきて正解でした」と返すのが自然です。',
            en='When someone remarks "It has gotten quite cold this morning, hasn\'t it?", agreeing with "Really. Wearing a thick coat was the right choice" is natural.',
            zh='面對「今天早上變得好冷呢」的寒暄，表示同感並回答「真的。穿厚大衣出門穿對了」最為自然。',
            ko='"오늘 아침은 꽤 추워졌네요"라는 말에 공감하며 "정말요. 두꺼운 코트를 입고 오길 잘했어요"라고 답하는 것이 자연스럽습니다.',
        ),
        img='images/listening_n4/n4_q23.jpg',
    ),
    dict(
        sec='4',
        title='試験前の応援に対する返答',
        situation='明日の日本語のテスト、頑張ってくださいね！',
        prompt='明日の日本語のテスト、頑張ってくださいね！',
        choices=[
            '頑張らなくても大丈夫ですよ。',
            'テストは昨日終わりましたよ。',
            'ありがとうございます、全力で頑張ります！',
        ],
        answer=2,
        exp=dict(
            ja='明日のテストに向けた応援の言葉に対し、感謝と意気込みを伝える「ありがとうございます、全力で頑張ります！」が適切な応答です。',
            en='When someone cheers you on for tomorrow\'s Japanese test, thanking them and expressing determination ("Thank you, I\'ll do my very best!") is appropriate.',
            zh='面對他人為明天的日語考試加油打氣，表達感謝與決心的「謝謝您，我會全力以赴的！」是最合適的回應。',
            ko='내일 일본어 시험 잘 보라는 응원의 말에 감사와 다짐을 전하는 "감사합니다, 전력을 다해 열심히 하겠습니다!"가 적절합니다.',
        ),
        img='images/listening_n4/n4_q24.jpg',
    ),
    dict(
        sec='4',
        title='お茶のおかわりを勧められたときの返答',
        situation='お茶のおかわりはいかがですか。',
        prompt='お茶のおかわりはいかがですか。',
        choices=[
            'ありがとうございます。では、もう一杯いただきます。',
            'はい、どうぞお茶を飲んでください。',
            'いいえ、まだ一滴も飲んでいません。',
        ],
        answer=0,
        exp=dict(
            ja='ホストから「お茶のおかわりはいかがですか」と勧められた際、お礼を言って受ける「ありがとうございます。では、もう一杯いただきます」が自然で丁寧です。',
            en='When offered a refill of tea ("Would you like another cup of tea?"), politely accepting with "Thank you. I\'ll have one more cup, then" is natural.',
            zh='當主人詢問「要不要再續一杯茶？」時，禮貌道謝並接受的「謝謝您，那我再來一杯」最自然得體。',
            ko='"차 한 잔 더 드시겠습니까?"라는 권유에 감사히 받는 "감사합니다. 그럼 한 잔 더 마시겠습니다"가 자연스럽고 정중합니다.',
        ),
        img='images/listening_n4/n4_q25.jpg',
    ),
    dict(
        sec='4',
        title='企画書のチェック依頼に対する上司の返答',
        situation='課長、来月の企画書のチェックをお願いしてもよろしいでしょうか。',
        prompt='課長、来月の企画書のチェックをお願いしてもよろしいでしょうか。',
        choices=[
            'はい、私が課長にお願いしますね。',
            'うん、机の上に置いておいて。後で見ておくよ。',
            'ええ、企画書はまだ書き始めていません。',
        ],
        answer=1,
        exp=dict(
            ja='部下からの「企画書のチェックをお願いしてもよろしいでしょうか」という依頼に対し、上司が引き受けて「うん、机の上に置いておいて。後で見ておくよ」と答えるのが自然です。',
            en='When a subordinate politely asks the section manager to review a proposal, the manager naturally replies, "Sure, leave it on my desk. I\'ll look it over later."',
            zh='面對部下請求「課長，可以請您幫我確認下個月的企劃書嗎？」，課長回答「嗯，先放在桌上，我晚點看」最為自然。',
            ko='부하 직원이 과장에게 기획서 검토를 부탁했을 때 과장이 "응, 책상 위에 올려두어. 나중에 봐 둘게"라고 답하는 것이 자연스럽습니다.',
        ),
        img='images/listening_n4/n4_q26.jpg',
    ),
    dict(
        sec='4',
        title='雨が降ってきたときの傘の確認',
        situation='外、雨が降ってきましたね。傘は持っていますか。',
        prompt='外、雨が降ってきましたね。傘は持っていますか。',
        choices=[
            'はい、かばんに折りたたみ傘が入っているので大丈夫です。',
            'ええ、今日は一日中いい天気でよかったですね。',
            'いいえ、さっき傘を差して帰りました。',
        ],
        answer=0,
        exp=dict(
            ja='雨が降ってきたことを心配して「傘は持っていますか」と聞かれたのに対し、「はい、かばんに折りたたみ傘が入っているので大丈夫です」と答えるのが自然です。',
            en='When asked "It started raining outside. Do you have an umbrella?", replying "Yes, I have a folding umbrella in my bag, so I\'m fine" is natural.',
            zh='當對方關心「外面開始下雨了呢，你有帶傘嗎？」時，回答「有，包包裡有折疊傘所以沒問題」最為自然。',
            ko='밖에 비가 오기 시작했다며 우산이 있는지 묻는 말에 "네, 가방에 접이식 우산이 들어 있어서 괜찮습니다"라고 답하는 것이 자연스럽습니다.',
        ),
        img='images/listening_n4/n4_q27.jpg',
    ),
    dict(
        sec='4',
        title='退勤時の労いの挨拶への返答',
        situation='お仕事、遅くまでお疲れ様でした。',
        prompt='お仕事、遅くまでお疲れ様でした。',
        choices=[
            'どういたしまして、いつでも聞いてください。',
            'はい、おはようございます。今日も頑張りましょう。',
            'お疲れ様でした！お先に失礼します。',
        ],
        answer=2,
        exp=dict(
            ja='職場で帰るときに「お疲れ様でした」と声をかけられたら、「お疲れ様でした！お先に失礼します」と挨拶を返すのが日本の職場の基本マナーです。',
            en='When a colleague says "Good work staying late today" as you leave work, replying "Thank you, good work to you too! Pardon me for leaving first" is standard workplace etiquette.',
            zh='下班時聽到同事慰勞「工作到這麼晚，辛苦了」，回答「您也辛苦了！我先告辭了」是日本職場的基本禮儀。',
            ko='퇴근할 때 동료가 "늦게까지 수고하셨습니다"라고 인사하면 "수고하셨습니다! 먼저 실례하겠습니다"라고 답하는 것이 직장 예절입니다.',
        ),
        img='images/listening_n4/n4_q28.jpg',
    ),
]


# ---------------------------------------------------------------- TTS text helper
_EXPL = re.compile(r'\{([^{}|]+)\|([^{}|]+)\}')
RISKY = [
    ('来られ', 'こられ'), ('来ます', 'きます'), ('来ました', 'きました'), ('来ませ', 'きませ'), ('来て', 'きて'),
    ('持ってこなければ', 'もってこなければ'), ('持ってきます', 'もってきます'), ('持っていく', 'もっていく'),
    ('午後', 'ごご'), ('午前', 'ごぜん'), ('この後', 'このあと'), ('その後', 'そのあと'), ('後で', 'あとで'),
    ('終わった後で', 'おわったあとで'),
    ('今日', 'きょう'), ('明日', 'あした'), ('昨日', 'きのう'), ('大人', 'おとな'), ('何人', 'なんにん'),
    ('一日中', 'いちにちじゅう'), ('一日', 'いちにち'), ('今朝', 'けさ'), ('今年', 'ことし'), ('去年', 'きょねん'),
    ('来週', 'らいしゅう'), ('来月', 'らいげつ'), ('来年', 'らいねん'), ('先週', 'せんしゅう'), ('今週', 'こんしゅう'),
    ('今月', 'こんげつ'), ('先月', 'せんげつ'), ('上手', 'じょうず'), ('下手', 'へた'), ('毎朝', 'まいあさ'), ('毎晩', 'まいばん'),
    ('来ない', 'こない'), ('来なけれ', 'こなけれ'), ('来なかった', 'こなかった'), ('一人', 'ひとり'), ('二人', 'ふたり'),
    ('何曜日', 'なんようび'), ('何時間', 'なんじかん'), ('何時', 'なんじ'), ('何を', 'なにを'), ('何が', 'なにが'),
    ('何も', 'なにも'), ('何に', 'なにに'), ('何か', 'なにか'), ('何と', 'なんと'), ('何から', 'なにから'),
    ('何の', 'なんの'), ('何です', 'なんです'), ('何だ', 'なんだ'), ('何分', 'なんぷん'), ('何枚', 'なんまい'),
    ('何本', 'なんぼん'), ('何個', 'なんこ'), ('何階', 'なんがい'), ('何部', 'なんぶ'),
    ('15部', 'じゅうごぶ'), ('2部', 'にぶ'), ('2名', 'にめい'), ('17名', 'じゅうななめい'),
    ('38度', 'さんじゅうはちど'), ('14時半', 'じゅうよじはん'), ('14時', 'じゅうよじ'),
    ('10分間', 'じゅっぷんかん'), ('1分間', 'いっぷんかん'), ('10分後', 'じゅっぷんご'), ('30分前', 'さんじゅっぷんまえ'),
    ('1枚', 'いちまい'), ('4番ホーム', 'よんばんホーム'), ('3番ホーム', 'さんばんホーム'),
    ('今出しますか', 'いまだしますか'),
    ('をした方がいい', 'をしたほうがいい'), ('した方がいい', 'したほうがいい'),
    ('一番', 'いちばん'), ('お冷', 'おひや'), ('裏面', 'うらめん'), ('海日和', 'うみびより'),
    ('前日', 'ぜんじつ'), ('高熱', 'こうねつ'), ('看病', 'かんびょう'), ('在宅勤務', 'ざいたくきんむ'),
    ('肩こり', 'かたこり'), ('決め手', 'きめて'), ('吸引力', 'きゅういんりょく'),
    ('強火', 'つよび'), ('弱火', 'よわび'), ('生中継', 'なまちゅうけい'),
    ('最新号', 'さいしんごう'), ('来月号', 'らいげつごう'), ('この号', 'このごう'),
    ('館内閲覧', 'かんないえつらん'), ('お貸し出し', 'おかしだし'), ('自動貸出機', 'じどうかしだしき'),
    ('貸出', 'かしだし'), ('肉離れ', 'にくばなれ'), ('捻挫', 'ねんざ'),
    ('お年寄り', 'おとしより'), ('通行人', 'つうこうにん'), ('紅葉', 'もみじ'),
    ('もう一杯', 'もういっぱい'), ('一滴', 'いってき'), ('お先に', 'おさきに'),
]

def tts_text(src):
    t = _EXPL.sub(lambda m: m.group(2), src)
    t = re.sub(r'<[^>]+>', '', t)
    for a, b in RISKY:
        t = t.replace(a, b)
    return t.replace('。。', '。').strip()

def speech_segments(n, it):
    """[(voice_name, text, pause_ms, role)]"""
    V = {'n': 'ja-JP-Neural2-B', 'f': 'ja-JP-Neural2-B', 'm': 'ja-JP-Neural2-C'}
    head = f"だい{num_reading(n)}もん。"
    sec = it['sec']
    seg = []
    if sec in ('1', '2'):
        intro = head + tts_text(it['situation'])
        seg.append(('n', intro, 1000))
        for who, line in it['dialogue']:
            seg.append((who, tts_text(line), 850))
        seg.append(('n', '質問。' + tts_text(it['prompt']), 1800))
    elif sec == '3':
        pr = tts_text(it['prompt'])
        seg.append(('n', head + pr, 1200))
        for i, c in enumerate(it['choices']):
            seg.append(('n', f"{['いち','に','さん'][i]}ばん。{tts_text(c)}", 1500))
        seg.append(('n', '質問。' + pr, 1800))
    else:
        # 問題4 即時応答: alternate male/female speakers for prompt & choices
        asker = 'f' if n % 2 == 0 else 'm'
        replier = 'm' if asker == 'f' else 'f'
        seg.append(('n', head, 600))
        seg.append((asker, tts_text(it['prompt']), 1200))
        for i, c in enumerate(it['choices']):
            seg.append((replier, f"{['いち','に','さん'][i]}ばん。{tts_text(c)}", 1500))
        seg.append(('n', '質問。発話を聞いて、最も適した返答を選んでください。', 1800))
    return [(V[v], t, p, v) for v, t, p in seg]


def build():
    errs = []
    out = []
    # Check 4-choice answer distribution in sec1 (8 Qs) and sec2 (7 Qs)
    # Current answers:
    # sec1: 0, 1, 2, 3, 2, 1, 3, 0 -> {0:2, 1:2, 2:2, 3:2} (perfectly balanced!)
    # sec2: 1, 3, 0, 2, 0, 1, 2 -> {0:2, 1:2, 2:2, 3:1} (perfectly balanced!)
    # sec3 (3-choice, 5 Qs): 0, 1, 2, 1, 0 -> {0:2, 1:2, 2:1} (balanced!)
    # sec4 (3-choice, 8 Qs): 2, 0, 1, 2, 0, 1, 0, 2 -> {0:3, 1:2, 2:3} (balanced!)

    for n, it in enumerate(ITEMS, 1):
        sec = it['sec']
        # Check no "あ、"
        all_lines = [it['situation'], it['prompt']] + it['choices'] + [l for _, l in it.get('dialogue', [])]
        for l in all_lines:
            if re.search(r'(?:^|[。！？\s「])あ、', l):
                errs.append(f'Q{n}: contains forbidden "あ、": {l}')
        allt = ''.join(all_lines) + it['exp']['ja']
        sh = sensitive_hits(allt)
        if sh:
            errs.append(f'Q{n}: sensitive hits {sh}')

        prompt_ruby = RR(it['prompt'])
        choices_ruby = [RR(c) for c in it['choices']]
        a_num = it['answer'] + 1
        pre = {
            'ja': RR(f'正解は{a_num}番です。'),
            'en': f'The correct answer is Choice {a_num}. ',
            'zh': f'正確答案是選項{a_num}。',
            'ko': f'정답은 {a_num}번입니다. ',
        }
        exja = pre['ja'] + RR(it['exp']['ja'])

        # Build script_html
        if sec in ('1', '2'):
            dlg_html = f'<p class="text-xs font-bold text-slate-400 mb-1">{RR(f"第{n}問。")}{RR(it["situation"])}</p>'
            for who, line in it['dialogue']:
                lab = '女の人' if who == 'f' else '男の人'
                dlg_html += f'<p><span class="font-bold text-[#1995AD]">{RR(lab)}：</span>{RR(line)}</p>'
            dlg_html += f'<p class="text-xs font-bold text-[#B8596E] mt-2">{RR("質問")}：{prompt_ruby}</p>'
        elif sec == '3':
            dlg_html = f'<p class="text-xs font-bold text-slate-400 mb-1">{RR(f"第{n}問。")}{prompt_ruby}</p>'
            for i, c in enumerate(choices_ruby):
                dlg_html += f'<p><span class="font-bold text-[#1995AD]">{i+1}{RR("番")}：</span>{c}</p>'
            dlg_html += f'<p class="text-xs font-bold text-[#B8596E] mt-2">{RR("質問")}：{prompt_ruby}</p>'
        else:
            asker_lab = '女の人' if n % 2 == 0 else '男の人'
            dlg_html = f'<p class="text-xs font-bold text-slate-400 mb-1">{RR(f"第{n}問。")}</p>'
            dlg_html += f'<p><span class="font-bold text-[#1995AD]">{RR(asker_lab)}：</span>「{prompt_ruby}」</p>'
            for i, c in enumerate(choices_ruby):
                dlg_html += f'<p><span class="font-bold text-[#1995AD]">{i+1}{RR("番")}：</span>{c}</p>'
            dlg_html += f'<p class="text-xs font-bold text-[#B8596E] mt-2">{RR("質問")}：{RR("発話を聞いて、最も適した返答を選んでください。")}</p>'

        script_html = f'<div class="space-y-2 text-sm leading-relaxed">{dlg_html}</div>'

        for k, h in (('prompt', prompt_ruby), ('choices', ''.join(choices_ruby)), ('exp', exja), ('script', script_html)):
            leak = lint_ruby(h)
            if leak:
                errs.append(f'Q{n}: ruby leak in {k}: {"".join(leak)}')

        segs = speech_segments(n, it)
        speech_audio_text = '\n\n'.join(t for _, t, _, _ in segs)

        out.append({
            'id': f'n4_lis_q{n}',
            'q_num': n,
            'section_id': f'sec{sec}',
            'section': SECS[sec],
            'section_name': SECS[sec],
            'title': it['title'],
            'situation': P(it['situation']),
            'has_illustration': True,
            'illustration_url': it['img'],
            'prompt': P(it['prompt']),
            'prompt_ruby': prompt_ruby,
            'speech_audio_text': speech_audio_text,
            'audio_file': f'audio/listening/n4_q{n}.mp3',
            'choices': choices_ruby,
            'choices_ruby': choices_ruby,
            'answer': it['answer'],
            'explanation': {
                'ja': exja,
                'en': pre['en'] + it['exp']['en'],
                'zh': pre['zh'] + it['exp']['zh'],
                'ko': pre['ko'] + it['exp']['ko'],
            },
            'script_html': script_html,
            '_segments': [(v, t, p) for v, t, p, _ in segs],
        })

    if errs:
        print('ERRORS FOUND:')
        for e in errs:
            print(' -', e)
        sys.exit(1)

    for s in ('1', '2', '3', '4'):
        ans = [q['answer'] for q in out if q['section_id'] == f'sec{s}']
        runs = [i + 1 for i in range(2, len(ans)) if ans[i] == ans[i-1] == ans[i-2]]
        print(f'sec{s}: {len(ans)} Qs, dist={dict(sorted(collections.Counter(ans).items()))}, 3-runs={runs}')
        assert not runs, f'3-run in sec{s}'

    pub = [{k: v for k, v in q.items() if not k.startswith('_')} for q in out]
    data = {
        'test_id': 'jlpt_n4_listening_test_01',
        'title': 'JLPT N4 聴解実戦模試 第1回',
        'level': 'N4',
        'total_questions': len(pub),
        'sections': [
            {'section_id': 'sec1', 'title': '問題1 課題理解', 'count': 8, 'desc': '質問を聞いて、次に何をすべきかを正確に聞き取る問題です。'},
            {'section_id': 'sec2', 'title': '問題2 ポイント理解', 'count': 7, 'desc': '質問を聞いた後、選択肢を読む時間があります。ポイントを聞き取ります。'},
            {'section_id': 'sec3', 'title': '問題3 発話表現', 'count': 5, 'desc': '場面に合わせてどのような表現を使うべきかを選ぶ問題です（3択）。'},
            {'section_id': 'sec4', 'title': '問題4 即時応答', 'count': 8, 'desc': '短い問いかけに対して、最も自然な返答を瞬時に選ぶ問題です（3択）。'},
        ],
        'questions': pub,
    }

    js_str = '// JLPT N4 Listening Comprehension Data (28 Questions, Multi-Speaker Audio & 4:3 Illustrations)\n'
    js_str += 'window.JLPT_N4_LISTENING_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n'
    for dst_rel in ('database/jlpt_n4_listening_data.js', 'public/database/jlpt_n4_listening_data.js'):
        p = os.path.join(REPO, dst_rel)
        if os.path.exists(os.path.dirname(p)):
            with open(p, 'w', encoding='utf-8') as f:
                f.write(js_str)
    print(f'Successfully wrote {len(pub)} N4 listening questions to database/jlpt_n4_listening_data.js')
    return out


def synth_all(out):
    os.environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS', os.path.join(REPO, 'secrets/google_tts_key.json'))
    from google.cloud import texttospeech
    cl = texttospeech.TextToSpeechClient()
    only = set(int(x) for x in sys.argv[sys.argv.index('--only') + 1:]) if '--only' in sys.argv else set()

    def synth(text, voice, ssml=False):
        inp = texttospeech.SynthesisInput(ssml=text) if ssml else texttospeech.SynthesisInput(text=text)
        r = cl.synthesize_speech(
            input=inp,
            voice=texttospeech.VoiceSelectionParams(language_code='ja-JP', name=voice),
            audio_config=texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3, speaking_rate=0.93)
        )
        return r.audio_content

    total_chars = 0
    for q in out:
        n = q['q_num']
        if only and n not in only:
            continue
        segs = q['_segments']
        buf = bytearray()
        for voice, text, pause in segs:
            buf += synth(text, voice)
            total_chars += len(text)
            if pause:
                buf += synth(f'<speak><break time="{pause}ms"/></speak>', voice, ssml=True)
        for d in (
            os.path.join(REPO, 'audio/listening', f'n4_q{n}.mp3'),
            os.path.join(REPO, 'public/audio/listening', f'n4_q{n}.mp3'),
        ):
            os.makedirs(os.path.dirname(d), exist_ok=True)
            with open(d, 'wb') as f:
                f.write(buf)
        print(f'Synthesized n4_q{n}.mp3 ({len(buf)} bytes)')
    print(f'Total synthesized characters: {total_chars}')


if __name__ == '__main__':
    out = build()
    if '--audio' in sys.argv:
        synth_all(out)
