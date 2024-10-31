from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

response = requests.get("https://www.reddit.com/r/programming/")
yc_web_page = response.text

# leitura do arquivo HTML:
with open("programming.html", "r", encoding="utf-8") as file:
    yc_web_page = file.read()

# variavel para utilizar o modulo BeautifulSoup:
soup = BeautifulSoup(yc_web_page, 'html.parser')

tag1 = soup.find(slot="title", id="post-title-t3_1gf0vf9")
tag2 = soup.find(slot="title", id="post-title-t3_1gesfdh")
tag3 = soup.find(slot="title", id="post-title-t3_1geuere")

text1 = tag1.getText()
text2 = tag2.getText()
text3 = tag3.getText()

link1 = tag1.get("href")
link2 = tag2.get("href")
link3 = tag3.get("href")

tag_upvote1 = soup.find(id="t3_1gf0vf9")
tag_upvote2 = soup.find(id="t3_1gesfdh")
tag_upvote3 = soup.find(id="t3_1geuere")

upvote1 = tag_upvote1.get("score")
upvote2 = tag_upvote2.get("score")
upvote3 = tag_upvote3.get("score")

excel_header = ["Titulo", "Links", "Upvotes"]
data = [[text1, link1, upvote1],[text2, link2, upvote2],[text3, link3, upvote3]]

df = pd.DataFrame(data, columns=excel_header)

writer = pd.ExcelWriter('file1.xlsx', engine ='xlsxwriter')

df.to_excel(writer, sheet_name= "Postagens")

writer._save()
