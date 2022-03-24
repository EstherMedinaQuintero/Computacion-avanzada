#!/usr/bin/python
# encoding: utf-8

import os
import sys
import re

nombre_fichero_entrada = sys.argv[1]
nombre_fichero_salida = sys.argv[2]

if os.path.exists(nombre_fichero_entrada): # Si el fichero existe

    fichero = open(nombre_fichero_entrada,'r')
    lineas_fichero = fichero.readlines() # Almacenamos las líneas
    lineas_arregladas = [] # Para guardarlas cuando las arreglemos
    fichero.close()

    for linea in lineas_fichero:

        fecha = re.findall(r'\d{4}/\d\d/\d\d',linea) # Buscamos las fechas
        if fecha != []:
            fecha_separada = fecha[0].split('/') # Separamos los datos
            fecha_separada.reverse() # Los colocamos en el orden correcto
            fecha_colocada = f'{fecha_separada[0]}/{fecha_separada[1]}/{fecha_separada[2]}' # Volvemos a pegarlos
            linea = linea.replace(fecha[0],fecha_colocada) # Sustituímos la fecha antigua por la nueva
        lineas_arregladas.append(linea)

    fichero = open(nombre_fichero_salida,'w') # Escribimos las líneas arregladas
    for linea in lineas_arregladas:
        fichero.write(linea)
    fichero.close()

else:
    print('Ese fichero no existe')