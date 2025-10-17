import os
from telebot import TeleBot
from flask import Flask, request
from utils.logger import logger
from utils.db_manager import DatabaseManager
from utils.matchmaking import MatchMaking
from handlers.start_handler import StartHandler
from handlers.chat_handler import ChatHandler
from config import (
    BOT_TOKEN, USE_WEBHOOK, WEBHOOK_URL,
    WEBHOOK_PATH, PORT
)
# إضافة الاستيرادات الجديدة
from messages import MAINTENANCE_MSG, ERROR_MSG
from keyboards import main_menu

# إعداد البوت
bot = TeleBot(BOT_TOKEN, parse_mode="HTML")
app = Flask(__name__)

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Server error: {error}")
    return ERROR_MSG, 500

@app.route("/")
def home():
    return "Bot is running"

@app.route(f"/{WEBHOOK_PATH}", methods=["POST"])
def webhook():
    try:
        update = bot.process_new_updates([
            telebot.types.Update.de_json(
                request.stream.read().decode('utf-8')
            )
        ])
        return "OK"
    except Exception as e:
        logger.error(f"Webhook error: {e}")
        return ERROR_MSG, 500