import os
from dotenv import load_dotenv
from twilio.rest import Client
from flight_data import FlightData

AUTH_TOKEN = os.getenv('AUTH_TOKEN')
ACCOUNT_SID = os.getenv('ACCOUNT_SID')

FROM = os.getenv('FROM')
TO = os.getenv('TO')

load_dotenv()

class NotificationManager:

    def send_message(self):
        print("Low Prices!\n")
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages \
            .create(
            body=f"{FlightData().infos()}",
            from_=FROM,
            to=TO
        )
        print(message.status)