#!/usr/bin/python

# Ejercicio 4

fichero = open(' /etc/passwd','r')
nombre = input('Introduzca el nombre de usuario:')

for line in fichero:

    linea_separada = line.split(':') # Separamos los datos

    if linea_separada[0] == nombre: # Buscamos el que coincide
        print('El nombre real del usuario es ', linea_separada[4])
        fichero.close()
        break