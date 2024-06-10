import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('space.csv', delimiter=';')

# Dados para EUA e China
usa = df[df['Location'].str.contains('USA', case=False)]['Company Name'].unique()
china = df[df['Location'].str.contains('China', case=False)]['Company Name'].unique()

# Contar o número de empresas
usa_count = len(usa)
china_count = len(china)

# Dados para a  cosntrução do gráfico
countries = ['USA', 'China']
counts = [usa_count, china_count]

#Montando o grafico
plt.figure(figsize=(10, 6))
plt.bar(countries, counts, color=['red', 'blue'])
plt.xlabel('País')
plt.ylabel('Número de Empresas Espaciais')
plt.title('Empresas Espaciais nos EUA e China')
plt.show()
