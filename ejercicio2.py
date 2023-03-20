# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 21:48:35 2023

@author: gvallejo

Ejercicio 2: Escribir una función que calcule el mínimo común múltiplo
entre dos números
"""
from ejercicio1 import mcd

def mcm(first, second):
    """
    Función que calcula minimo comun multiplo de dos números (mcm)

    Parameters
    ----------
    first : integer
        Primer valor  para calcular mcm.
    second : integer
        Segundo valor  para calcular mcm.

    Returns
    -------
    i: integer
        Minimo Comun Multiplo de first y second.
    """
    mcmult = float(first*second)/float(mcd(first, second))
    return int(mcmult)