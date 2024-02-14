class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def NameAge(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}")

class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado
    
    def Course(self):
        print(f"Course: {self.grado}")


estudiante1 = Estudiante("Pepe", 16, "3ero")

estudiante1.NameAge()
estudiante1.Course()