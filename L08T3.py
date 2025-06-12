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
# Tehtävä L08T3.py

import datetime

def valikko():
    print("Mitä haluat tehdä:")
    print("1) Tunnistaa aika-olion komponentit")
    print("2) Laskea iän päivinä")
    print("3) Tulostaa viikonpäivät")
    print("4) Tulostaa kuukaudet")
    print("0) Lopeta")
    valinta = int(input("Valintasi: "))
    return valinta

def aikaKomp():
    dttoform = input("Anna päivämäärä ja kello muodossa 'pp.kk.vvvv hh:mm': ")
    dttoform = datetime.datetime.strptime(dttoform, "%d.%m.%Y %H:%M")
    print("Annoit vuoden", dttoform.year)
    print("Annoit kuukauden", dttoform.month)
    print("Annoit päivän", dttoform.day)
    print("Annoit tunnin", dttoform.hour)
    print("Annoit minuutin", dttoform.minute)
    print()

def ikaPaivat():
    bdate = input("Anna syntymäpäiväsi muodossa pp.kk.vvvv: ")
    bdate = datetime.datetime.strptime(bdate, "%d.%m.%Y")
    exdate = datetime.datetime.strptime("1.1.2000", "%d.%m.%Y")
    ika = exdate - bdate
    print(f"1.1.2000 sinä olit {ika.days} päivää vanha.")
    print()

def tulostaVP():
    date = datetime.datetime.strptime("1.6.2025", "%d.%m.%Y")
    for i in range(0, 7):
        date = date + datetime.timedelta(days=1)
        print(date.strftime("%A"))
    print()

def tulostaKK():
    date = datetime.datetime.strptime("1.12.2024", "%d.%m.%Y")
    for i in range(0, 12):
        date = date + datetime.timedelta(days=31)
        print(date.strftime("%b"))
    print()

def paaohjelma():
    print("Tämä ohjelma käyttää datetime-kirjastoa tehtävien ratkaisemiseen.")
    toiminto = 1
    while (toiminto != 0):
        toiminto = valikko()
        if toiminto == 1:
            aikaKomp()
        elif toiminto == 2:
            ikaPaivat()
        elif toiminto == 3:
            tulostaVP()
        elif toiminto == 4:
            tulostaKK()
        elif toiminto == 0:
            print("Kiitos ohjelman käytöstä.")
        else:
            print("Valintaa ei tunnistettu, yritä uudestaan.\n")

paaohjelma()
# eof