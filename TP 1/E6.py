def concatenar(n1, n2):
    print(n1, end="")
    print(n2)
    
a = int(input("primer numero: "))
while(a < 0):
    print("numeros positivos solamente")
    a = int(input("primer numero: "))
b = int(input("segundo numero: "))
while(b < 0):
    print("numeros positivos solamente")
    b = int(input("segundo numero: "))

concatenar(a, b)
