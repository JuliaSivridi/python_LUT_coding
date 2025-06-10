luku = int(input("Anna positiivinen kokonaisluku: "))
print("Luku", luku, "kerrottuna itsellään on", luku * luku)

sade = int(input("Anna ympyrän säteen pituus kokonaislukuna: "))
keha = 3.14 * 2 * sade
pintaala = 3.14 * sade * sade
print("Ympyrän säde on ", sade, ", kehä on ", keha, " ja pinta-ala on ", pintaala, ".", sep="")

yhden = int(input("Anna suorakulmion yhden sivun pituus kokonaislukuna: "))
toisen = int(input("Anna suorakulmion toisen sivun pituus kokonaislukuna: "))
print("Suorakulmion sivut ovat ", yhden, " ja ", toisen, sep="", end=";")
print(" kehä on ", (2 * (yhden + toisen)), sep="", end=";")
print(" ja pinta-ala on ", (yhden * toisen), ".", sep="")

print("Kiitos ohjelman käytöstä.")
