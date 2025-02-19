from pyexpat.errors import messages
import os
import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": -26.8233,
    "lon": -49.2717,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()

weather_id = data["list"][0]["weather"][0]["id"]
description = data["list"][0]["weather"][0]["description"]

id_list = [i["weather"][0]["id"] for i in data["list"]]

for id in id_list:
    if id > 500:
        print("bring an umbrella!")
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="It's going to rain today. Remember to bring an umbrella.",
            from_="+15417256554",
            to="+5547988881707"
        )
        print(message.status)
