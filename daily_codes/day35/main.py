import requests
from twilio.rest import Client


twilio_phone ="12057975541"
account_sid = "AC1e4d2ae05ea49d10c12e38b4fb3f96cb"
auth_token = "eac9b137ba75d3c092982ba1431e0750"

# can change this to environmental variable using export ENV_NAME=content
parameter ={

    "lat":16.866070,
    "lon":96.195129,
    "appid" : "86752ca8a0c5f9ba40c07131a61808f4",
    "exclude":"minutely,current,daily"
}



response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall",params=parameter)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages \
        .create(
        body="Its going to rain today,please bring an umbrella",
        from_=twilio_phone,
        to="+60 17 907 1293"
    )
    print(message.status)


