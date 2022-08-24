def intercalar(l1, l2):
    i = 1
    j=0
    while (i < len(l1)):
        l1.insert(i, l2[j])
        i += 2
        j += 1
    l1.insert(i, l2[j])
    return l1


x = [8, 1, 3]
z = [5, 9, 7]

print(intercalar(x, z))