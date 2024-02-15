# ISP (Interface Segregation Principle)

from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass


class Humano(Trabajador,Durmiente,Comedor):
    def comer(self):
        print("El humano esta comiendo")
    def dormir(self):
        print("El humano esta durmiendo")
    def trabajar(self):
        print("El humano esta trabajando")
        
class Robot(Trabajador):
    def trabajar(self):
        print("El robot esta trabajando")
        

robot = Robot()
humano = Humano()


robot.trabajar()
humano.trabajar()
humano.comer()
humano.dormir()