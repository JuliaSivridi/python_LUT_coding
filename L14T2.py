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
# Tehtävä L14T2.py

import sys

def lueTiedosto(tnimi, tiedot):
    try:
        ltiedosto = open(tnimi, "r")
        while True:
            rivi = ltiedosto.readline()[:-1]
            if len(rivi) > 0:
                tiedot.append(rivi.lower())
            else:
                break
        ltiedosto.close()
        print(f"Luettiin {len(tiedot)} riviä tiedostosta '{tnimi}'.")
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tnimi))
        sys.exit(0)
    return tiedot

def analysoiTiedot(tiedot):
    pois = 0
    for tieto in tiedot.copy():
        if not tieto.isalpha():
            tiedot.remove(tieto)
            pois += 1
    print(f"Hylättiin {pois} riviä.")
    return tiedot

def talennaTiedosto(tnimi, tiedot):
    try:
        ktiedosto = open(tnimi, "w", encoding="utf-8")
        for tieto in tiedot:
            ktiedosto.write(tieto + '\n')
        ktiedosto.close()
        print(f"Kirjoitettiin {len(tiedot)} riviä tiedostoon '{tnimi}'.")
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tnimi))
        sys.exit(0)
    return None

def paaohjelma():
    tiedot = []
    lnimi = input("Anna luettavan tiedoston nimi: ")  # L14T2D1.txt
    tiedot = lueTiedosto(lnimi, tiedot)
    tiedot = analysoiTiedot(tiedot)
    knimi = input("Anna kirjoitettavan tiedoston nimi: ")  # L14T2T1.txt
    talennaTiedosto(knimi, tiedot)
    tiedot.clear()

    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
# eof