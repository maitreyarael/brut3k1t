# brut3k1t
## version 1 release
Server-side brute-force module.

## 1. Introduction

__brut3k1t__ is a server-side bruteforce module that supports dictionary attacks for several protocols.
The current protocols that are complete and in support are:

    ssh
    ftp
    smtp
    XMPP
    instagram
    facebook

There will be future implementations of different protocols and services (including Twitter, Facebook, Instagram).

## 2. Installation

Installation is simple. __brut3k1t__ requires several dependencies, although they will be installed by the
program if you do not have it.

* __argparse__ - utilized for parsing command line arguments
* __paramiko__ - utilized for working with SSH connections and authentication
* __ftplib__ - utilized for working with FTP connections and authentication
* __smtplib__ - utilized for working with SMTP (email) connections and authentication
* __fbchat__ - utilized for connecting with Facebook
* __selenium__ - utilized for web scraping, which is used with Instagram (and later Twitter)
* __xmppy__ - utiized for XMPP connections
...and more within the future!

Downloading is simple. Simply `git clone`.

    git clone https://github.com/ex0dus-0x/brut3k1t

Change to directory:

    cd /path/to/brut3k1t

## 3. Usage

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

### Examples of usage:

Cracking SSH server running on `192.168.1.3` using `root` and `wordlist.txt` as a wordlist.

    python brut3k1t.py -s ssh -a 192.168.1.3 -u root -w wordlist.txt

The program will automatically set the port to 22, but if it is different, specify with `-p` flag.

Cracking email `test@gmail.com` with `wordlist.txt` on port `25` with a 3 second delay. For email it is necessary to use the SMTP server's address. For e.g Gmail = `smtp.gmail.com`. You can research this using Google.

    python brut3k1t.py -s smtp -a smtp.gmail.com -u test@gmail.com -w wordlist.txt -p 25 -d 3

Cracking XMPP `test@creep.im` with `wordlist.txt` on default port `5222`. XMPP also is similar to SMTP, whereas you will need to provide the address of the XMPP server, in this case `creep.im`.

    python brut3k1t.py -s xmpp -a creep.im -u test -w wordlist.txt

Cracking Facebook is quite a challenge, since you will require the target user ID, not the username.

    python brut3k1t.py -s facebook -u 1234567890 -w wordlist.txt

Cracking Instagram with username `test` with wordlist `wordlist.txt` and a 5 second delay

     python brut3k1t.py -s instagram -u test -w wordlist.txt -d 5


 ## KEY NOTES TO REMEMBER

 * If you do not supply the port `-p` flag, the default port for that service will be used. You do not need to provide it for Facebook and Instagram, since they are um... web-based. :)

 * If you do not supply the delay `-d` flag, the default delay in seconds will be 1.

 * Remember, use the SMTP server address and XMPP server address for the address `-a` flag, when cracking SMTP and XMPP, respectively.

 * Facebook requires the username ID. This is a little bit of a setback since some people do not display their ID publicly on their profile.

 * Make sure the wordlist and its directory is specified. If it is in `/usr/local/wordlists/wordlist.txt` specify that for the wordlist `-w` flag.

 * Remember that some protocols are not based on their default port. A FTP server will not necessarily always be on port `21`. Please keep that in mind.

 * Use this for educational and ethical hacking purposes, as well as the sake of learning code and security-oriented practices. __No script kiddies!__



# Much more features to come!
