#len() devuelve cantidad de elementos de una lista

lista = ["Joaquin", 23, 1.80, True]

cantidad_de_elementos = len(lista)

#AGREGANDO ELEMENTOS:
#con append se modifica directamente la lista original, no en una variable
lista.append("Crossfit")

#con insert se agrega en un indice especifico
lista.insert(1, "Mauriño")

#con extend se agregan varios elementos a la lista, en formato lista
lista.extend(["snatch", "clean"])

#ELIMINANDO ELEMENTOS:
#pop elimina un elemento por su indice, si le pasamos -1 como parametro elimina el ultimo elemento, si le pasamos -2 elimina el anteultimo y etc.
lista.pop(4)

#remove elimina un elemento por su valor
lista.remove("clean")

#clear elimina todos los elementos de la lista
#lista.clear()


#ORDENANDO ELEMENTOS
#sort ordena la lista de forma ascendente pero solo valores numericos y booleanos
""" lista.sort()
lista.sort(reverse=True) con reverse es descendente"""

#reverse invierte los elementos sin importar su orden original
lista.reverse()

#index retorna el indice del elemento que buscamos 
index_of = lista.index("Joaquin")

print(index_of)