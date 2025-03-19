import requests
from dotenv import load_dotenv
import os

load_dotenv()

URL_SHEETY = os.getenv('URL_SHEETY')
TOKEN_SHEETY = os.getenv('TOKEN_SHEETY')

headers_sheety = {
    "Authorization": f"Bearer {TOKEN_SHEETY}",
}

headers_putRequest = {
    "Authorization": f"Bearer {TOKEN_SHEETY}",
    "Content-Type": "application/json"
}

data_put = {
    "price": {
        "city": "Lisb",
        "iataCode": "LIS"
    }
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # Get information from Google sheet using Sheety API
        self.destination_data = {}

    def get_destination(self):
        response = requests.get(url=URL_SHEETY, headers=headers_sheety)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
        # Return example: [{'city': 'Lisboa', 'iataCode': 'LIS', 'lowestPrice': 1200, 'id': 2}]

    def change_data_sheet(self):
        # return self.response.text
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"https://api.sheety.co/83f4174358310f1b63704345d604f7b4/flightDeals/prices/{city['id']}", headers=headers_sheety, json=new_data)
            print(response.text)