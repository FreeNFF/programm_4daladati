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
    for row in csv_reader:
        if row["ADRESE"] == "Rīga":
            print(row)
    