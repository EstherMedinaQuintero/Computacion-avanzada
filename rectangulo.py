#!/usr/bin/python

from punto import Punto

class Rectangulo :
    def __init__ ( self , base , altura , origen ) :
        self.base = base
        self.altura = altura
        self.origen = origen

    def trasladar ( self , dx = 0 , dy = 0) :
        self.origen = self . origen + Punto ( dx , dy )

    def area ( self ) :
        return self.base * self.altura

    def __str__ ( self ) :
        return f'Base:{self.base},Altura:{self.altura},Esquina inf.izq.:{self.origen}'

""" Comprobamos el funcionamiento de la clase Rectangulo """

if __name__ == '__main__':

    r1 = Rectangulo (5 , 10 , Punto (0 , 0) )
    p = Punto ( -1 , 2)
    r2 = Rectangulo (25 , 100 , p )
    print ( r1 )
    print ( r2 )
    print ( r1.area () )
    print ( r2.area () )
    r1.trasladar (10 , 20)
    print ( r1 )