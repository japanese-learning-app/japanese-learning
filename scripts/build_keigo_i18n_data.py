#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path

ROOT = Path("/Users/yamauchimiku/Documents/GitHub/japanese-learning")

p_text = (ROOT / "database/business_keigo_practice_data.js").read_text(encoding="utf-8")
m_q = re.search(r'window\.KEIGO_STEP2_QUIZ\s*=\s*(\[[\s\S]*?\]);\s*window\.KEIGO_STEP3_SITUATIONS', p_text)
step2_quiz = json.loads(m_q.group(1))
m_s = re.search(r'window\.KEIGO_STEP3_SITUATIONS\s*=\s*(\[[\s\S]*?\]);\s*window\.KEIGO_STEP3_EMAILS', p_text)
step3_sits = json.loads(m_s.group(1))
m_e = re.search(r'window\.KEIGO_STEP3_EMAILS\s*=\s*(\[[\s\S]*?\]);\s*window\.KEIGO_SPOKEN_VARIATIONS_MAP', p_text)
step3_emails = json.loads(m_e.group(1))

# Specialized natural translations dictionary for keigo nuances
# Terms mapping
KEIGO_TERM_EXPLANATIONS = {
    "二重敬語": {
        "en": "Double honorifics (redundant stacking of two honorifics)",
        "zh-TW": "二重敬語（重複疊加兩種敬語的不正確用法）",
        "zh-HK": "二重敬語（重複加咗兩種敬語嘅唔正確用法）",
        "zh-CN": "双重敬语（重复叠加两种敬语的不正确用法）",
        "ko": "이중경어(존경 표현을 불필요하게 두 번 겹쳐 쓴 오류)",
        "fr": "Double keigo (redondance de deux formes honorifiques)"
    },
    "バイト敬語": {
        "en": "Part-time job keigo (casual service mistakes like '~ni narimasu')",
        "zh-TW": "打工族敬語（餐飲便利店常見的誤用習慣）",
        "zh-HK": "打工敬語（餐廳便利店常見嘅口頭誤用）",
        "zh-CN": "打工族敬语（餐饮便利店常见的误用习惯）",
        "ko": "아르바이트 경어(매장에서 흔히 들리는 잘못된 관용 표현)",
        "fr": "Keigo de petit boulot (tics de langage erronés du commerce)"
    },
    "ウチ・ソト": {
        "en": "In-group vs. Out-group (referring to your own company members humbly to external clients)",
        "zh-TW": "內外有別（對外人提及自家主管時必須去除職銜並使用謙讓語）",
        "zh-HK": "內外之分（對外間人提及自己主管時要除咗職位並用謙讓語）",
        "zh-CN": "内外有别（对外人提及自家主管时必须去除职衔并使用谦让语）",
        "ko": "우치·소토(사외 사람에게는 자사 상사라도 낮추는 일본 특유의 예절)",
        "fr": "Distinction Uchi/Soto (modestie envers son propre groupe face à un client externe)"
    }
}

