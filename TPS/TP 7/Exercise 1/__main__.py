def calcularDigitos(n, contador):
    n = n // 10
    contador += 1
    return n, contador

def main():
    contador = 0
    try:
        n = int(input("numero: "))
        while n > 0:
            n, contador = calcularDigitos(n, contador)
        print(contador)
    except ValueError:
        print("valor invalido.")
        main()

main()