import requests

url = 'https://v1.apiplugin.io/v1/currency/wJr7EWfk/convert'
headers = {'Content-Type': 'application/json'}

params = {
    "amount": 1,
    "from": "sd",
    "to": "s"
}

response = requests.get(url, headers=headers, params=params)

# Print response
print(response.status_code)
print(response.json())
