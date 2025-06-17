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
# Tehtävä L12T1.py

import datetime

def hetu_ok(hetu):
    hetu = hetu.upper()

    if len(hetu) != 11:
        return False

    try:
        hetu_date = datetime.datetime.strptime(hetu[0:6], "%d%m%y")
    except Exception:
        return False

    if hetu[6:7] not in ['+', '-', 'A', 'B', 'C', 'D', 'E', 'F', 'Y', 'X', 'W', 'V', 'U']:
        return False

    Tarkistusmerkkijono = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    if (Tarkistusmerkkijono[int(hetu[0:6] + hetu[7:10]) % 31] != hetu[10:11]):
        return False

    return True

def paaohjelma():
    hetu = input("Anna henkilötunnus: ")

    if hetu_ok(hetu):
        print("Henkilötunnus hyväksytty.")
    else:
        print("Henkilötunnusta ei hyväksytä.")

    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
# eof