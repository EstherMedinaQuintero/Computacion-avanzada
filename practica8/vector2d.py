#!/usr/bin/python3
# encoding: utf-8

import unittest
import math


class Vector2D:
    """
    Clase que define un vector con dos componentes.
    La clase proporcionará métodos para sumar y restar vectores, 
    para calcular el producto escalar de dos vectores, 
    para calcular el módulo de un vector y
    para comparar si dos vectores son iguales.
    """

    def __init__(self, x = 0, y = 0):
        """
        Constructor de la clase Vector2D.
        Construye un vector con dos componentes numéricas.
        Se almacenarán las componentes como números reales.
        """
        valid_types = (int, float)
        if (type(x) in valid_types) and (type(y) in valid_types):
            self.__x = float(x)
            self.__y = float(y)
        else:
            raise TypeError("Las componentes del vector deben ser números enteros o reales.")

    def get_x(self):
        """
        Devuelve la primera componente del vector.
        """
        return self.__x

    def get_y(self):
        """
        Devuelve la segunda componente del vector.
        """
        return self.__y

    def set_x(self, x):
        """
        Modifica el valor de la primera componentes del vector.
        """
        if (type(x) in (int, float)):
            self.__x = float(x)
        else:
            raise TypeError("Las componentes del vector deben ser números enteros o reales.")

    def set_y(self, y):
        """
        Modifica el valor de la segunda componente del vector.
        """
        if (type(y) in (int, float)):
            self.__y = float(y)
        else:
            raise TypeError("Las componentes del vector deben ser números enteros o reales.")

    def __str__(self):
        """
        Convierte un vector bidimensional en una cadena de caracteres.
        """
        return '(' + str(self.__x) + ', ' + str(self.__y) + ')'

    def __eq__(self, other):
        """
        Compara si dos vectores son iguales.
        Devuelve True si las dos componentes de los vectores coinciden.
        """
        if (self.get_x() == other.get_x()) and (self.get_y() == other.get_y()):
            return True
        return False

    def __add__(self, other):
        """
        Sobrecarga el operador + para devolver la suma de dos vectores.
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
        Devuelve un float
        """
        return (self.get_x() * other.get_x()) + (self.get_y() * other.get_y())

    def __abs__(self):
        """
        Calcula el módulo de un vector.
        Devuelve un float.
        """
        return math.sqrt((self.__x * self.__x) + (self.__y * self.__y))


# Codigo para comprobar el funcionamiento de la clase vector2D
if __name__ == "__main__":

    v1 = Vector2D()
    print(v1)
    v2 = Vector2D(5)
    print(v2)
    v3 = Vector2D(1, 2)
    print(v3)
    v4 = Vector2D(1.5, 2.357)
    print(v4)
    # v5 = Vector2D(1.5, 2.357)
    # print(v5)
    print(v1.get_x())
    print(v1.get_y())

class TestVector2D(unittest.TestCase):

    def setUp(self):
        # self.v1 = Vector2D()
        # ...
        pass

    def test_init_default1(self):
        v1 = Vector2D()
        self.assertEqual(v1.get_x(), 0.0)
        self.assertEqual(v1.get_y(), 0.0)

    def test_init_default2(self):
        v2 = Vector2D(5)
        self.assertEqual(v2.get_x(), 5.0)
        self.assertEqual(v2.get_y(), 0.0)

    def test_getter_x(self):
        v3 = Vector2D(1, 2)
        self.assertIsInstance(v3.get_x(), float)

    def test_getter_y(self):
        v3 = Vector2D(1, 2)
        self.assertIsInstance(v3.get_y(), float)

    def test_setter_x(self):
        v3 = Vector2D(1, 2)
        v3.set_x(5)
        self.assertEqual(v3.get_x(), float(5))

    def test_setter_y(self):
        v3 = Vector2D(1, 2)
        v3.set_y(5)
        self.assertEqual(v3.get_y(), float(5))

    def test_str(self):
        self.assertEqual(str(Vector2D(1.5, 2.357)), '(1.5, 2.357)')

    def test_add(self):
        v1 = Vector2D(1, 5.5)
        v2 = Vector2D(2.0, 2.5)
        v3 = Vector2D(-1, -1)
        self.assertEqual(v1 + v2, Vector2D(3, 8))
        self.assertEqual(v1 + v3, Vector2D(0, 4.5))

    def test_sub(self):
        v1 = Vector2D(1, 5.5)
        v2 = Vector2D(2.0, 2.5)
        v3 = Vector2D(-1, -1)
        self.assertEqual(v1 - v2, Vector2D(-1, 3))
        self.assertEqual(v1 - v3, Vector2D(2, 6.5))

    def test_mul(self):
        v1 = Vector2D(1, 5)
        v2 = Vector2D(2, 3)
        self.assertEqual(v1 * v2, float(17))

    def test_abs(self):
        v1 = Vector2D(1, 2)
        self.assertEqual(abs(v1), float((1+4)**(1/2)))


# Codigo para comprobar el funcionamiento de la clase vector2D
if __name__ == '__main__':
    unittest.main()
