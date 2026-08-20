import requests

response = requests.get("https://brapi.dev/api/quote/PETR4")

print(response.status_code)
