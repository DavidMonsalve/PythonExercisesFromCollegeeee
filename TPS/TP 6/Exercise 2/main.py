def carga():
    try:
        dia = int(input("dia: "))
        while dia > 31 or (dia < 1):
            print("El dia no es válido.")
            dia = int(input("dia: "))
            
        mes = int(input("mes: "))
        while (mes < 1) or (mes > 12):
            print("Mes inválido.")
            mes = int(input("mes: "))

        mm = int(input("mm caidos: "))
        while (mm < 0):
            print("cantidad de lluvia inválida.")
            mm = int(input("mm caidos: "))

        sdia = str(dia)
        smes = str(mes)
        smm = str(mm)

    except ValueError:
        print("Ingresa solo numeros naturales.")
        print("Reiniciando carga de valores...")
        carga()


    finally:
        print("carga finalizada.")
        return sdia, smes, smm

xdia, xmes, xmm = carga()
update = xdia + ";" + xmes + ";" + xmm

f = open("datos.txt", "a")
f.write(update + "\n")
f.close()

exit = input("Presione cualquier tecla para finalizar.")