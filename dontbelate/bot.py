# A /sethome feature
# /setdestination feature
# /transportation feature
# Also it will ask what time the bus or train leaves to know which exactly you want to catch

import telebot

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
    # Bygg en egen phrase sorter here and if phrase not recognized show examples

bot.polling()
