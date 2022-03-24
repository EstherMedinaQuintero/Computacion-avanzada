#!/usr/bin/python3
# encoding: utf-8

import math

# Faltan los >>>

class Complejo:
    """
    Clase que define un numero complejo con dos componentes.
    La clase proporcionará métodos para sumar y restar complejos, 
    para calcular el producto de dos complejos, 
    para calcular el módulo de un complejo y
    para comparar si dos complejos son iguales.
    """

    def __init__(self, a = 0, b = 0):
        """
        Constructor de la clase Complejo.
        Construye un complejo con dos componentes numéricas.
        Se almacenarán las componentes como números reales.
        """
        valid_types = (int, float)
        if (type(a) in valid_types) and (type(b) in valid_types):
            self.__a = float(a)
            self.__b = float(b)
        else:
            raise TypeError("Las componentes del numero deben ser números enteros o reales.")

    def get_a(self):
        """
        Devuelve la primera componente del complejo.
        >>> c = Complejo(2,3)
        >>> c.get_a()
        2.0
        """
        return self.__a

    def get_b(self):
        """
        Devuelve la segunda componente del complejo.
        >>> c = Complejo(2,3)
        >>> c.get_b()
        3.0
        """
        return self.__b

    def set_a(self, a):
        """
        Modifica el valor de la primera componentes del complejo.
        """
        if (type(a) in (int, float)):
            self.__a = float(a)
        else:
            raise TypeError("Las componentes del complejo deben ser números enteros o reales.")

    def set_b(self, b):
        """
        Modifica el valor de la segunda componente del complejo.
        """
        if (type(b) in (int, float)):
            self.__b = float(b)
        else:
            raise TypeError("Las componentes del complejo deben ser números enteros o reales.")

    def __str__(self):
        """
        Convierte un complejo en una cadena de caracteres.
        >>> c = Complejo(2,3)
        >>> print(c)
        (2.0 +3.0i)
        """
        if self.__b >= 0:
            return '(' + str(self.__a) + ' +' + str(self.__b) + 'i)'
        else:
            return '(' + str(self.__a) + ' ' + str(self.__b) + 'i)'

    def __eq__(self, other):
        """
        Compara si dos complejos son iguales.
        Devuelve True si las dos componentes de los vectores coinciden.
        >>> c1 = Complejo(2,3)
        >>> c2 = Complejo(4,3)
        >>> c1 == c2
        False
        """
        if (self.get_a() == other.get_a()) and (self.get_b() == other.get_b()):
            return True
        return False

    def __add__(self, other):
        """
        Sobrecarga el operador + para devolver la suma de dos complejos.
        >>> c1 = Complejo(2,3)
        >>> c2 = Complejo(4,3)
        >>> c3 = c1 + c2
        >>> print(c3)
        (6.0 +6.0i)
        """
        return Complejo(self.get_a() + other.get_a(), self.get_b() + other.get_b())

    def __sub__(self, other):
        """
        Sobrecarga el operador - para devolver la resta de dos complejos.
        >>> c1 = Complejo(2,3)
        >>> c2 = Complejo(4,3)
        >>> c3 = c1 - c2
        >>> print(c3)
        (-2.0 +0.0i)
        """
        return Complejo(self.get_a() - other.get_a(), self.get_b() - other.get_b())

    def __mul__(self, other):
        """
        Sobrecarga el operador * para calcular el producto de dos complejos.
        Devuelve un complejo
        >>> c1 = Complejo(2,3)
        >>> c2 = Complejo(4,3)
        >>> c3 = c1 * c2
        >>> print(c3)
        (-1.0 +18.0i)
        """
        return Complejo((self.get_a() * other.get_a() - self.get_b() * other.get_b()), 
                        (self.get_a() * other.get_b() + self.get_b() * other.get_a()))

    def __abs__(self):
        """
        Calcula el módulo de un complejo.
        Devuelve un float.
        >>> c1 = Complejo(1,2)
        >>> b = str(abs(c1))
        >>> a = str(float((1+4)**(1/2)))
        >>> a == b
        True
        """
        return math.sqrt((self.get_a() * self.get_a()) + (self.get_b() * self.get_b()))

    def conjugado(self):
        """
        Calcula el conjugado de un complejo.
        Devuelve un complejo.
        >>> c1 = Complejo(1,2)
        >>> c1.conjugado()
        (1.0 -2.0i)
        """
        return Complejo(self.get_a(),-self.get_b())


# Codigo para comprobar el funcionamiento de la clase vector2D
if __name__ == '__main__':
    import doctest
    doctest.testmod()