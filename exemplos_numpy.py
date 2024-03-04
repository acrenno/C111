import numpy as np

'''
# NumPy Array
# 1-D

arr = np.array([1, 2, 3, 4])
print(arr)
print(type(arr))

#2-D
mtz = np.array([[1, 2],[3, 4]])
print(mtz)

#estruturando numpyarrays/matrizes
#criando uma matriz 5x5, funcao ones
mtz = np.ones([5, 5])
print(mtz)

#criando um vetor formado apenas por zeros, usando funcao zeros
arr = np.zeros(10)
print(arr)

#funcao arange, array em uma faixa de numeros
arr = np.arange(20, 30, 1) #inicio, fim, passo
print(arr)

#transformando o array em uma matriz
arr = np.arange(20, 30, 1).reshape(5,2)
print(arr)

'''


#OPERAÇOES ENTRE NUMPY ARRAYS
jan = np.arange(20, 30, 1)
fev = np.arange(40, 50, 1)

print(jan)
print(fev)
#fazendo soma de cade membro dos arrays
print(jan+fev)
#juntando os dois vetores
print(np.concatenate([jan, fev]).reshape(5, 4))


#TIRANDO INFORMAÇOES DE UM ARRAY
#Tamanho de um nparray
print(jan.size)
#tamanho dimensoes
print(jan.ndim)
#achar o shape
print(jan.shape)


