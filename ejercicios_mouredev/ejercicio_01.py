"""
                    FIZZ BUZZ
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""


def fizzbuzz():
    for num in range(1,101):
        multip_3 = num % 3 == 0
        multip_5 = num % 5 == 0 
        if(multip_3 and multip_5):
            print("fizzbuzz")
        elif(multip_3):
            print("fizz")
        elif(multip_5):
            print("buzz")
        else:
            print(num)
            
fizzbuzz()

#FIZZBUZZ OPTIMIZADA
def fizzbuzz():
    for num in range(1, 101):
        output = ""
        if num % 3 == 0:
            output += "fizz"
        if num % 5 == 0:
            output += "buzz"
        if not output:
            output = num
        print(output)

fizzbuzz()


#FIZZBUZZ CON BUCLE WHILE

def fizzbuzz2():
    condition = 1
    while condition <= 100:
        if condition % 3 == 0 and condition % 5 == 0:
            print("fizzbuzz")
        elif condition % 3 == 0:
            print("fizz")
        elif condition % 5 == 0:
            print("buzz")
        else:
            print(condition)
        condition += 1

fizzbuzz2()
