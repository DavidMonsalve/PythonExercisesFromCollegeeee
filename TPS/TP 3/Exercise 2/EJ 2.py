









import copy

def crear(filas, columnas):
    m = [[0]*columnas for i in range (filas)]
    return m

def a(matriz, filas):
    cantidad = 1
    m = copy.deepcopy(matriz)
    for i in range(filas):
        m[i][i] = cantidad
        cantidad += 2
    print("a ", m)
        
def b(matriz, filas, columnas):
    print("---------b-----------")
    m = copy.deepcopy(matriz)
    final = columnas
    num = 27
    for i in range(filas):
        m[i][final-1] = num
        num = num // 3
        final = final - 1

    print("b ", m)

def c(matriz, filas, columnas):
    m = copy.deepcopy(matriz)
    print("---------c------------")
    cantidad = 0
    numero = 4
    for i in range(filas):

filas = int(input("filas: "))
columnas = int(input("columnas: "))

matriz = crear(filas, columnas)
print("original ", matriz)

a(matriz, filas)
b(matriz, filas, columnas)
c(matriz, filas, columnas)