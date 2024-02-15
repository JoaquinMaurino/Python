class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def Llamar(self):
        print(f"Llamada iniciada desde: {self.modelo} {self.marca}")
            
    def Cortar(self):
        print("Llamada finalizada")

celular1 = Celular("Apple", "15 Pro Max", "58px")
celular2 = Celular("Samsung", "S23 Plus", "62px")

celular1.Llamar()
celular1.Cortar()