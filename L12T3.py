######################################################################
# CT10A0013 Ohjelmointi Pythonilla
# Tekijä: Iuliia Sivridi
# Opiskelijanumero: 003171020
# Päivämäärä: 16/06/2025
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Google Search + Stack Overflow
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L12T3.py

import sys
import re

def lueTiedosto(tnimi, lista):
    try:
        ltiedosto = open(tnimi, "r")
        while True:
            rivi = ltiedosto.readline()[:-1]
            if len(rivi) > 0:
                lista.append(rivi)
            else:
                break
        ltiedosto.close()
        print(f"Tiedosto '{tnimi}' luettu, {len(lista)} riviä.")
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tnimi))
        sys.exit(0)
    return None

def analysoiTiedot(lista, tulot):
    tulot.append(lista[0])
    for i in range(1, len(lista)):
        osat = lista[i].split(";")
        if (len(osat) != 3):
            print(f"Väärä määrä arvoja, rivi {i+1}: '{lista[i]}'")
        else:
            if not (re.match(r"^\d{4}$", osat[0])):
                print(f"Virheellinen ID, rivi {i+1}: '{lista[i]}'")
            else:
                try:
                    osat[2] = int(osat[2])
                except ValueError:
                    osat[2] = 0
                osat[1] = "".join(re.findall(r"[a-zA-Z0-9]", osat[1]))
                tulot.append(f"{osat[0]};{osat[1]};{osat[2]}")
    print(f"Tiedot analysoitu, {len(tulot) - 1} hyväksyttävää tietoalkiota.")
    return None

def talennaTiedosto(tnimi, tulot):
    try:
        ktiedosto = open(tnimi, "w", encoding="utf-8")
        for tulo in tulot:
            ktiedosto.write(tulo+"\n")
        ktiedosto.close()
        print(f"Tiedosto '{tnimi}' kirjoitettu, {len(tulot)} riviä.")
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tnimi))
        sys.exit(0)
    return None

def paaohjelma():
    lista = []
    tulot = []

    lnimi = input("Anna luettavan tiedoston nimi: ")  # L12T3D1.txt L12T3D2.txt eiole.txt
    knimi = input("Anna kirjoitettavan tiedoston nimi: ")  # L12T3T1.txt

    lueTiedosto(lnimi, lista)
    analysoiTiedot(lista, tulot)
    talennaTiedosto(knimi, tulot)

    lista.clear()
    tulot.clear()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
# eof