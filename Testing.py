import matplotlib.pyplot as plt
import pandas as pd

documento = "ArchivosCSV/pkmn.csv"
df_pkmn = pd.read_csv(documento)
print(df_pkmn)