class Punto():
    #definir una especie de constructor
    def __init__(self, valorX, valorY):
        #definimos el nombre de los atributos del objeto
        self.x = valorX
        self.y = valorY
    #lista de metodos get
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setX(self, valorX):
        #asignar el argumento al atributo del objeto
        self.x = valorX

    def setY(self, valorY):
        self.y = valorY

    #metodo toString: regresa los valores de los atributos x,y
    def toString(self):
        return "las coordenadas X,Y del punto son: ",str(self.getX())+","+str(self.getY())


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

