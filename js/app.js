// Haku-sensei's Japanese Flashcards App Logic
// State management, multi-language switching, 3D card flipping, TTS speech, Quiz mode, Mylist, and Admin batch import

(function() {
  // --- State ---
  let vocabList = [];
  let students = [];
  let currentStudent = null; // null represents Guest
  let currentLang = 'en'; // default en, switches automatically per student
  let currentDeckFilter = 'all'; // 'all' (shared) or 'mine' (student specific)
  let currentCategory = 'all';
  let isReverseMode = false; // false: Front is Japanese, true: Front is Native Language
  let isCardFlipped = false;
  let currentIndex = 0;
  let currentJlptDeckLevel = 'N5'; // Selected JLPT level when playing JLPT deck
  let activeDeck = [];
  let isSearchStudyMode = false; // true when studying a specific word clicked from search results
  let isMylistStudyMode = false; // true when studying cards initiated from My List
  let mylistSet = new Set(); // store card IDs in mylist
  let mylistSortOrder = localStorage.getItem('haku_mylist_sort_order') || 'newest'; // 'newest', 'oldest', 'gojuon', 'unlearned', 'random'
  let knownSet = new Set(); // store cards marked as learned
  let isFuriganaEnabled = localStorage.getItem('haku_furigana_enabled') !== 'false'; // default true
  let isAutoAudioEnabled = localStorage.getItem('haku_auto_audio_enabled') === 'true'; // default false
  let autoAudioTimer = null; // timer for debounce / chaining

  // --- Firebase Cloud Sync Configuration ---
  const firebaseConfig = {
    apiKey: "AIzaSyBNsrBL1xRErsuOHgvI7xNs15cai-auoSE",
    authDomain: "japanese-learning-e8a53.firebaseapp.com",
    projectId: "japanese-learning-e8a53",
    storageBucket: "japanese-learning-e8a53.firebasestorage.app",
    messagingSenderId: "1052063287116",
    appId: "1:1052063287116:web:7ccf89640419c489a3f1e9"
  };

  let fbApp = null;
  let fbAuth = null;
  let fbDb = null;
  let isFirebaseReady = false;

  try {
    if (window.firebase) {
      fbApp = firebase.initializeApp(firebaseConfig);
      fbAuth = firebase.auth();
      fbDb = firebase.firestore();
      isFirebaseReady = true;
      console.log('Firebase Cloud Database initialized successfully! ☁️✨');
    }
  } catch (err) {
    console.warn('Firebase init warning:', err);
  }

  // --- Quiz State ---
  let quizPool = [];
  let quizIndex = 0;
  let quizCurrentQuestion = null;
  let quizScore = 0;

  // --- High-Fidelity TTS Speech Engine ---
  // Converts kanji sentences to pure furigana readings using <ruby><rt>furigana</rt></ruby> tags,
  // ensuring the browser's speech synthesizer never misreads words like 二重価格.
  function cleanJapaneseForSpeech(text) {
    if (!text) return '';
    let s = String(text).trim();
    // If the entire text is enclosed in parentheses, unwrap it first so it doesn't get erased
    s = s.replace(/^[（\(\[【](.*?)[）\)\]】]$/, '$1').trim();
    // 1. Remove <rt> and <rp> ruby tags so the original natural kanji text is retained intact.
    // (Inserting spaces around furigana breaks morphological parsing, causing particles like 'は' to be mispronounced as 'ha' instead of 'wa'!)
    s = s.replace(/<rt[^>]*>[\s\S]*?<\/rt>/gi, '');
    s = s.replace(/<rp[^>]*>[\s\S]*?<\/rp>/gi, '');
    // 2. Replace <br> tags with natural sentence pauses (。)
    s = s.replace(/<br\s*\/?>/gi, '。');
    // 3. Remove all remaining HTML tags without inserting spaces between kanji and particles
    s = s.replace(/<[^>]+>/g, '');
    // 4. Strip speaker labels like A: or B:
    s = s.replace(/^[ABａｂＡＢ][:：]\s*/g, '');
    s = s.replace(/[。、!?！？]\s*[ABａｂＡＢ][:：]\s*/g, '。');
    // 5. Remove parenthetical readings from longer sentences (e.g. "信号（しんごう）を渡る" -> "信号を渡る")
    // but ONLY if there is text remaining outside the parentheses!
    const stripped = s.replace(/[（\(][\u3040-\u309F\u30A0-\u30FF・ー\s、。]+[）\)]/g, '');
    if (stripped.trim().length > 0) {
      s = stripped;
    } else {
      // It was purely a reading like (ねこ), strip only the bracket characters!
      s = s.replace(/[（\(\)）]/g, '');
    }
    // 5b. Strip any foreign translations appended after Japanese punctuation (e.g. English, Hangul, French, or Chinese text)
    s = s.replace(/([。！？])\s*[a-zA-Z\u00C0-\u024F\uAC00-\uD7A3]+[\s\S]*$/, '$1');
    s = s.replace(/([。！？])\s*[\u4e00-\u9fff]{3,}[\s\S]*$/, '$1');
    // 6. Clean duplicate punctuation and extra spaces
    s = s.replace(/[。]+/g, '。');
    return s.replace(/\s+/g, ' ').trim();
  }

  const MIDORI_NEW_CARD_IDS = [
    'card_midori_yoichi', 'card_midori_jiyuu', 'card_midori_tanoshimu', 'card_midori_oukasuru',
    'card_midori_kougeki', 'card_midori_tsuuchi', 'card_midori_shitsurei', 'card_midori_shitauchi',
    'card_midori_kazoekirenai', 'card_midori_iyanaomoi', 'card_midori_ekiin', 'card_midori_taidogawarui',
    'card_midori_eikyou', 'card_midori_tanseina', 'card_midori_kaodachi', 'card_midori_soudanninoru',
    'card_midori_furinosuru', 'card_midori_nisemono', 'card_midori_honmono', 'card_midori_sagi',
    'card_midori_kuyashii', 'card_midori_kiriganai', 'card_midori_haragatatsu', 'card_midori_mukatsuku',
    'card_midori_sewawosuru', 'card_midori_shugyou', 'card_midori_mukiau', 'card_midori_ajitsuke',
    'card_midori_mukumu', 'card_midori_panpan', 'card_midori_jojoni', 'card_midori_fuyasu',
    'card_midori_kobushi', 'card_midori_bai', 'card_midori_hiwotoosu', 'card_midori_atsukau',
    'card_midori_komugiko', 'card_midori_mezurashii', 'card_midori_ijou', 'card_midori_ika',
    'card_midori_enki', 'card_midori_teiji', 'card_midori_idensuru', 'card_midori_nenreikakunin',
    'card_midori_mibunshou', 'card_midori_kaoiro', 'card_midori_saikon', 'card_midori_burikko',
    'card_midori_tsukiai', 'card_midori_toshigahanareteiru'
  ];

    const MIDORI_CURATED_CARDS = [
  {
    "id": "card_midori_yoichi",
    "word": "夜市",
    "reading": "よいち",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "night market",
      "ja": "夜市",
      "zh_TW": "夜市",
      "zh_CN": "夜市",
      "ko": "야시장",
      "zh_HK": "夜市",
      "fr": "marché de nuit"
    },
    "example": {
      "ja": "<ruby>台湾<rt>たいわん</rt></ruby>に<ruby>行<rt>い</rt></ruby>ったら、<ruby>毎晩<rt>まいばん</rt></ruby><ruby>夜市<rt>よいち</rt></ruby>でおいしいものを<ruby>食<rt>た</rt></ruby>べたいです。",
      "en": "If I go to Taiwan, I want to eat delicious food at the night market every night.",
      "zh_TW": "去台灣的話，想每晚都在夜市吃美食。",
      "zh_CN": "去台湾的话，想每晚都在夜市吃美食。",
      "ko": "대만에 가면 매일 밤 야시장에서 맛있는 음식을 먹고 싶어요.",
      "zh_HK": "去台灣嘅話，想每晚都喺夜市食好嘢。",
      "fr": "Si je vais à Taïwan, je veux manger de la bonne nourriture au marché de nuit tous les soirs."
    },
    "related": "よいち（授業の重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_jiyuu",
    "word": "自由",
    "reading": "じゆう",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "freedom / free",
      "ja": "自由",
      "zh_TW": "自由",
      "zh_CN": "自由",
      "ko": "자유",
      "zh_HK": "自由",
      "fr": "liberté / libre"
    },
    "example": {
      "ja": "<ruby>週末<rt>しゅうまつ</rt></ruby>は<ruby>時間<rt>じかん</rt></ruby>が<ruby>自由<rt>じゆう</rt></ruby>にあるので、<ruby>好<rt>す</rt></ruby>きな<ruby>映画<rt>えいが</rt></ruby>を<ruby>見<rt>み</rt></ruby>ます。",
      "en": "I have free time on the weekend, so I watch my favorite movies.",
      "zh_TW": "週末時間很自由，所以我會看喜歡的電影。",
      "zh_CN": "周末时间很自由，所以我看喜欢的电影。",
      "ko": "주말에는 시간이 자유로워서 좋아하는 영화를 봐요.",
      "zh_HK": "週末時間好自由，所以我會睇鍾意嘅電影。",
      "fr": "Le week-end, j'ai du temps libre, donc je regarde mes films préférés."
    },
    "related": "じゆう（授業の重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_tanoshimu",
    "word": "楽しむ",
    "reading": "たのしむ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to enjoy / to have fun",
      "ja": "楽しむ",
      "zh_TW": "享受、盡情體驗",
      "zh_CN": "享受、尽情体验",
      "ko": "즐기다",
      "zh_HK": "享受、盡情體驗",
      "fr": "profiter / s'amuser"
    },
    "example": {
      "ja": "<ruby>日本<rt>にほん</rt></ruby>での<ruby>旅行<rt>りょこう</rt></ruby>を<ruby>心<rt>こころ</rt></ruby>から<ruby>楽<rt>たの</rt></ruby>しんでいます。",
      "en": "I am enjoying my trip in Japan from the bottom of my heart.",
      "zh_TW": "我打從心底享受在日本的旅行。",
      "zh_CN": "我由衷地享受在日本的旅行。",
      "ko": "일본 여행을 진심으로 즐기고 있습니다.",
      "zh_HK": "我由心咁享受喺日本嘅旅行。",
      "fr": "Je profite pleinement de mon voyage au Japon."
    },
    "related": "たのしむ（授業の重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_oukasuru",
    "word": "謳歌する",
    "reading": "おうかする",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to celebrate / to enjoy to the fullest",
      "ja": "謳歌する",
      "zh_TW": "謳歌、盡情享受",
      "zh_CN": "讴歌、尽情享受",
      "ko": "구가하다 / 마음껏 누리다",
      "zh_HK": "謳歌、盡情享受",
      "fr": "célébrer / profiter pleinement"
    },
    "example": {
      "ja": "<ruby>若<rt>わか</rt></ruby>い<ruby>人<rt>ひと</rt></ruby>たちが<ruby>大学<rt>だいがく</rt></ruby><ruby>生活<rt>せいかつ</rt></ruby>を<ruby>謳歌<rt>おうか</rt></ruby>しています。",
      "en": "Young people are enjoying their university life to the fullest.",
      "zh_TW": "年輕人們正在盡情享受大學生活。",
      "zh_CN": "年轻人们正在尽情享受大学生活。",
      "ko": "젊은이들이 대학 생활을 마음껏 누리고 있습니다.",
      "zh_HK": "年輕人正喺度盡情享受大學生活。",
      "fr": "Les jeunes profitent pleinement de leur vie universitaire."
    },
    "related": "おうかする（授業の重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_kougeki",
    "word": "攻撃",
    "reading": "こうげき",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "attack / offensive",
      "ja": "攻撃",
      "zh_TW": "攻擊",
      "zh_CN": "攻击",
      "ko": "공격",
      "zh_HK": "攻擊",
      "fr": "attaque / offensive"
    },
    "example": {
      "ja": "ネット<ruby>上<rt>じょう</rt></ruby>で<ruby>他人<rt>たにん</rt></ruby>を<ruby>攻撃<rt>こうげき</rt></ruby>するのはやめましょう。",
      "en": "Let's avoid attacking other people on the internet.",
      "zh_TW": "請不要在網路上攻擊他人。",
      "zh_CN": "请不要在网络上攻击他人。",
      "ko": "인터넷에서 다른 사람을 공격하는 것은 그만둡시다.",
      "zh_HK": "請唔好喺網上攻擊其他人。",
      "fr": "Évitons d'attaquer les autres sur Internet."
    },
    "related": "こうげき（授業の重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_tsuuchi",
    "word": "通知",
    "reading": "つうち",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "notification / notice",
      "ja": "通知",
      "zh_TW": "通知、推播提醒",
      "zh_CN": "通知、推送提醒",
      "ko": "알림 / 통지",
      "zh_HK": "通知、推播提醒",
      "fr": "notification / avis"
    },
    "example": {
      "ja": "スマホに<ruby>新<rt>あたら</rt></ruby>しいメッセージの<ruby>通知<rt>つうち</rt></ruby>が<ruby>届<rt>とど</rt></ruby>きました。",
      "en": "A notification for a new message arrived on my smartphone.",
      "zh_TW": "手機收到了新訊息的通知。",
      "zh_CN": "手机收到了新消息的通知。",
      "ko": "스마트폰에 새 메시지 알림이 도착했습니다.",
      "zh_HK": "手機收到咗新訊息嘅通知。",
      "fr": "Une notification pour un nouveau message est arrivée sur mon smartphone."
    },
    "related": "つうち（授業の重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_shitsurei",
    "word": "失礼",
    "reading": "しつれい",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "rude / discourteous",
      "ja": "失礼",
      "zh_TW": "失禮、不禮貌",
      "zh_CN": "失礼、不礼貌",
      "ko": "실례 / 무례함",
      "zh_HK": "失禮、不禮貌",
      "fr": "impoli / impolitesse"
    },
    "example": {
      "ja": "ご<ruby>挨拶<rt>あいさつ</rt></ruby>をしないのは、お<ruby>相手<rt>あいて</rt></ruby>に<ruby>対<rt>たい</rt></ruby>して<ruby>失礼<rt>しつれい</rt></ruby>です。",
      "en": "Not greeting someone is rude to that person.",
      "zh_TW": "不打招呼對對方是很失禮的。",
      "zh_CN": "不打招呼对对方是很失礼的。",
      "ko": "인사를 하지 않는 것은 상대방에 대해 실례입니다.",
      "zh_HK": "唔打招呼對對方係好失禮嘅。",
      "fr": "Ne pas saluer quelqu'un est impoli envers cette personne."
    },
    "related": "しつれい（授業の重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_shitauchi",
    "word": "舌打ち",
    "reading": "したうち",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "clicking one's tongue / tut-tutting",
      "ja": "舌打ち",
      "zh_TW": "嘖舌、彈舌",
      "zh_CN": "咂嘴、弹舌",
      "ko": "혀를 차다",
      "zh_HK": "嘖舌、彈舌",
      "fr": "claquement de langue"
    },
    "example": {
      "ja": "<ruby>彼<rt>かれ</rt></ruby>はイライラして、<ruby>思<rt>おも</rt></ruby>わず<ruby>舌打<rt>したう</rt></ruby>ちをしました。",
      "en": "He was frustrated and clicked his tongue without thinking.",
      "zh_TW": "他焦躁不安地忍不住嘖了舌。",
      "zh_CN": "他焦躁不安地忍不住咂了嘴。",
      "ko": "그는 짜증이 나서 무심코 혀를 찼습니다.",
      "zh_HK": "佢好焦躁咁忍唔住嘖咗一聲。",
      "fr": "Énervé, il a claqué de la langue sans s'en rendre compte."
    },
    "related": "したうち（授業の重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_kazoekirenai",
    "word": "数えきれないほど",
    "reading": "かぞえきれないほど",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "countless / innumerable",
      "ja": "数えきれないほど",
      "zh_TW": "數不清、不計其數",
      "zh_CN": "数不清、不计其数",
      "ko": "셀 수 없을 정도로",
      "zh_HK": "數唔清、不計其數",
      "fr": "innombrable / sans nombre"
    },
    "example": {
      "ja": "この<ruby>街<rt>まち</rt></ruby>には、<ruby>数<rt>かぞ</rt></ruby>えきれないほどの<ruby>魅力<rt>みりょく</rt></ruby>があります。",
      "en": "This city has countless charms.",
      "zh_TW": "這座城市有數不清的魅力。",
      "zh_CN": "这座城市有数不清的魅力。",
      "ko": "이 도시에는 셀 수 없을 정도로 많은 매력이 있습니다.",
      "zh_HK": "呢個城市有數唔清嘅魅力。",
      "fr": "Cette ville a d'innombrables charmes."
    },
    "related": "かぞえきれないほど（授業の重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_iyanaomoi",
    "word": "嫌な思いをする",
    "reading": "いやなおもいをする",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to have an unpleasant experience",
      "ja": "嫌な思いをする",
      "zh_TW": "感到不愉快、遭遇不快",
      "zh_CN": "感到不愉快、遭遇不快",
      "ko": "불쾌한 일을 겪다",
      "zh_HK": "感到不愉快、遭遇不快",
      "fr": "passer un mauvais moment / vivre une mauvaise expérience"
    },
    "example": {
      "ja": "<ruby>失礼<rt>しつれい</rt></ruby>なことを<ruby>言<rt>い</rt></ruby>われて、とても<ruby>嫌<rt>いや</rt></ruby>な<ruby>思<rt>おも</rt></ruby>いをしました。",
      "en": "Being told something rude gave me a very unpleasant experience.",
      "zh_TW": "被說了失禮的話，心裡感到非常不愉快。",
      "zh_CN": "被说了失礼的话，心里感到非常不愉快。",
      "ko": "무례한 말을 들어서 매우 불쾌한 기분이 들었습니다.",
      "zh_HK": "被講咗失禮嘅說話，心裏面覺得好唔舒服。",
      "fr": "On m'a dit des choses impolies, ce qui m'a mis très mal à l'aise."
    },
    "related": "いやなおもいをする（授業の重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_ekiin",
    "word": "駅員",
    "reading": "えきいん",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "station staff",
      "ja": "駅員",
      "zh_TW": "站務員、車站工作人員",
      "zh_CN": "站务员、车站工作人员",
      "ko": "역무원",
      "zh_HK": "站務員、車站工作人員",
      "fr": "employé de gare"
    },
    "example": {
      "ja": "<ruby>道<rt>みち</rt></ruby>が分からなかったので、<ruby>駅員<rt>えきいん</rt></ruby>さんに<ruby>尋<rt>たず</rt></ruby>ねました。",
      "en": "I didn't know the way, so I asked the station staff.",
      "zh_TW": "因為不知道路，所以向站務員詢問了。",
      "zh_CN": "因为不知道路，所以向站务员询问了。",
      "ko": "길을 몰라서 역무원에게 물어보았습니다.",
      "zh_HK": "因為唔識路，所以向站務員問路。",
      "fr": "Comme je ne connaissais pas le chemin, j'ai demandé à l'employé de gare."
    },
    "related": "えきいん（授業の重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_taidogawarui",
    "word": "態度が悪い",
    "reading": "たいどがわるい",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "bad attitude / poor manners",
      "ja": "態度が悪い",
      "zh_TW": "態度惡劣、態度差",
      "zh_CN": "态度恶劣、态度差",
      "ko": "태도가 나쁘다",
      "zh_HK": "態度惡劣、態度差",
      "fr": "mauvaise attitude / mauvaise conduite"
    },
    "example": {
      "ja": "<ruby>店員<rt>てんいん</rt></ruby>の<ruby>態度<rt>たいど</rt></ruby>が<ruby>悪<rt>わる</rt></ruby>くて、少しがっかりしました。",
      "en": "The store clerk had a bad attitude, which was a bit disappointing.",
      "zh_TW": "店員的態度很差，讓人有點失望。",
      "zh_CN": "店员的态度很差，让人有点失望。",
      "ko": "점원의 태도가 나빠서 조금 실망했습니다.",
      "zh_HK": "店員嘅態度好差，令人有啲失望。",
      "fr": "L'employé avait une mauvaise attitude, ce qui était un peu décevant."
    },
    "related": "たいどがわるい（授業の重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_eikyou",
    "word": "影響",
    "reading": "えいきょう",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "influence / effect",
      "ja": "影響",
      "zh_TW": "影響",
      "zh_CN": "影响",
      "ko": "영향",
      "zh_HK": "影響",
      "fr": "influence / effet"
    },
    "example": {
      "ja": "<ruby>先生<rt>せんせい</rt></ruby>の<ruby>優<rt>やさ</rt></ruby>しい<ruby>言葉<rt>ことば</rt></ruby>が、<ruby>私<rt>わたし</rt></ruby>の<ruby>将来<rt>しょうらい</rt></ruby>に<ruby>大<rt>おお</rt></ruby>きな<ruby>影響<rt>えいきょう</rt></ruby>を<ruby>与<rt>あた</rt></ruby>えました。",
      "en": "The teacher's gentle words had a great impact on my future.",
      "zh_TW": "老師溫柔的話語，對我的未來產生了很大的影響。",
      "zh_CN": "老师温柔的话语，对我的未来产生了很大的影响。",
      "ko": "선생님의 다정한 말씀이 제 미래에 큰 영향을 주었습니다.",
      "zh_HK": "老師溫柔嘅說話對我嘅未來產生咗好大嘅影響。",
      "fr": "Les paroles douces du professeur ont eu une grande influence sur mon avenir."
    },
    "related": "えいきょう（授業の重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_tanseina",
    "word": "端正な",
    "reading": "たんせいな",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "handsome / well-featured",
      "ja": "端正な",
      "zh_TW": "端正的、秀麗的",
      "zh_CN": "端正的、秀丽的",
      "ko": "단정한 / 준수한",
      "zh_HK": "端正的、秀麗的",
      "fr": "régulier / bien proportionné"
    },
    "example": {
      "ja": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>端正<rt>たんせい</rt></ruby>な<ruby>顔立<rt>かおだ</rt></ruby>ちをしていて、とても<ruby>人気<rt>にんき</rt></ruby>があります。",
      "en": "He has handsome, neat facial features and is very popular.",
      "zh_TW": "他長著端正清秀的五官，非常受歡迎。",
      "zh_CN": "他长着端正清秀的五官，非常受欢迎。",
      "ko": "그는 이목구비가 반듯해서 인기가 아주 많습니다.",
      "zh_HK": "佢生得五官端正清秀，非常受歡迎。",
      "fr": "Il a des traits réguliers et harmonieux, et il est très populaire."
    },
    "related": "たんせいな（授業の重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_kaodachi",
    "word": "顔立ち",
    "reading": "かおだち",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "facial features / looks",
      "ja": "顔立ち",
      "zh_TW": "五官容貌、長相",
      "zh_CN": "五官容貌、长相",
      "ko": "생김새 / 이목구비",
      "zh_HK": "五官容貌、長相",
      "fr": "traits du visage / physionomie"
    },
    "example": {
      "ja": "<ruby>彼女<rt>かのじょ</rt></ruby>は、お<ruby>母<rt>かあ</rt></ruby>さんにとてもよく<ruby>似<rt>に</rt></ruby>た<ruby>美<rt>うつく</rt></ruby>しい<ruby>顔立<rt>かおだ</rt></ruby>ちをしています。",
      "en": "She has beautiful facial features that closely resemble her mother's.",
      "zh_TW": "她有著與母親非常相像的美麗容貌。",
      "zh_CN": "她有着与母亲非常相像的美丽容貌。",
      "ko": "그녀는 어머니를 꼭 닮은 아름다운 생김새를 지니고 있습니다.",
      "zh_HK": "佢生得同媽媽非常似，有一張美麗嘅面孔。",
      "fr": "Elle a de beaux traits qui ressemblent beaucoup à ceux de sa mère."
    },
    "related": "かおだち（授業の重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_soudanninoru",
    "word": "相談に乗る",
    "reading": "そうだんにのる",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to give advice / to consult with",
      "ja": "相談に乗る",
      "zh_TW": "傾聽並給予建議、接受諮詢",
      "zh_CN": "倾听并给予建议、接受咨询",
      "ko": "상담에 응하다 / 조언을 해주다",
      "zh_HK": "傾聽並給予建議、接受諮詢",
      "fr": "donner des conseils / être à l'écoute"
    },
    "example": {
      "ja": "<ruby>困<rt>こま</rt></ruby>ったときは、いつでも<ruby>相談<rt>そうだん</rt></ruby>に<ruby>乗<rt>の</rt></ruby>るよ。",
      "en": "Whenever you are in trouble, I'm always here to listen and help.",
      "zh_TW": "遇到困難時，我隨時都可以幫你出主意喔。",
      "zh_CN": "遇到困难时，我随时都可以帮你出主意哦。",
      "ko": "어려울 때는 언제든지 상담해 줄게.",
      "zh_HK": "遇到困難嘅時候，我隨時都可以幫你諗計㗎。",
      "fr": "Si tu as un problème, je suis toujours là pour t'écouter et te conseiller."
    },
    "related": "そうだんにのる（授業の重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
{
    "id": "card_midori_furinosuru",
    "word": "〜のふりをする",
    "reading": "〜のふりをする",
    "meaning": {
      "ja": "〜のふりをする（見せかける）",
      "zh_TW": "假裝……、裝作……",
      "zh_CN": "假装……、装作……",
      "en": "to pretend to be...",
      "ko": "~인 척하다",
      "zh_HK": "扮……、假裝……",
      "fr": "faire semblant de..."
    },
    "example": {
      "ja": "A: <ruby>都合<rt>つごう</rt></ruby>が<ruby>悪<rt>わる</rt></ruby>くなると、<ruby>彼<rt>かれ</rt></ruby>はいつも<ruby>聞<rt>き</rt></ruby>こえないふりをします。<br/>B: それはずるいですね。しっかり<ruby>話<rt>はな</rt></ruby>し<ruby>合<rt>あ</rt></ruby>いましょう。",
      "zh_TW": "A: 情況一不利，他總是假裝沒聽見。<br/>B: 那樣太狡猾了呢。好好跟他談談吧。",
      "zh_CN": "A: 情况一不利，他总是假装没听见。<br/>B: 那样太狡猾了呢。好好跟他谈谈吧。",
      "en": "A: Whenever things become inconvenient, he always pretends not to hear.<br/>B: That's unfair. Let's have a proper talk with him.",
      "ko": "A: 상황이 불리해지면 그는 항상 안 들리는 척을 해요.<br/>B: 그건 비겁하네요. 제대로 이야기해 봐요.",
      "zh_HK": "A: 情況一唔對路，佢就成日扮聽唔到。<br/>B: 咁樣好狡猾㗎喎。同佢好好傾下啦。",
      "fr": "A: Quand la situation se complique, il fait toujours semblant de ne pas entendre.<br/>B: C'est malhonnête. Il faut en discuter sérieusement."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_midori_nisemono",
    "word": "偽物",
    "reading": "にせもの",
    "meaning": {
      "ja": "偽物",
      "zh_TW": "仿冒品、假貨",
      "zh_CN": "假货、仿冒品",
      "en": "fake / counterfeit",
      "ko": "가짜 / 모조품",
      "zh_HK": "假嘢、冒牌貨",
      "fr": "faux / contrefaçon"
    },
    "example": {
      "ja": "A: ネットで<ruby>安<rt>やす</rt></ruby>く<ruby>買<rt>か</rt></ruby>ったブランドバッグは<ruby>偽物<rt>にせもの</rt></ruby>でした。<br/>B: ええっ、それはショックですね！<ruby>返品<rt>へんぴん</rt></ruby>できますか。",
      "zh_TW": "A: 在網路上便宜買的名牌包居然是假貨。<br/>B: 咦！那太受打擊了吧！能退貨嗎？",
      "zh_CN": "A: 在网上便宜买的名牌包居然是假货。<br/>B: 咦！那太受打击了吧！能退货吗？",
      "en": "A: The designer bag I bought cheaply online turned out to be a fake.<br/>B: What! That's shocking! Can you return it?",
      "ko": "A: 인터넷에서 싸게 산 명품 가방이 가짜였어요.<br/>B: 헉, 충격이네요! 반품은 가능한가요?",
      "zh_HK": "A: 喺網上買嘅平價名牌袋竟然係假嘢。<br/>B: 吓！咁好打擊喎！退唔退到貨呀？",
      "fr": "A: Le sac de marque acheté pas cher en ligne était une contrefaçon.<br/>B: Mince alors ! Tu peux le retourner ?"
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_midori_honmono",
    "word": "本物",
    "reading": "ほんもの",
    "meaning": {
      "ja": "本物",
      "zh_TW": "真品、正品、名副其實的",
      "zh_CN": "真品、正品",
      "en": "genuine / real thing",
      "ko": "진짜 / 정품",
      "zh_HK": "真嘢、正貨",
      "fr": "vrai / authentique"
    },
    "example": {
      "ja": "A: このダイヤモンドの<ruby>指輪<rt>ゆびわ</rt></ruby>は<ruby>鑑定書<rt>かんていしょ</rt></ruby>が<ruby>付<rt>つ</rt></ruby>いている<ruby>本物<rt>ほんもの</rt></ruby>です。<br/>B: さすが、とても<ruby.輝<rt>かがや</rt></ruby>きが<ruby>綺麗<rt>きれい</rt></ruby>ですね！",
      "zh_TW": "A: 這只鑽石戒指附有鑑定書，是真品。<br/>B: 真不愧是真品，光芒非常璀璨美麗呢！",
      "zh_CN": "A: 这只钻石戒指附有鉴定证书，是真品。<br/>B: 真不愧是真品，光芒非常璀璨美丽呢！",
      "en": "A: This diamond ring comes with a certificate and is genuine.<br/>B: As expected, the sparkle is truly gorgeous!",
      "ko": "A: 이 다이아몬드 반지는 감정서가 딸린 진짜예요.<br/>B: 역시 빛이 아주 아름답네요!",
      "zh_HK": "A: 呢隻鑽石戒指有鑑定證書，係真嘢嚟㗎。<br/>B: 果然好嘢，閃得好靚呀！",
      "fr": "A: Cette bague en diamant est authentique avec certificat.<br/>B: En effet, son éclat est magnifique !"
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_midori_sagi",
    "word": "詐欺",
    "reading": "さぎ",
    "meaning": {
      "ja": "詐欺",
      "zh_TW": "詐欺、詐騙",
      "zh_CN": "诈骗、欺诈",
      "en": "fraud / scam",
      "ko": "사기",
      "zh_HK": "騙案、詐騙",
      "fr": "escroquerie / arnaque"
    },
    "example": {
      "ja": "A: <ruby>知<rt>し</rt></ruby>らない<ruby>番号<rt>ばんごう</rt></ruby>からの<ruby>電話<rt>でんわ</rt></ruby>で、<ruby>振<rt>ふ</rt></ruby>り<ruby>込<rt>こ</rt></ruby>め<ruby>詐欺<rt>さぎ</rt></ruby>に<ruby>遭<rt>あ</rt></ruby>いそうになりました。<br/>B: <ruby>危<rt>あぶ</rt></ruby>なかったですね！すぐにお<ruby>金<rt>かね</rt></ruby>を払わなくてよかったです。",
      "zh_TW": "A: 接到陌生號碼的電話，差點遇上匯款詐騙。<br/>B: 太危險了！好在沒有立刻匯錢。",
      "zh_CN": "A: 接到陌生号码的电话，差点碰上汇款诈骗。<br/>B: 太危险了！好在没有立刻转账。",
      "en": "A: I almost fell for a bank transfer scam from an unknown number.<br/>B: That was close! Good thing you didn't pay right away.",
      "ko": "A: 모르는 번호로 온 전화 때문에 보이스피싱 사기를 당할 뻔했어요.<br/>B: 위험했네요! 바로 돈을 안 보내서 다행이에요.",
      "zh_HK": "A: 接到陌生電話，爭啲中咗轉賬騙局。<br/>B: 好彩冇事！好在冇即刻過數啫。",
      "fr": "A: J'ai failli me faire arnaquer par téléphone d'un numéro inconnu.<br/>B: C'était moins une ! Heureusement que tu n'as pas payé."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_midori_kuyashii",
    "word": "悔しい",
    "reading": "くやしい",
    "meaning": {
      "ja": "悔しい（思い通りにいかず残念）",
      "zh_TW": "不甘心、懊悔",
      "zh_CN": "不甘心、懊悔",
      "en": "frustrated / regrettable",
      "ko": "분하다 / 억울하다 / 아쉽다",
      "zh_HK": "唔甘心、好懊悔",
      "fr": "frustrant / dépité"
    },
    "example": {
      "ja": "A: あと<ruby>一歩<rt>いっぽ</rt></ruby>のところで<ruby>試合<rt>しあい</rt></ruby>に<ruby>負<rt>ま</rt></ruby>けてしまい、<ruby>本当<rt>ほんとう</rt></ruby>に<ruby>悔<rt>くや</rt></ruby>しいです。<br/>B: その<ruby>悔<rt>くや</rt></ruby>しさをバネに、<ruby>次<rt>つぎ</rt></ruby>はきっと<ruby>勝<rt>か</rt></ruby>ちましょう！",
      "zh_TW": "A: 只差一步就輸掉了比賽，真的很不甘心。<br/>B: 把這份不甘心化為動力，下次一定會贏的！",
      "zh_CN": "A: 只差一步就输掉了比赛，真的很不甘心。<br/>B: 把这份不甘心化为动力，下次一定会赢的！",
      "en": "A: We lost the match by just a hair, it's so frustrating.<br/>B: Turn that frustration into strength, you'll win next time!",
      "ko": "A: 한 발자국 차이로 경기에서 져서 정말 분해요.<br/>B: 그 아쉬움을 발판 삼아 다음엔 꼭 이겨요!",
      "zh_HK": "A: 爭少少輸咗場比賽，真係好唔甘心。<br/>B: 將呢種唔甘心化為動力，下次一定贏！",
      "fr": "A: Nous avons perdu le match à un cheveu, c'est tellement rageant.<br/>B: Transforme cette déception en force pour la prochaine fois !"
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_midori_kiriganai",
    "word": "キリがない",
    "reading": "きりがない",
    "meaning": {
      "ja": "キリがない（きりがない・果てがない）",
      "zh_TW": "沒完沒了、無窮無盡",
      "zh_CN": "没完没了、无穷无尽",
      "en": "endless / there is no end to it",
      "ko": "끝이 없다",
      "zh_HK": "冇完冇了、冇止境",
      "fr": "sans fin / interminable"
    },
    "example": {
      "ja": "A: <ruby>欲<rt>よく</rt></ruby>を<ruby>言<rt>い</rt></ruby>い<ruby>出<rt>だ</rt></ruby>したらキリがないので、この<ruby>辺<rt>へん</rt></ruby>で<ruby>妥協<rt>だきょう</rt></ruby>しましょう。<br/>B: そうですね、<ruby>十分<rt>じゅうぶん</rt></ruby><ruby>満足<rt>まんぞく</rt></ruby>できる<ruby>結果<rt>けっか</rt></ruby>ですよ。",
      "zh_TW": "A: 慾望如果貪求起來是沒完沒了的，就在這裡妥協吧。<br/>B: 說得對，這已經是很令人滿意的結果了。",
      "zh_CN": "A: 欲望如果贪求起来是没完没了的，就在这里妥协吧。<br/>B: 说得对，这已经是很令人满意的结果了。",
      "en": "A: There's no end to greed once you start, so let's compromise here.<br/>B: You're right, this result is plenty satisfying.",
      "ko": "A: 욕심을 부리기 시작하면 끝이 없으니 이쯤에서 타협합시다.<br/>B: 맞아요, 충분히 만족스러운 결과예요.",
      "zh_HK": "A: 貪心起上嚟真係冇完冇了，不如喺度收手啦。<br/>B: 係呀，呢個結果已經好令人滿意。",
      "fr": "A: Si on commence à trop en vouloir, ça n'en finira jamais, arrêtons-nous là.<br/>B: C'est vrai, c'est déjà très satisfaisant."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_midori_haragatatsu",
    "word": "腹が立つ",
    "reading": "はらがたつ",
    "meaning": {
      "ja": "腹が立つ（怒りを感じる）",
      "zh_TW": "生氣、發怒",
      "zh_CN": "生气、发火",
      "en": "to get angry / to take offense",
      "ko": "화가 나다",
      "zh_HK": "好嬲、發火",
      "fr": "se mettre en colère"
    },
    "example": {
      "ja": "A: <ruby>彼<rt>かれ</rt></ruby>の<ruby>無責任<rt>むせきにん</rt></ruby>な<ruby>態度<rt>たいど</rt></ruby>を<ruby>見<rt>み</rt></ruby>ていると、<ruby>本当<rt>ほんとう</rt></ruby>に<ruby>腹<rt>はら</rt></ruby>が<ruby>立<rt>た</rt></ruby>ちます。<br/>B: <ruby>気持<rt>きも</rt></ruby>ちはわかりますが、まずは<ruby>深呼吸<rt>しんこきゅう</rt></ruby>して<ruby>落<rt>お</rt></ruby>ち<ruby>着<rt>つ</rt></ruby>きましょう。",
      "zh_TW": "A: 看著他那不負責任的態度，真的很令人火大。<br/>B: 我懂你的心情，但先深呼吸冷靜一下吧。",
      "zh_CN": "A: 看着他那不负责任的态度，真的很令人火大。<br/>B: 我懂你的心情，但先深呼吸冷静一下吧。",
      "en": "A: Looking at his irresponsible attitude really makes me angry.<br/>B: I understand how you feel, but let's take a deep breath and calm down.",
      "ko": "A: 그의 무책임한 태도를 보면 정말 화가 나요.<br/>B: 기분은 알겠지만 일단 심호흡하고 진정해요.",
      "zh_HK": "A: 望住佢嗰種唔負責任嘅態度，真係好火滾。<br/>B: 明白你感受，但深呼吸冷靜下先啦。",
      "fr": "A: Son attitude irresponsable me met vraiment en colère.<br/>B: Je comprends, mais respire un grand coup pour te calmer."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_midori_mukatsuku",
    "word": "ムカつく",
    "reading": "むかつく",
    "meaning": {
      "ja": "ムカつく（腹が立つ・苛立つ）",
      "zh_TW": "令人火大、令人作嘔",
      "zh_CN": "令人火大、令人恼火",
      "en": "to feel irritated / to get ticked off",
      "ko": "짜증나다 / 화나다",
      "zh_HK": "好躁、勁火滾",
      "fr": "être énervé / agacé"
    },
    "example": {
      "ja": "A: あいつの<ruby>偉<rt>えら</rt></ruby>そうな<ruby>言<rt>い</rt></ruby>い<ruby>方<rt>かた</rt></ruby>、<ruby>本当<rt>ほんとう</rt></ruby>にムカつきます！<br/>B: まあまあ、あまり<ruby>気<rt>き</rt></ruby>にしないほうがいいですよ。",
      "zh_TW": "A: 那傢伙高高在上的說話口氣，真讓人火大！<br/>B: 好啦好啦，別太往心裡去喔。",
      "zh_CN": "A: 那家伙自以为是的说话口气，真让人火大！<br/>B: 好啦好啦，别太往心里去哦。",
      "en": "A: That guy's arrogant tone really ticks me off!<br/>B: Come on, it's best not to let it bother you.",
      "ko": "A: 저 녀석의 거만한 말투, 정말 짜증나요!<br/>B: 에이, 너무 신경 쓰지 않는 게 좋아요.",
      "zh_HK": "A: 條友懶巴閉嘅口吻，真係好令人躁！<br/>B: 好啦好啦，唔好放喺心上啦。",
      "fr": "A: Son ton condescendant me tape vraiment sur les nerfs !<br/>B: Allez, essaie de ne pas y prêter attention."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_midori_sewawosuru",
    "word": "世話をする",
    "reading": "せわをする",
    "meaning": {
      "ja": "世話をする（面倒を見る）",
      "zh_TW": "照顧、照料",
      "zh_CN": "照顾、照料",
      "en": "to look after / to take care of",
      "ko": "돌보다 / 보살피다",
      "zh_HK": "照顧、打理",
      "fr": "s'occuper de / prendre soin de"
    },
    "example": {
      "ja": "A: <ruby>毎朝<rt>まいあさ</rt></ruby><ruby>早起<rt>はやお</rt></ruby>きして、<ruby>飼<rt>か</rt></ruby>っている<ruby>犬<rt>いぬ</rt></ruby>の<ruby>世話<rt>せわ</rt></ruby>をしています。<br/>B: <ruby>散歩<rt>さんぽ</rt></ruby>やご飯をあげるのは<ruby>大変<rt>たいへん</rt></ruby>ですが、とてもかわいいですね！",
      "zh_TW": "A: 我每天早起照顧家裡養的狗狗。<br/>B: 散步和餵食雖然辛苦，但牠一定很可愛吧！",
      "zh_CN": "A: 我每天早起照顾家里养的狗狗。<br/>B: 散步和喂食虽然辛苦，但它一定很可爱吧！",
      "en": "A: I wake up early every morning to take care of my dog.<br/>B: Walking and feeding takes effort, but dogs are so lovely!",
      "ko": "A: 매일 아침 일찍 일어나서 키우는 강아지를 돌봐요.<br/>B: 산책이랑 밥 주는 게 힘들지만 정말 귀엽겠네요!",
      "zh_HK": "A: 每日朝早早起照顧隻狗。<br/>B: 帶佢散步餵糧雖然辛苦，但好得意呀！",
      "fr": "A: Je me lève tôt tous les matins pour m'occuper de mon chien.<br/>B: Les promenades et les repas demandent du travail, mais c'est adorable !"
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_midori_shugyou",
    "word": "修行",
    "reading": "しゅぎょう",
    "meaning": {
      "ja": "修行（技術や精神を磨く訓練）",
      "zh_TW": "修行、修煉、學徒訓練",
      "zh_CN": "修行、学徒训练",
      "en": "ascetic training / apprentice training",
      "ko": "수행 / 수련",
      "zh_HK": "修煉、學徒訓練",
      "fr": "entraînement rigoureux / apprentissage"
    },
    "example": {
      "ja": "A: <ruby>一流<rt>いちりゅう</rt></ruby>の<ruby>寿司<rt>すし</rt></ruby><ruby>職人<rt>しょくにん</rt></ruby>になるために、<ruby>有名店<rt>ゆうめいてん</rt></ruby>で10<ruby>年間<rt>ねんかん</rt></ruby><ruby>修行<rt>しゅぎょう</rt></ruby>しました。<br/>B: 10<ruby>年<rt>ねん</rt></ruby>もの<ruby>厳<rt>きび</rt></ruby>しい<ruby>修行<rt>しゅぎょう</rt></ruby>を乗り越えたのは素晴らしいですね！",
      "zh_TW": "A: 為了成為一流的壽司師傅，他在名店修行了10年。<br/>B: 能熬過10年嚴格的學徒修行，真的很了不起呢！",
      "zh_CN": "A: 为了成为一流的寿司师傅，他在名店修行了10年。<br/>B: 能熬过10年严格的学徒修行，真的很了不起呢！",
      "en": "A: To become a top-tier sushi chef, he trained for 10 years at a famous restaurant.<br/>B: Overcoming 10 years of rigorous training is truly admirable!",
      "ko": "A: 일류 초밥 장인이 되기 위해 유명 식당에서 10년간 수행했어요.<br/>B: 10년의 혹독한 수련을 견뎌내다니 대단하네요!",
      "zh_HK": "A: 為咗做一流嘅壽司師傅，喺名店修行咗十年。<br/>B: 捱得過十年咁嚴格嘅學徒訓練，真係好犀利！",
      "fr": "A: Pour devenir un chef sushi de premier ordre, il s'est formé 10 ans dans un grand restaurant.<br/>B: Traverser 10 ans d'apprentissage rigoureux est admirable !"
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_midori_mukiau",
    "word": "向き合う",
    "reading": "むきあう",
    "meaning": {
      "ja": "向き合う（正面から対する・真剣に対処する）",
      "zh_TW": "面對面、正視、認真面對",
      "zh_CN": "面对、正视、认真对待",
      "en": "to confront / to face honestly",
      "ko": "마주하다 / 직면하다",
      "zh_HK": "正視、認真面對",
      "fr": "faire face / affronter"
    },
    "example": {
      "ja": "A: つらい<ruby>現実<rt>げんじつ</rt></ruby>から<ruby>逃<rt>に</rt></ruby>げずに、しっかり<ruby>向<rt>む</rt></ruby>き<ruby>合<rt>あ</rt></ruby>う<ruby>勇気<rt>ゆうき</rt></ruby>が<ruby>必要<rt>ひつよう</rt></ruby>です。<br/>B: ええ、<ruby>問題<rt>もんだい</rt></ruby>から目を背けずに<ruby>一歩<rt>いっぽ</rt></ruby>ずつ進みましょう。",
      "zh_TW": "A: 不要逃避痛苦的現實，需要好好正視它的勇氣。<br/>B: 是啊，不逃避問題，一步一步往前邁進吧。",
      "zh_CN": "A: 不要逃避痛苦的现实，需要好好正视它的勇气。<br/>B: 是啊，不逃避问题，一步一步往前迈进吧。",
      "en": "A: We need the courage to honestly face harsh reality without running away.<br/>B: Yes, let's move forward step by step without turning away from problems.",
      "ko": "A: 힘든 현실에서 도망치지 않고 정면으로 마주하는 용기가 필요해요.<br/>B: 맞아요, 문제에서 눈을 돌리지 말고 한 걸음씩 나아가요.",
      "zh_HK": "A: 唔好逃避殘酷嘅現實，要有勇氣好好正視。<br/>B: 係呀，唔好逃避，一步一步行向前啦。",
      "fr": "A: Il faut avoir le courage d'affronter la réalité sans fuir.<br/>B: Oui, avançons pas à pas sans fermer les yeux sur les difficultés."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_midori_ajitsuke",
    "word": "味付け",
    "reading": "あじつけ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "seasoning, flavoring",
      "ja": "味付け",
      "zh_TW": "調味、調味方式",
      "zh_CN": "調味、調味方式",
      "ko": "seasoning, flavoring",
      "zh_HK": "調味、調味方式",
      "fr": "seasoning, flavoring"
    },
    "example": {
      "ja": "<ruby>素材<rt>そざい</rt></ruby>の<ruby>味<rt>あじ</rt></ruby>を<ruby>生<rt>い</rt></ruby>かすために、うす<ruby>味<rt>あじ</rt></ruby>に<ruby>味付<rt>あじつ</rt></ruby>けした。",
      "en": "seasoning, flavoring",
      "zh_TW": "為了發揮食材本身的味道，做了清淡的調味。",
      "zh_CN": "為了發揮食材本身的味道，做了清淡的調味。",
      "ko": "為了發揮食材本身的味道，做了清淡的調味。",
      "zh_HK": "為了發揮食材本身的味道，做了清淡的調味。",
      "fr": "為了發揮食材本身的味道，做了清淡的調味。"
    },
    "related": "あじつけ（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_mukumu",
    "word": "浮腫む",
    "reading": "むくむ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to swell, to become swollen",
      "ja": "浮腫む",
      "zh_TW": "水腫、浮腫",
      "zh_CN": "水腫、浮腫",
      "ko": "to swell, to become swollen",
      "zh_HK": "水腫、浮腫",
      "fr": "to swell, to become swollen"
    },
    "example": {
      "ja": "<ruby>塩分<rt>えんぶん</rt></ruby>を<ruby>取<rt>と</rt></ruby>りすぎると、<ruby>翌朝<rt>よくあさ</rt></ruby><ruby>顔<rt>かお</rt></ruby>が<ruby>浮腫<rt>むく</rt></ruby>みやすい。",
      "en": "to swell, to become swollen",
      "zh_TW": "攝取過多鹽分的話，隔天早上臉部容易水腫。",
      "zh_CN": "攝取過多鹽分的話，隔天早上臉部容易水腫。",
      "ko": "攝取過多鹽分的話，隔天早上臉部容易水腫。",
      "zh_HK": "攝取過多鹽分的話，隔天早上臉部容易水腫。",
      "fr": "攝取過多鹽分的話，隔天早上臉部容易水腫。"
    },
    "related": "むくむ（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_panpan",
    "word": "パンパン",
    "reading": "ぱんぱん",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "swollen tight, packed full",
      "ja": "パンパン",
      "zh_TW": "腫脹得緊繃、塞得滿滿的",
      "zh_CN": "腫脹得緊繃、塞得滿滿的",
      "ko": "swollen tight, packed full",
      "zh_HK": "腫脹得緊繃、塞得滿滿的",
      "fr": "swollen tight, packed full"
    },
    "example": {
      "ja": "<ruby>一日中<rt>いちにちじゅう</rt></ruby><ruby>立<rt>た</rt></ruby>ち<ruby>仕事<rt>しごと</rt></ruby>をして、<ruby>足<rt>あし</rt></ruby>がパンパンになった。",
      "en": "swollen tight, packed full",
      "zh_TW": "站著工作了一整天，雙腳腫脹得緊繃。",
      "zh_CN": "站著工作了一整天，雙腳腫脹得緊繃。",
      "ko": "站著工作了一整天，雙腳腫脹得緊繃。",
      "zh_HK": "站著工作了一整天，雙腳腫脹得緊繃。",
      "fr": "站著工作了一整天，雙腳腫脹得緊繃。"
    },
    "related": "ぱんぱん（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_jojoni",
    "word": "徐々に",
    "reading": "じょじょに",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "gradually, step by step",
      "ja": "徐々に",
      "zh_TW": "逐漸、逐步、慢慢地",
      "zh_CN": "逐漸、逐步、慢慢地",
      "ko": "gradually, step by step",
      "zh_HK": "逐漸、逐步、慢慢地",
      "fr": "gradually, step by step"
    },
    "example": {
      "ja": "<ruby>薬<rt>くすり</rt></ruby>を<ruby>飲<rt>の</rt></ruby>んだら、<ruby>熱<rt>ねつ</rt></ruby>が<ruby>徐々<rt>じょじょ</rt></ruby>に<ruby>下<rt>さ</rt></ruby>がってきた。",
      "en": "gradually, step by step",
      "zh_TW": "吃了藥之後，體溫逐漸退了下來。",
      "zh_CN": "吃了藥之後，體溫逐漸退了下來。",
      "ko": "吃了藥之後，體溫逐漸退了下來。",
      "zh_HK": "吃了藥之後，體溫逐漸退了下來。",
      "fr": "吃了藥之後，體溫逐漸退了下來。"
    },
    "related": "じょじょに（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_fuyasu",
    "word": "増やす",
    "reading": "ふやす",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to increase, to add to",
      "ja": "増やす",
      "zh_TW": "增加、增添",
      "zh_CN": "增加、增添",
      "ko": "to increase, to add to",
      "zh_HK": "增加、增添",
      "fr": "to increase, to add to"
    },
    "example": {
      "ja": "<ruby>将来<rt>しょうらい</rt></ruby>のために、<ruby>貯金<rt>ちょきん</rt></ruby>を<ruby>増<rt>ふ</rt></ruby>やしたい。",
      "en": "to increase, to add to",
      "zh_TW": "為了將來，我想增加儲蓄。",
      "zh_CN": "為了將來，我想增加儲蓄。",
      "ko": "為了將來，我想增加儲蓄。",
      "zh_HK": "為了將來，我想增加儲蓄。",
      "fr": "為了將來，我想增加儲蓄。"
    },
    "related": "ふやす（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_kobushi",
    "word": "拳",
    "reading": "こぶし",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "fist",
      "ja": "拳",
      "zh_TW": "拳頭",
      "zh_CN": "拳頭",
      "ko": "fist",
      "zh_HK": "拳頭",
      "fr": "fist"
    },
    "example": {
      "ja": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>怒<rt>いか</rt></ruby>りに<ruby>震<rt>ふる</rt></ruby>えながら、ぎゅっと<ruby>拳<rt>こぶし</rt></ruby>を<ruby>握<rt>にぎ</rt></ruby>りしめた。",
      "en": "fist",
      "zh_TW": "他因憤怒而顫抖，緊緊握住了拳頭。",
      "zh_CN": "他因憤怒而顫抖，緊緊握住了拳頭。",
      "ko": "他因憤怒而顫抖，緊緊握住了拳頭。",
      "zh_HK": "他因憤怒而顫抖，緊緊握住了拳頭。",
      "fr": "他因憤怒而顫抖，緊緊握住了拳頭。"
    },
    "related": "こぶし（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_bai",
    "word": "〜倍",
    "reading": "〜ばい",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "... times, -fold",
      "ja": "〜倍",
      "zh_TW": "……倍",
      "zh_CN": "……倍",
      "ko": "... times, -fold",
      "zh_HK": "……倍",
      "fr": "... times, -fold"
    },
    "example": {
      "ja": "このスマホのバッテリーは、<ruby>従来<rt>じゅうらい</rt></ruby>の2<ruby>倍<rt>ばい</rt></ruby><ruby>長持<rt>ながも</rt></ruby>ちする。",
      "en": "... times, -fold",
      "zh_TW": "這款智慧型手機的電池，比以往的耐用兩倍。",
      "zh_CN": "這款智慧型手機的電池，比以往的耐用兩倍。",
      "ko": "這款智慧型手機的電池，比以往的耐用兩倍。",
      "zh_HK": "這款智慧型手機的電池，比以往的耐用兩倍。",
      "fr": "這款智慧型手機的電池，比以往的耐用兩倍。"
    },
    "related": "〜ばい（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_hiwotoosu",
    "word": "火を通す",
    "reading": "ひをとおす",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to cook thoroughly, to heat through",
      "ja": "火を通す",
      "zh_TW": "加熱煮熟、煮透",
      "zh_CN": "加熱煮熟、煮透",
      "ko": "to cook thoroughly, to heat through",
      "zh_HK": "加熱煮熟、煮透",
      "fr": "to cook thoroughly, to heat through"
    },
    "example": {
      "ja": "お<ruby>腹<rt>なか</rt></ruby>を<ruby>壊<rt>こわ</rt></ruby>さないように、<ruby>肉<rt>にく</rt></ruby>の<ruby>中心<rt>ちゅうしん</rt></ruby>までしっかり<ruby>火<rt>ひ</rt></ruby>を<ruby>通<rt>とお</rt></ruby>してください。",
      "en": "to cook thoroughly, to heat through",
      "zh_TW": "為了不吃壞肚子，請務必將肉的中心徹底加熱煮熟。",
      "zh_CN": "為了不吃壞肚子，請務必將肉的中心徹底加熱煮熟。",
      "ko": "為了不吃壞肚子，請務必將肉的中心徹底加熱煮熟。",
      "zh_HK": "為了不吃壞肚子，請務必將肉的中心徹底加熱煮熟。",
      "fr": "為了不吃壞肚子，請務必將肉的中心徹底加熱煮熟。"
    },
    "related": "ひをとおす（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_atsukau",
    "word": "扱う",
    "reading": "あつかう",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to handle, to deal with",
      "ja": "扱う",
      "zh_TW": "拿取、對待、販售、處理",
      "zh_CN": "拿取、對待、販售、處理",
      "ko": "to handle, to deal with",
      "zh_HK": "拿取、對待、販售、處理",
      "fr": "to handle, to deal with"
    },
    "example": {
      "ja": "ガラス<ruby>製品<rt>せいひん</rt></ruby>は<ruby>壊<rt>こわ</rt></ruby>れやすいので、<ruby>丁寧<rt>ていねい</rt></ruby>に<ruby>扱<rt>あつか</rt></ruby>ってください。",
      "en": "to handle, to deal with",
      "zh_TW": "玻璃製品容易破損，請小心拿取。",
      "zh_CN": "玻璃製品容易破損，請小心拿取。",
      "ko": "玻璃製品容易破損，請小心拿取。",
      "zh_HK": "玻璃製品容易破損，請小心拿取。",
      "fr": "玻璃製品容易破損，請小心拿取。"
    },
    "related": "あつかう（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_komugiko",
    "word": "小麦粉",
    "reading": "こむぎこ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "flour, wheat flour",
      "ja": "小麦粉",
      "zh_TW": "麵粉",
      "zh_CN": "麵粉",
      "ko": "flour, wheat flour",
      "zh_HK": "麵粉",
      "fr": "flour, wheat flour"
    },
    "example": {
      "ja": "<ruby>小麦粉<rt>こむぎこ</rt></ruby>と<ruby>卵<rt>たまご</rt></ruby>を<ruby>混<rt>ま</rt></ruby>ぜて、パンの<ruby>生地<rt>きじ</rt></ruby>を<ruby>作<rt>つく</rt></ruby>る。",
      "en": "flour, wheat flour",
      "zh_TW": "將麵粉和雞蛋混合，製作麵包麵團。",
      "zh_CN": "將麵粉和雞蛋混合，製作麵包麵團。",
      "ko": "將麵粉和雞蛋混合，製作麵包麵團。",
      "zh_HK": "將麵粉和雞蛋混合，製作麵包麵團。",
      "fr": "將麵粉和雞蛋混合，製作麵包麵團。"
    },
    "related": "こむぎこ（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_mezurashii",
    "word": "珍しい",
    "reading": "めずらしい",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "rare, unusual",
      "ja": "珍しい",
      "zh_TW": "罕見的、稀奇的",
      "zh_CN": "罕見的、稀奇的",
      "ko": "rare, unusual",
      "zh_HK": "罕見的、稀奇的",
      "fr": "rare, unusual"
    },
    "example": {
      "ja": "この<ruby>地域<rt>ちいき</rt></ruby>で<ruby>雪<rt>ゆき</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>るのはとても<ruby>珍<rt>めずら</rt></ruby>しい。",
      "en": "rare, unusual",
      "zh_TW": "這個地區下雪是非常罕見的。",
      "zh_CN": "這個地區下雪是非常罕見的。",
      "ko": "這個地區下雪是非常罕見的。",
      "zh_HK": "這個地區下雪是非常罕見的。",
      "fr": "這個地區下雪是非常罕見的。"
    },
    "related": "めずらしい（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_ijou",
    "word": "以上",
    "reading": "いじょう",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "more than, at least",
      "ja": "以上",
      "zh_TW": "以上（含基準）、既然……就……",
      "zh_CN": "以上（含基準）、既然……就……",
      "ko": "more than, at least",
      "zh_HK": "以上（含基準）、既然……就……",
      "fr": "more than, at least"
    },
    "example": {
      "ja": "18<ruby>歳以上<rt>さいいじょう</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>だけが、この<ruby>映画<rt>えいが</rt></ruby>を<ruby>観<rt>み</rt></ruby>ることができます。",
      "en": "more than, at least",
      "zh_TW": "只有年滿18歲以上的人才能觀看這部電影。",
      "zh_CN": "只有年滿18歲以上的人才能觀看這部電影。",
      "ko": "只有年滿18歲以上的人才能觀看這部電影。",
      "zh_HK": "只有年滿18歲以上的人才能觀看這部電影。",
      "fr": "只有年滿18歲以上的人才能觀看這部電影。"
    },
    "related": "いじょう（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_ika",
    "word": "以下",
    "reading": "いか",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "less than, below",
      "ja": "以下",
      "zh_TW": "以下（含基準）、如下",
      "zh_CN": "以下（含基準）、如下",
      "ko": "less than, below",
      "zh_HK": "以下（含基準）、如下",
      "fr": "less than, below"
    },
    "example": {
      "ja": "<ruby>小学生以下<rt>しょうがくせいいか</rt></ruby>の<ruby>子供<rt>こども</rt></ruby>は、<ruby>入場料<rt>にゅうじょうりょう</rt></ruby>が<ruby>無料<rt>むりょう</rt></ruby>です。",
      "en": "less than, below",
      "zh_TW": "小學生以下的孩童免收門票。",
      "zh_CN": "小學生以下的孩童免收門票。",
      "ko": "小學生以下的孩童免收門票。",
      "zh_HK": "小學生以下的孩童免收門票。",
      "fr": "小學生以下的孩童免收門票。"
    },
    "related": "いか（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_enki",
    "word": "延期",
    "reading": "えんき",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "postponement, delay",
      "ja": "延期",
      "zh_TW": "延期、延後",
      "zh_CN": "延期、延後",
      "ko": "postponement, delay",
      "zh_HK": "延期、延後",
      "fr": "postponement, delay"
    },
    "example": {
      "ja": "<ruby>雨<rt>あめ</rt></ruby>のため、<ruby>運動会<rt>うんどうかい</rt></ruby>は<ruby>来週<rt>らいしゅう</rt></ruby>に<ruby>延期<rt>えんき</rt></ruby>された。",
      "en": "postponement, delay",
      "zh_TW": "因為下雨，運動會延期至下週舉行。",
      "zh_CN": "因為下雨，運動會延期至下週舉行。",
      "ko": "因為下雨，運動會延期至下週舉行。",
      "zh_HK": "因為下雨，運動會延期至下週舉行。",
      "fr": "因為下雨，運動會延期至下週舉行。"
    },
    "related": "えんき（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_teiji",
    "word": "定時",
    "reading": "ていじ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "regular time, closing time",
      "ja": "定時",
      "zh_TW": "表定下班時間、規定的時間",
      "zh_CN": "表定下班時間、規定的時間",
      "ko": "regular time, closing time",
      "zh_HK": "表定下班時間、規定的時間",
      "fr": "regular time, closing time"
    },
    "example": {
      "ja": "<ruby>今日<rt>きょう</rt></ruby>は<ruby>仕事<rt>しごと</rt></ruby>が<ruby>早<rt>はや</rt></ruby>く<ruby>終<rt>お</rt></ruby>わったので、<ruby>定時<rt>ていじ</rt></ruby>で<ruby>帰<rt>かえ</rt></ruby>ります。",
      "en": "regular time, closing time",
      "zh_TW": "今天工作早早就做完了，所以要準時下班。",
      "zh_CN": "今天工作早早就做完了，所以要準時下班。",
      "ko": "今天工作早早就做完了，所以要準時下班。",
      "zh_HK": "今天工作早早就做完了，所以要準時下班。",
      "fr": "今天工作早早就做完了，所以要準時下班。"
    },
    "related": "ていじ（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_idensuru",
    "word": "遺伝する",
    "reading": "いでんする",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to be inherited, to inherit",
      "ja": "遺伝する",
      "zh_TW": "遺傳",
      "zh_CN": "遺傳",
      "ko": "to be inherited, to inherit",
      "zh_HK": "遺傳",
      "fr": "to be inherited, to inherit"
    },
    "example": {
      "ja": "<ruby>彼<rt>かれ</rt></ruby>の<ruby>高<rt>たか</rt></ruby>い<ruby>身長<rt>しんちょう</rt></ruby>は、<ruby>両親<rt>りょうしん</rt></ruby>から<ruby>遺伝<rt>いでん</rt></ruby>したようだ。",
      "en": "to be inherited, to inherit",
      "zh_TW": "他高挑的身高似乎是遺傳自父母。",
      "zh_CN": "他高挑的身高似乎是遺傳自父母。",
      "ko": "他高挑的身高似乎是遺傳自父母。",
      "zh_HK": "他高挑的身高似乎是遺傳自父母。",
      "fr": "他高挑的身高似乎是遺傳自父母。"
    },
    "related": "いでんする（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_nenreikakunin",
    "word": "年齢確認",
    "reading": "ねんれいかくにん",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "age verification",
      "ja": "年齢確認",
      "zh_TW": "年齡確認、查驗年齡",
      "zh_CN": "年齡確認、查驗年齡",
      "ko": "age verification",
      "zh_HK": "年齡確認、查驗年齡",
      "fr": "age verification"
    },
    "example": {
      "ja": "お<ruby>酒<rt>さけ</rt></ruby>を<ruby>買<rt>か</rt></ruby>う<ruby>際<rt>さい</rt></ruby>に、レジで<ruby>年齢確認<rt>ねんれいかくにん</rt></ruby>をされた。",
      "en": "age verification",
      "zh_TW": "買酒時在收銀檯被查驗了年齡。",
      "zh_CN": "買酒時在收銀檯被查驗了年齡。",
      "ko": "買酒時在收銀檯被查驗了年齡。",
      "zh_HK": "買酒時在收銀檯被查驗了年齡。",
      "fr": "買酒時在收銀檯被查驗了年齡。"
    },
    "related": "ねんれいかくにん（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_mibunshou",
    "word": "身分証",
    "reading": "みぶんしょう",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "identification, ID card",
      "ja": "身分証",
      "zh_TW": "身分證明文件、證件",
      "zh_CN": "身分證明文件、證件",
      "ko": "identification, ID card",
      "zh_HK": "身分證明文件、證件",
      "fr": "identification, ID card"
    },
    "example": {
      "ja": "<ruby>銀行<rt>ぎんこう</rt></ruby>の<ruby>口座<rt>こうざ</rt></ruby>を<ruby>開設<rt>かいせつ</rt></ruby>するために、<ruby>身分証<rt>みぶんしょう</rt></ruby>を<ruby>提示<rt>ていじ</rt></ruby>した。",
      "en": "identification, ID card",
      "zh_TW": "為了開立銀行帳戶，出示了身分證件。",
      "zh_CN": "為了開立銀行帳戶，出示了身分證件。",
      "ko": "為了開立銀行帳戶，出示了身分證件。",
      "zh_HK": "為了開立銀行帳戶，出示了身分證件。",
      "fr": "為了開立銀行帳戶，出示了身分證件。"
    },
    "related": "みぶんしょう（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_kaoiro",
    "word": "顔色",
    "reading": "かおいろ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "complexion, facial expression",
      "ja": "顔色",
      "zh_TW": "臉色、氣色、神色",
      "zh_CN": "臉色、氣色、神色",
      "ko": "complexion, facial expression",
      "zh_HK": "臉色、氣色、神色",
      "fr": "complexion, facial expression"
    },
    "example": {
      "ja": "<ruby>顔色<rt>かおいろ</rt></ruby>が<ruby>悪<rt>わる</rt></ruby>いようですが、どこか<ruby>具合<rt>ぐあい</rt></ruby>が<ruby>悪<rt>わる</rt></ruby>いのですか。",
      "en": "complexion, facial expression",
      "zh_TW": "你的臉色看起來不太好，是哪裡不舒服嗎？",
      "zh_CN": "你的臉色看起來不太好，是哪裡不舒服嗎？",
      "ko": "你的臉色看起來不太好，是哪裡不舒服嗎？",
      "zh_HK": "你的臉色看起來不太好，是哪裡不舒服嗎？",
      "fr": "你的臉色看起來不太好，是哪裡不舒服嗎？"
    },
    "related": "かおいろ（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_saikon",
    "word": "再婚",
    "reading": "さいこん",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "remarriage",
      "ja": "再婚",
      "zh_TW": "再婚",
      "zh_CN": "再婚",
      "ko": "remarriage",
      "zh_HK": "再婚",
      "fr": "remarriage"
    },
    "example": {
      "ja": "<ruby>母<rt>はは</rt></ruby>は<ruby>離婚<rt>りこん</rt></ruby>してから5<ruby>年後<rt>ねんご</rt></ruby>に、<ruby>優<rt>やさ</rt></ruby>しい<ruby>男性<rt>だんせい</rt></ruby>と<ruby>再婚<rt>さいこん</rt></ruby>した。",
      "en": "remarriage",
      "zh_TW": "母親離婚五年後，與一位溫柔的男士再婚了。",
      "zh_CN": "母親離婚五年後，與一位溫柔的男士再婚了。",
      "ko": "母親離婚五年後，與一位溫柔的男士再婚了。",
      "zh_HK": "母親離婚五年後，與一位溫柔的男士再婚了。",
      "fr": "母親離婚五年後，與一位溫柔的男士再婚了。"
    },
    "related": "さいこん（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_burikko",
    "word": "ぶりっ子",
    "reading": "ぶりっこ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "girl playing dumb/cute, coquette",
      "ja": "ぶりっ子",
      "zh_TW": "裝可愛、裝無辜造作的女孩",
      "zh_CN": "裝可愛、裝無辜造作的女孩",
      "ko": "girl playing dumb/cute, coquette",
      "zh_HK": "裝可愛、裝無辜造作的女孩",
      "fr": "girl playing dumb/cute, coquette"
    },
    "example": {
      "ja": "<ruby>彼女<rt>かのじょ</rt></ruby>は<ruby>男性<rt>だんせい</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>に<ruby>行<rt>い</rt></ruby>くと、<ruby>急<rt>きゅう</rt></ruby>にぶりっ<ruby>子<rt>こ</rt></ruby>になる。",
      "en": "girl playing dumb/cute, coquette",
      "zh_TW": "她一到男生面前，就突然變得很愛裝可愛。",
      "zh_CN": "她一到男生面前，就突然變得很愛裝可愛。",
      "ko": "她一到男生面前，就突然變得很愛裝可愛。",
      "zh_HK": "她一到男生面前，就突然變得很愛裝可愛。",
      "fr": "她一到男生面前，就突然變得很愛裝可愛。"
    },
    "related": "ぶりっこ（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_tsukiai",
    "word": "付き合い",
    "reading": "つきあい",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "socializing, association",
      "ja": "付き合い",
      "zh_TW": "交際、人際應酬、交往",
      "zh_CN": "交際、人際應酬、交往",
      "ko": "socializing, association",
      "zh_HK": "交際、人際應酬、交往",
      "fr": "socializing, association"
    },
    "example": {
      "ja": "<ruby>仕事<rt>しごと</rt></ruby>の<ruby>後<rt>あと</rt></ruby>の<ruby>付<rt>つ</rt></ruby>き<ruby>合<rt>あ</rt></ruby>いで、<ruby>同僚<rt>どうりょう</rt></ruby>と<ruby>飲<rt>の</rt></ruby>みに<ruby>行<rt>い</rt></ruby>った。",
      "en": "socializing, association",
      "zh_TW": "下班後因為人際應酬，和同事去喝了一杯。",
      "zh_CN": "下班後因為人際應酬，和同事去喝了一杯。",
      "ko": "下班後因為人際應酬，和同事去喝了一杯。",
      "zh_HK": "下班後因為人際應酬，和同事去喝了一杯。",
      "fr": "下班後因為人際應酬，和同事去喝了一杯。"
    },
    "related": "つきあい（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  },
  {
    "id": "card_midori_toshigahanareteiru",
    "word": "年が離れている",
    "reading": "としがはなれている",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "far apart in age, large age gap",
      "ja": "年が離れている",
      "zh_TW": "年齡差距大、年紀差很多",
      "zh_CN": "年齡差距大、年紀差很多",
      "ko": "far apart in age, large age gap",
      "zh_HK": "年齡差距大、年紀差很多",
      "fr": "far apart in age, large age gap"
    },
    "example": {
      "ja": "<ruby>私<rt>わたし</rt></ruby>たち<ruby>夫婦<rt>ふうふ</rt></ruby>は10<ruby>歳<rt>さい</rt></ruby>も<ruby>年<rt>とし</rt></ruby>が<ruby>離<rt>はな</rt></ruby>れている。",
      "en": "far apart in age, large age gap",
      "zh_TW": "我們夫妻倆年齡相差了十歲之多。",
      "zh_CN": "我們夫妻倆年齡相差了十歲之多。",
      "ko": "我們夫妻倆年齡相差了十歲之多。",
      "zh_HK": "我們夫妻倆年齡相差了十歲之多。",
      "fr": "我們夫妻倆年齡相差了十歲之多。"
    },
    "related": "としがはなれている（みどりさんの重要表現）",
    "studentId": "0012",
    "isCustom": true
  }
];

  const DANIEL_NEW_CARD_IDS = ['card_daniel_001', 'card_daniel_002', 'card_daniel_003', 'card_daniel_004', 'card_daniel_005', 'card_daniel_006', 'card_daniel_007', 'card_daniel_008', 'card_daniel_009', 'card_daniel_010', 'card_daniel_011', 'card_daniel_012', 'card_daniel_013', 'card_daniel_014', 'card_daniel_015', 'card_daniel_016', 'card_daniel_017', 'card_daniel_018', 'card_daniel_019', 'card_daniel_020', 'card_daniel_021', 'card_daniel_022', 'card_daniel_023', 'card_daniel_024', 'card_daniel_025', 'card_daniel_026', 'card_daniel_027', 'card_daniel_028', 'card_daniel_029', 'card_daniel_030', 'card_daniel_031', 'card_daniel_032', 'card_daniel_033', 'card_daniel_034', 'card_daniel_035', 'card_daniel_036', 'card_daniel_037', 'card_daniel_038', 'card_daniel_039', 'card_daniel_040', 'card_daniel_041', 'card_daniel_042', 'card_daniel_043', 'card_daniel_044', 'card_daniel_045', 'card_daniel_046', 'card_daniel_047', 'card_daniel_048', 'card_daniel_049', 'card_daniel_050', 'card_daniel_051', 'card_daniel_052', 'card_daniel_053', 'card_daniel_054', 'card_daniel_055', 'card_daniel_056', 'card_daniel_057', 'card_daniel_058', 'card_daniel_059', 'card_daniel_060', 'card_daniel_061', 'card_daniel_062', 'card_daniel_063', 'card_daniel_064', 'card_daniel_065', 'card_daniel_066', 'card_daniel_067', 'card_daniel_068', 'card_daniel_069', 'card_daniel_070', 'card_daniel_071', 'card_daniel_072', 'card_daniel_073', 'card_daniel_074', 'card_daniel_075', 'card_daniel_076', 'card_daniel_077', 'card_daniel_078', 'card_daniel_079', 'card_daniel_080', 'card_daniel_081', 'card_daniel_082', 'card_daniel_083', 'card_daniel_084', 'card_daniel_085', 'card_daniel_086', 'card_daniel_087', 'card_daniel_088', 'card_daniel_089', 'card_daniel_090', 'card_daniel_091', 'card_daniel_092', 'card_daniel_093', 'card_daniel_094', 'card_daniel_095', 'card_daniel_096', 'card_daniel_097', 'card_daniel_098', 'card_daniel_099', 'card_daniel_100', 'card_daniel_101', 'card_daniel_102', 'card_daniel_103'];


  const DANIEL_CURATED_CARDS = [
  {
    "id": "card_daniel_001",
    "word": "展覧会",
    "reading": "てんらんかい",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "exhibition",
      "ja": "展覧会",
      "zh_TW": "exhibition",
      "zh_CN": "exhibition",
      "ko": "exhibition",
      "zh_HK": "exhibition",
      "fr": "exhibition"
    },
    "example": {
      "ja": "<ruby>週末<rt>しゅうまつ</rt></ruby>、<ruby>美術館<rt>びじゅつかん</rt></ruby>の<ruby>展覧会<rt>てんらんかい</rt></ruby>に<ruby>行<rt>い</rt></ruby>きました。",
      "en": "I went to an exhibition at the art museum on the weekend.",
      "zh_TW": "<ruby>週末<rt>しゅうまつ</rt></ruby>、<ruby>美術館<rt>びじゅつかん</rt></ruby>の<ruby>展覧会<rt>てんらんかい</rt></ruby>に<ruby>行<rt>い</rt></ruby>きました。",
      "zh_CN": "<ruby>週末<rt>しゅうまつ</rt></ruby>、<ruby>美術館<rt>びじゅつかん</rt></ruby>の<ruby>展覧会<rt>てんらんかい</rt></ruby>に<ruby>行<rt>い</rt></ruby>きました。",
      "ko": "<ruby>週末<rt>しゅうまつ</rt></ruby>、<ruby>美術館<rt>びじゅつかん</rt></ruby>の<ruby>展覧会<rt>てんらんかい</rt></ruby>に<ruby>行<rt>い</rt></ruby>きました。",
      "zh_HK": "<ruby>週末<rt>しゅうまつ</rt></ruby>、<ruby>美術館<rt>びじゅつかん</rt></ruby>の<ruby>展覧会<rt>てんらんかい</rt></ruby>に<ruby>行<rt>い</rt></ruby>きました。",
      "fr": "<ruby>週末<rt>しゅうまつ</rt></ruby>、<ruby>美術館<rt>びじゅつかん</rt></ruby>の<ruby>展覧会<rt>てんらんかい</rt></ruby>に<ruby>行<rt>い</rt></ruby>きました。"
    },
    "related": "てんらんかい（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_002",
    "word": "営業マン",
    "reading": "えいぎょうマン",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "salesman; sales representative",
      "ja": "営業マン",
      "zh_TW": "salesman; sales representative",
      "zh_CN": "salesman; sales representative",
      "ko": "salesman; sales representative",
      "zh_HK": "salesman; sales representative",
      "fr": "salesman; sales representative"
    },
    "example": {
      "ja": "<ruby>兄<rt>あに</rt></ruby>は<ruby>車<rt>くるま</rt></ruby>の<ruby>営業<rt>えいぎょう</rt></ruby>マンです。",
      "en": "My older brother is a car salesman.",
      "zh_TW": "<ruby>兄<rt>あに</rt></ruby>は<ruby>車<rt>くるま</rt></ruby>の<ruby>営業<rt>えいぎょう</rt></ruby>マンです。",
      "zh_CN": "<ruby>兄<rt>あに</rt></ruby>は<ruby>車<rt>くるま</rt></ruby>の<ruby>営業<rt>えいぎょう</rt></ruby>マンです。",
      "ko": "<ruby>兄<rt>あに</rt></ruby>は<ruby>車<rt>くるま</rt></ruby>の<ruby>営業<rt>えいぎょう</rt></ruby>マンです。",
      "zh_HK": "<ruby>兄<rt>あに</rt></ruby>は<ruby>車<rt>くるま</rt></ruby>の<ruby>営業<rt>えいぎょう</rt></ruby>マンです。",
      "fr": "<ruby>兄<rt>あに</rt></ruby>は<ruby>車<rt>くるま</rt></ruby>の<ruby>営業<rt>えいぎょう</rt></ruby>マンです。"
    },
    "related": "えいぎょうマン（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_003",
    "word": "営業時間",
    "reading": "えいぎょうじかん",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "business hours; opening hours",
      "ja": "営業時間",
      "zh_TW": "business hours; opening hours",
      "zh_CN": "business hours; opening hours",
      "ko": "business hours; opening hours",
      "zh_HK": "business hours; opening hours",
      "fr": "business hours; opening hours"
    },
    "example": {
      "ja": "このお<ruby>店<rt>みせ</rt></ruby>の<ruby>営業時間<rt>えいぎょうじかん</rt></ruby>は<ruby>何時<rt>なんじ</rt></ruby>までですか。",
      "en": "Until what time is this shop open?",
      "zh_TW": "このお<ruby>店<rt>みせ</rt></ruby>の<ruby>営業時間<rt>えいぎょうじかん</rt></ruby>は<ruby>何時<rt>なんじ</rt></ruby>までですか。",
      "zh_CN": "このお<ruby>店<rt>みせ</rt></ruby>の<ruby>営業時間<rt>えいぎょうじかん</rt></ruby>は<ruby>何時<rt>なんじ</rt></ruby>までですか。",
      "ko": "このお<ruby>店<rt>みせ</rt></ruby>の<ruby>営業時間<rt>えいぎょうじかん</rt></ruby>は<ruby>何時<rt>なんじ</rt></ruby>までですか。",
      "zh_HK": "このお<ruby>店<rt>みせ</rt></ruby>の<ruby>営業時間<rt>えいぎょうじかん</rt></ruby>は<ruby>何時<rt>なんじ</rt></ruby>までですか。",
      "fr": "このお<ruby>店<rt>みせ</rt></ruby>の<ruby>営業時間<rt>えいぎょうじかん</rt></ruby>は<ruby>何時<rt>なんじ</rt></ruby>までですか。"
    },
    "related": "えいぎょうじかん（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_004",
    "word": "営業時間外",
    "reading": "えいぎょうじかんがい",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "outside business hours",
      "ja": "営業時間外",
      "zh_TW": "outside business hours",
      "zh_CN": "outside business hours",
      "ko": "outside business hours",
      "zh_HK": "outside business hours",
      "fr": "outside business hours"
    },
    "example": {
      "ja": "<ruby>営業時間外<rt>えいぎょうじかんがい</rt></ruby>なので、<ruby>電話<rt>でんわ</rt></ruby>がつながりません。",
      "en": "The phone won't connect because it's outside business hours.",
      "zh_TW": "<ruby>営業時間外<rt>えいぎょうじかんがい</rt></ruby>なので、<ruby>電話<rt>でんわ</rt></ruby>がつながりません。",
      "zh_CN": "<ruby>営業時間外<rt>えいぎょうじかんがい</rt></ruby>なので、<ruby>電話<rt>でんわ</rt></ruby>がつながりません。",
      "ko": "<ruby>営業時間外<rt>えいぎょうじかんがい</rt></ruby>なので、<ruby>電話<rt>でんわ</rt></ruby>がつながりません。",
      "zh_HK": "<ruby>営業時間外<rt>えいぎょうじかんがい</rt></ruby>なので、<ruby>電話<rt>でんわ</rt></ruby>がつながりません。",
      "fr": "<ruby>営業時間外<rt>えいぎょうじかんがい</rt></ruby>なので、<ruby>電話<rt>でんわ</rt></ruby>がつながりません。"
    },
    "related": "えいぎょうじかんがい（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_005",
    "word": "創業",
    "reading": "そうぎょう",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "founding (of a business)",
      "ja": "創業",
      "zh_TW": "founding (of a business)",
      "zh_CN": "founding (of a business)",
      "ko": "founding (of a business)",
      "zh_HK": "founding (of a business)",
      "fr": "founding (of a business)"
    },
    "example": {
      "ja": "この<ruby>店<rt>みせ</rt></ruby>は<ruby>創業<rt>そうぎょう</rt></ruby>100<ruby>年<rt>ねん</rt></ruby>です。",
      "en": "This shop has been in business for 100 years.",
      "zh_TW": "この<ruby>店<rt>みせ</rt></ruby>は<ruby>創業<rt>そうぎょう</rt></ruby>100<ruby>年<rt>ねん</rt></ruby>です。",
      "zh_CN": "この<ruby>店<rt>みせ</rt></ruby>は<ruby>創業<rt>そうぎょう</rt></ruby>100<ruby>年<rt>ねん</rt></ruby>です。",
      "ko": "この<ruby>店<rt>みせ</rt></ruby>は<ruby>創業<rt>そうぎょう</rt></ruby>100<ruby>年<rt>ねん</rt></ruby>です。",
      "zh_HK": "この<ruby>店<rt>みせ</rt></ruby>は<ruby>創業<rt>そうぎょう</rt></ruby>100<ruby>年<rt>ねん</rt></ruby>です。",
      "fr": "この<ruby>店<rt>みせ</rt></ruby>は<ruby>創業<rt>そうぎょう</rt></ruby>100<ruby>年<rt>ねん</rt></ruby>です。"
    },
    "related": "そうぎょう（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_006",
    "word": "経営する",
    "reading": "けいえいする",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to run; to manage (a business)",
      "ja": "経営する",
      "zh_TW": "to run; to manage (a business)",
      "zh_CN": "to run; to manage (a business)",
      "ko": "to run; to manage (a business)",
      "zh_HK": "to run; to manage (a business)",
      "fr": "to run; to manage (a business)"
    },
    "example": {
      "ja": "<ruby>父<rt>ちち</rt></ruby>はレストランを<ruby>経営<rt>けいえい</rt></ruby>しています。",
      "en": "My father runs a restaurant.",
      "zh_TW": "<ruby>父<rt>ちち</rt></ruby>はレストランを<ruby>経営<rt>けいえい</rt></ruby>しています。",
      "zh_CN": "<ruby>父<rt>ちち</rt></ruby>はレストランを<ruby>経営<rt>けいえい</rt></ruby>しています。",
      "ko": "<ruby>父<rt>ちち</rt></ruby>はレストランを<ruby>経営<rt>けいえい</rt></ruby>しています。",
      "zh_HK": "<ruby>父<rt>ちち</rt></ruby>はレストランを<ruby>経営<rt>けいえい</rt></ruby>しています。",
      "fr": "<ruby>父<rt>ちち</rt></ruby>はレストランを<ruby>経営<rt>けいえい</rt></ruby>しています。"
    },
    "related": "けいえいする（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_007",
    "word": "家族経営",
    "reading": "かぞくけいえい",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "family-run (business)",
      "ja": "家族経営",
      "zh_TW": "family-run (business)",
      "zh_CN": "family-run (business)",
      "ko": "family-run (business)",
      "zh_HK": "family-run (business)",
      "fr": "family-run (business)"
    },
    "example": {
      "ja": "ここは<ruby>家族経営<rt>かぞくけいえい</rt></ruby>の<ruby>小<rt>ちい</rt></ruby>さな<ruby>旅館<rt>りょかん</rt></ruby>です。",
      "en": "This is a small family-run inn.",
      "zh_TW": "ここは<ruby>家族経営<rt>かぞくけいえい</rt></ruby>の<ruby>小<rt>ちい</rt></ruby>さな<ruby>旅館<rt>りょかん</rt></ruby>です。",
      "zh_CN": "ここは<ruby>家族経営<rt>かぞくけいえい</rt></ruby>の<ruby>小<rt>ちい</rt></ruby>さな<ruby>旅館<rt>りょかん</rt></ruby>です。",
      "ko": "ここは<ruby>家族経営<rt>かぞくけいえい</rt></ruby>の<ruby>小<rt>ちい</rt></ruby>さな<ruby>旅館<rt>りょかん</rt></ruby>です。",
      "zh_HK": "ここは<ruby>家族経営<rt>かぞくけいえい</rt></ruby>の<ruby>小<rt>ちい</rt></ruby>さな<ruby>旅館<rt>りょかん</rt></ruby>です。",
      "fr": "ここは<ruby>家族経営<rt>かぞくけいえい</rt></ruby>の<ruby>小<rt>ちい</rt></ruby>さな<ruby>旅館<rt>りょかん</rt></ruby>です。"
    },
    "related": "かぞくけいえい（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_008",
    "word": "大家族",
    "reading": "だいかぞく",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "large family",
      "ja": "大家族",
      "zh_TW": "large family",
      "zh_CN": "large family",
      "ko": "large family",
      "zh_HK": "large family",
      "fr": "large family"
    },
    "example": {
      "ja": "<ruby>私<rt>わたし</rt></ruby>は<ruby>大家族<rt>だいかぞく</rt></ruby>で<ruby>育<rt>そだ</rt></ruby>ちました。",
      "en": "I grew up in a large family.",
      "zh_TW": "<ruby>私<rt>わたし</rt></ruby>は<ruby>大家族<rt>だいかぞく</rt></ruby>で<ruby>育<rt>そだ</rt></ruby>ちました。",
      "zh_CN": "<ruby>私<rt>わたし</rt></ruby>は<ruby>大家族<rt>だいかぞく</rt></ruby>で<ruby>育<rt>そだ</rt></ruby>ちました。",
      "ko": "<ruby>私<rt>わたし</rt></ruby>は<ruby>大家族<rt>だいかぞく</rt></ruby>で<ruby>育<rt>そだ</rt></ruby>ちました。",
      "zh_HK": "<ruby>私<rt>わたし</rt></ruby>は<ruby>大家族<rt>だいかぞく</rt></ruby>で<ruby>育<rt>そだ</rt></ruby>ちました。",
      "fr": "<ruby>私<rt>わたし</rt></ruby>は<ruby>大家族<rt>だいかぞく</rt></ruby>で<ruby>育<rt>そだ</rt></ruby>ちました。"
    },
    "related": "だいかぞく（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_009",
    "word": "亡くなる",
    "reading": "なくなる",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to pass away",
      "ja": "亡くなる",
      "zh_TW": "to pass away",
      "zh_CN": "to pass away",
      "ko": "to pass away",
      "zh_HK": "to pass away",
      "fr": "to pass away"
    },
    "example": {
      "ja": "<ruby>祖父<rt>そふ</rt></ruby>は<ruby>去年<rt>きょねん</rt></ruby><ruby>亡<rt>な</rt></ruby>くなりました。",
      "en": "My grandfather passed away last year.",
      "zh_TW": "<ruby>祖父<rt>そふ</rt></ruby>は<ruby>去年<rt>きょねん</rt></ruby><ruby>亡<rt>な</rt></ruby>くなりました。",
      "zh_CN": "<ruby>祖父<rt>そふ</rt></ruby>は<ruby>去年<rt>きょねん</rt></ruby><ruby>亡<rt>な</rt></ruby>くなりました。",
      "ko": "<ruby>祖父<rt>そふ</rt></ruby>は<ruby>去年<rt>きょねん</rt></ruby><ruby>亡<rt>な</rt></ruby>くなりました。",
      "zh_HK": "<ruby>祖父<rt>そふ</rt></ruby>は<ruby>去年<rt>きょねん</rt></ruby><ruby>亡<rt>な</rt></ruby>くなりました。",
      "fr": "<ruby>祖父<rt>そふ</rt></ruby>は<ruby>去年<rt>きょねん</rt></ruby><ruby>亡<rt>な</rt></ruby>くなりました。"
    },
    "related": "なくなる（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_010",
    "word": "肉体労働",
    "reading": "にくたいろうどう",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "physical labor; manual labor",
      "ja": "肉体労働",
      "zh_TW": "physical labor; manual labor",
      "zh_CN": "physical labor; manual labor",
      "ko": "physical labor; manual labor",
      "zh_HK": "physical labor; manual labor",
      "fr": "physical labor; manual labor"
    },
    "example": {
      "ja": "<ruby>肉体労働<rt>にくたいろうどう</rt></ruby>は<ruby>大変<rt>たいへん</rt></ruby>です。",
      "en": "Manual labor is hard.",
      "zh_TW": "<ruby>肉体労働<rt>にくたいろうどう</rt></ruby>は<ruby>大変<rt>たいへん</rt></ruby>です。",
      "zh_CN": "<ruby>肉体労働<rt>にくたいろうどう</rt></ruby>は<ruby>大変<rt>たいへん</rt></ruby>です。",
      "ko": "<ruby>肉体労働<rt>にくたいろうどう</rt></ruby>は<ruby>大変<rt>たいへん</rt></ruby>です。",
      "zh_HK": "<ruby>肉体労働<rt>にくたいろうどう</rt></ruby>は<ruby>大変<rt>たいへん</rt></ruby>です。",
      "fr": "<ruby>肉体労働<rt>にくたいろうどう</rt></ruby>は<ruby>大変<rt>たいへん</rt></ruby>です。"
    },
    "related": "にくたいろうどう（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_011",
    "word": "人手不足",
    "reading": "ひとでぶそく",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "labor shortage; short-staffed",
      "ja": "人手不足",
      "zh_TW": "labor shortage; short-staffed",
      "zh_CN": "labor shortage; short-staffed",
      "ko": "labor shortage; short-staffed",
      "zh_HK": "labor shortage; short-staffed",
      "fr": "labor shortage; short-staffed"
    },
    "example": {
      "ja": "どこの<ruby>会社<rt>かいしゃ</rt></ruby>も<ruby>人手不足<rt>ひとでぶそく</rt></ruby>です。",
      "en": "Every company is short-staffed.",
      "zh_TW": "どこの<ruby>会社<rt>かいしゃ</rt></ruby>も<ruby>人手不足<rt>ひとでぶそく</rt></ruby>です。",
      "zh_CN": "どこの<ruby>会社<rt>かいしゃ</rt></ruby>も<ruby>人手不足<rt>ひとでぶそく</rt></ruby>です。",
      "ko": "どこの<ruby>会社<rt>かいしゃ</rt></ruby>も<ruby>人手不足<rt>ひとでぶそく</rt></ruby>です。",
      "zh_HK": "どこの<ruby>会社<rt>かいしゃ</rt></ruby>も<ruby>人手不足<rt>ひとでぶそく</rt></ruby>です。",
      "fr": "どこの<ruby>会社<rt>かいしゃ</rt></ruby>も<ruby>人手不足<rt>ひとでぶそく</rt></ruby>です。"
    },
    "related": "ひとでぶそく（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_012",
    "word": "足りない",
    "reading": "たりない",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "not enough; insufficient",
      "ja": "足りない",
      "zh_TW": "not enough; insufficient",
      "zh_CN": "not enough; insufficient",
      "ko": "not enough; insufficient",
      "zh_HK": "not enough; insufficient",
      "fr": "not enough; insufficient"
    },
    "example": {
      "ja": "お<ruby>金<rt>かね</rt></ruby>が<ruby>少<rt>すこ</rt></ruby>し<ruby>足<rt>た</rt></ruby>りません。",
      "en": "I'm a little short of money.",
      "zh_TW": "お<ruby>金<rt>かね</rt></ruby>が<ruby>少<rt>すこ</rt></ruby>し<ruby>足<rt>た</rt></ruby>りません。",
      "zh_CN": "お<ruby>金<rt>かね</rt></ruby>が<ruby>少<rt>すこ</rt></ruby>し<ruby>足<rt>た</rt></ruby>りません。",
      "ko": "お<ruby>金<rt>かね</rt></ruby>が<ruby>少<rt>すこ</rt></ruby>し<ruby>足<rt>た</rt></ruby>りません。",
      "zh_HK": "お<ruby>金<rt>かね</rt></ruby>が<ruby>少<rt>すこ</rt></ruby>し<ruby>足<rt>た</rt></ruby>りません。",
      "fr": "お<ruby>金<rt>かね</rt></ruby>が<ruby>少<rt>すこ</rt></ruby>し<ruby>足<rt>た</rt></ruby>りません。"
    },
    "related": "たりない（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_013",
    "word": "不足する",
    "reading": "ふそくする",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to be lacking; to run short",
      "ja": "不足する",
      "zh_TW": "to be lacking; to run short",
      "zh_CN": "to be lacking; to run short",
      "ko": "to be lacking; to run short",
      "zh_HK": "to be lacking; to run short",
      "fr": "to be lacking; to run short"
    },
    "example": {
      "ja": "<ruby>最近<rt>さいきん</rt></ruby>、<ruby>睡眠<rt>すいみん</rt></ruby>が<ruby>不足<rt>ふそく</rt></ruby>しています。",
      "en": "Lately I haven't been getting enough sleep.",
      "zh_TW": "<ruby>最近<rt>さいきん</rt></ruby>、<ruby>睡眠<rt>すいみん</rt></ruby>が<ruby>不足<rt>ふそく</rt></ruby>しています。",
      "zh_CN": "<ruby>最近<rt>さいきん</rt></ruby>、<ruby>睡眠<rt>すいみん</rt></ruby>が<ruby>不足<rt>ふそく</rt></ruby>しています。",
      "ko": "<ruby>最近<rt>さいきん</rt></ruby>、<ruby>睡眠<rt>すいみん</rt></ruby>が<ruby>不足<rt>ふそく</rt></ruby>しています。",
      "zh_HK": "<ruby>最近<rt>さいきん</rt></ruby>、<ruby>睡眠<rt>すいみん</rt></ruby>が<ruby>不足<rt>ふそく</rt></ruby>しています。",
      "fr": "<ruby>最近<rt>さいきん</rt></ruby>、<ruby>睡眠<rt>すいみん</rt></ruby>が<ruby>不足<rt>ふそく</rt></ruby>しています。"
    },
    "related": "ふそくする（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_014",
    "word": "農場",
    "reading": "のうじょう",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "farm",
      "ja": "農場",
      "zh_TW": "farm",
      "zh_CN": "farm",
      "ko": "farm",
      "zh_HK": "farm",
      "fr": "farm"
    },
    "example": {
      "ja": "<ruby>北海道<rt>ほっかいどう</rt></ruby>の<ruby>農場<rt>のうじょう</rt></ruby>で<ruby>働<rt>はたら</rt></ruby>いています。",
      "en": "I work on a farm in Hokkaido.",
      "zh_TW": "<ruby>北海道<rt>ほっかいどう</rt></ruby>の<ruby>農場<rt>のうじょう</rt></ruby>で<ruby>働<rt>はたら</rt></ruby>いています。",
      "zh_CN": "<ruby>北海道<rt>ほっかいどう</rt></ruby>の<ruby>農場<rt>のうじょう</rt></ruby>で<ruby>働<rt>はたら</rt></ruby>いています。",
      "ko": "<ruby>北海道<rt>ほっかいどう</rt></ruby>の<ruby>農場<rt>のうじょう</rt></ruby>で<ruby>働<rt>はたら</rt></ruby>いています。",
      "zh_HK": "<ruby>北海道<rt>ほっかいどう</rt></ruby>の<ruby>農場<rt>のうじょう</rt></ruby>で<ruby>働<rt>はたら</rt></ruby>いています。",
      "fr": "<ruby>北海道<rt>ほっかいどう</rt></ruby>の<ruby>農場<rt>のうじょう</rt></ruby>で<ruby>働<rt>はたら</rt></ruby>いています。"
    },
    "related": "のうじょう（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_015",
    "word": "進出する",
    "reading": "しんしゅつする",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to expand into; to enter (a market)",
      "ja": "進出する",
      "zh_TW": "to expand into; to enter (a market)",
      "zh_CN": "to expand into; to enter (a market)",
      "ko": "to expand into; to enter (a market)",
      "zh_HK": "to expand into; to enter (a market)",
      "fr": "to expand into; to enter (a market)"
    },
    "example": {
      "ja": "その<ruby>会社<rt>かいしゃ</rt></ruby>は<ruby>海外<rt>かいがい</rt></ruby>に<ruby>進出<rt>しんしゅつ</rt></ruby>しました。",
      "en": "The company expanded overseas.",
      "zh_TW": "その<ruby>会社<rt>かいしゃ</rt></ruby>は<ruby>海外<rt>かいがい</rt></ruby>に<ruby>進出<rt>しんしゅつ</rt></ruby>しました。",
      "zh_CN": "その<ruby>会社<rt>かいしゃ</rt></ruby>は<ruby>海外<rt>かいがい</rt></ruby>に<ruby>進出<rt>しんしゅつ</rt></ruby>しました。",
      "ko": "その<ruby>会社<rt>かいしゃ</rt></ruby>は<ruby>海外<rt>かいがい</rt></ruby>に<ruby>進出<rt>しんしゅつ</rt></ruby>しました。",
      "zh_HK": "その<ruby>会社<rt>かいしゃ</rt></ruby>は<ruby>海外<rt>かいがい</rt></ruby>に<ruby>進出<rt>しんしゅつ</rt></ruby>しました。",
      "fr": "その<ruby>会社<rt>かいしゃ</rt></ruby>は<ruby>海外<rt>かいがい</rt></ruby>に<ruby>進出<rt>しんしゅつ</rt></ruby>しました。"
    },
    "related": "しんしゅつする（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_016",
    "word": "〜箇所",
    "reading": "〜かしょ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "counter for places/spots",
      "ja": "〜箇所",
      "zh_TW": "counter for places/spots",
      "zh_CN": "counter for places/spots",
      "ko": "counter for places/spots",
      "zh_HK": "counter for places/spots",
      "fr": "counter for places/spots"
    },
    "example": {
      "ja": "<ruby>間違<rt>まちが</rt></ruby>いが3<ruby>箇所<rt>かしょ</rt></ruby>あります。",
      "en": "There are mistakes in three places.",
      "zh_TW": "<ruby>間違<rt>まちが</rt></ruby>いが3<ruby>箇所<rt>かしょ</rt></ruby>あります。",
      "zh_CN": "<ruby>間違<rt>まちが</rt></ruby>いが3<ruby>箇所<rt>かしょ</rt></ruby>あります。",
      "ko": "<ruby>間違<rt>まちが</rt></ruby>いが3<ruby>箇所<rt>かしょ</rt></ruby>あります。",
      "zh_HK": "<ruby>間違<rt>まちが</rt></ruby>いが3<ruby>箇所<rt>かしょ</rt></ruby>あります。",
      "fr": "<ruby>間違<rt>まちが</rt></ruby>いが3<ruby>箇所<rt>かしょ</rt></ruby>あります。"
    },
    "related": "〜かしょ（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_017",
    "word": "田んぼ",
    "reading": "たんぼ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "rice paddy",
      "ja": "田んぼ",
      "zh_TW": "rice paddy",
      "zh_CN": "rice paddy",
      "ko": "rice paddy",
      "zh_HK": "rice paddy",
      "fr": "rice paddy"
    },
    "example": {
      "ja": "<ruby>家<rt>いえ</rt></ruby>の<ruby>周<rt>まわ</rt></ruby>りは<ruby>田<rt>た</rt></ruby>んぼばかりです。",
      "en": "There's nothing but rice paddies around my house.",
      "zh_TW": "<ruby>家<rt>いえ</rt></ruby>の<ruby>周<rt>まわ</rt></ruby>りは<ruby>田<rt>た</rt></ruby>んぼばかりです。",
      "zh_CN": "<ruby>家<rt>いえ</rt></ruby>の<ruby>周<rt>まわ</rt></ruby>りは<ruby>田<rt>た</rt></ruby>んぼばかりです。",
      "ko": "<ruby>家<rt>いえ</rt></ruby>の<ruby>周<rt>まわ</rt></ruby>りは<ruby>田<rt>た</rt></ruby>んぼばかりです。",
      "zh_HK": "<ruby>家<rt>いえ</rt></ruby>の<ruby>周<rt>まわ</rt></ruby>りは<ruby>田<rt>た</rt></ruby>んぼばかりです。",
      "fr": "<ruby>家<rt>いえ</rt></ruby>の<ruby>周<rt>まわ</rt></ruby>りは<ruby>田<rt>た</rt></ruby>んぼばかりです。"
    },
    "related": "たんぼ（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_018",
    "word": "滝",
    "reading": "たき",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "waterfall",
      "ja": "滝",
      "zh_TW": "waterfall",
      "zh_CN": "waterfall",
      "ko": "waterfall",
      "zh_HK": "waterfall",
      "fr": "waterfall"
    },
    "example": {
      "ja": "この<ruby>滝<rt>たき</rt></ruby>はとても<ruby>有名<rt>ゆうめい</rt></ruby>です。",
      "en": "This waterfall is very famous.",
      "zh_TW": "この<ruby>滝<rt>たき</rt></ruby>はとても<ruby>有名<rt>ゆうめい</rt></ruby>です。",
      "zh_CN": "この<ruby>滝<rt>たき</rt></ruby>はとても<ruby>有名<rt>ゆうめい</rt></ruby>です。",
      "ko": "この<ruby>滝<rt>たき</rt></ruby>はとても<ruby>有名<rt>ゆうめい</rt></ruby>です。",
      "zh_HK": "この<ruby>滝<rt>たき</rt></ruby>はとても<ruby>有名<rt>ゆうめい</rt></ruby>です。",
      "fr": "この<ruby>滝<rt>たき</rt></ruby>はとても<ruby>有名<rt>ゆうめい</rt></ruby>です。"
    },
    "related": "たき（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_019",
    "word": "無事",
    "reading": "ぶじ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "safe; safely; without incident",
      "ja": "無事",
      "zh_TW": "safe; safely; without incident",
      "zh_CN": "safe; safely; without incident",
      "ko": "safe; safely; without incident",
      "zh_HK": "safe; safely; without incident",
      "fr": "safe; safely; without incident"
    },
    "example": {
      "ja": "<ruby>無事<rt>ぶじ</rt></ruby>に<ruby>家<rt>いえ</rt></ruby>に<ruby>着<rt>つ</rt></ruby>きました。",
      "en": "I got home safely.",
      "zh_TW": "<ruby>無事<rt>ぶじ</rt></ruby>に<ruby>家<rt>いえ</rt></ruby>に<ruby>着<rt>つ</rt></ruby>きました。",
      "zh_CN": "<ruby>無事<rt>ぶじ</rt></ruby>に<ruby>家<rt>いえ</rt></ruby>に<ruby>着<rt>つ</rt></ruby>きました。",
      "ko": "<ruby>無事<rt>ぶじ</rt></ruby>に<ruby>家<rt>いえ</rt></ruby>に<ruby>着<rt>つ</rt></ruby>きました。",
      "zh_HK": "<ruby>無事<rt>ぶじ</rt></ruby>に<ruby>家<rt>いえ</rt></ruby>に<ruby>着<rt>つ</rt></ruby>きました。",
      "fr": "<ruby>無事<rt>ぶじ</rt></ruby>に<ruby>家<rt>いえ</rt></ruby>に<ruby>着<rt>つ</rt></ruby>きました。"
    },
    "related": "ぶじ（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_020",
    "word": "地下鉄",
    "reading": "ちかてつ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "subway",
      "ja": "地下鉄",
      "zh_TW": "subway",
      "zh_CN": "subway",
      "ko": "subway",
      "zh_HK": "subway",
      "fr": "subway"
    },
    "example": {
      "ja": "<ruby>地下鉄<rt>ちかてつ</rt></ruby>で<ruby>会社<rt>かいしゃ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。",
      "en": "I go to work by subway.",
      "zh_TW": "<ruby>地下鉄<rt>ちかてつ</rt></ruby>で<ruby>会社<rt>かいしゃ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。",
      "zh_CN": "<ruby>地下鉄<rt>ちかてつ</rt></ruby>で<ruby>会社<rt>かいしゃ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。",
      "ko": "<ruby>地下鉄<rt>ちかてつ</rt></ruby>で<ruby>会社<rt>かいしゃ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。",
      "zh_HK": "<ruby>地下鉄<rt>ちかてつ</rt></ruby>で<ruby>会社<rt>かいしゃ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。",
      "fr": "<ruby>地下鉄<rt>ちかてつ</rt></ruby>で<ruby>会社<rt>かいしゃ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。"
    },
    "related": "ちかてつ（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_021",
    "word": "宗教",
    "reading": "しゅうきょう",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "religion",
      "ja": "宗教",
      "zh_TW": "religion",
      "zh_CN": "religion",
      "ko": "religion",
      "zh_HK": "religion",
      "fr": "religion"
    },
    "example": {
      "ja": "<ruby>日本<rt>にほん</rt></ruby>にはいろいろな<ruby>宗教<rt>しゅうきょう</rt></ruby>があります。",
      "en": "There are various religions in Japan.",
      "zh_TW": "<ruby>日本<rt>にほん</rt></ruby>にはいろいろな<ruby>宗教<rt>しゅうきょう</rt></ruby>があります。",
      "zh_CN": "<ruby>日本<rt>にほん</rt></ruby>にはいろいろな<ruby>宗教<rt>しゅうきょう</rt></ruby>があります。",
      "ko": "<ruby>日本<rt>にほん</rt></ruby>にはいろいろな<ruby>宗教<rt>しゅうきょう</rt></ruby>があります。",
      "zh_HK": "<ruby>日本<rt>にほん</rt></ruby>にはいろいろな<ruby>宗教<rt>しゅうきょう</rt></ruby>があります。",
      "fr": "<ruby>日本<rt>にほん</rt></ruby>にはいろいろな<ruby>宗教<rt>しゅうきょう</rt></ruby>があります。"
    },
    "related": "しゅうきょう（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_022",
    "word": "存在",
    "reading": "そんざい",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "existence; presence",
      "ja": "存在",
      "zh_TW": "existence; presence",
      "zh_CN": "existence; presence",
      "ko": "existence; presence",
      "zh_HK": "existence; presence",
      "fr": "existence; presence"
    },
    "example": {
      "ja": "<ruby>幽霊<rt>ゆうれい</rt></ruby>の<ruby>存在<rt>そんざい</rt></ruby>を<ruby>信<rt>しん</rt></ruby>じますか。",
      "en": "Do you believe in the existence of ghosts?",
      "zh_TW": "<ruby>幽霊<rt>ゆうれい</rt></ruby>の<ruby>存在<rt>そんざい</rt></ruby>を<ruby>信<rt>しん</rt></ruby>じますか。",
      "zh_CN": "<ruby>幽霊<rt>ゆうれい</rt></ruby>の<ruby>存在<rt>そんざい</rt></ruby>を<ruby>信<rt>しん</rt></ruby>じますか。",
      "ko": "<ruby>幽霊<rt>ゆうれい</rt></ruby>の<ruby>存在<rt>そんざい</rt></ruby>を<ruby>信<rt>しん</rt></ruby>じますか。",
      "zh_HK": "<ruby>幽霊<rt>ゆうれい</rt></ruby>の<ruby>存在<rt>そんざい</rt></ruby>を<ruby>信<rt>しん</rt></ruby>じますか。",
      "fr": "<ruby>幽霊<rt>ゆうれい</rt></ruby>の<ruby>存在<rt>そんざい</rt></ruby>を<ruby>信<rt>しん</rt></ruby>じますか。"
    },
    "related": "そんざい（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_023",
    "word": "仏教",
    "reading": "ぶっきょう",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "Buddhism",
      "ja": "仏教",
      "zh_TW": "Buddhism",
      "zh_CN": "Buddhism",
      "ko": "Buddhism",
      "zh_HK": "Buddhism",
      "fr": "Buddhism"
    },
    "example": {
      "ja": "<ruby>仏教<rt>ぶっきょう</rt></ruby>はインドで<ruby>生<rt>う</rt></ruby>まれました。",
      "en": "Buddhism originated in India.",
      "zh_TW": "<ruby>仏教<rt>ぶっきょう</rt></ruby>はインドで<ruby>生<rt>う</rt></ruby>まれました。",
      "zh_CN": "<ruby>仏教<rt>ぶっきょう</rt></ruby>はインドで<ruby>生<rt>う</rt></ruby>まれました。",
      "ko": "<ruby>仏教<rt>ぶっきょう</rt></ruby>はインドで<ruby>生<rt>う</rt></ruby>まれました。",
      "zh_HK": "<ruby>仏教<rt>ぶっきょう</rt></ruby>はインドで<ruby>生<rt>う</rt></ruby>まれました。",
      "fr": "<ruby>仏教<rt>ぶっきょう</rt></ruby>はインドで<ruby>生<rt>う</rt></ruby>まれました。"
    },
    "related": "ぶっきょう（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_024",
    "word": "お正月",
    "reading": "おしょうがつ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "New Year (holidays)",
      "ja": "お正月",
      "zh_TW": "New Year (holidays)",
      "zh_CN": "New Year (holidays)",
      "ko": "New Year (holidays)",
      "zh_HK": "New Year (holidays)",
      "fr": "New Year (holidays)"
    },
    "example": {
      "ja": "お<ruby>正月<rt>しょうがつ</rt></ruby>は<ruby>家族<rt>かぞく</rt></ruby>と<ruby>過<rt>す</rt></ruby>ごします。",
      "en": "I spend New Year's with my family.",
      "zh_TW": "お<ruby>正月<rt>しょうがつ</rt></ruby>は<ruby>家族<rt>かぞく</rt></ruby>と<ruby>過<rt>す</rt></ruby>ごします。",
      "zh_CN": "お<ruby>正月<rt>しょうがつ</rt></ruby>は<ruby>家族<rt>かぞく</rt></ruby>と<ruby>過<rt>す</rt></ruby>ごします。",
      "ko": "お<ruby>正月<rt>しょうがつ</rt></ruby>は<ruby>家族<rt>かぞく</rt></ruby>と<ruby>過<rt>す</rt></ruby>ごします。",
      "zh_HK": "お<ruby>正月<rt>しょうがつ</rt></ruby>は<ruby>家族<rt>かぞく</rt></ruby>と<ruby>過<rt>す</rt></ruby>ごします。",
      "fr": "お<ruby>正月<rt>しょうがつ</rt></ruby>は<ruby>家族<rt>かぞく</rt></ruby>と<ruby>過<rt>す</rt></ruby>ごします。"
    },
    "related": "おしょうがつ（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_025",
    "word": "安くなる",
    "reading": "やすくなる",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to become cheaper",
      "ja": "安くなる",
      "zh_TW": "to become cheaper",
      "zh_CN": "to become cheaper",
      "ko": "to become cheaper",
      "zh_HK": "to become cheaper",
      "fr": "to become cheaper"
    },
    "example": {
      "ja": "<ruby>夜<rt>よる</rt></ruby>になると、お<ruby>弁当<rt>べんとう</rt></ruby>が<ruby>安<rt>やす</rt></ruby>くなります。",
      "en": "Bento boxes get cheaper at night.",
      "zh_TW": "<ruby>夜<rt>よる</rt></ruby>になると、お<ruby>弁当<rt>べんとう</rt></ruby>が<ruby>安<rt>やす</rt></ruby>くなります。",
      "zh_CN": "<ruby>夜<rt>よる</rt></ruby>になると、お<ruby>弁当<rt>べんとう</rt></ruby>が<ruby>安<rt>やす</rt></ruby>くなります。",
      "ko": "<ruby>夜<rt>よる</rt></ruby>になると、お<ruby>弁当<rt>べんとう</rt></ruby>が<ruby>安<rt>やす</rt></ruby>くなります。",
      "zh_HK": "<ruby>夜<rt>よる</rt></ruby>になると、お<ruby>弁当<rt>べんとう</rt></ruby>が<ruby>安<rt>やす</rt></ruby>くなります。",
      "fr": "<ruby>夜<rt>よる</rt></ruby>になると、お<ruby>弁当<rt>べんとう</rt></ruby>が<ruby>安<rt>やす</rt></ruby>くなります。"
    },
    "related": "やすくなる（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_026",
    "word": "セール",
    "reading": "セール",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "sale",
      "ja": "セール",
      "zh_TW": "sale",
      "zh_CN": "sale",
      "ko": "sale",
      "zh_HK": "sale",
      "fr": "sale"
    },
    "example": {
      "ja": "デパートでセールをしています。",
      "en": "There's a sale at the department store.",
      "zh_TW": "デパートでセールをしています。",
      "zh_CN": "デパートでセールをしています。",
      "ko": "デパートでセールをしています。",
      "zh_HK": "デパートでセールをしています。",
      "fr": "デパートでセールをしています。"
    },
    "related": "セール（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_027",
    "word": "お葬式",
    "reading": "おそうしき",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "funeral",
      "ja": "お葬式",
      "zh_TW": "funeral",
      "zh_CN": "funeral",
      "ko": "funeral",
      "zh_HK": "funeral",
      "fr": "funeral"
    },
    "example": {
      "ja": "<ruby>明日<rt>あした</rt></ruby>、<ruby>祖母<rt>そぼ</rt></ruby>のお<ruby>葬式<rt>そうしき</rt></ruby>があります。",
      "en": "My grandmother's funeral is tomorrow.",
      "zh_TW": "<ruby>明日<rt>あした</rt></ruby>、<ruby>祖母<rt>そぼ</rt></ruby>のお<ruby>葬式<rt>そうしき</rt></ruby>があります。",
      "zh_CN": "<ruby>明日<rt>あした</rt></ruby>、<ruby>祖母<rt>そぼ</rt></ruby>のお<ruby>葬式<rt>そうしき</rt></ruby>があります。",
      "ko": "<ruby>明日<rt>あした</rt></ruby>、<ruby>祖母<rt>そぼ</rt></ruby>のお<ruby>葬式<rt>そうしき</rt></ruby>があります。",
      "zh_HK": "<ruby>明日<rt>あした</rt></ruby>、<ruby>祖母<rt>そぼ</rt></ruby>のお<ruby>葬式<rt>そうしき</rt></ruby>があります。",
      "fr": "<ruby>明日<rt>あした</rt></ruby>、<ruby>祖母<rt>そぼ</rt></ruby>のお<ruby>葬式<rt>そうしき</rt></ruby>があります。"
    },
    "related": "おそうしき（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_028",
    "word": "貿易",
    "reading": "ぼうえき",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "(international) trade",
      "ja": "貿易",
      "zh_TW": "(international) trade",
      "zh_CN": "(international) trade",
      "ko": "(international) trade",
      "zh_HK": "(international) trade",
      "fr": "(international) trade"
    },
    "example": {
      "ja": "<ruby>日本<rt>にほん</rt></ruby>は<ruby>多<rt>おお</rt></ruby>くの<ruby>国<rt>くに</rt></ruby>と<ruby>貿易<rt>ぼうえき</rt></ruby>をしています。",
      "en": "Japan trades with many countries.",
      "zh_TW": "<ruby>日本<rt>にほん</rt></ruby>は<ruby>多<rt>おお</rt></ruby>くの<ruby>国<rt>くに</rt></ruby>と<ruby>貿易<rt>ぼうえき</rt></ruby>をしています。",
      "zh_CN": "<ruby>日本<rt>にほん</rt></ruby>は<ruby>多<rt>おお</rt></ruby>くの<ruby>国<rt>くに</rt></ruby>と<ruby>貿易<rt>ぼうえき</rt></ruby>をしています。",
      "ko": "<ruby>日本<rt>にほん</rt></ruby>は<ruby>多<rt>おお</rt></ruby>くの<ruby>国<rt>くに</rt></ruby>と<ruby>貿易<rt>ぼうえき</rt></ruby>をしています。",
      "zh_HK": "<ruby>日本<rt>にほん</rt></ruby>は<ruby>多<rt>おお</rt></ruby>くの<ruby>国<rt>くに</rt></ruby>と<ruby>貿易<rt>ぼうえき</rt></ruby>をしています。",
      "fr": "<ruby>日本<rt>にほん</rt></ruby>は<ruby>多<rt>おお</rt></ruby>くの<ruby>国<rt>くに</rt></ruby>と<ruby>貿易<rt>ぼうえき</rt></ruby>をしています。"
    },
    "related": "ぼうえき（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_029",
    "word": "政府",
    "reading": "せいふ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "government",
      "ja": "政府",
      "zh_TW": "government",
      "zh_CN": "government",
      "ko": "government",
      "zh_HK": "government",
      "fr": "government"
    },
    "example": {
      "ja": "<ruby>政府<rt>せいふ</rt></ruby>が<ruby>新<rt>あたら</rt></ruby>しい<ruby>政策<rt>せいさく</rt></ruby>を<ruby>発表<rt>はっぴょう</rt></ruby>しました。",
      "en": "The government announced a new policy.",
      "zh_TW": "<ruby>政府<rt>せいふ</rt></ruby>が<ruby>新<rt>あたら</rt></ruby>しい<ruby>政策<rt>せいさく</rt></ruby>を<ruby>発表<rt>はっぴょう</rt></ruby>しました。",
      "zh_CN": "<ruby>政府<rt>せいふ</rt></ruby>が<ruby>新<rt>あたら</rt></ruby>しい<ruby>政策<rt>せいさく</rt></ruby>を<ruby>発表<rt>はっぴょう</rt></ruby>しました。",
      "ko": "<ruby>政府<rt>せいふ</rt></ruby>が<ruby>新<rt>あたら</rt></ruby>しい<ruby>政策<rt>せいさく</rt></ruby>を<ruby>発表<rt>はっぴょう</rt></ruby>しました。",
      "zh_HK": "<ruby>政府<rt>せいふ</rt></ruby>が<ruby>新<rt>あたら</rt></ruby>しい<ruby>政策<rt>せいさく</rt></ruby>を<ruby>発表<rt>はっぴょう</rt></ruby>しました。",
      "fr": "<ruby>政府<rt>せいふ</rt></ruby>が<ruby>新<rt>あたら</rt></ruby>しい<ruby>政策<rt>せいさく</rt></ruby>を<ruby>発表<rt>はっぴょう</rt></ruby>しました。"
    },
    "related": "せいふ（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_030",
    "word": "最優先",
    "reading": "さいゆうせん",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "top priority",
      "ja": "最優先",
      "zh_TW": "top priority",
      "zh_CN": "top priority",
      "ko": "top priority",
      "zh_HK": "top priority",
      "fr": "top priority"
    },
    "example": {
      "ja": "<ruby>安全<rt>あんぜん</rt></ruby>が<ruby>最優先<rt>さいゆうせん</rt></ruby>です。",
      "en": "Safety is the top priority.",
      "zh_TW": "<ruby>安全<rt>あんぜん</rt></ruby>が<ruby>最優先<rt>さいゆうせん</rt></ruby>です。",
      "zh_CN": "<ruby>安全<rt>あんぜん</rt></ruby>が<ruby>最優先<rt>さいゆうせん</rt></ruby>です。",
      "ko": "<ruby>安全<rt>あんぜん</rt></ruby>が<ruby>最優先<rt>さいゆうせん</rt></ruby>です。",
      "zh_HK": "<ruby>安全<rt>あんぜん</rt></ruby>が<ruby>最優先<rt>さいゆうせん</rt></ruby>です。",
      "fr": "<ruby>安全<rt>あんぜん</rt></ruby>が<ruby>最優先<rt>さいゆうせん</rt></ruby>です。"
    },
    "related": "さいゆうせん（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_031",
    "word": "転生",
    "reading": "てんせい",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "reincarnation",
      "ja": "転生",
      "zh_TW": "reincarnation",
      "zh_CN": "reincarnation",
      "ko": "reincarnation",
      "zh_HK": "reincarnation",
      "fr": "reincarnation"
    },
    "example": {
      "ja": "<ruby>異世界<rt>いせかい</rt></ruby>に<ruby>転生<rt>てんせい</rt></ruby>するアニメが<ruby>人気<rt>にんき</rt></ruby>です。",
      "en": "Anime about being reincarnated in another world is popular.",
      "zh_TW": "<ruby>異世界<rt>いせかい</rt></ruby>に<ruby>転生<rt>てんせい</rt></ruby>するアニメが<ruby>人気<rt>にんき</rt></ruby>です。",
      "zh_CN": "<ruby>異世界<rt>いせかい</rt></ruby>に<ruby>転生<rt>てんせい</rt></ruby>するアニメが<ruby>人気<rt>にんき</rt></ruby>です。",
      "ko": "<ruby>異世界<rt>いせかい</rt></ruby>に<ruby>転生<rt>てんせい</rt></ruby>するアニメが<ruby>人気<rt>にんき</rt></ruby>です。",
      "zh_HK": "<ruby>異世界<rt>いせかい</rt></ruby>に<ruby>転生<rt>てんせい</rt></ruby>するアニメが<ruby>人気<rt>にんき</rt></ruby>です。",
      "fr": "<ruby>異世界<rt>いせかい</rt></ruby>に<ruby>転生<rt>てんせい</rt></ruby>するアニメが<ruby>人気<rt>にんき</rt></ruby>です。"
    },
    "related": "てんせい（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_032",
    "word": "生まれ変わる",
    "reading": "うまれかわる",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to be reborn",
      "ja": "生まれ変わる",
      "zh_TW": "to be reborn",
      "zh_CN": "to be reborn",
      "ko": "to be reborn",
      "zh_HK": "to be reborn",
      "fr": "to be reborn"
    },
    "example": {
      "ja": "<ruby>生<rt>う</rt></ruby>まれ<ruby>変<rt>か</rt></ruby>わったら、<ruby>鳥<rt>とり</rt></ruby>になりたいです。",
      "en": "If I'm reborn, I want to be a bird.",
      "zh_TW": "<ruby>生<rt>う</rt></ruby>まれ<ruby>変<rt>か</rt></ruby>わったら、<ruby>鳥<rt>とり</rt></ruby>になりたいです。",
      "zh_CN": "<ruby>生<rt>う</rt></ruby>まれ<ruby>変<rt>か</rt></ruby>わったら、<ruby>鳥<rt>とり</rt></ruby>になりたいです。",
      "ko": "<ruby>生<rt>う</rt></ruby>まれ<ruby>変<rt>か</rt></ruby>わったら、<ruby>鳥<rt>とり</rt></ruby>になりたいです。",
      "zh_HK": "<ruby>生<rt>う</rt></ruby>まれ<ruby>変<rt>か</rt></ruby>わったら、<ruby>鳥<rt>とり</rt></ruby>になりたいです。",
      "fr": "<ruby>生<rt>う</rt></ruby>まれ<ruby>変<rt>か</rt></ruby>わったら、<ruby>鳥<rt>とり</rt></ruby>になりたいです。"
    },
    "related": "うまれかわる（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_033",
    "word": "救う",
    "reading": "すくう",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to save; to rescue",
      "ja": "救う",
      "zh_TW": "to save; to rescue",
      "zh_CN": "to save; to rescue",
      "ko": "to save; to rescue",
      "zh_HK": "to save; to rescue",
      "fr": "to save; to rescue"
    },
    "example": {
      "ja": "<ruby>医者<rt>いしゃ</rt></ruby>は<ruby>多<rt>おお</rt></ruby>くの<ruby>命<rt>いのち</rt></ruby>を<ruby>救<rt>すく</rt></ruby>います。",
      "en": "Doctors save many lives.",
      "zh_TW": "<ruby>医者<rt>いしゃ</rt></ruby>は<ruby>多<rt>おお</rt></ruby>くの<ruby>命<rt>いのち</rt></ruby>を<ruby>救<rt>すく</rt></ruby>います。",
      "zh_CN": "<ruby>医者<rt>いしゃ</rt></ruby>は<ruby>多<rt>おお</rt></ruby>くの<ruby>命<rt>いのち</rt></ruby>を<ruby>救<rt>すく</rt></ruby>います。",
      "ko": "<ruby>医者<rt>いしゃ</rt></ruby>は<ruby>多<rt>おお</rt></ruby>くの<ruby>命<rt>いのち</rt></ruby>を<ruby>救<rt>すく</rt></ruby>います。",
      "zh_HK": "<ruby>医者<rt>いしゃ</rt></ruby>は<ruby>多<rt>おお</rt></ruby>くの<ruby>命<rt>いのち</rt></ruby>を<ruby>救<rt>すく</rt></ruby>います。",
      "fr": "<ruby>医者<rt>いしゃ</rt></ruby>は<ruby>多<rt>おお</rt></ruby>くの<ruby>命<rt>いのち</rt></ruby>を<ruby>救<rt>すく</rt></ruby>います。"
    },
    "related": "すくう（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_034",
    "word": "脱出",
    "reading": "だっしゅつ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "escape",
      "ja": "脱出",
      "zh_TW": "escape",
      "zh_CN": "escape",
      "ko": "escape",
      "zh_HK": "escape",
      "fr": "escape"
    },
    "example": {
      "ja": "<ruby>燃<rt>も</rt></ruby>えている<ruby>建物<rt>たてもの</rt></ruby>から<ruby>脱出<rt>だっしゅつ</rt></ruby>しました。",
      "en": "They escaped from the burning building.",
      "zh_TW": "<ruby>燃<rt>も</rt></ruby>えている<ruby>建物<rt>たてもの</rt></ruby>から<ruby>脱出<rt>だっしゅつ</rt></ruby>しました。",
      "zh_CN": "<ruby>燃<rt>も</rt></ruby>えている<ruby>建物<rt>たてもの</rt></ruby>から<ruby>脱出<rt>だっしゅつ</rt></ruby>しました。",
      "ko": "<ruby>燃<rt>も</rt></ruby>えている<ruby>建物<rt>たてもの</rt></ruby>から<ruby>脱出<rt>だっしゅつ</rt></ruby>しました。",
      "zh_HK": "<ruby>燃<rt>も</rt></ruby>えている<ruby>建物<rt>たてもの</rt></ruby>から<ruby>脱出<rt>だっしゅつ</rt></ruby>しました。",
      "fr": "<ruby>燃<rt>も</rt></ruby>えている<ruby>建物<rt>たてもの</rt></ruby>から<ruby>脱出<rt>だっしゅつ</rt></ruby>しました。"
    },
    "related": "だっしゅつ（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_035",
    "word": "逃げる",
    "reading": "にげる",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to run away; to flee",
      "ja": "逃げる",
      "zh_TW": "to run away; to flee",
      "zh_CN": "to run away; to flee",
      "ko": "to run away; to flee",
      "zh_HK": "to run away; to flee",
      "fr": "to run away; to flee"
    },
    "example": {
      "ja": "<ruby>猫<rt>ねこ</rt></ruby>が<ruby>逃<rt>に</rt></ruby>げてしまいました。",
      "en": "The cat ran away.",
      "zh_TW": "<ruby>猫<rt>ねこ</rt></ruby>が<ruby>逃<rt>に</rt></ruby>げてしまいました。",
      "zh_CN": "<ruby>猫<rt>ねこ</rt></ruby>が<ruby>逃<rt>に</rt></ruby>げてしまいました。",
      "ko": "<ruby>猫<rt>ねこ</rt></ruby>が<ruby>逃<rt>に</rt></ruby>げてしまいました。",
      "zh_HK": "<ruby>猫<rt>ねこ</rt></ruby>が<ruby>逃<rt>に</rt></ruby>げてしまいました。",
      "fr": "<ruby>猫<rt>ねこ</rt></ruby>が<ruby>逃<rt>に</rt></ruby>げてしまいました。"
    },
    "related": "にげる（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_036",
    "word": "荷物",
    "reading": "にもつ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "luggage; baggage; package",
      "ja": "荷物",
      "zh_TW": "luggage; baggage; package",
      "zh_CN": "luggage; baggage; package",
      "ko": "luggage; baggage; package",
      "zh_HK": "luggage; baggage; package",
      "fr": "luggage; baggage; package"
    },
    "example": {
      "ja": "<ruby>荷物<rt>にもつ</rt></ruby>が<ruby>重<rt>おも</rt></ruby>いです。",
      "en": "My luggage is heavy.",
      "zh_TW": "<ruby>荷物<rt>にもつ</rt></ruby>が<ruby>重<rt>おも</rt></ruby>いです。",
      "zh_CN": "<ruby>荷物<rt>にもつ</rt></ruby>が<ruby>重<rt>おも</rt></ruby>いです。",
      "ko": "<ruby>荷物<rt>にもつ</rt></ruby>が<ruby>重<rt>おも</rt></ruby>いです。",
      "zh_HK": "<ruby>荷物<rt>にもつ</rt></ruby>が<ruby>重<rt>おも</rt></ruby>いです。",
      "fr": "<ruby>荷物<rt>にもつ</rt></ruby>が<ruby>重<rt>おも</rt></ruby>いです。"
    },
    "related": "にもつ（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_037",
    "word": "多機能",
    "reading": "たきのう",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "multifunctional",
      "ja": "多機能",
      "zh_TW": "multifunctional",
      "zh_CN": "multifunctional",
      "ko": "multifunctional",
      "zh_HK": "multifunctional",
      "fr": "multifunctional"
    },
    "example": {
      "ja": "この<ruby>時計<rt>とけい</rt></ruby>はとても<ruby>多機能<rt>たきのう</rt></ruby>です。",
      "en": "This watch is very multifunctional.",
      "zh_TW": "この<ruby>時計<rt>とけい</rt></ruby>はとても<ruby>多機能<rt>たきのう</rt></ruby>です。",
      "zh_CN": "この<ruby>時計<rt>とけい</rt></ruby>はとても<ruby>多機能<rt>たきのう</rt></ruby>です。",
      "ko": "この<ruby>時計<rt>とけい</rt></ruby>はとても<ruby>多機能<rt>たきのう</rt></ruby>です。",
      "zh_HK": "この<ruby>時計<rt>とけい</rt></ruby>はとても<ruby>多機能<rt>たきのう</rt></ruby>です。",
      "fr": "この<ruby>時計<rt>とけい</rt></ruby>はとても<ruby>多機能<rt>たきのう</rt></ruby>です。"
    },
    "related": "たきのう（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_038",
    "word": "限定版",
    "reading": "げんていばん",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "limited edition",
      "ja": "限定版",
      "zh_TW": "limited edition",
      "zh_CN": "limited edition",
      "ko": "limited edition",
      "zh_HK": "limited edition",
      "fr": "limited edition"
    },
    "example": {
      "ja": "<ruby>限定版<rt>げんていばん</rt></ruby>のゲームを<ruby>買<rt>か</rt></ruby>いました。",
      "en": "I bought the limited edition of the game.",
      "zh_TW": "<ruby>限定版<rt>げんていばん</rt></ruby>のゲームを<ruby>買<rt>か</rt></ruby>いました。",
      "zh_CN": "<ruby>限定版<rt>げんていばん</rt></ruby>のゲームを<ruby>買<rt>か</rt></ruby>いました。",
      "ko": "<ruby>限定版<rt>げんていばん</rt></ruby>のゲームを<ruby>買<rt>か</rt></ruby>いました。",
      "zh_HK": "<ruby>限定版<rt>げんていばん</rt></ruby>のゲームを<ruby>買<rt>か</rt></ruby>いました。",
      "fr": "<ruby>限定版<rt>げんていばん</rt></ruby>のゲームを<ruby>買<rt>か</rt></ruby>いました。"
    },
    "related": "げんていばん（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_039",
    "word": "現地人",
    "reading": "げんちじん",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "local (person)",
      "ja": "現地人",
      "zh_TW": "local (person)",
      "zh_CN": "local (person)",
      "ko": "local (person)",
      "zh_HK": "local (person)",
      "fr": "local (person)"
    },
    "example": {
      "ja": "<ruby>現地人<rt>げんちじん</rt></ruby>しか<ruby>知<rt>し</rt></ruby>らないお<ruby>店<rt>みせ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きました。",
      "en": "I went to a shop that only locals know about.",
      "zh_TW": "<ruby>現地人<rt>げんちじん</rt></ruby>しか<ruby>知<rt>し</rt></ruby>らないお<ruby>店<rt>みせ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きました。",
      "zh_CN": "<ruby>現地人<rt>げんちじん</rt></ruby>しか<ruby>知<rt>し</rt></ruby>らないお<ruby>店<rt>みせ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きました。",
      "ko": "<ruby>現地人<rt>げんちじん</rt></ruby>しか<ruby>知<rt>し</rt></ruby>らないお<ruby>店<rt>みせ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きました。",
      "zh_HK": "<ruby>現地人<rt>げんちじん</rt></ruby>しか<ruby>知<rt>し</rt></ruby>らないお<ruby>店<rt>みせ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きました。",
      "fr": "<ruby>現地人<rt>げんちじん</rt></ruby>しか<ruby>知<rt>し</rt></ruby>らないお<ruby>店<rt>みせ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きました。"
    },
    "related": "げんちじん（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_040",
    "word": "車輪",
    "reading": "しゃりん",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "wheel",
      "ja": "車輪",
      "zh_TW": "wheel",
      "zh_CN": "wheel",
      "ko": "wheel",
      "zh_HK": "wheel",
      "fr": "wheel"
    },
    "example": {
      "ja": "<ruby>自転車<rt>じてんしゃ</rt></ruby>の<ruby>車輪<rt>しゃりん</rt></ruby>が<ruby>壊<rt>こわ</rt></ruby>れました。",
      "en": "The bicycle wheel broke.",
      "zh_TW": "<ruby>自転車<rt>じてんしゃ</rt></ruby>の<ruby>車輪<rt>しゃりん</rt></ruby>が<ruby>壊<rt>こわ</rt></ruby>れました。",
      "zh_CN": "<ruby>自転車<rt>じてんしゃ</rt></ruby>の<ruby>車輪<rt>しゃりん</rt></ruby>が<ruby>壊<rt>こわ</rt></ruby>れました。",
      "ko": "<ruby>自転車<rt>じてんしゃ</rt></ruby>の<ruby>車輪<rt>しゃりん</rt></ruby>が<ruby>壊<rt>こわ</rt></ruby>れました。",
      "zh_HK": "<ruby>自転車<rt>じてんしゃ</rt></ruby>の<ruby>車輪<rt>しゃりん</rt></ruby>が<ruby>壊<rt>こわ</rt></ruby>れました。",
      "fr": "<ruby>自転車<rt>じてんしゃ</rt></ruby>の<ruby>車輪<rt>しゃりん</rt></ruby>が<ruby>壊<rt>こわ</rt></ruby>れました。"
    },
    "related": "しゃりん（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_041",
    "word": "口に合わない",
    "reading": "くちにあわない",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "not to one's taste",
      "ja": "口に合わない",
      "zh_TW": "not to one's taste",
      "zh_CN": "not to one's taste",
      "ko": "not to one's taste",
      "zh_HK": "not to one's taste",
      "fr": "not to one's taste"
    },
    "example": {
      "ja": "この<ruby>料理<rt>りょうり</rt></ruby>は<ruby>私<rt>わたし</rt></ruby>の<ruby>口<rt>くち</rt></ruby>に<ruby>合<rt>あ</rt></ruby>いません。",
      "en": "This dish isn't to my taste.",
      "zh_TW": "この<ruby>料理<rt>りょうり</rt></ruby>は<ruby>私<rt>わたし</rt></ruby>の<ruby>口<rt>くち</rt></ruby>に<ruby>合<rt>あ</rt></ruby>いません。",
      "zh_CN": "この<ruby>料理<rt>りょうり</rt></ruby>は<ruby>私<rt>わたし</rt></ruby>の<ruby>口<rt>くち</rt></ruby>に<ruby>合<rt>あ</rt></ruby>いません。",
      "ko": "この<ruby>料理<rt>りょうり</rt></ruby>は<ruby>私<rt>わたし</rt></ruby>の<ruby>口<rt>くち</rt></ruby>に<ruby>合<rt>あ</rt></ruby>いません。",
      "zh_HK": "この<ruby>料理<rt>りょうり</rt></ruby>は<ruby>私<rt>わたし</rt></ruby>の<ruby>口<rt>くち</rt></ruby>に<ruby>合<rt>あ</rt></ruby>いません。",
      "fr": "この<ruby>料理<rt>りょうり</rt></ruby>は<ruby>私<rt>わたし</rt></ruby>の<ruby>口<rt>くち</rt></ruby>に<ruby>合<rt>あ</rt></ruby>いません。"
    },
    "related": "くちにあわない（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_042",
    "word": "保守的",
    "reading": "ほしゅてき",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "conservative",
      "ja": "保守的",
      "zh_TW": "conservative",
      "zh_CN": "conservative",
      "ko": "conservative",
      "zh_HK": "conservative",
      "fr": "conservative"
    },
    "example": {
      "ja": "<ruby>祖父<rt>そふ</rt></ruby>は<ruby>考<rt>かんが</rt></ruby>え<ruby>方<rt>かた</rt></ruby>が<ruby>保守的<rt>ほしゅてき</rt></ruby>です。",
      "en": "My grandfather has a conservative way of thinking.",
      "zh_TW": "<ruby>祖父<rt>そふ</rt></ruby>は<ruby>考<rt>かんが</rt></ruby>え<ruby>方<rt>かた</rt></ruby>が<ruby>保守的<rt>ほしゅてき</rt></ruby>です。",
      "zh_CN": "<ruby>祖父<rt>そふ</rt></ruby>は<ruby>考<rt>かんが</rt></ruby>え<ruby>方<rt>かた</rt></ruby>が<ruby>保守的<rt>ほしゅてき</rt></ruby>です。",
      "ko": "<ruby>祖父<rt>そふ</rt></ruby>は<ruby>考<rt>かんが</rt></ruby>え<ruby>方<rt>かた</rt></ruby>が<ruby>保守的<rt>ほしゅてき</rt></ruby>です。",
      "zh_HK": "<ruby>祖父<rt>そふ</rt></ruby>は<ruby>考<rt>かんが</rt></ruby>え<ruby>方<rt>かた</rt></ruby>が<ruby>保守的<rt>ほしゅてき</rt></ruby>です。",
      "fr": "<ruby>祖父<rt>そふ</rt></ruby>は<ruby>考<rt>かんが</rt></ruby>え<ruby>方<rt>かた</rt></ruby>が<ruby>保守的<rt>ほしゅてき</rt></ruby>です。"
    },
    "related": "ほしゅてき（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_043",
    "word": "制限する",
    "reading": "せいげんする",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to restrict; to limit",
      "ja": "制限する",
      "zh_TW": "to restrict; to limit",
      "zh_CN": "to restrict; to limit",
      "ko": "to restrict; to limit",
      "zh_HK": "to restrict; to limit",
      "fr": "to restrict; to limit"
    },
    "example": {
      "ja": "<ruby>子<rt>こ</rt></ruby>どものゲーム<ruby>時間<rt>じかん</rt></ruby>を<ruby>制限<rt>せいげん</rt></ruby>しています。",
      "en": "I limit my child's gaming time.",
      "zh_TW": "<ruby>子<rt>こ</rt></ruby>どものゲーム<ruby>時間<rt>じかん</rt></ruby>を<ruby>制限<rt>せいげん</rt></ruby>しています。",
      "zh_CN": "<ruby>子<rt>こ</rt></ruby>どものゲーム<ruby>時間<rt>じかん</rt></ruby>を<ruby>制限<rt>せいげん</rt></ruby>しています。",
      "ko": "<ruby>子<rt>こ</rt></ruby>どものゲーム<ruby>時間<rt>じかん</rt></ruby>を<ruby>制限<rt>せいげん</rt></ruby>しています。",
      "zh_HK": "<ruby>子<rt>こ</rt></ruby>どものゲーム<ruby>時間<rt>じかん</rt></ruby>を<ruby>制限<rt>せいげん</rt></ruby>しています。",
      "fr": "<ruby>子<rt>こ</rt></ruby>どものゲーム<ruby>時間<rt>じかん</rt></ruby>を<ruby>制限<rt>せいげん</rt></ruby>しています。"
    },
    "related": "せいげんする（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_044",
    "word": "あひる",
    "reading": "あひる",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "duck (domestic)",
      "ja": "あひる",
      "zh_TW": "duck (domestic)",
      "zh_CN": "duck (domestic)",
      "ko": "duck (domestic)",
      "zh_HK": "duck (domestic)",
      "fr": "duck (domestic)"
    },
    "example": {
      "ja": "<ruby>池<rt>いけ</rt></ruby>にあひるがいます。",
      "en": "There are ducks in the pond.",
      "zh_TW": "<ruby>池<rt>いけ</rt></ruby>にあひるがいます。",
      "zh_CN": "<ruby>池<rt>いけ</rt></ruby>にあひるがいます。",
      "ko": "<ruby>池<rt>いけ</rt></ruby>にあひるがいます。",
      "zh_HK": "<ruby>池<rt>いけ</rt></ruby>にあひるがいます。",
      "fr": "<ruby>池<rt>いけ</rt></ruby>にあひるがいます。"
    },
    "related": "あひる（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_045",
    "word": "渋滞",
    "reading": "じゅうたい",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "traffic jam",
      "ja": "渋滞",
      "zh_TW": "traffic jam",
      "zh_CN": "traffic jam",
      "ko": "traffic jam",
      "zh_HK": "traffic jam",
      "fr": "traffic jam"
    },
    "example": {
      "ja": "<ruby>道<rt>みち</rt></ruby>が<ruby>渋滞<rt>じゅうたい</rt></ruby>しています。",
      "en": "The road is jammed with traffic.",
      "zh_TW": "<ruby>道<rt>みち</rt></ruby>が<ruby>渋滞<rt>じゅうたい</rt></ruby>しています。",
      "zh_CN": "<ruby>道<rt>みち</rt></ruby>が<ruby>渋滞<rt>じゅうたい</rt></ruby>しています。",
      "ko": "<ruby>道<rt>みち</rt></ruby>が<ruby>渋滞<rt>じゅうたい</rt></ruby>しています。",
      "zh_HK": "<ruby>道<rt>みち</rt></ruby>が<ruby>渋滞<rt>じゅうたい</rt></ruby>しています。",
      "fr": "<ruby>道<rt>みち</rt></ruby>が<ruby>渋滞<rt>じゅうたい</rt></ruby>しています。"
    },
    "related": "じゅうたい（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_046",
    "word": "お年寄り",
    "reading": "おとしより",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "elderly person",
      "ja": "お年寄り",
      "zh_TW": "elderly person",
      "zh_CN": "elderly person",
      "ko": "elderly person",
      "zh_HK": "elderly person",
      "fr": "elderly person"
    },
    "example": {
      "ja": "バスでお<ruby>年寄<rt>としよ</rt></ruby>りに<ruby>席<rt>せき</rt></ruby>を<ruby>譲<rt>ゆず</rt></ruby>りました。",
      "en": "I gave my seat to an elderly person on the bus.",
      "zh_TW": "バスでお<ruby>年寄<rt>としよ</rt></ruby>りに<ruby>席<rt>せき</rt></ruby>を<ruby>譲<rt>ゆず</rt></ruby>りました。",
      "zh_CN": "バスでお<ruby>年寄<rt>としよ</rt></ruby>りに<ruby>席<rt>せき</rt></ruby>を<ruby>譲<rt>ゆず</rt></ruby>りました。",
      "ko": "バスでお<ruby>年寄<rt>としよ</rt></ruby>りに<ruby>席<rt>せき</rt></ruby>を<ruby>譲<rt>ゆず</rt></ruby>りました。",
      "zh_HK": "バスでお<ruby>年寄<rt>としよ</rt></ruby>りに<ruby>席<rt>せき</rt></ruby>を<ruby>譲<rt>ゆず</rt></ruby>りました。",
      "fr": "バスでお<ruby>年寄<rt>としよ</rt></ruby>りに<ruby>席<rt>せき</rt></ruby>を<ruby>譲<rt>ゆず</rt></ruby>りました。"
    },
    "related": "おとしより（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_047",
    "word": "優しい人",
    "reading": "やさしいひと",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "kind person",
      "ja": "優しい人",
      "zh_TW": "kind person",
      "zh_CN": "kind person",
      "ko": "kind person",
      "zh_HK": "kind person",
      "fr": "kind person"
    },
    "example": {
      "ja": "<ruby>彼<rt>かれ</rt></ruby>はとても<ruby>優<rt>やさ</rt></ruby>しい<ruby>人<rt>ひと</rt></ruby>です。",
      "en": "He is a very kind person.",
      "zh_TW": "<ruby>彼<rt>かれ</rt></ruby>はとても<ruby>優<rt>やさ</rt></ruby>しい<ruby>人<rt>ひと</rt></ruby>です。",
      "zh_CN": "<ruby>彼<rt>かれ</rt></ruby>はとても<ruby>優<rt>やさ</rt></ruby>しい<ruby>人<rt>ひと</rt></ruby>です。",
      "ko": "<ruby>彼<rt>かれ</rt></ruby>はとても<ruby>優<rt>やさ</rt></ruby>しい<ruby>人<rt>ひと</rt></ruby>です。",
      "zh_HK": "<ruby>彼<rt>かれ</rt></ruby>はとても<ruby>優<rt>やさ</rt></ruby>しい<ruby>人<rt>ひと</rt></ruby>です。",
      "fr": "<ruby>彼<rt>かれ</rt></ruby>はとても<ruby>優<rt>やさ</rt></ruby>しい<ruby>人<rt>ひと</rt></ruby>です。"
    },
    "related": "やさしいひと（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_048",
    "word": "豆乳",
    "reading": "とうにゅう",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "soy milk",
      "ja": "豆乳",
      "zh_TW": "soy milk",
      "zh_CN": "soy milk",
      "ko": "soy milk",
      "zh_HK": "soy milk",
      "fr": "soy milk"
    },
    "example": {
      "ja": "<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>豆乳<rt>とうにゅう</rt></ruby>を<ruby>飲<rt>の</rt></ruby>みます。",
      "en": "I drink soy milk every morning.",
      "zh_TW": "<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>豆乳<rt>とうにゅう</rt></ruby>を<ruby>飲<rt>の</rt></ruby>みます。",
      "zh_CN": "<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>豆乳<rt>とうにゅう</rt></ruby>を<ruby>飲<rt>の</rt></ruby>みます。",
      "ko": "<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>豆乳<rt>とうにゅう</rt></ruby>を<ruby>飲<rt>の</rt></ruby>みます。",
      "zh_HK": "<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>豆乳<rt>とうにゅう</rt></ruby>を<ruby>飲<rt>の</rt></ruby>みます。",
      "fr": "<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>豆乳<rt>とうにゅう</rt></ruby>を<ruby>飲<rt>の</rt></ruby>みます。"
    },
    "related": "とうにゅう（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_049",
    "word": "寒い",
    "reading": "さむい",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "cold (weather, air)",
      "ja": "寒い",
      "zh_TW": "cold (weather, air)",
      "zh_CN": "cold (weather, air)",
      "ko": "cold (weather, air)",
      "zh_HK": "cold (weather, air)",
      "fr": "cold (weather, air)"
    },
    "example": {
      "ja": "<ruby>今日<rt>きょう</rt></ruby>はとても<ruby>寒<rt>さむ</rt></ruby>いです。",
      "en": "It's very cold today.",
      "zh_TW": "<ruby>今日<rt>きょう</rt></ruby>はとても<ruby>寒<rt>さむ</rt></ruby>いです。",
      "zh_CN": "<ruby>今日<rt>きょう</rt></ruby>はとても<ruby>寒<rt>さむ</rt></ruby>いです。",
      "ko": "<ruby>今日<rt>きょう</rt></ruby>はとても<ruby>寒<rt>さむ</rt></ruby>いです。",
      "zh_HK": "<ruby>今日<rt>きょう</rt></ruby>はとても<ruby>寒<rt>さむ</rt></ruby>いです。",
      "fr": "<ruby>今日<rt>きょう</rt></ruby>はとても<ruby>寒<rt>さむ</rt></ruby>いです。"
    },
    "related": "さむい（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_050",
    "word": "冷たい",
    "reading": "つめたい",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "cold (to the touch); cold-hearted",
      "ja": "冷たい",
      "zh_TW": "cold (to the touch); cold-hearted",
      "zh_CN": "cold (to the touch); cold-hearted",
      "ko": "cold (to the touch); cold-hearted",
      "zh_HK": "cold (to the touch); cold-hearted",
      "fr": "cold (to the touch); cold-hearted"
    },
    "example": {
      "ja": "<ruby>冷<rt>つめ</rt></ruby>たい<ruby>水<rt>みず</rt></ruby>が<ruby>飲<rt>の</rt></ruby>みたいです。",
      "en": "I want to drink cold water.",
      "zh_TW": "<ruby>冷<rt>つめ</rt></ruby>たい<ruby>水<rt>みず</rt></ruby>が<ruby>飲<rt>の</rt></ruby>みたいです。",
      "zh_CN": "<ruby>冷<rt>つめ</rt></ruby>たい<ruby>水<rt>みず</rt></ruby>が<ruby>飲<rt>の</rt></ruby>みたいです。",
      "ko": "<ruby>冷<rt>つめ</rt></ruby>たい<ruby>水<rt>みず</rt></ruby>が<ruby>飲<rt>の</rt></ruby>みたいです。",
      "zh_HK": "<ruby>冷<rt>つめ</rt></ruby>たい<ruby>水<rt>みず</rt></ruby>が<ruby>飲<rt>の</rt></ruby>みたいです。",
      "fr": "<ruby>冷<rt>つめ</rt></ruby>たい<ruby>水<rt>みず</rt></ruby>が<ruby>飲<rt>の</rt></ruby>みたいです。"
    },
    "related": "つめたい（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_051",
    "word": "舌が肥える",
    "reading": "したがこえる",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to have a refined palate",
      "ja": "舌が肥える",
      "zh_TW": "to have a refined palate",
      "zh_CN": "to have a refined palate",
      "ko": "to have a refined palate",
      "zh_HK": "to have a refined palate",
      "fr": "to have a refined palate"
    },
    "example": {
      "ja": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>舌<rt>した</rt></ruby>が<ruby>肥<rt>こ</rt></ruby>えています。",
      "en": "He has a refined palate.",
      "zh_TW": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>舌<rt>した</rt></ruby>が<ruby>肥<rt>こ</rt></ruby>えています。",
      "zh_CN": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>舌<rt>した</rt></ruby>が<ruby>肥<rt>こ</rt></ruby>えています。",
      "ko": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>舌<rt>した</rt></ruby>が<ruby>肥<rt>こ</rt></ruby>えています。",
      "zh_HK": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>舌<rt>した</rt></ruby>が<ruby>肥<rt>こ</rt></ruby>えています。",
      "fr": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>舌<rt>した</rt></ruby>が<ruby>肥<rt>こ</rt></ruby>えています。"
    },
    "related": "したがこえる（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_052",
    "word": "蒸す",
    "reading": "むす",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to steam; to be humid",
      "ja": "蒸す",
      "zh_TW": "to steam; to be humid",
      "zh_CN": "to steam; to be humid",
      "ko": "to steam; to be humid",
      "zh_HK": "to steam; to be humid",
      "fr": "to steam; to be humid"
    },
    "example": {
      "ja": "<ruby>野菜<rt>やさい</rt></ruby>を<ruby>蒸<rt>む</rt></ruby>して<ruby>食<rt>た</rt></ruby>べます。",
      "en": "I steam vegetables to eat.",
      "zh_TW": "<ruby>野菜<rt>やさい</rt></ruby>を<ruby>蒸<rt>む</rt></ruby>して<ruby>食<rt>た</rt></ruby>べます。",
      "zh_CN": "<ruby>野菜<rt>やさい</rt></ruby>を<ruby>蒸<rt>む</rt></ruby>して<ruby>食<rt>た</rt></ruby>べます。",
      "ko": "<ruby>野菜<rt>やさい</rt></ruby>を<ruby>蒸<rt>む</rt></ruby>して<ruby>食<rt>た</rt></ruby>べます。",
      "zh_HK": "<ruby>野菜<rt>やさい</rt></ruby>を<ruby>蒸<rt>む</rt></ruby>して<ruby>食<rt>た</rt></ruby>べます。",
      "fr": "<ruby>野菜<rt>やさい</rt></ruby>を<ruby>蒸<rt>む</rt></ruby>して<ruby>食<rt>た</rt></ruby>べます。"
    },
    "related": "むす（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_053",
    "word": "湯気",
    "reading": "ゆげ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "steam (rising)",
      "ja": "湯気",
      "zh_TW": "steam (rising)",
      "zh_CN": "steam (rising)",
      "ko": "steam (rising)",
      "zh_HK": "steam (rising)",
      "fr": "steam (rising)"
    },
    "example": {
      "ja": "ラーメンから<ruby>湯気<rt>ゆげ</rt></ruby>が<ruby>出<rt>で</rt></ruby>ています。",
      "en": "Steam is rising from the ramen.",
      "zh_TW": "ラーメンから<ruby>湯気<rt>ゆげ</rt></ruby>が<ruby>出<rt>で</rt></ruby>ています。",
      "zh_CN": "ラーメンから<ruby>湯気<rt>ゆげ</rt></ruby>が<ruby>出<rt>で</rt></ruby>ています。",
      "ko": "ラーメンから<ruby>湯気<rt>ゆげ</rt></ruby>が<ruby>出<rt>で</rt></ruby>ています。",
      "zh_HK": "ラーメンから<ruby>湯気<rt>ゆげ</rt></ruby>が<ruby>出<rt>で</rt></ruby>ています。",
      "fr": "ラーメンから<ruby>湯気<rt>ゆげ</rt></ruby>が<ruby>出<rt>で</rt></ruby>ています。"
    },
    "related": "ゆげ（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_054",
    "word": "風物詩",
    "reading": "ふうぶつし",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "seasonal tradition; something that evokes a season",
      "ja": "風物詩",
      "zh_TW": "seasonal tradition; something that evokes a season",
      "zh_CN": "seasonal tradition; something that evokes a season",
      "ko": "seasonal tradition; something that evokes a season",
      "zh_HK": "seasonal tradition; something that evokes a season",
      "fr": "seasonal tradition; something that evokes a season"
    },
    "example": {
      "ja": "<ruby>花火<rt>はなび</rt></ruby>は<ruby>夏<rt>なつ</rt></ruby>の<ruby>風物詩<rt>ふうぶつし</rt></ruby>です。",
      "en": "Fireworks are a classic sign of summer.",
      "zh_TW": "<ruby>花火<rt>はなび</rt></ruby>は<ruby>夏<rt>なつ</rt></ruby>の<ruby>風物詩<rt>ふうぶつし</rt></ruby>です。",
      "zh_CN": "<ruby>花火<rt>はなび</rt></ruby>は<ruby>夏<rt>なつ</rt></ruby>の<ruby>風物詩<rt>ふうぶつし</rt></ruby>です。",
      "ko": "<ruby>花火<rt>はなび</rt></ruby>は<ruby>夏<rt>なつ</rt></ruby>の<ruby>風物詩<rt>ふうぶつし</rt></ruby>です。",
      "zh_HK": "<ruby>花火<rt>はなび</rt></ruby>は<ruby>夏<rt>なつ</rt></ruby>の<ruby>風物詩<rt>ふうぶつし</rt></ruby>です。",
      "fr": "<ruby>花火<rt>はなび</rt></ruby>は<ruby>夏<rt>なつ</rt></ruby>の<ruby>風物詩<rt>ふうぶつし</rt></ruby>です。"
    },
    "related": "ふうぶつし（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_055",
    "word": "人混み",
    "reading": "ひとごみ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "crowd",
      "ja": "人混み",
      "zh_TW": "crowd",
      "zh_CN": "crowd",
      "ko": "crowd",
      "zh_HK": "crowd",
      "fr": "crowd"
    },
    "example": {
      "ja": "<ruby>人混<rt>ひとご</rt></ruby>みが<ruby>苦手<rt>にがて</rt></ruby>です。",
      "en": "I don't like crowds.",
      "zh_TW": "<ruby>人混<rt>ひとご</rt></ruby>みが<ruby>苦手<rt>にがて</rt></ruby>です。",
      "zh_CN": "<ruby>人混<rt>ひとご</rt></ruby>みが<ruby>苦手<rt>にがて</rt></ruby>です。",
      "ko": "<ruby>人混<rt>ひとご</rt></ruby>みが<ruby>苦手<rt>にがて</rt></ruby>です。",
      "zh_HK": "<ruby>人混<rt>ひとご</rt></ruby>みが<ruby>苦手<rt>にがて</rt></ruby>です。",
      "fr": "<ruby>人混<rt>ひとご</rt></ruby>みが<ruby>苦手<rt>にがて</rt></ruby>です。"
    },
    "related": "ひとごみ（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_056",
    "word": "落ち着いた",
    "reading": "おちついた",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "calm; relaxed; subdued",
      "ja": "落ち着いた",
      "zh_TW": "calm; relaxed; subdued",
      "zh_CN": "calm; relaxed; subdued",
      "ko": "calm; relaxed; subdued",
      "zh_HK": "calm; relaxed; subdued",
      "fr": "calm; relaxed; subdued"
    },
    "example": {
      "ja": "<ruby>落<rt>お</rt></ruby>ち<ruby>着<rt>つ</rt></ruby>いた<ruby>雰囲気<rt>ふんいき</rt></ruby>のカフェが<ruby>好<rt>す</rt></ruby>きです。",
      "en": "I like cafés with a calm atmosphere.",
      "zh_TW": "<ruby>落<rt>お</rt></ruby>ち<ruby>着<rt>つ</rt></ruby>いた<ruby>雰囲気<rt>ふんいき</rt></ruby>のカフェが<ruby>好<rt>す</rt></ruby>きです。",
      "zh_CN": "<ruby>落<rt>お</rt></ruby>ち<ruby>着<rt>つ</rt></ruby>いた<ruby>雰囲気<rt>ふんいき</rt></ruby>のカフェが<ruby>好<rt>す</rt></ruby>きです。",
      "ko": "<ruby>落<rt>お</rt></ruby>ち<ruby>着<rt>つ</rt></ruby>いた<ruby>雰囲気<rt>ふんいき</rt></ruby>のカフェが<ruby>好<rt>す</rt></ruby>きです。",
      "zh_HK": "<ruby>落<rt>お</rt></ruby>ち<ruby>着<rt>つ</rt></ruby>いた<ruby>雰囲気<rt>ふんいき</rt></ruby>のカフェが<ruby>好<rt>す</rt></ruby>きです。",
      "fr": "<ruby>落<rt>お</rt></ruby>ち<ruby>着<rt>つ</rt></ruby>いた<ruby>雰囲気<rt>ふんいき</rt></ruby>のカフェが<ruby>好<rt>す</rt></ruby>きです。"
    },
    "related": "おちついた（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_057",
    "word": "見せびらかす",
    "reading": "みせびらかす",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to show off",
      "ja": "見せびらかす",
      "zh_TW": "to show off",
      "zh_CN": "to show off",
      "ko": "to show off",
      "zh_HK": "to show off",
      "fr": "to show off"
    },
    "example": {
      "ja": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>新<rt>あたら</rt></ruby>しい<ruby>時計<rt>とけい</rt></ruby>を<ruby>見<rt>み</rt></ruby>せびらかしています。",
      "en": "He's showing off his new watch.",
      "zh_TW": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>新<rt>あたら</rt></ruby>しい<ruby>時計<rt>とけい</rt></ruby>を<ruby>見<rt>み</rt></ruby>せびらかしています。",
      "zh_CN": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>新<rt>あたら</rt></ruby>しい<ruby>時計<rt>とけい</rt></ruby>を<ruby>見<rt>み</rt></ruby>せびらかしています。",
      "ko": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>新<rt>あたら</rt></ruby>しい<ruby>時計<rt>とけい</rt></ruby>を<ruby>見<rt>み</rt></ruby>せびらかしています。",
      "zh_HK": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>新<rt>あたら</rt></ruby>しい<ruby>時計<rt>とけい</rt></ruby>を<ruby>見<rt>み</rt></ruby>せびらかしています。",
      "fr": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>新<rt>あたら</rt></ruby>しい<ruby>時計<rt>とけい</rt></ruby>を<ruby>見<rt>み</rt></ruby>せびらかしています。"
    },
    "related": "みせびらかす（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_058",
    "word": "本屋",
    "reading": "ほんや",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "bookstore",
      "ja": "本屋",
      "zh_TW": "bookstore",
      "zh_CN": "bookstore",
      "ko": "bookstore",
      "zh_HK": "bookstore",
      "fr": "bookstore"
    },
    "example": {
      "ja": "<ruby>駅前<rt>えきまえ</rt></ruby>に<ruby>本屋<rt>ほんや</rt></ruby>があります。",
      "en": "There's a bookstore in front of the station.",
      "zh_TW": "<ruby>駅前<rt>えきまえ</rt></ruby>に<ruby>本屋<rt>ほんや</rt></ruby>があります。",
      "zh_CN": "<ruby>駅前<rt>えきまえ</rt></ruby>に<ruby>本屋<rt>ほんや</rt></ruby>があります。",
      "ko": "<ruby>駅前<rt>えきまえ</rt></ruby>に<ruby>本屋<rt>ほんや</rt></ruby>があります。",
      "zh_HK": "<ruby>駅前<rt>えきまえ</rt></ruby>に<ruby>本屋<rt>ほんや</rt></ruby>があります。",
      "fr": "<ruby>駅前<rt>えきまえ</rt></ruby>に<ruby>本屋<rt>ほんや</rt></ruby>があります。"
    },
    "related": "ほんや（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_059",
    "word": "天国",
    "reading": "てんごく",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "heaven; paradise",
      "ja": "天国",
      "zh_TW": "heaven; paradise",
      "zh_CN": "heaven; paradise",
      "ko": "heaven; paradise",
      "zh_HK": "heaven; paradise",
      "fr": "heaven; paradise"
    },
    "example": {
      "ja": "ここは<ruby>猫好<rt>ねこず</rt></ruby>きには<ruby>天国<rt>てんごく</rt></ruby>です。",
      "en": "This place is heaven for cat lovers.",
      "zh_TW": "ここは<ruby>猫好<rt>ねこず</rt></ruby>きには<ruby>天国<rt>てんごく</rt></ruby>です。",
      "zh_CN": "ここは<ruby>猫好<rt>ねこず</rt></ruby>きには<ruby>天国<rt>てんごく</rt></ruby>です。",
      "ko": "ここは<ruby>猫好<rt>ねこず</rt></ruby>きには<ruby>天国<rt>てんごく</rt></ruby>です。",
      "zh_HK": "ここは<ruby>猫好<rt>ねこず</rt></ruby>きには<ruby>天国<rt>てんごく</rt></ruby>です。",
      "fr": "ここは<ruby>猫好<rt>ねこず</rt></ruby>きには<ruby>天国<rt>てんごく</rt></ruby>です。"
    },
    "related": "てんごく（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_060",
    "word": "状況",
    "reading": "じょうきょう",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "situation; circumstances",
      "ja": "状況",
      "zh_TW": "situation; circumstances",
      "zh_CN": "situation; circumstances",
      "ko": "situation; circumstances",
      "zh_HK": "situation; circumstances",
      "fr": "situation; circumstances"
    },
    "example": {
      "ja": "<ruby>今<rt>いま</rt></ruby>の<ruby>状況<rt>じょうきょう</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えてください。",
      "en": "Please tell me the current situation.",
      "zh_TW": "<ruby>今<rt>いま</rt></ruby>の<ruby>状況<rt>じょうきょう</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えてください。",
      "zh_CN": "<ruby>今<rt>いま</rt></ruby>の<ruby>状況<rt>じょうきょう</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えてください。",
      "ko": "<ruby>今<rt>いま</rt></ruby>の<ruby>状況<rt>じょうきょう</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えてください。",
      "zh_HK": "<ruby>今<rt>いま</rt></ruby>の<ruby>状況<rt>じょうきょう</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えてください。",
      "fr": "<ruby>今<rt>いま</rt></ruby>の<ruby>状況<rt>じょうきょう</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えてください。"
    },
    "related": "じょうきょう（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_061",
    "word": "中心地",
    "reading": "ちゅうしんち",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "center; hub",
      "ja": "中心地",
      "zh_TW": "center; hub",
      "zh_CN": "center; hub",
      "ko": "center; hub",
      "zh_HK": "center; hub",
      "fr": "center; hub"
    },
    "example": {
      "ja": "ここは<ruby>町<rt>まち</rt></ruby>の<ruby>中心地<rt>ちゅうしんち</rt></ruby>です。",
      "en": "This is the center of town.",
      "zh_TW": "ここは<ruby>町<rt>まち</rt></ruby>の<ruby>中心地<rt>ちゅうしんち</rt></ruby>です。",
      "zh_CN": "ここは<ruby>町<rt>まち</rt></ruby>の<ruby>中心地<rt>ちゅうしんち</rt></ruby>です。",
      "ko": "ここは<ruby>町<rt>まち</rt></ruby>の<ruby>中心地<rt>ちゅうしんち</rt></ruby>です。",
      "zh_HK": "ここは<ruby>町<rt>まち</rt></ruby>の<ruby>中心地<rt>ちゅうしんち</rt></ruby>です。",
      "fr": "ここは<ruby>町<rt>まち</rt></ruby>の<ruby>中心地<rt>ちゅうしんち</rt></ruby>です。"
    },
    "related": "ちゅうしんち（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_062",
    "word": "噴火",
    "reading": "ふんか",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "(volcanic) eruption",
      "ja": "噴火",
      "zh_TW": "(volcanic) eruption",
      "zh_CN": "(volcanic) eruption",
      "ko": "(volcanic) eruption",
      "zh_HK": "(volcanic) eruption",
      "fr": "(volcanic) eruption"
    },
    "example": {
      "ja": "<ruby>火山<rt>かざん</rt></ruby>が<ruby>噴火<rt>ふんか</rt></ruby>しました。",
      "en": "The volcano erupted.",
      "zh_TW": "<ruby>火山<rt>かざん</rt></ruby>が<ruby>噴火<rt>ふんか</rt></ruby>しました。",
      "zh_CN": "<ruby>火山<rt>かざん</rt></ruby>が<ruby>噴火<rt>ふんか</rt></ruby>しました。",
      "ko": "<ruby>火山<rt>かざん</rt></ruby>が<ruby>噴火<rt>ふんか</rt></ruby>しました。",
      "zh_HK": "<ruby>火山<rt>かざん</rt></ruby>が<ruby>噴火<rt>ふんか</rt></ruby>しました。",
      "fr": "<ruby>火山<rt>かざん</rt></ruby>が<ruby>噴火<rt>ふんか</rt></ruby>しました。"
    },
    "related": "ふんか（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_063",
    "word": "大人っぽい",
    "reading": "おとなっぽい",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "mature-looking; grown-up",
      "ja": "大人っぽい",
      "zh_TW": "mature-looking; grown-up",
      "zh_CN": "mature-looking; grown-up",
      "ko": "mature-looking; grown-up",
      "zh_HK": "mature-looking; grown-up",
      "fr": "mature-looking; grown-up"
    },
    "example": {
      "ja": "<ruby>彼女<rt>かのじょ</rt></ruby>は<ruby>年<rt>とし</rt></ruby>のわりに<ruby>大人<rt>おとな</rt></ruby>っぽいです。",
      "en": "She looks mature for her age.",
      "zh_TW": "<ruby>彼女<rt>かのじょ</rt></ruby>は<ruby>年<rt>とし</rt></ruby>のわりに<ruby>大人<rt>おとな</rt></ruby>っぽいです。",
      "zh_CN": "<ruby>彼女<rt>かのじょ</rt></ruby>は<ruby>年<rt>とし</rt></ruby>のわりに<ruby>大人<rt>おとな</rt></ruby>っぽいです。",
      "ko": "<ruby>彼女<rt>かのじょ</rt></ruby>は<ruby>年<rt>とし</rt></ruby>のわりに<ruby>大人<rt>おとな</rt></ruby>っぽいです。",
      "zh_HK": "<ruby>彼女<rt>かのじょ</rt></ruby>は<ruby>年<rt>とし</rt></ruby>のわりに<ruby>大人<rt>おとな</rt></ruby>っぽいです。",
      "fr": "<ruby>彼女<rt>かのじょ</rt></ruby>は<ruby>年<rt>とし</rt></ruby>のわりに<ruby>大人<rt>おとな</rt></ruby>っぽいです。"
    },
    "related": "おとなっぽい（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_064",
    "word": "子供っぽい",
    "reading": "こどもっぽい",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "childish",
      "ja": "子供っぽい",
      "zh_TW": "childish",
      "zh_CN": "childish",
      "ko": "childish",
      "zh_HK": "childish",
      "fr": "childish"
    },
    "example": {
      "ja": "そんなことで<ruby>怒<rt>おこ</rt></ruby>るなんて、<ruby>子供<rt>こども</rt></ruby>っぽいですね。",
      "en": "Getting angry over something like that is childish.",
      "zh_TW": "そんなことで<ruby>怒<rt>おこ</rt></ruby>るなんて、<ruby>子供<rt>こども</rt></ruby>っぽいですね。",
      "zh_CN": "そんなことで<ruby>怒<rt>おこ</rt></ruby>るなんて、<ruby>子供<rt>こども</rt></ruby>っぽいですね。",
      "ko": "そんなことで<ruby>怒<rt>おこ</rt></ruby>るなんて、<ruby>子供<rt>こども</rt></ruby>っぽいですね。",
      "zh_HK": "そんなことで<ruby>怒<rt>おこ</rt></ruby>るなんて、<ruby>子供<rt>こども</rt></ruby>っぽいですね。",
      "fr": "そんなことで<ruby>怒<rt>おこ</rt></ruby>るなんて、<ruby>子供<rt>こども</rt></ruby>っぽいですね。"
    },
    "related": "こどもっぽい（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_065",
    "word": "バツイチ",
    "reading": "バツイチ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "divorced once (colloquial)",
      "ja": "バツイチ",
      "zh_TW": "divorced once (colloquial)",
      "zh_CN": "divorced once (colloquial)",
      "ko": "divorced once (colloquial)",
      "zh_HK": "divorced once (colloquial)",
      "fr": "divorced once (colloquial)"
    },
    "example": {
      "ja": "<ruby>彼<rt>かれ</rt></ruby>はバツイチです。",
      "en": "He's been divorced once.",
      "zh_TW": "<ruby>彼<rt>かれ</rt></ruby>はバツイチです。",
      "zh_CN": "<ruby>彼<rt>かれ</rt></ruby>はバツイチです。",
      "ko": "<ruby>彼<rt>かれ</rt></ruby>はバツイチです。",
      "zh_HK": "<ruby>彼<rt>かれ</rt></ruby>はバツイチです。",
      "fr": "<ruby>彼<rt>かれ</rt></ruby>はバツイチです。"
    },
    "related": "バツイチ（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_066",
    "word": "健康的",
    "reading": "けんこうてき",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "healthy",
      "ja": "健康的",
      "zh_TW": "healthy",
      "zh_CN": "healthy",
      "ko": "healthy",
      "zh_HK": "healthy",
      "fr": "healthy"
    },
    "example": {
      "ja": "<ruby>健康的<rt>けんこうてき</rt></ruby>な<ruby>食事<rt>しょくじ</rt></ruby>を<ruby>心<rt>こころ</rt></ruby>がけています。",
      "en": "I try to eat healthy meals.",
      "zh_TW": "<ruby>健康的<rt>けんこうてき</rt></ruby>な<ruby>食事<rt>しょくじ</rt></ruby>を<ruby>心<rt>こころ</rt></ruby>がけています。",
      "zh_CN": "<ruby>健康的<rt>けんこうてき</rt></ruby>な<ruby>食事<rt>しょくじ</rt></ruby>を<ruby>心<rt>こころ</rt></ruby>がけています。",
      "ko": "<ruby>健康的<rt>けんこうてき</rt></ruby>な<ruby>食事<rt>しょくじ</rt></ruby>を<ruby>心<rt>こころ</rt></ruby>がけています。",
      "zh_HK": "<ruby>健康的<rt>けんこうてき</rt></ruby>な<ruby>食事<rt>しょくじ</rt></ruby>を<ruby>心<rt>こころ</rt></ruby>がけています。",
      "fr": "<ruby>健康的<rt>けんこうてき</rt></ruby>な<ruby>食事<rt>しょくじ</rt></ruby>を<ruby>心<rt>こころ</rt></ruby>がけています。"
    },
    "related": "けんこうてき（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_067",
    "word": "皿洗い",
    "reading": "さらあらい",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "dishwashing",
      "ja": "皿洗い",
      "zh_TW": "dishwashing",
      "zh_CN": "dishwashing",
      "ko": "dishwashing",
      "zh_HK": "dishwashing",
      "fr": "dishwashing"
    },
    "example": {
      "ja": "<ruby>夕食<rt>ゆうしょく</rt></ruby>の<ruby>後<rt>あと</rt></ruby>、<ruby>皿洗<rt>さらあら</rt></ruby>いをします。",
      "en": "I wash the dishes after dinner.",
      "zh_TW": "<ruby>夕食<rt>ゆうしょく</rt></ruby>の<ruby>後<rt>あと</rt></ruby>、<ruby>皿洗<rt>さらあら</rt></ruby>いをします。",
      "zh_CN": "<ruby>夕食<rt>ゆうしょく</rt></ruby>の<ruby>後<rt>あと</rt></ruby>、<ruby>皿洗<rt>さらあら</rt></ruby>いをします。",
      "ko": "<ruby>夕食<rt>ゆうしょく</rt></ruby>の<ruby>後<rt>あと</rt></ruby>、<ruby>皿洗<rt>さらあら</rt></ruby>いをします。",
      "zh_HK": "<ruby>夕食<rt>ゆうしょく</rt></ruby>の<ruby>後<rt>あと</rt></ruby>、<ruby>皿洗<rt>さらあら</rt></ruby>いをします。",
      "fr": "<ruby>夕食<rt>ゆうしょく</rt></ruby>の<ruby>後<rt>あと</rt></ruby>、<ruby>皿洗<rt>さらあら</rt></ruby>いをします。"
    },
    "related": "さらあらい（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_068",
    "word": "お皿",
    "reading": "おさら",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "plate; dish",
      "ja": "お皿",
      "zh_TW": "plate; dish",
      "zh_CN": "plate; dish",
      "ko": "plate; dish",
      "zh_HK": "plate; dish",
      "fr": "plate; dish"
    },
    "example": {
      "ja": "お<ruby>皿<rt>さら</rt></ruby>を<ruby>割<rt>わ</rt></ruby>ってしまいました。",
      "en": "I broke a plate.",
      "zh_TW": "お<ruby>皿<rt>さら</rt></ruby>を<ruby>割<rt>わ</rt></ruby>ってしまいました。",
      "zh_CN": "お<ruby>皿<rt>さら</rt></ruby>を<ruby>割<rt>わ</rt></ruby>ってしまいました。",
      "ko": "お<ruby>皿<rt>さら</rt></ruby>を<ruby>割<rt>わ</rt></ruby>ってしまいました。",
      "zh_HK": "お<ruby>皿<rt>さら</rt></ruby>を<ruby>割<rt>わ</rt></ruby>ってしまいました。",
      "fr": "お<ruby>皿<rt>さら</rt></ruby>を<ruby>割<rt>わ</rt></ruby>ってしまいました。"
    },
    "related": "おさら（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_069",
    "word": "偏食",
    "reading": "へんしょく",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "picky eating; unbalanced diet",
      "ja": "偏食",
      "zh_TW": "picky eating; unbalanced diet",
      "zh_CN": "picky eating; unbalanced diet",
      "ko": "picky eating; unbalanced diet",
      "zh_HK": "picky eating; unbalanced diet",
      "fr": "picky eating; unbalanced diet"
    },
    "example": {
      "ja": "<ruby>子<rt>こ</rt></ruby>どもの<ruby>偏食<rt>へんしょく</rt></ruby>に<ruby>困<rt>こま</rt></ruby>っています。",
      "en": "I'm struggling with my child's picky eating.",
      "zh_TW": "<ruby>子<rt>こ</rt></ruby>どもの<ruby>偏食<rt>へんしょく</rt></ruby>に<ruby>困<rt>こま</rt></ruby>っています。",
      "zh_CN": "<ruby>子<rt>こ</rt></ruby>どもの<ruby>偏食<rt>へんしょく</rt></ruby>に<ruby>困<rt>こま</rt></ruby>っています。",
      "ko": "<ruby>子<rt>こ</rt></ruby>どもの<ruby>偏食<rt>へんしょく</rt></ruby>に<ruby>困<rt>こま</rt></ruby>っています。",
      "zh_HK": "<ruby>子<rt>こ</rt></ruby>どもの<ruby>偏食<rt>へんしょく</rt></ruby>に<ruby>困<rt>こま</rt></ruby>っています。",
      "fr": "<ruby>子<rt>こ</rt></ruby>どもの<ruby>偏食<rt>へんしょく</rt></ruby>に<ruby>困<rt>こま</rt></ruby>っています。"
    },
    "related": "へんしょく（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_070",
    "word": "井戸水",
    "reading": "いどみず",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "well water",
      "ja": "井戸水",
      "zh_TW": "well water",
      "zh_CN": "well water",
      "ko": "well water",
      "zh_HK": "well water",
      "fr": "well water"
    },
    "example": {
      "ja": "この<ruby>村<rt>むら</rt></ruby>では<ruby>井戸水<rt>いどみず</rt></ruby>を<ruby>使<rt>つか</rt></ruby>っています。",
      "en": "This village uses well water.",
      "zh_TW": "この<ruby>村<rt>むら</rt></ruby>では<ruby>井戸水<rt>いどみず</rt></ruby>を<ruby>使<rt>つか</rt></ruby>っています。",
      "zh_CN": "この<ruby>村<rt>むら</rt></ruby>では<ruby>井戸水<rt>いどみず</rt></ruby>を<ruby>使<rt>つか</rt></ruby>っています。",
      "ko": "この<ruby>村<rt>むら</rt></ruby>では<ruby>井戸水<rt>いどみず</rt></ruby>を<ruby>使<rt>つか</rt></ruby>っています。",
      "zh_HK": "この<ruby>村<rt>むら</rt></ruby>では<ruby>井戸水<rt>いどみず</rt></ruby>を<ruby>使<rt>つか</rt></ruby>っています。",
      "fr": "この<ruby>村<rt>むら</rt></ruby>では<ruby>井戸水<rt>いどみず</rt></ruby>を<ruby>使<rt>つか</rt></ruby>っています。"
    },
    "related": "いどみず（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_071",
    "word": "食習慣",
    "reading": "しょくしゅうかん",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "eating habits",
      "ja": "食習慣",
      "zh_TW": "eating habits",
      "zh_CN": "eating habits",
      "ko": "eating habits",
      "zh_HK": "eating habits",
      "fr": "eating habits"
    },
    "example": {
      "ja": "<ruby>国<rt>くに</rt></ruby>によって<ruby>食習慣<rt>しょくしゅうかん</rt></ruby>が<ruby>違<rt>ちが</rt></ruby>います。",
      "en": "Eating habits differ from country to country.",
      "zh_TW": "<ruby>国<rt>くに</rt></ruby>によって<ruby>食習慣<rt>しょくしゅうかん</rt></ruby>が<ruby>違<rt>ちが</rt></ruby>います。",
      "zh_CN": "<ruby>国<rt>くに</rt></ruby>によって<ruby>食習慣<rt>しょくしゅうかん</rt></ruby>が<ruby>違<rt>ちが</rt></ruby>います。",
      "ko": "<ruby>国<rt>くに</rt></ruby>によって<ruby>食習慣<rt>しょくしゅうかん</rt></ruby>が<ruby>違<rt>ちが</rt></ruby>います。",
      "zh_HK": "<ruby>国<rt>くに</rt></ruby>によって<ruby>食習慣<rt>しょくしゅうかん</rt></ruby>が<ruby>違<rt>ちが</rt></ruby>います。",
      "fr": "<ruby>国<rt>くに</rt></ruby>によって<ruby>食習慣<rt>しょくしゅうかん</rt></ruby>が<ruby>違<rt>ちが</rt></ruby>います。"
    },
    "related": "しょくしゅうかん（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_072",
    "word": "生活習慣",
    "reading": "せいかつしゅうかん",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "lifestyle habits",
      "ja": "生活習慣",
      "zh_TW": "lifestyle habits",
      "zh_CN": "lifestyle habits",
      "ko": "lifestyle habits",
      "zh_HK": "lifestyle habits",
      "fr": "lifestyle habits"
    },
    "example": {
      "ja": "<ruby>生活習慣<rt>せいかつしゅうかん</rt></ruby>を<ruby>見直<rt>みなお</rt></ruby>しましょう。",
      "en": "Let's review our lifestyle habits.",
      "zh_TW": "<ruby>生活習慣<rt>せいかつしゅうかん</rt></ruby>を<ruby>見直<rt>みなお</rt></ruby>しましょう。",
      "zh_CN": "<ruby>生活習慣<rt>せいかつしゅうかん</rt></ruby>を<ruby>見直<rt>みなお</rt></ruby>しましょう。",
      "ko": "<ruby>生活習慣<rt>せいかつしゅうかん</rt></ruby>を<ruby>見直<rt>みなお</rt></ruby>しましょう。",
      "zh_HK": "<ruby>生活習慣<rt>せいかつしゅうかん</rt></ruby>を<ruby>見直<rt>みなお</rt></ruby>しましょう。",
      "fr": "<ruby>生活習慣<rt>せいかつしゅうかん</rt></ruby>を<ruby>見直<rt>みなお</rt></ruby>しましょう。"
    },
    "related": "せいかつしゅうかん（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_073",
    "word": "育つ",
    "reading": "そだつ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to grow up; to be raised",
      "ja": "育つ",
      "zh_TW": "to grow up; to be raised",
      "zh_CN": "to grow up; to be raised",
      "ko": "to grow up; to be raised",
      "zh_HK": "to grow up; to be raised",
      "fr": "to grow up; to be raised"
    },
    "example": {
      "ja": "<ruby>私<rt>わたし</rt></ruby>は<ruby>大阪<rt>おおさか</rt></ruby>で<ruby>育<rt>そだ</rt></ruby>ちました。",
      "en": "I grew up in Osaka.",
      "zh_TW": "<ruby>私<rt>わたし</rt></ruby>は<ruby>大阪<rt>おおさか</rt></ruby>で<ruby>育<rt>そだ</rt></ruby>ちました。",
      "zh_CN": "<ruby>私<rt>わたし</rt></ruby>は<ruby>大阪<rt>おおさか</rt></ruby>で<ruby>育<rt>そだ</rt></ruby>ちました。",
      "ko": "<ruby>私<rt>わたし</rt></ruby>は<ruby>大阪<rt>おおさか</rt></ruby>で<ruby>育<rt>そだ</rt></ruby>ちました。",
      "zh_HK": "<ruby>私<rt>わたし</rt></ruby>は<ruby>大阪<rt>おおさか</rt></ruby>で<ruby>育<rt>そだ</rt></ruby>ちました。",
      "fr": "<ruby>私<rt>わたし</rt></ruby>は<ruby>大阪<rt>おおさか</rt></ruby>で<ruby>育<rt>そだ</rt></ruby>ちました。"
    },
    "related": "そだつ（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_074",
    "word": "子育て",
    "reading": "こそだて",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "child-rearing; parenting",
      "ja": "子育て",
      "zh_TW": "child-rearing; parenting",
      "zh_CN": "child-rearing; parenting",
      "ko": "child-rearing; parenting",
      "zh_HK": "child-rearing; parenting",
      "fr": "child-rearing; parenting"
    },
    "example": {
      "ja": "<ruby>子育<rt>こそだ</rt></ruby>ては<ruby>大変<rt>たいへん</rt></ruby>ですが、<ruby>楽<rt>たの</rt></ruby>しいです。",
      "en": "Raising children is hard but fun.",
      "zh_TW": "<ruby>子育<rt>こそだ</rt></ruby>ては<ruby>大変<rt>たいへん</rt></ruby>ですが、<ruby>楽<rt>たの</rt></ruby>しいです。",
      "zh_CN": "<ruby>子育<rt>こそだ</rt></ruby>ては<ruby>大変<rt>たいへん</rt></ruby>ですが、<ruby>楽<rt>たの</rt></ruby>しいです。",
      "ko": "<ruby>子育<rt>こそだ</rt></ruby>ては<ruby>大変<rt>たいへん</rt></ruby>ですが、<ruby>楽<rt>たの</rt></ruby>しいです。",
      "zh_HK": "<ruby>子育<rt>こそだ</rt></ruby>ては<ruby>大変<rt>たいへん</rt></ruby>ですが、<ruby>楽<rt>たの</rt></ruby>しいです。",
      "fr": "<ruby>子育<rt>こそだ</rt></ruby>ては<ruby>大変<rt>たいへん</rt></ruby>ですが、<ruby>楽<rt>たの</rt></ruby>しいです。"
    },
    "related": "こそだて（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_075",
    "word": "海岸",
    "reading": "かいがん",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "coast; seashore",
      "ja": "海岸",
      "zh_TW": "coast; seashore",
      "zh_CN": "coast; seashore",
      "ko": "coast; seashore",
      "zh_HK": "coast; seashore",
      "fr": "coast; seashore"
    },
    "example": {
      "ja": "<ruby>海岸<rt>かいがん</rt></ruby>を<ruby>散歩<rt>さんぽ</rt></ruby>しました。",
      "en": "I took a walk along the coast.",
      "zh_TW": "<ruby>海岸<rt>かいがん</rt></ruby>を<ruby>散歩<rt>さんぽ</rt></ruby>しました。",
      "zh_CN": "<ruby>海岸<rt>かいがん</rt></ruby>を<ruby>散歩<rt>さんぽ</rt></ruby>しました。",
      "ko": "<ruby>海岸<rt>かいがん</rt></ruby>を<ruby>散歩<rt>さんぽ</rt></ruby>しました。",
      "zh_HK": "<ruby>海岸<rt>かいがん</rt></ruby>を<ruby>散歩<rt>さんぽ</rt></ruby>しました。",
      "fr": "<ruby>海岸<rt>かいがん</rt></ruby>を<ruby>散歩<rt>さんぽ</rt></ruby>しました。"
    },
    "related": "かいがん（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_076",
    "word": "会談",
    "reading": "かいだん",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "talks; meeting (formal)",
      "ja": "会談",
      "zh_TW": "talks; meeting (formal)",
      "zh_CN": "talks; meeting (formal)",
      "ko": "talks; meeting (formal)",
      "zh_HK": "talks; meeting (formal)",
      "fr": "talks; meeting (formal)"
    },
    "example": {
      "ja": "<ruby>両国<rt>りょうこく</rt></ruby>の<ruby>首脳<rt>しゅのう</rt></ruby>が<ruby>会談<rt>かいだん</rt></ruby>しました。",
      "en": "The leaders of the two countries held talks.",
      "zh_TW": "<ruby>両国<rt>りょうこく</rt></ruby>の<ruby>首脳<rt>しゅのう</rt></ruby>が<ruby>会談<rt>かいだん</rt></ruby>しました。",
      "zh_CN": "<ruby>両国<rt>りょうこく</rt></ruby>の<ruby>首脳<rt>しゅのう</rt></ruby>が<ruby>会談<rt>かいだん</rt></ruby>しました。",
      "ko": "<ruby>両国<rt>りょうこく</rt></ruby>の<ruby>首脳<rt>しゅのう</rt></ruby>が<ruby>会談<rt>かいだん</rt></ruby>しました。",
      "zh_HK": "<ruby>両国<rt>りょうこく</rt></ruby>の<ruby>首脳<rt>しゅのう</rt></ruby>が<ruby>会談<rt>かいだん</rt></ruby>しました。",
      "fr": "<ruby>両国<rt>りょうこく</rt></ruby>の<ruby>首脳<rt>しゅのう</rt></ruby>が<ruby>会談<rt>かいだん</rt></ruby>しました。"
    },
    "related": "かいだん（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_077",
    "word": "研究室",
    "reading": "けんきゅうしつ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "laboratory; professor's office",
      "ja": "研究室",
      "zh_TW": "laboratory; professor's office",
      "zh_CN": "laboratory; professor's office",
      "ko": "laboratory; professor's office",
      "zh_HK": "laboratory; professor's office",
      "fr": "laboratory; professor's office"
    },
    "example": {
      "ja": "<ruby>先生<rt>せんせい</rt></ruby>の<ruby>研究室<rt>けんきゅうしつ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。",
      "en": "I'm going to the professor's lab.",
      "zh_TW": "<ruby>先生<rt>せんせい</rt></ruby>の<ruby>研究室<rt>けんきゅうしつ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。",
      "zh_CN": "<ruby>先生<rt>せんせい</rt></ruby>の<ruby>研究室<rt>けんきゅうしつ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。",
      "ko": "<ruby>先生<rt>せんせい</rt></ruby>の<ruby>研究室<rt>けんきゅうしつ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。",
      "zh_HK": "<ruby>先生<rt>せんせい</rt></ruby>の<ruby>研究室<rt>けんきゅうしつ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。",
      "fr": "<ruby>先生<rt>せんせい</rt></ruby>の<ruby>研究室<rt>けんきゅうしつ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。"
    },
    "related": "けんきゅうしつ（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_078",
    "word": "片付ける",
    "reading": "かたづける",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to tidy up; to put away",
      "ja": "片付ける",
      "zh_TW": "to tidy up; to put away",
      "zh_CN": "to tidy up; to put away",
      "ko": "to tidy up; to put away",
      "zh_HK": "to tidy up; to put away",
      "fr": "to tidy up; to put away"
    },
    "example": {
      "ja": "<ruby>部屋<rt>へや</rt></ruby>を<ruby>片付<rt>かたづ</rt></ruby>けてください。",
      "en": "Please tidy up your room.",
      "zh_TW": "<ruby>部屋<rt>へや</rt></ruby>を<ruby>片付<rt>かたづ</rt></ruby>けてください。",
      "zh_CN": "<ruby>部屋<rt>へや</rt></ruby>を<ruby>片付<rt>かたづ</rt></ruby>けてください。",
      "ko": "<ruby>部屋<rt>へや</rt></ruby>を<ruby>片付<rt>かたづ</rt></ruby>けてください。",
      "zh_HK": "<ruby>部屋<rt>へや</rt></ruby>を<ruby>片付<rt>かたづ</rt></ruby>けてください。",
      "fr": "<ruby>部屋<rt>へや</rt></ruby>を<ruby>片付<rt>かたづ</rt></ruby>けてください。"
    },
    "related": "かたづける（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_079",
    "word": "嘘をつく",
    "reading": "うそをつく",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to tell a lie",
      "ja": "嘘をつく",
      "zh_TW": "to tell a lie",
      "zh_CN": "to tell a lie",
      "ko": "to tell a lie",
      "zh_HK": "to tell a lie",
      "fr": "to tell a lie"
    },
    "example": {
      "ja": "<ruby>嘘<rt>うそ</rt></ruby>をついてはいけません。",
      "en": "You must not tell lies.",
      "zh_TW": "<ruby>嘘<rt>うそ</rt></ruby>をついてはいけません。",
      "zh_CN": "<ruby>嘘<rt>うそ</rt></ruby>をついてはいけません。",
      "ko": "<ruby>嘘<rt>うそ</rt></ruby>をついてはいけません。",
      "zh_HK": "<ruby>嘘<rt>うそ</rt></ruby>をついてはいけません。",
      "fr": "<ruby>嘘<rt>うそ</rt></ruby>をついてはいけません。"
    },
    "related": "うそをつく（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_080",
    "word": "嘘つき",
    "reading": "うそつき",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "liar",
      "ja": "嘘つき",
      "zh_TW": "liar",
      "zh_CN": "liar",
      "ko": "liar",
      "zh_HK": "liar",
      "fr": "liar"
    },
    "example": {
      "ja": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>嘘<rt>うそ</rt></ruby>つきです。",
      "en": "He is a liar.",
      "zh_TW": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>嘘<rt>うそ</rt></ruby>つきです。",
      "zh_CN": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>嘘<rt>うそ</rt></ruby>つきです。",
      "ko": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>嘘<rt>うそ</rt></ruby>つきです。",
      "zh_HK": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>嘘<rt>うそ</rt></ruby>つきです。",
      "fr": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>嘘<rt>うそ</rt></ruby>つきです。"
    },
    "related": "うそつき（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_081",
    "word": "ウイルス",
    "reading": "ウイルス",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "virus",
      "ja": "ウイルス",
      "zh_TW": "virus",
      "zh_CN": "virus",
      "ko": "virus",
      "zh_HK": "virus",
      "fr": "virus"
    },
    "example": {
      "ja": "パソコンがウイルスに<ruby>感染<rt>かんせん</rt></ruby>しました。",
      "en": "My computer got infected with a virus.",
      "zh_TW": "パソコンがウイルスに<ruby>感染<rt>かんせん</rt></ruby>しました。",
      "zh_CN": "パソコンがウイルスに<ruby>感染<rt>かんせん</rt></ruby>しました。",
      "ko": "パソコンがウイルスに<ruby>感染<rt>かんせん</rt></ruby>しました。",
      "zh_HK": "パソコンがウイルスに<ruby>感染<rt>かんせん</rt></ruby>しました。",
      "fr": "パソコンがウイルスに<ruby>感染<rt>かんせん</rt></ruby>しました。"
    },
    "related": "ウイルス（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_082",
    "word": "お湯",
    "reading": "おゆ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "hot water",
      "ja": "お湯",
      "zh_TW": "hot water",
      "zh_CN": "hot water",
      "ko": "hot water",
      "zh_HK": "hot water",
      "fr": "hot water"
    },
    "example": {
      "ja": "お<ruby>湯<rt>ゆ</rt></ruby>を<ruby>沸<rt>わ</rt></ruby>かします。",
      "en": "I'll boil some water.",
      "zh_TW": "お<ruby>湯<rt>ゆ</rt></ruby>を<ruby>沸<rt>わ</rt></ruby>かします。",
      "zh_CN": "お<ruby>湯<rt>ゆ</rt></ruby>を<ruby>沸<rt>わ</rt></ruby>かします。",
      "ko": "お<ruby>湯<rt>ゆ</rt></ruby>を<ruby>沸<rt>わ</rt></ruby>かします。",
      "zh_HK": "お<ruby>湯<rt>ゆ</rt></ruby>を<ruby>沸<rt>わ</rt></ruby>かします。",
      "fr": "お<ruby>湯<rt>ゆ</rt></ruby>を<ruby>沸<rt>わ</rt></ruby>かします。"
    },
    "related": "おゆ（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_083",
    "word": "目印",
    "reading": "めじるし",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "landmark; marker",
      "ja": "目印",
      "zh_TW": "landmark; marker",
      "zh_CN": "landmark; marker",
      "ko": "landmark; marker",
      "zh_HK": "landmark; marker",
      "fr": "landmark; marker"
    },
    "example": {
      "ja": "<ruby>駅<rt>えき</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>の<ruby>赤<rt>あか</rt></ruby>いビルが<ruby>目印<rt>めじるし</rt></ruby>です。",
      "en": "The red building in front of the station is the landmark.",
      "zh_TW": "<ruby>駅<rt>えき</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>の<ruby>赤<rt>あか</rt></ruby>いビルが<ruby>目印<rt>めじるし</rt></ruby>です。",
      "zh_CN": "<ruby>駅<rt>えき</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>の<ruby>赤<rt>あか</rt></ruby>いビルが<ruby>目印<rt>めじるし</rt></ruby>です。",
      "ko": "<ruby>駅<rt>えき</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>の<ruby>赤<rt>あか</rt></ruby>いビルが<ruby>目印<rt>めじるし</rt></ruby>です。",
      "zh_HK": "<ruby>駅<rt>えき</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>の<ruby>赤<rt>あか</rt></ruby>いビルが<ruby>目印<rt>めじるし</rt></ruby>です。",
      "fr": "<ruby>駅<rt>えき</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>の<ruby>赤<rt>あか</rt></ruby>いビルが<ruby>目印<rt>めじるし</rt></ruby>です。"
    },
    "related": "めじるし（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_084",
    "word": "お墓参り",
    "reading": "おはかまいり",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "visiting a family grave",
      "ja": "お墓参り",
      "zh_TW": "visiting a family grave",
      "zh_CN": "visiting a family grave",
      "ko": "visiting a family grave",
      "zh_HK": "visiting a family grave",
      "fr": "visiting a family grave"
    },
    "example": {
      "ja": "お<ruby>盆<rt>ぼん</rt></ruby>にお<ruby>墓参<rt>はかまい</rt></ruby>りに<ruby>行<rt>い</rt></ruby>きます。",
      "en": "I visit the family grave during Obon.",
      "zh_TW": "お<ruby>盆<rt>ぼん</rt></ruby>にお<ruby>墓参<rt>はかまい</rt></ruby>りに<ruby>行<rt>い</rt></ruby>きます。",
      "zh_CN": "お<ruby>盆<rt>ぼん</rt></ruby>にお<ruby>墓参<rt>はかまい</rt></ruby>りに<ruby>行<rt>い</rt></ruby>きます。",
      "ko": "お<ruby>盆<rt>ぼん</rt></ruby>にお<ruby>墓参<rt>はかまい</rt></ruby>りに<ruby>行<rt>い</rt></ruby>きます。",
      "zh_HK": "お<ruby>盆<rt>ぼん</rt></ruby>にお<ruby>墓参<rt>はかまい</rt></ruby>りに<ruby>行<rt>い</rt></ruby>きます。",
      "fr": "お<ruby>盆<rt>ぼん</rt></ruby>にお<ruby>墓参<rt>はかまい</rt></ruby>りに<ruby>行<rt>い</rt></ruby>きます。"
    },
    "related": "おはかまいり（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_085",
    "word": "祖先",
    "reading": "そせん",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "ancestor",
      "ja": "祖先",
      "zh_TW": "ancestor",
      "zh_CN": "ancestor",
      "ko": "ancestor",
      "zh_HK": "ancestor",
      "fr": "ancestor"
    },
    "example": {
      "ja": "<ruby>祖先<rt>そせん</rt></ruby>を<ruby>大切<rt>たいせつ</rt></ruby>にします。",
      "en": "We honor our ancestors.",
      "zh_TW": "<ruby>祖先<rt>そせん</rt></ruby>を<ruby>大切<rt>たいせつ</rt></ruby>にします。",
      "zh_CN": "<ruby>祖先<rt>そせん</rt></ruby>を<ruby>大切<rt>たいせつ</rt></ruby>にします。",
      "ko": "<ruby>祖先<rt>そせん</rt></ruby>を<ruby>大切<rt>たいせつ</rt></ruby>にします。",
      "zh_HK": "<ruby>祖先<rt>そせん</rt></ruby>を<ruby>大切<rt>たいせつ</rt></ruby>にします。",
      "fr": "<ruby>祖先<rt>そせん</rt></ruby>を<ruby>大切<rt>たいせつ</rt></ruby>にします。"
    },
    "related": "そせん（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_086",
    "word": "墓",
    "reading": "はか",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "grave; tomb",
      "ja": "墓",
      "zh_TW": "grave; tomb",
      "zh_CN": "grave; tomb",
      "ko": "grave; tomb",
      "zh_HK": "grave; tomb",
      "fr": "grave; tomb"
    },
    "example": {
      "ja": "<ruby>祖父<rt>そふ</rt></ruby>の<ruby>墓<rt>はか</rt></ruby>は<ruby>山<rt>やま</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>にあります。",
      "en": "My grandfather's grave is on the mountain.",
      "zh_TW": "<ruby>祖父<rt>そふ</rt></ruby>の<ruby>墓<rt>はか</rt></ruby>は<ruby>山<rt>やま</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>にあります。",
      "zh_CN": "<ruby>祖父<rt>そふ</rt></ruby>の<ruby>墓<rt>はか</rt></ruby>は<ruby>山<rt>やま</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>にあります。",
      "ko": "<ruby>祖父<rt>そふ</rt></ruby>の<ruby>墓<rt>はか</rt></ruby>は<ruby>山<rt>やま</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>にあります。",
      "zh_HK": "<ruby>祖父<rt>そふ</rt></ruby>の<ruby>墓<rt>はか</rt></ruby>は<ruby>山<rt>やま</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>にあります。",
      "fr": "<ruby>祖父<rt>そふ</rt></ruby>の<ruby>墓<rt>はか</rt></ruby>は<ruby>山<rt>やま</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>にあります。"
    },
    "related": "はか（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_087",
    "word": "港",
    "reading": "みなと",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "port; harbor",
      "ja": "港",
      "zh_TW": "port; harbor",
      "zh_CN": "port; harbor",
      "ko": "port; harbor",
      "zh_HK": "port; harbor",
      "fr": "port; harbor"
    },
    "example": {
      "ja": "<ruby>港<rt>みなと</rt></ruby>に<ruby>大<rt>おお</rt></ruby>きな<ruby>船<rt>ふね</rt></ruby>が<ruby>泊<rt>と</rt></ruby>まっています。",
      "en": "A big ship is docked at the port.",
      "zh_TW": "<ruby>港<rt>みなと</rt></ruby>に<ruby>大<rt>おお</rt></ruby>きな<ruby>船<rt>ふね</rt></ruby>が<ruby>泊<rt>と</rt></ruby>まっています。",
      "zh_CN": "<ruby>港<rt>みなと</rt></ruby>に<ruby>大<rt>おお</rt></ruby>きな<ruby>船<rt>ふね</rt></ruby>が<ruby>泊<rt>と</rt></ruby>まっています。",
      "ko": "<ruby>港<rt>みなと</rt></ruby>に<ruby>大<rt>おお</rt></ruby>きな<ruby>船<rt>ふね</rt></ruby>が<ruby>泊<rt>と</rt></ruby>まっています。",
      "zh_HK": "<ruby>港<rt>みなと</rt></ruby>に<ruby>大<rt>おお</rt></ruby>きな<ruby>船<rt>ふね</rt></ruby>が<ruby>泊<rt>と</rt></ruby>まっています。",
      "fr": "<ruby>港<rt>みなと</rt></ruby>に<ruby>大<rt>おお</rt></ruby>きな<ruby>船<rt>ふね</rt></ruby>が<ruby>泊<rt>と</rt></ruby>まっています。"
    },
    "related": "みなと（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_088",
    "word": "広告",
    "reading": "こうこく",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "advertisement",
      "ja": "広告",
      "zh_TW": "advertisement",
      "zh_CN": "advertisement",
      "ko": "advertisement",
      "zh_HK": "advertisement",
      "fr": "advertisement"
    },
    "example": {
      "ja": "<ruby>電車<rt>でんしゃ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に<ruby>広告<rt>こうこく</rt></ruby>がたくさんあります。",
      "en": "There are many ads on the train.",
      "zh_TW": "<ruby>電車<rt>でんしゃ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に<ruby>広告<rt>こうこく</rt></ruby>がたくさんあります。",
      "zh_CN": "<ruby>電車<rt>でんしゃ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に<ruby>広告<rt>こうこく</rt></ruby>がたくさんあります。",
      "ko": "<ruby>電車<rt>でんしゃ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に<ruby>広告<rt>こうこく</rt></ruby>がたくさんあります。",
      "zh_HK": "<ruby>電車<rt>でんしゃ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に<ruby>広告<rt>こうこく</rt></ruby>がたくさんあります。",
      "fr": "<ruby>電車<rt>でんしゃ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に<ruby>広告<rt>こうこく</rt></ruby>がたくさんあります。"
    },
    "related": "こうこく（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_089",
    "word": "人口",
    "reading": "じんこう",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "population",
      "ja": "人口",
      "zh_TW": "population",
      "zh_CN": "population",
      "ko": "population",
      "zh_HK": "population",
      "fr": "population"
    },
    "example": {
      "ja": "<ruby>日本<rt>にほん</rt></ruby>の<ruby>人口<rt>じんこう</rt></ruby>は<ruby>減<rt>へ</rt></ruby>っています。",
      "en": "Japan's population is decreasing.",
      "zh_TW": "<ruby>日本<rt>にほん</rt></ruby>の<ruby>人口<rt>じんこう</rt></ruby>は<ruby>減<rt>へ</rt></ruby>っています。",
      "zh_CN": "<ruby>日本<rt>にほん</rt></ruby>の<ruby>人口<rt>じんこう</rt></ruby>は<ruby>減<rt>へ</rt></ruby>っています。",
      "ko": "<ruby>日本<rt>にほん</rt></ruby>の<ruby>人口<rt>じんこう</rt></ruby>は<ruby>減<rt>へ</rt></ruby>っています。",
      "zh_HK": "<ruby>日本<rt>にほん</rt></ruby>の<ruby>人口<rt>じんこう</rt></ruby>は<ruby>減<rt>へ</rt></ruby>っています。",
      "fr": "<ruby>日本<rt>にほん</rt></ruby>の<ruby>人口<rt>じんこう</rt></ruby>は<ruby>減<rt>へ</rt></ruby>っています。"
    },
    "related": "じんこう（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_090",
    "word": "候補",
    "reading": "こうほ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "candidate; option",
      "ja": "候補",
      "zh_TW": "candidate; option",
      "zh_CN": "candidate; option",
      "ko": "candidate; option",
      "zh_HK": "candidate; option",
      "fr": "candidate; option"
    },
    "example": {
      "ja": "<ruby>旅行先<rt>りょこうさき</rt></ruby>の<ruby>候補<rt>こうほ</rt></ruby>がいくつかあります。",
      "en": "We have several possible travel destinations.",
      "zh_TW": "<ruby>旅行先<rt>りょこうさき</rt></ruby>の<ruby>候補<rt>こうほ</rt></ruby>がいくつかあります。",
      "zh_CN": "<ruby>旅行先<rt>りょこうさき</rt></ruby>の<ruby>候補<rt>こうほ</rt></ruby>がいくつかあります。",
      "ko": "<ruby>旅行先<rt>りょこうさき</rt></ruby>の<ruby>候補<rt>こうほ</rt></ruby>がいくつかあります。",
      "zh_HK": "<ruby>旅行先<rt>りょこうさき</rt></ruby>の<ruby>候補<rt>こうほ</rt></ruby>がいくつかあります。",
      "fr": "<ruby>旅行先<rt>りょこうさき</rt></ruby>の<ruby>候補<rt>こうほ</rt></ruby>がいくつかあります。"
    },
    "related": "こうほ（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_091",
    "word": "底",
    "reading": "そこ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "bottom",
      "ja": "底",
      "zh_TW": "bottom",
      "zh_CN": "bottom",
      "ko": "bottom",
      "zh_HK": "bottom",
      "fr": "bottom"
    },
    "example": {
      "ja": "<ruby>鍋<rt>なべ</rt></ruby>の<ruby>底<rt>そこ</rt></ruby>が<ruby>焦<rt>こ</rt></ruby>げました。",
      "en": "The bottom of the pot got burned.",
      "zh_TW": "<ruby>鍋<rt>なべ</rt></ruby>の<ruby>底<rt>そこ</rt></ruby>が<ruby>焦<rt>こ</rt></ruby>げました。",
      "zh_CN": "<ruby>鍋<rt>なべ</rt></ruby>の<ruby>底<rt>そこ</rt></ruby>が<ruby>焦<rt>こ</rt></ruby>げました。",
      "ko": "<ruby>鍋<rt>なべ</rt></ruby>の<ruby>底<rt>そこ</rt></ruby>が<ruby>焦<rt>こ</rt></ruby>げました。",
      "zh_HK": "<ruby>鍋<rt>なべ</rt></ruby>の<ruby>底<rt>そこ</rt></ruby>が<ruby>焦<rt>こ</rt></ruby>げました。",
      "fr": "<ruby>鍋<rt>なべ</rt></ruby>の<ruby>底<rt>そこ</rt></ruby>が<ruby>焦<rt>こ</rt></ruby>げました。"
    },
    "related": "そこ（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_092",
    "word": "お客様",
    "reading": "おきゃくさま",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "customer; guest (polite)",
      "ja": "お客様",
      "zh_TW": "customer; guest (polite)",
      "zh_CN": "customer; guest (polite)",
      "ko": "customer; guest (polite)",
      "zh_HK": "customer; guest (polite)",
      "fr": "customer; guest (polite)"
    },
    "example": {
      "ja": "お<ruby>客様<rt>きゃくさま</rt></ruby>、こちらへどうぞ。",
      "en": "This way, please.",
      "zh_TW": "お<ruby>客様<rt>きゃくさま</rt></ruby>、こちらへどうぞ。",
      "zh_CN": "お<ruby>客様<rt>きゃくさま</rt></ruby>、こちらへどうぞ。",
      "ko": "お<ruby>客様<rt>きゃくさま</rt></ruby>、こちらへどうぞ。",
      "zh_HK": "お<ruby>客様<rt>きゃくさま</rt></ruby>、こちらへどうぞ。",
      "fr": "お<ruby>客様<rt>きゃくさま</rt></ruby>、こちらへどうぞ。"
    },
    "related": "おきゃくさま（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_093",
    "word": "十分です",
    "reading": "じゅうぶんです",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "That's enough; sufficient",
      "ja": "十分です",
      "zh_TW": "That's enough; sufficient",
      "zh_CN": "That's enough; sufficient",
      "ko": "That's enough; sufficient",
      "zh_HK": "That's enough; sufficient",
      "fr": "That's enough; sufficient"
    },
    "example": {
      "ja": "もう<ruby>十分<rt>じゅうぶん</rt></ruby>です。ありがとうございます。",
      "en": "That's plenty, thank you.",
      "zh_TW": "もう<ruby>十分<rt>じゅうぶん</rt></ruby>です。ありがとうございます。",
      "zh_CN": "もう<ruby>十分<rt>じゅうぶん</rt></ruby>です。ありがとうございます。",
      "ko": "もう<ruby>十分<rt>じゅうぶん</rt></ruby>です。ありがとうございます。",
      "zh_HK": "もう<ruby>十分<rt>じゅうぶん</rt></ruby>です。ありがとうございます。",
      "fr": "もう<ruby>十分<rt>じゅうぶん</rt></ruby>です。ありがとうございます。"
    },
    "related": "じゅうぶんです（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_094",
    "word": "夜行バス",
    "reading": "やこうバス",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "overnight bus",
      "ja": "夜行バス",
      "zh_TW": "overnight bus",
      "zh_CN": "overnight bus",
      "ko": "overnight bus",
      "zh_HK": "overnight bus",
      "fr": "overnight bus"
    },
    "example": {
      "ja": "<ruby>夜行<rt>やこう</rt></ruby>バスで<ruby>東京<rt>とうきょう</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。",
      "en": "I'm going to Tokyo by overnight bus.",
      "zh_TW": "<ruby>夜行<rt>やこう</rt></ruby>バスで<ruby>東京<rt>とうきょう</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。",
      "zh_CN": "<ruby>夜行<rt>やこう</rt></ruby>バスで<ruby>東京<rt>とうきょう</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。",
      "ko": "<ruby>夜行<rt>やこう</rt></ruby>バスで<ruby>東京<rt>とうきょう</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。",
      "zh_HK": "<ruby>夜行<rt>やこう</rt></ruby>バスで<ruby>東京<rt>とうきょう</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。",
      "fr": "<ruby>夜行<rt>やこう</rt></ruby>バスで<ruby>東京<rt>とうきょう</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。"
    },
    "related": "やこうバス（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_095",
    "word": "馬車",
    "reading": "ばしゃ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "horse-drawn carriage",
      "ja": "馬車",
      "zh_TW": "horse-drawn carriage",
      "zh_CN": "horse-drawn carriage",
      "ko": "horse-drawn carriage",
      "zh_HK": "horse-drawn carriage",
      "fr": "horse-drawn carriage"
    },
    "example": {
      "ja": "<ruby>昔<rt>むかし</rt></ruby>は<ruby>馬車<rt>ばしゃ</rt></ruby>で<ruby>移動<rt>いどう</rt></ruby>していました。",
      "en": "People used to travel by horse-drawn carriage.",
      "zh_TW": "<ruby>昔<rt>むかし</rt></ruby>は<ruby>馬車<rt>ばしゃ</rt></ruby>で<ruby>移動<rt>いどう</rt></ruby>していました。",
      "zh_CN": "<ruby>昔<rt>むかし</rt></ruby>は<ruby>馬車<rt>ばしゃ</rt></ruby>で<ruby>移動<rt>いどう</rt></ruby>していました。",
      "ko": "<ruby>昔<rt>むかし</rt></ruby>は<ruby>馬車<rt>ばしゃ</rt></ruby>で<ruby>移動<rt>いどう</rt></ruby>していました。",
      "zh_HK": "<ruby>昔<rt>むかし</rt></ruby>は<ruby>馬車<rt>ばしゃ</rt></ruby>で<ruby>移動<rt>いどう</rt></ruby>していました。",
      "fr": "<ruby>昔<rt>むかし</rt></ruby>は<ruby>馬車<rt>ばしゃ</rt></ruby>で<ruby>移動<rt>いどう</rt></ruby>していました。"
    },
    "related": "ばしゃ（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_096",
    "word": "考え事をする",
    "reading": "かんがえごとをする",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to be lost in thought",
      "ja": "考え事をする",
      "zh_TW": "to be lost in thought",
      "zh_CN": "to be lost in thought",
      "ko": "to be lost in thought",
      "zh_HK": "to be lost in thought",
      "fr": "to be lost in thought"
    },
    "example": {
      "ja": "<ruby>考<rt>かんが</rt></ruby>え<ruby>事<rt>ごと</rt></ruby>をしていて、<ruby>駅<rt>えき</rt></ruby>を<ruby>乗<rt>の</rt></ruby>り<ruby>過<rt>す</rt></ruby>ごしました。",
      "en": "I was lost in thought and missed my stop.",
      "zh_TW": "<ruby>考<rt>かんが</rt></ruby>え<ruby>事<rt>ごと</rt></ruby>をしていて、<ruby>駅<rt>えき</rt></ruby>を<ruby>乗<rt>の</rt></ruby>り<ruby>過<rt>す</rt></ruby>ごしました。",
      "zh_CN": "<ruby>考<rt>かんが</rt></ruby>え<ruby>事<rt>ごと</rt></ruby>をしていて、<ruby>駅<rt>えき</rt></ruby>を<ruby>乗<rt>の</rt></ruby>り<ruby>過<rt>す</rt></ruby>ごしました。",
      "ko": "<ruby>考<rt>かんが</rt></ruby>え<ruby>事<rt>ごと</rt></ruby>をしていて、<ruby>駅<rt>えき</rt></ruby>を<ruby>乗<rt>の</rt></ruby>り<ruby>過<rt>す</rt></ruby>ごしました。",
      "zh_HK": "<ruby>考<rt>かんが</rt></ruby>え<ruby>事<rt>ごと</rt></ruby>をしていて、<ruby>駅<rt>えき</rt></ruby>を<ruby>乗<rt>の</rt></ruby>り<ruby>過<rt>す</rt></ruby>ごしました。",
      "fr": "<ruby>考<rt>かんが</rt></ruby>え<ruby>事<rt>ごと</rt></ruby>をしていて、<ruby>駅<rt>えき</rt></ruby>を<ruby>乗<rt>の</rt></ruby>り<ruby>過<rt>す</rt></ruby>ごしました。"
    },
    "related": "かんがえごとをする（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_097",
    "word": "厳しい",
    "reading": "きびしい",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "strict; severe; harsh",
      "ja": "厳しい",
      "zh_TW": "strict; severe; harsh",
      "zh_CN": "strict; severe; harsh",
      "ko": "strict; severe; harsh",
      "zh_HK": "strict; severe; harsh",
      "fr": "strict; severe; harsh"
    },
    "example": {
      "ja": "<ruby>父<rt>ちち</rt></ruby>はとても<ruby>厳<rt>きび</rt></ruby>しいです。",
      "en": "My father is very strict.",
      "zh_TW": "<ruby>父<rt>ちち</rt></ruby>はとても<ruby>厳<rt>きび</rt></ruby>しいです。",
      "zh_CN": "<ruby>父<rt>ちち</rt></ruby>はとても<ruby>厳<rt>きび</rt></ruby>しいです。",
      "ko": "<ruby>父<rt>ちち</rt></ruby>はとても<ruby>厳<rt>きび</rt></ruby>しいです。",
      "zh_HK": "<ruby>父<rt>ちち</rt></ruby>はとても<ruby>厳<rt>きび</rt></ruby>しいです。",
      "fr": "<ruby>父<rt>ちち</rt></ruby>はとても<ruby>厳<rt>きび</rt></ruby>しいです。"
    },
    "related": "きびしい（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_098",
    "word": "最低賃金",
    "reading": "さいていちんぎん",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "minimum wage",
      "ja": "最低賃金",
      "zh_TW": "minimum wage",
      "zh_CN": "minimum wage",
      "ko": "minimum wage",
      "zh_HK": "minimum wage",
      "fr": "minimum wage"
    },
    "example": {
      "ja": "<ruby>最低賃金<rt>さいていちんぎん</rt></ruby>が<ruby>上<rt>あ</rt></ruby>がりました。",
      "en": "The minimum wage went up.",
      "zh_TW": "<ruby>最低賃金<rt>さいていちんぎん</rt></ruby>が<ruby>上<rt>あ</rt></ruby>がりました。",
      "zh_CN": "<ruby>最低賃金<rt>さいていちんぎん</rt></ruby>が<ruby>上<rt>あ</rt></ruby>がりました。",
      "ko": "<ruby>最低賃金<rt>さいていちんぎん</rt></ruby>が<ruby>上<rt>あ</rt></ruby>がりました。",
      "zh_HK": "<ruby>最低賃金<rt>さいていちんぎん</rt></ruby>が<ruby>上<rt>あ</rt></ruby>がりました。",
      "fr": "<ruby>最低賃金<rt>さいていちんぎん</rt></ruby>が<ruby>上<rt>あ</rt></ruby>がりました。"
    },
    "related": "さいていちんぎん（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_099",
    "word": "引っ越す",
    "reading": "ひっこす",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to move (house)",
      "ja": "引っ越す",
      "zh_TW": "to move (house)",
      "zh_CN": "to move (house)",
      "ko": "to move (house)",
      "zh_HK": "to move (house)",
      "fr": "to move (house)"
    },
    "example": {
      "ja": "<ruby>来月<rt>らいげつ</rt></ruby>、<ruby>大阪<rt>おおさか</rt></ruby>に<ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>します。",
      "en": "I'm moving to Osaka next month.",
      "zh_TW": "<ruby>来月<rt>らいげつ</rt></ruby>、<ruby>大阪<rt>おおさか</rt></ruby>に<ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>します。",
      "zh_CN": "<ruby>来月<rt>らいげつ</rt></ruby>、<ruby>大阪<rt>おおさか</rt></ruby>に<ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>します。",
      "ko": "<ruby>来月<rt>らいげつ</rt></ruby>、<ruby>大阪<rt>おおさか</rt></ruby>に<ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>します。",
      "zh_HK": "<ruby>来月<rt>らいげつ</rt></ruby>、<ruby>大阪<rt>おおさか</rt></ruby>に<ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>します。",
      "fr": "<ruby>来月<rt>らいげつ</rt></ruby>、<ruby>大阪<rt>おおさか</rt></ruby>に<ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>します。"
    },
    "related": "ひっこす（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_100",
    "word": "新鮮な",
    "reading": "しんせんな",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "fresh",
      "ja": "新鮮な",
      "zh_TW": "fresh",
      "zh_CN": "fresh",
      "ko": "fresh",
      "zh_HK": "fresh",
      "fr": "fresh"
    },
    "example": {
      "ja": "この<ruby>魚<rt>さかな</rt></ruby>はとても<ruby>新鮮<rt>しんせん</rt></ruby>です。",
      "en": "This fish is very fresh.",
      "zh_TW": "この<ruby>魚<rt>さかな</rt></ruby>はとても<ruby>新鮮<rt>しんせん</rt></ruby>です。",
      "zh_CN": "この<ruby>魚<rt>さかな</rt></ruby>はとても<ruby>新鮮<rt>しんせん</rt></ruby>です。",
      "ko": "この<ruby>魚<rt>さかな</rt></ruby>はとても<ruby>新鮮<rt>しんせん</rt></ruby>です。",
      "zh_HK": "この<ruby>魚<rt>さかな</rt></ruby>はとても<ruby>新鮮<rt>しんせん</rt></ruby>です。",
      "fr": "この<ruby>魚<rt>さかな</rt></ruby>はとても<ruby>新鮮<rt>しんせん</rt></ruby>です。"
    },
    "related": "しんせんな（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_101",
    "word": "特に",
    "reading": "とくに",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "especially; particularly",
      "ja": "特に",
      "zh_TW": "especially; particularly",
      "zh_CN": "especially; particularly",
      "ko": "especially; particularly",
      "zh_HK": "especially; particularly",
      "fr": "especially; particularly"
    },
    "example": {
      "ja": "<ruby>果物<rt>くだもの</rt></ruby>が<ruby>好<rt>す</rt></ruby>きです。<ruby>特<rt>とく</rt></ruby>にりんごが<ruby>好<rt>す</rt></ruby>きです。",
      "en": "I like fruit, especially apples.",
      "zh_TW": "<ruby>果物<rt>くだもの</rt></ruby>が<ruby>好<rt>す</rt></ruby>きです。<ruby>特<rt>とく</rt></ruby>にりんごが<ruby>好<rt>す</rt></ruby>きです。",
      "zh_CN": "<ruby>果物<rt>くだもの</rt></ruby>が<ruby>好<rt>す</rt></ruby>きです。<ruby>特<rt>とく</rt></ruby>にりんごが<ruby>好<rt>す</rt></ruby>きです。",
      "ko": "<ruby>果物<rt>くだもの</rt></ruby>が<ruby>好<rt>す</rt></ruby>きです。<ruby>特<rt>とく</rt></ruby>にりんごが<ruby>好<rt>す</rt></ruby>きです。",
      "zh_HK": "<ruby>果物<rt>くだもの</rt></ruby>が<ruby>好<rt>す</rt></ruby>きです。<ruby>特<rt>とく</rt></ruby>にりんごが<ruby>好<rt>す</rt></ruby>きです。",
      "fr": "<ruby>果物<rt>くだもの</rt></ruby>が<ruby>好<rt>す</rt></ruby>きです。<ruby>特<rt>とく</rt></ruby>にりんごが<ruby>好<rt>す</rt></ruby>きです。"
    },
    "related": "とくに（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_102",
    "word": "見逃す",
    "reading": "みのがす",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "to miss (seeing); to overlook",
      "ja": "見逃す",
      "zh_TW": "to miss (seeing); to overlook",
      "zh_CN": "to miss (seeing); to overlook",
      "ko": "to miss (seeing); to overlook",
      "zh_HK": "to miss (seeing); to overlook",
      "fr": "to miss (seeing); to overlook"
    },
    "example": {
      "ja": "<ruby>好<rt>す</rt></ruby>きなドラマを<ruby>見逃<rt>みのが</rt></ruby>しました。",
      "en": "I missed my favorite drama.",
      "zh_TW": "<ruby>好<rt>す</rt></ruby>きなドラマを<ruby>見逃<rt>みのが</rt></ruby>しました。",
      "zh_CN": "<ruby>好<rt>す</rt></ruby>きなドラマを<ruby>見逃<rt>みのが</rt></ruby>しました。",
      "ko": "<ruby>好<rt>す</rt></ruby>きなドラマを<ruby>見逃<rt>みのが</rt></ruby>しました。",
      "zh_HK": "<ruby>好<rt>す</rt></ruby>きなドラマを<ruby>見逃<rt>みのが</rt></ruby>しました。",
      "fr": "<ruby>好<rt>す</rt></ruby>きなドラマを<ruby>見逃<rt>みのが</rt></ruby>しました。"
    },
    "related": "みのがす（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  },
  {
    "id": "card_daniel_103",
    "word": "賄賂",
    "reading": "わいろ",
    "category": "授業で習った言葉",
    "meaning": {
      "en": "bribe",
      "ja": "賄賂",
      "zh_TW": "bribe",
      "zh_CN": "bribe",
      "ko": "bribe",
      "zh_HK": "bribe",
      "fr": "bribe"
    },
    "example": {
      "ja": "<ruby>政治家<rt>せいじか</rt></ruby>が<ruby>賄賂<rt>わいろ</rt></ruby>を<ruby>受<rt>う</rt></ruby>け<ruby>取<rt>と</rt></ruby>りました。",
      "en": "A politician accepted a bribe.",
      "zh_TW": "<ruby>政治家<rt>せいじか</rt></ruby>が<ruby>賄賂<rt>わいろ</rt></ruby>を<ruby>受<rt>う</rt></ruby>け<ruby>取<rt>と</rt></ruby>りました。",
      "zh_CN": "<ruby>政治家<rt>せいじか</rt></ruby>が<ruby>賄賂<rt>わいろ</rt></ruby>を<ruby>受<rt>う</rt></ruby>け<ruby>取<rt>と</rt></ruby>りました。",
      "ko": "<ruby>政治家<rt>せいじか</rt></ruby>が<ruby>賄賂<rt>わいろ</rt></ruby>を<ruby>受<rt>う</rt></ruby>け<ruby>取<rt>と</rt></ruby>りました。",
      "zh_HK": "<ruby>政治家<rt>せいじか</rt></ruby>が<ruby>賄賂<rt>わいろ</rt></ruby>を<ruby>受<rt>う</rt></ruby>け<ruby>取<rt>と</rt></ruby>りました。",
      "fr": "<ruby>政治家<rt>せいじか</rt></ruby>が<ruby>賄賂<rt>わいろ</rt></ruby>を<ruby>受<rt>う</rt></ruby>け<ruby>取<rt>と</rt></ruby>りました。"
    },
    "related": "わいろ（授業の重要表現）",
    "studentId": "0014",
    "isCustom": true
  }
];

  const ELIIE_NEW_CARD_IDS = ["card_1791710688293_deirhe__祖父", "card_1791710688303_fh3t7j__小弟", "card_1791710688311_9zfvb5__上課", "card_1791710688319_zs3yra__查某囝", "card_1791710688325_7evzn9__表兄弟", "card_1791710688336_q6wafx__毋是", "card_1791710688346_73s76l__毋是按呢", "card_1791710688353_f3bg8v__國小學生", "card_1791710688364_qe1b03__國中學生", "card_1791710688376_iy5cb6__高中學生", "card_1791710688382_9oq0pi__大學生", "card_1791710688402_ry1bj3__請問你是佗一位？", "card_1791710688408_d265ew__教室", "card_1791710688415_he8qrr__辭典", "card_1791710688423_uigyv2__拊仔", "card_1791710688436_hob5io__家己煮", "card_1791710688454_nx4xci__趁錢", "card_1791710688468_79djqd__銀行", "card_1791710688474_g6755p__事務所", "card_1791710688480_rwo43z__桌仔", "card_1791710688494_kh4lzt__會議室", "card_1791710688516_ik2gk3__有飼", "card_1791710688526_e0wuwh__感情好", "card_1791710688541_0y0x7v__無好", "card_1791710688558_cwqljh__大人", "card_1791710688572_8rnism__揀食", "card_1791710688584_skej7u__茄仔", "card_1791710688591_goll5a__青椒", "card_1791710688597_v9gkjw__紅菜頭", "card_1791710688604_h9kaib__口感", "card_1791710688612_euyhaw__日式蒸卵", "card_eliie_kyuushoku", "card_eliie_kangoshi", "card_eliie_nuigurumi", "card_eliie_ryourinin", "card_eliie_anaba", "card_eliie_okashizukuri"];

  const ELIIE_CURATED_CARDS = [
  {
    "id": "card_1791710688293_deirhe__祖父",
    "word": "祖父",
    "reading": "そふ",
    "meaning": {
      "ja": "祖父（おじいちゃん）",
      "zh_TW": "祖父、爺爺",
      "zh_CN": "祖父、爷爷",
      "en": "grandfather",
      "ko": "할아버지",
      "zh_HK": "阿爺、爺爺",
      "fr": "grand-père"
    },
    "example": {
      "ja": "A: <ruby>祖父<rt>そふ</rt></ruby>は<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>散歩<rt>さんぽ</rt></ruby>をして、とても<ruby>元気<rt>げんき</rt></ruby>です。<br/>B: いつまでも<ruby>健康<rt>けんこう</rt></ruby>でいてほしいですね。",
      "zh_TW": "A: 爺爺每天早晨都去散步，身體非常硬朗。<br/>B: 真希望他能一直健健康康的呢。",
      "zh_CN": "A: 爷爷每天早晨都去散步，身体非常硬朗。<br/>B: 真希望他能一直健健康康的呢。",
      "en": "A: My grandfather takes a walk every morning and is very healthy.<br/>B: I hope he stays healthy for a long time.",
      "ko": "A: 할아버지는 매일 아침 산책을 하셔서 아주 건강하십니다.<br/>B: 언제까지나 건강하게 계시면 좋겠네요.",
      "zh_HK": "A: 爺爺每日朝早都去散步，身體非常精神。<br/>B: 真係想佢一直健健康康呀。",
      "fr": "A: Mon grand-père se promène tous les matins et est très énergique.<br/>B: J'espère qu'il restera toujours en bonne santé."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688303_fh3t7j__小弟",
    "word": "弟",
    "reading": "おとうと",
    "meaning": {
      "ja": "弟",
      "zh_TW": "弟弟",
      "zh_CN": "弟弟",
      "en": "younger brother",
      "ko": "남동생",
      "zh_HK": "細佬",
      "fr": "petit frère"
    },
    "example": {
      "ja": "A: <ruby>弟<rt>おとうと</rt></ruby>さんは<ruby>何歳<rt>なんさい</rt></ruby>ですか。<br/>B: <ruby>今年<rt>ことし</rt></ruby><ruby>高校生<rt>こうこうせい</rt></ruby>になりました。",
      "zh_TW": "A: 弟弟幾歲了呢？<br/>B: 今年升上高中了。",
      "zh_CN": "A: 弟弟几岁了呢？<br/>B: 今年升上高中了。",
      "en": "A: How old is your younger brother?<br/>B: He became a high school student this year.",
      "ko": "A: 남동생은 몇 살이에요?<br/>B: 올해 고등학생이 되었어요.",
      "zh_HK": "A: 細佬幾多歲呀？<br/>B: 今年升咗高中喇。",
      "fr": "A: Quel âge a ton petit frère ?<br/>B: Il est entré au lycée cette année."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688311_9zfvb5__上課",
    "word": "授業",
    "reading": "じゅぎょう",
    "meaning": {
      "ja": "授業",
      "zh_TW": "上課、課堂",
      "zh_CN": "上课、课堂",
      "en": "class / lesson",
      "ko": "수업",
      "zh_HK": "上堂、課堂",
      "fr": "cours / leçon"
    },
    "example": {
      "ja": "A: <ruby>今日<rt>きょう</rt></ruby>の<ruby>授業<rt>じゅぎょう</rt></ruby>は<ruby>何時<rt>なんじ</rt></ruby>からですか。<br/>B: <ruby>午後<rt>ごご</rt></ruby>2<ruby>時<rt>じ</rt></ruby>から<ruby>始<rt>はじ</rt></ruby>まりますよ。",
      "zh_TW": "A: 今天的課幾點開始？<br/>B: 下午兩點開始喔。",
      "zh_CN": "A: 今天的课几点开始？<br/>B: 下午两点开始哦。",
      "en": "A: What time does today's class start?<br/>B: It starts at 2:00 PM.",
      "ko": "A: 오늘 수업은 몇 시부터예요?<br/>B: 오후 2시부터 시작해요.",
      "zh_HK": "A: 今日堂課幾點開始呀？<br/>B: 下晝兩點開始呀。",
      "fr": "A: À quelle heure commence le cours d'aujourd'hui ?<br/>B: Il commence à 14h."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688319_zs3yra__查某囝",
    "word": "娘",
    "reading": "むすめ",
    "meaning": {
      "ja": "娘",
      "zh_TW": "女兒",
      "zh_CN": "女儿",
      "en": "daughter",
      "ko": "딸",
      "zh_HK": "女、女兒",
      "fr": "fille (la sienne)"
    },
    "example": {
      "ja": "A: <ruby>娘<rt>むすめ</rt></ruby>さんはおいくつですか。<br/>B: <ruby>今年<rt>ことし</rt></ruby>7<ruby>歳<rt>さい</rt></ruby>で、とても<ruby>元気<rt>げんき</rt></ruby>です。",
      "zh_TW": "A: 令媛幾歲了呢？<br/>B: 今年7歲，非常活潑。",
      "zh_CN": "A: 您女儿几岁了呢？<br/>B: 今年7岁，非常活泼。",
      "en": "A: How old is your daughter?<br/>B: She is 7 years old this year and very lively.",
      "ko": "A: 따님은 몇 살인가요?<br/>B: 올해 7살인데 아주 활발해요.",
      "zh_HK": "A: 你個女幾多歲呀？<br/>B: 今年7歲，好生猛。",
      "fr": "A: Quel âge a votre fille ?<br/>B: Elle a 7 ans cette année et est très vive."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688325_7evzn9__表兄弟",
    "word": "いとこ",
    "reading": "いとこ",
    "meaning": {
      "ja": "いとこ",
      "zh_TW": "堂表兄弟姊妹",
      "zh_CN": "堂表兄弟姐妹",
      "en": "cousin",
      "ko": "사촌",
      "zh_HK": "表兄弟姊妹",
      "fr": "cousin / cousine"
    },
    "example": {
      "ja": "A: <ruby>週末<rt>しゅうまつ</rt></ruby>はいとこの<ruby>家<rt>いえ</rt></ruby>へ<ruby>遊<rt>あそ</rt></ruby>びに行きました。<br/>B: <ruby>久<rt>ひさ</rt></ruby>しぶりに会えて楽しかったですね！",
      "zh_TW": "A: 週末我去了表親家玩。<br/>B: 久別重逢一定很開心吧！",
      "zh_CN": "A: 周末我去了堂表亲家玩。<br/>B: 久别重逢一定很开心吧！",
      "en": "A: I went to play at my cousin's house over the weekend.<br/>B: It must have been fun catching up after so long!",
      "ko": "A: 주말에 사촌 집에 놀러 갔어요.<br/>B: 오랜만에 만나서 즐거웠겠네요!",
      "zh_HK": "A: 週末我去咗表親屋企玩。<br/>B: 好耐冇見一定好開心啦！",
      "fr": "A: Ce week-end, je suis allé chez mon cousin.<br/>B: C'était chouette de se revoir après si longtemps !"
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688336_q6wafx__毋是",
    "word": "違います",
    "reading": "ちがいます",
    "meaning": {
      "ja": "違います",
      "zh_TW": "不是、不對",
      "zh_CN": "不是、不对",
      "en": "No, that's wrong / incorrect",
      "ko": "아닙니다 / 틀립니다",
      "zh_HK": "唔係、唔啱",
      "fr": "Ce n'est pas ça / C'est faux"
    },
    "example": {
      "ja": "A: あの<ruby>人<rt>ひと</rt></ruby>は<ruby>田中<rt>たなか</rt></ruby>さんですか。<br/>B: いいえ、<ruby>違<rt>ちが</rt></ruby>います。<ruby>佐藤<rt>さとう</rt></ruby>さんですよ。",
      "zh_TW": "A: 那個人是田中先生嗎？<br/>B: 不，不是喔。那位是佐藤先生。",
      "zh_CN": "A: 那个人是田中先生吗？<br/>B: 不，不是哦。那位是佐藤先生。",
      "en": "A: Is that person Mr. Tanaka?<br/>B: No, that's not right. That is Mr. Sato.",
      "ko": "A: 저 사람은 다나카 씨인가요?<br/>B: 아니요, 아닙니다. 사토 씨예요.",
      "zh_HK": "A: 嗰個人係咪田中先生呀？<br/>B: 唔係，嗰個係佐藤先生呀。",
      "fr": "A: Cette personne est M. Tanaka ?<br/>B: Non, ce n'est pas lui. C'est M. Sato."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688346_73s76l__毋是按呢",
    "word": "そうじゃありません",
    "reading": "そうじゃありません",
    "meaning": {
      "ja": "そうじゃありません",
      "zh_TW": "不是那樣的",
      "zh_CN": "不是那样的",
      "en": "That is not so / Not like that",
      "ko": "그렇지 않습니다",
      "zh_HK": "唔係咁㗎",
      "fr": "Ce n'est pas comme ça"
    },
    "example": {
      "ja": "A: <ruby>怒<rt>おこ</rt></ruby>っているんですか。<br/>B: いいえ、そうじゃありませんよ。<ruby>少<rt>すこ</rt></ruby>し<ruby>疲<rt>つか</rt></ruby>れているだけです。",
      "zh_TW": "A: 你在生氣嗎？<br/>B: 不，不是那樣的。我只是有點累而已。",
      "zh_CN": "A: 你在生气吗？<br/>B: 不，不是那样的。我只是有点累而已。",
      "en": "A: Are you angry?<br/>B: No, it's not like that. I'm just a little tired.",
      "ko": "A: 화나셨나요?<br/>B: 아니요, 그렇지 않아요. 조금 피곤할 뿐이에요.",
      "zh_HK": "A: 你係咪嬲緊呀？<br/>B: 唔係，唔係咁㗎。我只係有啲攰啫。",
      "fr": "A: Tu es en colère ?<br/>B: Non, pas du tout. Je suis juste un peu fatigué."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688353_f3bg8v__國小學生",
    "word": "小学生",
    "reading": "しょうがくせい",
    "meaning": {
      "ja": "小学生",
      "zh_TW": "國小生、小學生",
      "zh_CN": "小学生",
      "en": "elementary school student",
      "ko": "초등학생",
      "zh_HK": "小學生",
      "fr": "élève d'école primaire"
    },
    "example": {
      "ja": "A: お<ruby>子<rt>こ</rt></ruby>さんは<ruby>小学生<rt>しょうがくせい</rt></ruby>ですか。<br/>B: はい、<ruby>今年<rt>ことし</rt></ruby><ruby>小学校<rt>しょうがっこう</rt></ruby>3<ruby>年生<rt>ねんせい</rt></ruby>です。",
      "zh_TW": "A: 您的孩子是小學生嗎？<br/>B: 是的，今年讀小學三年級。",
      "zh_CN": "A: 您的孩子是小学生吗？<br/>B: 是的，今年读小学三年级。",
      "en": "A: Is your child an elementary school student?<br/>B: Yes, in third grade this year.",
      "ko": "A: 아이는 초등학생인가요?<br/>B: 네, 올해 초등학교 3학년이에요.",
      "zh_HK": "A: 你小朋友讀小學㗎？<br/>B: 係呀，今年讀小學三年級。",
      "fr": "A: Votre enfant est à l'école primaire ?<br/>B: Oui, il est en troisième année."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688364_qe1b03__國中學生",
    "word": "中学生",
    "reading": "ちゅうがくせい",
    "meaning": {
      "ja": "中学生",
      "zh_TW": "國中生",
      "zh_CN": "初中生",
      "en": "junior high school student",
      "ko": "중학생",
      "zh_HK": "初中生",
      "fr": "collégien"
    },
    "example": {
      "ja": "A: <ruby>弟<rt>おとうと</rt></ruby>は<ruby>来年<rt>らいねん</rt></ruby>から<ruby>中学生<rt>ちゅうがくせい</rt></ruby>になります。<br/>B: もう<ruby>中学生<rt>ちゅうがくせい</rt></ruby>ですか、<ruby>大<rt>おお</rt></ruby>きくなりましたね！",
      "zh_TW": "A: 我弟弟明年就要升國中了。<br/>B: 已經是國中生了呀，長得真快！",
      "zh_CN": "A: 我弟弟明年就要升初中了。<br/>B: 已经是初中生了呀，长得真快！",
      "en": "A: My brother will become a junior high student next year.<br/>B: Junior high already? He has grown so much!",
      "ko": "A: 남동생은 내년부터 중학생이 돼요.<br/>B: 벌써 중학생인가요, 많이 컸네요!",
      "zh_HK": "A: 細佬出年升中學喇。<br/>B: 已經升中喇？大得真係快！",
      "fr": "A: Mon frère entrera au collège l'année prochaine.<br/>B: Déjà au collège ? Il a tellement grandi !"
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688376_iy5cb6__高中學生",
    "word": "高校生",
    "reading": "こうこうせい",
    "meaning": {
      "ja": "高校生",
      "zh_TW": "高中生",
      "zh_CN": "高中生",
      "en": "high school student",
      "ko": "고등학생",
      "zh_HK": "高中生",
      "fr": "lycéen"
    },
    "example": {
      "ja": "A: <ruby>妹<rt>いもうと</rt></ruby>は<ruby>高校生<rt>こうこうせい</rt></ruby>で、<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>電車<rt>でんしゃ</rt></ruby>で<ruby>通学<rt>つうがく</rt></ruby>しています。<br/>B: <ruby>勉強<rt>べんきょう</rt></ruby>も<ruby>部活<rt>ぶかつ</rt></ruby>も<ruby>頑張<rt>がんば</rt></ruby>っているんですね。",
      "zh_TW": "A: 妹妹是高中生，每天早上搭電車上學。<br/>B: 課業和社團活動都很努力呢。",
      "zh_CN": "A: 妹妹是高中生，每天早上乘电车上学。<br/>B: 课业和社团活动都很努力呢。",
      "en": "A: My sister is a high school student and commutes by train every morning.<br/>B: She must be working hard in both studies and clubs.",
      "ko": "A: 여동생은 고등학생이라 매일 아침 전철로 통학해요.<br/>B: 공부도 동아리 활동도 열심히 하고 있네요.",
      "zh_HK": "A: 妹頭係高中生，每日朝早搭火車返學。<br/>B: 讀書同課外活動都好努力喎。",
      "fr": "A: Ma sœur est lycéenne et prend le train tous les matins.<br/>B: Elle travaille dur pour ses études et ses activités."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688382_9oq0pi__大學生",
    "word": "大学生",
    "reading": "だいがくせい",
    "meaning": {
      "ja": "大学生",
      "zh_TW": "大學生",
      "zh_CN": "大学生",
      "en": "college student / university student",
      "ko": "대학생",
      "zh_HK": "大學生",
      "fr": "étudiant universitaire"
    },
    "example": {
      "ja": "A: <ruby>兄<rt>あに</rt></ruby>は<ruby>今<rt>いま</rt></ruby><ruby>大学生<rt>だいがくせい</rt></ruby>で、<ruby>一人暮<rt>ひとりぐ</rt></ruby>らしをしています。<br/>B: <ruby>大学<rt>だいがく</rt></ruby>でどんなことを<ruby>学<rt>まな</rt></ruby>んでいるんですか。",
      "zh_TW": "A: 哥哥現在是大學生，正在一個人住。<br/>B: 他在大學主修什麼呢？",
      "zh_CN": "A: 哥哥现在是大学生，一个人在外面住。<br/>B: 他在大学学什么专业呢？",
      "en": "A: My older brother is currently a college student living alone.<br/>B: What is he studying at university?",
      "ko": "A: 형은 지금 대학생이고 자취를 하고 있어요.<br/>B: 대학교에서 어떤 것을 공부하고 있나요?",
      "zh_HK": "A: 呀哥依家係大學生，自己一個人住。<br/>B: 佢喺大學讀緊咩科呀？",
      "fr": "A: Mon grand frère est étudiant et vit seul.<br/>B: Qu'étudie-t-il à l'université ?"
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688402_ry1bj3__請問你是佗一位？",
    "word": "どちら様ですか",
    "reading": "どちらさまですか",
    "meaning": {
      "ja": "どちら様ですか（失礼ですが、お名前を伺ってもよろしいですか）",
      "zh_TW": "請問您是哪位？",
      "zh_CN": "请问您是哪位？",
      "en": "May I ask who is calling/speaking?",
      "ko": "어느 분이신가요? / 누구십니까?",
      "zh_HK": "請問邊位呀？",
      "fr": "Puis-je savoir qui est à l'appareil ?"
    },
    "example": {
      "ja": "A: お<ruby>電話<rt>でんわ</rt></ruby>ありがとうございます、ハク<ruby>日本語<rt>にほんご</rt></ruby><ruby>教室<rt>きょうしつ</rt></ruby>です。<br/>B: <ruby>失礼<rt>しつれい</rt></ruby>ですが、どちら<ruby>様<rt>さま</rt></ruby>でしょうか。",
      "zh_TW": "A: 謝謝您的來電，這裡是哈克日語教室。<br/>B: 請問您是哪位呢？",
      "zh_CN": "A: 感谢您的来电，这里是哈克日语教室。<br/>B: 请问您是哪位呢？",
      "en": "A: Thank you for calling Haku Japanese Class.<br/>B: May I ask who is calling, please?",
      "ko": "A: 전화 감사합니다, 하쿠 일본어 교실입니다.<br/>B: 실례지만 어느 분이신가요?",
      "zh_HK": "A: 多謝你打嚟，呢度係哈克日語教室。<br/>B: 請問邊位呀？",
      "fr": "A: Merci d'avoir appelé le cours de japonais Haku.<br/>B: Puis-je vous demander à qui j'ai l'honneur ?"
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688408_d265ew__教室",
    "word": "教室",
    "reading": "きょうしつ",
    "meaning": {
      "ja": "教室",
      "zh_TW": "教室",
      "zh_CN": "教室",
      "en": "classroom",
      "ko": "교실",
      "zh_HK": "課室、教室",
      "fr": "salle de classe"
    },
    "example": {
      "ja": "A: <ruby>次<rt>つぎ</rt></ruby>の<ruby>授業<rt>じゅぎょう</rt></ruby>はどの<ruby>教室<rt>きょうしつ</rt></ruby>ですか。<br/>B: 3<ruby>階<rt>かい</rt></ruby>の201<ruby>教室<rt>きょうしつ</rt></ruby>ですよ。",
      "zh_TW": "A: 下一堂課在哪間教室呢？<br/>B: 在3樓的201教室喔。",
      "zh_CN": "A: 下一节课在哪个教室呢？<br/>B: 在3楼的201教室哦。",
      "en": "A: Which classroom is the next lesson in?<br/>B: It's in classroom 201 on the 3rd floor.",
      "ko": "A: 다음 수업은 어느 교실인가요?<br/>B: 3층 201호 교실이에요.",
      "zh_HK": "A: 下一堂喺邊間課室上呀？<br/>B: 喺3樓嘅201課室呀。",
      "fr": "A: Dans quelle salle a lieu le prochain cours ?<br/>B: C'est en salle 201 au 3e étage."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688415_he8qrr__辭典",
    "word": "辞書",
    "reading": "じしょ",
    "meaning": {
      "ja": "辞書",
      "zh_TW": "字典、辭典",
      "zh_CN": "词典、字典",
      "en": "dictionary",
      "ko": "사전",
      "zh_HK": "字典、辭典",
      "fr": "dictionnaire"
    },
    "example": {
      "ja": "A: わからない<ruby>言葉<rt>ことば</rt></ruby>があったらどうしますか。<br/>B: スマホの<ruby>辞書<rt>じしょ</rt></ruby>アプリで<ruby>調<rt>しら</rt></ruby>べています。",
      "zh_TW": "A: 遇到不懂的單字該怎麼辦？<br/>B: 我都用手機上的辭典App查。",
      "zh_CN": "A: 遇到不懂的词汇该怎么办？<br/>B: 我都用手机上的词典App查。",
      "en": "A: What do you do when there's a word you don't know?<br/>B: I look it up on a smartphone dictionary app.",
      "ko": "A: 모르는 단어가 나오면 어떻게 하나요?<br/>B: 스마트폰 사전 앱으로 찾아요.",
      "zh_HK": "A: 唔識嘅字你會點做呀？<br/>B: 我會用手機字典App查。",
      "fr": "A: Que fais-tu quand tu ne connais pas un mot ?<br/>B: Je le cherche sur une appli de dictionnaire."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688423_uigyv2__拊仔",
    "word": "消しゴム",
    "reading": "けしごむ",
    "meaning": {
      "ja": "消しゴム",
      "zh_TW": "橡皮擦",
      "zh_CN": "橡皮擦",
      "en": "eraser",
      "ko": "지우개",
      "zh_HK": "擦膠",
      "fr": "gomme"
    },
    "example": {
      "ja": "A: すみません、<ruby>消<rt>け</rt></ruby>しゴムを<ruby>忘<rt>わす</rt></ruby>れてしまいました。<br/>B: <ruby>私<rt>わたし</rt></ruby>のを使ってもいいですよ。",
      "zh_TW": "A: 不好意思，我忘了帶橡皮擦。<br/>B: 可以借你用我的喔。",
      "zh_CN": "A: 不好意思，我忘了带橡皮擦。<br/>B: 可以借你用我的哦。",
      "en": "A: Excuse me, I forgot my eraser.<br/>B: You can borrow mine!",
      "ko": "A: 죄송해요, 지우개를 깜빡했어요.<br/>B: 제 것을 쓰셔도 돼요.",
      "zh_HK": "A: 唔好意思，我唔記得帶擦膠添。<br/>B: 你可以用我嗰嚿㗎。",
      "fr": "A: Excusez-moi, j'ai oublié ma gomme.<br/>B: Tu peux utiliser la mienne !"
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688436_hob5io__家己煮",
    "word": "自炊",
    "reading": "じすい",
    "meaning": {
      "ja": "自炊（自分で料理を作ること）",
      "zh_TW": "自己煮、自炊",
      "zh_CN": "自己做饭、自炊",
      "en": "cooking for oneself",
      "ko": "자취 요리 / 직접 요리하기",
      "zh_HK": "自己煮飯",
      "fr": "cuisiner soi-même"
    },
    "example": {
      "ja": "A: <ruby>普段<rt>ふだん</rt></ruby>は<ruby>自炊<rt>じすい</rt></ruby>をしていますか。<br/>B: はい、<ruby>健康<rt>けんこう</rt></ruby>と<ruby>節約<rt>せつやく</rt></ruby>のために<ruby>家<rt>いえ</rt></ruby>で<ruby>作<rt>つく</rt></ruby>っています。",
      "zh_TW": "A: 平常你會自己煮飯嗎？<br/>B: 會的，為了健康和省錢都在家自己煮。",
      "zh_CN": "A: 平常你会自己做饭吗？<br/>B: 会的，为了健康和省钱都在家做饭。",
      "en": "A: Do you usually cook for yourself?<br/>B: Yes, I cook at home for health and to save money.",
      "ko": "A: 평소에 직접 요리를 해 드시나요?<br/>B: 네, 건강과 절약을 위해 집에서 만들어 먹어요.",
      "zh_HK": "A: 平時你會唔會自己煮飯食㗎？<br/>B: 會呀，為咗健康同慳錢多數自己煮。",
      "fr": "A: Cuisines-tu toi-même d'habitude ?<br/>B: Oui, pour la santé et pour économiser."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688454_nx4xci__趁錢",
    "word": "稼ぐ",
    "reading": "かせぐ",
    "meaning": {
      "ja": "稼ぐ（お金を得る）",
      "zh_TW": "賺錢",
      "zh_CN": "赚钱",
      "en": "to earn (money)",
      "ko": "벌다 (돈을 벌다)",
      "zh_HK": "賺錢、搵錢",
      "fr": "gagner (de l'argent)"
    },
    "example": {
      "ja": "A: アルバイトでお<ruby>金<rt>かね</rt></ruby>を<ruby>稼<rt>かせ</rt></ruby>いで、<ruby>日本<rt>にほん</rt></ruby><ruby>旅行<rt>りょこう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きたいです。<br/>B: 素晴らしいですね！<ruby>応援<rt>おうえん</rt></ruby>しています。",
      "zh_TW": "A: 我想靠打工賺錢去日本旅行。<br/>B: 太棒了！我支持你。",
      "zh_CN": "A: 我想靠兼职打工赚钱去日本旅行。<br/>B: 太棒了！我支持你。",
      "en": "A: I want to earn money from a part-time job to travel to Japan.<br/>B: That's wonderful! I'm cheering for you.",
      "ko": "A: 아르바이트로 돈을 벌어서 일본 여행을 가고 싶어요.<br/>B: 멋지네요! 응원할게요.",
      "zh_HK": "A: 我想做兼職搵錢去日本旅行呀。<br/>B: 好正喎！撐你！",
      "fr": "A: Je veux gagner de l'argent avec un petit boulot pour voyager au Japon.<br/>B: C'est formidable ! Je t'encourage."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688468_79djqd__銀行",
    "word": "銀行",
    "reading": "ぎんこう",
    "meaning": {
      "ja": "銀行",
      "zh_TW": "銀行",
      "zh_CN": "银行",
      "en": "bank",
      "ko": "은행",
      "zh_HK": "銀行",
      "fr": "banque"
    },
    "example": {
      "ja": "A: これから<ruby>駅前<rt>えきまえ</rt></ruby>の<ruby>銀行<rt>ぎんこう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>ってきます。<br/>B: ついでにお<ruby>金<rt>かね</rt></ruby>をおろしてきてもらえますか。",
      "zh_TW": "A: 我現在要去站前的銀行一趟。<br/>B: 能順便幫我領點錢嗎？",
      "zh_CN": "A: 我现在要去站前的银行一趟。<br/>B: 能顺便帮我取点钱吗？",
      "en": "A: I'm going to the bank in front of the station now.<br/>B: Could you withdraw some cash for me while you're there?",
      "ko": "A: 지금부터 역 앞 은행에 다녀올게요.<br/>B: 가는 김에 돈 좀 찾아다 줄 수 있어요?",
      "zh_HK": "A: 我依家去站前嗰間銀行一趟。<br/>B: 可唔可以順便幫我撳啲錢呀？",
      "fr": "A: Je vais à la banque devant la gare.<br/>B: Peux-tu me retirer un peu d'argent en passant ?"
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688474_g6755p__事務所",
    "word": "事務所",
    "reading": "じむしょ",
    "meaning": {
      "ja": "事務所（オフィス）",
      "zh_TW": "辦公室、事務所",
      "zh_CN": "办公室、事务所",
      "en": "office",
      "ko": "사무소 / 사무실",
      "zh_HK": "寫字樓、辦公室",
      "fr": "bureau / cabinet"
    },
    "example": {
      "ja": "A: <ruby>提出<rt>ていしゅつ</rt></ruby><ruby>書類<rt>しょるい</rt></ruby>はどちらへ<ruby>持<rt>も</rt></ruby>って<ruby>行<rt>い</rt></ruby>けばいいですか。<br/>B: 1<ruby>階<rt>かい</rt></ruby>の<ruby>事務所<rt>じむしょ</rt></ruby>へ<ruby>提出<rt>ていしゅつ</rt></ruby>してください。",
      "zh_TW": "A: 要繳交的文件該送到哪裡呢？<br/>B: 請交到1樓的辦公室。",
      "zh_CN": "A: 要提交的文件该交到哪里呢？<br/>B: 请交到1楼的办公室。",
      "en": "A: Where should I take the documents to submit?<br/>B: Please submit them to the office on the 1st floor.",
      "ko": "A: 제출 서류는 어디로 가져가면 되나요?<br/>B: 1층 사무실에 제출해 주세요.",
      "zh_HK": "A: 份文件要交去邊度呀？<br/>B: 請交去1樓辦公室。",
      "fr": "A: Où dois-je apporter les documents à déposer ?<br/>B: Déposez-les au bureau du rez-de-chaussée."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688480_rwo43z__桌仔",
    "word": "机",
    "reading": "つくえ",
    "meaning": {
      "ja": "机",
      "zh_TW": "桌子、書桌",
      "zh_CN": "桌子、书桌",
      "en": "desk",
      "ko": "책상",
      "zh_HK": "書枱、枱",
      "fr": "bureau (meuble)"
    },
    "example": {
      "ja": "A: テキストはどこに<ruby>置<rt>お</rt></ruby>きましたか。<br/>B: <ruby>机<rt>つくえ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に<ruby>置<rt>お</rt></ruby>いてありますよ。",
      "zh_TW": "A: 課本放在哪裡了？<br/>B: 就放在桌上喔。",
      "zh_CN": "A: 课本放在哪里了？<br/>B: 就放在桌子上哦。",
      "en": "A: Where did you put the textbook?<br/>B: It's on top of the desk.",
      "ko": "A: 교재는 어디에 두었나요?<br/>B: 책상 위에 올려져 있어요.",
      "zh_HK": "A: 本書擺咗喺邊呀？<br/>B: 擺咗喺書枱上面呀。",
      "fr": "A: Où as-tu mis le manuel ?<br/>B: Il est posé sur le bureau."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688494_kh4lzt__會議室",
    "word": "会議室",
    "reading": "かいぎしつ",
    "meaning": {
      "ja": "会議室",
      "zh_TW": "會議室",
      "zh_CN": "会议室",
      "en": "meeting room / conference room",
      "ko": "회의실",
      "zh_HK": "會議室",
      "fr": "salle de réunion"
    },
    "example": {
      "ja": "A: <ruby>午後<rt>ごご</rt></ruby>のミーティングはどこで<ruby>行<rt>おこな</rt></ruby>いますか。<br/>B: 2<ruby>階<rt>かい</rt></ruby>の<ruby>会議室<rt>かいぎしつ</rt></ruby>Aに<ruby>集<rt>あつ</rt></ruby>まってください。",
      "zh_TW": "A: 下午的會議在哪裡開呢？<br/>B: 請大家到2樓的A會議室集合。",
      "zh_CN": "A: 下午的会议在哪里开呢？<br/>B: 请大家到2楼的A会议室集合。",
      "en": "A: Where will the afternoon meeting be held?<br/>B: Please gather in Conference Room A on the 2nd floor.",
      "ko": "A: 오후 미팅은 어디서 하나요?<br/>B: 2층 회의실 A로 모여 주세요.",
      "zh_HK": "A: 下晝個會喺邊度開呀？<br/>B: 請去2樓A會議室集合。",
      "fr": "A: Où se tiendra la réunion de l'après-midi ?<br/>B: Rendez-vous en salle de réunion A au 2e étage."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688516_ik2gk3__有飼",
    "word": "飼っています",
    "reading": "かっています",
    "meaning": {
      "ja": "飼っています（ペットを飼育している）",
      "zh_TW": "有養（寵物）",
      "zh_CN": "养着（宠物）",
      "en": "keeping / raising (a pet)",
      "ko": "기르고 있습니다 / 키우고 있습니다",
      "zh_HK": "養緊（寵物）",
      "fr": "élever / avoir (un animal de compagnie)"
    },
    "example": {
      "ja": "A: ペットは<ruby>何<rt>なに</rt></ruby>か<ruby>飼<rt>か</rt></ruby>っていますか。<br/>B: はい、かわいい<ruby>猫<rt>ねこ</rt></ruby>を2<ruby>匹<rt>ひき</rt></ruby><ruby>飼<rt>か</rt></ruby>っていますよ。",
      "zh_TW": "A: 你有養什麼寵物嗎？<br/>B: 有的，我養了兩隻可愛的貓咪喔。",
      "zh_CN": "A: 你有养什么宠物吗？<br/>B: 有的，我养了两只可爱的猫咪哦。",
      "en": "A: Do you have any pets?<br/>B: Yes, I have two cute cats.",
      "ko": "A: 반려동물 키우고 계신가요?<br/>B: 네, 귀여운 고양이 두 마리를 키우고 있어요.",
      "zh_HK": "A: 你有冇養寵物呀？<br/>B: 有呀，我養咗兩隻好得意嘅貓貓。",
      "fr": "A: Avez-vous des animaux de compagnie ?<br/>B: Oui, j'ai deux chats adorables."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688526_e0wuwh__感情好",
    "word": "仲が良い",
    "reading": "なかがいい",
    "meaning": {
      "ja": "仲が良い",
      "zh_TW": "感情好、關係融洽",
      "zh_CN": "关系好、感情好",
      "en": "on good terms / close with",
      "ko": "사이가 좋다",
      "zh_HK": "好老友、感情好",
      "fr": "bien s'entendre / être proches"
    },
    "example": {
      "ja": "A: あの2<ruby>人<rt>ふたり</rt></ruby>はいつも<ruby>一緒<rt>いっしょ</rt></ruby>ですね。<br/>B: ええ、<ruby>昔<rt>むかし</rt></ruby>からとても<ruby>仲<rt>なか</rt></ruby>が<ruby>良<rt>よ</rt></ruby>い<ruby>親友<rt>しんゆう</rt></ruby>なんです。",
      "zh_TW": "A: 那兩個人總是在一起呢。<br/>B: 是啊，他們從小就是感情非常好的摯友。",
      "zh_CN": "A: 那两个人总是在一起呢。<br/>B: 是啊，他们从小就是感情非常好的挚友。",
      "en": "A: Those two are always together, aren't they?<br/>B: Yes, they've been very close best friends for a long time.",
      "ko": "A: 저 두 사람은 언제나 함께 있네요.<br/>B: 네, 예전부터 사이가 아주 좋은 절친이에요.",
      "zh_HK": "A: 嗰兩條友成日黐埋一齊嘅。<br/>B: 係呀，佢哋由細到大都係好老友嘅知己嚟㗎。",
      "fr": "A: Ces deux-là sont toujours ensemble, n'est-ce pas ?<br/>B: Oui, ce sont de très bons amis de longue date."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688541_0y0x7v__無好",
    "word": "よくない",
    "reading": "よくない",
    "meaning": {
      "ja": "よくない（良くない）",
      "zh_TW": "不好、不太好",
      "zh_CN": "不好、不妥",
      "en": "not good",
      "ko": "좋지 않다",
      "zh_HK": "唔好",
      "fr": "pas bien / mauvais"
    },
    "example": {
      "ja": "A: <ruby>夜遅<rt>よるおそ</rt></ruby>くまでスマホを<ruby>見<rt>み</rt></ruby>るのはよくないですよ。<br/>B: そうですね、<ruby>今日<rt>きょう</rt></ruby>からは<ruby>早<rt>はや</rt></ruby>く<ruby>寝<rt>ね</rt></ruby>ます。",
      "zh_TW": "A: 看手機看到深夜對身體不好喔。<br/>B: 說得也是，今天起我會早點睡。",
      "zh_CN": "A: 玩手机玩到深夜对身体不好哦。<br/>B: 说的也是，今天起我会早点睡。",
      "en": "A: Looking at your smartphone late into the night is not good for you.<br/>B: You're right, I'll go to sleep early starting tonight.",
      "ko": "A: 밤늦게까지 스마트폰을 보는 건 좋지 않아요.<br/>B: 맞아요, 오늘부터는 일찍 잘게요.",
      "zh_HK": "A: 睇手機睇到咁夜對身體唔好㗎。<br/>B: 係呀，今晚開始我早啲瞓喇。",
      "fr": "A: Regarder son smartphone tard le soir n'est pas bon pour la santé.<br/>B: C'est vrai, je vais me coucher tôt dès ce soir."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688558_cwqljh__大人",
    "word": "大人",
    "reading": "おとな",
    "meaning": {
      "ja": "大人（成人）",
      "zh_TW": "大人、成人",
      "zh_CN": "大人、成年人",
      "en": "adult",
      "ko": "어른 / 성인",
      "zh_HK": "大人",
      "fr": "adulte"
    },
    "example": {
      "ja": "A: <ruby>日本<rt>にほん</rt></ruby>では<ruby>何歳<rt>なんさい</rt></ruby>から<ruby>大人<rt>おとな</rt></ruby>になりますか。<br/>B: <ruby>法律<rt>ほうりつ</rt></ruby><ruby>上<rt>じょう</rt></ruby>は18<ruby>歳<rt>さい</rt></ruby>から<ruby>成人<rt>せいじん</rt></ruby>ですよ。",
      "zh_TW": "A: 在日本幾歲算成年大人呢？<br/>B: 法律上滿18歲就是成人了喔。",
      "zh_CN": "A: 在日本几岁算成年大人呢？<br/>B: 法律上满18岁就是成人了哦。",
      "en": "A: At what age does someone become an adult in Japan?<br/>B: Legally, one becomes an adult at age 18.",
      "ko": "A: 일본에서는 몇 살부터 어른이 되나요?<br/>B: 법률상으로는 18세부터 성인이에요.",
      "zh_HK": "A: 喺日本幾多歲先算大人呀？<br/>B: 法律上18歲就係成年人喇。",
      "fr": "A: À quel âge devient-on adulte au Japon ?<br/>B: Légalement, la majorité est à 18 ans."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688572_8rnism__揀食",
    "word": "偏食",
    "reading": "へんしょく",
    "meaning": {
      "ja": "偏食（好き嫌いが多いこと）",
      "zh_TW": "挑食、偏食",
      "zh_CN": "挑食、偏食",
      "en": "picky eating / unbalanced diet",
      "ko": "편식",
      "zh_HK": "揀飲擇食、偏食",
      "fr": "alimentation déséquilibrée / faire le difficile"
    },
    "example": {
      "ja": "A: <ruby>子<rt>こ</rt></ruby>どもの<ruby>頃<rt>ころ</rt></ruby>は<ruby>野菜<rt>やさい</rt></ruby>が<ruby>嫌<rt>きら</rt></ruby>いで<ruby>偏食<rt>へんしょく</rt></ruby>でした。<br/>B: <ruby>今<rt>いま</rt></ruby>は<ruby>何<rt>なん</rt></ruby>でも<ruby>食<rt>た</rt></ruby>べられるようになりましたか。",
      "zh_TW": "A: 小時候我很討厭蔬菜，非常挑食。<br/>B: 現在什麼都吃得下了嗎？",
      "zh_CN": "A: 小时候我很讨厌蔬菜，非常挑食。<br/>B: 现在什么都能吃了吗？",
      "en": "A: When I was a child, I hated vegetables and was a picky eater.<br/>B: Can you eat everything now?",
      "ko": "A: 어릴 때는 채소를 싫어해서 편식을 했어요.<br/>B: 지금은 뭐든지 잘 먹게 되었나요?",
      "zh_HK": "A: 細個嗰陣我好憎食菜，好揀飲擇食。<br/>B: 依家係咪咩都食得喇？",
      "fr": "A: Enfant, je détestais les légumes et je faisais le difficile.<br/>B: Peux-tu tout manger maintenant ?"
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688584_skej7u__茄仔",
    "word": "ナス",
    "reading": "なす",
    "meaning": {
      "ja": "ナス（茄子）",
      "zh_TW": "茄子",
      "zh_CN": "茄子",
      "en": "eggplant / aubergine",
      "ko": "가지",
      "zh_HK": "矮瓜、茄子",
      "fr": "aubergine"
    },
    "example": {
      "ja": "A: <ruby>夏野菜<rt>なつやさい</rt></ruby>の<ruby>中<rt>なか</rt></ruby>ではナスが<ruby>一番<rt>いちばん</rt></ruby><ruby>好<rt>す</rt></ruby>きです。<br/>B: <ruby>焼<rt>や</rt></ruby>きナスや<ruby>天<rt>てん</rt></ruby>ぷらにすると<ruby>美味<rt>おい</rt></ruby>しいですね。",
      "zh_TW": "A: 夏天蔬菜當中我最喜歡茄子。<br/>B: 做成烤茄子或天婦羅非常美味呢。",
      "zh_CN": "A: 夏季蔬菜当中我最喜欢茄子。<br/>B: 做成烤茄子或天妇罗非常美味呢。",
      "en": "A: Among summer vegetables, I like eggplant the best.<br/>B: It's delicious grilled or made into tempura.",
      "ko": "A: 여름 채소 중에서는 가지를 제일 좋아해요.<br/>B: 가지구이나 튀김으로 먹으면 정말 맛있죠.",
      "zh_HK": "A: 咁多夏天蔬菜之中我最鍾意食矮瓜。<br/>B: 整燒茄子或者天婦羅都好好食㗎。",
      "fr": "A: Parmi les légumes d'été, c'est l'aubergine que je préfère.<br/>B: C'est délicieux grillé ou en tempura."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688591_goll5a__青椒",
    "word": "ピーマン",
    "reading": "ぴーまん",
    "meaning": {
      "ja": "ピーマン",
      "zh_TW": "青椒",
      "zh_CN": "青椒",
      "en": "green bell pepper",
      "ko": "피망",
      "zh_HK": "青椒",
      "fr": "poivron vert"
    },
    "example": {
      "ja": "A: <ruby>今晩<rt>こんばん</rt></ruby>はピーマンと<ruby>牛肉<rt>ぎゅうにく</rt></ruby>の<ruby>炒<rt>いた</rt></ruby>め<ruby>物<rt>もの</rt></ruby>を<ruby>作<rt>つく</rt></ruby>ります。<br/>B: ピーマンがシャキシャキして<ruby>美味<rt>おい</rt></ruby>しそうですね！",
      "zh_TW": "A: 今晚要做青椒炒牛肉。<br/>B: 青椒脆脆的一定很下飯美味！",
      "zh_CN": "A: 今晚要做青椒炒牛肉。<br/>B: 青椒脆脆的一定很下饭美味！",
      "en": "A: Tonight I'm making stir-fried beef with bell peppers.<br/>B: The crisp peppers sound delicious!",
      "ko": "A: 오늘 저녁엔 피망 소고기 볶음을 만들 거예요.<br/>B: 피망이 아삭아삭해서 맛있겠네요!",
      "zh_HK": "A: 今晚我會炒青椒牛肉。<br/>B: 青椒爽爽脆脆咁一定好好食！",
      "fr": "A: Ce soir, je prépare du bœuf sauté aux poivrons verts.<br/>B: Les poivrons bien croquants, ça a l'air délicieux !"
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688597_v9gkjw__紅菜頭",
    "word": "にんじん",
    "reading": "にんじん",
    "meaning": {
      "ja": "にんじん（人参）",
      "zh_TW": "紅蘿蔔、胡蘿蔔",
      "zh_CN": "胡萝卜",
      "en": "carrot",
      "ko": "당근",
      "zh_HK": "紅蘿蔔",
      "fr": "carotte"
    },
    "example": {
      "ja": "A: カレーにはにんじんをたっぷり<ruby>入<rt>い</rt></ruby>れます。<br/>B: <ruby>甘<rt>あま</rt></ruby>みが出てとても<ruby>美味<rt>おい</rt></ruby>しくなりますね。",
      "zh_TW": "A: 煮咖哩時我會放很多紅蘿蔔。<br/>B: 會散發自然的甜味，變得非常好吃呢。",
      "zh_CN": "A: 煮咖喱时我会放很多胡萝卜。<br/>B: 会散发自然的甜味，变得非常好吃呢。",
      "en": "A: I put lots of carrots in curry.<br/>B: It brings out the sweetness and makes it very delicious.",
      "ko": "A: 카레에는 당근을 듬뿍 넣어요.<br/>B: 단맛이 우러나서 아주 맛있어지죠.",
      "zh_HK": "A: 煮咖喱我會落好多紅蘿蔔。<br/>B: 出晒甜味咁好正㗎。",
      "fr": "A: Je mets beaucoup de carottes dans le curry.<br/>B: Cela apporte de la douceur et c'est délicieux."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688604_h9kaib__口感",
    "word": "食感",
    "reading": "しょっかん",
    "meaning": {
      "ja": "食感（食べたときの口当たりの感じ）",
      "zh_TW": "口感",
      "zh_CN": "口感",
      "en": "food texture / mouthfeel",
      "ko": "식감",
      "zh_HK": "口感",
      "fr": "texture en bouche"
    },
    "example": {
      "ja": "A: このお<ruby>餅<rt>もち</rt></ruby>はモチモチした<ruby>食感<rt>しょっかん</rt></ruby>が<ruby>最高<rt>さいこう</rt></ruby>ですね。<br/>B: ええ、<ruby>食<rt>た</rt></ruby>べごたえがあってとても<ruby>美味<rt>おい</rt></ruby>しいです。",
      "zh_TW": "A: 這款麻糬Q彈的口感真是絕品。<br/>B: 是啊，很有嚼勁非常好吃。",
      "zh_CN": "A: 这款麻薯Q弹的口感真是绝品。<br/>B: 是啊，很有嚼劲非常好吃。",
      "en": "A: This mochi has the best chewy texture.<br/>B: Yes, it's very satisfying and delicious.",
      "ko": "A: 이 떡은 쫄깃쫄깃한 식감이 최고네요.<br/>B: 네, 씹는 맛이 있어서 아주 맛있어요.",
      "zh_HK": "A: 呢舊麻糬煙煙韌韌嘅口感真係正。<br/>B: 係呀，好有咬口好好食。",
      "fr": "A: Ce mochi a une texture moelleuse formidable.<br/>B: Oui, c'est très consistant et savoureux."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_1791710688612_euyhaw__日式蒸卵",
    "word": "茶碗蒸し",
    "reading": "ちゃわんむし",
    "meaning": {
      "ja": "茶碗蒸し",
      "zh_TW": "日式茶碗蒸",
      "zh_CN": "日式茶碗蒸",
      "en": "chawanmushi (savory steamed egg custard)",
      "ko": "차완무시 (일본식 달걀찜)",
      "zh_HK": "日式茶碗蒸、日式燉蛋",
      "fr": "chawanmushi (flan aux œufs salé à la japonaise)"
    },
    "example": {
      "ja": "A: <ruby>和食<rt>わしょく</rt></ruby>の<ruby>茶碗蒸<rt>ちゃわんむ</rt></ruby>しを<ruby>食<rt>た</rt></ruby>べたことがありますか。<br/>B: はい、出汁の味がして、なめらかで<ruby>大好<rt>だいす</rt></ruby>きです。",
      "zh_TW": "A: 你吃過日式料理的茶碗蒸嗎？<br/>B: 吃過，高湯的味道很濃郁，口感滑嫩，我很喜歡。",
      "zh_CN": "A: 你吃过日料里的茶碗蒸吗？<br/>B: 吃过，高汤味很浓，口感滑嫩，我很喜欢。",
      "en": "A: Have you ever eaten Japanese chawanmushi?<br/>B: Yes, it has a rich dashi flavor, is so smooth, and I love it.",
      "ko": "A: 일본 요리인 차완무시를 드셔 본 적이 있나요?<br/>B: 네, 육수 맛이 나고 부드러워서 정말 좋아해요.",
      "zh_HK": "A: 你食過日本料理嘅茶碗蒸未呀？<br/>B: 食過呀，好香高湯味又滑，我好鍾意。",
      "fr": "A: As-tu déjà goûté au chawanmushi japonais ?<br/>B: Oui, c'est doux, riche en bouillon dashi et j'adore ça."
    },
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_eliie_kyuushoku",
    "word": "給食",
    "reading": "きゅうしょく",
    "meaning": {
      "ja": "給食",
      "zh_TW": "學校營養午餐、學校供餐",
      "zh_CN": "学校营养午餐、学校配餐",
      "en": "school lunch, provided meal",
      "ko": "급식",
      "zh_HK": "學校午餐、學校供餐",
      "fr": "repas scolaire, cantine"
    },
    "example": {
      "ja": "<ruby>小学校<rt>しょうがっこう</rt></ruby>の<ruby>頃<rt>ころ</rt></ruby>、<ruby>給食<rt>きゅうしょく</rt></ruby>の<ruby>時間<rt>じかん</rt></ruby>がいちばん<ruby>楽<rt>たの</rt></ruby>しみだった。",
      "zh_TW": "小學時，營養午餐時間是我最期待的時光。",
      "zh_CN": "小学时，吃营养午餐的时间是我最期待的时光。",
      "en": "When I was in elementary school, school lunch time was what I looked forward to the most.",
      "ko": "초등학교 시절, 급식 시간이 가장 기다려졌다.",
      "zh_HK": "小學嗰陣，食午餐嘅時間係我最期待嘅時光。",
      "fr": "À l'école primaire, le moment de la cantine était ce que j'attendais avec le plus d'impatience."
    },
    "related": "きゅうしょく（授業の重要表現）",
    "studentId": "0010",
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_eliie_kangoshi",
    "word": "看護師",
    "reading": "かんごし",
    "meaning": {
      "ja": "看護師",
      "zh_TW": "護理師",
      "zh_CN": "护士、护理师",
      "en": "nurse",
      "ko": "간호사",
      "zh_HK": "護士",
      "fr": "infirmier, infirmière"
    },
    "example": {
      "ja": "<ruby>彼女<rt>かのじょ</rt></ruby>は<ruby>大<rt>おお</rt></ruby>きな<ruby>総合病院<rt>そうごうびょういん</rt></ruby>で<ruby>看護師<rt>かんごし</rt></ruby>として<ruby>働<rt>はたら</rt></ruby>いている。",
      "zh_TW": "她在一家大型綜合醫院擔任護理師。",
      "zh_CN": "她在一家大型综合医院担任护士。",
      "en": "She works as a nurse at a large general hospital.",
      "ko": "그녀는 큰 종합병원에서 간호사로 일하고 있다.",
      "zh_HK": "佢喺一間大型綜合醫院做護士。",
      "fr": "Elle travaille comme infirmière dans un grand hôpital général."
    },
    "related": "かんごし（授業の重要表現）",
    "studentId": "0010",
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_eliie_nuigurumi",
    "word": "ぬいぐるみ",
    "reading": "ぬいぐるみ",
    "meaning": {
      "ja": "ぬいぐるみ",
      "zh_TW": "絨毛玩偶、布偶",
      "zh_CN": "毛绒玩偶、布偶",
      "en": "stuffed animal, plush toy",
      "ko": "봉제 인형",
      "zh_HK": "毛公仔、布公仔",
      "fr": "peluche, doudou"
    },
    "example": {
      "ja": "<ruby>子供<rt>こども</rt></ruby>の<ruby>誕生日<rt>たんじょうび</rt></ruby>に、<ruby>大<rt>おお</rt></ruby>きなクマのぬいぐるみをプレゼントした。",
      "zh_TW": "在孩子的生日時，送了一隻大熊絨毛玩偶當禮物。",
      "zh_CN": "在孩子生日时，送了一只大熊毛绒玩偶当礼物。",
      "en": "For my child's birthday, I gave them a big teddy bear plush toy as a present.",
      "ko": "아이 생일에 커다란 곰 인형을 선물했다.",
      "zh_HK": "喺仔女嘅生日嗰陣，送咗隻大熊毛公仔做禮物。",
      "fr": "Pour l'anniversaire de mon enfant, j'ai offert une grande peluche d'ours en cadeau."
    },
    "related": "ぬいぐるみ（授業の重要表現）",
    "studentId": "0010",
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_eliie_ryourinin",
    "word": "料理人",
    "reading": "りょうりにん",
    "meaning": {
      "ja": "料理人",
      "zh_TW": "廚師、料理人",
      "zh_CN": "厨师、料理人",
      "en": "chef, cook",
      "ko": "요리사",
      "zh_HK": "廚師、料理人",
      "fr": "cuisinier, chef"
    },
    "example": {
      "ja": "<ruby>彼<rt>かれ</rt></ruby>はフランスで<ruby>修行<rt>しゅぎょう</rt></ruby>を<ruby>積<rt>つ</rt></ruby>んだ<ruby>一流<rt>いちりゅう</rt></ruby>の<ruby>料理人<rt>りょうりにん</rt></ruby>だ。",
      "zh_TW": "他是在法國經歷嚴格磨練的一流廚師。",
      "zh_CN": "他是在法国经历严格磨炼的一流厨师。",
      "en": "He is a top-notch chef who trained in France.",
      "ko": "그는 프랑스에서 수련을 쌓은 일류 요리사이다.",
      "zh_HK": "佢係喺法國磨練過嘅一流廚師。",
      "fr": "C'est un cuisinier de premier ordre qui a fait son apprentissage en France."
    },
    "related": "りょうりにん（授業の重要表現）",
    "studentId": "0010",
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_eliie_anaba",
    "word": "穴場",
    "reading": "あなば",
    "meaning": {
      "ja": "穴場",
      "zh_TW": "私房景點、私房好去處、秘境",
      "zh_CN": "小众好去处、秘境",
      "en": "hidden gem, little-known good spot",
      "ko": "숨은 명소",
      "zh_HK": "私房好去處、秘境",
      "fr": "bon plan secret, lieu méconnu"
    },
    "example": {
      "ja": "ここは<ruby>観光客<rt>かんこうきゃく</rt></ruby>がほとんど<ruby>来<rt>こ</rt></ruby>ない、<ruby>地元<rt>じもと</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>だけが<ruby>知<rt>し</rt></ruby>る<ruby>穴場<rt>あなば</rt></ruby>のカフェだ。",
      "zh_TW": "這裡幾乎沒有觀光客來，是只有當地人才知道的私房咖啡廳。",
      "zh_CN": "这里几乎没有游客来，是只有当地人才知道的宝藏咖啡馆。",
      "en": "This is a hidden gem cafe where hardly any tourists come and only locals know about it.",
      "ko": "이곳은 관광객이 거의 오지 않는, 현지인들만 아는 숨은 카페이다.",
      "zh_HK": "呢度差唔多無遊客嚟，係得當地人先知嘅私房咖啡店。",
      "fr": "C'est un café secret où viennent très peu de touristes et que seuls les locaux connaissent."
    },
    "related": "あなば（授業の重要表現）",
    "studentId": "0010",
    "category": "授業で習った言葉",
    "isCustom": true
  },
  {
    "id": "card_eliie_okashizukuri",
    "word": "お菓子作り",
    "reading": "おかしづくり",
    "meaning": {
      "ja": "お菓子作り",
      "zh_TW": "做點心、做甜點、烘焙",
      "zh_CN": "做点心、做甜品、烘焙",
      "en": "making sweets, baking",
      "ko": "과자 만들기, 제과",
      "zh_HK": "整甜品、整糕點、烘焙",
      "fr": "pâtisserie, confection de confiseries"
    },
    "example": {
      "ja": "<ruby>彼女<rt>かのじょ</rt></ruby>の<ruby>趣味<rt>しゅみ</rt></ruby>はお<ruby>菓子作<rt>かしづく</rt></ruby>りで、<ruby>週末<rt>しゅうまつ</rt></ruby>によくクッキーを<ruby>焼<rt>や</rt></ruby>いている。",
      "zh_TW": "她的興趣是做甜點，週末經常烤餅乾。",
      "zh_CN": "她的爱好是做甜点，周末经常烤饼干。",
      "en": "Her hobby is baking sweets, and she often bakes cookies on weekends.",
      "ko": "그녀의 취미는 과자 만들기라 주말마다 쿠키를 굽곤 한다.",
      "zh_HK": "佢嘅興趣係整甜品，週末成日焗曲奇。",
      "fr": "Son passe-temps est la pâtisserie, et elle prépare souvent des biscuits le week-end."
    },
    "related": "おかしづくり（授業の重要表現）",
    "studentId": "0010",
    "category": "授業で習った言葉",
    "isCustom": true
  }
];

  const ARUN_NEW_CARD_IDS = ["card_0023_shitami", "card_0023_suugakusha", "card_0023_houritsu", "card_0023_irairasuru", "card_0023_koukai", "card_0023_hikoukai", "card_0023_okodukai", "card_0023_koukai_regret", "card_0023_kuchipaku", "card_0023_nokawarini", "card_0023_manten", "card_0023_tensai", "card_0023_souko", "card_0023_otoshita", "card_0023_burikko", "card_0023_damasareru", "card_0023_karimenkyo", "card_0023_shuukan", "card_0023_kitanai", "card_0023_chirakatteiru", "card_0023_shitsugyouritsu"];

  const ARUN_CURATED_CARDS = [
  {
    "id": "card_0023_shitami",
    "word": "下見",
    "reading": "したみ",
    "category": "授業で習った言葉",
    "meaning": {
      "ja": "下見",
      "en": "preview, preliminary inspection, viewing (property)",
      "zh_TW": "預先查看、勘查、看房",
      "ko": "사전 답사, 미리 보기"
    },
    "example": {
      "ja": "<ruby>結婚式<rt>けっこんしき</rt></ruby>の<ruby>会場<rt>かいじょう</rt></ruby>を<ruby>下見<rt>したみ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きました。",
      "en": "I went to preview the wedding venue.",
      "zh_TW": "去預先查看了婚禮會場。",
      "ko": "결혼식장을 사전 답사하러 갔습니다."
    },
    "related": "したみ（授業の重要表現）"
  },
  {
    "id": "card_0023_suugakusha",
    "word": "数学者",
    "reading": "すうがくしゃ",
    "category": "授業で習った言葉",
    "meaning": {
      "ja": "数学者",
      "en": "mathematician",
      "zh_TW": "數學家",
      "ko": "수학자"
    },
    "example": {
      "ja": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>世界的<rt>せかいてき</rt></ruby>に<ruby>有名<rt>ゆうめい</rt></ruby>な<ruby>数学者<rt>すうがくしゃ</rt></ruby>として<ruby>知<rt>し</rt></ruby>られています。",
      "en": "He is known as a world-famous mathematician.",
      "zh_TW": "他作為世界聞名的數學家而廣為人知。",
      "ko": "그는 세계적으로 유명한 수학자로 알려져 있습니다."
    },
    "related": "すうがくしゃ（授業の重要表現）"
  },
  {
    "id": "card_0023_houritsu",
    "word": "法律",
    "reading": "ほうりつ",
    "category": "授業で習った言葉",
    "meaning": {
      "ja": "法律",
      "en": "law, legislation",
      "zh_TW": "法律",
      "ko": "법률"
    },
    "example": {
      "ja": "<ruby>国民<rt>こくみん</rt></ruby>は<ruby>法律<rt>ほうりつ</rt></ruby>を<ruby>守<rt>まも</rt></ruby>る<ruby>義務<rt>ぎむ</rt></ruby>があります。",
      "en": "Citizens have an obligation to abide by the law.",
      "zh_TW": "國民有遵守法律的義務。",
      "ko": "국민은 법률을 준수할 의무가 있습니다."
    },
    "related": "ほうりつ（授業の重要表現）"
  },
  {
    "id": "card_0023_irairasuru",
    "word": "イライラする",
    "reading": "いらいらする",
    "category": "授業で習った言葉",
    "meaning": {
      "ja": "イライラする",
      "en": "to feel irritated, to be frustrated, to lose patience",
      "zh_TW": "焦躁不安、惱火、心煩",
      "ko": "안달하다, 짜증나다"
    },
    "example": {
      "ja": "<ruby>電車<rt>でんしゃ</rt></ruby>が<ruby>遅<rt>おく</rt></ruby>れていて、だんだんイライラしてきました。",
      "en": "The train was delayed, and I gradually started to get irritated.",
      "zh_TW": "電車延誤了，讓人漸漸感到焦躁惱火。",
      "ko": "전철이 늦어져서 점점 짜증이 나기 시작했습니다."
    },
    "related": "いらいらする（授業の重要表現）"
  },
  {
    "id": "card_0023_koukai",
    "word": "公開",
    "reading": "こうかい",
    "category": "授業で習った言葉",
    "meaning": {
      "ja": "公開",
      "en": "opening to the public, public release, disclosure",
      "zh_TW": "公開、上映、對外開放",
      "ko": "공개"
    },
    "example": {
      "ja": "<ruby>話題<rt>わだい</rt></ruby>の<ruby>新作映画<rt>しんさくえいが</rt></ruby>が<ruby>来週<rt>らいしゅう</rt></ruby>の<ruby>金曜日<rt>きんようび</rt></ruby>に<ruby>公開<rt>こうかい</rt></ruby>されます。",
      "en": "The much-talked-about new movie will be released in theaters next Friday.",
      "zh_TW": "備受熱議的新電影將於下週五上映。",
      "ko": "화제의 신작 영화가 다음 주 금요일에 개봉(공개)됩니다."
    },
    "related": "こうかい（授業の重要表現）"
  },
  {
    "id": "card_0023_hikoukai",
    "word": "非公開",
    "reading": "ひこうかい",
    "category": "授業で習った言葉",
    "meaning": {
      "ja": "非公開",
      "en": "private, closed to the public, undisclosed",
      "zh_TW": "不公開、非公開、私人",
      "ko": "비공개"
    },
    "example": {
      "ja": "プライバシーを<ruby>守<rt>まも</rt></ruby>るために、SNSのアカウントを<ruby>非公開<rt>ひこうかい</rt></ruby>にしています。",
      "en": "To protect my privacy, I keep my social media account set to private.",
      "zh_TW": "為了保護隱私，我把SNS帳號設為不公開。",
      "ko": "사생활을 보호하기 위해 SNS 계정을 비공개로 해 두고 있습니다."
    },
    "related": "ひこうかい（授業の重要表現）"
  },
  {
    "id": "card_0023_okodukai",
    "word": "お小遣い",
    "reading": "おこづかい",
    "category": "授業で習った言葉",
    "meaning": {
      "ja": "お小遣い",
      "en": "pocket money, allowance, spending money",
      "zh_TW": "零用錢",
      "ko": "용돈"
    },
    "example": {
      "ja": "<ruby>毎月<rt>まいつき</rt></ruby>1<ruby>日<rt>ついたち</rt></ruby>に<ruby>親<rt>おや</rt></ruby>からお<ruby>小遣<rt>こづか</rt></ruby>いをもらいます。",
      "en": "I receive an allowance from my parents on the 1st of every month.",
      "zh_TW": "每個月1號我會從父母那裡拿零用錢。",
      "ko": "매월 1일에 부모님께 용돈을 받습니다."
    },
    "related": "おこづかい（授業の重要表現）"
  },
  {
    "id": "card_0023_koukai_regret",
    "word": "後悔",
    "reading": "こうかい",
    "category": "授業で習った言葉",
    "meaning": {
      "ja": "後悔",
      "en": "regret, remorse",
      "zh_TW": "後悔",
      "ko": "후회"
    },
    "example": {
      "ja": "<ruby>若<rt>わか</rt></ruby>い<ruby>時<rt>とき</rt></ruby>にもっと<ruby>勉強<rt>べんきょう</rt></ruby>しておけばよかったと<ruby>後悔<rt>こうかい</rt></ruby>しています。",
      "en": "I regret that I didn't study more when I was younger.",
      "zh_TW": "我很後悔年輕時沒有多用功讀書。",
      "ko": "젊었을 때 좀 더 공부해 둘 걸 그랬다고 후회하고 있습니다."
    },
    "related": "こうかい（授業の重要表現）"
  },
  {
    "id": "card_0023_kuchipaku",
    "word": "口パク",
    "reading": "くちぱく",
    "category": "授業で習った言葉",
    "meaning": {
      "ja": "口パク",
      "en": "lip-syncing, mouthing words silently",
      "zh_TW": "對嘴、假唱、動嘴型不出聲",
      "ko": "립싱크, 벙긋거림"
    },
    "example": {
      "ja": "<ruby>彼<rt>かれ</rt></ruby>はライブコンサートで<ruby>口<rt>くち</rt></ruby>パクをしていたと<ruby>批判<rt>ひはん</rt></ruby>された。",
      "en": "He was criticized for lip-syncing at the live concert.",
      "zh_TW": "他因為在現場演唱會上對嘴假唱而受到批評。",
      "ko": "그는 라이브 콘서트에서 립싱크를 했다고 비판을 받았다."
    },
    "related": "くちぱく（授業の重要表現）"
  },
  {
    "id": "card_0023_nokawarini",
    "word": "〜の代わりに",
    "reading": "〜のかわりに",
    "category": "授業で習った言葉",
    "meaning": {
      "ja": "〜の代わりに",
      "en": "instead of..., in place of..., on behalf of...",
      "zh_TW": "代替……、作為……的交換",
      "ko": "~대신에"
    },
    "example": {
      "ja": "<ruby>体調<rt>たいちょう</rt></ruby>を<ruby>崩<rt>くず</rt></ruby>した<ruby>部長<rt>ぶちょう</rt></ruby>の<ruby>代<rt>か</rt></ruby>わりに、<ruby>私<rt>わたし</rt></ruby>が<ruby>会議<rt>かいぎ</rt></ruby>に<ruby>出席<rt>しゅっせき</rt></ruby>しました。",
      "en": "In place of the department manager who fell ill, I attended the meeting.",
      "zh_TW": "代替身體不適的部長，我出席了會議。",
      "ko": "컨디션이 안 좋아진 부장님 대신에 제가 회의에 참석했습니다."
    },
    "related": "〜のかわりに（授業の重要表現）"
  },
  {
    "id": "card_0023_manten",
    "word": "満点",
    "reading": "まんてん",
    "category": "授業で習った言葉",
    "meaning": {
      "ja": "満点",
      "en": "perfect score, full marks",
      "zh_TW": "滿分",
      "ko": "만점"
    },
    "example": {
      "ja": "<ruby>数学<rt>すうがく</rt></ruby>のテストで<ruby>満点<rt>まんてん</rt></ruby>を<ruby>取<rt>と</rt></ruby>ることができた。",
      "en": "I was able to get a perfect score on the math test.",
      "zh_TW": "我在數學考試中拿到了滿分。",
      "ko": "수학 시험에서 만점을 받을 수 있었다."
    },
    "related": "まんてん（授業の重要表現）"
  },
  {
    "id": "card_0023_tensai",
    "word": "天才",
    "reading": "てんさい",
    "category": "授業で習った言葉",
    "meaning": {
      "ja": "天才",
      "en": "genius, prodigy",
      "zh_TW": "天才",
      "ko": "천재"
    },
    "example": {
      "ja": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>幼<rt>おさな</rt></ruby>い<ruby>頃<rt>ころ</rt></ruby>からピアノの<ruby>天才<rt>てんさい</rt></ruby>として<ruby>知<rt>し</rt></ruby>られていた。",
      "en": "He has been known as a piano prodigy since he was young.",
      "zh_TW": "他從小就被稱為鋼琴天才。",
      "ko": "그는 어린 시절부터 피아노 천재로 알려져 있었다."
    },
    "related": "てんさい（授業の重要表現）"
  },
  {
    "id": "card_0023_souko",
    "word": "倉庫",
    "reading": "そうこ",
    "category": "授業で習った言葉",
    "meaning": {
      "ja": "倉庫",
      "en": "warehouse, storehouse",
      "zh_TW": "倉庫",
      "ko": "창고"
    },
    "example": {
      "ja": "<ruby>使<rt>つか</rt></ruby>わなくなった<ruby>家具<rt>かぐ</rt></ruby>や<ruby>季節<rt>きせつ</rt></ruby>の<ruby>道具<rt>どうぐ</rt></ruby>を<ruby>倉庫<rt>そうこ</rt></ruby>に<ruby>片付<rt>かたづ</rt></ruby>けた。",
      "en": "I stored unused furniture and seasonal tools away in the storage room.",
      "zh_TW": "把不再使用的家具和季節性用具整理收進了倉庫。",
      "ko": "사용하지 않게 된 가구와 계절 용품을 창고에 정리했다."
    },
    "related": "そうこ（授業の重要表現）"
  },
  {
    "id": "card_0023_otoshita",
    "word": "落とした",
    "reading": "おとした",
    "category": "授業で習った言葉",
    "meaning": {
      "ja": "落とした",
      "en": "dropped, lost",
      "zh_TW": "掉落、弄丟了",
      "ko": "떨어뜨렸다, 잃어버렸다"
    },
    "example": {
      "ja": "<ruby>歩<rt>ある</rt></ruby>いている<ruby>途中<rt>とちゅう</rt></ruby>で、ポケットから<ruby>財布<rt>さいふ</rt></ruby>を<ruby>落<rt>お</rt></ruby>としてしまった。",
      "en": "While walking, I accidentally dropped my wallet out of my pocket.",
      "zh_TW": "在走路途中，錢包不小心從口袋裡掉出來了。",
      "ko": "걷는 도중에 주머니에서 지갑을 떨어뜨려 버렸다."
    },
    "related": "おとした（授業の重要表現）"
  },
  {
    "id": "card_0023_burikko",
    "word": "ぶりっ子",
    "reading": "ぶりっこ",
    "category": "授業で習った言葉",
    "meaning": {
      "ja": "ぶりっ子",
      "en": "girl playing dumb/cute, feigning innocence",
      "zh_TW": "裝可愛的女生、做作女",
      "ko": "귀여운 척하는 사람, 내숭쟁이"
    },
    "example": {
      "ja": "<ruby>彼女<rt>かのじょ</rt></ruby>は<ruby>男性<rt>だんせい</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>に<ruby>行<rt>い</rt></ruby>くと、<ruby>急<rt>きゅう</rt></ruby>にぶりっ<ruby>子<rt>こ</rt></ruby>になる。",
      "en": "Whenever she is around men, she suddenly acts all cute and helpless.",
      "zh_TW": "她一到了男生面前，就會突然裝起可愛來。",
      "ko": "그녀는 남자 앞에 가면 갑자기 애교를 부린다."
    },
    "related": "ぶりっこ（授業の重要表現）"
  },
  {
    "id": "card_0023_damasareru",
    "word": "騙される",
    "reading": "だまされる",
    "category": "授業で習った言葉",
    "meaning": {
      "ja": "騙される",
      "en": "to be deceived, to be tricked",
      "zh_TW": "被騙、受騙",
      "ko": "속다, 사기당하다"
    },
    "example": {
      "ja": "<ruby>甘<rt>あま</rt></ruby>い<ruby>投資話<rt>とうしばなし</rt></ruby>に<ruby>騙<rt>だま</rt></ruby>されて、<ruby>大金<rt>たいきん</rt></ruby>を<ruby>失<rt>うしな</rt></ruby>ってしまった。",
      "en": "I was deceived by an enticing investment story and lost a large sum of money.",
      "zh_TW": "被誘人的投資話術所騙，損失了一大筆錢。",
      "ko": "달콤한 투자 권유에 속아 큰돈을 잃어버렸다."
    },
    "related": "だまされる（授業の重要表現）"
  },
  {
    "id": "card_0023_karimenkyo",
    "word": "仮免許",
    "reading": "かりめんきょ",
    "category": "授業で習った言葉",
    "meaning": {
      "ja": "仮免許",
      "en": "learner's permit, provisional driving license",
      "zh_TW": "學習駕照、臨時駕照",
      "ko": "임시 운전면허, 연습 면허"
    },
    "example": {
      "ja": "<ruby>仮免許<rt>かりめんきょ</rt></ruby>の<ruby>試験<rt>しけん</rt></ruby>に<ruby>一発<rt>いっぱつ</rt></ruby>で<ruby>合格<rt>ごうかく</rt></ruby>して、<ruby>明日<rt>あした</rt></ruby>から<ruby>路上教習<rt>ろじょうきょうしゅう</rt></ruby>が<ruby>始<rt>はじ</rt></ruby>まる。",
      "en": "I passed the learner's permit test on my first try, and on-road driving lessons start tomorrow.",
      "zh_TW": "我一次就考過了臨時駕照考試，明天開始上路練習。",
      "ko": "연습 면허 시험에 한 번에 합격해서 내일부터 도로 주행 교육이 시작된다."
    },
    "related": "かりめんきょ（授業の重要表現）"
  },
  {
    "id": "card_0023_shuukan",
    "word": "習慣",
    "reading": "しゅうかん",
    "category": "授業で習った言葉",
    "meaning": {
      "ja": "習慣",
      "en": "habit, custom",
      "zh_TW": "習慣",
      "ko": "습관"
    },
    "example": {
      "ja": "<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>起<rt>お</rt></ruby>きたら<ruby>白湯<rt>さゆ</rt></ruby>を<ruby>一杯<rt>いっぱい</rt></ruby><ruby>飲<rt>の</rt></ruby>むのが<ruby>私<rt>わたし</rt></ruby>の<ruby>習慣<rt>しゅうかん</rt></ruby>だ。",
      "en": "Drinking a cup of warm water every morning upon waking up is my habit.",
      "zh_TW": "每天早上起床後喝一杯溫開水是我的習慣。",
      "ko": "매일 아침 일어나면 따뜻한 물 한 잔을 마시는 것이 나의 습관이다."
    },
    "related": "しゅうかん（授業の重要表現）"
  },
  {
    "id": "card_0023_kitanai",
    "word": "汚い",
    "reading": "きたない",
    "category": "授業で習った言葉",
    "meaning": {
      "ja": "汚い",
      "en": "dirty, filthy, underhanded",
      "zh_TW": "髒的、不乾淨的、骯髒卑鄙的",
      "ko": "더럽다, 지저분하다, 치사하다"
    },
    "example": {
      "ja": "<ruby>泥遊<rt>どろあそ</rt></ruby>びをしたので、<ruby>服<rt>ふく</rt></ruby>も<ruby>手<rt>て</rt></ruby>も<ruby>真<rt>ま</rt></ruby>っ<ruby>黒<rt>くろ</rt></ruby>に<ruby>汚<rt>きたな</rt></ruby>い。",
      "en": "Since I played in the mud, both my clothes and hands are pitch-black dirty.",
      "zh_TW": "因為玩了泥巴，衣服和手都髒得黑漆漆的。",
      "ko": "흙장난을 해서 옷도 손도 새까맣게 더럽다."
    },
    "related": "きたない（授業の重要表現）"
  },
  {
    "id": "card_0023_chirakatteiru",
    "word": "散らかっている",
    "reading": "ちらかっている",
    "category": "授業で習った言葉",
    "meaning": {
      "ja": "散らかっている",
      "en": "messy, cluttered, scattered around",
      "zh_TW": "凌亂、散落一地",
      "ko": "어질러져 있다, 널려 있다"
    },
    "example": {
      "ja": "<ruby>部屋中<rt>へやじゅう</rt></ruby>に<ruby>服<rt>ふく</rt></ruby>や<ruby>本<rt>ほん</rt></ruby>が<ruby>散<rt>ち</rt></ruby>らかっていて、<ruby>足<rt>あし</rt></ruby>の<ruby>踏<rt>ふ</rt></ruby>み<ruby>場<rt>ば</rt></ruby>もない。",
      "en": "Clothes and books are scattered all over the room, leaving nowhere even to step.",
      "zh_TW": "房間裡到處散落著衣服和書本，連落腳的地方都沒有。",
      "ko": "방 안에 옷과 책이 널려 있어서 발 디딜 틈도 없다."
    },
    "related": "ちらかっている（授業の重要表現）"
  },
  {
    "id": "card_0023_shitsugyouritsu",
    "word": "失業率",
    "reading": "しつぎょうりつ",
    "category": "授業で習った言葉",
    "meaning": {
      "ja": "失業率",
      "en": "unemployment rate",
      "zh_TW": "失業率",
      "ko": "실업률"
    },
    "example": {
      "ja": "<ruby>景気<rt>けいき</rt></ruby>の<ruby>悪化<rt>あっか</rt></ruby>に<ruby>伴<rt>ともな</rt></ruby>い、<ruby>国内<rt>こくない</rt></ruby>の<ruby>完全失業率<rt>かんぜんしつぎょうりつ</rt></ruby>が<ruby>上昇<rt>じょうしょう</rt></ruby>した。",
      "en": "Accompanied by the economic downturn, the domestic unemployment rate rose.",
      "zh_TW": "隨著景氣惡化，國內的完全失業率上升了。",
      "ko": "경기 악화에 따라 국내의 완전 실업률이 상승했다."
    },
    "related": "しつぎょうりつ（授業の重要表現）"
  }
];



  const MIDORI_NEW_WORDS = new Set([
    '夜市', '自由', '楽しむ', '謳歌する',
    '攻撃', '通知', '失礼', '舌打ち',
    '数えきれないほど', '嫌な思いをする', '駅員', '態度が悪い',
    '影響', '端正な', '顔立ち', '相談に乗る',
    '〜のふりをする', '偽物', '本物', '詐欺', '悔しい', 'キリがない', '腹が立つ', 'ムカつく', '世話をする', '修行', '向き合う'
  ]);

  // Validator to determine if an ID belongs to a custom card (not seed card or class word)
  function isCustomCardId(id) {
    return typeof id === 'string' && !id.startsWith('class_word_') && !/^card_\d{4}$/.test(id);
  }

  // Automatic validator to detect any corrupted / reversed dialect cards
  const isCorruptedCard = (c) => {
    if (!c) return false;
    const w = (c.word || '').trim();
    const r = (c.reading || '').trim();
    const id = c.id || '';
    if (typeof ELIIE_NEW_CARD_IDS !== 'undefined' && ELIIE_NEW_CARD_IDS.includes(id)) return false;
    const exJa = (c.example && c.example.ja) ? c.example.ja : '';
    if (w.includes('面模仔') || r.includes('bīn') || exJa.includes('bīn-bôo-á') || exJa.includes('伊的面模仔')) return true;
    if (exJa.includes('他長著端正清秀的五官') || exJa.includes('かれはたんせいなかおかたち')) return true;
    if (/[āēīōūáéíóúàèìòùâêîôûǎěǐǒǔ]/.test(w) || /[āēīōūáéíóúàèìòùâêîôûǎěǐǒǔ]/.test(r)) return true;
    // Korean Hangul corruption check: word or reading must NOT be Hangul
    if (/[\uAC00-\uD7AF]/.test(w) || /[\uAC00-\uD7AF]/.test(r)) return true;
    // If meaning.ja is Korean Hangul, it is corrupted
    if (c.meaning && typeof c.meaning.ja === 'string' && /[\uAC00-\uD7AF]/.test(c.meaning.ja)) return true;
    return false;
  };

  let isSpeaking = false;
  let speechSequenceTimer = null;

  function stopJapaneseSpeech() {
    if (speechSequenceTimer) {
      clearTimeout(speechSequenceTimer);
      speechSequenceTimer = null;
    }
    if (autoAudioTimer) {
      clearTimeout(autoAudioTimer);
      autoAudioTimer = null;
    }
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      if (window.speechSynthesis.paused) {
        window.speechSynthesis.resume();
      }
    }
    window._activeUtterance = null;
    isSpeaking = false;
  }

  // Accepts either a string OR a card object { word, reading, example }
  // When given a card, prefers card.reading (e.g. にじゅうかかく) so kanji is read 100% accurately!
  function speakJapanese(target, onEnd = null) {
    if (!('speechSynthesis' in window)) {
      if (onEnd) onEnd();
      return;
    }
    try {
      if (window.speechSynthesis.paused) {
        window.speechSynthesis.resume();
      }
    } catch (e) {}
    stopJapaneseSpeech();

    let textToSpeak = '';
    if (target && typeof target === 'object') {
      // If object has reading (hiragana), unwrap any brackets and use it
      let r = (target.reading || '').trim().replace(/^[（\(\[【](.*?)[）\)\]】]$/, '$1');
      r = r.split(/[/／・]/)[0].trim();
      textToSpeak = r || target.word || '';
    } else {
      textToSpeak = String(target || '');
    }

    let cleanText = cleanJapaneseForSpeech(textToSpeak);
    // Safety fallback: if reading was somehow stripped to empty, fallback to word directly!
    if (!cleanText && target && typeof target === 'object' && target.word) {
      cleanText = cleanJapaneseForSpeech(target.word);
    }
    if (!cleanText) {
      if (onEnd) onEnd();
      return;
    }

    const utterance = new SpeechSynthesisUtterance(cleanText);
    utterance.lang = 'ja-JP';
    utterance.rate = 0.9; // natural conversational pacing for Japanese learning

    // Pick Google Japanese TTS voice first if available, then Kyoko / Otoya / Siri or ja-JP voice
    const voices = window.speechSynthesis.getVoices();
    const jaVoice = voices.find(v => (v.lang === 'ja-JP' || v.lang === 'ja_JP') && v.name.includes('Google')) ||
                    voices.find(v => (v.lang === 'ja-JP' || v.lang === 'ja_JP') && (v.name.includes('Kyoko') || v.name.includes('Otoya') || v.name.includes('Siri') || v.name.includes('Nanami') || v.name.includes('Keita'))) ||
                    voices.find(v => v.lang === 'ja-JP' || v.lang === 'ja_JP');
    if (jaVoice) {
      utterance.voice = jaVoice;
    }

    utterance.onstart = () => {
      isSpeaking = true;
    };
    utterance.onend = () => {
      isSpeaking = false;
      window._activeUtterance = null;
      if (onEnd) onEnd();
    };
    utterance.onerror = () => {
      isSpeaking = false;
      window._activeUtterance = null;
      if (onEnd) onEnd();
    };

    isSpeaking = true;
    window._activeUtterance = utterance;
    window.speechSynthesis.speak(utterance);
  }

  // 連続再生（単語を発音後、例文を続けて再生）
  function speakJapaneseSequence(firstTarget, secondTarget) {
    if (!firstTarget && !secondTarget) return;
    if (!secondTarget) {
      speakJapanese(firstTarget);
      return;
    }
    if (!firstTarget) {
      speakJapanese(secondTarget);
      return;
    }

    stopJapaneseSpeech();

    speakJapanese(firstTarget, () => {
      // 単語読み上げ後に少し間を空けて例文を発話
      speechSequenceTimer = setTimeout(() => {
        speechSequenceTimer = null;
        // カードが途中で閉じられたり切り替わっていないか確認しつつ発音
        if (!('speechSynthesis' in window)) return;
        if (window.speechSynthesis.paused) {
          window.speechSynthesis.resume();
        }
        let textToSpeak = '';
        if (typeof secondTarget === 'object') {
          const r = (secondTarget.reading || '').split(/[/／・]/)[0].trim();
          textToSpeak = r || secondTarget.word || '';
        } else {
          textToSpeak = String(secondTarget || '');
        }
        const cleanText = cleanJapaneseForSpeech(textToSpeak);
        if (!cleanText) return;

        const utterance = new SpeechSynthesisUtterance(cleanText);
        utterance.lang = 'ja-JP';
        utterance.rate = 0.9;
        const voices = window.speechSynthesis.getVoices();
        const jaVoice = voices.find(v => (v.lang === 'ja-JP' || v.lang === 'ja_JP') && v.name.includes('Google')) ||
                        voices.find(v => (v.lang === 'ja-JP' || v.lang === 'ja_JP') && (v.name.includes('Kyoko') || v.name.includes('Otoya') || v.name.includes('Siri') || v.name.includes('Nanami') || v.name.includes('Keita'))) ||
                        voices.find(v => v.lang === 'ja-JP' || v.lang === 'ja_JP');
        if (jaVoice) utterance.voice = jaVoice;

        utterance.onstart = () => {
          isSpeaking = true;
        };
        utterance.onend = () => {
          isSpeaking = false;
          window._activeUtterance = null;
        };
        utterance.onerror = () => {
          isSpeaking = false;
          window._activeUtterance = null;
        };

        isSpeaking = true;
        window._activeUtterance = utterance;
        window.speechSynthesis.speak(utterance);
      }, 350);
    });
  }

  // 音声ボタンクリック時に再生中なら即座に停止（トグル動作）するヘルパー
  function toggleJapaneseSpeech(target) {
    if (isSpeaking || ('speechSynthesis' in window && window.speechSynthesis.speaking)) {
      stopJapaneseSpeech();
      return;
    }
    speakJapanese(target);
  }

  // Helper to find a student's native translation when card meaning is English-only
  function getFallbackMeaningForWord(word, lang) {
    if (!word || !lang || lang === 'en' || lang === 'ja') return '';
    // 1. Check INITIAL_VOCAB_DATA
    if (window.INITIAL_VOCAB_DATA && Array.isArray(window.INITIAL_VOCAB_DATA)) {
      const found = window.INITIAL_VOCAB_DATA.find(c => c.word === word);
      if (found && found.meaning && found.meaning[lang] && found.meaning[lang] !== found.meaning.en) {
        return found.meaning[lang];
      }
    }
    // 2. Check CLASS_VOCAB_DATA
    if (window.CLASS_VOCAB_DATA && Array.isArray(window.CLASS_VOCAB_DATA)) {
      const found = window.CLASS_VOCAB_DATA.find(c => c.word === word);
      if (found && found.meaning && found.meaning[lang] && found.meaning[lang] !== found.meaning.en) {
        return found.meaning[lang];
      }
    }
    // 3. Check DICT_DATA (has zh and fr)
    if (window.DICT_DATA && Array.isArray(window.DICT_DATA)) {
      const entry = window.DICT_DATA.find(d => d.w === word);
      if (entry) {
        if ((lang === 'zh_TW' || lang === 'zh_CN' || lang === 'zh_HK') && entry.zh && entry.zh.length > 0) {
          return entry.zh.join(', ');
        }
        if (lang === 'fr' && entry.fr && entry.fr.length > 0) {
          return entry.fr.join(', ');
        }
      }
    }
    return '';
  }

  // --- Bilingual Translation Formatters (必ず母国語 & 英語) ---
  function getBilingualMeaning(meaningObj, lang, cardWord) {
    if (!meaningObj) return '—';
    const targetLang = lang || currentLang;
    let nativeMeaning = (meaningObj[targetLang]) || '';
    let enMeaning = meaningObj.en || '';

    // 英語訳が空の場合、辞書・JLPTマスターから自動補完
    if (!enMeaning && cardWord) {
      const cleanW = (cardWord || '').replace(/<[^>]+>/g, '').trim();
      const dictMatch = (window.DICT_DATA || []).find(d => d.w === cleanW) || (window.JLPT_VOCAB_ALL || []).find(d => d.word === cleanW || d.w === cleanW);
      if (dictMatch) {
        if (Array.isArray(dictMatch.m) && dictMatch.m.length) {
          enMeaning = dictMatch.m.slice(0, 2).join(', ');
        } else if (Array.isArray(dictMatch.meanings) && dictMatch.meanings.length) {
          enMeaning = dictMatch.meanings.slice(0, 2).join(', ');
        }
      }
    }

    // If native meaning is missing or identical to English, attempt fallback dictionary lookup
    if ((!nativeMeaning || nativeMeaning === enMeaning) && targetLang !== 'en' && targetLang !== 'ja') {
      const w = cardWord || meaningObj.ja;
      if (w) {
        const fb = getFallbackMeaningForWord(w, targetLang);
        if (fb) nativeMeaning = fb;
      }
    }

    if (targetLang === 'en') {
      return enMeaning || nativeMeaning || Object.values(meaningObj)[0] || '—';
    }
    if (targetLang === 'ja') {
      return nativeMeaning || enMeaning || Object.values(meaningObj)[0] || '—';
    }
    // For foreign language learners (zh_TW, ko, fr, zh_HK, zh_CN, etc.)
    // 必ず母国語と英語を併記！(すでに括弧英語が含まれている場合は二重付与を防ぐ)
    if (nativeMeaning) {
      if (/\([A-Za-z\s,/-]+\)/.test(nativeMeaning)) {
        return nativeMeaning;
      }
      if (enMeaning && nativeMeaning !== enMeaning) {
        return `${nativeMeaning} (${enMeaning})`;
      }
    }
    return nativeMeaning || enMeaning || Object.values(meaningObj)[0] || '—';
  }

  function getBilingualExampleTrans(exampleObj, lang) {
    if (!exampleObj) return '';
    const targetLang = lang || currentLang;
    const nativeEx = (exampleObj[targetLang]) || '';
    const enEx = exampleObj.en || '';

    if (targetLang === 'en') {
      return enEx || nativeEx || '';
    }
    if (targetLang === 'ja') {
      return nativeEx || enEx || '';
    }
    if (nativeEx && enEx && nativeEx !== enEx) {
      return `${nativeEx} <span class="text-slate-400 font-normal">(${enEx})</span>`;
    }
    return nativeEx || enEx || '';
  }

  // --- Toast Notification ---
  function showToast(msg) {
    const toast = document.getElementById('toastNotification');
    if (!toast) return;
    toast.textContent = msg;
    toast.classList.remove('opacity-0', 'pointer-events-none');
    toast.classList.add('opacity-100');
    setTimeout(() => {
      toast.classList.remove('opacity-100');
      toast.classList.add('opacity-0', 'pointer-events-none');
    }, 2000);
  }

  // --- Kana / Romaji Normalizer for Search ---
  function toHiragana(str) {
    if (!str) return '';
    // Convert Full-width Romaji/Alphabet to Half-width
    let s = str.replace(/[Ａ-Ｚａ-ｚ０-９]/g, ch => String.fromCharCode(ch.charCodeAt(0) - 0xFEE0)).toLowerCase();
    // Convert Katakana to Hiragana (30A1-30F6 -> 3041-3096)
    s = s.replace(/[\u30a1-\u30f6]/g, ch => String.fromCharCode(ch.charCodeAt(0) - 0x60));
    return s;
  }

  // --- UI Localization (日本語モード ⇄ 英語モード) ---
  // When 'ja' is selected, UI chrome adapts to Japanese. For all other languages, English is preserved.
  function applyUiLanguage(lang) {
    const isJa = (lang === 'ja');

    // 1. Top Header & Search
    const searchPlaceholders = {
      ja: '辞書・単語検索...',
      en: 'Search words...',
      zh_TW: '搜尋單字...',
      zh_CN: '搜索单词...',
      ko: '단어 검색...',
      zh_HK: '搜尋單字...',
      fr: 'Chercher un mot...'
    };
    const topSearch = document.getElementById('globalTopSearchInput');
    if (topSearch) {
      topSearch.placeholder = searchPlaceholders[lang] || 'Search words...';
    }

    // 2. Navigation Tabs
    const navStudyLabel = document.getElementById('navStudyLabel');
    if (navStudyLabel) navStudyLabel.textContent = isJa ? 'フラッシュカード' : 'Flashcards';
    const navQuizLabel = document.getElementById('navQuizLabel');
    if (navQuizLabel) navQuizLabel.textContent = isJa ? 'Quiz / Test' : 'Quiz / Test';
    const navMylistLabel = document.getElementById('navMylistLabel');
    if (navMylistLabel) navMylistLabel.textContent = isJa ? 'マイリスト' : 'My List';
    const navJlptLabel = document.getElementById('navJlptLabel');
    if (navJlptLabel) navJlptLabel.textContent = isJa ? 'JLPT' : 'JLPT';
    const drawerJlptLabel = document.getElementById('drawerJlptLabel');
    if (drawerJlptLabel) drawerJlptLabel.textContent = isJa ? 'JLPT 単語リスト' : 'JLPT Vocab List';

    // 3. Left Sidebar Curriculum Header
    const sideCurricTitle = document.getElementById('sidebarCurriculumTitle');
    if (sideCurricTitle) sideCurricTitle.textContent = isJa ? 'カリキュラム一覧' : 'Curriculum';
    const sideCurricSub = document.getElementById('sidebarCurriculumSub');
    if (sideCurricSub) sideCurricSub.textContent = isJa ? '全4ステージ / 44単元' : '4 Stages / 44 Units';
    const btnShuffleSideLabel = document.getElementById('btnShuffleAllSidebarLabel');
    if (btnShuffleSideLabel) btnShuffleSideLabel.textContent = isJa ? '全シャッフル' : 'Shuffle All';

    // 4. Deck Controls & Reverse Button
    const filterAll = document.getElementById('filterAllDeck');
    if (filterAll) filterAll.textContent = isJa ? '全員共有' : 'Shared Deck';
    const filterMy = document.getElementById('filterMyDeck');
    if (filterMy) filterMy.textContent = isJa ? '生徒専用' : 'My Deck';

    const reverseLabel = document.getElementById('reverseModeLabel');
    if (reverseLabel) {
      if (isJa) {
        reverseLabel.textContent = isReverseMode ? '表面: 母国語' : '表面: 日本語';
      } else {
        reverseLabel.textContent = isReverseMode ? 'Front: Native' : 'Front: Japanese';
      }
    }

    // 5. Folder & Unit Panels
    const folderOverTitle = document.getElementById('folderOverviewTitle');
    if (folderOverTitle) folderOverTitle.textContent = isJa ? 'フォルダを選択' : 'Select Folder';
    const btnShuffleAllLabel = document.getElementById('btnShuffleAllLabel');
    if (btnShuffleAllLabel) btnShuffleAllLabel.textContent = isJa ? '全単元シャッフル' : 'Shuffle All Units';

    const btnBackToFoldersLabel = document.getElementById('btnBackToFoldersLabel');
    if (btnBackToFoldersLabel) btnBackToFoldersLabel.textContent = isJa ? 'フォルダ一覧に戻る' : 'Back to Folders';
    const unitSelectHint = document.getElementById('unitSelectHint');
    if (unitSelectHint) unitSelectHint.textContent = isJa ? '学習する単元を選択してください' : 'Select a unit to study';
    const btnStudyFolderLabel = document.getElementById('btnStudyEntireFolderLabel');
    if (btnStudyFolderLabel) btnStudyFolderLabel.textContent = isJa ? '全学習' : 'Study All';
    const btnTestFolderLabel = document.getElementById('btnTestEntireFolderLabel');
    if (btnTestFolderLabel) btnTestFolderLabel.textContent = isJa ? 'テスト' : 'Test';

    // 6. Active Study Header Buttons
    const btnTestCurLabel = document.getElementById('btnTestCurrentLabel');
    if (btnTestCurLabel) btnTestCurLabel.textContent = isJa ? 'テスト' : 'Test';
    const btnShuffleCurLabel = document.getElementById('btnShuffleCurrentLabel');
    if (btnShuffleCurLabel) btnShuffleCurLabel.textContent = isJa ? 'シャッフル' : 'Shuffle';

    // 7. Flashcard Face Prompts
    const frontSubtext = document.getElementById('frontSubtext');
    if (frontSubtext) frontSubtext.textContent = isJa ? 'タップして答えを表示' : 'Tap to show answer';
    const frontFlipPrompt = document.getElementById('frontFlipPrompt');
    if (frontFlipPrompt) frontFlipPrompt.textContent = isJa ? 'タップで裏面' : 'Tap to flip';
    const backMeaningLabel = document.getElementById('backMeaningLabel');
    if (backMeaningLabel) backMeaningLabel.textContent = isJa ? '意味・翻訳' : 'Meaning / Translation';
    const backExampleLabel = document.getElementById('backExampleLabel');
    if (backExampleLabel) backExampleLabel.textContent = isJa ? '例文・会話' : 'Example';
    const exampleWordChipsLabel = document.getElementById('exampleWordChipsLabel');
    if (exampleWordChipsLabel) exampleWordChipsLabel.textContent = isJa ? '単語辞書:' : 'Dictionary:';
    const backRelatedLabel = document.getElementById('backRelatedLabel');
    if (backRelatedLabel) backRelatedLabel.textContent = isJa ? '関連語・活用形' : 'Related / Conjugations';
    const backFlipPrompt = document.getElementById('backFlipPrompt');
    if (backFlipPrompt) backFlipPrompt.textContent = isJa ? 'タップして表面に戻る' : 'Tap to flip back';

    // 8. Flashcard Bottom Navigation
    const btnPrevLabel = document.getElementById('btnPrevLabel');
    if (btnPrevLabel) btnPrevLabel.textContent = isJa ? '前へ' : 'Prev';
    const btnMarkReviewLabel = document.getElementById('btnMarkReviewLabel');
    if (btnMarkReviewLabel) btnMarkReviewLabel.textContent = isJa ? 'もう一度！' : 'Again / Review';
    const btnMarkKnownLabel = document.getElementById('btnMarkKnownLabel');
    if (btnMarkKnownLabel) btnMarkKnownLabel.textContent = isJa ? '覚えた！' : 'Learned!';
    const btnNextLabel = document.getElementById('btnNextLabel');
    if (btnNextLabel) btnNextLabel.textContent = isJa ? '次へ' : 'Next';

    // 9. Quiz View
    const quizBadgeTitle = document.getElementById('quizBadgeTitle');
    if (quizBadgeTitle) {
      if (currentQuizMode === 'test') {
        quizBadgeTitle.textContent = isJa ? '実践テスト' : 'Practice Test';
      } else {
        quizBadgeTitle.textContent = isJa ? '単語クイズ' : 'Review Quiz';
      }
    }
    const modeQuizLabel = document.getElementById('modeQuizLabel');
    if (modeQuizLabel) modeQuizLabel.textContent = isJa ? '単語クイズ' : 'Word Quiz';
    const modeTestLabel = document.getElementById('modeTestLabel');
    if (modeTestLabel) modeTestLabel.textContent = isJa ? '実践テスト' : 'Practice Test';
    const quizScopeLabel = document.getElementById('quizScopeLabel');
    if (quizScopeLabel) quizScopeLabel.textContent = isJa ? '出題範囲を選択:' : 'Select Quiz Range:';
    const btnQuizScopeCur = document.getElementById('btnQuizScopeCurrent');
    if (btnQuizScopeCur) btnQuizScopeCur.textContent = isJa ? '現在の単元' : 'Unit / Deck';
    const btnQuizScopeMy = document.getElementById('btnQuizScopeMylist');
    if (btnQuizScopeMy) btnQuizScopeMy.textContent = isJa ? '⭐ マイリスト' : '⭐ My List';
    const btnQuizScopeAl = document.getElementById('btnQuizScopeAll');
    if (btnQuizScopeAl) btnQuizScopeAl.textContent = isJa ? '全シャッフル' : 'Shuffle All';
    const quizQuestionPrompt = document.getElementById('quizQuestionPrompt');
    if (quizQuestionPrompt) quizQuestionPrompt.textContent = isJa ? '一致する日本語の単語を選んでください' : 'Select the matching Japanese word';
    const btnQuizNext = document.getElementById('btnQuizNext');
    if (btnQuizNext) btnQuizNext.textContent = isJa ? '次の問題へ' : 'Next Question';

    // 10. Mylist View
    const mylistHeaderTitle = document.getElementById('mylistHeaderTitle');
    if (mylistHeaderTitle) {
      if (lang === 'ja') mylistHeaderTitle.textContent = 'マイリスト';
      else if (lang === 'zh_TW' || lang === 'zh_HK') mylistHeaderTitle.textContent = '我的清單';
      else if (lang === 'zh_CN') mylistHeaderTitle.textContent = '我的清单';
      else if (lang === 'ko') mylistHeaderTitle.textContent = '마이 리스트';
      else if (lang === 'fr') mylistHeaderTitle.textContent = 'Ma liste';
      else mylistHeaderTitle.textContent = 'My List';
    }
    const btnToggleFoldersLabel = document.getElementById('btnToggleMylistFoldersLabel');
    if (btnToggleFoldersLabel) {
      if (lang === 'ja') btnToggleFoldersLabel.textContent = 'フォルダ';
      else if (lang === 'zh_TW' || lang === 'zh_HK') btnToggleFoldersLabel.textContent = '資料夾';
      else if (lang === 'zh_CN') btnToggleFoldersLabel.textContent = '文件夹';
      else if (lang === 'ko') btnToggleFoldersLabel.textContent = '폴더';
      else if (lang === 'fr') btnToggleFoldersLabel.textContent = 'Dossiers';
      else btnToggleFoldersLabel.textContent = 'Folders';
    }
    const mylistFolderSectionTitle = document.getElementById('mylistFolderSectionTitle');
    if (mylistFolderSectionTitle) {
      if (lang === 'ja') mylistFolderSectionTitle.textContent = '📁 フォルダを選択';
      else if (lang === 'zh_TW' || lang === 'zh_HK') mylistFolderSectionTitle.textContent = '📁 選擇資料夾';
      else if (lang === 'zh_CN') mylistFolderSectionTitle.textContent = '📁 选择文件夹';
      else if (lang === 'ko') mylistFolderSectionTitle.textContent = '📁 폴더 선택';
      else if (lang === 'fr') mylistFolderSectionTitle.textContent = '📁 Choisir un dossier';
      else mylistFolderSectionTitle.textContent = '📁 Select Folder';
    }
    const btnCreateMylistLabel = document.getElementById('btnCreateMylistFolderLabel');
    if (btnCreateMylistLabel) {
      if (lang === 'ja') btnCreateMylistLabel.textContent = '+ 新規フォルダ';
      else if (lang === 'zh_TW' || lang === 'zh_HK') btnCreateMylistLabel.textContent = '+ 新增資料夾';
      else if (lang === 'zh_CN') btnCreateMylistLabel.textContent = '+ 新建文件夹';
      else if (lang === 'ko') btnCreateMylistLabel.textContent = '+ 새 폴더';
      else if (lang === 'fr') btnCreateMylistLabel.textContent = '+ Nouveau dossier';
      else btnCreateMylistLabel.textContent = '+ New Folder';
    }
    const btnStudyMylist = document.getElementById('btnStudyMylist');
    const btnStudyMylistLabel = document.getElementById('btnStudyMylistLabel');
    if (btnStudyMylistLabel) {
      let labelText = '練習カード';
      let titleText = '練習カードで学習する';
      if (lang === 'ja') {
        labelText = '練習カード';
        titleText = '練習カードで学習する';
      } else if (lang === 'zh_TW' || lang === 'zh_HK') {
        labelText = '練習卡片';
        titleText = '使用練習卡片學習';
      } else if (lang === 'zh_CN') {
        labelText = '练习卡片';
        titleText = '使用练习卡片学习';
      } else if (lang === 'ko') {
        labelText = '연습 카드';
        titleText = '연습 카드로 학습하기';
      } else if (lang === 'fr') {
        labelText = 'Cartes de pratique';
        titleText = 'Pratiquer avec les cartes mémoire';
      } else {
        labelText = 'Practice Cards';
        titleText = 'Practice with flashcards';
      }
      btnStudyMylistLabel.textContent = labelText;
      if (btnStudyMylist) btnStudyMylist.setAttribute('title', titleText);
    }
    const btnTestMylistLabel = document.getElementById('btnTestMylistLabel');
    if (btnTestMylistLabel) {
      if (lang === 'ja') btnTestMylistLabel.textContent = 'テスト';
      else if (lang === 'zh_TW' || lang === 'zh_HK') btnTestMylistLabel.textContent = '測驗';
      else if (lang === 'zh_CN') btnTestMylistLabel.textContent = '测验';
      else if (lang === 'ko') btnTestMylistLabel.textContent = '테스트';
      else if (lang === 'fr') btnTestMylistLabel.textContent = 'Test';
      else btnTestMylistLabel.textContent = 'Test';
    }

    // Mylist Sort Toolbar Translations
    const labelMylistSort = document.getElementById('labelMylistSort');
    if (labelMylistSort) {
      if (lang === 'ja') labelMylistSort.textContent = '並び替え:';
      else if (lang === 'zh_TW' || lang === 'zh_HK') labelMylistSort.textContent = '排序方式:';
      else if (lang === 'zh_CN') labelMylistSort.textContent = '排序方式:';
      else if (lang === 'ko') labelMylistSort.textContent = '정렬:';
      else if (lang === 'fr') labelMylistSort.textContent = 'Trier par :';
      else labelMylistSort.textContent = 'Sort by:';
    }
    const selectMylistSort = document.getElementById('selectMylistSort');
    if (selectMylistSort) {
      const optNewest = selectMylistSort.querySelector('option[value="newest"]');
      const optOldest = selectMylistSort.querySelector('option[value="oldest"]');
      const optGojuon = selectMylistSort.querySelector('option[value="gojuon"]');
      const optUnlearned = selectMylistSort.querySelector('option[value="unlearned"]');
      const optRandom = selectMylistSort.querySelector('option[value="random"]');

      if (lang === 'ja') {
        if (optNewest) optNewest.textContent = '🕒 追加が新しい順';
        if (optOldest) optOldest.textContent = '⏳ 追加が古い順';
        if (optGojuon) optGojuon.textContent = '🔤 五十音順（あ〜ん）';
        if (optUnlearned) optUnlearned.textContent = '🎯 未暗記優先（復習）';
        if (optRandom) optRandom.textContent = '🎲 ランダム';
      } else if (lang === 'zh_TW' || lang === 'zh_HK') {
        if (optNewest) optNewest.textContent = '🕒 由新到舊（最新）';
        if (optOldest) optOldest.textContent = '⏳ 由舊到新（最早）';
        if (optGojuon) optGojuon.textContent = '🔤 五十音順（あ〜ん）';
        if (optUnlearned) optUnlearned.textContent = '🎯 尚未掌握優先（複習）';
        if (optRandom) optRandom.textContent = '🎲 隨機順序';
      } else if (lang === 'zh_CN') {
        if (optNewest) optNewest.textContent = '🕒 由新到旧（最新）';
        if (optOldest) optOldest.textContent = '⏳ 由旧到新（最早）';
        if (optGojuon) optGojuon.textContent = '🔤 五十音顺序（あ〜ん）';
        if (optUnlearned) optUnlearned.textContent = '🎯 尚未掌握优先（复习）';
        if (optRandom) optRandom.textContent = '🎲 随机顺序';
      } else if (lang === 'ko') {
        if (optNewest) optNewest.textContent = '🕒 최신 추가순';
        if (optOldest) optOldest.textContent = '⏳ 오래된 순';
        if (optGojuon) optGojuon.textContent = '🔤 오십음도순 (あ〜ん)';
        if (optUnlearned) optUnlearned.textContent = '🎯 미암기 우선 (복습)';
        if (optRandom) optRandom.textContent = '🎲 무작위 (랜덤)';
      } else if (lang === 'fr') {
        if (optNewest) optNewest.textContent = '🕒 Plus récents d\'abord';
        if (optOldest) optOldest.textContent = '⏳ Plus anciens d\'abord';
        if (optGojuon) optGojuon.textContent = '🔤 Ordre alphabétique (あ〜ん)';
        if (optUnlearned) optUnlearned.textContent = '🎯 Non mémorisés d\'abord';
        if (optRandom) optRandom.textContent = '🎲 Aléatoire';
      } else {
        if (optNewest) optNewest.textContent = '🕒 Newest First';
        if (optOldest) optOldest.textContent = '⏳ Oldest First';
        if (optGojuon) optGojuon.textContent = '🔤 Japanese A-Z (あ〜ん)';
        if (optUnlearned) optUnlearned.textContent = '🎯 Needs Review (Unlearned)';
        if (optRandom) optRandom.textContent = '🎲 Shuffle / Random';
      }
    }

    // 11. Side Drawer Menu
    const drawerMenuLabel = document.getElementById('drawerMenuLabel');
    if (drawerMenuLabel) drawerMenuLabel.textContent = isJa ? 'メニュー' : 'Navigation Menu';
    const drawerHomeLabel = document.getElementById('drawerHomeLabel');
    if (drawerHomeLabel) drawerHomeLabel.textContent = isJa ? 'ホーム (単語カード)' : 'Home (Flashcards)';
    const drawerMylistLabel = document.getElementById('drawerMylistLabel');
    if (drawerMylistLabel) drawerMylistLabel.textContent = isJa ? 'マイリスト' : 'My List';
    const drawerQuizLabel = document.getElementById('drawerQuizLabel');
    if (drawerQuizLabel) {
      if (lang === 'ja') drawerQuizLabel.textContent = 'テスト';
      else if (lang === 'zh_TW' || lang === 'zh_HK') drawerQuizLabel.textContent = '測驗 / 考試';
      else if (lang === 'zh_CN') drawerQuizLabel.textContent = '测验 / 考试';
      else if (lang === 'ko') drawerQuizLabel.textContent = '퀴즈 / 테스트';
      else if (lang === 'fr') drawerQuizLabel.textContent = 'Quiz / Test';
      else drawerQuizLabel.textContent = 'Quiz / Test';
    }
    const drawerHelpBtnText = document.getElementById('drawerHelpBtnText');
    if (drawerHelpBtnText) {
      if (lang === 'ja') drawerHelpBtnText.textContent = '使い方ガイド';
      else if (lang === 'zh_TW' || lang === 'zh_HK') drawerHelpBtnText.textContent = '使用指南';
      else if (lang === 'zh_CN') drawerHelpBtnText.textContent = '使用指南';
      else if (lang === 'ko') drawerHelpBtnText.textContent = '이용 가이드';
      else if (lang === 'fr') drawerHelpBtnText.textContent = 'Guide d\'utilisation';
      else drawerHelpBtnText.textContent = 'Help Guide';
    }
    const drawerLangLabel = document.getElementById('drawerLangLabel');
    if (drawerLangLabel) drawerLangLabel.textContent = isJa ? '母国語設定' : 'Native Language';
    const drawerStudentLabel = document.getElementById('drawerStudentLabel');
    if (drawerStudentLabel) drawerStudentLabel.textContent = isJa ? '生徒アカウント' : 'Student Account';
    const drawerHelpLabel = document.getElementById('drawerHelpLabel');
    if (drawerHelpLabel) drawerHelpLabel.textContent = isJa ? 'ヘルプ・ガイド' : 'Help & Guide';

    // Update student badge in top header
    const headerStudentBadge = document.getElementById('headerStudentBadge');
    if (headerStudentBadge) {
      if (currentStudent) {
        const isTeacher = (currentStudent.id === 'haku' || currentStudent.id === 'admin');
        if (isTeacher) {
          headerStudentBadge.textContent = 'ハク先生 🌸';
        } else {
          headerStudentBadge.textContent = isJa ? `生徒: ${currentStudent.name}` : `Student: ${currentStudent.name}`;
        }
      } else {
        headerStudentBadge.textContent = isJa ? '生徒: ゲスト' : 'Student: Guest';
      }
    }

    // 12. Re-render folder overview & units with updated bilingual titles
    if (typeof renderFolderOverview === 'function') {
      renderFolderOverview();
    }
    if (typeof renderSidebarFolderTree === 'function' && !sidebarSearchQuery) {
      renderSidebarFolderTree();
    }
    // Update active study header if currently studying
    const activeHeader = document.getElementById('activeStudyHeader');
    if (activeHeader && !activeHeader.classList.contains('hidden') && typeof FOLDER_CONFIGS !== 'undefined') {
      const fc = FOLDER_CONFIGS.find(f => f.id === currentFolder);
      if (currentSection !== 'all') {
        const secInfo = getCatalogSection(currentSection);
        const rawSecTitle = secInfo ? secInfo.title : `単元${currentSection}`;
        document.getElementById('activeStudySectionName').textContent = getBilingualSectionTitle(currentSection, rawSecTitle, lang);
      } else if (fc) {
        document.getElementById('activeStudySectionName').textContent = `${getBilingualFolderTitle(fc, lang)} (${isJa ? '全単元' : 'All Units'})`;
      }
      if (fc) {
        document.getElementById('activeStudyFolderName').textContent = getBilingualFolderTitle(fc, lang);
      }
    }
  }

  // --- Data Loading & Persistence ---
  // --- Data Loading & Persistence ---
  function initData() {
    // Master data version check to ensure newly added cards & furigana updates are immediately visible
    const CURRENT_DATA_VERSION = 'v63_student_cards_purged_and_healed';
    const savedVersion = localStorage.getItem('haku_vocab_version');

    const seedCards = window.INITIAL_VOCAB_DATA || [];
    const seedCardMap = new Map();
    seedCards.forEach(c => seedCardMap.set(c.id, c));

    // Load and preserve ALL custom cards across all students (strictly excluding seed/curriculum cards)
    let allCustomCards = [];
    try {
      const fromAll = JSON.parse(localStorage.getItem('haku_all_custom_cards') || '[]');
      if (Array.isArray(fromAll)) {
        fromAll.forEach(c => {
          if (c && c.id && !seedCardMap.has(c.id) && c.section_num === undefined && isCustomCardId(c.id)) {
            allCustomCards.push(c);
          }
        });
      }
    } catch(e) {}

    const savedVocab = localStorage.getItem('haku_vocab_data');
    if (savedVocab) {
      try {
        const oldList = JSON.parse(savedVocab);
        oldList.forEach(c => {
          if (c && c.id && !seedCardMap.has(c.id) && c.section_num === undefined && isCustomCardId(c.id)) {
            if (!allCustomCards.find(existing => existing.id === c.id)) {
              allCustomCards.push(c);
            }
          }
        });
      } catch (e) {}
    }

    // Ensure Midori's card_1791393927923_pd4xbi and Arun's new cards are present in custom pool
    const ensureCustomCard = (card) => {
      const idx = allCustomCards.findIndex(c => c.id === card.id);
      if (idx >= 0) allCustomCards[idx] = { ...allCustomCards[idx], ...card };
      else allCustomCards.push(card);
    };

    ensureCustomCard({
      id: 'card_1791393927923_pd4xbi',
      word: '先延ばし',
      reading: 'さきのばし',
      category: '授業で習った言葉',
      studentId: '0012',
      isCustom: true,
      meaning: {
        en: 'procrastination / putting things off',
        ja: '先延ばし',
        zh_TW: '拖延 / 延期',
        zh_CN: '拖延 / 延期',
        ko: '미루기 / 연기',
        zh_HK: '拖延 / 推遲',
        fr: 'procrastination / remise à plus tard'
      },
      example: {
        ja: 'A: <ruby>嫌<rt>いや</rt></ruby>なことをつい<ruby>先延<rt>さきの</rt></ruby>ばしにしてしまいます。<br/>B: <ruby>先延<rt>さきの</rt></ruby>ばしにすると、<ruby>後<rt>あと</rt></ruby>でさらに<ruby>大変<rt>たいへん</rt></ruby>になりますよ。',
        en: "A: I tend to put off things I dislike doing.<br/>B: If you procrastinate, it gets even harder later on.",
        zh_TW: 'A: 我總是忍不住把討厭的事拖延下去。<br/>B: 如果拖延的話，之後會變得更加麻煩喔。',
        zh_CN: 'A: 我总是忍不住把讨厌的事拖延下去。<br/>B: 如果拖延的话，之后会变得更加麻烦哦。',
        ko: 'A: 싫은 일을 자꾸 뒤로 미루게 돼요.<br/>B: 미루면 나중에 더 힘들어져요.',
        zh_HK: 'A: 我成日都忍唔住將討厭嘅事拖延落去。<br/>B: 如果拖延嘅話，之後會仲更加麻煩㗎。',
        fr: "A: J'ai tendance à remettre à plus tard les choses que je n'aime pas.<br/>B: Si vous procrastinez, ce sera encore plus difficile par la suite."
      },
      related: '先延ばしにする（授業の重要表現）'
    });

    ensureCustomCard({
      id: 'card_arun_houritsu',
      word: '法律',
      reading: 'ほうりつ',
      category: '授業で習った言葉',
      studentId: '0023',
      isCustom: true,
      meaning: {
        en: 'law / statute',
        ja: '法律',
        zh_TW: '法律',
        zh_CN: '法律',
        ko: '법률',
        zh_HK: '法律',
        fr: 'loi / législation'
      },
      example: {
        ja: 'A: <ruby>社会<rt>しゃかい</rt></ruby>のルールとして<ruby>法律<rt>ほうりつ</rt></ruby>を<ruby>守<rt>まも</rt></ruby>ることはとても<ruby>大切<rt>たいせつ</rt></ruby>です。<br/>B: はい、どんな<ruby>場合<rt>ばあい</rt></ruby>でも<ruby>法律<rt>ほうりつ</rt></ruby>に<ruby>基<rt>もと</rt></ruby>づいて<ruby>行動<rt>こうどう</rt></ruby>すべきですね。',
        en: 'A: Obeying the law as a social rule is very important.<br/>B: Yes, we should always act in accordance with the law.',
        zh_TW: 'A: 遵守法律作為社會規則是非常重要的。<br/>B: 是的，無論在任何情況下都應當依據法律行事。',
        zh_CN: 'A: 遵守法律作为社会规则是非常重要的。<br/>B: 是的，无论在任何情况下都应当依据法律行事。',
        ko: 'A: 사회 규칙으로서 법률을 지키는 것은 매우重要합니다.<br/>B: 네, 어떤 경우라도 법률에 근거해 행동해야 하죠.',
        zh_HK: 'A: 遵守法律作為社會規則係非常重要嘅。<br/>B: 係呀，無論任何情況下都應該根據法律行事。',
        fr: 'A: Il est essentiel de respecter la loi comme règle sociale.<br/>B: Oui, nous devons toujours agir conformément à la loi.'
      },
      related: 'ほうりつ（授業の重要表現）'
    });

    ensureCustomCard({
      id: 'card_arun_koukai',
      word: '公開',
      reading: 'こうかい',
      category: '授業で習った言葉',
      studentId: '0023',
      isCustom: true,
      meaning: {
        en: 'opening to public / release / premiere',
        ja: '公開',
        zh_TW: '公開 / 上映',
        zh_CN: '公开 / 上映',
        ko: '공개 / 개봉',
        zh_HK: '公開 / 上映',
        fr: 'ouverture au public / sortie'
      },
      example: {
        ja: 'A: <ruby>楽<rt>たの</rt></ruby>しみにしていた<ruby>映画<rt>えいが</rt></ruby>が<ruby>来週<rt>らいしゅう</rt></ruby><ruby>公開<rt>こうかい</rt></ruby>されますね！<br/>B: ええ、<ruby>公開<rt>こうかい</rt></ruby><ruby>初日<rt>しょにち</rt></ruby>に<ruby>見<rt>み</rt></ruby>に<ruby>行<rt>い</rt></ruby>くつもりです。',
        en: "A: The movie I've been looking forward to will be released next week!<br/>B: Yes, I plan to go see it on opening day.",
        zh_TW: 'A: 期待已久的電影下週就要上映了呢！<br/>B: 是的，我打算在上映首日就去看。',
        zh_CN: 'A: 期待已久的电影下周就要上映了呢！<br/>B: 是的，我打算在上映首日就去看。',
        ko: 'A: 기대하던 영화가 다음 주에 개봉하네요!<br/>B: 네, 개봉 첫날에 보러 갈 생각이에요.',
        zh_HK: 'A: 好期待嗰部戲下個禮拜就上映喇！<br/>B: 係呀，我打算上映第一日就去睇。',
        fr: 'A: Le film que j\'attendais sort la semaine prochaine !<br/>B: Oui, je compte aller le voir dès le premier jour.'
      },
      related: 'こうかい（授業の重要表現）'
    });

    ensureCustomCard({
      id: 'card_arun_hikoukai',
      word: '非公開',
      reading: 'ひこうかい',
      category: '授業で習った言葉',
      studentId: '0023',
      isCustom: true,
      meaning: {
        en: 'private / confidential / unlisted',
        ja: '非公開',
        zh_TW: '不公開 / 私密',
        zh_CN: '不公开 / 私密',
        ko: '비공개',
        zh_HK: '唔公開 / 私人',
        fr: 'privé / confidentiel'
      },
      example: {
        ja: 'A: このミーティングの<ruby>内容<rt>ないよう</rt></ruby>は<ruby>完全<rt>かんぜん</rt></ruby>に<ruby>非公開<rt>ひこうかい</rt></ruby>ですか？<br/>B: はい、<ruby>関係者<rt>かんけいしゃ</rt></ruby><ruby>以外<rt>いがい</rt></ruby>には<ruby>非公開<rt>ひこうかい</rt></ruby>となっています。',
        en: 'A: Is the content of this meeting strictly confidential?<br/>B: Yes, it is kept private from everyone except authorized parties.',
        zh_TW: 'A: 這次會議的內容是完全不公開的嗎？<br/>B: 是的，除了相關人員之外一律不公開。',
        zh_CN: 'A: 这次会议的内容是完全不公开的吗？<br/>B: 是的，除了相关人员之外一律不公开。',
        ko: 'A: 이 미팅의 내용은 완전히 비공개인가요?<br/>B: 네, 관계자 이외에는 비공개로 되어 있습니다.',
        zh_HK: 'A: 呢個會議嘅內容係咪完全唔公開㗎？<br/>B: 係呀，除咗相關人員之外一律都係非公開嘅。',
        fr: 'A: Le contenu de cette réunion est-il totalement confidentiel ?<br/>B: Oui, il reste privé pour toute personne extérieure.'
      },
      related: 'ひこうかい（授業の重要表現）'
    });

    // Ensure all 16 of Midori-san's new curated cards are always loaded in custom pool
    if (typeof MIDORI_CURATED_CARDS !== 'undefined') {
      MIDORI_CURATED_CARDS.forEach(c => ensureCustomCard(c));
    }
    if (typeof DANIEL_CURATED_CARDS !== 'undefined') {
      DANIEL_CURATED_CARDS.forEach(c => ensureCustomCard(c));
    }
    if (typeof ELIIE_CURATED_CARDS !== 'undefined') {
      ELIIE_CURATED_CARDS.forEach(c => ensureCustomCard(c));
    }
    if (typeof ARUN_CURATED_CARDS !== 'undefined') {
      ARUN_CURATED_CARDS.forEach(c => ensureCustomCard(c));
    }

    // Auto-purge any corrupted cards or seed duplicates from custom pool
    const seenCustomIds = new Set();
    allCustomCards = allCustomCards.filter(c => {
      if (!c || !c.id || isStubCard(c) || isCorruptedCard(c)) return false;
      if (seedCardMap.has(c.id) || c.section_num !== undefined || !isCustomCardId(c.id)) return false;
      if (seenCustomIds.has(c.id)) return false;
      seenCustomIds.add(c.id);
      return true;
    });

    localStorage.setItem('haku_all_custom_cards', JSON.stringify(allCustomCards));

    // Construct vocabList strictly: seed cards first, then custom cards (guaranteed 0 duplicates)
    const seenVocabIds = new Set();
    const finalVocabList = [];
    seedCards.forEach(c => {
      if (c && c.id && !seenVocabIds.has(c.id)) {
        seenVocabIds.add(c.id);
        finalVocabList.push(c);
      }
    });
    allCustomCards.forEach(c => {
      if (c && c.id && !seenVocabIds.has(c.id) && c.section_num === undefined) {
        seenVocabIds.add(c.id);
        finalVocabList.push(c);
      }
    });
    vocabList = finalVocabList;
    localStorage.setItem('haku_vocab_data', JSON.stringify(vocabList));

    if (savedVersion !== CURRENT_DATA_VERSION) {
      // Reload latest INITIAL_STUDENTS master list when version updates, while preserving edits & newly added ones
      const seedStudents = window.INITIAL_STUDENTS || [];
      const savedStudents = localStorage.getItem('haku_students');
      if (savedStudents) {
        try {
          const parsed = JSON.parse(savedStudents);
          const savedMap = new Map(parsed.map(s => [s.id, s]));
          // Apply teacher's edited names/passcodes onto seed students, or fallback to seed
          students = seedStudents.map(seed => {
            const saved = savedMap.get(seed.id);
            return saved ? { ...seed, ...saved } : seed;
          });
          // Also include any new students added beyond seed
          const seedIds = new Set(seedStudents.map(s => s.id));
          const customExtra = parsed.filter(s => !seedIds.has(s.id) && !s.id.startsWith('student_'));
          students = [...students, ...customExtra];
        } catch (e) {
          students = seedStudents;
        }
      } else {
        students = seedStudents;
      }
      localStorage.setItem('haku_students', JSON.stringify(students));

      // Initialize per-student exact tab card mappings
      const CLASS_FOLDER_ID = 'folder_class_words';
      const CLASS_FOLDER_NAME = '授業で習った言葉';

      const STUDENT_DOC_RANGES = {
        '0012': [1, 289],      // みどりさん (289語 + 1追加語)
        '0011': [290, 498],    // Keyvinさん (209語)
        '0013': [499, 538],    // ななさん (40語)
        '0014': [539, 639],    // Danielさん (101語)
        '0015': [640, 873],    // Stephenさん (234語)
        '0016': [874, 1144],   // ジウンさん (271語)
        '0017': [1145, 1213],  // ハンウさん (69語)
        '0018': [1214, 1232],  // Justinさん (19語)
        '0019': [1233, 1314],  // ミンギさん (82語)
        '0020': [1315, 1397],  // Colinさん (83語)
        '0021': [1398, 1598],  // ともやさん (201語)
        '0022': [1599, 1602]   // 生徒22 (追加語彙)
      };

      const allStudentIds = [...students.map(s => s.id), 'guest'];
      allStudentIds.forEach(stId => {
        const key = `haku_mylist_${stId}`;
        const foldersKey = `haku_mylist_folders_${stId}`;
        const mapKey = `haku_mylist_card_map_${stId}`;

        // Ensure "授業で習った言葉" folder exists
        let stFolders = [];
        try { stFolders = JSON.parse(localStorage.getItem(foldersKey) || '[]'); } catch (e) { stFolders = []; }
        if (!stFolders.find(f => f.id === CLASS_FOLDER_ID)) {
          stFolders.unshift({ id: CLASS_FOLDER_ID, name: CLASS_FOLDER_NAME });
          localStorage.setItem(foldersKey, JSON.stringify(stFolders));
        }

        // Clean previous class_word cards from this student's mylist
        let stSet = [];
        try { stSet = JSON.parse(localStorage.getItem(key) || '[]'); } catch (e) { stSet = []; }
        let stMap = {};
        try { stMap = JSON.parse(localStorage.getItem(mapKey) || '{}'); } catch (e) { stMap = {}; }

        // Remove old class_word_*
        const filteredSet = stSet.filter(id => !id.startsWith('class_word_'));
        Object.keys(stMap).forEach(id => {
          if (id.startsWith('class_word_')) {
            delete stMap[id];
          }
        });

        // Add ONLY this student's specific words
        const range = STUDENT_DOC_RANGES[stId];
        if (range) {
          const [startNum, endNum] = range;
          for (let num = startNum; num <= endNum; num++) {
            const cId = `class_word_${String(num).padStart(4, '0')}`;
            filteredSet.push(cId);
            stMap[cId] = CLASS_FOLDER_ID;
          }
          if (stId === '0012') {
            const mId = 'card_1791393927923_pd4xbi';
            filteredSet.push(mId);
            stMap[mId] = CLASS_FOLDER_ID;
            MIDORI_NEW_CARD_IDS.forEach(id => {
              filteredSet.push(id);
              stMap[id] = CLASS_FOLDER_ID;
            });
          }
          if (stId === '0014') {
            DANIEL_NEW_CARD_IDS.forEach(id => {
              filteredSet.push(id);
              stMap[id] = CLASS_FOLDER_ID;
            });
          }
        } else if (stId === '0023' && window.CLASS_ARUN_IDS) {
          // Special exact list for Arun (526 unique words)
          window.CLASS_ARUN_IDS.forEach(cId => {
            filteredSet.push(cId);
            stMap[cId] = CLASS_FOLDER_ID;
          });
        }

        localStorage.setItem(key, JSON.stringify(Array.from(new Set(filteredSet))));
        localStorage.setItem(mapKey, JSON.stringify(stMap));
      });

      // Purge any corrupted cards from local storage across custom cards and student mylists
      try {
        let storedCustom = JSON.parse(localStorage.getItem('haku_all_custom_cards') || '[]');
        if (Array.isArray(storedCustom)) {
          storedCustom = storedCustom.filter(c => !isCorruptedCard(c));
          localStorage.setItem('haku_all_custom_cards', JSON.stringify(storedCustom));
        }
        let storedVocab = JSON.parse(localStorage.getItem('haku_vocab_data') || '[]');
        if (Array.isArray(storedVocab)) {
          storedVocab = storedVocab.filter(c => !isCorruptedCard(c));
          localStorage.setItem('haku_vocab_data', JSON.stringify(storedVocab));
        }
      } catch(e) {}

      localStorage.setItem('haku_vocab_version', CURRENT_DATA_VERSION);
    }

    const savedStudents = localStorage.getItem('haku_students');
    if (savedStudents) {
      try {
        students = JSON.parse(savedStudents);
      } catch (e) {
        students = window.INITIAL_STUDENTS || [];
      }
    } else {
      students = window.INITIAL_STUDENTS || [];
    }

    // Load active student session if stored
    const savedStudentId = localStorage.getItem('haku_current_student_id');
    if (savedStudentId) {
      const found = students.find(s => s.id === savedStudentId);
      if (found) {
        setStudent(found);
      }
    }

    // 現代若者言葉・推し活・SNSネットスラング辞書の統合（最優先ヒット）
    if (window.MODERN_SLANG_DATA && Array.isArray(window.MODERN_SLANG_DATA)) {
      if (window.DICT_DATA && Array.isArray(window.DICT_DATA)) {
        const slangKeys = new Set(window.MODERN_SLANG_DATA.map(s => s.w));
        window.DICT_DATA = [...window.MODERN_SLANG_DATA, ...window.DICT_DATA.filter(d => !slangKeys.has(d.w))];
      } else {
        window.DICT_DATA = [...window.MODERN_SLANG_DATA];
      }
    }

    loadMylistForCurrentStudent();
    applyUiLanguage(currentLang);
    renderFolderOverview();
    initSidebarWordList();
    initLayoutMode();
    updateActiveDeck();
    renderAdminStudentList();
  }

  // --- Left Sidebar Wordbook & Unified Search with Inline Accordion ---
  // --- Left Sidebar Vertical Folders & Curriculum List (PC版: 縦の箇条書き) ---
  let sidebarSearchQuery = '';
  let expandedFolderIds = new Set(); // all closed by default; only one open at a time
  let expandedWordId = null; // Track currently expanded accordion item

  function initSidebarWordList() {
    renderSidebarContent();

    const topSearch = document.getElementById('globalTopSearchInput');
    const clearTopBtn = document.getElementById('btnClearTopSearch');

    if (topSearch) {
      topSearch.addEventListener('input', (e) => {
        sidebarSearchQuery = e.target.value.trim().toLowerCase();
        if (clearTopBtn) {
          clearTopBtn.classList.toggle('hidden', !sidebarSearchQuery);
        }
        renderSidebarContent();
      });

      // Show dropdown on focus if input has value
      topSearch.addEventListener('focus', () => {
        if (sidebarSearchQuery) {
          const dropdown = document.getElementById('searchDropdownContainer');
          if (dropdown) dropdown.classList.remove('hidden');
        }
      });
    }

    if (clearTopBtn) {
      clearTopBtn.addEventListener('click', () => {
        if (topSearch) topSearch.value = '';
        sidebarSearchQuery = '';
        clearTopBtn.classList.add('hidden');
        const dropdown = document.getElementById('searchDropdownContainer');
        if (dropdown) dropdown.classList.add('hidden');
        renderSidebarContent();

        // If the user was viewing a searched word card, return to folder overview
        if (isSearchStudyMode) {
          backToFolderOverview();
        }
      });
    }

    // Close dropdown when clicking outside
    document.addEventListener('click', (e) => {
      const topSearchContainer = document.getElementById('globalTopSearchInput')?.parentElement;
      const dropdown = document.getElementById('searchDropdownContainer');
      if (dropdown && topSearchContainer && !topSearchContainer.contains(e.target)) {
        dropdown.classList.add('hidden');
      }
    });

    // Connect sidebar shuffle button
    const btnShuffleSidebar = document.getElementById('btnShuffleAllSidebar');
    if (btnShuffleSidebar) {
      btnShuffleSidebar.addEventListener('click', () => {
        currentFolder = 'all';
        currentSection = 'all';
        const isJa = currentLang === 'ja';
        document.getElementById('activeStudySectionName').textContent = isJa ? '全単元 (全シャッフル)' : 'All Units (Shuffle All)';
        document.getElementById('activeStudyFolderName').textContent = isJa ? 'カリキュラム一覧' : 'Curriculum';
        document.getElementById('folderOverviewPanel').classList.add('hidden');
        document.getElementById('unitListPanel').classList.add('hidden');
        document.getElementById('activeStudyHeader').classList.remove('hidden');

        updateActiveDeck();
        activeDeck.sort(() => Math.random() - 0.5);
        currentIndex = 0;
        renderCurrentCard();
        showToast(isJa ? '全単元をシャッフルしました！🔀' : 'Shuffled all curriculum cards! 🔀');
      });
    }
  }

  // Smart dispatch: show vertical folders by default, or matched search words when searching
  function renderSidebarContent() {
    const rawQuery = (sidebarSearchQuery || '').trim();
    if (rawQuery) {
      renderUnifiedSearchResults(rawQuery);
    } else {
      const dropdown = document.getElementById('searchDropdownContainer');
      if (dropdown) dropdown.classList.add('hidden');
      renderSidebarFolderTree();
    }
  }

  // --- Filtering & Deck Navigation System ---
  let currentFolder = 'all'; // 'folder_1', 'folder_2', 'folder_3', 'folder_4'
  let currentSection = 'all'; // 1 to 43 or 'all'
  let currentNavLevel = 'folders'; // 'folders' (level 1), 'units' (level 2), 'study' (level 3)

  const FOLDER_CONFIGS = [
    {
      id: 'folder_1',
      title: '初級 1-10',
      desc: '挨拶・身の回り・家族・場所・体・数字',
      range: [1, 10],
      badge: 'STAGE 1',
      trans: {
        en: 'Beginner 1-10',
        zh_TW: '初級 1-10',
        zh_CN: '初级 1-10',
        ko: '초급 1-10',
        zh_HK: '初級 1-10',
        fr: 'Débutant 1-10'
      }
    },
    {
      id: 'folder_2',
      title: '初級 11-20',
      desc: '日時・数え方・動詞・食べ物・する動詞',
      range: [11, 20],
      badge: 'STAGE 2',
      trans: {
        en: 'Beginner 11-20',
        zh_TW: '初級 11-20',
        zh_CN: '初级 11-20',
        ko: '초급 11-20',
        zh_HK: '初級 11-20',
        fr: 'Débutant 11-20'
      }
    },
    {
      id: 'folder_3',
      title: '初級 21-30',
      desc: '会話・形容詞・予定・天気・電車・て形',
      range: [21, 30],
      badge: 'STAGE 3',
      trans: {
        en: 'Beginner 21-30',
        zh_TW: '初級 21-30',
        zh_CN: '初级 21-30',
        ko: '초급 21-30',
        zh_HK: '初級 21-30',
        fr: 'Débutant 21-30'
      }
    },
    {
      id: 'folder_4',
      title: '初級 31-43',
      desc: 'て形応用・動詞4/5・病気・ない形・可能形',
      range: [31, 43],
      badge: 'STAGE 4',
      trans: {
        en: 'Beginner 31-43',
        zh_TW: '初級 31-43',
        zh_CN: '初级 31-43',
        ko: '초급 31-43',
        zh_HK: '初級 31-43',
        fr: 'Débutant 31-43'
      }
    }
  ];

  // Master Catalog of all 44 curriculum units (0 to 43) to guarantee 100% availability
  const MASTER_SECTIONS_CATALOG = [
    { num: 0, title: 'まずは授業で使う単語を覚えよう！', folder_id: 'folder_1' },
    { num: 1, title: 'simple phrase', folder_id: 'folder_1' },
    { num: 2, title: '身の回りのもの', folder_id: 'folder_1' },
    { num: 3, title: '代名詞/家族', folder_id: 'folder_1' },
    { num: 4, title: '場所', folder_id: 'folder_1' },
    { num: 5, title: '動物', folder_id: 'folder_1' },
    { num: 6, title: '職業/身分', folder_id: 'folder_1' },
    { num: 7, title: '国/地名', folder_id: 'folder_1' },
    { num: 8, title: '体の名前', folder_id: 'folder_1' },
    { num: 9, title: '位置', folder_id: 'folder_1' },
    { num: 10, title: '基本の数字', folder_id: 'folder_1' },
    { num: 11, title: '日付（月/日）', folder_id: 'folder_2' },
    { num: 12, title: '時間/時間帯', folder_id: 'folder_2' },
    { num: 13, title: 'もの/人の数え方', folder_id: 'folder_2' },
    { num: 14, title: '時間/時制表現', folder_id: 'folder_2' },
    { num: 15, title: '基本動詞(1)', folder_id: 'folder_2' },
    { num: 16, title: '乗り物', folder_id: 'folder_2' },
    { num: 17, title: '時間/頻度', folder_id: 'folder_2' },
    { num: 18, title: '食べ物', folder_id: 'folder_2' },
    { num: 19, title: '基本動詞(2)', folder_id: 'folder_2' },
    { num: 20, title: 'する動詞（名詞）', folder_id: 'folder_2' },
    { num: 21, title: 'あいづち/接続し', folder_id: 'folder_3' },
    { num: 22, title: 'い形容詞(1)', folder_id: 'folder_3' },
    { num: 23, title: 'な形容詞', folder_id: 'folder_3' },
    { num: 24, title: '色/味', folder_id: 'folder_3' },
    { num: 25, title: '予定/映画/スポーツ', folder_id: 'folder_3' },
    { num: 26, title: '季節/天気', folder_id: 'folder_3' },
    { num: 27, title: '基本動詞(3)', folder_id: 'folder_3' },
    { num: 28, title: 'お出掛け', folder_id: 'folder_3' },
    { num: 29, title: '電車', folder_id: 'folder_3' },
    { num: 30, title: '基本動詞(1) てform', folder_id: 'folder_3' },
    { num: 31, title: '基本動詞(2) てform', folder_id: 'folder_4' },
    { num: 32, title: '基本動詞(3) てform', folder_id: 'folder_4' },
    { num: 33, title: '基本動詞(4)', folder_id: 'folder_4' },
    { num: 34, title: '基本動詞(5)', folder_id: 'folder_4' },
    { num: 35, title: 'い形容詞(2)', folder_id: 'folder_4' },
    { num: 36, title: '病気/症状', folder_id: 'folder_4' },
    { num: 37, title: '基本動詞 ないform (1)', folder_id: 'folder_4' },
    { num: 38, title: '基本動詞 ないform (2)', folder_id: 'folder_4' },
    { num: 39, title: '基本動詞 ないform (3)', folder_id: 'folder_4' },
    { num: 40, title: '基本動詞 ないform (4)', folder_id: 'folder_4' },
    { num: 41, title: '基本動詞 ないform (5)', folder_id: 'folder_4' },
    { num: 42, title: '基本動詞 可能形 (1)', folder_id: 'folder_4' },
    { num: 43, title: '基本動詞 可能形 (2)', folder_id: 'folder_4' }
  ];

  function getCatalogSection(secNum) {
    const n = Number(secNum);
    const item = MASTER_SECTIONS_CATALOG.find(s => s.num === n);
    if (item) return item;
    if (window.SECTIONS_DATA && Array.isArray(window.SECTIONS_DATA)) {
      const fromWin = window.SECTIONS_DATA.find(s => Number(s.num) === n);
      if (fromWin) return fromWin;
    }
    if (window.SECTIONS && window.SECTIONS[secNum]) {
      return { num: n, title: window.SECTIONS[secNum] };
    }
    return { num: n, title: `単元${secNum}` };
  }

  // Multilingual translations for all 44 curriculum unit titles
  const SECTION_TRANSLATIONS = {
    0: { en: 'Classroom Phrases', zh_TW: '課堂常用句', zh_CN: '课堂常用句', ko: '수업 필수 표현', zh_HK: '課堂常用句', fr: 'Phrases de classe' },
    1: { en: 'Simple Phrases', zh_TW: '簡易短句', zh_CN: '简易短句', ko: '간단한 표현', zh_HK: '簡易短句', fr: 'Phrases simples' },
    2: { en: 'Everyday Objects', zh_TW: '隨身物品', zh_CN: '随身物品', ko: '주변 사물', zh_HK: '隨身物品', fr: 'Objets du quotidien' },
    3: { en: 'Pronouns & Family', zh_TW: '代名詞與家族', zh_CN: '代名词与家族', ko: '대명사 및家族', zh_HK: '代名詞與家族', fr: 'Pronoms et Famille' },
    4: { en: 'Places', zh_TW: '場所', zh_CN: '场所', ko: '장소', zh_HK: '場所', fr: 'Lieux' },
    5: { en: 'Animals', zh_TW: '動物', zh_CN: '动物', ko: '동물', zh_HK: '動物', fr: 'Animaux' },
    6: { en: 'Occupations & Status', zh_TW: '職業與身分', zh_CN: '职业与身分', ko: '직업 및 신분', zh_HK: '職業與身分', fr: 'Métiers et Statut' },
    7: { en: 'Countries & Locations', zh_TW: '國家與地名', zh_CN: '国家与地名', ko: '국가 및 지명', zh_HK: '國家與地名', fr: 'Pays et Lieux' },
    8: { en: 'Body Parts', zh_TW: '身體部位', zh_CN: '身体部位', ko: '신체 부위', zh_HK: '身體部位', fr: 'Parties du corps' },
    9: { en: 'Positions & Directions', zh_TW: '方位與位置', zh_CN: '方位与位置', ko: '위치 및 방향', zh_HK: '方位與位置', fr: 'Positions' },
    10: { en: 'Basic Numbers', zh_TW: '基本數字', zh_CN: '基本数字', ko: '기본 숫자', zh_HK: '基本數字', fr: 'Nombres de base' },
    11: { en: 'Dates (Month / Day)', zh_TW: '日期（月份／日期）', zh_CN: '日期（月份／日期）', ko: '날짜 (월/일)', zh_HK: '日期（月份／日期）', fr: 'Dates (Mois / Jour)' },
    12: { en: 'Time & Time Periods', zh_TW: '時間與時段', zh_CN: '时间与时段', ko: '시간 및 시간대', zh_HK: '時間與時段', fr: 'Heure et Périodes' },
    13: { en: 'Counters (Things / People)', zh_TW: '計數詞（物／人）', zh_CN: '计数词（物／人）', ko: '수사 (사물/사람)', zh_HK: '計數詞（物／人）', fr: 'Compteurs' },
    14: { en: 'Time & Tense Expressions', zh_TW: '時間與時態', zh_CN: '时间与时态', ko: '시간 및 시제 표현', zh_HK: '時間與時態', fr: 'Temps et Expressions temporelles' },
    15: { en: 'Basic Verbs 1', zh_TW: '基本動詞 1', zh_CN: '基本动词 1', ko: '기본 동사 1', zh_HK: '基本動詞 1', fr: 'Verbes de base 1' },
    16: { en: 'Vehicles & Transport', zh_TW: '交通工具', zh_CN: '交通工具', ko: '교통수단', zh_HK: '交通工具', fr: 'Transports' },
    17: { en: 'Time & Frequency', zh_TW: '時間與頻率', zh_CN: '时间与频率', ko: '시간 및 빈도', zh_HK: '時間與頻率', fr: 'Temps et Fréquence' },
    18: { en: 'Food & Drinks', zh_TW: '食物與飲食', zh_CN: '食物与饮食', ko: '음식', zh_HK: '食物與飲食', fr: 'Nourriture' },
    19: { en: 'Basic Verbs 2', zh_TW: '基本動詞 2', zh_CN: '基本动词 2', ko: '기본 동사 2', zh_HK: '基本動詞 2', fr: 'Verbes de base 2' },
    20: { en: 'Suru Verbs (Nouns)', zh_TW: 'Suru動詞（名詞）', zh_CN: 'Suru动词（名词）', ko: 'Suru 동사 (명사)', zh_HK: 'Suru動詞（名詞）', fr: 'Verbes en Suru' },
    21: { en: 'Fillers & Conjunctions', zh_TW: '隨聲附和與連接詞', zh_CN: '随声附和与连接词', ko: '맞장구 및 접속사', zh_HK: '隨聲附和與連接詞', fr: 'Interjections et Conjonctions' },
    22: { en: 'I-Adjectives 1', zh_TW: 'い形容詞 1', zh_CN: 'い形容词 1', ko: 'い형용사 1', zh_HK: 'い形容詞 1', fr: 'Adjectifs en -i 1' },
    23: { en: 'Na-Adjectives', zh_TW: 'な形容詞', zh_CN: 'な形容词', ko: 'な형용사', zh_HK: 'な形容詞', fr: 'Adjectifs en -na' },
    24: { en: 'Colors & Tastes', zh_TW: '顏色與味道', zh_CN: '颜色与味道', ko: '색상 및 맛', zh_HK: '顏色與味道', fr: 'Couleurs et Goûts' },
    25: { en: 'Plans, Movies & Sports', zh_TW: '計畫、電影與運動', zh_CN: '计划、电影与运动', ko: '일정, 영화, 스포츠', zh_HK: '計畫、電影與運動', fr: 'Projets, Films et Sports' },
    26: { en: 'Seasons & Weather', zh_TW: '季節與天氣', zh_CN: '季节与天气', ko: '계절 및 날씨', zh_HK: '季節與天氣', fr: 'Saisons et Météo' },
    27: { en: 'Basic Verbs 3', zh_TW: '基本動詞 3', zh_CN: '基本动词 3', ko: '기본 동사 3', zh_HK: '基本動詞 3', fr: 'Verbes de base 3' },
    28: { en: 'Going Out', zh_TW: '外出', zh_CN: '外出', ko: '외출', zh_HK: '外出', fr: 'Sorties' },
    29: { en: 'Trains & Subways', zh_TW: '電車與鐵路', zh_CN: '电车与铁路', ko: '전철 및 기차', zh_HK: '電車與鐵路', fr: 'Train et Métro' },
    30: { en: 'Basic Verbs 1 (Te-form)', zh_TW: '基本動詞 1（て形）', zh_CN: '基本动词 1（て形）', ko: '기본 동사 1 (て형)', zh_HK: '基本動詞 1（て形）', fr: 'Verbes de base 1 (forme en te)' },
    31: { en: 'Basic Verbs 2 (Te-form)', zh_TW: '基本動詞 2（て形）', zh_CN: '基本动词 2（て形）', ko: '기본 동사 2 (て형)', zh_HK: '基本動詞 2（て形）', fr: 'Verbes de base 2 (forme en te)' },
    32: { en: 'Basic Verbs 3 (Te-form)', zh_TW: '基本動詞 3（て形）', zh_CN: '基本动词 3（て形）', ko: '기본 동사 3 (て형)', zh_HK: '基本動詞 3（て形）', fr: 'Verbes de base 3 (forme en te)' },
    33: { en: 'Basic Verbs 4', zh_TW: '基本動詞 4', zh_CN: '基本动词 4', ko: '기본 동사 4', zh_HK: '基本動詞 4', fr: 'Verbes de base 4' },
    34: { en: 'Basic Verbs 5', zh_TW: '基本動詞 5', zh_CN: '基本动词 5', ko: '기본 동사 5', zh_HK: '基本動詞 5', fr: 'Verbes de base 5' },
    35: { en: 'I-Adjectives 2', zh_TW: 'い形容詞 2', zh_CN: 'い形容词 2', ko: 'い형용사 2', zh_HK: 'い形容詞 2', fr: 'Adjectifs en -i 2' },
    36: { en: 'Illness & Symptoms', zh_TW: '疾病與症狀', zh_CN: '疾病与症状', ko: '질병 및 증상', zh_HK: '疾病與症狀', fr: 'Maladie et Symptômes' },
    37: { en: 'Basic Verbs 1 (Nai-form)', zh_TW: '基本動詞 1（ない形）', zh_CN: '基本动词 1（ない形）', ko: '기본 동사 1 (ない형)', zh_HK: '基本動詞 1（ない形）', fr: 'Verbes de base 1 (forme en nai)' },
    38: { en: 'Basic Verbs 2 (Nai-form)', zh_TW: '基本動詞 2（ない形）', zh_CN: '基本动词 2（ない形）', ko: '기본 동사 2 (ない형)', zh_HK: '基本動詞 2（ない形）', fr: 'Verbes de base 2 (forme en nai)' },
    39: { en: 'Basic Verbs 3 (Nai-form)', zh_TW: '基本動詞 3（ない形）', zh_CN: '基本动词 3（ない形）', ko: '기본 동사 3 (ない형)', zh_HK: '基本動詞 3（ない形）', fr: 'Verbes de base 3 (forme en nai)' },
    40: { en: 'Basic Verbs 4 (Nai-form)', zh_TW: '基本動詞 4（ない形）', zh_CN: '基本动词 4（ない形）', ko: '기본 동사 4 (ない형)', zh_HK: '基本動詞 4（ない形）', fr: 'Verbes de base 4 (forme en nai)' },
    41: { en: 'Basic Verbs 5 (Nai-form)', zh_TW: '基本動詞 5（ない形）', zh_CN: '基本动词 5（ない形）', ko: '기본 동사 5 (ない형)', zh_HK: '基本動詞 5（ない形）', fr: 'Verbes de base 5 (forme en nai)' },
    42: { en: 'Basic Verbs 1 (Potential)', zh_TW: '基本動詞 1（可能形）', zh_CN: '基本动词 1（可能形）', ko: '기본 동사 1 (가능형)', zh_HK: '基本動詞 1（可能形）', fr: 'Verbes de base 1 (forme potentielle)' },
    43: { en: 'Basic Verbs 2 (Potential)', zh_TW: '基本動詞 2（可能形）', zh_CN: '基本动词 2（可能形）', ko: '기본 동사 2 (가능형)', zh_HK: '基本動詞 2（可能形）', fr: 'Verbes de base 2 (forme potentielle)' }
  };

  // Helper to format bilingual title: 日本語 (各言語訳)
  function getBilingualSectionTitle(secNum, rawJapaneseTitle, lang) {
    const sInfo = getCatalogSection(secNum);
    const jpTitle = rawJapaneseTitle || (sInfo ? sInfo.title : `単元${secNum}`);
    if (lang === 'ja' || !lang) {
      return jpTitle;
    }
    const tMap = SECTION_TRANSLATIONS[secNum];
    if (!tMap) return jpTitle;
    const trans = tMap[lang] || tMap.en;
    if (!trans) return jpTitle;
    return `${jpTitle} (${trans})`;
  }

  function getBilingualFolderTitle(fc, lang) {
    if (!fc) return '';
    if (lang === 'ja' || !lang) return fc.title;
    const trans = fc.trans ? (fc.trans[lang] || fc.trans.en) : null;
    if (!trans || trans === fc.title) return fc.title;
    return `${fc.title} (${trans})`;
  }

  // Render vertical bullet / hierarchical folder tree (PC版 縦の箇条書きスタイル)
  function renderSidebarFolderTree() {
    const container = document.getElementById('sidebarFolderListContainer');
    if (!container) return;
    container.innerHTML = '';

    const sectionsCatalog = window.SECTIONS_DATA || [];
    const sectionsMap = window.SECTIONS || {};

    FOLDER_CONFIGS.forEach(fc => {
      const isExpanded = expandedFolderIds.has(fc.id);
      const folderCards = vocabList.filter(c => c.folder_id === fc.id);
      const bilingualFolderTitle = getBilingualFolderTitle(fc, currentLang);

      // Folder Item Container
      const folderWrapper = document.createElement('div');
      folderWrapper.className = 'border border-softBorder rounded-2xl bg-white shadow-2xs overflow-hidden transition-all shrink-0';

      // Folder Header
      const headerDiv = document.createElement('div');
      headerDiv.className = 'px-3 py-2.5 bg-slate-50/80 hover:bg-lightBlueBg/40 cursor-pointer flex items-center justify-between transition select-none';
      headerDiv.innerHTML = `
        <div class="flex items-center space-x-2 truncate pr-2">
          <i data-lucide="${isExpanded ? 'folder-open' : 'folder'}" class="w-4 h-4 text-deepNavy shrink-0"></i>
          <div class="truncate">
            <span class="text-xs font-bold text-darkNavyText truncate">${bilingualFolderTitle}</span>
            <span class="text-[10px] text-slate-400 font-medium ml-1">(${folderCards.length}語)</span>
          </div>
        </div>
        <div class="flex items-center space-x-1 shrink-0">
          <button class="btn-folder-play p-1 text-deepNavy hover:bg-white rounded-lg transition" title="Study this entire folder">
            <i data-lucide="play" class="w-3.5 h-3.5 fill-deepNavy text-deepNavy"></i>
          </button>
          <button class="btn-folder-test p-1 text-emerald-600 hover:bg-white rounded-lg transition" title="Quiz this folder">
            <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-600"></i>
          </button>
          <i data-lucide="${isExpanded ? 'chevron-up' : 'chevron-down'}" class="w-4 h-4 text-slate-400"></i>
        </div>
      `;

      // Click header toggles folder collapse
      headerDiv.addEventListener('click', (e) => {
        if (e.target.closest('.btn-folder-play')) {
          e.stopPropagation();
          currentFolder = fc.id;
          startStudyingEntireFolder();
          renderSidebarFolderTree();
          return;
        }
        if (e.target.closest('.btn-folder-test')) {
          e.stopPropagation();
          currentFolder = fc.id;
          startQuizWithScope('folder', fc.id, fc.title);
          return;
        }
        if (expandedFolderIds.has(fc.id)) {
          expandedFolderIds.delete(fc.id);
        } else {
          expandedFolderIds.clear(); expandedFolderIds.add(fc.id);
        }
        renderSidebarFolderTree();
      });

      folderWrapper.appendChild(headerDiv);

      // Units Bullet List inside Folder
      if (isExpanded) {
        const unitsContainer = document.createElement('div');
        unitsContainer.className = 'py-1 px-1.5 space-y-0.5 border-t border-slate-100 bg-white max-h-[340px] sm:max-h-[400px] overflow-y-auto overscroll-contain units-scroll-container';

        const [minSec, maxSec] = fc.range;
        // For folder_1, also check for Section 0 (まずは授業で使う単語を覚えよう！)
        const secNumsToRender = [];
        if (fc.id === 'folder_1') {
          secNumsToRender.push(0);
        }
        for (let s = minSec; s <= maxSec; s++) {
          secNumsToRender.push(s);
        }

        secNumsToRender.forEach(secNum => {
          const secInfo = getCatalogSection(secNum);
          const rawSecTitle = (secInfo && secInfo.title) || `${secNum}. 単元${secNum}`;
          const bilingualTitle = getBilingualSectionTitle(secNum, rawSecTitle, currentLang);
          const count = vocabList.filter(c => Number(c.section_num) === Number(secNum)).length;
          const isCurrentActive = (Number(currentSection) === Number(secNum) && currentFolder === fc.id);
          const numDisplay = secNum === 0 ? '★' : `${secNum}`;

          const unitItem = document.createElement('div');
          unitItem.className = `group flex items-center justify-between px-2.5 py-1.5 rounded-xl cursor-pointer transition text-xs ${
            isCurrentActive 
              ? 'bg-lightBlueBg/70 text-deepNavy font-bold border border-softBorder shadow-2xs' 
              : 'text-slate-700 hover:bg-slate-50 font-medium'
          }`;

          unitItem.innerHTML = `
            <div class="flex items-center space-x-2 truncate pr-2">
              <span class="w-1.5 h-1.5 rounded-full ${isCurrentActive ? 'bg-deepNavy' : 'bg-slate-300 group-hover:bg-coralPink'}"></span>
              <span class="text-[11px] font-bold text-slate-400 w-4 text-center">${numDisplay}</span>
              <span class="truncate text-[11px]">${bilingualTitle}</span>
            </div>
            <div class="flex items-center space-x-1 shrink-0">
              <span class="text-[9px] px-1.5 py-0.2 rounded-full font-bold ${isCurrentActive ? 'bg-deepNavy text-white' : 'bg-slate-100 text-slate-500'}">${count}語</span>
              <i data-lucide="chevron-right" class="w-3 h-3 text-slate-300 group-hover:text-deepNavy transition"></i>
            </div>
          `;

          unitItem.addEventListener('click', () => {
            currentFolder = fc.id;
            startStudyingSection(secNum, rawSecTitle);
            renderSidebarFolderTree();
          });

          unitsContainer.appendChild(unitItem);
        });

        folderWrapper.appendChild(unitsContainer);
      }

      container.appendChild(folderWrapper);
    });

    lucide.createIcons({ root: container });
  }

  // Render unified search results both into Dropdown (Mobile/PC instant preview) and Sidebar (PC tree)
  // Helper to calculate relevance score for search query
  function calculateSearchRelevance(item, rawQuery, hiraQuery) {
    let score = 0;
    const w = (item.word || '').toLowerCase();
    const r = (item.reading || '').toLowerCase();
    const rHira = toHiragana(r);
    const wHira = toHiragana(w);

    // Exact match on word or reading (highest priority)
    if (w === rawQuery || r === rawQuery || wHira === hiraQuery || rHira === hiraQuery) {
      score += 10000;
    } else if (w.startsWith(rawQuery) || r.startsWith(rawQuery) || wHira.startsWith(hiraQuery) || rHira.startsWith(hiraQuery)) {
      score += 5000;
    } else if (w.includes(rawQuery) || r.includes(rawQuery) || wHira.includes(hiraQuery) || rHira.includes(hiraQuery)) {
      score += 2000;
    }

    // Meaning matches (English, Chinese, etc.)
    const meaningObj = item.meaning || {};
    const meaningsList = Object.values(meaningObj).filter(Boolean);
    const combinedMeanings = meaningsList.join(' ').toLowerCase();

    // Check individual meanings or words
    let exactMeaningMatch = false;
    let wordBoundaryMatch = false;

    // Regex for word boundary in English/alphabetic queries (e.g., "\bcat\b")
    const isAlpha = /^[a-zA-Z0-9\s]+$/.test(rawQuery);
    const boundRegex = isAlpha ? new RegExp(`\\b${rawQuery.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\\b`, 'i') : null;

    for (const m of meaningsList) {
      const mStr = String(m).toLowerCase();
      // Split by comma or semicolon
      const subMeanings = mStr.split(/[,;\/|]/).map(s => s.trim());
      for (const sm of subMeanings) {
        if (sm === rawQuery) {
          exactMeaningMatch = true;
          break;
        }
      }
      if (boundRegex && boundRegex.test(mStr)) {
        wordBoundaryMatch = true;
      }
    }

    if (exactMeaningMatch) {
      score += 8000;
    } else if (wordBoundaryMatch) {
      score += 4000;
    } else if (combinedMeanings.startsWith(rawQuery)) {
      score += 3000;
    } else if (combinedMeanings.includes(rawQuery)) {
      score += 1500;
    }

    // Example sentence matches
    const exJa = (item.example && item.example.ja ? item.example.ja.replace(/<[^>]+>/g, '') : '').toLowerCase();
    const exJaHira = toHiragana(exJa);
    if (exJa.includes(rawQuery) || exJaHira.includes(hiraQuery)) {
      score += 300;
    }
    const exTrans = Object.values(item.example || {}).join(' ').toLowerCase();
    if (exTrans.includes(rawQuery)) {
      score += 200;
    }

    // Boost curriculum cards slightly over dictionary entries when scores are comparable
    if (!item.isDict) {
      score += 50;
    }

    // Prefer shorter words when matching query (e.g., "cat" -> "猫" over long expressions)
    if (w.length > 0 && score > 0) {
      score += Math.max(0, 30 - w.length);
    }

    return score;
  }

  // Render unified search results both into Dropdown (Mobile/PC instant preview) and Sidebar (PC tree)
  function renderUnifiedSearchResults(rawQuery) {
    const sidebarContainer = document.getElementById('sidebarFolderListContainer');
    const dropdownContainer = document.getElementById('searchDropdownContainer');

    const hiraQuery = toHiragana(rawQuery);

    // 1. Search Curriculum Words (shared by everyone)
    let curFiltered = vocabList.map(c => {
      const score = calculateSearchRelevance(c, rawQuery, hiraQuery);
      return { card: c, score };
    }).filter(item => item.score > 0);

    // 2. Search Current Student's Personal My List ONLY
    const studentMylistCards = getMylistCards();
    const curriculumIds = new Set(vocabList.map(c => c.id));
    const curriculumWords = new Set(vocabList.map(c => c.word));
    let mylistFiltered = [];
    studentMylistCards.forEach(c => {
      if (!c || curriculumIds.has(c.id) || curriculumWords.has(c.word)) return;
      const score = calculateSearchRelevance(c, rawQuery, hiraQuery);
      if (score > 0) {
        // Boost relevance so the student's own learned words appear prominently
        mylistFiltered.push({ card: c, score: score + 120 });
      }
    });

    // 3. Search Dictionary Words
    const dictSource = window.DICT_DATA || [];
    const exMap = window.DICT_EXAMPLES_MAP || {};
    const knownWords = new Set([
      ...vocabList.map(c => c.word),
      ...studentMylistCards.map(c => c.word)
    ]);

    let dictFiltered = [];
    for (let idx = 0; idx < dictSource.length; idx++) {
      const entry = dictSource[idx];
      if (knownWords.has(entry.w)) continue;

      const w = (entry.w || '').toLowerCase();
      const r = (entry.r || '').toLowerCase();
      const mList = (entry.m || []).join(' ').toLowerCase();
      const zhList = (entry.zh || []).join(' ').toLowerCase();
      const frList = (entry.fr || []).join(' ').toLowerCase();

      if (
        w.includes(rawQuery) ||
        r.includes(rawQuery) ||
        w.includes(hiraQuery) ||
        r.includes(hiraQuery) ||
        mList.includes(rawQuery) ||
        zhList.includes(rawQuery) ||
        frList.includes(rawQuery)
      ) {
        const matchedEx = exMap[entry.w] || (entry.r ? exMap[entry.r] : null);
        const dictCard = {
          id: `dict_${entry.w}_${idx}`,
          word: entry.w,
          reading: entry.r || entry.w,
          category: entry.l ? `JLPT ${entry.l}` : '辞書',
          section_title: '日本語大辞書',
          meaning: {
            en: (entry.m && entry.m.join(', ')) || '—',
            zh_TW: (entry.zh && entry.zh.join(', ')) || (entry.m && entry.m.join(', ')) || '—',
            zh_CN: (entry.zh && entry.zh.join(', ')) || (entry.m && entry.m.join(', ')) || '—',
            ko: (entry.m && entry.m.join(', ')) || '—',
            zh_HK: (entry.zh && entry.zh.join(', ')) || (entry.m && entry.m.join(', ')) || '—',
            fr: (entry.fr && entry.fr.join(', ')) || (entry.m && entry.m.join(', ')) || '—'
          },
          example: {
            ja: matchedEx ? matchedEx.ja : '',
            en: matchedEx ? (matchedEx.en || '') : ''
          },
          related: `【品詞】${entry.p || '一般'} / 【JLPT】${entry.l || '一般'}`,
          isDict: true
        };
        const score = calculateSearchRelevance(dictCard, rawQuery, hiraQuery);
        dictFiltered.push({ card: dictCard, score });
        if (dictFiltered.length >= 120) break; // Keep search fast
      }
    }

    // Combine and sort strictly by relevance score descending
    const allScored = [...curFiltered, ...mylistFiltered, ...dictFiltered];
    allScored.sort((a, b) => b.score - a.score);

    const results = allScored.map(item => item.card);

    // Save previous scroll position of dropdown before re-rendering
    const prevScrollTop = dropdownContainer ? dropdownContainer.scrollTop : 0;

    // Build DOM elements for a given container
    function populateContainer(targetDom, isDropdown = false) {
      if (!targetDom) return;
      targetDom.innerHTML = '';

      const summaryHeader = document.createElement('div');
      summaryHeader.className = 'px-3 py-1.5 text-xs sm:text-sm font-bold text-slate-600 flex items-center justify-between border-b border-slate-200 pb-2';
      summaryHeader.innerHTML = `
        <div class="flex items-center space-x-1.5">
          <span>${currentLang === 'ja' ? '検索結果' : 'Search Results'}: <strong class="text-coralPink font-black text-sm sm:text-base">${results.length}</strong> ${currentLang === 'ja' ? '件' : 'words'}</span>
        </div>
        <div class="flex items-center space-x-2">
          <span class="text-[11px] sm:text-xs text-slate-400 hidden sm:inline">${currentLang === 'ja' ? 'タップで詳細・例文・学習' : 'Tap for details'}</span>
          <button class="btn-close-dropdown px-3 py-1 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold flex items-center space-x-1 transition">
            <i data-lucide="x" class="w-3.5 h-3.5"></i>
            <span>${currentLang === 'ja' ? '閉じる' : 'Close'}</span>
          </button>
        </div>
      `;
      const btnCloseDrop = summaryHeader.querySelector('.btn-close-dropdown');
      if (btnCloseDrop) {
        btnCloseDrop.addEventListener('click', (e) => {
          e.stopPropagation();
          const topSearch = document.getElementById('globalTopSearchInput');
          const clearTopBtn = document.getElementById('btnClearTopSearch');
          const dropdown = document.getElementById('searchDropdownContainer');
          if (topSearch) topSearch.value = '';
          if (clearTopBtn) clearTopBtn.classList.add('hidden');
          if (dropdown) dropdown.classList.add('hidden');
          sidebarSearchQuery = '';
          if (isSearchStudyMode) {
            backToFolderOverview();
          }
        });
      }
      targetDom.appendChild(summaryHeader);

      if (results.length === 0) {
        const emptyDiv = document.createElement('div');
        emptyDiv.className = 'text-center py-10 text-slate-400 text-sm';
        emptyDiv.innerHTML = `
          <i data-lucide="search-x" class="w-8 h-8 mx-auto mb-2 text-slate-300"></i>
          <p class="font-bold">${currentLang === 'ja' ? '一致する単語が見つかりませんでした' : 'No matching words found'}</p>
        `;
        targetDom.appendChild(emptyDiv);
        lucide.createIcons({ root: targetDom });
        return;
      }

      results.slice(0, 100).forEach(card => {
        const isStarred = mylistSet.has(card.id) || mylistSet.has(card.word);
        const isExpanded = expandedWordId === card.id;

        let displayCategory = card.category || (card.isDict ? '辞書' : '一般');
        if (displayCategory === '授業で習った言葉' && !isStarred) {
          displayCategory = card.isDict ? '辞書' : '一般';
        }

        const itemCard = document.createElement('div');
        itemCard.className = `rounded-2xl border transition-all overflow-hidden ${
          isExpanded
            ? 'bg-blue-50/60 border-deepNavy shadow-md'
            : 'bg-white border-slate-200 hover:border-softBorder hover:bg-slate-50'
        }`;

        const targetMeaning = getBilingualMeaning(card.meaning, currentLang);
        const targetExTrans = getBilingualExampleTrans(card.example, currentLang);

        itemCard.innerHTML = `
          <div class="search-item-header p-3 sm:p-3.5 flex items-center justify-between cursor-pointer select-none">
            <div class="flex-1 min-w-0 pr-2 pointer-events-none">
              <div class="flex items-baseline flex-wrap gap-x-2 gap-y-0.5">
                <span class="text-base sm:text-lg font-black text-darkNavyText font-jp leading-tight">${card.word}</span>
                ${card.reading && card.reading !== card.word ? `<span class="text-xs sm:text-sm font-bold text-coralPink font-jp">（${card.reading}）</span>` : ''}
                ${displayCategory ? `<span class="text-[10px] sm:text-xs px-2 py-0.5 rounded-full font-bold ${card.isDict ? 'bg-slate-100 text-slate-600' : 'bg-lightBlueBg text-deepNavy'}">${displayCategory}</span>` : ''}
              </div>
              <p class="text-xs sm:text-sm text-slate-700 font-medium leading-snug truncate mt-1">${targetMeaning}</p>
            </div>
            <div class="flex items-center space-x-1 sm:space-x-1.5 shrink-0">
              <button class="btn-play-card p-2 rounded-full hover:bg-slate-100 text-deepNavy transition active:scale-95" title="${currentLang === 'ja' ? 'カードで学習' : 'Study Card'}">
                <i data-lucide="play" class="w-4 h-4 fill-deepNavy"></i>
              </button>
              <button class="btn-search-star p-2 rounded-full hover:bg-slate-100 text-slate-300 hover:text-amber-400 transition active:scale-95" title="マイリスト">
                <i data-lucide="star" class="w-4 h-4 ${isStarred ? 'fill-amber-400 text-amber-400' : ''}"></i>
              </button>
              <div class="p-1.5 rounded-full text-slate-400">
                <i data-lucide="${isExpanded ? 'chevron-up' : 'chevron-down'}" class="w-4 h-4"></i>
              </div>
            </div>
          </div>

          <div class="${isExpanded ? 'block' : 'hidden'} px-3.5 pb-3.5 pt-2 border-t border-softBorder/60 bg-white/90 space-y-2.5">
            <div class="rounded-xl p-3 bg-lightBlueBg/40 border border-softBorder/60 flex items-center justify-between">
              <div>
                <span class="text-xs font-bold text-deepNavy uppercase block mb-0.5">${currentLang === 'ja' ? '意味・訳' : 'Meaning / Translation'}</span>
                <p class="text-sm sm:text-base font-black text-darkNavyText leading-snug">${targetMeaning}</p>
              </div>
              <button class="btn-audio-word p-1.5 rounded-full bg-deepNavy text-white hover:opacity-90 shadow-2xs active:scale-95 transition" title="音声">
                <i data-lucide="volume-2" class="w-4 h-4"></i>
              </button>
            </div>

            ${card.example && card.example.ja ? `
              <div class="rounded-xl p-3 bg-slate-50 border border-slate-200">
                <div class="flex items-center justify-between mb-1.5">
                  <span class="text-xs font-bold text-slate-700 flex items-center space-x-1">
                    <i data-lucide="message-square" class="w-3.5 h-3.5 text-deepNavy"></i>
                    <span>${currentLang === 'ja' ? '例文' : 'Example'}</span>
                  </span>
                  <button class="btn-audio-example text-deepNavy hover:opacity-80 p-1 active:scale-95 transition" title="例文音声">
                    <i data-lucide="volume-2" class="w-4 h-4"></i>
                  </button>
                </div>
                <p class="text-sm sm:text-base font-bold text-slate-800 leading-relaxed font-jp mb-1.5">${card.example.ja}</p>
                ${targetExTrans ? `<p class="text-xs sm:text-sm text-slate-600 leading-relaxed">${targetExTrans}</p>` : ''}
              </div>
            ` : ''}

            ${card.related ? `
              <div class="rounded-xl p-3 bg-slate-50 border border-slate-200 text-xs sm:text-sm text-slate-700 leading-relaxed font-medium">
                <span class="font-bold text-slate-700 block mb-1">${currentLang === 'ja' ? '活用形・情報' : 'Related / Conjugations'}</span>
                ${card.related.replace(/\n/g, '<br/>')}
              </div>
            ` : ''}

            <div class="pt-1.5 flex items-center justify-end">
              <button class="btn-study-this-card px-4 py-2 rounded-full bg-deepNavy text-white font-bold text-xs sm:text-sm shadow-sm hover:opacity-90 flex items-center space-x-1.5 transition active:scale-95">
                <i data-lucide="play" class="w-3.5 h-3.5 fill-white"></i>
                <span>${currentLang === 'ja' ? 'この単語をカードで練習する' : 'Study this card'}</span>
              </button>
            </div>
          </div>
        `;

        lucide.createIcons({ root: itemCard });

        // Toggling accordion on clicking card header (excluding explicit buttons)
        const itemHeader = itemCard.querySelector('.search-item-header');
        if (itemHeader) {
          itemHeader.addEventListener('click', (e) => {
            // Ignore if clicked on play button or star button
            if (e.target.closest('.btn-play-card') || e.target.closest('.btn-search-star')) {
              return;
            }
            e.stopPropagation();
            expandedWordId = (expandedWordId === card.id) ? null : card.id;
            renderUnifiedSearchResults(rawQuery);
          });
        }

        // Voice audio buttons
        const audioWordBtn = itemCard.querySelector('.btn-audio-word');
        if (audioWordBtn) {
          audioWordBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            toggleJapaneseSpeech(card);
          });
        }
        const audioExBtn = itemCard.querySelector('.btn-audio-example');
        if (audioExBtn && card.example && card.example.ja) {
          audioExBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            toggleJapaneseSpeech(card.example.ja);
          });
        }

        // Study this card directly in flashcards view
        const studyCardHandler = (e) => {
          e.stopPropagation();
          // Hide dropdown if open
          if (dropdownContainer) dropdownContainer.classList.add('hidden');
          // Switch activeDeck to focus on this card
          isSearchStudyMode = true;
          activeDeck = [card];
          currentIndex = 0;
          switchView('flashcards');
          document.getElementById('folderOverviewPanel').classList.add('hidden');
          document.getElementById('unitListPanel').classList.add('hidden');
          document.getElementById('activeStudyHeader').classList.remove('hidden');
          document.getElementById('activeStudySectionName').textContent = card.word;
          let studyCat = displayCategory || (currentLang === 'ja' ? '検索単語' : 'Search Word');
          document.getElementById('activeStudyFolderName').textContent = studyCat;
          renderCurrentCard();
          showToast(currentLang === 'ja' ? `「${card.word}」のカードを表示しました（←で一覧に戻れます）` : `Loaded "${card.word}" flashcard (Tap ← to go back)`);
        };

        const playBtn = itemCard.querySelector('.btn-play-card');
        if (playBtn) playBtn.addEventListener('click', studyCardHandler);
        const studyThisBtn = itemCard.querySelector('.btn-study-this-card');
        if (studyThisBtn) studyThisBtn.addEventListener('click', studyCardHandler);

        // Star toggle
        const starBtn = itemCard.querySelector('.btn-search-star');
        if (starBtn) {
          starBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            promptFolderSelectAndAdd(card, () => {
              renderUnifiedSearchResults(rawQuery);
            });
          });
        }

        targetDom.appendChild(itemCard);
      });
    }

    // Populate Sidebar
    if (sidebarContainer) {
      populateContainer(sidebarContainer, false);
    }

    // Populate Dropdown under search input and show it
    if (dropdownContainer) {
      dropdownContainer.classList.remove('hidden');
      populateContainer(dropdownContainer, true);
      // Restore previous scroll position so user doesn't lose place when expanding/collapsing
      if (prevScrollTop > 0) {
        dropdownContainer.scrollTop = prevScrollTop;
      }
    }
  }

  // --- PC / Tablet / Mobile Layout (Responsive 2-Column on Desktop & Tablet, Centered on Mobile) ---
  function isTabletOrDesktop() {
    const ua = navigator.userAgent || '';
    const touchPoints = navigator.maxTouchPoints || 0;
    // iPad (including iPadOS 13+ which presents as MacIntel with touch points)
    const isIpad = (/iPad/i.test(ua)) || (/Macintosh/i.test(ua) && touchPoints > 1);
    // Android tablet: Android UA without Mobile, or containing Tablet
    const isAndroidTablet = (/Android/i.test(ua) && !/Mobile/i.test(ua)) || (/Tablet/i.test(ua));
    // Screen width: tablets / PC screens (>= 768px)
    const isWide = (window.innerWidth || 0) >= 768;
    return isIpad || isAndroidTablet || isWide;
  }

  function initLayoutMode() {
    const sidebar = document.getElementById('vocabSidebar');
    const mainContainer = document.getElementById('mainContainer');
    const viewFlashcards = document.getElementById('viewFlashcards');
    const btnMarkReview = document.getElementById('btnMarkReview');
    const btnMarkKnown = document.getElementById('btnMarkKnown');
    const containerToggleAutoAudio = document.getElementById('containerToggleAutoAudio');
    const containerToggleFurigana = document.getElementById('containerToggleFurigana');
    const btnToggleAutoAudioMobile = document.getElementById('btnToggleAutoAudioMobile');
    const btnToggleFuriganaMobile = document.getElementById('btnToggleFuriganaMobile');
    const folderOverviewPanel = document.getElementById('folderOverviewPanel');

    function applyLayout() {
      const isDesktop = isTabletOrDesktop();

      // 1. Sidebar & Main Container (2-Column on Desktop & Tablet)
      if (sidebar) {
        if (isDesktop) {
          sidebar.classList.remove('hidden');
          sidebar.classList.add('block');
        } else {
          sidebar.classList.add('hidden');
          sidebar.classList.remove('block');
        }
      }
      if (mainContainer) {
        mainContainer.className = isDesktop
          ? 'flex-1 w-full max-w-5xl mx-auto p-3 sm:p-4 transition-all'
          : 'flex-1 w-full max-w-md mx-auto p-3 sm:p-4 transition-all';
      }

      // 2. Flashcard side-by-side flex layout on PC & Tablet
      if (viewFlashcards) {
        if (isDesktop) {
          viewFlashcards.classList.remove('flex-col');
          viewFlashcards.classList.add('flex-row', 'items-start');
        } else {
          viewFlashcards.classList.remove('flex-row', 'items-start');
          viewFlashcards.classList.add('flex-col');
        }
      }

      // 3. PC-specific bottom buttons: 「もう一度！」「覚えた！」
      if (btnMarkReview) {
        if (isDesktop) {
          btnMarkReview.classList.remove('hidden');
          btnMarkReview.classList.add('flex');
        } else {
          btnMarkReview.classList.add('hidden');
          btnMarkReview.classList.remove('flex');
        }
      }
      if (btnMarkKnown) {
        if (isDesktop) {
          btnMarkKnown.classList.remove('hidden');
          btnMarkKnown.classList.add('flex');
        } else {
          btnMarkKnown.classList.add('hidden');
          btnMarkKnown.classList.remove('flex');
        }
      }

      // 4. Header Audio & Furigana Switches
      if (containerToggleAutoAudio) {
        if (isDesktop) {
          containerToggleAutoAudio.classList.remove('hidden');
          containerToggleAutoAudio.classList.add('flex');
        } else {
          containerToggleAutoAudio.classList.add('hidden');
          containerToggleAutoAudio.classList.remove('flex');
        }
      }
      if (containerToggleFurigana) {
        if (isDesktop) {
          containerToggleFurigana.classList.remove('hidden');
          containerToggleFurigana.classList.add('flex');
        } else {
          containerToggleFurigana.classList.add('hidden');
          containerToggleFurigana.classList.remove('flex');
        }
      }
      if (btnToggleAutoAudioMobile) {
        if (isDesktop) btnToggleAutoAudioMobile.classList.add('hidden');
        else btnToggleAutoAudioMobile.classList.remove('hidden');
      }
      if (btnToggleFuriganaMobile) {
        if (isDesktop) btnToggleFuriganaMobile.classList.add('hidden');
        else btnToggleFuriganaMobile.classList.remove('hidden');
      }

      // 5. Hide mobile folder overview panel when in Desktop/Tablet mode
      if (folderOverviewPanel) {
        if (isDesktop) folderOverviewPanel.classList.add('hidden');
        else if (currentNavLevel === 'folders') folderOverviewPanel.classList.remove('hidden');
      }
    }

    applyLayout();
    window.addEventListener('resize', applyLayout);
    window.addEventListener('orientationchange', () => setTimeout(applyLayout, 100));
  }

  async function setStudent(student) {
    currentStudent = student;
    const isTeacher = !!(student && (student.id === 'haku' || student.id === 'admin'));
    const drawerBtnOpenAdmin = document.getElementById('drawerBtnOpenAdmin');
    if (drawerBtnOpenAdmin) {
      if (isTeacher) {
        drawerBtnOpenAdmin.classList.remove('hidden');
      } else {
        drawerBtnOpenAdmin.classList.add('hidden');
      }
    }

    const drawerName = document.getElementById('drawerStudentName');
    const drawerStatus = document.getElementById('drawerStudentStatus');
    const drawerBtnLogin = document.getElementById('drawerBtnLogin');
    const drawerBtnLogout = document.getElementById('drawerBtnLogout');
    const btnLoginLogout = document.getElementById('btnLoginLogout');

    if (student) {
      localStorage.setItem('haku_current_student_id', student.id);
      if (window.AppAuth && typeof window.AppAuth.refreshCurrentStudent === 'function') {
        window.AppAuth.refreshCurrentStudent();
        window.AppAuth.updateAllHeaderUI();
      }
      document.getElementById('headerStudentBadge').textContent = isTeacher ? 'ハク先生 🌸' : `Student: ${student.name}`;
      // Update drawer student display
      if (drawerName) drawerName.textContent = student.name;
      if (drawerStatus) drawerStatus.textContent = isTeacher ? 'Teacher Mode 🌸' : 'Logged In';
      if (drawerBtnLogin) drawerBtnLogin.textContent = 'Switch ID';
      if (drawerBtnLogout) drawerBtnLogout.classList.remove('hidden');
      if (btnLoginLogout) btnLoginLogout.classList.remove('hidden');

      // Auto-switch language based on student profile!
      currentLang = student.lang || 'en';
      const drawerLangSelect = document.getElementById('drawerLangSelect');
      if (drawerLangSelect) drawerLangSelect.value = currentLang;

      if (!isTeacher) {
        showToast(`Logged in as ${student.name}`);
      }

      // First load local cache immediately for instantaneous UI responsiveness
      loadMylistForCurrentStudent();
      applyUiLanguage(currentLang);
      updateActiveDeck();

      // Authenticate with Firebase & sync latest cloud data safely through mutex
      try {
        await syncStudentFromCloud(student.id);
        if (isTeacher) {
          setTimeout(() => recoverLostCustomCards(), 1500);
        }
      } catch (err) {
        console.warn('setStudent cloud sync note:', err);
      }
      loadMylistForCurrentStudent();
      updateActiveDeck();
    } else {
      localStorage.removeItem('haku_current_student_id');
      if (window.AppAuth && typeof window.AppAuth.refreshCurrentStudent === 'function') {
        window.AppAuth.refreshCurrentStudent();
        window.AppAuth.updateAllHeaderUI();
      }
      document.getElementById('headerStudentBadge').textContent = 'Student: Guest';
      if (drawerName) drawerName.textContent = 'Guest';
      if (drawerStatus) drawerStatus.textContent = 'Not logged in';
      if (drawerBtnLogin) drawerBtnLogin.textContent = 'Log In';
      if (drawerBtnLogout) drawerBtnLogout.classList.add('hidden');
      if (btnLoginLogout) btnLoginLogout.classList.add('hidden');
      if (drawerBtnOpenAdmin) drawerBtnOpenAdmin.classList.add('hidden');
      if (currentView === 'admin') {
        switchView('flashcards');
      }
      if (fbAuth && fbAuth.currentUser) {
        fbAuth.signOut().catch(() => {});
      }
      loadMylistForCurrentStudent();
      applyUiLanguage(currentLang);
      updateActiveDeck();
    }
  }

  let mylistFolders = []; // array of { id, name }
  let mylistCardFolderMap = {}; // cardId -> folderId (or null for root/unfiled)
  let activeMylistFolderId = 'all'; // 'all' or folderId

  function loadMylistForCurrentStudent() {
    const studentPrefix = currentStudent ? currentStudent.id : 'guest';
    const key = `haku_mylist_${studentPrefix}`;
    const foldersKey = `haku_mylist_folders_${studentPrefix}`;
    const mapKey = `haku_mylist_card_map_${studentPrefix}`;

    const saved = localStorage.getItem(key);
    mylistSet = new Set(saved ? JSON.parse(saved) : []);

    const savedFolders = localStorage.getItem(foldersKey);
    mylistFolders = savedFolders ? JSON.parse(savedFolders) : [];

    // Ensure the default folders are always present for every student:
    // 1. "授業で習った言葉" (folder_class_words)
    // 2. "覚えた！" (folder_learned)
    // 3. "もう一度！" (folder_review)
    const CLASS_FOLDER_ID = 'folder_class_words';
    const CLASS_FOLDER_NAME = '授業で習った言葉';
    const LEARNED_FOLDER_ID = 'folder_learned';
    const LEARNED_FOLDER_NAME = '覚えた！';
    const REVIEW_FOLDER_ID = 'folder_review';
    const REVIEW_FOLDER_NAME = 'もう一度！';

    let foldersUpdated = false;
    if (!mylistFolders.find(f => f.id === CLASS_FOLDER_ID || f.name === CLASS_FOLDER_NAME)) {
      mylistFolders.unshift({ id: CLASS_FOLDER_ID, name: CLASS_FOLDER_NAME });
      foldersUpdated = true;
    }
    if (!mylistFolders.find(f => f.id === LEARNED_FOLDER_ID || f.name === LEARNED_FOLDER_NAME)) {
      mylistFolders.push({ id: LEARNED_FOLDER_ID, name: LEARNED_FOLDER_NAME });
      foldersUpdated = true;
    }
    if (!mylistFolders.find(f => f.id === REVIEW_FOLDER_ID || f.name === REVIEW_FOLDER_NAME)) {
      mylistFolders.push({ id: REVIEW_FOLDER_ID, name: REVIEW_FOLDER_NAME });
      foldersUpdated = true;
    }
    if (foldersUpdated) {
      localStorage.setItem(foldersKey, JSON.stringify(mylistFolders));
    }

    const savedMap = localStorage.getItem(mapKey);
    mylistCardFolderMap = savedMap ? JSON.parse(savedMap) : {};

    // Exact Google Doc Tab Word Mappings per Student
    // 1: みどりさん (0012) -> class_word_0001 ~ class_word_0289 (289 words)
    // 2: Keyvinさん (0011) -> class_word_0290 ~ class_word_0498 (209 words)
    // 3: ななさん (0013) -> class_word_0499 ~ class_word_0538 (40 words)
    // 4: Danielさん (0014) -> class_word_0539 ~ class_word_0639 (101 words)
    // 5: Stephenさん (0015) -> class_word_0640 ~ class_word_0873 (234 words)
    // 6: ジウンさん (0016) -> class_word_0874 ~ class_word_1144 (271 words)
    // 7: ハンウさん (0017) -> class_word_1145 ~ class_word_1213 (69 words)
    // 8: Justinさん (0018) -> class_word_1214 ~ class_word_1232 (19 words)
    // 9: ミンギさん (0019) -> class_word_1233 ~ class_word_1314 (82 words)
    // 10: Colinさん (0020) -> class_word_1315 ~ class_word_1397 (83 words)
    // 11: ともやさん (0021) -> class_word_1398 ~ class_word_1598 (201 words)
    // 12: 生徒22 (0022) -> class_word_1599 ~ class_word_1602 (追加語彙)
    const STUDENT_DOC_RANGES = {
      '0012': [1, 289],
      '0011': [290, 498],
      '0013': [499, 538],
      '0014': [539, 639],
      '0015': [640, 873],
      '0016': [874, 1144],
      '0017': [1145, 1213],
      '0018': [1214, 1232],
      '0019': [1233, 1314],
      '0020': [1315, 1397],
      '0021': [1398, 1598],
      '0022': [1599, 1602]
    };

    const studentRange = STUDENT_DOC_RANGES[studentPrefix];
    if (studentRange) {
      let needsSave = false;
      const [startNum, endNum] = studentRange;
      for (let num = startNum; num <= endNum; num++) {
        const cId = `class_word_${String(num).padStart(4, '0')}`;
        if (!mylistSet.has(cId)) {
          mylistSet.add(cId);
          needsSave = true;
        }
        if (!mylistCardFolderMap[cId]) {
          mylistCardFolderMap[cId] = CLASS_FOLDER_ID;
          needsSave = true;
        }
      }
      if (studentPrefix === '0012') {
        const mCardId = 'card_1791393927923_pd4xbi';
        if (!mylistSet.has(mCardId)) {
          mylistSet.add(mCardId);
          needsSave = true;
        }
        if (!mylistCardFolderMap[mCardId]) {
          mylistCardFolderMap[mCardId] = CLASS_FOLDER_ID;
          needsSave = true;
        }
        // Ensure Midori's curated cards are present
        MIDORI_NEW_CARD_IDS.forEach(id => {
          if (!mylistSet.has(id)) {
            mylistSet.add(id);
            needsSave = true;
          }
          if (!mylistCardFolderMap[id]) {
            mylistCardFolderMap[id] = CLASS_FOLDER_ID;
            needsSave = true;
          }
        });
      }
      if (currentStudent && currentStudent.id === '0014') {
        DANIEL_NEW_CARD_IDS.forEach(id => {
          if (!mylistSet.has(id)) {
            mylistSet.add(id);
            needsSave = true;
          }
          if (!mylistCardFolderMap[id]) {
            mylistCardFolderMap[id] = CLASS_FOLDER_ID;
            needsSave = true;
          }
        });
      }

      // Universal self-healing: automatically purge any corrupted/dialect card from this student's mylist
      Array.from(mylistSet).forEach(cId => {
        const card = getCardById(cId);
        if (card && isCorruptedCard(card)) {
          mylistSet.delete(cId);
          delete mylistCardFolderMap[cId];
          needsSave = true;
        }
      });

      if (needsSave) {
        localStorage.setItem(key, JSON.stringify(Array.from(mylistSet)));
        localStorage.setItem(mapKey, JSON.stringify(mylistCardFolderMap));
      }
    } else if (studentPrefix === '0023') {
      let needsSave = false;
      if (typeof ARUN_NEW_CARD_IDS !== 'undefined') {
        ARUN_NEW_CARD_IDS.forEach(cId => {
          if (!mylistSet.has(cId)) {
            mylistSet.add(cId);
            needsSave = true;
          }
          if (!mylistCardFolderMap[cId]) {
            mylistCardFolderMap[cId] = CLASS_FOLDER_ID;
            needsSave = true;
          }
        });
      }
      if (window.CLASS_ARUN_IDS) {
        window.CLASS_ARUN_IDS.forEach(cId => {
          if (!mylistSet.has(cId)) {
            mylistSet.add(cId);
            needsSave = true;
          }
          if (!mylistCardFolderMap[cId]) {
            mylistCardFolderMap[cId] = CLASS_FOLDER_ID;
            needsSave = true;
          }
        });
      }
      if (needsSave) {
        localStorage.setItem(key, JSON.stringify(Array.from(mylistSet)));
        localStorage.setItem(mapKey, JSON.stringify(mylistCardFolderMap));
      }
    } else if (studentPrefix === '0010' && typeof ELIIE_CURATED_CARDS !== 'undefined') {
      let needsSave = false;
      ELIIE_NEW_CARD_IDS.forEach(cId => {
        if (!mylistSet.has(cId)) {
          mylistSet.add(cId);
          needsSave = true;
        }
        if (!mylistCardFolderMap[cId]) {
          mylistCardFolderMap[cId] = CLASS_FOLDER_ID;
          needsSave = true;
        }
      });
      if (needsSave) {
        localStorage.setItem(key, JSON.stringify(Array.from(mylistSet)));
        localStorage.setItem(mapKey, JSON.stringify(mylistCardFolderMap));
      }
    }

    // Universal self-healing & strict deduplication for any student
    let needsCleanSave = false;

    // 1. Purge corrupted cards, dialect cards, and duplicate manual imports
    Array.from(mylistSet).forEach(cId => {
      const card = getCardById(cId);
      if (card && isCorruptedCard(card)) {
        mylistSet.delete(cId);
        delete mylistCardFolderMap[cId];
        needsCleanSave = true;
      }
    });

    // 2. Strict Deduplication by Japanese Word across My List
    // If multiple cards share the exact same Japanese word, keep only the highest quality/canonical card
    const wordCardMap = new Map();
    Array.from(mylistSet).forEach(cId => {
      const card = getCardById(cId);
      if (!card || isStubCard(card)) return;
      const w = (card.word || '').trim();
      if (!w) return;

      if (!wordCardMap.has(w)) {
        wordCardMap.set(w, { id: cId, card });
      } else {
        const existing = wordCardMap.get(w);
        const getScore = (id, c) => {
          if ((typeof MIDORI_NEW_CARD_IDS !== 'undefined' && MIDORI_NEW_CARD_IDS.includes(id)) ||
              (typeof DANIEL_NEW_CARD_IDS !== 'undefined' && DANIEL_NEW_CARD_IDS.includes(id)) ||
              (typeof ELIIE_NEW_CARD_IDS !== 'undefined' && ELIIE_NEW_CARD_IDS.includes(id))) return 1000;
          if (id && id.startsWith('card_')) {
            const exLen = (c && c.example && c.example.ja) ? c.example.ja.length : 0;
            return 600 + exLen;
          }
          if (id && id.startsWith('class_word_')) {
            const exLen = (c && c.example && c.example.ja) ? c.example.ja.length : 0;
            return 500 + exLen;
          }
          if (id && id.startsWith('seed_')) return 400;
          let s = 100;
          if (c && c.example && c.example.ja && !c.example.ja.includes('(')) s += 50;
          return s;
        };

        const newScore = getScore(cId, card);
        const oldScore = getScore(existing.id, existing.card);

        if (newScore > oldScore) {
          // Replace with better card
          mylistSet.delete(existing.id);
          delete mylistCardFolderMap[existing.id];
          wordCardMap.set(w, { id: cId, card });
        } else {
          // Keep existing card
          mylistSet.delete(cId);
          delete mylistCardFolderMap[cId];
        }
        needsCleanSave = true;
      }
    });


    if (needsCleanSave) {
      localStorage.setItem(key, JSON.stringify(Array.from(mylistSet)));
      localStorage.setItem(mapKey, JSON.stringify(mylistCardFolderMap));
    }

    updateMylistBadge();
  }

  // --- Firebase Cloud Sync Core ---
  // Authenticates student behind the scenes using internal virtual email (e.g. 0001@haku.local)
  // This satisfies Gemini's security rule: request.auth.token.email == studentId + '@haku.local'
  async function ensureStudentCloudAuth(studentId, passcode) {
    if (!isFirebaseReady || !fbAuth || !studentId || studentId === 'guest') return false;
    const virtualEmail = `${studentId.toLowerCase()}@haku.local`;
    const passwordStr = `haku_${passcode}_sec`;

    try {
      if (fbAuth.currentUser && fbAuth.currentUser.email === virtualEmail) {
        return true;
      }
      // Try sign in
      try {
        await fbAuth.signInWithEmailAndPassword(virtualEmail, passwordStr);
        return true;
      } catch (signInErr) {
        if (signInErr.code === 'auth/user-not-found' || signInErr.code === 'auth/invalid-credential' || signInErr.code === 'auth/wrong-password') {
          // Create user account if not exists
          try {
            await fbAuth.createUserWithEmailAndPassword(virtualEmail, passwordStr);
            return true;
          } catch (createErr) {
            // If already exists or error, try sign in once more
            console.warn('Firebase user creation note:', createErr.message);
          }
        }
      }
    } catch (err) {
      console.warn('Firebase student auth note:', err.message);
    }
    return !!fbAuth.currentUser;
  }

  // Sequential Promise Mutex to guarantee Firebase Auth switches never collide
  let cloudSyncMutex = Promise.resolve();
  function runWithCloudSyncLock(fn) {
    const next = cloudSyncMutex.then(() => fn().catch(err => {
      console.warn('Locked cloud sync operation error:', err);
      throw err;
    }));
    cloudSyncMutex = next.catch(() => {});
    return next;
  }

  // Push student's mylist, folders, and mapping to Cloud Firestore with explicit auth
  async function syncStudentToCloudDirect(studentId, dataToSync) {
    if (!isFirebaseReady || !fbDb || !studentId || studentId === 'guest') return false;
    const targetStudent = students.find(s => s.id === studentId) || (currentStudent && currentStudent.id === studentId ? currentStudent : null);
    if (!targetStudent) return false;
    const originalStudent = currentStudent;

    return runWithCloudSyncLock(async () => {
      try {
        // Authenticate as target student to satisfy Firestore security rules
        await ensureStudentCloudAuth(studentId, targetStudent.passcode);
        const docRef = fbDb.collection('students').doc(studentId);
        if (Array.isArray(dataToSync.customCards)) {
          try {
            const snap = await docRef.get();
            const cloudCards = (snap.exists && Array.isArray(snap.data().customCards)) ? snap.data().customCards : [];
            if (snap.exists && snap.data().wordNames) {
              dataToSync.wordNames = { ...snap.data().wordNames, ...(dataToSync.wordNames || {}) };
            }
            const haveIds = new Set(dataToSync.customCards.map(c => c.id));
            cloudCards.forEach(c => {
              if (c && c.id && !isStubCard(c) && !isCorruptedCard(c) && !haveIds.has(c.id)) {
                dataToSync.customCards.push(c);
                haveIds.add(c.id);
              }
            });
            dataToSync.customCards = dataToSync.customCards.filter(c => !isCorruptedCard(c));
          } catch (e) {}
        }
        await docRef.set(dataToSync, { merge: true });
        console.log(`Cloud sync direct pushed for student ${studentId} ☁️`);

        // Restore original session if needed
        if (originalStudent && originalStudent.id !== studentId) {
          await ensureStudentCloudAuth(originalStudent.id, originalStudent.passcode);
        }
        return true;
      } catch (err) {
        console.warn(`Cloud sync direct note for ${studentId}:`, err.message);
        if (originalStudent && originalStudent.id !== studentId) {
          try { await ensureStudentCloudAuth(originalStudent.id, originalStudent.passcode); } catch(e) {}
        }
        return false;
      }
    });
  }

  // Push student's mylist, folders, and mapping to Cloud Firestore
  async function syncStudentToCloud(studentId) {
    if (!isFirebaseReady || !fbDb || !studentId || studentId === 'guest') return;
    return runWithCloudSyncLock(async () => {
      try {
        const targetStudent = students.find(s => s.id === studentId) || currentStudent;
        const passcode = targetStudent ? targetStudent.passcode : (currentStudent ? currentStudent.passcode : '1122');
        await ensureStudentCloudAuth(studentId, passcode);

        // Gather any card objects that this student has in their mylist and aren't in INITIAL_VOCAB_DATA or CLASS_VOCAB_DATA
        const seedIds = new Set((window.INITIAL_VOCAB_DATA || []).map(c => c.id));
        const classIds = new Set((window.CLASS_VOCAB_DATA || []).map(c => c.id));
        const customCardsToSync = [];
        mylistSet.forEach(cId => {
          if (!seedIds.has(cId) && !classIds.has(cId) && !cId.startsWith('class_word_')) {
            const resolvedCard = getCardById(cId);
            if (resolvedCard && !isStubCard(resolvedCard) && !resolvedCard.isRebuilt && !isCorruptedCard(resolvedCard)) customCardsToSync.push(resolvedCard);
          }
        });

        const docRef = fbDb.collection('students').doc(studentId);

        // ★ 単語名レジストリ（定義が消えても単語名から復元できるように）
        recordWordNames(customCardsToSync);
        let wordNamesToSync = buildWordNamesFor(Array.from(mylistSet));

        // ★ クラウドに既にある正しいカード定義を消さないよう、必ずマージしてから保存
        try {
          const snap = await docRef.get();
          if (snap.exists && snap.data().wordNames) {
            mergeWordNames(snap.data().wordNames);
            wordNamesToSync = buildWordNamesFor(Array.from(mylistSet));
          }
          const cloudCards = (snap.exists && Array.isArray(snap.data().customCards)) ? snap.data().customCards : [];
          const haveIds = new Set(customCardsToSync.map(c => c.id));
          cloudCards.forEach(c => {
            if (c && c.id && !isStubCard(c) && !isCorruptedCard(c) && !haveIds.has(c.id) && mylistSet.has(c.id)) {
              customCardsToSync.push(c);
              haveIds.add(c.id);
            }
          });
        } catch (e) {}

        await docRef.set({
          mylist: Array.from(mylistSet),
          folders: mylistFolders,
          cardFolderMap: mylistCardFolderMap,
          customCards: customCardsToSync.filter(c => !isCorruptedCard(c)),
          wordNames: wordNamesToSync,
          updatedAt: firebase.firestore.FieldValue.serverTimestamp()
        }, { merge: true });
        console.log(`Cloud sync pushed for student ${studentId} ☁️`);
      } catch (err) {
        console.warn('Cloud sync push note:', err.message);
      }
    });
  }

  // Pull student's mylist, folders, and mapping from Cloud Firestore
  async function syncStudentFromCloud(studentId) {
    if (!isFirebaseReady || !fbDb || !studentId || studentId === 'guest') return false;
    return runWithCloudSyncLock(async () => {
      try {
        // Ensure user is authenticated first
        const targetStudent = students.find(s => s.id === studentId) || currentStudent;
        const passcode = targetStudent ? targetStudent.passcode : (currentStudent ? currentStudent.passcode : '1122');
        await ensureStudentCloudAuth(studentId, passcode);

      const docRef = fbDb.collection('students').doc(studentId);
      const snap = await docRef.get();
      if (snap.exists) {
        const data = snap.data();
        let changed = false;

        // 1. Sync custom card definitions (e.g. newly imported cards from PC)
        if (Array.isArray(data.customCards) && data.customCards.length > 0) {
          let vocabChanged = false;
          let storedCustom = [];
          try {
            storedCustom = JSON.parse(localStorage.getItem('haku_all_custom_cards') || '[]');
          } catch(e) { storedCustom = []; }

          const classIds = new Set((window.CLASS_VOCAB_DATA || []).map(c => c.id));
          const seedIds = new Set((window.INITIAL_VOCAB_DATA || []).map(c => c.id));
          data.customCards.forEach(card => {
            if (!card || isStubCard(card) || isCorruptedCard(card)) return;
            if (card && card.id && !card.isRebuilt && !classIds.has(card.id) && !seedIds.has(card.id) && !card.id.startsWith('class_word_')) {
              card.isCustom = true;
              const vIdx = vocabList.findIndex(c => c.id === card.id);
              if (vIdx >= 0 && isStubCard(vocabList[vIdx])) {
                vocabList[vIdx] = card;
                vocabChanged = true;
              } else if (vIdx < 0) {
                vocabList.push(card);
                vocabChanged = true;
              }
              const sIdx = storedCustom.findIndex(c => c.id === card.id);
              if (sIdx >= 0) {
                storedCustom[sIdx] = isStubCard(storedCustom[sIdx]) ? card : { ...storedCustom[sIdx], ...card };
              } else {
                storedCustom.push(card);
                vocabChanged = true;
              }
            }
          });
          if (vocabChanged) {
            localStorage.setItem('haku_vocab_data', JSON.stringify(vocabList));
            localStorage.setItem('haku_all_custom_cards', JSON.stringify(storedCustom));
            changed = true;
          }
        }

        // 1b. Sync word-name registry
        if (data.wordNames && typeof data.wordNames === 'object') {
          if (mergeWordNames(data.wordNames)) changed = true;
        }

        // 2. Sync mylist IDs（先生が削除した単語は端末からも消す）
        const removedSet = new Set(Array.isArray(data.removedIds) ? data.removedIds : []);
        removedSet.forEach(id => { if (mylistSet.has(id)) { mylistSet.delete(id); changed = true; } });
        if (Array.isArray(data.mylist)) {
          data.mylist.filter(id => !removedSet.has(id)).forEach(id => {
            const c = getCardById(id);
            if (c && isCorruptedCard(c)) return;
            if (!mylistSet.has(id)) {
              mylistSet.add(id);
              changed = true;
            }
          });
        }

        // 3. Sync custom folders
        if (Array.isArray(data.folders) && data.folders.length > 0) {
          data.folders.forEach(f => {
            if (!mylistFolders.find(ex => ex.id === f.id)) {
              mylistFolders.push(f);
              changed = true;
            }
          });
        }

        // 4. Sync card to folder mapping
        if (data.cardFolderMap && typeof data.cardFolderMap === 'object') {
          Object.assign(mylistCardFolderMap, data.cardFolderMap);
          changed = true;
        }

        // 5. Strict Word Deduplication after cloud pull
        const wordCardMap = new Map();
        Array.from(mylistSet).forEach(cId => {
          const card = getCardById(cId);
          if (!card || isStubCard(card) || isCorruptedCard(card)) {
            if (card && isCorruptedCard(card)) {
              mylistSet.delete(cId);
              delete mylistCardFolderMap[cId];
              changed = true;
            }
            return;
          }
          const w = (card.word || '').trim();
          if (!w) return;
          if (!wordCardMap.has(w)) {
            wordCardMap.set(w, { id: cId, card });
          } else {
            const existing = wordCardMap.get(w);
            const getScore = (id, c) => {
              if ((typeof MIDORI_NEW_CARD_IDS !== 'undefined' && MIDORI_NEW_CARD_IDS.includes(id)) ||
                  (typeof DANIEL_NEW_CARD_IDS !== 'undefined' && DANIEL_NEW_CARD_IDS.includes(id)) ||
                  (typeof ELIIE_NEW_CARD_IDS !== 'undefined' && ELIIE_NEW_CARD_IDS.includes(id))) return 1000;
              if (id && id.startsWith('card_')) return 600 + ((c && c.example && c.example.ja) ? c.example.ja.length : 0);
              if (id && id.startsWith('class_word_')) return 500 + ((c && c.example && c.example.ja) ? c.example.ja.length : 0);
              if (id && id.startsWith('seed_')) return 400;
              return 100;
            };
            if (getScore(cId, card) > getScore(existing.id, existing.card)) {
              mylistSet.delete(existing.id);
              delete mylistCardFolderMap[existing.id];
              wordCardMap.set(w, { id: cId, card });
            } else {
              mylistSet.delete(cId);
              delete mylistCardFolderMap[cId];
            }
            changed = true;
          }
        });

        // Hoist any custom cards to the top of newest sort
        const dynamicCustomCards = Array.from(mylistSet).filter(id => {
          return !id.startsWith('class_word_') && 
                 !(typeof MIDORI_NEW_CARD_IDS !== 'undefined' && MIDORI_NEW_CARD_IDS.includes(id)) &&
                 !(typeof DANIEL_NEW_CARD_IDS !== 'undefined' && DANIEL_NEW_CARD_IDS.includes(id)) &&
                 !(typeof ELIIE_NEW_CARD_IDS !== 'undefined' && ELIIE_NEW_CARD_IDS.includes(id));
        });
        if (dynamicCustomCards.length > 0) {
          dynamicCustomCards.forEach(id => {
            mylistSet.delete(id);
            mylistSet.add(id);
          });
          changed = true;
        }

        if (changed) {
          // Update local cache
          const key = `haku_mylist_${studentId}`;
          const foldersKey = `haku_mylist_folders_${studentId}`;
          const mapKey = `haku_mylist_card_map_${studentId}`;
          localStorage.setItem(key, JSON.stringify(Array.from(mylistSet)));
          localStorage.setItem(foldersKey, JSON.stringify(mylistFolders));
          localStorage.setItem(mapKey, JSON.stringify(mylistCardFolderMap));
          console.log(`Cloud data successfully synced down for ${studentId}! ☁️✨`);
        }
        updateMylistBadge();
        const mylistViewElem = document.getElementById('viewMylist');
        if (mylistViewElem && !mylistViewElem.classList.contains('hidden')) {
          renderMylistView();
        }
        return changed;
      }
      return false;
    } catch (err) {
      console.warn('Cloud sync pull note:', err.message);
      return false;
    }
  });
}

  // ★ 先生ログイン時: 失われたカード定義を「先生PCの保存データ＋全生徒のクラウドデータ」から集めて復元し、
  //    定義が欠けている生徒のクラウドへ配り直す（マイリストのランダムID文字化けの修復）
  let isRecoveringCards = false;
  async function recoverLostCustomCards() {
    if (isRecoveringCards || !isFirebaseReady || !fbDb) return;
    isRecoveringCards = true;
    const teacher = currentStudent;
    try {
      const pool = new Map();
      const addToPool = (c) => { if (c && c.id && !isStubCard(c) && !pool.has(c.id)) pool.set(c.id, c); };

      // 1. この端末に保存されている正しい定義
      let storedCustom = [];
      try { storedCustom = JSON.parse(localStorage.getItem('haku_all_custom_cards') || '[]'); } catch (e) {}
      storedCustom.forEach(c => {
        if (c && c.id && isCustomCardId(c.id) && c.section_num === undefined && !isStubCard(c)) {
          addToPool(c);
        }
      });
      vocabList.forEach(c => {
        if (c && c.id && isCustomCardId(c.id) && c.section_num === undefined && !isStubCard(c)) {
          addToPool(c);
        }
      });

      // 2. 全生徒のクラウドデータ
      const docsById = {};
      for (const st of students) {
        if (!st || !st.id || st.id === 'haku' || st.id === 'admin') continue;
        try {
          await ensureStudentCloudAuth(st.id, st.passcode);
          const snap = await fbDb.collection('students').doc(st.id).get();
          if (snap.exists) {
            const d = snap.data();
            docsById[st.id] = d;
            (d.customCards || []).forEach(c => {
              if (c && c.id && isCustomCardId(c.id) && c.section_num === undefined && !isStubCard(c)) {
                addToPool(c);
              }
            });
            if (d.wordNames) mergeWordNames(d.wordNames);
          }
        } catch (e) {}
      }

      // 3. この端末のダミーを削除し、正しい定義で上書き（教材カードは絶対に混入させない）
      const cleaned = storedCustom.filter(c => !isStubCard(c) && isCustomCardId(c.id) && c.section_num === undefined);
      pool.forEach(c => {
        if (c && c.id && isCustomCardId(c.id) && c.section_num === undefined && !cleaned.find(x => x.id === c.id)) {
          cleaned.push(c);
        }
      });
      localStorage.setItem('haku_all_custom_cards', JSON.stringify(cleaned));

      vocabList = vocabList.filter(c => !isStubCard(c));
      const existingVocabIds = new Set(vocabList.map(c => c.id));
      pool.forEach(c => {
        if (c && c.id && isCustomCardId(c.id) && c.section_num === undefined && !existingVocabIds.has(c.id)) {
          vocabList.push({ ...c, isCustom: true });
          existingVocabIds.add(c.id);
        }
      });
      localStorage.setItem('haku_vocab_data', JSON.stringify(vocabList));

      recordWordNames(Array.from(pool.values()));

      // 4. 定義が欠けている／ダミーになっている生徒へ配り直す ＋ 単語名も不明な単語を一覧化
      let repaired = 0;
      const lostReport = {};
      for (const [sid, d] of Object.entries(docsById)) {
        const ids = Array.isArray(d.mylist) ? d.mylist : [];
        const current = (d.customCards || []).filter(c => !isStubCard(c));
        const haveIds = new Set(current.map(c => c.id));
        const hadStubs = (d.customCards || []).some(c => isStubCard(c));
        let added = 0;
        ids.forEach(id => {
          if (!haveIds.has(id) && pool.has(id)) { current.push(pool.get(id)); haveIds.add(id); added++; }
        });
        const lost = ids.filter(id => isCustomCardId(id) && id.startsWith('card_') && !haveIds.has(id) && !getKnownWordName(id));
        if (lost.length) lostReport[sid] = lost;
        const names = buildWordNamesFor(ids);
        const needNames = Object.keys(names).some(id => !(d.wordNames && d.wordNames[id]));
        if (added > 0 || hadStubs || needNames) {
          const st = students.find(s => s.id === sid);
          try {
            await ensureStudentCloudAuth(sid, st.passcode);
            await fbDb.collection('students').doc(sid).set({ customCards: current, wordNames: names }, { merge: true });
            repaired++;
          } catch (e) {}
        }
      }
      try { localStorage.setItem('haku_lost_cards_report', JSON.stringify({ at: Date.now(), report: lostReport })); } catch (e) {}
      renderLostCardsReport();
      console.log(`Card recovery: pool=${pool.size}, repaired students=${repaired}`);
    } catch (err) {
      console.warn('Card recovery note:', err.message);
    } finally {
      if (teacher) { try { await ensureStudentCloudAuth(teacher.id, teacher.passcode); } catch (e) {} }
      isRecoveringCards = false;
      updateMylistBadge();
      const mv = document.getElementById('viewMylist');
      if (mv && !mv.classList.contains('hidden')) renderMylistView();
    }
  }

  // ★ 管理画面: 単語名も不明な単語を「生徒 × 追加日」ごとに一覧表示
  function renderLostCardsReport() {
    const box = document.getElementById('lostCardsReport');
    if (!box) return;
    let data = null;
    try { data = JSON.parse(localStorage.getItem('haku_lost_cards_report') || 'null'); } catch (e) {}
    const report = (data && data.report) || {};
    const sids = Object.keys(report).filter(sid => report[sid] && report[sid].length);
    if (!sids.length) { box.classList.add('hidden'); box.innerHTML = ''; return; }

    const fmt = (d) => d ? `${d.getFullYear()}/${d.getMonth() + 1}/${d.getDate()}` : '日付不明';
    let total = 0;
    let html = '';
    sids.forEach(sid => {
      const st = students.find(s => s.id === sid);
      const groups = {};
      report[sid].forEach(id => {
        const key = fmt(getCardCreatedDate(id));
        (groups[key] = groups[key] || []).push(id);
      });
      total += report[sid].length;
      html += `<div class="mt-1.5"><p class="text-[11px] font-bold text-slate-700">${st ? st.name : sid}（${sid}）</p>`;
      Object.entries(groups).forEach(([day, ids]) => {
        html += `
          <div class="flex items-center justify-between text-[11px] bg-white rounded-lg border border-amber-200 px-2 py-1 mt-1">
            <span class="text-slate-700">${day} に追加した単語：<b>${ids.length}件</b></span>
            <button class="btn-remove-lost text-[10px] px-2 py-0.5 rounded-full bg-slate-100 hover:bg-rose-100 text-slate-600 font-bold" data-sid="${sid}" data-ids="${ids.join(',')}">マイリストから削除</button>
          </div>`;
      });
      html += `</div>`;
    });

    box.innerHTML = `
      <div class="rounded-2xl border-2 border-amber-300 bg-amber-50 p-2.5">
        <p class="text-xs font-bold text-amber-800">⚠️ 中身が見つからない単語：${total}件</p>
        <p class="text-[10px] text-amber-700 mt-0.5 leading-snug">古い形式で保存され、データも単語名も失われた単語です。授業メモと日付を照らし合わせて、下のインポートからもう一度追加してください（新しく追加した単語は単語名が必ず残るので、今後は自動で復元されます）。</p>
        ${html}
      </div>`;
    box.classList.remove('hidden');

    box.querySelectorAll('.btn-remove-lost').forEach(btn => {
      btn.addEventListener('click', async () => {
        const sid = btn.getAttribute('data-sid');
        const ids = (btn.getAttribute('data-ids') || '').split(',').filter(Boolean);
        if (!ids.length || !confirm(`${ids.length}件をこの生徒のマイリストから削除しますか？`)) return;
        // ローカル
        const key = `haku_mylist_${sid}`;
        try {
          const arr = JSON.parse(localStorage.getItem(key) || '[]').filter(id => !ids.includes(id));
          localStorage.setItem(key, JSON.stringify(arr));
        } catch (e) {}
        if (currentStudent && currentStudent.id === sid) ids.forEach(id => mylistSet.delete(id));
        // クラウド
        const st = students.find(s => s.id === sid);
        const teacher = currentStudent;
        if (isFirebaseReady && fbDb && st) {
          try {
            await ensureStudentCloudAuth(sid, st.passcode);
            await fbDb.collection('students').doc(sid).update({ mylist: firebase.firestore.FieldValue.arrayRemove(...ids), removedIds: firebase.firestore.FieldValue.arrayUnion(...ids) });
          } catch (e) { console.warn('remove lost note:', e.message); }
          if (teacher && teacher.id !== sid) { try { await ensureStudentCloudAuth(teacher.id, teacher.passcode); } catch (e) {} }
        }
        // レポート更新
        try {
          const d = JSON.parse(localStorage.getItem('haku_lost_cards_report') || '{}');
          if (d.report && d.report[sid]) d.report[sid] = d.report[sid].filter(id => !ids.includes(id));
          localStorage.setItem('haku_lost_cards_report', JSON.stringify(d));
        } catch (e) {}
        renderLostCardsReport();
        updateMylistBadge();
        showToast(`${ids.length}件を削除しました`);
      });
    });
  }

  function saveMylistForCurrentStudent() {
    const studentPrefix = currentStudent ? currentStudent.id : 'guest';
    const key = `haku_mylist_${studentPrefix}`;
    const foldersKey = `haku_mylist_folders_${studentPrefix}`;
    const mapKey = `haku_mylist_card_map_${studentPrefix}`;

    localStorage.setItem(key, JSON.stringify(Array.from(mylistSet)));
    localStorage.setItem(foldersKey, JSON.stringify(mylistFolders));
    localStorage.setItem(mapKey, JSON.stringify(mylistCardFolderMap));
    try { recordWordNames(getMylistCards()); } catch (e) {}

    updateMylistBadge();

    // Trigger asynchronous cloud sync to persist on all devices!
    if (currentStudent && currentStudent.id !== 'guest') {
      syncStudentToCloud(currentStudent.id);
    }
  }

  // --- Folder Picker Modal for Adding Cards to My List ---
  function promptFolderSelectAndAdd(card, onComplete) {
    // If already in mylist, toggle off directly
    if (mylistSet.has(card.id)) {
      mylistSet.delete(card.id);
      delete mylistCardFolderMap[card.id];
      saveMylistForCurrentStudent();
      showToast(currentLang === 'ja' ? `「${card.word}」をマイリストから解除しました` : `Removed "${card.word}" from My List`);
      if (onComplete) onComplete(false);
      return;
    }

    // Existing folders
    const CLASS_FOLDER_ID = 'folder_class_words';
    const CLASS_FOLDER_NAME = '授業で習った言葉';
    if (!mylistFolders.find(f => f.id === CLASS_FOLDER_ID || f.name === CLASS_FOLDER_NAME)) {
      mylistFolders.unshift({ id: CLASS_FOLDER_ID, name: CLASS_FOLDER_NAME });
    }

    // Build modal overlay
    const overlay = document.createElement('div');
    overlay.className = 'fixed inset-0 z-50 flex items-center justify-center bg-slate-900/60 backdrop-blur-xs p-4 animate-fade-in';
    
    let folderOptionsButtons = `
      <button data-folder-id="" class="w-full text-left px-3.5 py-2.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-slate-100 flex items-center justify-between text-xs font-bold text-slate-700 transition">
        <span class="flex items-center space-x-2"><span>📂</span><span>${currentLang === 'ja' ? 'フォルダ指定なし（未分類）' : 'Unfiled (No folder)'}</span></span>
        <span class="text-[10px] text-slate-400">Default</span>
      </button>
    `;

    mylistFolders.forEach(f => {
      folderOptionsButtons += `
        <button data-folder-id="${f.id}" class="w-full text-left px-3.5 py-2.5 rounded-xl border border-softBorder bg-white hover:bg-lightBlueBg/40 flex items-center justify-between text-xs font-bold text-deepNavy transition">
          <span class="flex items-center space-x-2"><span>📁</span><span>${f.name}</span></span>
          <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-slate-400"></i>
        </button>
      `;
    });

    overlay.innerHTML = `
      <div class="bg-white rounded-3xl p-5 max-w-sm w-full shadow-2xl border border-softBorder space-y-4 animate-scale-up" onclick="event.stopPropagation()">
        <div class="flex items-center justify-between border-b border-slate-100 pb-3">
          <div>
            <h3 class="text-sm font-bold text-deepNavy flex items-center space-x-1.5">
              <span>⭐</span>
              <span>${currentLang === 'ja' ? 'マイリストの保存先フォルダ' : 'Choose Folder'}</span>
            </h3>
            <p class="text-[11px] text-slate-500 mt-0.5">${currentLang === 'ja' ? `「${card.word}」の保存先を選択してください` : `Save "${card.word}" into:`}</p>
          </div>
          <button class="btn-close-modal p-1.5 text-slate-400 hover:text-slate-600 rounded-full hover:bg-slate-100 transition">
            <i data-lucide="x" class="w-4 h-4"></i>
          </button>
        </div>

        <div class="space-y-2 max-h-60 overflow-y-auto pr-1">
          ${folderOptionsButtons}
        </div>

        <div class="pt-2 border-t border-slate-100">
          <button class="btn-cancel-modal w-full py-2 rounded-xl text-xs font-bold text-slate-500 hover:bg-slate-100 transition">
            ${currentLang === 'ja' ? 'キャンセル' : 'Cancel'}
          </button>
        </div>
      </div>
    `;

    document.body.appendChild(overlay);
    if (window.lucide) lucide.createIcons({ root: overlay });

    const closeModal = () => {
      overlay.classList.add('opacity-0');
      setTimeout(() => {
        if (overlay.parentNode) overlay.parentNode.removeChild(overlay);
      }, 150);
    };

    overlay.querySelector('.btn-close-modal').addEventListener('click', closeModal);
    overlay.querySelector('.btn-cancel-modal').addEventListener('click', closeModal);
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) closeModal();
    });

    overlay.querySelectorAll('[data-folder-id]').forEach(btn => {
      btn.addEventListener('click', () => {
        const destFolderId = btn.getAttribute('data-folder-id') || null;
        mylistSet.add(card.id);
        if (destFolderId) {
          mylistCardFolderMap[card.id] = destFolderId;
        } else {
          delete mylistCardFolderMap[card.id];
        }
        saveMylistForCurrentStudent();

        const folderObj = mylistFolders.find(f => f.id === destFolderId);
        const folderName = folderObj ? folderObj.name : (currentLang === 'ja' ? '未分類' : 'Unfiled');
        showToast(currentLang === 'ja' ? `「${card.word}」を「${folderName}」に保存しました ⭐` : `Saved "${card.word}" to ${folderName} ⭐`);

        closeModal();
        if (onComplete) onComplete(true);
      });
    });
  }

  function updateMylistBadge() {
    const count = getMylistCards().length;
    const badge = document.getElementById('mylistCountBadge');
    if (badge) badge.textContent = count;
    const drawerBadge = document.getElementById('drawerMylistBadge');
    if (drawerBadge) drawerBadge.textContent = count;
  }

  // --- Sliding Menu Drawer Controls (2枚目画像スタイル) ---
  function openMenuDrawer() {
    const drawer = document.getElementById('portalDrawer');
    const overlay = document.getElementById('portalDrawerOverlay');
    if (!drawer || !overlay) return;

    if (window.lucide) {
      lucide.createIcons({ root: drawer });
    }

    overlay.classList.remove('hidden');
    // trigger reflow for smooth animation
    void overlay.offsetWidth;
    overlay.classList.remove('opacity-0');
    drawer.classList.remove('-translate-x-full');
  }

  function closeMenuDrawer() {
    const drawer = document.getElementById('portalDrawer');
    const overlay = document.getElementById('portalDrawerOverlay');
    if (!drawer || !overlay) return;

    overlay.classList.add('opacity-0');
    drawer.classList.add('-translate-x-full');
    setTimeout(() => {
      overlay.classList.add('hidden');
    }, 300);
  }

  let expandedOverviewFolderIds = new Set(); // tracks which folders are open in Level 1 overview

  function createFolderElement(fc) {
    const isExpanded = expandedOverviewFolderIds.has(fc.id);
    const folderCards = vocabList.filter(c => c.folder_id === fc.id);
    const bilingualFolderTitle = getBilingualFolderTitle(fc, currentLang);

    // Wrapper matching Image 2: rounded-2xl border bg-white
    const folderWrapper = document.createElement('div');
    folderWrapper.className = 'border border-softBorder rounded-2xl bg-white shadow-2xs overflow-hidden transition-all shrink-0';

    // Header row: [Folder icon] [初級 1-10 (262語)] ... [Play] [Check/Test] [Chevron]
    const headerDiv = document.createElement('div');
    headerDiv.className = 'px-3.5 py-3 hover:bg-slate-50 cursor-pointer flex items-center justify-between select-none transition';
    headerDiv.innerHTML = `
      <div class="flex items-center space-x-2.5 truncate pr-2">
        <i data-lucide="${isExpanded ? 'folder-open' : 'folder'}" class="w-5 h-5 text-deepNavy shrink-0"></i>
        <span class="text-sm font-bold text-darkNavyText truncate">${bilingualFolderTitle}</span>
        <span class="text-xs text-slate-400 font-medium shrink-0">(${folderCards.length}語)</span>
      </div>
      <div class="flex items-center space-x-2 shrink-0">
        <button class="btn-overview-play p-1 text-deepNavy hover:bg-slate-100 rounded-lg transition" title="このフォルダの全単語を学習">
          <i data-lucide="play" class="w-4 h-4 fill-deepNavy text-deepNavy"></i>
        </button>
        <button class="btn-overview-test p-1 text-emerald-600 hover:bg-slate-100 rounded-lg transition" title="このフォルダのテストを開始">
          <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-600"></i>
        </button>
        <button class="btn-overview-toggle p-0.5 text-slate-400 hover:text-deepNavy transition" title="${isExpanded ? '閉じる' : '開く'}">
          <i data-lucide="${isExpanded ? 'chevron-up' : 'chevron-down'}" class="w-4 h-4"></i>
        </button>
      </div>
    `;

    // Header click toggles open/close
    headerDiv.addEventListener('click', (e) => {
      if (e.target.closest('.btn-overview-play')) {
        e.stopPropagation();
        currentFolder = fc.id;
        startStudyingEntireFolder();
        return;
      }
      if (e.target.closest('.btn-overview-test')) {
        e.stopPropagation();
        currentFolder = fc.id;
        startQuizWithScope('folder', fc.id, fc.title);
        return;
      }

      // Toggle open/collapse
      if (expandedOverviewFolderIds.has(fc.id)) {
        expandedOverviewFolderIds.delete(fc.id);
      } else {
        expandedOverviewFolderIds.clear(); expandedOverviewFolderIds.add(fc.id);
      }
      renderFolderOverview();
    });

    folderWrapper.appendChild(headerDiv);

    // Collapsible units list inside this folder
    if (isExpanded) {
      const unitsContainer = document.createElement('div');
      unitsContainer.className = 'py-1 px-2 space-y-1 border-t border-slate-100 bg-slate-50/50 max-h-[340px] sm:max-h-[400px] overflow-y-auto overscroll-contain units-scroll-container';

      const [minSec, maxSec] = fc.range;
      const secNumsToRender = [];
      if (fc.id === 'folder_1') {
        secNumsToRender.push(0);
      }
      for (let s = minSec; s <= maxSec; s++) {
        secNumsToRender.push(s);
      }

      secNumsToRender.forEach(secNum => {
        const secInfo = getCatalogSection(secNum);
        const rawSecTitle = (secInfo && secInfo.title) || `${secNum}. 単元${secNum}`;
        const bilingualTitle = getBilingualSectionTitle(secNum, rawSecTitle, currentLang);
        const secCards = vocabList.filter(c => Number(c.section_num) === Number(secNum));
        const numDisplay = secNum === 0 ? '★' : `${secNum}`;

        const isCurrentActive = (Number(currentSection) === Number(secNum) && currentFolder === fc.id);

        const unitItem = document.createElement('div');
        unitItem.className = `group flex items-center justify-between px-3 py-2 rounded-xl cursor-pointer transition text-xs ${
          isCurrentActive
            ? 'bg-lightBlueBg/80 border-2 border-deepNavy text-deepNavy font-bold shadow-xs'
            : 'bg-white border border-slate-200/80 hover:border-deepNavy hover:bg-blue-50/30 text-slate-800'
        }`;
        unitItem.innerHTML = `
          <div class="flex items-center space-x-2 truncate pr-2">
            <span class="w-5 h-5 rounded-md ${isCurrentActive ? 'bg-deepNavy text-white' : 'bg-slate-100 text-slate-700'} font-bold text-[10px] flex items-center justify-center shrink-0">${numDisplay}</span>
            <span class="truncate font-semibold text-xs">${bilingualTitle}</span>
          </div>
          <div class="flex items-center space-x-1 shrink-0 text-slate-400">
            <span class="text-[10px] px-1.5 py-0.5 rounded font-medium ${isCurrentActive ? 'bg-deepNavy text-white' : 'bg-slate-100 text-slate-600'}">${secCards.length}語</span>
            <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-slate-300 group-hover:text-deepNavy transition"></i>
          </div>
        `;

        unitItem.addEventListener('click', (e) => {
          e.stopPropagation();
          currentFolder = fc.id;
          startStudyingSection(secNum, rawSecTitle);
        });

        unitsContainer.appendChild(unitItem);
      });

      folderWrapper.appendChild(unitsContainer);
    }

    return folderWrapper;
  }

  function renderFolderOverview() {
    const pcContainer = document.getElementById('folderButtonsContainer');
    const mobileContainer = document.getElementById('folderButtonsContainerMobile');

    const containers = [pcContainer, mobileContainer].filter(Boolean);
    containers.forEach(c => { c.innerHTML = ''; });

    FOLDER_CONFIGS.forEach(fc => {
      if (pcContainer) pcContainer.appendChild(createFolderElement(fc));
      if (mobileContainer) mobileContainer.appendChild(createFolderElement(fc));
    });

    containers.forEach(c => {
      lucide.createIcons({ root: c });
    });
  }

  function openFolderUnits(folderId) {
    currentFolder = folderId;
    currentNavLevel = 'units';

    const fc = FOLDER_CONFIGS.find(f => f.id === folderId);
    const bilingualFolderTitle = getBilingualFolderTitle(fc, currentLang);
    document.getElementById('currentFolderTitle').textContent = fc ? bilingualFolderTitle : '単元一覧';

    const container = document.getElementById('unitButtonsContainer');
    container.innerHTML = '';

    const [minSec, maxSec] = fc.range;

    const secNumsToRender = [];
    if (folderId === 'folder_1') {
      secNumsToRender.push(0);
    }
    for (let s = minSec; s <= maxSec; s++) {
      secNumsToRender.push(s);
    }

    secNumsToRender.forEach(secNum => {
      const secInfo = getCatalogSection(secNum);
      const rawSecTitle = (secInfo && secInfo.title) || `${secNum}. 単元${secNum}`;
      const bilingualTitle = getBilingualSectionTitle(secNum, rawSecTitle, currentLang);
      const secCards = vocabList.filter(c => Number(c.section_num) === Number(secNum));
      const numDisplay = secNum === 0 ? '★' : `${secNum}`;

      const unitBtn = document.createElement('button');
      unitBtn.className = 'w-full p-2.5 rounded-xl border border-slate-200 bg-white hover:border-rose-300 hover:bg-rose-50/50 flex items-center justify-between text-left transition text-xs font-semibold text-slate-800 shadow-2xs';
      unitBtn.innerHTML = `
        <div class="flex items-center space-x-2 truncate pr-2">
          <span class="w-6 h-6 rounded-lg bg-slate-100 text-slate-700 flex items-center justify-center font-bold text-[11px] shrink-0">${numDisplay}</span>
          <span class="truncate">${bilingualTitle}</span>
        </div>
        <div class="flex items-center space-x-1 text-slate-400 shrink-0">
          <span class="text-[10px] bg-slate-100 px-1.5 py-0.5 rounded">${secCards.length}語</span>
          <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
        </div>
      `;
      lucide.createIcons({ root: unitBtn });

      unitBtn.addEventListener('click', () => {
        startStudyingSection(secNum, rawSecTitle);
      });
      container.appendChild(unitBtn);
    });

    // Toggle panels
    document.getElementById('folderOverviewPanel').classList.add('hidden');
    document.getElementById('unitListPanel').classList.remove('hidden');
    document.getElementById('activeStudyHeader').classList.add('hidden');
  }

  function startStudyingSection(sectionNum, sectionTitle) {
    currentSection = sectionNum;
    currentNavLevel = 'study';

    // Update active study header with bilingual titles
    const fc = FOLDER_CONFIGS.find(f => f.id === currentFolder);
    const bilingualSec = getBilingualSectionTitle(sectionNum, sectionTitle, currentLang);
    const bilingualFold = getBilingualFolderTitle(fc, currentLang);
    document.getElementById('activeStudySectionName').textContent = bilingualSec;
    document.getElementById('activeStudyFolderName').textContent = fc ? bilingualFold : '';

    // Switch panels
    document.getElementById('folderOverviewPanel').classList.add('hidden');
    document.getElementById('unitListPanel').classList.add('hidden');
    document.getElementById('activeStudyHeader').classList.remove('hidden');

    updateActiveDeck();
    renderFolderOverview();
    showToast(`「${sectionTitle}」の学習を開始します`);

    // スマホ版ならスワイプ操作ガイドポップアップを表示
    checkAndShowSwipeGuide();
  }

  function startStudyingEntireFolder() {
    currentSection = 'all';
    currentNavLevel = 'study';

    const fc = FOLDER_CONFIGS.find(f => f.id === currentFolder);
    document.getElementById('activeStudySectionName').textContent = fc ? `${fc.title} (全単元)` : 'フォルダ全体';
    document.getElementById('activeStudyFolderName').textContent = '全単語';

    document.getElementById('folderOverviewPanel').classList.add('hidden');
    document.getElementById('unitListPanel').classList.add('hidden');
    document.getElementById('activeStudyHeader').classList.remove('hidden');

    updateActiveDeck();
    showToast(`${fc ? fc.title : 'このフォルダ'}の全単語を学習します`);

    // スマホ版ならスワイプ操作ガイドポップアップを表示
    checkAndShowSwipeGuide();
  }

  function backToFolderOverview() {
    currentNavLevel = 'folders';
    if (isMylistStudyMode) {
      isMylistStudyMode = false;
      isSearchStudyMode = false;
      document.getElementById('activeStudyHeader').classList.add('hidden');
      switchView('mylist');
      return;
    }
    isSearchStudyMode = false;
    document.getElementById('folderOverviewPanel').classList.remove('hidden');
    document.getElementById('unitListPanel').classList.add('hidden');
    document.getElementById('activeStudyHeader').classList.add('hidden');
    // Restore default deck so flashcards are not stuck on the search single card
    updateActiveDeck();
  }

  function makeSafeRubyWord(word, reading) {
    if (!word) return '';
    const hasKanji = /[\u4e00-\u9faf\u3400-\u4dbf]/.test(word);
    if (!hasKanji || !reading || reading === word) {
      return word;
    }
    return `<ruby>${word}<rt>${reading}</rt></ruby>`;
  }

  function getNaturalDefaultDialogue(word, reading) {
    const rw = makeSafeRubyWord(word, reading);
    return {
      ja: `A: 「${rw}」はどういう<ruby>意味<rt>いみ</rt></ruby>ですか？<br/>B: <ruby>日常<rt>にちじょう</rt></ruby><ruby>会話<rt>かいわ</rt></ruby>でもよく<ruby>使<rt>つか</rt></ruby>われる<ruby>表現<rt>ひょうげん</rt></ruby>ですよ。`,
      en: `A: What does "${word}" mean?<br/>B: It is a common expression used in daily conversation.`,
      zh_TW: `A: 「${word}」是什麼意思呢？<br/>B: 這是日常生活中非常常用的表達方式喔。`,
      zh_CN: `A: 「${word}」是什么意思呢？<br/>B: 这是日常生活中非常常用的表达方式哦。`,
      ko: `A: "${word}"은(는) 무슨 뜻인가요?<br/>B: 일상 대화에서도 자주 쓰이는 표현이에요.`,
      zh_HK: `A: 「${word}」係咩意思呢？<br/>B: 呢個係日常生活好常用嘅表達嚟㗎。`,
      fr: `A: Que signifie « ${word} » ?<br/>B: C'est une expression couramment utilisée dans la conversation quotidienne.`
    };
  }

  function updateActiveDeck() {
    if (currentDeckFilter === 'jlpt') {
      const lvl = currentJlptDeckLevel || 'N5';
      const jlptList = (window.JLPT_VOCAB && window.JLPT_VOCAB[lvl]) || [];
      const dictMap = window.DICT_EXAMPLES_MAP || {};
      activeDeck = jlptList.map((entry, idx) => {
        const dictEx = dictMap[entry.word] || (entry.reading && dictMap[entry.reading]);
        const ex = (entry.examples && entry.examples[0]) ? entry.examples[0] : (dictEx || null);
        const fallbackDlg = getNaturalDefaultDialogue(entry.word, entry.reading || entry.k);
        const meaningText = (entry.meanings || []).join(', ') || '—';
        return {
          id: `jlpt_${entry.level || lvl}_${idx}_${entry.word}`,
          word: entry.word,
          reading: entry.reading || entry.k || entry.word,
          category: `JLPT ${entry.level || lvl}`,
          section_title: `JLPT ${entry.level || lvl} 単語`,
          folder_id: `jlpt_${lvl}`,
          meaning: {
            en: meaningText,
            ja: entry.word,
            zh_TW: meaningText,
            zh_CN: meaningText,
            ko: meaningText,
            zh_HK: meaningText,
            fr: meaningText
          },
          example: {
            ja: ex ? ex.ja : fallbackDlg.ja,
            en: ex ? (ex.en || '') : fallbackDlg.en
          },
          related: `【JLPT】${entry.level || lvl} / 【行】${entry.row || '—'}`,
          isJlpt: true
        };
      });
      currentIndex = 0;
      isCardFlipped = false;
      renderCurrentCard();
      return;
    }

    let pool = vocabList.filter(card => {
      // Shared vs Student dedicated
      if (currentDeckFilter === 'mine') {
        if (!currentStudent) return false;
        return card.studentId === currentStudent.id;
      } else {
        return !card.studentId || card.studentId === 'all';
      }
    });

    // Filter by Folder
    if (currentFolder !== 'all') {
      pool = pool.filter(card => card.folder_id === currentFolder);
    }

    // Filter by Section
    if (currentSection !== 'all') {
      pool = pool.filter(card => Number(card.section_num) === Number(currentSection));
    }

    activeDeck = pool;
    currentIndex = 0;
    isCardFlipped = false;
    renderCurrentCard();
  }

  // --- 3D Card Rendering & Interaction ---
  function renderCurrentCard() {
    const cardEl = document.getElementById('flashcardElement');
    if (!cardEl) return;

    // Reset flip animation
    isCardFlipped = false;
    cardEl.classList.remove('rotate-y-180');

    if (!activeDeck || activeDeck.length === 0) {
      document.getElementById('cardProgressText').textContent = '0 / 0';
      document.getElementById('frontWord').textContent = 'カードがありません';
      document.getElementById('frontReading').textContent = '';
      document.getElementById('frontCategoryBadge').textContent = '空';
      document.getElementById('backMeaning').textContent = 'カードを追加してください';
      return;
    }

    if (currentIndex >= activeDeck.length) currentIndex = activeDeck.length - 1;
    if (currentIndex < 0) currentIndex = 0;

    const card = activeDeck[currentIndex];
    document.getElementById('cardProgressText').textContent = `${currentIndex + 1} / ${activeDeck.length}`;

    // 🛡️ カード表裏整合ガード: もし word が外国語で meaning に日本語がある場合は自動スワップ
    let jpWord = card.word;
    let readingText = card.reading || '';
    let meaningObj = card.meaning || {};
    let exampleObj = card.example || {};

    const hasJpInWord = /[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]/.test(card.word);
    if (!hasJpInWord && typeof card.meaning === 'object') {
      const candidateJp = card.meaning.ja || Object.values(card.meaning).find(v => typeof v === 'string' && /[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]/.test(v));
      if (candidateJp) {
        jpWord = candidateJp;
        meaningObj = { ...card.meaning, [currentLang]: card.word };
        if (!readingText || readingText === card.word || /[\uAC00-\uD7AF]/.test(readingText)) {
          readingText = '';
        }
      }
    }

    // Check Star / Mylist state
    const btnStar = document.getElementById('btnStarCurrent');
    if (mylistSet.has(card.id)) {
      btnStar.innerHTML = `<i data-lucide="star" class="w-5 h-5 fill-amber-400 text-amber-400"></i>`;
    } else {
      btnStar.innerHTML = `<i data-lucide="star" class="w-5 h-5 text-slate-300"></i>`;
    }
    lucide.createIcons({ root: btnStar });

    // Multi-language translation lookup (必ず母国語 & 英語)
    const targetMeaning = getBilingualMeaning(meaningObj, currentLang, jpWord);
    const targetExTrans = getBilingualExampleTrans(exampleObj, currentLang);

    // Reverse Mode handling: 日本語 ⇄ 母国語
    if (!isReverseMode) {
      // Normal: Front is Japanese, Back is Native & English Meaning
      document.getElementById('frontWord').textContent = jpWord;
      document.getElementById('frontWord').className = 'text-3xl sm:text-4xl font-extrabold text-darkNavyText tracking-tight leading-snug';
      const hasKanji = /[\u4e00-\u9faf]/.test(jpWord);
      const showReading = hasKanji || (readingText && readingText !== jpWord);
      document.getElementById('frontReading').textContent = showReading ? readingText : '';
      document.getElementById('frontReading').className = 'text-base sm:text-lg font-bold text-coralPink tracking-wider mb-1 font-jp min-h-[1.5rem]';
      document.getElementById('frontReading').classList.remove('hidden');
      document.getElementById('backMeaning').textContent = targetMeaning;
    } else {
      // Reverse: Front is Native & English Meaning, Back is Japanese
      const targetLang = currentLang;
      let nativeMeaning = meaningObj ? (meaningObj[targetLang] || '') : '';
      let enMeaning = meaningObj ? (meaningObj.en || '') : '';

      if (Array.isArray(card.meanings)) {
        enMeaning = card.meanings.join(', ');
      }

      // Safeguard: Ensure enMeaning is NEVER Japanese kanji/kana
      if (enMeaning && /[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]/.test(enMeaning)) {
        enMeaning = '';
      }

      // If nativeMeaning is missing or identical to English, search fallback dictionary
      if ((!nativeMeaning || nativeMeaning === enMeaning) && targetLang !== 'en' && targetLang !== 'ja') {
        const fallback = getFallbackMeaningForWord(jpWord, targetLang);
        if (fallback) nativeMeaning = fallback;
      }

      if (targetLang === 'en' || !nativeMeaning || nativeMeaning === enMeaning) {
        // English-only student or no native translation available: show English
        document.getElementById('frontReading').textContent = '';
        document.getElementById('frontReading').classList.add('hidden');
        document.getElementById('frontWord').textContent = enMeaning || nativeMeaning || jpWord;
        document.getElementById('frontWord').className = 'text-2xl sm:text-3xl font-extrabold text-darkNavyText tracking-tight leading-snug';
      } else {
        // Non-English student: show Native language prominently AND English together!
        document.getElementById('frontWord').textContent = nativeMeaning;
        document.getElementById('frontWord').className = 'text-2xl sm:text-3xl font-extrabold text-darkNavyText tracking-tight leading-snug';
        if (enMeaning && !nativeMeaning.includes(`(${enMeaning})`)) {
          document.getElementById('frontReading').textContent = `(${enMeaning})`;
          document.getElementById('frontReading').className = 'text-sm sm:text-base font-bold text-slate-500 mb-1.5 tracking-normal';
          document.getElementById('frontReading').classList.remove('hidden');
        } else {
          document.getElementById('frontReading').textContent = '';
          document.getElementById('frontReading').classList.add('hidden');
        }
      }

      document.getElementById('backMeaning').textContent = `${jpWord}${readingText ? ` （${readingText}）` : ''}`;
    }

    let currentCardCategory = card.category || '一般';
    if (currentCardCategory === '授業で習った言葉' && !mylistSet.has(card.id) && !mylistSet.has(card.word)) {
      currentCardCategory = card.isDict ? '辞書' : '一般';
    }
    document.getElementById('frontCategoryBadge').textContent = currentCardCategory;
    document.getElementById('backCategoryBadge').textContent = currentCardCategory;
    document.getElementById('backWordHeader').textContent = jpWord;
    document.getElementById('backReadingHeader').textContent = readingText ? `（${readingText}）` : '';

    // Example sentence & Translation (Render HTML <ruby> tags for furigana and <br> for dialogues)
    let exJa = (card.example && card.example.ja) || '';
    let exTrans = targetExTrans;

    // 🛡️ 例文表裏ガード: もし exJa が外国語で始まっていて括弧内に日本語がある場合、日本語を抽出
    if (exJa && !/^[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF<]/.test(exJa) && /[（(]([\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF].+?)[）)]/.test(exJa)) {
      const match = exJa.match(/[（(]([\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF].+?)[）)]/);
      if (match) {
        const foreignPart = exJa.replace(match[0], '').trim();
        exJa = match[1];
        if (!exTrans) exTrans = foreignPart;
      }
    }

    // Auto-convert Kanji(furigana) parentheses in exJa to <ruby> tags if not already ruby
    if (exJa && !exJa.includes('<ruby>') && /([\u4e00-\u9faf\u3400-\u4dbf]+)[（\(]([\u3040-\u309f]+)[）\)]/.test(exJa)) {
      exJa = exJa.replace(/([\u4e00-\u9faf\u3400-\u4dbf]+)[（\(]([\u3040-\u309f]+)[）\)]/g, '<ruby>$1<rt>$2</rt></ruby>');
    }

    if (exJa) {
      document.getElementById('backExampleJa').innerHTML = exJa;
      document.getElementById('backExampleTranslation').innerHTML = exTrans;
      document.getElementById('backExampleJa').parentElement.classList.remove('hidden');
      // ★ 例文から単語辞書ボタンチップを自動抽出して描画
      if (typeof renderExampleWordChips === 'function') {
        renderExampleWordChips(exJa);
      }
    } else {
      document.getElementById('backExampleJa').parentElement.classList.add('hidden');
      const chipsCont = document.getElementById('exampleWordChipsContainer');
      if (chipsCont) chipsCont.classList.add('hidden');
    }

    // Related Words / Verb Conjugations (関連する言葉は日本語、説明は母国語)
    const relContainer = document.getElementById('backRelatedContainer');
    if (card.related && card.related.trim()) {
      relContainer.classList.remove('hidden');

      // Dictionary of linguistic terms for multilingual students
      const LINGUISTIC_TERMS = {
        '名詞': { en: 'Noun', zh_TW: '名詞', zh_CN: '名词', ko: '명사', zh_HK: '名詞', fr: 'Nom' },
        '動詞': { en: 'Verb', zh_TW: '動詞', zh_CN: '动词', ko: '동사', zh_HK: '動詞', fr: 'Verbe' },
        'い形容詞': { en: 'I-Adjective', zh_TW: 'い形容詞', zh_CN: 'い形容词', ko: 'い형용사', zh_HK: 'い形容詞', fr: 'Adjectif en -i' },
        'な形容詞': { en: 'Na-Adjective', zh_TW: 'な形容詞', zh_CN: 'な形容词', ko: 'な형용사', zh_HK: 'な形容詞', fr: 'Adjectif en -na' },
        '相槌': { en: 'Interjection / Backchannel', zh_TW: '附和語 / 應答', zh_CN: '附和语 / 应答', ko: '맞장구 / 리액션', zh_HK: '附和語 / 應答', fr: 'Interjection' },
        '場所': { en: 'Place / Facility', zh_TW: '場所 / 設施', zh_CN: '场所 / 设施', ko: '장소 / 시설', zh_HK: '場所 / 設施', fr: 'Lieu / Installation' },
        '代名詞': { en: 'Pronoun / Family', zh_TW: '代名詞 / 家族', zh_CN: '代名词 / 家族', ko: '대명사 / 가족', zh_HK: '代名詞 / 家族', fr: 'Pronom / Famille' },
        '文法': { en: 'Grammar', zh_TW: '文法', zh_CN: '语法', ko: '문법', zh_HK: '語法', fr: 'Grammaire' },
        '原型（辞書形）': { en: 'Dictionary Form', zh_TW: '原形（辭書形）', zh_CN: '原形（辞书形）', ko: '기본형 (사전형)', zh_HK: '原形（辭書形）', fr: 'Forme du dictionnaire' },
        'ます形': { en: 'Masu Form', zh_TW: 'ます形', zh_CN: 'ます形', ko: 'ます형 (정중형)', zh_HK: 'ます形', fr: 'Forme en -masu' },
        'て形': { en: 'Te Form', zh_TW: 'て形', zh_CN: 'て形', ko: 'て형 (연결형)', zh_HK: 'て形', fr: 'Forme en -te' },
        'ない形': { en: 'Nai Form', zh_TW: 'ない形', zh_CN: 'ない形', ko: 'ない형 (부정형)', zh_HK: 'ない形', fr: 'Forme en -nai' },
        'た形': { en: 'Ta Form', zh_TW: 'た形', zh_CN: 'た形', ko: 'た형 (과거형)', zh_HK: 'た形', fr: 'Forme en -ta' },
        'グループ・連語': { en: 'Group & Collocation', zh_TW: '分類與慣用搭配', zh_CN: '分类与惯用搭配', ko: '그룹 및 연어', zh_HK: '分類與慣用搭配', fr: 'Groupe & Collocation' },
        '日常会話の重要語彙': { en: 'Essential daily vocabulary', zh_TW: '日常會話重要語彙', zh_CN: '日常会话重要词汇', ko: '일상 회화 중요 어휘', zh_HK: '日常會話重要字詞', fr: 'Vocabulaire essentiel du quotidien' }
      };

      let formattedRelated = card.related;
      // Add native translation explanation if applicable and currentLang is not 'ja'
      if (currentLang !== 'ja') {
        formattedRelated = formattedRelated.split('\n').map(line => {
          let translatedSub = '';
          for (const [jpKey, transMap] of Object.entries(LINGUISTIC_TERMS)) {
            if (line.includes(`【${jpKey}】`) || line.includes(jpKey)) {
              translatedSub = transMap[currentLang] || transMap.en || '';
              break;
            }
          }
          if (translatedSub) {
            return `${line} <span class="text-[10px] text-slate-400 font-normal">(${translatedSub})</span>`;
          }
          return line;
        }).join('<br/>');
      } else {
        formattedRelated = formattedRelated.replace(/\n/g, '<br/>');
      }

      document.getElementById('backRelated').innerHTML = formattedRelated;
    } else {
      relContainer.classList.add('hidden');
    }

    // ★ 音声自動再生: 表面が表示された瞬間に単語を即座に自動再生
    // モバイルのタップ・クリックのユーザー操作コンテキストを即時利用してブロックを完全回避
    if (isAutoAudioEnabled && card) {
      if (autoAudioTimer) clearTimeout(autoAudioTimer);
      if (!isCardFlipped) {
        speakJapanese(card);
      }
    }
  }

  function flipCard() {
    const cardEl = document.getElementById('flashcardElement');
    if (!cardEl) return;
    isCardFlipped = !isCardFlipped;
    if (isCardFlipped) {
      cardEl.classList.add('rotate-y-180');
      // ★ 音声自動再生: 裏面が表示された瞬間に単語と例文を連続自動再生
      if (isAutoAudioEnabled && activeDeck[currentIndex]) {
        const card = activeDeck[currentIndex];
        const exampleJa = (card.example && card.example.ja) ? card.example.ja : null;
        speakJapaneseSequence(card, exampleJa);
      }
    } else {
      cardEl.classList.remove('rotate-y-180');
      // 表面に戻ったときも即座に自動再生
      if (isAutoAudioEnabled && activeDeck[currentIndex]) {
        speakJapanese(activeDeck[currentIndex]);
      }
    }
  }

  // --- Quiz & Test Mode Logic ---
  let currentQuizMode = 'quiz'; // 'quiz' (単語クイズ) or 'test' (実践テスト)
  let currentTestSubtype = 'all'; // 'all' (A+B), 'fillblank' (A: 穴埋め), 'conjugation' (B: 活用)
  let isMultilingualEnabled = (localStorage.getItem('haku_multilingual_quiz') !== 'false'); // true (ON) by default
  let currentQuestionMeta = null; // Stores question metadata for answer feedback
  let quizQuestionLimit = 10; // 10, 20, 30, or 99999 ('all')

  // Conjugates Japanese verbs into standard forms (Godan, Ichidan, Suru, Kuru)
  function conjugateJapaneseVerb(dictForm, reading, category) {
    if (!dictForm) return null;
    dictForm = dictForm.trim();
    dictForm = dictForm.replace(/<rt>[^<]*<\/rt>/g, '').replace(/<\/?ruby>/g, '').trim();

    if (dictForm === 'する' || dictForm.endsWith('する') || (category && category.includes('する動詞'))) {
      const base = dictForm.endsWith('する') ? dictForm.slice(0, -2) : dictForm;
      return {
        dict: base + 'する',
        masu: base + 'します',
        nai: base + 'しない',
        te: base + 'して',
        ta: base + 'した',
        pot: base + 'できる',
        group: '3グループ (サ変)'
      };
    }
    if (dictForm === '来る' || dictForm === 'くる') {
      return {
        dict: '来る',
        masu: '来ます',
        nai: '来ない',
        te: '来て',
        ta: '来た',
        pot: '来られる',
        group: '3グループ (カ変)'
      };
    }
    if (dictForm === '行く' || dictForm === 'いく') {
      return {
        dict: '行く',
        masu: '行きます',
        nai: '行かない',
        te: '行って',
        ta: '行った',
        pot: '行ける',
        group: '1グループ (五段)'
      };
    }

    const ichidanPrefixes = ['食べ', '見', '寝', '起き', '開け', '閉め', '教え', '答', '着', '出', '借', '忘', '変え', '助け', '覚'];
    const isIchidanExplicit = ichidanPrefixes.some(p => dictForm.startsWith(p));
    const endsWithRu = dictForm.endsWith('る');
    const secondLast = dictForm.length >= 2 ? dictForm[dictForm.length - 2] : '';
    const isIorE = /[いきしちにひみりえけせてねべめれ]/.test(secondLast);
    const godanExceptions = ['作る', '帰る', '入る', '走る', '知る', '切る', '要る', '限る', '喋る', '減る', '滑る'];
    const isGodanException = godanExceptions.some(g => dictForm.endsWith(g));
    
    const isIchidan = (isIchidanExplicit || (endsWithRu && isIorE)) && !isGodanException;

    if (isIchidan && endsWithRu) {
      const stem = dictForm.slice(0, -1);
      return {
        dict: dictForm,
        masu: stem + 'ます',
        nai: stem + 'ない',
        te: stem + 'て',
        ta: stem + 'た',
        pot: stem + 'られる',
        group: '2グループ (一段)'
      };
    }

    const last = dictForm[dictForm.length - 1];
    const stem = dictForm.slice(0, -1);
    const godanMap = {
      'う': { nai: 'わない', masu: 'います', pot: 'える', te: 'って', ta: 'った' },
      'く': { nai: 'かない', masu: 'きます', pot: 'ける', te: 'いて', ta: 'いた' },
      'ぐ': { nai: 'がない', masu: 'ぎます', pot: 'げる', te: 'いで', ta: 'いだ' },
      'す': { nai: 'さない', masu: 'します', pot: 'せる', te: 'して', ta: 'した' },
      'つ': { nai: 'たない', masu: 'ちます', pot: 'てる', te: 'って', ta: 'った' },
      'ぬ': { nai: 'なない', masu: 'にます', pot: 'ねる', te: 'んで', ta: 'んだ' },
      'ぶ': { nai: 'ばない', masu: 'びます', pot: 'べる', te: 'んで', ta: 'んだ' },
      'む': { nai: 'まない', masu: 'みます', pot: 'める', te: 'んで', ta: 'んだ' },
      'る': { nai: 'らない', masu: 'ります', pot: 'れる', te: 'って', ta: 'った' },
    };

    if (godanMap[last]) {
      const m = godanMap[last];
      return {
        dict: dictForm,
        masu: stem + m.masu,
        nai: stem + m.nai,
        te: stem + m.te,
        ta: stem + m.ta,
        pot: stem + m.pot,
        group: '1グループ (五段)'
      };
    }
    return null;
  }

  // Resolves the dictionary form of a conjugated verb
  function getBaseVerbFromConjugated(word, category) {
    if (!word) return '';
    word = word.replace(/<rt>[^<]*<\/rt>/g, '').replace(/<\/?ruby>/g, '').trim();
    
    if (word.endsWith('しない')) return word.slice(0, -3) + 'する';
    if (word === '来ない' || word === 'こない') return '来る';
    if (word === '行かない' || word === 'いかない') return '行く';
    
    if (word.endsWith('ない')) {
      const stem = word.slice(0, -2);
      const ichidanCandidate = stem + 'る';
      const c1 = conjugateJapaneseVerb(ichidanCandidate);
      if (c1 && c1.nai === word) return ichidanCandidate;
      
      const aToU = { 'わ': 'う', 'か': 'く', 'が': 'ぐ', 'さ': 'す', 'た': 'つ', 'な': 'ぬ', 'ば': 'ぶ', 'ま': 'む', 'ら': 'る' };
      const lastChar = stem[stem.length - 1];
      if (aToU[lastChar]) {
        return stem.slice(0, -1) + aToU[lastChar];
      }
    }
    if (word.endsWith('して')) return word.slice(0, -2) + 'する';
    if (word === '来て' || word === 'きて') return '来る';
    if (word === '行って' || word === 'いって') return '行く';
    if (word.endsWith('て') || word.endsWith('で')) {
      const pool = (window.INITIAL_VOCAB_DATA || []);
      const found = pool.find(c => {
        const conj = conjugateJapaneseVerb(c.word);
        return conj && conj.te === word;
      });
      if (found) return found.word;
    }
    return word;
  }

  function escapeRegex(s) {
    if (!s) return '';
    return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  // Masks the target word in a ruby-tagged Japanese example sentence
  function maskTargetWordInSentence(sentenceHtml, word) {
    if (!sentenceHtml || !word) return sentenceHtml || '';
    const cleanWord = word.replace(/<rt>[^<]*<\/rt>/g, '').replace(/<\/?ruby>/g, '').trim();
    const blankHtml = '<span class="quiz-blank-slot">［ ？ ］</span>';
    let result = sentenceHtml;

    // 1. If the whole word is wrapped in a single ruby tag: <ruby>cleanWord<rt>...</rt></ruby>
    // e.g. <ruby>水泳<rt>すいえい</rt></ruby> or <ruby>確認<rt>かくにん</rt></ruby>
    const exactRubyRegex = new RegExp('<ruby>\\s*' + escapeRegex(cleanWord) + '\\s*<rt>[^<]*<\\/rt><\\/ruby>', 'g');
    if (exactRubyRegex.test(sentenceHtml)) {
      result = sentenceHtml.replace(exactRubyRegex, blankHtml);
    } else {
      // 2. Flexible per-character ruby:
      // e.g. <ruby>作<rt>つく</rt></ruby>らない, <ruby>買<rt>か</rt></ruby>ってきた
      const patternParts = [];
      for (const ch of cleanWord) {
        if (ch >= '\u4e00' && ch <= '\u9fff') {
          patternParts.push('(?:<ruby>\\s*' + ch + '\\s*<rt>[^<]*<\\/rt><\\/ruby>|' + ch + ')');
        } else {
          patternParts.push(escapeRegex(ch));
        }
      }
      const flexibleRegex = new RegExp(patternParts.join(''), 'g');
      if (flexibleRegex.test(sentenceHtml)) {
        result = sentenceHtml.replace(flexibleRegex, blankHtml);
      } else {
        // 3. Fallback: ruby where cleanWord is contained inside the kanji portion
        const anyRubyRegex = new RegExp('<ruby>\\s*[^<]*?' + escapeRegex(cleanWord) + '[^<]*?<rt>[^<]*<\\/rt><\\/ruby>', 'g');
        if (anyRubyRegex.test(sentenceHtml)) {
          result = sentenceHtml.replace(anyRubyRegex, blankHtml);
        } else if (sentenceHtml.includes(cleanWord)) {
          // 4. Exact plain text replacement (for words without kanji/ruby, e.g. よっつ, セール)
          result = sentenceHtml.replace(cleanWord, blankHtml);
        }
      }
    }

    // 5. Absolute Safety Net: If any <ruby> or <rt> wraps or follows the blank slot, PURGE IT!
    result = result.replace(/<ruby>\s*(<span class="quiz-blank-slot">［ ？ ］<\/span>)\s*<rt>[^<]*<\/rt><\/ruby>/g, '$1');
    result = result.replace(/(<span class="quiz-blank-slot">［ ？ ］<\/span>)\s*<rt>[^<]*<\/rt>/g, '$1');
    result = result.replace(/<ruby>\s*([^<]*?<span class="quiz-blank-slot">［ ？ ］<\/span>[^<]*?)\s*<rt>[^<]*<\/rt><\/ruby>/g, '$1');

    return result;
  }

  function updateMultilingualButtonUI() {
    const btn = document.getElementById('btnToggleMultilingual');
    const dot = document.getElementById('multilingualToggleDot');
    const text = document.getElementById('multilingualToggleText');
    if (!btn || !dot || !text) return;
    const isJa = (currentLang === 'ja');
    if (isMultilingualEnabled) {
      btn.className = 'py-0.5 px-2.5 rounded-full text-[10px] font-extrabold transition shadow-2xs flex items-center space-x-1.5 bg-emerald-100 text-emerald-800 border border-emerald-300 active:scale-95';
      dot.className = 'w-1.5 h-1.5 rounded-full bg-emerald-500 inline-block';
      text.textContent = isJa ? 'ON（表示）' : 'ON (Show)';
    } else {
      btn.className = 'py-0.5 px-2.5 rounded-full text-[10px] font-extrabold transition shadow-2xs flex items-center space-x-1.5 bg-slate-100 text-slate-600 border border-slate-300 active:scale-95';
      dot.className = 'w-1.5 h-1.5 rounded-full bg-slate-400 inline-block';
      text.textContent = isJa ? 'OFF（非表示）' : 'OFF (Hide)';
    }
  }

  function setQuizMode(mode) {
    currentQuizMode = (mode === 'test') ? 'test' : 'quiz';
    const btnModeQuiz = document.getElementById('btnModeQuiz');
    const btnModeTest = document.getElementById('btnModeTest');
    const testTypeContainer = document.getElementById('testTypeSelectorContainer');
    const quizBadgeTitle = document.getElementById('quizBadgeTitle');
    const inactivePill = 'flex-1 py-1.5 px-2 rounded-xl text-xs font-bold transition flex items-center justify-center space-x-1 text-slate-500 hover:text-darkNavyText';
    const activeQuizPill = 'flex-1 py-1.5 px-2 rounded-xl text-xs font-bold transition flex items-center justify-center space-x-1 bg-white text-darkNavyText shadow-2xs';
    const activeTestPill = 'flex-1 py-1.5 px-2 rounded-xl text-xs font-bold transition flex items-center justify-center space-x-1 bg-teal-700 text-white shadow-2xs';

    if (currentQuizMode === 'test') {
      if (btnModeQuiz) btnModeQuiz.className = inactivePill;
      if (btnModeTest) btnModeTest.className = activeTestPill;
      if (testTypeContainer) testTypeContainer.classList.remove('hidden');
      if (quizBadgeTitle) {
        quizBadgeTitle.textContent = (currentLang === 'ja') ? '実践テスト' : 'Practice Test';
        quizBadgeTitle.className = 'text-xs font-black text-teal-800 px-2.5 py-0.5 bg-teal-50 border border-teal-200 rounded-full';
      }
    } else {
      if (btnModeQuiz) btnModeQuiz.className = activeQuizPill;
      if (btnModeTest) btnModeTest.className = inactivePill;
      if (testTypeContainer) testTypeContainer.classList.add('hidden');
      if (quizBadgeTitle) {
        quizBadgeTitle.textContent = (currentLang === 'ja') ? '単語クイズ' : 'Review Quiz';
        quizBadgeTitle.className = 'text-xs font-bold text-deepNavy px-2.5 py-0.5 bg-lightBlueBg rounded-full';
      }
    }
  }

  function getEffectiveQuizLimit() {
    if (quizQuestionLimit === 'all' || quizQuestionLimit >= 9999) {
      return quizPool.length;
    }
    return Math.min(quizPool.length, quizQuestionLimit);
  }

  // --- Allowed Quiz Vocabulary Pool (生徒マイリスト + 全員共有単語のみ) ---
  function getAllowedQuizCards() {
    const currentId = currentStudent ? currentStudent.id : 'guest';
    const isTeacher = !!(currentStudent && (currentStudent.id === 'haku' || currentStudent.id === 'admin'));

    return vocabList.filter(c => {
      if (!c || isStubCard(c) || isCorruptedCard(c)) return false;
      // 1. マイリストに入っている単語は生徒本人の学習対象なので最優先で含める！
      if (mylistSet && mylistSet.has(c.id)) return true;
      // 2. 先生ログイン中は全単語対象
      if (isTeacher) return true;
      // 3. 全員共有単語（seedカード、または studentId が未設定 / 'all' の単語）
      if (!c.studentId || c.studentId === 'all') return true;
      // 4. 自分自身の生徒ID宛ての単語
      if (currentId !== 'guest' && c.studentId === currentId) return true;
      // 5. それ以外の生徒専用カード（他の生徒専用カード）は絶対に除外！
      return false;
    });
  }
  let quizScope = 'current'; // 'current', 'folder', 'mylist', 'all'
  let quizScopeDetails = { type: 'current', id: null, title: '現在の単元' };

  function startQuizWithScope(type, id = null, title = '') {
    quizScope = type;
    quizScopeDetails = { type, id, title: title || '選択中スコープ' };
    switchView('quiz');
    startQuiz();
  }

  function startQuiz() {
    setQuizMode(currentQuizMode);
    let sourcePool = [];

    if (quizScope === 'all') {
      sourcePool = getAllowedQuizCards();
    } else if (quizScope === 'mylist') {
      let starredCards = getMylistCards();
      if (activeMylistFolderId && activeMylistFolderId !== 'all') {
        starredCards = starredCards.filter(c => mylistCardFolderMap[c.id] === activeMylistFolderId);
      }
      sourcePool = starredCards;
    } else if (quizScope === 'folder') {
      const folderId = quizScopeDetails.id || currentFolder;
      sourcePool = vocabList.filter(c => c.folder_id === folderId);
    } else {
      // 'current' unit or whatever activeDeck is
      sourcePool = (activeDeck && activeDeck.length >= 2) ? [...activeDeck] : getAllowedQuizCards();
    }

    // Update UI badge
    const summaryBadge = document.getElementById('quizScopeSummaryBadge');
    if (summaryBadge) {
      if (quizScope === 'all') {
        summaryBadge.textContent = 'Shuffle All Units';
      } else if (quizScope === 'mylist') {
        const folderObj = mylistFolders.find(f => f.id === activeMylistFolderId);
        summaryBadge.textContent = folderObj ? `My List: 📁${folderObj.name}` : 'My List (All)';
      } else if (quizScope === 'folder') {
        const fc = FOLDER_CONFIGS.find(f => f.id === (quizScopeDetails.id || currentFolder));
        summaryBadge.textContent = fc ? `📁 ${fc.title}` : 'Entire Folder';
      } else {
        summaryBadge.textContent = quizScopeDetails.title || 'Current Unit';
      }
    }

    // Highlight active scope button if matches
    const btnCur = document.getElementById('btnQuizScopeCurrent');
    const btnMy = document.getElementById('btnQuizScopeMylist');
    const btnAll = document.getElementById('btnQuizScopeAll');
    if (btnCur && btnMy && btnAll) {
      const inactiveClass = 'py-1 px-1.5 rounded-xl text-[10px] font-bold border border-softBorder bg-white text-slate-600 hover:border-deepNavy transition text-center truncate';
      const activeClass = 'py-1 px-1.5 rounded-xl text-[10px] font-bold bg-deepNavy text-white transition shadow-2xs text-center truncate';
      btnCur.className = (quizScope === 'current' || quizScope === 'folder') ? activeClass : inactiveClass;
      btnMy.className = (quizScope === 'mylist') ? activeClass : inactiveClass;
      btnAll.className = (quizScope === 'all') ? activeClass : inactiveClass;
    }

    if (sourcePool.length < 2) {
      const container = document.getElementById('quizChoicesContainer');
      if (container) {
        container.innerHTML = `
          <div class="text-center py-10 text-slate-400 text-xs">
            <i data-lucide="alert-circle" class="w-8 h-8 mx-auto text-amber-500 mb-2"></i>
            <p class="font-bold text-slate-600 text-sm">Not enough words to test</p>
            <p class="mt-1">At least 2 words are required to start a test.</p>
          </div>
        `;
        lucide.createIcons({ root: container });
      }
      document.getElementById('quizQuestionText').textContent = '—';
      document.getElementById('quizQuestionHint').textContent = '';
      return;
    }

    // Shuffle cards for quiz pool
    quizPool = sourcePool.sort(() => Math.random() - 0.5);
    quizIndex = 0;
    quizScore = 0;
    renderQuizQuestion();
  }

  function renderQuizQuestion() {
    const effectiveLimit = getEffectiveQuizLimit();
    if (quizIndex >= effectiveLimit) {
      showQuizFinished();
      return;
    }

    quizCurrentQuestion = quizPool[quizIndex];
    document.getElementById('quizScoreBadge').textContent = `Question ${quizIndex + 1} / ${effectiveLimit}`;
    updateMultilingualButtonUI();
    
    const meaning = getBilingualMeaning(quizCurrentQuestion.meaning, currentLang);
    const isJa = (currentLang === 'ja');

    const promptEl = document.getElementById('quizQuestionPrompt');
    const textEl = document.getElementById('quizQuestionText');
    const hintEl = document.getElementById('quizQuestionHint');
    const typeBadgeContainer = document.getElementById('quizQuestionTypeBadgeContainer');
    const typeBadge = document.getElementById('quizQuestionTypeBadge');
    const sentenceBox = document.getElementById('quizSentenceBox');
    const sentenceText = document.getElementById('quizSentenceText');
    const sentenceTrans = document.getElementById('quizSentenceTrans');
    const container = document.getElementById('quizChoicesContainer');
    container.innerHTML = '';

    const feedbackBox = document.getElementById('quizFeedbackBox');
    feedbackBox.classList.add('hidden');
    feedbackBox.innerHTML = `
      <p id="quizFeedbackMessage" class="text-sm font-bold"></p>
      <div id="quizFeedbackDetail" class="text-xs mt-1 text-slate-600 select-text"></div>
    `;
    document.getElementById('btnQuizNext').disabled = true;

    let hasAnsweredThisQuestion = false;

    // Determine Question Type
    const isTestMode = (currentQuizMode === 'test');
    let chosenTestType = isTestMode ? currentTestSubtype : 'quiz';
    const baseVerb = getBaseVerbFromConjugated(quizCurrentQuestion.word, quizCurrentQuestion.category);
    const hasVerbConjugation = !!(baseVerb && (baseVerb !== quizCurrentQuestion.word || (quizCurrentQuestion.category && (quizCurrentQuestion.category.includes('動詞') || quizCurrentQuestion.category.includes('form') || quizCurrentQuestion.category.includes('形')))));
    const hasSentence = !!(quizCurrentQuestion.example && quizCurrentQuestion.example.ja);

    if (isTestMode) {
      if (chosenTestType === 'all') {
        chosenTestType = (hasVerbConjugation && Math.random() < 0.5) ? 'conjugation' : 'fillblank';
      }
      if (chosenTestType === 'conjugation' && !hasVerbConjugation) {
        chosenTestType = 'fillblank'; // fallback if no conjugation available
      }
    }

    let choices = [];
    currentQuestionMeta = {
      mode: currentQuizMode,
      type: chosenTestType,
      baseWord: baseVerb || quizCurrentQuestion.word,
      targetCard: quizCurrentQuestion,
      bilingualMeaning: meaning,
      sentenceHtml: quizCurrentQuestion.example ? quizCurrentQuestion.example.ja : '',
      sentenceTrans: quizCurrentQuestion.example ? (quizCurrentQuestion.example[currentLang] || quizCurrentQuestion.example.en || '') : ''
    };

    if (isTestMode && chosenTestType === 'fillblank') {
      // ===== TYPE A: 例文 穴埋めテスト =====
      if (typeBadgeContainer) {
        typeBadgeContainer.classList.remove('hidden');
        if (typeBadge) typeBadge.innerHTML = '<i data-lucide="book-open" class="w-3 h-3 text-teal-600"></i><span>A: 例文 穴埋めテスト (Fill-in-the-blank)</span>';
      }
      if (sentenceBox) {
        sentenceBox.classList.remove('hidden');
        if (sentenceText) sentenceText.innerHTML = maskTargetWordInSentence(quizCurrentQuestion.example ? quizCurrentQuestion.example.ja : '', quizCurrentQuestion.word);
        if (sentenceTrans) {
          if (isMultilingualEnabled && currentQuestionMeta.sentenceTrans) {
            let transText = currentQuestionMeta.sentenceTrans.replace(/<br\s*\/?>/gi, '<br/>');
            // Foolproof safeguard: mask any Japanese in parentheses or the target word itself from the translation
            transText = transText.replace(/\([ぁ-んァ-ヶ一-龥]+\)/g, '［ ? ］');
            const cleanTargetWord = (quizCurrentQuestion.word || '').replace(/<rt>[^<]*<\/rt>/g, '').replace(/<\/?ruby>/g, '').trim();
            if (cleanTargetWord) {
              transText = transText.replace(new RegExp(escapeRegex(cleanTargetWord), 'g'), '［ ? ］');
            }
            if (quizCurrentQuestion.reading) {
              transText = transText.replace(new RegExp(escapeRegex(quizCurrentQuestion.reading), 'g'), '［ ? ］');
            }
            sentenceTrans.innerHTML = transText;
            sentenceTrans.classList.remove('hidden');
          } else {
            sentenceTrans.classList.add('hidden');
          }
        }
      }

      if (promptEl) promptEl.textContent = isJa ? '文中の［ ？ ］に入る最も適切な言葉を選んでください' : 'Select the best word/form that fits the sentence';
      if (textEl) {
        textEl.className = 'my-1.5 text-center select-text font-jp';
        // Only show base verb if it is truly a conjugated form (e.g. 作る -> 作らない)
        if (hasVerbConjugation && currentQuestionMeta.baseWord !== quizCurrentQuestion.word) {
          textEl.innerHTML = `
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-100 border border-slate-200 text-xs font-semibold text-slate-700 shadow-2xs">
              <span class="text-teal-700 font-bold">💡 変化させる動詞:</span>
              <span class="font-extrabold text-darkNavyText">「${currentQuestionMeta.baseWord}」</span>
              ${isMultilingualEnabled ? `<span class="text-slate-400 font-medium">(${meaning})</span>` : ''}
            </div>
          `;
        } else {
          // General vocabulary (nouns, counters, etc.): NEVER show the Japanese word before answering!
          if (isMultilingualEnabled) {
            textEl.innerHTML = `
              <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-100 border border-slate-200 text-xs font-semibold text-slate-700 shadow-2xs">
                <span class="text-teal-700 font-bold">💡 意味のヒント:</span>
                <span class="text-slate-700 font-medium">${meaning}</span>
              </div>
            `;
          } else {
            textEl.innerHTML = '';
          }
        }
      }
      if (hintEl) hintEl.textContent = quizCurrentQuestion.category ? `【分類】${quizCurrentQuestion.category}` : '';

      // Build Choices for Type A
      if (hasVerbConjugation) {
        const conj = conjugateJapaneseVerb(currentQuestionMeta.baseWord, quizCurrentQuestion.reading, quizCurrentQuestion.category);
        if (conj) {
          const formCandidates = [
            { id: quizCurrentQuestion.id, word: quizCurrentQuestion.word, reading: quizCurrentQuestion.reading || '', meaning: quizCurrentQuestion.meaning, formLabel: '正解' },
            { id: 'f_masu', word: conj.masu, reading: '', meaning: { en: 'masu-form' }, formLabel: 'ます形' },
            { id: 'f_nai', word: conj.nai, reading: '', meaning: { en: 'nai-form' }, formLabel: 'ない形' },
            { id: 'f_te', word: conj.te, reading: '', meaning: { en: 'te-form' }, formLabel: 'て形' },
            { id: 'f_dict', word: conj.dict, reading: '', meaning: { en: 'dictionary-form' }, formLabel: '辞書形' },
            { id: 'f_pot', word: conj.pot, reading: '', meaning: { en: 'potential-form' }, formLabel: '可能形' }
          ];
          const uniqueWords = new Set([quizCurrentQuestion.word]);
          const selectedForms = [{ id: quizCurrentQuestion.id, word: quizCurrentQuestion.word, reading: quizCurrentQuestion.reading || '', meaning: quizCurrentQuestion.meaning, formLabel: '正解' }];
          formCandidates.forEach(fc => {
            if (!uniqueWords.has(fc.word) && selectedForms.length < 4) {
              uniqueWords.add(fc.word);
              selectedForms.push(fc);
            }
          });
          choices = selectedForms.sort(() => Math.random() - 0.5);
        }
      }
      if (choices.length < 4) {
        const candidatePool = (quizScope === 'all' ? getAllowedQuizCards() : (activeDeck && activeDeck.length >= 4 ? activeDeck : getAllowedQuizCards()));
        const distractorCandidates = candidatePool
          .filter(c => c && c.id !== quizCurrentQuestion.id && c.word !== quizCurrentQuestion.word && (c.reading || c.word))
          .sort(() => Math.random() - 0.5)
          .slice(0, 4 - choices.length);
        choices = [quizCurrentQuestion, ...distractorCandidates].sort(() => Math.random() - 0.5);
      }

    } else if (isTestMode && chosenTestType === 'conjugation') {
      // ===== TYPE B: 活用・文法変換テスト =====
      if (typeBadgeContainer) {
        typeBadgeContainer.classList.remove('hidden');
        if (typeBadge) typeBadge.innerHTML = '<i data-lucide="shuffle" class="w-3 h-3 text-teal-600"></i><span>B: 活用・文法変換テスト (Conjugation Form)</span>';
      }
      if (sentenceBox) sentenceBox.classList.add('hidden');

      const conj = conjugateJapaneseVerb(currentQuestionMeta.baseWord, quizCurrentQuestion.reading, quizCurrentQuestion.category);
      let targetFormName = 'ない形（否定）';
      let wrongPattern = currentQuestionMeta.baseWord + 'ない';

      if (quizCurrentQuestion.category && quizCurrentQuestion.category.includes('てform') || quizCurrentQuestion.word.endsWith('て') || quizCurrentQuestion.word.endsWith('で')) {
        targetFormName = 'て形';
        wrongPattern = currentQuestionMeta.baseWord.slice(0, -1) + 'りて';
      } else if (quizCurrentQuestion.category && quizCurrentQuestion.category.includes('可能形')) {
        targetFormName = '可能形（できる）';
        wrongPattern = currentQuestionMeta.baseWord + 'られる';
      } else if (quizCurrentQuestion.category && quizCurrentQuestion.category.includes('ないform') || quizCurrentQuestion.word.endsWith('ない')) {
        targetFormName = 'ない形（否定）';
        wrongPattern = currentQuestionMeta.baseWord + 'ない';
      } else {
        targetFormName = 'ます形';
        wrongPattern = currentQuestionMeta.baseWord + 'ます';
      }
      currentQuestionMeta.formName = targetFormName;

      if (promptEl) {
        promptEl.textContent = isJa 
          ? '指定された活用形を選んでください' 
          : 'Select the requested verb form:';
      }
      if (textEl) {
        textEl.className = 'my-2 text-center select-text font-jp';
        textEl.innerHTML = `
          <div class="flex flex-col items-center justify-center space-y-1.5">
            <span class="text-2xl sm:text-3xl font-black text-darkNavyText">「${currentQuestionMeta.baseWord}」</span>
            <span class="inline-flex items-center px-3.5 py-1 rounded-full bg-teal-50 border border-teal-300 text-teal-800 text-xs sm:text-sm font-extrabold shadow-2xs">
              【 ${targetFormName} 】
            </span>
            ${isMultilingualEnabled ? `<span class="text-xs text-slate-500 font-medium pt-0.5">意味: ${meaning}</span>` : ''}
          </div>
        `;
      }
      if (hintEl) hintEl.textContent = conj ? `【動詞グループ】${conj.group}` : (quizCurrentQuestion.category || '文法・活用');

      if (conj) {
        const poolOptions = [
          { id: quizCurrentQuestion.id, word: quizCurrentQuestion.word, reading: quizCurrentQuestion.reading || '', meaning: quizCurrentQuestion.meaning, formLabel: targetFormName },
          { id: 'f_wrong', word: wrongPattern, reading: '', meaning: { en: 'Incorrect form' }, formLabel: '誤答例' },
          { id: 'f_masu', word: conj.masu, reading: '', meaning: { en: 'masu-form' }, formLabel: 'ます形' },
          { id: 'f_te', word: conj.te, reading: '', meaning: { en: 'te-form' }, formLabel: 'て形' },
          { id: 'f_nai', word: conj.nai, reading: '', meaning: { en: 'nai-form' }, formLabel: 'ない形' },
          { id: 'f_dict', word: conj.dict, reading: '', meaning: { en: 'dict-form' }, formLabel: '辞書形' }
        ];
        const uniqueWords = new Set();
        const selectedForms = [];
        poolOptions.forEach(p => {
          if (!uniqueWords.has(p.word) && selectedForms.length < 4) {
            uniqueWords.add(p.word);
            selectedForms.push(p);
          }
        });
        choices = selectedForms.sort(() => Math.random() - 0.5);
      }
      if (choices.length < 4) {
        const candidatePool = (quizScope === 'all' ? getAllowedQuizCards() : (activeDeck && activeDeck.length >= 4 ? activeDeck : getAllowedQuizCards()));
        const distractorCandidates = candidatePool
          .filter(c => c && c.id !== quizCurrentQuestion.id && c.word !== quizCurrentQuestion.word && (c.reading || c.word))
          .sort(() => Math.random() - 0.5)
          .slice(0, 4 - choices.length);
        choices = [quizCurrentQuestion, ...distractorCandidates].sort(() => Math.random() - 0.5);
      }

    } else {
      // ===== STANDARD QUIZ: 単語・意味マッチ =====
      if (typeBadgeContainer) typeBadgeContainer.classList.add('hidden');
      if (sentenceBox) sentenceBox.classList.add('hidden');

      if (promptEl) promptEl.textContent = isJa ? '一致する日本語の単語を選んでください' : 'Select the matching Japanese word';
      if (textEl) {
        textEl.className = 'text-xl sm:text-2xl font-extrabold text-darkNavyText my-1 select-text font-jp';
        if (quizCurrentQuestion.category && quizCurrentQuestion.category.includes('ないform')) {
          textEl.textContent = isMultilingualEnabled ? `${meaning} [ない-form / 否定]` : `${quizCurrentQuestion.word} [ない形]`;
        } else if (quizCurrentQuestion.category && quizCurrentQuestion.category.includes('てform')) {
          textEl.textContent = isMultilingualEnabled ? `${meaning} [て-form]` : `${quizCurrentQuestion.word} [て形]`;
        } else if (quizCurrentQuestion.category && quizCurrentQuestion.category.includes('可能形')) {
          textEl.textContent = isMultilingualEnabled ? `${meaning} [可能形 / potential]` : `${quizCurrentQuestion.word} [可能形]`;
        } else {
          textEl.textContent = isMultilingualEnabled ? meaning : quizCurrentQuestion.word;
        }
      }
      if (hintEl) hintEl.textContent = quizCurrentQuestion.category ? `【分類】${quizCurrentQuestion.category}` : 'General';

      const candidatePool = (quizScope === 'all' ? getAllowedQuizCards() : (activeDeck && activeDeck.length >= 4 ? activeDeck : getAllowedQuizCards()));
      const distractorCandidates = candidatePool
        .filter(c => c && c.id !== quizCurrentQuestion.id && (c.reading || c.word))
        .sort(() => Math.random() - 0.5)
        .slice(0, 3);
      choices = [quizCurrentQuestion, ...distractorCandidates].sort(() => Math.random() - 0.5);
    }

    choices.forEach(card => {
      const cardMeaningText = getBilingualMeaning(card.meaning, currentLang);
      const isCorrectCard = (card.id === quizCurrentQuestion.id || card.word === quizCurrentQuestion.word);

      const btn = document.createElement('div');
      btn.className = 'quiz-choice-card w-full p-3 sm:p-3.5 rounded-2xl border-2 border-softBorder hover:border-deepNavy bg-white text-darkNavyText text-left transition flex flex-col shadow-2xs text-sm cursor-pointer select-text relative active:scale-[0.99]';
      btn.setAttribute('data-card-id', card.id || card.word);
      btn.setAttribute('data-card-word', card.word);

      btn.innerHTML = `
        <div class="choice-main-row flex items-center justify-between w-full select-text">
          <div class="flex items-center space-x-2 min-w-0 select-text">
            <span class="choice-word font-extrabold text-base sm:text-lg text-darkNavyText select-text font-jp">${card.word}</span>
            <span class="choice-reading card-reading-text text-xs text-slate-400 font-normal select-text">${card.reading ? '（' + card.reading + '）' : (card.formLabel ? '【' + card.formLabel + '】' : '')}</span>
          </div>
          <div class="choice-action-row flex items-center space-x-1.5 shrink-0">
            <button class="btn-choice-tts p-1.5 rounded-full hover:bg-slate-100 text-slate-400 hover:text-deepNavy transition active:scale-95" title="発音を聴く">
              <i data-lucide="volume-2" class="w-4 h-4"></i>
            </button>
            <span class="choice-badge-indicator flex items-center">
              <i data-lucide="chevron-right" class="w-4 h-4 text-slate-300"></i>
            </span>
          </div>
        </div>
        <!-- 意味表示パネル（回答後またはタップで表示） -->
        <div class="choice-meaning-panel mt-2 pt-2 border-t border-slate-100 text-xs text-slate-600 font-medium select-text hidden animate-fade-in">
          <div class="flex items-center justify-between gap-1.5 flex-wrap">
            <span class="text-slate-800 select-text font-bold flex-1">
              ${isMultilingualEnabled ? `<span class="text-[10px] text-slate-400 uppercase font-bold mr-1">意味:</span>${cardMeaningText}` : (card.formLabel ? `<span class="text-[10px] text-teal-700 uppercase font-bold mr-1">形:</span>${card.formLabel}` : `<span class="text-[10px] text-slate-400 uppercase font-bold mr-1">単語:</span>${card.word}`)}
            </span>
            <div class="flex items-center space-x-1 shrink-0">
              <button class="btn-choice-dict text-[10px] px-2 py-0.5 rounded-md bg-sky-50 text-sky-700 hover:bg-sky-100 border border-sky-200 font-bold transition flex items-center space-x-0.5" title="辞書で詳細を見る">
                <i data-lucide="search" class="w-2.5 h-2.5"></i>
                <span>辞書</span>
              </button>
              <button class="btn-choice-save text-[10px] px-2 py-0.5 rounded-md ${mylistSet.has(card.id) ? 'bg-coralPink text-white' : 'bg-slate-100 hover:bg-slate-200 text-slate-600'} font-bold transition flex items-center space-x-0.5" title="マイリストに追加">
                <i data-lucide="bookmark" class="w-2.5 h-2.5"></i>
                <span class="choice-save-label">${mylistSet.has(card.id) ? '保存済' : '保存'}</span>
              </button>
            </div>
          </div>
        </div>
      `;
      lucide.createIcons({ root: btn });

      // TTS Audio
      const ttsBtn = btn.querySelector('.btn-choice-tts');
      if (ttsBtn) {
        ttsBtn.addEventListener('click', (e) => {
          e.stopPropagation();
          speakJapanese(card);
        });
      }

      // Dict button
      const dictBtn = btn.querySelector('.btn-choice-dict');
      if (dictBtn) {
        dictBtn.addEventListener('click', (e) => {
          e.stopPropagation();
          openDictLookupModal(card.word, card.reading);
        });
      }

      // Save to My List button
      const saveBtn = btn.querySelector('.btn-choice-save');
      if (saveBtn) {
        saveBtn.addEventListener('click', (e) => {
          e.stopPropagation();
          const label = saveBtn.querySelector('.choice-save-label');
          if (mylistSet.has(card.id)) {
            mylistSet.delete(card.id);
            saveBtn.className = 'btn-choice-save text-[10px] px-2 py-0.5 rounded-md bg-slate-100 hover:bg-slate-200 text-slate-600 font-bold transition flex items-center space-x-0.5';
            if (label) label.textContent = '保存';
            showToast('マイリストから解除しました');
          } else {
            promptFolderSelectAndAdd(card, () => {
              saveBtn.className = 'btn-choice-save text-[10px] px-2 py-0.5 rounded-md bg-coralPink text-white font-bold transition flex items-center space-x-0.5';
              if (label) label.textContent = '保存済';
              updateMylistBadge();
            });
          }
          saveMylistForCurrentStudent();
        });
      }

      // Card click
      btn.addEventListener('click', () => {
        if (!hasAnsweredThisQuestion) {
          hasAnsweredThisQuestion = true;
          handleQuizAnswer(card, btn, container, choices);
        } else {
          speakJapanese(card);
          const panel = btn.querySelector('.choice-meaning-panel');
          if (panel) {
            panel.classList.remove('hidden');
          }
        }
      });

      container.appendChild(btn);
    });
  }

  function handleQuizAnswer(selectedCard, clickedBtn, container, choices) {
    const feedbackBox = document.getElementById('quizFeedbackBox');
    feedbackBox.classList.remove('hidden');

    const isCorrect = (selectedCard.id === quizCurrentQuestion.id || selectedCard.word === quizCurrentQuestion.word);
    const allCards = container.querySelectorAll('.quiz-choice-card');

    // Reveal meaning on all choice cards so student sees meaning of all words!
    allCards.forEach(cardEl => {
      const cWord = cardEl.getAttribute('data-card-word');
      const isTarget = (cWord === quizCurrentQuestion.word);
      const isChosenWrong = (cardEl === clickedBtn && !isCorrect);
      
      const panel = cardEl.querySelector('.choice-meaning-panel');
      if (panel) panel.classList.remove('hidden');

      const indicator = cardEl.querySelector('.choice-badge-indicator');
      if (isTarget) {
        cardEl.classList.remove('border-softBorder', 'hover:border-deepNavy');
        cardEl.classList.add('border-emerald-500', 'bg-emerald-50/70', 'ring-1', 'ring-emerald-400');
        if (indicator) {
          indicator.innerHTML = '<span class="text-[11px] font-bold px-2 py-0.5 rounded-full bg-emerald-600 text-white shrink-0 shadow-2xs">✓ 正解</span>';
        }
      } else if (isChosenWrong) {
        cardEl.classList.remove('border-softBorder', 'hover:border-deepNavy');
        cardEl.classList.add('border-coralPink', 'bg-rose-50/70', 'ring-1', 'ring-rose-400');
        if (indicator) {
          indicator.innerHTML = '<span class="text-[11px] font-bold px-2 py-0.5 rounded-full bg-coralPink text-white shrink-0 shadow-2xs">✕ あなたの回答</span>';
        }
      }
    });

    const targetMeaning = getBilingualMeaning(quizCurrentQuestion.meaning, currentLang);
    const selectedMeaning = getBilingualMeaning(selectedCard.meaning, currentLang);

    let feedbackDetailHtml = '';
    if (currentQuestionMeta && currentQuestionMeta.type === 'fillblank') {
      feedbackDetailHtml = `
        <div class="mt-2 p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-700 leading-relaxed font-jp">
          <span class="text-[10px] font-black px-1.5 py-0.2 rounded-md bg-teal-100 text-teal-800 mr-1">完成文</span>
          ${currentQuestionMeta.sentenceHtml || quizCurrentQuestion.word}
        </div>
      `;
    } else if (currentQuestionMeta && currentQuestionMeta.type === 'conjugation') {
      feedbackDetailHtml = `
        <div class="mt-2 p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-700 leading-relaxed font-jp">
          <span class="text-[10px] font-black px-1.5 py-0.2 rounded-md bg-teal-100 text-teal-800 mr-1">活用ルール</span>
          ${currentQuestionMeta.baseWord} → <strong class="text-emerald-700 underline font-extrabold">${quizCurrentQuestion.word}</strong>（${currentQuestionMeta.formName || '正解の形'}）
          ${currentQuestionMeta.sentenceHtml ? `<div class="mt-1 text-slate-500 text-[11px]">例文: ${currentQuestionMeta.sentenceHtml}</div>` : ''}
        </div>
      `;
    }

    if (isCorrect) {
      quizScore++;
      feedbackBox.className = 'p-3.5 rounded-2xl my-3 text-center bg-emerald-50 border border-emerald-200 text-emerald-900 select-text animate-fade-in shadow-2xs';
      feedbackBox.innerHTML = `
        <div class="flex items-center justify-center space-x-1.5 font-extrabold text-sm text-emerald-800">
          <span>✨</span>
          <span>Correct! 正解です！</span>
        </div>
        <div class="mt-2 p-2.5 rounded-xl bg-white/90 border border-emerald-200 text-left select-text shadow-2xs">
          <div class="flex items-center justify-between">
            <span class="font-extrabold text-sm text-darkNavyText font-jp select-text">${quizCurrentQuestion.word}（${quizCurrentQuestion.reading || ''}）</span>
            <button class="btn-feedback-speak p-1.5 rounded-full text-emerald-700 hover:bg-emerald-100 transition" data-word="${escapeHtml(quizCurrentQuestion.word)}" title="発音を聴く">
              <i data-lucide="volume-2" class="w-4 h-4"></i>
            </button>
          </div>
          ${isMultilingualEnabled ? `<p class="text-xs text-emerald-800 font-semibold mt-0.5 select-text"><span class="text-[10px] text-slate-400 uppercase font-bold mr-1">意味:</span>${targetMeaning}</p>` : ''}
          ${feedbackDetailHtml}
        </div>
      `;
      speakJapanese(quizCurrentQuestion);
    } else {
      feedbackBox.className = 'p-3.5 rounded-2xl my-3 text-center bg-rose-50 border border-rose-200 text-rose-900 select-text animate-fade-in shadow-2xs';
      feedbackBox.innerHTML = `
        <div class="font-extrabold text-sm text-rose-800 flex items-center justify-center space-x-1">
          <span>Not quite! 不正解</span>
        </div>

        <!-- 正解の単語 -->
        <div class="mt-2 p-2.5 rounded-xl bg-white/95 border-2 border-emerald-400 text-left select-text shadow-2xs">
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-1.5 select-text">
              <span class="text-[10px] px-1.5 py-0.2 rounded-full bg-emerald-600 text-white font-bold shrink-0">正解</span>
              <span class="font-extrabold text-sm text-darkNavyText font-jp select-text">${quizCurrentQuestion.word}（${quizCurrentQuestion.reading || ''}）</span>
            </div>
            <button class="btn-feedback-speak p-1.5 rounded-full text-emerald-700 hover:bg-emerald-100 transition" data-word="${escapeHtml(quizCurrentQuestion.word)}" title="発音を聴く">
              <i data-lucide="volume-2" class="w-4 h-4"></i>
            </button>
          </div>
          ${isMultilingualEnabled ? `<p class="text-xs text-emerald-900 font-bold mt-1 select-text"><span class="text-[10px] text-slate-400 uppercase font-bold mr-1">意味:</span>${targetMeaning}</p>` : ''}
          ${feedbackDetailHtml}
        </div>

        <!-- ユーザーが選んだ言葉 -->
        <div class="mt-1.5 p-2.5 rounded-xl bg-white/95 border-2 border-coralPink text-left select-text shadow-2xs">
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-1.5 select-text">
              <span class="text-[10px] px-1.5 py-0.2 rounded-full bg-coralPink text-white font-bold shrink-0">選んだ形</span>
              <span class="font-extrabold text-sm text-darkNavyText font-jp select-text">${selectedCard.word}（${selectedCard.reading || ''}）</span>
            </div>
            <button class="btn-feedback-speak p-1.5 rounded-full text-rose-700 hover:bg-rose-100 transition" data-word="${escapeHtml(selectedCard.word)}" title="発音を聴く">
              <i data-lucide="volume-2" class="w-4 h-4"></i>
            </button>
          </div>
          ${isMultilingualEnabled ? `<p class="text-xs text-rose-900 font-bold mt-1 select-text"><span class="text-[10px] text-slate-400 uppercase font-bold mr-1">意味:</span>${selectedMeaning}</p>` : ''}
        </div>

        <p class="text-[10px] text-slate-500 font-medium mt-2">💡 上の選択肢カードでも全単語の意味や発音が確認でき、保存も可能です。</p>
      `;
      mylistSet.add(quizCurrentQuestion.id);
      saveMylistForCurrentStudent();
      showToast('間違えた単語をマイリストに追加しました ⭐');
    }

    lucide.createIcons({ root: feedbackBox });
    feedbackBox.querySelectorAll('.btn-feedback-speak').forEach(btn => {
      btn.addEventListener('click', () => {
        const w = btn.getAttribute('data-word');
        speakJapanese({ word: w });
      });
    });

    document.getElementById('btnQuizNext').disabled = false;
  }

  function showQuizFinished() {
    const container = document.getElementById('quizChoicesContainer');
    container.innerHTML = `
      <div class="text-center py-6">
        <div class="text-4xl mb-2">🏆</div>
        <h4 class="text-xl font-bold text-slate-900">Quiz Completed!</h4>
        <p class="text-sm text-slate-600 mt-1">Score: <span class="text-rose-600 font-extrabold text-lg">${quizScore}</span> / ${getEffectiveQuizLimit()} Correct</p>
        <button id="btnRestartQuiz" class="mt-5 px-6 py-2.5 rounded-2xl bg-rose-600 text-white font-bold text-xs shadow-md">Try Again</button>
      </div>
    `;
    document.getElementById('quizQuestionText').textContent = 'Well done! Great job! 🎉';
    document.getElementById('quizQuestionHint').textContent = '';
    document.getElementById('quizFeedbackBox').classList.add('hidden');
    document.getElementById('btnQuizNext').classList.add('hidden');

    document.getElementById('btnRestartQuiz').addEventListener('click', () => {
      document.getElementById('btnQuizNext').classList.remove('hidden');
      startQuiz();
    });
  }

  // --- Card Resolution Helper for My List & Study ---
  // Resolves a card by ID or word across vocabList, CLASS_VOCAB_DATA, INITIAL_VOCAB_DATA, and DICT_DATA
  function getCardById(cardId) {
    if (!cardId) return null;
    if (typeof MIDORI_CURATED_CARDS !== 'undefined') {
      const mCurated = MIDORI_CURATED_CARDS.find(c => c.id === cardId || c.word === cardId);
      if (mCurated) return mCurated;
    }
    if (typeof DANIEL_CURATED_CARDS !== 'undefined') {
      const dCurated = DANIEL_CURATED_CARDS.find(c => c.id === cardId || c.word === cardId);
      if (dCurated) return dCurated;
    }
    if (typeof ELIIE_CURATED_CARDS !== 'undefined') {
      const eCurated = ELIIE_CURATED_CARDS.find(c => c.id === cardId || c.word === cardId);
      if (eCurated) return eCurated;
    }
    if (typeof ARUN_CURATED_CARDS !== 'undefined') {
      const aCurated = ARUN_CURATED_CARDS.find(c => c.id === cardId || c.word === cardId);
      if (aCurated) return aCurated;
    }
    // 1. Check current in-memory vocabList
    let found = vocabList.find(c => (c.id === cardId || c.word === cardId) && !isStubCard(c));
    if (found) return found;

    // 1b. Check haku_all_custom_cards from localStorage
    try {
      const storedCustom = JSON.parse(localStorage.getItem('haku_all_custom_cards') || '[]');
      if (Array.isArray(storedCustom)) {
        found = storedCustom.find(c => (c.id === cardId || c.word === cardId) && !isStubCard(c));
        if (found) {
          found.isCustom = true;
          if (!vocabList.find(c => c.id === found.id)) vocabList.push(found);
          return found;
        }
      }
    } catch (e) {}

    // 2. Check CLASS_VOCAB_DATA
    if (window.CLASS_VOCAB_DATA) {
      found = window.CLASS_VOCAB_DATA.find(c => c.id === cardId || c.word === cardId);
      if (found) return found;
    }

    // 3. Check INITIAL_VOCAB_DATA
    if (window.INITIAL_VOCAB_DATA) {
      found = window.INITIAL_VOCAB_DATA.find(c => c.id === cardId || c.word === cardId);
      if (found) return found;
    }

    // 4. Check DICT_DATA
    if (window.DICT_DATA) {
      let wordToFind = cardId;
      if (cardId.startsWith('dict_')) {
        const parts = cardId.split('_');
        if (parts.length >= 3) {
          wordToFind = parts.slice(1, parts.length - 1).join('_');
        }
      }
      const entry = window.DICT_DATA.find(d => d.w === wordToFind || d.w === cardId);
      if (entry) {
        const exMap = window.DICT_EXAMPLES_MAP || {};
        const matchedEx = exMap[entry.w] || (entry.r ? exMap[entry.r] : null);
        const fallbackDlg = getNaturalDefaultDialogue(entry.w, entry.r);
        return {
          id: cardId,
          word: entry.w,
          reading: entry.r || entry.w,
          category: entry.l ? `JLPT ${entry.l}` : '辞書',
          section_title: '日本語大辞書',
          meaning: {
            en: (entry.m && entry.m.join(', ')) || '—',
            ja: entry.w,
            zh_TW: (entry.zh && entry.zh.join(', ')) || (entry.m && entry.m.join(', ')) || '—',
            zh_CN: (entry.zh && entry.zh.join(', ')) || (entry.m && entry.m.join(', ')) || '—',
            ko: (entry.m && entry.m.join(', ')) || '—',
            zh_HK: (entry.zh && entry.zh.join(', ')) || (entry.m && entry.m.join(', ')) || '—',
            fr: (entry.fr && entry.fr.join(', ')) || (entry.m && entry.m.join(', ')) || '—'
          },
          example: {
            ja: matchedEx ? matchedEx.ja : fallbackDlg.ja,
            en: matchedEx ? (matchedEx.en || '') : fallbackDlg.en
          },
          related: `【品詞】${entry.p || '一般'} / 【JLPT】${entry.l || '一般'}`,
          isDict: true
        };
      }
    }

    // 5. Check JLPT_VOCAB
    if (window.JLPT_VOCAB) {
      let jlptWordToFind = cardId;
      if (cardId.startsWith('jlpt_')) {
        const parts = cardId.split('_');
        if (parts.length >= 4) {
          jlptWordToFind = parts.slice(3).join('_');
        } else if (parts.length >= 3) {
          jlptWordToFind = parts.slice(1, parts.length - 1).join('_');
        }
      }
      for (const lvl of ['N5', 'N4', 'N3', 'N2', 'N1']) {
        const list = window.JLPT_VOCAB[lvl] || [];
        const entry = list.find(w => w.word === jlptWordToFind || w.word === cardId);
        if (entry) {
          const dictMap = window.DICT_EXAMPLES_MAP || {};
          const dictEx = dictMap[entry.word] || (entry.reading && dictMap[entry.reading]);
          const ex = (entry.examples && entry.examples[0]) ? entry.examples[0] : (dictEx || null);
          const fallbackDlg = getNaturalDefaultDialogue(entry.word, entry.reading || entry.k);
          const meaningText = (entry.meanings || []).join(', ') || '—';
          return {
            id: cardId,
            word: entry.word,
            reading: entry.reading || entry.k || entry.word,
            category: `JLPT ${entry.level || lvl}`,
            section_title: `JLPT ${entry.level || lvl} 単語`,
            meaning: {
              en: meaningText,
              ja: entry.word,
              zh_TW: meaningText,
              zh_CN: meaningText,
              ko: meaningText,
              zh_HK: meaningText,
              fr: meaningText
            },
            example: {
              ja: ex ? ex.ja : fallbackDlg.ja,
              en: ex ? (ex.en || '') : fallbackDlg.en
            },
            related: `【JLPT】${entry.level || lvl} / 【行】${entry.row || '—'}`,
            isJlpt: true
          };
        }
      }
    }

    // 6. 単語名がわかる場合は、辞書・授業の単語・ネット辞書から自動で作り直す
    const nameInfo = getKnownWordName(cardId);
    if (nameInfo && nameInfo.w && nameInfo.w !== cardId) {
      const base = getCardById(nameInfo.w);
      if (base && !isStubCard(base) && !base.isNameOnly) {
        const resolved = { ...base, id: cardId, word: nameInfo.w, reading: nameInfo.r || base.reading, category: '授業で習った言葉', isRebuilt: true };
        if (!vocabList.find(c => c.id === cardId)) vocabList.push(resolved);
        return resolved;
      }
      const online = getOnlineDictCache()[nameInfo.w];
      if (online && online.en) {
        const fallbackDlg = getNaturalDefaultDialogue(nameInfo.w, nameInfo.r);
        const resolved = {
          id: cardId, word: nameInfo.w, reading: nameInfo.r || '', category: '授業で習った言葉',
          meaning: { en: online.en, ja: nameInfo.w, zh_TW: online.en, zh_CN: online.en, ko: online.en, zh_HK: online.en, fr: online.en },
          example: { ja: fallbackDlg.ja, en: fallbackDlg.en },
          related: '', isRebuilt: true
        };
        if (!vocabList.find(c => c.id === cardId)) vocabList.push(resolved);
        return resolved;
      }
      scheduleOnlineLookup(nameInfo.w);
      const looking = onlineLookupFailed.has(nameInfo.w)
        ? { en: 'Meaning could not be loaded (check connection)', ja: '意味を読み込めませんでした（通信を確認）', zh_TW: '無法載入意思（請檢查網路）', zh_CN: '无法加载意思（请检查网络）', ko: '뜻을 불러오지 못했습니다 (연결 확인)', zh_HK: '載入唔到意思（請檢查網絡）', fr: 'Sens indisponible (vérifiez la connexion)' }
        : { en: 'Looking up meaning…', ja: '意味を調べています…', zh_TW: '正在查詢意思…', zh_CN: '正在查询意思…', ko: '뜻을 찾는 중…', zh_HK: '正在查意思…', fr: 'Recherche du sens…' };
      const fallbackDlg = getNaturalDefaultDialogue(nameInfo.w, nameInfo.r);
      const resolved = {
        id: cardId, word: nameInfo.w, reading: nameInfo.r || '', category: '授業で習った言葉',
        meaning: looking,
        example: { ja: fallbackDlg.ja, en: fallbackDlg.en },
        related: '', isRebuilt: true, isNameOnly: true
      };
      if (!vocabList.find(c => c.id === cardId)) vocabList.push(resolved);
      return resolved;
    }

    // 7. 単語名も不明（古い形式のIDでデータが失われたもの）。isStub を付けてクラウドへは送らない
    return {
      id: cardId,
      word: cardId.replace(/^card_\d+_/, '').replace(/^dict_/, '').replace(/_\d+$/, '') || cardId,
      reading: '',
      category: 'マイリスト',
      meaning: { en: 'Saved Word', ja: cardId, zh_TW: '單詞', zh_CN: '单词', ko: '단어', zh_HK: '單詞', fr: 'Mot' },
      example: { ja: '', en: '' },
      isStub: true
    };
  }

  // --- 単語名レジストリ（ID → 単語名・読み）。定義が消えても単語名だけは必ず残す ---
  function getWordNameRegistry() {
    try { return JSON.parse(localStorage.getItem('haku_word_names') || '{}') || {}; } catch (e) { return {}; }
  }
  function saveWordNameRegistry(reg) {
    try { localStorage.setItem('haku_word_names', JSON.stringify(reg)); } catch (e) {}
  }
  function isCustomCardId(id) {
    return typeof id === 'string' && !id.startsWith('class_word_') && !/^card_\d{4}$/.test(id);
  }
  // 実際のカードから単語名を記録（複数まとめて）
  function recordWordNames(cards) {
    const reg = getWordNameRegistry();
    let changed = false;
    (cards || []).forEach(c => {
      if (!c || !c.id || !c.word || isStubCard(c) || c.isNameOnly || !isCustomCardId(c.id)) return;
      const cur = reg[c.id];
      if (!cur || cur.w !== c.word || (c.reading && cur.r !== c.reading)) {
        reg[c.id] = { w: c.word, r: c.reading || '' };
        changed = true;
      }
    });
    if (changed) saveWordNameRegistry(reg);
    return reg;
  }
  function mergeWordNames(obj) {
    if (!obj || typeof obj !== 'object') return false;
    const reg = getWordNameRegistry();
    let changed = false;
    Object.entries(obj).forEach(([id, v]) => {
      if (v && v.w && !reg[id]) { reg[id] = { w: v.w, r: v.r || '' }; changed = true; }
    });
    if (changed) saveWordNameRegistry(reg);
    return changed;
  }
  // ID から単語名を取得（レジストリ → ID埋め込みの単語名）
  function getKnownWordName(id) {
    if (!id || typeof id !== 'string') return null;
    const reg = getWordNameRegistry();
    if (reg[id] && reg[id].w) return reg[id];
    let m = id.match(/^card_\d+_[a-z0-9]+__(.+)$/);
    if (m) return { w: m[1], r: '' };
    m = id.match(/^(?:custom_ex|custom_dict|dict|jlpt)_(.+)_\d+$/);
    if (m) return { w: m[1], r: '' };
    return null;
  }
  // 指定IDの単語名一覧（クラウド保存用）
  function buildWordNamesFor(ids) {
    const reg = getWordNameRegistry();
    const out = {};
    (ids || []).forEach(id => { if (reg[id]) out[id] = reg[id]; });
    return out;
  }
  // IDの作成日時（card_<timestamp>_...）
  function getCardCreatedDate(id) {
    const m = String(id || '').match(/^card_(\d{12,})_/);
    if (!m) return null;
    const d = new Date(Number(m[1]));
    return isNaN(d.getTime()) ? null : d;
  }

  // --- ネット辞書（Wiktionary）での意味検索。辞書にない単語用 ---
  function getOnlineDictCache() {
    try { return JSON.parse(localStorage.getItem('haku_online_dict_cache') || '{}') || {}; } catch (e) { return {}; }
  }
  const onlineLookupPending = new Set();
  const onlineLookupFailed = new Set(); // 通信失敗した単語はこのセッション中は再検索しない
  let onlineLookupRerenderTimer = null;
  function scheduleOnlineLookup(word) {
    if (!word || onlineLookupPending.has(word) || onlineLookupFailed.has(word) || typeof fetch !== 'function') return;
    const cache = getOnlineDictCache();
    if (cache[word]) return;
    onlineLookupPending.add(word);
    fetch(`https://en.wiktionary.org/api/rest_v1/page/definition/${encodeURIComponent(word)}`)
      .then(r => r.ok ? r.json() : null)
      .then(data => {
        let en = '';
        const ja = data && data.ja;
        if (Array.isArray(ja)) {
          const defs = [];
          ja.forEach(sec => (sec.definitions || []).forEach(d => {
            const txt = String(d.definition || '').replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim();
            if (txt && defs.length < 2) defs.push(txt);
          }));
          en = defs.join(' / ');
        }
        const c = getOnlineDictCache();
        c[word] = { en: en || '(meaning not found — please ask your teacher)', t: Date.now() };
        try { localStorage.setItem('haku_online_dict_cache', JSON.stringify(c)); } catch (e) {}
      })
      .catch(() => { onlineLookupFailed.add(word); })
      .finally(() => {
        onlineLookupPending.delete(word);
        if (onlineLookupRerenderTimer) clearTimeout(onlineLookupRerenderTimer);
        onlineLookupRerenderTimer = setTimeout(() => {
          try {
            updateMylistBadge();
            const mv = document.getElementById('viewMylist');
            if (mv && !mv.classList.contains('hidden')) renderMylistView();
          } catch (e) {}
        }, 400);
      });
  }

  // 定義が失われた「ダミーカード」（ランダムIDが単語として表示される文字化けの原因）を判定
  function isStubCard(c) {
    if (!c || typeof c !== 'object') return true;
    if (c.isStub) return true;
    const m = c.meaning || {};
    if (m.en === 'Saved Word' && (!c.example || !c.example.ja)) return true;
    if (m.ja && m.ja === c.id && !c.reading) return true;
    return false;
  }

  // Returns all resolved card objects currently in My List (strictly preserving insertion order)
  function getMylistCards() {
    const cards = [];
    const seenWords = new Set();

    mylistSet.forEach(id => {
      const card = getCardById(id);
      if (card && !isStubCard(card) && !isCorruptedCard(card)) {
        const w = (card.word || '').trim();
        if (!seenWords.has(w)) {
          seenWords.add(w);
          cards.push(card);
        }
      }
    });

    return cards;
  }

  // Helper to convert Katakana to Hiragana for uniform Gojuon (Japanese alphabetical) sorting
  function toHiragana(str) {
    return (str || '').replace(/[\u30a1-\u30f6]/g, m => String.fromCharCode(m.charCodeAt(0) - 0x60));
  }

  function getGojuonSortKey(card) {
    if (!card) return '';
    const raw = card.reading || card.word || '';
    // Strip leading punctuation like 〜, ・, -, quotes, brackets, spaces
    const clean = raw.replace(/^[〜\-\s・\(\)（）「」『』\/\\]+/, '');
    return toHiragana(clean);
  }

  // Helper to extract a numerical timestamp for strict chronological sorting of cards
  function getCardSortTimestamp(card, originalIndex) {
    if (!card) return originalIndex != null ? originalIndex : 0;

    // 1. Explicit timestamp fields
    if (typeof card.createdAt === 'number' && card.createdAt > 0) return card.createdAt;
    if (card.createdAt) {
      const t = new Date(card.createdAt).getTime();
      if (!isNaN(t) && t > 0) return t;
    }
    if (typeof card.addedAt === 'number' && card.addedAt > 0) return card.addedAt;
    if (card.addedAt) {
      const t = new Date(card.addedAt).getTime();
      if (!isNaN(t) && t > 0) return t;
    }

    // 2. Embedded 13-digit Unix millisecond timestamp in ID (e.g. card_1792595245476_... or custom_ex_word_1792...)
    if (card.id && typeof card.id === 'string') {
      const m = card.id.match(/(?:card_|custom_|dict_|_|^)(\d{13})(?:_|$)/) || card.id.match(/(\d{13})/);
      if (m) {
        const val = Number(m[1]);
        if (val >= 1500000000000 && val <= 3000000000000) {
          return val;
        }
      }
    }

    // 3. Curriculum / preset seed cards (class_word_*, card_midori_*, card_daniel_*, seed_*)
    // Baseline introduction sequence (older than dynamic custom cards, preserving relative index)
    return 1000000000000 + (originalIndex != null ? originalIndex : 0);
  }

  // Sorts My List cards according to selected sort order
  function sortMylistCards(cards, order) {
    if (!cards || cards.length <= 1) return cards ? cards.slice() : [];
    const list = cards.slice();

    if (order === 'oldest') {
      // Oldest first: lowest timestamp / earliest introduction first
      return list.map((card, idx) => ({ card, idx, ts: getCardSortTimestamp(card, idx) }))
        .sort((a, b) => (a.ts !== b.ts ? a.ts - b.ts : a.idx - b.idx))
        .map(item => item.card);
    }
    if (order === 'newest') {
      // Latest added = first (highest timestamp first; tie-breaker: later insertion index first)
      return list.map((card, idx) => ({ card, idx, ts: getCardSortTimestamp(card, idx) }))
        .sort((a, b) => (b.ts !== a.ts ? b.ts - a.ts : b.idx - a.idx))
        .map(item => item.card);
    }
    if (order === 'gojuon') {
      // Japanese alphabetical (あ〜ん) by reading/word
      return list.sort((a, b) => {
        const ra = getGojuonSortKey(a);
        const rb = getGojuonSortKey(b);
        return ra.localeCompare(rb, 'ja');
      });
    }
    if (order === 'unlearned') {
      // Needs review / Unlearned first, then learned (secondary sort: newest first)
      const sortedNewest = list.map((card, idx) => ({ card, idx, ts: getCardSortTimestamp(card, idx) }))
        .sort((a, b) => (b.ts !== a.ts ? b.ts - a.ts : b.idx - a.idx))
        .map(item => item.card);
      const unlearned = [];
      const learned = [];
      sortedNewest.forEach(c => {
        const isLearned = knownSet.has(c.id) || mylistCardFolderMap[c.id] === 'folder_learned';
        if (isLearned) {
          learned.push(c);
        } else {
          unlearned.push(c);
        }
      });
      return unlearned.concat(learned);
    }
    if (order === 'random') {
      // Fisher-Yates shuffle
      const shuffled = list.slice();
      for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
      }
      return shuffled;
    }
    return list.map((card, idx) => ({ card, idx, ts: getCardSortTimestamp(card, idx) }))
      .sort((a, b) => (b.ts !== a.ts ? b.ts - a.ts : b.idx - a.idx))
      .map(item => item.card);
  }

  // --- Mylist View Rendering with Custom Folders ---
  function renderMylistView() {
    renderMylistFolderTabs();
    renderMylistItems();
  }

  function renderMylistFolderTabs() {
    const tabsContainer = document.getElementById('mylistFolderTabs');
    if (!tabsContainer) return;
    tabsContainer.innerHTML = '';

    const allCards = getMylistCards();

    // 'All' tab
    const allStarredCount = allCards.length;
    const allTab = document.createElement('button');
    const isAllActive = activeMylistFolderId === 'all';
    allTab.className = `px-3 py-1 rounded-full text-xs font-bold transition flex items-center space-x-1 shrink-0 ${
      isAllActive
        ? 'bg-deepNavy text-white shadow-xs'
        : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
    }`;
    allTab.innerHTML = `<span>All</span><span class="text-[10px] opacity-80">(${allStarredCount})</span>`;
    allTab.addEventListener('click', () => {
      activeMylistFolderId = 'all';
      renderMylistView();
    });
    tabsContainer.appendChild(allTab);

    // Custom folders tabs
    mylistFolders.forEach(folder => {
      const folderCardsCount = allCards.filter(c => mylistCardFolderMap[c.id] === folder.id).length;
      const tab = document.createElement('button');
      const isActive = activeMylistFolderId === folder.id;
      tab.className = `px-3 py-1 rounded-full text-xs font-bold transition flex items-center space-x-1 shrink-0 ${
        isActive
          ? 'bg-coralPink text-white shadow-xs'
          : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
      }`;
      tab.innerHTML = `<span>📁 ${folder.name}</span><span class="text-[10px] opacity-80">(${folderCardsCount})</span>`;
      tab.addEventListener('click', () => {
        activeMylistFolderId = folder.id;
        renderMylistView();
      });
      tabsContainer.appendChild(tab);
    });

    // Action bar for current selected folder
    const actionBar = document.getElementById('mylistFolderActionBar');
    const folderNameElem = document.getElementById('currentMylistFolderName');
    if (actionBar && folderNameElem) {
      if (activeMylistFolderId === 'all') {
        actionBar.classList.add('hidden');
      } else {
        const currentFolderObj = mylistFolders.find(f => f.id === activeMylistFolderId);
        if (currentFolderObj) {
          actionBar.classList.remove('hidden');
          folderNameElem.textContent = `📁 Folder: ${currentFolderObj.name}`;
        } else {
          actionBar.classList.add('hidden');
        }
      }
    }
  }

  function renderMylistItems() {
    const container = document.getElementById('mylistItemsContainer');
    if (!container) return;
    container.innerHTML = '';

    let displayedCards = getMylistCards();
    if (activeMylistFolderId !== 'all') {
      displayedCards = displayedCards.filter(c => mylistCardFolderMap[c.id] === activeMylistFolderId);
    }
    displayedCards = sortMylistCards(displayedCards, mylistSortOrder);

    // Update count display
    const wordCountElem = document.getElementById('mylistWordCountText');
    if (wordCountElem) {
      if (currentLang === 'ja') wordCountElem.textContent = `全 ${displayedCards.length} 語`;
      else if (currentLang === 'zh_TW' || currentLang === 'zh_HK') wordCountElem.textContent = `共 ${displayedCards.length} 詞`;
      else if (currentLang === 'zh_CN') wordCountElem.textContent = `共 ${displayedCards.length} 词`;
      else if (currentLang === 'ko') wordCountElem.textContent = `총 ${displayedCards.length}단어`;
      else if (currentLang === 'fr') wordCountElem.textContent = `Total : ${displayedCards.length} mots`;
      else wordCountElem.textContent = `${displayedCards.length} words`;
    }

    // Keep select in sync
    const selectSortElem = document.getElementById('selectMylistSort');
    if (selectSortElem && selectSortElem.value !== mylistSortOrder) {
      selectSortElem.value = mylistSortOrder;
    }

    // 単語名も定義も失われたカード（復元不可）はグレー表示で残す（練習・クイズには入れない）
    const lostIds = [];
    mylistSet.forEach(id => {
      if (activeMylistFolderId !== 'all' && mylistCardFolderMap[id] !== activeMylistFolderId) return;
      const c = getCardById(id);
      if (!c || isStubCard(c)) lostIds.push(id);
    });

    if (displayedCards.length === 0 && lostIds.length === 0) {
      container.innerHTML = `
        <div class="text-center py-12 text-slate-400 text-xs">
          <p>${activeMylistFolderId === 'all' ? 'No words saved to My List yet.' : 'No words in this folder yet.'}</p>
          <p class="mt-1">Tap the "⭐" icon on cards or use the folder dropdown to add words.</p>
        </div>
      `;
      return;
    }

    displayedCards.forEach(card => {
      let displayWord = card.word;
      let displayReading = card.reading || '';
      // Safeguard against inverted cards in list view
      if (!/[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]/.test(displayWord) && card.meaning && typeof card.meaning === 'object') {
        const candidateJp = card.meaning.ja || Object.values(card.meaning).find(v => typeof v === 'string' && /[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]/.test(v));
        if (candidateJp) {
          displayWord = candidateJp;
          if (!displayReading || /[\uAC00-\uD7AFa-zA-Z]/.test(displayReading)) displayReading = '';
        }
      }
      if (displayReading && /[\uAC00-\uD7AF]/.test(displayReading)) {
        displayReading = '';
      }
      const item = document.createElement('div');
      item.className = 'p-3 rounded-2xl border border-slate-200 bg-slate-50 flex items-center justify-between transition hover:shadow-2xs';
      const meaning = getBilingualMeaning(card.meaning, currentLang, displayWord);
      const currentFolderId = mylistCardFolderMap[card.id] || '';
      const isLearned = knownSet.has(card.id) || mylistCardFolderMap[card.id] === 'folder_learned';
      const learnedBadgeHtml = isLearned
        ? `<span class="px-1.5 py-0.5 rounded-full bg-emerald-100 text-emerald-700 text-[10px] font-bold shrink-0">✓ ${currentLang === 'ja' ? '覚えた' : (currentLang === 'zh_TW' || currentLang === 'zh_HK' ? '已掌握' : (currentLang === 'zh_CN' ? '已掌握' : (currentLang === 'ko' ? '암기' : (currentLang === 'fr' ? 'Mémorisé' : 'Learned'))))}</span>`
        : '';

      // Build folder selector options
      let folderOptionsHtml = `<option value="" ${!currentFolderId ? 'selected' : ''}>Unfiled</option>`;
      mylistFolders.forEach(f => {
        folderOptionsHtml += `<option value="${f.id}" ${currentFolderId === f.id ? 'selected' : ''}>📁 ${f.name}</option>`;
      });

      item.innerHTML = `
        <div class="flex-1 pr-2 cursor-pointer btn-open-card-study">
          <div class="flex items-center space-x-1.5 flex-wrap">
            <span class="font-bold text-slate-900 text-sm hover:text-deepNavy transition">${displayWord}</span>
            <span class="card-reading-text text-xs text-slate-400">（${displayReading}）</span>
            ${learnedBadgeHtml}
          </div>
          <p class="text-xs text-rose-600 font-medium mt-0.5">${meaning}</p>
          <div class="mt-1 flex items-center space-x-1" onclick="event.stopPropagation()">
            <label class="text-[10px] text-slate-400 font-medium">Folder:</label>
            <select class="folder-assign-select text-[10px] py-0.5 px-1.5 rounded-lg border border-slate-200 bg-white text-slate-600 focus:outline-none focus:ring-1 focus:ring-deepNavy">
              ${folderOptionsHtml}
            </select>
          </div>
        </div>
        <div class="flex items-center space-x-1 shrink-0">
          <button class="btn-study-single p-2 text-deepNavy hover:text-coralPink transition rounded-full hover:bg-white" title="${currentLang === 'ja' ? '練習カードで学習' : (currentLang === 'zh_TW' || currentLang === 'zh_HK' ? '練習卡片' : (currentLang === 'zh_CN' ? '练习卡片' : (currentLang === 'ko' ? '연습 카드' : (currentLang === 'fr' ? 'Cartes de pratique' : 'Practice Card'))))}">
            <i data-lucide="play" class="w-4 h-4 fill-deepNavy"></i>
          </button>
          <button class="btn-voice p-2 text-slate-500 hover:text-coralPink transition rounded-full hover:bg-white" title="Listen">
            <i data-lucide="volume-2" class="w-4 h-4"></i>
          </button>
          <button class="btn-remove-star p-2 text-amber-500 hover:text-slate-400 transition rounded-full hover:bg-white" title="Remove from My List">
            <i data-lucide="star" class="w-4 h-4 fill-amber-400"></i>
          </button>
        </div>
      `;
      lucide.createIcons({ root: item });

      // Click on word or play button opens in interactive 3D flashcard study mode
      const studySingleHandler = (e) => {
        e.stopPropagation();
        // 現在表示中のマイリスト単語リスト全体をデッキにし、クリックした単語から学習を開始
        activeDeck = displayedCards.slice();
        const clickedIdx = activeDeck.findIndex(c => c.id === card.id);
        currentIndex = clickedIdx >= 0 ? clickedIdx : 0;
        isSearchStudyMode = true;
        isMylistStudyMode = true;
        switchView('flashcards');
        document.getElementById('folderOverviewPanel').classList.add('hidden');
        document.getElementById('unitListPanel').classList.add('hidden');
        document.getElementById('activeStudyHeader').classList.remove('hidden');
        const folderObj = mylistFolders.find(f => f.id === activeMylistFolderId);
        const folderName = folderObj ? folderObj.name : (currentLang === 'ja' ? 'マイリスト全体' : 'My List (All)');
        document.getElementById('activeStudySectionName').textContent = folderName;
        document.getElementById('activeStudyFolderName').textContent = currentLang === 'ja' ? 'マイリスト' : 'My List';
        renderCurrentCard();
      };

      const wordTitle = item.querySelector('.btn-open-card-study');
      if (wordTitle) wordTitle.addEventListener('click', studySingleHandler);
      const btnStudySingle = item.querySelector('.btn-study-single');
      if (btnStudySingle) btnStudySingle.addEventListener('click', studySingleHandler);

      // Voice
      item.querySelector('.btn-voice').addEventListener('click', (e) => {
        e.stopPropagation();
        toggleJapaneseSpeech(card);
      });

      // Remove from star
      item.querySelector('.btn-remove-star').addEventListener('click', () => {
        mylistSet.delete(card.id);
        delete mylistCardFolderMap[card.id];
        saveMylistForCurrentStudent();
        renderMylistView();
        renderCurrentCard();
      });

      // Folder change dropdown
      const selectElem = item.querySelector('.folder-assign-select');
      selectElem.addEventListener('change', (e) => {
        const newFolderId = e.target.value;
        if (newFolderId) {
          mylistCardFolderMap[card.id] = newFolderId;
        } else {
          delete mylistCardFolderMap[card.id];
        }
        saveMylistForCurrentStudent();
        renderMylistView();
        showToast('Moved to folder 📁');
      });

      container.appendChild(item);
    });

    if (lostIds.length > 0) {
      const byDate = {};
      lostIds.forEach(id => {
        const dt = getCardCreatedDate(id);
        const d = dt ? `${dt.getFullYear()}/${String(dt.getMonth() + 1).padStart(2, '0')}/${String(dt.getDate()).padStart(2, '0')}` : '日付不明';
        (byDate[d] = byDate[d] || []).push(id);
      });
      const isJa = currentLang === 'ja';
      const title = isJa
        ? `読み込めなかった単語：${lostIds.length}件（先生に確認してください）`
        : `${lostIds.length} word(s) could not be loaded — please ask your teacher`;
      const rows = Object.keys(byDate).sort().map(d =>
        `<div class="flex items-center justify-between py-1 border-b border-slate-200 last:border-0">
           <span>${d} ${isJa ? '追加' : 'added'}</span><span class="font-bold">${byDate[d].length}${isJa ? '件' : ''}</span>
         </div>`).join('');
      const box = document.createElement('details');
      box.className = 'p-3 rounded-2xl border border-dashed border-slate-300 bg-slate-100 text-slate-500 text-xs';
      box.innerHTML = `<summary class="cursor-pointer font-bold">⚠️ ${title}</summary><div class="mt-2">${rows}</div>`;
      container.appendChild(box);
    }
  }

  // --- Admin Student Management Rendering ---
  function renderAdminStudentList() {
    const container = document.getElementById('adminStudentList');
    const targetSelect = document.getElementById('adminTargetStudent');

    // Populate Target Student dropdown for adding cards
    if (targetSelect) {
      const currentSelected = targetSelect.value || 'all';
      let optionsHtml = `<option value="all">全員共有デッキ (All Students)</option>`;
      students.filter(s => s.id !== 'haku' && s.id !== 'admin').forEach(st => {
        optionsHtml += `<option value="${st.id}">[${st.id}] ${st.name} (${st.lang})</option>`;
      });
      targetSelect.innerHTML = optionsHtml;
      targetSelect.value = currentSelected;
    }

    if (!container) return;
    container.innerHTML = '';

    students.forEach(st => {
      // Don't show admin entries in normal student list or mark specially
      const isTeacher = (st.id === 'haku' || st.id === 'admin');
      const isCurrentLoggedIn = currentStudent && currentStudent.id === st.id;
      const row = document.createElement('div');
      row.className = `flex items-center justify-between p-1.5 sm:p-2 rounded-xl bg-white border transition ${
        isCurrentLoggedIn ? 'border-coralPink bg-rose-50/30 ring-1 ring-coralPink/30' : 'border-slate-200 hover:border-slate-300'
      } shadow-2xs text-xs gap-1`;
      row.innerHTML = `
        <div class="btn-select-student flex-1 min-w-0 flex items-center space-x-1 sm:space-x-1.5 cursor-pointer hover:opacity-80 py-0.5" title="クリックしてこの生徒としてログイン">
          <span class="font-mono text-[9px] font-bold px-1.5 py-0.5 rounded bg-slate-100 text-slate-700 shrink-0">${st.id}</span>
          <span class="font-bold text-slate-800 truncate text-xs sm:text-sm font-jp">${st.name}</span>
          <span class="text-[9px] px-1.5 py-0.2 rounded font-semibold bg-lightBlueBg text-deepNavy shrink-0">${st.lang}</span>
          ${isCurrentLoggedIn ? '<span class="text-[9px] px-1.5 py-0.2 rounded font-bold bg-coralPink text-white shrink-0">利用中</span>' : ''}
        </div>
        <div class="flex items-center space-x-0.5 shrink-0">
          <span class="font-mono text-[10px] text-rose-600 font-bold bg-rose-50 px-1.5 py-0.5 rounded-md border border-rose-100 whitespace-nowrap" title="パスコード">
            PIN: ${st.passcode}
          </span>
          ${!isTeacher ? `
            <button class="btn-login-as-student p-1 sm:p-1.5 rounded-lg ${isCurrentLoggedIn ? 'bg-coralPink text-white shadow-2xs' : 'bg-slate-100 hover:bg-deepNavy hover:text-white text-slate-700'} transition flex items-center justify-center active:scale-95" title="${st.name}としてログイン">
              <i data-lucide="log-in" class="w-3.5 h-3.5"></i>
            </button>
            <button class="btn-edit-student p-1 sm:p-1.5 rounded-lg text-slate-400 hover:text-sky-600 hover:bg-sky-50 transition active:scale-95" title="生徒情報を編集">
              <i data-lucide="edit-3" class="w-3.5 h-3.5"></i>
            </button>
            <button class="btn-delete-student p-1 sm:p-1.5 rounded-lg text-slate-300 hover:text-rose-500 hover:bg-rose-50 transition active:scale-95" title="生徒を削除">
              <i data-lucide="trash-2" class="w-3.5 h-3.5"></i>
            </button>
          ` : '<span class="text-[10px] text-slate-400 font-bold px-1">先生</span>'}
        </div>
      `;
      lucide.createIcons({ root: row });

      if (!isTeacher) {
        const handleLoginAs = async () => {
          showToast(`生徒「${st.name}」のデータを同期中...`);
          await setStudent(st);
          renderAdminStudentList();
          switchView('mylist');
          showToast(`生徒「${st.name}」としてログインしました！🎓`);
        };

        const selectStudentBtn = row.querySelector('.btn-select-student');
        if (selectStudentBtn) {
          selectStudentBtn.addEventListener('click', handleLoginAs);
        }

        const loginBtn = row.querySelector('.btn-login-as-student');
        if (loginBtn) {
          loginBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            handleLoginAs();
          });
        }

        const editBtn = row.querySelector('.btn-edit-student');
        if (editBtn) {
          editBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            openEditStudentModal(st);
          });
        }

        const delBtn = row.querySelector('.btn-delete-student');
        if (delBtn) {
          delBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            if (!confirm(`生徒「${st.name}」（ID: ${st.id}）を削除しますか？`)) return;
            students = students.filter(s => s.id !== st.id);
            localStorage.setItem('haku_students', JSON.stringify(students));
            renderAdminStudentList();
            showToast(`生徒「${st.name}」を削除しました`);
          });
        }
      }

      container.appendChild(row);
    });
  }

  // --- Batch Import Logic for Haku-sensei ---
  function showImportBanner(isSuccess, title, message, wordsList = [], studentObj = null) {
    const banner = document.getElementById('adminImportResultBanner');
    const icon = document.getElementById('adminImportResultIcon');
    const titleEl = document.getElementById('adminImportResultTitle');
    const textEl = document.getElementById('adminImportResultText');
    const chipsEl = document.getElementById('adminImportWordChips');
    const btn = document.getElementById('btnAdminViewStudentMylist');
    if (!banner) return;

    banner.classList.remove('hidden', 'bg-emerald-50', 'border-emerald-300', 'text-emerald-900', 'bg-rose-50', 'border-rose-300', 'text-rose-900');
    if (isSuccess) {
      banner.classList.add('bg-emerald-50', 'border-emerald-300', 'text-emerald-900');
      if (icon) {
        icon.className = 'w-5 h-5 text-emerald-600 shrink-0 mt-0.5';
        icon.setAttribute('data-lucide', 'check-circle');
      }
      if (titleEl) {
        titleEl.textContent = title || '✅ 追加できました！';
        titleEl.className = 'font-extrabold text-sm mb-1 leading-snug text-emerald-900';
      }
      if (textEl) {
        textEl.textContent = message;
        textEl.className = 'text-xs text-emerald-800 leading-relaxed';
      }
      if (chipsEl) {
        if (wordsList && wordsList.length > 0) {
          chipsEl.innerHTML = wordsList.map(w => `<span class="px-2 py-0.5 bg-emerald-100 border border-emerald-300 text-emerald-900 rounded-lg text-[11px] font-bold shadow-2xs">${escapeHtml(w)}</span>`).join('');
          chipsEl.classList.remove('hidden');
        } else {
          chipsEl.classList.add('hidden');
        }
      }
      if (btn) {
        if (studentObj && studentObj.id !== 'all') {
          btn.textContent = `生徒「${studentObj.name}」の画面で確認 ↗`;
          btn.onclick = async () => {
            btn.disabled = true;
            btn.textContent = '読込中...';
            try {
              await setStudent(studentObj);
              switchView('mylist');
            } finally {
              btn.disabled = false;
              btn.textContent = `生徒「${studentObj.name}」の画面で確認 ↗`;
            }
          };
          btn.classList.remove('hidden');
        } else {
          btn.textContent = 'マイリストを確認 ↗';
          btn.onclick = () => {
            switchView('mylist');
          };
          btn.classList.remove('hidden');
        }
      }
    } else {
      banner.classList.add('bg-rose-50', 'border-rose-300', 'text-rose-900');
      if (icon) {
        icon.className = 'w-5 h-5 text-rose-600 shrink-0 mt-0.5';
        icon.setAttribute('data-lucide', 'alert-circle');
      }
      if (titleEl) {
        titleEl.textContent = title || '❌ エラー：追加できませんでした';
        titleEl.className = 'font-extrabold text-sm mb-1 leading-snug text-rose-900';
      }
      if (textEl) {
        textEl.textContent = message;
        textEl.className = 'text-xs text-rose-800 leading-relaxed';
      }
      if (chipsEl) chipsEl.classList.add('hidden');
      if (btn) btn.classList.add('hidden');
    }
    if (window.lucide) lucide.createIcons();
  }

  // --- Batch Import Logic for Haku-sensei ---
  let isImporting = false;
  async function executeImport() {
    if (isImporting) return;
    const btnExecute = document.getElementById('btnExecuteImport');
    const originalBtnHtml = btnExecute ? btnExecute.innerHTML : '';

    const rawText = document.getElementById('adminImportText').value.trim();
    const target = document.getElementById('adminTargetStudent').value;
    const targetFolderSelect = document.getElementById('adminImportFolderSelect')?.value || 'folder_class_words';
    if (!rawText) {
      showImportBanner(false, '❌ エラー：テキストが入力されていません', '貼り付けエリアに単語テキストを入力してから「デッキに一括追加する」を押してください。');
      showToast('インポートするテキストを入力してください');
      return;
    }

    isImporting = true;
    if (btnExecute) {
      btnExecute.disabled = true;
      btnExecute.innerHTML = '<span class="inline-block animate-spin mr-2">⏳</span>クラウドへ保存中...';
    }

    try {
      // Smart splitting: support newline-separated, single-line comma/space-separated, and markdown tables
      let rawItems = [];
      if (rawText.includes('\n')) {
        rawItems = rawText.split('\n');
      } else {
        // Single continuous line like: 観光地（かんこうち）,tourist destination 飲食店（いんしょくてん）,restaurant
        const regexPattern = /([^\s,，\t]+(?:（[^）]+）|\([^)]+\))?)\s*[,，\t]\s*([^,，\t\n]+?)(?=(?:\s+[^\s,，\t]+(?:（[^）]+）|\([^)]+\))?\s*[,，\t])|$)/g;
        let match;
        while ((match = regexPattern.exec(rawText)) !== null) {
          if (match[1] && match[2]) {
            rawItems.push(`${match[1].trim()}\t${match[2].trim()}`);
          }
        }
        if (rawItems.length === 0) {
          rawItems = [rawText];
        }
      }

      let addedCount = 0;
      const addedCardIds = [];
      const addedWords = [];

      const importLangOption = document.getElementById('adminImportLangSelect')?.value || 'auto';
      const targetStudentObj = students.find(s => s.id === target);
      const targetStudentLang = targetStudentObj ? targetStudentObj.lang : 'en';

      // Helper: Dictionary lookup across DICT_DATA, CLASS_VOCAB_DATA, INITIAL_VOCAB_DATA, JLPT_VOCAB
      const lookupDictionary = (w) => {
        if (!w) return null;
        if (window.DICT_DATA && Array.isArray(window.DICT_DATA)) {
          const entry = window.DICT_DATA.find(d => d.w === w);
          if (entry) {
            return {
              reading: entry.r || entry.w,
              en: (entry.m && entry.m.join(', ')) || '',
              zh: (entry.zh && entry.zh.join(', ')) || '',
              fr: (entry.fr && entry.fr.join(', ')) || ''
            };
          }
        }
        if (window.CLASS_VOCAB_DATA && Array.isArray(window.CLASS_VOCAB_DATA)) {
          const c = window.CLASS_VOCAB_DATA.find(x => x.word === w);
          if (c) {
            return {
              reading: c.reading || c.word,
              en: (c.meaning && c.meaning.en) || '',
              zh: (c.meaning && (c.meaning.zh_TW || c.meaning.zh_CN || c.meaning.zh_HK)) || '',
              ko: (c.meaning && c.meaning.ko) || '',
              fr: (c.meaning && c.meaning.fr) || ''
            };
          }
        }
        if (window.INITIAL_VOCAB_DATA && Array.isArray(window.INITIAL_VOCAB_DATA)) {
          const c = window.INITIAL_VOCAB_DATA.find(x => x.word === w);
          if (c) {
            return {
              reading: c.reading || c.word,
              en: (c.meaning && c.meaning.en) || '',
              zh: (c.meaning && (c.meaning.zh_TW || c.meaning.zh_CN || c.meaning.zh_HK)) || '',
              ko: (c.meaning && c.meaning.ko) || '',
              fr: (c.meaning && c.meaning.fr) || ''
            };
          }
        }
        if (window.JLPT_VOCAB) {
          for (const lvl of ['N5', 'N4', 'N3', 'N2', 'N1']) {
            const list = window.JLPT_VOCAB[lvl] || [];
            const entry = list.find(x => x.word === w);
            if (entry) {
              return {
                reading: entry.reading || entry.k || entry.word,
                en: (entry.meanings && entry.meanings.join(', ')) || ''
              };
            }
          }
        }
        return null;
      };

      let allCustomCards = [];
      try {
        allCustomCards = JSON.parse(localStorage.getItem('haku_all_custom_cards') || '[]');
      } catch (e) { allCustomCards = []; }

      rawItems.forEach(line => {
        line = line.trim();
        if (!line || line.startsWith('#')) return;
        // Skip table header divider e.g. |---|---|
        if (/^\|?\s*[-:\s|]+\s*\|?$/.test(line)) return;
        // Skip header lines or metadata labels
        if (/^(フラッシュカード|単語一覧|今日の単語|インポート用|コピー用|リスト用|【|#|No\.|番号)/i.test(line) || 
            line.endsWith('インポート用:') || line.endsWith('インポート用：') || 
            line.endsWith('一覧:') || line.endsWith('一覧：')) return;
        if (/^\|?\s*(単語|言葉|語彙|Word|Japanese|No)\s*\|/i.test(line)) return;

        // Strip leading numbers (1. / ① / (1)) and bullet points (・ / ◆ / ■ / ● / ★ / ☆ / - / *)
        line = line.replace(/^[\(\（]?[①-⑳\d]+[\)\）\.\:\s、\-]+/, '').trim();
        line = line.replace(/^[・◆■●★☆\-*]\s*/, '').trim();
        if (!line) return;

        // Universal column parsing
        let parts = [];
        if (line.includes('|')) {
          parts = line.split('|').map(s => s.trim()).filter((s, idx, arr) => {
            if ((idx === 0 || idx === arr.length - 1) && s === '') return false;
            return true;
          });
        } else if (line.includes('\t')) {
          parts = line.split('\t').map(s => s.trim()).filter(s => s !== '');
        } else if (line.includes('  ') || line.includes('\u3000')) {
          parts = line.split(/[\t\u3000]|\s{2,}/).map(s => s.trim()).filter(s => s !== '');
        } else if (/^[^:：\s]+(?:（[^）]+）|\([^)]+\))?\s*[:：]\s*.+$/.test(line)) {
          const colonIdx = line.search(/[:：]/);
          parts = [line.slice(0, colonIdx).trim(), line.slice(colonIdx + 1).trim()];
        } else if (/^[^-\s]+(?:（[^）]+）|\([^)]+\))?\s+[-–—]\s+.+$/.test(line)) {
          const dashMatch = line.match(/^(.*?)\s+[-–—]\s+(.*)$/);
          if (dashMatch) {
            parts = [dashMatch[1].trim(), dashMatch[2].trim()];
          } else {
            parts = [line.trim()];
          }
        } else if (line.includes(',') || line.includes('，')) {
          parts = line.split(/[,，]/).map(s => s.trim()).filter(s => s !== '');
        } else {
          parts = [line.trim()];
        }

        if (parts.length >= 1) {
          const rawWord = parts[0].trim();
          if (!rawWord) return;

          // 1. Extract word and reading
          let word = rawWord;
          let reading = '';
          let cols = parts.slice(1);

          // Safeguard 1: Reverse order detection!
          // If word has NO Japanese kana or kanji, and any col has Japanese, automatically swap them!
          const hasKanaOrKanji = (s) => /[\u3040-\u309f\u30a0-\u30ff\u4e00-\u9faf]/.test(s);
          const hasRomanOrForeign = (s) => /[a-zA-Z\uac00-\ud7a3āēīōūáéíóúàèìòùâêîôûǎěǐǒǔ]/.test(s);
          if (cols.length >= 1 && !hasKanaOrKanji(word)) {
            const jpColIdx = cols.findIndex(c => hasKanaOrKanji(c));
            if (jpColIdx >= 0) {
              const temp = cols[jpColIdx];
              cols[jpColIdx] = word;
              word = temp;
            }
          }

          const match = word.match(/^(.*?)[（\(](.*?)[）\)]/);
          if (match) {
            word = match[1].trim();
            reading = match[2].trim();
          } else if (cols.length >= 2 && /^[ぁ-んァ-ヶー〜・\s]+$/.test(cols[0])) {
            // Format where col 0 is Word and col 1 is Reading: e.g. 食べる \t たべる \t 吃 \t to eat
            reading = cols[0].trim();
            cols = cols.slice(1);
          }

          // Safeguard 2: Ensure reading is strictly Japanese kana
          if (reading && hasRomanOrForeign(reading)) {
            reading = '';
          }

          // Dictionary lookup for missing reading or missing meanings
          const dictInfo = lookupDictionary(word);
          if (!reading && dictInfo && dictInfo.reading) {
            reading = dictInfo.reading;
          }

          let parsedNative = '';
          let parsedEn = '';
          let exJa = '';
          let exTrans = '';
          let related = '';

          // Helper detection functions
          const isEnglish = (s) => /^[a-zA-Z0-9\s,.'"\(\)\/\-]+$/.test(s.trim()) && /[a-zA-Z]{2,}/.test(s);
          const isJapaneseSentence = (s) => /[\u3040-\u309f]/.test(s) && (/[。、！？]/.test(s) || s.includes('A:') || s.includes('A：') || s.length > 10);

          // Distribute columns intelligently
          if (cols.length === 3 && isJapaneseSentence(cols[1])) {
            if (isEnglish(cols[0])) {
              parsedEn = cols[0];
            } else {
              parsedNative = cols[0];
            }
            exJa = cols[1];
            exTrans = cols[2];
          } else if (cols.length === 2 && isJapaneseSentence(cols[1])) {
            if (isEnglish(cols[0])) {
              parsedEn = cols[0];
            } else {
              parsedNative = cols[0];
            }
            exJa = cols[1];
          } else {
            for (const col of cols) {
              const c = col.trim();
              if (!c) continue;
              if (isJapaneseSentence(c) && !exJa) {
                exJa = c;
              } else if (exJa && !exTrans) {
                exTrans = c;
              } else if (isEnglish(c) && !parsedEn) {
                parsedEn = c;
              } else if (!parsedNative) {
                parsedNative = c;
              } else if (!parsedEn) {
                parsedEn = c;
              } else if (!exJa) {
                exJa = c;
              } else if (!exTrans) {
                exTrans = c;
              } else if (!related) {
                related = c;
              }
            }
          }

          // Smart parser for packed bilingual meaning (e.g. "吃 (to eat)" or "去 / to go")
          if (parsedNative && !parsedEn) {
            const parenMatch = parsedNative.match(/^(.*?)[（\(\[](.*?)[）\)\]]$/);
            if (parenMatch) {
              const p1 = parenMatch[1].trim();
              const p2 = parenMatch[2].trim();
              if (isEnglish(p2)) {
                parsedNative = p1 || p2;
                parsedEn = p2;
              } else if (isEnglish(p1)) {
                parsedNative = p2;
                parsedEn = p1;
              }
            } else if (parsedNative.includes('/')) {
              const slashParts = parsedNative.split('/').map(s => s.trim());
              const enPart = slashParts.find(s => isEnglish(s));
              const nativePart = slashParts.find(s => !isEnglish(s));
              if (enPart && nativePart) {
                parsedEn = enPart;
                parsedNative = nativePart;
              }
            }
          }

          // Automatic fallback lookup if either or both are missing
          if (!parsedEn && !parsedNative && dictInfo) {
            if (dictInfo.en) parsedEn = dictInfo.en;
            if (dictInfo.zh) parsedNative = dictInfo.zh;
            if (dictInfo.ko && targetStudentLang === 'ko') parsedNative = dictInfo.ko;
            if (dictInfo.fr && targetStudentLang === 'fr') parsedNative = dictInfo.fr;
          }
          if (!parsedNative && parsedEn) {
            const fb = getFallbackMeaningForWord(word, targetStudentLang);
            if (fb) parsedNative = fb;
          }
          if (!parsedEn && parsedNative) {
            if (dictInfo && dictInfo.en) {
              parsedEn = dictInfo.en;
            }
          }

          if (!parsedEn && !parsedNative) {
            parsedEn = word;
            parsedNative = word;
          }

          // Determine specific language to assign
          const activeLangKey = (importLangOption !== 'auto') ? importLangOption : (targetStudentLang !== 'en' ? targetStudentLang : 'zh_TW');

          const meaningObj = {
            en: parsedEn || parsedNative || 'Meaning',
            ja: parsedNative || parsedEn || word,
            zh_TW: parsedNative || parsedEn || '意思',
            zh_CN: parsedNative || parsedEn || '意思',
            ko: parsedNative || parsedEn || '뜻',
            zh_HK: parsedNative || parsedEn || '意思',
            fr: parsedEn || parsedNative || 'Sens'
          };

          if (activeLangKey && activeLangKey !== 'en') {
            meaningObj[activeLangKey] = parsedNative || parsedEn;
          }
          if (parsedEn) {
            meaningObj.en = parsedEn;
          }
          if (parsedNative) {
            if (!meaningObj.zh_TW || meaningObj.zh_TW === '意思') meaningObj.zh_TW = parsedNative;
            if (!meaningObj.zh_CN || meaningObj.zh_CN === '意思') meaningObj.zh_CN = parsedNative;
            if (!meaningObj.zh_HK || meaningObj.zh_HK === '意思') meaningObj.zh_HK = parsedNative;
          }

          // Find dictionary example if exJa is not explicitly provided
          let resolvedJa = '';
          let resolvedEn = '';
          let resolvedZhTW = '';
          let resolvedZhCN = '';
          let resolvedKo = '';
          let resolvedZhHK = '';
          let resolvedFr = '';

          if (exJa) {
            let cleanExJa = exJa.trim();
            let extractedExTrans = '';

            const matchExWithTrans = cleanExJa.match(/^([\s\S]*?[。！？](?:\s*[（\(][\u3040-\u309F\u30A0-\u30FF・ー\s、。]+[）\)])?)\s*([^（\(]+.*)$/);
            if (matchExWithTrans) {
              cleanExJa = matchExWithTrans[1].trim();
              extractedExTrans = matchExWithTrans[2].trim();
            } else if (exTrans) {
              extractedExTrans = exTrans.trim();
            }

            cleanExJa = cleanExJa.replace(/\s*[（\(][\u3040-\u309F\u30A0-\u30FF・ー\s、。]+[）\)]\s*$/, '').trim();
            cleanExJa = cleanExJa.replace(/([\u4e00-\u9faf\u3400-\u4dbf]+)[（\(]([\u3040-\u309f]+)[）\)]/g, '<ruby>$1<rt>$2</rt></ruby>');

            resolvedJa = cleanExJa;
            if (extractedExTrans) {
              resolvedZhTW = extractedExTrans;
              resolvedZhCN = extractedExTrans;
              resolvedZhHK = extractedExTrans;
              resolvedEn = isEnglish(extractedExTrans) ? extractedExTrans : resolvedJa;
              resolvedKo = extractedExTrans;
              resolvedFr = extractedExTrans;
            } else {
              resolvedEn = resolvedJa;
              resolvedZhTW = resolvedJa;
              resolvedZhCN = resolvedJa;
              resolvedKo = resolvedJa;
              resolvedZhHK = resolvedJa;
              resolvedFr = resolvedJa;
            }
          }

          if (!resolvedJa) {
            const dictMap = window.DICT_EXAMPLES_MAP || {};
            const matchedEx = dictMap[word] || (reading ? dictMap[reading] : null);
            if (matchedEx && matchedEx.ja) {
              resolvedJa = matchedEx.ja;
              resolvedEn = matchedEx.en || matchedEx.ja;
              resolvedZhTW = matchedEx.zh_TW || matchedEx.en || matchedEx.ja;
              resolvedZhCN = matchedEx.zh_CN || matchedEx.en || matchedEx.ja;
              resolvedKo = matchedEx.ko || matchedEx.en || matchedEx.ja;
              resolvedZhHK = matchedEx.zh_HK || matchedEx.en || matchedEx.ja;
              resolvedFr = matchedEx.fr || matchedEx.en || matchedEx.ja;
            } else {
              const fallbackDlg = getNaturalDefaultDialogue(word, reading);
              resolvedJa = fallbackDlg.ja;
              resolvedEn = fallbackDlg.en;
              resolvedZhTW = fallbackDlg.zh_TW;
              resolvedZhCN = fallbackDlg.zh_CN;
              resolvedKo = fallbackDlg.ko;
              resolvedZhHK = fallbackDlg.zh_HK;
              resolvedFr = fallbackDlg.fr;
            }
          }

          // Card ID & deduplication
          let cardId;
          const existingCustom = (Array.isArray(allCustomCards) ? allCustomCards : []).find(c => c && c.word === word && !isStubCard(c) && !isCorruptedCard(c));
          if (existingCustom && existingCustom.id) {
            cardId = existingCustom.id;
          } else {
            cardId = `card_${Date.now()}_${Math.random().toString(36).substr(2, 6)}__${String(word).replace(/[\/\s]/g, '')}`;
          }

          const newCard = {
            id: cardId,
            word: word,
            reading: reading || word,
            category: '授業で習った言葉',
            studentId: target === 'all' ? null : target,
            meaning: meaningObj,
            example: {
              ja: resolvedJa,
              en: resolvedEn || resolvedJa,
              zh_TW: resolvedZhTW || resolvedJa,
              zh_CN: resolvedZhCN || resolvedJa,
              ko: resolvedKo || resolvedJa,
              zh_HK: resolvedZhHK || resolvedJa,
              fr: resolvedFr || resolvedJa
            },
            related: related || (reading ? `${reading}` : '重要表現'),
            createdAt: Date.now()
          };

          try {
            const stored = JSON.parse(localStorage.getItem('haku_all_custom_cards') || '[]');
            const exIdx = stored.findIndex(c => c.id === newCard.id);
            if (exIdx >= 0) stored[exIdx] = newCard;
            else stored.push(newCard);
            localStorage.setItem('haku_all_custom_cards', JSON.stringify(stored));
          } catch (e) {}

          const vIdx = vocabList.findIndex(c => c.id === newCard.id);
          if (vIdx >= 0) vocabList[vIdx] = newCard;
          else vocabList.push(newCard);

          recordWordNames([newCard]);
          addedCardIds.push(cardId);
          addedWords.push(word);
          addedCount++;
        }
      });

      if (addedCount === 0) {
        showImportBanner(false, '❌ エラー：単語を検出できませんでした', '貼り付けられた内容から単語を認識できませんでした。形式をご確認の上、再度お試しください。');
        showToast('単語が検出されませんでした。形式をご確認ください');
        return;
      }

      // どの生徒向けにインポートした場合でも、常にアプリのカスタム辞書マスターに登録
      localStorage.setItem('haku_vocab_data', JSON.stringify(vocabList));

      const syncErrors = [];

      // Auto-add to My List and assign to requested folder!
      if (targetFolderSelect !== 'none') {
        const destFolderId = (targetFolderSelect === 'folder_class_words') ? 'folder_class_words' : '';
        const destFolderName = '授業で習った言葉';

        // Targets: if 'all', all students + guest; else the specific student
        const recipientStudentIds = (target === 'all') 
          ? [...students.map(s => s.id), 'guest'] 
          : [target];

        for (const stId of recipientStudentIds) {
          const key = `haku_mylist_${stId}`;
          const foldersKey = `haku_mylist_folders_${stId}`;
          const mapKey = `haku_mylist_card_map_${stId}`;

          // Folders
          let stFolders = [];
          try { stFolders = JSON.parse(localStorage.getItem(foldersKey) || '[]'); } catch (e) { stFolders = []; }
          if (destFolderId === 'folder_class_words') {
            if (!stFolders.find(f => f.id === 'folder_class_words')) {
              stFolders.unshift({ id: 'folder_class_words', name: destFolderName });
              localStorage.setItem(foldersKey, JSON.stringify(stFolders));
            }
          }

          // Card folder map
          let stMap = {};
          try { stMap = JSON.parse(localStorage.getItem(mapKey) || '{}'); } catch (e) { stMap = {}; }
          if (destFolderId) {
            addedCardIds.forEach(id => { stMap[id] = destFolderId; });
            localStorage.setItem(mapKey, JSON.stringify(stMap));
          }

          // Mylist items
          let stSet = [];
          try { stSet = JSON.parse(localStorage.getItem(key) || '[]'); } catch (e) { stSet = []; }
          const setObj = new Set([...stSet, ...addedCardIds]);
          localStorage.setItem(key, JSON.stringify(Array.from(setObj)));

          // Synchronize to Cloud for this student safely through mutex with await
          if (isFirebaseReady && fbDb && stId !== 'guest') {
            const mylistCardIds = new Set(setObj);
            let studentCustomCards = [];
            try {
              const storedCustom = JSON.parse(localStorage.getItem('haku_all_custom_cards') || '[]');
              studentCustomCards = [...vocabList, ...storedCustom].filter(c => mylistCardIds.has(c.id) && isCustomCardId(c.id) && c.section_num === undefined && !isStubCard(c) && !c.isRebuilt);
            } catch (e) {
              studentCustomCards = vocabList.filter(c => mylistCardIds.has(c.id) && isCustomCardId(c.id) && c.section_num === undefined && !isStubCard(c) && !c.isRebuilt);
            }
            try {
              const ok = await syncStudentToCloudDirect(stId, {
                mylist: Array.from(setObj),
                folders: stFolders,
                cardFolderMap: stMap,
                customCards: studentCustomCards,
                wordNames: buildWordNamesFor(Array.from(setObj)),
                updatedAt: firebase.firestore.FieldValue.serverTimestamp()
              });
              if (!ok) syncErrors.push(stId);
            } catch (syncErr) {
              console.warn('Sync student error during import:', syncErr);
              syncErrors.push(stId);
            }
          }
        }

        // If the current logged in student is one of the recipients, reload their mylist state immediately
        const currentId = currentStudent ? currentStudent.id : 'guest';
        if (recipientStudentIds.includes(currentId)) {
          loadMylistForCurrentStudent();
        }
      }

      document.getElementById('adminImportText').value = '';
      updateActiveDeck();

      const targetName = (target && target !== 'all' && targetStudentObj) ? targetStudentObj.name : '全員共有デッキ';
      if (syncErrors.length > 0) {
        const warnTitle = `⚠️ 追加完了（一部クラウド同期エラー: ${syncErrors.join(', ')}）`;
        const warnMsg = `生徒「${targetName}」の端末保存は完了しましたが、Firebaseクラウド同期で一部通信エラーが発生しました。通信環境をご確認ください。`;
        showImportBanner(false, warnTitle, warnMsg, addedWords, targetStudentObj);
        showToast(warnTitle);
      } else {
        const successTitle = `✅ 追加できました！（全${addedCount}件）`;
        const successMsg = `追加先：生徒「${targetName}」のマイリスト（フォルダ：授業で習った言葉）に正常に反映されました！クラウド同期も完了しました☁️🌸`;
        showImportBanner(true, successTitle, successMsg, addedWords, targetStudentObj);
        showToast(successTitle);
      }

      if (typeof renderAdminStudentList === 'function') {
        renderAdminStudentList();
      }
    } catch (err) {
      console.error('Fatal import error:', err);
      showImportBanner(false, '❌ エラーが発生しました', err.message || 'インポート中にエラーが発生しました');
      showToast('❌ エラーが発生しました');
    } finally {
      isImporting = false;
      if (btnExecute) {
        btnExecute.disabled = false;
        btnExecute.innerHTML = originalBtnHtml;
      }
    }
  }

  // --- View Switching Navigation ---
  function switchView(viewName) {
    document.getElementById('viewFlashcards').classList.add('hidden');
    document.getElementById('viewQuiz').classList.add('hidden');
    document.getElementById('viewMylist').classList.add('hidden');
    const viewJlptEl = document.getElementById('viewJlpt');
    if (viewJlptEl) viewJlptEl.classList.add('hidden');
    document.getElementById('viewAdmin').classList.add('hidden');

    const navStudy = document.getElementById('navStudy');
    const navQuiz = document.getElementById('navQuiz');
    const navMylist = document.getElementById('navMylist');
    const navJlpt = document.getElementById('navJlpt');

    const inactiveClass = 'flex-1 max-w-[150px] py-1.5 px-2.5 rounded-full border border-softBorder hover:border-deepNavy bg-white text-slate-700 flex items-center justify-center space-x-1.5 transition shrink-0';
    const activeClass = 'flex-1 max-w-[150px] py-1.5 px-2.5 rounded-full text-white bg-deepNavy flex items-center justify-center space-x-1.5 transition shadow-xs shrink-0';

    if (navStudy) navStudy.className = (viewName === 'flashcards') ? activeClass : inactiveClass;
    if (navQuiz) navQuiz.className = (viewName === 'quiz' || viewName === 'test') ? activeClass : inactiveClass;
    if (navMylist) navMylist.className = (viewName === 'mylist') ? activeClass : inactiveClass;
    if (navJlpt) navJlpt.className = (viewName === 'jlpt') ? activeClass : inactiveClass;

    if (viewName === 'flashcards') {
      document.getElementById('viewFlashcards').classList.remove('hidden');
      checkAndShowSwipeGuide();
    } else if (viewName === 'quiz') {
      setQuizMode('quiz');
      document.getElementById('viewQuiz').classList.remove('hidden');
      startQuiz();
    } else if (viewName === 'test') {
      setQuizMode('test');
      document.getElementById('viewQuiz').classList.remove('hidden');
      startQuiz();
    } else if (viewName === 'mylist') {
      document.getElementById('viewMylist').classList.remove('hidden');
      renderMylistView();
      // Instantly pull any new data from cloud when opening My List
      if (currentStudent && currentStudent.id !== 'guest') {
        syncStudentFromCloud(currentStudent.id).then(changed => {
          if (changed) {
            renderMylistView();
          }
        });
      }
    } else if (viewName === 'jlpt') {
      if (viewJlptEl) {
        viewJlptEl.classList.remove('hidden');
        initJlptView();
      }
    } else if (viewName === 'admin') {
      const viewAdmin = document.getElementById('viewAdmin');
      if (viewAdmin) viewAdmin.classList.remove('hidden');
      if (typeof renderAdminStudentList === 'function') {
        renderAdminStudentList();
      }
      try { renderLostCardsReport(); } catch (e) {}
    }
  }

  // --- Setup Event Listeners ---
  function setupListeners() {
    let hasMovedBeyondTapThreshold = false;

    // Navigation tabs
    document.getElementById('navStudy').addEventListener('click', () => {
      // Clear search query and close dropdown
      const topSearch = document.getElementById('globalTopSearchInput');
      const clearTopBtn = document.getElementById('btnClearTopSearch');
      const dropdown = document.getElementById('searchDropdownContainer');
      if (topSearch) topSearch.value = '';
      if (clearTopBtn) clearTopBtn.classList.add('hidden');
      if (dropdown) dropdown.classList.add('hidden');
      sidebarSearchQuery = '';

      // Return to folder overview
      backToFolderOverview();
      switchView('flashcards');
    });
    document.getElementById('navQuiz').addEventListener('click', () => switchView('quiz'));
    document.getElementById('navMylist').addEventListener('click', () => switchView('mylist'));
    const navJlptEl = document.getElementById('navJlpt');
    if (navJlptEl) {
      navJlptEl.addEventListener('click', () => switchView('jlpt'));
    }
    // Discreet Teacher Admin Drawer Trigger (先生でログイン中のみドロワー内に表示)
    const drawerBtnOpenAdmin = document.getElementById('drawerBtnOpenAdmin');
    if (drawerBtnOpenAdmin) {
      drawerBtnOpenAdmin.addEventListener('click', () => {
        if (typeof closeMenuDrawer === 'function') closeMenuDrawer();
        switchView('admin');
        showToast('ハク先生専用・管理画面を開きました ✨');
      });
    }

    const btnAdminBackToCards = document.getElementById('btnAdminBackToCards');
    if (btnAdminBackToCards) {
      btnAdminBackToCards.addEventListener('click', () => {
        switchView('flashcards');
      });
    }

    // --- Furigana & Auto Audio Toggle Controls (Top Header) ---
    function updateFuriganaUi() {
      const btn = document.getElementById('btnToggleFurigana');
      if (document.body) {
        document.body.classList.toggle('furigana-off', !isFuriganaEnabled);
      }
      if (btn) {
        btn.setAttribute('aria-checked', isFuriganaEnabled ? 'true' : 'false');
        if (isFuriganaEnabled) {
          btn.classList.add('is-on');
          btn.classList.remove('is-off');
        } else {
          btn.classList.remove('is-on');
          btn.classList.add('is-off');
        }
      }

      // スマホ版「あ」ボタンのUI更新（人型アイコンと同じ半透明ホワイト系デザイン）
      const btnMobile = document.getElementById('btnToggleFuriganaMobile');
      const labelMobile = document.getElementById('labelToggleFuriganaMobile');
      if (btnMobile && labelMobile) {
        if (isFuriganaEnabled) {
          btnMobile.className = 'md:hidden w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-white/25 hover:bg-white/35 text-white ring-1 ring-white/30 flex items-center justify-center transition active:scale-95';
          labelMobile.className = 'text-xs sm:text-sm font-black leading-none font-jp text-white';
        } else {
          btnMobile.className = 'md:hidden w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-white/10 hover:bg-white/20 text-white/40 flex items-center justify-center transition active:scale-95';
          labelMobile.className = 'text-xs sm:text-sm font-bold leading-none font-jp text-white/40 line-through';
        }
      }
    }

    function updateAutoAudioUi() {
      const btn = document.getElementById('btnToggleAutoAudio');
      if (btn) {
        btn.setAttribute('aria-checked', isAutoAudioEnabled ? 'true' : 'false');
        if (isAutoAudioEnabled) {
          btn.classList.add('is-on');
          btn.classList.remove('is-off');
        } else {
          btn.classList.remove('is-on');
          btn.classList.add('is-off');
        }
      }

      // スマホ版「音のマーク」ボタンのUI更新（人型アイコンと同じ半透明ホワイト系デザイン）
      const btnMobile = document.getElementById('btnToggleAutoAudioMobile');
      if (btnMobile) {
        if (isAutoAudioEnabled) {
          btnMobile.className = 'md:hidden w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-white/25 hover:bg-white/35 text-white ring-1 ring-white/30 flex items-center justify-center transition active:scale-95';
          btnMobile.innerHTML = '<i data-lucide="volume-2" class="w-4 h-4 text-white"></i>';
        } else {
          btnMobile.className = 'md:hidden w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-white/10 hover:bg-white/20 text-white/40 flex items-center justify-center transition active:scale-95';
          btnMobile.innerHTML = '<i data-lucide="volume-x" class="w-4 h-4 text-white/40"></i>';
        }
        if (window.lucide) {
          lucide.createIcons({ root: btnMobile });
        }
      }
    }

    // Initial state setup on boot
    updateFuriganaUi();
    updateAutoAudioUi();

    function handleToggleFurigana() {
      isFuriganaEnabled = !isFuriganaEnabled;
      localStorage.setItem('haku_furigana_enabled', isFuriganaEnabled ? 'true' : 'false');
      updateFuriganaUi();
      showToast(isFuriganaEnabled ? 'ふりがなを表示します（ON）' : 'ふりがなを非表示にしました（OFF）');
    }

    const btnToggleFuri = document.getElementById('btnToggleFurigana');
    if (btnToggleFuri) {
      btnToggleFuri.addEventListener('click', handleToggleFurigana);
    }
    const btnToggleFuriMobile = document.getElementById('btnToggleFuriganaMobile');
    if (btnToggleFuriMobile) {
      btnToggleFuriMobile.addEventListener('click', handleToggleFurigana);
    }
    const containerToggleFuri = document.getElementById('containerToggleFurigana');
    if (containerToggleFuri) {
      containerToggleFuri.addEventListener('click', (e) => {
        if (!e.target.closest('#btnToggleFurigana')) {
          handleToggleFurigana();
        }
      });
    }

    function handleToggleAutoAudio() {
      isAutoAudioEnabled = !isAutoAudioEnabled;
      localStorage.setItem('haku_auto_audio_enabled', isAutoAudioEnabled ? 'true' : 'false');
      updateAutoAudioUi();
      showToast(isAutoAudioEnabled ? '音声自動再生を有効にしました（ON 🔊）' : '音声自動再生を解除しました（OFF 🔇）');
      if (isAutoAudioEnabled && activeDeck[currentIndex]) {
        const card = activeDeck[currentIndex];
        if (!isCardFlipped) {
          speakJapanese(card);
        } else {
          const exampleJa = (card.example && card.example.ja) ? card.example.ja : null;
          speakJapaneseSequence(card, exampleJa);
        }
      }
    }

    const btnToggleAudio = document.getElementById('btnToggleAutoAudio');
    if (btnToggleAudio) {
      btnToggleAudio.addEventListener('click', handleToggleAutoAudio);
    }
    const btnToggleAudioMobile = document.getElementById('btnToggleAutoAudioMobile');
    if (btnToggleAudioMobile) {
      btnToggleAudioMobile.addEventListener('click', handleToggleAutoAudio);
    }
    const containerToggleAudio = document.getElementById('containerToggleAutoAudio');
    if (containerToggleAudio) {
      containerToggleAudio.addEventListener('click', (e) => {
        if (!e.target.closest('#btnToggleAutoAudio')) {
          handleToggleAutoAudio();
        }
      });
    }

    // PC版 / スマホ版の自動切り替え連動（画面リサイズ・回転時）
    window.addEventListener('resize', () => {
      updateAutoAudioUi();
      updateFuriganaUi();
    });

    // Portal Drawer Open/Close controls (2枚目写真仕様)
    const btnOpenDrawer = document.getElementById('btnOpenMenuDrawer');
    if (btnOpenDrawer) {
      btnOpenDrawer.addEventListener('click', openMenuDrawer);
    }

    const btnCloseDrawer = document.getElementById('btnCloseMenuDrawer');
    if (btnCloseDrawer) {
      btnCloseDrawer.addEventListener('click', closeMenuDrawer);
    }

    const drawerOverlay = document.getElementById('portalDrawerOverlay');
    if (drawerOverlay) {
      drawerOverlay.addEventListener('click', closeMenuDrawer);
    }

    // Portal Drawer Menu Buttons
    const drawerBtnHome = document.getElementById('drawerBtnHome');
    if (drawerBtnHome) {
      drawerBtnHome.addEventListener('click', () => {
        closeMenuDrawer();
        const topSearch = document.getElementById('globalTopSearchInput');
        const clearTopBtn = document.getElementById('btnClearTopSearch');
        const dropdown = document.getElementById('searchDropdownContainer');
        if (topSearch) topSearch.value = '';
        if (clearTopBtn) clearTopBtn.classList.add('hidden');
        if (dropdown) dropdown.classList.add('hidden');
        sidebarSearchQuery = '';

        backToFolderOverview();
        switchView('flashcards');
      });
    }

    const drawerBtnMylist = document.getElementById('drawerBtnMylist');
    if (drawerBtnMylist) {
      drawerBtnMylist.addEventListener('click', () => {
        closeMenuDrawer();
        switchView('mylist');
      });
    }

    const drawerBtnJlpt = document.getElementById('drawerBtnJlpt');
    if (drawerBtnJlpt) {
      drawerBtnJlpt.addEventListener('click', () => {
        closeMenuDrawer();
        switchView('jlpt');
      });
    }

    const drawerBtnQuiz = document.getElementById('drawerBtnQuiz');
    if (drawerBtnQuiz) {
      drawerBtnQuiz.addEventListener('click', () => {
        closeMenuDrawer();
        switchView('quiz');
      });
    }

    const drawerBtnLogin = document.getElementById('drawerBtnLogin');
    if (drawerBtnLogin) {
      drawerBtnLogin.addEventListener('click', () => {
        closeMenuDrawer();
        document.getElementById('loginModal').classList.remove('hidden');
      });
    }

    const drawerBtnLogout = document.getElementById('drawerBtnLogout');
    if (drawerBtnLogout) {
      drawerBtnLogout.addEventListener('click', () => {
        closeMenuDrawer();
        setStudent(null);
        showToast('Logged out / ログアウトしました');
      });
    }

    const drawerBtnHelpGuide = document.getElementById('drawerBtnHelpGuide');
    if (drawerBtnHelpGuide) {
      drawerBtnHelpGuide.addEventListener('click', () => {
        closeMenuDrawer();
        openHelpGuideModal();
      });
    }

    // Language selector in Drawer (母国語設定)
    const drawerLangSelect = document.getElementById('drawerLangSelect');
    if (drawerLangSelect) {
      drawerLangSelect.addEventListener('change', (e) => {
        currentLang = e.target.value;
        applyUiLanguage(currentLang);
        renderCurrentCard();
        renderSidebarContent();
        showToast(currentLang === 'ja' ? '母国語を日本語に設定しました' : 'Native language updated');
      });
    }

    // Deck toggle: Shared vs Student Dedicated vs JLPT
    const filterAllBtn = document.getElementById('filterAllDeck');
    const filterMyBtn = document.getElementById('filterMyDeck');
    const filterJlptBtn = document.getElementById('filterJlptDeck');

    function updateDeckFilterPillUi() {
      const activeClass = 'px-2.5 py-0.5 rounded-full bg-deepNavy text-white font-bold transition text-[11px] shadow-xs';
      const inactiveClass = 'px-2.5 py-0.5 rounded-full text-slate-600 font-semibold transition text-[11px] hover:text-slate-900';

      if (filterAllBtn) filterAllBtn.className = (currentDeckFilter === 'all') ? activeClass : inactiveClass;
      if (filterMyBtn) filterMyBtn.className = (currentDeckFilter === 'mine') ? activeClass : inactiveClass;
      if (filterJlptBtn) {
        if (currentDeckFilter === 'jlpt') {
          filterJlptBtn.className = 'px-2.5 py-0.5 rounded-full bg-teal-600 text-white font-bold transition text-[11px] shadow-xs';
          filterJlptBtn.textContent = `JLPT (${currentJlptDeckLevel})`;
        } else {
          filterJlptBtn.className = inactiveClass;
          filterJlptBtn.textContent = 'JLPT';
        }
      }
    }

    if (filterAllBtn) {
      filterAllBtn.addEventListener('click', () => {
        currentDeckFilter = 'all';
        updateDeckFilterPillUi();
        updateActiveDeck();
      });
    }

    if (filterMyBtn) {
      filterMyBtn.addEventListener('click', () => {
        if (!currentStudent) {
          showToast('Please log in with student credentials');
          document.getElementById('loginModal').classList.remove('hidden');
          return;
        }
        currentDeckFilter = 'mine';
        updateDeckFilterPillUi();
        updateActiveDeck();
      });
    }

    if (filterJlptBtn) {
      filterJlptBtn.addEventListener('click', () => {
        // Show JLPT Level Select modal first so user can pick N5..N1
        openJlptLevelSelectModal();
      });
    }

    // Flip card click
    document.getElementById('flashcardElement').addEventListener('click', (e) => {
      // Prevent flipping if clicked on button or if user is selecting text in example
      if (e.target.closest('button')) return;
      // If user performed a drag / swipe gesture, do not flip
      if (hasMovedBeyondTapThreshold) {
        hasMovedBeyondTapThreshold = false;
        return;
      }
      const sel = window.getSelection();
      if (sel && !sel.isCollapsed && sel.toString().trim().length > 0) return;
      if (e.target.closest('#exampleTextContainer')) return;
      flipCard();
    });

    // Reverse Mode (Front: Japanese ⇄ Native)
    document.getElementById('btnToggleReverse').addEventListener('click', () => {
      isReverseMode = !isReverseMode;
      const reverseLabel = document.getElementById('reverseModeLabel');
      if (reverseLabel) {
        if (currentLang === 'ja') {
          reverseLabel.textContent = isReverseMode ? '表面: 母国語' : '表面: 日本語';
        } else {
          reverseLabel.textContent = isReverseMode ? 'Front: Native' : 'Front: Japanese';
        }
      }
      renderCurrentCard();
    });

    // Folder & Unit Navigation Listeners
    document.getElementById('btnBackToFolders').addEventListener('click', backToFolderOverview);
    document.getElementById('btnStudyEntireFolder').addEventListener('click', startStudyingEntireFolder);
    document.getElementById('btnChangeUnit').addEventListener('click', () => {
      if (isMylistStudyMode || isSearchStudyMode) {
        // Return directly to My List or folder overview
        backToFolderOverview();
      } else {
        // Return to units list of current folder
        openFolderUnits(currentFolder === 'all' ? 'folder_1' : currentFolder);
      }
    });

    // Shuffle current unit or current deck
    document.getElementById('btnShuffleCurrent').addEventListener('click', () => {
      if (activeDeck.length === 0) {
        showToast('No cards in this deck');
        return;
      }
      activeDeck.sort(() => Math.random() - 0.5);
      currentIndex = 0;
      renderCurrentCard();
      showToast('Shuffled current deck 🔀');
    });

    // Shuffle ALL cards
    document.getElementById('btnShuffleAll').addEventListener('click', () => {
      currentFolder = 'all';
      currentSection = 'all';
      const isJa = currentLang === 'ja';
      document.getElementById('activeStudySectionName').textContent = isJa ? '全単元 (全シャッフル)' : 'All Units (Shuffle All)';
      document.getElementById('activeStudyFolderName').textContent = isJa ? 'カリキュラム一覧' : 'Curriculum';
      document.getElementById('folderOverviewPanel').classList.add('hidden');
      document.getElementById('unitListPanel').classList.add('hidden');
      document.getElementById('activeStudyHeader').classList.remove('hidden');

      updateActiveDeck();
      activeDeck.sort(() => Math.random() - 0.5);
      currentIndex = 0;
      renderCurrentCard();
      showToast(isJa ? '全単元をシャッフルしました！🔀' : 'Shuffled all curriculum cards! 🔀');
    });

    // Prev / Next Card Controls
    document.getElementById('btnPrev').addEventListener('click', () => {
      if (currentIndex > 0) {
        currentIndex--;
        renderCurrentCard();
      } else {
        showToast('First card');
      }
    });

    document.getElementById('btnNext').addEventListener('click', () => {
      if (currentIndex < activeDeck.length - 1) {
        currentIndex++;
        renderCurrentCard();
      } else {
        showToast('Last card! Try taking a quiz 🎉');
      }
    });

    // Star / Mylist Toggle on current card
    document.getElementById('btnStarCurrent').addEventListener('click', (e) => {
      e.stopPropagation();
      if (!activeDeck[currentIndex]) return;
      const card = activeDeck[currentIndex];
      promptFolderSelectAndAdd(card, () => {
        renderCurrentCard();
      });
    });

    // --- Card Marking Helpers (覚えた！ & もう一度！) ---
    function markCardLearned(cardToMark = null) {
      const card = cardToMark || activeDeck[currentIndex];
      if (!card) return;
      const LEARNED_FOLDER_ID = 'folder_learned';
      const LEARNED_FOLDER_NAME = '覚えた！';

      // フォルダ存在確認
      if (!mylistFolders.find(f => f.id === LEARNED_FOLDER_ID || f.name === LEARNED_FOLDER_NAME)) {
        mylistFolders.push({ id: LEARNED_FOLDER_ID, name: LEARNED_FOLDER_NAME });
      }

      // マイリストに追加＆フォルダ割り当て
      mylistSet.add(card.id);
      mylistCardFolderMap[card.id] = LEARNED_FOLDER_ID;
      knownSet.add(card.id);
      saveMylistForCurrentStudent();

      showToast(currentLang === 'ja' ? `「${card.word}」を『覚えた！』に保存しました ✨` : `Saved "${card.word}" to Learned! ✨`);

      // 自動的に次のカードへ進む
      if (currentIndex < activeDeck.length - 1) {
        currentIndex++;
        renderCurrentCard();
      } else {
        renderCurrentCard();
        showToast(currentLang === 'ja' ? '最後のカードです！お疲れ様でした 🎉' : 'Last card! Great job 🎉');
      }
    }

    function markCardReview(cardToMark = null) {
      const card = cardToMark || activeDeck[currentIndex];
      if (!card) return;
      const REVIEW_FOLDER_ID = 'folder_review';
      const REVIEW_FOLDER_NAME = 'もう一度！';

      // フォルダ存在確認
      if (!mylistFolders.find(f => f.id === REVIEW_FOLDER_ID || f.name === REVIEW_FOLDER_NAME)) {
        mylistFolders.push({ id: REVIEW_FOLDER_ID, name: REVIEW_FOLDER_NAME });
      }

      // マイリストに追加＆フォルダ割り当て
      mylistSet.add(card.id);
      mylistCardFolderMap[card.id] = REVIEW_FOLDER_ID;
      knownSet.delete(card.id); // まだ覚えていないので既習フラグを外す
      saveMylistForCurrentStudent();

      showToast(currentLang === 'ja' ? `「${card.word}」を『もう一度！』に保存しました 🔁` : `Saved "${card.word}" to Review again! 🔁`);

      // 自動的に次のカードへ進む
      if (currentIndex < activeDeck.length - 1) {
        currentIndex++;
        renderCurrentCard();
      } else {
        renderCurrentCard();
        showToast(currentLang === 'ja' ? '最後のカードです！もう一度復習しましょう 🔁' : 'Last card! Review again 🔁');
      }
    }

    // 「覚えた！」ボタン (右側): マイリストに追加し「覚えた！」フォルダに保存して次のカードへ進む
    const btnMarkKnown = document.getElementById('btnMarkKnown');
    if (btnMarkKnown) {
      btnMarkKnown.addEventListener('click', () => markCardLearned());
    }

    // 「もう一度！」ボタン (左側): マイリストに追加し「もう一度！」フォルダに保存して次のカードへ進む
    const btnMarkReview = document.getElementById('btnMarkReview');
    if (btnMarkReview) {
      btnMarkReview.addEventListener('click', () => markCardReview());
    }

    // --- スマホ版スワイプ操作 (右スワイプ: 覚えた！ / 左スワイプ: もう一回！) ---
    const flashcardEl = document.getElementById('flashcardElement');
    const badgeLearned = document.getElementById('swipeBadgeLearned');
    const badgeReview = document.getElementById('swipeBadgeReview');

    let touchStartX = 0;
    let touchStartY = 0;
    let touchCurrentX = 0;
    let touchCurrentY = 0;
    let isSwiping = false;
    hasMovedBeyondTapThreshold = false;

    if (flashcardEl) {
      flashcardEl.addEventListener('touchstart', (e) => {
        // ボタンやテキスト選択エリアでのタッチは無視
        if (e.target.closest('button') || e.target.closest('#exampleTextContainer')) return;
        const touch = e.touches[0];
        touchStartX = touch.clientX;
        touchStartY = touch.clientY;
        touchCurrentX = touch.clientX;
        touchCurrentY = touch.clientY;
        isSwiping = true;
        hasMovedBeyondTapThreshold = false;
      }, { passive: true });

      flashcardEl.addEventListener('touchmove', (e) => {
        if (!isSwiping || !activeDeck[currentIndex]) return;
        const touch = e.touches[0];
        touchCurrentX = touch.clientX;
        touchCurrentY = touch.clientY;

        const deltaX = touchCurrentX - touchStartX;
        const deltaY = touchCurrentY - touchStartY;

        // タップ判定の閾値（8px以上動いたらスワイプ動作とみなす）
        if (Math.abs(deltaX) > 8 || Math.abs(deltaY) > 8) {
          hasMovedBeyondTapThreshold = true;
        }

        // 横スワイプが縦スクロールより優勢な場合にカードを物理的に追従
        if (Math.abs(deltaX) > Math.abs(deltaY) && Math.abs(deltaX) > 12) {
          // 水平スクロールをキャンセル
          if (e.cancelable) e.preventDefault();

          const rotation = (deltaX / 18); // 傾き効果
          const baseRotateY = isCardFlipped ? 180 : 0;
          flashcardEl.style.transition = 'none';
          flashcardEl.style.transform = `translateX(${deltaX}px) rotate(${rotation}deg) rotateY(${baseRotateY}deg)`;

          // バッジの透明度調整 (50px〜120pxでフェードイン)
          if (deltaX > 25) {
            // 右スワイプ: 覚えた！
            const opacity = Math.min(1, (deltaX - 25) / 60);
            if (badgeLearned) badgeLearned.style.opacity = opacity;
            if (badgeReview) badgeReview.style.opacity = '0';
          } else if (deltaX < -25) {
            // 左スワイプ: もう一回！
            const opacity = Math.min(1, (Math.abs(deltaX) - 25) / 60);
            if (badgeReview) badgeReview.style.opacity = opacity;
            if (badgeLearned) badgeLearned.style.opacity = '0';
          } else {
            if (badgeLearned) badgeLearned.style.opacity = '0';
            if (badgeReview) badgeReview.style.opacity = '0';
          }
        }
      }, { passive: false });

      const handleTouchEnd = (e) => {
        if (!isSwiping) return;
        isSwiping = false;

        const deltaX = touchCurrentX - touchStartX;
        const deltaY = touchCurrentY - touchStartY;
        const SWIPE_THRESHOLD = 75; // スワイプ成立とみなす移動距離 (px)
        const baseRotateY = isCardFlipped ? 180 : 0;

        // バッジリセット
        if (badgeLearned) badgeLearned.style.opacity = '0';
        if (badgeReview) badgeReview.style.opacity = '0';

        // スワイプ成立判定 (横方向が優勢かつ閾値超え)
        if (Math.abs(deltaX) > SWIPE_THRESHOLD && Math.abs(deltaX) > Math.abs(deltaY)) {
          // モバイルの音声合成エンジンをアクティブに復帰
          if ('speechSynthesis' in window && window.speechSynthesis.paused) {
            window.speechSynthesis.resume();
          }
          if (deltaX > 0) {
            // ★ 右スワイプ: 「覚えた！」
            flashcardEl.style.transition = 'transform 0.22s cubic-bezier(0.2, 0.8, 0.4, 1), opacity 0.22s ease';
            flashcardEl.style.transform = `translateX(120%) rotate(25deg) rotateY(${baseRotateY}deg)`;
            flashcardEl.style.opacity = '0';

            setTimeout(() => {
              flashcardEl.style.transition = 'none';
              flashcardEl.style.transform = `rotateY(${baseRotateY}deg)`;
              flashcardEl.style.opacity = '1';
              markCardLearned();
            }, 220);
          } else {
            // ★ 左スワイプ: 「もう一回！」
            flashcardEl.style.transition = 'transform 0.22s cubic-bezier(0.2, 0.8, 0.4, 1), opacity 0.22s ease';
            flashcardEl.style.transform = `translateX(-120%) rotate(-25deg) rotateY(${baseRotateY}deg)`;
            flashcardEl.style.opacity = '0';

            setTimeout(() => {
              flashcardEl.style.transition = 'none';
              flashcardEl.style.transform = `rotateY(${baseRotateY}deg)`;
              flashcardEl.style.opacity = '1';
              markCardReview();
            }, 220);
          }
        } else {
          // スワイプキャンセル: 元の位置にスムーズに戻す
          flashcardEl.style.transition = 'transform 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
          flashcardEl.style.transform = `translateX(0px) rotate(0deg) rotateY(${baseRotateY}deg)`;
        }
      };

      flashcardEl.addEventListener('touchend', handleTouchEnd);
      flashcardEl.addEventListener('touchcancel', handleTouchEnd);
    }

    // Speech Audio buttons
    document.getElementById('btnSpeakFront').addEventListener('click', (e) => {
      e.stopPropagation();
      if (activeDeck[currentIndex]) {
        toggleJapaneseSpeech(activeDeck[currentIndex]);
      }
    });

    document.getElementById('btnSpeakBack').addEventListener('click', (e) => {
      e.stopPropagation();
      if (activeDeck[currentIndex]) {
        toggleJapaneseSpeech(activeDeck[currentIndex]);
      }
    });

    document.getElementById('btnSpeakExample').addEventListener('click', (e) => {
      e.stopPropagation();
      if (activeDeck[currentIndex] && activeDeck[currentIndex].example) {
        toggleJapaneseSpeech(activeDeck[currentIndex].example.ja);
      }
    });

    // Quiz Scope Switchers (Current Unit / My List / Shuffle All)
    const btnQuizScopeCur = document.getElementById('btnQuizScopeCurrent');
    if (btnQuizScopeCur) {
      btnQuizScopeCur.addEventListener('click', () => {
        quizScope = 'current';
        startQuiz();
        showToast('Quiz set to: Current Unit / Deck');
      });
    }

    const btnQuizScopeMy = document.getElementById('btnQuizScopeMylist');
    if (btnQuizScopeMy) {
      btnQuizScopeMy.addEventListener('click', () => {
        quizScope = 'mylist';
        startQuiz();
        const folderObj = mylistFolders.find(f => f.id === activeMylistFolderId);
        showToast(folderObj ? `Quiz set to: My List 📁 ${folderObj.name}` : 'Quiz set to: My List (All)');
      });
    }

    const btnQuizScopeAl = document.getElementById('btnQuizScopeAll');
    if (btnQuizScopeAl) {
      btnQuizScopeAl.addEventListener('click', () => {
        quizScope = 'all';
        startQuiz();
        showToast('Quiz set to: Shuffle All Units');
      });
    }

    // Quiz Question Count Buttons (10問 / 20問 / 30問 / 全問)
    document.querySelectorAll('.quiz-count-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const countVal = e.currentTarget.getAttribute('data-count');
        quizQuestionLimit = (countVal === 'all') ? 99999 : (Number(countVal) || 10);
        document.querySelectorAll('.quiz-count-btn').forEach(b => {
          b.className = 'quiz-count-btn px-2 py-0.5 rounded-lg text-[10px] font-bold bg-slate-100 hover:bg-slate-200 text-slate-600 transition';
        });
        e.currentTarget.className = 'quiz-count-btn active px-2 py-0.5 rounded-lg text-[10px] font-bold bg-deepNavy text-white transition shadow-2xs';
        startQuiz();
      });
    });

    // Direct Test button on active study header
    const btnTestCur = document.getElementById('btnTestCurrent');
    if (btnTestCur) {
      btnTestCur.addEventListener('click', () => {
        startQuizWithScope('current', currentSection, document.getElementById('activeStudySectionName')?.textContent);
      });
    }

    // Direct Test button on folder overview panel
    const btnTestEntireFld = document.getElementById('btnTestEntireFolder');
    if (btnTestEntireFld) {
      btnTestEntireFld.addEventListener('click', () => {
        const fc = FOLDER_CONFIGS.find(f => f.id === currentFolder);
        startQuizWithScope('folder', currentFolder, fc ? fc.title : 'フォルダ全体');
      });
    }

    // Quiz Next Button
    document.getElementById('btnQuizNext').addEventListener('click', () => {
      quizIndex++;
      renderQuizQuestion();
    });

    // Quiz & Test Mode Switcher Buttons (単語クイズ vs 実践テスト)
    const btnModeQuiz = document.getElementById('btnModeQuiz');
    if (btnModeQuiz) {
      btnModeQuiz.addEventListener('click', () => {
        setQuizMode('quiz');
        startQuiz();
      });
    }
    const btnModeTest = document.getElementById('btnModeTest');
    if (btnModeTest) {
      btnModeTest.addEventListener('click', () => {
        setQuizMode('test');
        startQuiz();
      });
    }

    // Test Subtype Selector Buttons (A+B すべて, A: 例文 穴埋め, B: 活用・文法)
    document.querySelectorAll('.test-type-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const type = e.currentTarget.getAttribute('data-test-type');
        currentTestSubtype = type || 'all';
        document.querySelectorAll('.test-type-btn').forEach(b => {
          if (b === e.currentTarget) {
            b.className = 'test-type-btn active py-1 px-1 rounded-xl text-[10px] font-bold bg-teal-700 text-white transition shadow-2xs text-center truncate';
          } else {
            b.className = 'test-type-btn py-1 px-1 rounded-xl text-[10px] font-bold border border-softBorder bg-white text-slate-600 hover:border-teal-700 transition text-center truncate';
          }
        });
        const badge = document.getElementById('testTypeBadge');
        if (badge) {
          if (currentTestSubtype === 'fillblank') badge.textContent = 'A: 例文 穴埋め';
          else if (currentTestSubtype === 'conjugation') badge.textContent = 'B: 活用・文法';
          else badge.textContent = 'A + B MIX';
        }
        startQuiz();
      });
    });

    // Multilingual Hint Toggle Button (ON: 翻訳表示 / OFF: 日本語のみ)
    const btnToggleMulti = document.getElementById('btnToggleMultilingual');
    if (btnToggleMulti) {
      btnToggleMulti.addEventListener('click', () => {
        isMultilingualEnabled = !isMultilingualEnabled;
        localStorage.setItem('haku_multilingual_quiz', isMultilingualEnabled ? 'true' : 'false');
        updateMultilingualButtonUI();
        renderQuizQuestion();
        showToast(isMultilingualEnabled ? '🌐 多言語ヒント: ON（表示中）' : '🌐 多言語ヒント: OFF（日本語のみ）');
      });
    }

    // Toggle Folders Dropdown in Mylist
    const btnToggleFolders = document.getElementById('btnToggleMylistFolders');
    const foldersContainer = document.getElementById('mylistFoldersDropdownContainer');
    const arrowIcon = document.getElementById('iconToggleFoldersArrow');
    if (btnToggleFolders && foldersContainer) {
      btnToggleFolders.addEventListener('click', () => {
        const isHidden = foldersContainer.classList.contains('hidden');
        foldersContainer.classList.toggle('hidden', !isHidden);
        if (arrowIcon) {
          arrowIcon.style.transform = isHidden ? 'rotate(180deg)' : 'rotate(0deg)';
        }
      });
    }

    // Create New Custom Folder in Mylist
    const btnCreateFolder = document.getElementById('btnCreateMylistFolder');
    if (btnCreateFolder) {
      btnCreateFolder.addEventListener('click', () => {
        const folderName = window.prompt('Enter new folder name (e.g. N5 Verbs, Travel Phrases, Exam Prep):');
        if (!folderName || !folderName.trim()) return;
        const trimmed = folderName.trim();
        const newFolderId = `mf_${Date.now()}`;
        mylistFolders.push({ id: newFolderId, name: trimmed });
        activeMylistFolderId = newFolderId;
        saveMylistForCurrentStudent();
        renderMylistView();
        showToast(`Created folder "${trimmed}" 📁`);
      });
    }

    // Rename Custom Folder
    const btnRenameFolder = document.getElementById('btnRenameMylistFolder');
    if (btnRenameFolder) {
      btnRenameFolder.addEventListener('click', () => {
        if (activeMylistFolderId === 'all') return;
        const folder = mylistFolders.find(f => f.id === activeMylistFolderId);
        if (!folder) return;
        const newName = window.prompt('Enter new folder name:', folder.name);
        if (!newName || !newName.trim()) return;
        folder.name = newName.trim();
        saveMylistForCurrentStudent();
        renderMylistView();
        showToast('Folder renamed ✨');
      });
    }

    // Delete Custom Folder
    const btnDeleteFolder = document.getElementById('btnDeleteMylistFolder');
    if (btnDeleteFolder) {
      btnDeleteFolder.addEventListener('click', () => {
        if (activeMylistFolderId === 'all') return;
        const folder = mylistFolders.find(f => f.id === activeMylistFolderId);
        if (!folder) return;
        if (!confirm(`Delete folder "${folder.name}"?\n(Words will remain in My List)`)) return;
        
        // Remove folder and unassign cards from it
        mylistFolders = mylistFolders.filter(f => f.id !== folder.id);
        Object.keys(mylistCardFolderMap).forEach(cardId => {
          if (mylistCardFolderMap[cardId] === folder.id) {
            delete mylistCardFolderMap[cardId];
          }
        });
        activeMylistFolderId = 'all';
        saveMylistForCurrentStudent();
        renderMylistView();
        showToast('Folder deleted');
      });
    }

    // Mylist Sort select handler
    const selectMylistSortElem = document.getElementById('selectMylistSort');
    if (selectMylistSortElem) {
      selectMylistSortElem.value = mylistSortOrder;
      selectMylistSortElem.addEventListener('change', (e) => {
        mylistSortOrder = e.target.value;
        localStorage.setItem('haku_mylist_sort_order', mylistSortOrder);
        renderMylistItems();
      });
    }

    // Mylist Study button (Studies active folder, or all if 'all' is selected)
    document.getElementById('btnStudyMylist').addEventListener('click', () => {
      let targetCards = getMylistCards();
      if (activeMylistFolderId !== 'all') {
        targetCards = targetCards.filter(c => mylistCardFolderMap[c.id] === activeMylistFolderId);
      }
      targetCards = sortMylistCards(targetCards, mylistSortOrder);
      if (targetCards.length === 0) {
        showToast(currentLang === 'ja' ? '学習する単語がありません' : 'No words to study');
        return;
      }
      const folderObj = mylistFolders.find(f => f.id === activeMylistFolderId);
      const folderName = folderObj ? folderObj.name : (currentLang === 'ja' ? 'マイリスト全体' : 'My List (All)');

      activeDeck = targetCards;
      currentIndex = 0;
      isSearchStudyMode = true; // Allows back button to return gracefully
      isMylistStudyMode = true;

      switchView('flashcards');

      // Setup active study header
      document.getElementById('folderOverviewPanel').classList.add('hidden');
      document.getElementById('unitListPanel').classList.add('hidden');
      document.getElementById('activeStudyHeader').classList.remove('hidden');
      document.getElementById('activeStudySectionName').textContent = folderName;
      renderCurrentCard();
      let startMsg = `「${folderName}」の練習カードを開始します ⭐`;
      if (currentLang === 'zh_TW' || currentLang === 'zh_HK') startMsg = `開始「${folderName}」的練習卡片 ⭐`;
      else if (currentLang === 'zh_CN') startMsg = `开始「${folderName}」的练习卡片 ⭐`;
      else if (currentLang === 'ko') startMsg = `"${folderName}" 연습 카드를 시작합니다 ⭐`;
      else if (currentLang === 'fr') startMsg = `Début de la pratique des cartes pour « ${folderName} » ⭐`;
      else if (currentLang !== 'ja') startMsg = `Practicing "${folderName}" cards ⭐`;
      showToast(startMsg);
    });

    // Mylist Test button (Quizzes active folder, or all if 'all' is selected)
    const btnTestMy = document.getElementById('btnTestMylist');
    if (btnTestMy) {
      btnTestMy.addEventListener('click', () => {
        let targetCards = getMylistCards();
        if (activeMylistFolderId !== 'all') {
          targetCards = targetCards.filter(c => mylistCardFolderMap[c.id] === activeMylistFolderId);
        }
        if (targetCards.length < 2) {
          showToast('At least 2 words are required to start a test');
          return;
        }
        const folderObj = mylistFolders.find(f => f.id === activeMylistFolderId);
        startQuizWithScope('mylist', activeMylistFolderId, folderObj ? `My List: 📁${folderObj.name}` : 'My List (All)');
      });
    }

    // Admin execute import
    document.getElementById('btnExecuteImport').addEventListener('click', executeImport);

    // Help guide modal toggle & slide controls
    const btnHelpGuide = document.getElementById('btnHelpGuide');
    if (btnHelpGuide) {
      btnHelpGuide.addEventListener('click', openHelpGuideModal);
    }
    const btnHelpGuidePrev = document.getElementById('btnHelpGuidePrev');
    if (btnHelpGuidePrev) {
      btnHelpGuidePrev.addEventListener('click', prevHelpGuideSlide);
    }
    const btnHelpGuideNext = document.getElementById('btnHelpGuideNext');
    if (btnHelpGuideNext) {
      btnHelpGuideNext.addEventListener('click', nextHelpGuideSlide);
    }

    // Mobile shuffle all button
    const btnShuffleAllMobile = document.getElementById('btnShuffleAllMobile');
    if (btnShuffleAllMobile) {
      btnShuffleAllMobile.addEventListener('click', () => {
        document.getElementById('btnShuffleAll')?.click();
      });
    }

    // Login modal toggles
    document.getElementById('userBtn').addEventListener('click', () => {
      document.getElementById('loginModal').classList.remove('hidden');
    });

    document.getElementById('btnLoginCancel').addEventListener('click', () => {
      document.getElementById('loginModal').classList.add('hidden');
    });

    document.getElementById('btnLoginSubmit').addEventListener('click', async () => {
      const studentIdInput = document.getElementById('loginStudentId').value.trim();
      const passcodeInput = document.getElementById('loginPasscode').value.trim();

      // Check if user is logging in as Haku-sensei / Admin using the passcode ppooiillkk
      const isTeacherId = (!studentIdInput || studentIdInput.toLowerCase() === 'haku' || studentIdInput === 'ハク' || studentIdInput.toLowerCase() === 'admin' || studentIdInput === '先生');
      if (passcodeInput === 'ppooiillkk' && isTeacherId) {
        let teacherUser = students.find(s => s.id === 'haku');
        if (!teacherUser) {
          teacherUser = { id: 'haku', name: 'ハク先生', lang: 'ja', passcode: 'ppooiillkk' };
          students.unshift(teacherUser);
          localStorage.setItem('haku_students', JSON.stringify(students));
        }
        setStudent(teacherUser);
        document.getElementById('loginModal').classList.add('hidden');
        if (typeof closeMenuDrawer === 'function') closeMenuDrawer();
        switchView('admin');
        showToast('ハク先生・管理者モードを開きました！🌸');
        return;
      }

      let student = students.find(s => 
        (s.id.toLowerCase() === studentIdInput.toLowerCase() || s.name.toLowerCase() === studentIdInput.toLowerCase()) &&
        s.passcode === passcodeInput
      );

      // If not matched locally, attempt Cloud Firebase authentication check
      if (!student && isFirebaseReady && fbAuth && studentIdInput) {
        try {
          const authSuccess = await ensureStudentCloudAuth(studentIdInput, passcodeInput);
          if (authSuccess) {
            // Find existing student entry or create placeholder entry
            student = students.find(s => s.id.toLowerCase() === studentIdInput.toLowerCase());
            if (!student) {
              student = { id: studentIdInput, name: `生徒${studentIdInput}`, lang: 'en', passcode: passcodeInput };
              students.push(student);
              localStorage.setItem('haku_students', JSON.stringify(students));
            } else {
              student.passcode = passcodeInput;
              localStorage.setItem('haku_students', JSON.stringify(students));
            }
          }
        } catch (authErr) {
          console.warn('Cloud login attempt error:', authErr);
        }
      }

      if (student) {
        setStudent(student);
        document.getElementById('loginModal').classList.add('hidden');
      } else {
        showToast('Invalid Student ID or passcode');
      }
    });

    const btnLoginLogout = document.getElementById('btnLoginLogout');
    if (btnLoginLogout) {
      btnLoginLogout.addEventListener('click', () => {
        setStudent(null);
        document.getElementById('loginModal').classList.add('hidden');
        showToast('Logged out / ログアウトしました');
      });
    }

    // Add new student button in admin (Opens modal with auto-suggested ID and passcode)
    const btnAddNewStudent = document.getElementById('btnAddNewStudent');
    const addStudentModal = document.getElementById('addStudentModal');
    const nameInput = document.getElementById('newStudentNameInput');
    const idInput = document.getElementById('newStudentIdInput');
    const passcodeInput = document.getElementById('newStudentPasscodeInput');
    const langSelect = document.getElementById('newStudentLangSelect');
    const btnCancelAddStudent = document.getElementById('btnCancelAddStudent');
    const btnSaveNewStudent = document.getElementById('btnSaveNewStudent');

    if (btnAddNewStudent && addStudentModal) {
      btnAddNewStudent.addEventListener('click', () => {
        // Calculate next numeric ID e.g. 0022
        const numericIds = students
          .map(s => parseInt(s.id, 10))
          .filter(n => !isNaN(n));
        const nextNum = numericIds.length > 0 ? Math.max(...numericIds) + 1 : 1;
        const nextIdStr = String(nextNum).padStart(4, '0');
        // Generate memorable paired digits (e.g. 1122, 2233, 3344, 4455, 5566...)
        const d1 = (nextNum % 9) + 1;
        const d2 = ((nextNum + 1) % 9) + 1;
        const nextPasscodeStr = `${d1}${d1}${d2}${d2}`;

        if (nameInput) nameInput.value = '';
        if (idInput) idInput.value = nextIdStr;
        if (passcodeInput) passcodeInput.value = nextPasscodeStr;
        if (langSelect) langSelect.value = 'en';

        addStudentModal.classList.remove('hidden');
        if (nameInput) nameInput.focus();
      });
    }

    if (btnCancelAddStudent && addStudentModal) {
      btnCancelAddStudent.addEventListener('click', () => {
        addStudentModal.classList.add('hidden');
      });
    }

    if (btnSaveNewStudent && addStudentModal) {
      btnSaveNewStudent.addEventListener('click', () => {
        const nameVal = nameInput ? nameInput.value.trim() : '';
        const idVal = idInput ? idInput.value.trim() : '';
        const pinVal = passcodeInput ? passcodeInput.value.trim() : '';
        const langVal = langSelect ? langSelect.value : 'en';

        if (!nameVal) {
          showToast('生徒の名前を入力してください');
          if (nameInput) nameInput.focus();
          return;
        }

        if (!idVal) {
          showToast('生徒IDを入力してください');
          return;
        }

        if (!pinVal || pinVal.length < 4) {
          showToast('4桁のパスコードを入力してください');
          return;
        }

        // Check if ID is duplicate
        if (students.some(s => s.id.toLowerCase() === idVal.toLowerCase())) {
          showToast('この生徒IDは既に使用されています');
          return;
        }

        const newStudent = {
          id: idVal,
          name: nameVal,
          lang: langVal,
          passcode: pinVal
        };

        students.push(newStudent);
        localStorage.setItem('haku_students', JSON.stringify(students));

        // Initialize empty "授業で習った言葉" folder for this new student
        const CLASS_FOLDER_ID = 'folder_class_words';
        const CLASS_FOLDER_NAME = '授業で習った言葉';
        const foldersKey = `haku_mylist_folders_${idVal}`;
        localStorage.setItem(foldersKey, JSON.stringify([{ id: CLASS_FOLDER_ID, name: CLASS_FOLDER_NAME }]));

        renderAdminStudentList();
        addStudentModal.classList.add('hidden');
        showToast(`生徒「${nameVal}」（ID: ${idVal} / PIN: ${pinVal}）を追加しました！✨`);
        alert(`【新規生徒アカウント発行完了】\n\n生徒名: ${nameVal}\n生徒ID: ${idVal}\nパスコード (PIN): ${pinVal}\n\n※このパスコードは先生用管理画面の「生徒アカウント一覧」でもいつでも確認できます。`);
      });
    }

    // --- Edit Student Modal Handling ---
    const editStudentModal = document.getElementById('editStudentModal');
    const editIdInput = document.getElementById('editStudentIdInput');
    const editNameInput = document.getElementById('editStudentNameInput');
    const editPasscodeInput = document.getElementById('editStudentPasscodeInput');
    const editLangSelect = document.getElementById('editStudentLangSelect');
    const btnCancelEditStudent = document.getElementById('btnCancelEditStudent');
    const btnSaveEditStudent = document.getElementById('btnSaveEditStudent');
    let studentBeingEdited = null;

    window.openEditStudentModal = function(studentObj) {
      if (!studentObj || !editStudentModal) return;
      studentBeingEdited = studentObj;
      if (editIdInput) editIdInput.value = studentObj.id;
      if (editNameInput) editNameInput.value = studentObj.name;
      if (editPasscodeInput) editPasscodeInput.value = studentObj.passcode;
      if (editLangSelect) editLangSelect.value = studentObj.lang || 'en';
      editStudentModal.classList.remove('hidden');
      if (editNameInput) editNameInput.focus();
    };

    if (btnCancelEditStudent && editStudentModal) {
      btnCancelEditStudent.addEventListener('click', () => {
        editStudentModal.classList.add('hidden');
        studentBeingEdited = null;
      });
    }

    if (btnSaveEditStudent && editStudentModal) {
      btnSaveEditStudent.addEventListener('click', async () => {
        if (!studentBeingEdited) return;
        const newName = editNameInput ? editNameInput.value.trim() : '';
        const newPin = editPasscodeInput ? editPasscodeInput.value.trim() : '';
        const newLang = editLangSelect ? editLangSelect.value : 'en';

        if (!newName) {
          showToast('生徒の名前を入力してください');
          if (editNameInput) editNameInput.focus();
          return;
        }

        if (!newPin || newPin.length < 4) {
          showToast('4桁以上のパスコードを入力してください');
          if (editPasscodeInput) editPasscodeInput.focus();
          return;
        }

        const oldPin = studentBeingEdited.passcode;
        const studentId = studentBeingEdited.id;

        // 1. Update in-memory and local storage
        studentBeingEdited.name = newName;
        studentBeingEdited.passcode = newPin;
        studentBeingEdited.lang = newLang;

        // Update in students array
        const idx = students.findIndex(s => s.id === studentId);
        if (idx !== -1) {
          students[idx] = { ...studentBeingEdited };
        }
        localStorage.setItem('haku_students', JSON.stringify(students));

        // If currently logged-in student is this student, update session info
        if (currentStudent && currentStudent.id === studentId) {
          currentStudent.name = newName;
          currentStudent.passcode = newPin;
          currentStudent.lang = newLang;
          document.getElementById('headerStudentBadge').textContent = `Student: ${newName}`;
          const drawerName = document.getElementById('drawerStudentName');
          if (drawerName) drawerName.textContent = newName;
        }

        // 2. Synchronize new password to Firebase Cloud Auth behind the scenes
        if (isFirebaseReady && fbAuth && studentId !== 'haku' && studentId !== 'admin') {
          try {
            const virtualEmail = `${studentId.toLowerCase()}@haku.local`;
            const oldPasswordStr = `haku_${oldPin}_sec`;
            const newPasswordStr = `haku_${newPin}_sec`;

            // Try signing in with old passcode to update to new passcode
            try {
              const userCred = await fbAuth.signInWithEmailAndPassword(virtualEmail, oldPasswordStr);
              if (userCred && userCred.user) {
                await userCred.user.updatePassword(newPasswordStr);
                console.log(`Cloud password updated for student ${studentId} ☁️🔑`);
              }
            } catch (authErr) {
              // If not found or couldn't sign in, attempt account creation with new passcode
              if (authErr.code === 'auth/user-not-found' || authErr.code === 'auth/invalid-credential') {
                try {
                  await fbAuth.createUserWithEmailAndPassword(virtualEmail, newPasswordStr);
                  console.log(`New cloud account created with updated password for ${studentId} ☁️`);
                } catch (cErr) {}
              }
            }
          } catch (cloudErr) {
            console.warn('Cloud password sync notice:', cloudErr);
          }
        }

        renderAdminStudentList();
        editStudentModal.classList.add('hidden');
        showToast(`生徒「${newName}」（ID: ${studentId}）の情報を更新しました！✏️✨`);
      });
    }

    // --- JLPT View Controls ---
    const btnJlptBackHome = document.getElementById('btnJlptBackHome');
    if (btnJlptBackHome) {
      btnJlptBackHome.addEventListener('click', () => {
        switchView('flashcards');
      });
    }

    const btnJlptPracticeCards = document.getElementById('btnJlptPracticeCards');
    if (btnJlptPracticeCards) {
      btnJlptPracticeCards.addEventListener('click', () => {
        selectJlptLevelForCards(currentJlptLevel || 'N5');
      });
    }

    const btnJlptViewCard = document.getElementById('btnJlptViewCard');
    const btnJlptViewList = document.getElementById('btnJlptViewList');
    if (btnJlptViewCard && btnJlptViewList) {
      btnJlptViewCard.addEventListener('click', () => {
        currentJlptViewMode = 'card';
        btnJlptViewCard.className = 'p-1 rounded-md bg-deepNavy text-white transition';
        btnJlptViewList.className = 'p-1 rounded-md text-slate-500 hover:text-slate-800 transition';
        renderJlptPage();
      });
      btnJlptViewList.addEventListener('click', () => {
        currentJlptViewMode = 'list';
        btnJlptViewList.className = 'p-1 rounded-md bg-deepNavy text-white transition';
        btnJlptViewCard.className = 'p-1 rounded-md text-slate-500 hover:text-slate-800 transition';
        renderJlptPage();
      });
    }

    const jlptSearchInput = document.getElementById('jlptSearchInput');
    if (jlptSearchInput) {
      jlptSearchInput.addEventListener('input', () => {
        currentJlptPage = 1;
        filterJlptWords();
      });
    }

    const btnJlptModalSpeak = document.getElementById('btnJlptModalSpeak');
    if (btnJlptModalSpeak) {
      btnJlptModalSpeak.addEventListener('click', () => {
        if (currentJlptModalWord) {
          speakJapanese(currentJlptModalWord.word);
        }
      });
    }

    const btnJlptModalSave = document.getElementById('btnJlptModalSave');
    if (btnJlptModalSave) {
      btnJlptModalSave.addEventListener('click', toggleJlptModalSave);
    }
  }


  // =========================================================================
  // ★ 写真完全再現: 例文の文字選択 ＆ 辞書で調べる / マイリスト保存ポップアップ
  // =========================================================================

  let currentSelectedExampleWord = '';
  let currentSelectedExampleReading = '';

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  function sanitizeSelectedWordText(raw) {
    if (!raw) return '';
    let t = raw.replace(/<rt>.*?<\/rt>/gi, '')
               .replace(/<[^>]+>/g, '')
               .trim();
    // 句読点、記号、かっこなどを除去
    t = t.replace(/^[、。！？!?「」『』（）()[\]\s…・:：;；〜~\-\—]+|[、。！？!?「」『』（）()[\]\s…・:：;；〜~\-\—]+$/g, '');
    return t;
  }

  // 例文から重要単語チップ（ボタン）を自動抽出して表示
  function extractKeywordsFromExampleHtml(htmlText) {
    if (!htmlText) return [];
    const candidates = [];
    const seen = new Set();

    // 1. <ruby>漢字<rt>読み</rt></ruby> から漢字単語と読みを抽出
    const rubyRegex = /<ruby>([^<]+)<rt>([^<]+)<\/rt><\/ruby>/g;
    let m;
    while ((m = rubyRegex.exec(htmlText)) !== null) {
      const k = m[1].trim();
      const r = m[2].trim();
      if (k && !seen.has(k)) {
        seen.add(k);
        candidates.push({ word: k, reading: r });
      }
    }

    // 2. 漢字熟語（2文字以上）やカタカナ単語（2文字以上）を抽出
    const plain = htmlText.replace(/<rt>.*?<\/rt>/g, '').replace(/<[^>]+>/g, '');
    const kanjiMatches = plain.match(/[一-龥]{2,}/g) || [];
    const katakanaMatches = plain.match(/[゠-ヿ]{2,}/g) || [];

    [...kanjiMatches, ...katakanaMatches].forEach(w => {
      const clean = w.trim();
      if (clean && !seen.has(clean) && clean.length >= 2) {
        seen.add(clean);
        candidates.push({ word: clean, reading: '' });
      }
    });

    return candidates.slice(0, 6);
  }

  function renderExampleWordChips(exampleHtml) {
    const container = document.getElementById('exampleWordChipsContainer');
    const list = document.getElementById('exampleWordChipsList');
    if (!container || !list) return;

    const chips = extractKeywordsFromExampleHtml(exampleHtml);
    if (!chips || chips.length === 0) {
      container.classList.add('hidden');
      list.innerHTML = '';
      return;
    }

    container.classList.remove('hidden');
    list.innerHTML = chips.map(c => {
      return `
        <button class="btn-example-word-chip px-2 py-0.5 rounded-lg border border-sky-300 bg-sky-50 hover:bg-sky-100 text-sky-800 text-[11px] font-bold cursor-pointer transition shadow-2xs active:scale-95" 
          data-word="${escapeHtml(c.word)}" 
          data-reading="${escapeHtml(c.reading || '')}"
          title="タップして辞書で調べる">
          ${escapeHtml(c.word)}
        </button>
      `;
    }).join('');

    list.querySelectorAll('.btn-example-word-chip').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation(); // カード反転を防止
        const w = btn.getAttribute('data-word');
        const r = btn.getAttribute('data-reading') || '';
        openDictLookupModal(w, r);
      });
    });
  }

  // 例文のテキスト選択ツールバー（なぞった文字の真上に浮き出る黒い操作バー）
  function initExampleSelectionToolbar() {
    const area = document.getElementById('exampleTextContainer');
    const toolbar = document.getElementById('textSelectionToolbar');
    const previewEl = document.getElementById('selectionTextPreview');
    const btnDict = document.getElementById('btnToolbarDict');
    const btnSave = document.getElementById('btnToolbarMylist');

    if (!toolbar) return;

    function updateToolbar() {
      const sel = window.getSelection();
      if (!sel || sel.isCollapsed || !sel.rangeCount) {
        toolbar.classList.add('hidden');
        toolbar.classList.remove('flex');
        return;
      }

      const range = sel.getRangeAt(0);
      let containerNode = range.commonAncestorContainer;
      if (containerNode.nodeType === 3) containerNode = containerNode.parentElement;
      if (!containerNode) return;

      // Don't trigger if inside form input/textarea/select
      if (containerNode.closest && containerNode.closest('input, textarea, select')) {
        toolbar.classList.add('hidden');
        toolbar.classList.remove('flex');
        return;
      }

      // Check if selection is within selectable areas (example sentence, quiz view, flashcards, my list, main container)
      const mainContainer = document.getElementById('mainContainer');
      const isInsideSelectable = (
        (area && area.contains(containerNode)) ||
        (document.getElementById('viewQuiz') && document.getElementById('viewQuiz').contains(containerNode)) ||
        (mainContainer && mainContainer.contains(containerNode))
      );

      if (!isInsideSelectable) {
        toolbar.classList.add('hidden');
        toolbar.classList.remove('flex');
        return;
      }

      // レンジのクローンから<rt>（ふりがな）タグを完全除去して本文の漢字・かなのみ抽出
      let cleaned = '';
      let hintReading = '';
      try {
        const clonedFragment = range.cloneContents();
        const rts = clonedFragment.querySelectorAll ? clonedFragment.querySelectorAll('rt') : [];
        if (rts && rts.length > 0) {
          hintReading = Array.from(rts).map(rt => rt.textContent.trim()).filter(Boolean).join('');
          rts.forEach(rt => rt.remove());
        }
        cleaned = sanitizeSelectedWordText(clonedFragment.textContent);
      } catch (err) {
        cleaned = sanitizeSelectedWordText(sel.toString());
      }

      if (!cleaned || cleaned.length > 30) {
        toolbar.classList.add('hidden');
        toolbar.classList.remove('flex');
        return;
      }

      // ルビ付き要素なら読み仮名も自動取得（もしhintReadingが空の場合）
      if (!hintReading) {
        try {
          const rubyEl = containerNode.closest ? containerNode.closest('ruby') : null;
          if (rubyEl) {
            const rt = rubyEl.querySelector('rt');
            if (rt) hintReading = rt.innerText.trim();
          }
        } catch (e) {}
      }

      // もしクイズの選択肢内なら、そのカードの読み仮名を取得
      try {
        const choiceCard = containerNode.closest ? containerNode.closest('.quiz-choice-card') : null;
        if (choiceCard) {
          const cId = choiceCard.getAttribute('data-card-id');
          const resolved = getCardById(cId);
          if (resolved && (resolved.word === cleaned || cleaned.includes(resolved.word) || resolved.word.includes(cleaned))) {
            hintReading = resolved.reading || '';
          }
        }
      } catch(e) {}

      const rect = range.getBoundingClientRect();
      if (rect.width === 0 && rect.height === 0) {
        toolbar.classList.add('hidden');
        toolbar.classList.remove('flex');
        return;
      }

      currentSelectedExampleWord = cleaned;
      currentSelectedExampleReading = hintReading;

      if (previewEl) previewEl.textContent = cleaned;

      toolbar.classList.remove('hidden');
      toolbar.classList.add('flex');

      // 画面上部や左右にはみ出さないよう座標を補正
      const top = Math.max(10, rect.top - 52);
      const left = Math.min(window.innerWidth - 260, Math.max(10, rect.left + rect.width / 2 - 125));
      toolbar.style.top = `${top}px`;
      toolbar.style.left = `${left}px`;
    }

    // Attach listeners on mouseup, touchend, and copy
    document.addEventListener('mouseup', () => setTimeout(updateToolbar, 60));
    document.addEventListener('touchend', () => setTimeout(updateToolbar, 120));

    // クリップボードへのコピー時もルビ（<rt>）を巻き込まず、本文の文字列のみをコピー
    document.addEventListener('copy', (e) => {
      const sel = window.getSelection();
      if (!sel || sel.isCollapsed || !sel.rangeCount) return;
      try {
        const range = sel.getRangeAt(0);
        const clonedFragment = range.cloneContents();
        const rts = clonedFragment.querySelectorAll ? clonedFragment.querySelectorAll('rt') : [];
        if (rts && rts.length > 0) {
          rts.forEach(rt => rt.remove());
          const cleanText = clonedFragment.textContent;
          if (e.clipboardData && cleanText) {
            e.clipboardData.setData('text/plain', cleanText);
            e.preventDefault();
          }
        }
      } catch (err) {}
      setTimeout(updateToolbar, 80);
    });

    document.addEventListener('selectionchange', () => {
      const sel = window.getSelection();
      if (!sel || sel.isCollapsed) {
        if (!toolbar.classList.contains('hidden')) {
          toolbar.classList.add('hidden');
          toolbar.classList.remove('flex');
        }
      }
    });

    if (btnDict) {
      btnDict.addEventListener('click', (e) => {
        e.stopPropagation();
        if (currentSelectedExampleWord) {
          openDictLookupModal(currentSelectedExampleWord, currentSelectedExampleReading);
          toolbar.classList.add('hidden');
          toolbar.classList.remove('flex');
        }
      });
    }

    if (btnSave) {
      btnSave.addEventListener('click', (e) => {
        e.stopPropagation();
        if (currentSelectedExampleWord) {
          quickSaveExampleWordToMylist(currentSelectedExampleWord, currentSelectedExampleReading);
          toolbar.classList.add('hidden');
          toolbar.classList.remove('flex');
        }
      });
    }
  }

  // ==========================================
  // 日本語形態素 活用形復元（辞書形・原形）エンジン
  // ==========================================
  function deinflectJapaneseWord(word) {
    if (!word || typeof word !== 'string') return [];
    const clean = word.trim();
    if (!clean) return [];

    const candidates = [];
    const seen = new Set([clean]);

    function addCandidate(w, ruleName) {
      if (!w || typeof w !== 'string') return;
      const trimmed = w.trim();
      if (!trimmed || seen.has(trimmed)) return;
      seen.add(trimmed);
      candidates.push({ word: trimmed, rule: ruleName || '辞書形・原形' });
    }

    // 1. 接頭語の除去 (お・ご) と お〜連用形 の動詞・定型表現復元
    if ((clean.startsWith('お') || clean.startsWith('ご')) && clean.length >= 2) {
      const bare = clean.slice(1);
      addCandidate(bare, '接頭語除去');
      expandRenyoukei(bare); // お疲れ -> 疲れる, お待ち -> 待つ, お話し -> 話す
      if (clean === 'お疲れ' || clean === 'おつかれ') {
        addCandidate('お疲れ様', '定型表現');
        addCandidate('疲れる', '動詞・辞書形');
      }
      if (clean === 'お願い' || clean === 'おねがい') {
        addCandidate('お願いします', '定型表現');
        addCandidate('願う', '動詞・辞書形');
      }
    }

    // 2. 挨拶・丁寧語尾の除去 (様でした, でした, です, 様)
    const politeEndings = ['様でした', 'さまでした', 'でした', 'です', '様', 'さま'];
    for (const pe of politeEndings) {
      if (clean.endsWith(pe) && clean.length > pe.length) {
        const stem = clean.slice(0, -pe.length);
        addCandidate(stem, '丁寧語尾除去');
        if (stem.startsWith('お') || stem.startsWith('ご')) {
          const bare = stem.slice(1);
          addCandidate(bare, '接頭語除去');
          expandRenyoukei(bare);
        }
      }
    }

    // 3. 助詞・付属語の除去
    const particles = [
      'とか', 'など', 'より', 'から', 'まで', 'だけ', 'ほど', 'ばかり', 'くらい', 'ぐらい',
      'な', 'だ', 'に', 'を', 'の', 'が', 'は', 'で', 'と', 'へ', 'も', 'よ', 'ね', 'か'
    ];
    for (const p of particles) {
      if (clean.endsWith(p) && clean.length > p.length) {
        addCandidate(clean.slice(0, -p.length), '助詞除去');
      }
    }

    // 3. い形容詞 (新しく, 新しくて, 新しかった, 新しくない, 新しければ)
    const adjSuffixes = ['くなかった', 'かった', 'くない', 'くて', 'く', 'ければ'];
    for (const sfx of adjSuffixes) {
      if (clean.endsWith(sfx) && clean.length > sfx.length) {
        const stem = clean.slice(0, -sfx.length);
        addCandidate(stem + 'い', 'い形容詞・原形');
      }
    }

    // 4. な形容詞 (静かだ, 静かで, 静かな, 静かに)
    const naSuffixes = ['だった', 'ではない', 'じゃない', 'なら', 'だ', 'で', 'な', 'に'];
    for (const sfx of naSuffixes) {
      if (clean.endsWith(sfx) && clean.length > sfx.length) {
        addCandidate(clean.slice(0, -sfx.length), 'な形容詞・語幹');
      }
    }

    // 5. ます形 (丁寧語)
    const masuSuffixes = ['ませんでした', 'ましょう', 'ました', 'ません', 'ます'];
    for (const sfx of masuSuffixes) {
      if (clean.endsWith(sfx) && clean.length > sfx.length) {
        const stem = clean.slice(0, -sfx.length);
        addCandidate(stem, 'ます形語幹');
        expandRenyoukei(stem);
      }
    }

    // 6. 連用形そのものの判定 (例: はかどり、買い、話し、読み、調べ)
    const godanRenyouEnding = 'いきぎしちにびみり';
    const ichidanRenyouEnding = 'えけげせてねべめれいきぎしちにびみり';
    const lastChar = clean.slice(-1);
    if (godanRenyouEnding.includes(lastChar) || ichidanRenyouEnding.includes(lastChar)) {
      expandRenyoukei(clean);
    }

    function expandRenyoukei(stem) {
      if (!stem || stem.length < 1) return;
      const last = stem.slice(-1);
      const stemBase = stem.slice(0, -1);

      // 五段動詞の連用形 -> 終止形 (う段)
      const godanMap = {
        'い': 'う', // 買い -> 買う
        'き': 'く', // 行き -> 行く, 書き -> 書く
        'ぎ': 'ぐ', // 泳ぎ -> 泳ぐ, 急ぎ -> 急ぐ
        'し': 'す', // 話し -> 話す, 落とし -> 落とす
        'ち': 'つ', // 立ち -> 立つ, 待ち -> 待つ
        'に': 'ぬ', // 死に -> 死ぬ
        'び': 'ぶ', // 呼び -> 呼ぶ, 遊び -> 遊ぶ
        'み': 'む', // 読み -> 読む, 飲み -> 飲む, 進み -> 進む
        'り': 'る'  // はかどり -> はかどる, 作り -> 作る, 走り -> 走る
      };
      if (godanMap[last]) {
        addCandidate(stemBase + godanMap[last], '五段動詞・辞書形');
      }

      // 一段動詞の連用形 -> 終止形 (stem + る)
      addCandidate(stem + 'る', '一段動詞・辞書形');

      // サ変動詞 (stem + する)
      if (stem.endsWith('し')) {
        addCandidate(stem.slice(0, -1) + 'する', 'サ変動詞');
        addCandidate(stem.slice(0, -1), 'サ変名詞');
      }
    }

    // 7. て形・た形 (音便の復元)
    if (clean.endsWith('って') || clean.endsWith('った')) {
      const stem = clean.slice(0, -2);
      addCandidate(stem + 'る', '五段動詞(る)');
      addCandidate(stem + 'つ', '五段動詞(つ)');
      addCandidate(stem + 'う', '五段動詞(う)');
      addCandidate(stem + 'く', '五段動詞(く/行く)');
    } else if (clean.endsWith('いて') || clean.endsWith('いた')) {
      const stem = clean.slice(0, -2);
      addCandidate(stem + 'く', '五段動詞(く)');
    } else if (clean.endsWith('いで') || clean.endsWith('いだ')) {
      const stem = clean.slice(0, -2);
      addCandidate(stem + 'ぐ', '五段動詞(ぐ)');
    } else if (clean.endsWith('して') || clean.endsWith('した')) {
      const stem = clean.slice(0, -2);
      addCandidate(stem + 'す', '五段動詞(す)');
      addCandidate(stem + 'する', 'サ変動詞(する)');
      addCandidate(stem, 'サ変名詞');
    } else if (clean.endsWith('んで') || clean.endsWith('んだ')) {
      const stem = clean.slice(0, -2);
      addCandidate(stem + 'む', '五段動詞(む)');
      addCandidate(stem + 'ぶ', '五段動詞(ぶ)');
      addCandidate(stem + 'ぬ', '五段動詞(ぬ)');
    } else if (clean.endsWith('て') || clean.endsWith('た')) {
      const stem = clean.slice(0, -1);
      addCandidate(stem + 'る', '一段動詞・辞書形');
    }

    // 8. ない形・否定形 (未然形)
    const naiSuffixes = ['なかった', 'なくて', 'ない', 'ず', 'ぬ'];
    for (const sfx of naiSuffixes) {
      if (clean.endsWith(sfx) && clean.length > sfx.length) {
        const stem = clean.slice(0, -sfx.length);
        addCandidate(stem + 'る', '一段動詞(ない形)');
        const mizenMap = {
          'わ': 'う', 'か': 'く', 'が': 'ぐ', 'さ': 'す',
          'た': 'つ', 'な': 'ぬ', 'ば': 'ぶ', 'ま': 'む', 'ら': 'る'
        };
        const last = stem.slice(-1);
        if (mizenMap[last]) {
          addCandidate(stem.slice(0, -1) + mizenMap[last], '五段動詞(ない形)');
        }
      }
    }

    // 9. サ変動詞
    if (clean.endsWith('する') && clean.length > 2) {
      addCandidate(clean.slice(0, -2), 'サ変名詞');
    }
    if (clean.endsWith('できる') && clean.length > 3) {
      addCandidate(clean.slice(0, -3) + 'する', 'サ変動詞');
      addCandidate(clean.slice(0, -3), 'サ変名詞');
    }

    // 10. カ変動詞
    if (['来ます', '来て', '来た', '来ない', 'こない', 'きたり', 'きた'].includes(clean)) {
      addCandidate('来る', 'カ変動詞');
    }

    return candidates;
  }

  // 辞書データベースの品詞コード記号（[vg], [n], [v5r] 等）を除去してきれいに整形
  function cleanDefinitionText(str) {
    if (!str || typeof str !== 'string') return '';
    return str
      .replace(/\[[a-z0-9|\-]+\]/gi, ' ')
      .replace(/\s+/g, ' ')
      .trim();
  }

  // 辞書データの兄弟エントリ（漢字表記とかな表記のペア）から不足している訳文・レベルを相互補完
  function enrichDictEntry(d) {
    if (!d) return d;
    const w = d.w || '';
    const r = d.r || '';
    let zh = (d.zh && d.zh.length) ? [...d.zh] : [];
    let fr = (d.fr && d.fr.length) ? [...d.fr] : [];
    let m = (d.m && d.m.length) ? [...d.m] : [];
    let l = d.l || '';

    if (window.DICT_DATA && Array.isArray(window.DICT_DATA)) {
      let sibling = null;
      if (r) {
        sibling = window.DICT_DATA.find(x => x.w === r && (x.zh?.length || x.fr?.length || x.l));
      } else if (w) {
        sibling = window.DICT_DATA.find(x => x.r === w && (x.zh?.length || x.fr?.length || x.l));
      }
      if (sibling) {
        if (!zh.length && sibling.zh?.length) zh = [...sibling.zh];
        if (!fr.length && sibling.fr?.length) fr = [...sibling.fr];
        if (!l && sibling.l) l = sibling.l;
        if (m.length <= 1 && sibling.m?.length > m.length) m = [...sibling.m];
      }
    }
    return { ...d, w, r, zh, fr, m, l };
  }

  // オンライン辞書（Google翻訳API + ウィクショナリーREST API）から語義を取得
  async function fetchOnlineDictionaryDefinition(query) {
    if (!query) return null;
    const clean = query.trim();
    if (!clean) return null;
    const enc = encodeURIComponent(clean);

    try {
      const tlEnUrl = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=ja&tl=en&dt=t&q=${enc}`;
      const tlZhUrl = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=ja&tl=zh-TW&dt=t&q=${enc}`;
      const tlFrUrl = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=ja&tl=fr&dt=t&q=${enc}`;
      const tlKoUrl = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=ja&tl=ko&dt=t&q=${enc}`;
      const wikUrl = `https://ja.wiktionary.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=${enc}&format=json&origin=*`;

      const [enRes, zhRes, frRes, koRes, wikRes] = await Promise.allSettled([
        fetch(tlEnUrl).then(r => r.json()),
        fetch(tlZhUrl).then(r => r.json()),
        fetch(tlFrUrl).then(r => r.json()),
        fetch(tlKoUrl).then(r => r.json()),
        fetch(wikUrl).then(r => r.json())
      ]);

      function parseTranslate(res) {
        if (res.status === 'fulfilled' && res.value && res.value[0] && Array.isArray(res.value[0])) {
          return res.value[0].map(item => item[0]).filter(Boolean).join(' ').trim();
        }
        return '';
      }

      const enText = parseTranslate(enRes);
      const zhText = parseTranslate(zhRes);
      const frText = parseTranslate(frRes);
      const koText = parseTranslate(koRes);

      let jaExplain = '';
      if (wikRes.status === 'fulfilled' && wikRes.value?.query?.pages) {
        const pages = wikRes.value.query.pages;
        for (const pid in pages) {
          if (pid !== '-1' && pages[pid].extract) {
            const rawExt = pages[pid].extract;
            const lines = rawExt.split('\n')
              .map(l => l.trim())
              .filter(l => l && !l.startsWith('=') && !l.includes('青空文庫') && !l.includes('閲覧。'));
            jaExplain = lines.slice(0, 3).join(' ');
            break;
          }
        }
      }

      return {
        en: enText || clean,
        zh_TW: zhText || enText || clean,
        zh_CN: zhText || enText || clean,
        ko: koText || enText || clean,
        fr: frText || enText || clean,
        ja: jaExplain || ''
      };
    } catch (err) {
      console.warn('Online dictionary lookup error:', err);
      return null;
    }
  }

  // なぞった単語をワンタップでマイリストに追加（またはフォルダ選択）
  function quickSaveExampleWordToMylist(word, hintReading) {
    const cleanWord = sanitizeSelectedWordText(word);
    if (!cleanWord) return;

    // 1. 既存カード・辞書を直接探索
    let card = vocabList.find(c => c.word === cleanWord || c.id === cleanWord);
    if (!card) {
      card = getMylistCards().find(c => c.word === cleanWord || c.id === cleanWord);
    }
    if (!card && window.CLASS_VOCAB_DATA) {
      const classCard = window.CLASS_VOCAB_DATA.find(c => c.word === cleanWord);
      if (classCard) {
        card = {
          ...classCard,
          id: `custom_ex_${cleanWord}_${Date.now()}`,
          category: '例文から保存',
          section_title: '例文から保存した単語'
        };
      }
    }
    if (!card && window.DICT_DATA) {
      const rawEntry = window.DICT_DATA.find(d => d.w === cleanWord || (d.r && d.r === cleanWord));
      if (rawEntry) {
        const entry = enrichDictEntry(rawEntry);
        card = {
          id: `dict_${entry.w}_${Date.now()}`,
          word: entry.w,
          reading: entry.r || hintReading || entry.w,
          category: entry.category || (entry.l ? `JLPT ${entry.l}` : '辞書'),
          section_title: '例文から保存した単語',
          meaning: {
            en: (entry.m && entry.m.map(cleanDefinitionText).join(', ')) || '—',
            zh_TW: (entry.zh && entry.zh.map(cleanDefinitionText).join(', ')) || (entry.m && entry.m.map(cleanDefinitionText).join(', ')) || '—',
            zh_CN: (entry.zh_CN && entry.zh_CN.map(cleanDefinitionText).join(', ')) || (entry.zh && entry.zh.map(cleanDefinitionText).join(', ')) || (entry.m && entry.m.map(cleanDefinitionText).join(', ')) || '—',
            ko: (entry.ko && entry.ko.map(cleanDefinitionText).join(', ')) || (entry.m && entry.m.map(cleanDefinitionText).join(', ')) || '—',
            fr: (entry.fr && entry.fr.map(cleanDefinitionText).join(', ')) || (entry.m && entry.m.map(cleanDefinitionText).join(', ')) || '—'
          }
        };
      }
    }

    // 2. 直接見つからなければ活用形（辞書形・語幹）から探索
    if (!card) {
      const lemmas = deinflectJapaneseWord(cleanWord);
      for (const lm of lemmas) {
        const lw = lm.word;
        card = vocabList.find(c => c.word === lw || (c.reading && c.reading === lw));
        if (card) break;
        card = getMylistCards().find(c => c.word === lw || (c.reading && c.reading === lw));
        if (card) break;
        if (window.CLASS_VOCAB_DATA) {
          const classCard = window.CLASS_VOCAB_DATA.find(c => c.word === lw || (c.reading && c.reading === lw));
          if (classCard) {
            card = {
              ...classCard,
              id: `custom_ex_${classCard.word}_${Date.now()}`,
              category: '例文から保存',
              section_title: '例文から保存した単語'
            };
            break;
          }
        }
        if (window.DICT_DATA) {
          const rawEntry = window.DICT_DATA.find(d => d.w === lw || (d.r && d.r === lw));
          if (rawEntry) {
            const entry = enrichDictEntry(rawEntry);
            card = {
              id: `dict_${entry.w}_${Date.now()}`,
              word: entry.w,
              reading: entry.r || (entry.w === lw ? '' : lw),
              category: entry.category || (entry.l ? `JLPT ${entry.l}` : '辞書'),
              section_title: '例文から保存した単語',
              meaning: {
                en: (entry.m && entry.m.map(cleanDefinitionText).join(', ')) || '—',
                zh_TW: (entry.zh && entry.zh.map(cleanDefinitionText).join(', ')) || (entry.m && entry.m.map(cleanDefinitionText).join(', ')) || '—',
                zh_CN: (entry.zh_CN && entry.zh_CN.map(cleanDefinitionText).join(', ')) || (entry.zh && entry.zh.map(cleanDefinitionText).join(', ')) || (entry.m && entry.m.map(cleanDefinitionText).join(', ')) || '—',
                ko: (entry.ko && entry.ko.map(cleanDefinitionText).join(', ')) || (entry.m && entry.m.map(cleanDefinitionText).join(', ')) || '—',
                fr: (entry.fr && entry.fr.map(cleanDefinitionText).join(', ')) || (entry.m && entry.m.map(cleanDefinitionText).join(', ')) || '—'
              }
            };
            break;
          }
        }
      }
    }

    // 3. 辞書にもなければ新規単語として構成
    if (!card) {
      card = {
        id: `custom_ex_${cleanWord}_${Date.now()}`,
        word: cleanWord,
        reading: hintReading || cleanWord,
        category: '例文から保存',
        section_title: '例文から保存した単語',
        meaning: {
          en: cleanWord,
          zh_TW: cleanWord,
          zh_CN: cleanWord,
          ko: cleanWord,
          fr: cleanWord
        }
      };
    }

    // フォルダ選択モーダルを開いて保存
    promptFolderSelectAndAdd(card, () => {
      updateMylistBadge();
      renderCurrentCard();
    });
  }

  // 単語辞書検索 ＆ 詳細モーダル (活用形復元・形態素優先・オンライン辞書連携)
  function openDictLookupModal(queryWord, hintReading) {
    if (!queryWord) return;
    const cleanWord = sanitizeSelectedWordText(queryWord);
    if (!cleanWord) return;

    const modal = document.getElementById('dictPopupModal');
    const content = document.getElementById('dictPopupModalContent');
    if (!modal || !content) return;

    // --- 1. 形態素・活用形復元リストの生成 ---
    const lemmas = deinflectJapaneseWord(cleanWord);
    const lemmaMap = new Map(); // word -> ruleName
    lemmas.forEach(l => {
      if (!lemmaMap.has(l.word)) lemmaMap.set(l.word, l.rule);
    });
    const lemmaWords = Array.from(lemmaMap.keys());

    // 漢字部分文字列（例: 「10分以上」→「以上」のように漢字が複数連続する場合のみ）
    const kanjiSubWords = [];
    const kanjiMatches = cleanWord.match(/[\u4e00-\u9fff]{2,}/g) || [];
    kanjiMatches.forEach(km => {
      if (km !== cleanWord && !kanjiSubWords.includes(km)) {
        kanjiSubWords.push(km);
      }
    });

    // 漢字1文字リスト
    const singleKanjiList = Array.from(new Set(cleanWord.match(/[\u4e00-\u9fff]/g) || []));

    // --- 2. カリキュラム単語 ＋ マイリスト単語の検索 ---
    let matchedCurriculumCards = [];
    const lookupPool = [...vocabList];
    const poolIds = new Set(vocabList.map(c => c.id));
    getMylistCards().forEach(mc => {
      if (mc && !poolIds.has(mc.id)) {
        lookupPool.push(mc);
        poolIds.add(mc.id);
      }
    });

    lookupPool.forEach(c => {
      let score = 0;
      let matchType = '';
      const w = c.word || '';
      const r = c.reading || '';

      if (w === cleanWord) {
        score = 10000;
        matchType = '完全一致';
      } else if (r && r === cleanWord) {
        score = 9500;
        matchType = '読み完全一致';
      } else if (lemmaMap.has(w)) {
        score = 9000;
        matchType = lemmaMap.get(w);
      } else if (r && lemmaMap.has(r)) {
        score = 8500;
        matchType = lemmaMap.get(r);
      } else if (w.startsWith(cleanWord)) {
        score = 5000 - w.length * 10;
        matchType = '前方一致';
      } else if (w.includes(cleanWord)) {
        score = 3000 - w.length * 10;
        matchType = '部分一致';
      }

      if (score > 0) {
        matchedCurriculumCards.push({ card: c, score, matchType, targetWord: w });
      }
    });
    matchedCurriculumCards.sort((a, b) => b.score - a.score);

    // --- 3. DICT_DATA (日本語大辞書 68,000語) からの検索 ---
    let dictScoredMatches = [];
    const seenDictKeys = new Set();
    const lvlScoreMap = { 'N5': 80, 'N4': 60, 'N3': 40, 'N2': 20, 'N1': 10 };

    if (window.DICT_DATA && Array.isArray(window.DICT_DATA)) {
      for (const rawD of window.DICT_DATA) {
        const w = rawD.w || '';
        const r = rawD.r || '';
        const key = `${w}_${r}`;
        if (seenDictKeys.has(key)) continue;

        let score = 0;
        let matchType = '';

        if (w === cleanWord) {
          score = 10000;
          matchType = '完全一致';
        } else if (r && r === cleanWord) {
          score = 9500;
          matchType = '読み完全一致';
        } else if (lemmaMap.has(w)) {
          score = 9000;
          matchType = lemmaMap.get(w);
        } else if (r && lemmaMap.has(r)) {
          score = 8500;
          matchType = lemmaMap.get(r);
        } else if (w.startsWith(cleanWord) && cleanWord.length >= 2) {
          score = 5000 - w.length * 10;
          matchType = '前方一致';
        } else if (w.includes(cleanWord) && cleanWord.length >= 2) {
          score = 3000 - w.length * 10;
          matchType = '部分一致';
        }

        if (score > 0) {
          score += (lvlScoreMap[rawD.l] || 0);
          if (hintReading && r === hintReading) score += 500;
          seenDictKeys.add(key);
          dictScoredMatches.push({ item: enrichDictEntry(rawD), score, matchType, targetWord: w });
        }
      }
      dictScoredMatches.sort((a, b) => b.score - a.score);
    }

    // --- 4. 最高スコアが不十分（未検出）の場合のみ漢字複合語・漢字1文字でフォールバック ---
    const highestCurriculumScore = matchedCurriculumCards[0]?.score || 0;
    const highestDictScore = dictScoredMatches[0]?.score || 0;
    const maxScore = Math.max(highestCurriculumScore, highestDictScore);

    if (maxScore < 7000 && (kanjiSubWords.length > 0 || singleKanjiList.length > 0)) {
      if (window.DICT_DATA && Array.isArray(window.DICT_DATA)) {
        for (const rawD of window.DICT_DATA) {
          const w = rawD.w || '';
          const r = rawD.r || '';
          const key = `${w}_${r}`;
          if (seenDictKeys.has(key)) continue;

          let fbScore = 0;
          let fbType = '';

          for (const ksw of kanjiSubWords) {
            if (w === ksw) { fbScore = Math.max(fbScore, 2000 - w.length * 5); fbType = '関連語'; break; }
            else if (w.startsWith(ksw)) { fbScore = Math.max(fbScore, 1500 - w.length * 5); fbType = '関連語'; break; }
          }
          if (fbScore === 0) {
            for (const sk of singleKanjiList) {
              if (w.startsWith(sk)) { fbScore = Math.max(fbScore, 500 - w.length * 5); fbType = '関連漢字'; break; }
            }
          }

          if (fbScore > 0) {
            fbScore += (lvlScoreMap[rawD.l] || 0);
            seenDictKeys.add(key);
            dictScoredMatches.push({ item: enrichDictEntry(rawD), score: fbScore, matchType: fbType, targetWord: w });
          }
        }
        dictScoredMatches.sort((a, b) => b.score - a.score);
      }
    }

    // --- 5. 訳文取得用ヘルパー ---
    function formatDictMeaning(d) {
      const enriched = enrichDictEntry(d);
      const mList = (enriched.m || []).map(cleanDefinitionText).filter(Boolean).join(', ');
      const zhList = (enriched.zh || []).map(cleanDefinitionText).filter(Boolean).join(', ');
      const zhCnList = (enriched.zh_CN || enriched.zh || []).map(cleanDefinitionText).filter(Boolean).join(', ');
      const koList = (enriched.ko || []).map(cleanDefinitionText).filter(Boolean).join(', ');
      const frList = (enriched.fr || []).map(cleanDefinitionText).filter(Boolean).join(', ');

      let res = mList || '—';
      if (currentLang === 'zh_TW' || currentLang === 'zh_HK') {
        res = zhList || mList || '—';
      } else if (currentLang === 'zh_CN') {
        res = zhCnList || zhList || mList || '—';
      } else if (currentLang === 'fr') {
        res = frList || mList || '—';
      } else if (currentLang === 'ko') {
        res = koList || mList || '—';
      }

      if (d.note) {
        res += ` （※ ${d.note}）`;
      }
      return res;
    }

    // --- 6. トップ表示する単語カードの決定 ---
    let topWord = cleanWord;
    let topReading = hintReading || '';
    let topCategory = '辞書';
    let topMeaningText = '';
    let topCardForSave = null;
    let topMatchRule = '';
    let isNeedOnlineFetch = false;

    const bestCurriculum = matchedCurriculumCards[0];
    const bestDict = dictScoredMatches[0];

    if (bestCurriculum && bestCurriculum.score >= 8000) {
      const c = bestCurriculum.card;
      const isStarred = mylistSet.has(c.id) || mylistSet.has(c.word);
      topWord = c.word;
      topReading = c.reading || hintReading || '';
      let cat = c.category || '一般';
      if (cat === '授業で習った言葉' && !isStarred) cat = '辞書';
      topCategory = cat;
      topMeaningText = getBilingualMeaning(c.meaning, currentLang);
      topCardForSave = c;
      topMatchRule = bestCurriculum.matchType;
    } else if (bestDict && bestDict.score >= 8000) {
      const d = bestDict.item;
      topWord = d.w;
      topReading = d.r || hintReading || '';
      topCategory = d.category || (d.l ? `JLPT ${d.l}` : '辞書');
      topMeaningText = formatDictMeaning(d);
      topCardForSave = {
        id: `dict_${d.w}_${d.r || ''}`,
        word: d.w,
        reading: topReading,
        category: topCategory,
        meaning: {
          en: (d.m || []).map(cleanDefinitionText).join(', ') || '—',
          zh_TW: (d.zh || d.m || []).map(cleanDefinitionText).join(', ') || '—',
          zh_CN: (d.zh_CN || d.zh || d.m || []).map(cleanDefinitionText).join(', ') || '—',
          ko: (d.ko || d.m || []).map(cleanDefinitionText).join(', ') || '—',
          fr: (d.fr || d.m || []).map(cleanDefinitionText).join(', ') || '—'
        }
      };
      topMatchRule = bestDict.matchType;
    } else if (bestCurriculum) {
      const c = bestCurriculum.card;
      topWord = c.word;
      topReading = c.reading || hintReading || '';
      topCategory = c.category || '辞書';
      topMeaningText = getBilingualMeaning(c.meaning, currentLang);
      topCardForSave = c;
      topMatchRule = bestCurriculum.matchType || '関連語';
    } else if (bestDict) {
      const d = bestDict.item;
      topWord = d.w;
      topReading = d.r || hintReading || '';
      topCategory = d.category || (d.l ? `JLPT ${d.l}` : '辞書');
      topMeaningText = formatDictMeaning(d);
      topCardForSave = {
        id: `dict_${d.w}_${d.r || ''}`,
        word: d.w,
        reading: topReading,
        category: topCategory,
        meaning: {
          en: (d.m || []).map(cleanDefinitionText).join(', ') || '—',
          zh_TW: (d.zh || d.m || []).map(cleanDefinitionText).join(', ') || '—',
          zh_CN: (d.zh_CN || d.zh || d.m || []).map(cleanDefinitionText).join(', ') || '—',
          ko: (d.ko || d.m || []).map(cleanDefinitionText).join(', ') || '—',
          fr: (d.fr || d.m || []).map(cleanDefinitionText).join(', ') || '—'
        }
      };
      topMatchRule = bestDict.matchType || '関連語';
    } else {
      // 辞書・カリキュラム未登録の単語 -> オンライン辞書APIで自動取得
      topWord = cleanWord;
      topReading = hintReading || cleanWord;
      topCategory = '辞書 (Web連携)';
      topMeaningText = 'オンライン辞書・翻訳から検索中...';
      isNeedOnlineFetch = true;
      topCardForSave = {
        id: `custom_dict_${cleanWord}_${Date.now()}`,
        word: cleanWord,
        reading: topReading,
        category: '例文から保存',
        meaning: {
          en: cleanWord,
          zh_TW: cleanWord,
          zh_CN: cleanWord,
          ko: cleanWord,
          fr: cleanWord
        }
      };
    }

    const isAlreadySaved = mylistSet.has(topCardForSave.id) || mylistSet.has(topWord) || (topReading && mylistSet.has(topReading));

    // --- 7. 関連単語リスト（無関係な音片を排除し、真の派生語・関連語のみ選出） ---
    const relatedList = [];
    const usedWordKeys = new Set([topWord]);

    // 形態素・活用形の相方（例: 「はかどる」に対して「捗る」など）を優先追加
    lemmaWords.forEach(lm => {
      if (!usedWordKeys.has(lm) && window.DICT_DATA) {
        const sibling = window.DICT_DATA.find(d => d.w === lm || (d.r && d.r === lm));
        if (sibling && !usedWordKeys.has(sibling.w)) {
          usedWordKeys.add(sibling.w);
          const enr = enrichDictEntry(sibling);
          relatedList.push({
            word: enr.w,
            reading: enr.r || '',
            category: enr.l ? `JLPT ${enr.l}` : '辞書',
            badgeClass: enr.l ? 'bg-sky-100 text-sky-800' : 'bg-slate-100 text-slate-700',
            meaning: formatDictMeaning(enr),
            cardObj: {
              id: `dict_${enr.w}_${enr.r || ''}`,
              word: enr.w,
              reading: enr.r || '',
              category: enr.l ? `JLPT ${enr.l}` : '辞書',
              meaning: {
                en: (enr.m || []).map(cleanDefinitionText).join(', ') || '—',
                zh_TW: (enr.zh || enr.m || []).map(cleanDefinitionText).join(', ') || '—',
                zh_CN: (enr.zh || enr.m || []).map(cleanDefinitionText).join(', ') || '—',
                ko: (enr.m || []).map(cleanDefinitionText).join(', ') || '—',
                fr: (enr.fr || enr.m || []).map(cleanDefinitionText).join(', ') || '—'
              }
            }
          });
        }
      }
    });

    // カリキュラム単語のヒットを追加
    matchedCurriculumCards.forEach(mc => {
      if (!usedWordKeys.has(mc.card.word) && mc.score >= 3000 && relatedList.length < 8) {
        usedWordKeys.add(mc.card.word);
        const isStarred = mylistSet.has(mc.card.id) || mylistSet.has(mc.card.word);
        let cat = mc.card.category || '一般';
        if (cat === '授業で習った言葉' && !isStarred) cat = '辞書';
        relatedList.push({
          word: mc.card.word,
          reading: mc.card.reading || '',
          category: cat,
          badgeClass: (cat === '授業で習った言葉') ? 'bg-lightBlueBg text-deepNavy' : 'bg-rose-100 text-rose-800',
          meaning: getBilingualMeaning(mc.card.meaning, currentLang),
          cardObj: mc.card
        });
      }
    });

    // 辞書の高スコア語彙を追加（スコア3000以上＝接頭一致・重要語のみに厳選）
    dictScoredMatches.forEach(dm => {
      if (!usedWordKeys.has(dm.item.w) && dm.score >= 3000 && relatedList.length < 10) {
        usedWordKeys.add(dm.item.w);
        const d = dm.item;
        const meaning = formatDictMeaning(d);
        relatedList.push({
          word: d.w,
          reading: d.r || '',
          category: d.category || (d.l ? `JLPT ${d.l}` : '辞書'),
          badgeClass: d.category ? 'bg-pink-100 text-pink-800 border border-pink-200' : (d.l ? 'bg-sky-100 text-sky-800' : 'bg-slate-100 text-slate-700'),
          meaning: meaning,
          cardObj: {
            id: `dict_${d.w}_${d.r || ''}`,
            word: d.w,
            reading: d.r || '',
            category: d.category || (d.l ? `JLPT ${d.l}` : '辞書'),
            meaning: {
              en: (d.m || []).map(cleanDefinitionText).join(', ') || '—',
              zh_TW: (d.zh || d.m || []).map(cleanDefinitionText).join(', ') || '—',
              zh_CN: (d.zh_CN || d.zh || d.m || []).map(cleanDefinitionText).join(', ') || '—',
              ko: (d.ko || d.m || []).map(cleanDefinitionText).join(', ') || '—',
              fr: (d.fr || d.m || []).map(cleanDefinitionText).join(', ') || '—'
            }
          }
        });
      }
    });

    // --- 8. モーダルHTML生成 ---
    let headerNoticeHtml = '';
    if (topWord !== cleanWord) {
      if (topMatchRule && (topMatchRule.includes('辞書形') || topMatchRule.includes('動詞') || topMatchRule.includes('原形'))) {
        headerNoticeHtml = `
          <div class="px-3.5 py-2 rounded-xl bg-blue-50 border border-blue-200 text-blue-800 text-xs flex items-center justify-between shadow-2xs">
            <span>活用形 <strong>「${escapeHtml(cleanWord)}」</strong> の辞書形（原形）: <strong class="text-blue-900 font-bold font-jp">「${escapeHtml(topWord)}」</strong></span>
            <span class="text-[10px] font-bold bg-blue-600 text-white px-2 py-0.5 rounded-full shrink-0 ml-2">${escapeHtml(topMatchRule)}</span>
          </div>
        `;
      } else if (topMatchRule === '助詞除去') {
        headerNoticeHtml = `
          <div class="px-3.5 py-2 rounded-xl bg-blue-50 border border-blue-200 text-blue-800 text-xs flex items-center justify-between shadow-2xs">
            <span>助詞を除去: <strong>「${escapeHtml(cleanWord)}」</strong> → <strong class="text-blue-900 font-bold font-jp">「${escapeHtml(topWord)}」</strong></span>
            <span class="text-[10px] font-bold bg-blue-600 text-white px-2 py-0.5 rounded-full shrink-0 ml-2">助詞除去</span>
          </div>
        `;
      } else {
        headerNoticeHtml = `
          <div class="px-3.5 py-2 rounded-xl bg-amber-50 border border-amber-200 text-amber-800 text-xs flex items-center justify-between shadow-2xs">
            <span>選択: <strong>「${escapeHtml(cleanWord)}」</strong> に関連する単語: <strong class="text-amber-900 font-bold font-jp">「${escapeHtml(topWord)}」</strong></span>
            <span class="text-[10px] font-bold bg-amber-200/80 text-amber-900 px-2 py-0.5 rounded-md shrink-0 ml-2">関連検索</span>
          </div>
        `;
      }
    }

    let modalHtml = `
      ${headerNoticeHtml}

      <!-- メインヒット単語カード -->
      <div class="p-4 sm:p-5 rounded-2xl bg-sky-50/80 border border-sky-200 space-y-3 shadow-2xs">
        <div class="flex items-baseline justify-between flex-wrap gap-2">
          <div>
            <span class="text-[10px] sm:text-xs font-extrabold bg-sky-600 text-white px-2.5 py-0.5 rounded-full mr-1.5">${topCategory}</span>
            <span class="text-2xl sm:text-3xl font-black text-slate-900 font-jp">${escapeHtml(topWord)}</span>
            ${topReading && topReading !== topWord ? `<span class="text-sm sm:text-base font-bold text-coralPink ml-1.5 font-jp">【${escapeHtml(topReading)}】</span>` : ''}
          </div>
          <div class="flex items-center space-x-1.5">
            <button id="btnModalSpeakWord" class="p-2 sm:px-3 sm:py-2 rounded-xl bg-white border border-sky-200 text-sky-700 hover:bg-sky-100 transition shadow-2xs font-bold text-xs sm:text-sm flex items-center space-x-1" title="発音を聞く">
              <span>🔊</span>
              <span>発音</span>
            </button>
            <button id="btnModalSaveWord" class="px-3 py-2 rounded-xl font-bold text-xs sm:text-sm transition shadow-2xs flex items-center space-x-1 text-white ${isAlreadySaved ? 'bg-emerald-700 hover:bg-emerald-800' : 'bg-emerald-600 hover:bg-emerald-500'}" title="マイリストに保存">
              <span>${isAlreadySaved ? '✅' : '🔖'}</span>
              <span>${isAlreadySaved ? 'マイリスト保存中' : 'マイリストに追加'}</span>
            </button>
          </div>
        </div>

        <div class="pt-2 border-t border-sky-200/60 text-sm sm:text-base text-slate-700 leading-relaxed">
          <strong class="text-slate-900 block mb-0.5 text-xs sm:text-sm font-bold">意味・訳:</strong>
          <p id="dictModalMeaningText" class="font-bold text-slate-900 text-sm sm:text-base">${escapeHtml(topMeaningText)}</p>
        </div>

        ${isNeedOnlineFetch ? `
          <div id="dictOnlineStatusBox" class="mt-2 p-2.5 rounded-xl bg-sky-100/70 border border-sky-200 text-sky-800 text-xs flex items-center justify-between">
            <span id="dictOnlineStatusText" class="flex items-center space-x-1.5">
              <span class="inline-block animate-spin">⏳</span>
              <span>オンライン辞書・Web翻訳から解説を取得中...</span>
            </span>
            <span class="text-[10px] font-bold bg-sky-200 text-sky-800 px-2 py-0.5 rounded-md shrink-0">Web自動連携</span>
          </div>
        ` : ''}

        <!-- 外部辞書クイック検索リンク -->
        <div class="pt-1 flex items-center flex-wrap gap-2 text-xs">
          <a href="https://www.google.com/search?q=${encodeURIComponent(topWord + ' 意味')}" target="_blank" rel="noopener noreferrer" class="px-2.5 py-1 rounded-lg bg-white border border-slate-200 text-slate-600 hover:text-sky-700 hover:border-sky-300 font-bold transition flex items-center space-x-1 shadow-2xs">
            <span>🔍 Googleで調べる</span>
          </a>
          <a href="https://kotobank.jp/word/${encodeURIComponent(topWord)}" target="_blank" rel="noopener noreferrer" class="px-2.5 py-1 rounded-lg bg-white border border-slate-200 text-slate-600 hover:text-sky-700 hover:border-sky-300 font-bold transition flex items-center space-x-1 shadow-2xs">
            <span>📖 コトバンク</span>
          </a>
          <a href="https://ja.wiktionary.org/wiki/${encodeURIComponent(topWord)}" target="_blank" rel="noopener noreferrer" class="px-2.5 py-1 rounded-lg bg-white border border-slate-200 text-slate-600 hover:text-sky-700 hover:border-sky-300 font-bold transition flex items-center space-x-1 shadow-2xs">
            <span>📚 ウィクショナリー</span>
          </a>
        </div>
      </div>
    `;

    // 関連単語リストのレンダリング
    if (relatedList.length > 0) {
      modalHtml += `
        <div class="space-y-2 pt-1">
          <h4 class="text-xs sm:text-sm font-bold text-slate-700 flex items-center justify-between">
            <span class="flex items-center space-x-1">
              <span>📚</span>
              <span>「${escapeHtml(cleanWord)}」に関連する単語 (${relatedList.length}件)</span>
            </span>
            <span class="text-[10px] sm:text-xs text-slate-400 font-normal">タップで詳細表示</span>
          </h4>
          <div class="space-y-2 max-h-[42vh] overflow-y-auto pr-1">
            ${relatedList.map((rel, idx) => {
              const isRelSaved = mylistSet.has(rel.cardObj.id) || mylistSet.has(rel.word);
              return `
                <div class="rel-word-item p-3 rounded-xl bg-slate-50 border border-slate-200 flex items-center justify-between text-xs sm:text-sm hover:bg-blue-50/50 hover:border-sky-300 transition cursor-pointer shadow-2xs" data-idx="${idx}">
                  <div class="flex items-baseline space-x-2 truncate pr-2">
                    <span class="font-bold text-slate-900 text-sm sm:text-base font-jp">${escapeHtml(rel.word)}</span>
                    ${rel.reading ? `<span class="text-xs sm:text-sm text-coralPink font-bold font-jp">（${escapeHtml(rel.reading)}）</span>` : ''}
                    <span class="text-[9px] sm:text-[10px] px-1.5 py-0.5 rounded font-bold ${rel.badgeClass} shrink-0">${rel.category}</span>
                    <span class="text-xs sm:text-sm text-slate-600 ml-1 truncate font-medium">${escapeHtml(rel.meaning)}</span>
                  </div>
                  <div class="flex items-center space-x-1 shrink-0">
                    <button class="btn-sub-speak-word p-1.5 text-slate-400 hover:text-sky-600 rounded transition" title="発音を聞く" data-word="${escapeHtml(rel.word)}">
                      <span>🔊</span>
                    </button>
                    <button class="btn-sub-save-word px-2.5 py-1 rounded-lg border font-bold text-xs transition ${isRelSaved ? 'bg-emerald-100 border-emerald-400 text-emerald-800' : 'bg-white border-emerald-300 text-emerald-700 hover:bg-emerald-50'}"
                      data-idx="${idx}">
                      ${isRelSaved ? '✓ 保存中' : '🔖 保存'}
                    </button>
                  </div>
                </div>
              `;
            }).join('')}
          </div>
        </div>
      `;
    }

    content.innerHTML = modalHtml;

    // --- 9. 未登録単語のオンライン非同期辞書取得 ---
    if (isNeedOnlineFetch) {
      fetchOnlineDictionaryDefinition(cleanWord).then(onlineData => {
        const meaningEl = content.querySelector('#dictModalMeaningText');
        const statusBox = content.querySelector('#dictOnlineStatusBox');
        const statusText = content.querySelector('#dictOnlineStatusText');

        if (onlineData) {
          let displayText = '';
          if (currentLang === 'zh_TW' || currentLang === 'zh_HK') displayText = onlineData.zh_TW;
          else if (currentLang === 'zh_CN') displayText = onlineData.zh_CN;
          else if (currentLang === 'fr') displayText = onlineData.fr;
          else if (currentLang === 'ko') displayText = onlineData.ko;
          else displayText = onlineData.en;

          if (onlineData.ja) {
            displayText = `${displayText} (${onlineData.ja})`;
          }

          if (meaningEl) meaningEl.textContent = displayText || '日本語表現・単語';
          topCardForSave.meaning = {
            en: onlineData.en || cleanWord,
            zh_TW: onlineData.zh_TW || cleanWord,
            zh_CN: onlineData.zh_CN || cleanWord,
            ko: onlineData.ko || cleanWord,
            fr: onlineData.fr || cleanWord
          };

          if (statusBox) {
            statusBox.className = 'mt-2 p-2 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-800 text-xs flex items-center justify-between';
            if (statusText) statusText.innerHTML = '<span>✅ オンライン辞書から解説を取得しました</span>';
          }
        } else {
          if (statusBox) {
            statusBox.className = 'mt-2 p-2 rounded-xl bg-amber-50 border border-amber-200 text-amber-800 text-xs flex items-center justify-between';
            if (statusText) statusText.innerHTML = '<span>辞書に見つかりませんでした。下のGoogleまたはコトバンクで検索できます。</span>';
          }
        }
      });
    }

    // --- 10. イベントリスナーの接続 ---
    const btnSpeak = content.querySelector('#btnModalSpeakWord');
    if (btnSpeak) {
      btnSpeak.addEventListener('click', () => {
        toggleJapaneseSpeech(topWord);
      });
    }

    const btnSave = content.querySelector('#btnModalSaveWord');
    if (btnSave) {
      btnSave.addEventListener('click', () => {
        promptFolderSelectAndAdd(topCardForSave, () => {
          updateMylistBadge();
          renderCurrentCard();
          openDictLookupModal(queryWord, hintReading); // モーダル内のボタン表示を更新
        });
      });
    }

    // 関連単語クリックでその単語の詳細をモーダルで開く
    content.querySelectorAll('.rel-word-item').forEach(item => {
      item.addEventListener('click', (e) => {
        if (e.target.closest('button')) return;
        const idx = parseInt(item.getAttribute('data-idx'), 10);
        const targetRel = relatedList[idx];
        if (targetRel) {
          openDictLookupModal(targetRel.word, targetRel.reading);
        }
      });
    });

    // 関連単語の発音ボタン
    content.querySelectorAll('.btn-sub-speak-word').forEach(spkBtn => {
      spkBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        const sw = spkBtn.getAttribute('data-word');
        if (sw) toggleJapaneseSpeech(sw);
      });
    });

    // 関連単語の保存ボタン
    content.querySelectorAll('.btn-sub-save-word').forEach(subBtn => {
      subBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        const idx = parseInt(subBtn.getAttribute('data-idx'), 10);
        const targetRel = relatedList[idx];
        if (!targetRel) return;

        promptFolderSelectAndAdd(targetRel.cardObj, () => {
          updateMylistBadge();
          renderCurrentCard();
          openDictLookupModal(queryWord, hintReading);
        });
      });
    });

    modal.classList.remove('hidden');
    modal.classList.add('flex');
  }

  function closeDictPopupModal() {
    const modal = document.getElementById('dictPopupModal');
    if (modal) {
      modal.classList.add('hidden');
      modal.classList.remove('flex');
    }
  }

  // --- スワイプ操作ガイド ポップアップ (スマホ版案内) ---
  function openSwipeGuideModal() {
    const modal = document.getElementById('swipeGuideModal');
    if (modal) {
      modal.classList.remove('hidden');
      modal.classList.add('flex');
    }
  }

  function closeSwipeGuideModal() {
    const modal = document.getElementById('swipeGuideModal');
    if (modal) {
      modal.classList.add('hidden');
      modal.classList.remove('flex');
    }
    sessionStorage.setItem('haku_swipe_guide_shown', 'true');
  }

  function checkAndShowSwipeGuide(force = false) {
    if (!isTabletOrDesktop()) {
      const alreadyShown = sessionStorage.getItem('haku_swipe_guide_shown');
      if (!alreadyShown || force) {
        openSwipeGuideModal();
      }
    }
  }

  window.openSwipeGuideModal = openSwipeGuideModal;
  window.closeSwipeGuideModal = closeSwipeGuideModal;
  window.checkAndShowSwipeGuide = checkAndShowSwipeGuide;

  // ==========================================
  // --- 使い方ガイド (Help Guide) スライド式コントローラー ---
  // ==========================================
  let currentHelpGuideSlideIndex = 0;

  const HELP_GUIDE_SLIDES = [
    {
      id: 'search',
      badge: { ja: 'ステップ 1 / 検索', en: 'Step 1 / Search' },
      title: { ja: '🔍 検索窓で探してマイリストへ追加', en: 'Search & Add to My List' },
      subtitle: {
        ja: '上部の検索バーに日本語（漢字・ひらがな・ローマ字）や母国語を入力するだけで、瞬時に目的の単語が見つかります。',
        en: 'Type Japanese (kanji, hiragana, romaji) or your native language in the top search bar to find words instantly.'
      },
      diagramHtml: `
        <div class="rounded-2xl bg-gradient-to-br from-slate-50 to-sky-50 border border-sky-100 p-3 shadow-inner space-y-2.5">
          <!-- 検索バーのイラスト風UI -->
          <div class="flex items-center space-x-2 bg-deepNavy text-white px-3 py-2 rounded-full shadow-sm">
            <span class="text-xs">🔍</span>
            <span class="text-[11px] font-mono text-white/90 bg-white/20 px-2 py-0.5 rounded-full font-bold">ねこ / cat / 猫</span>
            <span class="text-[10px] text-white/60 ml-auto">母国語・日本語OK</span>
          </div>
          <!-- 検索結果のカード例 -->
          <div class="bg-white rounded-xl p-2.5 border border-slate-200 shadow-2xs flex items-center justify-between">
            <div>
              <div class="flex items-baseline space-x-1.5">
                <span class="text-sm font-black text-slate-800">猫</span>
                <span class="text-[11px] font-bold text-deepNavy">（ねこ）</span>
              </div>
              <p class="text-[10px] text-slate-500 font-medium">cat / 猫咪 / 고양이</p>
            </div>
            <!-- アクションボタン -->
            <div class="flex items-center space-x-1">
              <span class="text-[10px] font-bold px-2 py-1 rounded-lg bg-amber-50 border border-amber-300 text-amber-700 flex items-center space-x-0.5 shadow-2xs">
                <span>⭐</span>
                <span>マイリスト追加</span>
              </span>
            </div>
          </div>
        </div>
      `,
      tips: {
        ja: '💡 漢字一文字や「〜の時」のような語句でも、関連する単語を自動的に探してくれます！',
        en: '💡 Search works with single kanji, phrases, or grammar patterns too!'
      }
    },
    {
      id: 'swipe_marking',
      badge: { ja: 'ステップ 2 / 復習管理', en: 'Step 2 / Review & Learn' },
      title: { ja: '🔄 「覚えた！」と「もう一回」に仕分け', en: 'Sort into "Learned" & "Review"' },
      subtitle: {
        ja: 'カードをめくって学習したら、理解度に合わせて仕分け。スマホ版は左右のスワイプ操作で直感的に仕分けできます！',
        en: 'After flipping the card, sort it. On smartphones, easily swipe left or right!'
      },
      diagramHtml: `
        <div class="rounded-2xl bg-gradient-to-br from-rose-50/50 via-white to-emerald-50/50 border border-slate-200 p-3 shadow-inner space-y-3">
          <!-- スマホスワイプジェスチャーの図解 -->
          <div class="relative bg-white rounded-2xl border-2 border-dashed border-slate-300 p-3 text-center shadow-xs overflow-hidden">
            <div class="text-[11px] font-extrabold text-slate-400 mb-1">📱 スマホ版スワイプ操作</div>
            <div class="flex items-center justify-between px-2">
              <!-- 左スワイプ -->
              <div class="flex flex-col items-center">
                <span class="text-lg">👈</span>
                <span class="text-[10px] font-black px-2 py-0.5 rounded-full bg-rose-100 text-coralPink border border-rose-200 mt-0.5">左: もう一回！</span>
              </div>
              <!-- 中央カード -->
              <div class="w-20 py-2 rounded-xl bg-deepNavy text-white text-[11px] font-bold shadow-md">
                単語カード
              </div>
              <!-- 右スワイプ -->
              <div class="flex flex-col items-center">
                <span class="text-lg">👉</span>
                <span class="text-[10px] font-black px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 border border-emerald-200 mt-0.5">右: 覚えた！</span>
              </div>
            </div>
          </div>
          <!-- PC版ボタンの図解 -->
          <div class="flex items-center justify-center space-x-3 text-xs">
            <span class="px-3 py-1 rounded-xl bg-white border border-rose-200 text-coralPink font-extrabold shadow-2xs">
              🔁 もう一度！
            </span>
            <span class="text-[10px] text-slate-400 font-bold">PC版はボタンをクリック</span>
            <span class="px-3 py-1 rounded-xl bg-deepNavy text-white font-extrabold shadow-2xs">
              ✨ 覚えた！
            </span>
          </div>
        </div>
      `,
      tips: {
        ja: '💡 仕分けた単語はマイリストの『覚えた！』『もう一度！』フォルダに自動保存されます。',
        en: '💡 Words are automatically saved to your "Learned" and "Review" folders.'
      }
    },
    {
      id: 'dict_card',
      badge: { ja: 'ステップ 3 / 辞書機能', en: 'Step 3 / Dictionary' },
      title: { ja: '📖 充実の辞書で言葉を深く理解', en: 'Rich Built-in Dictionary' },
      subtitle: {
        ja: '検索結果や単語カードをタップすると「辞書カード」が開きます。正確なふりがな・音声・母国語訳・実践的な会話例文・関連語までまとめて学べます！',
        en: 'Tap any search result or card to open the Dictionary Card. Check accurate furigana, audio playback, native translations, real dialogues, and related words!'
      },
      diagramHtml: (isJa) => `
        <div class="rounded-2xl bg-gradient-to-br from-sky-50/70 via-indigo-50/50 to-purple-50/70 border border-sky-200 p-2.5 sm:p-3 shadow-inner space-y-2">
          <!-- 辞書カードのモックアップ -->
          <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-2.5 sm:p-3 space-y-2">
            <!-- 単語ヘッダー -->
            <div class="flex items-center justify-between pb-1.5 border-b border-slate-100">
              <div>
                <ruby class="text-base sm:text-lg font-black text-slate-900 font-jp">図書館<rt class="text-coralPink font-bold text-[10px]">としょかん</rt></ruby>
                <span class="text-[9px] font-black px-1.5 py-0.5 rounded bg-teal-50 text-teal-700 border border-teal-200 ml-1.5">N5</span>
              </div>
              <!-- 発音ボタン -->
              <span class="px-2 py-0.5 rounded-full bg-deepNavy text-white text-[10px] font-bold flex items-center space-x-0.5 shadow-2xs">
                <span>🔊</span>
                <span>${isJa ? '発音' : 'Audio'}</span>
              </span>
            </div>

            <!-- 意味（多言語対応） -->
            <div class="space-y-0.5">
              <span class="text-[9px] font-black uppercase tracking-wider text-slate-400 block">${isJa ? '意味・母国語訳' : 'Meaning / Native'}</span>
              <p class="text-xs font-bold text-slate-800">
                library / 圖書館 / 图书馆 / 도서관 / bibliothèque
              </p>
            </div>

            <!-- 会話例文 -->
            <div class="bg-slate-50 rounded-xl p-2 border border-slate-200/80 space-y-0.5">
              <span class="text-[9px] font-bold text-slate-400 block">${isJa ? '会話例文と対訳' : 'Real Dialogue & Translation'}</span>
              <p class="text-[11px] font-bold text-slate-800 leading-tight font-jp">
                A: 明日、図書館へ行きませんか？<br/>
                B: いいですね、一緒に行きましょう！
              </p>
              <p class="text-[9px] text-slate-500 font-medium leading-tight">
                A: Shall we go to the library tomorrow? B: Sounds great, let's go together!
              </p>
            </div>

            <!-- 関連語 ＆ マイリスト追加ボタン -->
            <div class="flex items-center justify-between pt-0.5">
              <div class="text-[10px] text-slate-600 flex items-center space-x-1">
                <span class="font-bold text-slate-400">${isJa ? '関連:' : 'Related:'}</span>
                <span class="bg-slate-100 px-1.5 py-0.2 rounded text-[9px] font-medium text-slate-700">本（ほん）</span>
                <span class="bg-slate-100 px-1.5 py-0.2 rounded text-[9px] font-medium text-slate-700">読書</span>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-amber-500 text-white font-extrabold text-[10px] shadow-2xs flex items-center space-x-0.5">
                <span>⭐</span>
                <span>${isJa ? 'マイリストに保存' : 'Save to List'}</span>
              </span>
            </div>
          </div>
        </div>
      `,
      tips: {
        ja: '💡 動詞の活用形（「行った」「食べた」「待って」）でも自動で元の辞書形（行く・食べる・待つ）を判定して表示してくれます！',
        en: '💡 Automatically recognizes conjugated verbs (e.g. 行った, 食べた) and finds their base dictionary forms!'
      }
    },
    {
      id: 'dict_lookup',
      badge: { ja: 'ステップ 4 / 例文検索', en: 'Step 4 / Sentence Lookup' },
      title: { ja: '🔍 例文の言葉をなぞって辞書へ', en: 'Lookup & Save from Sentences' },
      subtitle: {
        ja: '例文の中で知らない単語や漢字があったら、指やマウスで選択（なぞる）だけですぐにツールバーが出現！辞書で調べたりマイリストへ即保存できます。',
        en: 'Highlight any unknown word or kanji in the example sentence to lookup and save instantly!'
      },
      diagramHtml: (isJa) => `
        <div class="rounded-2xl bg-gradient-to-br from-sky-50 to-indigo-50 border border-sky-200 p-2.5 sm:p-3 shadow-inner space-y-2.5">
          <!-- 選択ツールバーのイラスト風再現 -->
          <div class="bg-white rounded-xl p-2.5 border border-slate-200 shadow-2xs">
            <p class="text-xs text-slate-700 leading-relaxed font-jp">
              明日、友達と<span class="bg-sky-200 text-sky-900 font-bold px-1 rounded shadow-xs">図書館</span>へ行きます。
            </p>
          </div>
          <!-- ツールバーの吹き出し -->
          <div class="flex items-center justify-center space-x-1.5 bg-slate-900 text-white px-3 py-1.5 rounded-xl shadow-lg border border-slate-700 text-xs">
            <span class="font-extrabold text-sky-400 text-[11px] font-jp">図書館</span>
            <span class="px-2 py-0.5 rounded-lg bg-sky-600 font-bold text-[10px] flex items-center space-x-0.5 shadow-2xs">
              <span>🔍</span>
              <span>${isJa ? '辞書で調べる' : 'Lookup'}</span>
            </span>
            <span class="px-2 py-0.5 rounded-lg bg-emerald-600 font-bold text-[10px] flex items-center space-x-0.5 shadow-2xs">
              <span>🔖</span>
              <span>${isJa ? '保存' : 'Save'}</span>
            </span>
          </div>
        </div>
      `,
      tips: {
        ja: '💡 なぞった単語から辞書を開いて詳しい例文を確認でき、例文中の単語も次々と調べられます！',
        en: '💡 Lookup words from any sentence and add them to your My List in one tap!'
      }
    },
    {
      id: 'custom_folders',
      badge: { ja: 'ステップ 5 / 整理', en: 'Step 5 / Folders' },
      title: { ja: '📁 フォルダを自由に作成して整理', en: 'Create Custom Folders' },
      subtitle: {
        ja: '「旅行用」「苦手な漢字」「第5課復習」など、自分で好きなフォルダを作って単語を自由にまとめられます。',
        en: 'Organize words into your own custom folders like "Travel", "Tricky Kanji", or "Lesson 5".'
      },
      diagramHtml: `
        <div class="rounded-2xl bg-gradient-to-br from-amber-50/60 to-orange-50/60 border border-amber-200 p-3 shadow-inner space-y-2">
          <!-- フォルダ作成ヘッダー -->
          <div class="flex items-center justify-between bg-white px-3 py-1.5 rounded-xl border border-amber-200 shadow-2xs">
            <span class="text-xs font-bold text-amber-900 flex items-center space-x-1">
              <span>📁</span>
              <span>マイリストのフォルダ</span>
            </span>
            <span class="text-[10px] font-black px-2 py-0.5 rounded-full bg-deepNavy text-white shadow-2xs">
              ＋ フォルダ作成
            </span>
          </div>
          <!-- フォルダタグ一覧例 -->
          <div class="grid grid-cols-3 gap-1.5 pt-1">
            <div class="bg-white p-2 rounded-xl border border-slate-200 text-center shadow-2xs">
              <span class="text-sm block">🌸</span>
              <span class="text-[10px] font-bold text-slate-700">日常会話</span>
            </div>
            <div class="bg-white p-2 rounded-xl border border-slate-200 text-center shadow-2xs">
              <span class="text-sm block">✈️</span>
              <span class="text-[10px] font-bold text-slate-700">旅行・買い物</span>
            </div>
            <div class="bg-white p-2 rounded-xl border border-slate-200 text-center shadow-2xs">
              <span class="text-sm block">📝</span>
              <span class="text-[10px] font-bold text-slate-700">苦手な動詞</span>
            </div>
          </div>
        </div>
      `,
      tips: {
        ja: '💡 単語の保存時に保存先フォルダを選べるほか、フォルダごとの集中テストもできます！',
        en: '💡 Choose which folder to save each word to, and take quizzes by folder!'
      }
    },
    {
      id: 'auto_audio',
      badge: { ja: 'ステップ 6 / 音声機能', en: 'Step 6 / Audio & Voice' },
      title: { ja: '🔊 音声自動再生で耳から覚える', en: 'Auto Audio Playback' },
      subtitle: {
        ja: '画面上部の「自動再生」（スマホ版は「？」マークの左隣にある音のマーク 🔊）をONにすると、カードを表示した時やめくった時に単語と例文が自動で流れます。',
        en: 'Turn on "Auto Audio" in the top bar (on mobile, tap the speaker icon 🔊 next to "?") to automatically hear words and example sentences.'
      },
      diagramHtml: (isJa) => `
        <div class="rounded-2xl bg-gradient-to-br from-rose-50/60 to-sky-50/60 border border-softBorder p-2.5 sm:p-3 shadow-inner space-y-2.5">
          <!-- スマホ版 vs PC版のUI比較カード -->
          <div class="bg-deepNavy text-white p-2.5 rounded-xl shadow-xs space-y-2.5">
            <!-- 📱 スマホ版: 音マークアイコン -->
            <div class="flex items-center justify-between pb-2 border-b border-white/10">
              <div class="flex items-center space-x-1.5">
                <span class="text-xs">📱</span>
                <div>
                  <span class="text-[11px] font-bold block leading-tight">${isJa ? 'スマホ版（ヘッダー上部）' : 'Mobile (Top Header)'}</span>
                  <span class="text-[9px] text-blue-200">${isJa ? '「？」の左隣の音マーク' : 'Speaker icon next to "?"'}</span>
                </div>
              </div>
              <div class="flex items-center space-x-1.5 shrink-0">
                <!-- ON -->
                <div class="flex items-center space-x-1 bg-white/20 px-2 py-0.5 rounded-lg border border-white/30">
                  <span class="w-6 h-6 rounded-full bg-white/30 text-white flex items-center justify-center text-xs shadow-2xs font-bold ring-1 ring-white/50">🔊</span>
                  <span class="text-[10px] font-black text-emerald-300">ON</span>
                </div>
                <!-- OFF -->
                <div class="flex items-center space-x-1 bg-white/5 px-2 py-0.5 rounded-lg border border-white/10 opacity-70">
                  <span class="w-6 h-6 rounded-full bg-white/10 text-white/50 flex items-center justify-center text-xs shadow-2xs">🔇</span>
                  <span class="text-[10px] font-bold text-slate-300">OFF</span>
                </div>
              </div>
            </div>

            <!-- 💻 PC版: スイッチ -->
            <div class="flex items-center justify-between pt-0.5">
              <div class="flex items-center space-x-1.5">
                <span class="text-xs">💻</span>
                <span class="text-[11px] font-bold">${isJa ? 'PC版（トグルスイッチ）' : 'PC / Desktop (Switch)'}</span>
              </div>
              <div class="flex items-center space-x-1.5">
                <span class="text-[10px] font-bold text-slate-200">${isJa ? '自動再生' : 'Auto Audio'}</span>
                <div class="flex items-center space-x-1 bg-coralPink px-2.5 py-0.5 rounded-full border border-white text-[10px] font-black text-white shadow-2xs">
                  <span>ON</span>
                  <span class="w-2.5 h-2.5 rounded-full bg-white ml-0.5 inline-block"></span>
                </div>
              </div>
            </div>
          </div>

          <!-- 音声ストップ機能の図解 -->
          <div class="bg-white rounded-xl p-2 sm:p-2.5 border border-slate-200 shadow-2xs space-y-1">
            <div class="flex items-center space-x-1.5 text-[11px] font-bold text-slate-700">
              <span class="w-4 h-4 rounded-full bg-coralPink text-white flex items-center justify-center text-[9px] shadow-2xs">🔊</span>
              <span>${isJa ? '音声ボタンをもう一度押すと停止（Stop）' : 'Tap voice button again to Stop'}</span>
            </div>
            <p class="text-[10px] text-slate-500 leading-relaxed pl-5.5">
              ${isJa ? '再生中に音声ボタンをもう一度タップすると、いつでもすぐにストップできます。' : 'Tap the voice button while playing to stop immediately anytime.'}
            </p>
          </div>
        </div>
      `,
      tips: {
        ja: '💡 例文も自然な日本語イントネーションで発音されます。シャドーイングの練習に最適です！',
        en: '💡 Plays natural Japanese intonation, perfect for shadowing practice!'
      }
    },
    {
      id: 'furigana',
      badge: { ja: 'ステップ 7 / 漢字練習', en: 'Step 7 / Furigana OFF' },
      title: { ja: '✍️ ふりがなOFFで漢字テスト', en: 'Practice Reading Kanji' },
      subtitle: {
        ja: '「ふりがな」（スマホ版は音マークの左隣にある「あ」マーク）をOFFに切り替えると、漢字の上の読みが隠れるので、漢字を自力で読めるか確認・特訓できます。',
        en: 'Turn Furigana OFF (on mobile, tap the "あ" icon next to speaker) to hide readings above kanji and test your memory.'
      },
      diagramHtml: (isJa) => `
        <div class="rounded-2xl bg-gradient-to-br from-slate-100 to-slate-200 border border-slate-300 p-2.5 sm:p-3 shadow-inner space-y-2.5">
          <!-- スマホ版 vs PC版のUI比較カード -->
          <div class="bg-deepNavy text-white p-2.5 rounded-xl shadow-xs space-y-2.5">
            <!-- 📱 スマホ版: 「あ」アイコン -->
            <div class="flex items-center justify-between pb-2 border-b border-white/10">
              <div class="flex items-center space-x-1.5">
                <span class="text-xs">📱</span>
                <div>
                  <span class="text-[11px] font-bold block leading-tight">${isJa ? 'スマホ版（ヘッダー上部）' : 'Mobile (Top Header)'}</span>
                  <span class="text-[9px] text-blue-200">${isJa ? '音マークの左隣の「あ」マーク' : '"あ" icon next to speaker'}</span>
                </div>
              </div>
              <div class="flex items-center space-x-1.5 shrink-0">
                <!-- ON -->
                <div class="flex items-center space-x-1 bg-white/20 px-2 py-0.5 rounded-lg border border-white/30">
                  <span class="w-6 h-6 rounded-full bg-white/30 text-white flex items-center justify-center text-xs shadow-2xs font-black font-jp ring-1 ring-white/50">あ</span>
                  <span class="text-[10px] font-black text-emerald-300">ON</span>
                </div>
                <!-- OFF -->
                <div class="flex items-center space-x-1 bg-white/5 px-2 py-0.5 rounded-lg border border-white/10 opacity-70">
                  <span class="w-6 h-6 rounded-full bg-white/10 text-white/50 flex items-center justify-center text-xs shadow-2xs font-bold font-jp line-through">あ</span>
                  <span class="text-[10px] font-bold text-slate-300">OFF</span>
                </div>
              </div>
            </div>

            <!-- 💻 PC版: スイッチ -->
            <div class="flex items-center justify-between pt-0.5">
              <div class="flex items-center space-x-1.5">
                <span class="text-xs">💻</span>
                <span class="text-[11px] font-bold">${isJa ? 'PC版（トグルスイッチ）' : 'PC / Desktop (Switch)'}</span>
              </div>
              <div class="flex items-center space-x-1.5">
                <span class="text-[10px] font-bold text-slate-200">${isJa ? 'ふりがな' : 'Furigana'}</span>
                <div class="flex items-center space-x-1 bg-slate-600 px-2.5 py-0.5 rounded-full border border-white text-[10px] font-black text-white shadow-2xs">
                  <span class="w-2.5 h-2.5 rounded-full bg-white mr-0.5 inline-block"></span>
                  <span>OFF</span>
                </div>
              </div>
            </div>
          </div>

          <!-- 比較イラスト -->
          <div class="grid grid-cols-2 gap-2 text-center text-xs">
            <div class="bg-white p-2 rounded-xl border border-slate-200 shadow-2xs">
              <span class="text-[10px] font-bold text-slate-400 block mb-0.5">${isJa ? '【ON】 読みつき' : '【ON】 With Furigana'}</span>
              <ruby class="text-sm font-bold text-slate-800">朝ご飯<rt class="text-deepNavy">あさごはん</rt></ruby>
            </div>
            <div class="bg-white p-2 rounded-xl border-2 border-coralPink shadow-2xs">
              <span class="text-[10px] font-bold text-coralPink block mb-0.5">${isJa ? '【OFF】 漢字チャレンジ' : '【OFF】 Kanji Quiz'}</span>
              <span class="text-sm font-black text-slate-900">朝ご飯</span>
            </div>
          </div>
        </div>
      `,
      tips: {
        ja: '💡 辞書を開いたときは、OFF時でも常に正確なふりがなが表示されるので安心です！',
        en: '💡 Furigana is always available inside the dictionary lookup modal!'
      }
    }
  ];

  function renderHelpGuideSlide(index) {
    if (index < 0) index = 0;
    if (index >= HELP_GUIDE_SLIDES.length) index = HELP_GUIDE_SLIDES.length - 1;
    currentHelpGuideSlideIndex = index;

    const slide = HELP_GUIDE_SLIDES[currentHelpGuideSlideIndex];
    const isJa = (currentLang === 'ja');
    const total = HELP_GUIDE_SLIDES.length;

    // ステップバッジ更新
    const stepBadge = document.getElementById('helpGuideStepBadge');
    if (stepBadge) {
      stepBadge.textContent = `${currentHelpGuideSlideIndex + 1} / ${total}`;
    }

    // スライド本体更新
    const container = document.getElementById('helpGuideSlideContainer');
    if (container) {
      const badgeText = isJa ? slide.badge.ja : slide.badge.en;
      const titleText = isJa ? slide.title.ja : slide.title.en;
      const subtitleText = isJa ? slide.subtitle.ja : slide.subtitle.en;
      const tipText = isJa ? slide.tips.ja : slide.tips.en;

      container.innerHTML = `
        <div class="space-y-3.5">
          <!-- 上部バッジ & タイトル -->
          <div>
            <span class="inline-block px-2.5 py-0.5 rounded-full bg-deepNavy/10 text-deepNavy text-[11px] font-extrabold mb-1">
              ${badgeText}
            </span>
            <h3 class="text-base sm:text-lg font-black text-slate-800 leading-snug">
              ${titleText}
            </h3>
            <p class="text-xs text-slate-600 leading-relaxed mt-1">
              ${subtitleText}
            </p>
          </div>

          <!-- イラスト・図解カード -->
          <div>
            ${typeof slide.diagramHtml === 'function' ? slide.diagramHtml(isJa) : slide.diagramHtml}
          </div>

          <!-- ヒント・アドバイス -->
          <div class="p-2.5 rounded-xl bg-amber-50/70 border border-amber-200/80 text-[11px] text-amber-900 font-medium leading-relaxed">
            ${tipText}
          </div>
        </div>
      `;
    }

    // ドット インジケーター更新
    const dotsContainer = document.getElementById('helpGuideDotsContainer');
    if (dotsContainer) {
      dotsContainer.innerHTML = HELP_GUIDE_SLIDES.map((_, i) => {
        const isActive = (i === currentHelpGuideSlideIndex);
        return `
          <button onclick="goToHelpGuideSlide(${i})" class="w-2 h-2 sm:w-2.5 sm:h-2.5 rounded-full transition-all duration-200 ${isActive ? 'bg-deepNavy w-5 sm:w-6' : 'bg-slate-300 hover:bg-slate-400'}" title="Slide ${i + 1}"></button>
        `;
      }).join('');
    }

    // ナビゲーションボタン更新
    const btnPrev = document.getElementById('btnHelpGuidePrev');
    const btnNext = document.getElementById('btnHelpGuideNext');
    const prevText = document.getElementById('helpGuidePrevText');
    const nextText = document.getElementById('helpGuideNextText');

    if (btnPrev) {
      btnPrev.disabled = (currentHelpGuideSlideIndex === 0);
    }
    if (prevText) {
      prevText.textContent = isJa ? '前へ' : 'Prev';
    }

    if (btnNext && nextText) {
      const isLast = (currentHelpGuideSlideIndex === total - 1);
      if (isLast) {
        nextText.textContent = isJa ? '完了 (閉じる)' : 'Done (Close)';
        btnNext.className = 'px-4 py-1.5 rounded-full bg-emerald-600 hover:bg-emerald-700 text-white font-bold transition text-xs flex items-center space-x-1 shadow-xs active:scale-95';
      } else {
        nextText.textContent = isJa ? '次へ' : 'Next';
        btnNext.className = 'px-4 py-1.5 rounded-full bg-deepNavy hover:bg-slate-800 text-white font-bold transition text-xs flex items-center space-x-1 shadow-xs active:scale-95';
      }
    }

    // Lucide アイコン再初期化
    if (window.lucide) {
      const modalEl = document.getElementById('helpGuideModal');
      if (modalEl) lucide.createIcons({ root: modalEl });
    }
  }

  function goToHelpGuideSlide(index) {
    renderHelpGuideSlide(index);
  }

  function nextHelpGuideSlide() {
    if (currentHelpGuideSlideIndex < HELP_GUIDE_SLIDES.length - 1) {
      renderHelpGuideSlide(currentHelpGuideSlideIndex + 1);
    } else {
      closeHelpGuideModal();
    }
  }

  function prevHelpGuideSlide() {
    if (currentHelpGuideSlideIndex > 0) {
      renderHelpGuideSlide(currentHelpGuideSlideIndex - 1);
    }
  }

  function openHelpGuideModal() {
    const modal = document.getElementById('helpGuideModal');
    if (modal) {
      currentHelpGuideSlideIndex = 0;
      renderHelpGuideSlide(0);
      modal.classList.remove('hidden');
      modal.classList.add('flex');
    }
  }

  function closeHelpGuideModal() {
    const modal = document.getElementById('helpGuideModal');
    if (modal) {
      modal.classList.add('hidden');
      modal.classList.remove('flex');
    }
  }

  // ==================== JLPT CONTROLLER & LEVEL PICKER ====================
  const JLPT_LEVEL_INFO = {
    N5: { title: 'JLPT N5 — 初級 (Beginner)', sub: '基本の日常生活単語。日本語学習のスタートライン。', cls: 'banner-n5', count: '702' },
    N4: { title: 'JLPT N4 — 初中級 (Elementary)', sub: '身近な日常会話・よく使われる表現。', cls: 'banner-n4', count: '668' },
    N3: { title: 'JLPT N3 — 中級 (Intermediate)', sub: '日常の幅広い場面で使われる重要単語。', cls: 'banner-n3', count: '1,843' },
    N2: { title: 'JLPT N2 — 上級 (Upper Intermediate)', sub: '新聞・ビジネス・幅広いトピックの語彙。', cls: 'banner-n2', count: '1,949' },
    N1: { title: 'JLPT N1 — 最上級 (Advanced)', sub: '論理的・専門的で高度な表現を含む総合語彙。', cls: 'banner-n1', count: '3,748' },
  };

  const JLPT_PAGE_SIZE = 60;
  let currentJlptLevel = 'N5';
  let currentJlptRow = 'all';
  let currentJlptViewMode = 'card'; // 'card' or 'list'
  let filteredJlptWords = [];
  let currentJlptPage = 1;
  let currentJlptModalWord = null;

  function initJlptView() {
    updateJlptHeaderSavedCount();
    switchJlptLevel(currentJlptLevel || 'N5');
  }

  function updateJlptHeaderSavedCount() {
    const el = document.getElementById('jlptSavedCount');
    if (el) {
      el.textContent = getMylistCards().length;
    }
  }

  function switchJlptLevel(level) {
    currentJlptLevel = level;
    currentJlptRow = 'all';
    currentJlptPage = 1;

    const searchInput = document.getElementById('jlptSearchInput');
    if (searchInput) searchInput.value = '';

    ['N5', 'N4', 'N3', 'N2', 'N1'].forEach(lvl => {
      const tabs = document.querySelectorAll(`.jlpt-level-tab.${lvl.toLowerCase()}`);
      tabs.forEach(tab => {
        tab.classList.toggle('active', lvl === level);
      });
    });

    // Reset Gojuon buttons
    document.querySelectorAll('.jlpt-gojuon-btn').forEach(btn => btn.classList.remove('active'));
    const allBtn = document.getElementById('jlptRow-all');
    if (allBtn) allBtn.classList.add('active');

    // Update banner
    const info = JLPT_LEVEL_INFO[level] || JLPT_LEVEL_INFO['N5'];
    const bannerBox = document.getElementById('jlptBannerBox');
    if (bannerBox) {
      bannerBox.className = 'rounded-2xl p-3 sm:p-4 flex items-center justify-between flex-wrap gap-2 shadow-2xs ' + info.cls;
    }
    const badge = document.getElementById('jlptBannerLevelBadge');
    if (badge) badge.textContent = level;
    const title = document.getElementById('jlptBannerTitle');
    if (title) title.textContent = info.title;
    const sub = document.getElementById('jlptBannerSub');
    if (sub) sub.textContent = info.sub;

    filterJlptWords();
  }

  function filterJlptRow(row) {
    currentJlptRow = row;
    currentJlptPage = 1;
    document.querySelectorAll('.jlpt-gojuon-btn').forEach(btn => btn.classList.remove('active'));
    const target = document.getElementById('jlptRow-' + row);
    if (target) target.classList.add('active');
    filterJlptWords();
  }

  function filterJlptWords() {
    const searchInput = document.getElementById('jlptSearchInput');
    const q = searchInput ? searchInput.value.trim().toLowerCase() : '';
    const allWords = (window.JLPT_VOCAB && window.JLPT_VOCAB[currentJlptLevel]) || [];

    filteredJlptWords = allWords.filter(w => {
      if (currentJlptRow !== 'all' && w.row !== currentJlptRow) {
        return false;
      }
      if (q.length > 0) {
        const wordMatch = (w.word || '').toLowerCase().includes(q);
        const readingMatch = (w.reading || '').toLowerCase().includes(q) || (w.k || '').toLowerCase().includes(q);
        const meaningMatch = (w.meanings || []).some(m => String(m).toLowerCase().includes(q));
        return wordMatch || readingMatch || meaningMatch;
      }
      return true;
    });

    renderJlptPage();
  }

  function isJlptWordInMylist(word) {
    if (!word) return false;
    for (const id of mylistSet) {
      if (id === word) return true;
      if (id.startsWith('jlpt_') && id.endsWith(`_${word}`)) return true;
      const card = getCardById(id);
      if (card && card.word === word) return true;
    }
    return false;
  }

  function toggleJlptWordMylist(event, idx) {
    if (event) event.stopPropagation();
    const w = filteredJlptWords[idx];
    if (!w) return;

    const cardId = `jlpt_${currentJlptLevel}_${idx}_${w.word}`;
    let existingId = null;
    for (const id of mylistSet) {
      if (id === w.word || (id.startsWith('jlpt_') && id.endsWith(`_${w.word}`))) {
        existingId = id;
        break;
      }
    }

    if (existingId) {
      mylistSet.delete(existingId);
      delete mylistCardFolderMap[existingId];
      saveMylistForCurrentStudent();
      showToast(currentLang === 'ja' ? `「${w.word}」をマイリストから解除しました` : `Removed "${w.word}" from My List`);
    } else {
      mylistSet.add(cardId);
      saveMylistForCurrentStudent();
      showToast(currentLang === 'ja' ? `「${w.word}」をマイリストに追加しました ⭐` : `Added "${w.word}" to My List ⭐`);
    }

    updateJlptHeaderSavedCount();
    renderJlptPage();
  }

  function renderJlptPage() {
    const totalWords = filteredJlptWords.length;
    const totalPages = Math.ceil(totalWords / JLPT_PAGE_SIZE);
    const start = (currentJlptPage - 1) * JLPT_PAGE_SIZE;
    const end = Math.min(start + JLPT_PAGE_SIZE, totalWords);
    const pageWords = filteredJlptWords.slice(start, end);

    const totalCountEl = document.getElementById('jlptTotalLevelCount');
    if (totalCountEl) totalCountEl.textContent = totalWords.toLocaleString();

    const rangeEl = document.getElementById('jlptShownRange');
    if (rangeEl) {
      rangeEl.textContent = totalWords > 0 ? `${(start + 1)}-${end}` : '0';
    }

    const container = document.getElementById('jlptWordsContainer');
    const empty = document.getElementById('jlptEmptyState');
    if (!container) return;

    if (totalWords === 0) {
      container.innerHTML = '';
      if (empty) empty.classList.remove('hidden');
      renderJlptPagination(0);
      return;
    }
    if (empty) empty.classList.add('hidden');

    if (currentJlptViewMode === 'card') {
      container.className = 'grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-2.5';
      container.innerHTML = pageWords.map((w, i) => buildJlptCardHtml(w, start + i)).join('');
    } else {
      container.className = 'flex flex-col space-y-2';
      container.innerHTML = pageWords.map((w, i) => buildJlptListItemHtml(w, start + i)).join('');
    }

    renderJlptPagination(totalPages);

    if (window.lucide) {
      lucide.createIcons({ root: container });
    }
  }

  function buildJlptCardHtml(w, globalIdx) {
    const reading = (w.reading && w.reading !== w.word) ? w.reading : (w.k || '');
    const meaningsText = (w.meanings || []).slice(0, 3).join(', ');
    const isSaved = isJlptWordInMylist(w.word);

    return `
      <div class="jlpt-word-card bg-white rounded-[14px] border border-[#E2E8F0] hover:border-[#82CBD3] p-3.5 transition shadow-2xs cursor-pointer flex flex-col justify-between" onclick="openJlptModal(${globalIdx})">
        <div>
          <div class="flex items-start justify-between gap-2 mb-1">
            <span class="text-xs text-[#576579] font-medium leading-none">${globalIdx + 1}</span>
            <div class="flex items-center space-x-1.5" onclick="event.stopPropagation()">
              ${w.row ? `<span class="text-[10px] px-2 py-0.5 rounded-md bg-[#F1F5F9] text-[#576579] font-medium leading-tight">${escapeHtml(w.row)}</span>` : ''}
              <button class="jlpt-save-btn ${isSaved ? 'saved' : ''}" onclick="toggleJlptWordMylist(event, ${globalIdx})" title="${isSaved ? 'マイリストから解除' : 'マイリストに保存'}">
                ${isSaved ? '★ 保存' : '☆ 保存'}
              </button>
              <button class="jlpt-tts-btn" onclick="event.stopPropagation(); speakJapanese('${escapeHtml(w.word)}')" title="発音を聴く">
                <i data-lucide="volume-2" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>
          <div class="text-[1.45rem] font-semibold text-[#1E5989] leading-tight font-jp mt-1">${escapeHtml(w.word)}</div>
          ${reading ? `<div class="text-[0.82rem] font-semibold text-[#C4688A] mt-0.5 font-jp">${escapeHtml(reading)}</div>` : ''}
          <div class="text-[0.82rem] text-[#232C3A] mt-2 line-clamp-2 leading-relaxed font-sans">${escapeHtml(meaningsText)}</div>
        </div>
      </div>`;
  }

  function buildJlptListItemHtml(w, globalIdx) {
    const reading = (w.reading && w.reading !== w.word) ? w.reading : (w.k || '');
    const meaningsText = (w.meanings || []).slice(0, 2).join(', ');
    const isSaved = isJlptWordInMylist(w.word);

    return `
      <div class="bg-white rounded-xl border border-softBorder px-3.5 py-2.5 flex items-center justify-between gap-3 hover:border-sky-300 transition shadow-2xs cursor-pointer" onclick="openJlptModal(${globalIdx})">
        <div class="flex items-center space-x-3 min-w-0">
          <span class="text-xs text-[#576579] font-medium font-sans w-7 shrink-0">${globalIdx + 1}</span>
          <div class="truncate">
            <div class="flex items-baseline space-x-2">
              <span class="font-semibold text-base text-[#1E5989] font-jp">${escapeHtml(w.word)}</span>
              ${reading ? `<span class="text-xs font-semibold text-[#C4688A] font-jp">${escapeHtml(reading)}</span>` : ''}
              ${w.row ? `<span class="text-[10px] text-[#576579] bg-[#F1F5F9] px-1.5 py-0.5 rounded font-medium">${escapeHtml(w.row)}</span>` : ''}
            </div>
            <div class="text-xs text-[#232C3A] truncate font-sans">${escapeHtml(meaningsText)}</div>
          </div>
        </div>
        <div class="flex items-center space-x-1.5 shrink-0" onclick="event.stopPropagation()">
          <button class="jlpt-save-btn ${isSaved ? 'saved' : ''}" onclick="toggleJlptWordMylist(event, ${globalIdx})">
            ${isSaved ? '★ 保存' : '☆ 保存'}
          </button>
          <button class="jlpt-tts-btn" onclick="event.stopPropagation(); speakJapanese('${escapeHtml(w.word)}')">
            <i data-lucide="volume-2" class="w-3.5 h-3.5"></i>
          </button>
        </div>
      </div>`;
  }

  function renderJlptPagination(totalPages) {
    const container = document.getElementById('jlptPaginationContainer');
    if (!container) return;

    if (totalPages <= 1) {
      container.innerHTML = '';
      return;
    }

    let html = '';
    if (currentJlptPage > 1) {
      html += `<button class="px-2.5 py-1 rounded-lg bg-white border border-slate-200 text-xs font-bold text-slate-700 hover:bg-slate-50 shadow-2xs" onclick="goJlptPage(${currentJlptPage - 1})">← 前へ</button>`;
    }

    const start = Math.max(1, currentJlptPage - 2);
    const end = Math.min(totalPages, currentJlptPage + 2);

    if (start > 1) {
      html += `<button class="w-7 h-7 rounded-lg bg-white border border-slate-200 text-xs font-bold text-slate-700 hover:bg-slate-50 shadow-2xs" onclick="goJlptPage(1)">1</button>`;
      if (start > 2) html += `<span class="text-xs text-slate-400">…</span>`;
    }

    for (let p = start; p <= end; p++) {
      const active = (p === currentJlptPage);
      html += `<button class="w-7 h-7 rounded-lg text-xs font-black shadow-2xs transition ${active ? 'bg-deepNavy text-white' : 'bg-white border border-slate-200 text-slate-700 hover:bg-slate-50'}" onclick="goJlptPage(${p})">${p}</button>`;
    }

    if (end < totalPages) {
      if (end < totalPages - 1) html += `<span class="text-xs text-slate-400">…</span>`;
      html += `<button class="w-7 h-7 rounded-lg bg-white border border-slate-200 text-xs font-bold text-slate-700 hover:bg-slate-50 shadow-2xs" onclick="goJlptPage(${totalPages})">${totalPages}</button>`;
    }

    if (currentJlptPage < totalPages) {
      html += `<button class="px-2.5 py-1 rounded-lg bg-white border border-slate-200 text-xs font-bold text-slate-700 hover:bg-slate-50 shadow-2xs" onclick="goJlptPage(${currentJlptPage + 1})">次へ →</button>`;
    }

    container.innerHTML = html;
  }

  function goJlptPage(p) {
    currentJlptPage = p;
    renderJlptPage();
    const container = document.getElementById('viewJlpt');
    if (container) {
      container.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  let currentJlptModalWordExamples = [];

  function formatRubyHtml(str) {
    if (!str) return '';
    if (/<ruby\b/i.test(str)) {
      return str.replace(/<(?!\/?(?:ruby|rt|rp|br)\b)[^>]+>/gi, '');
    }
    return escapeHtml(str);
  }

  function getJlptWordFallbackExample(w) {
    if (!w) return null;
    const vocabLists = [window.CLASS_VOCAB_DATA, window.INITIAL_VOCAB_DATA];
    for (const list of vocabLists) {
      if (!list) continue;
      const item = list.find(v => v && (v.word === w.word || (w.reading && v.reading === w.reading)));
      if (item && item.example && item.example.ja) {
        return item.example;
      }
    }
    if (window.DICT_EXAMPLES_MAP) {
      const ex = window.DICT_EXAMPLES_MAP[w.word] || (w.reading && window.DICT_EXAMPLES_MAP[w.reading]);
      if (ex && ex.ja) {
        return ex;
      }
    }
    return null;
  }

  function speakJlptExampleByIndex(idx) {
    const ex = currentJlptModalWordExamples[idx];
    if (ex && ex.ja) {
      speakJapanese(ex.ja);
    }
  }

  function openJlptModal(idx) {
    const w = filteredJlptWords[idx];
    if (!w) return;
    currentJlptModalWord = w;

    const modal = document.getElementById('jlptDetailModal');
    if (!modal) return;

    document.getElementById('jlptModalBadgeLevel').textContent = currentJlptLevel;
    document.getElementById('jlptModalWord').textContent = w.word;
    document.getElementById('jlptModalReading').textContent = (w.reading && w.reading !== w.word) ? w.reading : (w.k || '');

    const meaningsList = document.getElementById('jlptModalMeanings');
    meaningsList.innerHTML = (w.meanings || []).map((m, i) =>
      `<div class="flex items-start space-x-2"><span class="w-4 h-4 rounded-full bg-slate-100 text-[10px] font-black text-slate-600 flex items-center justify-center shrink-0 mt-0.5">${i + 1}</span><span>${escapeHtml(m)}</span></div>`
    ).join('');

    const exSec = document.getElementById('jlptModalExamplesSection');
    const exList = document.getElementById('jlptModalExamplesList');
    let examples = (w.examples && w.examples.length > 0) ? [...w.examples] : [];
    if (examples.length === 0) {
      const fallbackEx = getJlptWordFallbackExample(w);
      if (fallbackEx) {
        examples = [fallbackEx];
      }
    }
    currentJlptModalWordExamples = examples;

    if (examples.length > 0) {
      exSec.style.display = 'block';
      exList.innerHTML = examples.map((ex, exIdx) => {
        const trans = getBilingualExampleTrans(ex, currentLang) || ex.en || '';
        const jaHtml = formatRubyHtml(ex.ja);
        return `
        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
          <div class="flex items-start justify-between gap-2">
            <div class="font-medium text-slate-900 font-jp leading-relaxed select-text">${jaHtml}</div>
            <button class="w-6 h-6 rounded-full bg-white text-slate-700 flex items-center justify-center shrink-0 border border-slate-200 shadow-2xs hover:bg-slate-100 transition active:scale-95" onclick="speakJlptExampleByIndex(${exIdx})" title="発音を聞く">
              ▶
            </button>
          </div>
          ${trans ? `<div class="text-[12px] text-slate-600 font-medium">${trans}</div>` : ''}
        </div>`;
      }).join('');
    } else {
      exSec.style.display = 'none';
      exList.innerHTML = '';
    }

    updateJlptModalSaveBtn();
    modal.classList.remove('hidden');
    modal.classList.add('flex');

    if (window.lucide) lucide.createIcons({ root: modal });
  }

  function closeJlptModal() {
    const modal = document.getElementById('jlptDetailModal');
    if (modal) {
      modal.classList.add('hidden');
      modal.classList.remove('flex');
    }
  }

  function updateJlptModalSaveBtn() {
    const btn = document.getElementById('btnJlptModalSave');
    const textEl = document.getElementById('btnJlptModalSaveText');
    if (!btn || !textEl || !currentJlptModalWord) return;

    const isSaved = isJlptWordInMylist(currentJlptModalWord.word);
    if (isSaved) {
      btn.className = 'flex-1 py-2 px-3 rounded-full bg-slate-200 hover:bg-slate-300 text-slate-700 font-bold text-xs flex items-center justify-center space-x-1 shadow-xs transition';
      textEl.textContent = '★ マイリストから解除';
    } else {
      btn.className = 'flex-1 py-2 px-3 rounded-full bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs flex items-center justify-center space-x-1 shadow-xs transition';
      textEl.textContent = '🔖 マイリストに保存';
    }
  }

  function toggleJlptModalSave() {
    if (!currentJlptModalWord) return;
    const word = currentJlptModalWord.word;
    const cardId = `jlpt_${currentJlptLevel}_0_${word}`;

    let existingId = null;
    for (const id of mylistSet) {
      if (id === word || (id.startsWith('jlpt_') && id.endsWith(`_${word}`))) {
        existingId = id;
        break;
      }
    }

    if (existingId) {
      mylistSet.delete(existingId);
      delete mylistCardFolderMap[existingId];
      saveMylistForCurrentStudent();
      showToast(currentLang === 'ja' ? `「${word}」をマイリストから解除しました` : `Removed "${word}" from My List`);
    } else {
      mylistSet.add(cardId);
      saveMylistForCurrentStudent();
      showToast(currentLang === 'ja' ? `「${word}」をマイリストに追加しました ⭐` : `Added "${word}" to My List ⭐`);
    }

    updateJlptModalSaveBtn();
    updateJlptHeaderSavedCount();
    renderJlptPage();
  }

  // --- JLPT Flashcards Level Selector Modal ---
  function openJlptLevelSelectModal() {
    const modal = document.getElementById('jlptLevelSelectModal');
    if (modal) {
      modal.classList.remove('hidden');
      modal.classList.add('flex');
      if (window.lucide) lucide.createIcons({ root: modal });
    }
  }

  function closeJlptLevelSelectModal() {
    const modal = document.getElementById('jlptLevelSelectModal');
    if (modal) {
      modal.classList.add('hidden');
      modal.classList.remove('flex');
    }
  }

  function selectJlptLevelForCards(level) {
    currentJlptDeckLevel = level;
    currentDeckFilter = 'jlpt';
    closeJlptLevelSelectModal();

    // Update pill UI
    const filterAllBtn = document.getElementById('filterAllDeck');
    const filterMyBtn = document.getElementById('filterMyDeck');
    const filterJlptBtn = document.getElementById('filterJlptDeck');
    const inactiveClass = 'px-2.5 py-0.5 rounded-full text-slate-600 font-semibold transition text-[11px] hover:text-slate-900';

    if (filterAllBtn) filterAllBtn.className = inactiveClass;
    if (filterMyBtn) filterMyBtn.className = inactiveClass;
    if (filterJlptBtn) {
      filterJlptBtn.className = 'px-2.5 py-0.5 rounded-full bg-teal-600 text-white font-bold transition text-[11px] shadow-xs';
      filterJlptBtn.textContent = `JLPT (${level})`;
    }

    switchView('flashcards');
    updateActiveDeck();
    showToast(currentLang === 'ja' ? `JLPT ${level} の単語（${activeDeck.length}語）を読み込みました！` : `Loaded JLPT ${level} words (${activeDeck.length} words)!`);
  }

  // グローバル露出（インラインイベント等からの呼出用）
  window.switchJlptLevel = switchJlptLevel;
  window.filterJlptRow = filterJlptRow;
  window.filterJlptWords = filterJlptWords;
  window.goJlptPage = goJlptPage;
  window.openJlptModal = openJlptModal;
  window.closeJlptModal = closeJlptModal;
  window.speakJlptExampleByIndex = speakJlptExampleByIndex;
  window.toggleJlptWordMylist = toggleJlptWordMylist;
  window.toggleJlptModalSave = toggleJlptModalSave;
  window.openJlptLevelSelectModal = openJlptLevelSelectModal;
  window.closeJlptLevelSelectModal = closeJlptLevelSelectModal;
  window.selectJlptLevelForCards = selectJlptLevelForCards;

  window.closeDictPopupModal = closeDictPopupModal;
  window.openDictLookupModal = openDictLookupModal;
  window.openHelpGuideModal = openHelpGuideModal;
  window.closeHelpGuideModal = closeHelpGuideModal;
  window.goToHelpGuideSlide = goToHelpGuideSlide;
  window.nextHelpGuideSlide = nextHelpGuideSlide;
  window.prevHelpGuideSlide = prevHelpGuideSlide;

  // --- App Startup ---
  function startup() {
    initData();
    setupListeners();
    // ★ 例文のテキスト選択ツールバー（辞書で調べる / マイリスト保存）初期化
    if (typeof initExampleSelectionToolbar === 'function') {
      initExampleSelectionToolbar();
    }
    if ('speechSynthesis' in window) {
      window.speechSynthesis.onvoiceschanged = () => {
        window.speechSynthesis.getVoices();
      };
      try { window.speechSynthesis.getVoices(); } catch (e) {}
    }
    // Mobile WebKit speech audio unlock listeners (prevent iOS pausing)
    const resumeSpeechAudio = () => {
      if ('speechSynthesis' in window && window.speechSynthesis.paused) {
        window.speechSynthesis.resume();
      }
    };
    document.addEventListener('touchstart', resumeSpeechAudio, { passive: true });
    document.addEventListener('touchend', resumeSpeechAudio, { passive: true });
    document.addEventListener('click', resumeSpeechAudio, { passive: true });
    // 📱 端末間同期: 別端末（スマホ・他PC）で保存・更新された後、この画面に戻ってきた瞬間に自動PULL同期！
    document.addEventListener('visibilitychange', () => {
      if (!document.hidden && currentStudent && currentStudent.id !== 'guest') {
        syncStudentFromCloud(currentStudent.id).then(changed => {
          if (changed) {
            loadMylistForCurrentStudent();
            updateActiveDeck();
            if (currentView === 'mylist') renderMylistGrid();
          }
        }).catch(() => {});
      }
    });

    window.addEventListener('focus', () => {
      if (currentStudent && currentStudent.id !== 'guest') {
        syncStudentFromCloud(currentStudent.id).then(changed => {
          if (changed) {
            loadMylistForCurrentStudent();
            updateActiveDeck();
            if (currentView === 'mylist') renderMylistGrid();
          }
        }).catch(() => {});
      }
    });

    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('view')) {
      switchView(urlParams.get('view'));
    }
    if (urlParams.get('section') !== null) {
      const secNum = Number(urlParams.get('section'));
      const secInfo = getCatalogSection(secNum);
      const title = secInfo ? secInfo.title : `単元${secNum}`;
      currentFolder = 'folder_1';
      startStudyingSection(secNum, title);
    }
  }

  if (document.readyState === 'loading') {
    window.addEventListener('DOMContentLoaded', startup);
  } else {
    startup();
  }

})();
