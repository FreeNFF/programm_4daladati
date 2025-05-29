from audioop import lin2alaw
import requests

url = "https://restcountries.com/v3.1/all"
response = requests.get(url)

#pārbauda, vai no servera ir saņemta pareiz atbilde
if response.status_code == 200:
    dati = response.json()
    print(dati)

#Iegūst un izvada datus vispārpieņemtos nosaukumus

    print("Vispārpieņemtie valsts nosaukumi:")

    for valstis in dati:
        nosaukums = valstis.get("name",{}).get("common","Nezināms")
        print(nosaukums)

    kop_skaits = len(dati)
    print(f"Valsts kopējais skaits ir {kop_skaits}.")

    kop_populacija = sum(valstis["population"] for valstis in dati)
    videja_populacija = kop_populacija / kop_skaits
    print(f"Vidējais iedzīvotāju skaits ir {videja_populacija:.0f}")

    lielaka_populacija = valstis["population"] = max
    valsts_lielaka = lielaka_populacija.get("name",{}).get("common","Nezināms")
    print(f"Lielākais iedzīvotāju skaits ir valstī {valsts_lielaka}.")

    
