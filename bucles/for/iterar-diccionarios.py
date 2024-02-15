diccionario = {"nombre": "Joaquin", "apellido": "Mauriño", "edad": 23}

# recorriendo diccionario para obtener solo las claves
for key in diccionario:
    print(key)

# recorriendo diccionario con items para obtener clave y valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"Clave: {key}, Valor: {value}")
