def tulostaSana(l, s):
    for i in range(l):
        print(s)
    print()

def kysy():
    while True:
        sana = input("Anna teksti: ")
        if sana == "lopeta":
            print("Lopetetaan.")
            break
        luku = int(input("Anna luku: "))
        tulostaSana(luku, sana)

kysy()
print("Kiitos ohjelman käytöstä.")
