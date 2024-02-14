class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):   #geter => funcion que accede a un atributo privado
        return self.__nombre

    @nombre.setter     #setter => funcion que modifica un atributo privado
    def nombre(self,new_nombre):
        self.__nombre = new_nombre
    
    @nombre.deleter
    def nombre(self):
        del self.__nombre
        

dalto = Persona("Lucas", 21)

# nombre = dalto.nombre

# print(nombre) #Lucas

# dalto.nombre = "Joaquin"

# print(dalto.nombre) #Joaquin

# del dalto.nombre

# print(dalto.nombre)