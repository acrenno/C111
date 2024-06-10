import pandas as pd
import matplotlib.pyplot as plt


dfPaises = pd.read_csv(r"C:\Users\annac\Downloads\paises.csv", delimiter=';')

dfNorte = dfPaises[dfPaises['Region'].str.contains('North America', case=False, na=False)]

dfpaises = dfNorte['Country']
dfmortalidade = dfNorte['Deathrate']
dfnascimento = dfNorte['Birthrate']


fig, ax1 = plt.subplots(figsize=(12, 8))

ax1.set_xlabel('País')
ax1.set_ylabel('Taxa de Mortalidade', color='tab:red')
ax1.bar(dfpaises, dfmortalidade, color='tab:red', alpha=0.6, label='Taxa de Mortalidade')
ax1.tick_params(axis='y', labelcolor='tab:red')


ax2 = ax1.twinx()
ax2.set_ylabel('Taxa de Natalidade', color='tab:blue')
ax2.plot(dfpaises, dfnascimento, color='tab:blue', marker='o', linestyle='-', linewidth=2, markersize=5, label='Taxa de Natalidade')
ax2.tick_params(axis='y', labelcolor='tab:blue')


fig.tight_layout()
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()
