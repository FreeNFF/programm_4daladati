import requests

valstis = ["Latvia", "Estonia", "Lithuania", "Poland", "Germany", "France", "Spain", "Italy", "Portugal", "Greece"]

def dati_valsts(name):

  url = f"https://restcountries.com/v2/name/{name}/?fullText=true"
  response = requests.get(url)
  dati = response.json()[0]

  return {
    "Valsts" : dati["name"],
    "Galvaspilsēta" : dati["capital"],
    "Iedzīvotāji" : dati["population"],
    "Valūta" : dati["currencies"][0]["name"],
    "Reģions": dati["region"],
    "Karogs" : dati["flag"]
    }

for rinda in valstis:
  info = dati_valsts(rinda)
  print(f"\nValsts: {info['Valsts']}")
  print(f"Galvaspilsēta: {info['Galvaspilsēta']}")
  print(f"Iedzīvotāji: {info['Iedzīvotāji']}")
  print(f"Valūta: {info['Valūta']}")
  print(f"Reģions: {info['Reģions']}")
  print(f"Karogs: {info['Karogs']}")
  
