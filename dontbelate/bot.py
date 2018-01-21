# A /sethome feature
# /setdestination feature
# /transportation feature
# Also it will ask what time the bus or train leaves to know which exactly you want to catch
# Ask for timezone

import telebot

bot = telebot.TeleBot("518828418:AAFmQrTfRxkXVp_hGpgCbslEtif1lRsYUaQ")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	if("My bus leaves at" in message or "I have got a bus" in message or "I am getting there by bus" in message):
		bot.reply_to(message, "Your bus leaves at a certain time")
	bot.reply_to(message, message.text)
    # phrase sorter here and if phrase not recognized show examples
	# Phrase sorter not working
	# examples: My bus leaves at, I have got a bus at, I am getting there by bus

bot.polling()
