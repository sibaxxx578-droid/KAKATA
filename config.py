"""
=====================================================================
 DRIP KEY SHOP BOT - CONFIGURATION FILE
=====================================================================
 Fill in every value below before starting the bot.
 This is the ONLY file you need to edit to configure the bot.
=====================================================================
"""

# ---------------------------------------------------------------
# 1) TELEGRAM BOT SETTINGS
# ---------------------------------------------------------------
BOT_TOKEN = "8701375870:AAF_-h0guJUtxKECjCKLrMWimI7wN7V7pPk"

# Telegram numeric user IDs (int) of bot owners / super admins.
# You can find your numeric ID by messaging @userinfobot on Telegram.
ADMIN_IDS = [
    7337091751,
]

# Telegram username (without @) used for manual balance top-ups.
TOPUP_CONTACT_USERNAME = "GIKSSEM16"

# Minimum top-up amount accepted (in USD)
MIN_TOPUP_USD = 5.0

# Binance Pay history API. Add a fresh read-only USER_DATA key and secret locally.
BINANCE_API_KEY = "Z37tSKvADp8FjBiV7nptLMyj3FmGSzEKXXa23Lk7ymhihkZQO10xMfjksAh0buYn"
BINANCE_API_SECRET = "70wFErBl29fb9NQsasP5JG4pK22OuXixMEv5JljZxjb9t1dRqsCQQX5PSYiaicAV"
BINANCE_PAY_UID = "1166125109"
BINANCE_PAY_ASSET = "USDT"
BINANCE_API_BASE_URL = "https://api.binance.com"
BINANCE_PAY_ORDER_TTL_MINUTES = 30


# ---------------------------------------------------------------
# 2) DRIP CLIENT STORE API SETTINGS
# ---------------------------------------------------------------
API_BASE_URL = "https://dripclientstore.shop/api/v1"
API_TOKEN = "48f5e330521b2067bc56202861c1857bec3d5c637589551d98b7c1e1b26d9d4b"

GENERATE_KEY_ENDPOINT = f"{API_BASE_URL}/generate_key.php"
RESET_KEY_ENDPOINT = f"{API_BASE_URL}/reset_key.php"

# The "api" identifier value required by generate/reset endpoints
API_STORE_NAME = "drip"


# ---------------------------------------------------------------
# 3) GOOGLE GEMINI AI SETTINGS (Reseller Support Assistant)
# ---------------------------------------------------------------
GEMINI_API_KEY = "AIzaSyDPrFLuRbtsaiypR5CZIkmNso3X4EoPGtI"
GEMINI_MODEL = "gemini-2.5-pro"

# System instructions given to the AI assistant
GEMINI_SYSTEM_PROMPT = (
    "You are a professional, friendly technical support assistant for "
    "'Drip Key Shop', a Telegram bot that sells license keys to resellers. "
    "Resellers may describe a technical problem in text or send a screenshot. "
    "Always answer with the SIMPLEST possible working solution, in short, "
    "clear steps. If a screenshot is provided, analyze it carefully before "
    "answering. Keep tone helpful, concise, and professional. "
    "Always answer in clear, concise Arabic unless the user explicitly requests another language. "
    "Never reveal API tokens, database internals, or source code."
)


# ---------------------------------------------------------------
# 4) SECURITY / ANTI-SPAM SETTINGS
# ---------------------------------------------------------------
# Max number of button/callback presses allowed within TIME window
SPAM_MAX_ACTIONS = 5
SPAM_TIME_WINDOW_SECONDS = 3

# Max messages allowed within TIME window (chat flood protection)
FLOOD_MAX_MESSAGES = 6
FLOOD_TIME_WINDOW_SECONDS = 4

# Set to True to auto-ban offenders immediately and notify admins
AUTO_BAN_ON_SPAM = True


# ---------------------------------------------------------------
# 5) DATABASE SETTINGS
# ---------------------------------------------------------------
DATABASE_PATH = "database/shop.db"


# ---------------------------------------------------------------
# 6) BRANDING / TEXT SETTINGS
# ---------------------------------------------------------------
BOT_NAME = "DRIP KEY SHOP"
BOT_TAGLINE = "Trusted Digital Key Marketplace"
CURRENCY_SYMBOL = "$"
REFERRAL_REWARD_USD = 0.02

# ---------------------------------------------------------------
# 7) MAINTENANCE MODE (also togglable live from Admin Panel)
# ---------------------------------------------------------------
MAINTENANCE_MODE_DEFAULT = False
