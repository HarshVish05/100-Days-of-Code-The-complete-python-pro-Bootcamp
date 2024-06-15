import requests
# import certifi

MY_LAT = 22.572645
MY_LONG = 88.363892

# data = requests.get(url= "http://api.open-notify.org/is-now.json")
# print(data.status_code)

# data.raise_for_status() # will raise an exception according to the status code 
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG
}
response = requests.get("https://api.sunrise-sunset.org/json", params= parameters, verify= False)
response.raise_for_status()


