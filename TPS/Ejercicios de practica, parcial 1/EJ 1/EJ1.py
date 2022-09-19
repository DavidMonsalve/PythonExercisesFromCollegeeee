






from random import randint

def leerMatriz(m, f, c):
    for i in range(f):
        for j in range(c):
            print(str(m[i][j]).center(15, " "), end=" ")
        print(" ")

def codigoRepuesto(m, f, c, lista):
    #primer valor fila 0
    m[0][0] = randint(1, 100)
    m[0][1] = randint(500, 1000)
    m[0][2] = randint(1, 25)

    valor = m[0][2]
    valor = lista[valor]

    valor = valor + str(m[0][0]) + str(m[0][1])
    return valor

def cargarLista(m, f, c,):
    for i in range(f):
        j = 3
        while (j < len(m[0])):    
            CR = codigoRepuesto(m, filas, columnas, lista)
            m[0][j] = CR

            m[1][j] = randint(1, 200)

            m[2][j] = randint(10, 30)

            if m[1][j] < m[2][j]:
                m[3][j] = "reponer"
            else:
                m[3][j] = "buenStock"
            j+=1

    leerMatriz(m, f, c)


def reposicion(m, f, c, lista):
    for i in range(f):
        for j in range(c):
            if m[i][j] == "reponer":
                lista.append(m[0][j])

    aReponer = len(lista)-1
    x = "Reponer: " + str(aReponer)
    lista.append(x)

    buenStock = (len(m[0]) - 3 )
    
    porcentaje = (aReponer / buenStock) * 100
    y = "Porcentaje a reponer: " + str(porcentaje) + "%" 
    lista.append(y)

    for i in range(len(lista)):
            print(str(lista[i]).center(30, "-").title())


listaReposicion = ["la vieja heladera ----- lvh"]
filas = 4
columnas = 100  
"""                                                                                           !!!!!!!!!! If someone is ever gonna test this program CHANGE THIS VALUE (columnas) to a lower number,
                                                                                                          if you run it as it is, the output in the console is gonna be a desaster.
                                                                                                          I used "100" because it is a requirement in my homework.

"""
lista = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
    "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
    "w", "x", "y", "z"
]

m = [[0]*columnas for i in range(filas)]
cargarLista(m, filas, columnas)

reposicion(m, filas, columnas, listaReposicion)