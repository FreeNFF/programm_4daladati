import requests

url = "https://restcountries.com/v2/name/{name}/fullText=true"

response = requests.get(url)

