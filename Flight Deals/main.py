import time
import data_manager
from data_manager import DataManager
from flight_data import FlightData
from pprint import pprint
from dotenv import load_dotenv
from flight_search import FlightSearch
import os
from twilio.rest import Client
from notification_manager import NotificationManager

load_dotenv()

# print(sheet_data.get_flight_offers())
# print(sheet_data.get_city_code())

# data_manager = DataManager()
# sheet_data = data_manager.get_destination()

flight_data = FlightData().find_cheapest_flight()

if FlightData().cheap_flight():
    notification = NotificationManager().send_message()
else:
    pass

# Get new token
# flight_search = FlightSearch()
# print(flight_search._get_new_token())

# get_data = DataManager().get_destination()
# print(get_data)

# change_data = DataManager().change_data_sheet()
# print(change_data)

# price_dict = {}
# for i in range(144):
#     if float(flight_data["data"][i]["price"]["total"]) < 1200.00:
#         price_dict[i] = float(flight_data["data"][i]["price"]["total"])
# print(price_dict)

########## 111
# flight_search = FlightSearch().get_flight_offers()

# for row in sheet_data:
#     if row.get("iataCode", "") == "":
#         row["iataCode"] = flight_search.get_city_code(row["city"])
#         time.sleep(2)
#
# print(f"sheet_data: \n {sheet_data}")

# for row in sheet_data:
#     if row.get("lowestPrice", "") == "":
#         row["lowestPrice"] = flight_search.get_city_code(row["city"])
#         time.sleep(2)

# data_manager.destination_data = sheet_data
# data_manager.change_data_sheet()
