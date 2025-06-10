def ens():
    print("Nyt olemme tulosta-aliohjelmassa")
    print("Tämä aliohjelma tulostaa vain tekstiä.")
    print("Tämä sopii hyvin valikon tulostamiseen.")
    return None

def toinen(luku):
    print("Aliohjelmassa parametrin arvo on", luku)
    print("Aliohjelmassa parametrin arvo on neliöön korottamisen jälkeen", luku ** 2)

def kolmas(e, s):
    return e + " " + s

print("Ensimmäinen vaihe:")
ens()

print("\nToinen vaihe:")
luku = int(input("Anna luku: "))
print("Päätasolla ennen aliohjelmaa luku on", luku)
toinen(luku)
print("Päätasolla aliohjelman jälkeen luku on", luku)

print("\nKolmas vaihe:")
etunimi = input("Anna etunimi: ")
sukunimi = input("Anna sukunimi: ")
nimi = kolmas(etunimi, sukunimi)
print("Etunimi '", etunimi, "' ja sukunimi '", sukunimi, "' muodostavat nimen '", nimi, "'.", sep="")

print("Kiitos ohjelman käytöstä.")
