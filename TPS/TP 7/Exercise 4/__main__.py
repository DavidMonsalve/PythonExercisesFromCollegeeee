def producto(a, b, total, auxA, auxB):

    while auxA < auxB:
        total = total + a
        auxA += 1
        producto(a, b, total, auxA, auxB)
    
    print(total)
    quit()

def carga():
    try:
        a = int(input("numero_1: "))
        b = int(input("numero_2: "))
        return a, b
    except ValueError:
        print("caracter invalido.")
        carga()

def main():
    total = 0
    a, b = carga()
    auxA = 0
    auxB = b
    producto(a, b, total, auxA, auxB)

main()