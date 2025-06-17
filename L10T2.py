######################################################################
# CT10A0013 Ohjelmointi Pythonilla
# Tekijä: Iuliia Sivridi
# Opiskelijanumero: 003171020
# Päivämäärä: 14/06/2025
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L10T2.py

import sys

def lueTiedosto(tnimi, lista):
    try:
        ltiedosto = open(tnimi, "r")
        ltiedosto.readline()
        while True:
            rivi = ltiedosto.readline()[:-1]
            if len(rivi) > 0:
                lista.append(rivi)
            else:
                break
        ltiedosto.close()
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tnimi))
        sys.exit(0)
    return lista

def analysoiTiedot(lista, datat):
    for l in lista:
        osat = l.split(';')
        vuosi = osat[1][0:4]
        if vuosi not in datat:
            datat[vuosi] = 1
        else:
            datat[vuosi] += 1
    return datat

def tulosta(datat):
    datat_sorted = dict(sorted(datat.items(), key=lambda x:x[0], reverse=True))
    print("Autot lajiteltuna vuosiluvun mukaan laskevaan järjestykseen.")
    print("Vuosi: Autoja")
    for vuosi, maara in datat_sorted.items():
        print(f"{vuosi}: {maara}")
    print(f"Yhteensä {sum(datat_sorted.values())} autoa." )
    return None

def paaohjelma():
    lista = []
    datat = {}
    lnimi = input("Anna luettavan tiedoston nimi: ")  # L10T2D1.txt

    lista = lueTiedosto(lnimi, lista)
    if (len(lista) > 0):
        datat = analysoiTiedot(lista, datat)
        tulosta(datat)

    else:
        print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")

    lista.clear()
    datat.clear()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
# eof