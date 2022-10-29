def contarvocales(p):
    dic = {}
    a = 0
    e = 0
    i = 0

    letras = list(p)
    print(letras)

    for vocal in letras:
        if vocal == "a":
            a += 1
        elif vocal == "e":
            e += 1
        elif vocal == "i":
            i += 1
    dic["a"] = a
    dic["e"] = e
    dic["i"] = i
    print(dic)

palabra = input("palabra: ")
contarvocales(palabra)