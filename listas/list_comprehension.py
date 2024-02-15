original_list = [0,1,2,3,4,5,6,7]
print(original_list)

my_range = range(8)
print(list(my_range))

my_list = [i for i in range(8)]
print(my_list)

special_list = [i * i for i in range(8)]
print(special_list)

def sum_five(num):
    return num + 5 

special_list = [sum_five(i) for i in range(8)]
print(special_list)