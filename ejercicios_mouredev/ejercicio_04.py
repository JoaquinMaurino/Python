"""  
            NUMEROS PRIMOS
* Escribe un programa que se encargue de comprobar si un número es o no primo.
* Hecho esto, imprime los números primos entre 1 y 100. """


def is_prime_num():
    for num in range(1,101):
        if num >= 2:
            is_divisible = False
            for i in range(2,num):
                if num % i == 0:
                    is_divisible = True
            if not is_divisible:
                print(num)
is_prime_num()