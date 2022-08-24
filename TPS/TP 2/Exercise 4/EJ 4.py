x = ["car", "house", "dog", "bread"]
y = ["eggs", "car", "house", "ketchup"]
z = []

print("x (original): ", x)
print("y           : ", y)

for i in x:
    if i in y:
        z.append(i)

for i in z:
    if i in x:
        x.remove(i)
print(" ")
print(" ")
print("z (a eliminar): ", z)
print("x (resultante): ", x)