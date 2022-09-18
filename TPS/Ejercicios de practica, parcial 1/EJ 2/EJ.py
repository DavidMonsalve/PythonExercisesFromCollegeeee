from random import randint

def leerMatriz(m, filas, columnas):
    for i in range(filas):
        for j in range(columnas):
            if i == 0:
                print(str(m[i][j]).zfill(8), end=" ")
            else:
                print(str(m[i][j]).rjust(8, " "), end=" ")
        print(" ")


def crearMatriz(filas, columnas):
    m = [[0]*columnas for i in range(filas)]
    return m

def cargarMatriz(matriz, filas, columnas):

    #cargar legajo
    for i in range(columnas):
        matriz[0][i] = randint(1000000, 10000000)

    #primera nota
    for i in range(columnas):
        matriz[1][i] = randint(1, 10)
    
    #segunda nota
    for i in range(columnas):
        matriz[2][i] = randint(1, 10)

    #promedio
    for i in range(columnas):
        matriz[3][i] = (matriz[1][i] + matriz[2][i]) // 2
    print("MATRIZ CON TODOS LOS ALUMNOS")
    leerMatriz(matriz, filas, columnas)

def sePromociona(m, f, c):
    for i in range(c):
        nota = str(m[3][i])
        lu =  str(m[0][i])
        print(nota.zfill(4), end=" ")
        print(lu.zfill(16))

def examenFinal(m, f, c):
    for i in range (c):
        if m[3][i] >= 7:
            nota = str(m[3][i])
            lu =  str(m[0][i])
            print(nota.zfill(4), end=" ")
            print(lu.zfill(16))

def aplazados(m, filas, columnas):
    a = []                                         #cargando la lista con los aplazados
    for i in range(columnas):
        if (m[1][i] < 5) and (m[2][i] < 5):
            a.append(m[0][i])               


#                                                  ordenandolos de mayor a menor por LU
    a.sort()    
    a.reverse()
    print(a)
            

materia = input("Materia: ")                                                               #cargando nombre de materia
codCurso = int(input("Codigo del curso: "))                                                #cargando codigo de curso
while (codCurso < 10000) or (codCurso > 99999):
    print("Invalido")
    codCurso = int(input("Codigo del curso: "))

regimen = int(input("¿Como se aprueba la materia? 1- Promoción. 2- Examen Final. "))        #seleccionando regimen de aprobacion
while (regimen != 1) or (regimen != 2):
    if (regimen == 1) or (regimen == 2):
        break
    print("invalido.")
    regimen = int(input("¿Como se aprueba la materia? 1- Promoción. 2- Examen Final. "))

filas = 4                                                                               #dimensiones de la matriz
columnas = int(input("cant alumnos: "))

print(" ") 
print(" ")
print("Universidad Argentina de la Empresa ----- UADE.")                                
print(materia)
print("Codigo de materia: ", codCurso)
matriz = crearMatriz(filas, columnas)
cargarMatriz(matriz, filas, columnas)

if regimen == 1:                            #(se promociona)
    sePromociona(matriz, filas, columnas)
else:
    examenFinal(matriz, filas, columnas)

aplazados(matriz, filas, columnas)