with open("archivos\\texto_curso.txt","w",encoding="utf-8") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("Pero en 3v3 quedamos platino")
    archivo.writelines(["Se lego a champ\n", "Que quilombo"])
