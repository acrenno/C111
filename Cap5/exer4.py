import numpy as np
import pandas as pd

Paises = pd.read_csv(r"C:\Users\annac\Downloads\paises.csv", delimiter=';')
#print(dfPaises)


#QUAIS PAISES DA OCEANIA
dfCM = Paises[Paises['Coastline (coast/area ratio)'] == 0]
print(dfCM)
dfCM.to_csv("C:/Users/annac/Downloads/paises_sem_coastline.csv", sep=';', header=False)



