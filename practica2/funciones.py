#!/usr/bin/python

# Ejercicio 20

def factorial_for(n):

    factorial = 1

    for n in range(2,n+1):
        factorial *= n
    return(factorial)



def factorial_while(n):

    contador = 2
    factorial = 1

    while contador < n:
        factorial *= contador
        contador += 1
    return(factorial)



# Ejercicio 21

def factorial_for_parar(n):

    factorial = 1

    for n in range(1,n+1):
        factorial *= n
        if factorial > 1000:
            print('El resultado es mayor que 1000.')
            break

    if factorial <= 1000:
        return(factorial)



def factorial_while_parar(n):

    contador = 1
    factorial = 1

    while (contador < n) and (factorial > 1000):
        factorial *= contador
        contador += 1

    if factorial > 10000:
        print('El resultado es mayor que 1000.')

    return(factorial)



# Ejercicio 22

def tabla_multiplicar():

    num = int(input('Introduzca un número:'))

    for n in range(1,11):
        print(f'{num} x {n} = {num*n}')



# Ejercicio 25

def suma_pares(n,m):

    pares = []

    if n < m:
        for num in range(n,m+1):
            if num%2 == 0:
                pares.append(num)

    else:
        for num in range(m,n+1):
            if num%2 == 0:
                pares.append(num)

    return(sum(pares))



# Ejercicio 26

def suma_divisores(n):

    divisores = [1]

    for num in range(2,n//2+1):
        if n%num == 0:
            divisores.append(num)
    if n != 1:
        divisores.append(n)

    return(sum(divisores))