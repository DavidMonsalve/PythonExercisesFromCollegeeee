










def crear(filas, columnas):
    m = [[0]*columnas for i in range (filas)]
    return m

def a(m, filas):
    cantidad = 1
    for i in range(filas):
        m[i][i] = cantidad
        cantidad += 2
    print(m)
        



filas = int(input("filas: "))
columnas = int(input("columnas: "))

matriz = crear(filas, columnas)
print(matriz)

a(matriz, filas)