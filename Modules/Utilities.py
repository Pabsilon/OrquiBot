from Modules.Users import LOGGED_ADMINS
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def getChatIdByUser(user):
        return list(LOGGED_ADMINS.get(user)).chatId


def sendMessage(bot,update,args):
    bot.sendMessage(chat_id=args[0], text = args[1])


def sendMessage(bot,chatId,content):
    bot.sendMessage(chat_id=chatId, text = content)


def broadcastAdmins(bot,content):
    for admin in LOGGED_ADMINS.values():
        sendMessage(bot, admin.get('chatId'), content)
        print("Sending message to " + admin.get('name'))

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