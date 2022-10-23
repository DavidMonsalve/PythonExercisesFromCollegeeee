















from random import randint as azar
def carga():
  
        """
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

xdia, xmes, xmm = carga()"""


dia = azar(1, 31)
mes = azar(1, 12)
mm = azar(0, 999999)
rango = azar(50, 200)

for i in range(rango):
    dia = azar(1, 31)
    mes = azar(1, 12)
    mm = azar(0, 999999)
    rango = azar(50, 200)
    update = str(dia) + ";" + str(mes) + ";" + str(mm)

    f = open("datos.txt", "a")
    f.write(update + "\n")
    f.close()

#--- leer
with open("datos.txt", "r") as f:
    for fila in f:
        print(fila)

exit = input("Presione cualquier tecla para finalizar.")