def diasiguiente(d, m, y, add):
    for i in range(add):
        if (d < 31):
            d += 1
        elif (d == 31):
            d = 1
            if (m < 12):
                m += 1
            elif (m == 12):
                m = 1
                y += 1
    print(d, "/", end=" ")
    print(m, "/", end=" ")
    print(y, "/", end=" ")
    print(" ")


dddd = int(input("Dia: "))
mmmm = int(input("Mes: "))
yyyy = int(input("año: "))

sumar_dias = int(input("cantidad de dias: "))

diasiguiente(dddd, mmmm, yyyy, sumar_dias)