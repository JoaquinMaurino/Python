# Chatbot analizador de sentimientos
# En este proyecto, podrías desarrollar un chatbot en python, que nos pida que le digamos algo y tome eso que le decimos, analice el sentimiento y nos responda cual es el sentimiento
# Este proyecto te daría la oportunidad de trabajar con varios aspectos de la Programación Orientada a Objetos (POO), módulos, API, análisis de datos, etc...

from textblob import TextBlob

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity >= -0.7 and analisis.sentiment.polarity <= -0.3:
            return "\x1b[1;31m" + f"Polaridad[{analisis.sentiment.polarity}]: Negativo"+ "\x1b[1;37m"
        elif analisis.sentiment.polarity > -0.3 and analisis.sentiment.polarity < -0.1:
            return "\x1b[1;31m" + f"Polaridad[{analisis.sentiment.polarity}]: Algo Negativo"+ "\x1b[1;37m"
        elif analisis.sentiment.polarity >= -0.1 and analisis.sentiment.polarity <=0.1:
            return "\x1b[1;33m" + f"Polaridad[{analisis.sentiment.polarity}]: Neutral"+ "\x1b[1;37m"
        elif analisis.sentiment.polarity > 0.1 and analisis.sentiment.polarity <= 0.3:
            return "\x1b[1;32m" + f"Polaridad[{analisis.sentiment.polarity}]: Algo positivo"+ "\x1b[1;37m"
        elif analisis.sentiment.polarity > 0.3 and analisis.sentiment.polarity <= 0.9:
            return "\x1b[1;32m" + f"Polaridad[{analisis.sentiment.polarity}]: Positivo"+ "\x1b[1;37m"
        elif analisis.sentiment.polarity > 0.9:
            return "\x1b[1;32m" + f"Polaridad[{analisis.sentiment.polarity}]: Muy Positivo"+ "\x1b[1;37m"
        else:
            return "\x1b[1;31m" + f"Polaridad[{analisis.sentiment.polarity}]: Muy Negativo" + "\x1b[1;37m"


analizador = AnalizadorDeSentimientos()

while True:
    user_prompt = input("\x1b[1;33m" + "\nTell me something: " + "\x1b[1;37m")
    resultado = analizador.analizar_sentimiento(user_prompt)
    print(resultado)