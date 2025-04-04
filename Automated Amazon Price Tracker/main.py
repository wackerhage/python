from bs4 import BeautifulSoup
import requests
import smtplib
import re
from dotenv import load_dotenv
import os

load_dotenv()

URL = os.environ['URL']
MY_EMAIL = os.environ['MY_EMAIL']
PASSWORD = os.environ['PASSWORD']

response = requests.get(url=URL, headers={
    'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    'Accept-Encoding':"gzip, deflate, br, zstd",
    'Accept-Language':"pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    'priority':"u=0, i",
    'x-forwarded-proto':"https",
    'x-https':"on",
})

web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

price = soup.find(name="span", attrs={"class":"a-price","data-a-size":"medium_plus"})
price = price.getText()[12::]
price = price.replace(".", "").replace(",", ".")
price = float(price)

title_product = soup.find(id="productTitle").getText()
title_product = " ".join(title_product.split())
title_product = re.sub(r"[^a-zA-Z0-9 ]", "", title_product)

body = f"\n{title_product} \nNow {price} \n{URL}"

if price > 2500:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="wackerhaged@yahoo.com",
                            msg=f"Subject: Amazon Price Alert\n\n{body}")
