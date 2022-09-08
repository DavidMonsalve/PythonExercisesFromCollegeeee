import copy
from random import randint


def cargar_sala(filas, columnas):
    matriz = [[randint(0, 1) for i in range(columnas)] for j in range(filas)]
    return matriz


def imprimir(matriz, filas, columnas):
    for i in range(filas):
        for j in range(columnas):
            print(matriz[i][j], end=" ")
        print(" ")

def mostrar_butacas(matriz, filas, columnas):
    print("D = Disponible")
    print("T = Tomado")
    for i in range(filas):
        for j in range(columnas):
            if (matriz[i][j] == 0) or (matriz[i][j] == "D"):
                matriz[i][j] = "D"
            elif (matriz[i][j] == 1) or (matriz[i][j] == "T"):
                matriz[i][j] = "T"
    imprimir(matriz, filas, columnas)


def seleccionButaca(matriz, filas, columnas):
    fila = int(input("fila en la que se desea sentar: "))
    while(fila > filas) or (fila < 0):
        print("fila invalida, por favor, intente de nuevo...")
        fila = int(input("fila en la que se desea sentar: "))

    butaca = int(input("butaca en la que se desea sentar: "))
    while(butaca > columnas) or (butaca < 0):
        print("butaca invalida, por favor, intente de nuevo...")
        fila = int(input("butaca en la que se desea sentar: "))

    return fila, butaca

def verificarSalaNoEsteCompleta(matriz, filas, columnas):
    comprobante = "D"
    booleano = False
    for i in range(filas):
        for j in range(columnas):
            if (matriz[i][j] == comprobante):
                booleano = True
            else:
                booleano = False
    return booleano

def reservar(matriz, filas, columnas, Bfila, BCol):
    if (verificarSalaNoEsteCompleta (matriz, filas, columnas)):
        while (matriz[Bfila][BCol] != "D"):
            print("El asiento ya esta reservado. Intente nuevamente...")
            Bfila, BCol = seleccionButaca(matriz, filas, columnas)
        if (matriz[Bfila][BCol] == "D"):
            matriz[Bfila][BCol] = "T"
            print("Reservado exitosamente!")

            print("---------ESTADO DE LA SALA---------")
            mostrar_butacas(matriz, filas, columnas)
    else:
        print("Lo sentimos. La sala está completa.")

def butacas_libres(matriz, filas, columnas):
    contador = 0
    for i in range(filas):
        for j in range(columnas):
            if (matriz[i][j] == "D"):
                contador += 1
    print("Butacas libres: ", contador)

def butacas_contiguas(matriz, filas, columnas):
    max = 0
    inicio_definitivo = []
    for i in range(filas):
        contador = 0
        inicio = []
        for j in range(columnas-1):
            if (matriz[i][j] == matriz[i][j+1]) and (matriz[i][j] == "D"):
                contador += 1
                inicio = [i, j]
        if contador > max:
            max = contador
            inicio_definitivo = copy.deepcopy(inicio)
    print("Mayor secuencia de butacas continuas: ", max+1)
    print("inicio en: ", inicio_definitivo[0], inicio_definitivo[1]-1)
            
            

filas = int(input("filas: "))
columnas = int(input("columnas: "))

matriz = cargar_sala(filas, columnas)
#imprimir(matriz, filas, columnas)
print("---------ESTADO DE LA SALA---------")
mostrar_butacas(matriz, filas, columnas)

filaSeleccionada, butacaSeleccionada = seleccionButaca(matriz, filas, columnas)
reservar(matriz, filas, columnas, filaSeleccionada, butacaSeleccionada)

butacas_libres(matriz, filas, columnas)

butacas_contiguas(matriz, filas, columnas)