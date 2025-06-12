######################################################################
# CT10A0013 Ohjelmointi Pythonilla
# Tekijä: Iuliia Sivridi
# Opiskelijanumero: 003171020
# Päivämäärä: 12/06/2025
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T5.py
# Kirjasto: L08T5Kirjasto.py versio 1.0

class Tuote:
    def __init__(self, tunniste, lukumaara, hinta):
        self.tunniste = tunniste
        self.lukumaara = int(lukumaara)
        self.hinta = float(hinta)

def lueTiedosto(lnimi, tiedot):
    ltiedosto = open(lnimi, "r", encoding="utf-8")
    while True:
        rivi = ltiedosto.readline()[:-1]
        if len(rivi) > 0:
            tiedot.append(rivi)
        else:
            break
    ltiedosto.close()
    print(f"Tiedosto '{lnimi}' luettu, {len(tiedot)} riviä.\n")

def analysoiTiedot(tiedot, tulot):
    arvo = 0
    for t in tiedot:
        osat = t.split(';')
        tuote = Tuote(osat[0], osat[1], osat[2])
        tulot.append(round((tuote.lukumaara * tuote.hinta), 2))
        arvo += tulot[-1]
    print(f"Tiedot analysoitu, varaston arvo on {arvo:.2f} EUR.\n")

def tallennaTulokset(knimi, tulot):
    ktiedosto = open(knimi, "w", encoding="utf-8")
    for tulo in tulot:
        ktiedosto.write(f'{tulo:.2f}\n')
    ktiedosto.close()
    print(f"Tulokset tallennettu tiedostoon '{knimi}'.\n")
# eof