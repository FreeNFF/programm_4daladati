import csv

with open("agenti.csv", mode="r", encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)
    print("Visi dati:")
    for row in csv_reader:
        print(row)


print("\nAtlasītie dati:\n")

with open("agenti.csv", mode="r", encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        if row["TIPS"] == "Izglītības iestāde":
            print(row)

with open("agenti.csv", mode="r", encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        if row["TIPS"] == "Valsts iestāde":
            print(row)


print("\nRīgas iestādes:\n")

with open("agenti.csv", mode="r", encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)
    for rinda in csv_reader:
        if len(rinda) >= 3:
            nosaukums = rinda[1]
            adrese_dalas = [dala.strip() for dala in rinda[2:]]

            if 'Rīga' in adrese_dalas:
                adrese = ', '.join(adrese_dalas)
                print(f"{nosaukums} - {adrese}")

    