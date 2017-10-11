#status reboot distress
import Config,Utils
import requests,socket
import pythoncom
import wmi

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def start(bot, update,args):
    update.message.reply_text('Hello Wolrd!')

def status(bot,update,args):
    #status should check if diferent services are up or down
    update.message.reply_text    ('Orquibot   [ ON]')

    #Torrent
    sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    torrent=sock.connect_ex((str(Config.HOST_NAME),8080))
    if (torrent == 0):
        update.message.reply_text("Torrent    [ ON]")
    else:
        update.message.reply_text("Torrent    [OFF]")

    #SSH    
    sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssh=sock.connect_ex((str(Config.HOST_NAME),22022))
    if (ssh == 0):
        update.message.reply_text("ssh        [ ON]")
    else:
        update.message.reply_text("ssh        [OFF]")


    update.message.reply_text("Nothong more")

def distress(bot,update,args): 
    message = "Help, I'm "+ update.message.from_user.first_name
    if(len(args)>1):
        length = len(args)
        message=message+" and : "
        call=args[1:len(args)]
        for x in call:
            message= message +x+" "
    Utils.sendMessage(Config.API_TOKEN,Config.DISTRESS_CHAT,message)
    update.message.reply_text("Espera: Tengo el telefono del que sabe, un momento")
    
def HWStatus(bot,update,args):
    try:
        pythoncom.CoInitialize()
        w = wmi.WMI(namespace="root\OpenHardwareMonitor")
    except Exception as e:
        print(e.__doc__)
        print(e.message)
        update.message.reply_text("OpenHardwareMonitor might not be running on the server..")

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
    update.message.reply_text("Server Information:\n"
                              "CPU Temperature:     " + str(HWinfo['cpuTemp']) + "C\n"
                              "CPU Load:                     " + str(HWinfo['cpuLoad']) + "%\n"
                              "Memory:                        " + str(HWinfo['memUse']) + "GB/" + str(HWinfo['memUse']+HWinfo['memAv']) + "GB")

def HWInfo(bot,update,args):
    try:
        pythoncom.CoInitialize()
        w = wmi.WMI(namespace="root\OpenHardwareMonitor")
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
    update.message.reply_text("/Server manages the server, you can:\n"+
                              "server start --------------> to let the bot know you are there\n"+
                              "server status -------------> to know what services are up\n"+
                              "server HStatus ------------> to know some basic hardware numbers\n"+
                              "server help ---------------> to print this help\n"+
                              "server distress {mensaje} -> to give us a call")

def handler(bot,update,args):
    print("server called with ",end=' ')
    for arg in args:
        print(arg,  end=' ')
    print("")
    admin=False
    if (admin==True):
        print("There's and admin on the floor")
    if ( len(args)==0 or args[0].lower() == 'help'):
        help(bot,update,args)
    elif (args[0].lower() == 'start'):
        start(bot,update,args)
    elif (args[0].lower() == 'status'):
        status(bot,update,args)
    elif (args[0].lower() == 'distress'):
        distress(bot,update,args)
    elif (args[0].lower() == 'hwstatus'):
        HWStatus(bot,update,args)
    elif (args[0].lower() == 'hwinfo'):
        HWInfo(bot,update,args)
    else:
        update.message.reply_text("I'm sorry, I don't understand")
    #check other outcomes