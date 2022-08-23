def verificar(d, m, y):
    Booleana = False
    if (d > 0) and (d <= 31):
        if (m > 1) and (m <= 12):
            if (y >= 0) and (y < 2023):
                Booleana = True
    return Booleana


dddd = int(input("Dia: "))
mmmm = int(input("Mes: "))
yyyy = int(input("año: "))

x = verificar(dddd, mmmm, yyyy)

print(x)