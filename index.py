import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

def extraer_valores_columna(dataframe, nombre_columna):
    valores = dataframe[nombre_columna].tolist()
    return valores

def calcular_edades(lista_fechas):
    lista_fechas = pd.to_datetime(lista_fechas, format='%d/%m/%Y')
    # Convertir la fecha actual a un objeto datetime
    fecha_actual = datetime(2024, 5, 1)
   # Calcular la diferencia entre cada fecha en la lista y la fecha actual en días
    diferencias_en_dias = [(fecha_actual - fecha).days for fecha in lista_fechas]
    
    # Convertir la diferencia en días a una estimación de la edad en años
    edades_en_anios = [round(diferencia / 365) for diferencia in diferencias_en_dias]
    
    return edades_en_anios

def contar_valores(lista):
    diccionario_contadores = {}
    lista.sort()
    for valor in lista:
        if valor in diccionario_contadores:
            diccionario_contadores[valor] += 1
        else:
            diccionario_contadores[valor] = 1
    return diccionario_contadores

def crear_df(diccionario):
    data_frame = pd.DataFrame()
    data_frame["Edades"] = diccionario.keys()
    data_frame["Cant. Personas"] = diccionario.values()
    return data_frame

# Leer el archivo CSV
df = pd.read_csv("edades.csv")

#Extraer las fechas de la columna age a una lista
lista_con_fechas = extraer_valores_columna(df,'age')

#Comparar las fechas con la fecha actual y obtener una lista de edades
edades = calcular_edades(lista_con_fechas)

#Agregamos una columna al dataframe con las edades
df['edad_valor'] = edades

#Creamos un dataframe solo con las personas mayores a 25
personas_mayores = df[df['edad_valor'] > 25]
#Ordenamos las filas por edad de menor a mayor
df_ordenado = personas_mayores.sort_values(by='edad_valor')
#Imprimimos lo pedido por la consigna
print(df_ordenado)


#Extraemos las edade en una lista
lista_valores = df_ordenado['edad_valor'].tolist()
#Creamos un diccionario de contadores de edades
dicci = contar_valores(lista_valores)
#Utilizamos diccionario para responder las consignas
print(f"La cantidad de Edades existntes es de: {len(dicci)}")
for clave, valor in dicci.items():
    print(f"La edad {clave} se repite {valor} veces")

#Creamos un dataframe en base al diccionario anterior
df_comprimido = crear_df(dicci)
print(df_comprimido)


#poligono de frecuencias
fig, ax = plt.subplots()
ax.plot(df_comprimido["Edades"], df_comprimido["Cant. Personas"])
plt.title("Cantidad de personas por edad")
plt.xlabel('Edad') # definir el nombre del eje X
plt.ylabel('Cantidad de Personas') # definir el nombre del eje Y
plt.show()
