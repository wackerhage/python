import requests
import json
import datetime as date
from requests.auth import HTTPBasicAuth
import os

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

APP_ID = os.environ['APP_ID']
URL_ROW = os.environ['URL_ROW']
API_KEY = os.environ['API_KEY']

today = date.datetime.now().date().strftime("%d/%m/%Y")
now_time = date.datetime.now().strftime("%X")

headers = {
    "Authorization": "Bearer dpsakdpokaspdksadoopfkdop",
}

response = requests.get(url=URL_ROW, headers=headers)
print(response.text)

user_params = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

data = {
    "query": input("Tell me which exercises you did and how much: "),
}

add_row = {
    "email": {
        "name": "dominique wackerhage",
        "email": "domwackerhage@gmail.com",
    }
}

response = requests.post(url=nutritionix_endpoint, headers=user_params, json=data)
data = response.json()

with open("data.json", "w") as file:
    json.dump(data, file)

with open("data.json", "r") as file:
    data_json = json.load(file)

workout = {
    "workout": {
        "date": today,
        "time": now_time,
        "exercise": data_json["exercises"][0]["name"].title(),
        "duration": f"{int(data_json["exercises"][0]["duration_min"])}:00",
        "calories": data_json["exercises"][0]["nf_calories"]
    }
}

#Add row
response = requests.post(url=URL_ROW, headers=user_params, json=workout)
print(response.json())
