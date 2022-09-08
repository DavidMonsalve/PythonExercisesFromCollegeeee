def rebanadas(cadena, pos, cant, largo):
    if (largo >= cant) and (largo >= pos):
        print(cadena[pos:(pos+cant)])
    else:
        print("con los datos ingresados no se puede trabajar.")


def sinRebanadas(cadena, pos, cant, largo):
    texto = ""
    for i in range(cant):
        texto = texto + cadena[pos]
        pos += 1
    print(texto)


cadena = input("Cadena de texto: ")
pos = int(input("posicion a buscar: "))
cant = int(input("cant de caracteres: "))
largo = len(cadena)

rebanadas(cadena, pos, cant, largo)
sinRebanadas(cadena, pos, cant, largo)