from multiprocessing.managers import Value

import requests
import json
import os
from dotenv import load_dotenv
from flight_search import FlightSearch
from datetime import datetime
import time

load_dotenv()

TOKEN = os.getenv('TOKEN')
URL_FLIGHT_OFFERS = os.getenv('URL_FLIGHT_OFFERS')
CLIENT_ID = os.getenv('CLIENT_ID')
API_SECRET = os.getenv('API_SECRET')

# user_params = {
#     "Content-Type": "application/json",
#     "x-app-id": API_KEY,
#     "x-app-key": API_SECRET,
# }

class FlightData:

    def __init__(self):
        pass

    def find_cheapest_flight(self):
        flight_search = FlightSearch()
        data_flight = flight_search.get_flight_offers()

        try:
            if data_flight["data"][0]["itineraries"][0]["segments"][0]["departure"]["iataCode"] is None:
                raise ValueError("Result Cannot be None")
            else:
                for i in range(1):
                    print("Searching for good prices...\n")
                    time.sleep(2)
                    print(f"Departure: {data_flight["data"][i]["itineraries"][0]["segments"][0]["departure"]["iataCode"]} {data_flight["data"][i]["itineraries"][0]["segments"][0]["number"]} Destination: {data_flight["data"][1]["itineraries"][-1]["segments"][0]["departure"]["iataCode"]} {data_flight["data"][i]["itineraries"][-1]["segments"][0]["number"]}")
                    print(f"Total price: €{data_flight["data"][i]["price"]["total"]}")
                    print(f"Last day to buy: {data_flight["data"][i]["lastTicketingDate"]}")
                    print(f"Tickets remaining: {data_flight["data"][i]["numberOfBookableSeats"]}")
                    date = data_flight["data"][i]["itineraries"][0]["segments"][0]["departure"]["at"]
                    print(f"Departure date: {date.split("T")[0]}\n")
                    time.sleep(2)
        except ValueError as e:
            print(f"ValueError ocorred: {e}")
        except Exception as e:
            print(f"An Error ocorred: {e}")
        finally:
            print("\nExecution completed.")

    def cheap_flight(self):
        flight_search = FlightSearch()
        data_flight = flight_search.get_flight_offers()
        for i in range(5):
            price = float(data_flight["data"][i]["price"]["total"])
            if price < 1200:
                return True

    def infos(self):
        flight_search = FlightSearch()
        data_flight = flight_search.get_flight_offers()
        departure = data_flight["data"][0]["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        destination = data_flight["data"][1]["itineraries"][-1]["segments"][0]["departure"]["iataCode"]
        price = f"Total price: €{data_flight["data"][0]["price"]["total"]}"
        last_day_to_buy = data_flight["data"][0]["lastTicketingDate"]
        date_unformatted = data_flight["data"][0]["itineraries"][0]["segments"][0]["departure"]["at"]
        date = date_unformatted.split("T")[0]

        return f"Low price alert! Only €{price} to fly from {departure} to {destination}, on {date} until {last_day_to_buy}"

    # def read_flights(self):
    #     with open("data_flights.json", "r") as file:
    #         self.data_flight = json.load(file)
    #     return self.data_flight

# with open("data_flights.json", "w") as file:
#     json.dump(response.json(), file)

