dic = {
    "cuaderno":500,
    "lapiz":250,
    "hoja":100,
    "libro":1000
}

precio = dic.get("cuaderno")
aumento = precio * 0.12
precio = precio + aumento

dic["cuaderno"] = precio
print(dic)