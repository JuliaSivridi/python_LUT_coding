ala = int(input("Anna alueen alaraja: "))
yla = int(input("Anna alueen yläraja: "))

l = False
for luku in range(ala, yla+1):
    if (luku % 5 == 0):
        if (luku % 7 == 0):
            print("Luku", luku, "on jaollinen 5:llä ja 7:llä.")
            print("Lopetetaan etsintä.")
            l = True
            break
        else:
            print(luku, "ei ole jaollinen seitsemällä, hylätään.")
    else:
        print(luku, "ei ole jaollinen viidellä, hylätään.")
if not l:
    print("Alueelta ei löytynyt sopivaa arvoa.")

print("Kiitos ohjelman käytöstä.")
