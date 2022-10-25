def calculo(n, total):
    print(n)

    while n > 0:
        total = total + n
        n = n-1
        calculo(n, total)

    print("total: ", total)
    quit()

def main():
    n = int(input("numero: "))
    total = 0
    calculo(n, total)

main()