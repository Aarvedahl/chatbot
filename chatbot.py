from telegram.ext import Updater
updater = Updater(token=462046710:AAFS-Xk2jtsGuyyCZa5jqNN5KRxwntSi5ro)
dispatcher = updater.dispatcher
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


