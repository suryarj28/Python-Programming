import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "xxxxxxxxxxxxxxxxxxxxxxx"


weather_params = {
    "lat": 66.971599,
    "lon": 17.594566,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = True

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️ ",
        from_="+17xxxxxxxxx",
        to="+91xxxxxxxxxxx"
    )


print(message.status)
