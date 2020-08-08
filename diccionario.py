"""
Nombre: diccionario.py
Objetivo: Muestra la operación de los diccionarios en python
Autor: Luis David Delgado
Fecha: 05/08/2020
"""

def main():
    #Creamos un diccionario con distintos key y datos
    print("===========================")
    dic = {'clave':20082133, 'nombre':'Luis David Delgado Díaz', 'edad':21, 'cursos':['Python', 'Progra Web', 'IA']}
    #Listar items del diccionario
    print("Los items son: ", dic)
    #Imprimir un item de un diccionario proporcionando su key
    print("===========================")
    print("El valor de la key es: ", dic['nombre'])
    #Imprimir los valores de todas las keys del diccionario
    print("===========================")
    for i in dic:
        print(i, ":", dic[i])
    
    #En el caso de la lista incluidas como un item del diccionario, lo accesamos
    print("===========================")
    for i in dic['cursos']:
        print(i)

    #Investigar los métodos los diccionarios y correrlos en el programa.
    """
    get, pop, key, clean, items, update
    """


if __name__ == "__main__":
    main()