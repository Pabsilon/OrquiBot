LOGGED_ADMINS = {}
LOGGED_USERS = {}

from random import choice
import hashlib

def generateHashedPass(pwd, salt):
    return hashlib.sha512(pwd+salt).hexdigest()

def generateSalt():
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars = []
    for i in range(64):
        chars.append(choice(alphabet))
    "".join(chars)
    return chars