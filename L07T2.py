######################################################################
# CT10A0013 Ohjelmointi Pythonilla
# Tekijä: Iuliia Sivridi
# Opiskelijanumero: 003171020
# Päivämäärä: 11/06/2025
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L07T2.py

class AUTO:
    merkki = ""
    lkm = 0

def kysy_auto():
    auto = AUTO()
    auto.merkki = input("Anna automerkki: ")
    auto.lkm = input("Anna automerkin lukumäärä varastossa: ")
    return auto

def tulosta_auto(auto):
    print("Varastossa on nyt "+auto.merkki+"-merkkisiä autoja "+auto.lkm+" kpl.")

def paaohjelma():
    vauto = kysy_auto()
    tulosta_auto(vauto)
    print("Kiitos ohjelman käytöstä.")

paaohjelma()
# eof