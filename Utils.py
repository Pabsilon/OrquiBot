from pip._vendor import requests

def sendMessage(fromWho,toWho,message):
    #Sends a message from a bot (fromWho) to a person (a chat the bot is in)
    url="http://api.telegram.org/bot"+fromWho+"/sendMessage?chat_id="+toWho+"&text="+message
    requests.get(url)