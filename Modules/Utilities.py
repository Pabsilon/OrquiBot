from Modules.Users import LOGGED_ADMINS


def getChatIdByUser(user):
        return list(LOGGED_ADMINS.get(user))[0]


def sendMessage(bot,update,args):
    bot.sendMessage(chat_id=getChatIdByUser(args[0]), text = args[1])


def sendMessage(bot,chatId,content):
    bot.sendMessage(chat_id=chatId, text = content)


def broadcastAdmins(bot,content):
    for admin in LOGGED_ADMINS.values():
        for api in admin:
            try:
                sendMessage(bot, api, content)
            except:
                print("Sending message to " + api)