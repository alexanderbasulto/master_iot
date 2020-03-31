import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters


def calculo_est_30(df_clean):
    estaciones_30 = df_clean['Total'] == 30
    total_esta = len (df_clean[estaciones_30])
    print ('El numero de estaciones con un total de 30 son:', total_esta)

def media_mas_alta(df_clean):
    estacion_grupo = df_clean.groupby('Estacion').aggregate({'Disponible': ['mean', 'count']})
    solo_media = estacion_grupo.iloc[:, 0]
    media = solo_media.sort_values(0, ascending=False)    #La estacion con la media mas alta de bicis Disponible es la #50
    media_alta = media.iloc[0:1]
    print('La media mas altas es la',media_alta)
    return()

def histograma(df_clean):
    filtro_50 = df_clean['Estacion'] == 50  # Filtramos la estacion 50 y guardamos el dataframe en una variable
    estacion_50 = df[filtro_50]
    plt.hist(estacion_50['Disponible'])
    plt.ylabel('Frecuencia')
    plt.xlabel('Free bikes')
    return(estacion_50)

def linea_temporal(data_50):
    gl_50 = data_50.sort_values('Actualizado', ascending=True)  # Ordenar la serie temporal
    time = gl_50['Actualizado']
    data = gl_50['Libre']
    df_lineal = pd.DataFrame([time, data])
    df_T = df_lineal.T
    df_T.columns = ["Time", "Data"]
    df_T = df_T.sort_values('Time', ascending=True)
    plt.plot(df_T['Time'], df_T['Data'])
    plt.xticks(rotation='vertical')
    return()

if __name__ == "__main__":
    df = pd.read_csv('./estaciones_bici.csv', delimiter=';', encoding="utf-8")    #Archivo cargado en df
    df = df.rename(
        columns={"_id": "ID", "available": "Disponible", "connected": "Conectado", "download_date": "Fecha Descarga",
                 "estation": "Estacion", "free": "Libre", "open": "Abierto", "ticket": "Tiquete", "total": "Total",
                 "updated": "Actualizado"})
    calculo_est_30(df)
    media_mas_alta(df)
    datos_50 = histograma(df)
    linea_temporal(datos_50)