













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














#MÉTODOS()------------------------------------------------------------------------------------------------------

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