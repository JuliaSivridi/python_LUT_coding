######################################################################
# CT10A0013 Ohjelmointi Pythonilla
# Tekijä: Iuliia Sivridi
# Opiskelijanumero: 003171020
# Päivämäärä: 19/06/2025
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L14T4.py

import sys
import random
from random import randint

def makeRandom(tiedot, m, a, y):
    for i in range(m):
        tiedot.append(randint(a, y))
    return tiedot

def talennaTiedosto(tnimi, tiedot, m, a, y):
    try:
        ktiedosto = open(tnimi, "w", encoding="utf-8")
        ktiedosto.write(f"Arvottu {m} lukua väliltä {a}-{y}:\n")
        for tieto in tiedot:
            ktiedosto.write(str(tieto) + '\n')
        ktiedosto.close()
        print(f"Tiedosto '{tnimi}' luotu, kiitos ohjelman käytöstä.")
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tnimi))
        sys.exit(0)
    return None

def paaohjelma():
    random.seed(1)
    tiedot = []
    print("Tämä ohjelma arpoo haluamasi määrän kokonaislukuja halutulta väliltä\nja kirjoittaa ne tekstitiedostoon.")
    knimi = input("Anna tehtävän tiedoston nimi: ")  # L14T4T1.txt
    m, a, y = map(int, input("Anna lukujen määrä, Alaraja ja yläraja, esim. 7 1 37: ").split(" "))
    tiedot = makeRandom(tiedot, m, a, y)
    talennaTiedosto(knimi, tiedot, m, a, y)
    tiedot.clear()
    return None

paaohjelma()
# eof