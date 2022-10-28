direccion = input("correo: ")
correo = direccion.split("@")

nombre = correo[0]
info = correo[1]

detailed_info = tuple(info.split("."))

tupla = (nombre,)
for i in range(len(detailed_info)):
    pedazo = detailed_info[i]
    tupla = tupla + (pedazo,)
print(tupla)