def leerCodigoDeSocio():

    socio = int(input("Codigo de socio (0 para finalizar): "))
    if socio != 0:
        while (socio < 10000) or (socio > 99999):
            print("solo codigos de cinco digitos son permitidos")
            socio = int(input("Codigo de socio (0 para finalizar): "))
    return socio

def cargarSocio(socio, lista):
    lista.append(socio)
    return lista

def informarApariciones(lista):
    lista2 = lista
    revisados = []
    for i in range(len(lista2)):
        contador = 0
        x = lista2[i]
        if not(x in revisados):
            for j in range(len(lista2)):
                if lista2[j] == x:
                    contador += 1
                    revisados.append(x)
            print(x, "- estuvo en el club ", contador, end="")
            if contador > 1:
                print(" veces")
            else:
                print(" vez")

def ingresarSocioAeliminar(lista):
    SocioAeliminar = int(input("Socio a eliminar: "))
    while not(SocioAeliminar in lista):
        print("El socio no se encuentra en la lista. Quiza haya escrito el codigo incorrecto.")
        SocioAeliminar = int(input("Socio a eliminar: "))
    print("Socio a eliminar ingresado correctamente: ", "[", SocioAeliminar ,"]")
    return SocioAeliminar

def eliminarExSocio(lista, socio):

    #mostrar sus apariciones antes de eliminarlo de la lista.
    listaTemporal = lista
    print("---Apariciones de dicho socio en el club---")
    for i in range (len(listaTemporal)):
        if listaTemporal[i] == socio:
            print(socio)
    print("--------------------------------------------------")

    print("ingresos antes de eliminar al socio: ", lista)
    #eliminarlo de la lista original
    ingresos = 0
    while lista.count(socio) > 0:
        ingresos += 1
        lista.remove(socio)
    print("se eliminaron ", ingresos, "ingresos.")
    print("ingresos luego de eliminar al socio: ", lista)

    listaTemporal = []


ListaSocios = []
socio = leerCodigoDeSocio()

while (socio != 0):
    x = cargarSocio(socio, ListaSocios)
    ListaSocios = x
    socio = leerCodigoDeSocio()

print(ListaSocios)

informarApariciones(ListaSocios)

exSocio = ingresarSocioAeliminar(ListaSocios)
eliminarExSocio(ListaSocios, exSocio)