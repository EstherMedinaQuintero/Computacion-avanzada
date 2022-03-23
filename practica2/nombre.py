#!/usr/bin/python

# Ejercicio 14

nombre = repetido = input('Escriba el nombre que quiere repetir:')

# Concatenación:

repetido = (nombre + ' ')*999 + nombre
print(repetido)

# Bucle:

for n in range(1,1000):
    repetido += ' ' + nombre

print(nombre)