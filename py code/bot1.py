import logging
import echo
from telegram  import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


# Start Command
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"weh {user.first_name} ! Lo tuh ngentot!!")

# Help Command
def help(update: Update, context: CallbackContext):
    help_text = "list command bot\n" \
                "/start - mulai bot\n /help - list perintah\n /stop - memberhentikan bot"
    update.message.reply_text(help_text)

# Stop Command
def stop(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Yeehhh ga penting banget\n gangguin gue aja lo blokk")

def get_chat_id(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    print("Chat ID:", chat_id)

# Token Bot Telegram
def main():
    updater = Updater("6074258817:AAHx1HQGCSbLytm-3R5zCvPWGKagw7RO3GY")

    

    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.all, get_chat_id))
    
    # Handler command /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Handler command /help
    dispatcher.add_handler(CommandHandler("help", help))

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