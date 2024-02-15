class Personaje:
    def __init__(self,nombre,fuerza,velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    
    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"

    def __add__(self,other):
        nuevo_nombre = self.nombre + "-" + other.nombre
        nueva_fuerza = round(((self.fuerza + other.fuerza)/2)**1.2)
        nueva_velocidad = round(((self.velocidad + other.velocidad)/2)**1.2)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)


goku = Personaje("Goku", 100, 100)
vegeta = Personaje("Vegeta", 98, 105)
gogeta = goku + vegeta
print(goku)
print(vegeta)
print(gogeta)