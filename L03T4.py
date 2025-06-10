sana1 = input("Anna sana 1: ")
sana2 = input("Anna sana 2: ")
if sana1 < sana2:
    print("'", sana1, "' on aakkosissa aiemmin kuin '", sana2, "'.", sep="")
elif sana2 < sana1:
    print("'", sana2, "' on aakkosissa aiemmin kuin '", sana1, "'.", sep="")
else:
    print("Sanat ovat samoja.")

if 'z' in sana1:
    print("Kirjain 'z' löytyy sanasta 1.")
if 'z' in sana2:
    print("Kirjain 'z' löytyy sanasta 2.")
if not ('z' in sana1) and not ('z' in sana2):
    print("Kummastakaan sanasta ei löytynyt kirjainta 'z'.")

palindromi = input("Anna testattava sana: ")
if palindromi == palindromi[::-1]:
    print("Antamasi sana '", palindromi, "' on palindromi.", sep="")
else:
    print("Antamasi sana ei ole palindromi.")
    print("Se on väärinpäin '", palindromi[::-1], "' ja oikein päin '", palindromi, "'.", sep="")

print("Kiitos ohjelman käytöstä.")
