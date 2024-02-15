import pandas as pd
#libreria de visualizacion de datos de forma grafica
import matplotlib.pyplot as plt 
#libreria de graficos estadisticos
import seaborn as sns


df = pd.read_csv("problemas_graficos\\datos_grafico_dispersion.csv")


#creando el grafico
sns.scatterplot(x="tiempo", y="dinero", data=df)


#mostrando el grafico 
plt.show()