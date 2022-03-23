#!/usr/bin/python

# Ejercicio 3

def buscar_palabras(nombre_fichero,palabra):

    num_linea = 0
    lineas = []

    fichero = open(nombre_fichero,'r')

    for line in fichero:
        num_linea += 1
        if palabra in line:
            lineas.append(num_linea)

    fichero.close()
    print(lineas)


# Ejercicio 6

def binario(cadena):
    for c in cadena:
        if c!=0 and c!=1:
            return False
        return True