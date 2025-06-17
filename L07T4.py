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
# Tehtävä L07T4.py

class AUTO:
    merkki = ""
    hinta = 0

def valikko(lista):
    print("Käytettävissä olevat toiminnot:")
    print("1) Anna auton tiedot")
    print("2) Tulosta autojen tiedot")
    print("0) Lopeta")
    valinta = int(input("Valintasi: "))
    return valinta

def kysy_auto():
    auto = AUTO()
    auto.merkki = input("Anna auton merkki: ")
    auto.hinta = int(input("Anna auton hinta: "))
    return auto

def tulosta_auto(lista):
    print("Listalta löytyy seuraavat automerkit ja hinnat:")
    for auto in lista:
          print(auto.merkki, auto.hinta)
    return None

def paaohjelma():
    print("Tämä ohjelma lisää autojen tietoja listaan ja tulostaa ne.")
    autolista = []
    while True:
        toiminta = valikko(autolista)
        if toiminta == 1:
            uus_auto = kysy_auto()
            autolista.append(uus_auto)
        elif toiminta == 2:
            tulosta_auto(autolista)
        elif toiminta == 0:
            print("Kiitos ohjelman käytöstä.")
            autolista.clear()
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
    return None

paaohjelma()
# eof