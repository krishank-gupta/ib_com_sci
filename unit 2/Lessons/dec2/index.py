# API Part 2

# Post Requests

import requests
from datetime import datetime

# Creating new users

# new_user = {
#     "username": "Krishank",
#     "password": "delete"
# }

# req = requests.post('http://192.168.6.142/register', json=new_user)

# print(req.json())

# Login
user = {
    "username": "Krishank",
    "password": "delete"
}

req = requests.post('http://192.168.6.142/login', json=user)
access_token = req.json()["access_token"]

print(access_token)

auth = {
    "Authorization": f"Bearer {access_token}"
}


# new_sensor = {
#     "type": "Tempeterature",
#     "location": "R1-14B",
#     "name": "temp_sensor_krish",
#     "unit": "C"
# }

# r = requests.post('http://192.168.6.142/sensor/new', json=new_sensor, headers=auth)

# print(r.json())


# Post sensor recording
new_record = {
    "datetime": datetime.isoformat(datetime.now()),
    "sensor_id": 7,
    "value": 20.10
}

r = requests.post('http://192.168.6.142/reading/new', json=new_record, headers=auth)

print(r.json())