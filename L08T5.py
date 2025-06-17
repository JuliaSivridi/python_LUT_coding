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
# Tehtävä L08T5.py

import L08T5Kirjasto

def valikko():
    print("Mitä haluat tehdä:")
    print("1) Lue tiedosto")
    print("2) Analysoi tiedot")
    print("3) Tallenna Tulokset")
    print("0) Lopeta")
    valinta = int(input("Valintasi: "))
    return valinta

def paaohjelma():
    tiedot = []
    tulot = []

    lnimi = input("Anna luettavan tiedoston nimi: ")  # L08T5D1.txt
    knimi = input("Anna kirjoitettavan tiedoston nimi: ")  # L08T5T1.txt

    toiminto = 1
    while (toiminto != 0):
        toiminto = valikko()
        if toiminto == 1:
            L08T5Kirjasto.lueTiedosto(lnimi, tiedot)
        elif toiminto == 2:
            if not tiedot:
                print("Tiedot puuttuvat, lue ensin tiedosto.")
            else:
                L08T5Kirjasto.analysoiTiedot(tiedot, tulot)
        elif toiminto == 3:
            if not tulot:
                print("Tietoja ei ole analysoitu.")
            else:
                L08T5Kirjasto.tallennaTulokset(knimi, tulot)
        elif toiminto == 0:
            print("Kiitos ohjelman käytöstä.")
        else:
            print("Valintaa ei tunnistettu, yritä uudestaan.\n")
    return None

paaohjelma()
# eof