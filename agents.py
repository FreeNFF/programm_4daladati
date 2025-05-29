import csv

with open("agenti.csv", mode="r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    print("Visi dati:")
    for row in file:
        print(row)