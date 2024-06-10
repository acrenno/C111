import numpy as np
import pandas as pd

Paises = pd.read_csv(r"C:\Users\annac\Downloads\paises.csv", delimiter=';')
#print(dfPaises)

#calculando media de alfabetizacao
media_alfabetizacao = Paises['Literacy (%)'].mean()
print("Media de alfabetização mundial")
print(media_alfabetizacao)