#!/usr/bin/python
import sys, time, subprocess, pip, os, socket

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green					# Variables for text colors. Saves me the trouble thank you!
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray


try:
    import argparse
    import mechanize
    import selenium
    import paramiko
except ImportError:
    print R + "You are missing dependencies! They will be installed for you with pip." + W
    print "Loading..."
    time.sleep(3)
    pip.main(["install", "mechanize", "selenium", "paramiko"])


def get_args():
    parser = argparse.ArgumentParser(description='Server-side bruteforce module written in Python')
    required = parser.add_argument_group('required arguments')
    required.add_argument('-s', '--service', dest='service', help="Provide a service being attacked. Several protocols and services are supported")
    required.add_argument('-u', '--username', dest='username', help='Provide a valid username for service/protocol being executed')
    required.add_argument('-w', '--wordlist', dest='password', help='Provide a wordlist or directory to a wordlist')
    parser.add_argument('-a', '--address', dest='address', help='Provide host address for specified service. Required for certain protocols')
    parser.add_argument('-p', '--port', dest='port', help='Provide port for host address for specified service. If not specified, will be automatically set')

    args = parser.parse_args()

    man_options = ['username', 'password']
    for m in man_options:
        if not args.__dict__[m]:
            print R + "[!] You have to specify a username AND a wordlist! [!]" + W
            sys.exit()

    service = args.service
    username = args.username
    wordlist = args.password
    address = args.address
    port = args.port

    return service, username, wordlist, address, port



def main():

    service, username, wordlist, address, port = get_args()

    print G + "[*] Username: %s " % username
    time.sleep(0.5)
    print G + "[*] Wordlist: %s " % wordlist
    time.sleep(0.5)
    print C + "[*] Service: %s "  % service + W
    time.sleep(0.5)

    # SSH bruteforce
    if service == 'ssh':
        if address is None:
            print R + "[!] You need to provide a SSH address for cracking! [!]" + W
        else:
            print C + "[*] Address: %s" % address + W
            if port is None:
                print O + "[?] Port not set. Automatically set to 22 for you [?]" + W
                port = 22
            time.sleep(0.5)
            print C + "[*] Port: %s "  % port + W

    # FTP bruteforce
    elif service == 'ftp':
        if address is None:
            print R + "[!] You need to provide a FTP address for cracking! [!]" + W




if __name__ == '__main__':
    main()
