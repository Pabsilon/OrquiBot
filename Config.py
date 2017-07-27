import socket

HOST_NAME = 'orquishare.orquimed.es'

if socket.gethostname() == 'DESKTOP-1E39VB7' or 'ALPHA': #Ordenadores de Mac
    XML_PATH='c:\\Users\\Pabs\\Desktop\\FileZilla Server.xml'
    API_TOKEN = '350174683:AAFL4yesbHgQxOhI_5LybVZV8akQIycyVuw' # ORQUITESTBOT
elif socket.gethostname() == 'Zarya': #El ordenador de pont
    XML_PATH='Ruta con doble \\ al fichero xml.'
    API_TOKEN = '436440922:AAGUFL-tiwt3g7dmX8Z7S10URD2QDwJJupU'  # NOTORQUIBOT
elif socket.gethostname() == 'Server'
    XML_PATH='c:\\Hosted\\FileZilla Server\\FileZilla Server.xml'
    API_TOKEN = '376202632:AAHFi16Wc37p1VY_mJseP5S1zdy0xw5cncU'  # Orquibot


ADMIN_GROUP = 'SuperUsers'
USERS_GROUP = 'Users', 'SubAdmin'