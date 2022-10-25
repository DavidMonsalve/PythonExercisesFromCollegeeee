def producto(a, b, resto):

    while resto >= b:
        resto = resto - b
        producto(a, b, resto)
    
    print(resto)
    quit()

def carga():
    try:
        a = int(input("dividendo: "))
        b = int(input("divisor: "))
        if a < b:
            print("error.")
            carga()
        return a, b
    except ValueError:
        print("caracter invalido.")
        carga()

def main():
    a, b = carga()
    resto = a
    producto(a, b, resto)

main()