import openai

openai.api_key = "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"

system_role = """Tu rol va a ser analizador de un texto y en base a ese texto vas a determinar el sentimiento con el que fue escrito, en terminos de positividad y negatividad de dicho sentimiento.
Yo te voy a pasar un texto y lo vas a analizar y ponerle un puntaje numerico, int o float, que va a ir desde el -1 hasta el 1, siendo -1 el valor de negatividad máxima, el 0 un valor neutro y el 1 el de máxima positividad. Solo podes responder con int o float, entre esa escala."""

mensajes = [{"role":"system", "content": system_role}]

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self,polaridad):
        if polaridad >= -0.7 and polaridad <= -0.3:
            return "\x1b[1;31m" + "Negativo"+ "\x1b[1;37m"
        elif polaridad > -0.3 and polaridad < -0.1:
            return "\x1b[1;31m" + "Algo Negativo"+ "\x1b[1;37m"
        elif polaridad >= -0.1 and polaridad <=0.1:
            return "\x1b[1;33m" + "Neutral"+ "\x1b[1;37m"
        elif polaridad > 0.1 and polaridad <= 0.3:
            return "\x1b[1;32m" + "Algo positivo"+ "\x1b[1;37m"
        elif polaridad > 0.3 and polaridad <= 0.9:
            return "\x1b[1;32m" + "Positivo"+ "\x1b[1;37m"
        elif polaridad > 0.9:
            return "\x1b[1;32m" + "Muy Positivo"+ "\x1b[1;37m"
        else:
            return "\x1b[1;31m" + "Muy Negativo" + "\x1b[1;37m"
        

analizador = AnalizadorDeSentimientos()

while True:
    user_prompt = input("\x1b[1;33m" + "\nDecime Algo: " + "\x1b[1;37m")
    mensajes.append({"role":"user", "content": user_prompt})
    
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = mensajes,
        max_tokens = 8
    )
    
    respuesta = completion.choices[0].message["content"]
    mensajes.append({"role":"assistant", "content": respuesta})
    
    sentimiento = analizador.analizar_sentimiento(respuesta)
    
    print(sentimiento)