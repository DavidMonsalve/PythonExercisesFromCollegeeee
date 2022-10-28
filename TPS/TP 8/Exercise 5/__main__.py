def calcular(a, b):
    x = (a[0]) * (b[0]) + (a[1]) * (b[1])
    if x == 0:
        detector = True
    else:
        detector = False

    print(x)
    print(detector)

a = (2, 3)
b = (-3, 2)

calcular(a, b)