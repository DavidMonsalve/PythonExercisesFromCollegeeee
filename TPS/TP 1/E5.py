def p_1(filas):
    for j in range(5):
        for i in range(filas):
            print("*", end = " ")
        print(" ")

def p_2(filas):
    for j in range(5):
        for i in range(filas):
            print("*", end = " ")
        print(" ")
        filas += 2


f = int(input("numero de filas: "))
p_1(f)

print(" ")
f = int(input("numero de filas inicial: "))
p_2(f)