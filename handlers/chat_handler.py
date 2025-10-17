from telebot import TeleBot
from telebot.types import Message
from utils.error_handler import handle_errors
from utils.logger import logger
from utils.db_manager import DatabaseManager
from typing import Optional
# إضافة الاستيرادات الجديدة
from messages import (
    CHAT_STARTED_MSG, CHAT_ENDED_MSG,
    PARTNER_LEFT_MSG, ERROR_MSG
)
from keyboards import chat_menu, main_menu

class ChatHandler:
    def __init__(self, bot: TeleBot, db: DatabaseManager):
        self.bot = bot
        self.db = db

    @handle_errors
    def handle_chat_message(self, message: Message):
        user_id = message.from_user.id
        user = self.db.get_user(user_id)
        partner_id = user.get('chat_partner')

        if not partner_id:
            self.bot.reply_to(message, "أنت لست في محادثة حالياً.", reply_markup=main_menu())
            return

        try:
            self.bot.forward_message(
                partner_id,
                message.chat.id,
                message.message_id
            )
            logger.info(f"Message forwarded from {user_id} to {partner_id}")
        except Exception as e:
            logger.error(f"Error forwarding message: {e}")
            self.bot.reply_to(message, ERROR_MSG)

    @handle_errors
    def handle_end_chat(self, message: Message):
        user_id = message.from_user.id
        user = self.db.get_user(user_id)
        partner_id = user.get('chat_partner')

        if not partner_id:
            self.bot.reply_to(message, "أنت لست في محادثة حالياً.", reply_markup=main_menu())
            return

        # إنهاء المحادثة لكلا المستخدمين
        self._end_chat_for_both(user_id, partner_id)
        
        # إرسال رسائل الإنهاء
        self.bot.send_message(user_id, CHAT_ENDED_MSG, reply_markup=main_menu())
        self.bot.send_message(partner_id, PARTNER_LEFT_MSG, reply_markup=main_menu())