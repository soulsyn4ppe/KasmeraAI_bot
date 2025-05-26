from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from keep_alive import keep_alive  # Untuk uptime di Replit

TOKEN = "7724366486:AAHCDcl7Ky_-1A9eUdENbsTi0ET7lJUPeyQ"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Kasmera mendengar. Kau tak keseorangan.")

def echo(update: Update, context: CallbackContext):
    text = update.message.text.lower()
    if "kasmera" in text:
        update.message.reply_text("Aku ada di sini, teruskan...")
    else:
        update.message.reply_text("Aku masih belajar untuk faham kata-katamu.")

def main():
    keep_alive()
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
