from random import randint

def crear(filas, columnas):
    matriz = [[0]*columnas for i in range(filas)]
    return matriz

def cargar(matriz, filas, columnas):
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = randint(0, 150)

#imprime la matriz de una forma mas grafica.    
def imprimir(matriz, filas, columnas):
    for i in range(filas):
        print("[fabrica", i+1,"]", end=" ")
        for j in range(columnas):
            print(matriz[i][j], end=" ")
        print(" ")

def seleccionDia(maxDia):
    if (maxDia == 0):
        print("lunes")
    elif(maxDia == 1):
        print("martes")
    elif(maxDia == 2):
        print("miercoles")
    elif(maxDia == 3):
        print("jueves")
    elif(maxDia == 4):
        print("viernes")
    elif(maxDia == 5):
        print("sabado")

def imprimirTranspuesta(t, filasT, columnasT):
    for i in range(filasT):
        for j in range(columnasT):
            print(t[i][j], end=" ")
        print(" ")

#Mostrar la cantidad de bicicletas fabricadas por cada fabrica
def totalPorFabrica(matriz, filas, columnas):
    for i in range(filas):
        total = 0
        for j in range(columnas):
            total = total + matriz[i][j]
        print("Fabrica", i+1, " = ", total)

#Cual es la fabrica que mas produjo en un solo dia (detallar dia y fabrica)
def maxProd(matriz, filas, columnas):
    max = 0
    maxFab = -1
    maxDia = -1
    for i in range(filas):
        for j in range(columnas):
            if (matriz[i][j] > max):
                max = matriz[i][j]
                maxFab = i+1
                maxDia = j
    print("-----FABRICA con Maxima Producción-----")
    print("FABRICA ", maxFab)
    print("cantidad: ", max)
    
    seleccionDia(maxDia)


#Cual es el dia mas productivo, considerando todas las fabricas combinadas.
def diaMasProd(matriz, filas, columnas):
    t = []
    #voy a transponer la matriz, en una nueva matriz. De esta manera puedo recorrerla de una manera mas comoda y legible para otro programador.
    for i in range(columnas):
        t.append([])
        for j in range(filas):
            t[i].append(matriz[j][i])
        filasT = len(t)
        columnasT = len(t[0])
    #print("----Matriz Transpuesta----")
    #imprimirTranspuesta(t, filasT, columnasT)

    #ahora las columnas son los dias y las filas las fabricas.
    #ahora recorro cada columna, a ver cual dia fue el mas productivo.
    print("----DIA mas productivo----")

    max = -1
    diaMax = -1
    for i in range(filasT):
        total = 0
        for j in range(columnasT):
            total = total + t[i][j]
        print("Total dia", i, " = ", total)
        if total > max:
            max = total
            diaMax = i
        
    print("Dia mas productivo: ", end=" ")
    seleccionDia(diaMax)
    print("cantidad producida: ", max)

def menorPorFabrica(matriz, filas, columnas):
    max = 151
    lista = [min(matriz[i][j] for j in range(columnas)) for i in range(filas)]
    print("----Menor cantidad por FABRICA----")
    print(lista)

    for i in range(len(lista)):
        print("FABRICA", i+1, "=", lista[i])


filas = int(input("filas: "))
columnas = int(input("columnas: "))

matriz = crear(filas, columnas)
cargar(matriz, filas, columnas)
imprimir(matriz, filas, columnas)

totalPorFabrica(matriz, filas, columnas)
maxProd(matriz, filas, columnas)
diaMasProd(matriz, filas, columnas)
imprimir(matriz, filas, columnas)
menorPorFabrica(matriz, filas, columnas)