import os
import pickle

documento = "./abonado.dat"
# Contenido original del documento:
# [{'numAbo': '636363636', 'nomAbo': 'Alex', 'facAbo': 34.45}, {'numAbo': '626262626', 'nomAbo': 'Ana', 'facAbo': 41.87}]

# Cargamos el archivo y le metemos la lista inicial
with open("abonado.dat", "wb") as archivo:
    lista = [{'numAbo': '636363636', 'nomAbo': 'Alex', 'facAbo': 34.45}, {'numAbo': '626262626', 'nomAbo': 'Ana', 'facAbo': 41.87}]
    pickle.dump(lista, archivo)

# Funciones que te crió:
# 1º Alta de nuevos abonados.
# Pedimos los datos a introducir al usuario.
# Abrimos el archivo en modo lectura binaria y cargamos los datos en una lista.
# Añadimos a dicha lista los datos introducidos como nuevo diccionario.
# Abrimos el archivo en modo lectura/escritura brinaria
# y volcamos dentro el contenido de dicha lista.

def opcion1():
    numAbo = input("\033[1mNúmero del abonado: \033[0m")
    nomAbo = input("\033[1mNombre: \033[0m")
    facAbo = float(input("\033[1mValor de la factura: \033[0m"))
    with open(documento, "rb") as archivo:
        lista1 = pickle.load(archivo)
    lista1.append({'numAbo': numAbo, 'nomAbo': nomAbo, 'facAbo': facAbo})
    with open(documento, "rb+") as archivo:
        pickle.dump(lista1, archivo)
        print()
        print("\tDatos del nuevo usuario incorporados al fichero.")
        print()

# 2º Modificación del valor de la factura de un abonado.
# Pedimos al usuario que introduzca el número de abonado a consultar.
# Abrimos el archivo en modo lectura binaria y cargamos los datos en una lista.
# Añadimos a dicha lista los datos introducidos como nuevo diccionario.
# Con un for recorreremos la lista y con un if comprobamos si el número introducido
# coincide con alguno de los existentes en el fichero, en cuyo caso se solicita al
# usuario que introduzca el nuevo valor de la factura y actualizamos su valor en la lista.
# Volvemos a abrir el archivo en modo lectura/escritura brinaria
# y volcamos dentro el contenido de dicha lista.

def opcion2():
    modAbo = input("\033[1mNúmero del abonado: \033[0m")
    print()
    with open(documento, "rb") as archivo:
        lista = pickle.load(archivo)
    for item in lista:
        if item["numAbo"] == modAbo:
            print("\tValor de la factura: ", item["facAbo"])
            print()
            importe = float(input("\033[1mNuevo Valor factura: \033[0m"))
            item["facAbo"] = importe
            print()
            print("\tDato del usuario modificado en el fichero")
            print()
    with open(documento, "rb+") as archivo:
        pickle.dump(lista, archivo)

# 3º Consulta del dato de facturación de un abonado.
# Pedimos al usuario que introduzca el número de abonado a consultar.
# Inicializamos la variable control a 0.
# Abrimos el archivo en modo lectura binaria y cargamos los datos en una lista.
# Con un for recorreremos la lista y con un if comprobamos si el número de abonado
# coincide con alguno de los existentes en el fichero, en cuyo caso se muestra por pantalla
# el valor actual de la factura. Igualamos el control a 1 para que no entre en el siguiente
# if y deje de buscar dentro del mismo item de la lista.
# Si no se encuentra el número de abonado y no entrar al primer if entonces entrará a un
# segundo if, indentado a la altura del for, ya que control es 0, e imprimirá por pantalla
# que el número de abonado no se ha encontrado.

def opcion3():
    modAbo = str(input("\033[1mNúmero del abonado: \033[0m"))
    print()
    control = 0
    with open(documento, "rb") as archivo:
        lista = pickle.load(archivo)
    for item in lista:
        if item["numAbo"] == modAbo:
            print("\tValor de la factura: ",item["facAbo"])
            control = 1
            print()
    if control == 0:
        print("\tAbonado no registrado.")
        print()

