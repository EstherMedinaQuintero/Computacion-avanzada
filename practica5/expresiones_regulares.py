#!/usr/bin/python
# encoding: utf-8

import re



# Primer apartado:

texto1 = '''Este es un texto de prueba 12123542D para saber
si lo de abajo 67294653-F funciona bien.'''

dnis = re.findall(r'\d{8}-?[A-Za-z]',texto1)
print(dnis)



# Segundo apartado:

texto2 = '''Este es un texto 34 de prueba 0,15 para saber
+45,03 si 982,01 lo de abajo -1,5 funciona 333.'''

decimales = re.findall(r'[+-]?\d+\.\d{3,}[^a-zA-Z]',texto2)
print(decimales)



# Tercer apartado:

texto3 = '''Este es un ejemplo (quitar eso) para saber si
(esto también) lo de abajo (23334) funciona.'''

eliminar = re.sub(r'\(.*\)','',texto3)
print(eliminar)



# Cuarto apartado

texto4 = '''Este es un texto pepito@gmail.com de prueba juanito@hotmail.com
para saber si manola.manolita@gmail.com lo de abajo funciona.'''

sin_email = re.sub(r'\S+@\S+','[email]',texto)
print(sin_email)



# Quinto apartado

texto5 = '''Este es un. Texto de prueba. Para saber si lo de abajo. Funciona.'''

salto = re.sub(r'([^\n]\. ?)([^\.])','\\1\n\\2',texto5)
print(salto)