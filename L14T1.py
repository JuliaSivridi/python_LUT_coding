######################################################################
# CT10A0013 Ohjelmointi Pythonilla
# Tekijä: Iuliia Sivridi
# Opiskelijanumero: 003171020
# Päivämäärä: 19/06/2025
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L14T1.py

def paaohjelma():
    km = float(input("Anna vuotuiset kilometrit: "))
    pk = float(input("Anna moottorin polttoaineen kulutus (l/100km): "))
    ph = float(input("Anna polttoaineen hinta (€/l): "))
    ai = float(input("Anna auton ikä vuosissa: "))
    vm = float(input("Anna vakuutusten määrä (euroissa): "))
    b = float(input("Anna bonusprosentti kokonaislukuna: ")) / 100
    verot = float(input("Anna verojen määrä: "))

    kokosumma = 0
    for v in range(5):
        summa = (km/100 * pk * ph) + (vm * (1 - b)) + verot + (200 * (ai + v) ** .5)
        kokosumma += summa
        print(f"{v+1}. vuosi: {int(round(summa, 0))}")
    print(f"Viiden vuoden aikana autoon käytettiin rahaa {int(round(kokosumma, 0))} euroa.")

    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
# eof