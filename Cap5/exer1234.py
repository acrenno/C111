import numpy as np
import pandas as pd

Paises = pd.read_csv(r"C:\Users\annac\Downloads\paises.csv", delimiter=';')
#print(dfPaises)

#--------------------------EXER1----------------------------

#QUAIS PAISES DA OCEANIA
dfOceania = Paises[Paises['Region'] == 'OCEANIA                            ']
print(dfOceania)

#QUANTOS PAISES DA OCEANIA
num_paises_oceania = dfOceania.shape[0]
print('Quantidade de paises localizados na Oceania:')
print(num_paises_oceania)


#------------------------------EXER2---------------------------------------

#calculando media de alfabetizacao
media_alfabetizacao = Paises['Literacy (%)'].mean()
print("Media de alfabetização mundial")
print(media_alfabetizacao)

#--------------------------------EXER3----------------------------------------

#pais com maior populacao
popumax = Paises['Population'].idxmax()

# saindo com nome e regiao
print(Paises.loc[popumax, 'Country'])
print(Paises.loc[popumax, 'Region'])

#------------------------------------------EXER4---------------------------

#QUAIS SEM COASTLINE
dfCM = Paises[Paises['Coastline (coast/area ratio)'] == 0]
print(dfCM)
dfCM.to_csv("C:/Users/annac/Downloads/paises_sem_coastline.csv", sep=';', header=False)


