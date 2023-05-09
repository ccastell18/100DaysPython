import smtplib
import random

# my_email = "ccastell0018@gmail.com"
# password = "aqnjyodlbgotfjxu"
#
# # connection = smtplib.SMTP("smtp.gmail.com", port=587)
# # connection.starttls()
# # connection.login(user=my_email, password=password)
# # connection.sendmail(from_addr=my_email, to_addrs="c.castellano18@yahoo.com", msg="Subject:Hello\n\nThis is the body of the email")
# # connection.close()
#
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="c.castellano18@yahoo.com", msg="Subject:Hello\n\nThis is the body of the email")
#

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

my_email = "ccastell0018@gmail.com"
password = "aqnjyodlbgotfjxu"

if day_of_week == 0:
        with open("quotes.txt")as quote_file:
            all_quotes = quote_file.readlines()
            quote = random.choice(all_quotes)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="c.castellano18@yahoo.com",
                                msg=f"Subject:Motivational quote\n\n{quote}")