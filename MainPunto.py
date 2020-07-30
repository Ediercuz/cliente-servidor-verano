#Incluir el archivo de la clase

from Punto import Punto


#Creamos objetos dentro del mismo archivo
puntoA = Punto(0,0)
#invocamos metodos get
print("El valor de la coordenada X es:",puntoA.getX())
print("El valor de la coordenada Y es:",puntoA.getY())
#invocamos metodos get
puntoA.setX(23)
puntoA.setY(12)
#imprimimos los valores de los atributos del objeto puntoA
print(puntoA.toString())
#Creamos objetos dentro del mismo archivo
puntoB = Punto(-10, -20)
#invocamos metodos get
print("El valor de la coordenada X es:",puntoB.getX())
print("El valor de la coordenada Y es:",puntoB.getY())
#invocamos metodos get
puntoB.setX(10)
puntoB.setY(20)
#imprimimos los valores de los atributos del objeto puntoA
print(puntoB.toString())