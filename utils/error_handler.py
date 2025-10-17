from functools import wraps
from utils.logger import logger
from telebot.types import Message
from typing import Callable, Any

def handle_errors(func: Callable) -> Callable:
    """مزخرف لمعالجة الأخطاء في معالجات البوت"""
    @wraps(func)
    def wrapper(message: Message, *args: Any, **kwargs: Any) -> Any:
        try:
            return func(message, *args, **kwargs)
        except Exception as e:
            user_id = message.from_user.id if message and message.from_user else "Unknown"
            logger.error(f"Error in {func.__name__} for user {user_id}: {str(e)}", exc_info=True)
            # إرسال رسالة خطأ للمستخدم
            try:
                bot = kwargs.get('bot')
                if bot:
                    bot.reply_to(message, "عذراً، حدث خطأ. الرجاء المحاولة مرة أخرى لاحقاً.")
            except:
                logger.error("Failed to send error message to user", exc_info=True)
    return wrapper