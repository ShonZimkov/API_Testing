import requests

header = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json'
}

request_payload = {
    "id": 150,
    "title": "Shon Testing API",
    "dueDate": "2023-12-18T12:10:32.0848819+00:00",
    "completed": True
}

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities"
                         , json=request_payload, headers=header)

print(response.status_code)
print(response.json())

data = response.json()
print(data['id'])

assert response.status_code == 200
assert data['id'] == 150
