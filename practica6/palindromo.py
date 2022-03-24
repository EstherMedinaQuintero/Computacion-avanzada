#!/usr/bin/python
# encoding: utf-8

print('El ejercicio está inacabado')

import sys
import palindromo.py

def suma_es_capicua(num):

    num_cad = str(num) # Convertimos en cadena
    num_cad_inverso = num_cad[::-1] # Invertimos la cadena
    num_inverso = int(num_cad_inverso) # Convertimos a número
    suma = num + num_inverso # Sumamos los números
    if suma == suma[::-1]: # Comprobamos que es capicua
        return True
    else:
        return False

'''Me he dado cuenta de que es mejor comprobar por separado si el número
es capicua para luego usar la suma abajo, pero no me da tiempo a cambiarlo'''

print('El programa se queda bloqueado.')

nombre_fichero = sys.argv[1]
numero = int(sys.argv[2])

for num in range(1,numero+1): # Recorremos todos los números en ese intervalo

    capicua = False
    numero = num # Para ir incrementando
    iteraciones = 1 # Para ir contando las iteraciones

    while (iteraciones < 10) and (capicua == False):

        if palindromo.es_capicua(numero) == True:
            capicua = True

        else:
            iteraciones +=1


'''for num in range(1,numero+1): # Recorremos todos los números en ese intervalo

    bucle = True # Para entrar en el bucle
    numero = num

    while bucle: # Mientras no se cumpla, seguimos revisando <10 and no cap

        if (iteraciones < 10) and (num > 4): # Miramos si ya llevamos 10 iteraciones

            for n in range(int(len(suma_list))//2): # Recorremos la lista comprobando si los extremos son iguales

                if suma_list[n-1] != suma_list[-n-1]: # Si los extremos no coinciden, terminamos de revisar y pasamos al siguiente
                    bucle = False
                    iteraciones += 1
                    numero += 1
                    break

        elif (iteraciones < 10) and (num <= 4): # Si los números son menos que cuatro, ya sabemos que es una iteración

            fichero = open(nombre_fichero,'a')
            fichero.write(f'{num}: 1\n')
            fichero.close()
            iteraciones = 1
            bucle = False

        else: # Si ya llevamos 10 iteraciones, escribimos ya el número y pasamos al siguiente

            fichero = open(nombre_fichero,'a')
            fichero.write(f'{num}: >10\n')
            fichero.close()
            print(f'{num} no llega en 10 iteraciones.') # Mostramos ese número
            iteraciones = 1
            bucle = False'''