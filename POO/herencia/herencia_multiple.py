class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def Saludar(self):
        print(f"Hola, soy {self.nombre}")


class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
        
    def MostrarHabilidad(self):
        return f"{self.habilidad}"


class EmpleadoArtistico(Persona,Artista):
    def __init__(self, nombre,edad,nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa

    #Para crear un metodo que utilice metodos de las clases padre, en vez de usar self.metodo usamos super().metodo:
    def Presentar(self):
        print(f"Hola soy {self.nombre}, mi habilidad es {super().MostrarHabilidad()} y trabajo en {self.empresa}")
        
empleado_artistico1 = EmpleadoArtistico("Pepe", 24, "arg", "bailar", 5400, "telecom")
#empleado_artistico1.Presentar()

herencia1 = issubclass(EmpleadoArtistico,Persona) #True
herencia2 = issubclass(EmpleadoArtistico,Artista) #True
herencia3 = issubclass(Artista,Persona) #False

instancia1 = isinstance(empleado_artistico1,EmpleadoArtistico) #True
instancia2= isinstance(empleado_artistico1,Persona) #True
instancia3 = isinstance(empleado_artistico1,Artista) #True

#print(EmpleadoArtistico.mro())