#!/usr/bin/python

import copy

class Punto:
    # """ Clase que define un punto en el plano """
    # def __init__(self,x = 0,y = 0):
        # """ Constructor 1 de la clase Punto """
        # self.x = x
        # self.y = y

    # def __init__(self, x=0 , y=0 ):
        # """ Constructor 2 de la clase Punto """
        # if isinstance(x,(int,float)) and isinstance(y,(int,float)):
            # Las coordenadas de x e y deben ser numéricas
            # self.x = x
            # self.y = y
        # else:
            # raise TypeError('Las coordenadas x e y deben ser numericas')

    def __init__(self, x=0 , y=0 ):
        """ Constructor 3 de la clase Punto """
        if (type(x) in (float,int)) and (type(y) in (float,int)):
            # Las coordenadas de x e y deben ser numéricas
            self.x = x
            self.y = y
        else:
            raise TypeError('Las coordenadas x e y deben ser numericas')


    # """ Código 1 para comprobar el funcionamiento del modulo """

    # p = Punto(1,2)
    # print(f'({p.x},{p.y})')

    # q = Punto(3)
    # print(f'({q.x},{q.y})')

    # r = Punto()
    # print(f'({r.x},{r.y})')

    # s = Punto(y=2,x=1)
    # print(f'({s.x},{s.y})')

    # """ Código 2 para comprobar el funcionamiento del modulo """

    # if __name__ == '__main__':
        # p = Punto(1,2)
        # print(f'({p.x},{p.y})')

        # q = Punto(3)
        # print(f'({q.x},{q.y})')

        # r = Punto()
        # print(f'({r.x},{r.y})')

        # s = Punto(y=2,x=1)
        # print(f'({s.x},{s.y})')

    def __str__(self):
        """ Metodo para convertir un punto a cadena """
        return f'({self.x},{self.y})'

    def __eq__(self,other):
        """ Metodo para comparar dos objetos de tipo Punto """
        if (self.x == other.x) and (self.y == other.y):
            return True
        return False

    def __ne__ ( self , other ):
        return not ( self == other )

    def __copy__(self):
        """ Metodo para hacer una copia del objeto """
        return Punto ( self.x , self.y )

    def __add__(self,other):
        return Punto(self.x + other.x, self.y + other.y)

""" Código 4 para comprobar el funcionamiento del modulo """

if __name__ == '__main__':
    p = Punto (3 , 4)
    q = Punto (3 , 4)
    r = p
    print ( p == q )
    p.x = 0
    print ( p == q )
    print ( p == r )
    print ( p )
    print ( r )


    # """ Código 3 para comprobar el funcionamiento del modulo """

    # if __name__ == '__main__':
        # p = Punto(1,2)
        # print(p)

        # q = Punto(3)
        # print(q)

        # r = Punto()
        # print(r)

        # s = Punto(y = 2)
        # print(s)
