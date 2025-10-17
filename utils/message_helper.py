from typing import Optional
from telebot import TeleBot
from telebot.types import Message
from utils.logger import logger
from messages import ERROR_MSG
from stickers import *

class MessageHelper:
    @staticmethod
    def send_sticker_safely(bot: TeleBot, chat_id: int, sticker_id: str) -> bool:
        """إرسال ستيكر مع معالجة الأخطاء"""
        try:
            bot.send_sticker(chat_id, sticker_id)
            return True
        except Exception as e:
            logger.error(f"Error sending sticker: {e}")
            return False

    @staticmethod
    def send_message_safely(
        bot: TeleBot,
        chat_id: int,
        text: str,
        reply_markup: Optional[any] = None
    ) -> bool:
        """إرسال رسالة مع معالجة الأخطاء"""
        try:
            bot.send_message(chat_id, text, reply_markup=reply_markup)
            return True
        except Exception as e:
            logger.error(f"Error sending message: {e}")
            bot.send_message(chat_id, ERROR_MSG)
            return False