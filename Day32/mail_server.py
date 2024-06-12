# import smtplib

# # if you are using different email provider use settings for that
# my_email = "codeharshit05@gmail.com"  
# password = "bjmvipelrylujioz"

# receiver_email = "123havish123@gmail.com"

# 1st method
# connection = smtplib.SMTP("smtp.gmail.com")

# connection.starttls()

# connection.login(user= my_email, password= password)
# connection.sendmail(from_addr= my_email, to_addrs= receiver_email, msg= "Subject:Email sent from python code\n\nHello, my friend")

# connection.close()

# 2nd method
# with smtplib.SMTP("smtp.gmail.com") as connection:

#     connection.starttls()

#     connection.login(user= my_email, password= password)
#     connection.sendmail(from_addr= my_email, to_addrs= receiver_email, msg= "Subject:Email sent from python code\n\nHello, my friend")


# import datetime as dt

# now = dt.datetime.now()
# year = now.year

# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=1999, month=10, day=5)
# print(date_of_birth)

# challenge 1
# send an email with a random motivational quote on a particular day

import datetime as dt
import smtplib
import random

my_email = "codeharshit05@gmail.com"  
password = "bjmvipelrylujioz"

receiver_email = "123havish123@gmail.com"

now = dt.datetime.now()
# day = now.weekday()
# print(day)
day = now.strftime("%A")
# print(day)

with open('quotes.txt') as data:
    quotes = data.readlines()
    # quotes =[line.strip() for line in data.readlines()] 

quote = random.choice(quotes)
# print(quote)

if day == "Wednesday":
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= my_email, password= password)
        
        connection.sendmail(
            from_addr= my_email, 
            to_addrs= receiver_email, 
            msg=f"Subject:{day} motivation\n\n{quote}".encode('utf-8')  # used encode to encode characters in utf-8
            )