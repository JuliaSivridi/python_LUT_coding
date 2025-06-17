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
# Tehtävä L09T1.py

import sys

def lueTiedosto(tnimi, lista):
    try:
        ltiedosto = open(tnimi, "r")
        while True:
            luku = ltiedosto.readline()[:-1]
            if len(luku) > 0:
                lista.append(int(luku))
            else:
                break
        ltiedosto.close()
        print("Tiedoston '{0:s}' lukeminen onnistui, {1} riviä.".format(tnimi, len(lista)))
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tnimi))
        sys.exit(0)
    return lista

def talennaTiedosto(tnimi, lista):
    try:
        ktiedosto = open(tnimi, "w", encoding="utf-8")
        for l in lista:
            ktiedosto.write(str(l)+'\n')
        ktiedosto.close()
        print("Tiedoston '{0:s}' kirjoittaminen onnistui.".format(tnimi))
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tnimi))
        sys.exit(0)
    return None

def paaohjelma():
    lista = []

    lnimi = input("Anna luettavan tiedoston nimi: ")  # L09T1D1.txt
    lista = lueTiedosto(lnimi, lista)

    knimi = input("Anna kirjoitettavan tiedoston nimi: ") # L09T1T1.txt
    talennaTiedosto(knimi, lista)

    lista.clear()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
# eof