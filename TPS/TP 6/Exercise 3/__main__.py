def añadirJugador():
    print("nombre: ")
    nombre = input("Respuesta: ---> ")
    if (nombre.isalpha):
        try:
            altura = float(input("altura: "))
            altura = str(altura)
            return nombre, altura
        except ValueError:
            print("dato invalido. ")
            print("reiniciar carga de datos de jugador. ")
            añadirJugador()
    else:
        while (nombre.isalpha == False):
            print("nombre invalido intente de nuevo. ")
            añadirJugador()
            
def addDeporte():
    print("Desea añadir un deporte? ")
    print("1 - Si.")
    print("2 - No.")

    respuesta = int(input("Respuesta: ---> "))
    try: 
        if (respuesta == 1):
            print("Nombre del deporte: ")
            deporte = input("Respuesta: ---> ")
            if (deporte.isalpha()):
                return deporte
            else:
                print("valor invalido")
                addDeporte()
        elif (respuesta == 2):
            print("Bien...")
            menu_1()

        else:
            print("valor invalido")
            addDeporte()

    except ValueError:
        print("valor invalido")
        addDeporte()


def popUpJugador():
    try:
        print("¿desea añadir un nuevo jugador?")
        print("1 - Si.")
        print("2 - No.")
        respuesta = int(input("Respuesta ---> "))
        
        if (respuesta == 1):
            nombre, altura = añadirJugador() 
            return nombre, altura     
        elif (respuesta == 2):
            menu_1()

        else:
            print("Error: valor invalido")
            popUpJugador()

    except ValueError:
        ("Error: valor invalido")
        popUpJugador() 


def escribirDocumento(deporte, nombre, altura):
    with open("jugadores.txt", "a") as f:
        f.write("deporte: " + str(deporte) + "\n")
        f.write("---" + "\n")
        f.write("nombre: " + nombre + "\n")
        f.write("altura: " + altura + "\n" )
        f.write("---")

    with open("jugadores.txt", "r") as f:
        print(f.read())

def selector(respuesta):
    if respuesta == "1":
        deporte = addDeporte()
        nombre, altura = popUpJugador()
        escribirDocumento(deporte, nombre, altura)
        popUpJugador()
    elif (respuesta == "2"):
        try:
            with open("jugadores.txt", "r") as f:
                print(f.read())
            menu_1()
        except FileNotFoundError:
            print("Error: documento no encontrado. Quiza aun no esta creado.")
            menu_1()
    elif (respuesta == "3"):
        quit()

def menu_1():
    print("¿Qué desea hacer?")
    print("1 - Añadir nuevo deporte")
    print("2 - Ver deportes con jugadores")
    print("3 - Salir")
    respuesta = input("Respuesta ---> ")

    selector(respuesta)


menu_1()