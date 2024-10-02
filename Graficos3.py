import pandas as pd
import matplotlib.pyplot as plt

documento = "ArchivosCSV/alturasypeso.csv"
infoDf = pd.read_csv(documento)
print(infoDf)

infoDfMasculino=infoDf[infoDf["gender"]==1]

infoDfMasculino2=infoDfMasculino.groupby("yr")["height"].mean()

infoDfMasculino.plot(x="yr", y="height", kind="line", figsize=(10, 6))

plt.title('Crecimiento Promedio en Varones')
plt.xlabel('Edad')
plt.ylabel('Altura (cm)')
plt.xticks(rotation=45)
plt.show()
