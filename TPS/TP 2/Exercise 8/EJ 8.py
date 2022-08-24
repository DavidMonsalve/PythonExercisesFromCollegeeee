x = []
n = int(input("cantidad de valores: "))

for i in range (n):
    elemento = int(input("elemento: "))
    while (elemento > 200) or (elemento < 100) or (elemento % 2 == 0):
        print("elemento invalido, intente de nuevo")
        elemento = int(input("elemento: "))
    x.append(elemento)
print(x)