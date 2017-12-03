from Modules.Users import LOGGED_ADMINS


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