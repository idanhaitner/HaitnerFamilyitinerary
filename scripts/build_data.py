#!/usr/bin/env python3
"""Build family-haitner/docs/js/data.js from the Haitner family Excel itinerary (Japan only)."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "js" / "data.js"


def place(id, name, name_local, city, country, tags, lat, lng, blurb, taxi_address=None):
    p = {
        "id": id, "name": name, "nameJa": name_local, "city": city, "country": country,
        "tags": tags, "lat": lat, "lng": lng, "blurb": blurb,
    }
    if taxi_address:
        p["taxiAddress"] = taxi_address
    return p


PLACES = {}


def add(p):
    PLACES[p["id"]] = p


for p in [
    # Hotels (booked per Excel)
    place("keio-plaza", "Keio Plaza Hotel Tokyo", "京王プラザホテル", "Tokyo", "JP",
          ["hotel", "booked"], 35.6906, 139.6921,
          "בסיס בטוקיו ליד שינג׳וקו — צ׳ק־אין ביום הנחיתה.",
          "東京都新宿区西新宿2-2-1 京王プラザホテル"),
    place("kajikaso", "Hotel Kajikaso", "ホテルかじか荘", "Hakone", "JP",
          ["hotel", "onsen", "booked"], 35.2335, 139.0885,
          "ריוקאן/מלון בהאקונה עם אונסן — לילה אחד.",
          "神奈川県足柄下郡箱根町湯本茶屋624 ホテルかじか荘"),
    place("musse-kyoto", "Hotel Musse Kyoto Shijo Kawaramachi", "ホテルミュッセ京都四条河原町名鉄", "Kyoto", "JP",
          ["hotel", "booked"], 35.0037, 135.7685,
          "מלון בקיוטו ליד שיג׳ו־קווארמאצ׳י.",
          "京都府京都市中京区河原町通四条上る２丁目稲荷町３３６−１ ホテルミュッセ京都四条河原町名鉄"),
    place("daiwa-hiroshima", "Daiwa Roynet Hotel Hiroshima", "ダイワロイネットホテル広島", "Hiroshima", "JP",
          ["hotel", "booked"], 34.3927, 132.4553,
          "מלון בהירושימה — בסיס למיאג׳ימה.",
          "広島県広島市中区大手町3-6-18 ダイワロイネットホテル広島"),
    place("cross-osaka", "Cross Hotel Osaka", "クロスホテル大阪", "Osaka", "JP",
          ["hotel", "booked"], 34.6693, 135.5013,
          "מלון באוסקה ליד נמבה ודוטונבורי.",
          "大阪府大阪市中央区千日前1-1-13 クロスホテル大阪"),
    place("solaria", "Solaria Nishitetsu Hotel Ginza", "ソラリア西鉄ホテル銀座", "Tokyo", "JP",
          ["hotel", "booked"], 35.6695, 139.7668,
          "חזרה לטוקיו — מלון בגינזה ללילות האחרונים.",
          "東京都中央区銀座1-1-7 ソラリア西鉄ホテル銀座"),

    # Transport
    place("narita", "Narita Airport (NRT)", "成田国際空港", "Tokyo", "JP",
          ["transport"], 35.7720, 140.3929, "נחיתה והמראה — נחיתה 17:40, המראה 22:30."),

    # Tokyo
    place("shinjuku", "Shinjuku", "新宿", "Tokyo", "JP",
          ["neighborhood", "food", "nightlife", "shopping"], 35.6938, 139.7034,
          "מרכז קניות וחיי לילה — Godzilla, ניאון ואווירה אורבנית."),
    place("shibuya-crossing", "Shibuya Crossing", "渋谷スクランブル交差点", "Tokyo", "JP",
          ["must-see", "icon"], 35.6595, 139.7005, "מעבר החצייה המפורסם + האצ׳יקו."),
    place("miyashita-park", "Miyashita Park", "ミヤシタパーク", "Tokyo", "JP",
          ["shopping", "park"], 35.6615, 139.7018, "מתחם קניות עם פארק על הגג בשיבויה."),
    place("shibuya-hikarie", "Shibuya Hikarie", "渋谷ヒカリエ", "Tokyo", "JP",
          ["shopping", "view"], 35.6591, 139.7035, "קומפלקס עם מרפסת תצפית חינמית בקומה 11."),
    place("meiji-jingu", "Meiji Jingu", "明治神宮", "Tokyo", "JP",
          ["must-see", "culture", "shrine"], 35.6764, 139.6993, "מקדש שינטו ביער בלב טוקיו."),
    place("takeshita", "Takeshita Street", "竹下通り", "Tokyo", "JP",
          ["food", "shopping"], 35.6702, 139.7050, "הראג׳וקו — קרפים ואופנת רחוב."),
    place("cat-street", "Cat Street", "キャットストリート", "Tokyo", "JP",
          ["shopping", "neighborhood"], 35.6658, 139.7038, "רחוב רגוע יותר עם אופנה צבעונית."),
    place("omotesando", "Omotesando", "表参道", "Tokyo", "JP",
          ["shopping", "architecture"], 35.6652, 139.7122, "שדרת הבוטיקים היוקרתית של טוקיו."),
    place("disneysea", "Tokyo DisneySea", "東京ディズニーシー", "Tokyo", "JP",
          ["must-see", "park"], 35.6267, 139.8851, "פארק דיסני ייחודי — יום מלא."),
    place("ameyoko", "Ameyoko Market", "アメ横", "Tokyo", "JP",
          ["food", "market", "must-see"], 35.7095, 139.7745, "שוק רחוב בין אוקאצ׳ימאצ׳י לאואנו."),
    place("akihabara", "Akihabara", "秋葉原", "Tokyo", "JP",
          ["shopping", "culture"], 35.7023, 139.7745, "אלקטרוניקה, ארקיידים ותרבות אוטאקו."),
    place("golden-gai", "Shinjuku Golden Gai", "新宿ゴールデン街", "Tokyo", "JP",
          ["must-see", "nightlife"], 35.6938, 139.7047, "סמטאות ברים זעירים בשינג׳וקו."),
    place("daikanyama", "Daikanyama T-Site", "代官山T-SITE", "Tokyo", "JP",
          ["culture", "food", "shopping"], 35.6492, 139.7032, "מתחם ספרים ועיצוב אלגנטי."),
    place("starbucks-reserve", "Starbucks Reserve Roastery Tokyo", "スターバックス リザーブ ロースタリー 東京", "Tokyo", "JP",
          ["food", "icon"], 35.6490, 139.7125, "סניף דגל ליד נהר מגורו."),
    place("nakameguro", "Nakameguro / Meguro River", "中目黒", "Tokyo", "JP",
          ["neighborhood", "food", "must-see"], 35.6442, 139.6988, "טיילת נהר, בוטיקים ומסעדות."),
    place("ny-bar", "New York Bar (Park Hyatt)", "ニューヨークバー", "Tokyo", "JP",
          ["nightlife", "view", "must-see"], 35.6855, 139.6905, "בר Lost in Translation מעל טוקיו."),
    place("imperial-east", "Imperial Palace East Gardens", "皇居東御苑", "Tokyo", "JP",
          ["culture", "park", "must-see"], 35.6865, 139.7575, "גני הארמון הקיסרי."),
    place("marunouchi", "Marunouchi", "丸の内", "Tokyo", "JP",
          ["shopping", "neighborhood", "architecture"], 35.6812, 139.7649,
          "אזור עסקים יוקרתי בין הארמון לתחנת טוקיו."),
    place("ginza", "Ginza", "銀座", "Tokyo", "JP",
          ["shopping", "food", "must-see"], 35.6712, 139.7649, "חנויות כלבו, Uniqlo דגל וקניות אלגנטיות."),
    place("asakusa", "Asakusa / Senso-ji", "浅草寺", "Tokyo", "JP",
          ["must-see", "culture", "food"], 35.7148, 139.7967, "מקדש סנסוג׳י + נקאמיסה."),
    place("asakusa-info", "Asakusa Culture Tourist Information Center", "浅草文化観光センター", "Tokyo", "JP",
          ["view", "culture"], 35.7115, 139.7967, "מרכז מידע של קנגו קומה עם מרפסת תצפית."),
    place("kappabashi", "Kappabashi Street", "合羽橋道具街", "Tokyo", "JP",
          ["food", "shopping"], 35.7155, 139.7870, "רחוב כלי מטבח ודגמי אוכל."),
    place("skytree", "Tokyo Skytree", "東京スカイツリー", "Tokyo", "JP",
          ["must-see", "view"], 35.7101, 139.8107, "מגדל 634 מ׳ + סולמאצ׳י."),
    place("tsukiji", "Tsukiji Outer Market", "築地場外市場", "Tokyo", "JP",
          ["must-see", "food"], 35.6654, 139.7707, "ארוחת בוקר ושוק דגים חיצוני לפני הטיסה."),

    # Hakone
    place("open-air", "Hakone Open-Air Museum", "箱根彫刻の森美術館", "Hakone", "JP",
          ["culture", "must-see"], 35.2445, 139.0515, "מוזיאון פסלים פתוח בעמק."),
    place("owakudani", "Owakudani", "大涌谷", "Hakone", "JP",
          ["must-see", "nature", "food"], 35.2424, 139.0204, "עמק געשי + ביצים שחורות."),
    place("lake-ashi", "Lake Ashi Pirate Ship", "箱根海賊船", "Hakone", "JP",
          ["nature", "park", "must-see"], 35.2065, 139.0250, "שייט פיראטים על אגם אשי."),
    place("hakone-shrine", "Hakone Shrine", "箱根神社", "Hakone", "JP",
          ["must-see", "shrine"], 35.2051, 139.0256, "טוריי אדום על שפת האגם."),

    # Kyoto
    place("nishiki", "Nishiki Market", "錦市場", "Kyoto", "JP",
          ["must-see", "food"], 35.0050, 135.7649, "המטבח של קיוטו."),
    place("gion", "Gion", "祇園", "Kyoto", "JP",
          ["must-see", "neighborhood"], 35.0037, 135.7788, "רובע הגיישות — Hanami-koji ושירוקאווה."),
    place("yasaka-shrine", "Yasaka Shrine", "八坂神社", "Kyoto", "JP",
          ["shrine", "culture"], 35.0036, 135.7786, "מקדש שינטו בלב גיון."),
    place("pontocho", "Pontocho Alley", "先斗町", "Kyoto", "JP",
          ["food", "nightlife", "must-see"], 35.0045, 135.7712, "סמטת ארוחת ערב ליד נהר קאמו."),
    place("togetsukyo", "Togetsukyo Bridge", "渡月橋", "Kyoto", "JP",
          ["icon", "nature"], 35.0135, 135.6778, "הגשר האייקוני של אראשיאמה."),
    place("bamboo", "Arashiyama Bamboo Grove", "竹林の小径", "Kyoto", "JP",
          ["must-see", "nature"], 35.0173, 135.6721, "שביל הבמבוק המפורסם."),
    place("monkey-park", "Iwatayama Monkey Park", "嵐山モンキーパーク", "Kyoto", "JP",
          ["park", "nature"], 35.0117, 135.6761, "קופים + תצפית על קיוטו (¥600)."),
    place("tenryuji", "Tenryu-ji", "天龍寺", "Kyoto", "JP",
          ["temple", "culture", "must-see"], 35.0156, 135.6736, "מקדש זן אונסק״ו עם גן נוף."),
    place("teamlab-biovortex", "teamLab Biovortex Kyoto", "チームラボ バイオヴォルテックス 京都", "Kyoto", "JP",
          ["must-see", "culture"], 34.9828, 135.7568, "teamLab הגדול ביפן — ליד תחנת קיוטו."),
    place("fushimi-inari", "Fushimi Inari Taisha", "伏見稲荷大社", "Kyoto", "JP",
          ["must-see", "shrine"], 34.9671, 135.7727, "אלפי שערי טוריי אדומים."),
    place("uji-bridge", "Uji Bridge", "宇治橋", "Kyoto", "JP",
          ["nature", "food"], 34.8895, 135.8075, "גשר עתיק על נהר אוג׳י + בתי תה."),
    place("byodoin", "Byodo-in Temple", "平等院", "Kyoto", "JP",
          ["must-see", "temple"], 34.8894, 135.8077, "היכל הפניקס — על מטבע 10 ין."),
    place("byodoin-omotesando", "Byodo-in Omotesando", "平等院表参道", "Kyoto", "JP",
          ["food", "shopping"], 34.8900, 135.8065, "רחוב המאצ׳ה של אוג׳י."),
    place("tea-ceremony", "Kimono Tea Ceremony MAIKOYA", "舞妓体験処舞香屋", "Kyoto", "JP",
          ["must-see", "culture"], 35.0025, 135.7595, "טקס תה מסורתי באזור קראסומה־שיג׳ו."),
    place("kiyomizu", "Kiyomizu-dera", "清水寺", "Kyoto", "JP",
          ["must-see", "temple"], 34.9949, 135.7850, "מקדש עם מרפסת עץ מעל קיוטו."),
    place("sannenzaka", "Sannenzaka & Ninenzaka", "三年坂・二年坂", "Kyoto", "JP",
          ["must-see", "food", "shopping"], 34.9958, 135.7815, "רחובות אבן ציוריים בהיגשיאמה."),
    place("yasaka-pagoda", "Yasaka Pagoda (Hokan-ji)", "法観寺・八坂の塔", "Kyoto", "JP",
          ["must-see", "icon", "temple"], 34.9980, 135.7790, "פגודה בת חמש קומות — נקודת צילום."),
    place("kodaiji", "Kodai-ji Temple", "高台寺", "Kyoto", "JP",
          ["temple", "culture"], 35.0000, 135.7815, "מקדש זן עם גנים ובתי תה."),
    place("starbucks-ninenzaka", "Starbucks Ninenzaka Yasaka Chaya", "スターバックス 京都二寧坂ヤサカ茶屋", "Kyoto", "JP",
          ["food", "icon"], 34.9965, 135.7805, "סטארבקס בבית עץ מסורתי עם טאטאמי."),
    place("higashiyama", "Higashiyama District", "東山区", "Kyoto", "JP",
          ["neighborhood", "must-see", "culture"], 34.9985, 135.7800, "הלב ההיסטורי של קיוטו."),

    # Hiroshima
    place("shukkeien", "Shukkeien Garden", "縮景園", "Hiroshima", "JP",
          ["culture", "park", "must-see"], 34.3995, 132.4674, "גן נוף מוקטן עם אגם ושביל מעגלי."),
    place("peace-park", "Peace Memorial Park", "平和記念公園", "Hiroshima", "JP",
          ["must-see", "culture"], 34.3955, 132.4536, "כיפת הפצצה + אנדרטאות."),
    place("peace-museum", "Hiroshima Peace Memorial Museum", "広島平和記念資料館", "Hiroshima", "JP",
          ["must-see", "culture"], 34.3916, 132.4531, "מוזיאון השלום — שעה עד שעה וחצי."),
    place("hondori", "Hondori Shopping Street", "本通商店街", "Hiroshima", "JP",
          ["shopping", "food"], 34.3930, 132.4565, "רחוב קניות מקורה במרכז הירושימה."),
    place("nagarekawa", "Nagarekawa Nightlife", "流川町", "Hiroshima", "JP",
          ["nightlife", "food"], 34.3920, 132.4620, "רובע חיי הלילה של הירושימה."),
    place("miyajima-omotesando", "Miyajima Omotesando", "宮島表参道商店街", "Hiroshima", "JP",
          ["food", "shopping"], 34.2975, 132.3210, "רחוב קניות ואוכל בדרך למקדש."),
    place("miyajima", "Itsukushima Shrine", "厳島神社", "Hiroshima", "JP",
          ["must-see", "shrine"], 34.2960, 132.3198, "טוריי צף — גאות ושפל."),
    place("misen", "Mt. Misen Ropeway", "弥山ロープウェイ", "Hiroshima", "JP",
          ["nature", "view", "must-see"], 34.2905, 132.3185, "רכבל ופסגה עם נוף לים סטו."),

    # Osaka / Nara
    place("kuromon", "Kuromon Market", "黒門市場", "Osaka", "JP",
          ["must-see", "food"], 34.6664, 135.5064, "המטבח של אוסקה — דגים ואוכל רחוב."),
    place("osaka-castle", "Osaka Castle", "大阪城", "Osaka", "JP",
          ["culture", "must-see"], 34.6873, 135.5262, "טירה + פארק ומוזיאון."),
    place("dotonbori", "Dotonbori", "道頓堀", "Osaka", "JP",
          ["must-see", "food", "nightlife"], 34.6687, 135.5013, "ניאון, גליקו ואוכל רחוב."),
    place("nara-park", "Nara Park / Todai-ji", "奈良公園・東大寺", "Osaka", "JP",
          ["must-see", "culture"], 34.6889, 135.8398, "איילים + בודהה גדול."),
    place("kasuga", "Kasuga Taisha", "春日大社", "Osaka", "JP",
          ["shrine", "culture"], 34.6814, 135.8482, "מקדש עם מאות פנסים."),
    place("nakatanidou", "Nakatanidou Mochi", "中谷堂", "Osaka", "JP",
          ["food"], 34.6820, 135.8305, "מוצ׳י מהיר בלייב ליד נארה."),
    place("shinsekai", "Shinsekai / Tsutenkaku", "新世界・通天閣", "Osaka", "JP",
          ["food", "neighborhood", "must-see"], 34.6525, 135.5063, "אוסקה רטרו + מגדל צוטנקאקו."),
    place("tenjinbashi", "Tenjinbashi-suji", "天神橋筋商店街", "Osaka", "JP",
          ["shopping", "food", "must-see"], 34.7045, 135.5110, "רחוב הקניות המקורה הארוך ביפן."),
    place("tenmangu", "Osaka Tenmangu Shrine", "大阪天満宮", "Osaka", "JP",
          ["shrine", "culture"], 34.6965, 135.5125, "מקדש שינטו ליד תחילת טנג׳ינבאשי."),
    place("umeda-sky", "Umeda Sky Building", "梅田スカイビル", "Osaka", "JP",
          ["must-see", "view"], 34.7055, 135.4897, "מצפה Floating Garden בקומה 39."),
]:
    add(p)


def day(id, date, weekday, city, country, hotel_id, title, summary, food, place_ids, transport, tips, timeline, transfer=None):
    d = {
        "id": id, "date": date, "weekday": weekday, "city": city, "country": country,
        "hotelId": hotel_id, "title": title, "summary": summary, "food": food,
        "placeIds": place_ids, "transport": transport, "tips": tips, "timeline": timeline,
    }
    if transfer:
        d["transfer"] = transfer
    return d


def infer_category(title, place_id, note=""):
    text = f"{title} {note}".lower()
    tags = []
    if place_id and place_id in PLACES:
        tags = PLACES[place_id].get("tags") or []
    if place_id and place_id in PLACES and "hotel" in tags:
        return "hotel"
    if any(k in text for k in ("flight", "train", "shinkansen", "romancecar", "subway", "bus", "ferry", "transfer", "depart", "airport", "ropeway", "טיסה", "רכבת", "שינקנסן", "העברה", "נחיתה", "המראה", "מעבורת", "רכבל")) or "transport" in tags:
        return "transit"
    if any(k in text for k in ("breakfast", "lunch", "dinner", "food", "market", "crepe", "ramen", "sushi", "café", "cafe", "okonomi", "ארוחה", "שוק", "אוכל", "קפה", "תה", "מוצ׳י")) or "food" in tags or "market" in tags:
        return "dining"
    if any(k in text for k in ("shop", "souvenir", "ginza", "depachika", "קניות", "חנויות")) or "shopping" in tags:
        return "shopping"
    if any(k in text for k in ("temple", "shrine", "palace", "garden", "museum", "zen", "tea", "מקדש", "גן", "מוזיאון", "טקס")) or "culture" in tags or "temple" in tags or "shrine" in tags:
        return "culture"
    if "park" in tags or any(k in text for k in ("disney", "teamlab", "skytree", "tower", "park", "monkey", "cruise", "פארק", "שייט", "מגדל")):
        return "attraction"
    if "nightlife" in tags:
        return "dining"
    return "attraction"


def t(time, title, place_id=None, note="", end=None, category=None):
    item = {"time": time, "title": title, "note": note}
    if place_id:
        item["placeId"] = place_id
    if end:
        item["end"] = end
    if category:
        item["category"] = category
    return item


TRANSFERS = {
    "d01": {
        "mode": "flight",
        "label": "נחיתה בנריטה",
        "detail": "הגעה ל־Narita בשעה 17:40 — נהג פרטי למלון (~1.5 שע׳)",
        "duration": "~1.5 שע׳ לשדה→מלון",
        "fromCity": "Home",
        "toCity": "Tokyo",
    },
    "d06": {
        "mode": "train",
        "label": "טוקיו → האקונה",
        "detail": "Romancecar משינג׳וקו ל־Hakone-Yumoto",
        "duration": "~1 שע׳ 45 דק׳",
        "fromCity": "Tokyo",
        "toCity": "Hakone",
    },
    "d07": {
        "mode": "train",
        "label": "האקונה → קיוטו",
        "detail": "Hakone-Yumoto → Odawara → שינקנסן Hikari לקיוטו + מונית למלון",
        "duration": "~2.5 שע׳",
        "fromCity": "Hakone",
        "toCity": "Kyoto",
    },
    "d11": {
        "mode": "train",
        "label": "קיוטו → הירושימה",
        "detail": "שינקנסן Nozomi לקיוטו→הירושימה + חשמליות למלון",
        "duration": "~2.5 שע׳",
        "fromCity": "Kyoto",
        "toCity": "Hiroshima",
    },
    "d13": {
        "mode": "train",
        "label": "הירושימה → אוסקה",
        "detail": "שינקנסן Nozomi ל־Shin-Osaka + מידוסוג׳י לנמבה",
        "duration": "~2.5 שע׳",
        "fromCity": "Hiroshima",
        "toCity": "Osaka",
    },
    "d16": {
        "mode": "train",
        "label": "אוסקה → טוקיו",
        "detail": "שינקנסן Nozomi לשינגאווה + קייקיו להיגאשי־גינזה",
        "duration": "~3 שע׳ 20 דק׳",
        "fromCity": "Osaka",
        "toCity": "Tokyo",
    },
    "d18": {
        "mode": "flight",
        "label": "טוקיו → הביתה",
        "detail": "המראה מנריטה בשעה 22:30 — לצאת מוקדם לשדה",
        "duration": "להגיע לשדה כ־3 שע׳ לפני",
        "fromCity": "Tokyo",
        "toCity": "Home",
    },
}

DAYS = [
    day("d01", "2026-09-09", "Wednesday", "Tokyo", "JP", "keio-plaza",
        "נחיתה והסתגלות בשינג׳וקו",
        "נחיתה בנריטה ב־17:40, נסיעה עם נהג פרטי למלון Keio Plaza, ושיטוט רגוע בשינג׳וקו להסתגלות לג׳ט לג.",
        "ארוחת ערב מוקדמת באזור המלון / שינג׳וקו.",
        ["narita", "keio-plaza", "shinjuku"],
        [
            "מהשדה למלון (~1.5 שע׳) — נהג פרטי מחכה בנריטה.",
            "שיטוט רגלי באזור שינג׳וקו ליד המלון.",
        ],
        [
            "יום רגוע להסתגלות — בלי לו״ז צפוף.",
            "ארוחת ערב מוקדמת ושינה מוקדמת עוזרות לסנכרון לשעון יפן.",
        ],
        [
            t("17:40", "נחיתה בנריטה", "narita", "איסוף מהשדה על ידי נהג פרטי."),
            t("19:15", "צ׳ק־אין ב־Keio Plaza", "keio-plaza", "בסיס ליד שינג׳וקו."),
            t("20:00", "שיטוט ערב בשינג׳וקו", "shinjuku", "קניות קלות, Godzilla, אווירה אורבנית — בלי לחץ.", "21:30"),
        ]),

    day("d02", "2026-09-10", "Thursday", "Tokyo", "JP", "keio-plaza",
        "שיבויה, מייג׳י והראג׳וקו",
        "יום מלא בשיבויה (מעבר החצייה, מיאשיטה, היקאריה), מקדש מייג׳י, טקשיטה + קאט סטריט, וסיום באומוטסנדו.",
        "קרפ בהראג׳וקו; קפה/צהריים באומוטסנדו.",
        ["shibuya-crossing", "miyashita-park", "shibuya-hikarie", "meiji-jingu", "takeshita", "cat-street", "omotesando"],
        [
            "מלון → שיבויה: יאמאנוטה משינג׳וקו (~20 דק׳).",
            "שיבויה → מייג׳י: יאמאנוטה ליויוגי (~15 דק׳).",
            "מייג׳י → טקשיטה בהליכה (~10 דק׳); קאט + אומוטסנדו בהליכה.",
            "חזרה למלון: יאמאנוטה מהראג׳וקו (~30 דק׳).",
        ],
        [
            "יום עם הליכה מרובה — לתכנן עצירות בקניונים ובתי קפה.",
            "דרכון לקניות Tax Free מעל ¥5,000.",
            "אם הג׳ט לג עדיין מורגש — אפשר לחזור למלון להפסקה קצרה.",
        ],
        [
            t("09:30", "מעבר החצייה שיבויה + האצ׳יקו", "shibuya-crossing", "התחלה מחוץ לתחנת שיבויה."),
            t("10:15", "Miyashita Park", "miyashita-park", "חנויות + פארק על הגג."),
            t("11:00", "Shibuya Hikarie", "shibuya-hikarie", "מרפסת תצפית חינמית בקומה 11."),
            t("12:00", "מקדש מייג׳י", "meiji-jingu", "יער שקט — אפשר לכתוב Ema.", "13:15"),
            t("13:30", "Takeshita + Cat Street", "takeshita", "אופנת רחוב וקרפים בהראג׳וקו.", "15:00"),
            t("15:15", "Omotesando", "omotesando", "שדרה יוקרתית — בוטיקים ובתי קפה.", "17:00"),
            t("17:30", "חזרה למלון", "keio-plaza"),
        ]),

    day("d03", "2026-09-11", "Friday", "Tokyo", "JP", "keio-plaza",
        "יום מלא ב־DisneySea",
        "יום שלם בטוקיו דיסניסי — Rope Drop עד סגירה לפי כרטיסים ושעות הפארק.",
        "ארוחות בתוך הפארק לפי תורים ואזורים.",
        ["disneysea"],
        [
            "רכבת/מונית לדיסניסי מאזור שינג׳וקו — לצאת מוקדם.",
            "לוודא כרטיסים ושעות Rope Drop מראש.",
        ],
        [
            "יום מלא בפארק — נעליים נוחות וטעינת סוללה.",
            "להזמין כרטיסים מראש ולבדוק שעות פתיחה.",
        ],
        [
            t("07:30", "יציאה לדיסניסי", "disneysea", "הגעה מוקדמת ל־Rope Drop."),
            t("09:00", "Tokyo DisneySea — יום מלא", "disneysea", "מתקנים, מופעים וארוחות בפארק.", "20:00"),
            t("21:00", "חזרה למלון", "keio-plaza"),
        ]),

    day("d04", "2026-09-12", "Saturday", "Tokyo", "JP", "keio-plaza",
        "אמייוקו, אקיהברה וגולדן גאי",
        "בוקר בשוק אמייוקו, צהריים/אחה״צ באקיהברה (ארקיידים ו־Maid Café), ובערב אופציה לגולדן גאי בשינג׳וקו.",
        "נשנושים באמייוקו; יקיטורי לפני גולדן גאי (למשל Gekibutori).",
        ["ameyoko", "akihabara", "golden-gai"],
        [
            "מלון → אמייוקו: יאמאנוטה לאוקאצ׳ימאצ׳י (~40 דק׳).",
            "אמייוקו → אקיהברה: יאמאנוטה (~15 דק׳).",
            "חזרה לשינג׳וקו; גולדן גאי ~15 דק׳ הליכה מהמלון.",
        ],
        [
            "באמייוקו להגיע רעבים — דוכנים וטעימות תוך כדי הליכה.",
            "באקיהברה: ארקיידים ו־Maid Café כחוויה קלילה.",
            "בגולדן גאי — אם יש שלט ״יפנית בלבד״ ממשיכים לבר הבא; לעיתים דמי כניסה קטנים.",
        ],
        [
            t("10:00", "שוק אמייוקו", "ameyoko", "אוכל רחוב ואווירת שוק חי (~10:00–20:00).", "12:30"),
            t("13:00", "אקיהברה", "akihabara", "ארקיידים, אלקטרוניקה, אופציונלי Maid Café.", "17:00"),
            t("18:00", "מנוחה במלון / ארוחה", "keio-plaza"),
            t("20:30", "גולדן גאי — לילה בשינג׳וקו", "golden-gai", "ברים קטנים — אם נשאר כוח.", "23:00"),
        ]),

    day("d05", "2026-09-13", "Sunday", "Tokyo", "JP", "keio-plaza",
        "דאיקניאמה, מגורו וניו יורק בר",
        "יום רגוע בשכונות האלגנטיות: T-Site בדאיקניאמה, טיילת נהר מגורו ונקאמגורו, ובערב New York Bar ב־Park Hyatt.",
        "קפה/צהריים בדאיקניאמה או נקאמגורו; קוקטייל בערב בבר.",
        ["daikanyama", "starbucks-reserve", "nakameguro", "ny-bar"],
        [
            "מלון → דאיקניאמה: Fukutoshin ל־Daikan-yama (~30 דק׳).",
            "הליכה לנהר מגורו ונקאמגורו.",
            "חזרה: Toyoko לשינג׳וקו־סאנצ׳ומה (~25 דק׳).",
            "New York Bar — כ־10 דק׳ הליכה מהמלון.",
        ],
        [
            "לקחת את הזמן — שכונות לשיטוט ובתי קפה.",
            "ל־New York Bar: Smart casual; לעיתים תור קצר.",
            "לשלוח מזוודות מראש למלון בקיוטו ולהמשיך להאקונה עם תיק לילה.",
        ],
        [
            t("10:00", "Daikanyama T-Site", "daikanyama", "Tsutaya, עיצוב ובתי קפה.", "12:00"),
            t("12:15", "Starbucks Reserve (אופציונלי)", "starbucks-reserve", "סניף דגל ליד הנהר."),
            t("13:00", "טיילת נהר מגורו + נקאמגורו", "nakameguro", "בוטיקים, גשרים ומסעדות.", "17:00"),
            t("18:00", "חזרה והתארגנות", "keio-plaza"),
            t("20:00", "New York Bar — Park Hyatt", "ny-bar", "נוף וקוקטיילים — Lost in Translation.", "22:00"),
        ]),

    day("d06", "2026-09-14", "Monday", "Hakone", "JP", "kajikaso",
        "האקונה: מוזיאון, אוואקודאני ואגם",
        "יציאה מטוקיו ל־Hotel Kajikaso, מוזיאון הפסלים הפתוח, אוואקודאני, שייט באגם אשי ומקדש האקונה.",
        "ביצים שחורות / גלידה שחורה באוואקודאני; ארוחת ערב במלון/אונסן.",
        ["kajikaso", "open-air", "owakudani", "lake-ashi", "hakone-shrine"],
        [
            "שינג׳וקו → Hakone-Yumoto ב־Romancecar (~1 שע׳ 45 דק׳).",
            "אוטובוס Tozan למוזיאון ולאוואקודאני.",
            "רכבל ל־Togendai + שייט פיראטים ל־Moto-Hakone → מקדש.",
            "חזרה למלון באוטובוס H.",
        ],
        [
            "להתחיל מוקדם — מעברים בהאקונה אורכים זמן.",
            "אם עמוס מדי: לדלג על המוזיאון הפתוח ולהמשיך לאוואקודאני.",
            "לבדוק מזג אוויר לתצפית על פוג׳י.",
        ],
        [
            t("08:00", "יציאה מטוקיו להאקונה", None, "Romancecar ל־Hakone-Yumoto."),
            t("10:00", "צ׳ק־אין / השארת מזוודות", "kajikaso"),
            t("10:45", "מוזיאון הפסלים הפתוח", "open-air", "אמנות + נופי עמק — אופציונלי אם לוח הזמנים צפוף.", "12:30"),
            t("13:15", "אוואקודאני", "owakudani", "עמק געשי, ביצים שחורות, תצפית פוג׳י.", "14:45"),
            t("15:15", "שייט באגם אשי", "lake-ashi", "ספינת פיראטים מ־Togendai ל־Moto-Hakone."),
            t("16:15", "מקדש האקונה", "hakone-shrine", "טוריי באגם + יער.", "17:15"),
            t("18:00", "חזרה למלון ואונסן", "kajikaso"),
        ]),

    day("d07", "2026-09-15", "Tuesday", "Kyoto", "JP", "musse-kyoto",
        "הגעה לקיוטו: נישיקי, גיון ופונטוצ׳ו",
        "מעבר מהאקונה לקיוטו, צ׳ק־אין ב־Hotel Musse, שוק נישיקי, גיון בשעת הזהב, וערב בפונטוצ׳ו.",
        "טעימות בנישיקי; ארוחת ערב בפונטוצ׳ו.",
        ["musse-kyoto", "nishiki", "gion", "yasaka-shrine", "pontocho"],
        [
            "Hakone-Yumoto → Odawara → שינקנסן לקיוטו + מונית למלון (~2.5 שע׳).",
            "נישיקי ~5 דק׳ הליכה מהמלון; גיון ~10 דק׳ מנישיקי.",
            "פונטוצ׳ו בהליכה מהמלון בערב.",
        ],
        [
            "הכל במרחק הליכה מהמלון — אפשר לחזור לנוח.",
            "גיון מומלץ סביב 17:00–18:00 כשהפנסים נדלקים.",
        ],
        [
            t("08:30", "יציאה מהאקונה לקיוטו", None, "רכבת + שינקנסן."),
            t("12:00", "צ׳ק־אין ב־Hotel Musse", "musse-kyoto"),
            t("13:00", "שוק נישיקי", "nishiki", "המטבח של קיוטו — טעימות וקניות מזון.", "15:00"),
            t("16:30", "גיון + מקדש יאסקה", "gion", "Hanami-koji, שירוקאווה, Yasaka.", "18:15"),
            t("19:00", "ערב בפונטוצ׳ו", "pontocho", "מסעדות וברים; הליכה לאורך נהר קאמו.", "21:30"),
        ]),

    day("d08", "2026-09-16", "Wednesday", "Kyoto", "JP", "musse-kyoto",
        "אראשיאמה ו־teamLab Biovortex",
        "בוקר מוקדם באראשיאמה (גשר, במבוק, פארק קופים, טנריו־ג׳י), ואחה״צ ב־teamLab Biovortex ליד תחנת קיוטו.",
        "צהריים קל באראשיאמה; חזרה במונית מה־teamLab (~5 דק׳).",
        ["togetsukyo", "bamboo", "monkey-park", "tenryuji", "teamlab-biovortex"],
        [
            "מלון → אראשיאמה: Hankyu דרך Katsura (~35 דק׳).",
            "חזרה: JR Saga-Arashiyama → Kyoto Station (~45 דק׳) + הליכה ל־teamLab.",
        ],
        [
            "לצאת לפני 08:00 לבמבוק — פחות עומס.",
            "פארק הקופים: עלייה מתונה, נעליים נוחות, כניסה ¥600.",
            "ל־teamLab להגיע 10–15 דק׳ לפני שעת הכניסה.",
        ],
        [
            t("07:30", "יציאה לאראשיאמה", "togetsukyo", "התחלה מוקדמת ליד הגשר."),
            t("08:15", "יער הבמבוק", "bamboo", "לפני העומס."),
            t("09:15", "פארק הקופים Iwatayama", "monkey-park", "עלייה ~20 דק׳ + תצפית.", "10:45"),
            t("11:15", "מקדש טנריו־ג׳י", "tenryuji", "גן זן אונסק״ו."),
            t("12:30", "צהריים ושיטוט באראשיאמה", "togetsukyo"),
            t("15:00", "teamLab Biovortex Kyoto", "teamlab-biovortex", "אמנות דיגיטלית — כניסה מתוזמנת.", "17:30"),
            t("18:00", "חזרה למלון במונית", "musse-kyoto"),
        ]),

    day("d09", "2026-09-17", "Thursday", "Kyoto", "JP", "musse-kyoto",
        "פושימי אינארי, אוג׳י וטקס תה",
        "בוקר בפושימי אינארי, המשך לאוג׳י (גשר, אומוטסנדו מאצ׳ה, ביודו־אין), ואחה״צ טקס תה ב־MAIKOYA.",
        "מאצ׳ה וקינוחים באוג׳י; טקס תה אחר הצהריים.",
        ["fushimi-inari", "uji-bridge", "byodoin-omotesando", "byodoin", "tea-ceremony"],
        [
            "מלון → פושימי: Keihan ל־Fushimi-Inari (~25 דק׳).",
            "פושימי → אוג׳י: JR Nara Line (~30 דק׳).",
            "חזרה למלון עד ~15:00 לטקס התה (~15 דק׳ הליכה/מונית).",
        ],
        [
            "להגיע מוקדם לפושימי — אחד האתרים העמוסים בקיוטו.",
            "נעליים נוחות לעלייה בשערי הטוריי.",
            "לצאת מאוג׳י סביב 15:00 כדי להספיק לטקס התה.",
        ],
        [
            t("07:30", "פושימי אינארי", "fushimi-inari", "שערי טוריי — אפשר רק את החלק התחתון או להמשיך במעלה ההר.", "10:00"),
            t("10:45", "גשר אוג׳י", "uji-bridge", "נהר, בתי תה ונוף ירוק."),
            t("11:30", "Byodo-in Omotesando", "byodoin-omotesando", "רחוב המאצ׳ה — גלידות וקינוחים."),
            t("12:30", "מקדש ביודו־אין", "byodoin", "היכל הפניקס + גנים.", "14:00"),
            t("15:30", "חזרה למלון", "musse-kyoto"),
            t("16:30", "טקס תה — MAIKOYA", "tea-ceremony", "Chanoyu עם הסבר באנגלית.", "18:00"),
        ]),

    day("d10", "2026-09-18", "Friday", "Kyoto", "JP", "musse-kyoto",
        "קיומיזו והיגשיאמה",
        "קיומיזו־dera, סננזקה/ניננזקה, פגודת יאסקה, קודאי־ג׳י, סטארבקס טאטאמי, ושיטוט חופשי בהיגשיאמה.",
        "מאצ׳ה ודוכנים לאורך הסמטאות; קפה בסטארבקס ניננזקה.",
        ["kiyomizu", "sannenzaka", "yasaka-pagoda", "kodaiji", "starbucks-ninenzaka", "higashiyama"],
        [
            "מלון → קיומיזו: אוטובוס 207 ל־Kiyomizumichi (~25 דק׳).",
            "רוב האתרים בהליכה של 5–10 דק׳ זה מזה.",
            "חזרה: אוטובוס 207 מ־Umamachi לשיג׳ו־קווארמאצ׳י.",
        ],
        [
            "להגיע מוקדם לקיומיזו לפני העומס.",
            "הליכה בעליות — נעליים נוחות.",
            "לשלוח מזוודות לאוסקה ולהמשיך להירושימה עם טרולי.",
        ],
        [
            t("08:00", "קיומיזו־dera", "kiyomizu", "מרפסת עץ + מפל Otowa.", "10:00"),
            t("10:15", "סננזקה וניננזקה", "sannenzaka", "חנויות, תה ומזכרות.", "11:30"),
            t("11:45", "פגודת יאסקה", "yasaka-pagoda", "נקודת צילום אייקונית."),
            t("12:30", "מקדש קודאי־ג׳י", "kodaiji", "גנים ובתי תה שקטים."),
            t("13:30", "סטארבקס ניננזקה", "starbucks-ninenzaka", "בית עץ עם טאטאמי."),
            t("14:30", "שיטוט בהיגשיאמה", "higashiyama", "סמטאות, חנויות ושקיעה באזור.", "17:30"),
        ]),

    day("d11", "2026-09-19", "Saturday", "Hiroshima", "JP", "daiwa-hiroshima",
        "הירושימה: גן, פארק השלום וערב",
        "מעבר מקיוטו להירושימה, צ׳ק־אין ב־Daiwa Roynet, גן שוקיין, פארק ומוזיאון השלום, אופציה להונדורי/נאגארקאווה בערב.",
        "צהריים באזור הפארק; ערב בנאגארקאווה אם נשאר כוח.",
        ["daiwa-hiroshima", "shukkeien", "peace-park", "peace-museum", "hondori", "nagarekawa"],
        [
            "קיוטו → הירושימה בשינקנסן Nozomi + חשמליות ל־Chuden-mae (~2.5 שע׳).",
            "מונית קצרה לגן שוקיין ולפארק השלום.",
        ],
        [
            "בגן — קצב רגוע לפני החלק ההיסטורי.",
            "במוזיאון השלום להקדיש שעה–שעתיים.",
            "ערב: נאגארקאווה לברים ואיזאקאיות.",
        ],
        [
            t("08:30", "יציאה מקיוטו להירושימה", None, "שינקנסן Nozomi."),
            t("11:30", "צ׳ק־אין ב־Daiwa Roynet", "daiwa-hiroshima"),
            t("12:30", "גן שוקיין", "shukkeien", "גן נוף מוקטן — שביל סביב האגם.", "14:00"),
            t("14:30", "פארק השלום", "peace-park", "כיפת הפצצה ואנדרטאות."),
            t("15:30", "מוזיאון השלום", "peace-museum", "ביקור עוצמתי — שעה עד שעה וחצי.", "17:00"),
            t("17:30", "הונדורי / מנוחה", "hondori"),
            t("19:30", "ערב בנאגארקאווה (אופציונלי)", "nagarekawa", "חיי לילה של הירושימה."),
        ]),

    day("d12", "2026-09-20", "Sunday", "Hiroshima", "JP", "daiwa-hiroshima",
        "יום באי מיאג׳ימה",
        "יום מלא במיאג׳ימה: אומוטסנדו, מקדש איצוקושימה בגאות, הר מיסן ברכבל, וביקור חוזר בטוריי בשפל.",
        "צדפות, צלופחים ומומיג׳י מנג׳ו ברחוב אומוטסנדו.",
        ["miyajima-omotesando", "miyajima", "misen"],
        [
            "מלון → Miyajimaguchi (~55 דק׳) + מעבורת לאי (~10 דק׳).",
            "הליכה לאומוטסנדו ולמקדש; ~15 דק׳ לרכבל מיסן.",
            "חזרה באותו מסלול (~50 דק׳ מהתחנה למלון).",
        ],
        [
            "לצאת מוקדם לפני העומס.",
            "לבדוק שעות גאות/שפל לטוריי.",
            "אחרי הרכבל יש עוד הליכה לפסגה — נעליים נוחות.",
        ],
        [
            t("07:30", "יציאה למיאג׳ימה", None, "רכבת + מעבורת."),
            t("09:00", "רחוב אומוטסנדו", "miyajima-omotesando", "קניות ואוכל מקומי."),
            t("10:00", "מקדש איצוקושימה — גאות", "miyajima", "טוריי ״צף״ על המים.", "11:30"),
            t("12:00", "הר מיסן — רכבל ותצפית", "misen", "נוף לים סטו + אתרים בודהיסטיים.", "15:00"),
            t("15:30", "טוריי בשפל (אופציונלי)", "miyajima", "הליכה קרוב לשער כשהמים נסוגים."),
            t("17:00", "חזרה להירושימה", "daiwa-hiroshima"),
        ]),

    day("d13", "2026-09-21", "Monday", "Osaka", "JP", "cross-osaka",
        "הגעה לאוסקה: קורומון, טירה ודוטונבורי",
        "מעבר מהירושימה ל־Cross Hotel Osaka, שוק קורומון, טירת אוסקה, ובערב דוטונבורי ממש ליד המלון.",
        "נשנושים בקורומון; טאקויאקי/אוקונומיאקי בדוטונבורי.",
        ["cross-osaka", "kuromon", "osaka-castle", "dotonbori"],
        [
            "הירושימה → Shin-Osaka בשינקנסן + מידוסוג׳י לנמבה (~2.5 שע׳).",
            "קורומון ~15 דק׳ הליכה מהמלון.",
            "טירה: רכבת תחתית ~35 דק׳; דוטונבורי ~5 דק׳ הליכה מהמלון.",
        ],
        [
            "להגיע רעבים לקורומון.",
            "יום עם הליכה — נעליים נוחות; מתחם הטירה גדול.",
            "לחזור למלון לפני ערב בדוטונבורי.",
        ],
        [
            t("08:30", "יציאה מהירושימה לאוסקה", None, "שינקנסן Nozomi."),
            t("11:30", "צ׳ק־אין ב־Cross Hotel", "cross-osaka"),
            t("12:30", "שוק קורומון", "kuromon", "דגים טריים ואוכל רחוב.", "14:00"),
            t("14:45", "טירת אוסקה", "osaka-castle", "מוזיאון, תצפית ופארק.", "17:00"),
            t("18:00", "מנוחה במלון", "cross-osaka"),
            t("19:30", "ערב בדוטונבורי", "dotonbori", "ניאון, גליקו ואוכל רחוב.", "22:00"),
        ]),

    day("d14", "2026-09-22", "Tuesday", "Osaka", "JP", "cross-osaka",
        "נארה ושינסקאי",
        "יום בנארה (פארק, טודאי־ג׳י, קאסוגה, גנים, מוצ׳י), ובערב שינסקאי עם מגדל צוטנקאקו.",
        "קאקינוהה־זושי בנארה; אוכל רחוב בשינסקאי.",
        ["nara-park", "kasuga", "nakatanidou", "shinsekai"],
        [
            "נמבה → Kintetsu-Nara (~45 דק׳).",
            "חזרה לשינסקאי דרך ניפוןבאשי + Sakaisuji (~55 דק׳).",
            "שינסקאי → מלון: מידוסוג׳י מ־Dobutsuen-mae (~25 דק׳).",
        ],
        [
            "לצאת ב־08:00–08:30 לנארה לפני העומס.",
            "האיילים חופשיים — לשמור על שקיות וחפצים.",
            "אפשר לקצר ולהישאר רק בנארה אם מתעייפים.",
        ],
        [
            t("08:00", "יציאה לנארה", "nara-park"),
            t("09:00", "פארק נארה + טודאי־ג׳י", "nara-park", "איילים + בודהה ענק.", "11:30"),
            t("11:45", "קאסוגה טאישה", "kasuga", "מקדש עם פנסים."),
            t("12:45", "מוצ׳י בנקאטנידו / צהריים", "nakatanidou", "מוצ׳י בלייב אם מזדמן."),
            t("14:30", "חזרה לאוסקה — שינסקאי", "shinsekai", "צוטנקאקו, רטרו ואוכל רחוב.", "18:00"),
            t("18:30", "חזרה למלון", "cross-osaka"),
        ]),

    day("d15", "2026-09-23", "Wednesday", "Osaka", "JP", "cross-osaka",
        "טנג׳ינבאשי ואומדה סקיי",
        "רחוב הקניות טנג׳ינבאשי־סוג׳י (הארוך ביפן) עם עצירה בטנמאנגו, ואחה״צ מצפה Umeda Sky Building.",
        "טאקויאקי/קרוקטים בטנג׳ינבאשי; קפה באזור אומדה.",
        ["tenmangu", "tenjinbashi", "umeda-sky"],
        [
            "מלון → טנג׳ינבאשי: Sakaisuji ל־Ogimachi (~25 דק׳).",
            "טנג׳ינבאשי → אומדה סקיי: Osaka Loop ל־Osaka Station (~20 דק׳).",
            "חזרה: מידוסוג׳י מאומדה לנמבה (~30 דק׳).",
        ],
        [
            "להיכנס לחנויות מקומיות קטנות — לא רק רשתות.",
            "דרכון ל־Tax Free מעל ¥5,000.",
        ],
        [
            t("10:00", "אוסקה טנמאנגו", "tenmangu", "לפני תחילת ההליכה ברחוב."),
            t("10:30", "טנג׳ינבאשי־סוג׳י", "tenjinbashi", "שיטוט וקניות לאורך ~2.6 ק״מ.", "13:30"),
            t("14:30", "Umeda Sky Building", "umeda-sky", "מצפה Floating Garden בקומה 39.", "16:30"),
            t("17:30", "חזרה למלון", "cross-osaka"),
        ]),

    day("d16", "2026-09-24", "Thursday", "Tokyo", "JP", "solaria",
        "חזרה לטוקיו: מרונוצ׳י וגינזה",
        "שינקנסן מאוסקה לטוקיו, צ׳ק־אין ב־Solaria Ginza, ויום רגוע במרונוצ׳י ובגינזה בהליכה מהמלון.",
        "צהריים/קפה במרונוצ׳י או בגינזה; קניות Tax Free.",
        ["solaria", "imperial-east", "marunouchi", "ginza"],
        [
            "נמבה → Shin-Osaka → שינקנסן Nozomi לשינגאווה → קייקיו להיגאשי־גינזה (~3 שע׳ 20 דק׳).",
            "כל האטרקציות ביום זה במרחק הליכה מהמלון.",
        ],
        [
            "יום איזי אחרי נסיעה ארוכה — בלי לו״ז צפוף.",
            "דרכון לקניות Tax Free.",
        ],
        [
            t("08:30", "יציאה מאוסקה לטוקיו", None, "שינקנסן Nozomi."),
            t("12:30", "צ׳ק־אין ב־Solaria Ginza", "solaria"),
            t("14:00", "גני הארמון הקיסרי", "imperial-east", "הליכה רגועה באזור הארמון."),
            t("15:00", "מרונוצ׳י", "marunouchi", "Shin Marunouchi, Nakadori, Brick Square.", "16:30"),
            t("17:00", "שיטוט בגינזה", "ginza", "Uniqlo דגל, Ginza Six, Mitsukoshi, Loft.", "19:30"),
        ]),

    day("d17", "2026-09-25", "Friday", "Tokyo", "JP", "solaria",
        "אסאקוסה, קאפאבשי וסקייטרי",
        "אסאקוסה (מרכז מידע, נקאמיסה, סנסוג׳י), רחוב קאפאבשי לכלי מטבח, ומגדל טוקיו סקייטרי + סולמאצ׳י.",
        "ארוחה באסאקוסה (למשל Hatoya / פנקייקים / פירות); קניות בסולמאצ׳י.",
        ["asakusa-info", "asakusa", "kappabashi", "skytree"],
        [
            "מלון → אסאקוסה: קו Asakusa מהיגאשי־גינזה (~20 דק׳).",
            "קאפאבשי ~10 דק׳ הליכה מסנסוג׳י.",
            "סקייטרי: Tobu Skytree Line (~25 דק׳); חזרה ב־Asakusa Line מאושיאגה.",
        ],
        [
            "יום עם הליכה — נעליים נוחות.",
            "עומס בסנסוג׳י לרוב 16:00–18:30 — עדיף מוקדם יותר.",
        ],
        [
            t("09:30", "מרכז המידע באסאקוסה", "asakusa-info", "תצפית בקומה 8."),
            t("10:00", "נקאמיסה + סנסוג׳י", "asakusa", "מקדש קאנון ורחוב המזכרות.", "12:30"),
            t("13:00", "רחוב קאפאבשי", "kappabashi", "סכינים, כלי מטבח ודגמי אוכל.", "14:30"),
            t("15:15", "טוקיו סקייטרי", "skytree", "תצפית + קניות בסולמאצ׳י.", "18:00"),
            t("18:30", "חזרה למלון", "solaria"),
        ]),

    day("d18", "2026-09-26", "Saturday", "Tokyo", "JP", "solaria",
        "צוקיג׳י והמראה מנריטה",
        "בוקר רגוע בשוק צוקיג׳י החיצוני, אריזה וצ׳ק־אאוט, ונסיעה לנריטה לטיסת 22:30.",
        "ארוחת בוקר/סושי בצוקיג׳י; אוכל בשדה לפי הצורך.",
        ["tsukiji", "narita", "solaria"],
        [
            "צוקיג׳י בהליכה/רכבת קצרה מאזור גינזה.",
            "לשדה: להשאיר ~2.5–3 שע׳ דלת־לשער; המראה 22:30.",
        ],
        [
            "לאחר צוקיג׳י — חזרה למלון לאסוף מזוודות.",
            "דרכונים, Visit Japan Web, וזמן ביטחון בשדה.",
        ],
        [
            t("08:30", "שוק צוקיג׳י החיצוני", "tsukiji", "ארוחת בוקר ושיטוט אחרון.", "11:00"),
            t("12:00", "צ׳ק־אאוט ואריזה", "solaria"),
            t("17:00", "יציאה לנריטה", "narita", "להגיע כ־3 שע׳ לפני הטיסה."),
            t("19:30", "שדה התעופה נריטה", "narita", "ביטחון, אוכל, דיוטי־פרי."),
            t("22:30", "המראה הביתה", "narita"),
        ]),
]

TRIP = {
    "title": "יפן 2026",
    "subtitle": "הטיול של משפחת הייטנר",
    "dates": "9–26 בספטמבר, 2026",
    "route": ["Tokyo", "Hakone", "Kyoto", "Hiroshima", "Osaka", "Tokyo"],
    "notes": [
        "מסלול לפי אקסל המשפחה: טוקיו → האקונה → קיוטו → הירושימה → אוסקה → טוקיו.",
        "מלונות: Keio Plaza (טוקיו), Kajikaso (האקונה), Musse (קיוטו), Daiwa Roynet (הירושימה), Cross (אוסקה), Solaria Ginza (טוקיו).",
        "נחיתה בנריטה 17:40 (9/9); המראה מנריטה 22:30 (26/9).",
        "לחצו על מקומות לניווט במפות.",
    ],
}

for d in DAYS:
    if d["id"] in TRANSFERS:
        d["transfer"] = TRANSFERS[d["id"]]
    for item in d.get("timeline") or []:
        if not item.get("category"):
            item["category"] = infer_category(item.get("title", ""), item.get("placeId"), item.get("note", ""))


def dumps(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2)


js = f"""/* Auto-generated — משפחת הייטנר · יפן 9–26 בספט׳ 2026 (מקור: האקסל ב־reference/) */
window.TRIP = {dumps(TRIP)};
window.PLACES = {dumps(PLACES)};
window.DAYS = {dumps(DAYS)};
"""
OUT.write_text(js, encoding="utf-8")
print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")
print(f"Days: {len(DAYS)}, Places: {len(PLACES)}")
print("Transfers:", sum(1 for d in DAYS if d.get("transfer")))
print("Route:", " → ".join(TRIP["route"]))
