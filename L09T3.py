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
# Tehtävä L09T3.py

import sys

def lueTiedosto(tnimi, lista):
    try:
        ltiedosto = open(tnimi, "r")
        while True:
            luku = ltiedosto.readline()[:-1]
            if len(luku) > 0:
                lista.append(luku)
            else:
                break
        ltiedosto.close()
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tnimi))
        sys.exit(0)
    return lista

def analysoiTiedot(lista, merkit):
    for l in lista:
        if l not in merkit:
            merkit.append(l)
    print(f"Tiedostossa oli {len(merkit)} eri automerkkiä.")
    return None

def talennaTiedosto(tnimi, merkit):
    try:
        ktiedosto = open(tnimi, "w", encoding="utf-8")
        for m in merkit:
            print(m)
            ktiedosto.write(str(m)+'\n')
        ktiedosto.close()
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tnimi))
        sys.exit(0)
    return None

def paaohjelma():
    lista = []
    merkit = []
    lnimi = input("Anna luettavan tiedoston nimi: ")  # L09T3D1.txt L09T3D2.txt L09T3D3.txt
    knimi = input("Anna kirjoitettavan tiedoston nimi: ") # L09T3T1.txt

    lista = lueTiedosto(lnimi, lista)
    if (len(lista) > 0):
        analysoiTiedot(lista, merkit)
        talennaTiedosto(knimi, merkit)

    else:
        print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")

    lista.clear()
    merkit.clear()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
# eof