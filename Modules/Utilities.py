from Modules.Users import LOGGED_ADMINS


def getChatIdByUser(user):
        return list(LOGGED_ADMINS.get(user))[0]

def sendMessage(bot,update,args):
    bot.sendMessage(chat_id=getChatIdByUser(args[0]), text = args[1])