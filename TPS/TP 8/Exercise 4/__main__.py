from random import randint as azar

def calcular(t, t2):
    detector = False

    if t[0] == t2[0]:
        detector = True
    if t[0] == t2[1]:
        detector = True
    if t[1] == t2[0]:
        detector = True
    if t[1] == t2[1]:
        detector = True
    
    return detector

def main():
    n1 = azar(1, 6) 
    n2 = azar(1, 6) 
    n3 = azar(1, 6) 
    n4 = azar(1, 6)

    t1 = (n1, n2,)
    t2 = (n3, n4,)
    print(t1)
    print(t2)

    detector = calcular(t1, t2)

    print(detector)

main()