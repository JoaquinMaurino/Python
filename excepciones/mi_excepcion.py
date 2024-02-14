#creando mi propia excepcion
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Cometiste el siguiente error: {err}")

#lanzando mi propia excepcion
#raise MiExcepcion("Le pifiaste")

#manejandola
try:
    raise MiExcepcion("Le pifiaste")
except:
    print("Como vas a cometer ese error")

