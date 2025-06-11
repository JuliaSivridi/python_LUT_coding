def TiedostoKirjoita(tnimi):
    tiedosto = open(tnimi, "w")
    while True:
        nimi = input("Anna tiedostoon tallennettava nimi (0 lopettaa): ")
        if nimi == "0":
            break
        tiedosto.write(nimi+"\n")
    tiedosto.close()

def TiedostoLue(tnimi):
    print("Tiedostoon '"+tnimi+"' on tallennettu seuraavat nimet:")
    tiedosto = open(tnimi, "r")
    while True:
        rivi = tiedosto.readline()
        if rivi == "":
            break
        print(rivi, end="")
    tiedosto.close()

def paaohjelma():
    tiedoston_nimi = input("Anna tallennettavan tiedoston nimi: ")
    TiedostoKirjoita(tiedoston_nimi)
    TiedostoLue(tiedoston_nimi)
    print("Kiitos ohjelman käytöstä.")

paaohjelma()
