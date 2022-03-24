#!/usr/bin/python

import math

def mcd(a,b):
    resto = 0
    while(b > 0):
        resto = b
        b = a % b
        a = resto
    return a

def mcm(a,b):
    num1 = max(a,b)
    num2 = min(a,b)
    mcm = (num1/mcd(num1,num2))*b
    return mcm