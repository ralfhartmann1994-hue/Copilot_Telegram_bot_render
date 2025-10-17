from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu() -> ReplyKeyboardMarkup:
    """القائمة الرئيسية"""
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(
        KeyboardButton("🔍 البحث عن دردشة"),
        KeyboardButton("🧾 ملفي")
    )
    markup.row(
        KeyboardButton("💰 رصيدي"),
        KeyboardButton("ℹ️ المساعدة")
    )
    return markup

def profile_menu() -> ReplyKeyboardMarkup:
    """قائمة الملف الشخصي"""
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(
        KeyboardButton("✏️ تعديل الاسم"),
        KeyboardButton("🎂 تعديل العمر")
    )
    markup.row(KeyboardButton("🔙 العودة"))
    return markup

def gender_menu() -> ReplyKeyboardMarkup:
    """قائمة اختيار الجنس"""
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(
        KeyboardButton("👦 ذكر"),
        KeyboardButton("👧 أنثى")
    )
    return markup

def topics_menu() -> ReplyKeyboardMarkup:
    """قائمة المواضيع"""
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(
        KeyboardButton("⚽ رياضة"),
        KeyboardButton("🗳️ سياسة")
    )
    markup.row(
        KeyboardButton("🎬 أفلام"),
        KeyboardButton("🎮 ألعاب")
    )
    markup.row(
        KeyboardButton("🎭 عشوائي"),
        KeyboardButton("💬 تعارف")
    )
    markup.row(KeyboardButton("🔙 العودة"))
    return markup

def balance_menu() -> ReplyKeyboardMarkup:
    """قائمة الرصيد"""
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton("💰 احصل على كوينز مجانا"))
    markup.row(KeyboardButton("🔙 العودة"))
    return markup

def chat_menu() -> ReplyKeyboardMarkup:
    """قائمة المحادثة"""
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton("❌ إنهاء المحادثة"))
    markup.row(
        KeyboardButton("👍 تقييم إيجابي"),
        KeyboardButton("👎 تقييم سلبي")
    )
    return markup