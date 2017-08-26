import socket

machine=socket.gethostname()
if machine in ('DESKTOP-1E39VB7' , 'ALPHA'): #Ordenadores de Mac
    XML_PATH='c:\\Users\\Pabs\\Desktop\\FileZilla Server.xml'
    API_TOKEN = '350174683:AAFL4yesbHgQxOhI_5LybVZV8akQIycyVuw' # ORQUITESTBOT
elif machine in ('Zarya','OptimusPrime'): #El ordenador de pont
    XML_PATH='c:\\Users\\pablo\\Documents\\FileZilla Server.xml'
    API_TOKEN = '436440922:AAGUFL-tiwt3g7dmX8Z7S10URD2QDwJJupU'  # NOTORQUIBOT
    PERSISTENT_FILE='c:\\Users\\pablo\\git\\Orquibot\\persistent.json'

elif machine in ('Server'):
    print(socket.gethostname())
    XML_PATH='c:\\Hosted\\FileZilla Server\\FileZilla Server.xml'
    API_TOKEN = '376202632:AAHFi16Wc37p1VY_mJseP5S1zdy0xw5cncU'  # Orquibot
else:#Default
    XML_PATH=None
    API_TOKEN=None

HOST_NAME = 'orquishare.orquimed.es'
ADMIN_GROUP = 'SuperUsers'
USERS_GROUP = 'Users', 'SubAdmin'
DISTRESS_CHAT = '286257058'