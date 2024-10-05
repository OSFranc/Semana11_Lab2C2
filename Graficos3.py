#Importamos las librerías matplotlib para graficar y pandas para obtener nuestro dataframe
import pandas as pd
import matplotlib.pyplot as plt

#Creamos una variable que señale la ruta donde tenemos nuestro archivo csv
documento = "ArchivosCSV/alturasypeso.csv"

#Pasamos esa variable al método read csv para poder definir nuestro dataframe
infoDf = pd.read_csv(documento)
print(infoDf)

#Colocamos un filtro para solamente obtener los resultados masculinos del gráfico
infoDfMasculino=infoDf[infoDf["gender"]==1]

#Agrupamos las edades con las alturas y con el método .mean obtenemos el promedio de este resultado
infoDfMasculino2=infoDfMasculino.groupby("yr")["height"].mean()

#Creamos el gráfico de líneas con los valores de edades y altura.
infoDfMasculino.plot(x="yr", y="height", kind="line", figsize=(10, 6))

# Configuraciones del gráfico
plt.title('Crecimiento Promedio en Varones')
plt.xlabel('Edad')
plt.ylabel('Altura (cm)')
plt.xticks(rotation=45) #Colocamos una rotación en las etiquetas del eje x para mejorar su lectura.
plt.show()

#En el gráfico mostrado podemos observar la evolución de la altura con relación a la edad siendo directamente proporcional
#Hasta llegar a la vejez donde se ve una disminución de esta tendencia comenzando a disminuir la altura a medida se envejece 
#Este gráfico puede ser de utilidad en la medicina para comparar la tabla de crecimiento normal o promedio de un individuo 
#en relación a la altura de un paciente. 