### Funciones Lambda ###

sum_two_values = lambda num1,num2: num1 + num2

print(sum_two_values(2,8))

multiply_values = lambda num1, num2: num1 * num2
print(multiply_values(2,8))


def sum_three_values(num):
    return lambda num1,num2: num1 + num2 + num

print(sum_three_values(1)(2,3))

