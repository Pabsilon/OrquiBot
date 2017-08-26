import json
import logging
config=False
try:
    import Config
    config=True
except:
    config=False

#This file will manage storage to a persistent JSON file for every diferent module
JSONFile=None
#Config file should store pairs<machine,<key,xmlPath>> and a default configure options
#for everyother option
def start():
    if config:
        file=open(Config.PERSISTENT_FILE,"r")
    else:
        file=open('c:\\Users\\pablo\\git\\Orquibot\\persistent.json',"r")
    raw=str(file.read())
    persistent=json.loads(raw)

def load(module): #this should load a pojo stile object given a module name
    logging.info(str(module)+"tried to get his data")


def  building():#this should run to do some trial and error
    if config:
        file=open(Config.PERSISTENT_FILE,"r")
    else:
        file=open('c:\\Users\\pablo\\git\\Orquibot\\persistent.json',"r")
    raw=str(file.read())
    persistent=json.loads(raw)
    persistent.keys()
    print("waiting")
building()