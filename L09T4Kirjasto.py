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
# Tehtävä L09T4.py
# Kirjasto: L09T4Kirjasto.py versio 1.0

import sys

def lueTiedosto(tnimi, luvut):
    try:
        ltiedosto = open(tnimi, "r")
        while True:
            luku = ltiedosto.readline()[:-1]
            if len(luku) > 0:
                luvut.append(int(luku))
            else:
                break
        ltiedosto.close()
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tnimi))
        sys.exit(0)
    print(f"Luettu tiedosto '{tnimi}'.")
    return luvut

def summa(a, b):
    return f"Summa {a} + {b} = {a + b}"

def osamaara(a, b):
    if b == 0:
        return "Nollalla ei voi jakaa."
    else:
        return f"Osamäärä {a} / {b} = {round(a / b, 2)}"

def talennaTiedosto(tnimi, tulot):
    try:
        ktiedosto = open(tnimi, "w", encoding="utf-8")
        for tulo in tulot:
            ktiedosto.write(tulo+'\n')
        ktiedosto.close()
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tnimi))
        sys.exit(0)
    print(f"Tallennettu tiedosto '{tnimi}'.")
    return None

# eof