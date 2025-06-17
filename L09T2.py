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
# Tehtävä L09T2.py

def valikko():
    print("Mitä haluat tehdä:")
    print("1) Testaa ValueError")
    print("2) Testaa IndexError")
    print("3) Testaa ZeroDivisionError")
    print("4) Testaa TypeError")
    print("0) Lopeta")
    while True:
        valinta = input("Valintasi: ")
        try:
            return int(valinta)
        except ValueError:
            print("Anna valinta kokonaislukuna.")

def testIE():
    lista = [11, 22, 33, 44, 55]
    try:
        indexi = int(input("Anna indeksi 0-4: "))
        print(f"Listan arvo on {lista[indexi]} indeksillä {indexi}.")
    except IndexError:
        print(f"Tuli IndexError, indeksi {indexi}.")
    lista.clear()
    return None

def testZDE():
    try:
        jakaja = int(input("Anna jakaja: "))
        print(f"4/{jakaja} on {4/jakaja:.2f}.")
    except ZeroDivisionError:
        print(f"Tuli ZeroDivisionError, jakaja {jakaja}.")
    return None

def testTE():
    try:
        numero = input("Anna numero: ")
        numero = numero * numero
    except TypeError:
        print(f"Tuli TypeError, {numero}*{numero} merkkijonoilla ei onnistunut.")
    return None

def paaohjelma():
    toiminto = 1
    while (toiminto != 0):
        toiminto = valikko()
        if toiminto == 1:
            print("Valikko-ohjelma testaa ValueError'n.")
        elif toiminto == 2:
            testIE()
        elif toiminto == 3:
            testZDE()
        elif toiminto == 4:
            testTE()
        elif toiminto == 0:
            print("Kiitos ohjelman käytöstä.")
        else:
            print("Valintaa ei tunnistettu, yritä uudestaan.")
    return None

paaohjelma()
# eof