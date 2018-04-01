from xml.etree import ElementTree as ET
from Config import XML_PATH, ADMIN_GROUP, USERS_GROUP, USERS_FOLDER
from Modules.Users import LOGGED_ADMINS, LOGGED_USERS
import logging, os.path, string, random

def adminLogIn(bot, update, args):
    logging.warning("Log in attempt by " + str(update.message.from_user.username))
    #Allows an admin from the ftp to log in.

    try:
        user = args[0]
        alreadyLoggedIn = False;
        #This block checks if the user is already logged in, as either User or Admin and returns a message.
        for dict in LOGGED_ADMINS.values():
            if user in dict:
                alreadyLoggedIn = True
        for dict in LOGGED_USERS.values():
            if user in dict:
                alreadyLoggedIn = True
        if LOGGED_ADMINS.get(update.message.from_user.username):
            #This is only if you're already logged in as an admin
            update.message.reply_text('You\'re already logged in as ' + LOGGED_ADMINS[update.message.from_user.username].get('name'))
        elif LOGGED_USERS.get(update.message.from_user.username):
            #This is only if you're already logged in as a user
            update.message.reply_text('You\'re already logged in as ' + LOGGED_USERS[update.message.from_user.username].get('name'))
        elif alreadyLoggedIn:
            #This only happens if another user is logged with your account (hax much?)
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
                    fname = USERS_FOLDER +'\\' + args[0] + "\\orclogin.txt"
                    if os.path.isfile(fname):
                        if options.text in ADMIN_GROUP:
                            file = open(fname, "r")
                            text = file.readline()
                            if args[1] == text:
                                file.close()
                                os.remove(fname)
                                LOGGED_ADMINS[update.message.from_user.username] = {'name': args[0], 'chatId': update.message.chat_id}
                                update.message.reply_text('Welcome, Admin: ' + args[0] + ' logged as ' + update.message.from_user.username)
                            else:
                                update.message.reply_text('Auth failed. Try removing the orclogin.txt file to generate a new one')
                        elif options.text in USERS_GROUP:
                            file = open(fname, "r")
                            text = file.readline()
                            if args[1] == text:
                                file.close()
                                os.remove(fname)
                                LOGGED_USERS[update.message.from_user.username] = {'name': args[0], 'chatId': update.message.chat_id}
                                update.message.reply_text('Yay! ' + args[0] + ' logged as ' + update.message.from_user.username)

                    else:
                        file = open(fname, "w+")
                        text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                        file.write(text)
                        file.close()
                        update.message.reply_text('A file has been generated in your personal folder. Please, repeat the command adding the content of orclogin.txt from your FTP folder at the end')

            if not exists:
                update.message.reply_text('I don\'t know anyone with that name...')
        else:
            update.message.reply_text('XML file missing. Try updating Config.py')

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /login Username - Remember, Username is Case Sensitive')

def logOut(bot,update):
    logging.warning("Logout attempted by " + str(update.message.from_user.username))
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

