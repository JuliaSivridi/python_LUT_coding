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
# Tehtävä L12T2.py

import re

def annaluku(prompt):
    pattern = r"^[01]+$"
    while True:
        luku = input(prompt)
        if re.match(pattern, luku):
            return luku

def dec_bin(dec_numero):
    if dec_numero == 0:
        return "0"
    bin_numero = ""
    while dec_numero > 0:
        bin_numero = str(dec_numero % 2) + bin_numero
        dec_numero //= 2
    return bin_numero

def bin_dec(bin_numero):
    dec_numero = 0
    kerroin = 1
    for numero in reversed(bin_numero):
        dec_numero += int(numero) * kerroin
        kerroin *= 2
    return dec_numero

def paaohjelma():
    bin1 = annaluku("Anna ensimmäinen binaariluku: ")
    bin2 = annaluku("Anna toinen binaariluku: ")
    dec1 = bin_dec(bin1)
    dec2 = bin_dec(bin2)
    print(f"Bittijonosi {bin1} on kymmenkantaisena kokonaislukuna {dec1}")
    print(f"Bittijonosi {bin2} on kymmenkantaisena kokonaislukuna {dec2}")
    print(f"Lukujen {dec1} ja {dec2} erotus on {dec1-dec2}")

    print("Kiitos ohjelman käytöstä.")

paaohjelma()
# eof