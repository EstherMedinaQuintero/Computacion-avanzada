#!/usr/bin/python

# Ejercicio 17

num = float(input('Escriba el número:'))

while (num >= 0) and (num <= 10):

    print('Número fuera del rango.')
    num = float(input('Escriba el número:'))

print('Número dentro del rango')