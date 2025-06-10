luku1 = 0
luku2 = 0

while True:
    print("Tämä laskin osaa seuraavat toiminnot:", "1) Anna luvut", "2) Summa", "3) Erotus", "4) Tulo", "5) Osamäärä", "6) Potenssi", "0) Lopeta", sep="\n")
    toiminto = input("Valitse toiminto (0-6): ")
    if toiminto == "1":
        luku1 = int(input("Anna ensimmäinen luku: "))
        luku2 = int(input("Anna toinen luku: "))
        print("Annoit luvut", luku1, "ja", luku2)
    elif toiminto == "2":
        print("Summa", luku1, "+", luku2, "=", luku1 + luku2)
    elif toiminto == "3":
        print("Erotus", luku1, "-", luku2, "=", luku1 - luku2)
    elif toiminto == "4":
        print("Tulo", luku1, "*", luku2, "=", luku1 * luku2)
    elif toiminto == "5":
        if luku2 == 0:
            print("Nollalla ei voi jakaa.")
        else:
            print("Osamäärä", luku1, "/", luku2, "=", round(luku1 / luku2, 2))
    elif toiminto == "6":
        print("Potenssi", luku1, "**", luku2, "=", luku1 ** luku2)
    elif toiminto == "0":
        print("Lopetetaan")
        break
    else:
        print("Tuntematon valinta, yritä uudestaan.")

print("Kiitos ohjelman käytöstä.")
