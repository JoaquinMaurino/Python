archivo_sin_leer = open("archivos\\texto_curso.txt", encoding="UTF-8")

#Leer archivo completo
#archivo = archivo_sin_leer.read()

#leer linea por linea => retorna una lista con las lineas 
#lineas = archivo_sin_leer.readlines()

#leer una sola linea
linea = archivo_sin_leer.readline()

#cerrar archivo abierto 
archivo_sin_leer.close()