<<<<<<< HEAD
import numpy as np
import pandas as pd

Paises = pd.read_csv(r"C:\Users\annac\Downloads\paises.csv", delimiter=';')
#print(dfPaises)

#calculando media de alfabetizacao
media_alfabetizacao = Paises['Literacy (%)'].mean()
print("Media de alfabetização mundial")
=======
import numpy as np
import pandas as pd

Paises = pd.read_csv(r"C:\Users\annac\Downloads\paises.csv", delimiter=';')
#print(dfPaises)

#calculando media de alfabetizacao
media_alfabetizacao = Paises['Literacy (%)'].mean()
print("Media de alfabetização mundial")
>>>>>>> 68b168cc43a150e4377e27ac6f1671e0f78384fe
print(media_alfabetizacao)