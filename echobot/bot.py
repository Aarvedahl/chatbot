from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent


def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


updater = Updater('462046710:AAFS-Xk2jtsGuyyCZa5jqNN5KRxwntSi5ro')
j = updater.job_queue
remindtext = ''


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)


def callback_1min(bot, job):
    bot.send_message(chat_id='183358557',
            text='I was going to remind you ' + remindtext + ', have you done it yet?')


def callback(bot, update, args):
    remindmetext = ' '.join(args)
    global remindtext
    remindtext = remindmetext
    bot.send_message(chat_id=update.message.chat_id, text="Ok, I will remind you!")
    j.run_once(callback_1min, 60)

def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    bot.answer_inline_query(update.inline_query.id, results)


def unknown(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Sorry, I didn't understand that command Try something like /start")


start_handler = CommandHandler('start', start)
dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)
callback_handler = CommandHandler('remindme', callback, pass_args=True)
dispatcher.add_handler(callback_handler)
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()
