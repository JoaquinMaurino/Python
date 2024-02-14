import pandas as pd
#df = data frame (datos bidimensionales - similar a una hoja de calculo)
df = pd.read_csv("archivos\\texto_csv.csv")
df2 = pd.read_csv("archivos\\texto_csv.csv")

#obteniendo todos los datos
print(df)
#obteniendo los datos de la columna nombre
#nombres = df["nombre"]
#edades = df["edad"]

#----------- Slicing
cadena = "0123456789"
#print(cadena[:-1])
#------------------
 
#ordenando el dataframe por la edad
df_ordenado_as = df.sort_values("edad")
#print(df_ordenado_as)

#ordenandolo de forma descendenter
df_ordenado_des = df.sort_values("edad", ascending=False)
#print(df_ordenado_des)

#concatenando dos data frames
df_concatenado = pd.concat([df_ordenado_as, df_ordenado_des])
#print(df_concatenado)


#accediendo a las primeras 3 filas con head()
primer_fila = df.head(3)
#print(primer_fila)


#accediendo a las ultimas 2 filas con taiL()
ultima_fila = df.tail(2)
#print(ultima_fila)



#accediendo a la canitdad de filas y columnas 
filas_columnas_totales = df.shape
#print(filas_columnas_totales)
#esto retorna una tupla con dos valores (filas, columnas) (5,3)
#filas_totales = filas_columnas_totales[0]
#olumnas_totales = filas_columnas_totales[1]

#se puede lograr lo mismo pero desempaquetando desde un principio:
filas_totales, columnas_totales = df.shape
#print(filas_totales)
#print(columnas_totales)

#accediendo a un elemento especifico del df con loc (edad fila 2)
elemento_especifico_loc = df.loc[2, "edad"]

#accediendo a un elemento especifico del df con iloc (edad fila 2)
elemento_especifico_iloc = df.iloc[2, 2]


#accediendo a todas las filas de una columna loc
apellidos_loc = df.loc[:,"apellido"]

#accediendo a todas las filas de una columna  iloc
apellidos_iloc = df.iloc[:,1]


#accediendo a la fila 3 (con loc e iloc es igual porque las filas van por indice, no por nombre como las columnas)
fila_3 = df.loc[2,:]


#accediendo a filas con edad mayor a 30
mayor_30 = df.loc[df["edad"]>30,:]


