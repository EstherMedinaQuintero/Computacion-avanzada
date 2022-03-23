#!/usr/bin/python

# Ejercicio 24

n = int(input('Número positivo:'))
numeros = []

for num in range(0,n+1):
    numeros.append(num)

numeros.reverse()

for i in range(len(numeros)):
    print(numeros[i])