#status reboot distress

def start(bot, update,args):
    print("I\'m starting")
    update.message.reply_text('Hello Wolrd!')

def status(bot,update,args):
    print ("I'm status")
    #status should check if diferent services are up or down
    update.message.reply_text('I\'m still here')
#def distress(bot,update):
 #   update.message.reply_text('If you want to contact the admins text to @SeñorPont')
def help(bot,update,args):
    print('I\'m helping')
    update.message.reply_text("/Server manages the server, you can:\n"+
                              "/start\tto let the bot know you are there\n"+
                              "/status\tto know what services are up\n"+
                              "/help\tto print this help\n")

def handler(bot,update,args):
    print("server called with ",end=' ')
    for arg in args:
        print(arg,  end=' ')
    print("")
    if (args[0].lower() == 'start'):
        start(bot,update,args)
    if (args[0].lower() == 'status'):
        status(bot,update,args)
    if (args[0].lower() == 'help' or len(args)==0):
        help(bot,update,args)