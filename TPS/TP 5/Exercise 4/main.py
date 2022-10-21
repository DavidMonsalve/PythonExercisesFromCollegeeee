try:
    act = 0
    for i in range (100001):
        act = i
        print(i)
except KeyboardInterrupt:
    print("Are your sure you want to stop the program?")
    print("1 - YES.")
    print("2 - NO.")

    userInput = input("")
    possibleAnswers = ["1", "2"]
    while userInput not in possibleAnswers:
        print("ERROR: Ingresa un 1 o un 2.")
        userInput = input("")


    if userInput == "1":
        print("Finalizando programa.")
        exit()    
    else:
        for i in range (act, 100001, 1):
            print(i)

f = input("Presiona cualquier tecla para finalizar.")