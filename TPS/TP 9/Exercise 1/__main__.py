from random import randint as azar
lista = []
for i in range(10):
    lista.append(azar(1, 20))

listaAux = []
for i in range(len(lista)):
    listaAux.append(lista[i])

suma = 0
for i in range(len(listaAux)):
    print(listaAux[-1], end=" ")
    suma = suma + listaAux[-1]
    listaAux.pop()
    
print()
print(suma)