lnimi = input("Anna luettavan tiedoston nimi: ") # L06T3D1.txt
knimi = "L06T3T1.txt"

ltiedosto = open(lnimi, "r", encoding="utf-8")
ktiedosto = open(knimi, "w", encoding="utf-8")
while True:
    rivi = ltiedosto.readline()[:-1]
    if rivi == "":
        break
    if rivi.isdigit():
        print("Rivi '"+rivi+"' on numerorivi.")
    else:
        if rivi == rivi[::-1]:
            print("Rivi '"+rivi+"' on palindromi.")
            ktiedosto.write(rivi + "\n")
        else:
            print("Rivi '"+rivi+"' ei ole palindromi.")
ltiedosto.close()
ktiedosto.close()

print("Kiitos ohjelman käytöstä.")
