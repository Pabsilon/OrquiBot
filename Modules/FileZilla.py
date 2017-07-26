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
            for child in root:
                if args[0] == child.get('Name'):
                    update.message.reply_text(child.attrib)
        else:
            update.message.reply_text('File not Open!')

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /adminLogIn Username')