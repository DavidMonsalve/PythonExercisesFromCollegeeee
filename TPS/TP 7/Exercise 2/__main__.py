def ultimoDigito(n):
    digito = n % 10
    n = n // 10
    return digito, n

def convertir(n, total, exponente):

    digito, n = ultimoDigito(n)

    if digito == 1:
        resultado = 2 ** exponente
        total = total + resultado
    
    exponente += 1

    return n, exponente, total

def main():
    exponente = 0
    total = 0
    n = int(input("Numero binario: "))

    while n > 0:
        n, exponente, total = convertir(n, total, exponente)
    print(total)

main()