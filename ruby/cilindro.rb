load "punto.rb"

#creamos los objetos y llamamos a sus metodos
class Cilindro < Punto
    def initialize(vRadio)
        @radio = vRadio
    end

    def getRadio()
        return @radio
    end

    def setRadio(vRadio)
        @radio = vRadio
    end

    def getAltura()
        return @altura