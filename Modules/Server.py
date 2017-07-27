#status reboot distress
import Config, requests

def start(bot, update,args):
    update.message.reply_text('Hello Wolrd!')

def status(bot,update,args):
    #status should check if diferent services are up or down
    update.message.reply_text('I\'m still here')

def distress(bot,update,args):
    #   update.message.reply_text('If you want to contact the admins text to @SeñorPont')
    message = "help, I'm "+update.message.from_user.first_name
    if(len(args)>1):
        length = len(args)
        message=message+" and :"
        call=args[2,length-1]
        for x in call:
            message= message +x+" "
    print ("message: "+message)
    url=str("http://"+"api.telegram.org/bot"+Config.API_TOKEN+"/sendMessage?chat_id="+Config.DISTRESS_CHAT+"&text="+message)
    print(url)
    requests.get(url)



def help(bot,update,args):
    update.message.reply_text("/Server manages the server, you can:\n"+
                              "server start ---> to let the bot know you are there\n"+
                              "server status --> to know what services are up\n"+
                              "server help ----> to print this help\n"+
                              "server distress > to give us a call")

def handler(bot,update,args):
    print("server called with ",end=' ')
    for arg in args:
        print(arg,  end=' ')
    print("")
    if ( len(args)==0 or args[0].lower() == 'help'):
        help(bot,update,args)
    elif (args[0].lower() == 'start'):
        start(bot,update,args)
    elif (args[0].lower() == 'status'):
        status(bot,update,args)
    elif (args[0].lower() == 'distress'):
        distress(bot,update,args)
    else:
        update.message.reply_text("I'm sorry, I don't understand")
    #check other outcomes