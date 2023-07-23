import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import pytz
import serial
import time
import echo

# Pengaturan zona waktu
jakarta_timezone = pytz.timezone('Asia/Jakarta')

# Inisialisasi koneksi ke sensor
ser = serial.Serial('COM5', 9600, timeout=.15) # sesuaikan port ('COM#') dan baud rate

# Inisialisasi bot
updater = Updater("6074258817:AAHx1HQGCSbLytm-3R5zCvPWGKagw7RO3GY")

# Start Command
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"hallo {user.first_name} ! Gunakan /help untuk melihat list perintah.")

# Help Command
def help(update: Update, context: CallbackContext):
    help_text = "list command bot\n" \
                "/start - mulai bot\n /help - list perintah\n  /cek - Cek suhu saat ini\n /stop - memberhentikan bot"
    update.message.reply_text(help_text)

# Cek Command
def cek(update: Update, context: CallbackContext):
    cek_text = f"suhu saat ini adalah {temp} °C\n" \
                f"klembaban saat ini adalah {hum} %"
    update.message.reply_text(cek_text)

# Stop Command
def stop(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"I will always comeback")

# Token Bot Telegram
def main():
    dispatcher = updater.dispatcher

    # Handler command /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Handler command /help
    dispatcher.add_handler(CommandHandler("help", help))

    # Handler command /cek
    dispatcher.add_handler(CommandHandler("cek", cek))

    # Handler command /stop
    dispatcher.add_handler(CommandHandler("stop", stop))

    # Handler pesan text
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Mulai Bot
    updater.start_polling()

# Kirim pesan terjadwal untuk grup
def pesan(bot):
    chat_id = '-956376415'

    if temp >= 23:
        message = f"suhu saat ini adalah {temp} C\n SUHU TERLALU TINGGI! HARAP SEGERA DICEK"
        bot.send_message(chat_id=chat_id, text=message)

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    main()

    # Inisialisasi scheduler
    from apscheduler.schedulers.background import BackgroundScheduler
    scheduler = BackgroundScheduler(timezone=pytz.utc)
    scheduler.add_job(pesan, 'interval', minutes=2, args=(updater.bot,))

    # Jalankan scheduler
    scheduler.start()

    try:
        while True:
            if ser.in_waiting > 0:
                data = ser.readline().decode().strip() # Read data until a newline character is received

                if data:
                    commaIndex = data.find(',') # Find the index of the delimiter

                    if commaIndex != -1:
                        temp_str = data[:commaIndex]
                        hum_str = data[commaIndex + 1:]

                        temp = float(temp_str)
                        hum = float(hum_str)

                        print(f"Temp: {temp}°C, Hum: {hum}%")
                    #else:
                    #    print("Invalid data format - no delimiter found")
                #else:
                    #print("No data found")

                time.sleep(5)

    except KeyboardInterrupt:
        scheduler.shutdown()
