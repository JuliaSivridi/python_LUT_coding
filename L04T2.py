summa = 0
lkm = 0

while True:
    kurssiarvosana = int(input("Anna kurssiarvosana väliltä 1-5 (-1 lopettaa): "))
    if kurssiarvosana == -1:
        break
    elif kurssiarvosana not in range(1,6):
        print("Väärä syöte. Vain arvosanat 1-5 kelpaavat (-1 lopettaa).")
    else:
        summa += kurssiarvosana
        lkm += 1

if lkm > 0:
    print("Arvosanojen keskiarvo on ", round(summa / lkm, 2), ".", sep="")

print("Kiitos ohjelman käytöstä.")
