# creando una funcion lambda para multiplicar por dos:
multiplicar_po_dos = lambda x: x * 2

# ---------------------------------------

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# creando una funcion comun que diga si es par o no


def es_par(num):
    if num % 2 == 0:
        return True


def es_impar(num):
    if num % 2 == 1:
        return True


# usando filter (build-in) con una funcion comun

numeros_pares = filter(es_par, numeros)
numeros_impares = filter(es_impar, numeros)

print(list(numeros_pares))
print(list(numeros_impares))

# creando lo mismo con una funcion lambda:

numeros_pares_lambda = filter(lambda x: x % 2 == 0, numeros)
numeros_impares_lambda = filter(lambda x: x % 2 == 1, numeros)

print(list(numeros_pares_lambda))
print(list(numeros_impares_lambda))
