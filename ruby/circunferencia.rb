# Clase que muestra la herencia de ruby

load "punto.rb"


class Circunferencia < Punto

    def initialize(vRadio)
        @radio = vRadio
    end

    def getRadio()
        return @radio
    end

    def setRadio(vRadio)
        @radio = vRadio
    end

    # Escribir un metodo que calcule el area de la circunfera

end

cir = Circunferencia.new(3)

puts "El radio es: #{cir.getRadio()}"
# Invocamos Métodos de la clase Punto
cir.setX(10)
cir.setY(10)
puts "Las Coordenadas: #{cir.getX()}, #{cir.getY}"

def area(vRadio)
    return Math::PI*(vRadio**2)
end

end

cir = Circunferencia.new(6)
puts"el radio es: #{cir.getr}"
#invocamos metodos de los puntos
cir.setx(10)
cir.sety(5)
puts "las coordenadas: #{cir.getx}, #{cir.gety}"
puts "el area es: #{cir.area(cir.getr)}"