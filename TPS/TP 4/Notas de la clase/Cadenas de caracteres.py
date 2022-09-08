#Las cadenas de caracteres son Case Sensitive.

#OPERADORES ------------------------------------------------------------------------------------------------------
#Concatenar (+)

nombre = input("Ingrese nombre: ")
saludo = ("Hola, " + nombre)
print(saludo)


#Replicar (*)
astericos = "*" * 10
print(astericos)


#Buscar (in)
cad = ("Hoy es dia de programacion")
if "pro" in cad:
    print("SI está")
else:
    print("NO está")


#Comparar (==)
pais = input("Ingrese pais: ")
if pais == "Argentina":
    print("argentino")
else:
    print("extranjero")
#-----------------------------------------------------------------------------------------------------------------









#FORMAS DE IMPRIMIR UNA CADENA------------------------------------------------------------------------------------------------------------------------------------

#iterar una cadena --> a traves de un ciclo se puede tomar caracter a caracter.
cad = "Hoy es martes"
for letra in cad:
    print(letra, end=" ")
print("")


#SUBINDICES
cad = "Me gusta la clase de programación"
print(cad[4])
print(cad[-1])

    #lo que NO se puede hacer es:
    #cad[4] = "z" DA ERROR.
    #No se puede modificar la cadena usando subindices, es inmutable.
    
#REBANADAS
cad = "Me gusta la clase de programación"
print(cad[9:18])

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------














#FUNCIONES()------------------------------------------------------------------------------------------------------

cad = "Me gusta la clase de programación"

#str() Transforma un numero en una cadena.
edad = 25
print("La edad es " + str(edad))


#len() longitud de la cadena
print(len(cad))

#max() devuelve valor con mayor valor ASCII
print(max(cad))

#min() devuelve valor con menor valor ASCII
print(min(cad))

#count() Devuelve la cantidad de veces que se repite el parametro.
print(cad.count("a"))

#index() Devuelve posicion de subcadena en la cadena principal
print(cad.index("progra"))

#replace Reemplaza un texto por otro.
print(cad.replace("gusta", "divierte"))

#isalpha() Retorna True o False. Si la cadena es completamente alfabetica retorna True, de lo contrario False.
print(cad.isalpha())

#isdigit() Hace lo mismo que la anterior pero con numeros.
cad2 = "123456"
print(cad2.isdigit())

#isalnum() Determina si la cadena esta compuesta exclusivamente por caracteres alfabeticos y numericos. no acepta nada mas, por ejemplo
#espacios, @, #, -, +, etc. (no acepta caracteres especiales)
cad3 = "Python3"
print(cad3.isalnum())


#isupper() Determina si esta en mayus
cadupper = "ABCD"
print(cadupper.isupper())

#islower Determina si esta en minus
cadminus = "abcd"
print(cadminus.islower())


#----------------------------------------------------------------------------------------------------------------------------------------------------------









#METODOS-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#.upper() Pone todo en mayus
cad = "programacion"
print(cad.upper())


#.lower() Pone todo en minus
print(cad.lower())

#.capitalize() Pone la primera letra del string en Mayus
cap = "bienvenido a la clase"
print(cap.capitalize())

#.title() Pone mayus la 1era letra de cada palabra
print(cap.title())

#.split() Crea una lista con cada palabra de la cadena.
print(cap.split())

#"".join(cadena) Lo que se escriba entre las comillas sera puesto entre cada caracter de la cadena
cap =" ".join(cap)
print(cap)


#.center(<ancho>, <relleno>) Completa la cadena con el caracter que indiquemos hasta llegar al numero indicado.
#Si ponemos Hola y pasamos como parametro 10 y *
#Imprimira = ***Hola***
cadena = "hola"
print(cadena.center(10, "-"))

#variaciones del .center() = 

    #.ljust(<ancho>, <relleno>)
print(cadena.ljust(10, "-"))

    #rjust(<ancho>, <relleno>)
print(cadena.rjust(10, "-"))








#.zfill() rellena con tantos 0's como indiquemos
cad = "123"
print(cad.zfill(10)) #0000000123


#.lstrip("dato") elimina el caracter indicado, a la izquierda
cad = "----hola mundo----"
print(cad.lstrip("-")) #hola mundo----

#.rstrip("dato") elimina el caracter indicado, a la derecha
cad = "----hola mundo----"
print(cad.lstrip("-")) #----hola mundo

#.strip("dato") elimina el caracter indicado, a ambos lados
cad = "----hola mundo----"
print(cad.strip("-")) #hola mundo

#format Pone un espacio.
a = 25
print("%4d" %a)

#format

legajo = 123456
nombre = "maria"
nota = 8
print("Legajo {} Nombre {} Nota {}" .format(legajo, nombre, nota))
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Realizar los siguientes ejercicios de la practica:

#1 - 2 - 3 - 6 - 7 - 9 - 12 - 14.