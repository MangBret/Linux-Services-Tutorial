from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# Fungsi untuk menampilkan chat ID dari update
def get_chat_id(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    print("Chat ID:", chat_id)

def main():
    # Ganti 'YOUR_BOT_TOKEN' dengan token bot Anda
    updater = Updater("6074258817:AAHx1HQGCSbLytm-3R5zCvPWGKagw7RO3GY")

    # Dapatkan objek Dispatcher
    dispatcher = updater.dispatcher

    # Daftarkan handler untuk mencetak chat ID setiap kali ada pesan masuk
    dispatcher.add_handler(MessageHandler(Filters.all, get_chat_id))

    # Jalankan bot Anda
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
