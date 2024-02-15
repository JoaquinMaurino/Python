#Cambiar el tipo de dato de una columna
import pandas as pd

df = pd.read_csv("resolviendo_problemas_archivos\\texto_csv.csv")

#convertir de numpy.int a str los datos de una columna

df['edad'] = df['edad'].astype(str)
#mostrar el tipo de dato del primer elemento de la columna edad
#print(type(df['edad'][0]))


#reemplazar un dato de la columna nombre por otro 

df['nombre'].replace("joaquin", "el zorro", inplace=True)
#print(df['nombre'])


#eliminando las filas con datos vacios
df = df.dropna()
#para eliminar columnas con datos faltantes:
#df = df.dropna(axis=1)


#eliminando filas repetidas

df = df.drop_duplicates()


#creando un csv con el df resultante (limpio)

df.to_csv("resolviendo_problemas_archivos\\df_limpio.csv")