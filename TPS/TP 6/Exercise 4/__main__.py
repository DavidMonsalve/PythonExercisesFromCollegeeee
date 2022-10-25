try:
    with open("C:\\Users\\david\\Desktop\\uade 2 cuatri\\Materias\\Algoritmia 2\\Resolucion TPs\\TPS\\TP 6\\Exercise 4\\usuarios.txt", "r") as f:
        for line in f:
            apellido, nombre = line.split(",")
            if nombre.startswith(" "):
                nombre = nombre[1:]
            
            user = apellido + ", " + nombre

            if apellido[-3:] == "ian":
                print(user)
                with open("C:\\Users\\david\\Desktop\\uade 2 cuatri\\Materias\\Algoritmia 2\\Resolucion TPs\\TPS\\TP 6\\Exercise 4\\ARMENIA.TXT", "a") as armenia:
                    armenia.write(user+"\n")
            
            elif apellido[-3:] == "ini":
                print(user)
                with open("C:\\Users\\david\\Desktop\\uade 2 cuatri\\Materias\\Algoritmia 2\\Resolucion TPs\\TPS\\TP 6\\Exercise 4\\ITALIA.txt", "a") as italia:
                    italia.write(user+"\n")
            
            elif apellido[-2:] == "ez":
                print(user)
                with open("C:\\Users\\david\\Desktop\\uade 2 cuatri\\Materias\\Algoritmia 2\\Resolucion TPs\\TPS\\TP 6\\Exercise 4\\ESPAÑA.txt", "a") as italia:
                    italia.write(user+"\n")

            else:
                print(user, "(descartar)")

except IOError:
    print("No se pudo abrir el archivo.")