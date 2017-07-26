#status reboot distress

def start(bot, update,args):
    update.message.reply_text('Hello Wolrd!')

def status(bot,update,args):
    #status should check if diferent services are up or down
    update.message.reply_text('I\'m still here')

#def distress(bot,update):
 #   update.message.reply_text('If you want to contact the admins text to @SeñorPont')

def help(bot,update,args):
    update.message.reply_text("/Server manages the server, you can:\n"+
                              "/server start\tto let the bot know you are there\n"+
                              "/status\tto know what services are up\n"+
                              "/help\tto print this help\n")

def handler(bot,update,args):
    print("server called with ",end=' ')
    for arg in args:
        print(arg,  end=' ')
    print("")
    if ( len(args)==0 or args[0].lower() == 'help'):
        help(bot,update,args)
    if (args[0].lower() == 'start'):
        start(bot,update,args)
    if (args[0].lower() == 'status'):
        status(bot,update,args)