
def borrar(conjunto):
    try:
        n = int(input("numero a borrar (-1) para detener: "))
        while n != -1:
            if n in conjunto:
                conjunto.discard(n)
                print("numero eliminado: ", n)
            else:
                print("el numero no esta en el conjunto...")
            n = int(input("numero a borrar (-1) para detener: "))
    except ValueError:
        borrar(conjunto)

conjunto = set()
for i in range (9):
    conjunto.add(i+1)
print(conjunto)

borrar(conjunto)
print(conjunto)