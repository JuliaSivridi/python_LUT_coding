######################################################################
# CT10A0013 Ohjelmointi Pythonilla
# Tekijä: Iuliia Sivridi
# Opiskelijanumero: 003171020
# Päivämäärä: 13/06/2025
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L10T3.py

import numpy
R = 4
S = 4

def paaohjelma():
    print("Tämä ohjelma esittelee numpy-matriisin käyttöä.")
    Matriisi = numpy.zeros((R, S), int)
    for rivi in range(R):
        for sarake in range(S):
            Matriisi[rivi][sarake] = (rivi+1) * (sarake+1)

    print("Matriisi tulostettuna numpy-muotoilulla:")
    print(Matriisi)
    print()

    print("Matriisi tulostettuna alkiot puolipisteillä eroteltuna:")
    for rivi in range(R):
        for sarake in range(S):
            print(Matriisi[rivi][sarake], end=";")
        print()
    print()

    print("Kiitos ohjelman käytöstä.")

paaohjelma()
# eof