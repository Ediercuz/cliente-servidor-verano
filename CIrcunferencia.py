"""
Nombre:CIrcunferencia.py
Objetivo: muestra como trabajar en objetos con python
Autor:Luis David Delgado Díaz
Fecha:28 de julio de 2020
"""
import math
from Punto import Punto
class CIrcunferencia(Punto):
    #contructor
    def __init__(self, valorX, valorY, vRadio):
        #atributos de punto
        Punto.__init__(self, valorY, valorX)
        #Atributo de la circunferencia
        self.radio = vRadio

    def getRadio(self):
        return radio

    def setRadio(self, vRadio):
        self.radio = vRadio

    def getArea(self):
        return str(math.pi*math.pow(self.radio, 2))
    def toString(self):
        return Punto.toString(self)+"el valor del radio es:"+str(self.radio)+"y el area es: "+self.getArea())

 



