#creando una funcion simple:

def Saludar_simple(mensaje):
    print(mensaje)

Saludar_simple("Hola")

def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "rey"
    else:
        adjetivo = "crack"
    saludo = f"Hola {nombre}, como andas {adjetivo}?"
    return saludo

def create_random_password(num):
    chars = "abcdefghijkl"
    num_str = str(num)
    num_int = int(num_str[0])
    c1 = num_int - 1
    c2 = num_int - 2
    c3 = num_int - 3
    c4 = num_int - 4
    password = f"{chars[c1]}{num*5}{chars[c2]}{num*3}{chars[c3]}{num*1}{chars[c4]}{num*8}"
    return password.upper(),num_int

saludo = saludar("Joaquin", "Hombre")
password,num_utilizado = create_random_password(54)    
frase = f"{saludo} Tu contraseña es: {password} y el numero utilizado para crearla es: {num_utilizado}"
print(frase)


print(__name__)