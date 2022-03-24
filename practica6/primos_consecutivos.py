#!/usr/bin/python
# encoding: utf-8

import sys
import re
import es_primo

num = int(sys.argv[1])

if num >= 5:


    numeros = {} # Diccionario de la forma: {num1:[num2,num3]} num1 es el primer número del intervalo, num2 el segundo y num3 el que cumple las condiciones
    primos = [] # Lista auxiliar para guardar los primos


    for i in range(5,num+1):

        if es_primo.es_primo(i): # Comprobamos si es primo:
            primos.append(i)


    for i in range(len(primos)-1): # Recorremos todos menos el último
        primer_primo = primos[i]
        segundo_primo = primos[i+1]

        contador = primer_primo + 1 # Empezamos en el siguiente número
        primer_primo_buscar = str(primer_primo)+'$'

        while contador != 0:

            if (re.search(primer_primo_buscar,str(contador)) != None) and (contador%segundo_primo == 0): # Si cumple ambas condiciones
                lista = [segundo_primo,contador]
                numeros[primer_primo] = lista # Lo añadimos todo al diccionario
                contador = 0
            else:
                contador += 1

    para_sumar = [] # Para guardar los números que queremos sumar
    for key in numeros:
        para_sumar.append(numeros[key][1]) # Preparamos los números que vamos a sumar

    print('La suma de los números es:',sum(para_sumar)) # Enseñamos la suma

    fichero = open(input('Fichero de salida:'),'w') # Para escribir los resultados

    for key in numeros: # Escribimos en el fichero
        fichero.write(f'({key},{numeros[key][0]}): {numeros[key][1]}\n')

    fichero.close() # Cerramos el fichero

else:
    print('El número debe ser mayor o igual a 5.')