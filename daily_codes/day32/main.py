#import smtplib

#my_email = "swqq5200@gmail.com"
#password = "Cy01032002"

# differ with email-provider

#with smtplib.SMTP("smtp.gmail.com") as connection:
#   connection.starttls()
#  connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="swqq520@yahoo.com", msg="Subject:Hello\n\n"
#                                                                          "This is the body of my email!")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.weekday()


date_of_birth = dt.datetime(year=2002, month=10, day=1)
print(date_of_birth)