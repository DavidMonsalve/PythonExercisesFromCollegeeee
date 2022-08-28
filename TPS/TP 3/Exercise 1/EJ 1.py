












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
    filas = len(matriz[0])
    columnas = filas
    aux = 0
    i = 1
    while (i < filas):
        if matriz[i-1][0] > matriz[i][0]:
            aux = matriz[i]
            matriz[i] = matriz[i-1]
            matriz[i-1] = aux
        i += 1
    print("----matriz en orden ascendente por filas.----")
    leerMatriz(matriz, filas, columnas)

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