def ingresar():
    try:
        dia = int(input("dia: "))
        while (dia > 31) or (dia < 1):
            dia = int(input("dia: "))

        mes = int(input("mes: "))
        while (mes > 12) or (mes < 1):
            mes  = int(input("mes: "))

        año = int(input("año: "))
        while (año < 0):
            año = int(input("año: "))

        fecha = (dia, mes, año,)

        return fecha
    except ValueError:
        print("valor invalido")
        ingresar()

def calculo(f, cant):
    contador = 0
    for i in range(cant):
        if (f[0] == 31):
            if (f[1] == 12):
                f[2] += 1
                f[1] = 1
                f[0] = 1
            else:
                f[1] += 1
                f[0] = 1
        f[0] += 1
    return f



def sumarDias(fecha):
    
    message_2 = "DIAS A SUMARLE A LA FECHA ANTERIOR.".center(50, "-")
    print(message_2)

    try:
        cant = int(input("Cantidad de dias: "))
        fecha_final = calculo(fecha, cant)
        return fecha_final
    except ValueError:
        print("valor invalido.")
        sumarDias()