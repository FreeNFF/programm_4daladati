import requests

valstsis = ["Latvia", "Estonia", "Lithuania", "Poland", "Germany", "France", "Spain", "Italy", "Portugal", "Greece"]

def dati_valsts():
  url = f"https://restcountries.com/v2/name/{name}/fullText=true"
  response = requests.get(url)
  dati = response.json()[0]
  return {
    "Valsts" : dati["name"],
    "Galvaspilsēta" : dati["capital"],
    "Iedzīvotāji" : dati["population"],
    "Valūta" : dati["currencies"][0]["name"],
    "Reģions": dati["region"]
    }