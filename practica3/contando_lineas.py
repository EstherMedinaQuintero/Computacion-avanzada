#!/usr/bin/python

# Ejercicio 2

import os # Para usar la función

nombre_fichero = input('Introduzca el nombre del fichero:')

if os.path.exist(nombre_fichero):  # Si el fichero existe

    fichero = open(nombre_fichero,'r') # Abrimos el fichero
    lineas = caracteres = 0 # Para luego ir sumando

    for line in fichero: # Contamos las líneas y los caracteres
        lineas += 1
        caracteres += len(line)
    print('Líneas:',lineas)
    print('Caracteres:',caracteres)
    fichero.close()

else:
    print('Ese fichero no existe.')