######################################################################
# CT10A0013 Ohjelmointi Pythonilla
# Tekijä: Iuliia Sivridi
# Opiskelijanumero: 003171020
# Päivämäärä: 18/06/2025
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L14T3.py

import datetime

def paaohjelma():
    vuosi = int(input("Anna vuosi: "))
    kuukausi = int(input("Anna kuukausi: "))

    if kuukausi == 12:
        monthdays = (datetime.date(vuosi+1, 1, 1) - datetime.date(vuosi, kuukausi, 1)).days
    else:
        monthdays = (datetime.date(vuosi, kuukausi+1, 1) - datetime.date(vuosi, kuukausi, 1)).days

    weekday_start = datetime.date(vuosi, kuukausi, 1).weekday()

    weeks = {}
    w, day = 1, 1
    while day <= monthdays:
        weeks[w] = {}
        for d in range(7):
            if w == 1 and d < weekday_start:
                weeks[w][d] = ""
            elif day <= monthdays:
                weeks[w][d] = day
                day += 1
            else:
                weeks[w][d] = ""
        w += 1

    count = 0
    print("Kalenteri näyttää seuraavalle:")
    print(" Ma Ti Ke To Pe La Su")
    for week in weeks.values():
        for d in range(7):
            print(f"{week[d]:3}", end="")
            if week[d] != "":
                count += 1
            if count == monthdays:
                break
        print()
    return None

paaohjelma()
# eof