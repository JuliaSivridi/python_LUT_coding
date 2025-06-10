pituus = int(input("Anna pituus (cm): "))
massa = int(input("Anna paino (kg): "))

osa = ((pituus / 100) ** 2)
painoindeksi = round(massa / osa, 1)

if painoindeksi <= 17:
    print("Painoindeksi on", painoindeksi, "(Vaarallinen aliravitsemus)")
elif 17 < painoindeksi < 18.5:
    print("Painoindeksi on", painoindeksi, "(Liiallinen laihuus)")
elif 18.5 <= painoindeksi < 25:
    print("Painoindeksi on", painoindeksi, "(Normaali paino)")
elif 25 <= painoindeksi < 30:
    print("Painoindeksi on", painoindeksi, "(Ylipaino eli lievä lihavuus)")
elif 30 <= painoindeksi < 35:
    print("Painoindeksi on", painoindeksi, "(Merkittävä lihavuus)")
elif 35 <= painoindeksi < 40:
    print("Painoindeksi on", painoindeksi, "(Vaikea lihavuus)")
elif 40 <= painoindeksi:
    print("Painoindeksi on", painoindeksi, "(Sairaalloinen lihavuus)")

tavoiteindeksi = float(input("Anna tavoiteindeksi: "))
uus_massa = tavoiteindeksi * osa
if tavoiteindeksi < painoindeksi:
    print("Tavoiteindeksi vastaa", round(massa - uus_massa, 1), "kg alhaisempaa painoa.")
elif tavoiteindeksi > painoindeksi:
    print("Tavoiteindeksi vastaa", round(uus_massa - massa, 1),"kg suurempaa painoa.")

print("Kiitos ohjelman käytöstä.")
