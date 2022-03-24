#!/usr/bin/python
# encoding: utf-8

import os
import sys
import datetime
import locale

nombre_fichero_entrada = sys.argv[1]
nombre_fichero_salida = sys.argv[2]
idioma = sys.argv[3]

if (idioma == 'spanish') or (idioma == 'español'): # Primero comprobamos el idioma y lo cambiamos
    locale.setlocale(locale.LC_TIME,'es_ES.UTF-8')
else:
    locale.setlocale(locale.LC_TIME,'en_US.UTF-8')

if os.path.exists(nombre_fichero_entrada): # Si el fichero existe, lo leemos
    fichero_entrada = open(nombre_fichero_entrada,'r')
    fechas = fichero_entrada.readlines()
    fichero_entrada.close()

    # Ahora escribimos las fechas en el fichero de salida
    fichero_salida = open(nombre_fichero_salida,'w')

    for fecha in fechas:

        fecha_str = fecha.rstrip() # Arreglamos la fecha
        fecha_obj = datetime.datetime.strptime(fecha_str,'%d/%m/%Y')

        if (idioma == 'spanish') or (idioma == 'español'):
            fichero_salida.write(fecha_obj.strftime('%A %d de %B de %Y')+'\n')

        else:
            fichero_salida.write(fecha_obj.strftime('%A, %B %d, %Y')+'\n')

    fichero_salida.close()

else:
    print('Ese fichero no existe.')