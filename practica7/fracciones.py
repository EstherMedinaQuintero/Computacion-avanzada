#!/usr/bin/python

import auxiliar

class Fraccion:
    """ Clase que define una fraccion """

    # Den = 0

    def __init__(self, num=0 , den=1 ):
        """ Constructor de la clase Fraccion
        Por defecto los valores son 0/1 """
        if (type(num) and type(den)) == int:
            # a y b deben ser numéricos
            self.numerador = num
            self.denominador = den
        else:
            raise TypeError('Debes introducir números enteros')

    def __str__(self):
        """ Para mostrar la fracción """
        return f'{self.numerador}/{self.denominador}'

    def __eq__(self,other):
        """ Para comparar fracciones """
        if (self.numerador/self.denominador == other.numerador/other.denominador):
            return True
        return False

    def __ne__(self,other):
        """ Para comparar fracciones """
        if (self.numerador/self.denominador != other.numerador/other.denominador):
            return True
        return False

    def __lt__(self,other):
        """ Para comparar fracciones """
        if (self.numerador/self.denominador < other.numerador/other.denominador):
            return True
        return False

    def __le__(self,other):
        """ Para comparar fracciones """
        if (self.numerador/self.denominador <= other.numerador/other.denominador):
            return True
        return False

    def __gt__(self,other):
        """ Para comparar fracciones """
        if (self.numerador/self.denominador > other.numerador/other.denominador):
            return True
        return False

    def __ge__(self,other):
        """ Para comparar fracciones """
        if (self.numerador/self.denominador >= other.numerador/other.denominador):
            return True
        return False

    def __float__(self):
        """ Para convertir a real """
        return self.numerador/self.denominador

    def __mul__(self,other):
        """ Para multiplicar fracciones """
        return Fraccion(self.numerador*other.numerador,self.denominador*other.denominador)

    def __add__(self,other):
        """ Para sumar fracciones """
        return Fraccion(other.denominador*self.numerador+self.denominador*other.numerador,self.denominador*other.denominador)

    def __sub__(self,other):
        """ Para restar fracciones """
        return Fraccion(other.denominador*self.numerador-self.denominador*other.numerador,self.denominador*other.denominador)

    def __truediv__(self,other):
        """ Para dividir fracciones """
        return Fraccion(self.numerador*other.denominador,self.denominador*other.numerador)

    def simplificar(self):
        """ Para simplificar fracciones """
        mcd = auxiliar.mcd(self.numerador,self.denominador)
        self.numerador //= mcd
        self.denominador //= mcd

    def get_numerador(self):
        """ Metodo getter para el numerador """
        return self.numerador

    def set_numerador(self,a):
        """ Metodo setter para el numerador """
        self.numerador = a

    def get_denominador(self):
        """ Metodo getter para el denominador """
        return self.denominador

    def set_denominador(self,a):
        """ Metodo setter para el denominador """
        self.denominador = a

""" Comprobamos el funcionamiento de la clase Fraccion """

if __name__ == '__main__':
    fraccion1 = Fraccion(1,2)
    print(fraccion1)
    fraccion2 = Fraccion(2,4)
    print(fraccion2)
    print(f'Comparar (==):{fraccion1 == fraccion2}')
    print(f'Comparar (<=):{fraccion1 <= fraccion2}')
    print(f'Comparar (<):{fraccion1 < fraccion2}')
    print(f'Comparar (>=):{fraccion1 >= fraccion2}')
    print(f'Comparar (>):{fraccion1 > fraccion2}')
    print(f'Entero:{float(fraccion1)}')
    print(f'Multiplicar:{fraccion1*fraccion2}')
    print(f'Sumar:{fraccion1+fraccion2}')
    print(f'Restar:{fraccion1-fraccion2}')
    print(f'Dividir:{fraccion1/fraccion2}')
    fraccion1.simplificar()
    print(f'Simplificar:{fraccion1}')