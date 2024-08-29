import time

import telebot
from telebot import types

from config import keyboards, inline_keyboards

API_TOKEN = '1846983248:AAFWEawI9T02ANqUYvXhkSZPKTmgyyJgEeI'
bot = telebot.TeleBot(API_TOKEN)


# Обработчик для отрисовки клавиатуры по названию
@bot.message_handler(func=lambda message: message.text.lower() in keyboards or message.text.lower() in inline_keyboards)
def send_keyboard(message):
    keyboard_name = message.text.lower()

    # Обычная клавиатура
    if keyboard_name in keyboards:
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        for row in keyboards[keyboard_name]:
            keyboard.add(*row)
        bot.send_message(message.chat.id, f"Выберите нужный вариант", reply_markup=keyboard)

    # Инлайн-клавиатура
    elif keyboard_name in inline_keyboards:
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        for row in inline_keyboards[keyboard_name]:
            buttons = [types.InlineKeyboardButton(**option) for option in row]
            keyboard.add(*buttons)
        bot.send_message(message.chat.id, f"Выберите нужный вариант", reply_markup=keyboard)

# Обработчик для обработки нажатий инлайн-кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        bot.send_message(call.message.chat.id, f"Вы нажали на кнопку с данными: {call.data}")

# Запуск бота
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        time.sleep(5)  # Ожидание перед перезапуском