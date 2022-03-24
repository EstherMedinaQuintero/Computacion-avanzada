#!/usr/bin/python3
# encoding: utf-8

import unittest
import math


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
        """
        return self.__a

    def get_b(self):
        """
        Devuelve la segunda componente del complejo.
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
        """
        if self.__b >= 0:
            return '(' + str(self.__a) + ' +' + str(self.__b) + 'i)'
        else:
            return '(' + str(self.__a) + ' ' + str(self.__b) + 'i)'

    def __eq__(self, other):
        """
        Compara si dos complejos son iguales.
        Devuelve True si las dos componentes de los vectores coinciden.
        """
        if (self.get_a() == other.get_a()) and (self.get_b() == other.get_b()):
            return True
        return False

    def __add__(self, other):
        """
        Sobrecarga el operador + para devolver la suma de dos complejos.
        """
        return Complejo(self.get_a() + other.get_a(), self.get_b() + other.get_b())

    def __sub__(self, other):
        """
        Sobrecarga el operador - para devolver la resta de dos complejos.
        """
        return Complejo(self.get_a() - other.get_a(), self.get_b() - other.get_b())

    def __mul__(self, other):
        """
        Sobrecarga el operador * para calcular el producto de dos complejos.
        Devuelve un complejo
        """
        return Complejo((self.get_a() * other.get_a() - self.get_b() * other.get_b()), 
                        (self.get_a() * other.get_b() + self.get_b() * other.get_a()))

    def __abs__(self):
        """
        Calcula el módulo de un complejo.
        Devuelve un float.
        """
        return math.sqrt((self.get_a() * self.get_a()) + (self.get_b() * self.get_b()))

    def conjugado(self):
        """
        Calcula el conjugado de un complejo.
        Devuelve un complejo.
        """
        return Complejo(self.get_a(),-self.get_b())


# Codigo para comprobar el funcionamiento de la clase Complejo
if __name__ == "__main__":

    c1 = Complejo()
    print(c1)
    c2 = Complejo(5)
    print(c2)
    c3 = Complejo(1, 2)
    print(c3)
    c4 = Complejo(1.5, 2.357)
    print(c4)
    print(c1.get_a())
    print(c1.get_b())
    print(c1 + c2)
    print(c2 - c3)
    print(c2 * c3)
    print(c3.conjugado())
    print(abs(c3))

class TestComplejo(unittest.TestCase):

    def setUp(self):
        pass

    def test_init_default1(self):
        c1 = Complejo()
        self.assertEqual(c1.get_a(), 0.0)
        self.assertEqual(c1.get_b(), 0.0)

    def test_init_default2(self):
        c2 = Complejo(5)
        self.assertEqual(c2.get_a(), 5.0)
        self.assertEqual(c2.get_b(), 0.0)

    def test_getter_a(self):
        c3 = Complejo(1, 2)
        self.assertIsInstance(c3.get_a(), float)

    def test_getter_b(self):
        c3 = Complejo(1, 2)
        self.assertIsInstance(c3.get_b(), float)

    def test_setter_a(self):
        c3 = Complejo(1, 2)
        c3.set_a(5)
        self.assertEqual(c3.get_a(), float(5))

    def test_setter_b(self):
        c3 = Complejo(1, 2)
        c3.set_b(5)
        self.assertEqual(c3.get_b(), float(5))

    def test_str(self):
        self.assertEqual(str(Complejo(1.5, 2.357)), '(1.5 +2.357i)')

    def test_add(self):
        c1 = Complejo(1, 5.5)
        c2 = Complejo(2.0, 2.5)
        c3 = Complejo(-1, -1)
        self.assertEqual(c1 + c2, Complejo(3, 8))
        self.assertEqual(c1 + c3, Complejo(0, 4.5))

    def test_sub(self):
        c1 = Complejo(1, 5.5)
        c2 = Complejo(2.0, 2.5)
        c3 = Complejo(-1, -1)
        self.assertEqual(c1 - c2, Complejo(-1, 3))
        self.assertEqual(c1 - c3, Complejo(2, 6.5))

    def test_mul(self):
        c1 = Complejo(1, 5)
        c2 = Complejo(2, 3)
        self.assertEqual(c1 * c2, Complejo(-13,13))

    def test_abs(self):
        c1 = Complejo(1, 2)
        self.assertEqual(abs(c1), float((1+4)**(1/2)))

# Codigo para comprobar el funcionamiento de la clase vector2D
if __name__ == '__main__':
    unittest.main()