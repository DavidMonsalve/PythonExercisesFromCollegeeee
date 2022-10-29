conjunto = set()

cad = input("frase: ")

lista = cad.split(" ")

for i in range(len(lista)):
    conjunto.add(lista[i])

lista_ordenada = list(sorted(conjunto, key = len))
  
print(lista_ordenada)