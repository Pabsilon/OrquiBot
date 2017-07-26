#status reboot distress

def start(bot, update):
    update.message.reply_text('Hello Wolrd!')

def status(bot,update):
    update.message.reply_text('I\'m still here')
#def distress(bot,update):
 #   update.message.reply_text('If you want to contact the admins text to @SeñorPont')
def help(bot,update):
    print('help')

def handler(bot,update,message):
    print('handler')