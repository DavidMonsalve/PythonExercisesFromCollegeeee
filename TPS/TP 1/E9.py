import random

def f_1(n):
    n_jugo = 0
    naranjasValidas = 0
    nUtilizables = 0
    cajones = 0

    peso_nValidas = []
    peso_total_nValidas = 0
    for i in range(n):
        
        peso_n = random.randint(150, 350)

        if (peso_n < 200) or (peso_n > 300):
            n_jugo += 1
        else:
            naranjasValidas += 1
            nUtilizables +=1
            peso_nValidas.append(naranjasValidas)

            if naranjasValidas == 100:
                cajones += 1

                for i in range(len(peso_nValidas)):
                    peso_total_nValidas = peso_total_nValidas + peso_nValidas[i]
                
                peso_nValidas = []
                naranjasValidas = 0
    pesoEnKilos = (peso_total_nValidas // 1000)


    auxPeso = pesoEnKilos
    camiones = 0
    porcentaje_minimo = 500*0.80

    while (auxPeso > 500):
        camiones += 1
        auxPeso -= 500 
    if (auxPeso > porcentaje_minimo):
        camiones += 1
        auxPeso -= auxPeso


    print("total de naranjas utiles: ", nUtilizables)
    print("naranjas para jugo: ", n_jugo)
    print("naranjas restantes: ", naranjasValidas, " (es decir, las que no llegaron a completar un cajon)")
    print("Se pueden llenar: ", cajones, " cajones")
    print("peso total cajones (g): ", peso_total_nValidas)
    print("peso total cajones (kg): ", pesoEnKilos)
    
    print("-------------------------")
    print("camiones necesarios: ", camiones)
    print("total de naranja inmovilizada por falta de ocupacion en camion (menor al 80%): ", auxPeso, "KG")


naranjas = int(input("Cantidad naranjas: "))


f_1(naranjas)


salida = input("presiona cualquier tecla para salir.")