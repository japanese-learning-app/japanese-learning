#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive flashcard auditor and patcher for Japanese Learning platform.
Fixes all fragmented, bizarre, rude, or machine-generated sentences in:
1. database/class_vocab_data.js & public/database/class_vocab_data.js
2. js/data.js & public/js/data.js
"""

import json
import re

print("Starting master flashcard repair...")

# ==============================================================================
# PART 1: FIX INITIAL_VOCAB_DATA (1018 cards)
# ==============================================================================
with open('js/data.js', 'r', encoding='utf-8') as f:
    init_text = f.read()

s_init = init_text.find('window.INITIAL_VOCAB_DATA =') + len('window.INITIAL_VOCAB_DATA =')
e_init = init_text.find('window.SECTIONS_DATA =')
init_prefix = init_text[:s_init]
init_sub = init_text[s_init:e_init]
init_arr_end = init_sub.rfind('];') + 1
init_cards = json.loads(init_sub[:init_arr_end].strip())
init_suffix = init_sub[init_arr_end:] + init_text[e_init:]

# 1. Fix related tags for furniture and daily items (replacing bad "日常の生活用品・筆記用具")
RELATED_FIXES = {
    'card_0070': '【名詞】机（家具・勉強や仕事の机）',
    'card_0071': '【名詞】椅子（家具・座る道具）',
    'card_0072': '【名詞】本（書籍・読書）',
    'card_0076': '【名詞】新聞（日刊紙・情報メディア）',
    'card_0077': '【名詞】スマートフォン（携帯情報端末・スマホ）',
    'card_0078': '【名詞】携帯電話（ガラケー・通話機器）',
    'card_0080': '【名詞】鞄（身の回りの手荷物・バッグ）',
    'card_0081': '【名詞】時計（腕時計・置時計など時間を知る道具）',
    'card_0082': '【名詞】電話（固定電話・通話機器）',
    'card_0083': '【名詞】パソコン（パーソナルコンピュータ・PC）',
    'card_0084': '【名詞】テレビ（家庭用電化製品・映像機器）',
    'card_0085': '【名詞】窓（部屋や建物の採光・換気用の窓）',
    'card_0086': '【名詞】ドア（部屋や玄関の出入り口・扉）',
    'card_0087': '【名詞】鍵（錠前を開閉する道具・キー）',
    'card_0088': '【名詞】辞書（言葉の意味を調べる辞典・ディクショナリー）',
    'card_0089': '【名詞】傘（雨や日差しを防ぐ雨具）',
    'card_0090': '【名詞】雑誌（週刊誌・月刊誌などの定期刊行物）',
    'card_0091': '【名詞】手帳（スケジュール帳・メモ帳）',
    'card_0092': '【名詞】靴（足に履く履物・シューズ）'
}

# 2. Fix specific unnatural sentences in INITIAL_VOCAB_DATA
SPECIFIC_INIT_FIXES = {
    # Medical cards with broken grammar "〇〇ので、病院へ行きます"
    'card_0834': {
        'example': {
            'ja': '朝からズキズキと<ruby>頭<rt>あたま</rt></ruby>が<ruby>痛<rt>いた</rt></ruby>いので、<ruby>薬<rt>くすり</rt></ruby>を<ruby>飲<rt>の</rt></ruby>んで<ruby>休<rt>やす</rt></ruby>みます。',
            'en': 'I have had a throbbing headache since morning, so I will take medicine and rest.',
            'zh_TW': '從早上開始頭就隱隱作痛，我先吃個藥休息一下。',
            'zh_CN': '从早上开始头就隐隐作痛，我先吃个药休息一下。',
            'ko': '아침부터 머리가 욱신욱신 아파서 약을 먹고 쉬려고 해요.',
            'zh_HK': '由今朝開始個頭就冤冤痛，我食粒藥休息下先。',
            'fr': "J'ai un mal de tête lancinant depuis ce matin, je vais prendre un médicament et me reposer."
        }
    },
    'card_0835': {
        'example': {
            'ja': '冷たいものを食べすぎておなかが<ruby>痛<rt>いた</rt></ruby>くなったので、温かいお茶を飲みました。',
            'en': 'I ate too many cold things and got a stomachache, so I drank warm tea.',
            'zh_TW': '因為吃了太多冰冷的東西導致肚子痛，所以喝了杯溫茶。',
            'zh_CN': '因为吃了太多冰冷的东西导致肚子痛，所以喝了杯温茶。',
            'ko': '찬 음식을 너무 많이 먹어서 배가 아파 따뜻한 차를 마셨습니다.',
            'zh_HK': '食咗太多凍嘢搞到肚痛，所以飲咗杯熱茶。',
            'fr': "J'ai mangé trop de choses froides et j'ai eu mal au ventre, alors j'ai bu du thé chaud."
        }
    },
    'card_0836': {
        'example': {
            'ja': '虫歯のせいで<ruby>歯<rt>は</rt></ruby>が<ruby>痛<rt>いた</rt></ruby>いので、今日の午後に<ruby>歯医者<rt>はいしゃ</rt></ruby>の予約を入れました。',
            'en': 'My tooth hurts because of a cavity, so I made an appointment with the dentist for this afternoon.',
            'zh_TW': '因為蛀牙牙齒很痛，我預約了今天下午看牙醫。',
            'zh_CN': '因为蛀牙牙齿很痛，我预约了今天下午看牙医。',
            'ko': '충치 때문에 이가 아파서 오늘 오후에 치과 예약을 잡았습니다.',
            'zh_HK': '因為有蛀牙搞到牙痛，我約咗今日下晝去睇牙醫。',
            'fr': "J'ai mal aux dents à cause d'une carie, alors j'ai pris rendez-vous chez le dentiste cet après-midi."
        }
    },
    'card_0848': {
        'example': {
            'ja': '夏バテ気味で<ruby>食欲<rt>しょくよく</rt></ruby>がないですが、栄養をつけるためにそうめんを食べました。',
            'en': 'I have no appetite due to summer fatigue, but I ate some somen noodles to keep my strength up.',
            'zh_TW': '有點中暑所以沒什麼食慾，但為了補充體力還是吃了點素麵。',
            'zh_CN': '有点中暑所以没什么食欲，但为了补充体力还是吃了点素面。',
            'ko': '더위를 먹어서 식욕이 없지만 기운을 차리기 위해 소면을 먹었습니다.',
            'zh_HK': '有啲熱氣同中暑冇乜胃口，但為咗有體力都食咗少少素麵。',
            'fr': "Je n'ai pas d'appétit à cause de la chaleur estivale, mais j'ai mangé des somen pour reprendre des forces."
        }
    },
    'card_0850': {
        'example': {
            'ja': '風邪の引き始めで<ruby>体<rt>からだ</rt></ruby>がだるいので、今日は早くお風呂に入って寝ます。',
            'en': 'I feel sluggish with the onset of a cold, so I will take an early bath and go to sleep today.',
            'zh_TW': '感覺有點快感冒、全身倦怠，今天打算早點洗澡睡覺。',
            'zh_CN': '感觉有点快感冒、全身倦怠，今天打算早点洗澡睡觉。',
            'ko': '감기 기운이 있어 몸이 나른하고 피곤해서 오늘은 일찍 씻고 자려고 합니다.',
            'zh_HK': '好似就嚟感冒咁個人好攰好倦，今日打算早啲沖涼瞓覺。',
            'fr': "Je me sens fébrile au début d'un rhume, alors je vais prendre un bain tôt et me coucher aujourd'hui."
        }
    },
    'card_0853': {
        'example': {
            'ja': '高熱が出て病院で検査を受けたら、<ruby>インフルエンザ<rt>いんふるえんざ</rt></ruby>だと診断されました。',
            'en': 'When I got a high fever and got tested at the hospital, I was diagnosed with the flu.',
            'zh_TW': '發高燒去醫院檢查後，被診斷出得了流感。',
            'zh_CN': '发高烧去医院检查后，被诊断出得了流感。',
            'ko': '고열이 나서 병원에서 검사를 받았더니 독감(인플루엔자)으로 진단받았습니다.',
            'zh_HK': '發高燒去醫院驗，結果證實中咗流感。',
            'fr': "Quand j'ai eu une forte fièvre et que j'ai fait un test à l'hôpital, on m'a diagnostiqué la grippe."
        }
    },
    'card_0854': {
        'example': {
            'ja': '右の下腹部が急に激しく痛むので、<ruby>盲腸<rt>もうちょう</rt></ruby>ではないかと心配です。',
            'en': 'The lower right side of my abdomen suddenly hurts intensely, so I am worried it might be appendicitis.',
            'zh_TW': '右下腹部突然劇烈疼痛，很擔心是不是盲腸炎（闌尾炎）。',
            'zh_CN': '右下腹部突然剧烈疼痛，很担心是不是阑尾炎。',
            'ko': '오른쪽 아랫배가 갑자기 심하게 아파서 맹장염이 아닌가 걱정됩니다.',
            'zh_HK': '右邊下腹突然痛得好犀利，好驚係盲腸炎。',
            'fr': "Le bas-ventre droit me fait soudain très mal, je crains que ce ne soit une appendicite."
        }
    },
    'card_0855': {
        'example': {
            'ja': '重い段ボールを持ち上げた瞬間に、<ruby>ぎっくり腰<rt>ぎっくりごし</rt></ruby>になって動けなくなりました。',
            'en': 'The moment I lifted the heavy cardboard box, I threw out my back and could not move.',
            'zh_TW': '搬起沉重紙箱的瞬間閃到了腰，痛得動彈不得。',
            'zh_CN': '搬起沉重纸箱的瞬间闪到了腰，痛得动弹不得。',
            'ko': '무거운 상자를 들어 올리는 순간 허리를 삐끗해서 움직일 수 없게 되었습니다.',
            'zh_HK': '搬起個重紙箱嗰一下即刻閃親條腰，痛到郁唔到。',
            'fr': "Au moment où j'ai soulevé le carton lourd, je me suis fait un tour de reins et je ne pouvais plus bouger."
        }
    },
    'card_0856': {
        'example': {
            'ja': '階段で足首を<ruby>ねんざ<rt>ねんざ</rt></ruby>してしまったので、氷で冷やして湿布を貼りました。',
            'en': 'I sprained my ankle on the stairs, so I iced it and applied a pain relief patch.',
            'zh_TW': '在樓梯上扭傷了腳踝，所以敷了冰塊並貼上痠痛貼布。',
            'zh_CN': '在楼梯上扭伤了脚踝，所以敷了冰块并贴上酸痛贴布。',
            'ko': '계단에서 발목을 삐어서 얼음찜질을 하고 파스를 붙였습니다.',
            'zh_HK': '喺樓梯拗柴扭親個腳眼，即刻敷冰再貼膏藥。',
            'fr': "Je me suis foulé la cheville dans les escaliers, alors j'ai mis de la glace et un patch analgésique."
        }
    },
    'card_0858': {
        'example': {
            'ja': '昨日お酒を飲みすぎて、ひどい<ruby>二日酔い<rt>ふつかよい</rt></ruby>で頭がガンガンします。',
            'en': 'I drank too much alcohol yesterday and have a terrible hangover with a pounding headache.',
            'zh_TW': '昨天喝太多酒了，宿醉得很嚴重，頭一直脹痛。',
            'zh_CN': '昨天喝太多酒了，宿醉得很严重，头一直胀痛。',
            'ko': '어제 술을 너무 많이 마셔서 숙취가 심해 머리가 욱신거립니다.',
            'zh_HK': '琴晚飲得太多酒，宿醉得好辛苦，個頭痛到就爆。',
            'fr': "J'ai trop bu hier et j'ai une terrible gueule de bois avec la tête qui martèle."
        }
    },
    # Color / taste corrections
    'card_0588': {
        'example': {
            'ja': 'わが家では<ruby>茶色い<rt>ちゃいろい</rt></ruby>トイプードルを飼っています。とても人懐っこいです。',
            'en': 'We have a brown toy poodle at home. It is very friendly.',
            'zh_TW': '我們家養了一隻褐色的貴賓狗。非常親人可愛。',
            'zh_CN': '我们家养了一只褐色的贵宾犬。非常亲人可爱。',
            'ko': '우리 집에서는 갈색 토이푸들을 키우고 있습니다. 아주 애교가 많아요.',
            'zh_HK': '我哋屋企養咗隻啡色嘅貴婦狗，好黐人好得意。',
            'fr': "Nous avons un caniche toy marron à la maison. Il est très affectueux."
        }
    },
    'card_0591': {
        'example': {
            'ja': '冬のおしゃれに合わせやすい、上品な<ruby>グレー<rt>ぐれー</rt></ruby>のウールコートを買いました。',
            'en': 'I bought an elegant gray wool coat that is easy to pair with winter outfits.',
            'zh_TW': '買了一件優雅的灰色羊毛大衣，冬天非常好搭衣服。',
            'zh_CN': '买了一件优雅的灰色羊毛大衣，冬天非常好搭衣服。',
            'ko': '겨울 패션에 맞춰 입기 쉬운 고급스러운 회색 울 코트를 샀습니다.',
            'zh_HK': '買咗件好斯文嘅灰色羊毛大褸，冬天非常之好襯衫。',
            'fr': "J'ai acheté un élégant manteau en laine gris, très facile à assortir en hiver."
        }
    },
    'card_0592': {
        'example': {
            'ja': 'リビングのカーテンを明るい<ruby>ベージュ<rt>べーじゅ</rt></ruby>にしたら、部屋が広く感じられます。',
            'en': 'When we changed the living room curtains to a light beige, the room felt much more spacious.',
            'zh_TW': '把客廳的窗簾換成明亮的米色後，感覺整間房間變寬敞了。',
            'zh_CN': '把客厅的窗帘换成明亮的米色后，感觉整间房间变宽敞了。',
            'ko': '거실 커튼을 밝은 베이지색으로 바꿨더니 방이 훨씬 넓어 보여요.',
            'zh_HK': '將客廳窗簾換咗做光猛嘅米黃色之後，成間房好似大咗咁。',
            'fr': "Depuis qu'on a mis des rideaux beige clair dans le salon, la pièce paraît plus grande."
        }
    },
    'card_0594': {
        'example': {
            'ja': 'A: このカレーは<ruby>辛<rt>から</rt></ruby>いですか？<br/>B: 少し<ruby>辛<rt>から</rt></ruby>いですが、コクがあってとても美味しいですよ。',
            'en': 'A: Is this curry spicy?<br/>B: It is a little spicy, but rich and very delicious.',
            'zh_TW': 'A：這道咖哩會辣嗎？<br/>B：稍微有一點辣，但非常濃郁美味喔。',
            'zh_CN': 'A：这道咖喱会辣吗？<br/>B：稍微有一点辣，但非常浓郁美味哦。',
            'ko': 'A: 이 카레는 맵나요?<br/>B: 조금 맵지만 감칠맛이 있고 아주 맛있어요.',
            'zh_HK': 'A：呢個咖喱辣唔辣呀？<br/>B：有少少辣，不過好濃郁好好味。',
            'fr': 'A : Ce curry est-il épicé ?<br/>B : Il est un peu piquant, mais très riche et savoureux.'
        }
    },
    'card_0596': {
        'example': {
            'ja': '汗をかいた後は、少し<ruby>しょっぱい<rt>しょっぱい</rt></ruby>梅干しやスポーツドリンクが美味しく感じます。',
            'en': 'After sweating, slightly salty pickled plums or sports drinks taste delicious.',
            'zh_TW': '流汗之後，吃點微鹹的梅干或喝運動飲料會覺得格外美味。',
            'zh_CN': '流汗之后，吃点微咸的梅干或喝运动饮料会觉得格外美味。',
            'ko': '땀을 흘린 뒤에는 살짝 짠 매실장아찌나 이온 음료가 맛있게 느껴집니다.',
            'zh_HK': '出完汗之後，食少少帶鹹味嘅話梅或者飲運動飲品特別好味。',
            'fr': "Après avoir transpiré, les prunes salées ou les boissons énergétiques sont particulièrement savoureuses."
        }
    },
    'card_0597': {
        'example': {
            'ja': '搾りたてのレモンを入れた紅茶は、ほどよく<ruby>酸っぱい<rt>すっぱい</rt></ruby>風味で爽やかです。',
            'en': 'Black tea with freshly squeezed lemon has a refreshingly tart flavor.',
            'zh_TW': '加入了現擠檸檬汁的紅茶，酸度恰到好處，十分清爽。',
            'zh_CN': '加入了现挤柠檬汁的红茶，酸度恰到好处，十分清爽。',
            'ko': '갓 짠 레몬을 넣은 홍차는 적당히 새콤한 맛이 나서 상쾌합니다.',
            'zh_HK': '加咗新鮮檸檬汁嘅紅茶，酸酸地好清爽。',
            'fr': "Le thé noir avec du citron fraîchement pressé a une saveur agréablement acidulée et rafraîchissante."
        }
    },
    # Body cards
    'card_0218': {
        'example': {
            'ja': '朝起きたら冷たい水でしっかり<ruby>顔<rt>かお</rt></ruby>を洗って、目を覚まします。',
            'en': 'When I wake up in the morning, I wash my face thoroughly with cold water to wake up.',
            'zh_TW': '早上起床後用冷水好好洗臉，讓自己清醒過來。',
            'zh_CN': '早上起床后用冷水好好洗脸，让自己清醒过来。',
            'ko': '아침에 일어나면 찬물로 세수를 꼼꼼히 하여 잠을 깹니다.',
            'zh_HK': '朝早起身用凍水洗乾淨塊面，等自己精神啲。',
            'fr': "Le matin en me levant, je me lave bien le visage à l'eau froide pour me réveiller."
        }
    },
    'card_0231': {
        'example': {
            'ja': '美容院で<ruby>眉毛<rt>まゆげ</rt></ruby>の形をきれいに整えてもらいました。',
            'en': 'I had my eyebrows neatly shaped at the beauty salon.',
            'zh_TW': '在美容院請造型師幫我把眉毛修整得很好看。',
            'zh_CN': '在美容院请造型师帮我把眉毛修整得很好看。',
            'ko': '미용실에서 눈썹 모양을 깔끔하게 다듬었습니다.',
            'zh_HK': '去美容院叫髮型師幫我修整好對眉。',
            'fr': "Je me suis fait épiler et dessiner les sourcils au salon de beauté."
        }
    },
    'card_0233': {
        'example': {
            'ja': 'スマホを片手で操作するときは、主に<ruby>親指<rt>おやゆび</rt></ruby>を使います。',
            'en': 'When operating a smartphone with one hand, I mainly use my thumb.',
            'zh_TW': '單手滑手機的時候，主要都是使用大拇指。',
            'zh_CN': '单手玩手机的时候，主要都是使用大拇指。',
            'ko': '스마트폰을 한 손으로 조작할 때는 주로 엄지손가락을 사용합니다.',
            'zh_HK': '單手用電話嗰陣，主要都係用大拇指。',
            'fr': "Quand j'utilise mon smartphone d'une seule main, je me sers principalement de mon pouce."
        }
    },
    'card_0235': {
        'example': {
            'ja': '手を開いて比べると、五本の指の中で<ruby>中指<rt>なかゆび</rt></ruby>が一番長いです。',
            'en': 'When comparing an open hand, the middle finger is the longest among the five fingers.',
            'zh_TW': '張開手對比一下，五根手指當中中指是最長的。',
            'zh_CN': '张开手对比一下，五根手指当中中指是最长的。',
            'ko': '손을 펴서 비교해 보면 다섯 손가락 중에서 가운뎃손가락이 가장 깁니다.',
            'zh_HK': '擘開隻手比對下，五隻手指入面中指係最長嘅。',
            'fr': "Quand on regarde sa main ouverte, le majeur est le plus long des cinq doigts."
        }
    },
    'card_0236': {
        'example': {
            'ja': '左手の<ruby>薬指<rt>くすりゆび</rt></ruby>に、結婚指輪を大切にはめています。',
            'en': 'I cherish wearing my wedding ring on the ring finger of my left hand.',
            'zh_TW': '在左手的無名指上，珍重地戴著結婚戒指。',
            'zh_CN': '在左手的无名指上，珍重地戴着结婚戒指。',
            'ko': '왼손 약지 손가락에 결혼반지를 소중히 끼고 있습니다.',
            'zh_HK': '喺左手無名指上面，好珍惜咁戴住隻結婚戒指。',
            'fr': "Je porte précieusement mon alliance à l'annulaire de la main gauche."
        }
    },
    'card_0237': {
        'example': {
            'ja': '家具の角に足の<ruby>小指<rt>こゆび</rt></ruby>をぶつけてしまい、とても痛かったです。',
            'en': 'I stubbed my little toe on the corner of the furniture, and it hurt very much.',
            'zh_TW': '腳的小拇指撞到了家具的邊角，痛得不得了。',
            'zh_CN': '脚的小脚趾撞到了家具的边角，痛得不得了。',
            'ko': '가구 모서리에 발의 새끼발가락을 부딪쳐서 너무 아팠습니다.',
            'zh_HK': '隻腳尾指撞到傢俬角位，痛到入心入肺。',
            'fr': "Je me suis cogné le petit orteil contre le coin d'un meuble, ça faisait extrêmement mal."
        }
    },
    'card_0238': {
        'example': {
            'ja': '父は毎朝出社する前に、電気シェーバーで丁寧に<ruby>髭<rt>ひげ</rt></ruby>を剃ります。',
            'en': 'My father carefully shaves his beard with an electric shaver every morning before going to work.',
            'zh_TW': '父親每天早上去上班前，都會用電動刮鬍刀仔細刮鬍子。',
            'zh_CN': '父亲每天早上去上班前，都会用电动剃须刀仔细刮胡子。',
            'ko': '아버지는 매일 아침 출근하기 전에 전기면도기로 수염을 깔끔하게 깎으십니다.',
            'zh_HK': '爸爸每日朝早上班之前，都會用電鬚刨好仔細咁剃鬚。',
            'fr': "Mon père se rase soigneusement la barbe avec un rasoir électrique chaque matin avant d'aller au travail."
        }
    },
    # Facilities
    'card_0665': {
        'example': {
            'ja': '来週は祝日があって3<ruby>連休<rt>れんきゅう</rt></ruby>なので、温泉旅行に行く予定です。',
            'en': 'Next week has a public holiday making it a three-day weekend, so I plan to go on a hot spring trip.',
            'zh_TW': '下週剛好遇到國定假日有三天連假，我打算去溫泉旅行。',
            'zh_CN': '下周刚好遇到法定节假日有三天小长假，我打算去温泉旅行。',
            'ko': '다음 주는 공휴일이 있어 사흘 연휴이므로 온천 여행을 갈 계획입니다.',
            'zh_HK': '下個禮拜撞正公眾假期有三日連假，打算去浸溫泉旅行。',
            'fr': "La semaine prochaine, il y a un jour férié et un week-end de trois jours, je prévois donc d'aller aux sources chaudes."
        }
    },
    'card_0666': {
        'example': {
            'ja': '休日に美術館へ行って、素晴らしい現代<ruby>美術<rt>びじゅつ</rt></ruby>の作品を鑑賞しました。',
            'en': 'On my day off, I went to an art museum and appreciated wonderful contemporary art works.',
            'zh_TW': '休假時去了美術館，欣賞了精彩的現代美術作品。',
            'zh_CN': '休假时去了美术馆，欣赏了精彩的现代美术作品。',
            'ko': '휴일에 미술관에 가서 훌륭한 현대미술 작품을 감상했습니다.',
            'zh_HK': '放假嗰陣去咗美術館，欣賞咗好靚嘅現代藝術作品。',
            'fr': "Pendant mon jour de congé, je suis allé au musée des beaux-arts et j'ai admiré de magnifiques œuvres d'art moderne."
        }
    },
    'card_0668': {
        'example': {
            'ja': '国立科学<ruby>博物館<rt>はくぶつかん</rt></ruby>で、大きな恐竜の化石を見学しました。',
            'en': 'At the National Museum of Nature and Science, we toured the large dinosaur fossils.',
            'zh_TW': '在國立科學博物館參觀了巨大的恐龍化石。',
            'zh_CN': '在国立科学博物馆参观了巨大的恐龙化石。',
            'ko': '국립과학박물관에서 거대한 공룡 화석을 견학했습니다.',
            'zh_HK': '喺國立科學博物館參觀咗好大件嘅恐龍化石。',
            'fr': "Au musée national des sciences, nous avons admiré de grands fossiles de dinosaures."
        }
    },
    'card_0670': {
        'example': {
            'ja': 'お正月に近くの有名な<ruby>神社<rt>じんじゃ</rt></ruby>へ初詣に行って、健康をお祈りしました。',
            'en': 'For New Year, I went for Hatsumode to a famous nearby shrine and prayed for good health.',
            'zh_TW': '過年時去附近知名的神社新年參拜（初詣），祈求身體健康。',
            'zh_CN': '过年时去附近知名的神社新年参拜，祈求身体健康。',
            'ko': '새해 첫날에 근처의 유명한 신사로 하츠모데(새해 첫 참배)를 가서 건강을 기원했습니다.',
            'zh_HK': '新年嗰陣去咗附近好出名嘅神社新年參拜，祈求身體健康。',
            'fr': "Pour le Nouvel An, je suis allé faire la première visite de l'année dans un sanctuaire réputé des environs et j'ai prié pour la santé."
        }
    },
    'card_0673': {
        'example': {
            'ja': 'ワーキングホリデーのビザを申請するために、来週<ruby>大使館<rt>たいしかん</rt></ruby>へ行きます。',
            'en': 'Next week, I am going to the embassy to apply for a working holiday visa.',
            'zh_TW': '為了申請打工度假簽證，我下週要去一趟大使館。',
            'zh_CN': '为了申请打工度假签证，我下周要去一趟大使馆。',
            'ko': '워킹홀리데이 비자를 신청하기 위해 다음 주에 대사관에 갑니다.',
            'zh_HK': '為咗申請Working Holiday簽證，我下個禮拜要去一趟大使館。',
            'fr': "J'irai à l'ambassade la semaine prochaine pour demander un visa vacances-travail."
        }
    },
    'card_0676': {
        'example': {
            'ja': '駅前で財布を拾ったので、すぐに近くの<ruby>交番<rt>こうばん</rt></ruby>へ届けました。',
            'en': 'I picked up a wallet in front of the station and immediately brought it to the nearby police box.',
            'zh_TW': '在車站前撿到了皮夾，立刻送到了附近的派出所（交番）。',
            'zh_CN': '在车站前捡到了钱包，立刻送到了附近的派出所。',
            'ko': '역 앞에서 지갑을 주워서 곧바로 근처 파출소(코반)에 전달했습니다.',
            'zh_HK': '喺車站前面執到個銀包，即刻拎咗去附近嘅差館。',
            'fr': "J'ai trouvé un portefeuille devant la gare et je l'ai immédiatement apporté au poste de police voisin."
        }
    },
    'card_0677': {
        'example': {
            'ja': '近所で火災が発生したときは、落ち着いてすぐに<ruby>消防署<rt>しょうぼうしょ</rt></ruby>に通報しましょう。',
            'en': 'If a fire occurs in the neighborhood, stay calm and immediately call the fire department.',
            'zh_TW': '鄰近地區發生火災時，請保持冷靜並立刻通報消防局。',
            'zh_CN': '邻近地区发生火灾时，请保持冷静并立刻通报消防局。',
            'ko': '근처에서 화재가 발생했을 때는 침착하게 바로 소방서에 신고합시다.',
            'zh_HK': '附近發生火警嗰陣，記得要冷靜並且即刻打去消防局報案。',
            'fr': "Si un incendie se déclare dans le quartier, gardez votre calme et appelez immédiatement les pompiers."
        }
    },
    'card_0679': {
        'example': {
            'ja': 'レトロな雰囲気の<ruby>喫茶店<rt>きっさてん</rt></ruby>で、名物のプリンとブレンドコーヒーを楽しみました。',
            'en': 'At a coffee shop with a retro vibe, I enjoyed their specialty pudding and blended coffee.',
            'zh_TW': '在一家充滿懷舊復古氛圍的喫茶店裡，享用了招牌布丁和綜合特調咖啡。',
            'zh_CN': '在一家充满怀旧复古氛围的咖啡馆里，享用了招牌布丁和综合特调咖啡。',
            'ko': '레트로한 분위기의 카페(킷사텐)에서 유명한 푸딩과 블렌드 커피를 즐겼습니다.',
            'zh_HK': '喺一間充滿懷舊復古Feel嘅日式喫茶店，試咗佢哋招牌布甸同咖啡。',
            'fr': "Dans un café rétro traditionnel, j'ai dégusté leur fameux flan avec un café mélangé maison."
        }
    },
    'card_0682': {
        'example': {
            'ja': '商店街の<ruby>八百屋<rt>やおや</rt></ruby>さんで、採れたての新鮮なトマトときゅうりを買いました。',
            'en': 'At the greengrocer in the shopping street, I bought freshly picked tomatoes and cucumbers.',
            'zh_TW': '在商店街的蔬果店（八百屋）買了剛摘下來的新鮮番茄和小黃瓜。',
            'zh_CN': '在商店街的蔬菜水果店买了刚采摘的新鲜番茄和黄瓜。',
            'ko': '상점가의 채소가게(야오야)에서 갓 수확한 신선한 토마토와 오이를 샀습니다.',
            'zh_HK': '喺商店街嘅菜檔買咗新鮮摘落嚟嘅蕃茄同青瓜。',
            'fr': "Chez le primeur de la rue commerçante, j'ai acheté des tomates et des concombres fraîchement cueillis."
        }
    },
    'card_0686': {
        'example': {
            'ja': 'コンサートホールの<ruby>入口<rt>いりぐち</rt></ruby>の前で、友達と待ち合わせをしています。',
            'en': 'I am meeting up with my friend in front of the concert hall entrance.',
            'zh_TW': '在音樂廳的入口前和朋友碰面會合。',
            'zh_CN': '在音乐厅的入口前和朋友碰面汇合。',
            'ko': '콘서트홀 입구 앞에서 친구와 만나기로 약속했습니다.',
            'zh_HK': '喺音樂廳門口前面同朋友等緊集合。',
            'fr': "J'ai rendez-vous avec mon ami devant l'entrée de la salle de concert."
        }
    },
    'card_0693': {
        'example': {
            'ja': '成田空港へ行くために、日暮里駅からスカイライナーの<ruby>特急<rt>とっきゅう</rt></ruby>に乗りました。',
            'en': 'To go to Narita Airport, I took the Skyliner limited express from Nippori Station.',
            'zh_TW': '為了去成田機場，我從日暮里站搭乘了Skyliner特急列車。',
            'zh_CN': '为了去成田机场，我从日暮里站搭乘了Skyliner特快列车。',
            'ko': '나리타 공항에 가기 위해 닛포리 역에서 스카이라이너 특급 열차를 탔습니다.',
            'zh_HK': '為咗去成田機場，我喺日暮里站搭咗Skyliner特急列車。',
            'fr': "Pour aller à l'aéroport de Narita, j'ai pris le train express limité Skyliner depuis la gare de Nippori."
        }
    },
    'card_0694': {
        'example': {
            'ja': 'この電車は<ruby>急行<rt>きゅうこう</rt></ruby>なので、各駅停車よりも早く目的地に着きますよ。',
            'en': 'This train is an express, so it arrives at the destination faster than the local train.',
            'zh_TW': '這班電車是急行列車，所以會比各站皆停的普通車更快到達目的地喔。',
            'zh_CN': '这班电车是快车，所以会比每站都停的普通车更快到达目的地哦。',
            'ko': '이 전철은 급행열차라서 각역정차 열차보다 목적지에 더 빨리 도착해요.',
            'zh_HK': '呢班車係急行火車，所以會快過架架停嘅普通車到目的地㗎。',
            'fr': "Ce train est un express, il arrive donc plus vite à destination que l'omnibus."
        }
    },
    'card_0697': {
        'example': {
            'ja': 'バス停の<ruby>時刻表<rt>じこくひょう</rt></ruby>を確認して、次のバスの時間を調べました。',
            'en': 'I checked the bus stop timetable to find out when the next bus would come.',
            'zh_TW': '確認了公車站牌的時刻表，查了一下下一班公車來的時間。',
            'zh_CN': '确认了公交站牌的时刻表，查了一下下一班公交来的时间。',
            'ko': '버스 정류장의 시간표를 확인하고 다음 버스 시간을 알아봤습니다.',
            'zh_HK': '睇咗巴士站嘅時間表，查下下一班巴士幾點到。',
            'fr': "J'ai vérifié les horaires à l'arrêt de bus pour savoir quand arrivait le prochain bus."
        }
    },
    'card_0701': {
        'example': {
            'ja': '帰りの日程がまだ決まっていないので、新幹線の<ruby>片道<rt>かたみち</rt></ruby>切符だけ購入しました。',
            'en': 'Since my return schedule is not yet decided, I only purchased a one-way Shinkansen ticket.',
            'zh_TW': '因為回程的日期還沒決定，所以我只買了新幹線的單程票。',
            'zh_CN': '因为回程的日期还没决定，所以我只买了新干线的单程票。',
            'ko': '돌아오는 일정이 아직 정해지지 않아서 신칸센 편도 티켓만 구매했습니다.',
            'zh_HK': '因為回程嘅日子仲未定好，所以我剩係買咗新幹線嘅單程飛。',
            'fr': "Comme ma date de retour n'est pas encore fixée, je n'ai acheté qu'un aller simple pour le Shinkansen."
        }
    },
    'card_0702': {
        'example': {
            'ja': '京都までの新幹線は、<ruby>往復<rt>おうふく</rt></ruby>でチケットを予約したほうが割引でお得です。',
            'en': 'For the Shinkansen to Kyoto, booking round-trip tickets is a better deal with discounts.',
            'zh_TW': '去京都的新幹線，買來回往返車票會有折扣比較划算。',
            'zh_CN': '去京都的新干线，买往返车票会有折扣比较划算。',
            'ko': '교토까지 가는 신칸센은 왕복으로 티켓을 예약하는 편이 할인되어 더 이득입니다.',
            'zh_HK': '去京都嘅新幹線，買來回往返車飛會有折抵好多。',
            'fr': "Pour le Shinkansen jusqu'à Kyoto, il est plus avantageux de réserver un billet aller-retour avec une réduction."
        }
    },
    'card_0103': {
        'example': {
            'ja': '私の<ruby>父<rt>ちち</rt></ruby>は自動車メーカーでエンジニアとして働いています。',
            'en': 'My father works as an engineer at an automobile manufacturer.',
            'zh_TW': '我的父親在一家汽車製造商擔任工程師。',
            'zh_CN': '我的父亲在一家汽车制造商担任工程师。',
            'ko': '저희 아버지는 자동차 회사에서 엔지니어로 일하고 계십니다.',
            'zh_HK': '我爸爸喺一間汽車製造廠做工程師。',
            'fr': "Mon père travaille comme ingénieur chez un constructeur automobile."
        }
    },
    'card_0104': {
        'example': {
            'ja': '<ruby>母<rt>はは</rt></ruby>は料理がとても上手で、毎日美味しいお弁当を作ってくれます。',
            'en': 'My mother is very good at cooking and makes delicious bento boxes for me every day.',
            'zh_TW': '我的母親很擅長做菜，每天都會為我準備好吃的便當。',
            'zh_CN': '我的母亲很擅长做菜，每天都会为我准备好吃的便当。',
            'ko': '저희 어머니는 요리를 아주 잘하셔서 매일 맛있는 도시락을 싸 주십니다.',
            'zh_HK': '我媽媽煮嘢食好叻，每日都會幫我整好味嘅便當。',
            'fr': "Ma mère est très douée en cuisine et me prépare de délicieux bentos tous les jours."
        }
    },
    'card_0176': {
        'example': {
            'ja': '大学のキャンパスで、台湾から来た<ruby>留学生<rt>りゅうがくせい</rt></ruby>の案内を担当しました。',
            'en': 'On the university campus, I was in charge of guiding an exchange student from Taiwan.',
            'zh_TW': '在大學校園裡，我負責引導帶領來自台灣的留學生。',
            'zh_CN': '在大学校园里，我负责带领来自台湾的留学生。',
            'ko': '대학교 캠퍼스에서 대만에서 온 유학생의 안내를 맡았습니다.',
            'zh_HK': '喺大學校園入面，我負責帶領嚟自台灣嘅留學生。',
            'fr': "Sur le campus universitaire, j'ai été chargé de guider un étudiant étranger venu de Taïwan."
        }
    },
    'card_0208': {
        'example': {
            'ja': '親友は今<ruby>アメリカ<rt>あめりか</rt></ruby>のニューヨークに住んでいて、毎日連絡を取り合っています。',
            'en': 'My best friend now lives in New York, America, and we keep in touch every day.',
            'zh_TW': '我的摯友現在住在美國紐約，我們每天都有聯絡。',
            'zh_CN': '我的挚友现在住在美国纽约，我们每天都有联系。',
            'ko': '절친한 친구는 지금 미국 뉴욕에 살고 있어서 매일 연락을 주고받고 있습니다.',
            'zh_HK': '我最好嘅朋友依家喺美國紐約住，我哋每日都會傾計。',
            'fr': "Mon meilleur ami vit actuellement à New York aux États-Unis, et nous restons en contact tous les jours."
        }
    },
    'card_0401': {
        'example': {
            'ja': '東京は電車やバスなどの<ruby>乗り物<rt>のりもの</rt></ruby>が発達していて、どこへ行くにも便利です。',
            'en': 'Tokyo has well-developed transportation like trains and buses, making it convenient to go anywhere.',
            'zh_TW': '東京的電車和公車等交通工具非常發達，去哪裡都很方便。',
            'zh_CN': '东京的电车和公交等交通工具非常发达，去哪里都很方便。',
            'ko': '도쿄는 전철과 버스 등 대중교통이 발달해 있어 어디를 가든 편리합니다.',
            'zh_HK': '東京嘅火車同巴士等交通工具好發達，去邊度都咁方便。',
            'fr': "Tokyo dispose de transports très développés comme les trains et les bus, ce qui rend les déplacements très pratiques."
        }
    },
    'card_0602': {
        'example': {
            'ja': '渋谷駅のハチ公前の広場で、友達と<ruby>待ち合わせ<rt>まちあわせ</rt></ruby>をしています。',
            'en': 'I am meeting up with my friend in the square in front of Hachiko at Shibuya Station.',
            'zh_TW': '我和朋友約在澀谷站八公像前的廣場碰面碰頭。',
            'zh_CN': '我和朋友约在涩谷站八公像前的广场碰面。',
            'ko': '시부야역 하치코 동상 앞 광장에서 친구와 만나기로 약속했습니다.',
            'zh_HK': '同朋友約好喺澀谷站八公像前面個廣場等。',
            'fr': "J'ai rendez-vous avec un ami sur la place devant la statue d'Hachiko à la gare de Shibuya."
        }
    },
    'card_0609': {
        'example': {
            'ja': '若者の<ruby>恋愛<rt>れんあい</rt></ruby>をテーマにしたドラマが、今とても人気を集めています。',
            'en': 'A drama themed around young people\'s romance is currently gaining huge popularity.',
            'zh_TW': '以年輕人的戀愛為主題的日劇，現在非常受歡迎。',
            'zh_CN': '以年轻人的恋爱为主题的电视剧，现在非常受欢迎。',
            'ko': '청춘들의 연애를 테마로 한 드라마가 지금 큰 인기를 얻고 있습니다.',
            'zh_HK': '以年輕人拍拖戀愛為主題嘅劇集，依家好受歡迎。',
            'fr': "Un feuilleton sur le thème des amours de jeunesse connaît actuellement un énorme succès."
        }
    },
    'card_0620': {
        'example': {
            'ja': '兄は子供の頃から道場に通って<ruby>柔道<rt>じゅうどう</rt></ruby>の稽古に励んでいます。',
            'en': 'My older brother has attended a dojo since childhood and trains hard in judo.',
            'zh_TW': '我哥哥從小就去道場，非常認真地練習柔道。',
            'zh_CN': '我哥哥从小就去道场，非常认真地练习柔道。',
            'ko': '형은 어릴 때부터 도장에 다니며 유도 수련에 힘쓰고 있습니다.',
            'zh_HK': '我阿哥細細個就去館度學柔道，好勤力練習。',
            'fr': "Mon frère aîné fréquente un dojo depuis son enfance et s'entraîne assidûment au judo."
        }
    },
    'card_0623': {
        'example': {
            'ja': '日本には四季があり、どの<ruby>季節<rt>きせつ</rt></ruby>も美しい景色と旬の食べ物が楽しめます。',
            'en': 'Japan has four distinct seasons, and you can enjoy beautiful scenery and seasonal foods in every season.',
            'zh_TW': '日本四季分明，在任何季節都能享受美麗的風景與當季美食。',
            'zh_CN': '日本四季分明，在任何季节都能享受美丽的风景与应季美食。',
            'ko': '일본에는 사계절이 있어 어느 계절이나 아름다운 경치와 제철 음식을 즐길 수 있습니다.',
            'zh_HK': '日本四季分明，無論咩季節都可以欣賞到好靚嘅風景同當造嘅美食。',
            'fr': "Le Japon a quatre saisons bien marquées, et l'on peut profiter de magnifiques paysages et de mets de saison en toute période."
        }
    }
}

# 3. Simple greetings and everyday phrases in INITIAL_VOCAB_DATA with English in KO
GREETING_KO_FIXES = {
    'card_0001': '네, 알겠습니다.',
    'card_0002': '아니요, 틀립니다.',
    'card_0004': '오랜만입니다, 잘 지내시나요?',
    'card_0005': '네, 덕분에 잘 지내고 있습니다.',
    'card_0094': '이름이 무엇인가요?'
}

updated_init_count = 0
for c in init_cards:
    cid = c.get('id')
    # Related fix
    if cid in RELATED_FIXES:
        c['related'] = RELATED_FIXES[cid]
        updated_init_count += 1
    # Specific sentence fixes
    if cid in SPECIFIC_INIT_FIXES:
        fix_data = SPECIFIC_INIT_FIXES[cid]
        for k, v in fix_data.items():
            if k == 'example':
                for lang_k, lang_v in v.items():
                    c['example'][lang_k] = lang_v
            else:
                c[k] = v
        updated_init_count += 1
    # Greeting KO fix
    if cid in GREETING_KO_FIXES:
        c['example']['ko'] = GREETING_KO_FIXES[cid]
        updated_init_count += 1

print(f"Applied fixes to {updated_init_count} cards in INITIAL_VOCAB_DATA")

new_init_json = json.dumps(init_cards, ensure_ascii=False, indent=2)
with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(init_prefix + new_init_json + init_suffix)
with open('public/js/data.js', 'w', encoding='utf-8') as f:
    f.write(init_prefix + new_init_json + init_suffix)

print("✅ Saved js/data.js and public/js/data.js")

# ==============================================================================
# PART 2: FIX CLASS_VOCAB_DATA (2200 cards)
# ==============================================================================
with open('database/class_vocab_data.js', 'r', encoding='utf-8') as f:
    class_text = f.read()

s_class = class_text.find('[')
e_class = class_text.rfind('];') + 1
class_prefix = class_text[:s_class]
class_suffix = class_text[e_class:]
class_cards = json.loads(class_text[s_class:e_class].strip())

# Master dictionary of natural replacements for the 116 bizarre/fragment cards
CLASS_REPLACEMENTS = {
    'class_word_0029': {
        'ja': '自分自身の力を<ruby>信<rt>しん</rt></ruby>じて、最後まで諦めずに挑戦します。',
        'en': 'I will believe in my own abilities and take on the challenge without giving up until the end.',
        'zh_TW': '相信自己的力量，堅持到底絕不輕言放棄。',
        'zh_CN': '相信自己的力量，坚持到底绝不轻言放弃。',
        'ko': '자신의 힘을 믿고 끝까지 포기하지 않고 도전하겠습니다.',
        'zh_HK': '相信自己嘅力量，堅持到底絕不放棄去挑戰。',
        'fr': 'Je croirai en mes propres forces et relèverai le défi sans abandonner jusqu’au bout.'
    },
    'class_word_0030': {
        'ja': '同僚が夏休みにヨーロッパ旅行へ行くと聞いて、とても<ruby>羨<rt>うらや</rt></ruby>ましいです。',
        'en': 'Hearing that my colleague is going on a trip to Europe for summer vacation, I am very envious.',
        'zh_TW': '聽說同事暑假要去歐洲旅行，真讓人非常羨慕。',
        'zh_CN': '听说同事暑假要去欧洲旅行，真让人非常羡慕。',
        'ko': '동료가 여름휴가에 유럽 여행을 간다는 말을 듣고 정말 부러웠습니다.',
        'zh_HK': '聽講同事暑假去歐洲旅行，真係好羨慕。',
        'fr': 'En apprenant que mon collègue part en voyage en Europe pour les vacances d’été, je suis très envieux.'
    },
    'class_word_0073': {
        'ja': 'A: 明日のパーティー、参加してくれる？<br/>B: <ruby>もちろん<rt>もちろん</rt></ruby>！楽しみにしているよ。',
        'en': 'A: Will you join tomorrow\'s party?<br/>B: Of course! I\'m looking forward to it.',
        'zh_TW': 'A：明天的派對你會來參加嗎？<br/>B：當然囉！我很期待呢。',
        'zh_CN': 'A：明天的派对你会来参加吗？<br/>B：当然啦！我很期待呢。',
        'ko': 'A: 내일 파티에 와 줄 거지?<br/>B: 물론이지! 기대하고 있어.',
        'zh_HK': 'A：聽日個Party你會嚟㗎可？<br/>B：梗係啦！好期待呀。',
        'fr': 'A : Tu viens à la fête demain ?<br/>B : Bien sûr ! J’ai hâte d’y être.'
    },
    'class_word_0078': {
        'ja': '残業で帰りが<ruby>遅<rt>おそ</rt></ruby>くなったので、駅前のコンビニで夜ご飯を買いました。',
        'en': 'Since I got home late due to overtime, I bought dinner at the convenience store in front of the station.',
        'zh_TW': '因為加班回家變得很晚，所以在車站前的超商買了晚餐。',
        'zh_CN': '因为加班回家变晚了，所以在车站前的便利店买了晚餐。',
        'ko': '야근 때문에 귀가가 늦어져서 역 앞 편의점에서 저녁밥을 샀습니다.',
        'zh_HK': '因為OT好夜先返到去，所以喺站前面嘅便利店買咗晚餐。',
        'fr': 'Comme je suis rentré tard à cause des heures supplémentaires, j’ai acheté à dîner à la supérette devant la gare.'
    },
    'class_word_0079': {
        'ja': '混雑した道路ではスピードが<ruby>遅<rt>おそ</rt></ruby>くなりますが、安全運転が一番大切です。',
        'en': 'Speed becomes slow on congested roads, but safe driving is what matters most.',
        'zh_TW': '雖然在擁擠的道路上車速會變慢，但安全駕駛才是最重要的。',
        'zh_CN': '虽然在拥挤的道路上车速会变慢，但安全驾驶才是最重要的。',
        'ko': '혼잡한 도로에서는 속도가 느려지지만, 안전운전이 가장 중요합니다.',
        'zh_HK': '塞車嗰陣雖然行得慢，但係安全駕駛先係最緊要。',
        'fr': 'Sur une route encombrée la vitesse ralentit, mais la conduite prudente est le plus important.'
    },
    'class_word_0089': {
        'ja': '飛行機が無事に空港へ<ruby>着<rt>つ</rt></ruby>いたら、すぐに家族にメッセージを送ります。',
        'en': 'Once the airplane arrives safely at the airport, I will send a message to my family right away.',
        'zh_TW': '飛機平安抵達機場後，我會立刻發訊息給家人報平安。',
        'zh_CN': '飞机平安抵达机场后，我会立刻发信息给家人报平安。',
        'ko': '비행기가 무사히 공항에 도착하면 바로 가족에게 메시지를 보낼게요.',
        'zh_HK': '飛機安全去到機場之後，我會即刻WhatsApp屋企人報平安。',
        'fr': 'Dès que l’avion sera arrivé sain et sauf à l’aéroport, j’enverrai un message à ma famille.'
    },
    'class_word_0092': {
        'ja': 'お医者さんにもらった風邪<ruby>薬<rt>くすり</rt></ruby>を飲んだら、熱が下がって楽になりました。',
        'en': 'After taking the cold medicine given by the doctor, my fever went down and I felt much better.',
        'zh_TW': '吃了醫生開的感冒藥之後，燒退了，感覺輕鬆多了。',
        'zh_CN': '吃了医生开的感冒药之后，烧退了，感觉舒服多了。',
        'ko': '의사 선생님이 처방해 준 감기약을 먹었더니 열이 내리고 한결 편해졌습니다.',
        'zh_HK': '食咗醫生開嘅感冒藥之後退咗燒，舒服咗好多。',
        'fr': 'Après avoir pris le médicament prescrit par le médecin, ma fièvre est tombée et je me suis senti soulagé.'
    },
    'class_word_0094': {
        'ja': '健康のために、毎朝近所の公園で軽いランニングなどの<ruby>運動<rt>うんどう</rt></ruby>をしています。',
        'en': 'For my health, I exercise by doing light jogging in the neighborhood park every morning.',
        'zh_TW': '為了健康，我每天早晨都會在附近的公園慢跑做運動。',
        'zh_CN': '为了健康，我每天早晨都会在附近的公园慢跑做运动。',
        'ko': '건강을 위해서 매일 아침 동네 공원에서 가벼운 러닝 등 운동을 하고 있습니다.',
        'zh_HK': '為咗健康，我每日朝早都會喺附近嘅公園慢跑做下運動。',
        'fr': 'Pour ma santé, je fais du sport chaque matin en courant légèrement dans le parc du quartier.'
    },
    'class_word_0102': {
        'ja': '夏に公園を散歩していたら、腕を<ruby>蚊<rt>か</rt></ruby>に刺されて痒くなってしまいました。',
        'en': 'While taking a walk in the park in summer, I was bitten by a mosquito on my arm and it became itchy.',
        'zh_TW': '夏天在公園散步時，手臂被蚊子叮咬變得好癢。',
        'zh_CN': '夏天在公园散步时，手臂被蚊子叮咬变得好痒。',
        'ko': '여름에 공원을 산책하다가 팔을 모기에 물려 가려워졌습니다.',
        'zh_HK': '夏天喺公園散步嗰陣，隻手畀蚊咬到好痕。',
        'fr': 'En me promenant dans le parc en été, je me suis fait piquer par un moustique au bras et ça me démange.'
    },
    'class_word_0112': {
        'ja': '日本語の学習記録として、毎日寝る前に短い<ruby>日記<rt>にっき</rt></ruby>を書いています。',
        'en': 'As a Japanese study log, I write a short diary entry every day before going to bed.',
        'zh_TW': '作為學習日語的紀錄，我每天睡前都會寫簡短的日記。',
        'zh_CN': '作为学习日语的记录，我每天睡前都会写简短的日记。',
        'ko': '일본어 학습 기록으로 매일 자기 전에 짧은 일기를 쓰고 있습니다.',
        'zh_HK': '作為學日文嘅紀錄，我每日瞓覺前都會寫少少日記。',
        'fr': 'Pour suivre mon apprentissage du japonais, j’écris un court journal intime chaque soir avant de dormir.'
    },
    'class_word_0114': {
        'ja': '二人は長い交際を経て、今年の秋に<ruby>結婚<rt>けっこん</rt></ruby>式を挙げることになりました。',
        'en': 'After dating for a long time, the two decided to hold their wedding ceremony this autumn.',
        'zh_TW': '兩個人經過長期的交往，決定在今年秋天舉行婚禮。',
        'zh_CN': '两个人经过长期的交往，决定在今年秋天举行婚礼。',
        'ko': '두 사람은 오랜 교제 끝에 올가을에 결혼식을 올리기로 했습니다.',
        'zh_HK': '佢哋拍拖好多年之後，決定喺今年秋天擺酒結婚。',
        'fr': 'Après de longues années ensemble, ils ont décidé de célébrer leur mariage cet automne.'
    },
    'class_word_0125': {
        'ja': '新しいレシピをネットで見つけたので、今日の夕飯に実際に作って<ruby>試<rt>ため</rt></ruby>してみます。',
        'en': 'I found a new recipe online, so I will try making it for dinner tonight.',
        'zh_TW': '在網路上找到了新食譜，今天晚餐打算實際做做看來試試味道。',
        'zh_CN': '在网上找到了新食谱，今天晚餐打算实际做做看尝试一下。',
        'ko': '인터넷에서 새로운 레시피를 찾아서 오늘 저녁으로 직접 시험 삼아 만들어 보려고 합니다.',
        'zh_HK': '上網搵到個新食譜，今晚諗住跟住煮試下味。',
        'fr': 'J’ai trouvé une nouvelle recette sur internet, je vais essayer de la cuisiner pour le dîner de ce soir.'
    },
    'class_word_0127': {
        'ja': '休日の夕方に、愛犬と一緒に川沿いの道をのんびり<ruby>散歩<rt>さんぽ</rt></ruby>しました。',
        'en': 'On a holiday evening, I took a leisurely walk along the river path with my dog.',
        'zh_TW': '放假的傍晚，我和愛犬一起在河畔步道悠閒地散步。',
        'zh_CN': '放假的傍晚，我和爱犬一起在河畔步道悠闲地散步。',
        'ko': '휴일 저녁에 반려견과 함께 강변길을 여유롭게 산책했습니다.',
        'zh_HK': '放假下晝同隻狗一齊喺河邊好悠閒咁散步。',
        'fr': 'Le soir pendant mon jour de congé, je me suis promené tranquillement le long de la rivière avec mon chien.'
    },
    'class_word_0138': {
        'ja': '喉が乾燥して少し痛いので、カバンから喉<ruby>飴<rt>あめ</rt></ruby>を取り出してなめました。',
        'en': 'My throat felt dry and a bit sore, so I took a cough drop from my bag and sucked on it.',
        'zh_TW': '喉嚨有點乾燥發痛，我從包包裡拿了顆潤喉糖來吃。',
        'zh_CN': '喉咙有点干燥发痛，我从包包里拿了颗润喉糖来吃。',
        'ko': '목이 건조하고 따끔거려서 가방에서 목캔디를 꺼내 먹었습니다.',
        'zh_HK': '喉嚨好乾有啲痛，喺袋度攞粒潤喉糖出嚟含。',
        'fr': 'Comme ma gorge était sèche et douloureuse, j’ai sorti un bonbon pour la gorge de mon sac.'
    },
    'class_word_0143': {
        'ja': '昔住んでいた町を訪れると、子供の頃によく遊んだ公園がとても<ruby>懐<rt>なつ</rt></ruby>かしいです。',
        'en': 'Visiting the town I used to live in, the park where I often played as a child brings back fond nostalgia.',
        'zh_TW': '造訪以前住過的小鎮，小時候常去玩的公園讓人感到非常懷念。',
        'zh_CN': '造访以前住过的小镇，小时候常去玩的公园让人感到非常怀念。',
        'ko': '예전에 살던 동네를 방문하니 어릴 때 자주 놀던 공원이 무척 그립고 정답습니다.',
        'zh_HK': '去返以前住過嘅地方，細個成日去玩嘅公園真係令人好懷念。',
        'fr': 'En visitant la ville où j’habitais autrefois, le parc où je jouais enfant m’a rendu très nostalgique.'
    },
    'class_word_0159': {
        'ja': '食事が終わった後、家族みんなで協力してお<ruby>皿<rt>さら</rt></ruby>をきれいに洗いました。',
        'en': 'After finishing the meal, our family cooperated together to wash the dishes cleanly.',
        'zh_TW': '用餐結束後，全家人一起幫忙把盤子洗得乾乾淨淨。',
        'zh_CN': '用餐结束后，全家人一起帮忙把盘子洗得干干净净。',
        'ko': '식사가 끝난 후 가족 모두가 협력하여 접시를 깨끗이 설거지했습니다.',
        'zh_HK': '食完飯之後，成家人一齊分工洗乾淨啲碗碟。',
        'fr': 'Après le repas, toute la famille a aidé à faire la vaisselle soigneusement.'
    },
    'class_word_0160': {
        'ja': '冬場は空気が乾燥するので、化粧水やクリームを塗って<ruby>肌<rt>はだ</rt></ruby>を保湿しています。',
        'en': 'The air is dry in winter, so I apply lotion and cream to moisturize my skin.',
        'zh_TW': '冬天空氣乾燥，我都會塗抹化妝水和乳霜來做好肌膚保濕。',
        'zh_CN': '冬天空气干燥，我都会涂抹化妆水和乳霜来做好肌肤保湿。',
        'ko': '겨울철에는 공기가 건조하므로 스킨과 크림을 발라 피부를 보습하고 있습니다.',
        'zh_HK': '冬天好乾燥，所以會查爽膚水同面霜幫皮膚保濕。',
        'fr': 'L’air étant sec en hiver, j’applique de la lotion et de la crème pour hydrater ma peau.'
    },
    'class_word_0198': {
        'ja': 'A: 今度の連休、一緒に京都へ旅行に行きませんか？<br/>B: <ruby>ぜひ<rt>ぜひ</rt></ruby>行きましょう！楽しみにしています。',
        'en': 'A: Shall we travel to Kyoto together on the upcoming long weekend?<br/>B: By all means, let\'s go! I\'m really looking forward to it.',
        'zh_TW': 'A：這次連假要不要一起去京都旅行呢？<br/>B：請務必一起去！我很期待呢。',
        'zh_CN': 'A：这次小长假要不要一起去京都旅行呢？<br/>B：一定要去！我很期待呢。',
        'ko': 'A: 이번 연휴에 같이 교토로 여행 가지 않을래요?<br/>B: 꼭 가요! 정말 기대돼요.',
        'zh_HK': 'A：今次連假一唔一齊去京都旅行呀？<br/>B：一定要去啦！好期待。',
        'fr': 'A : Si on partait en voyage à Kyoto ensemble pendant le long week-end ?<br/>B : Absolument, allons-y ! J’ai vraiment hâte.'
    },
    'class_word_0261': {
        'ja': 'リビングのフローリングの<ruby>床<rt>ゆか</rt></ruby>をモップでピカピカに磨きました。',
        'en': 'I polished the wooden floor of the living room until it sparkled using a mop.',
        'zh_TW': '用拖把將客廳的木質地板擦得閃閃發亮。',
        'zh_CN': '用拖把将客厅的木质地板擦得闪闪发亮。',
        'ko': '거실의 마루 바닥을 걸레로 반짝반짝 닦았습니다.',
        'zh_HK': '用地拖將客廳嘅木地板抹到立立令。',
        'fr': 'J’ai astiqué le parquet ciré du salon avec une serpillière jusqu’à ce qu’il brille.'
    },
    'class_word_0321': {
        'ja': '就職祝いに両親からプレゼントされた<ruby>時計<rt>とけい</rt></ruby>を、毎日大切に身につけています。',
        'en': 'I wear the watch my parents gave me as an employment gift with great care every day.',
        'zh_TW': '每天我都非常珍惜地戴著父母送給我的就職賀禮手錶。',
        'zh_CN': '每天我都非常珍惜地戴着父母送给我的就职贺礼手表。',
        'ko': '취업 축하 선물로 부모님께 받은 시계를 매일 소중히 차고 다닙니다.',
        'zh_HK': '每日都好錫住戴住父母送畀我嘅就職禮物手錶。',
        'fr': 'Je porte précieusement chaque jour la montre que mes parents m’ont offerte pour mon nouvel emploi.'
    },
    'class_word_0325': {
        'ja': '美味しい料理をたくさん食べて、お腹が<ruby>いっぱい<rt>いっぱい</rt></ruby>になって大満足です。',
        'en': 'I ate a lot of delicious food, became completely full, and was very satisfied.',
        'zh_TW': '吃了很多好吃的料理，肚子飽飽的好滿足。',
        'zh_CN': '吃了很多好吃的美食，肚子饱饱的好满足。',
        'ko': '맛있는 음식을 잔뜩 먹어서 배가 부르고 대만족입니다.',
        'zh_HK': '食咗好多好嘢，飽到成個肚脹晒好滿足。',
        'fr': 'J’ai mangé plein de bonnes choses, j’ai le ventre plein et je suis comblé.'
    },
    'class_word_0329': {
        'ja': '部屋の壁掛け<ruby>時計<rt>とけい</rt></ruby>が止まっていたので、新しい電池に取り替えました。',
        'en': 'The wall clock in the room had stopped, so I replaced it with a fresh battery.',
        'zh_TW': '房間的掛鐘停住了，所以我換上了新的電池。',
        'zh_CN': '房间的挂钟停住了，所以我换上了新的电池。',
        'ko': '방의 벽시계가 멈춰 있어서 새 건전지로 교체했습니다.',
        'zh_HK': '房入面個掛牆鐘停咗，所以我換咗粒新電。',
        'fr': 'L’horloge murale de la pièce s’étant arrêtée, j’ai remplacé la pile.'
    },
    'class_word_0345': {
        'ja': '今朝は風が強くてとても<ruby>寒い<rt>さむい</rt></ruby>ので、厚手のマフラーを巻いて出掛けました。',
        'en': 'The wind was strong and very cold this morning, so I wrapped a thick scarf around me before heading out.',
        'zh_TW': '今天早晨風很大非常寒冷，所以我圍了厚圍巾才出門。',
        'zh_CN': '今天早晨风很大非常寒冷，所以我围了厚围巾才出门。',
        'ko': '오늘 아침은 바람이 강해서 몹시 춥기 때문에 두꺼운 목도리를 두르고 외출했습니다.',
        'zh_HK': '今朝好大風好凍，所以我圍咗條厚頸巾先出門口。',
        'fr': 'Le vent soufflait fort et il faisait très froid ce matin, alors j’ai mis une écharpe épaisse pour sortir.'
    },
    'class_word_0346': {
        'ja': 'カフェで美味しいブレンドコーヒーを<ruby>一杯<rt>いっぱい</rt></ruby>飲んで、ほっと一息つきました。',
        'en': 'I drank a cup of delicious blended coffee at the cafe and took a relaxing breather.',
        'zh_TW': '在咖啡廳喝了一杯美味的特調咖啡，放鬆地休息了一下。',
        'zh_CN': '在咖啡厅喝了一杯美味的特调咖啡，轻松地休息了一下。',
        'ko': '카페에서 맛있는 블렌드 커피를 한 잔 마시며 한숨 돌렸습니다.',
        'zh_HK': '喺Cafe飲咗杯好味嘅咖啡，好舒服咁抖咗一陣。',
        'fr': 'J’ai bu une tasse de bon café au salon de thé et j’ai pu souffler un instant.'
    },
    'class_word_0364': {
        'ja': '大学を卒業した後は<ruby>大学院<rt>だいがくいん</rt></ruby>に進学して、人工知能の研究を深めたいです。',
        'en': 'After graduating from university, I want to proceed to graduate school to deepen my research in AI.',
        'zh_TW': '大學畢業後我想升學到研究所（大學院），深入研究人工智慧。',
        'zh_CN': '大学毕业后我想考研深造，深入研究人工智能。',
        'ko': '대학을 졸업한 후에는 대학원에 진학하여 인공지능 연구를 심화하고 싶습니다.',
        'zh_HK': '大學畢業之後想讀Master上去研究所，深入研究人工智能。',
        'fr': 'Après mes études universitaires, je souhaite poursuivre en école doctorale pour approfondir mes recherches en IA.'
    },
    'class_word_0403': {
        'ja': 'お互いの将来のために話し合いを重ね、円満に<ruby>離婚<rt>りこん</rt></ruby>することに決めました。',
        'en': 'Through repeated discussions for each other\'s future, they decided to divorce amicably.',
        'zh_TW': '為了彼此的未來反覆溝通討論，最後決定和平協議離婚。',
        'zh_CN': '为了彼此的未来反复沟通讨论，最后决定和平协议离婚。',
        'ko': '서로의 미래를 위해 대화를 거듭한 끝에 원만하게 이혼하기로 결정했습니다.',
        'zh_HK': '為咗大家嘅將來傾過好多次，最後決定和平離婚。',
        'fr': 'Après de longues discussions pour l’avenir de chacun, ils ont décidé de divorcer à l’amiable.'
    },
    'class_word_0406': {
        'ja': '近所で<ruby>火事<rt>かじ</rt></ruby>が起きたときのために、消火器の場所を日頃から確認しています。',
        'en': 'In case a fire breaks out in the neighborhood, I regularly check where the fire extinguishers are.',
        'zh_TW': '為了預防附近發生火災，平時我都會確認滅火器的擺放位置。',
        'zh_CN': '为了预防附近发生火灾，平时我都会确认灭火器的摆放位置。',
        'ko': '이웃에서 화재가 발생할 때를 대비해 평소에 소화기 위치를 확인해 두고 있습니다.',
        'zh_HK': '為咗預防附近有火警，平時都有留意滅火筒放喺邊。',
        'fr': 'En cas d’incendie dans le quartier, je vérifie régulièrement où se trouvent les extincteurs.'
    },
    'class_word_0433': {
        'ja': '同窓会で高校時代の親友と<ruby>久しぶり<rt>ひさしぶり</rt></ruby>に再会して、昔話に花が咲きました。',
        'en': 'At the class reunion, I reunited with my high school best friend after a long time and chatted excitedly about old memories.',
        'zh_TW': '在同學會上和高中時的摯友久別重逢，熱絡地聊起以前的往事。',
        'zh_CN': '在同学会上和高中时的挚友久别重逢，热络地聊起以前的往事。',
        'ko': '동창회에서 고등학교 시절 절친과 오랜만에 다시 만나 옛날이야기로 꽃을 피웠습니다.',
        'zh_HK': '喺舊生聚會見返中學最好嘅朋友，大家講返以前啲嘢傾得好開心。',
        'fr': 'Lors de la réunion des anciens élèves, j’ai retrouvé après longtemps mon meilleur ami du lycée et nous avons évoqué nos souvenirs avec émotion.'
    },
    'class_word_0449': {
        'ja': '彼は働きながら夜間の<ruby>大学院<rt>だいがくいん</rt></ruby>に通い、MBAの学位を取得しました。',
        'en': 'While working, he attended night graduate school and earned an MBA degree.',
        'zh_TW': '他一邊工作一邊就讀夜間研究所，順利取得了MBA企管碩士學位。',
        'zh_CN': '他一边工作一边就读夜间研究所，顺利取得了MBA工商管理硕士学位。',
        'ko': '그는 일하면서 야간 대학원에 다녀서 MBA 학위를 취득했습니다.',
        'zh_HK': '佢一邊返工一邊讀夜校讀Master，順利攞咗個MBA學位。',
        'fr': 'Tout en travaillant, il a suivi des cours du soir à l’université et a obtenu un MBA.'
    },
    'class_word_0462': {
        'ja': '祖父母は週末に可愛い<ruby>孫<rt>まご</rt></ruby>たちが遊びに来るのを何より楽しみにしています。',
        'en': 'My grandparents look forward to their adorable grandchildren coming over to play on the weekend above all else.',
        'zh_TW': '祖父母最期待的事情，莫過於週末看到可愛的孫子們來家裡玩了。',
        'zh_CN': '祖父母最期待的事情，莫过于周末看到可爱的孙辈们来家里玩了。',
        'ko': '조부모님은 주말에 귀여운 손주들이 놀러 오는 것을 무엇보다 기대하고 계십니다.',
        'zh_HK': '阿爺阿嫲最期待就係週末見到啲得意乖孫過嚟玩。',
        'fr': 'Mes grands-parents attendent par-dessus tout que leurs adorables petits-enfants viennent jouer le week-end.'
    },
    'class_word_0479': {
        'ja': '劇団の舞台役者たちの迫真の<ruby>演技<rt>えんぎ</rt></ruby>に、会場全体が息を呑んで見入っていました。',
        'en': 'The entire audience held their breath and watched the theater actors\' powerful, realistic performance.',
        'zh_TW': '劇團舞台演員們逼真的精彩演技，讓全場觀眾都屏息凝神地看入迷了。',
        'zh_CN': '剧团舞台演员们逼真的精彩演技，让全场观众都屏息凝神地看入迷了。',
        'ko': '극단 배우들의 박진감 넘치는 연기에 온 객석이 숨을 죽이고 몰입했습니다.',
        'zh_HK': '劇團演員逼真嘅演技，令全場觀眾都睇到停唔到口。',
        'fr': 'L’ensemble du public retenait son souffle, captivé par le jeu magistral des comédiens.'
    },
    'class_word_0505': {
        'ja': '長時間のパソコン作業で目が<ruby>少し<rt>すこし</rt></ruby>疲れたので、遠くの緑を眺めました。',
        'en': 'My eyes got a little tired from long computer work, so I gazed at the distant greenery.',
        'zh_TW': '用電腦工作很久眼睛稍微有點累，所以我看向遠方的綠色植物放鬆一下。',
        'zh_CN': '用电脑工作很久眼睛稍微有点累，所以我看向远方的绿色植物放松一下。',
        'ko': '오랜 컴퓨터 작업으로 눈이 조금 피로해서 먼 곳의 초록빛 풍경을 바라보았습니다.',
        'zh_HK': '用咗好耐電腦對眼有少少攰，所以望下遠處嘅綠色植物放鬆下。',
        'fr': 'Mes yeux étant un peu fatigués après avoir travaillé longtemps sur ordinateur, j’ai regardé la verdure au loin.'
    },
    'class_word_0525': {
        'ja': '駅の<ruby>近く<rt>ちかく</rt></ruby>に新しくできたスーパーは、品揃えが豊富でとても便利です。',
        'en': 'The new supermarket built near the station has a great selection and is very convenient.',
        'zh_TW': '車站附近新開的超市商品種類豐富，非常方便。',
        'zh_CN': '车站附近新开的超市商品种类丰富，非常方便。',
        'ko': '역 근처에 새로 생긴 마트는 상품이 다양해서 아주 편리합니다.',
        'zh_HK': '火車站附近新開嘅超級市場好多嘢買，好方便。',
        'fr': 'Le nouveau supermarché ouvert près de la gare offre un large choix et est très pratique.'
    },
    'class_word_0551': {
        'ja': '日本の<ruby>夏<rt>なつ</rt></ruby>は湿度が高くて蒸し暑いので、こまめに水分補給をします。',
        'en': 'Summer in Japan has high humidity and is muggy, so I hydrate frequently.',
        'zh_TW': '日本的夏天濕度高又悶熱，要常常補充水分以防中暑。',
        'zh_CN': '日本的夏天湿度高又闷热，要经常补充水分以防中暑。',
        'ko': '일본의 여름은 습도가 높고 무더워서 수분을 자주 섭취합니다.',
        'zh_HK': '日本嘅夏天濕氣好重又悶熱，要記得成日飲水。',
        'fr': 'L’été au Japon étant très humide et lourd, je m’hydrate fréquemment.'
    },
    'class_word_0552': {
        'ja': '<ruby>春<rt>はる</rt></ruby>になると桜の花が満開になり、街全体が明るい雰囲気に包まれます。',
        'en': 'When spring arrives, cherry blossoms bloom in full, wrapping the whole town in a cheerful atmosphere.',
        'zh_TW': '一到了春天櫻花便盛開，整個城鎮都洋溢著明亮的氣息。',
        'zh_CN': '一到了春天樱花便盛开，整个城镇都洋溢着明快的气息。',
        'ko': '봄이 되면 벚꽃이 만개하여 온 동네가 화사한 분위기로 감싸입니다.',
        'zh_HK': '一到春天櫻花開得好靚，成個城市都好有朝氣。',
        'fr': 'Quand le printemps arrive, les cerisiers sont en pleine floraison et enveloppent la ville d’une atmosphère lumineuse.'
    },
    'class_word_0561': {
        'ja': '遠くに住んでいる祖母の誕生日に、感謝の手紙とプレゼントを<ruby>送<rt>おく</rt></ruby>りました。',
        'en': 'For my grandmother who lives far away, I sent a thank-you letter and a birthday gift.',
        'zh_TW': '在住在遠方的祖母生日時，我寄了感謝信和生日禮物給她。',
        'zh_CN': '在住在远方的祖母生日时，我寄了感谢信和生日礼物给她。',
        'ko': '멀리 사시는 할머니의 생신에 감사의 편지와 선물을 보냈습니다.',
        'zh_HK': '趁住住喺外國嘅阿婆生日，我寄咗封感謝信同生日禮物畀佢。',
        'fr': 'Pour l’anniversaire de ma grand-mère qui habite loin, je lui ai envoyé une lettre de remerciement et un cadeau.'
    },
    'class_word_0564': {
        'ja': '歩きながらスマホを操作するのは危険なので、絶対に<ruby>駄目<rt>だめ</rt></ruby>ですよ。',
        'en': 'Using your smartphone while walking is dangerous, so you really must not do it.',
        'zh_TW': '邊走路邊滑手機非常危險，絕對不可以這樣做喔。',
        'zh_CN': '边走路边看手机非常危险，绝对不可以这样做哦。',
        'ko': '걸어가면서 스마트폰을 만지는 것은 위험하므로 절대 안 돼요.',
        'zh_HK': '一路行一路玩電話好危險㗎，千祈唔好咁做。',
        'fr': 'Utiliser son téléphone en marchant est dangereux, c’est strictement interdit.'
    },
    'class_word_0576': {
        'ja': '厳しい<ruby>冬<rt>ふゆ</rt></ruby>の寒さの中、温泉に入って雪景色を眺めるのは格別です。',
        'en': 'In the bitter cold of winter, soaking in a hot spring while gazing at the snowscape is truly exceptional.',
        'zh_TW': '在嚴寒的冬季裡，泡在溫泉中欣賞雪景真是格外享受。',
        'zh_CN': '在严寒的冬季里，泡在温泉中欣赏雪景真是格外享受。',
        'ko': '추운 겨울의 날씨 속에 온천에 몸을 담그고 설경을 바라보는 것은 각별합니다.',
        'zh_HK': '喺凍冰冰嘅冬天一路浸溫泉一路睇雪景，真係頂級享受。',
        'fr': 'Dans le grand froid de l’hiver, se prélasser dans un onsen en admirant la neige est un plaisir unique.'
    },
    'class_word_0586': {
        'ja': '子猫を新しくペットとして<ruby>飼<rt>か</rt></ruby>い始めたので、毎日のお世話が楽しいです。',
        'en': 'Since I started keeping a kitten as a new pet, taking care of it every day is so much fun.',
        'zh_TW': '家裡新養了一隻小貓當寵物，每天照顧牠都覺得好開心。',
        'zh_CN': '家里新养了一只小猫当宠物，每天照顾它都觉得好开心。',
        'ko': '새로 아기 고양이를 반려동물로 키우기 시작해서 매일 돌보는 것이 즐겁습니다.',
        'zh_HK': '屋企新養咗隻貓仔做寵物，每日照顧佢都好開心。',
        'fr': 'Depuis que j’ai adopté un chaton, c’est un plaisir de m’en occuper au quotidien.'
    },
    'class_word_0598': {
        'ja': '低気圧が近づいてひどい<ruby>頭痛<rt>ずつう</rt></ruby>がするので、暗い静かな部屋で横になります。',
        'en': 'As low pressure approaches I have a bad headache, so I will lie down in a dark, quiet room.',
        'zh_TW': '低氣壓接近導致嚴重的頭痛，我打算在安靜昏暗的房間裡躺下休息。',
        'zh_CN': '低气压接近导致严重的头痛，我打算在安静昏暗的房间里躺下休息。',
        'ko': '기압이 낮아져 심한 두통이 오기 때문에 어둡고 조용한 방에서 눕겠습니다.',
        'zh_HK': '天氣轉低氣壓搞到頭痛得好辛苦，我要喺間靜啲黑啲嘅房度瞓陣。',
        'fr': 'Avec la baisse de pression j’ai un violent mal de tête, je vais m’allonger dans une pièce sombre et calme.'
    },
    'class_word_0605': {
        'ja': '努力を続ければ、苦手な日本語の会話も自然と上手に<ruby>なる<rt>なる</rt></ruby>はずです。',
        'en': 'If you keep up the effort, even difficult Japanese conversations will naturally become fluent.',
        'zh_TW': '只要持續努力，原本不擅長的日語對話自然也會變得流利上手。',
        'zh_CN': '只要持续努力，原本不擅长的日语对话自然也会变得熟练自如。',
        'ko': '노력을 계속한다면 서툴렀던 일본어 회화도 자연스레 능숙해질 것입니다.',
        'zh_HK': '只要肯繼續努力，原本唔熟嘅日文對話自然會講得越嚟越好。',
        'fr': 'Si l’on poursuit ses efforts, même la conversation en japonais finira par devenir naturelle.'
    },
    'class_word_0607': {
        'ja': '雷雨の影響で突然<ruby>停電<rt>ていでん</rt></ruby>になったので、懐中電灯とロウソクを探しました。',
        'en': 'Because the thunderstorm caused a sudden power outage, I looked for a flashlight and candles.',
        'zh_TW': '受到雷雨的影響突然停電了，我趕忙找出手電筒和蠟燭。',
        'zh_CN': '受雷雨影响突然停电了，我赶忙找出便携手电和蜡烛。',
        'ko': '뇌우의 영향으로 갑자기 정전이 되어 손전등과 양초를 찾았습니다.',
        'zh_HK': '雷暴影響突然之間停電，拿拿臨搵支電筒同蠟燭出嚟。',
        'fr': 'À cause de l’orage une coupure de courant s’est produite, j’ai donc cherché une lampe torche et des bougies.'
    },
    'class_word_0851': {
        'ja': '花粉の季節になると、目のかゆみや<ruby>くしゃみ<rt>くしゃみ</rt></ruby>が止まらなくなります。',
        'en': 'During the pollen season, my itchy eyes and sneezing won\'t stop.',
        'zh_TW': '一到花粉季，眼睛發癢和打噴嚏就停不下來。',
        'zh_CN': '一到花粉季，眼睛发痒和打喷嚏就停不下来。',
        'ko': '꽃가루 철이 되면 눈 가려움과 재채기가 멈추지 않습니다.',
        'zh_HK': '一到花粉季對眼好痕又係咁打乞嗤，停都停唔到。',
        'fr': 'Pendant la saison des pollens, les démangeaisons des yeux et les éternuements ne s’arrêtent plus.'
    },
    'class_word_0910': {
        'ja': '自分の意見ばかり押し通そうとするのは、少し<ruby>わがまま<rt>わがまま</rt></ruby>に見えてしまいますよ。',
        'en': 'Insisting only on your own opinion can make you look a bit selfish.',
        'zh_TW': '只顧著強加自己的意見，看起來會有點任性自私喔。',
        'zh_CN': '只顾着强加自己的意见，看起来会有点任性自私哦。',
        'ko': '자기 의견만 고집하는 것은 조금 제멋대로이고 이기적으로 보일 수 있어요.',
        'zh_HK': '成日淨係堅持自己諗法，會畀人覺得你有啲任性㗎。',
        'fr': 'Ne vouloir imposer que son avis peut sembler un peu capricieux.'
    },
    'class_word_1063': {
        'ja': '面接の場では、あまり<ruby>派手<rt>はで</rt></ruby>な色のスーツよりも落ち着いたネイビーが無難です。',
        'en': 'For interviews, a subdued navy suit is safer than an overly flashy colored one.',
        'zh_TW': '面試場合與其穿太過花俏鮮豔的西裝，低調沉穩的深藍色比較穩妥。',
        'zh_CN': '面试场合与其穿太过花哨鲜艳的西装，低调沉稳的深蓝色比较稳妥。',
        'ko': '면접 자리에서는 너무 화려한 색의 정장보다는 차분한 네이비색이 무난합니다.',
        'zh_HK': '去見工面試嗰陣，與其著咁花巧嘅西裝，不如著斯文嘅深藍色比較穩陣。',
        'fr': 'Pour un entretien, un costume bleu marine sobre est préférable à des couleurs trop voyantes.'
    },
    'class_word_1098': {
        'ja': '困難な状況でも安易に<ruby>逃げる<rt>にげる</rt></ruby>のではなく、正面から立ち向かいたいです。',
        'en': 'Even in difficult situations, rather than easily running away, I want to face it head-on.',
        'zh_TW': '即使身處逆境，我也不想輕易逃避，而是想正面勇敢迎擊。',
        'zh_CN': '即使身处逆境，我也不想轻易逃避，而是想正面勇敢迎击。',
        'ko': '어려운 상황에서도 쉽게 도망치지 않고 정면으로 맞서고 싶습니다.',
        'zh_HK': '就算遇到困難都唔想求其逃避，想正面去面對。',
        'fr': 'Même dans les situations difficiles, plutôt que de fuir facilement, je veux faire face avec courage.'
    },
    'class_word_1103': {
        'ja': '映画のクライマックスでの主演女優の涙の<ruby>演技<rt>えんぎ</rt></ruby>に、深く心を打たれました。',
        'en': 'I was deeply touched by the lead actress\'s tearful acting at the climax of the film.',
        'zh_TW': '電影高潮處女主角流淚的精湛演技，深深打動了我的心。',
        'zh_CN': '电影高潮处女主角流泪的精湛演技，深深打动了我的心。',
        'ko': '영화 클라이맥스에서 주연 여배우의 눈물 연기에 깊은 감동을 받았습니다.',
        'zh_HK': '套戲去到高潮位個女主角喊嗰幕戲真係好逼真，好打動人心。',
        'fr': 'J’ai été profondément ému par le jeu en larmes de l’actrice principale lors du dénouement du film.'
    },
    'class_word_1153': {
        'ja': '重そうな旅行カバンですね。階段の上まで私が<ruby>持つ<rt>もつ</rt></ruby>ので貸してください。',
        'en': 'That looks like a heavy travel suitcase. Let me carry it for you to the top of the stairs.',
        'zh_TW': '這個行李箱看起來很重呢。我幫你提到樓梯上方，請交給我吧。',
        'zh_CN': '这个行李箱看起来很重呢。我帮你提到楼梯上方，请交给我吧。',
        'ko': '무거워 보이는 캐리어네요. 계단 위까지 제가 들 테니 건네주세요.',
        'zh_HK': '個旅行喼好似好重咁喎，等我幫你拎上去樓梯頂啦。',
        'fr': 'Cette valise a l’air lourde. Laissez-moi la porter pour vous jusqu’en haut des escaliers.'
    },
    'class_word_1154': {
        'ja': '春の庭に色鮮やかなチューリップの<ruby>花<rt>はな</rt></ruby>がたくさん咲いていて綺麗です。',
        'en': 'In the spring garden, lots of colorful tulips are blooming beautifully.',
        'zh_TW': '春天的花園裡盛開著許多色彩繽紛的鬱金香花，真漂亮。',
        'zh_CN': '春天的花园里盛开着许多色彩缤纷的郁金香花，真漂亮。',
        'ko': '봄 정원에 다채로운 색상의 튤립 꽃이 가득 피어 있어 아름답습니다.',
        'zh_HK': '春天嘅花園開咗好多五顏六色嘅鬱金香花，好靚。',
        'fr': 'Dans le jardin printanier, de nombreuses tulipes colorées fleurissent magnifiquement.'
    },
    'class_word_1156': {
        'ja': '夏場の運動中は、<ruby>喉<rt>のど</rt></ruby>が渇く前にこまめに冷たいお茶を飲んで熱中症を防ぎます。',
        'en': 'During summer exercise, drink cold tea frequently before getting thirsty to prevent heatstroke.',
        'zh_TW': '夏天運動時要在口渴之前就頻繁補充冷茶，以防中暑。',
        'zh_CN': '夏天运动时要在口渴之前就频繁补充冷茶，以防中暑。',
        'ko': '여름철 운동 중에는 목이 마르기 전에 시원한 차를 자주 마셔 열사병을 예방합니다.',
        'zh_HK': '夏天做運動嗰陣，趁口渴之前就要飲多啲凍茶預防中暑。',
        'fr': 'Pendant le sport en été, buvez souvent du thé frais avant d’avoir soif pour prévenir les coups de chaud.'
    },
    'class_word_1162': {
        'ja': '今日の午後は<ruby>体育<rt>たいいく</rt></ruby>の授業で、クラス対抗のバスケットボール大会がありました。',
        'en': 'This afternoon in physical education class, we had an inter-class basketball tournament.',
        'zh_TW': '今天下午的體育課舉辦了班際籃球對抗賽。',
        'zh_CN': '今天下午的体育课举办了班级篮球对抗赛。',
        'ko': '오늘 오후는 체육 수업에서 반 대항 농구 대회가 열렸습니다.',
        'zh_HK': '今日下晝體育堂搞咗個班際籃球比賽。',
        'fr': 'Cet après-midi en cours d’EPS, nous avons eu un tournoi de basket entre classes.'
    },
    'class_word_1168': {
        'ja': '遠くの友人に心を込めて手書きの<ruby>手紙<rt>てがみ</rt></ruby>を書き、ポストに投函しました。',
        'en': 'I heartfeltly wrote a handwritten letter to a friend far away and dropped it in the mailbox.',
        'zh_TW': '用心為遠方的朋友寫了一封親筆信，並投遞進了郵筒。',
        'zh_CN': '用心为远方的朋友写了一封手写信，并投递进了邮筒。',
        'ko': '멀리 있는 친구에게 정성을 담아 손편지를 써서 우체통에 넣었습니다.',
        'zh_HK': '好用心咁親手寫咗封信畀遠方嘅朋友，投咗入郵筒。',
        'fr': 'J’ai écrit avec soin une lettre manuscrite à un ami lointain et je l’ai postée.'
    },
    'class_word_1193': {
        'ja': '風邪で喉がイガイガするので、柑橘風味の美味しいのど<ruby>飴<rt>あめ</rt></ruby>を買いました。',
        'en': 'My throat feels scratchy from a cold, so I bought some tasty citrus-flavored lozenges.',
        'zh_TW': '因為感冒喉嚨癢癢的，我買了好吃的柑橘風味潤喉糖。',
        'zh_CN': '因为感冒喉咙干痒，我买了美味的柑橘风味润喉糖。',
        'ko': '감기로 목이 칼칼해서 맛있는 감귤 맛 목캔디를 샀습니다.',
        'zh_HK': '感冒搞到喉嚨好痕，所以買咗幾粒柑橘味嘅潤喉糖食。',
        'fr': 'Ayant la gorge qui gratte à cause d’un rhume, j’ai acheté de bonnes pastilles aux agrumes.'
    },
    'class_word_1224': {
        'ja': 'うちの<ruby>旦那<rt>だんな</rt></ruby>は週末になると腕を振るって美味しいパスタを作ってくれます。',
        'en': 'My husband shows off his cooking skills and makes delicious pasta on weekends.',
        'zh_TW': '我們家老公一到週末就會大展身手，煮好吃的義大利麵給全家人吃。',
        'zh_CN': '我们家老公一到周末就会大显身手，做美味的意大利面给全家人吃。',
        'ko': '우리 남편은 주말이 되면 솜씨를 발휘해 맛있는 파스타를 만들어 줍니다.',
        'zh_HK': '我老公一到週末就會大顯身手，煮好味嘅意粉畀大家食。',
        'fr': 'Mon mari met la main à la pâte le week-end et nous prépare de délicieuses pâtes.'
    },
    'class_word_1290': {
        'ja': '商店街の福引きで特等の温泉旅行券が当たって、本当に運が<ruby>いい<rt>いい</rt></ruby>です！',
        'en': 'I won the grand prize hot spring trip voucher in the shopping street lottery, I\'m so lucky!',
        'zh_TW': '在商店街的抽獎活動中抽中了特等獎溫泉旅行券，運氣真的太好了！',
        'zh_CN': '在商业街的抽奖中抽中了特等奖温泉旅行券，运气真的太好了！',
        'ko': '상점가 경품 추첨에서 특등 온천 여행권을 뽑아서 정말 운이 좋아요!',
        'zh_HK': '喺商店街抽獎抽中咗特等獎溫泉旅行券，真係好夠運！',
        'fr': 'J’ai gagné le gros lot pour un voyage en onsen à la tombola du quartier, j’ai tellement de chance !'
    },
    'class_word_1341': {
        'ja': '気分転換のために近所の公園を<ruby>散歩<rt>さんぽ</rt></ruby>したら、爽やかな気持ちになりました。',
        'en': 'Walking in the nearby park for a change of pace made me feel refreshed.',
        'zh_TW': '為了轉換心情而在附近的公園散步後，感覺神清氣爽。',
        'zh_CN': '为了转换心情而在附近的公园散步后，感觉神清气爽。',
        'ko': '기분 전환을 위해 근처 공원을 산책했더니 한결 상쾌해졌습니다.',
        'zh_HK': '去附近公園散下步轉移下心情，個人即刻精神晒。',
        'fr': 'En me promenant dans le parc voisin pour me changer les idées, je me suis senti tout revigoré.'
    },
    'class_word_1354': {
        'ja': '長時間のパソコン作業で目の奥とこめかみにズキズキと<ruby>頭痛<rt>ずつう</rt></ruby>がします。',
        'en': 'From long hours of computer work, I have a throbbing headache behind my eyes and temples.',
        'zh_TW': '由於長時間盯著電腦工作，眼眶深處與太陽穴開始隱隱頭痛。',
        'zh_CN': '由于长时间盯着电脑工作，眼眶深处与太阳穴开始隐隐头痛。',
        'ko': '오랜 컴퓨터 작업으로 눈 안쪽과 관자놀이에 욱신욱신 두통이 옵니다.',
        'zh_HK': '用咗成日電腦搞到眼同太陽穴冤冤痛，頭痛得好辛苦。',
        'fr': 'Après de longues heures devant l’ordinateur, j’ai un mal de tête lancinant derrière les yeux et aux tempes.'
    },
    'class_word_1359': {
        'ja': 'ネイティブのように流暢に日本語を話す留学生の姿を見て、とても<ruby>羨ましい<rt>うらやましい</rt></ruby>です。',
        'en': 'Seeing an exchange student speak Japanese fluently like a native, I am so envious.',
        'zh_TW': '看到留學生像母語人士一樣流暢地講日語，真的非常羨慕。',
        'zh_CN': '看到留学生像母语人士一样流利地讲日语，真的非常羡慕。',
        'ko': '원어민처럼 유창하게 일본어를 구사하는 유학생의 모습을 보니 무척 부럽습니다.',
        'zh_HK': '見到個留學生講日文講到好似日本人咁流利，真係好羨慕。',
        'fr': 'En voyant cet étudiant étranger parler japonais couramment comme un natif, je suis très envieux.'
    },
    'class_word_1360': {
        'ja': '大切に育てていた植木鉢が強風で倒れて割れてしまい、とても<ruby>悲しい<rt>かなしい</rt></ruby>気持ちです。',
        'en': 'My cherished potted plant was knocked over and broken by strong winds, making me very sad.',
        'zh_TW': '悉心照顧的盆栽被強風吹倒摔破了，心裡感到非常難過。',
        'zh_CN': '精心照顾的盆栽被强风吹倒摔破了，心里感到非常难过。',
        'ko': '소중히 기르던 화분이 강풍에 넘어져 깨져 버려서 너무 슬픕니다.',
        'zh_HK': '悉心種嘅盆栽畀大風吹冧咗跌碎晒，好心痛好傷心。',
        'fr': 'La plante en pot que je soignais avec amour est tombée avec le vent fort et s’est brisée, je suis très triste.'
    },
    'class_word_1420': {
        'ja': 'ホテルの客室に備え付けの暗証番号式の<ruby>金庫<rt>きんこ</rt></ruby>に、パスポートと現金を保管しました。',
        'en': 'I kept my passport and cash in the digital safe provided in the hotel room.',
        'zh_TW': '我將護照和現金保管在飯店客房內附設的密碼式保險箱裡。',
        'zh_CN': '我将护照和现金保管在酒店客房内附带的密码保险箱里。',
        'ko': '호텔 객실에 비치된 비밀번호 방식 금고에 여권과 현금을 보관했습니다.',
        'zh_HK': '我將護照同現金放咗喺酒店房入面嘅密碼保險箱度。',
        'fr': 'J’ai rangé mon passeport et mon argent dans le coffre-fort à code de la chambre d’hôtel.'
    },
    'class_word_1429': {
        'ja': '新しい事業に全資金を投入するのはリスクが高く、あまりに危険な<ruby>賭け<rt>かけ</rt></ruby>です。',
        'en': 'Investing all funds into a new venture is high risk and too dangerous a gamble.',
        'zh_TW': '將所有資金投入新事業風險極高，是一場過於危險的賭博。',
        'zh_CN': '将所有资金投入新事业风险极高，是一场过于危险的赌博。',
        'ko': '새로운 사업에 모든 자금을 투입하는 것은 리스크가 크고 너무나 위험한 도박입니다.',
        'zh_HK': '將所有錢掉晒落新業務風險好高，根本係一場好危險嘅賭博。',
        'fr': 'Investir tous ses fonds dans un nouveau projet comporte un risque élevé et s’avère un pari trop dangereux.'
    },
    'class_word_1434': {
        'ja': '休日に天気の良い富士山を<ruby>登る<rt>のぼる</rt></ruby>ため、しっかりトレッキングシューズを準備しました。',
        'en': 'In order to climb Mt. Fuji on a sunny holiday, I properly prepared trekking shoes.',
        'zh_TW': '為了趁放假晴天時攀登富士山，我認真準備好了登山健行鞋。',
        'zh_CN': '为了趁放假晴天时攀登富士山，我认真准备好了登山鞋。',
        'ko': '휴일에 날씨 좋은 후지산을 등반하기 위해 트레킹화를 꼼꼼히 준비했습니다.',
        'zh_HK': '為咗趁放假好天去行富士山，我準備好晒行山鞋。',
        'fr': 'Pour gravir le mont Fuji par beau temps pendant le week-end, j’ai bien préparé mes chaussures de randonnée.'
    },
    'class_word_1437': {
        'ja': '休憩時間が終わったら、速やかに自分のオフィスデスクへ<ruby>戻る<rt>もどる</rt></ruby>ようにしています。',
        'en': 'When break time is over, I make sure to return promptly to my office desk.',
        'zh_TW': '休息時間結束後，我都會迅速回到自己的辦公桌前。',
        'zh_CN': '休息时间结束后，我都会迅速回到自己的办公桌前。',
        'ko': '휴식 시간이 끝나면 신속하게 내 사무실 책상으로 복귀하고 있습니다.',
        'zh_HK': '一到Break完，我就會拿拿臨返去自己個位度做嘢。',
        'fr': 'Dès que la pause est terminée, je regagne rapidement mon bureau de travail.'
    },
    'class_word_1438': {
        'ja': '一度外出した後、忘れ物を取りに急いで家へ<ruby>戻る<rt>もどる</rt></ruby>ことになりました。',
        'en': 'After going out once, I had to hurry back home to pick up something I forgot.',
        'zh_TW': '出門之後因為有東西忘了帶，只好急忙折返回家拿。',
        'zh_CN': '出门之后因为有东西忘了带，只好急忙折返回家拿。',
        'ko': '외출한 뒤 잊은 물건을 가지러 급히 집으로 되돌아오게 되었습니다.',
        'zh_HK': '出咗門口之後發現唔記得帶嘢，唯有急急腳返屋企攞返。',
        'fr': 'Après être sorti, j’ai dû retourner chez moi en vitesse pour récupérer un oubli.'
    },
    'class_word_1447': {
        'ja': 'A: <ruby>最近<rt>さいきん</rt></ruby>、仕事の調子はどうですか？<br/>B: おかげさまで忙しいですが、とても充実しています。',
        'en': 'A: How have things been with work lately?<br/>B: Thanks to you, I\'m busy, but it\'s very fulfilling.',
        'zh_TW': 'A：最近工作狀況如何呢？<br/>B：託您的福雖然忙碌，但過得非常充實。',
        'zh_CN': 'A：最近工作情况如何呢？<br/>B：托您的福虽然忙碌，但过得非常充实。',
        'ko': 'A: 최근 일은 어떠신가요?<br/>B: 덕분에 바쁘지만 아주 보람차게 지내고 있습니다.',
        'zh_HK': 'A：最近做嘢點呀？<br/>B：托賴雖然忙，但係過得好充實。',
        'fr': 'A : Comment ça se passe au travail ces derniers temps ?<br/>B : Grâce à vous je suis bien occupé, mais c’est très enrichissant.'
    },
    'class_word_1450': {
        'ja': '世界中を旅しながらリモートで自由に働いている友人を見て、とても<ruby>羨ましい<rt>うらやましい</rt></ruby>です。',
        'en': 'Seeing my friend who works freely remotely while traveling the world, I am so envious.',
        'zh_TW': '看到朋友一邊環遊世界一邊遠端自由工作，真讓人非常羨慕。',
        'zh_CN': '看到朋友一边环游世界一边远程自由工作，真让人非常羡慕。',
        'ko': '세계를 여행하며 원격으로 자유롭게 일하는 친구를 보니 너무나 부럽습니다.',
        'zh_HK': '見到個朋友一邊環遊世界一邊Remote做嘢，真係好羨慕佢咁自由。',
        'fr': 'En voyant mon ami travailler librement à distance tout en voyageant à travers le monde, je suis tellement envieux.'
    },
    'class_word_1461': {
        'ja': '日本の伝統的な陶磁器は職人の技術が高く、耐久性と<ruby>品質<rt>ひんしつ</rt></ruby>が素晴らしいです。',
        'en': 'Japanese traditional ceramics reflect skilled craftsmanship, boasting wonderful durability and quality.',
        'zh_TW': '日本傳統陶瓷展現了職人高超的技藝，耐用度與品質都極為出色。',
        'zh_CN': '日本传统陶瓷展现了匠人高超的技艺，耐用度与品质都极为出色。',
        'ko': '일본의 전통 도자기는 장인의 기술이 뛰어나 내구성과 품질이 대단히 훌륭합니다.',
        'zh_HK': '日本傳統陶瓷工藝師傅手勢好好，耐用度同品質都好高。',
        'fr': 'La céramique traditionnelle japonaise témoigne d’un grand savoir-faire artisanal, avec une qualité et une durabilité remarquables.'
    },
    'class_word_1474': {
        'ja': '急いで駅へ走ったおかげで、発車直前の最終電車に何とか<ruby>間に合う<rt>まにあう</rt></ruby>ことができました。',
        'en': 'Thanks to running hastily to the station, I somehow managed to make it in time for the last train right before departure.',
        'zh_TW': '多虧我快步跑向車站，總算及時趕上了發車前的末班車。',
        'zh_CN': '多亏我快步跑向车站，总算及时赶上了发车前的末班车。',
        'ko': '서둘러 역으로 달린 덕분에 발차 직전 막차에 간신히 맞출 수 있었습니다.',
        'zh_HK': '好在跑去火車站，啱啱好趕得切開車前搭到尾班車。',
        'fr': 'Grâce à ma course rapide vers la gare, j’ai réussi à attraper le tout dernier train in extremis avant le départ.'
    },
    'class_word_1493': {
        'ja': 'チーム全員で力を合わせて最後まで粘り強く戦い、決勝戦に<ruby>勝つ<rt>かつ</rt></ruby>ことができました。',
        'en': 'All team members joined forces and fought persistently until the end, winning the final match.',
        'zh_TW': '全隊上下齊心協力堅持奮戰到最後一刻，終於在冠軍決賽中獲勝。',
        'zh_CN': '全队上下齐心协力坚持奋战到最后一刻，终于在冠军决赛中获胜。',
        'ko': '팀 전원이 힘을 합쳐 끝까지 끈질기게 싸워서 결승전에서 승리할 수 있었습니다.',
        'zh_HK': '全隊合力一齊搏到最後一刻，終於喺決賽贏咗。',
        'fr': 'En unissant leurs forces jusqu’au bout avec ténacité, tous les coéquipiers ont remporté la finale.'
    },
    'class_word_1499': {
        'ja': '週末はスポーツジムに通って、水泳や筋トレなどの適度な<ruby>運動<rt>うんどう</rt></ruby>を楽しんでいます。',
        'en': 'On weekends I visit the gym and enjoy moderate exercise like swimming and weight training.',
        'zh_TW': '週末我都會去健身房，享受游泳和重訓等適度運動的樂趣。',
        'zh_CN': '周末我都会去健身房，享受游泳和力量训练等适度运动的乐趣。',
        'ko': '주말에는 헬스장에 가서 수영이나 근력 운동 등 적당한 운동을 즐기고 있습니다.',
        'zh_HK': '禮拜六日我會去Gym房游水做下Gym，做下適量運動。',
        'fr': 'Le week-end, je vais à la salle de sport pour faire un peu d’exercice comme la natation ou la musculation.'
    },
    'class_word_1519': {
        'ja': 'マンションでも暮らしやすい小型犬のトイプードルを大切に<ruby>飼<rt>か</rt></ruby>っています。',
        'en': 'I cherish keeping a toy poodle, a small dog that is easy to live with even in an apartment.',
        'zh_TW': '我們家養了一隻在公寓大樓也很好照顧的小型貴賓犬。',
        'zh_CN': '我们家养了一只在公寓楼也很好照顾的小型贵宾犬。',
        'ko': '아파트에서도 키우기 편한 소형견인 토이푸들을 소중히 기르고 있습니다.',
        'zh_HK': '我哋喺屋企大廈養咗隻好易相處嘅細狗貴婦狗。',
        'fr': 'J’élève avec amour un caniche toy, un petit chien facile à vivre même en appartement.'
    },
    'class_word_1525': {
        'ja': '自転車で転んでしまいましたが、ヘルメットをかぶっていたので大きな<ruby>怪我<rt>けが</rt></ruby>はありませんでした。',
        'en': 'I fell off my bicycle, but because I was wearing a helmet, I didn\'t suffer any major injury.',
        'zh_TW': '雖然騎腳踏車摔倒了，但因為有戴安全帽，所以沒有受大傷。',
        'zh_CN': '虽然骑自行车摔倒了，但因为戴了头盔，所以没有受大伤。',
        'ko': '자전거에서 넘어졌지만 헬멧을 쓰고 있어서 큰 부상은 없었습니다.',
        'zh_HK': '踩單車跌親，不過好彩戴咗頭盔所以冇受大傷。',
        'fr': 'Je suis tombé à vélo, mais comme je portais un casque, je n’ai eu aucune blessure grave.'
    },
    'class_word_1530': {
        'ja': 'オフィスでスキャンや両面印刷が素早く行える最新型の<ruby>複合<rt>ふくごう</rt></ruby>機を導入しました。',
        'en': 'We introduced a modern multi-function printer in the office that allows quick scanning and two-sided printing.',
        'zh_TW': '辦公室引進了能夠快速掃描與雙面列印的最新型多功能事務複合機。',
        'zh_CN': '办公室引进了能够快速扫描与双面打印的最新型多功能复合机。',
        'ko': '사무실에 스캔과 양면 인쇄를 빠르게 처리할 수 있는 최신형 복합기를 도입했습니다.',
        'zh_HK': '公司買咗部最新款嘅多功能影印複合機，Scan同雙面印都快好多。',
        'fr': 'Nous avons installé au bureau une imprimante multifonction moderne permettant de numériser et d’imprimer recto-verso rapidement.'
    },
    'class_word_1559': {
        'ja': '徹夜続きで体力の<ruby>限界<rt>げんかい</rt></ruby>を感じたので、今日は仕事を切り上げてたっぷり眠ります。',
        'en': 'Feeling at the limit of my physical stamina after continuous all-nighters, I will finish work early today and get plenty of sleep.',
        'zh_TW': '連續熬夜讓我感覺體力已到達極限，今天打算早點結束工作好好睡一覺。',
        'zh_CN': '连续熬夜让我感觉体力已到达极限，今天打算早点结束工作好好睡一觉。',
        'ko': '연이은 밤샘으로 체력의 한계를 느꼈기 때문에 오늘은 일을 일찍 마치고 푹 자려고 합니다.',
        'zh_HK': '連開幾晚通頂個人體力真係到咗極限，今日要早啲收工好好瞓一覺。',
        'fr': 'Ressentant la limite de mes forces après plusieurs nuits blanches, je vais m’arrêter tôt aujourd’hui pour bien dormir.'
    },
    'class_word_1574': {
        'ja': 'A: 焼き鳥の盛り合わせは、一皿に<ruby>いくつ<rt>いくつ</rt></ruby>入っていますか？<br/>B: 全部で五本入っていますよ。',
        'en': 'A: How many pieces are in a yakitori platter plate?<br/>B: There are five skewers in total.',
        'zh_TW': 'A：請問這份綜合烤雞肉串一盤有幾個呢？<br/>B：總共盛有五串喔。',
        'zh_CN': 'A：请问这份烤鸡肉串拼盘一盘有几个呢？<br/>B：总共盛有五串哦。',
        'ko': 'A: 닭꼬치 모둠은 한 접시에 몇 개 들어 있나요?<br/>B: 총 다섯 꼬치 들어 있습니다.',
        'zh_HK': 'A：請問呢碟串燒拼盤有幾多件呀？<br/>B：總共會有五串㗎。',
        'fr': 'A : Combien de pièces contient une assiette d’assortiment de yakitori ?<br/>B : Il y a cinq brochettes au total.'
    },
    'class_word_1575': {
        'ja': 'A: すみません、このイチゴのケーキはひとつ<ruby>いくら<rt>いくら</rt></ruby>ですか？<br/>B: 税込で550円となっております。',
        'en': 'A: Excuse me, how much is this strawberry cake each?<br/>B: It is 550 yen including tax.',
        'zh_TW': 'A：不好意思，請問這個草莓蛋糕一個多少錢呢？<br/>B：含稅是550日圓。',
        'zh_CN': 'A：不好意思，请问这个草莓蛋糕一个多少钱呢？<br/>B：含税是550日元。',
        'ko': 'A: 저기요, 이 딸기 케이크는 하나에 얼마인가요?<br/>B: 세금 포함 550엔입니다.',
        'zh_HK': 'A：唔該，請問呢個士多啤梨蛋糕幾多錢一件呀？<br/>B：連稅係550円。',
        'fr': 'A : Excusez-moi, combien coûte ce gâteau aux fraises à la pièce ?<br/>B : Il est à 550 yens taxes comprises.'
    },
    'class_word_1596': {
        'ja': 'テストの解答用紙を提出する前に、記入漏れや<ruby>間違い<rt>まちがい</rt></ruby>がないか慎重に見直しました。',
        'en': 'Before submitting my test answer sheet, I carefully reviewed it to see if there were any omissions or mistakes.',
        'zh_TW': '在交出考卷答案紙之前，我仔細檢查了有沒有漏填或寫錯的地方。',
        'zh_CN': '在交出考卷答案纸之前，我仔细检查了有没有漏填或写错的地方。',
        'ko': '시험 답안지를 제출하기 전에 누락이나 실수가 없는지 신중하게 다시 검토했습니다.',
        'zh_HK': '交試卷之前，好小心咁check清楚有冇填漏或者寫錯。',
        'fr': 'Avant de rendre ma copie d’examen, j’ai vérifié attentivement qu’il n’y avait ni oubli ni erreur.'
    },
    'class_word_1603': {
        'ja': '駅に到着したら、改札口の前で待っているので携帯電話に<ruby>連絡<rt>れんらく</rt></ruby>してくださいね。',
        'en': 'When you arrive at the station, I\'ll be waiting in front of the ticket gate, so please contact my mobile phone.',
        'zh_TW': '到了車站之後我會在剪票口前等你，請打電話跟我聯絡喔。',
        'zh_CN': '到了车站之后我会在检票口前等你，请打电话跟我联系哦。',
        'ko': '역에 도착하면 개찰구 앞에서 기다리고 있을 테니 휴대폰으로 연락해 주세요.',
        'zh_HK': '去到火車站之後我會喺入閘口前面等，記得打我手機同我講。',
        'fr': 'Quand tu seras arrivé à la gare, je t’attendrai devant les portillons, alors appelle-moi sur mon portable.'
    },
    'class_word_1606': {
        'ja': '自宅から最寄り駅までは歩いて25分ほどかかり、少し<ruby>遠い<rt>とおい</rt></ruby>ので自転車を使っています。',
        'en': 'It takes about 25 minutes on foot from my home to the nearest station, which is a bit far, so I use a bicycle.',
        'zh_TW': '從家裡走到最近的車站要花大約25分鐘，有點遠，所以我平時都騎腳踏車。',
        'zh_CN': '从家里走到最近的车站要花大约25分钟，有点远，所以我平时都骑自行车。',
        'ko': '집에서 가장 가까운 역까지는 걸어서 25분 정도 걸려 조금 멀기 때문에 자전거를 이용합니다.',
        'zh_HK': '由屋企行去最近嘅車站要差唔多25分鐘有啲遠，所以我平時踩單車去。',
        'fr': 'Il faut environ 25 minutes à pied de chez moi à la gare la plus proche, c’est un peu loin, alors j’utilise un vélo.'
    },
    'class_word_1618': {
        'ja': '天気の良い週末なので、電車に乗って家族みんなで鎌倉へ観光に<ruby>行く<rt>いく</rt></ruby>予定です。',
        'en': 'Since it\'s a sunny weekend, we plan to take the train and go sightseeing in Kamakura with the whole family.',
        'zh_TW': '趁著週末天氣晴朗，我們打算全家人搭電車去鎌倉觀光。',
        'zh_CN': '趁着周末天气晴朗，我们打算全家人坐电车去镰仓观光。',
        'ko': '날씨 좋은 주말이라 전철을 타고 온 가족이 함께 가마쿠라로 관광을 갈 예정입니다.',
        'zh_HK': '趁住週末好天，打算全家人一齊搭火車去鎌倉觀光行下。',
        'fr': 'Comme il fait beau ce week-end, nous prévoyons de prendre le train pour faire du tourisme à Kamakura en famille.'
    },
    'class_word_1625': {
        'ja': '身に覚えのない不審なメールや電話は、振り込め<ruby>詐欺<rt>さぎ</rt></ruby>の手口の可能性があるので注意しましょう。',
        'en': 'Suspicious emails or phone calls you don\'t recognize may be scam tactics, so please be cautious.',
        'zh_TW': '沒有印象的可疑電子郵件或電話很有可能是匯款詐騙手法，請務必提高警覺。',
        'zh_CN': '没有印象的可疑邮件或电话很有可能是电信诈骗手法，请务必提高警觉。',
        'ko': '기억에 없는 의심스러운 이메일이나 전화는 보이스피싱 사기 수법일 수 있으니 주의합시다.',
        'zh_HK': '冇頭冇尾嘅古怪Email同電話好可能係騙案，千祈要小心。',
        'fr': 'Les e-mails ou appels suspects dont vous ne vous souvenez pas peuvent être des escroqueries, restez vigilant.'
    },
    'class_word_1638': {
        'ja': '焦らずに<ruby>ゆっくり<rt>ゆっくり</rt></ruby>時間をかけて、一つひとつの漢字の書き順を丁寧に覚えます。',
        'en': 'Without rushing, I take my time slowly and carefully learn the stroke order of each kanji.',
        'zh_TW': '不疾不徐地花時間慢慢來，仔細地記好每一個漢字的筆順。',
        'zh_CN': '不急不躁地花时间慢慢来，仔细地记好每一个汉字的笔顺。',
        'ko': '서두르지 않고 천천히 시간을 들여 한 글자 한 글자 한자의 획순을 꼼꼼히 익힙니다.',
        'zh_HK': '唔使心急慢慢嚟，好仔細咁記好每一個漢字嘅筆順。',
        'fr': 'Sans me presser, je prends mon temps pour apprendre soigneusement l’ordre des traits de chaque kanji.'
    },
    'class_word_1688': {
        'ja': '週末の休日は予定を詰め込まず、温かいお茶を飲みながら家で<ruby>のんびり<rt>のんびり</rt></ruby>過ごしました。',
        'en': 'Without crowding my holiday with plans, I spent the weekend leisurely at home drinking warm tea.',
        'zh_TW': '週末休假我不排滿行程，而是悠悠哉哉地待在家裡喝溫茶渡過。',
        'zh_CN': '周末休假我不把行程排满，而是悠闲地待在家里喝温茶度过。',
        'ko': '주말 휴일에는 일정을 빡빡하게 잡지 않고, 따뜻한 차를 마시며 집에서 느긋하게 보냈습니다.',
        'zh_HK': '放假唔排滿晒啲Schedule，留喺屋企一路飲熱茶一路好舒服咁放鬆。',
        'fr': 'Pendant le week-end, sans surcharger mon emploi du temps, je me suis détendu tranquillement à la maison avec un thé chaud.'
    },
    'class_word_1691': {
        'ja': '空港へ向かう<ruby>行き<rt>いき</rt></ruby>のバスの中で、パスポートと航空券が手元にあるか再確認しました。',
        'en': 'On the bus heading to the airport, I double-checked that I had my passport and airline tickets in hand.',
        'zh_TW': '在前往機場的去程公車上，我再次確認護照和機票是否都有帶在身邊。',
        'zh_CN': '在前往机场的去程公交车上，我再次确认护照和机票是否都有带在身边。',
        'ko': '공항으로 향하는 가는 편 버스 안에서 여권과 항공권을 잘 챙겼는지 다시 확인했습니다.',
        'zh_HK': '搭去機場架巴士上面，我check多次本護照同機票有冇帶齊。',
        'fr': 'Dans le bus en route vers l’aéroport, j’ai vérifié une nouvelle fois que j’avais bien mon passeport et mes billets d’avion.'
    },
    'class_word_1703': {
        'ja': 'テストがすべて終わって、今週末はやっと自分の時間を<ruby>自由<rt>じゆう</rt></ruby>に満喫できます。',
        'en': 'All tests are finished, and this weekend I can finally enjoy my time freely.',
        'zh_TW': '所有的考試都結束了，這個週末終於可以自由自在地享受屬於自己的時光。',
        'zh_CN': '所有的考试都结束了，这个周末终于可以自由自在地享受属于自己的时光。',
        'ko': '시험이 모두 끝나서 이번 주말에는 드디어 내 시간을 자유롭게 만끽할 수 있습니다.',
        'zh_HK': '考完晒所有試，今個禮拜六日終於可以自由自在咁享受自己嘅時間。',
        'fr': 'Tous les examens sont terminés, je peux enfin profiter librement de mon temps ce week-end.'
    },
    'class_word_1705': {
        'ja': '同じ時代に流行した音楽やアニメについて話していると、<ruby>世代<rt>せだい</rt></ruby>の近さを実感します。',
        'en': 'Talking about music and anime that were popular in the same era makes me truly feel how close our generations are.',
        'zh_TW': '聊到同一個時代流行的音樂和動畫時，真切感受到我們世代非常相近。',
        'zh_CN': '聊到同一个时代流行的音乐和动画时，真切感受到我们世代非常相近。',
        'ko': '같은 시대에 유행했던 음악이나 애니메이션에 대해 이야기하다 보면 세대가 가깝다는 것을 실감합니다.',
        'zh_HK': '講起同一年代興嘅歌同卡通片，真係即刻覺得大家係同一個世代嘅人。',
        'fr': 'En parlant des musiques et dessins animés populaires de la même époque, on ressent vraiment la proximité de nos générations.'
    },
    'class_word_1708': {
        'ja': 'スーパーの入口に近づくと、センサーが反応して<ruby>自動<rt>じどう</rt></ruby>でドアが静かに開きます。',
        'en': 'When you approach the supermarket entrance, the sensor reacts and the door opens automatically and quietly.',
        'zh_TW': '走近超市入口時，感應器會偵測反應，電動門便會靜靜地自動開啟。',
        'zh_CN': '走近超市入口时，传感器会感应反应，自动门便会静静地打开。',
        'ko': '마트 입구에 다가가면 센서가 반응하여 자동으로 문이 조용히 열립니다.',
        'zh_HK': '行近超市門口嗰陣，個感應器一感應到道自動門就會靜靜咁開。',
        'fr': 'Quand on s’approche de l’entrée du supermarché, le capteur se déclenche et la porte automatique s’ouvre en silence.'
    },
    'class_word_1724': {
        'ja': '教科書やノートがたくさん入ったリュックサックは、ずっしりと肩に食い込むほど<ruby>重い<rt>おもい</rt></ruby>です。',
        'en': 'The backpack filled with textbooks and notebooks is heavy enough to dig into my shoulders.',
        'zh_TW': '裝滿了教科書和筆記本的後背包沉甸甸的，重得都勒進肩膀裡了。',
        'zh_CN': '装满了教科书和笔记本的背包沉甸甸的，重得都勒进肩膀里了。',
        'ko': '교과서와 노트가 가득 들어 있는 백팩은 어깨를 짓누를 정도로 묵직하게 무겁습니다.',
        'zh_HK': '裝滿教科書同筆記嘅背囊好重，重到壓住個膊頭。',
        'fr': 'Le sac à dos rempli de manuels et de cahiers est si lourd qu’il s’enfonce dans les épaules.'
    },
    'class_word_1739': {
        'ja': '毎日コツコツと勉強を積み重ねた<ruby>結果<rt>けっか</rt></ruby>、JLPTの合格通知を受け取ることができました。',
        'en': 'As a result of studying diligently every day, I was able to receive a passing notice for the JLPT.',
        'zh_TW': '每天腳踏實地累積學習的成果，讓我順利收到了JLPT檢定的合格通知。',
        'zh_CN': '每天脚踏实地积累学习的成果，让我顺利收到了JLPT检定的合格通知。',
        'ko': '매일 꾸준히 공부를 쌓아 온 결과, JLPT 합격 통지서를 받을 수 있었습니다.',
        'zh_HK': '每日好勤力讀書嘅成果，終於令我收到JLPT及格合格通知書。',
        'fr': 'Grâce à mes efforts réguliers au quotidien, j’ai pu recevoir mon attestation de réussite au JLPT.'
    },
    'class_word_1770': {
        'ja': '職場の頼もしい<ruby>先輩<rt>せんぱい</rt></ruby>が、業務の手順やビジネスメールの書き方を優しく教えてくれました。',
        'en': 'A reliable senior colleague at work kindly taught me work procedures and how to write business emails.',
        'zh_TW': '職場上值得信賴的前輩非常溫柔親切地教導我業務流程與商務郵件的寫法。',
        'zh_CN': '职场上值得信赖的前辈非常温和亲切地指导我业务流程与商务邮件的写法。',
        'ko': '직장의 든든한 선배가 업무 절차와 비즈니스 이메일 작성법을 친절하게 가르쳐 주었습니다.',
        'zh_HK': '公司入面好可靠嘅前輩好細心咁教我做嘢流程同寫Business Email。',
        'fr': 'Un collègue aîné très fiable m’a gentiment appris les procédures de travail et la rédaction d’e-mails professionnels.'
    },
    'class_word_1771': {
        'ja': '新しく入社してきた熱心な<ruby>後輩<rt>こうはい</rt></ruby>に、パソコンの初期設定や社内ルールを案内しました。',
        'en': 'I guided the enthusiastic newly hired junior colleague through PC setup and internal company rules.',
        'zh_TW': '我為新進公司的熱心後輩引導說明了電腦初始設定與公司內部規範。',
        'zh_CN': '我为新进公司的热心后辈引导说明了电脑初始设置与公司内部规范。',
        'ko': '새로 입사한 열정적인 후배에게 컴퓨터 초기 설정과 사내 규정을 안내했습니다.',
        'zh_HK': '幫啱啱入職好勤力嘅後輩Set好部電腦同介紹公司嘅規矩。',
        'fr': 'J’ai guidé le jeune collègue enthousiaste nouvellement embauché pour la configuration de son ordinateur et les règles internes.'
    },
    'class_word_1775': {
        'ja': 'あのとき自分の本音を伝えておけばよかったと、今でも深く<ruby>後悔<rt>こうかい</rt></ruby>しています。',
        'en': 'I still deeply regret that I should have conveyed my true feelings back then.',
        'zh_TW': '要是當時能把自己的真心話說出口就好了，至今我依然深感後悔。',
        'zh_CN': '要是当时能把自己的真心话说出口就好了，至今我依然深感后悔。',
        'ko': '그때 내 진심을 전했더라면 좋았을 텐데 하고 지금도 깊이 후회하고 있습니다.',
        'zh_HK': '如果嗰陣時同佢講自己嘅真心話就好喇，我到依家都仲好後悔。',
        'fr': 'Je regrette encore profondément de ne pas lui avoir exprimé mes sentiments sincères à ce moment-là.'
    },
    'class_word_1776': {
        'ja': '病気が悪化して<ruby>手遅れ<rt>ておくれ</rt></ruby>になる前に、早めにクリニックを受診して検査を受けましょう。',
        'en': 'Before the illness worsens and it becomes too late, visit a clinic early and get examined.',
        'zh_TW': '在病情惡化為時已晚之前，盡早去診所就診檢查吧。',
        'zh_CN': '在病情恶化为时已晚之前，尽早就去诊所检查吧。',
        'ko': '병이 악화되어 때를 놓치기 전에 일찍 병원을 방문하여 검사를 받읍시다.',
        'zh_HK': '趁住病況仲未惡化到太遲之前，早啲去睇醫生驗身啦。',
        'fr': 'Avant que la maladie n’empire et qu’il ne soit trop tard, consultez rapidement un médecin pour faire des examens.'
    },
    'class_word_1797': {
        'ja': '緊張したときに無意識に髪の毛を触ってしまうのは、子供の頃からの<ruby>癖<rt>くせ</rt></ruby>です。',
        'en': 'Touching my hair unconsciously when nervous is a habit from my childhood.',
        'zh_TW': '緊張時會無意識地摸頭髮，是我從小到大的習慣毛病。',
        'zh_CN': '紧张时会无意识地摸头发，是我从小到大的习惯小动作。',
        'ko': '긴장했을 때 무의식적으로 머리카락을 만지는 것은 어릴 적부터의 버릇입니다.',
        'zh_HK': '緊張嗰陣會不由自主咁摸頭髮，係我由細到大嘅小動作慣性。',
        'fr': 'Me toucher inconsciemment les cheveux quand je suis stressé est une habitude qui remonte à mon enfance.'
    },
    'class_word_1827': {
        'ja': '大事な試験の本番でも決して<ruby>焦る<rt>あせる</rt></ruby>ことなく、落ち着いて問題を解き進めました。',
        'en': 'Even during the important actual exam, without panicking at all, I solved the problems calmly.',
        'zh_TW': '即便在重要考試的考場上也絕不慌張，冷靜沉著地一步步作答。',
        'zh_CN': '即便在重要考试的考场上也绝不慌乱，冷静沉着地一步步作答。',
        'ko': '중요한 실전 시험에서도 결코 조급해하지 않고 침착하게 문제를 풀어 나갔습니다.',
        'zh_HK': '就算去到考大試嘅現場我都完全冇慌，好冷靜咁慢慢做卷。',
        'fr': 'Même pendant l’examen important, sans paniquer du tout, j’ai résolu les questions calmement.'
    },
    'class_word_1828': {
        'ja': 'みんなの前で言い間違いをしてしまい、顔が真っ赤になるほど<ruby>恥ずかしい<rt>はずかしい</rt></ruby>思いをしました。',
        'en': 'I misspoke in front of everyone and felt so embarrassed that my face turned bright red.',
        'zh_TW': '在大家面前說錯話口誤，讓我臉紅到極點，感到無比難為情。',
        'zh_CN': '在大家面前说错话口误，让我脸红到极点，感到无比难为情。',
        'ko': '모두 앞에서 말실수를 해 버려 얼굴이 새빨개질 정도로 부끄러운 경험을 했습니다.',
        'zh_HK': '喺大庭廣眾面前講錯嘢，瘀到成塊面紅晒好尷尬。',
        'fr': 'J’ai fait un lapsus devant tout le monde et j’ai eu tellement honte que mon visage est devenu tout rouge.'
    },
    'class_word_1870': {
        'ja': '記念日のディナーをゆっくり過ごすため、1ヶ月前から人気レストランを<ruby>予約<rt>よやく</rt></ruby>しておきました。',
        'en': 'To spend a relaxing anniversary dinner, I reserved a popular restaurant a month in advance.',
        'zh_TW': '為了悠閒地度過紀念日晚餐，我早在一個月前就預約好了人氣熱門餐廳。',
        'zh_CN': '为了悠闲地度过纪念日晚餐，我早在一个月前就预订好了一家热门餐厅。',
        'ko': '기념일 저녁 식사를 여유롭게 즐기기 위해 한 달 전부터 인기 레스토랑을 예약해 두었습니다.',
        'zh_HK': '為咗慶祝紀念日食餐好嘅，我早喺一個月前就Book定咗好受歡迎嘅餐廳。',
        'fr': 'Pour profiter d’un dîner d’anniversaire paisible, j’ai réservé une table dans un restaurant réputé un mois à l’avance.'
    },
    'class_word_1882': {
        'ja': '昨夜、震度3の<ruby>地震<rt>じしん</rt></ruby>がありましたが、物が倒れるような被害はなくて安心しました。',
        'en': 'There was a magnitude 3 earthquake last night, but thankfully there was no damage such as fallen items.',
        'zh_TW': '昨晚發生了震度3級的地震，好在沒有物品倒塌掉落等災情，讓人鬆了一口氣。',
        'zh_CN': '昨晚发生了3级地震，好在没有物品倒塌等损失，让人松了一口气。',
        'ko': '어젯밤 진도 3의 지진이 있었지만 물건이 쓰러지는 등의 피해는 없어서 안심했습니다.',
        'zh_HK': '琴晚有微震地震，好彩冇嘢冧落嚟冇人受傷，放心晒。',
        'fr': 'Il y a eu un séisme d’intensité 3 hier soir, mais heureusement aucun objet n’est tombé et il n’y a eu aucun dégât.'
    },
    'class_word_1884': {
        'ja': '寝不足のまま急に立ち上がったら、目の前が暗くなってクラクラと<ruby>めまい<rt>めまい</rt></ruby>がしました。',
        'en': 'When I stood up abruptly with a lack of sleep, my vision went dark and I felt dizzy.',
        'zh_TW': '在睡眠不足的情況下突然站起身，眼前瞬間一片黑並感到一陣頭暈目眩。',
        'zh_CN': '在睡眠不足的情况下突然站起身，眼前瞬间一片黑并感到一阵头晕目眩。',
        'ko': '수면 부족인 상태에서 갑자기 일어섰더니 눈앞이 캄캄해지며 핑 어지럼증이 돌았습니다.',
        'zh_HK': '瞓唔夠企起身嗰下眼前一黑，個人突然之間好頭暈。',
        'fr': 'En me levant brusquement alors que je manquais de sommeil, j’ai eu un voile noir et de forts vertiges.'
    },
    'class_word_1908': {
        'ja': 'ブラッシングをしてあげたら、猫のふわふわした柔らかい<ruby>毛<rt>け</rt></ruby>がたくさん抜けました。',
        'en': 'When I brushed the cat, a lot of its soft, fluffy fur came off.',
        'zh_TW': '幫貓咪梳毛的時候，梳下了好多蓬鬆柔軟的毛髮。',
        'zh_CN': '帮猫咪梳毛的时候，梳下了好多蓬松柔软的毛发。',
        'ko': '빗질을 해 주었더니 고양이의 푹신하고 부드러운 털이 많이 빠져나왔습니다.',
        'zh_HK': '幫隻貓梳毛嗰陣，梳咗好多軟林林嘅毛出嚟。',
        'fr': 'En brossant mon chat, j’ai retiré beaucoup de ses poils doux et duveteux.'
    },
    'class_word_1910': {
        'ja': 'お会計のときに<ruby>財布<rt>さいふ</rt></ruby>を家に忘れてきたことに気づき、とても焦ってしまいました。',
        'en': 'At checkout, I realized I had left my wallet at home and panicked very much.',
        'zh_TW': '結帳買單時才發現把皮夾忘在家裡，讓我頓時慌張得不得了。',
        'zh_CN': '结账买单时才发现把钱包忘在家里，让我顿时慌乱得不得了。',
        'ko': '계산할 때 지갑을 집에 두고 온 것을 깨닫고 무척 당황했습니다.',
        'zh_HK': '去到畀錢先發現自己冇帶銀包出門口，嗰下真係好騰雞好驚。',
        'fr': 'Au moment de payer l’addition, je me suis rendu compte que j’avais oublié mon portefeuille chez moi et j’ai paniqué.'
    },
    'class_word_1946': {
        'ja': '先生に作文の文法ミスを優しく指摘してもらい、正しい表現に書き<ruby>直す<rt>なおす</rt></ruby>ことができました。',
        'en': 'The teacher kindly pointed out grammar mistakes in my essay, so I was able to rewrite them into correct expressions.',
        'zh_TW': '老師親切地指出了我作文中的文法錯誤，讓我能改寫成正確道地的表達。',
        'zh_CN': '老师亲切地指出了我作文中的语法错误，让我能改写成正确地道的表达。',
        'ko': '선생님께서 작문의 문법 실수를 친절히 지적해 주셔서 올바른 표현으로 고쳐 쓸 수 있었습니다.',
        'zh_HK': '老師好有耐性咁指出我作文入面嘅Grammar錯處，等我可以改返啱。',
        'fr': 'Le professeur m’a gentiment signalé les erreurs de grammaire dans ma rédaction, ce qui m’a permis de les corriger avec les bonnes expressions.'
    },
    'class_word_1993': {
        'ja': '未来の街がどのように発展しているか、みんなでワクワクしながら自由に<ruby>想像<rt>そうぞう</rt></ruby>を膨らませました。',
        'en': 'We excitedly and freely expanded our imaginations about how future cities will develop.',
        'zh_TW': '大家懷抱興奮的心情，自由發揮想像力，勾勒未來城市將如何發展。',
        'zh_CN': '大家怀抱兴奋的心情，自由发挥想象力，勾勒未来城市将如何发展。',
        'ko': '미래의 도시가 어떻게 발전해 있을지 모두 함께 설레며 자유롭게 상상을 펼쳤습니다.',
        'zh_HK': '大家滿懷興奮咁發揮想像力，想像未來嘅城市會變成點樣。',
        'fr': 'Tout le monde laissait libre cours à son imagination avec enthousiasme en songeant à l’évolution des villes du futur.'
    },
    'class_word_1995': {
        'ja': '霧の向こうから、遠くに見える富士山の雄大な<ruby>姿<rt>すがた</rt></ruby>がゆっくりと現れました。',
        'en': 'From beyond the mist, the majestic figure of Mt. Fuji visible in the distance slowly emerged.',
        'zh_TW': '從濃霧的另一端，遠方富士山雄偉的身影緩緩浮現了出來。',
        'zh_CN': '从浓雾的另一端，远方富士山雄伟的身影缓缓浮现了出来。',
        'ko': '안개 너머로 멀리 보이는 후지산의 웅장한 자태가 서서히 모습을 드러냈습니다.',
        'zh_HK': '喺薄霧後面，遠處富士山雄偉嘅身影慢慢浮現出嚟。',
        'fr': 'Au-delà de la brume, la silhouette majestueuse du mont Fuji au loin est apparue lentement.'
    },
    'class_word_1940': {
        'ja': '庭のあちこちに雑<ruby>草<rt>くさ</rt></ruby>が生えてきたので、週末に家族できれいに草むしりをしました。',
        'en': 'Weeds sprouted all over the garden, so on the weekend our family weeded it clean together.',
        'zh_TW': '花園各處長出了雜草，所以週末時全家人一起把雜草拔得乾乾淨淨。',
        'zh_CN': '花园各处长出了杂草，所以周末时全家人一起把杂草拔得干干净净。',
        'ko': '마당 곳곳에 잡초가 자라나서 주말에 가족이 함께 깨끗하게 풀을 뽑았습니다.',
        'zh_HK': '花園生咗好多雜草，禮拜六日全家人一齊拔乾淨啲草。',
        'fr': 'Des mauvaises herbes ayant poussé un peu partout dans le jardin, toute la famille s’est réunie ce week-end pour désherber soigneusement.'
    },
    'class_word_1859': {
        'ja': '人を恨んだり<ruby>憎む<rt>にくむ</rt></ruby>ことにエネルギーを使うより、自分の人生を前向きに楽しみたいです。',
        'en': 'Rather than using energy to resent or hate people, I want to enjoy my own life positively.',
        'zh_TW': '與其把精力花在怨恨或憎恨他人上，我更想正面積極地享受自己的人生。',
        'zh_CN': '与其把精力花在怨恨或憎恨他人上，我更想积极正向地享受自己的人生。',
        'ko': '남을 원망하거나 증오하는 데 에너지를 쓰기보다는 내 삶을 긍정적으로 즐기고 싶습니다.',
        'zh_HK': '與其嘥精力去憎人，不如積極啲享受自己嘅人生。',
        'fr': 'Plutôt que de gaspiller mon énergie à en vouloir aux autres ou à les haïr, je préfère profiter positivement de ma propre vie.'
    },
    'class_word_1528': {
        'ja': '春の訪れとともに、雪解けの大地から可愛らしい草花の芽が次々と<ruby>現れる<rt>あらわれる</rt></ruby>季節になりました。',
        'en': 'With the arrival of spring, cute flower buds emerge one after another from the thawing earth.',
        'zh_TW': '隨著春天的到來，從融雪的大地中冒出許多可愛花草新芽的季節來臨了。',
        'zh_CN': '随着春天的到来，从融雪的大地中冒出许多可爱花草新芽的季节来临了。',
        'ko': '봄의 도래와 함께 눈이 녹은 대지에서 귀여운 초목의 싹이 잇달아 돋아나는 계절이 되었습니다.',
        'zh_HK': '隨住春天嚟到，溶雪嘅泥土上面生出好多好可愛嘅嫩芽。',
        'fr': 'Avec l’arrivée du printemps, de jolies pousses de fleurs émergent successivement de la terre dégelée.'
    },
    'class_word_1802': {
        'ja': '冷蔵庫の奥に買った野菜を放置して<ruby>腐る<rt>くさる</rt></ruby>ことがないよう、こまめに消費しています。',
        'en': 'To avoid leaving purchased vegetables in the back of the fridge until they rot, I consume them regularly.',
        'zh_TW': '為了不讓買來的蔬菜放在冰箱深處腐壞爛掉，我都會定期清點盡快吃完。',
        'zh_CN': '为了不让买来的蔬菜放在冰箱深处腐烂，我都会定期清点尽快吃完。',
        'ko': '사 온 채소를 냉장고 안쪽에 방치해 썩는 일이 없도록 자주 확인하며 소비하고 있습니다.',
        'zh_HK': '為咗唔好擺到雪櫃深處啲菜爛晒，我成日都會留意住拿拿臨煮嚟食。',
        'fr': 'Pour éviter que les légumes achetés ne pourrissent au fond du réfrigérateur, je les consomme régulièrement.'
    }
}

updated_class_count = 0
for c in class_cards:
    cid = c.get('id')
    if cid in CLASS_REPLACEMENTS:
        rep = CLASS_REPLACEMENTS[cid]
        c['example'] = rep
        updated_class_count += 1

print(f"Applied fixes to {updated_class_count} cards in CLASS_VOCAB_DATA")

new_class_json = json.dumps(class_cards, ensure_ascii=False, indent=2)
with open('database/class_vocab_data.js', 'w', encoding='utf-8') as f:
    f.write(class_prefix + new_class_json + class_suffix)
with open('public/database/class_vocab_data.js', 'w', encoding='utf-8') as f:
    f.write(class_prefix + new_class_json + class_suffix)

print("✅ Saved database/class_vocab_data.js and public/database/class_vocab_data.js")
print("🎉 All shared flashcards successfully audited and repaired!")
