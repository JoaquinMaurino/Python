# todo aplica para tuplas y conjuntos

animales = ["perro", "gato", "loro", "cocodrilo"]
for animal in animales:
    print(animal)


numeros = [1, 2, 3, 4]
for numero in numeros:
    print(numero)

# funcion zip() para iterar mas de una lista al mismo tiempo
for animal, numero in zip(animales, numeros):
    print(
        f"""recorriendo las listas de animales y numeros: 
Animal:{animal}
N°:{numero}"""
    )


# forma no optima de recorrer una lista con su indice:   NO FUNCIONA CON CONJUNTOS
for num in range(len(numeros)):
    print(numeros[num])

# forma correcta utilizando su indice:
for num in enumerate(numeros):
    print(num)
# esto retorna una tupla con un valor par, el indice y el valor (0, 1)

# para acceder al indice se utiliza var[0] y para el valor var[1]:
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es: {indice} y el valor es: {valor}")

# que es lo mismo que:
for i, num in enumerate(numeros):
    print(f"El indice es: {i}, y el valor: {num}")
