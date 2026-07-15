import telebot
from telebot import types
import time
import sys

TOKEN = "8891115599:AAE6yA19GYrJcGhoHyG8nsKcnFcuD4pcreE"
ADMIN_ID = 1627756188

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("📩 Написати майстру", url="https://t.me/Scrapzik")
    markup.add(btn)
    
    bot.send_message(
        message.chat.id,
        "📸 Вітаю! Я бот для ретуші фото.\n\n"
        "💰 Ціна: 100 грн/фото\n"
        "🎁 Перше фото — БЕЗКОШТОВНО!\n\n"
        "👇 Натисни кнопку нижче і надішли фото в особисті повідомлення:",
        reply_markup=markup
    )

@bot.message_handler(commands=['price'])
def price(message):
    bot.send_message(
        message.chat.id,
        "💰 ПРАЙС-ЛИСТ:\n\n"
        "📷 1 фото — 100 грн\n"
        "📸 5 фото — 400 грн (знижка 20%)\n"
        "🎞️ 10 фото — 700 грн (знижка 30%)\n\n"
        "⚡️ Перше фото завжди БЕЗКОШТОВНЕ!"
    )

print("✅ Бот запущено!")
bot.infinity_polling()
