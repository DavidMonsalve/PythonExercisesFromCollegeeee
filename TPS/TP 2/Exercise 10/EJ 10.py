from random import randint
def generar(l):
    for i in range (10):
        l.append(randint(1, 100))
    return l

vacia = []
y = []
x = generar(vacia)

i = 0
while (i < len(x)):
    if (x[i] % 2 != 0):
        y.append(x[i])
    i +=1

print("original: ", x)
print("impares: ", y)