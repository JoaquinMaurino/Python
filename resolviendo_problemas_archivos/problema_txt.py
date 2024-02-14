#teniendo dos listas con nombres y apellidos, hay que escribir los datos en un archivo de texto de manera optima con un for

nombres = ["joaquin", "lucas", "nahue", "mati"]
apellidos = ["mauriño", "carrasco", "fontana", "lorqui"]

with open("resolviendo_problemas_archivos\\nombres_y_apellidos.txt", "w") as archivo:
    archivo.writelines("Los nombres completos son:\n\n")
    [archivo.writelines(f"Nombre: {n}\nApellido: {a}\n----------\n") for n,a in zip(nombres,apellidos)]

#que es lo mismo que poner 
#for n,a in zip(nombres,apellidos):
#    archivo.writelines(f"Nombre: {n}\nApellido: {a}\n----------\n")

#leer archivo creado en el open anterior
with open("resolviendo_problemas_archivos\\nombres_y_apellidos.txt") as archivo:
    leer_archivo = archivo.read()
    print(leer_archivo)