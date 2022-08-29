def crear(filas, columnas):
    matriz [0*columnas in range (filas)]

def a(filas):
    matriz = []
    cantidad = 0
    for i in range(filas):
        matriz[i][i] = i + cantidad
        cantidad = 2
    print(matriz)
        



filas = int(input("dimension de la matriz: "))
columnas = filas

a(filas)