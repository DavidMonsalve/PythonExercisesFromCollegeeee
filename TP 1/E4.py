def vuelto(c, r):
    diferencia = r - c
    billetes = []
    if (diferencia > 0):
        while (diferencia >= 500):
            billetes.append("500")
            diferencia = diferencia - 500
        while (diferencia >= 100):
            billetes.append("100")
            diferencia = diferencia - 100
        while (diferencia >= 50):
            billetes.append("50")
            diferencia = diferencia - 50
        while (diferencia >= 20):
            billetes.append("20")
            diferencia = diferencia - 20
        while (diferencia >= 10):
            billetes.append("10")
            diferencia = diferencia - 10
        while (diferencia >= 5):
            billetes.append("5")
            diferencia = diferencia - 5
        while (diferencia >= 1):
            billetes.append("1")
            diferencia = diferencia - 1
    else:
        billetes.append("Pago justo, sin necesidad de vuelto.")
    
    return billetes





compra = int(input("total compra:"))
recibido = int(input("Dinero recibido: "))

while (recibido < compra):
    print("--ERROR 403-- Monto recibido menor a compra.")
    recibido = int(input("Dinero recibido: "))

x = vuelto(compra, recibido)

print(x)