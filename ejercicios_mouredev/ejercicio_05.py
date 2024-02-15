"""  
        INVIRTIENDO CADENAS
* Crea un programa que invierta el orden de una cadena de texto
* sin usar funciones propias del lenguaje que lo hagan de forma automática.
* - Si le pasamos "Hola mundo" nos retornaría "odnum aloH" """

def revert(text):
    reverted_text = ""
    for i in range(len(text)):
        reverted_text += text[-i-1]
    return reverted_text

print(revert("Hola mundo"))