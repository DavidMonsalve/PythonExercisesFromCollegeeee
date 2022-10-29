def leer(dic, n):
    numero = str(n)
    for name,value in dic.items():
        print(numero + " x " + str(name) + " = " + str(value))

def cargar(dic, n):
    for i in range(12):
        clave = i + 1
        dato = n * clave

        dic[clave] = dato
    leer(dic, n)

dic = {}
n = int(input("numero: "))
dic = cargar(dic, n)