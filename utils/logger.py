import logging
import os
from datetime import datetime

def setup_logger():
    # إنشاء مجلد للسجلات إذا لم يكن موجوداً
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # تكوين التسجيل
    logger = logging.getLogger('telegram_bot')
    logger.setLevel(logging.INFO)

    # تسجيل في ملف
    log_file = os.path.join(log_dir, f'bot_{datetime.now().strftime("%Y%m%d")}.log')
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.INFO)

    # تسجيل في وحدة التحكم
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # تنسيق السجل
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

logger = setup_logger()