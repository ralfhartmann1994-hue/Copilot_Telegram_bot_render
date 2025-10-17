from typing import Dict, Any, Optional
from datetime import datetime, timedelta
import pymongo
from utils.logger import logger

class DatabaseManager:
    def __init__(self, mongo_uri: str):
        self.client = pymongo.MongoClient(mongo_uri)
        self.db = self.client.telegram_bot
        self.users = self.db.users
        self.chats = self.db.chats
        self.setup_indexes()

    def setup_indexes(self):
        """إعداد الفهارس لتحسين الأداء"""
        self.users.create_index("user_id", unique=True)
        self.users.create_index("referral_code", unique=True)
        self.chats.create_index([("user1_id", 1), ("user2_id", 1)])

    def get_user(self, user_id: int) -> Optional[Dict[str, Any]]:
        """جلب معلومات المستخدم"""
        return self.users.find_one({"user_id": user_id})

    def update_user(self, user_id: int, updates: Dict[str, Any]) -> bool:
        """تحديث معلومات المستخدم"""
        try:
            self.users.update_one(
                {"user_id": user_id},
                {"$set": updates},
                upsert=True
            )
            return True
        except Exception as e:
            logger.error(f"Error updating user {user_id}: {e}")
            return False

    def add_coins(self, user_id: int, amount: int) -> bool:
        """إضافة عملات للمستخدم"""
        try:
            self.users.update_one(
                {"user_id": user_id},
                {"$inc": {"coins": amount}}
            )
            return True
        except Exception as e:
            logger.error(f"Error adding coins for user {user_id}: {e}")
            return False

    def create_chat(self, user1_id: int, user2_id: int, topic: str) -> str:
        """إنشاء محادثة جديدة"""
        chat_id = f"{user1_id}_{user2_id}_{datetime.now().timestamp()}"
        self.chats.insert_one({
            "chat_id": chat_id,
            "user1_id": user1_id,
            "user2_id": user2_id,
            "topic": topic,
            "started_at": datetime.now(),
            "status": "active"
        })
        return chat_id

    def end_chat(self, chat_id: str) -> bool:
        """إنهاء محادثة"""
        try:
            self.chats.update_one(
                {"chat_id": chat_id},
                {
                    "$set": {
                        "status": "ended",
                        "ended_at": datetime.now()
                    }
                }
            )
            return True
        except Exception as e:
            logger.error(f"Error ending chat {chat_id}: {e}")
            return False