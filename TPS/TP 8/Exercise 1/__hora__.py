def ingreso():
    try:
        hora = int(input("hora: "))
        while(hora > 23) or (hora < 0):
            hora = int(input("hora: "))

        minutos = int(input("minutos: "))
        while (minutos > 59) or ( minutos < 0):
            minutos = int(input("minutos: "))

        if hora < 11:
            meridian = "AM"
        else:
            meridian = "PM"
        
        tiempo = (hora, minutos, meridian,)

        return tiempo

    except ValueError:
        print("dato invalido.")
        ingreso()


def calculo(hora1, hora2):
    contador_horas = 0
    contador_min = 0

    L1 = list(hora1) 
    L2 = list(hora2)


    #Calculo de tiempo entre HORAS.
    if L1[0] == L2[0]:
        contador_horas = 0
    elif L1[0] < L2[0]:

        while L1[0] < L2[0]:
            L1[0] += 1
            contador_horas += 1

    else:

        while L1[0] != L2[0]:

            if L1[0] == 24:
                L1[0] = 0

            else:
                L1[0] +=1
                contador_horas +=1

    #Calculo de tiempo entre MINUTOS.
    if (L1[1] == L2[1]):
        contador_min = 0
    elif (L1[1] < L2[1]):
        contador_min = L1[1] - L2[1]
        contador_min = abs(contador_min)
    
    else:
        contador_min = L1[1] - L2[1]

    tiempo_diferencia = (contador_horas, contador_min,)
    return tiempo_diferencia
