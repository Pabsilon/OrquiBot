from Modules.Users import LOGGED_ADMINS, LOGGED_USERS
import os
import logging

def loadAdmins():
    logging.warning("Loading admins.")
    try:
        if os.stat("admins.orc").st_size!=0:
            file = open("admins.orc", "r")
            line = file.readline()
            while line != '':
                LOGGED_ADMINS[line.rstrip("\n")]={'name': file.readline().rstrip("\n"), 'chatId' : file.readline().rstrip("\n")}
                line = file.readline()
            file.close()
    except FileNotFoundError:
        logging.warning("No admins previously logged in")

def saveAdmins():
    logging.warning("Saving admins.")
    file = open ("admins.orc", "w+")
    for admin in LOGGED_ADMINS:
        file.write(admin + "\n")
        file.write(LOGGED_ADMINS[admin].get('name')+"\n")
        test = LOGGED_ADMINS[admin].get('chatId')
        file.write(str(test) + "\n")
    file.close()


def loadUsers():
    logging.warning("Loading users.")
    try:
        if os.stat("users.orc").st_size != 0:
            file = open("users.orc", "r")
            line = file.readline()
            while line != '':
                LOGGED_USERS[line.rstrip("\n")] = {'name': file.readline().rstrip("\n"), 'chatId': file.readline().rstrip("\n")}
                line = file.readline()
            file.close()
    except FileNotFoundError:
        logging.warning("No users previously logged in")


def saveUsers():
    logging.warning("Saving users.")
    file = open("users.orc", "w+")
    for user in LOGGED_USERS:
        file.write(user + "\n")
        file.write(LOGGED_USERS[user].get('name') + "\n")
        test = LOGGED_USERS[user].get('chatId')
        file.write(str(test) + "\n")
    file.close()
