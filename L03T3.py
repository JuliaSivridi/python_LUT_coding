luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
print("Laskin osaa seuraavat toiminnot:", "1) Summa", "2) Erotus", "3) Tulo", "4) Osamäärä", "5) Potenssi", sep="\n")
print("Antamasi luvut ovat", luku1, "ja", luku2)
toiminto = input("Valitse toiminto (1-5): ")
if toiminto == "1":
    print("Summa", luku1, "+", luku2, "=", luku1 + luku2)
elif toiminto == "2":
    print("Erotus", luku1, "-", luku2, "=", luku1 - luku2)
elif toiminto == "3":
    print("Tulo", luku1, "*", luku2, "=", luku1 * luku2)
elif toiminto == "4":
    if luku2 == 0:
        print("Nollalla ei voi jakaa.")
    else:
        print("Osamäärä", luku1, "/", luku2, "=", round(luku1 / luku2, 2))
elif toiminto == "5":
    print("Potenssi", luku1, "**", luku2, "=", luku1 ** luku2)
else:
    print("Toimintoa ei tunnistettu.")

print("Kiitos ohjelman käytöstä.")
