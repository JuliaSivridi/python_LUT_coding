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
# Tehtävä L13T2.py

import sys

def paaohjelma():
    args = sys.argv
    args.pop(0)

    parilliset = []
    for num in args:
        if int(num) % 2 == 0:
            parilliset.append(int(num))

    print("Syötteen parilliset luvut ovat seuraavat:")
    for p in parilliset:
        print(p, end=' ')
    print(f"\nLukujen keskiarvo on {sum(parilliset)/len(parilliset):.2f}.")

    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
# eof