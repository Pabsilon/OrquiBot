from Modules import PersistentStorage
import json, random

def start():
    random.seed()
    persist=PersistentStorage.get('Ana')

def porn(bot, update):
    update.message.reply_text("https://reddit.com/r/randnsfw")
def boobs(bot, update):
    update.message.reply_text(boobs[random.randrange(len(boobs))])

def idleWait():
    print(waiting)
    return "waited"