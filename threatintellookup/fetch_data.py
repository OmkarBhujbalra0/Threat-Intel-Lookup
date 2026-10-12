import requests 
import os
from dotenv import load_dotenv
import json

load_dotenv()

url = 'https://api.abuseipdb.com/api/v2/blacklist'

headers = {
    "Key": os.environ['API_KEY'],
    "Accept": "application/json",
}

params = {
    "limit": 50,
}

res = requests.get(url, headers=headers, params=params)
print(res.status_code)
print(res.json())

with open('blacklist.json','w') as f:
    json.dump(res.json(),f,indent=4)