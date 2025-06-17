######################################################################
# CT10A0013 Ohjelmointi Pythonilla
# Tekijä: Iuliia Sivridi
# Opiskelijanumero: 003171020
# Päivämäärä: 17/06/2025
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L13T1.py

import L13T1Kirjasto

def valikko():
    print("1) Anna tiedoston nimi")
    print("2) Lue tiedosto")
    print("3) Tulosta tiedot")
    print("4) Kirjoita tiedosto")
    print("0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta

def paaohjelma():
    tiedot = []
    lnimi, knimi = "", "L13T1T1.txt"

    print("Tämä ohjelma lukee tiedoston ja tulostaa sen tiedot näytölle.")
    toiminto = 1
    while (toiminto != 0):
        toiminto = valikko()
        if toiminto == 1:
            lnimi = L13T1Kirjasto.kysyTiedosto("Anna luettavan tiedoston nimi: ")  # L13T1D1.txt
        elif toiminto == 2:
            tiedot = L13T1Kirjasto.lueTiedosto(lnimi, tiedot)
        elif toiminto == 3:
            L13T1Kirjasto.tulosta(tiedot)
        elif toiminto == 4:
            L13T1Kirjasto.talennaTiedosto(knimi, tiedot)
        elif toiminto == 0:
            tiedot.clear()
            print("Kiitos ohjelman käytöstä.")
        else:
            print("Tuntematon valinta, yritä uudestaan.")

    return None

paaohjelma()
# eof