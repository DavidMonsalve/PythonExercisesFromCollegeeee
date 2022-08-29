












def leerMatriz(matriz, filas, columnas):
    for f in range (filas):
        for c in range (columnas):
            print(matriz[f][c], end=" ")
        print(" ")

def cargar():
    filas = int(input("Ingrese cantidad de filas y columnas: "))
    columnas = filas
    matriz = [columnas*[0] for f in range(filas)]
    print(matriz)
    for f in range (filas):
        for c in range (columnas):
            dato = int(input("ingrese valor "))
            matriz[f][c] = dato
    leerMatriz(matriz, filas, columnas)
    return matriz


def ordenAscendente(matriz):
    matrizAscendente = list(matriz)
    filas = len(matrizAscendente[0])
    columnas = filas
    aux = 0
    i = 1
    while (i < filas):
        if matrizAscendente[i-1][0] > matrizAscendente[i][0]:
            aux = matrizAscendente[i]
            matrizAscendente[i] = matrizAscendente[i-1]
            matrizAscendente[i-1] = aux
        i += 1
    print("----matriz en orden ascendente por filas.----")
    leerMatriz(matrizAscendente, filas, columnas)

def cargarFilasAintercambiar(matriz):
    a = int(input("fila: "))
    while (a < 0) or (a > (len(matriz) - 1)):
        print("ingrese nuevamente - ERROR")
        a = int(input("fila: "))
    return a 

def intercambiarFilas(matriz, a, b):
    columnas = len(matriz[0])
    filas = len(matriz)
    print("----Intercambiando filas----")
    print("moviendo fila ", a, " al lugar de ", b)
    aux = matriz[a]
    matriz[a] = matriz[b]
    matriz[b] = aux
    leerMatriz(matriz, filas, columnas)

def transponer(matriz):
    t = [] 
    columnas = len(matriz[0])
    filas = len(matriz)
    print("-----Transponer matriz-----")
    print("MATRIZ ORIGINAL")
    leerMatriz(matriz, filas, columnas)
    for i in range (columnas):
        t.append([])
        for j in range (filas):
            t[i].append(matriz[j][i])
    
    print("MATRIZ TRANSPUESTA")
    leerMatriz(t, filas, columnas)

def promedioFila(matriz):
    fila = int(input("Fila de la cual desea saber promedio: "))
    columnas = len(matriz[0])
    sumador = 0
    for i in range (columnas):
        sumador = sumador + matriz[fila][i]
    promedio = sumador / columnas
    print(promedio)

def porcentajeImpar(matriz):
    fila = int(input("Fila de la cual desea saber porcentaje de elementos impares: "))
    columnas = len(matriz[0])
    sumador = 0
    for i in range (columnas):
        if (matriz[fila][i] % 2 != 0):
            sumador +=1
    porcentaje = (sumador/columnas)*100
    print(porcentaje, "%")

def SimetriaDiagonalPrincipal(matriz):
    print("--------------Calculando simetria de matriz con respecto a diagonal principal--------------")
    diagonalPrincipal = []
    for i in range(len(matriz)):
        diagonalPrincipal.append(matriz[i][i])
    diagonalPrincipalInvertida = list(diagonalPrincipal)
    diagonalPrincipalInvertida.reverse()
    print(diagonalPrincipal)
    print(diagonalPrincipalInvertida)

    if diagonalPrincipal == diagonalPrincipalInvertida:
        print("La matriz es simetrica en relacion a su diagonal principal!")
    else:
        print("La matriz NO es simetrica en relacion a su diagonal principal...")

def SimetriaDiagonalSecundaria(matriz):
    print("--------------Calculando simetria de matriz con respecto a diagonal secundaria--------------")
    diagonalSecundaria = []
    columna = 0
    for i in range(len(matriz)-1, -1, -1):
        diagonalSecundaria.append(matriz[i][columna])
        columna += 1
    diagonalSecundariaInvertida = list(diagonalSecundaria)
    diagonalSecundariaInvertida.reverse()
    print(diagonalSecundaria)
    print(diagonalSecundariaInvertida)

    if diagonalSecundaria == diagonalSecundariaInvertida:
        print("La matriz es simetrica en relacion a su diagonal secundaria!")
    else:
        print("La matriz NO es simetrica en relacion a su diagonal secundaria...")


matriz = cargar()
ordenAscendente(matriz)

print("----- filas a cambiar -----")
print("¿Cuales filas desea intercambiar?")
a = cargarFilasAintercambiar(matriz)
b = cargarFilasAintercambiar(matriz)
intercambiarFilas(matriz, a, b)
transponer(matriz)
promedioFila(matriz)
porcentajeImpar(matriz)
SimetriaDiagonalPrincipal(matriz)
SimetriaDiagonalSecundaria(matriz)