# 4º Consulta del dato de facturación total de la compañía.
# Inicializamos la variable totalFac a 0.
# Abrimos el archivo en modo lectura binaria y cargamos los datos en una lista.
# Con un for recorreremos la lista e iremos almacenando en totalFac el valor anterior de la
# misma más el importe de la factura de cada abonado que se ha ido recorriendo con for.
# Finalmente, imprimimos por pantalla la suma total acumulada en totalFac

def opcion4():
    totalFac = 0.0
    with open(documento, "rb") as archivo:
        lista = pickle.load(archivo)
        for item in lista:
            totalFac = totalFac + item["facAbo"]
    print("\tFacturación total: ", totalFac)
    print()

# 5º Eliminar el fichero.
# Utilizamos la estructura de if...else para comprobar si el archivo a borrar existe.
# En el primer if, os.path.exists('abonado.dat') nos devuelve True si el archivo existe, en
# cuyo caso podemos continuar dentro del if, con os.remove('abonado.dat') borramos el archivo.
# Si no se encontró el archivo, saltamos al else e imprimimos por pantalla un aviso al
# usuario indicándole que no hay ningún archivo que eliminar.

def opcion5():
    if os.path.exists('abonado.dat'):
        os.remove('abonado.dat')
        print("\tFichero eliminado.")
        print()
    else:
        print('\tNo hay ningún archivo que eliminar.')
        print()

# Comienzo del programa principal
titulo = '\033[1m\033[4mPROGRAMA GESTIÓN COMPAÑÍA TELEFÓNICA\033[0m\033[0m'
print(titulo.center(100, ' '))
print()

# En un diccionario creamos el menú de opciones
menu = {}
menu['\t\t1)'] = "Alta de nuevos abonados"
menu['\t\t2)'] = "Modificación del valor de la factura de un abonado"
menu['\t\t3)'] = "Consulta del dato de facturación de un abonado"
menu['\t\t4)'] = "Consulta del dato de facturación total de la compañía"
menu['\t\t5)'] = "Eliminar el fichero"
menu['\t\t6)'] = "Salir"

# Usaremos un while para gestionar las opciones del menu
while True:
    meop = ('\033[1mMenú de Opciones\033[0m')
    print(meop.center(90, ' '))
    subr = ('\033[1m================\033[0m')
    print(subr.center(90, ' '))
    print()
    opciones = menu.keys()
    for selec in opciones:
        print(selec.rjust(21,' '), menu[selec])
    print()
    selection = input("\t \t \t \t \t \t \t \t \033[1mOpción: \033[0m")

# Primera Opción.
    if selection == '1':
        print("\033[1m\033[4mAlta de factura\033[0m\033[0m")
        print()
# Llamada a la funcion opcion1()
        opcion1()

# Segunda Opción.
    elif selection == '2':
        print("\033[1m\033[4mModificación del valor de factura\033[0m\033[0m")
        print()
# Llamada a la funcion opcion2()
        opcion2()

# Tercera Opción.
    elif selection == '3':
        print("\033[1m\033[4mConsulta facturación abonado\033[0m\033[0m")
        print()
# Llamada a la funcion opcion3()
        opcion3()

# Cuarta Opción.
    elif selection == '4':
        print("\033[1m\033[4mConsulta facturación total\033[0m\033[0m")
        print()
# Llamada a la funcion opcion4()
        opcion4()

# Quinta Opción.
    elif selection == '5':
        print("\033[1m\033[4mEliminar fichero\033[0m\033[0m")
        print()
# Llamada a la funcion opcion5()
        opcion5()

# Sexta Opción, finalizamos la ejecución del programa con Break.
    elif selection == '6':
        break
# Séptima y resto de opciones
    else:
# Un aviso de cortesía para cuando el usuario introduce un valor inexistente.
        print("Opción incorrecta. Por favor, inténtelo de nuevo.")
        print()