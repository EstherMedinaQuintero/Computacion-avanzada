#!/usr/bin/python

# Ejercicio 18

lista = [] # Lista vacía para ir introduciendo números
cantidad = int(input('¿Cuántos números quiere introducir?:'))

for n in range(0,cantidad):
    lista.append(int(input('Introduzca un número:')))

print(f'El número máximo introducido es {max(lista)}')

'''Para ahorrar tiempo podríamos haber
comprobado con un if e ir actualizando
el máximo.'''