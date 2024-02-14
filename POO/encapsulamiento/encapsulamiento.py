class MiClase:
    def __init__(self):
        self._atributo_privado = "Valor" #1 _ privado
        self.__atributo_privado = "Valor" #2 __ muy privado

    def _MetodoPrivado(self):
        print("Accion")
    
    def __MetodoMuyPrivado(self):
        print("Accion")
    
objeto = MiClase()
print(objeto.__atributo_privado)
objeto.__MetodoMuyPrivado()