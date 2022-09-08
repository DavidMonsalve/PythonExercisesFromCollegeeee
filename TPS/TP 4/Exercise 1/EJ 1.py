def invertir_cadena(cadena):
    cadenaInvertida = ""
    for letra in cadena:
        cadenaInvertida = letra + cadenaInvertida
    return cadenaInvertida

def esCapicua(cadena):
    cadena_2 = invertir_cadena(cadena)
    if cadena == cadena_2:
        print("es capicua")
    else:
        print("no es capicua")

cadena = input("Cadena de caracteres: ")
esCapicua(cadena)