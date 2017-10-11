#status reboot distress
import Config,Utils
import requests,socket
import pythoncom
import wmi

def sizeof_fmt(num, suffix='B'):
    #basic function to display human ready numbers
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def start(bot, update,args):
    #now it's a place holder, eventually should start basic services like open hardware monitor
    #and its own server startup batch job
    update.message.reply_text('Hello Wolrd!')

def status(bot,update,args):
    #status should check if diferent services are up or down
    #eventually it should call torrent.up() and every module should know how to 
    #check itself. some exceptions are orquibot witch cheks himself by executing and
    #ssh witch wont have a module and will be managed by /server. It is checkede waiting
    #for a tcp open port at the correct place, if it is something else it will do false positive
    update.message.reply_text    ('⚙️Orquibot   ✅')

    #Torrent
    sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    torrent=sock.connect_ex((str(Config.HOST_NAME),8080))
    if (torrent == 0):
        update.message.reply_text("⛵️Torrent    ✅")
    else:
        update.message.reply_text("⛵️Torrent    ❌")

    #SSH    
    sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssh=sock.connect_ex((str(Config.HOST_NAME),22022))
    if (ssh == 0):
        update.message.reply_text("🔌ssh        ✅")
    else:
        update.message.reply_text("🔌ssh        ❌")


    update.message.reply_text("🚧Nothing more🚧")

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
    
def HStatus(bot,update,args):
    try:
        pythoncom.CoInitialize()
        w = wmi.WMI(namespace="root\OpenHardwareMonitor")
    except Exception as e:
        print(e.__doc__)
        print(e.message)

    temperature_infos = w.Sensor()
    for sensor in temperature_infos:
        if sensor.SensorType == u'Temperature':
            update.message.reply_text(str(sensor.Name) + ": " + str(sensor.Value))



def help(bot,update,args):
    #basic help for all the commands supported, eventually it should tell users apart
    #and display more or less commands
    update.message.reply_text("/Server manages the server, you can:\n"+
                              "server start --------------> to let the bot know you are there\n"+
                              "server status -------------> to know what services are up\n"+
                              "server HStatus ------------> to know some basic hardware numbers\n"+
                              "server machine ------------> to know whats the machine name\n"
                              "server help ---------------> to print this help\n"+
                              "server distress {mensaje} -> to give us a call")

def handler(bot,update,args):
    #catch-up process to dispatch commands
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
    elif (args[0].lower() == 'machine'):
        machine(bot,update,args)
    elif (args[0].lower() == 'distress'):
        distress(bot,update,args)
    elif (args[0].lower() == 'hstatus'):
        HStatus(bot,update,args)
    else:
        update.message.reply_text("I'm sorry, I don't understand")
    #check other outcomes