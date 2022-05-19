import datetime as dt
import random as rd
import smtplib
now = dt.datetime.now()
today = now.weekday()

with open("quotes.txt") as file:
    quotes = file.readlines()
    sentences = rd.choice(quotes)

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()

my_email = "swqq5200@gmail.com"
password = "Cy01032002"
connection.login(user=my_email, password=password)

if today == 3:
    connection.sendmail(from_addr=my_email, to_addrs="mandreayong@yahoo.com", msg=f"Subject:Motivations\n\n"
                                                                          f"{sentences}"
                        )



