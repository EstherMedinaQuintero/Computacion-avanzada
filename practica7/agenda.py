#!/usr/bin/python

import sys
from contacto import Contacto
import datetime
import os

class Agenda:
    """ Clase que define una agenda """

    def __init__(self,nombre_fichero = sys.argv[1]):
        """ Constructor de la clase Agenda """

        if os.path.exists(nombre_fichero): # Si el fichero existe

            lista_contactos = []
            self.__filename = nombre_fichero
            self.__date = datetime.datetime.now()

            # Extraemos los datos del fichero
            fichero = open(nombre_fichero,'r')
            lineas = fichero.readlines()
            fichero.close()

            # Los arreglamos
            for line in lineas:
                name,num,mail = line.split()
                contacto = Contacto(name,num,mail)
                lista_contactos.append(contacto)

            self.__agenda = lista_contactos

        else:
            print('Ese fichero no existe.')

    def __str__(self):
        """ Para convertir en cadena una Agenda """
        cadena = ''
        for i in range(len(self.__agenda)):
            cadena += str(self.__agenda[i])
        return cadena

    def guardar__agenda(self):
        """ Para guardar una agenda """
        fichero = open(self.__filename,'w')
        fichero.write(cadena)
        fichero.close()

    def search__name(self,name):
        """ Para buscar un contacto """
        for i in range(len(self.__agenda)):
            if self.__agenda[i].get_name() == name:
                return print(self.__agenda[i])
        print('No existe ese contacto')

    def add__contacto(self,contacto):
        """ Para añadir un contacto """
        self.__agenda.append(contacto)
        self.__date = datetime.datetime.now()

    def del__contacto(self,name):
        """ Para borrar un contacto """
        for i in range(len(self.__agenda)):
            if self.__agenda[i].__name == name:
                del(self.agenda__[i])
                self.__date = datetime.datetime.now()
        print('No existe ese contacto')


""" Comprobamos el funcionamiento de la clase Fraccion """

if __name__ == '__main__':

    Agenda1 = Agenda()
    print(Agenda1)
    Agenda1.add__contacto(Contacto('Paco','123123','paco@gmail.com'))
    print(Agenda1)
    Agenda1.add__contacto(Contacto('Manu','321321','manu@gmail.com'))
    print(Agenda1)
    Agenda1.search__name('Paco')
    Agenda1.del__contacto('Paco')