#SRP (single responsability principle)

class Auto:
    def __init__(self,tanque):
        self.posicion = 0
        self.tanque = tanque
    
    def mover(self,distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia 
            self.tanque.usar_combustible(distancia / 2)
            print("has movido el auto exitosamente")

        else:
            print("no hay suficiente combustible")
            
    def obtener_posicion(self):
        return self.posicion
    
class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self,cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self,cantidad):
        self.combustible -= cantidad
        

tanque = TanqueDeCombustible()

auto = Auto(tanque)

print(auto.tanque.combustible)
print(auto.obtener_posicion())
print(auto.mover(80))
print(auto.obtener_posicion())
print(auto.mover(40))
print(auto.obtener_posicion())
print(auto.mover(90))
print(auto.obtener_posicion())

