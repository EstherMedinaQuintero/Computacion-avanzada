#!/usr/bin/python3
# encoding: utf-8

import sys
import os


class Cell:

    """ Clase que define una celula """

    def __init__(self, viva=True):
        """ Para iniciar una celula, viva 
        debe ser boleano. Si no se pasa valor, 
        se inicia a viva"""
        self.__isAlive = viva

    def __str__(self):
        """ Convierte la celula a cadena """
        if self.__isAlive == True:
            return 'o'
        else:
            return '*'

    def getAlive(self):
        """ Devuelve si una celula esta viva o no """
        return self.__isAlive

    def setAlive(self, viva):
        """ Cambia el estado de la celula """
        self.__isAlive = viva


class World:

    """ Clase que define un mundo """

    def readFromFile(self, nombre_fichero=sys.argv[1]):
        """ Metodo que permite leer el
        fichero de entrada  """

        if os.path.exists(nombre_fichero):

            fichero = open(nombre_fichero,'r')
            fichero_lineas = fichero.readlines()
            fichero.close()

            self.__numRows = int(fichero_lineas.pop(0))
            self.__numCols = int(fichero_lineas.pop(1))

            matriz = []

            for i in range(self.__numRows): # Recorremos las filas
                lista_provisional = []
                for j in range(self.__numCols): # Recorremos las columnas
                    if fichero_lineas[i][j] == 'o':
                        cell = Cell(True)
                        lista_provisional.append(cell)
                    else:
                        cell = Cell(False)
                        lista_provisional.append(cell)

                matriz.append(lista_provisional)
                self.__matriz = matriz

        else:
            print('Ese fichero no existe.')

    def __init__(self):
        """ Constructor de la clase World, que inicializa todos los 
        atributos a valores arbitrarios."""
        self.__numRows = 0
        self.__numCols = 0
        self.__matriz = [[]]

    def __str__(self):
        """ Convierte a cadena un mundo """
        for i in range(self.__numRows): # Recorremos las filas
            linea_provisional = ''
            for j in range(self.__numCols): # Recorremos las columnas
                linea_provisional += str(self.__matriz[i][j])
                print(linea_provisional)

    def writeToFile(self, nombre_fichero=sys.argv[2]):
        """ Guarda en un fichero el mundo """
        fichero = open(nombre_fichero,'w')
        fichero.write(f'{self.__numRows}\n')
        fichero.write(f'{self.__numCols}\n')
        fichero.write(str(self.__matriz))
        fichero.close()


    def isAlive(self, row, col):
        """ Comprueba si la celula de esa posicion esta viva """
        return self.__matriz[row][col].__isAlive()

    def getNumberAliveNeighbours(self,row,col):
        """ Devuelve el numero de vecinos vivos """
        num_vivos = 0

        for i in range(-1,2):
            for j in range(-1,2):
                if i!= j:
                    if self.__matriz[row+i][col+j]._isAlive() == True:
                        num_vivos += 1

        return num_vivos

    def  isGoingToBeAlive(self, row, col):
        """ Devuelve si va a estar viva en la siguiente iteracion """
        return self.__matriz[row][col].getNumberAliveNeighbours


# Codigo para comprobar el funcionamiento de la clase vector2D
if __name__ == '__main__':
    cel1 = Cell()
    print(cel1)
    print(cel1.getAlive())
    cel1.setAlive(False)
    print(cel1.getAlive())
    print(cel1)
    Mundo = World()
    print(Mundo)