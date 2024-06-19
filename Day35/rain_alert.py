# https://home.openweathermap.org/api_keys
# you can refer to ventusky to know what weather is where

# This code worked in replit not in vs code cause of ssl certification error
# twilio recovery - WHS28Y7HY5CLV6W7XG8UFNDL

# https://apilist.fun/   -  all api list you can check and build

import requests
import urllib3
from twilio.rest import Client
import os


api_key = os.environ.get("OPENWEATHER_API_KEY")

MY_LAT = 22.572645
MY_LONG = 88.363892
account_sid = "AC370cd4f4ecb471b2a3a790e2ce3db21c"
auth_token  = os.getenv("TWILIO_AUTH_TOKEN")

print(auth_token)

# Disable SSL warnings
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# challenge - work with 3hour interval api
# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
parameters = {
    "lat" : MY_LAT,
    "lon": MY_LONG,
    "appid" : api_key,
    "cnt": 4,            # specifies no of timestamps it will return
}

# response = requests.get(url= "https://api.openweathermap.org/data/2.5/forecast", params= parameters, verify= False)
# response.raise_for_status()

# weather_data = response.json()

# # challenge - look through weather data get the id and if it is < 700 print bring umbrella
# weather_data_list = weather_data['list']

# will_rain = False
# for weatherData in weather_data_list:
#     condition_code = weatherData['weather'][0]['id']
#     # print(type(condition_code))
#     # if  condition_code < 700:    # condition to check whether rain is happening or not
#     if  condition_code > 800:  # used this condition for testing purposes
#         will_rain = True

    
# if will_rain:
#     # Step 1: Initialize the Twilio client (no network connection yet)
#     client = Client(account_sid, auth_token)
    
#     # Step 2: Send the message (network connection is made here)
#     message = client.messages.create(
#                   body = "It's going to rain today. Bring an umbrella ☂️.",
#                   from_ = "+12093077352",
#                   to = "+918777656566",
#               )

#     print(message.status)
# print(weather_data['list'][0]['weather'][0]['id'])



