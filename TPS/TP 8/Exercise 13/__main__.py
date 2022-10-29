def buscarclave(dic, valor):
    lista = []
    c = 0
    nombre = list(dic.keys())
    print(nombre)
    for obj in dic:
        
        nombre_actual = nombre[c]

        x = dic.get(obj)
        if valor == x:
            print(nombre_actual)
            lista.append(nombre_actual)

        c += 1
    
    print(lista)

dic = {
    "a": 1,
    "b": 1,
    "c": 3,
    "d": 2,
    "e": 1,
}

valor = int(input("valor: "))

buscarclave(dic, valor)