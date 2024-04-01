import numpy as np

arr = np.loadtxt(R'C:\Users\annac\OneDrive\Área de Trabalho\INATEL\7 periodo\C111\C111\space.csv', delimiter=';', dtype='str', encoding='utf-8', skiprows=1)

#1
failureCount = np.char.find(arr[:,-1], 'Success').sum() * (-1)

totalCount = arr[:,-1].size

porcentagem = ((1-(failureCount/totalCount))*100)
print(round(porcentagem,2), "%")


#2
gastos = arr[:, -2].astype(float)

gastoTotal = gastos[gastos > 0].sum()

available = gastos[gastos > 0].size

media = gastoTotal / available
print(round(media,2))

#3
local= arr[:,2]

USAs = np.char.count(local, 'USA').sum()

print(USAs, ' missões')

#4

spacex = arr[arr[:,1] == 'SpaceX']

maisCara = spacex[spacex[:,-2].astype(float).argmax()]

print(maisCara)

#5

empresa, counts = np.unique(arr[:,1], return_counts=True)

print('Quantidade de missões:')
for i in range(empresa.size):
    print(empresa[i], ':', counts[i])