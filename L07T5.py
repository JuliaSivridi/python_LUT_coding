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
# Tehtävä L07T5.py

def valikko():
    print("Tämä laskin osaa seuraavat toiminnot:")
    print("1) Anna luvut")
    print("2) Summa")
    print("3) Osamäärä")
    print("0) Lopeta")
    valinta = int(input("Valitse toiminto (0-3): "))
    return valinta

def lueTiedosto(tnimi, luvut):
    ltiedosto = open(tnimi, "r")
    luku = ltiedosto.readline()[:-1]
    while (len(luku) > 0):
        luvut.append(int(luku))
        luku = ltiedosto.readline()[:-1]
    ltiedosto.close()
    print(f"Luettu tiedosto '{tnimi}'.")
    return luvut

def summa(a, b):
    return f"Summa {a} + {b} = {a + b}"

def osamaara(a, b):
    if b == 0:
        return "Nollalla ei voi jakaa."
    else:
        return f"Osamäärä {a} / {b} = {round(a / b, 2)}"

def talennaTiedosto(tnimi, tulot):
    ktiedosto = open(tnimi, "w", encoding="utf-8")
    for tulo in tulot:
        ktiedosto.write(tulo+'\n')
    ktiedosto.close()
    print(f"Tallennettu tiedosto '{tnimi}'.")
    return None

def paaohjelma():
    tulot = []
    luvut = []
    indexi = 0
    indexe = None

    lnimi = input("Anna luettavan tiedoston nimi: ")  # L06T5D2.txt L06T5D1.txt
    knimi = input("Anna kirjoitettavan tiedoston nimi: ") # L06T5T1.txt

    toiminto = 1
    while (toiminto != 0):
        toiminto = valikko()
        if toiminto == 1:
            if (indexe == None):
                luvut = lueTiedosto(lnimi, luvut)
                indexe = len(luvut) - 1
            else:
                indexi += 2

            if (indexi < indexe):
                luku1 = luvut[indexi]
                luku2 = luvut[indexi+1]
                print("Luettiin luvut", luku1, "ja", luku2)
            else:
                print("Luvut loppuivat, lopeta ohjelma.")
        elif toiminto == 2:
            tulot.append(summa(luku1, luku2))
            print("Tulos lisätty listaan.")
        elif toiminto == 3:
            tulot.append(osamaara(luku1, luku2))
            print("Tulos lisätty listaan.")
        elif toiminto == 0:
            talennaTiedosto(knimi, tulot)
            luvut.clear()
            tulot.clear()
        else:
            print("Tuntematon valinta, yritä uudestaan.")

    print("Kiitos ohjelman käytöstä.")

paaohjelma()
# eof