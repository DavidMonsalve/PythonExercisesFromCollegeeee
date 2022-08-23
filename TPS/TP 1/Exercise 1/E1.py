def calcular():
    aux = -2
    max = -1
    for i in range(3):
        n = int(input("Numero: "))


        if n >= max:
            if (n == aux):
                max = -1
            else:
                aux = n
                max = n
    return max
        

mayor = calcular()

print(mayor)