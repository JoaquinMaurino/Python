import re

texto_simple = """Hola maestro, esta es la cadena 1. como estas mi capitan.
Esta es la  linea 2 de texto 456
Y esta es la final, 35, definitiva 1234."""

#Haciendo una busqueda simple
#retorna una lista con todas las coincidencias, el parametro ignora mayusculas 
#resultado = re.findall("esta", texto_simple, flags=re.IGNORECASE)

# \d -> busca digitos numericos del 0 al 9
#resultado = re.findall(r"\d", texto_simple)

# \D -> busca TODO MENOS digitos numericos del 0 al 9
#resultado = re.findall(r"\D", texto_simple)

# \w -> busca caracteres alfa numericos [a-z, A-Z, 0-9, _ ]
#resultado = re.findall(r"\w", texto_simple)

# \W -> busca TODO MENOS caracteres alfa numericos [a-z, A-Z, 0-9, _ ]
#resultado = re.findall(r"\W", texto_simple)

# \s -> busca espacios en blanco (espacios, tabs, saltos de linea)
#resultado = re.findall(r"\s", texto_simple)

# \S -> busca TODO MENOS espacios en blanco (espacios, tabs, saltos de linea)
#resultado = re.findall(r"\S", texto_simple)

#\n -> busca saltos de linea
#resultado = re.findall(r"\n", texto_simple)

# . -> busca TODO MENOS saltos de linea
#resultado = re.findall(r".", texto_simple)

# \ +[el caracter especial que querramos buscar]
#resultado = re.findall(r"\.", texto_simple)

#armando una cadena que busque un numero, seguido de un punto y un espacio "1. "
#resultado = re.findall(r"\d\.\s", texto_simple)


#Buscando el principio de una linea
# ^ busca el comienzo de una linea - flags=re.M activa la busqueda multilinea
#resultado = re.findall(r"^Hola", texto_simple, flags=re.M)

#Buscando el principio de una linea
# $ busca el final de una linea - flags=re.M activa la busqueda multilinea
#resultado = re.findall(r"texto$", texto_simple, flags=re.M)


#{n} busca n cantidad de veces el parametro que busquemos 
#resultado = re.findall(r"\d{3}", texto_simple)

#{n,m} busca al menos n y maximo m 
#resultado = re.findall(r"\d{2,4}", texto_simple)

# | busca lo que esta a la izquierda y lo que esta a la derecha, puede ser una o la otra o ambas
resultado = re.findall(r"\d{2,4}|Hola", texto_simple)




