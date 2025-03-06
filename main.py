from datetime import datetime
import requests
import json
import os
from twilio.rest import Client

from more_itertools.more import difference

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHA_VANTAGE_API_KEY = "9HRJJASUU8UR3X74"
NEWS_API = "1de7de0e794b436f9205827e19e710df"
# account_sid = os.environ.get("ACCOUNT_SID")
# auth_token = os.environ.get("AUTH_TOKEN")
account_sid = "AC82af2d34a373b5a1a22a589f17d00c90"
auth_token = "d36ce19afbe13871037438c8f9988843"

parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VANTAGE_API_KEY
}

parameters_news = {
    "q": COMPANY_NAME,
    "sortBy": "popularity",
    "apikey": NEWS_API
}

# today = datetime.now()
# print(today.date())

# response_stock = requests.get(STOCK_ENDPOINT, params=parameters_stock)
# response_stock.raise_for_status()
# data_stock = response_stock.json()

# print(data_stock)

# with open("data_stock.json", "w") as file:
#     json.dump(data_stock, file, indent=4)

with open("data_stock.json", "r") as file:
    data_stock = json.load(file)

with open("data_news.json", "r") as file:
    data_news = json.load(file)

yesterday_closing_stock = data_stock["Time Series (Daily)"]["2025-02-28"]["4. close"]
before_yesterday_closing_stock = data_stock["Time Series (Daily)"]["2025-02-27"]["4. close"]
print(before_yesterday_closing_stock, yesterday_closing_stock)

positive_diference = abs(float(yesterday_closing_stock) - float(before_yesterday_closing_stock))

percentage_difference = (float(yesterday_closing_stock) * 100) / float(before_yesterday_closing_stock) - 100

if percentage_difference < 5.0:
    description_list = [data_news["articles"][i]["description"] for i in range(3)]
    title_list = [data_news["articles"][i]["title"] for i in range(3)]

    # for i in range(3):
    print("Look at the News!\n")
    print(title_list[0])
    print(description_list[0])
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"{title_list[0]}", # title_list[i], description_list[i]
        from_="+15417256554",
        to="+5547988881707"
    )
    print(message.status)

# response_news = requests.get(NEWS_ENDPOINT, params=parameters_news)
# response_news.raise_for_status()
# data_news = response_news.json()

# with open("data_news.json", "w") as file:
#     json.dump(data_news, file, indent=4)

#Optional TODO: Format the message like this:

# TODO: RUN

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

