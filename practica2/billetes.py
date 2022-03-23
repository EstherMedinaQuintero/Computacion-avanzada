#!/usr/bin/python

# Ejercicio 16

dinero = int(input('Dinero:')) # Pedimos la cantidad

lista = [500,200,100,50,20,10,5,2,1] # Para después clasificar

for n in lista:

    cantidad = int(dinero//n)

    if cantidad > 0: # Por si el denominador es mayor que el numerador

        if n > 2: # Aquí estamos en los billetes
            print(f'{cantidad} billete(s) de {n} euros')
        else: # Aquí estamos en las monedas
            print(f'{cantidad} moneda(s) de {n} euros')

        dinero -= n*cantidad


'''Para clasificar en billete o billetes sencillamente
tendríamos que añadir condiciones; es decir, mirar si
la cantidad de billetes (o monedas) es igual o mayor
que uno.'''