##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import datetime as dt
import pandas as pd
import smtplib
import random as rd

now = dt.datetime.now()
month = now.month
day = now.day

birthday = pd.read_csv("birthdays.csv").to_dict(orient="record")
receiver = {}

my_email = "swqq5200@gmail.com"
password = "Cy01032002"
to_address = "swqq520@yahoo.com"

for person in birthday:
    if person["month"] == month and person["day"] == day:
        receiver = person

letter_num = rd.randint(1, 3)

with open(f"letter_templates/letter_{letter_num}.txt", "r+") as file:
    content = file.read()
    content = content.replace("[NAME]", receiver["name"])

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs=to_address, msg=f"Subject:Happy Birthday!\n\n{content}")









