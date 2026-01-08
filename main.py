import telebot
from telebot.types import ReactionTypeEmoji
import random
import os

# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("8563550318:AAEBOMVGhgZC6pt4mRKlDt5-af8rZYp3xkQ")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот.\nНапиши что-нибудь!")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    imgs = os.listdir(r'C:\Users\rearzty\Desktop\my_project\meme_bot\images')
    with open(fr'C:\Users\rearzty\Desktop\my_project\meme_bot\images\{random.choice(imgs)}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)


bot.polling()
