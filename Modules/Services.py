import psutil
from Config import SERVICES_LIST as servs
from Main import logging



def listprocess(bot,update,args):
    logging.warning("Service listprocess called by " + str(update.message.from_user.username))
    online = []
    for p in psutil.process_iter():
        if p.name() in servs:
            online.append(p.name())
    message = ""
    for s in servs:
        message += s
        if (s in online):
            message += " is Online \n"
        else:
            message += " is Offline \n"
    update.message.reply_text(message)


def handler(bot,update,args):
    #catch-up process to dispatch commands
    print("services called with ",end=' ')
    for arg in args:
        print(arg,  end=' ')
    print("")
    admin=False
    if (admin==True):
        print("There's and admin on the floor")
    if ( len(args)==0 or args[0].lower() == 'help'):
        help(bot,update,args)
    elif (args[0].lower() == 'list'):
        listprocess(bot,update,args)
    else:
        update.message.reply_text("I'm sorry, I don't understand")
    #check other outcomes