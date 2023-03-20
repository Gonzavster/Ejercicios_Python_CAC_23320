# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 21:54:17 2023

@author: gvallejo

Ejercicio 8: Vamos a definir ahora una “Cuenta Joven”, para ello vamos a
crear una nueva clase CuantaJoven que deriva de la clase creada en el
punto 7. Cuando se crea esta nueva clase, además del titular y la cantidad
se debe guardar una bonificación que estará expresada en tanto por ciento.
Crear los siguientes métodos para la clase:
- Un constructor.
- Los setters y getters para el nuevo atributo.
- En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor
de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve
verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso
contrario.
- Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
- El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la
bonificación de la cuenta.
"""
from ejercicio6 import Persona 
from ejercicio7 import Cuenta


class CuentaJoven(Cuenta):
    def __init__(self, titular=Persona(), cantidad=0.0, bonificacion="0%"):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
    
    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self, valor):
        self._bonificacion = valor
        
    def es_titular_valido(self):
        if self._titular.edad > 18 or self._titular.edad < 25:
            return True
        else:
            return False
        
    def mostrar(self):
        print("Cuenta Joven")
        print(self._bonificacion)
        self.titular.mostrar()
        print(self.cantidad)
        return(["Cuenta Joven", self._bonificacion, self._titular.nombre, self._titular.edad, self._titular.dni, self.cantidad])
    
    def retirar(self, monto):
        if self.es_titular_valido():
            self.__cantidad = self.__cantidad + monto
            return self._cantidad
        else:
            print("El titular no es válido")