def cuadrado(N):
    lista = []
    for i in range(N):
        x = (i+1)**2
        lista.append(x)
    print("Lista completa: ", lista)
    print("Ultimos 10 elementos de la lista: ", lista[10:])

n = int(input("A: "))
while(n < 10):
    print("numero invalido, debe ser mayor que 9")
    n = int(input("A: "))
cuadrado(n)