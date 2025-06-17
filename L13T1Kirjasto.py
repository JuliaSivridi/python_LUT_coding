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
# Kirjasto: L13T1Kirjasto.py

import sys

class Henkilo:
    def __init__(self, nimi, puhelin, ika):
        self.nimi = nimi
        self.puhelin = puhelin
        self.ika = int(ika)

def kysyTiedosto(prompt):
    return input(prompt)

def lueTiedosto(tnimi, tiedot):
    try:
        rivit = []
        ltiedosto = open(tnimi, "r")
        while True:
            rivi = ltiedosto.readline()[:-1]
            if len(rivi) > 0:
                rivit.append(rivi)
            else:
                break
        ltiedosto.close()
        for rivi in rivit:
            osat = rivi.split(";")
            tiedot.append(Henkilo(osat[0], osat[1], osat[2]))
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tnimi))
        sys.exit(0)
    return tiedot

def tulosta(tiedot):
    for hklo in tiedot:
        print(f"{hklo.nimi} on {hklo.ika} vuotta vanha ja hänen puhelinnumero on {hklo.puhelin}.")
    return None

def talennaTiedosto(tnimi, tiedot):
    ika = int(input("Minkä ikäiset ihmiset otetaan mukaan tiedostoon (vuosia): "))
    maara = 0
    rivit = []
    for hklo in tiedot:
        if hklo.ika >= ika:
            maara += 1
            rivit.append(f"{hklo.nimi};{hklo.puhelin};{hklo.ika}\n")
    otsiko = f"Tiedostossa on mukana {maara} vähintään {ika} vuotiasta henkilöä:\n"
    try:
        ktiedosto = open(tnimi, "w", encoding="utf-8")
        ktiedosto.write(otsiko)
        ktiedosto.writelines(rivit)
        ktiedosto.close()
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tnimi))
        sys.exit(0)
    return None
# eof