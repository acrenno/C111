import numpy as np

#importanto arquivo excel
arr = np.loadtxt(R'C:\Users\annac\OneDrive\Área de Trabalho\INATEL\7 periodo\C111\C111\exerprova1\paises.csv', delimiter=';', dtype='str', encoding='utf-8', skiprows=1)

#1
#fazendo slicing do arquivo
arraysli=(arr[1:, :4]) 
print(arraysli)
print("----------------------------------------------------------")

#2
slicing_countries = arr[1:, 1]
regioes = np.unique(slicing_countries)
print("Quantidade de regioes no mundo")
print ({len(regioes)})
print(regioes)
print('------------------')

#3
alfabetizacao = arr[1:,9].astype(np.float64)
print("Media de alfabetizacao: ")
print({np.mean(alfabetizacao)})
print('----------------------')

#4
NA = np.char.find(slicing_countries, 'NORTHERN AMERICA') >= 0
countries_column = arr[1:,0]
num_countries_NA = len(countries_column[NA])
print("Numero de paises NORTHERN AMERICA")
print( {num_countries_NA})

#5
region_LA_and_Caribbean_filter = np.char.find(slicing_countries, 'LATIN AMER. & CARIB') >= 0

gdp_column = arr[1:,8].astype(np.float64)
gdp_countries_LA_and_Caribbean = gdp_column[region_LA_and_Caribbean_filter]

max_gdp_LA_and_Caribbean = np.max(np.array(gdp_countries_LA_and_Caribbean))
pos_max_gdp_LA_and_Caribbean = gdp_countries_LA_and_Caribbean == max_gdp_LA_and_Caribbean

countries_LA_and_Caribbean = countries_column[region_LA_and_Caribbean_filter]

print(f'Paises com a maior renda per capita: {countries_LA_and_Caribbean[pos_max_gdp_LA_and_Caribbean][0]}')