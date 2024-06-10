import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


dfSpace = pd.read_csv(r"C:\Users\annac\Downloads\space.csv", delimiter=';')


dfEua = dfSpace[dfSpace['Location'].str.contains('EUA', case=False, na=False)]
dfChina = dfSpace[dfSpace['Location'].str.contains('China', case=False, na=False)]

empresa_count = {
    'EUA': len(dfEua),
    'China': len(dfChina)
}

# Criando o gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(empresa_count.keys(), empresa_count.values(), color=['blue', 'red'])
plt.xlabel('País')
plt.ylabel('Número de Empresas')
plt.xticks(rotation=0)  # Mantém os rótulos dos países horizontais
plt.show()


