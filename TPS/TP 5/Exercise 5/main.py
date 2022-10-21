import math


def raiz():
    try:
        numero = int(input("numero a sacar raiz cuadrada: "))
        print(math.sqrt(numero))
    except ValueError:
        print("ERROR: solo numeros naturales.")
        raiz()


raiz()

f = input("Presiona Enter para finalizar.")