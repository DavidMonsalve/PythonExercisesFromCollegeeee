def ingreso():

    try:
        n = int(input("Numero: "))
        if (n > 0):
            print("Correcto. Retorno: ", n)
            return n
        else:
            print("El numero debe ser mayor a 0.")
            ingreso()
    except ValueError:
        print("ingrese un numero entero.")
        ingreso()
 
numero = ingreso()