#!/usr/bin/python3

import math


class Vector2D:
    """
    Clase que define un vector en un plano de coordenadas bidimensional.
    La clase proporcionará métodos para sumar y restar vectores, 
    para calcular el producto escalar de dos vectores, 
    para calcular el módulo de un vector y
    para comparar si dos vectores son iguales.
    """

    def __init__(self, x = 0, y = 0):
        """
        Constructor de la clase Vector2D.
        Construye un vector 2D a partir de dos coordenadas numéricas.
        Se almacenarán las coordenadas como números de tipo real.
        """
        valid_types = (int, float)
        if (type(x) in valid_types) and (type(y) in valid_types):
            self.__x = float(x)
            self.__y = float(y)
        else:
            raise TypeError("Las coordenadas introducidas deben ser números enteros o reales.")

    def get_x(self):
        """
        Devuelve la primera coordenada del vector.
        """
        return self.__x

    def get_y(self):
        """
        Devuelve la segunda coordenada del vector.
        """
        return self.__y

    def set_x(self, x):
        """
        Modifica el valor de la primera coordenada del vector.
        """
        if (type(x) in (int, float)):
            self.__x = float(x)
        else:
            raise TypeError("Las coordenadas deben ser números enteros o reales.")

    def set_y(self, y):
        """
        Modifica el valor de la segunda coordenada del vector.
        """
        if (type(y) in (int, float)):
            self.__y = float(y)
        else:
            raise TypeError("Las coordenadas deben ser números enteros o reales.")

    def __str__(self):
        """
        Convierte un vector bidimensional en una cadena de caracteres.
        """
        return f'({self.__x}, {self.__y})'

    def __eq__(self, other):
        """
        Compara si dos vectores son iguales.
        Devuelve True si las dos coordenadas de los vectores coinciden.
        """
        if (self.get_x() == other.get_x()) and (self.get_y() == other.get_y()):
            return True
        return False

    def __add__(self, other):
        """
        Sobrecarga el operador + para devolver la suma de dos vectores.
        >>> str(Vector2D(1, 5) + Vector2D(2, 3))
        '(3.0, 8.0)'
        """
        return Vector2D(self.get_x() + other.get_x(), self.get_y() + other.get_y())

    def __sub__(self, other):
        """
        Sobrecarga el operador - para devolver la resta de dos vectores.
        """
        return Vector2D(self.get_x() - other.get_x(), self.get_y() - other.get_y())

    def __mul__(self, other):
        """
        Sobrecarga el operador * para calcular el producto escalar de dos vectores.
        Devuelve un float como resultado.
        >>> Vector2D(1, 5) * Vector2D(2, 3)
        17.0
        """
        return (self.get_x() * other.get_x()) + (self.get_y() * other.get_y())

    def __abs__(self):
        """
        Calcula el módulo de un vector.
        Devuelve un float.
        >>> abs(Vector2D(1, 2))
        2.23606797749979
        """
        return math.sqrt((self.__x * self.__x) + (self.__y * self.__y))


# Codigo para comprobar el funcionamiento de la clase vector2D
if __name__ == '__main__':
    import doctest
    doctest.testmod()

