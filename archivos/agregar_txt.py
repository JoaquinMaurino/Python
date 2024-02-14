#con el "a" => append se va a agregar el texto y no sobreescribirlo
with open("archivos\\texto_curso.txt","a",encoding="utf-8") as archivo:

    for i in range(5):
        archivo.write(f"\nLinea {i+1} agregada")