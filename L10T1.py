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
# Tehtävä L10T1.py

import sys

def lueTiedosto(tnimi, lista):
    try:
        ltiedosto = open(tnimi, "r")
        while True:
            auto = ltiedosto.readline()[:-1]
            if len(auto) > 0:
                lista.append(auto)
            else:
                break
        ltiedosto.close()
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tnimi))
        sys.exit(0)
    return lista

def analysoiTiedot(lista, autot):
    for l in lista:
        if l not in autot:
            autot[l] = 1
        else:
            autot[l] += 1
    return autot

def talennaTiedosto(tnimi, autot):
    try:
        autot_sorted = dict(sorted(autot.items(), key=lambda x:x[0]))
        ktiedosto = open(tnimi, "w", encoding="utf-8")
        mjono = f"Tunnistettiin {len(autot)} automerkkiä ja {sum(autot.values())} autoa:"
        print(mjono)
        ktiedosto.write(mjono + '\n')
        for merkki, maara in autot_sorted.items():
            postfix = "" if (maara == 1) else "a"
            mjono = f"{merkki}: {maara} auto{postfix}"
            print(mjono)
            ktiedosto.write(mjono+'\n')
        ktiedosto.close()
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tnimi))
        sys.exit(0)
    return None

def paaohjelma():
    lista = []
    autot = {}
    lnimi = input("Anna luettavan tiedoston nimi: ")  # L09T3D1.txt L09T3D2.txt L09T3D3.txt
    knimi = input("Anna kirjoitettavan tiedoston nimi: ") # L10T1T1.txt

    lista = lueTiedosto(lnimi, lista)
    if (len(lista) > 0):
        autot = analysoiTiedot(lista, autot)
        talennaTiedosto(knimi, autot)

    else:
        print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")

    lista.clear()
    autot.clear()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
# eof