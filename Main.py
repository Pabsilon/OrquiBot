from telegram.ext import Updater, CommandHandler
from Modules import Help, Hello, FileZilla
import Config
import os

#Pont was here and didn't want to touch anything more
def start(bot, update):
    update.message.reply_text('Hello Wolrd!')


def isItOn(bot, update):
    response = os.system("ping -c 1 " + Config.HOST_NAME)
    update.message.reply_text('Pinging...')
    if response == 0:
        update.message.reply_text('No luck mate')
    else:
        update.message.reply_text('Server is up!')

updater = Updater(Config.API_TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', Hello.hello))
updater.dispatcher.add_handler(CommandHandler('help', Help.help))
updater.dispatcher.add_handler(CommandHandler('status', isItOn))
updater.dispatcher.add_handler(CommandHandler('adminLogIn', FileZilla.adminLogIn, pass_args=True,))

updater.start_polling()
updater.idle()