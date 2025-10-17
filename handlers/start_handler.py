from telebot import TeleBot
from telebot.types import Message
from utils.error_handler import handle_errors
from utils.logger import logger
from utils.db_manager import DatabaseManager
from config import MIN_AGE, MAX_AGE, COINS_NEW_USER, COINS_REFERRAL
# إضافة الاستيرادات الجديدة
from messages import (
    WELCOME_MSG, ASK_NAME, ASK_GENDER, ASK_AGE,
    TOO_YOUNG_MSG, PROFILE_MSG
)
from stickers import (
    WELCOME_STICKER, AFTER_NAME_STICKER,
    NABEEL_YOUNG_STICKER
)
from keyboards import main_menu, gender_menu