#! /usr/bin/env python

import requests
import json
from getpass import getpass


# insert your api key here for the location
print('Enter your the City of where you want know the current weather.')
city_name = input()


# insert your api key here for the location
print('Enter your the State whole name of where you want know the current weather.')
state = input() 

# who do you want to send this information to?
print('To whom would you like to send this weather information to? Enter their email now.')
whoto = input()

weather_api_key = getpass('enter you weather api key now.')

webexapikey = getpass('enter your webex api key now.')

wurl = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{state}&units=imperial&appid={weather_api_key}'

payload = {}
headers= {}

response = requests.request("GET", wurl, headers=headers, data = payload)

print(response.text.encode('utf8'))

message_dict = response.json()
message = json.dumps(message_dict, indent= 4)




url = "https://api.ciscospark.com/v1/messages"

payload = {
    "text": message,
    "toPersonEmail": whoto
}

headers = {
    'Authorization': 'Bearer ' + webexapikey,
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

print(response.text.encode('utf8'))

