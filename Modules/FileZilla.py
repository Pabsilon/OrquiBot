from xml.etree import ElementTree as ET
from Config import XML_PATH,LOGGED_ADMINS

def adminLogIn(bot, update, args):
    #Allows an admin from the ftp to log in.
    try:
        user = args[0]
        if LOGGED_ADMINS.get(update.message.from_user.username):
            update.message.reply_text('You\'re already logged in as ' + LOGGED_ADMINS.get(update.message.from_user.username))
        elif user:
            tree = ET.parse(XML_PATH)
            root = tree.getroot()
            root = root[2]
            exists = False
            for child in root:
                if args[0] == child.get('Name'):
                    exists = True
                    options = child[2]
                    if options.text == 'SuperUsers':
                        LOGGED_ADMINS[update.message.from_user.username]=args[0]
                        update.message.reply_text('Yay! ' + args[0] + ' logged as ' + update.message.from_user.username)
                    else:
                        update.message.reply_text('I don\'t know any admins with that name...')
            if not exists:
                update.message.reply_text('I don\'t know any admins with that name...')
        else:
            update.message.reply_text('XML file missing. Try updating Config.py')

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /adminLogIn Username')