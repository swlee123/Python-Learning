import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 3.139003 # Your latitude
MY_LONG = 101.686852 # Your longitude


#Your position is within +5 or -5 degrees of the ISS position.
def is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if iss_longitude-5 <= MY_LONG <= iss_longitude+5 and iss_latitude <= MY_LAT <= iss_latitude:
        return True
    else:
        return False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour

    if hour_now >= sunset or hour_now <= sunrise:
        return True
    else:
        return False

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    if is_night() and is_close():
        my_email = "swqq5200@gmail.com"
        password = "Cy01032002"
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(to_addrs="swqq520@yahoo.com", from_addr=my_email, msg="Subject:Announcement\n\nLook up ! "
                                                                                  "The ISS is currently above you!"
                                                                                  "\nIt's currently dark!"
                                                                    )
    time.sleep(60)