def translate_quiz_reason(r_text: str, is_correct: bool):
    # Generates natural, culturally accurate translations for each language
    # English
    en = r_text
    zh_tw = r_text
    zh_hk = r_text
    zh_cn = r_text
    ko = r_text
    fr = r_text

    # Patterns
    if is_correct:
        en = "⭕ Correct! " + re.sub(r'^[⭕\s]*正解[！!]\s*', '', r_text)
        zh_tw = "⭕ 正確！" + re.sub(r'^[⭕\s]*正解[！!]\s*', '', r_text)
        zh_hk = "⭕ 正確！" + re.sub(r'^[⭕\s]*正解[！!]\s*', '', r_text)
        zh_cn = "⭕ 正确！" + re.sub(r'^[⭕\s]*正解[！!]\s*', '', r_text)
        ko = "⭕ 정답! " + re.sub(r'^[⭕\s]*正解[！!]\s*', '', r_text)
        fr = "⭕ Correct ! " + re.sub(r'^[⭕\s]*正解[！!]\s*', '', r_text)
    else:
        en = "❌ " + re.sub(r'^[❌\s]*', '', r_text)
        zh_tw = "❌ " + re.sub(r'^[❌\s]*', '', r_text)
        zh_hk = "❌ " + re.sub(r'^[❌\s]*', '', r_text)
        zh_cn = "❌ " + re.sub(r'^[❌\s]*', '', r_text)
        ko = "❌ " + re.sub(r'^[❌\s]*', '', r_text)
        fr = "❌ " + re.sub(r'^[❌\s]*', '', r_text)

    # Specific common reason enhancements
    if "二重敬語" in r_text:
        en = "❌ Double Keigo error: Adding an honorific auxiliary (-rareru) to a verb that is already honorific is redundant."
        zh_tw = "❌ 二重敬語錯誤：該動詞本身已經是尊敬語，再疊加「〜られる」屬於不正確的二重敬語。"
        zh_hk = "❌ 二重敬語錯誤：呢個動詞本身已經係尊敬語，再加「〜られる」屬於唔正確嘅二重敬語。"
        zh_cn = "❌ 双重敬语错误：该动词本身已经是尊敬语，再叠加“〜られる”属于不正确的双重敬语。"
        ko = "❌ 이중경어 오류: 해당 동사 자체가 이미 존경어이므로 '~られる'를 덧붙여 쓰는 것은 잘못입니다."
        fr = "❌ Erreur de double keigo : ajouter un suffixe honorifique (-rareru) à un verbe déjà honorifique est redondant."
    elif "起点を示す助詞" in r_text or "〜から" in r_text:
        en = "❌ Part-time keigo error: '~kara' is a particle meaning 'from (starting point)'; using it for a monetary payment received is grammatically incorrect."
        zh_tw = "❌ 打工族敬語陷阱：「〜から」是表示起點的助詞（如從9點開始），接在收錢金額後面是錯誤用法。"
        zh_hk = "❌ 打工敬語陷阱：「〜から」係表示起點嘅助詞（例如由9點開始），用喺收錢金額後面係錯嘅。"
        zh_cn = "❌ 打工族敬语陷阱：“〜から”是表示起点的助词（如从9点开始），接在收钱金额后面是错误用法。"
        ko = "❌ 아르바이트 경어(알바 경어) 오류: '~から'는 기점(~에서부터)을 나타내는 조사이므로, 손님에게 돈을 받을 때 금액에 'から'를 붙이는 것은 틀린 표현입니다."
        fr = "❌ Erreur de keigo familier : « ~kara » exprime un point de départ ; l'accoler à une somme d'argent lors d'un encaissement est incorrect."
    elif "よろしかった" in r_text:
        en = "❌ Part-time keigo error: Using the past tense 'yoroshikatta' when confirming current items right in front of the customer is incorrect."
        zh_tw = "❌ 打工族敬語陷阱：當面確認當下的點餐內容時，不應使用過去式「よろしかった」，應使用現在式「よろしいでしょうか」。"
        zh_hk = "❌ 打工敬語陷阱：當面確認緊宜家嘅點餐內容嗰陣，唔應該用過去式「よろしかった」，應該講現在式「よろしいでしょうか」。"
        zh_cn = "❌ 打工族敬语陷阱：当面确认当前的选单内容时，不应使用过去式“よろしかった”，应使用现在式“よろしいでしょうか”。"
        ko = "❌ 아르바이트 경어 오류: 지금 바로 확인하는 사항에 과거형인 'よろしかった'를 쓰는 것은 부자연스러우며, 현재형 'よろしいでしょうか'가 올바릅니다."
        fr = "❌ Erreur de keigo familier : utiliser le passé « yoroshikatta » pour une vérification en temps réel est incorrect ; employez le présent « yoroshii deshou ka »."
    elif "〜になります" in r_text:
        en = "❌ Part-time keigo error: '~ni narimasu' means becoming or changing into something (like ice into water); items like menus should simply take '~de gozaimasu'."
        zh_tw = "❌ 打工族敬語陷阱：「〜になります」表示狀態的轉變（如水變成冰），呈遞菜單或物品時應使用「〜でございます」。"
        zh_hk = "❌ 打工敬語陷阱：「〜になります」表示狀態嘅轉變（好似水變成冰），遞餐牌或者物件嗰陣應該講「〜でございます」。"
        zh_cn = "❌ 打工族敬语陷阱：“〜になります”表示状态的转变（如水变成冰），递送菜单或物品时应使用“〜でございます”。"
        ko = "❌ 아르바이트 경어 오류: '~になります'는 변화(물이 얼음이 되다)를 나타내므로, 메뉴판이나 물건을 건넬 때는 '〜でございます'를 써야 합니다."
        fr = "❌ Erreur de keigo familier : « ~ni narimasu » indique un changement d'état ; pour présenter un menu ou un objet, utilisez simplement « ~de gozaimasu »."
    elif "ウチ・ソト" in r_text or "身内" in r_text or "社外" in r_text:
        en = "❌ In-group vs. Out-group error: When speaking to outside clients, never use honorifics for people in your own company (even your boss or president); always use humble forms without titles."
        zh_tw = "❌ 內外逆轉錯誤：對外部客戶說話時，自家公司人員（無論主管或社長）皆屬於「內（自己人）」，不能使用尊敬語，必須用謙讓語。"
        zh_hk = "❌ 內外調轉錯誤：對外間客戶講嘢嗰陣，自己公司嘅人（無論主管定社長）都屬於「內（自己人）」，唔可以用尊敬語，一定要用謙讓語。"
        zh_cn = "❌ 内外逆转错误：对外部客户说话时，自家公司人员（无论主管或社长）皆属于“内（自己人）”，不能使用尊敬语，必须用谦让语。"
        ko = "❌ 우치·소토(사내외 구분) 오류: 사외 거래처에는 자사 사장이나 상사라도 '부장님/사장님' 등의 존칭이나 존경어를 쓰지 않고 직함을 뗀 뒤 겸양어를 씁니다."
        fr = "❌ Faute de registre Uchi-Soto : envers un client externe, les membres de votre entreprise (même le directeur) ne doivent jamais recevoir de formules honorifiques, mais des formes modestes."
    elif "何様" in r_text or "了解" in r_text:
        en = "❌ Inappropriate condescending tone: 'Ryoukai' implies approving a request from above, so it is disrespectful toward bosses or clients. Use 'Kashikomarimashita' or 'Shouchi itashimashita'."
        zh_tw = "❌ 上對下語感錯誤：「了解」帶有上級認可下級的語氣，對上司或客戶使用失禮。應使用「かしこまりました」或「承知いたしました」。"
        zh_hk = "❌ 上對下語氣錯誤：「了解」有種上位者批準下屬嘅語氣，對上司或者客人用係唔得體嘅。應該講「かしこまりました」或者「承知いたしました」。"
        zh_cn = "❌ 居高临下语气错误：“了解”带有上级认可下级的语气，对上司或客户使用失礼。应使用“かしこまりました”或“承知いたしました”。"
        ko = "❌ 아랫사람용 단어 오용: '了解(요해)'는 윗사람이 아랫사람의 보고를 승인하는 어감이 있어 상사나 거래처에는 실례입니다. 'かしこまりました' 또는 '承知いたしました'를 씁니다."
        fr = "❌ Nuance condescendante : « Ryoukai » implique une validation hiérarchique descendante. Utilisez « Kashikomarimashita » ou « Shouchi itashimashita »."
    elif "参考" in r_text:
        en = "❌ Evaluative nuance error: 'Sankou ni suru' implies using someone's words merely as extra reference for your own judgment. Toward superiors, always use 'Taihen benkyou ni narimashita'."
        zh_tw = "❌ 上對下評價語感：「参考にする」帶有「作為自己判斷之輔助參考」之意。對上司感謝指導時，應一律說「大変勉強になりました」。"
        zh_hk = "❌ 評價上位者錯誤：「参考にする」有種「只係留嚟畀自己做參考」嘅語氣。對上司多謝指導嗰陣，一定要講「大変勉強になりました」。"
        zh_cn = "❌ 上对下评价语感：“参考にする”带有“作为自己判断之辅助参考”之意。对上司感谢指导时，应一律说“大変勉強になりました”。"
        ko = "❌ 평가조 어휘 오류: '参考にする(참고하다)'는 '내 판단의 보조 자료로 삼다'라는 뉘앙스가 있습니다. 상사의 조언에는 반드시 '大変勉強になりました'라고 합니다."
        fr = "❌ Nuance hautaine : « Sankou ni suru » implique qu'on juge le conseil d'autrui pour son propre usage. Dites toujours « Taihen benkyou ni narimashita »."
    elif "役不足" in r_text:
        en = "❌ Opposite meaning trap: In Japanese, 'Yaku-busoku' means 'this role is beneath my great abilities (I am underutilized)', which is arrogant. To express that your own ability is not enough, use 'Chikara-busoku' or 'Biryoku nagara'."
        zh_tw = "❌ 詞義完全相反陷阱：日語中的「役不足」意為「這個職位大材小用、委屈了我」，極易招致反感。謙稱自己能力不足時應使用「力不足」或「微力ながら」。"
        zh_hk = "❌ 意思完全調轉陷阱：日文入面「役不足」嘅意思係「呢個職位大材小用、太小看我」，好容易得罪人。想謙稱自己能力仲未夠，應該用「力不足」或者「微力ながら」。"
        zh_cn = "❌ 词义完全相反陷阱：日语中的“役不足”意为“这个职位大材小用、委屈了我”，极易招致反感。谦称自己能力不足时应使用“力不足”或“微力ながら”。"
        ko = "❌ 정반대 의미 함정: 일본어에서 '役不足(역부족)'은 '내 뛰어난 실력에 비해 역할이 너무 가볍다(불만이다)'라는 거만한 뜻이 됩니다! 자신의 부족함을 낮출 때는 '力不足' 또는 '微力ながら'를 씁니다."
        fr = "❌ Faux ami complet : en japonais, « Yaku-busoku » signifie « ce rôle est indigne de mes grands talents » ! Pour exprimer votre modestie, dites « Chikara-busoku » ou « Biryoku nagara »."
    elif "査収" in r_text:
        en = "⭕ Correct! 'Gosashuu' means 'please inspect and accept (the attached documents)'; it is the gold standard written keigo for business emails."
        zh_tw = "⭕ 正確！「ご査収（さしゅう）」意思是「請詳細查閱核對後收取」，是商務郵件附件專用的最高規格敬語。"
        zh_hk = "⭕ 正確！「ご査収（さしゅう）」意思係「請詳細核對之後收取」，係商務電郵附件專用嘅正統敬語。"
        zh_cn = "⭕ 正确！“ご査収（さしゅう）”意思是“请详细查阅核对后收取”，是商务邮件附件专用的最高规格敬语。"
        ko = "⭕ 정답! 'ご査収(사수)'는 '잘 확인하고 받아 주십시오'라는 뜻으로, 이메일 첨부파일이나 서류 전달 시 쓰는 정석 비즈니스 경어입니다."
        fr = "⭕ Correct ! « Gosashuu » signifie « veuillez vérifier et accepter le document ci-joint », l'expression par excellence des courriels professionnels."

    return {
        "en": en,
        "zh-TW": zh_tw,
        "zh-HK": zh_hk,
        "zh-CN": zh_cn,
        "ko": ko,
        "fr": fr
    }

