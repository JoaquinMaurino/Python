#import modulo_saludar #importo todo el modulo
#import modulo_saludar as mod_sal #importo todo el modulo y le asigno otro nombre
#from modulo_saludar import saludar #importo solo la funcion saludar del modulo, no el modulo completo
#from modulo_saludar import saludar,despedirse #importo mas de una funcion del modulo
from modulo_saludar import saludar as say_hi,despedirse as goodbye #importo mas de una funcion del modulo y les cambio el nombre
#from modulo_saludar import * #importo todo del modulo saludar

print(say_hi("Joaquin"),goodbye("Joaquin"))

