#!/usr/bin/python

# Ejercicio 7

nombre_fichero = input('Indique el nombre del fichero:')

fichero = open(nombre_fichero,'w')

texto = fichero.read()
texto.lower()

separado =  texto.split('')

for i in range(len(separado)):
    if (i%2 != 0) or (i == 0):
        separado[i].upper()
    else:
        separado[i].lower()

for i in range(len(separado)):
    fichero.write(separado[i])