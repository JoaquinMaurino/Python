import pandas as pd
#libreria de visualizacion de datos de forma grafica
import matplotlib.pyplot as plt 
#libreria de graficos estadisticos
import seaborn as sns


df = pd.read_csv("problemas_graficos\\datos_grafico_barras.csv")


#creando el grafico
sns.barplot(x="fuente", y="ingresos", data=df)

#obteniendo el total - el metodo sum() suma todos los valores de una columna
total_ingresos = df['ingresos'].sum()

#mostrando el total 
print(f"El total de ingresos es de: ${total_ingresos}")

#mostrando el grafico 
plt.show()