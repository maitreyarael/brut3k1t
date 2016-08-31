# brut3k1t
## Work-in-progress beta
Server-side brute-force module.

### 1. Introduction

__brut3k1t__ is a server-side bruteforce module that supports dictionary attacks for several protocols.
The current protocols that are complete and in support are:

    ssh
    ftp
    smtp

There will be future implementations of different protocols and services (including Twitter, Facebook, Instagram).

### 2. Installation

Installation is simple. __brut3k1t__ requires several dependencies, although they will be installed by the
program if you do not have it.

* __argparse__ - utilized for parsing command line arguments
* __paramiko__ - utilized for working with SSH connections and authentication
* __ftplib__ - utilized for working with FTP connections and authentication
* __smtplib__ - utilized for working with SMTP (email) connections and authentication
...and more within the future!

Downloading is simple. Simply `git clone`.

    git clone https://github.com/ex0dus-0x/brut3k1t

Change to directory:

    cd /path/to/brut3k1t

### 3. Usage

Utilizing __brut3k1t__ is a little more complicated than just running a Python file.

Typing `python brut3k1t -h` shows the help menu:

    usage: brut3k1t.py [-h] [-s SERVICE] [-u USERNAME] [-w PASSWORD] [-a ADDRESS]
                   [-p PORT] [-d DELAY]

    Server-side bruteforce module written in Python

    optional arguments:
    -h, --help            show this help message and exit
    -a ADDRESS, --address ADDRESS
                        Provide host address for specified service. Required
                        for certain protocols
    -p PORT, --port PORT  Provide port for host address for specified service.
                        If not specified, will be automatically set
    -d DELAY, --delay DELAY
                        Provide the number of seconds the program delays as
                        each password is tried

    required arguments:
    -s SERVICE, --service SERVICE
                        Provide a service being attacked. Several protocols
                        and services are supported
    -u USERNAME, --username USERNAME
                        Provide a valid username for service/protocol being
                        executed
    -w PASSWORD, --wordlist PASSWORD
                        Provide a wordlist or directory to a wordlist

Examples of usage:

Cracking SSH server running on `192.168.1.3` using `root` and `wordlist.txt` as a wordlist.

    python brut3k1t.py -s ssh -a 192.168.1.3 -u root -w wordlist.txt

The program will automatically set the port to 22, but if it is different, specify with `-p` flag.

Cracking email `test@gmail.com` with `wordlist.txt` on port `25` with a 3 second delay

    python brut3k1t.py -s smtp -a smtp.gmail.com -u test@gmail.com -w wordlist.txt -p 25 -d 3


# Much more features to come! This README file is currently incomplete!
