import Config
import socket
import pythoncom
import wmi
from Modules.Users import LOGGED_ADMINS
import subprocess
import Modules.Utilities as Utils
from pexpect import popen_spawn
from Modules.PersistentStorage import saveAdmins
from Main import logging


def sizeof_fmt(num, suffix='B'):
    #basic function to display human ready numbers
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def status(bot,update,args):
    #status should check if diferent services are up or down
    #eventually it should call torrent.up() and every module should know how to 
    #check itself. some exceptions are orquibot witch cheks himself by executing and
    #ssh witch wont have a module and will be managed by /server. It is checkede waiting
    #for a tcp open port at the correct place, if it is something else it will do false positive
    logging.warning("Server status called by " + str(update.message.from_user.username))
    update.message.reply_text('⚙️Orquibot   ✅')

    #Torrent
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    torrent = sock.connect_ex((str(Config.HOST_NAME), 8080))
    if torrent == 0:
        update.message.reply_text("⛵️Torrent    ✅")
    else:
        update.message.reply_text("⛵️Torrent    ❌")
    #SSH
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssh = sock.connect_ex((str(Config.HOST_NAME), 22022))
    if ssh == 0:
        update.message.reply_text("🔌ssh        ✅")
    else:
        update.message.reply_text("🔌ssh        ❌")
    update.message.reply_text("🚧Nothing more🚧")


def distress(bot, update, args):
    #We generate the distress message that we will send to the admins
    logging.warning("Server distress called by " + str(update.message.from_user.username))
    message = "Help, I'm " + update.message.from_user.first_name
    if len(args) > 1:
        message = message + " and : "
        call = args[1:len(args)]
        for x in call:
            message = message + x + " "
    #Message is sent to all the admins and the user is notified
    Utils.sendMessage(bot, Config.DISTRESS_CHAT, message)
    update.message.reply_text("An administrator has been notified.")


def reboot(bot, update, args):
    #Non admins won't be able to reboot the server
    logging.warning("Server reboot called by " + str(update.message.from_user.username))
    test = LOGGED_ADMINS.get(update.message.from_user.username)
    if not LOGGED_ADMINS.get(update.message.from_user.username):
        update.message.reply_text("You cheeky bastard ain't shutting me off.")
    else:
        # If the admin has added a time range for the reboot, it will be notified.
        try:
            if int(args[1]) > 4:
                Utils.broadcastAdmins(bot, "The server will reboot in " + args[1] + " minutes. If you have second thoughts, or this was a mistake, use the command /server cancelreboot")
                saveAdmins()
                subprocess.call(["shutdown", "/r", "/t", str(int(args[1])*60)]) # Time has to be in seconds
            elif int(args[1]) < 5: # For safety reasons, minimum reboot time (urgent) will be 5 minutes)
                update.message.reply_text("Number of minutes for reboot has to be greater than one")
        except:
            Utils.broadcastAdmins(bot, "The server will reboot in 15 (FIFTEEN) minutes. If you have second thoughts, or this was a mistake, use the command /server cancelreboot")
            saveAdmins()
            subprocess.call(["shutdown", "/r", "/t", "900"]) #15 minutes; the default for reboot.

def cancelreboot(bot,update,args):
    # A non admin shouldn't be able to cancel the server's reboot
    logging.warning("Server cancel reboot called by " + str(update.message.from_user.username))
    if not LOGGED_ADMINS.get(update.message.from_user.username):
        update.message.reply_text("You cheeky bastard ain't stopping me from killing meself!") # That's why we insult him.
    else:
        subprocess.call(["shutdown", "/a"]) # Abort command
        Utils.broadcastAdmins(bot,"Armaggedon avoided!") # Notify Admins that the server won't reboot now.

