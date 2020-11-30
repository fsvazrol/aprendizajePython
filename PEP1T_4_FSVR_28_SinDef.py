# Importamos la función random para generar números aleatorios
import random

titulo = "\033[1m\033[4mPROGRAMA GENERA DADOS\033[0m\033[0m"
print(titulo.center(100," "))
print()

# Creamos un diccionario con las seis caras del dado.
dicedic = {
    1 : "     \n   *  \n      ",
    2 : "    *\n      \n *    ",
    3 : "    *\n   *  \n *    ",
    4 : "*   *\n      \n *   *",
    5 : "*   *\n   *  \n *   *",
    6 : "*   *\n *   *\n *   *"}

# Creamos una lista vacía para ir almacenando los resultados de las tiradas.
result = []

# "While" hará que se repita el bucle hasta que encuentre un "break".
while True:
    dicenum = int(input("¿Cuántos dados lanzamos? "))
    print()
# Si el número no es 0, entra al "If"
    if dicenum != 0:
# El "For" tendrá tantas iteraciones como hayamos especidifcado en dicenum
        for dice in range(dicenum):
# Generamos número aleatorio entre 1 y 6
            num = random.randint(1,6)
# Si el número generado no está previamente ya almacenado en la lista, entra al "If"
            if num not in result:
# Y lo añadimos a la lista
                result.append(num)
# Imprime por pantalla el número de tirada y el valor del diccionario que corresponde a su clave num
            print(f'El dado número {dice+1} ha generado aleatoriamente un: {num} \n\n {dicedic[num]}')
            print()
# Si el número es 0 (salir del programa) entrará al "Else"
    else:
        result.sort()
# Se imprimen los resultados por pantalla, pasando la lista a cadena con Str y aplicando
# Strip, una función que es para cadenas, y retiramos los [] de inicio y fin
        print(f'Los valores de los dados lanzados fueron: {str(result).strip("[]")}')
        print()
        print('Fin del programa')
# El Break hace que el programa salga del bucle While y termine.
        break