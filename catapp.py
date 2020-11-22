import json
import requests
import os

api_token = 'DB_PASS'
response = requests.get('https://api.thecatapi.com/v1/images/search?breed_id=beng')

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())