from telegram.ext import Updater, CommandHandler
from Modules import Help, Hello, FileZilla, Server,PersistentStorage,Services
import Config
import os
import logging

#Pont was here and didn't want to touch anything more

def isItOn(bot, update):
    response = os.system("ping -c 1 " + Config.HOST_NAME)
    update.message.reply_text('Pinging...')
    if response == 0:
        update.message.reply_text('No luck mate')
    else:
        update.message.reply_text('Server is up!')

if __name__ == "__main__":
    updater = Updater(Config.API_TOKEN)
    logging.basicConfig(format='%(asctime)s %(message)s')
    PersistentStorage.loadAdmins()
    PersistentStorage.loadUsers()
    updater.dispatcher.add_handler(CommandHandler('hello', Hello.hello))
    updater.dispatcher.add_handler(CommandHandler('help', Help.help))
    updater.dispatcher.add_handler(CommandHandler('status', isItOn))
    updater.dispatcher.add_handler(CommandHandler('logIn', FileZilla.login, pass_args=True,))
    updater.dispatcher.add_handler(CommandHandler('logOut', FileZilla.logout))
    updater.dispatcher.add_handler(CommandHandler('Server', Server.handler, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('services', Services.handler, pass_args=True))

    updater.start_polling()
    updater.idle()
