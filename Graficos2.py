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