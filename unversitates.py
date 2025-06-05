import requests

url = "http://universities.hipolabs.com/search?country=latvia"

respnse = requests.get(url)



if respnse.status_code == 200:
    dati = respnse.json()
    print(dati)

    print("Latvijas universitātes:")

    saraksts = []
    
    for universitates in dati:
        saraksts.append(universitates.get("name"))
    
    saraksts.sort()
    
    for nosaukums in saraksts:
        print(nosaukums)