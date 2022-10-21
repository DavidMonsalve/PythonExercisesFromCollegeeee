from xml.etree.ElementTree import tostring


def cargar_lista(original):

    lista = list(original)
    try:
        x = int(input("valor: "))
        while (x != -1):
            lista.append(x)
            print(lista)
            x = int(input("valor: "))
        return lista

    except ValueError:
        print("ERROR: ingresa un numero entero.")
        cargar_lista(original)

def buscar(original, counter):
    try:
        while counter != 3:
            dato = int(input("dato a buscar: "))
            lugar = original.index(dato)
            print("posicion: ", lugar)
    except ValueError:
        print("el dato ingresado no se encuentra en la lista.")
        if counter != 3:
            counter += 1
            print(counter, "error/es.")
            print("El numero no esta en la lista.")
            buscar(original, counter)
        else:
            quit()


counter = 0
original = []
original = cargar_lista(original)
print(original)
buscar(original, counter)