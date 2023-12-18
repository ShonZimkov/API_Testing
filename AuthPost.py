import requests

header = {
    'Authorization': 'Bearer 98f5f48289a00edef428fe3779f13d9f5976733c4d3d02bdc0bfd1e245a5eb0d',
    'Content-Type': 'application/json'
}

body = {
    "name": "Shon",
    "email": "shoniki95112@gmail.com",
    "gender": "female",
    "status": "active"
}

url = 'https://gorest.co.in/public/v2/users'

response = requests.post(url, json=body, headers=header)

print(response.json())
print(response.status_code)
assert response.status_code == 201

getResponse = requests.get(url + '/' + str(response.json()['id']), headers=header)
print(getResponse.json())
