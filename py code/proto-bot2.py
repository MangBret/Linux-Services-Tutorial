import logging
import echo
from telegram  import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import pytz
jakarta_timezone = pytz.timezone('Asia/Jakarta')

import serial
import time

ser = serial.Serial('COM5', 9600, timeout=.15) # sesuaikan port ('COM#') dan baud rate

updater = Updater("6074258817:AAHx1HQGCSbLytm-3R5zCvPWGKagw7RO3GY")

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

# Token Bot Telegram
def main():
    #updater = Updater("6074258817:AAHx1HQGCSbLytm-3R5zCvPWGKagw7RO3GY")

    dispatcher = updater.dispatcher

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
    #updater.idle()

# Kirim pesan terjadwal untuk grup
def pesan():
    #bot = Bot(token='6074258817:AAHx1HQGCSbLytm-3R5zCvPWGKagw7RO3GY')
    updater = Updater("6074258817:AAHx1HQGCSbLytm-3R5zCvPWGKagw7RO3GY")

    chat_id = '-874843380'

    a = 25

    if a >= 23:
        message = f"suhu saat ini adalah {a} C\n SUHU TERLALU TINGGI! HARAP SEGERA DICEK"
        updater.pesan(chat_id=chat_id, text=message)
        time.sleep(120)


"""from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler(timezone=pytz.utc)
scheduler.add_job(pesan, 'interval', minutes=2)"""
if __name__ == "__main__":
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        main()

while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip() # Read data until a newline character is reciever

        if data:
            commaIndex = data.find(',') # Find the index of the delimiter
    
            if commaIndex != 1:
                temp_str = data[:commaIndex]
                hum_str = data[commaIndex + 1:]

                temp = float(temp_str)
                hum = float(hum_str)
        
                print(f"Temp: {temp}°C, Hum: {hum}%")
            else:
                print("Invalid data format - no delimiter found")
        else :
           print("no data found")
    
    def pesan():
        #bot = Bot(token='6074258817:AAHx1HQGCSbLytm-3R5zCvPWGKagw7RO3GY')
        #updater = Updater("6074258817:AAHx1HQGCSbLytm-3R5zCvPWGKagw7RO3GY")

        chat_id = '-874843380'        

        if temp >= 23:
            message = f"suhu saat ini adalah {temp} C\n SUHU TERLALU TINGGI! HARAP SEGERA DICEK"
            updater.pesan(chat_id=chat_id, text=message)
            time.sleep(5)
    
    updater.idle()    


    
    







"""try:
    while True:
        pass
except KeyboardInterrupt:
    scheduler.shutdown()"""


