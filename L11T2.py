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
# Tehtävä L11T2.py

def paaohjelma():
    kuut = int(input("Anna kuukausien lukumäärä: "))
    ennen = 1
    kanit = 1
    for _ in range(kuut-1):
        ennen, kanit = kanit, kanit + ennen
    print(f"Kanipariskuntia on {kuut} kuukauden kuluttua {kanit}")

    print("Kiitos ohjelman käytöstä.")

paaohjelma()
# eof