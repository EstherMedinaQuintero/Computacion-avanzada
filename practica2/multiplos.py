#!/usr/bin/python

# Ejercicio 23

n = int(input('Primer número:'))
m = int(input('Segundo número:'))

'''if n < m:
    multiplos = []
    contador = n

    while n <= contador and  contador <= m*n:
        if contador%n == 0:
            multiplos.append(contador)
        contador +=1

    print(multiplos)'''

if n < m:
    multiplos = []

    for num in range(n,n*m+1):
        if num%n == 0:
            multiplos.append(num)

    print(multiplos)