# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 21:49:43 2023

@author: gvallejo

Ejercicio 3: Escribir un programa que reciba una cadena de caracteres
y devuelva un diccionario con cada palabra que contiene y la cantidad
de veces que aparece (frecuencia)
"""

def word_counter(sentence):
    """
    Función que toma una frase, arma una lista con todas
    sus palabras y luego la recorre y arma un diccionario
    con cada palabra única como key y la fecuencia con la
    que aparece como valor

    Parameters
    ----------
    sentence : string
        Frase para dividir.

    Returns
    -------
    words_dict : dictionary
        dictionary[word] = word count.
    """
    words_dict = {}
    words = sentence.split()
    for word in words:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] = words_dict[word] + 1
    return words_dict