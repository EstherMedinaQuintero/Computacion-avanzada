#!/usr/bin/python

import os # Para saber si el fichero existe

nombre_fichero = input('Nombre del fichero:')

'''Esta parte es para sacar los datos del fichero y trabajar con ellos'''

if os.path.exist(nombre_fichero):  # Si el fichero existe

    fichero = open(nombre_fichero,'r')
    lineas = fichero.readlines()
    fichero.close()
    alumnado = {} # Para guardar los alumnos y sus notas

    for i in range(0,len(lineas)):
        persona = lineas.pop(0)
        separado = persona.split(' ')

        nombre = separado[0]
        nota = separado[1].strip()

        alumnado[nombre] = nota

else:
    print('Ese fichero no existe.')

# Ejercicio 2 (primera parte)

def nota_alumno(nombre):

    for key in alumnado:
        if key == nombre:
            print(diccionario[key])
        else:
            print('Ese alumno no existe.')

# Ejercicio 2 (segunda parte)

def agregar_alumno(nombre,nota):

    alumnado[nombre] = nota # Añadimos a la persona
    fichero = open(nombre_fichero,'w')
    for key in diccionario:
        fichero.write(nombre+' '+nota+'\n') # Escribimos todo
    fichero.close()
    return fichero

# Ejercicio 2 (tercera parte)

def eliminar_alumno(nombre):

    del alumnado[nombre] # Eliminamos a la persona
    fichero = open(nombre_fichero,'w')
    for key in diccionario:
        fichero.write(nombre+' '+nota+'\n') # Escribimos todo
    fichero.close()
    return fichero