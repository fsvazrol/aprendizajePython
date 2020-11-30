import random

titulo = "\033[1m\033[4mPROGRAMA GENERA DADOS\033[0m\033[0m"
print(titulo.center(100," "))
print()

obtenido = 0
lista = []

dado1 = "     \n  *  \n     "
dado2 = "*    \n     \n    *"
dado3 = "*    \n  *  \n    *"
dado4 = "*   *\n     \n*   *"
dado5 = "*   *\n  *  \n*   *"
dado6 = "*   *\n*   *\n*   *"

def generar():
    generado = random.randint(1, 6)
    return generado

def imprimir():
    lanzamiento = int(input("¿Cuános dados lanzamos?: "))

    if (lanzamiento == 0):
        lista.sort()
        print("Los valores de los dados lanzados fueron: ", end = "")

        for i in range(len(lista)):
            if (i != (len(lista)-1)):
                print(lista[i], end=", ")
            else:
                print(lista[i])
    elif (lanzamiento < 0):
        print("Valor erróneo")
        return
    else:
        for i in range(lanzamiento):

            comprobacion = False

            obtenido = generar()
            print("El dado numero " + str(i + 1) + " ha generado aleatoriamente un: ")

            if(obtenido == 1):
                print(dado1)
                print("")

            elif(obtenido == 2):
                print(dado2)
                print("")

            elif (obtenido == 3):
                print(dado3)
                print("")

            elif (obtenido == 4):
                print(dado4)
                print("")

            elif (obtenido == 5):
                print(dado5)
                print("")

            elif (obtenido == 6):
                print(dado6)
                print("")

            else:
                print("Introduzca un numero")

            for x in lista:
                if(x == obtenido):
                    comprobacion = True

            if(comprobacion == False):
                lista.append(obtenido)

        imprimir()
imprimir()