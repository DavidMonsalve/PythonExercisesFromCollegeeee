from random import randint as azar

lista = []
for i in range(5):
    lista.append(azar(1, 10))
    print(lista[i], end=" ")
print()

invertida = []
for i in range(len(lista)):
    invertida.append(lista[-1])
    lista.pop()
    print(invertida[i], end=" ")
print()