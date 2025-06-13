import requests

url = ""

response = requests.get(url)

dati = response.json()