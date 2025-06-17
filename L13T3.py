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
# Tehtävä L13T3.py

import sys

def valikko():
    print("Anna haluamasi toiminnon numero seuraavasta valikosta: ")
    print("1) Lue tiedosto")
    print("2) Analysoi tiedot viikonpäivittäin")
    print("0) Lopeta")
    valinta = int(input("Valintasi: "))
    return valinta

def lueTiedosto(tiedot):
    tnimi = input("Anna luettavan tiedoston nimi: ") # L13T3D1.txt L13T3D2.txt L13T3D3.txt
    try:
        ltiedosto = open(tnimi, "r")
        ltiedosto.readline()
        while True:
            rivi = ltiedosto.readline()[:-1]
            if len(rivi) > 0:
                osat = rivi.split(";")
                for osa in osat:
                    if (len(osa) > 0):
                        tiedot.append(osa)
            else:
                break
        ltiedosto.close()
        print("Tiedosto luettu.")
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tnimi))
        sys.exit(0)
    return tiedot

def analysoiTiedot(tiedot, tulot):
    for date in tiedot:
        wd = date.split(",")[0]
        tulot[wd] += 1
    return None

def tulostaTulot(tulot):
    print(";Palautuksia viikonpäivittäin")
    for wd, count in tulot.items():
        print(f"{wd};{count}")
    print(f"Yhteensä;{sum(tulot.values())}")
    return None

def paaohjelma():
    tiedot = []
    tulot = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}

    toiminto = 1
    while (toiminto != 0):
        toiminto = valikko()
        if toiminto == 1:
            tiedot = lueTiedosto(tiedot)
        elif toiminto == 2:
            analysoiTiedot(tiedot, tulot)
            tulostaTulot(tulot)
        elif toiminto == 0:
            tiedot.clear()
            print("Kiitos ohjelman käytöstä.")
        else:
            print("Tuntematon valinta, yritä uudestaan.")

    return None

paaohjelma()
# eof