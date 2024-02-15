### Higher Order Functions ###  Funcion que recibe otra funcion como parametro

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_plus_one(first_value, second_value):
    return sum_one(first_value + second_value)

print(sum_two_values_plus_one(5,2))


def sum_two_values_and_add_valdue(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_valdue(5,2, sum_one))
print(sum_two_values_and_add_valdue(5,2, sum_five))

#----------------------------------------------------------
### Closures ###  Funcion que define otra funcion y la retorna

def sum_ten():
    def add(value):
        return value + 10
    return add

#Se puede ejecutar asi:
print(sum_ten()(5))

#O inicializar sum_ten en una variable, y luego esa variable recibe el parametro para add
add_closure = sum_ten()
print(add_closure(10))

#-----------------------------------
### Build-in Higher Order Functions ###

