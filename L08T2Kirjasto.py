######################################################################
# CT10A0013 Ohjelmointi Pythonilla
# Tekijä: Iuliia Sivridi
# Opiskelijanumero: 003171020
# Päivämäärä: 12/06/2025
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T2.py
# Kirjasto: L08T2Kirjasto.py versio 1.0

def CF(llampo):
    return float((llampo * 9/5) + 32)

def CK(llampo):
    return float(llampo + 273.15)

def FK(llampo):
    return float((llampo - 32) * 5/9 + 273.15)

def FC(llampo):
    return float((llampo - 32) * 5/9)

def KC(llampo):
    return float(llampo - 273.15)

def KF(llampo):
    return float((llampo - 273.15) * 9/5 + 32)
# eof