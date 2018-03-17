import psutil
from Config import SERVICES_LIST, SERVICES_LOCATION, SERVICES_SHUTDOWN
from Modules.Server import cmd
import logging

LANCHED_SERVICES = {}


def listprocess(bot,update,args):
    logging.warning("Service listprocess called by " + str(update.message.from_user.username))
    online = []
    for p in psutil.process_iter():
        if p.name() in SERVICES_LIST:
            online.append(p.name())
    message = ""
    for s in SERVICES_LIST:
        message += s
        if (s in online):
            message += " is Online \n"
        else:
            message += " is Offline \n"
    update.message.reply_text(message)


def launchservice(bot, update, args):
    logging.warning("Service launchservice called by " + str(update.message.from_user.username))
    args.pop(0)
    if args[0] in SERVICES_LIST:
        tolaunch = args[0]
        cmd(update, SERVICES_LOCATION[tolaunch])

    else:
        update.message.reply_text("I'm sorry, that service is not configured, or doesn't exist")


def handler(bot,update,args):
    #catch-up process to dispatch commands
    print("services called with ",end=' ')
    for arg in args:
        print(arg,  end=' ')
    print("")
    if len(args) == 0 or args[0].lower() == 'help':
        help(bot,update,args)
    elif args[0].lower() == 'list':
        listprocess(bot, update, args)
    elif args[0].lower() == 'launch':
        launchservice(bot, update, args)
    else:
        update.message.reply_text("I'm sorry, I don't understand")
    #check other outcomes