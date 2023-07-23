import os
import telebot

#export BOT_TOKEN=6074258817:AAHx1HQGCSbLytm-3R5zCvPWGKagw7RO3GY

BOT_TOKEN = os.environ.get('6074258817:AAHx1HQGCSbLytm-3R5zCvPWGKagw7RO3GY')
bot = telebot.TeleBot(BOT_TOKEN)



@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "weh ngentot")

bot.infinity_polling()