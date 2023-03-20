# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 21:53:52 2023

@author: gvallejo

Ejercicio 7: Crea una clase llamada Cuenta que tendrá los siguientes
atributos: titular (que es una persona) y cantidad (puede tener decimales).
El titular será obligatorio y la cantidad es opcional. Crear los siguientes
métodos para la clase:
- Un constructor, donde los datos pueden estar vacíos.
- Los setters y getters para cada uno de los atributos. El atributo no se
puede modificar directamente, sólo ingresando o retirando dinero.
- mostrar(): Muestra los datos de la cuenta.
- ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad
introducida es negativa, no se hará nada.
- retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede
estar en números rojos.
"""
from ejercicio6 import Persona

class Cuenta:
    def __init__(self, titular=Persona(), cantidad=0.0):
        self.titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self): 
        return self._titular
    
    @property
    def cantidad(self): 
        return self._cantidad
      
    @titular.setter
    def titular(self, value):
        self._titular = value
        
    @cantidad.setter
    def __cantidad(self, value):
        self._cantidad = value
      
    def mostrar(self):
        self.titular.mostrar()
        print(self.__cantidad)
        return([self._titular.nombre, self._titular.edad, self._titular.dni, self.__cantidad])
        
    def ingresar(self, monto):
        self.__cantidad = self.__cantidad + monto
        return self._cantidad
     
    def retirar(self, monto):
        self.__cantidad = self.__cantidad - monto
        return self._cantidad