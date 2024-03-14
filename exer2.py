import numpy as np

#1
#funcao arange, array em uma faixa de numeros
arr = np.arange(0, 21, 1) #inicio, fim, passo
print(arr)

#2

array1 = np.arange(0, 51, 2)
array2 = np.arange(100, 50, -2)
arrayf = np.concatenate((array1, array2))
array_ordenado = np.sort(arrayf)
print(array_ordenado)

#3
arraydecre = np.flip(np.sort(arrayf))
print(arraydecre)

#4
mtz = np.ones([3, 4])
arrafi = mtz.ravel()

#5
mt2 = np.ones([3,4])
nl, nc = mt2.shape
prod = nl * nc

if prod % 2 == 0:
    print("Numero par de elementos.")
else:
    print("Numero impar de elementos.")
