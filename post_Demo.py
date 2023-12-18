import requests
import json

base_url = 'https://reqres.in/api/users'

headers_test = {'Content-Type': 'application/json'}

# payload = {
#     "name": "Shon",
#     "job": "QA"
# }

json_file = open('./users.json')
json_payload = json.load(json_file)

response = requests.post(url=base_url, json=json_payload, headers=headers_test)
print(response.status_code)
print(response.text)

