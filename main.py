from twilio.rest import Client
import requests

account_sid = ""
auth_token = ""
my_number = ""

KEY=""
MY_LAT = 0 # My latitude
MY_LONG = 0 # My longitude

parameters = {
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":KEY,
    "units":"metric",
    "cnt":4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
will_rain = False
for day in data["list"]:
    if int(day["weather"][0]["id"]) < 700: #from API doc if id < 700 there will be rain
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="It's going to rain today. Remember to bring an umbrella",
        to=f"whatsapp:{my_number}"
    )

