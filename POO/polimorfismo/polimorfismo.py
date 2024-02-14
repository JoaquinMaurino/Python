class Gato:
    def Sonido(self):
        return "Miau"

class Perro:
    def Sonido(self):
        return "Guau"

def HacerSonido(animal):
    print(animal.Sonido())    

gato = Gato()
perro = Perro()

HacerSonido(gato) 
HacerSonido(perro) 

