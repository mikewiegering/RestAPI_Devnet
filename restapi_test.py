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

print('enter you weather api key now.')
weather_api_key = getpass()

print('enter your webex api key now.')
webexapikey = getpass()

wurl = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{state}&units=imperial&appid={weather_api_key}'

payload = {}
headers= {}

response = requests.request("GET", wurl, headers=headers, data = payload)

print(response.text.encode('utf8'))

message = str(response.text.encode('utf8'))


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

