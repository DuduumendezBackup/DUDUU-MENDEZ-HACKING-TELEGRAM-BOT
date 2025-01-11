# bot.py
import os
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from dotenv import load_dotenv
from utils.logging import setup_logging
from handlers import (
    start,
    joined,
    camera_hacking,
    free_instagram_likes,
    instagram_hacking,
    facebook_hacking,
    whatsapp_hacking,
    website_info
)
import pytz

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Set up logging
logger = setup_logging()

async def main() -> None:
    # Build the application
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Set the timezone
    application.job_queue.scheduler.timezone = pytz.UTC

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(joined, pattern="joined"))
    application.add_handler(CallbackQueryHandler(camera_hacking, pattern="camera_hacking"))
    application.add_handler(CallbackQueryHandler(free_instagram_likes, pattern="free_instagram_likes"))
    application.add_handler(CallbackQueryHandler(instagram_hacking, pattern="instagram_hacking"))
    application.add_handler(CallbackQueryHandler(facebook_hacking, pattern="facebook_hacking"))
    application.add_handler(CallbackQueryHandler(whatsapp_hacking, pattern="whatsapp_hacking"))
    application.add_handler(CallbackQueryHandler(website_info, pattern="mendez_website"))

    # Start the bot
    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    import threading

    def run_bot():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main())
        loop.close()

    threading.Thread(target=run_bot).start()