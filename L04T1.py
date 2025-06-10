aloitusarvo = int(input("Anna aloitusarvo: "))
lopetusarvo = int(input("Anna lopetusarvo: "))

print("Toteutus for-lauseella:")
for i in range(aloitusarvo, lopetusarvo+1):
    print(i, end=" ")

print("\n\nToteutus while-lauseella:")
j = aloitusarvo
while (j < lopetusarvo+1):
    print(j, end=" ")
    j += 1

print("\n\nKiitos ohjelman käytöstä.")
