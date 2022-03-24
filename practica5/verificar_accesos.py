#!/usr/bin/python
# encoding: utf-8

import os
import sys
import re

nombre_fichero_entrada = sys.argv[1]

if os.path.exists(nombre_fichero_entrada):

    fichero_entrada = open(nombre_fichero_entrada,'r')
    lineas = fichero_entrada.readlines()
    fichero_entrada.close()

    usuarios = {}

    '''Diccionario de la forma:   {'nombre': [fecha, hora, True/False, True/Flalse]}'''

    for i in range(len(lineas)):

        lineas[i] = lineas[i].replace('\n','') # Quitamos los \n
        separado = lineas[i].split(' ') # Separamos los datos
        usuario = separado[0] # Almacenamos el usuario

        if (re.match(r'[0-2][0-9]\/([0-9]|10|11|12)\/\d{4}',lineas[1])) == None:
            datos = [] # Lista provisional
            datos.append(separado[1]) # Añadimos la fecha
            datos.append(separado[2]) # Añadimos la hora
            datos.append(False) # Añadimos que la fecha está mal
            usuarios[usuario] = datos
        else:
            datos = [] # Lista provisional
            datos.append(separado[1]) # Añadimos la fecha
            datos.append(separado[2]) # Añadimos la hora
            datos.append(True) # Añadimos que la fecha está bien
            usuarios[usuario] = datos

        if (re.match(r'[0-2][0-9]:[0-5][0-9]:[0-5][0-9]',lineas[2])) == None:
            usuarios[usuario].append(False) # Añadimos que la hora está mal

        else:
            usuarios[usuario].append(True) # Añadimos que la hora está bien


    print('Fechas incorrectas') # Mostramos las que tienen Flase

    for key in usuarios:
        if usuarios[key][2] == False:
            print(f'{key}: {usuarios[key][0]}')

    print('Horas incorrectas') # Mostramos las que tienen False

    for key in usuarios:
        if usuarios[key][3] == False:
            print(f'{key}: {usuarios[key][1]}')

else:
    print('Ese fichero no existe')