#crear clase estudiante, con atributos nombre, edad y grado, metodo estudiar() que diga "el estudiante {nombre} esá estudiando". Se debe interactuar con el usuario y este debe brindar los atributos

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def Estudiar(self):
        print(f"{self.nombre} está estudiando...")

nombre = input(f"Ingresar nombre: ")
edad = input(f"Ingresar edad: ")
grado = input(f"Ingresar grado: ")

estudiante1 = Estudiante(nombre, edad, grado)

print(f""" 
      Datos del estudiante: \n
      ----------------------\n
      Nombre: {estudiante1.nombre}\n
      Edad: {estudiante1.edad}\n
      Grado: {estudiante1.grado}""")

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante1.Estudiar()
        break

