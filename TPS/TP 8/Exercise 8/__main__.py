from random import randint as azar
def cargar(dic):
    for i in range (5):
        clave = azar(1, 20)
        valor = clave ** 2
        dic[clave] = valor
    return dic

dic = {}
dic = cargar(dic)
print(dic)
