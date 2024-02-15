class Animal:
    def Comer(self):
        print("El animal esta comiendo")


class Mamifero(Animal):
    def Amamantar(self):
        print("El animal esta amamantando")



class Ave(Animal):
    def Volar(self):
        print("El animal esta volando")


class Murcielago(Mamifero,Ave):
    pass


murcielago = Murcielago()

murcielago.Amamantar()
murcielago.Volar()
murcielago.Comer()

print(Murcielago.mro())