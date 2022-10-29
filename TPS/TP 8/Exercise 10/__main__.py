def eliminarclaves(lista, dic):
    for i in range(len(lista)):
        del dic[lista[i]]

    print(dic)

lista_claves = [5, 10, 30]
dic = {5: "futbol", 8: "morgan freeman", 10:"gotham", 30:"uade"}
eliminarclaves(lista_claves, dic)