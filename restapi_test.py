#! /usr/bin/env python

import requests
import json

# insert your api key here for the location
print('Enter your the City of where you want know the current weather.')
city_name = input()


# insert your api key here for the location
print('Enter your the State whole name of where you want know the current weather.')
state = input() 

# who do you want to send this information to?
print('To whom would you like to send this weather information to? Enter their email now.')
whoto = input()

weather_api_key = '497dea13dacd7892ebae54c630194ee2'

wurl = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{state}&appid={weather_api_key}'

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
    'Authorization': 'Bearer Y2Q1ODI1NzItNDM5Zi00OTY3LWE4Y2ItN2I2OGJjNTM4MTAyMDFiYWM2M2EtYmU0_PF84_f88c9535-c5ce-4eb5-b166-be95180e4c32',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

print(response.text.encode('utf8'))

