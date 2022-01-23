import requests
from twilio.rest import Client

account_sid = "hide"
auth_token = "hide"

API_KEY = "hide"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
LAT = 59.938480
LONG = 30.312481
parameters = {"lat": LAT,
              "lon": LONG,
              'exclude': 'daily,minutely,current',
              "appid": API_KEY,
              }
will_rain = False
response = requests.get(url=OWM_endpoint, params=parameters)
response.raise_for_status()
hourly_data = response.json()['hourly']
for n in range(12):
    weather_id = hourly_data[n]["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It`s going to rain today. Remember to bring an ☂️",
        from_="hide",
        to="hide"
    )
    print(message.status)
