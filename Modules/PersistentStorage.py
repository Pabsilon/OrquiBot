from Modules.Users import LOGGED_ADMINS
import os
from Main import logging


def loadAdmins():
    logging.warning("Loading admins.")
    if os.stat("admins.orc").st_size!=0:
        file = open("admins.orc", "r")
        line = file.readline()
        while line != '':
            LOGGED_ADMINS[line.rstrip("\n")]={'name': file.readline().rstrip("\n"), 'chatId' : file.readline().rstrip("\n")}
            line = file.readline()
        file.close()


def saveAdmins():
    logging.warning("Saving admins."))
    file = open ("admins.orc", "w")
    for admin in LOGGED_ADMINS:
        file.write(admin + "\n")
        file.write(LOGGED_ADMINS[admin].get('name')+"\n")
        test = LOGGED_ADMINS[admin].get('chatId')
        file.write(str(test) + "\n")
    file.close()