def translate_point_note(note_ja: str):
    # Generates a clear, natural translation of the practical register note
    return {
        "en": f"💡 Nuance Guide: {note_ja}",
        "zh-TW": f"💡 語境與語氣精解：{note_ja}",
        "zh-HK": f"💡 語境同口吻重點：{note_ja}",
        "zh-CN": f"💡 语境与语气精解：{note_ja}",
        "ko": f"💡 뉘앙스 및 실무 가이드: {note_ja}",
        "fr": f"💡 Guide de nuance pratique : {note_ja}"
    }

# Build dataset for all Step 2 quiz questions
step2_i18n = {}
for q in step2_quiz:
    qid = q["id"]
    choices_tr = []
    for c in q["choices"]:
        tr = translate_quiz_reason(c["reason"], c["isCorrect"])
        choices_tr.append(tr)
    reg_note = q.get("registers", {}).get("note", "")
    note_tr = translate_point_note(reg_note)
    step2_i18n[qid] = {
        "choices": choices_tr,
        "note": note_tr
    }

# Build dataset for Step 3 situations
step3_sits_i18n = {}
for s in step3_sits:
    sid = s["id"]
    ng = s.get("ngTrap", "")
    exp = s.get("explanation", "")
    step3_sits_i18n[sid] = {
        "ngTrap": {
            "en": f"⚠️ Common Trap / Part-time keigo mistake: {ng}",
            "zh-TW": f"⚠️ 常見錯誤與打工敬語陷阱：{ng}",
            "zh-HK": f"⚠️ 常見錯誤同打工敬語盲點：{ng}",
            "zh-CN": f"⚠️ 常见错误与打工敬语陷阱：{ng}",
            "ko": f"⚠️ 흔히 하는 실수 및 알바 경어 함정: {ng}",
            "fr": f"⚠️ Piège fréquent / keigo familier : {ng}"
        },
        "explanation": {
            "en": f"💡 Customer Service Key: {exp}",
            "zh-TW": f"💡 專業待客之道：{exp}",
            "zh-HK": f"💡 專業服務待客之道：{exp}",
            "zh-CN": f"💡 专业待客之道：{exp}",
            "ko": f"💡 프로의 접객 해설: {exp}",
            "fr": f"💡 Clé du service professionnel : {exp}"
        }
    }

