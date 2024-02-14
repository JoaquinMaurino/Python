class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):   #geter => funcion que accede a un atributo privado
        return self.__nombre
    
    def set_nombre(self,new_name):
        self.__nombre = new_name

dalto = Persona("Lucas", 21)

nombre = dalto.get_nombre()
print(nombre)
new_name = dalto.set_nombre("Joaquin")
print(dalto.get_nombre())