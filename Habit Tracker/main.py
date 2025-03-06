from http.client import responses
from datetime import datetime
import requests
from urllib3 import request

pixela_endpoint = "https://pixe.la/v1/users"
USER_NAME = "wackerhage"
TOKEN = "?"

today = datetime(year=2025, month=3, day=5)

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#       Creating a username and registrate the token:
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Page:
# https://pixe.la/@wackerhage

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Exercise Graph",
    "unit": "minutes",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_body_update = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "60.0",
}

graph_pixel_update = {
    "quantity": "55.0",
}

#       Creating the graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

graph_update = f"{pixela_endpoint}/{USER_NAME}/graphs/{graph_config["id"]}"

response = requests.post(url=graph_update, json=graph_body_update, headers=headers)
print(response.text)

# pixel_update = f"{pixela_endpoint}/{USER_NAME}/graphs/{graph_config["id"]}/{graph_body_update["date"]}"

# delete_pixel = f"{pixela_endpoint}/{USER_NAME}/graphs/{graph_config["id"]}/{graph_body_update["date"]}"
# response = requests.delete(url=delete_pixel, headers=headers)
# print(response.text)
