class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def Saludar(self):
        print(f"Hola, soy {self.nombre}")

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad,trabajo,salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
    def Presentar(self):
        print(f"Soy {self.trabajo} y gano {self.salario}")
            

roberto = Empleado("Roberto", 43, "Arg", "Programador", 3000)

roberto.Saludar()
roberto.Presentar()

