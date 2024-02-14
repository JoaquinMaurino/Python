frase = input("Ingresa una frase y te calculo cuanto tardarias diciendolo: ")

palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)


if cantidad_de_palabras > 120:
    print("Para flaco tampoco te pedi un testamento")

print(
    f"Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras / 2} segundos en decirlo"
)
print(f"Por otra parte, Dalto tardaria {cantidad_de_palabras / 2 / 1.3} segundos")
