# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 21:51:16 2023

@author: gvallejo

Ejercicio 4: Escribir una función que reciba una cadena de caracteres
y devuelva un diccionario con cada palabra que contiene y la cantidad
de veces que aparece (frecuencia). Escribir otra función que reciba el
diccionario generado con la función anterior y devuelva una tupla con
la palabra más repetida y su frecuencia.
"""

def most_frequent(words_dict):
    """
    Parameters
    ----------
    words_dict : dictionary
        Diccionario con cada palabra única como key y la
        fecuencia con la que aparece como valor

    Returns
    -------
    max_kv : touple
        Tupla con la palabra más repetida y su frecuencia.
    """
    
    wd = words_dict
    max_key = max(wd, key=wd.get)
    max_value = wd[max_key]
    max_kv = (max_key, max_value)
    return max_kv