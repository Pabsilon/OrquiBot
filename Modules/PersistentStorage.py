from Modules.Users import LOGGED_ADMINS

def loadAdmins():
    file = open ("admins.orc", "r")
    line = "notEmpty"
    while line != '':
        line = file.readline()
        LOGGED_ADMINS[line.rstrip("\n")]={file.readline().rstrip("\n"),file.readline().rstrip("\n")}
    file.close()
def saveAdmins():
    file = open ("admins.orc", "w")
    for admin in LOGGED_ADMINS:
        file.write(admin + "\n")
        for value in LOGGED_ADMINS[admin]:
            file.write(str(value)+ "\n")
    file.close()