from random import randint as azar


def escribir(m):
    if m == 1:
        MES = "Enero"
    elif m == 2:
        MES = "Febrero"
    elif m == 3:
        MES = "Marzo"
    elif m == 4:
        MES = "Abril"
    elif m == 5:
        MES = "Mayo"
    elif m == 6:
        MES = "Junio"
    elif m == 7:
        MES = "Julio"
    elif m == 8:
        MES = "Agosto"
    elif m == 9:
        MES = "Septiembre"
    elif m == 10:
        MES = "Octubre"
    elif m == 11:
        MES = "Noviembre"
    elif m == 12:
        MES = "Diciembre"

    return MES

dia = (azar(1, 31))
mes = (azar(1, 12))
año = (azar(0, 2022))

fecha = (dia, mes, año,)

print(fecha)

MES_escrito = escribir(mes)

mensaje = str(dia) + " de " + MES_escrito + " del " + str(año)

print(mensaje)