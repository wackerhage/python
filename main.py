from re import search

import requests
from bs4 import BeautifulSoup
import re
import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

# CLIENT_ID = os.environ["CLIENT_ID"]
# CLIENT_SECRET = os.environ["CLIENT_SECRET"]
CLIENT_ID="c6fbc1f355b0448f93c3d0a20589e843"
CLIENT_SECRET="5213258c56574a6c80d07dfd8690178c"
REDIRECT_URI = "http://127.0.0.1:8888/"

spotipy = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-modify-public playlist-modify-private"
))

answer = input("Which year would you like to travel to? YYYY-MM-DD e.g.")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
}

URL = f"https://www.billboard.com/charts/hot-100/{answer}/"
# URL = "https://www.billboard.com/charts/hot-100/1996-09-04/"

response = requests.get(url=URL, headers=headers)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

song_titles = []

titles = soup.find_all(name="div", class_="o-chart-results-list-row-container")

for title in titles:
    song_titles.append(str(title.h3.getText().strip()))

song_artists = []
artists = soup.find_all(name="li", class_="lrv-u-width-100p")

for artist in artists:
    artist_text = (artist.ul.span).getText().strip()
    clean_text = re.sub(r"\d+", "", artist_text)
    song_artists.append(str(clean_text.strip()))

song_artists = [item.strip() for item in song_artists if item.strip()]
print(song_artists)

user = spotipy.current_user()
username_id = user["id"]

# This will create a public Playlist on Spotify:
playlist = spotipy.user_playlist_create(user=username_id, name=f"{answer[:4]}: 100 Billboard Songs", public=True, description=f"This is the most popular songs from {answer[:4]}.")

# Adding songs to the playlist:
list_track_uri = []
for i in range(0,100):
    search_results = spotipy.search(q=f"{song_titles[i]} {song_artists[i]}",limit=10, type="track")
    track_uri = search_results["tracks"]['items'][0]['uri']
    list_track_uri.append(track_uri)

spotipy.playlist_add_items(playlist_id=playlist["id"], items=list_track_uri)