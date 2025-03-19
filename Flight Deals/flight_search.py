import os
from http.client import responses
from pprint import pprint
from dotenv import load_dotenv
import requests
from datetime import datetime
import time

URL_AUTH = os.getenv('URL_AUTH')
CLIENT_ID = os.getenv('CLIENT_ID')
API_SECRET = os.getenv('API_SECRET')

load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ["CLIENT_ID"]
        self._api_secret = os.environ["API_SECRET"]
        self._token = os.environ["TOKEN"]

    def _get_new_token(self):

        data_auth = {
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": API_SECRET,
        }

        self.response = requests.post(url=URL_AUTH, data=data_auth)
        return self.response.text

    def get_flight_offers(self):

        headers_flight = {
            "Authorization": f"Bearer {self._token}",
            "Content-Type": "application/json",
        }

        params = {
            "originLocationCode": "NVT",
            "destinationLocationCode": "LIS",
            "departureDate": "2025-07-12",
            "returnDate": "2025-07-19",
            "adults": 1,
        }

        response = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers", headers=headers_flight, params=params)
        data_flight = response.json()

        return data_flight

    def get_city_code(self, city_name):

        params = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS"
        }

        headers_flight = {
            "Authorization": f"Bearer {self._token}",
            "Content-Type": "application/json",
        }

        url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

        self.response = requests.get(url=url, headers=headers_flight, params=params)

        print(f"Status code {self.response.status_code}. Airport IATA: {self.response.text}")
        try:
            code = self.response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/a"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code
