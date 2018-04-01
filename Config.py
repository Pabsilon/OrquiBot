import socket

HOST_NAME = 'orquishare.orquimed.es'

if socket.gethostname() == 'DESKTOP-1E39VB7' or 'ALPHA':  # Ordenadores de Mac
    XML_PATH = 'd:\\Pabs\\Desktop\\FileZilla Server.xml'
    API_TOKEN = '350174683:AAFL4yesbHgQxOhI_5LybVZV8akQIycyVuw'  # ORQUITESTBOT
if socket.gethostname() == 'Zarya':  # El ordenador de pont
    XML_PATH = 'Ruta con doble \\ al fichero xml.'
    API_TOKEN = '436440922:AAGUFL-tiwt3g7dmX8Z7S10URD2QDwJJupU'  # NOTORQUIBOT
if socket.gethostname() == 'Orquishare':
    print(socket.gethostname())
    XML_PATH = 'c:\\Hosted\\FilleZilla\\FileZilla Server.xml'
    API_TOKEN = '376202632:AAHFi16Wc37p1VY_mJseP5S1zdy0xw5cncU'  # Orquibot

ADMIN_GROUP = {'SuperUsers'}
USERS_GROUP = {'Users', 'SubAdmin', 'UsersTorrent'}
DISTRESS_CHAT = '286257058'
USERS_FOLDER = 'D:\\UsuariosOrquishare'

SERVICES_LIST = ["OpenHardwareMonitor.exe", "FileZilla Server.exe", "Plex Media Server.exe", "deluged.exe", "deluged-web.exe", "Factorio.exe"]
SERVICES_LOCATION = {
    # "OpenHardwareMonitor.exe": "C:\\Users\\Administrador.WIN-2AL7APBAKHS\\Desktop\\OpenHardwareMonitor\\OpenHardwareMonitor.exe",
    "OpenHardwareMonitor.exe": "D:\\Pabs\\Desktop\\OpenHardwareMonitor\\OpenHardwareMonitor.exe",
    "Factorio.exe": "C:\\Hosted\\Steam\\steamapps\\common\\Factorio\\bin\\x64\\FactorioServer.bat",
    "Plex Media Server.exe": "C:\\Hosted\\Plex Server\\Plex Media Server.exe",
    "deluged.exe": "C:\\Hosted\\Deluge\\deluged.exe",
    "deluged-web.exe": "C:\\Hosted\\Deluge\\deluge-web.exe",
    "FileZilla Server.exe": "C:\\Hosted\\FilleZilla\\FileZilla Server.exe"}
SERVICES_SHUTDOWN = {
    "Factorio.exe": "save",
}