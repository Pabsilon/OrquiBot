XML_PATH='c:\\Users\\Pabs\\Desktop\\FileZilla Server.xml'
from xml.etree import ElementTree as ET

def adminLogIn(bot, update, args):
    #Allows an admin from the ftp to log in.
    try:
        user = args[0]
        if user:
            tree = ET.parse(XML_PATH)
            root = tree.getroot()
            root = root[2]
            exists = False
            for child in root:
                if args[0] == child.get('Name'):
                    exists = True
                    options = child[2]
                    if options.text == 'SuperUsers':
                        update.message.reply_text('Yay')
                    else:
                        update.message.reply_text('Wait a second! You\' re not an admin!')
            if not exists:
                update.message.reply_text('I don\'t know anyone with that name...')
        else:
            update.message.reply_text('File not Open!')

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /adminLogIn Username')