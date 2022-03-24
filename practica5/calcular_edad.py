#!/usr/bin/python
# encoding: utf-8

import os
import sys
import datetime

nombre_fichero_entrada = sys.argv[1]
nombre_fichero_salida = sys.argv[2]

if os.path.exists(nombre_fichero_entrada): # Si existe

    fichero_entrada = open(nombre_fichero_entrada,'r')
    lineas = fichero_entrada.readlines()
    fichero_entrada.close()

    personas = {} # Para guardar los datos

    for i in range(len(lineas)):
        lineas[i] = lineas[i].replace('\n','') # Quitamos los \n
        separado = lineas[i].split(' ') # Separamos los datos
        nombre = separado.pop(0) # Almacenamos el nombre y lo quitamos de la lista
        personas[nombre] = separado[0]+' '+separado[1] # Guardamos el resto en el diccionario

    fichero_salida = open(nombre_fichero_salida,'w')

    for key in personas:

        diferencia = str(datetime.datetime.now()- datetime.datetime.strptime(personas[key],'%d/%m/%Y %H:%M')) # Calculamos la diferencia
        diferencia = diferencia.split(' ') # Separamos los datos
        diferencia[2] = diferencia[2].split(':') # Separamos de nuevo los datos
        fichero_salida.write(print(f'{key} tiene {diferencia[0]} días, {diferencia[2][0]} horas y {diferencia[2][1]} minutos')) # Mostramos los datos)

    fichero_salida.close()

else:
    print('Ese fichero no existe')