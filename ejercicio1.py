# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 21:28:38 2023

@author: gvallejo

Ejercicio 1: Escribir una función que calcule el máximo común divisor
entre dos números.
"""

def mcd(first, second):
    """
    Función que calcula maximo comun divisor de dos números (mcd)

    Parameters
    ----------
    first : integer
        Primer valor  para calcular mcd.
    second : integer
        Segundo valor  para calcular mcd.

    Returns
    -------
    i : integer
        Maximo Común Divisor de first y second.
    """
    
    if first > second:
        for i in range(second, 0, -1):
            if second % i == 0 and first % i == 0:
                return i
    else:
        for i in range(first, 0, -1):
            if first % i == 0 and second % i == 0:
                return i