def HWStatus(bot,update,args):
    logging.warning("Server HWStatus called by " + str(update.message.from_user.username))
    try:
        pythoncom.CoInitialize() # We need to initialize the WMI python interface
        w = wmi.WMI(namespace="root\OpenHardwareMonitor") # And load the OpenHardwareMonitor item.
    except Exception as e:
        print(e.__doc__)
        print(e.message)
        update.message.reply_text("OpenHardwareMonitor might not be running on the server..") # Probably, maybe not, maybe a windows update broke our shit
    # Begin wmi parsing
    temperature_infos = w.Sensor()
    HWinfo = {}
    for sensor in temperature_infos:
        if sensor.Name == u'CPU Package' and sensor.sensorType == u'Temperature':
            HWinfo['cpuTemp'] = sensor.Value
        elif sensor.Name == u'CPU Total':
            HWinfo['cpuLoad'] = round(sensor.Value,2)
        elif sensor.Name == u'Used Memory':
            HWinfo['memUse'] = round(sensor.Value,2)
        elif sensor.Name == u'Available Memory':
            HWinfo['memAv'] = round(sensor.Value,2)
    #Message the info to the user.
    update.message.reply_text("Server Information:\n"
                              "CPU Temperature:     " + str(HWinfo['cpuTemp']) + "C\n"
                              "CPU Load:                     " + str(HWinfo['cpuLoad']) + "%\n"
                              "Memory:                        " + str(HWinfo['memUse']) + "GB/" + str(HWinfo['memUse']+HWinfo['memAv']) + "GB")

def HWInfo(bot,update,args):
    logging.warning("Server HWINFO called by " + str(update.message.from_user.username))
    try:
        pythoncom.CoInitialize() # We initialize the pyhon wmi interface
        w = wmi.WMI(namespace="root\OpenHardwareMonitor") #We open the OpenHardwareMonitor wmi interface
    except Exception as e:
        print(e.__doc__)
        print(e.message)
        update.message.reply_text("OpenHardwareMonitor might not be running on the server..")
    hwinfo = w.Hardware()
    info = {}

    for hardware in hwinfo:
        if hardware.HardwareType == u'Mainboard':
            info['mobo'] = str(hardware.Name)
        elif hardware.HardwareType == u'CPU':
            info['cpu'] = str(hardware.Name)
    update.message.reply_text("The server is currently hosted by a " + info['mobo'] +
                              " Motherboard running a " + info['cpu'] + " processor.")


def help(bot,update,args):
    logging.warning("Server Help called by " + str(update.message.from_user.username))
    #List of commands. -> This has to be updated before going into PROD. FFS
    update.message.reply_text("/Server does some server management:\n"+
                              "server status -------------> Displays a list of  active services\n"+
                              "server HWStatus -----------> Displays current server usage\n"+
                              "server HWInfo -------------> Displays the list of the server's specs\n"
                              "server distress {message} -> Warn an Admin. Abuse will not be tolerated")
    if LOGGED_ADMINS.get(update.message.from_user.username):
        #Admin secret menu of commands for the server
        update.message.reply_text("Since you're an Admin, here are the secret admin cheatcodes:\n"+
                                  "server reboot {minutes} ---> Orders the server to reboot in N minutes (default 15) and will warn all other admins\n"+
                                  "server cancelreboot -------> Cancels the reboot order"
                                  "")

def doubleDir(bot,update,args):
    logging.warning("Attempting console parsing")
    #This is me trying to communicate with a process
    try:
        process = popen_spawn.PopenSpawn('cmd') # Of course, we have to popen our way in through CMD
    except Exception as e:
        print(e.__doc__)
        print(e.message)
    process.sendline('help') #This is how we send a message
    process.expect('CMD.EXE') # An expected message? Probably not mandatory, requires further testing: TODO
    test = process.before # This shit shows EVERYTHING up to now on the console -> TODO: not taking into account already shown messages.
    update.message.reply_text(str(test))

def test(bot,update,args):
    Utils.askAdminsYesOrNo(bot)

def handler(bot,update,args):
    #catch-up process to dispatch commands
    print("server called with",end=' ')
    for arg in args:
        print(arg,  end=' ')
    print("")
    if ( len(args)==0 or args[0].lower() == 'help'):
        help(bot,update,args)
    elif (args[0].lower() == 'status'):
        status(bot,update,args)
    elif (args[0].lower() == 'distress'):
        distress(bot,update,args)
    elif (args[0].lower() == 'hwstatus'):
        HWStatus(bot,update,args)
    elif (args[0].lower() == 'hwinfo'):
        HWInfo(bot,update,args)
    elif (args[0].lower() == 'reboot'):
        reboot(bot,update,args)
    elif (args[0].lower() == 'cancelreboot'):
        cancelreboot(bot,update,args)
    elif (args[0].lower() == 'doubledir'):
        doubleDir(bot,update,args)
    elif (args[0].lower() == 'test'):
        test(bot,update,args)
    else:
        update.message.reply_text("I'm sorry, I don't understand")
    #check other outcomes