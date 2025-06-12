alfabets = [
    "A", "Ā", "B", "C", "Č", "D", "E", "Ē", "F", "G", "Ģ", "H", "I", "Ī", "J",
    "K", "Ķ", "L", "Ļ", "M", "N", "Ņ", "O", "P", "R", "S", "Š", "T", "U", "Ū",
    "V", "Z", "Ž"
]

vardi = [
    "Ainaži", "Saulkrasti", "Dobele", "Sigulda", "Tukums", "Liepāja", "Talsi",
    "Ludza", "Cēsis", "Gulbene", "Ventspils", "Vecumnieki", "Engure", "Ērgļi",
    "Staicele", "Kuldīga", "Aizpute", "Krāslava", "Madona", "Jūrmala", "Rīga"
]


def izvade():
  for rinda in alfabets:
    print(rinda)


def sarindošana():
  for rinda in vardi:
    pirmais_burts = rinda[0]
    for karta in alfabets:
      primais_alfabet = karta[0]

      if pirmais_burts.upper() in alfabets:
        alfabets.insert(alfabets.index(pirmais_burts[0].upper()), rinda)
        alfabets.remove(pirmais_burts.upper())

      elif pirmais_burts.upper() in primais_alfabet:
        alfabets.insert(alfabets.index(karta), rinda)
        alfabets.remove(karta)


while True:
  atbilde = input("Vai vēlaties iziet no programmas? (ja/ne): ")
  if atbilde == "ja":
    print("Programma ir izslēgta.\n\n------------------------\n")
    break

  elif atbilde == "ne":
    print("Programma turpinās.")
    pilseta = input("Ievadiet pilsēts nosaukumu: ")
    
    while True:
      if pilseta[0].isupper() and pilseta.isalpha() and " " not in pilseta:
        vardi.append(pilseta)
        break
        
      else:
        pilseta = input(
            "Nepareiza ievade. Pilsētas nosaukumam jāsākas ar lielo burtu, satur tikai burtus un vairāk nekā viens vārds.\nIevadiet pilsētas nosaukumu:"
        )

  else:
    print("Nepareiza ievade. Ievadiet 'ja' vai 'ne'.\n")

sarindošana()
izvade()