import telebot
import config
import adminPanel

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['find'])
def start(message):
    bot.send_message(message.chat.id, "This is find menu")

@bot.message_handler(commands=['rents'])
def start(message):
    bot.send_message(message.chat.id, "This is menu of a book that u are renting now")

@bot.message_handler(commands=['search'])
def start(message):
    bot.send_message(message.chat.id, "There will be list of all available books")

@bot.message_handler(commands=['adminCheck'])
def start(message):
    bot.send_message(message.chat.id, "Keneke, write ur password")
    adminPanel()


# run()

bot.polling(none_stop=True)
