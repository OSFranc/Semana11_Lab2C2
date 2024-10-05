#Importamos las librerías matplotlib para graficar y pandas para obtener nuestro dataframe
import pandas as pd
import matplotlib.pyplot as plt

archivoCSV = "ArchivosCSV/LenguajesPopulares.csv"

# Utilizamos panda para leer el archivo CSV
lecturaPd = pd.read_csv(archivoCSV)

print(lecturaPd)

# Renombramos las columnas para que sean más faciles de leer
lecturaPd.columns = [col.replace(' Worldwide(%)', '') for col in lecturaPd.columns]

# Seleccionamos la última fila del archivo df (último mes)
ultimo_mes = lecturaPd.iloc[-1]

# Excluimos la columna del mes al no ser valores numéricos
ultimo_mes_sin_mes = ultimo_mes.drop('Month')

# Graficamos con plot de tipo Barras
ultimo_mes_sin_mes.plot(kind="bar")

# Configuraciones del gráfico
plt.title('Lenguajes de Programación Más Utilizados - Último Mes')
plt.ylabel('Porcentaje de Uso (%)')
plt.xlabel('Lenguaje de Programación')
plt.xticks(rotation=45)
plt.show()

#En este gráfico de barras podemos comparar los lenguajes de programación de mayor uso en la actualidad 
#Este es de suma utilidad al momento del desarrollo de proyectos de aplicaciones o sistemas digitales 
#en relación a la compatibilidad, facilidad de uso y documentación. Así como para establecer la ruta 
#que llevará el proyecto