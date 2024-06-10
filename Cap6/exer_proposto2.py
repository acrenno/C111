import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('paises.csv', delimiter=';')
df['Region'] = df['Region'].str.strip()

# Paises da America do norte
northern_america_data = df[df['Region'] == 'NORTHERN AMERICA']

# colunas para birthrate e deathrate
countries = northern_america_data['Country']
birthrates = northern_america_data['Birthrate']
deathrates = northern_america_data['Deathrate']

plt.figure(figsize=(10, 6))

# Birthrate
plt.plot(countries, birthrates, label='Birthrate', marker='o')

# Deathrate
plt.plot(countries, deathrates, label='Deathrate', marker='o')

# gráfico
plt.title('Birthrate e Deathratena America do Norte')
plt.xlabel('Country')
plt.ylabel('Rate')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
