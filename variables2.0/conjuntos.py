# creando un conjunto con set
conjunto = set(["dato1", "dato2"])

# metiendo un conjunto dentro de otro:
conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1, "dato3"}
# hay que usar la funcion frozenset([])


# sub y super conjuntos
conjunto1 = {1, 3, 5, 7, 9, 11}
conjunto2 = {3, 7, 11}

# verificando si es un subconjunto
resultado1 = conjunto2.issubset(conjunto1)  # true
resultado2 = conjunto2 <= conjunto1  # true

# verificando si es un superconjunto
resultado3 = conjunto1.issuperset(conjunto2)  # true
resultado4 = conjunto1 >= conjunto2  # true

print(resultado1, resultado2, resultado3, resultado4)
