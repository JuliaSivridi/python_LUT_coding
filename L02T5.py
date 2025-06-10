print("Tämä ohjelma laskee antamiesi 3 luvun keskiarvon.")

luku1 = int(input("Anna luku 0 ja 10 väliltä: "))
luku2 = int(input("Anna toinen luku 0 ja 10 väliltä: "))
luku3 = int(input("Anna kolmas luku 0 ja 10 väliltä: "))
print("")

print("Antamiesi lukujen summa on", luku1 + luku2 + luku3, end=".\n")
print("Antamiesi lukujen keskiarvo on", (luku1 + luku2 + luku3)/3, end=".\n")
print("Keskiarvo on kokonaislukuna", int((luku1 + luku2 + luku3)/3), end=".\n")
print("Keskiarvo pyöristettynä 3 desimaalin tarkkuuteen on", round((luku1 + luku2 + luku3)/3, 3), end=".\n")

print("Kiitos ohjelman käytöstä.")
