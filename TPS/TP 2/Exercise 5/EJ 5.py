def calcular(x):
    flag = 0
    i = 1
    while (i < len(x)):
        if x[i] < x[i-1]:
            flag = 1
        i +=1
    if flag == 1:
        return False
    else:
        return True

x = [1, 2, 3, 4, 5]
y = [1, 5, 3, 4, 5]
z = ["b", "a"]
k = ["a", "b"]

print(calcular(x))
