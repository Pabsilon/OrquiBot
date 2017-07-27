from xml.etree import ElementTree as ET
from Config import XML_PATH, ADMIN_GROUP, USERS_GROUP
from Modules.Users import LOGGED_ADMINS, LOGGED_USERS
from random import choice
import hashlib

def adminLogIn(bot, update, args):
    #Allows an admin from the ftp to log in.
    try:
        user = args[0]
        if LOGGED_ADMINS.get(update.message.from_user.username):
            update.message.reply_text('You\'re already logged in as ' + LOGGED_ADMINS.get(update.message.from_user.username))
        elif LOGGED_USERS.get(update.message.from_user.username):
            update.message.reply_text('You\'re already logged in as ' + LOGGED_USERS.get(update.message.from_user.username))
        elif user:
            tree = ET.parse(XML_PATH)
            root = tree.getroot()
            root = root[2]
            exists = False
            for child in root:
                if args[0] == child.get('Name'):
                    exists = True
                    options = child[2]
                    if options.text in ADMIN_GROUP:
                        LOGGED_ADMINS[update.message.from_user.username]=args[0]
                        update.message.reply_text('Welcome, Admin: ' + args[0] + ' logged as ' + update.message.from_user.username)
                    elif options.text in USERS_GROUP:
                        LOGGED_USERS[update.message.from_user.username] = args[0]
                        update.message.reply_text('Yay! ' + args[0] + ' logged as ' + update.message.from_user.username)

            if not exists:
                update.message.reply_text('I don\'t know anyone with that name...')
        else:
            update.message.reply_text('XML file missing. Try updating Config.py')

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /adminLogIn Username')

def logOut(bot,update):
    user = update.message.from_user.username
    try:
        LOGGED_ADMINS.pop(user)
    except KeyError:
        try:
            LOGGED_USERS.pop(user)
        except KeyError:
            update.message.reply_text('Wait a second... You weren\'t event logged in!')
            return
    update.message.reply_text('Bye bye, '+user)
