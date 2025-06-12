######################################################################
# CT10A0013 Ohjelmointi Pythonilla
# Tekijä: Iuliia Sivridi
# Opiskelijanumero: 003171020
# Päivämäärä: 12/06/2025
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T1.py

import math
import random
from random import randint

def valikko():
    print("Mitä haluat tehdä:")
    print("1) Laskea ympyrän pinta-alan")
    print("2) Arvata luvun")
    print("0) Lopeta")
    valinta = int(input("Valintasi: "))
    return valinta

def ympyranLaskenta():
    sade = int(input("Anna ympyrän säde kokonaislukuna: "))
    ala = math.pi * math.pow(sade, 2)
    print(f"Säteellä {sade} ympyrän pinta-ala on {ala:.2f}.\n")

def arvaLuku():
    random.seed(1)
    arva = randint(0, 1000)
    luku = -1
    kierro = 0
    print("Arvaa ohjelman arpoma kokonaisluku.")
    while (luku != arva):
        luku = int(input("Anna kokonaisluku välillä 0-1000: "))
        kierro += 1
        if (luku < arva):
            print("Haettu luku on suurempi.")
        elif (luku > arva):
            print("Haettu luku on pienempi.")
        else:
            print(f"Oikein! Käytit arvaamiseen {kierro} kierrosta.\n")

def paaohjelma():
    print("Tämä ohjelma käyttää kirjastoja tehtävien ratkaisemiseen.")
    toiminto = 1
    while (toiminto != 0):
        toiminto = valikko()
        if toiminto == 1:
            ympyranLaskenta()
        elif toiminto == 2:
            arvaLuku()
        elif toiminto == 0:
            print("Kiitos ohjelman käytöstä.")
        else:
            print("Tuntematon valinta, yritä uudestaan.")

paaohjelma()
# eof