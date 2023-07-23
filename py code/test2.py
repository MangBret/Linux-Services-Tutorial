import logging
import echo
from telegram  import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


# Start Command
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hallo {user.first_name} ! Lo tuh ngentot!!")


# Stop Command
def stop(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Yeehhh ga penting banget\n gangguin gue aja lo blokk")

# Token Bot Telegram
def main():
    updater = Updater("6074258817:AAHx1HQGCSbLytm-3R5zCvPWGKagw7RO3GY")

    dispatcher = updater.dispatcher

    # Handler command /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Handler command /stop
    dispatcher.add_handler(CommandHandler("stop", stop))

    # Handler pesan text
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    
    # Mulai Bot
    updater.start_polling()

    # Bot idle sampai ctrl + c
    updater.idle()



if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    main()