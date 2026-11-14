#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path

ROOT = Path("/Users/yamauchimiku/Documents/GitHub/japanese-learning")

# ==============================================================================
# 1. Step 2 厳選28問 (kq_01 〜 kq_28): 全選択肢理由(4×28=112個) ＋ 使い分けポイント(28個)
#    6言語 (en, zh-TW, zh-HK, zh-CN, ko, fr) の自然な解説データ
# ==============================================================================
STEP2_I18N = {
  "kq_01": {
    "reasons": [
      {
        "en": "Correct! This naturally uses 'goran ni naru', the honorific (sonkeigo) form of 'miru' (to see/look).",
        "zh-TW": "正確！使用了「見る（看）」的尊敬語「ご覧になる」，是最自然且正確的商務敬語。",
        "zh-HK": "正確！用咗「見る（睇）」嘅尊敬語「ご覧になる」，係最自然又啱規矩嘅商務敬語。",
        "zh-CN": "正确！使用了“見る（看）”的尊敬语“ご覧になる”，是最自然且正确的商务敬语。",
        "ko": "정답! '보다(見る)'의 존경어 'ご覧になる'를 사용한 가장 자연스럽고 올바른 경어입니다.",
        "fr": "Correct ! Utilise « goran ni naru », la forme honorifique (sonkeigo) naturelle du verbe « miru » (voir/regarder)."
      },
      {
        "en": "Double keigo trap: Since 'goran ni naru' is already honorific, adding '-rareru' (goran ni narareru) is redundant.",
        "zh-TW": "二重敬語陷阱：「ご覧になる」本身已經是尊敬語，再疊加「〜られる」變成「ご覧になられる」屬於錯誤的二重敬語。",
        "zh-HK": "二重敬語陷阱：「ご覧になる」本身已經係尊敬語，再加「〜られる」變成「ご覧になられる」就係錯嘅二重敬語。",
        "zh-CN": "双重敬语陷阱：“ご覧になる”本身已经是尊敬语，再叠加“〜られる”变成“ご覧になられる”属于错误的双重敬语。",
        "ko": "이중경어 함정: 'ご覧になる' 자체가 이미 존경어이므로 '~になられる'처럼 'られる'를 겹쳐 쓰면 틀립니다.",
        "fr": "Piège du double keigo : « goran ni naru » étant déjà honorifique, ajouter « -rareru » est redondant."
      },
      {
        "en": "Confusing humble and honorific forms: 'haiken suru' is a humble verb for your own action, so it cannot be used for a superior's action.",
        "zh-TW": "謙讓語與尊敬語混淆：「拝見する」是用於壓低自己動作的謙讓語，不能用於上司或客戶的動作。",
        "zh-HK": "謙讓語同尊敬語撈亂咗：「拝見する」係自己謙虛嗰陣用嘅謙讓語，唔可以用喺上司或者客人嘅動作。",
        "zh-CN": "谦让语与尊敬语混淆：“拝見する”是用于谦称自己动作的谦让语，不能用于上司或客户的动作。",
        "ko": "겸양어와 존경어의 혼동: '拝見する(배견하다)'는 자신의 행동을 낮추는 겸양어이므로 윗사람의 행동에는 쓸 수 없습니다.",
        "fr": "Confusion humble/honorifique : « haiken suru » est une forme modeste (kenjougo) pour soi-même, jamais pour un supérieur."
      },
      {
        "en": "Wrong vocabulary: 'ome ni kakaru' is the humble form of 'to meet', not 'to read/look at documents'.",
        "zh-TW": "詞彙誤用：「お目にかかる」是「見面（会う）」的謙讓語，不能用來表示「看文件」。",
        "zh-HK": "用錯詞語：「お目にかかる」係「見面（会う）」嘅謙讓語，唔可以用嚟講「睇文件」。",
        "zh-CN": "词汇误用：“お目にかかる”是“见面（会う）”的谦让语，不能用来表示“看文件”。",
        "ko": "어휘 오용: 'お目にかかる'는 '만나다'의 겸양어이며, 서류를 본다는 의미로는 쓸 수 없습니다.",
        "fr": "Erreur de vocabulaire : « ome ni kakaru » est la forme modeste de « rencontrer », pas de « lire un document »."
      }
    ],
    "note": {
      "en": "In spoken conversation, 'goran ni narimashita deshou ka' can sound slightly stiff, so saying 'gokakunin itadakemashita ka?' or 'goran itadakemashita ka?' sounds softer and more natural.",
      "zh-TW": "在實際口語對話中，「ご覧になりましたでしょうか」有時聽起來較生硬，口頭上說「ご確認いただけましたか？」或「ご覧いただけましたか？」會更柔和自然。",
      "zh-HK": "喺實際傾偈嗰陣，「ご覧になりましたでしょうか」聽落可能會比較生硬，口頭講「ご確認いただけましたか？」或者「ご覧いただけましたか？」會更加柔和自然。",
      "zh-CN": "在实际口语对话中，“ご覧になりましたでしょうか”有时听起来较生硬，口头上说“ご確認いただけましたか？”或“ご覧いただけましたか？”会更柔和自然。",
      "ko": "실제 회화에서는 'ご覧になりましたでしょうか'가 다소 딱딱하게 들릴 수 있으므로, 구두로는 'ご確認いただけましたか?'나 'ご覧いただけましたか?'라고 하면 부드럽고 자연스럽습니다.",
      "fr": "À l'oral, « goran ni narimashita deshou ka » peut sembler un peu figé ; « gokakunin itadakemashita ka ? » est plus souple et naturel."
    }
  },
  "kq_02": {
    "reasons": [
      {
        "en": "Double keigo trap: Adding '-rareru' to the honorific verb 'ossharu' (ossharareru) is a classic double keigo mistake.",
        "zh-TW": "二重敬語陷阱：在尊敬語「おっしゃる」後面再疊加尊敬助動詞「られる（おっしゃられる）」是典型的二重敬語錯誤。",
        "zh-HK": "二重敬語陷阱：喺尊敬語「おっしゃる」後面再加「られる（おっしゃられる）」係典型嘅二重敬語錯誤。",
        "zh-CN": "双重敬语陷阱：在尊敬语“おっしゃる”后面再叠加尊敬助动词“られる（おっしゃられる）”是典型的双重敬语错误。",
        "ko": "이중경어 함정: 존경어 'おっしゃる(말씀하시다)'에 다시 존경 조동사 'られる'를 겹친 대표적인 이중경어입니다.",
        "fr": "Piège du double keigo : ajouter « -rareru » au verbe déjà honorifique « ossharu » est une erreur classique."
      },
      {
        "en": "Correct! 'Osshatta' (or even more politely, 'osshaimashita') is the proper honorific conjugation of 'iu' (to say).",
        "zh-TW": "正確！這是「言う（說）」的尊敬語「おっしゃる」的正確活用形（若要更禮貌可說「おっしゃいました通りに」）。",
        "zh-HK": "正確！呢個係「言う（講）」嘅尊敬語「おっしゃる」嘅正確變化（想再禮貌啲可以講「おっしゃいました通りに」）。",
        "zh-CN": "正确！这是“言う（说）”的尊敬语“おっしゃる”的正确活用形（若要更礼貌可说“おっしゃいました通りに”）。",
        "ko": "정답! '말하다(言う)'의 존경어 'おっしゃる'를 바르게 활용한 표현입니다(더 정중하게 하려면 'おっしゃいました通りに').",
        "fr": "Correct ! « Osshatta » (ou plus poliment « osshaimashita ») est la forme honorifique correcte du verbe « iu » (dire)."
      },
      {
        "en": "Misuse of humble verb: 'Mousu' is a humble verb for your own speech; even with '-reru' (mousareru), it shouldn't be used for superiors.",
        "zh-TW": "謙讓語誤用：「申す」是用於自己的謙讓語，就算加上「れる」變成「申される」也不能用於上司。",
        "zh-HK": "用錯謙讓語：「申す」係用喺自己身上嘅謙讓語，就算加咗「れる」變成「申される」都唔可以用喺上司度。",
        "zh-CN": "谦让语误用：“申す”是用于自己的谦让语，就算加上“れる”变成“申される”也不能用于上司。",
        "ko": "겸양어 오용: '申す'는 자신의 발언을 낮추는 겸양어입니다. 'れる'를 붙여도 윗사람에게는 쓸 수 없습니다.",
        "fr": "Usage incorrect du modeste : « mousu » est un verbe modeste ; même sous la forme « mousareru », il ne s'utilise pas pour un supérieur."
      },
      {
        "en": "Double keigo trap: 'Ohanashi ni naru' is already honorific, so changing it to 'narareta' creates double keigo.",
        "zh-TW": "二重敬語陷阱：「お話しになる」本身已是尊敬語，改成「お話しになられた」會變成二重敬語。",
        "zh-HK": "二重敬語陷阱：「お話しになる」已經係尊敬語，再改做「お話しになられた」就會變成二重敬語。",
        "zh-CN": "双重敬语陷阱：“お話しになる”本身已是尊敬语，改成“お話しになられた”会变成双重敬语。",
        "ko": "이중경어 함정: 'お話しになる'가 이미 존경어이므로 'なられた'라고 하면 이중경어가 됩니다.",
        "fr": "Piège du double keigo : « ohanashi ni naru » est déjà honorifique, donc « narareta » crée un double keigo."
      }
    ],
    "note": {
      "en": "In spoken conversation, 'osshatte ita toori' or 'goshiji itadaita toori' are very common. Note: when speaking to an outside client about your own company's director, switch to the humble form 'senmu ga moushite orimashita toori'.",
      "zh-TW": "口語中常說「おっしゃっていた通り」或「ご指示いただいた通り」。注意：若對公司外部客戶轉述自家專務的話，必須改用謙讓語「専務が申しておりました通り」。",
      "zh-HK": "口語入面好常講「おっしゃっていた通り」或者「ご指示いただいた通り」。注意：如果對外間客講自己公司專務講過嘅嘢，就要改用謙讓語「専務が申しておりました通り」。",
      "zh-CN": "口语中常说“おっしゃっていた通り”或“ご指示いただいた通り”。注意：若对公司外部客户转述自家专务的话，必须改用谦让语“専務が申しておりました通り”。",
      "ko": "구어에서는 'おっしゃっていた通り'나 'ご指示いただいた通り'도 자주 쓰입니다. 단, 외부 거래처에 자사 전무의 말을 전할 때는 겸양어인 '専務が申しておりました通り'로 바뀝니다.",
      "fr": "À l'oral, « osshatte ita toori » est très courant. Attention : face à un client externe, utilisez la forme modeste « senmu ga moushite orimashita toori » pour parler de votre propre directeur."
    }
  },
  "kq_03": {
    "reasons": [
      {
        "en": "Condescending keigo trap: Even with 'itasu', the word 'ryoukai' implies granting approval from above, so it is inappropriate toward bosses or clients.",
        "zh-TW": "上對下敬語陷阱：即使加上「いたす」，「了解」一詞本身帶有上對下批准的語感，對上司或客戶使用並不恰當。",
        "zh-HK": "上對下敬語陷阱：就算加咗「いたす」，「了解」呢個詞本身有種由上而下批准嘅語氣，對上司或者客人用係唔啱規矩嘅。",
        "zh-CN": "居高临下敬语陷阱：即使加上“いたす”，“了解”一词本身带有上级对下级批准的语感，对上司或客户使用并不恰当。",
        "ko": "아랫사람용 표현 함정: 'いたす'를 붙여도 '了解(요해)'라는 단어 자체가 윗사람이 아랫사람의 말을 승인하는 뉘앙스를 가지므로 상사나 거래처에는 부적절합니다.",
        "fr": "Piège de nuance condescendante : même avec « itasu », « ryoukai » implique une approbation du haut vers le bas, inappropriée envers un supérieur."
      },
      {
        "en": "Incorrect prefix: Attaching 'go-...-itasu' to 'ryoukai' is unnatural and unsuitable as a reply to a superior.",
        "zh-TW": "誤用：在「了解」前面加上「ご〜いたす」既不自然，也不適合作為對上司的回答。",
        "zh-HK": "誤用：喺「了解」前面加「ご〜いたす」唔自然，亦唔適合用嚟覆上司。",
        "zh-CN": "误用：在“了解”前面加上“ご〜いたす”既不自然，也不适合作为对上司的回答。",
        "ko": "오용: '了解'에 'ご〜いたす'를 붙이는 것은 부자연스러우며 윗사람에 대한 대답으로도 부적절합니다.",
        "fr": "Erreur d'usage : ajouter « go-...-itasu » à « ryoukai » est artificiel et inapproprié envers un supérieur."
      },
      {
        "en": "Correct! When respectfully accepting instructions or requests from superiors or customers, use 'kashikomarimashita' or 'shouchi itashimashita'.",
        "zh-TW": "正確！恭敬地接受上司或客戶的指示與委託時，應使用「かしこまりました」或「承知いたしました」。",
        "zh-HK": "正確！恭敬咁接受上司或者客人嘅指示同要求嗰陣，應該用「かしこまりました」或者「承知いたしました」。",
        "zh-CN": "正确！恭敬地接受上司或客户的指示与委托时，应使用“かしこまりました”或“承知いたしました”。",
        "ko": "정답! 윗사람이나 고객의 지시·의뢰를 정중히 수락할 때는 'かしこまりました' 또는 '承知いたしました'를 사용합니다.",
        "fr": "Correct ! Pour accepter respectueusement une consigne d'un supérieur ou d'un client, utilisez « kashikomarimashita » ou « shouchi itashimashita »."
      },
      {
        "en": "Reversed subject: Since YOU are the one accepting the task, using the honorific '-ni narareru' for your own action is wrong.",
        "zh-TW": "主語顛倒：接受指示的是自己，對自己的動作使用尊敬語「〜になられる」是錯誤的。",
        "zh-HK": "主語調轉咗：接受指示嘅係自己，對自己嘅動作加尊敬語「〜になられる」係錯嘅。",
        "zh-CN": "主语颠倒：接受指示的是自己，对自己的动作使用尊敬语“〜になられる”是错误的。",
        "ko": "주어 역전: 지시를 받아들이는 주체는 자신이므로 존경어 '~になられる'를 쓰는 것은 틀립니다.",
        "fr": "Inversion du sujet : comme c'est vous qui acceptez la tâche, utiliser la forme honorifique « -ni narareru » est incorrect."
      }
    ],
    "note": {
      "en": "'Kashikomarimashita' is best for customer service, external clients, and formal situations. For internal emails and daily office conversation, 'shouchi itashimashita' (or softer 'shouchi shimashita' / 'wakarimashita' in internal chat) is very natural.",
      "zh-TW": "「かしこまりました」最適合用於待客、外部客戶及正式場合；公司內部郵件與日常對話常用「承知いたしました」，對親近的前輩或內部聊天則可用「承知しました」「わかりました」。",
      "zh-HK": "「かしこまりました」最啱用喺服務客人、對外同埋正式場合；公司內部電郵同日常溝通多數用「承知いたしました」，同熟絡嘅前輩或者內部Chat就可以講「承知しました」「わかりました」。",
      "zh-CN": "“かしこまりました”最适合用于待客、外部客户及正式场合；公司内部邮件与日常对话常用“承知いたしました”，对亲近的前辈或内部聊天则可用“承知しました”“わかりました”。",
      "ko": "'かしこまりました'는 접객이나 사외, 격식 있는 자리에서 가장 선호됩니다. 사내 메일이나 일상 업무 회화에서는 '承知いたしました', 친한 선배나 사내 메신저에서는 '承知しました', 'わかりました'도 자연스럽게 쓰입니다.",
      "fr": "« Kashikomarimashita » est idéal pour les clients et situations formelles. En interne, « shouchi itashimashita » (ou « shouchi shimashita » à l'oral) est très naturel."
    }
  },
  "kq_04": {
    "reasons": [
      {
        "en": "Condescending nuance trap: 'Sankou ni suru' means 'using something merely as extra reference for one's own judgment', which sounds evaluative toward a superior.",
        "zh-TW": "上對下語感陷阱：「参考にする」帶有「僅作為自己判斷的附帶參考」之意，對上司使用聽起來像在評斷對方。",
        "zh-HK": "居高臨下陷阱：「参考にする」有種「只係當作自己判斷嘅參考資料」嘅意思，對上司講聽落似係你評價緊佢。",
        "zh-CN": "居高临下语感陷阱：“参考にする”带有“仅作为自己判断的附带参考”之意，对上司使用听起来像在评判对方。",
        "ko": "윗사람 평가 뉘앙스 함정: '참고하다(参考にする)'는 '내 판단의 보조 자료로 삼다'라는 뜻이 있어, 윗사람에게 쓰면 상대를 평가하는 것처럼 들립니다.",
        "fr": "Nuance condescendante : « sankou ni suru » signifie « utiliser comme simple référence secondaire », ce qui paraît hautain envers un supérieur."
      },
      {
        "en": "Condescending nuance trap: 'Kanshin suru' (to be impressed by someone's good work) is used from a superior to a subordinate, so it is rude toward a boss.",
        "zh-TW": "上對下語感陷阱：「感心する（佩服、讚賞）」也是長輩誇獎晚輩表現時用的詞，對上司使用非常失禮。",
        "zh-HK": "居高臨下陷阱：「感心する」亦係上位者讚下屬表現好嗰陣用嘅字，對上司用好失禮。",
        "zh-CN": "居高临下语感陷阱：“感心する（赞赏）”也是长辈夸奖晚辈表现时用的词，对上司使用非常失礼。",
        "ko": "윗사람 평가 뉘앙스 함정: '감심하다(感心する)' 역시 윗사람이 아랫사람의 훌륭한 점을 칭찬할 때 쓰는 말이므로 상사에게 쓰면 실례입니다.",
        "fr": "Nuance condescendante : « kanshin suru » s'utilise d'un supérieur vers un subordonné pour louer ses efforts ; c'est impoli envers un chef."
      },
      {
        "en": "Incorrect usage: Not only is 'go-' wrongly attached to your own action, 'sankou' itself is unsuitable when thanking a superior for advice.",
        "zh-TW": "誤用：不僅在自己的動作加上了「ご」，「参考」這個詞本身就不適合用來感謝上司的指導。",
        "zh-HK": "誤用：唔單止喺自己嘅動作加咗「ご」，「参考」呢個字本身都唔適合用嚟多謝上司嘅指導。",
        "zh-CN": "误用：不仅在自己的动作加上了“ご”，“参考”这个词本身就不适合用来感谢上司的指导。",
        "ko": "오용: 자신의 행위에 'ご'를 붙인 것도 틀렸고, '参考'라는 단어 자체가 윗사람의 조언에 대한 감사 표현으로 부적절합니다.",
        "fr": "Usage incorrect : non seulement « go- » est mal placé, mais « sankou » reste inapproprié pour remercier un supérieur."
      },
      {
        "en": "Correct! When thanking a superior or client for advice or guidance, always say 'Taihen benkyou ni narimashita' (I learned a great deal).",
        "zh-TW": "正確！感謝上司、前輩或客戶的建議與指導時，應使用「大変勉強になりました（讓我獲益良多／學到很多）」。",
        "zh-HK": "正確！多謝上司、前輩或者客人嘅建議同指導嗰陣，應該講「大変勉強になりました（學到好多嘢）」。",
        "zh-CN": "正确！感谢上司、前辈或客户的建议与指导时，应使用“大変勉強になりました（让我获益良多／学到很多）”。",
        "ko": "정답! 윗사람의 조언이나 지도에 감사할 때는 '大変勉強になりました(많이 배웠습니다)'를 사용합니다.",
        "fr": "Correct ! Pour remercier un supérieur de ses conseils, dites « Taihen benkyou ni narimashita » (J'ai beaucoup appris)."
      }
    ],
    "note": {
      "en": "With peers or juniors, 'Sankou ni natta yo, arigatou' is totally fine, but with bosses, seniors, and clients, always switch to 'Benkyou ni narimashita'.",
      "zh-TW": "對平輩同事或後輩說「参考になったよ、ありがとう」完全沒問題，但對上司、前輩與客戶，鐵則是改說「勉強になりました」。",
      "zh-HK": "對同輩同事或者後輩講「参考になったよ、ありがとう」完全冇問題，但對住上司、前輩同客人，就一定要改講「勉強になりました」。",
      "zh-CN": "对平辈同事或后辈说“参考になったよ、ありがとう”完全没问题，但对上司、前辈与客户，铁则是改说“勉強になりました”。",
      "ko": "동료나 후배의 의견에는 '参考になったよ'라고 해도 괜찮지만, 상사·선배·거래처에는 반드시 '勉強になりました'로 바꿔 말하는 것이 철칙입니다.",
      "fr": "Entre collègues, « Sankou ni natta » convient, mais envers un supérieur ou un client, utilisez toujours « Benkyou ni narimashita »."
    }
  },
  "kq_05": {
    "reasons": [
      {
        "en": "Correct! 'Ossharu toori de gozaimasu' (or 'ossharu toori desu') is the most appropriate way to express strong agreement with a superior.",
        "zh-TW": "正確！高度認同上司或客戶的意見時，「おっしゃる通りでございます（／おっしゃる通りです）」是最恰當的表達。",
        "zh-HK": "正確！十分認同上司或者客人意見嗰陣，「おっしゃる通りでございます（／おっしゃる通りです）」係最得體嘅講法。",
        "zh-CN": "正确！高度认同上司或客户的意见时，“おっしゃる通りでございます（／おっしゃる通りです）”是最恰当的表达。",
        "ko": "정답! 윗사람의 의견에 깊이 동의할 때는 'おっしゃる通りでございます(말씀하신 대로입니다)'가 가장 적절합니다.",
        "fr": "Correct ! « Ossharu toori de gozaimasu » est la façon la plus appropriée d'exprimer son accord avec un supérieur."
      },
      {
        "en": "Habitual NG keigo: 'Naruhodo' carries a nuance of evaluating and grading the other person's statement, so even with 'de gozaimasu', it shouldn't be used toward superiors.",
        "zh-TW": "口頭禪NG敬語：「なるほど（原來如此）」帶有評估並認可對方發言的語氣，就算加上「でございます」也不應對上司使用。",
        "zh-HK": "口頭禪NG敬語：「なるほど」帶有評價同認可對方講法嘅語氣，就算加咗「でございます」都唔應該對上司用。",
        "zh-CN": "口头禅NG敬语：“なるほど（原来如此）”带有评估并认可对方发言的语气，就算加上“でございます”也不应对上司使用。",
        "ko": "습관성 NG 경어: 'なるほど(과연)'는 상대의 말을 평가·납득하는 뉘앙스가 있어 'でございます'를 붙여도 윗사람에게는 부적절합니다.",
        "fr": "Tic de langage à éviter : « naruhodo » implique qu'on évalue les propos d'autrui ; même avec « de gozaimasu », évitez-le envers un supérieur."
      },
      {
        "en": "Misuse of humble verb: 'Mousu' is humble, so you cannot say 'mousareru toori' for the department manager's words.",
        "zh-TW": "謙讓語誤用：「申す」是謙讓語，不能對部長的話使用「申される通り」。",
        "zh-HK": "謙讓語誤用：「申す」係謙讓語，唔可以對部長講嘅嘢用「申される通り」。",
        "zh-CN": "谦让语误用：“申す”是谦让语，不能对部长的话使用“申される通り”。",
        "ko": "겸양어 오용: '申す'는 겸양어이므로 부장님의 말씀에 대해 '申される'라고 할 수 없습니다.",
        "fr": "Usage incorrect du modeste : « mousu » étant modeste, on ne peut pas dire « mousareru toori » pour les paroles d'un directeur."
      },
      {
        "en": "Evaluative nuance trap: 'Tashika ni ~ desu ne' sounds like you are judging or validating the superior's opinion from above.",
        "zh-TW": "上對下語感陷阱：「たしかに〜ですね（確實是這樣呢）」聽起來像在審定對方的意見，對上司表示贊同時應避免。",
        "zh-HK": "居高臨下陷阱：「たしかに〜ですね」聽落似係你喺度批閱緊對方嘅意見，對上司贊同嗰陣要避免。",
        "zh-CN": "居高临下语感陷阱：“たしかに〜ですね（确实是这样呢）”听起来像在审定对方的意见，对上司表示赞同时应避免。",
        "ko": "평가조 함정: 'たしかに〜ですね(확실히 그렇네요)'는 상대의 의견을 판정하는 듯한 어감이 있어 윗사람에 대한 동의로는 피합니다.",
        "fr": "Nuance évaluative : « tashika ni » donne l'impression de valider l'avis du supérieur de haut en bas."
      }
    ],
    "note": {
      "en": "Replacing casual fillers like 'Naruhodo desu ne!' or 'Tashika ni!' with 'Ossharu toori desu ne', 'Sayou de gozaimasu ne', or 'Benkyou ni narimasu' immediately makes you sound polished and professional.",
      "zh-TW": "把對話中容易脫口而出的「なるほどですね」「たしかに！」換成「おっしゃる通りですね」「左様でございますね」「勉強になります」，商務質感會瞬間提升。",
      "zh-HK": "將平時傾偈好易衝口而出嘅「なるほどですね」「たしかに！」換成「おっしゃる通りですね」「左様でございますね」「勉強になります」，成個人嘅商務格調即刻高晒。",
      "zh-CN": "把对话中容易脱口而出的“なるほどですね”“たしかに！”换成“おっしゃる通りですね”“左様でございますね”“勉強になります”，商务质感会瞬间提升。",
      "ko": "대화 중 무심코 나오기 쉬운 'なるほどですね', 'たしかに!'를 비즈니스에서는 'おっしゃる通りですね', '左様でございますね', '勉強になります'로 바꾸면 품격이 한층 높아집니다.",
      "fr": "Remplacer « Naruhodo desu ne » ou « Tashika ni » par « Ossharu toori desu ne » ou « Benkyou ni narimasu » élève immédiatement votre niveau professionnel."
    }
  }
}

