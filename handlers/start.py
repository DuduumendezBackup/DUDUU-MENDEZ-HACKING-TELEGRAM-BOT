from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Join Channel", url="https://t.me/DUDUU_MENDEZ_HACKING_BOT")],
        [InlineKeyboardButton("I've Joined", callback_data="joined")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome to *DUDUU_MENDEZ_HACKING_BOT*! Please join our channel to start using the bot.",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )