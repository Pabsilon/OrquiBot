from xml.etree import ElementTree as ET
from Config import XML_PATH, ADMIN_GROUP, USERS_GROUP
from Modules.Users import LOGGED_ADMINS, LOGGED_USERS


def adminLogIn(bot, update, args):
    #Allows an admin from the ftp to log in.

    try:
        user = args[0]
        alreadyLoggedIn = False;
        for dict in LOGGED_ADMINS.values():
            if user in dict:
                alreadyLoggedIn = True
        for dict in LOGGED_USERS.values():
            if user in dict:
                alreadyLoggedIn = True
        if LOGGED_ADMINS.get(update.message.from_user.username):
            update.message.reply_text('You\'re already logged in as ' + LOGGED_ADMINS[update.message.from_user.username].get('name'))
        elif LOGGED_USERS.get(update.message.from_user.username):
            update.message.reply_text('You\'re already logged in as ' + LOGGED_USERS[update.message.from_user.username].get('name'))
        elif alreadyLoggedIn:
            update.message.reply_text('That user is already logged on by another person. If you think this is a mistake, well.. tough luck.')
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
                        LOGGED_ADMINS[update.message.from_user.username] = {'name': args[0], 'chatId': update.message.chat_id}
                        update.message.reply_text('Welcome, Admin: ' + args[0] + ' logged as ' + update.message.from_user.username)
                    elif options.text in USERS_GROUP:
                        LOGGED_USERS[update.message.from_user.username] = {'name': args[0], 'chatId': update.message.chat_id}
                        update.message.reply_text('Yay! ' + args[0] + ' logged as ' + update.message.from_user.username)

            if not exists:
                update.message.reply_text('I don\'t know anyone with that name...')
        else:
            update.message.reply_text('XML file missing. Try updating Config.py')

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /login Username - Remember, Username is Case Sensitive')

def logOut(bot,update):
    user = update.message.from_user.username
    try:
        LOGGED_ADMINS.pop(user)
    except KeyError:
        try:
            LOGGED_USERS.pop(user)
        except KeyError:
            update.message.reply_text('Wait a second... You aren\'t even logged in!')
            return
    update.message.reply_text('Bye bye, '+user+'!')

