#!/usr/bin/python
# enconding: utf-8

import os
import sys
import datetime
import locale

if len(sys.argv) !=3:
    print('Está usando mal el programa.')

else:

    nombre_fichero = sys.argv[1]
    num = int(sys.argv[2])
    locale.setlocale(locale.LC-TIME,'es_ES.UTF-8') # Horario español

    if os.path.exists(nombre_fichero): # Si el fichero existe
        fichero = open(nombre_fichero,'r')
        meses = {'enero':1,'febrero':2,'marzo':3,'abril':4,'mayo':5,'junio':6,'julio':7,'agosto':8,'septiembre':9,'octubre':10,'noviembre':11,'diciembre':12} # Diccionario auxiliar para acudir a él luego

        for line in fichero: # Arreglamos los datos del fichero
            nombre,dia,mes,año = line.split()
            fecha_incompleta = datetime.date(int(año),meses[mes.lower()],int(dia))
            fecha_completa = fecha_incompleta + datetime.timedelta(days = num*365)

            if datetime.date.today() >= fecha_completa: # Comprobamos si ha superado el tiempo
                print(f'El usuario {nombre} ya ha cumplido el periodo de permanencia')

        fichero.close()

    else:
        print('Ese fichero no existe.')