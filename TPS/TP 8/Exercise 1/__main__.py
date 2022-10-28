import __fecha__
import __hora__

def main():

    message_1 = "FECHA".center(50, "-")
    print(message_1)

    fecha = __fecha__.ingresar()
    ListaFecha = list(fecha)

    fechaResultante = __fecha__.sumarDias(ListaFecha)
    tuplaResultante = tuple(fechaResultante)
    print(tuplaResultante)


    print("Breve explicacion".center(50, "-"))
    print("Se usa horario militar. Es decir la hora va de 00:00, hasta 23:59.")
    print("PRIMERA HORA".center(50, "-"))
    hora_1 = __hora__.ingreso()
    print(hora_1)

    print("SEGUNDA HORA".center(50, "-"))
    hora_2 = __hora__.ingreso()
    print(hora_2)

    print("DIFERENCIA TEMPORAL ENTRE AMBAS HORAS".center(50, "-"))
    diferencia = __hora__.calculo(hora_1, hora_2)
    diferencia = list(diferencia)
    print("la diferencia entre ambas horas es de: ", diferencia[0], ":", diferencia[1], "horas.")

main()