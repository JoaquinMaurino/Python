#forma NO optima de sumar valores
""" def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados

resultado = suma([5,4,6]) """

#forma optima de sumar valores:
#utilizo el parametro ARGS => * y el parametro que quiera
#si quiero pasar mas parametros aparte del args, deben ir antes, args es el ultimo
def suma(*numeros):
    return sum(numeros)

resultado = suma(5,4,6)
print(resultado)
#--------------------------------
def suma_con_nombre(nombre,*numeros):
    return f"Hola {nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado = suma_con_nombre("Joaquin",5,4,100,6)
print(resultado)