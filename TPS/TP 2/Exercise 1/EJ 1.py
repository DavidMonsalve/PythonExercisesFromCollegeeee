from random import randint
from tkinter.messagebox import RETRY

cantElementos = randint(10, 15)
digitos = randint(10, 15)
lista = []

#Funcion para cargar la lista
def cargar_lista(cantElementos, digitos):
    for i in range(cantElementos):
        lista.append(digitos)
        digitos = randint(10, 15)
    return lista

#Funcion para calcular la suma de todos los elementos en la lista
def sumarLista(lista):
    suma = sum(lista)
    return suma

#Eliminar todas las apariciones de un elemento de una lista anterior. 
def eliminar_apariciones(lista, elemento):
    listaSinElemento = list(filter(lambda x:x != elemento, lista))
    return listaSinElemento

#Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas auxiliares.
def esCapicua(lista, n):
    i = 0
    flag = 0
    print(lista)
    #mientras que 
    # *i no sea la mitad del array(n//2)(n siendo la longitud)
    # y la lista no este vacia (n!= 0),
    #  que se ejecute el siguiente codigo:
    while (i <= n//2) and (n != 0):
        if (lista[i] != lista[n - i - 1]):
            flag = 1
            break
        i += 1
    #si el flag esta encendido entonces no es capicua, por el contrario, lo es.
    if (flag == 1):
        print('No es capicua')
    else:
        print('Es capicua')



listaGlobal = cargar_lista(cantElementos, digitos)
print(listaGlobal)

sumaTotal = sumarLista(listaGlobal)
print(sumaTotal)

elemento = int(input("Ingrese elemento a borrar en la lista: "))
listaElementoEliminado = eliminar_apariciones(lista, elemento)
print(listaElementoEliminado)

listaCapicua = [1, 3, 5, 3, 1] #Solo la creo con propositos comprobativos. En el codigo final el programa utilizara la lista creada aleatorialemente.
n = len(listaGlobal)
esCapicua(listaGlobal, n)