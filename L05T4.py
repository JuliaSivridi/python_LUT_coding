MIN = 5
MAX = 15

def kysy_merkkijono():
    jono = input(f"Anna merkkijono, {MIN}-{MAX} merkkiä: ")
    return jono

def tarkista(merkkijono):
    pituus = 0
    for merkki in merkkijono:
        pituus += 1
    if pituus < MIN:
        print(f"Liian lyhyt, {pituus} merkkiä, anna uusi.")
    elif pituus > MAX:
        print(f"Liian pitkä, {pituus} merkkiä, anna uusi.")
    else:
        print(f"Annoit sopivan merkkijonon, {pituus} merkkiä.")
    if pituus > 0:
        return pituus
    return None

def paaohjelma():
    merkkijono = kysy_merkkijono()
    while True:
        p = tarkista(merkkijono)
        if not p:
            break
        elif not (5 <= p <= 15):
            merkkijono = kysy_merkkijono()
        else:
            break
    print("Kiitos ohjelman käytöstä.")

paaohjelma()
