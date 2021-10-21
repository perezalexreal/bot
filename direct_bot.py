from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time
import random
import csv
import re
import time
import urllib.request
import os
from selenium.webdriver.common.action_chains import ActionChains


# Username and password of your instagram account:
my_username = 'pagina1303@gmail.com'
my_password = 'pag1303sk'

# Instagram username list for DM:
usernames = []


with open('/Users/alexanderjaviercabelloperez/Desktop/followers.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if len(row) != 0:
            for element in row:
                usernames.append(element)

# Delay time between messages in sec:
between_messages = 5

browser = webdriver.Firefox()

# Authorization:


def auth(username, password):
    try:
        browser.get('https://instagram.com')
        time.sleep(random.randrange(2, 4))

        input_username = browser.find_element_by_name('username')
        input_password = browser.find_element_by_name('password')

        input_username.send_keys(username)
        time.sleep(random.randrange(1, 2))
        input_password.send_keys(password)
        time.sleep(random.randrange(1, 2))
        input_password.send_keys(Keys.ENTER)

    except Exception as err:
        print(err)
        browser.quit()

# Sending messages:


def send_message(users):
    try:
        time.sleep(random.randrange(4, 5))
        browser.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        time.sleep(random.randrange(3, 5))
        browser.find_element_by_xpath(
            '/html/body/div[6]/div/div/div/div[3]/button[2]').click()
        time.sleep(random.randrange(1, 2))
        browser.find_element_by_xpath(
            '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button').click()
        for user in users:
            time.sleep(random.randrange(1, 2))
            browser.find_element_by_xpath(
                '/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(user)
            time.sleep(random.randrange(2, 3))
            browser.find_element_by_xpath(
                '/html/body/div[6]/div/div/div[2]/div[2]').find_element_by_tag_name('button').click()
            time.sleep(random.randrange(3, 4))
            browser.find_element_by_xpath(
                '/html/body/div[6]/div/div/div[1]/div/div[2]/div/button').click()
            time.sleep(random.randrange(3, 4))
            text_area = browser.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
            messages = os.linesep.join([f'Ciao {user} ! Sono Marco del team @igflameofficial. \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t '

'Hai un profilo davvero fantastico! Potresti far arrivare i tuoi contenuti a molte più persone, siamo una piattaforma di crescita online, il nostro obiettivo è far crescere le persone e le loro pagine in modo costante e quotidiano.'
'                                                                                                                                                                                                                  '
'👉300 FOLLOWER 19,99€'
'👉500 FOLLOWER 29,99€'
'👉1000 FOLLOWER 49,99€'
'⭐️3000+ FOLLOWERS da 99€.'
'                                                                                                                                                                                                                  '
'Per qualsiasi domanda puoi chiedere qui o sul nostro sito web ☺️'


'                                                                                                                                                                                                                  '

'https://www.igflame.com/'])

           # messages = []
           # with open('/Users/alexanderjaviercabelloperez/Desktop/texto.csv', 'r') as testo_ccsv:
           #    testocsv = csv.reader(testo_ccsv)
           #    for row in testocsv:
           #       if len(row) != 0:
           #           for element in row:
           #               messages.append(element) 

            text_area.send_keys(messages)
            time.sleep(random.randrange(2, 4))
            text_area.send_keys(Keys.ENTER)
            print(f'Message successfully sent to {user}')
            time.sleep(between_messages)
            browser.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()

    except Exception as err:
        print(err)


auth(my_username, my_password)
time.sleep(random.randrange(2, 4))
send_message(usernames)
