"""
Nombre:Cilindro.py
Objetivo: muestra como trabajar en objetos con python
Autor:Luis David Delgado Díaz
Fecha:28 de julio de 2020
"""

from Circunferencia import Circunferencia
class Cilindro(CIrcunferencia):

    #definimos el constructor
    def __init__(self, valorX, valorY, valorRadio, valorArea):
        #constructor de circunferencia
        Circunferencia.__init__(self, valorRadio)
        #contructor de cilindro
        self.altura = valorAltura
    
    def getAltura(self):
        return self.altura

    def setAltura(selg, valorAltura):
        self.altura = valorAltura

    def toString(self):
        return CIrcunferencia.toString(self)+"y la altura es: "+str(self.altura)+"el volumen es: "+self.getVolumen()


    def getVolumen(self):
        return str(Circunferencia.getArea(self) * self.getAltura())


    c=Cilindro(2,3,4,7)
    print(c.toString())