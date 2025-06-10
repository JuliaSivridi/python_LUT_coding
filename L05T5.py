def valikko():
    print("Tämä laskin osaa seuraavat toiminnot:")
    print("1) Anna luvut")
    print("2) Summa")
    print("3) Osamäärä")
    print("0) Lopeta")
    valinta = int(input("Valitse toiminto (0-3): "))
    return valinta

def annaluku(prompt):
    luku = int(input(prompt))
    return luku

def summa(a, b):
    return f"Summa {a} + {b} = {a + b}"

def osamaara(a, b):
    if b == 0:
        return "Nollalla ei voi jakaa."
    else:
        return f"Osamäärä {a} / {b} = {round(a / b, 2)}"

def paaohjelma():
    luku1 = 0
    luku2 = 0
    while True:
        toiminto = valikko()
        if toiminto == 1:
            luku1 = annaluku("Anna ensimmäinen luku: ")
            luku2 = annaluku("Anna toinen luku: ")
            print("Annoit luvut", luku1, "ja", luku2)
        elif toiminto == 2:
            print(summa(luku1, luku2))
        elif toiminto == 3:
            print(osamaara(luku1, luku2))
        elif toiminto == 0:
            print("Lopetetaan")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
    print("Kiitos ohjelman käytöstä.")

paaohjelma()
