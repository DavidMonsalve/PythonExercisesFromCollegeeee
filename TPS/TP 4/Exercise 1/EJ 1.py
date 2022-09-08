def esCapicua(cadena):
    anterior = 0
    ultimo = len(cadena) - 1

    while (anterior <= ultimo):
        if cadena[anterior] != cadena[ultimo]:
            return False
        anterior += 1
        ultimo -= 1
    return True

cadena = input("Cadena de caracteres: ")
if esCapicua(cadena) == True:
    print("Es capicúa")
else:
    print("No es capicua")