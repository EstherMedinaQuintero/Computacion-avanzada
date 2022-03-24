#!/usr/bin/python

class Contacto:
    """ Clase que define un contacto """

    def __init__(self,name,num,mail):
        """ Constructor de la clase Contacto """
        self.__name = name
        self.__num = num
        self.__mail = mail

    def __str__(self):
        """ Convierte a cadena un contacto """
        return f'{self.__name} {self.__num} {self.__mail}'

    def __eq__(self,other):
        """ Compara dos contactos """
        if (self.__name == other.__name) and (self.__num == other.__num) and (self.__mail == other.__mail):
            return True
        return False

    # def __lt__(self,other):
        # """ Compara dos contactos """
        # if (self.__name).lower < (other.__name).lower:
            # return True
        # return False

    # def __gt__(self,other):
        # """ Compara dos contactos """
        # if (self.__name).lower > (other.__name).lower:
            # return True
        # return False

    def get_name(self):
        """ Metodo getter para el nombre """
        return self.__name

    def get_num(self):
        """ Metodo getter para el numero """
        return self.__num

    def get_mail(self):
        """ Metodo getter para el mail """
        return self.__mail

    def set_name(self,newname):
        """ Metodo setter para el nombre """
        self.__name = newname

    def set_num(self,newnum):
        """ Metodo setter para el numero """
        self.__num = newnum

    def set_mail(self,newmail):
        """ Metodo setter para el mail """
        self.__mail = newmail

""" Comprobamos el funcionamiento de la clase Contacto """

if __name__ == '__main__':
    Paco = Contacto('Paco','123123','paco@gmail.com')
    Manu = Contacto('Manu','321321','manu@gmail.com')
    print(Paco)
    print(Manu)
    print(f'Comparar (==) :{Paco==Manu}')
    # print(f'Comparar (<) : {Paco<Manu}')
    # print(f'Comparar (>) : {Paco>Manu}')
    print(Paco.get_name())
    print(Paco.get_num())
    print(Paco.get_mail())