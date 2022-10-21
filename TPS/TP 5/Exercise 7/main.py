






from random import randint as azar

def userResponse(c):
    try:
        userGuess = int(input("Intente adivinar el numero entre 1 y 500: "))
        return userGuess, c
    except ValueError:
        print("solamente ingresa numeros naturales. (1-500)")
        print("esto te costo un intento.")
        c += 1
        userResponse(c)

def check(number, guess, counter):

    final = False
    if number == guess:
        print("Congrats, you won! ...it only took u", counter+1, "attempts.")
        final = True
        counter += 1
        return counter, final
    else:
        counter +=1
        if guess > number:
            print("el numero es mas chico que el ingresado.")
        elif guess < number:
            print("el numero es mas grande que el ingresado.")
        userResponse(counter)


def fin(result):
    if result == True:
        print("result: yayy u won!")
    else:
        print("result: u lost.")


print("Bienvenido al JUEGO DE LAS PREGUNTAS!")


counter = 0
resultadoFinal = False
while resultadoFinal == False:
    number = azar(1, 500)
    print(number, " para testing y desarrollo de la app.")
    guess, counter = userResponse(counter)
    datosCheck = check(number, guess, counter)     """este programa pude haberlo solucionado desempacando la tupla de ahi sacar counter y el resultado del juego y bueno pero prefiero gastar ese tiempo en otra practica mas importante."""
    resultadoFinal = 
    print(counter)
    fin(resultadoFinal)



print("intentos: ", counter)

