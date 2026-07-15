import telebot
from telebot import types
import time

# ТВІЙ ТОКЕН (отримай новий у BotFather, якщо цей не працює)
TOKEN = "8891115599:AAE6yAl9GYrJCGhohYg8nsWcnFcuD4pcreE"
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

# Запуск з обробкою помилок
while True:
    try:
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        print(f"Помилка: {e}")
        time.sleep(5)
