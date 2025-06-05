import requests

url = "https://data.gov.lv/dati/lv/api/3/action/datastore_search?resource_id=92ac6e57-c5a5-444e-aaca-ae90c120cc3d&limit=1000"#ja limitu, tad &limit=100

response = requests.get(url)

if response.status_code == 200:
    dati = response.json()
    records = dati["result"]["records"]

    for ieraksts in records:
        if ieraksts.get("8 : Baterijas un akumulatori", "").lower() == "x":
            adrese = ieraksts.get("adrese")
            novads = ieraksts.get("pilsetanovads")
            print(f"Adrese priekš baterijām un akumulatoriem ir {adrese} un novads ir {novads}")
            
    print("\n----------------------------------------------------------\n")
    
    for ieraksts in records:
        if ieraksts.get("10 : Nolietotās riepas", "").lower() == "x":
            adrese = ieraksts.get("adrese")
            novads = ieraksts.get("pilsetanovads")
            print(f"Adrese priekš nolietotajām riepām ir {adrese} un novads ir {novads}")

    print("\n----------------------------------------------------------\n")

    for ieraksts in records:
        if ieraksts.get("3 : Metāls", "").lower() == "x":
            adrese = ieraksts.get("adrese")
            novads = ieraksts.get("pilsetanovads")
            print(f"Adrese priekš metāla ir {adrese} un novads ir {novads}")