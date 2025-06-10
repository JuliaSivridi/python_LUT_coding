a = int(input("Anna a:n arvo: "))
b = int(input("Anna b:n arvo: "))

while True:
    print("a:", a, "b:", b)
    if (a > 1000) or (b > 1000):
        break
    else:
        a *= 2
        b += 100

print("Kiitos ohjelman käytöstä.")
