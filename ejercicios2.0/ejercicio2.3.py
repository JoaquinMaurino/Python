# creando una funcion que muestre la serie fibonacci entre 0 y el numero dado


def fibonacci(num):
    a, b = 0, 1
    fibonacci_lista = [0]
    for i in range(num + 1):
        if b > num:
            return fibonacci_lista
        else:
            fibonacci_lista.append(b)
            a, b = b, a + b


resultado = fibonacci(8)
print(resultado)
