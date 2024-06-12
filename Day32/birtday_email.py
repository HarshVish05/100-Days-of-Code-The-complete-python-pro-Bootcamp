import smtplib
import pandas
import datetime as dt

my_email = "codeharshit05@gmail.com"  
password = "bjmvipelrylujioz"

birthday_data = pandas.read_csv('birthday_emails.csv')

# print(birthday_data.values[0][1])

now = dt.datetime.now()
day = now.day
month = now.month
# print(month)

for index, row in birthday_data.iterrows():
    if row['day'] == day and row['month'] == month:
        
        name = row['name']
        email = row['email']
        
        # print(name)
        with open('letter.txt') as data:
            letter = data.read()
            
        # print(letter.format(name= name))

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=email, 
                msg=f"Subject:Happy Birthday!!! {name}\n\n{letter.format(name= name)}"
                )
    
    

#   this script is running in cloud in pythonanywhere.com       

