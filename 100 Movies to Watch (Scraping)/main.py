from tkinter.ttk import Label

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

title_h1 = soup.find(name="h1").getText()

movies = []

all_title_movies = soup.find_all(name="h3")

for title in all_title_movies:
    movies.append(title.getText())

with open("movies.txt", mode="w") as file:
    for movie in reversed(movies):
        file.write(f"{movie}\n")
