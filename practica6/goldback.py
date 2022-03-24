#!/usr/bin/python
# encoding: utf-8

import es_primo
import sys

'''Este ejercicio está incompleto, no me funciona del todo (si lo ejecutas se queda bloqueado en el número que no cumple la condición)'''

se_cumple = True # Asumimos que la conjetura se cumple
num_impar = 9 # Para empezar con el primer número impar que cumple

nombre_fichero = sys.argv[1]
fichero = open(nombre_fichero,'w')

while se_cumple:

    primos = [] # Para almacenar los primos menores que el número
    cuadrados_perfectos = [] # Para almacenar los cuadrados

    for i in range(num_impar): # Guardamos los primos
        if es_primo.es_primo(i) == True:
            primos.append(i)

    for i in range(1,num_impar//2): # Guardamos los cuadrados
        cuadrados_perfectos.append(i*i)

    if es_primo.es_primo(num_impar) == False: # Si es compuesto seguimos

        se_cumple = False

        for primo in primos: # while

            for cuadrado in cuadrados_perfectos:

                if num_impar == primo + 2*cuadrado: # Comprobamos si lo cumple y, si lo hace, probamos con el siguiente
                    print(f'{num_impar} lo cumple.')
                    fichero.write(f'{num_impar} = {primo} + {cuadrado}\n') # No siempre escribe en el fichero, tampoco entiendo el motivo
                    num_impar += 2
                    se_cumple = True
                    break

        '''Aquí intenté rompé el bucle (ya que significaría que pasó por todos los cuadrados y todos los primos sin
        encontrar que se cumpliera) poniendo "se_cumple = False" pero no me funcionaba, ya que se paraba tras comprobar
        con el primer número (el 9).'''

    else: # Si no es compuesto, pasamos directamente al siguiente
        num_impar += 2