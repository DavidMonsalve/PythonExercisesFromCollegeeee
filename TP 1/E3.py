def calcular(cant, t):
    gasto = 0
    descuento = 0
    if (cant >=1) and (cant <=20):
        gasto = cant*t
    elif (cant >=21) and (cant <=30):
        descuento = (cant*t)*0.20
        gasto = (cant*t) - descuento
    elif (cant >=31) and (cant <=40):
        descuento = (cant*t)*0.30
        gasto = (cant*t) - descuento
    elif (cant >40):
        descuento = (cant*t)*0.40
        gasto = (cant*t) - descuento
    return gasto

tarifa = 26
viajes = int(input("Viajes realizados: "))

x = calcular(viajes, tarifa)

print("total gastado: ", x)