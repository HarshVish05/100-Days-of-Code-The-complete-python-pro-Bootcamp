import requests
from datetime import datetime
import os

TOKEN = os.getenv("Token")    # this token is there in replit it is not written here so that i can push it to git this token is randomly created by myself
USERNAME = "harsh05"


user_params = {
    "token" : TOKEN,   
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

pixela_endpoint = "https://pixe.la/v1/users"
# to create the user and you can comment out this code once user is created
# I have created the user and this is my profile page - https://pixe.la/@harsh05  and the token is - in replit
# response = requests.post(url= pixela_endpoint, json= user_params, verify= False)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Walking Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

auth_header = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url= graph_endpoint, headers= auth_header, json= graph_config, verify= False )
# print(response.text)


# posting a pixel
pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"
today_date = datetime(year= 2024, month= 6, day=22)
# today_date = datetime.now()
pixel_data = {
    "date": today_date.strftime("%Y%m%d"),
    "quantity": "10"     # you can also use input method to let the user input their run instead of hard coding
}

# response = requests.post(url= pixel_endpoint, headers= auth_header, json= pixel_data, verify= False)
# print(response.text)

# updating the pixel
update_endpoint = f"{pixel_endpoint}/{pixel_data['date']}"

update_data = {
    'quantity': "6.54"
}

# response = requests.put(url= update_endpoint, json= update_data, headers= auth_header, verify= False)
# print(response.text)

date_of_pixel_to_delete = "20240624"
delete_endpoint = f"{pixel_endpoint}/{date_of_pixel_to_delete}"

response = requests.delete(url= delete_endpoint, headers= auth_header, verify= False)
print(response.text)