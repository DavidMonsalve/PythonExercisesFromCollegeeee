claveMaestra = input("clave maestra: ")

clave_1 = " "
clave_2 = " "
for i in range(len(claveMaestra)):
    if i % 2 == 0:
        clave_1 = clave_1 + claveMaestra[i]
    else:
        clave_2 = clave_2 + claveMaestra[i]

print("Clave caja 1: ", clave_1)
print("Clave caja 2: ", clave_2)