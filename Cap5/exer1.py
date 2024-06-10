import numpy as np
import pandas as pd

Paises = pd.read_csv(r"C:\Users\annac\Downloads\paises.csv", delimiter=';')
#print(dfPaises)


#QUAIS PAISES DA OCEANIA
dfOceania = Paises[Paises['Region'] == 'OCEANIA                            ']
print(dfOceania)

#QUANTOS PAISES DA OCEANIA
num_paises_oceania = dfOceania.shape[0]
print('Quantidade de paises localizados na Oceania:')
print(num_paises_oceania)

