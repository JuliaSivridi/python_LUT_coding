######################################################################
# CT10A0013 Ohjelmointi Pythonilla
# Tekijä: Iuliia Sivridi
# Opiskelijanumero: 003171020
# Päivämäärä: 16/06/2025
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L11T3.py

def tulosta(sana, maara, nyt=1):
    if (nyt <= maara):
        print(f"Sana on '{sana}', {nyt}. kerta.")
        return tulosta(sana, maara, nyt+1)

def paaohjelma():
    sana = input("Anna tulostettava sana: ")
    maara = int(input("Anna tulostuskertojen määrä: "))
    tulosta(sana, maara)

    print("Kiitos ohjelman käytöstä.")

paaohjelma()
# eof