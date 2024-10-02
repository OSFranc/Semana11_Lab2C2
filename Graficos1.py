import matplotlib.pyplot as plt
import pandas as pd

documento = "ArchivosCSV/pkmn.csv"
df_pkmn = pd.read_csv(documento)

numPkdex = int(input("Seleccione un número de la pokedex: "))

filaPkmn= df_pkmn[df_pkmn["ID"] == numPkdex]

nombrePkmn = filaPkmn['Name'].values[0]

estadisticasDex = df_pkmn[df_pkmn["ID"] == numPkdex]
estadisticasDex2 = estadisticasDex.iloc[0]
estadisticasDexGraf = estadisticasDex2[["HP","Attack","Defense","SpAtk","SpDef","Speed"]]
print(estadisticasDexGraf)

plt.figure(figsize=(8, 8))  # Ajustar el tamaño de la figura
plt.pie(estadisticasDexGraf, labels=estadisticasDexGraf.index, autopct=lambda p: f'{int(p * sum(estadisticasDexGraf) / 100)}')

    # Título del gráfico
plt.title(f"Estadísticas de {nombrePkmn}")
plt.axis('equal')  # Para asegurar que el gráfico sea circular
plt.show()