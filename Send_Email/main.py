import smtplib
import datetime as dt
import random

my_email = "****************"
my_password ="**************"

now = dt.datetime.now()
weekday =now.weekday()

if weekday == 0:
    with open("quotes.txt", "rb")as quotes_file:
        my_quote = quotes_file.readlines()
        selected_quote = random.choice(my_quote)
        print(type(selected_quote))

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr= my_email,
                            to_addrs= "wakamaujoy@gmail.com",
                            msg= f"Subject:Monday Motivation\n\n{selected_quote}"

        )