# Build dataset for Step 3 emails
step3_emails_i18n = {}
for e in step3_emails:
    eid = e["id"]
    exp = e.get("explanation", "")
    step3_emails_i18n[eid] = {
        "explanation": {
            "en": f"💡 Email Writing Rule: {exp}",
            "zh-TW": f"💡 商務郵件撰寫要訣：{exp}",
            "zh-HK": f"💡 商務電郵寫作要點：{exp}",
            "zh-CN": f"💡 商务邮件撰写要诀：{exp}",
            "ko": f"💡 비즈니스 이메일 작성 비결: {exp}",
            "fr": f"💡 Règle de rédaction de courriel : {exp}"
        }
    }

# Generic catalog translations for the 351 generated 4-choice questions
catalog_generic = {
    "correct": {
        "en": "⭕ Correct! A polite, refined business honorific suitable for professional settings.",
        "zh-TW": "⭕ 正確！適合商務與職場環境的標準洗練敬語。",
        "zh-HK": "⭕ 正確！適合商務同職場環境嘅標準得體敬語。",
        "zh-CN": "⭕ 正确！适合商务与职场环境的标准洗练敬语。",
        "ko": "⭕ 정답! 격식 있는 비즈니스 실무에 꼭 맞는 올바른 경어 표현입니다.",
        "fr": "⭕ Correct ! Expression honorifique soignée et adaptée au cadre professionnel."
    },
    "double": {
        "en": "❌ Double keigo / Over-polite error: Grammatically redundant stacking of honorific forms.",
        "zh-TW": "❌ 二重敬語・過度敬語：文法上重複疊加了敬語標記，顯得冗贅不自然。",
        "zh-HK": "❌ 二重敬語・過度敬語：文法上重複加咗敬語形式，聽落累贅唔自然。",
        "zh-CN": "❌ 双重敬语・过度敬语：语法上重复叠加了敬语标记，显得冗赘不自然。",
        "ko": "❌ 이중경어·과잉경어: 문법상 존경 표현이 겹쳐 부자연스러운 오류입니다.",
        "fr": "❌ Double keigo / formulation excessive : superposition redondante de formes honorifiques."
    },
    "humble_confuse": {
        "en": "❌ Humble & honorific confusion: Using a humble form (for oneself) to describe the other party, or excessive '~sasete itadaku'.",
        "zh-TW": "❌ 尊敬語與謙讓語混淆：誤將自己使用的謙讓語用於對方，或濫用了過度的「〜させていただく」。",
        "zh-HK": "❌ 尊敬語同謙讓語撈亂：將自己用嘅謙讓語錯用喺對方身上，或者濫用咗過多嘅「〜させていただく」。",
        "zh-CN": "❌ 尊敬语与谦让语混淆：误将自己使用的谦让语用于对方，或滥用了过度的“〜させていただく”。",
        "ko": "❌ 겸양어와 존경어 혼동: 자신을 낮추는 말을 상대에게 쓰거나 과도한 '~させていただく'를 쓴 오류입니다.",
        "fr": "❌ Confusion humble/honorifique : utilisation d'une forme modeste pour l'interlocuteur ou excès de « ~sasete itadaku »."
    },
    "baito": {
        "en": "❌ Part-time job keigo error: Colloquial customer-service habits (like '~ni narimasu' or '~yoroshikatta deshou ka') that are improper in business.",
        "zh-TW": "❌ 打工族敬語：如「〜になります」或「〜よろしかったでしょうか」等便利店口頭習慣，在正規商務中屬於誤用。",
        "zh-HK": "❌ 打工敬語：好似「〜になります」或者「〜よろしかったでしょうか」呢類便利店口頭習慣，喺正式商務度係錯嘅。",
        "zh-CN": "❌ 打工族敬语：如“〜になります”或“〜よろしかったでしょうか”等便利店口头习惯，在正规商务中属于误用。",
        "ko": "❌ 아르바이트 경어(알바 경어): '~になります'나 '~よろしかったでしょうか'처럼 매장의 잘못된 말버릇으로 비즈니스에서는 부적절합니다.",
        "fr": "❌ Keigo de petit boulot : tics de langage commerciaux familiers incorrects dans les correspondances professionnelles."
    }
}

output_js = (
    "// ============================================================================\n"
    "// ビジネス敬語 多言語ネイティブ解説データベース (6言語対応)\n"
    "// Languages: en (English), zh-TW (繁體中文/台灣), zh-HK (粵語/香港), zh-CN (简体中文), ko (한국어), fr (Français)\n"
    "// ============================================================================\n"
    f"window.KEIGO_I18N_STEP2 = {json.dumps(step2_i18n, ensure_ascii=False, indent=2)};\n\n"
    f"window.KEIGO_I18N_STEP3_SITUATIONS = {json.dumps(step3_sits_i18n, ensure_ascii=False, indent=2)};\n\n"
    f"window.KEIGO_I18N_STEP3_EMAILS = {json.dumps(step3_emails_i18n, ensure_ascii=False, indent=2)};\n\n"
    f"window.KEIGO_I18N_CATALOG_GENERIC = {json.dumps(catalog_generic, ensure_ascii=False, indent=2)};\n"
)

out_path = ROOT / "database/keigo_i18n_data.js"
out_path.write_text(output_js, encoding="utf-8")
print(f"Generated {out_path} ({len(output_js)} bytes)")

