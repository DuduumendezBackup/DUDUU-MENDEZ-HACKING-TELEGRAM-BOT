from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Replace with your bot token
BOT_TOKEN = "7818915591:AAF1G5KKcZm51N6iuf99IlzIRDFoVsCr2iI"

# Define pages with buttons
PAGES = {
    1: [["Button 1", "Button 2", "Button 3"], ["Button 4", "Button 5", "Button 6"], ["➡️ Next Page"]],
    2: [["Button 7", "Button 8", "Button 9"], ["Button 10", "Button 11", "Button 12"], ["⬅️ Previous Page", "➡️ Next Page"]],
    3: [["Button 13", "Button 14", "Button 15"], ["Button 16", "Button 17", "Button 18"], ["⬅️ Previous Page"]],
}

# Editable messages for each button
MESSAGES = {
    "Button 1": "CAMERA HACKING AND IP ADDRESS\n\n"
    "Click here to start bot of Camera hacking @Prankstdbot",
    "Button 2": "FREE 100 INSTAGRAM LIKES EVERYDAY.\n\n"
    "Get free 100 likes everyday for free click here to Start 👉 @InstagramLikeRoBot",
    "Button 3": (
        "Insta-Breaker is a tool designed for automated login attempts on Instagram using a username and a file containing multiple passwords. "
        "It is intended for ethical use only, such as testing the security of your own Instagram account.\n\n"
        "💵 *INSTALLATION USING TERMUX* COPY AND PASTE THESE COMMANDS:\n\n"
        "`$ pkg update`\n"
        "`$ pkg install python -y`\n"
        "`$ git clone https://github.com/GH05T-HUNTER5/insta-breaker`\n"
        "`$ cd insta-breaker`\n"
        "`$ bash install.sh`\n"
        "`$ insta-breaker`\n\n"
        "The test password should be tested by adding your password on line one, two, three, or four in the file:\n\n"
        "`$ Password.txt`\n\n"
        "Example passwords:\n"
        "```\n"
        "18273939\n"
        "Iwieieie\n"
        "Iejdhdhd\n"
        "Your--pass\n"
        "Jajsndndn\n"
        "```\n\n"
        "*100% Working, POWERED BY DUDUU_MENDEZ*"
    ),
        "Button 4": (
        "How to ban Facebook IDs:\n\n"
        "`$ apt update && apt upgrade`\n"
        "`$ apt install python`\n"
        "`$ apt install git`\n"
        "`$ git clone https://github.com/IlayTamvan/Report`\n"
        "`$ cd Report`\n"
        "`$ ls`\n"
        "`$ unzip Report.zip`\n"
        "`$ python2 Report.py`\n\n"
        "With this tool, you can ban Facebook IDs, but success depends on factors such as how old the ID is. "
        "Newer IDs are banned more easily, while older IDs take more time.\n\n"
        "*Tip:* Only for educational purposes—please do not misuse.\n\n"
        "*BY DUDUU_MENDEZ*"
    ),
    "Button 5": (
        "WhatsApp OTP Lock Method By 〔OG CHAMP〕√\n\n"
        "*Through Termux*\n\n"
        "*Commands:*\n"
        "`$ apt-get update -y`\n"
        "`$ apt-get upgrade -y`\n"
        "`$ pkg install python -y`\n"
        "`$ pkg install git -y`\n"
        "`$ git clone https://github.com/mohsin091143/PERMA-OTP_LOCKS.git`\n"
        "`$ cd PERMA-OTP_LOCKS`\n"
        "`$ pip install requests`\n"
        "`$ pip install rich`\n"
        "`$ ls`\n"
        "`$ python MOHSIN_OTP_LOCK.py`\n\n"
        "*Termux Version*: 0.118.0\n\n"
        "*CREDIT*: DUDUU_MENDEZ"
    ),
     "Button 6": (
        "How to activate Windows 11/10 without License key 🗝\n\n"
        "*Steps:*\n"
        "1. Make sure you are connected to the internet.\n"
        "2. Run `cmd` or open 'Windows PowerShell' as 'Run as administrator.'\n\n"
        "*Then run the following commands one by one:*\n"
        "`slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX`\n"
        "`slmgr /skms kms8.msguides.com`\n"
        "`slmgr /ato`\n\n"
        "4. *Windows Activated.*\n"
        "==================="
    ),
       "Button 7": (
        "🔰 How to Hack WhatsApp By Sending a Link 🔰\n\n"
        "🌀 *OTP Bypass WhatsApp Hacking Method (Termux Phishing Tool)*\n\n"
        "⚠️ *Only For Educational Purposes!*\n\n"
        "*Commands:*\n"
        "`$ git clone https://github.com/Ignitetch/AdvPhishing.git`\n"
        "`$ ls`\n"
        "`$ cd AdvPhishing/`\n"
        "`$ ls`\n"
        "`$ chmod 777 *`\n"
        "`$ ls`\n"
        "`$ ./Linux-Setup.sh`\n"
        "`$ ./AdvPhishing.sh`\n\n"
        "After setup, you will get the name of apps you want to hack. Input the number of the app you want to hack.\n\n"
        "Now you will get a final link. Share the link with your target. They will input their contact details on the phishing site, which you will receive in your Termux app.\n\n"
        "Clone the target's WhatsApp and send an OTP to their number. The target will input the OTP on the website, and you will receive it in Termux. Now use the OTP to log into their WhatsApp.\n\n"
        "*Note*: Always stay online with the victim to send the OTP instantly.\n\n"
        "*CREDIT: MENDEZ*"
    ),
    "Button 8": (
        "😈 *INSTAGRAM LIVESTREAM BANNING METHOD* 😈\n\n"
        "This is *not guaranteed* to work and is shared *only for educational purposes.*\n\n"
        "*Tutorial:*\n"
        "1. Go to your target's livestream.\n"
        "2. Copy the code below and post it in the comments.\n"
        "3. Report the livestream as spam.\n"
        "4. Wait up to 5 minutes, and the livestream may be banned.\n\n"
        "♒ *Code* 👇\n"
        "```\n"
        "ማርቆስ ይስጥልኝ እኔ ይህን መገለጫ የሚያስከፋ ይዘት እና የወንጀል እና ስለዚህ እናንተ ወዲያውኑ ለማስወገድ ተስፋ እና አመሰግናለሁ የብልግና ምስል ማተም ...\n"
        "```\n\n"
        "*CREDIT: MENDEZ*"
    ),
     "Button 9": (
        "How To Hack Android Phone By Its IP Address Using PhoneSploitPro ♦️\n\n"
        "😈 *Commands For Linux:*\n\n"
        "`$ git clone https://github.com/AzeemIdrisi/PhoneSploit-Pro.git`\n"
        "`$ cd PhoneSploit-Pro/`\n"
        "`$ pip install -r requirements.txt`\n"
        "`$ python3 phonesploitpro.py`\n"
    ),
    "Button 10": (
        "*ʜᴏᴡ ᴛᴏ ᴛʀᴀᴄᴋ ᴀɴʏᴏɴᴇ's ʟᴏᴄᴀᴛɪᴏɴ ᴜsɪɴɢ ɪᴘ ᴀᴅᴅʀᴇss ᴀɴᴅ sᴏᴍᴇ ᴅᴇᴛᴀɪʟs ᴜsɪɴɢ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ 💀*\n\n"
        "*ᴄᴏᴍᴍᴀɴᴅs:*\n\n"
        "`$ apt update && apt upgrade`\n"
        "`$ pkg install git`\n"
        "`$ pkg install python3`\n"
        "`$ git clone https://github.com/HunxByts/GhostTrack.git`\n"
        "`$ cd GhostTrack`\n"
        "`$ pip3 install -r requirements.txt`\n"
        "`$ python3 GhostTR.py`\n\n"
        "*ᴊᴜsᴛ ᴄᴏᴘʏ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ɪɴᴛᴏ ᴛᴇʀᴍᴜx*\n\n"
        "> ꧁༺⚔︎MENDEZ҉⚔︎༻꧂"
    ),
      "Button 11": (
        "*HOW TO GET MORE VIEWS ON TIKTOK*\n\n"
        "1️⃣ *FIRST OPEN THE BOT:*\n"
        "[Click here](https://t.me/Free_Tiktok_Views_Robot?start=7407125972)\n\n"
        "2️⃣ *NEXT CLICK BONUS:*\n"
        "You'll get bonus points randomly ranging from *500 to 1000 points*.\n\n"
        "📝 *NOTE:* 1 Point = 1 View\n\n"
        "3️⃣ *TAP ORDER VIEW:*\n"
        "Add your TikTok video link.\n\n"
        "4️⃣ *WAIT FOR 30-50 MINUTES AND CHECK YOUR TIKTOK:*\n"
        "💥 BOOM 💢💣 You're going to rub it in your friends' faces!"
    ),
    "Button 12": "This is the custom message for Button 12.",
    "Button 13": "This is the custom message for Button 13.",
    "Button 14": "This is the custom message for Button 14.",
    "Button 15": "This is the custom message for Button 15.",
    "Button 16": "This is the custom message for Button 16.",
    "Button 17": "This is the custom message for Button 17.",
    "Button 18": "This is the custom message for Button 18.",
}

