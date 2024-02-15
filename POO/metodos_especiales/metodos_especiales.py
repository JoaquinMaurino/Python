class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self) -> str:
        return f"Persona(nombre={self.nombre},edad={self.edad})"
    
    #Con este metodo especial definimos como se comportan los objetos de la clase Persona cuando los sumo 
    def __add__(self,other):
        nuevo_valor = self.edad + other.edad
        return Persona(self.nombre+other.nombre,nuevo_valor)

joaquin = Persona("Joaquin",24)
pedro = Persona("Pedro",21)
maria = Persona("Maria",18)

nueva_persona = joaquin + pedro + maria
print(nueva_persona)
