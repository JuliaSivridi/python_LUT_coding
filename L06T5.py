def valikko():
    print("Tämä laskin osaa seuraavat toiminnot:")
    print("1) Anna luvut")
    print("2) Summa")
    print("3) Osamäärä")
    print("0) Lopeta")
    valinta = int(input("Valitse toiminto (0-3): "))
    return valinta

def TarkistaLuku(luku):
    if (luku != "" and luku.isdigit()):
        return int(luku)
    else:
        print("Luvut loppuivat, lopeta ohjelma.")
        return 0

def summa(a, b):
    return f"Summa {a} + {b} = {a + b}\n"

def osamaara(a, b):
    if b == 0:
        return "Nollalla ei voi jakaa."
    else:
        return f"Osamäärä {a} / {b} = {round(a / b, 2)}\n"

def paaohjelma():
    lnimi = input("Anna luettavan tiedoston nimi: ")  # L06T5D2.txt L06T5D1.txt
    knimi = "L06T5T1.txt"
    ltiedosto = open(lnimi, "r")
    ktiedosto = open(knimi, "w", encoding="utf-8")
    while True:
        toiminto = valikko()
        if toiminto == 1:
            luku1 = ltiedosto.readline()[:-1]
            luku1 = TarkistaLuku(luku1)
            luku2 = ltiedosto.readline()[:-1]
            luku2 = TarkistaLuku(luku2)
            print("Luettiin luvut", luku1, "ja", luku2)
        elif toiminto == 2:
            print("Tulos tallennettu tiedostoon.")
            ktiedosto.write(summa(luku1, luku2))
        elif toiminto == 3:
            print("Tulos tallennettu tiedostoon.")
            ktiedosto.write(osamaara(luku1, luku2))
        elif toiminto == 0:
            print("Lopetetaan")
            ltiedosto.close()
            ktiedosto.close()
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")

    print("Kiitos ohjelman käytöstä.")

paaohjelma()
