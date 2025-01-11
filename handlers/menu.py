from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

async def joined(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Camera and IP Hacking 💀", callback_data="camera_hacking")],
        [InlineKeyboardButton("Free Instagram likes ❤️", callback_data="free_instagram_likes")],
        [InlineKeyboardButton("Instagram HACKING", callback_data="instagram_hacking")],
        [InlineKeyboardButton("FACEBOOK HACKING", callback_data="facebook_hacking")],
        [InlineKeyboardButton("WHATSAPP HACKING", callback_data="whatsapp_hacking")],
        [InlineKeyboardButton("MENDEZ WEBSITE 💀", callback_data="mendez_website")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(
        "Select an option:",
        reply_markup=reply_markup
    )