#status reboot distress
import Config, requests


def sendMessage(fromWho,toWho,message):
    #Sends a message from a bot (fromWho) to a person (a chat the bot is in)
    url="http://api.telegram.org/bot"+fromWho+"/sendMessage?chat_id="+toWho+"&text="+message
    requests.get(url)

def start(bot, update,args):
    update.message.reply_text('Hello Wolrd!')

def status(bot,update,args):
    #status should check if diferent services are up or down
    update.message.reply_text('I\'m still here')

def distress(bot,update,args):
    #   update.message.reply_text('If you want to contact the admins text to @Se�orPont')
    if(len(args)>1):
        length = len(args)
        message=message+" and :"
        call=args[2,length-1]
        for x in call:
            message= message +x+" "
    sendMessage(Config.API_TOKEN,Config.DISTRESS_CHAT,message)
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