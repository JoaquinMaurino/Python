import csv

with open("archivos\\texto_csv.csv", encoding="utf-8") as archivo:
    #print(archivo.read())
    reader = csv.reader(archivo)
    for row in reader:
        print(row)