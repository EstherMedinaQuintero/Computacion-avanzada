#!/usr/bin/python

# Ejercicio 5

import math # Para usar sus funciones

fichero = open('notas.txt','r')
notas = []

for line in fichero: # Añadimos las notas a la lista
    linea_separada = line.split('')
    notas.append(linea_separada[3])

fichero.clase()

print('La nota máxima fue ',max(notas),' y la mínima fue ',min(notas))
print('La nota media fue ',sum(notas)/len(notas))