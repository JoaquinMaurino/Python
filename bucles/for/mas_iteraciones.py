frutas = ["banana", "manzana", "naranja", "durazno", "pera"]
cadena = "Hola Dalto"
numeros = [2, 4, 6, 8, 10]

# evitando que se coma una naranja con la sentencia continue
for fruta in frutas:
    if fruta == "naranja":
        continue
    print(f"Voy a comer: {fruta}")

# evitar que el bucle siga ejecutandose
for fruta in frutas:
    print(f"Voy a comer: {fruta}")
    if fruta == "naranja":
        break
print("Bucle terminado")


# iterar una cadena
for letra in cadena:
    print(letra)

# duplicar numeros en una linea
numeros_duplicados = [x * 2 for x in numeros]
print(numeros_duplicados)
