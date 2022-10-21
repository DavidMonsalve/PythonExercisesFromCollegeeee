def monthFinder():
    try:
        month = int(input("mes a buscar: "))
        monthS = ["january", "february", "march", "april", "may",
                "june", "july", "agost", "september",
                "octuber", "november", "december"]

        print(monthS[month-1])
    except IndexError:
        print("El numero ingresado esta fuera del rango de la lista de los meses.")
        monthFinder()
    except ValueError:
        print("ERROR: Ingresar un numero entero del 1 al 12.")
        monthFinder()

monthFinder()