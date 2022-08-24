def normalizar(lista):
    print('Original List:', )
    minimo = min(lista) 
    maximo=max(lista)
    for i, x in enumerate(lista):
      lista[i] = (x-minimo) / (maximo-minimo)
    print('Lista normalizada:',lista)


lista = [1, 2, 3]

normalizar(lista)