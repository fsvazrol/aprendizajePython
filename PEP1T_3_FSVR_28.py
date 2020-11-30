import sys
titulo = '\033[1m\033[4mPROGRAMA OPTIMIZACIÓN TELEGRAMA\033[0m\033[0m'
print(titulo.center(100, ' '))
print()

#  Parametro: Llego mañana alrededor del almuerzo. Yo llevo los pasteles.

lmensaje = (sys.argv[1:])
mensaje = ' '.join(lmensaje)
mensupper = mensaje.upper()
print('Cadena recibida:',mensupper)
print()
# En un diccionario creamos el menú de opciones
menu = {}
menu['\t\t1)'] = "Envío con precio normal"
menu['\t\t2)'] = "Envío con precio reducido"
menu['\t\t3)'] = "Envío barato en código morse"
menu['\t\t4)'] = "Salir"
# Usaremos un while para gestionar las opciones del menu
while True:
    meop = ('\033[1mMenú de Opciones\033[0m')
    print(meop.center(90, ' '))
    subr = ('\033[1m================\033[0m')
    print(subr.center(90, ' '))
    print()
    num5 = 0
    num4 = 0
    opciones = menu.keys()
    for selec in opciones:
        print(selec.rjust(21,' '), menu[selec])
    print()
    selection = input("\t \t \t \t \t \t \t \t Opción: ")

# Primera Opción
    if selection == '1':
# Esta opción es copiada del Puntuable anterior
        cadena1 = mensupper.replace('.', ' ')
        listatelegrama = cadena1.split()
# Dos for para recorrer cada elemento de la lista y otro for para recorrer cada letra de la palabra
        for palabra in listatelegrama:
            if (len(palabra) > 5):
                num5 = num5 + 1
            else:
                num4 = num4 + 1
# Asignamos el precio en variables por si en un futuro queremos cambiarlos
        preciopalabra4 = 0.25
        preciopalabra5 = 0.50
        print()
        print(f'La cadena contiene {len(listatelegrama)} palabras, de las cuales {num5} tienen más de 5 letras.')
        print(f'Por tanto, al precio de {preciopalabra4}€/palabra tenemos {num4} y a {preciopalabra5}€/palabra hay otras {num5}.')
        #total = float((0.25 * num4) + (0.50 * num5))
        print(f'Precio Total: {(preciopalabra4*num4) + (preciopalabra5*num5)}€')
        print()
        print('Mensaje enviado:')
        cadena2 = mensupper.replace('.', ' STOP')
        lista1 = cadena2.split()
# Damos la vuelta a la lista
        lista1.reverse()
# Al dar la vuelta a la lista, index buscará en que posición se encuentra el primer STOP
        stopfinal = lista1.index('STOP')
# Si el valor devuelto por index es 0 entrará al if
        if stopfinal == 0:
# Pop eliminará el elemento de la lista en la posición 0 (el STOP del punto final)
            lista1.pop(0)
# Volvemos a poner la lista del derecho
            lista1.reverse()
# Y añadimos el STOPSTOP final
            lista1.append('STOPSTOP')
# Unimos la lista y ya tenemos la cadena preparada
            print(' '.join(lista1))
        else:
# Si el valor devuelto por index no es 0 (no hay un STOP al final), ponemos la cadena del derecho
            lista1.reverse()
# Y le añadimos el STOPSTOP al final
            lista1.append('STOPSTOP')
# Unimos la lista y ya tenemos la cadena preparada
            print(' '.join(lista1))
        print()

# Segunda Opción
    elif selection == '2':
        cadena3 = mensupper.replace('.', '')
        listatelegrama = cadena3.split()
# Dos for para recorrer cada elemento de la lista y otro for para recorrer cada letra de la palabra
        for palabra in listatelegrama:
            if (len(palabra) > 5):
                num5 = num5 + 1
            else:
                num4 = num4 + 1
# Asignamos el precio en una variable por si en un futuro queremos cambiarlo
        preciopalabra = 0.25
        print()
        print(f'La cadena contiene {len(listatelegrama)} palabras, de las cuales {num5} tenían más de 5 letras pero se han recortado.')
        print(f'Por tanto, el mensaje se envía al precio de {preciopalabra}€/palabra.')
        print(f'Precio Total: {preciopalabra*(num4+num5)}€')
        print()
        cadena4 = mensupper.replace('.', ' STOP')
        listaupper = cadena4.split()
# Creamos una lista vacía y acortamos palabras superiores a 5 letras usando un for
        lista2 = []
        for palabra in listaupper:
            if (len(palabra) > 5):
# Almacenamos en una variable la palabra pero solo desde la primera letra hasta la 4
                palabra2 = palabra[0:5] + '@'
                lista2.append(palabra2)
            else:
                lista2.append(palabra)
        print('Mensaje enviado:')
# Damos la vuelta a la lista y repetimos el proceso de la opción 1
        lista2.reverse()
        stopfinal = lista2.index('STOP')
        if stopfinal == 0:
            lista2.pop(0)
            lista2.reverse()
            lista2.append('STOPSTOP')
            print(' '.join(lista2))
        else:
            lista2.reverse()
            lista2.append('STOPSTOP')
            print(' '.join(lista2))
        print()

# Tercera Opción
    elif selection == '3':
        morse = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.',
                 'F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
                 'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---',
                 'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
                 'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--',
                 'Z':'--..','.':'.-.-.-',
                 '0':'-----','1':'.----','2':'..---','3':'...--','4':'....-',
                 '5':'.....','6':'-....','7':'--...','8':'---..','9':'----.',}
        lista3 = []
        lmensaje = mensupper.split()
# Dos for para recorrer cada elemento de la lista
        for palabra in lmensaje:
# Y otro for para recorrer cada letra de la palabra
            for letra in palabra:
# Con .get(,) especificamos que queremos que tome el valor del diccionario y si no lo encuentra, que tome el valor ???
                    letra2 = morse.get(letra, '???')
                    lista3.append(letra2)
# Unimos la lista y ya tenemos la cadena preparada
        cadena5 = ' '.join(lista3)
# Ahora toca calcular el precio de la cadena, inicializamos variables
        numpuntos = 0
        numrayas = 0
# Con dos for recorremos cada bloque (la palabra en morse) y cada caracter (la letra en morse)
        for bloque in lista3:
            for caracter in bloque:
                if caracter == '.':
                    numpuntos = numpuntos + 1
                elif caracter == '-':
                    numrayas = numrayas + 1
                else:
                    break
# Creamos variables para los precios, por si en un futuro queremos cambiarlos.
        preciopuntos = 0.005
        preciorayas= 0.01
        print()
        print(f'La cadena convertida a código Morse tiene {numpuntos} puntos ({preciopuntos}€/punto) y {numrayas} rayas ({preciorayas}€/raya)')
        print(f'Por tanto, el mensaje se envía al precio de {numpuntos*preciopuntos + numrayas*preciorayas}€ ({numpuntos*preciopuntos}€ y {numrayas*preciorayas}€)')
        print('Mensaje enviado:')
        print(cadena5)
        print()
# Cuarta Opción
    elif selection == '4':
# Con el break finalizamos la ejecución del programa
        break
# Quinta y resto de opciones
    else:
# Un aviso de cortesía por si el usuario se equivoca introduciendo un valor inexistente
        print("Opción incorrecta. Por favor, inténtelo de nuevo.")