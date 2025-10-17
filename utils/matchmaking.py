from typing import Optional, Dict, List
from datetime import datetime, timedelta
from utils.logger import logger
from utils.db_manager import DatabaseManager
# إضافة الاستيرادات الجديدة
from messages import (
    CHAT_STARTED_MSG, SEARCHING_MSG,
    get_category_welcome
)
from stickers import (
    SPORTS_STICKER, POLITICS_STICKER,
    MOVIES_STICKER, GAMES_STICKER,
    RANDOM_STICKER, SOCIAL_STICKER
)

class MatchMaking:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.waiting_users: Dict[str, List[Dict]] = {}
        self.search_timeout = timedelta(minutes=5)
        self.topic_stickers = {
            "sports": SPORTS_STICKER,
            "politics": POLITICS_STICKER,
            "movies": MOVIES_STICKER,
            "games": GAMES_STICKER,
            "random": RANDOM_STICKER,
            "social": SOCIAL_STICKER
        }

    def add_to_queue(self, user_id: int, topic: str, gender: str, target_gender: str, bot: TeleBot) -> None:
        """إضافة مستخدم إلى قائمة الانتظار"""
        if topic not in self.waiting_users:
            self.waiting_users[topic] = []
        
        self.waiting_users[topic].append({
            "user_id": user_id,
            "gender": gender,
            "target_gender": target_gender,
            "timestamp": datetime.now()
        })
        
        # إرسال رسالة الترحيب بالموضوع والستيكر المناسب
        if topic in self.topic_stickers:
            try:
                bot.send_sticker(user_id, self.topic_stickers[topic])
            except Exception as e:
                logger.error(f"Error sending topic sticker: {e}")
        
        bot.send_message(user_id, get_category_welcome(topic))
        bot.send_message(user_id, SEARCHING_MSG)
        logger.info(f"User {user_id} added to queue for topic {topic}")