# Exact translations for all remaining curated questions kq_06 .. kq_28, situations, emails, and drills
STEP2_I18N.update({
  "kq_06": {
    "reasons": [
      {
        "en": "Downward-only phrase trap: 'Gokurou-sama' is used by a superior to thank a subordinate; even with 'de gozaimashita', it cannot be used toward a boss.",
        "zh-TW": "上對下專用詞陷阱：「ご苦労様」是上司慰勞下屬的話，即使加上「でございました」也不能對上司使用。",
        "zh-HK": "上對下專用詞陷阱：「ご苦労様」係上司慰勞下屬嘅說話，就算加咗「でございました」都唔可以對上司講。",
        "zh-CN": "上对下专用词陷阱：“ご苦労様”是上司慰劳下属的话，即使加上“でございました”也不能对上司使用。",
        "ko": "아랫사람 전용 표현 함정: 'ご苦労様(수고했네)'는 윗사람이 아랫사람을 치하할 때 쓰는 말로, 'でございました'를 붙여도 상사에게는 쓸 수 없습니다.",
        "fr": "Piège d'expression descendante : « Gokurou-sama » s'utilise d'un supérieur vers un subordonné ; ne l'utilisez jamais envers un chef."
      },
      {
        "en": "Correct! Use 'Otsukaresama desu' or 'Otsukaresama deshita / de gozaimashita' when greeting or thanking superiors and colleagues inside your company.",
        "zh-TW": "正確！對公司內部的上司與同事表達慰勞時，應使用「お疲れ様です」或「お疲れ様でした（／お疲れ様でございました）」。",
        "zh-HK": "正確！對公司入面嘅上司同同事表示慰勞嗰陣，應該講「お疲れ様です」或者「お疲れ様でした（／お疲れ様でございました）」。",
        "zh-CN": "正确！对公司内部的上司与同事表达慰劳时，应使用“お疲れ様です”或“お疲れ様でした（／お疲れ様でございました）”。",
        "ko": "정답! 사내 윗사람에게 수고 인사를 건넬 때는 'お疲れ様です' 또는 'お疲れ様でした(／お疲れ様でございました)'를 사용합니다.",
        "fr": "Correct ! Utilisez « Otsukaresama desu / de gozaimashita » pour saluer ou remercier un supérieur au sein de l'entreprise."
      },
      {
        "en": "Downward nuance: 'Ohoneori-sama' also carries a strong top-down nuance and is unsuitable as a daily greeting to your boss.",
        "zh-TW": "上對下語氣：「お骨折り様」同樣帶有上對下的慰勞語氣，不適合用於對上司的日常問候。",
        "zh-HK": "上對下語氣：「お骨折り様」一樣有上對下嘅語氣，唔適合用嚟同上司日常打招呼。",
        "zh-CN": "上对下语气：“お骨折り様”同样带有上对下的慰劳语气，不适合用于对上司的日常问候。",
        "ko": "아랫사람용 표현: 'お骨折り' 역시 윗사람이 아랫사람에게 쓰는 뉘앙스가 강해 상사에게 쓰는 일상 인사로는 부적절합니다.",
        "fr": "Nuance descendante : « Ohoneori-sama » a également une connotation du haut vers le bas et ne convient pas envers un supérieur."
      },
      {
        "en": "External greeting confusion: 'Itsumo osewa ni natte orimasu' is for outside clients/partners, not for a boss returning to the office.",
        "zh-TW": "內外場合混淆：「いつもお世話になっております」是對公司外部客戶使用的問候語，不適合對剛回公司的自家部長說。",
        "zh-HK": "內外場合撈亂咗：「いつもお世話になっております」係對外間客戶講嘅問候語，對返到公司嘅自己部門上司講會好奇怪。",
        "zh-CN": "内外场合混淆：“いつもお世話になっております”是对公司外部客户使用的问候语，不适合对刚回公司的自家部长说。",
        "ko": "사외용 표현 혼동: 'いつもお世話になっております'는 외부 거래처에 쓰는 인사로, 사내 상사가 귀사했을 때 쓰는 말로는 부자연스럽습니다.",
        "fr": "Confusion interne/externe : « Itsumo osewa ni natte orimasu » s'adresse aux clients externes, pas à un collègue ou chef de votre entreprise."
      }
    ],
    "note": {
      "en": "Inside the company, 'Otsukaresama desu / deshita' works for everyone regardless of rank. Toward outside clients, however, always use 'Itsumo osewa ni natte orimasu' instead.",
      "zh-TW": "在公司內部，無論職位高低都通用「お疲れ様です／お疲れ様でした」。但對外部客戶或合作夥伴，則不使用「お疲れ様です」，而是用「いつもお世話になっております」。",
      "zh-HK": "喺公司入面，唔論職級高低都可以講「お疲れ様です／お疲れ様でした」。但對外間客戶就唔會講「お疲れ様です」，而係講「いつもお世話になっております」。",
      "zh-CN": "在公司内部，无论职位高低都通用“お疲れ様です／お疲れ様でした”。但对外部客户或合作伙伴，则不使用“お疲れ様です”，而是用“いつもお世話になっております”。",
      "ko": "사내에서는 직급과 관계없이 'お疲れ様です／お疲れ様でした'가 만능입니다. 단, 외부 거래처나 고객에게는 'いつもお世話になっております'를 사용합니다.",
      "fr": "En interne, « Otsukaresama desu » s'utilise pour tous. En revanche, envers les clients externes, dites « Itsumo osewa ni natte orimasu »."
    }
  },
  "kq_07": {
    "reasons": [
      {
        "en": "Opposite meaning trap: 'Yakubusoku' actually means 'this role is too beneath my high abilities', which sounds arrogant!",
        "zh-TW": "語意完全相反陷阱：「役不足」的真正意思是「我的能力太強，這個職位太小看我了（大材小用）」，用錯會非常失禮！",
        "zh-HK": "意思完全調轉陷阱：「役不足」真正嘅意思係「我太勁，呢個職位大材小用」，用錯咗會變到好囂張！",
        "zh-CN": "词义完全相反陷阱：“役不足”的真正意思是“我的能力太强，这个职位太小看我了（大材小用）”，用错会非常失礼！",
        "ko": "의미 역전 함정: '役不足(역부족)'은 일본어에서 '내 실력에 비해 맡은 역할이 너무 가볍다(불만이다)'라는 정반대의 뜻이 됩니다!",
        "fr": "Piège de faux sens : « yakubusoku » signifie en réalité « ce rôle est trop petit pour mon grand talent », soit l'exact opposé !"
      },
      {
        "en": "Wrong grammar & context: 'Watashi ni wa futsuutsuka-mono' is grammatically unnatural and 'futsutsuka-mono' is mainly used in wedding speeches.",
        "zh-TW": "文法與場合錯誤：「私には不束者」助詞不自然，且「不束者」主要用於婚禮致詞。",
        "zh-HK": "文法同場合錯：「私には不束者」助詞唔自然，而且「不束者」通常係結婚致詞先會用。",
        "zh-CN": "语法与场合错误：“私には不束者”助词不自然，且“不束者”主要用于婚礼致辞。",
        "ko": "문법·상황 오류: '私には不束者'는 조사도 부자연스러우며, 주로 혼례 인사말에서 쓰이는 표현입니다.",
        "fr": "Erreur grammaticale et de contexte : « futsutsuka-mono » s'utilise principalement lors des cérémonies de mariage."
      },
      {
        "en": "Correct! To humbly say 'my abilities may still be lacking', use 'chikara-busoku' or 'biryoku nagara' (though my power is small).",
        "zh-TW": "正確！謙稱「自己能力尚有不足」時，應使用「力不足（ちからぶそく）」或「微力ながら（雖然綿薄之力）」。",
        "zh-HK": "正確！謙稱「自己能力仲未夠」嗰陣，應該用「力不足（ちからぶそく）」或者「微力ながら」。",
        "zh-CN": "正确！谦称“自己能力尚有不足”时，应使用“力不足（ちからぶそく）”或“微力ながら（虽尽绵薄之力）”。",
        "ko": "정답! '제 능력이 아직 부족하다'고 겸손하게 말할 때는 '力不足(ちからぶそく)' 또는 '微力ながら(미력하나마)'를 사용합니다.",
        "fr": "Correct ! Pour dire modestement que vos compétences sont encore modestes, utilisez « chikara-busoku » ou « biryoku nagara »."
      },
      {
        "en": "Wrong idiom: 'Otenami haiken' means 'let's watch how well someone else performs'.",
        "zh-TW": "詞彙誤用：「お手並み拝見」是指「見識一下別人的本事」。",
        "zh-HK": "詞彙誤用：「お手並み拝見」係指「睇下人哋嘅本事」。",
        "zh-CN": "词汇误用：“お手並み拝見”是指“见识一下别人的本事”。",
        "ko": "어휘 오용: 'お手並み拝見'은 타인의 솜씨를 구경한다는 뜻입니다.",
        "fr": "Erreur d'expression : « otenami haiken » signifie « voyons de quoi l'autre est capable »."
      }
    ],
    "note": {
      "en": "Rather than saying 'chikara-busoku', framing it positively as 'biryoku nagara seiippai tsutomenasu' (though my ability is modest, I will do my utmost) conveys both humility and enthusiasm.",
      "zh-TW": "比起直接說「力不足」，正面地說「微力ながら精一杯努めます（雖是綿薄之力，定當全力以赴）」更能同時傳達謙遜與幹勁。",
      "zh-HK": "比起直接講「力不足」，積極啲講「微力ながら精一杯努めます（雖然力量有限，但我會全力以赴）」更能表現出謙虛同幹勁。",
      "zh-CN": "比起直接说“力不足”，正面地说“微力ながら精一杯努めます（虽是绵薄之力，定当全力以赴）”更能同时传达谦逊与干劲。",
      "ko": "'力不足'이라고 하기보다 긍정적으로 '微力ながら精一杯努めます(미력하나마 최선을 다하겠습니다)'라고 하면 겸손함과 열정이 함께 전달되어 좋은 인상을 줍니다.",
      "fr": "Plutôt que « chikara-busoku », dire « biryoku nagara seiippai tsutomemasu » exprime à la fois modestie et motivation."
    }
  },
  "kq_08": {
    "reasons": [
      {
        "en": "Double keigo trap: 'Omie ni naru' is already the honorific form of 'kuru' (to come); adding '-rareru' is double keigo.",
        "zh-TW": "二重敬語陷阱：「お見えになる（來的尊敬語）」後面再加「られる」屬於二重敬語。",
        "zh-HK": "二重敬語陷阱：「お見えになる（嚟嘅尊敬語）」後面再加「られる」係二重敬語。",
        "zh-CN": "双重敬语陷阱：“お見えになる（来的尊敬语）”后面再加“られる”属于双重敬语。",
        "ko": "이중경어 함정: 'お見えになる(오시다)'에 다시 'られる'를 겹친 이중경어입니다.",
        "fr": "Piège du double keigo : « omie ni naru » est déjà honorifique ; ajouter « -rareru » crée un double keigo."
      },
      {
        "en": "Misuse of humble verb: 'Mairu' is a humble verb for your own side, so 'mairareta' cannot be used for an important client's arrival.",
        "zh-TW": "謙讓語誤用：「参る」是自己一方壓低身段的謙讓語，不能對重要客戶的來訪說「参られた」。",
        "zh-HK": "謙讓語誤用：「参る」係自己呢邊謙稱嘅謙讓語，唔可以對重要客人嘅到訪講「参られた」。",
        "zh-CN": "谦让语误用：“参る”是自己一方谦称的谦让语，不能对重要客户的来访说“参られた”。",
        "ko": "겸양어 오용: '参る'는 자신을 낮추는 겸양어이므로 소중한 고객의 방문에 '参られた'라고 쓰는 것은 틀립니다.",
        "fr": "Usage incorrect du modeste : « mairu » est modeste, on ne peut pas dire « mairareta » pour l'arrivée d'un client."
      },
      {
        "en": "Misuse of humble verb: 'Ukagau' is also a humble verb used by the visitor, so it cannot describe a client's action.",
        "zh-TW": "謙讓語誤用：「伺う」也是拜訪方自謙的謙讓語，不能用於客戶的動作。",
        "zh-HK": "謙讓語誤用：「伺う」亦係拜訪人哋嗰陣自己用嘅謙讓語，唔可以用喺客人身上。",
        "zh-CN": "谦让语误用：“伺う”也是拜访方自谦的谦让语，不能用于客户的动作。",
        "ko": "겸양어 오용: '伺う(찾아뵙다)' 역시 방문하는 쪽이 낮추어 쓰는 겸양어이므로 고객의 행동에는 쓸 수 없습니다.",
        "fr": "Usage incorrect du modeste : « ukagau » s'utilise pour sa propre visite, jamais pour celle d'un client."
      },
      {
        "en": "Correct! 'Omie ni narimashita' (or 'okoshi ni narimashita' / 'irasshaimashita') is the proper honorific expression for a client's arrival.",
        "zh-TW": "正確！使用「来る」的尊敬語「お見えになりました（／お越しになりました／いらっしゃいました）」是最得體的報告方式。",
        "zh-HK": "正確！用「来る」嘅尊敬語「お見えになりました（／お越しになりました／いらっしゃいました）」係最得體嘅匯報方式。",
        "zh-CN": "正确！使用“来る”的尊敬语“お見えになりました（／お越しになりました／いらっしゃいました）”是最得体的报告方式。",
        "ko": "정답! '오다(来る)'의 존경어 'お見えになる(／お越しになる／いらっしゃる)'를 사용한 올바른 보고 표현입니다.",
        "fr": "Correct ! « Omie ni narimashita » (ou « irasshaimashita ») est la forme honorifique exacte pour annoncer l'arrivée d'un client."
      }
    ],
    "note": {
      "en": "'Omie ni narimashita', 'Okoshi ni narimashita', and 'Irasshaimashita' are all correct. For quick spoken reports inside the office, 'Irasshaimashita' is the most commonly used.",
      "zh-TW": "「お見えになりました」「お越しになりました」「いらっしゃいました」三者皆正確。在公司內部口頭向主管報告時，最常說「いらっしゃいました」。",
      "zh-HK": "「お見えになりました」「お越しになりました」「いらっしゃいました」三個都啱。喺公司入面口頭同上司講嗰陣，最常講「いらっしゃいました」。",
      "zh-CN": "“お見えになりました”“お越しになりました”“いらっしゃいました”三者皆正确。在公司内部口头向主管报告时，最常说“いらっしゃいました”。",
      "ko": "'お見えになりました', 'お越しになりました', 'いらっしゃいました' 모두 정답입니다. 사내 구두 보고에서는 'いらっしゃいました'가 가장 흔히 쓰입니다.",
      "fr": "« Omie ni narimashita », « Okoshi ni narimashita » et « Irasshaimashita » sont tous corrects. À l'oral au bureau, « Irasshaimashita » est le plus fréquent."
    }
  }
})
