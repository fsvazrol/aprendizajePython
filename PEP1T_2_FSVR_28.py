titulo = '\033[1m\033[4mPROGRAMA TELEGRAMA\033[0m\033[0m'  # Le damos título al programa.
print(titulo.center(100,' '))  # Y lo sacamos por pantalla centrándolo 100 espacios.
cadena = str(input('Teclea el mensaje: '))
print()
print('Cadena tecleada:', cadena)
print()
print('Mensaje a enviar:')
telegrama = cadena.replace('.', ' STOP') + 'STOP'  # Reemplazamos los puntos por un espacio seguido de la palabra STOP y añadimos un STOP al final del mensaje.
print(telegrama)  # Imprimimos la cadena telegrama.
print()
mensaje = cadena.replace('.',' ')  # Al mensaje original le retiramos los puntos y dejamos el mensaje solo con los espacios.
listatelegrama = mensaje.split()  # La función .split romperá la cadena donde encuentre un espacio, y pasará a ser una lista donde cada palabra será un item de la lista.
num5 = 0
num4 = 0
for palabra in listatelegrama:  # Con la función for le pedimos a Python que recorra cada palabra de la lista.
    if (len(palabra) > 5):  # Con la función len(cadena) Python sabrá la longitud de la cadena.
        num5 = num5 + 1  # Si la longitud de la palabra es >5 se almacena en la variable num5 sumándole 1 por cada palabra >5 que encuentre.
    else (len(palabra) <= 5):  # Si la longitud de la palabra es <=5 se almacena en la variable num4 sumándole 1 por cada palabra <=5 que encuentre.
        num4 = num4 + 1
print(f'La cadena contiene {len(listatelegrama)} palabras, de las cuales {num5} tienen más de 5 letras.')  # Sacamos por pantalla la información usando la
print(f'Por tanto, al precio de 0.25€/palabra tenemos {num4} y a 0.50€/palabra hay otras {num5}.')         # función mas eficiente a partir de Python 3.6, print(f' ')
total = float(0.25 * num4) + (0.50 * num5)
print(f'Total: {total}€')