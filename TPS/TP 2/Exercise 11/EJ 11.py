def registrarUrgencias(urgencias, afiliado):
    urgencias.append(afiliado)
    return urgencias
def registrarTurnos(turnos, afiliado):
    turnos.append(afiliado)
    return turnos
def buscarAfiliadoUrgencias(lista, afiliado):
    x = lista.count(afiliado)
    return x
def buscarAfiliadoTurnos(lista, afiliado):
    y = lista.count(afiliado)
    return y

urgencias = []
turnos = []



#ingresamos el codigo la primera vez
afiliado = int(input("Codigo de afiliado (-1 para finalizar): "))
if afiliado != -1:
    while (afiliado < 1000) or (afiliado > 9999):
        print("codigo erroneo.")
        print("solo codigos de cuatro digitos son permitidos")
        afiliado = int(input("Codigo de afiliado (-1 para finalizar): "))

#inicializamos un ciclo while para seguir haciendolo cuantas veces sea necesario.

while (afiliado != -1):

    #registro el tipo de visita
    tipoVisita = int(input("0 si viene por emergencia, 1 si viene con turno: "))
    while (tipoVisita > 1) or (tipoVisita < 0):
        print("Ingresar unicamente 1 ó 0.")
        tipoVisita = int(input("0 si viene por emergencia, 1 si viene con turno: "))

    if (tipoVisita == 0):
        xUrgencias = registrarUrgencias(urgencias ,afiliado)
        urgencias = xUrgencias
    else:
        xTurnos = registrarTurnos(turnos, afiliado)
        turnos = xTurnos
    #registramos otro usuario o paramos el ciclo

    
    afiliado = int(input("Codigo de afiliado (-1 para finalizar): "))
    if afiliado != -1:
        while (afiliado < 1000) or (afiliado > 9999):
            print("codigo erroneo.")
            print("solo codigos de cuatro digitos son permitidos")
            afiliado = int(input("Codigo de afiliado (-1 para finalizar): "))
    
print("Urgencias: ", urgencias)
print("Turnos: ", turnos)


afiliado = int(input("Codigo de afiliado a buscar en las listas (-1 para finalizar): "))
if afiliado != -1:
    while (afiliado < 1000) or (afiliado > 9999):
        print("codigo erroneo.")
        print("solo codigos de cuatro digitos son permitidos")
        afiliado = int(input("Codigo de afiliado (-1 para finalizar): "))

while (afiliado != -1):
    print("Cantidad de veces que el afiliado ", afiliado, " entro por urgencias: ", buscarAfiliadoUrgencias(urgencias, afiliado))
    print("Cantidad de veces que el afiliado ", afiliado, " entro con turno: ", buscarAfiliadoTurnos(turnos, afiliado))

    afiliado = int(input("Codigo de afiliado a buscar en las listas (-1 para finalizar): "))
    if afiliado != -1:
        while (afiliado < 1000) or (afiliado > 9999):
            print("codigo erroneo.")
            print("solo codigos de cuatro digitos son permitidos")
            afiliado = int(input("Codigo de afiliado (-1 para finalizar): "))