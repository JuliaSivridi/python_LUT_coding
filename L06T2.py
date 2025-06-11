def paaohjelma():
    nimet = 0
    merkit = 0

    tiedoston_nimi = input("Anna luettavan tiedoston nimi: ") # L06T2D2.txt L06T2D3.txt
    tiedosto = open(tiedoston_nimi, "r", encoding="utf-8")
    while True:
        nimi = tiedosto.readline()
        nimet += 1
        merkit += len(nimi)
        if nimi == "":
            nimet -= 1
            break
    tiedosto.close()
    keskm = int(round((merkit - nimet) / nimet))

    print(f"Tiedostossa oli {nimet} nimeä ja {merkit} merkkiä.")
    print(f"Keskimääräinen nimen pituus oli {keskm} merkkiä.")

    print("Kiitos ohjelman käytöstä.")

paaohjelma()
