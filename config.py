# config.py — إعدادات البوت المحسنة
import os
from typing import Optional

def get_required_env(key: str) -> str:
    """Get required environment variable or raise error"""
    value = os.getenv(key)
    if not value:
        raise RuntimeError(f"Required environment variable {key} is not set")
    return value

def get_optional_env(key: str, default: str) -> str:
    """Get optional environment variable with default"""
    return os.getenv(key, default)

# Telegram Configuration
BOT_TOKEN = get_required_env("BOT_TOKEN")
USE_WEBHOOK = os.getenv("USE_WEBHOOK", "1").lower() in ("1", "true")
WEBHOOK_URL = get_optional_env("WEBHOOK_URL", "")
WEBHOOK_PATH = get_optional_env("WEBHOOK_PATH", "webhook")
PORT = int(get_optional_env("PORT", "10000"))

# Admin Configuration
ADMIN_ID = int(get_optional_env("ADMIN_ID", "0"))
SUPPORT_HANDLE = get_optional_env("SUPPORT_HANDLE", "@MAA2857")

# Economy Configuration
COINS_NEW_USER = int(get_optional_env("COINS_NEW_USER", "100"))
COINS_REFERRAL = int(get_optional_env("COINS_REFERRAL", "50"))
COINS_SEARCH_GIRL = int(get_optional_env("COINS_SEARCH_GIRL", "25"))

# Security Configuration
MAX_DAILY_REFERRALS = int(get_optional_env("MAX_DAILY_REFERRALS", "10"))
MIN_AGE = int(get_optional_env("MIN_AGE", "13"))
MAX_AGE = int(get_optional_env("MAX_AGE", "99"))

# Chat Configuration
CHAT_TIMEOUT_MINUTES = int(get_optional_env("CHAT_TIMEOUT_MINUTES", "30"))
SEARCH_TIMEOUT_MINUTES = int(get_optional_env("SEARCH_TIMEOUT_MINUTES", "5"))

# Logging Configuration
LOG_LEVEL = get_optional_env("LOG_LEVEL", "INFO")