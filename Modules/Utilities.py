from Modules.Users import LOGGED_ADMINS, LOGGED_USERS
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging


def getChatIdByUser(user):
        return list(LOGGED_ADMINS.get(user)).chatId


def sendMessage(bot,update,args):
    bot.sendMessage(chat_id=args[0], text = args[1])


def sendMessage(bot,chatId,content):
    bot.sendMessage(chat_id=chatId, text = content)


def broadcastAdmins(bot,content):
    logging.warning("Sending a message to all logged Admins: " + str(LOGGED_ADMINS.values()))
    logging.warning(content)
    for admin in LOGGED_ADMINS.values():
        sendMessage(bot, admin.get('chatId'), content)
        print("Sending message to " + admin.get('name'))

def broadcastUsers(bot, content):
    logging.warning("Sending a message to all logged Users: " + str(LOGGED_USERS.values()))
    logging.warning(content)
    for user in LOGGED_USERS.values():
        sendMessage(bot, user.get('chatId'), content)
        print("Sending message to " + user.get('name'))

def askAdminsYesOrNo(bot):
    for admin in LOGGED_ADMINS.values():
        keyboard = [[InlineKeyboardButton("Yes", callback_data='1'),
                     InlineKeyboardButton("No", callback_data='2')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        try:
            bot.sendMessage(chat_id=admin.get('chatId'), reply_markup=reply_markup, text="test")
        except Exception as e:
            print(e.__doc__)
            print(e.message)