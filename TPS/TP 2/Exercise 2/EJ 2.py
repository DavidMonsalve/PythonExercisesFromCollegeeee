from random import randint

#Recibir una lista como parametro y devolver True si la misma contiene algun elemento repetido. La funcion no debe modificar la lista.
def hayRepetidos(lista):
    cuenta = [lista.count(numeros) for numeros in set(lista)]    
    total = 1
    
    #se supone que si ningun elemento se repitio, el set creado previamente debe tener todos sus valores
    #equivalentes a 1, si los multiplicamos entre si por 1, el resultado debe ser 1. De lo contrario es porque algun valor se repitio
    #y nuestra funcion retornara False.
    
    for i in range(len(cuenta)):
        total = cuenta[i]*total

    if total > 1:
        return True
    else:
        return False
    

#Recibir una lista como parametro y devolver una nueva lista con los elementos unicos de la lista original, sin importar el orden.
def elementos_unicos(lista):

    #Cuento cuantas veces se repitio un numero, lo guardo en OcurrenciasDeElementos, creo otra lista llamada Output.
    #Si el indice de OcurrenciasDeElementos es igual a 1, significa que dicho elemento solo esta una vez en nuestra lista.
    #Aprovechando que todas las listas tienen el mismo Length, utilizo el indice de la lista original pasada como parametro
    #para añadir en Output los valores unicos.
    output = []
    OcurrenciasDeElementos = [lista.count(numeros) for numeros in lista]
    print("----------------------------")
    print("Lista original: ", lista)
    for i in range (len(OcurrenciasDeElementos)):
        if OcurrenciasDeElementos[i] == 1:
            output.append(lista[i])
    return output


#Generar una lista de 50 numeros aleatorios del 1 al 100.
lista = []

for i in range(50):
    lista.append(randint(1, 100))
print("-----Lista original-------")
print(lista)

print("-------hay repetidos?---------")
print(hayRepetidos(lista))


listaNueva = [1, 2, 1, 5, 3]
listaSinRepetidos = elementos_unicos(listaNueva)
print("Lista sin repetidos: ", listaSinRepetidos)