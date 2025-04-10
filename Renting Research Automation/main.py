from itertools import count
from time import sleep

from dotenv import load_dotenv
import os
import bs4
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Importing .env
load_dotenv()

# Ambient variable
FORMS_LINK = os.environ['FORMS_LINK']
ZILLOW_LINK = os.environ['ZILLOW_LINK']

# Getting the request from the webpage
response = requests.get(ZILLOW_LINK)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

# Web Scraping prices
soup_prices = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
list_prices = []
for i in soup_prices:
    list_prices.append(i.text[:6:].replace("+", "").replace(",", ""))

# Web Scraping links
soup_links = soup.find_all(class_="StyledPropertyCardDataArea-anchor")
list_links = []
for i in soup_links:
    list_links.append(i['href'])

# Web Scraping addresses
soup_address = soup.find_all(class_="StyledPropertyCardDataArea-anchor")
list_address = []
for i in soup_address:
    list_address.append(i.text.lstrip().rstrip().replace("|", ""))

#Keeps the Chrome running
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#Creating the bot
driver = webdriver.Chrome(options=chrome_options)
driver.get(FORMS_LINK)

sleep(1)

count = int(len(list_address))

for i in range(count):
    inputs = driver.find_elements(By.CSS_SELECTOR,".whsOnd.zHQkBf")
    inputs[0].click()
    inputs[0].send_keys(list_address[i])

    inputs[1].click()
    inputs[1].send_keys(list_prices[i])

    inputs[2].click()
    inputs[2].send_keys(list_links[i])

    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()

    sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()



