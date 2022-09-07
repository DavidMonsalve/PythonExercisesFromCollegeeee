from random import randint

def crear(filas):
    columnas = filas
    m = [[0]*columnas for i in range(filas)]
    return m

def rellenar(matriz, n):
    m = matriz
    filas, columnas = n, n
    print(filas, columnas)
    for i in range(filas):
        for j in range(columnas):
            valor = randint(0, ((n**2)-1))
            while (valor in m):
                valor = randint(0, ((n**2)-1))
            m[i][j] = valor
    print(m)


n = int(input("dimension de la matriz (NxN): "))
matriz = crear(n)
print(matriz)


rellenar(matriz, n)