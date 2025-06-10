def tulostaOhjeet():
    print("Tämä ohjelma etsii antamistasi luvuista pienimmän.")
    print("Ohjelman lopussa se kertoo pienimmän luvun lisäksi antamiesi\nlukujen lukumäärän.\n")

def kysyLuku(kysy):
    luku = int(input(kysy))
    return luku

def vertaileLukuja(l, vl):
    if l < vl:
        return l
    return vl

def tulostaTiedot(maara, min):
    if maara > 1:
        print("\nAnnoit", maara, "lukua.")
        print("Annetuista luvuista pienin oli ", min, ".", sep="")
    else:
        print("\nAnnoit yhden luvun, joka oli ", min, ".", sep="")

def paaohjelma():
    tulostaOhjeet()
    luku = kysyLuku("Anna positiivinen kokonaisluku: ")
    maara = 1
    min = luku

    vertaile_luku = kysyLuku("Anna vertailtava positiivinen kokonaisluku (0 lopettaa): ")
    while True:
        if vertaile_luku == 0:
            break
        maara += 1
        min = vertaileLukuja(min, vertaile_luku)
        print("Annetuista luvuista pienempi oli ", min, ".", sep="")
        vertaile_luku = kysyLuku("Anna uusi positiivinen kokonaisluku (0 lopettaa): ")

    tulostaTiedot(maara, min)
    print("Kiitos ohjelman käytöstä.")

paaohjelma()
