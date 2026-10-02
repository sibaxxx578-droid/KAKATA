"""
=====================================================================
 DRIP KEY SHOP BOT — MAIN ENTRY POINT
=====================================================================
 Run this file to start the bot:
     python3 bot.py

 Project structure:
   config.py                -> all configuration (edit this first!)
   database/db.py           -> SQLite database layer
   services/drip_api.py     -> Drip Client Store API integration
   services/ai_support.py   -> Google Gemini AI support integration
   core/state.py            -> conversation state machine
   core/security.py         -> anti-spam / anti-flood engine
   utils/keyboards.py       -> all inline keyboards
   utils/formatting.py      -> decorated message templates
   handlers/common.py       -> /start, main menu
   handlers/store.py        -> store, profile, top-up
   handlers/reseller.py     -> reset key, AI support (reseller-only)
   handlers/admin/*         -> full admin control panel
=====================================================================
"""

import telebot

from config import ADMIN_IDS, API_TOKEN, BOT_TOKEN, BOT_NAME
from core.middleware import GlobalSecurityMiddleware
from database import db
from utils import formatting

from handlers import common, store, reseller
from handlers.admin import panel as admin_panel
from handlers.admin import categories as admin_categories
from handlers.admin import products as admin_products
from handlers.admin import users as admin_users
from handlers.admin import misc as admin_misc
from handlers.admin import giftcodes as admin_giftcodes


missing_settings = []
if not BOT_TOKEN.strip():
    missing_settings.append("BOT_TOKEN")
if not API_TOKEN.strip():
    missing_settings.append("API_TOKEN")
if not ADMIN_IDS:
    missing_settings.append("ADMIN_IDS")

if missing_settings:
    raise RuntimeError(
        "Configure the following settings in config.py before starting the bot: "
        + ", ".join(missing_settings)
    )


bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None, use_class_middlewares=True)

# ---------------------------------------------------------------
# GLOBAL SECURITY MIDDLEWARE (anti-spam / anti-flood / ban guard)
# ---------------------------------------------------------------
bot.setup_middleware(GlobalSecurityMiddleware(bot))


# ---------------------------------------------------------------
# REGISTER ALL HANDLERS
# ---------------------------------------------------------------
common.register(bot)
store.register(bot)
reseller.register(bot)

admin_panel.register(bot)
admin_categories.register(bot)
admin_products.register(bot)
admin_users.register(bot)
admin_misc.register(bot)
admin_giftcodes.register(bot)


@bot.chat_member_handler()
def handle_required_channel_member_update(update):
    if db.get_setting("force_sub_enabled", "0") != "1":
        return
    channel = db.get_setting("force_sub_channel", "")
    chat_username = getattr(update.chat, "username", None)
    if not channel or not chat_username or f"@{chat_username}".casefold() != channel.casefold():
        return
    if update.new_chat_member.status not in ("left", "kicked"):
        return
    result = db.revoke_referral(update.new_chat_member.user.id)
    if result:
        try:
            bot.send_message(
                result["referrer_id"],
                formatting.referral_reversal_notice(
                    result,
                    update.new_chat_member.user,
                    db.get_user_language(result["referrer_id"]),
                ),
            )
        except Exception:
            pass


if __name__ == "__main__":
    print(f"🚀 {BOT_NAME} is starting...")
    print("✅ Database initialized.")
    print("✅ Handlers registered.")
    print("🤖 Bot is now polling for updates...")
    bot.infinity_polling(
        skip_pending=True,
        allowed_updates=["message", "callback_query", "chat_member"],
    )
