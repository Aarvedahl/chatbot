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
    bot.send_message(message.chat.id, "To set a destination please write, /setdestination 'Your Destination'")

@bot.message_handler(commands=['sethome'])
def set_home(message):
    bot.send_message(message.chat.id, "To set your home address please write, Sethome 'Your home address'") 
    

@bot.message_handler(commands=['transportation'])
def set_transportation(message):
    bot.send_message(message.chat.id, "To set your form of transportation please write, Settransportation 'Your form of Transportation, Either Car, Walking or Bicycle'") 


@bot.message_handler(commands=['setdestination'])
def set_destinaton(message):
    msg = message.text.split(" ")
    str1 = ' '.join(msg[1:])
    bot.send_message(message.chat.id, "Your destination has been set to " + str1)
     


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if "My bus leaves" in message.text or "I have got a bus" in message.text or "I am getting there by bus" in message.text:
        messages = message.text.split(" ")
        for i in range(1, len(messages)):
            if messages[i] == "at":
                currentTime = messages[i+1].split(":")
                bot.send_message(message.chat.id, datetime.now())
                date = datetime.now()
                newDate = date.replace(hour=int(currentTime[0]), minute=int(currentTime[1]), second=0)
                bot.send_message(message.chat.id, newDate)
                minutesToSleep = time.sleep(60 * ((newDate.hour - date.hour)* 60) + (newDate.minute - date.minute))

    
    # Check the users current time and set a callback for the time busLeaves - estTimeToBus
    # Check wether it is 12/24 HOUR
    else:
        bot.reply_to(message, "Your message was not recognized, please see some of the examples")
    # phrase sorter here and if phrase not recognized show examples



bot.polling()
