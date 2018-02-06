from datetime import datetime
import time
import telebot
import googlemaps


bot = telebot.TeleBot("518828418:AAFmQrTfRxkXVp_hGpgCbslEtif1lRsYUaQ")
gmaps = googlemaps.Client(key="AIzaSyBc6xZkMQRCcTCqUW2qp1uPqI4NwJdmYFA")
home = ""
destination = ""
transportation = ""

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
    bot.send_message(message.chat.id, "To set a destination please write, /setdestination 'Your Destination'")
    bot.send_message(message.chat.id, "To set your form of transportation please write, /settransportation 'Your form of Transportation, Either Driving, Walking or Bicycling'")
    bot.send_message(message.chat.id, "To set your home address please write, /sethome 'Your home address'")


@bot.message_handler(commands=['sethome'])
def set_home(message):
    msg = message.text.split(" ")
    str1 = ' '.join(msg[1:])
    bot.send_message(message.chat.id, "Your home has been set to " + str1)
    global home
    home = str1


@bot.message_handler(commands=['settransportation'])
def set_transportation(message):
    msg = message.text.split(" ")
    str1 = ' '.join(msg[1:])
    bot.send_message(message.chat.id, "Your form of transportation has been set to " + str1)
    global transportation
    transportation = str1.lower()


@bot.message_handler(commands=['setdestination'])
def set_destinaton(message):
    msg = message.text.split(" ")
    str1 = ' '.join(msg[1:])
    bot.send_message(message.chat.id, "Your destination has been set to " + str1)
    global destination
    destination = str1


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if "My bus leaves" in message.text or "I have got a bus" in message.text or "I am getting there by bus" in message.text:
        global home, transportation, destination
        if not home or not transportation or not destination:
            bot.send_message(message.chat.id, "You have not set all of your variables, please try setting them again")
        else:
            messages = message.text.split(" ")
            for i in range(1, len(messages)):
                if messages[i] == "at":
                    currentTime = messages[i+1].split(":")
                    date = datetime.now()
                    global estTimeToBus
                    newDate = date.replace(hour=int(currentTime[0]), minute=int(currentTime[1]), second=0)
                    bot.send_message(message.chat.id, "I will remind you when you need to leave from you to do not miss your bus/train")
                    test = gmaps.distance_matrix(home, destination, mode=transportation)
                    duration = test['rows'][0]['elements'][0]['duration']
                    bot.send_message(message.chat.id, "It is going to take you about " + duration['text'] + " to reach your destination")
                    time.sleep(60 * ((newDate.hour - date.hour)* 60) + (newDate.minute - (2 + date.minute + (duration['value']/60))))
                    bot.send_message(message.chat.id, "You need to leave now to do not miss your bus")
                else:
                    bot.send_message(message.chat.id, "Message was not recognized please write at what time your bus leaves")
    else:
        bot.reply_to(message, "Your message was not recognized, please see some of the examples by typing /start or /help")


bot.polling()
