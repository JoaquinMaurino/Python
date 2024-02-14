#Lista
lista = ["Joaquin", "Mauriño", 1.80, True]
print(lista)
print(lista[0]) #Joaquin
lista[0] = "Lucas"  #Se puede modificar
print(lista[0]) #Lucas
print(lista) #['Lucas', 'Mauriño', 1.8, True]


#Las tuplas son iguales que las listas pero No se pueden modificar los elementos de manera particular
#Las tuplas si se pueden redefinir
tupla = ("Joaquin", "Mauriño", 1.80, True)
#tupla[0] = "Lucas"  => Error


#Conjunto (set) (objeto)
#Son iguales que las tuplas pero no se puede acceder a un elemento por su indice, estan desordenados
#No almacena datos duplicados
conjunto = {"Joaquin", "Mauriño", 1.80, True}
#conjunto[0] = "Lucas"  => Error
#print(conjunto[0]) => Error
#conjunto = {"Lucas"}  => Valido
conjunto = {"Joaquin", "Mauriño", 1.80, True, "Joaquin"}
print(conjunto) # output => {'Joaquin', 'Mauriño', 1.8, True}


#Diccionario = JSON
diccionario = {
    'nombre' : 'Joaquin Mauriño',
    'altura' : 1.80,
    'entrena' : True
}

print(diccionario['nombre'])  #Joaquin Mauriño
