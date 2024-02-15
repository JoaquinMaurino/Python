import pandas as pd
#libreria de visualizacion de datos de forma grafica
import matplotlib.pyplot as plt 
#libreria de graficos estadisticos
import seaborn as sns


df = pd.read_csv("problemas_graficos\\datos_grafico_lineal.csv")

print(df)

#creando el grafico
sns.lineplot(x="fecha", y="estornudos", data=df)

#creando un punto en el pico del grafico
plt.plot("01-12", 21, "o")

#mostrando el grafico 
plt.show() 