#Importamos las librerías matplotlib para graficar y pandas para obtener nuestro dataframe
import matplotlib.pyplot as plt
import pandas as pd

#Creamos una variable que señale la ruta donde tenemos nuestro archivo csv
documento = "ArchivosCSV/pkmn.csv"
#Pasamos esa variable al método read csv para poder definir nuestro dataframe
df_pkmn = pd.read_csv(documento)

#Solocitamos al usuario mediante consola ingresar un un número de la pokedex 
numPkdex = int(input("Seleccione un número de la pokedex: "))

#Colocamos un filtro en el dataframe correspondiente al número de la pokedex obtenido
estadisticasDex = df_pkmn[df_pkmn["ID"] == numPkdex]

#Obtenemos el nombre del pokemon y la guardamos en una variable para luego colocarla en el título del gráfico
nombrePkmn = estadisticasDex['Name'].values[0]

#Nos aseguramos que estamos en la fila correspondiente al ID del Pokemon
estadisticasDex2 = estadisticasDex.iloc[0]

#Seleccionamos las columas que queremos graficar
estadisticasDexGraf = estadisticasDex2[["HP","Attack","Defense","SpAtk","SpDef","Speed"]]
print(estadisticasDexGraf)

#Creamos el gráfico circular o de pastel con los filtros y parámetros que hemos establecido.
plt.pie(estadisticasDexGraf, labels=estadisticasDexGraf.index, autopct=lambda p: f'{int(p * sum(estadisticasDexGraf) / 100)}')

# Título del gráfico
plt.title(f"Estadísticas de {nombrePkmn}")
plt.show()

#En este gráfico de barras se obtienen todas las estadísticas relevantes de un pokemon según sus datos
#oficiales en la pokedex, podemos observar sus destrezas en relación a sus estadísticas y puntos mas débiles
#del pokemon de manera clara.