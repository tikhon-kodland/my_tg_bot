import telebot
from telebot.types import ReactionTypeEmoji
import random
from bot_logic import generate_password

# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("8563550318:AAEBOMVGhgZC6pt4mRKlDt5-af8rZYp3xkQ")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот.\nНапиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['genpass'])
def gen_pass(message):
    password = generate_password(10)
    bot.reply_to(message, password)

@bot.message_handler(func=lambda message: True)
def send_reaction(message):
    emo = ["\U0001F525", "\U0001F917", "\U0001F60E"]  # or use ["🔥", "🤗", "😎"]
    bot.set_message_reaction(message.chat.id, message.id, [ReactionTypeEmoji(random.choice(emo))], is_big=False)


bot.polling()
