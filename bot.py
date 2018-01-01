from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
'''
def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))
'''
def start(bot, update):
       bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

updater = Updater('462046710:AAFS-Xk2jtsGuyyCZa5jqNN5KRxwntSi5ro')



start_handler = CommandHandler('start', start)
dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
#updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()