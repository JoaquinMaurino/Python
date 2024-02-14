#Si el modulo se encuentra en la misma ruta:
""" import funciones_buenas.saludar
print(funciones_buenas.saludar.saludar("Joaquin")) """

#import funciones_buenas.saludar as saludo

#print(saludo.saludar("Joaquin"))

#-----------------------------------------------------
#Pero si se encuentra en otra carpeta afuera hay que usar el modulo de python sys:

import sys 

sys.path.append("C:\\Users\\Joaquitoxfit\\Desktop\\git-repositorio\\Python\\funciones")

import crear_funciones as modulo_importado

modulo_importado.Saludar_simple("Como estas bro")