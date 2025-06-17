######################################################################
# CT10A0013 Ohjelmointi Pythonilla
# Tekijä: Iuliia Sivridi
# Opiskelijanumero: 003171020
# Päivämäärä: 11/06/2025
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L07T3.py

def paaohjelma():
    lnimi = input("Anna tiedoston nimi: ")  # L07T3D1.txt L07T3D2.txt
    ltiedosto = open(lnimi, "r")
    rivi = ltiedosto.readline()[:-1]
    while True:
        rivi = ltiedosto.readline()[:-1]
        if rivi == "":
            break
        tiedot = rivi.split(';')
        print(f"Kello oli {tiedot[2]}, kun punnittiin marjoja {tiedot[0]}.")
    ltiedosto.close()

    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
# eof