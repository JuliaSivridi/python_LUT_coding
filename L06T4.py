def laske_summa(tnimi):
    summa = 0
    ltiedosto = open(tnimi, "r")
    while True:
        askel = ltiedosto.readline()[:-1]
        if askel.isdigit():
            askel = int(askel)
            summa += askel
        else:
            break
    ltiedosto.close()
    return summa

def laske_min(tnimi):
    minimi = 1000000000
    ltiedosto = open(tnimi, "r")
    while True:
        askel = ltiedosto.readline()[:-1]
        if askel.isdigit():
            askel = int(askel)
            if askel < minimi:
                minimi = askel
        else:
            break
    ltiedosto.close()
    return minimi

def laske_max(tnimi):
    maximi = 0
    ltiedosto = open(tnimi, "r")
    while True:
        askel = ltiedosto.readline()[:-1]
        if askel.isdigit():
            askel = int(askel)
            if askel > maximi:
                maximi = askel
        else:
            break
    ltiedosto.close()
    return maximi

def tulosta(tnimi, minimi, maximi, summa):
    print(f"Pienin askelmäärä oli {minimi} askelta.")
    print(f"Suurin askelmäärä oli {maximi} askelta.")
    print(f"Yhteensä askelia oli {summa} askelta.")
    ktiedosto = open(tnimi, "w", encoding="utf-8")
    ktiedosto.write(f"Pienin askelmäärä oli {minimi} askelta.\n")
    ktiedosto.write(f"Suurin askelmäärä oli {maximi} askelta.\n")
    ktiedosto.write(f"Yhteensä askelia oli {summa} askelta.\n")
    ktiedosto.close()

def paaohjelma():
    lue_nimi = input("Anna tiedot sisältävän tiedoston nimi: ") # L06T4D1.txt
    summa = laske_summa(lue_nimi)
    minimi = laske_min(lue_nimi)
    maximi = laske_max(lue_nimi)

    kir_nimi = input("Anna tallennettavan tiedoston nimi: ") # L06T4T1.txt
    tulosta(kir_nimi, minimi, maximi, summa)

    print("Kiitos ohjelman käytöstä.")

paaohjelma()
