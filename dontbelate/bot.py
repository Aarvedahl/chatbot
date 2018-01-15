# A /sethome feature
# /setdestination feature
# /transportation feature
# Also it will ask what time the bus or train leaves to know which exactly you want to catch

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Welcome! I am DoNotBeLate bot. /n What is your home address? /n What is your preferred way of transportation? Walk, Cycle or Car /n What is usually your destination?")

updater = Updater("token")

start_handler = CommandHandler('start', start)
dispatcher = updater.dispatcher
dispatcher.add(start_handler)

updater.start_polling()
updater.idle()

