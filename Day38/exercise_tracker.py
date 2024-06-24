#  nutritionix, google sheets, sheety
# the code with right environment variables is stored in replit
import requests
from datetime import datetime
import os

# os.environ['APP_ID_NUTRITION'] = "0db2fc88"  # setting the environment variable
# print(os.getenv('APP_ID_NUTRITION'))
APP_ID = os.getenv('APP_ID')

API_KEY_NUTRITION = os.getenv('API_KEY_NUTRITION')

HOST_DOMAIN = "https://trackapi.nutritionix.com"

exercise_endpoint = f"{HOST_DOMAIN}/v2/natural/exercise"

exercise_data ={
    "query" : input("What exercises did you do today? ")
}

auth_header = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY_NUTRITION
}

response = requests.post(url= exercise_endpoint, headers= auth_header, json= exercise_data, verify= False)
results = response.json()
# print(results['exercises'][0]['name'])

sheety_endpoint = "https://api.sheety.co/8ad185ca25c0967f2979b29aa325a310/myWorkoutTracaking/workouts"

for details in results['exercises']:
    today_date = datetime.now().strftime("%d%m%Y")
    time = datetime.now().strftime("%X")

    sheet_data = {
        "workout":{
            "date": today_date,
            "time" : time,
            "exercise": details['name'].title(), 
            "duration": details['duration_min'],
            "calories": details['nf_calories']
        }
    }
    
    sheety_response = requests.post(url= sheety_endpoint, json= sheet_data,auth= (os.getenv('harsh'), os.getenv('havish123')), verify= False)
    print(sheety_response.text)
