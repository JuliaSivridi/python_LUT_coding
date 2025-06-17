######################################################################
# CT10A0013 Ohjelmointi Pythonilla
# Tekijä: Iuliia Sivridi
# Opiskelijanumero: 003171020
# Päivämäärä: 16/06/2025
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L11T1.py

def paaohjelma():
    luku = int(input("Anna luku: "))
    i = 0
    while (i+1)**2 <= luku:
        i += 1
    if (luku - i ** 2 <= (i+1) ** 2 - luku):
        print(f"Neliöjuuri on {i}")
    else:
        print(f"Neliöjuuri on {i+1}")

    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
# eof