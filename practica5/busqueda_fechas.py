#!/usr/bin/python
# encoding: utf-8

import os
import sys
import re

# Ejercicio que hice sin mirar el de clase:

nombre_fichero = sys.argv[1]

if os.path.exists(nombre_fichero): # Si el fichero existe

    fichero = open(nombre_fichero,'r')
    lineas_fichero = fichero.readlines() # Almacenamos las líneas
    fichero.close()

    fichero = open(nombre_fichero,'r')
    texto = fichero.read() # Almacenamos el texto
    fichero.close()

    huecos_blancos = 0 # Para saber si hay algún hueco

    for i in range(len(lineas_fichero)):
        lineas_fichero[i] = lineas_fichero[i].replace('\n','') # Quitamos los \n

    linea_fecha = {} # Para guardar la fecha, junto a su línea y su intervalo

    for linea in lineas_fichero:

        fechas_linea = re.findall(r'\d{4}/\d\d/\d\d|\d\d/\d\d/\d{4}',linea) # Buscamos las fechas

        for i in fechas_linea: # Las metemos en el diccionario

            lista = []

            intervalo_mal = str(re.search(i,texto)) # Buscamos los caracteres
            intervalo_bien = str(re.findall(r'(\d.., \d..)',intervalo_mal)) # Arreglamos
            intervalo_bien = intervalo_bien.replace("['","") # Arreglamos
            intervalo_bien = intervalo_bien.replace("']","") # Arreglamos
            intervalo_bien = intervalo_bien.split(', ') # Separamos los dos números
            lista.append(intervalo_bien[0]) # Añadimos a la lista
            lista.append(intervalo_bien[1]) # Añadimos a la lista
            lista.append(i) # Añadimos la fecha
            linea_fecha[lineas_fichero.index(linea)] = lista # Añadimos la lista al diccionario

    for key in linea_fecha: # Mostramos los datos
        print(f'[{key}: {linea_fecha[key][0]} - {linea_fecha[key][1]} ] {linea_fecha[key][2]}')

else:
    print('Ese fichero no existe.')

'''Ejercicio de clase:

filename = sys.argv[1]

if os.path.exists(filename):
    filein = open(filename, 'r')

    nline = 0
    for line in filein:
        nline += 1
        # findall: devuelve la lista con las cadenas
        # finditer: devuelve un match object (lo cual nos permite acceder a las posiciones concretas)
        #dates = re.findall(r'(\d{2}/\d{2}/\d{4})|(\d{4}/\d{2}/\d{2})', line)
        matches = re.finditer(r'(\d{2}/\d{2}/\d{4})|(\d{4}/\d{2}/\d{2})', line)
        for m in matches:
            print(f'[{nline}: {m.start()} - {m.end()}] {m.group()}')
    filein.close()

else:
    print(f'El fichero {filename} no existe')'''