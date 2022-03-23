#!/usr/bin/python

# Ejercicio 19

n = int(input('Número:'))
factorial = 1




'''for n in range(2,n+1):
    factorial *= n
print(factorial)'''



contador = 2

while contador < n:
    factorial *= contador
    contador += 1
print(factorial)