diccionario = {
    "nombre" : "Joaquin",
    "apellido" : "Mauriño",
    "snatch" : 105
}

#keys() nos devuelve un objeto dict_keys([]):
claves = diccionario.keys()
#dict_values([]):
valores = diccionario.values()

#obtener el valor de la key que pasamos:
get = diccionario.get("nombre") #no se rompe, tira none 
print(diccionario["nombre"]) #si no encuentra tira error

#eliminar todo del diccionario 
#diccionario.clear() # => {}

#eliminando un solo elemento del diccionario 
#diccionario.pop("apellido")

#obteniendo un elemento dict_items([]) iterable
diccionario_iterable = diccionario.items() # => dict_items([('nombre', 'Joaquin'), ('apellido', 'Mauriño'), ('snatch', 105)])

print(diccionario_iterable)