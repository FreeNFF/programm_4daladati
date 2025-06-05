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

    valsts_ar_lielako_populaciju = max(dati, key=lambda x: x.get("population", 0))
    valsts_lielaka = valsts_ar_lielako_populaciju.get("name", {}).get("common", "Nezināms")
    populacija = valsts_ar_lielako_populaciju.get("population", 0)
    print(f"Lielākais iedzīvotāju skaits ({populacija}) ir valstī {valsts_lielaka}.")

    kop_zeme = sum(valstis["area"] for valstis in dati)
    print(f"Valstu kopējā platība ir {kop_zeme:.2f}.")

    for valstis in dati:
        if valstis.get("name",{}).get("common","Nezināms") == "Latvia":
            print("Latvija pieder pie šada apakšreģiona:")
            print(valstis.get("subregion"))
    
    for valstis in dati:
        if valstis.get("name",{}).get("common","Nezināms") == "Latvia":
            print("Latvija robežojas ar šādām valstīm:")
            print(valstis.get("borders"))
