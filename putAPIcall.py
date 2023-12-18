import requests

header = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json'
}

put_payload = {
    "id": 150,
    "title": "Shon Testing API New",
    "dueDate": "2023-12-18T12:10:32.0848819+00:00",
    "completed": True
}

responsePut = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/150"
                         , json=put_payload, headers=header)

print(responsePut.status_code)

data = responsePut.json()
print(data['title'])

assert responsePut.status_code == 200
assert data['title'] == 'Shon Testing API New'
