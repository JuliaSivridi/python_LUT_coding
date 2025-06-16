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
# Tehtävä L11T4.py
# Käyttämällä L11T4_pohja.py

import time
import sys

def LueTiedosto(Nimi, Numerot):
    try:
        ltiedosto = open(Nimi, "r") # L11T4D1.txt L11T4D2.txt L11T4D3.txt
        while True:
            rivi = ltiedosto.readline()[:-1]
            if len(rivi) > 0:
                Numerot.append(int(rivi))
            else:
                break
        ltiedosto.close()
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(Nimi))
        sys.exit(0)
    return Numerot

def HidasHakufunktio(Numerot):
    Luvut = ["",""]
    Luvut[0] = 0  #Pienempi luku tallennetaan tähän
    Luvut[1] = 0  #Suurempi luku tallennetaan tähän

    Mini = Numerot[0]
    Maxi = Numerot[0]

    Loytyi = False
    for Numero in Numerot:
        Mini = Numero
        for Numero2 in Numerot:
            if (Numero2 > 3 * Mini):
                Luvut[1] = Numero2
                Luvut[0] = Mini
                Loytyi = True
                break
        if Loytyi == True:
            break
    return Luvut

def NopeaHakufunktio(Numerot):
    Luvut = ["",""]
    Luvut[0] = 0  #Pienempi luku tallennetaan tähän
    Luvut[1] = 0  #Suurempi luku tallennetaan tähän

    NumSort = sorted(Numerot)
    Loytyi = False
    for Numero in NumSort:
        left, right = 0, len(NumSort)
        while left < right:
            mid = (left + right) // 2
            if NumSort[mid] > 3 * Numero:
                Luvut[1] = NumSort[mid]
                Luvut[0] = Numero
                Loytyi = True
                break
            else:
                left = mid + 1
        if Loytyi == True:
            break
    return Luvut

def paaohjelma():
    Numerot = []
    Nimi = input("Anna tiedoston nimi: ")

    Numerot = LueTiedosto(Nimi, Numerot)

    # Toteutus hitaalla versiolla (hidas versio annetaan pohjassa)
    Kello1 = time.perf_counter()
    TulosluvutHidas = HidasHakufunktio(Numerot)
    Kello2 = time.perf_counter()
    AikaHidas = Kello2 - Kello1

    # Toteutus opiskelijan tekemällä funktiolla
    Kello1 = time.perf_counter()
    TulosluvutNopea = NopeaHakufunktio(Numerot)
    Kello2 = time.perf_counter()
    AikaNopea = Kello2 - Kello1
    
    if (TulosluvutNopea[0] == 0 and TulosluvutNopea[1] == 0):
        print("Tiedostosta ei löytynyt sopivaa lukuparia.")

    elif AikaNopea < (AikaHidas / 10):
        print("Hakualgoritmi oli riittävän nopea!")
        print("Se löysi sopivan parin:", TulosluvutNopea[0], "ja", TulosluvutNopea[1])
    else:
        print("Hakualgoritmi ei ollut tarpeeksi nopea.")
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
# eof