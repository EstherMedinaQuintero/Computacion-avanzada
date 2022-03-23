#!/usr/bin/python

# Ejercicio 6 (programa)

import funciones.py

nombre_fichero_entrada = input('Indique el nombre del fichero de entrada:')
nombre_fichero_salida = input('Indique el nombre del fichero de salida:')

fichero_entrada = open(nombre_fichero_entrada,'r')
fichero_salida = open(nombre_fichero_salida,'a')

for line in fichero_entrada:
    linea = line.split('')

    for i in range(len(linea)):

        if binario(linea[i]) == True:
            fichero_salida.write(linea[i])

fichero_entrada.close()
fichero_salida.close()