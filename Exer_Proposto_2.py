import numpy as np

#1
np.random.seed(5)

array = np.random.uniform(-1, 1, 10)

arrayf = array * 100

array_int = np.floor(arrayf)

print(array)
print(array_int)


#2

np.random.seed(10)

mat= np.random.randint(1, 51, size=(4, 4))

print(mat)

#3
medias_linhas = np.mean(mat, axis=1)
medias_colunas = np.mean(mat, axis=0)
print(np.max(medias_linhas))
print(np.max(medias_colunas))

#4

#pesquisei e achei essas funçoes, mas nunca vi na vida, nem nos slides

contagem = np.bincount(mat.flatten())
numeros_duas_vezes = np.where(contagem == 2)[0]



