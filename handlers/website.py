# handlers/website.py
from telegram import Update
from telegram.ext import ContextTypes

async def website_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.callback_query.edit_message_text(
        "Enjoy more info about hacking from Mendez website 👉 [Mendez Website](https://mendez-website.vercel.app/)",
        parse_mode="Markdown"
    )