# Store the current page for each user
current_page = {}
has_joined = {}  # Track whether a user has clicked "Joined to Continue"

async def start(update: Update, context):
    """Handle the /start command."""
    user_id = update.effective_user.id
    current_page[user_id] = 1  # Start on page 1
    has_joined[user_id] = False  # Mark the user as not having joined yet

    # Prompt to join the channel
    await update.message.reply_text(
        "👋 Welcome to the bot! Please consider joining our channel to support us:\n\n"
        "👉 [Duduu Mendez Store](https://t.me/duduu_mendez_store)\n\n"
        "Click 'Joined to Continue' when ready.",
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardMarkup([["Joined to Continue"]], resize_keyboard=True),
    )

async def handle_message(update: Update, context):
    """Handle all user interactions."""
    user_id = update.effective_user.id
    user_text = update.message.text

    # Handle "Joined to Continue" action
    if user_text == "Joined to Continue":
        has_joined[user_id] = True  # Mark the user as having joined
        await show_menu(update, context)
        return

    # Check if the user has clicked "Joined to Continue"
    if not has_joined.get(user_id, False):
        await update.message.reply_text("❓ Invalid choice. Please click 'Joined to Continue'.")
        return

    # Handle navigation and button messages
    if user_text == "➡️ Next Page":
        current_page[user_id] = min(current_page.get(user_id, 1) + 1, len(PAGES))
        await show_menu(update, context)
    elif user_text == "⬅️ Previous Page":
        current_page[user_id] = max(current_page.get(user_id, 1) - 1, 1)
        await show_menu(update, context)
    elif user_text in MESSAGES:
        await update.message.reply_text(MESSAGES[user_text])
    else:
        await update.message.reply_text("❓ Invalid choice. Please use the menu buttons.")

async def show_menu(update: Update, context):
    """Display the menu for the current page."""
    user_id = update.effective_user.id
    page = current_page.get(user_id, 1)
    buttons = PAGES.get(page, [])
    await update.message.reply_text(
        f"📜 Menu Page {page}:",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True),
    )

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()