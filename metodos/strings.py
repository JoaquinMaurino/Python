cadena1 = "Hola soy Joaquin"
cadena2 = "123"

#La funcion dir() nos muestra todos los metodos que se le pueden aplicar a ese tipo de dato
#metodos_posibles = dir(cadena1)
#print(metodos_posibles)


#Los metodos se ejecutan => cadena1.upper()
mayuscula = cadena1.upper()
minuscula = cadena1.lower()
primera_mayuscula = cadena1.capitalize()

#busca una cadena en otra cadena, retornan su Indice
busqueda_find = cadena1.find("J") #Si no existe retorna -1
busqueda_index = cadena1.index("J") #Si no existe retorna error/excepcion

#busca una cadena en otra cadena, retornan su la cantidad de veces que aparece
count = cadena1.count("f")

# .isnumeric() / .isalphanum()  => True / False
#Si es un string que solo contiene numeros isnumeric => true

#longitud de la cadena // len() es una funcion, no un metodo 
longitud = len(cadena1)

#reemplaza un valor en una cadena por otro valor dado
cadena_nueva = cadena1.replace("soy", "me llamo")

#separa la cadena existente y devuelve una lista de cadenas separadas
cadena3 = "Hola,me,llamo,Joaquin"
cadena_separada = cadena3.split(",") # => ['Hola', 'me', 'llamo', 'Joaquin']
