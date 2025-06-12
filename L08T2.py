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
# Tehtävä L08T2.py

import L08T2Kirjasto

def valikko():
    print("Minkä lämpötilamuunnoksen haluat tehdä?")
    print("1) Celsius->Fahrenheit")
    print("2) Celsius->Kelvin")
    print("3) Fahrenheit->Kelvin")
    print("4) Fahrenheit->Celsius")
    print("5) Kelvin->Celsius")
    print("6) Kelvin->Fahrenheit")
    print("0) Lopeta")
    valinta = int(input("Valintasi: "))
    return valinta

def annaLampo():
    lampo = int(input("Anna lähtölämpötila: "))
    return lampo

def paaohjelma():
    print("Käytetään lämpötilamuunnoskirjaston versiota 1.0")
    toiminto = 1
    while (toiminto != 0):
        toiminto = valikko()
        if toiminto == 1:
            lahtolampo = annaLampo()
            tulolampo = round(L08T2Kirjasto.CF(lahtolampo), 2)
            print(f"Lämpötila Fahrenheit asteina: {tulolampo}\n")
        elif toiminto == 2:
            lahtolampo = annaLampo()
            tulolampo = round(L08T2Kirjasto.CK(lahtolampo), 2)
            print(f"Lämpötila Kelvin asteina: {tulolampo}\n")
        elif toiminto == 3:
            lahtolampo = annaLampo()
            tulolampo = round(L08T2Kirjasto.FK(lahtolampo), 2)
            print(f"Lämpötila Kelvin asteina: {tulolampo}\n")
        elif toiminto == 4:
            lahtolampo = annaLampo()
            tulolampo = round(L08T2Kirjasto.FC(lahtolampo), 2)
            print(f"Lämpötila Celsius asteina: {tulolampo}\n")
        elif toiminto == 5:
            lahtolampo = annaLampo()
            tulolampo = round(L08T2Kirjasto.KC(lahtolampo), 2)
            print(f"Lämpötila Celsius asteina: {tulolampo}\n")
        elif toiminto == 6:
            lahtolampo = annaLampo()
            tulolampo = round(L08T2Kirjasto.KF(lahtolampo), 2)
            print(f"Lämpötila Fahrenheit asteina: {tulolampo}\n")
        elif toiminto == 0:
            print("Kiitos ohjelman käytöstä.")
        else:
            print("Valintaa ei tunnistettu, yritä uudestaan.\n")

paaohjelma()
# eof