<<<<<<< HEAD
import numpy as np
import pandas as pd

Paises = pd.read_csv(r"C:\Users\annac\Downloads\paises.csv", delimiter=';')
#print(dfPaises)

#pais com maior populacao
popumax = Paises['Population'].idxmax()

# saindo com nome e regiao
print(Paises.loc[popumax, 'Country'])
=======
import numpy as np
import pandas as pd

Paises = pd.read_csv(r"C:\Users\annac\Downloads\paises.csv", delimiter=';')
#print(dfPaises)

#pais com maior populacao
popumax = Paises['Population'].idxmax()

# saindo com nome e regiao
print(Paises.loc[popumax, 'Country'])
>>>>>>> 68b168cc43a150e4377e27ac6f1671e0f78384fe
print(Paises.loc[popumax, 'Region'])