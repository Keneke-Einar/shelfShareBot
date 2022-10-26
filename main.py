from datetime import time
from telebot import apihelper, types
import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


# handlers

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    btn1 = types.InlineKeyboardButton("User", callback_data='user')
    btn2 = types.InlineKeyboardButton("Admin", callback_data='user')

    markup.add(btn1, btn2)

    mess = f"<b>Enter as</b>:"
    bot.send_message(message.chat.id, mess, reply_markup=markup)


@bot.message_handler(commands=['idCheck'])
def idCheck(message):
    bot.send_message(message.chat.id, f"ID is - {message.from_user.id}")

# run()

while True:
    try:
        bot.polling(none_stop=True)
        apihelper.proxy = {
            'https': 'socks5h://165.227.79.99:7497'
        }

    except Exception as e:
        print(e)
        time.sleep(15)
