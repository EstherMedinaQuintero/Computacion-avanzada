#!/usr/bin/python

import primos # Para usar la función es_primo
import sys # Para usar la llamada
import os # Para saber si el fichero existe

# Ejercicio 1 (primera parte)

def es_primo(num):

    if num < 2: # Descartamos ya esos
        return False
    else:
        for i in range(2,num):
            if num%i == 0: # Significaría que es divisible entre ese número, así que no sería primo
                return False
        return True # Solo quedarían los que son primos, así que devolvemos verdadero

# Ejercicio 1 (segunda parte)

fichero_primos = sys.argv[1]

if os.path.exist(fichero_primos):  # Si el fichero existe

    fichero = open(fichero_primos,'r')
    numeros = [] # Para guardar los números

    for line in fichero: # Arreglamos los números y los añadimos
        lineafea = line
        lineafea.replace('\n','')
        lineabonita = int(lineafea)
        numeros.append(lineabonita)

    fichero.close()

    for i in numeros: # Comprobamos si son primos
        if es_primo(i):
            print(i,' es primo.')
        else:
            print(i,' es compuesto.')

else:
    print('Ese fichero no existe.')