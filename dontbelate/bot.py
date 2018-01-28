# A /sethome feature
# /setdestination feature
# /transportation feature
# Also it will ask what time the bus or train leaves to know which exactly you want to catch
# Ask for timezone

import telebot

bot = telebot.TeleBot("518828418:AAFmQrTfRxkXVp_hGpgCbslEtif1lRsYUaQ")
busLeaves = 0

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	if "My bus leaves" in message.text or "I have got a bus" in message.text or "I am getting there by bus" in message.text:
		bot.reply_to(message, "Your bus leaves at a certain time")
		messages = message.text.split(" ")
		for i in range(1, len(messages)):
			if messages[i] == "at":
				bot.send_message(message.chat.id, "We have found the time")
				global busLeaves
				busLeaves = messages[i+1]
				bot.send_message(message.chat.id, "The time is " + messages[i+1])
	else:
		bot.reply_to(message, "Your message was not recognized, please see some of the examples")
    # phrase sorter here and if phrase not recognized show examples
	# Phrase sorter not working

bot.polling()
