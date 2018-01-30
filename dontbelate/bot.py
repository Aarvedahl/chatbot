# A /sethome feature
# /setdestination feature
# /transportation feature
# Also it will ask what time the bus or train leaves to know which exactly you want to catch
# Ask for timezone
from datetime import datetime
import sched, time
import telebot


bot = telebot.TeleBot("518828418:AAFmQrTfRxkXVp_hGpgCbslEtif1lRsYUaQ")
busLeaves = 0
estTimeToBus = 20

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['sethome'])
def set_home(message):
	bot.reply_to(message, "Howdy, your home address has now been set")


@bot.message_handler(commands=['transportation'])
def set_transportation(message):
	bot.reply_to(message, "Howdy, your choice of transportation has now been set")


@bot.message_handler(commands=['setdestination'])
def set_destinaton(message):
	bot.reply_to(message, "Howdy, your destination address has now been set")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	if "My bus leaves" in message.text or "I have got a bus" in message.text or "I am getting there by bus" in message.text:
		messages = message.text.split(" ")
		for i in range(1, len(messages)):
			if messages[i] == "at":
				currentTime = messages[i+1].split(":")
				bot.send_message(message.chat.id, datetime.now())
				date = datetime.now()
				newDate = date.replace(hour=int(currentTime[0]), minute=int(currentTime[1]))
				bot.send_message(message.chat.id, newDate)
				# Tmer set och skicka meddelande när timern är slut
				# Check the users current time and set a callback for the time busLeaves - estTimeToBus
				# Check wether it is 12/24 HOUR
	else:
		bot.reply_to(message, "Your message was not recognized, please see some of the examples")
    # phrase sorter here and if phrase not recognized show examples



bot.polling()
