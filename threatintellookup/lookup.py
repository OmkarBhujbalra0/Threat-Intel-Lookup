import json
from dotenv import load_dotenv
import os
import requests
import time

load_dotenv()

ip_list = []

with open('blacklist.json','r') as f:
    blacklist = json.load(f)

for i in blacklist['data']:
    ip_list.append(i['ipAddress'])


url = 'https://api.abuseipdb.com/api/v2/check'

def check_ip(ip):
    headers = {'Key': os.environ['API_KEY'],'Accept':'application/json'}
    params = {'ipAddress': ip, 'maxAgeInDays': 90}
    res = requests.get(url, headers=headers, params=params)
    if res.status_code == 200:
        return res.json()['data']
    else:
        print(f"Error checking IP: {ip} - {res.status_code}")
        return None

result = []
for ip in ip_list:
    ipresult =  check_ip(ip)
    if ipresult:
        result.append(ipresult)
    time.sleep(1)

checked_ips = {ip['ipAddress']: ip for ip in result}

with open('checked.json','w') as f:
    json.dump(checked_ips,f,indent=4)