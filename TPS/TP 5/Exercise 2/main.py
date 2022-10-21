def dataEntry():
    try:
        a = float(input("ingrese numero real 1: "))
        b = float(input("ingrese numero real 2: "))
        c = a + b

        print("RESULTADO: ", c)
    except ValueError:
        print("Ambos valores deben ser numeros reales. (CODIGO: -1)")
        dataEntry()


dataEntry()