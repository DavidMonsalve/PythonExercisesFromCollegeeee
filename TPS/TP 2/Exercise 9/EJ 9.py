from ast import Not
from random import randint

def generar(x, cant, A, B):
    for i in range (cant):
        elemento = randint(1, 1000)
        while (elemento < A) or (elemento > B) or (elemento % 7 != 0) or (elemento % 5 == 0):
            elemento = randint(1, 1000)
        print("Elemento valido encontrado: ", elemento)
        x.append(elemento)
    return x




x = []
A = int(input("A: "))
B = int(input("B: "))
cant = int(input("cantidad de elementos: "))

lista = generar(x, cant, A, B)
print(lista)